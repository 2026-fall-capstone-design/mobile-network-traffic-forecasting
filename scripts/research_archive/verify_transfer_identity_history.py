"""13/14 저장예측·소속·지표 검산. 원 모델/코드/새 난수 실행 없음."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

import numpy as np


def verify(source: Path) -> dict:
    """Verify stored transfer and ID diagnostics; retain reported-only limitations."""
    manifest = json.loads(source.read_text(encoding="utf-8-sig"))
    CATALOG = {r["source_id"]: r for r in manifest["sources"]}
    checks = []
    accessed = {}

    def exact(name, actual, expected):
        """Compare identities, counts or exact saved arrays."""
        ok = (
            bool(np.array_equal(actual, expected))
            if isinstance(actual, np.ndarray) or isinstance(expected, np.ndarray)
            else actual == expected
        )
        checks.append(dict(check=name, passed=bool(ok)))
        assert ok, (name, actual, expected)

    def numeric(name, actual, expected):
        """Compare matching shapes using tolerances for stored float32 results."""
        a, b = np.asarray(actual), np.asarray(expected)
        ok = a.shape == b.shape and bool(np.allclose(a, b, rtol=1e-7, atol=1e-9))
        checks.append(dict(check=name, passed=ok))
        assert ok, (name, actual, expected)

    def access(sid, scope):
        """Check archived byte identity and record only the accessed scope."""
        row = CATALOG[sid]
        p = source.parent / row["archive_path"]
        if sid not in accessed:
            raw = p.read_bytes()
            exact(sid + ":sha256", hashlib.sha256(raw).hexdigest(), row["sha256"])
            exact(sid + ":size", len(raw), row["size_bytes"])
            accessed[sid] = {k: row[k] for k in ["source_id", "path", "sha256", "size_bytes"]}
            accessed[sid]["read_scope"] = []
        accessed[sid]["read_scope"] = sorted(set(accessed[sid]["read_scope"]) | set(scope))
        return p

    def saved_json(sid):
        """Read all saved JSON keys without executing its historical instructions."""
        return json.loads(access(sid, ["JSON:all_keys"]).read_text(encoding="utf-8-sig"))

    def arrays(sid, keys=None):
        """Read specified numeric arrays with pickle disabled."""
        with np.load(
            access(sid, ["NPZ:all_numeric_arrays" if keys is None else "NPZ:" + ",".join(keys)]),
            allow_pickle=False,
        ) as z:
            if keys is None:
                keys = z.files
            values = {key: z[key] for key in keys}
        for key, a in values.items():
            exact(
                sid + ":finite_numeric:" + key,
                a.dtype.kind in "bifu" and bool(np.isfinite(a).all()),
                True,
            )
        return values

    def average_ranks(a):
        """Use average ranks for ties, without importing the original scipy call."""
        order = np.argsort(a, kind="stable")
        result = np.empty(len(a), dtype=float)
        start = 0
        while start < len(a):
            end = start + 1
            while end < len(a) and a[order[end]] == a[order[start]]:
                end += 1
            result[order[start:end]] = (start + 1 + end) / 2
            start = end
        return result

    expected_new = {
        "SRC-0020929",
        "SRC-0020950",
        "SRC-0020972",
        "SRC-0023210",
        "SRC-0022570",
        "SRC-0023614",
        "SRC-0023615",
        "SRC-0024836",
        "SRC-0024837",
        "SRC-0024838",
        "SRC-0024839",
        "SRC-0024840",
        "SRC-0024841",
    }
    exact(
        "manifest:new_preserved_source_ids",
        tuple(
            sorted(
                r["source_id"]
                for r in manifest["sources"]
                if r.get("preservation") == "new_byte_identical_archive"
            )
        ),
        tuple(sorted(expected_new)),
    )
    exact(
        "manifest:all_source_ids",
        tuple(sorted(r["source_id"] for r in manifest["sources"])),
        tuple(sorted(expected_new | {"SRC-0023577", "SRC-0023605", "SRC-0023612"})),
    )

    for sid in ["SRC-0020929", "SRC-0020950", "SRC-0020972", "SRC-0023210", "SRC-0022570"]:
        access(sid, ["hash_only_in_arithmetic; full_text_read_separately"])
    t = saved_json("SRC-0023614")
    v = arrays("SRC-0023615")
    s = saved_json("SRC-0024841")
    started = saved_json("SRC-0024840")
    finished = saved_json("SRC-0024839")
    calls = saved_json("SRC-0024836")
    identity = arrays("SRC-0024837")
    partial = arrays("SRC-0024838")
    d = arrays("SRC-0023577", ["X", "Y", "raw", "scales", "times", "cell_indices"])
    p = arrays(
        "SRC-0023605", ["median", "cell_ids", "query_times", "context_times", "selected_cells"]
    )
    u = arrays("SRC-0023612")
    ids = p["cell_ids"]
    n = len(ids)
    q = p["query_times"]
    sel = p["selected_cells"]
    exact("pilot:cells", n, 16)
    exact("pilot:unique_cells", len(set(ids)), 16)
    exact("pilot:source_ids", d["cell_indices"][sel] + 1, ids)
    exact("pilot:query_count", len(q), 64)
    exact("pilot:query_unique", len(set(q)), 64)
    exact("pilot:query_bounds", bool(np.all((q >= 672) & (q < 840))), True)
    exact("pilot:source_context", p["context_times"], np.arange(168, 672))
    exact("input:shapeX", d["X"].shape, (32, 840, 16))
    exact("input:shapeY", d["Y"].shape, (32, 840))
    exact("input:times", d["times"], np.arange(168, 1008))
    numeric("input:scale_from_first672", d["raw"][:672].mean(0), d["scales"])
    numeric("input:Y_from_scaled_raw", (d["raw"][168:] / d["scales"]).T.astype(np.float32), d["Y"])
    qi = np.searchsorted(d["times"], q)
    exact("query:time_mapping", d["times"][qi], q)
    Y = d["Y"][sel][:, qi]
    exact("transfer:plan_hash", t["plan_sha256"], CATALOG["SRC-0020929"]["sha256"])
    exact("transfer:prediction_hash", t["prediction_sha256"], CATALOG["SRC-0023605"]["sha256"])
    exact("transfer:IDs", t["cell_ids"], ids.tolist())
    exact("transfer:query_times", t["query_times"], q.tolist())
    exact(
        "transfer:array_keys",
        set(v),
        {
            "cell_ids",
            "cross_MAE",
            "cross_excess",
            "symmetric_excess",
            "raw_PCC",
            "profile_PCC",
            "input_support",
        },
    )
    exact("transfer:saved_IDs", v["cell_ids"], ids)
    exact("transfer:prediction_shape", p["median"].shape, (16, 1088))
    cross_pred = p["median"][:, 64:].reshape(n, n, len(q))
    mae = np.abs(cross_pred - Y[None, :, :]).mean(2).T
    numeric("transfer:cross_MAE_from_predictions", mae, v["cross_MAE"])
    excess = mae - np.diag(mae)[:, None]
    symmetric = (excess + excess.T) / 2
    numeric("transfer:cross_excess", excess, v["cross_excess"])
    numeric("transfer:symmetric_excess", symmetric, v["symmetric_excess"])
    numeric("transfer:self_mean", np.diag(mae).mean(), t["own_context_mean_MAE"])
    other = ~np.eye(n, dtype=bool)
    numeric("transfer:other_mean", mae[other].mean(), t["other_context_mean_MAE"])
    upper = np.triu_indices(n, 1)
    values = symmetric[upper]
    numeric(
        "transfer:excess_quantiles",
        np.quantile(values, [0, 0.25, 0.5, 0.75, 1]),
        t["symmetric_cross_excess_quantiles"],
    )
    raw = d["raw"][:672, sel]
    weekday = np.array(
        [(datetime(2013, 11, 1) + timedelta(days=i)).weekday() < 5 for i in range(28)]
    )
    numeric("transfer:raw_PCC_from_saved_raw", np.corrcoef(raw.T), v["raw_PCC"])
    numeric(
        "transfer:profile_PCC_from_saved_raw",
        np.corrcoef(raw.reshape(28, 24, n)[weekday].mean(0).T),
        v["profile_PCC"],
    )
    support = v["input_support"]
    exact("transfer:support_shape", support.shape, (16, 16))
    exact("transfer:support_fraction_bounds", bool(np.all((support >= 0) & (support <= 1))), True)
    exact("transfer:support_denominator64", support * 64, np.round(support * 64))
    numeric(
        "transfer:support_quantiles",
        np.quantile(support[other], [0, 0.25, 0.5, 0.75, 1]),
        t["input_support_fraction_quantiles"],
    )
    numeric("transfer:own_support", np.diag(support), t["own_input_support_fraction"])
    associations = {}
    for name, a in [
        ("raw_PCC_dissimilarity", 1 - v["raw_PCC"]),
        ("weekday_profile_PCC_dissimilarity", 1 - v["profile_PCC"]),
        ("input_distance_exceedance_fraction", 1 - (support + support.T) / 2),
    ]:
        rho = float(np.corrcoef(average_ranks(a[upper]), average_ranks(values))[0, 1])
        numeric("transfer:spearman:" + name, rho, t["pair_rank_correlations"][name])
        associations[name] = rho
    expected_names = {
        f"{wave}_K{k}_{order}_{period}"
        for wave in ["daily_profile", "weekday_sequence"]
        for k in [3, 4, 5]
        for order in ["ascending", "descending"]
        for period in ["first", "second"]
    }
    exact("UPC:stored_24_names", set(u), expected_names)
    exact(
        "UPC:record_24_names",
        tuple(r["name"] for r in t["partition_records"]),
        tuple(sorted(expected_names)),
    )
    partitions = []
    memberships = {}
    for row in t["partition_records"]:
        name = row["name"]
        labels = u[name][ids - 1]
        exact(name + ":all_16_assigned", bool(np.all(labels >= 0)), True)
        exact(name + ":labels", labels, row["labels"])
        exact(name + ":included_cells", row["included_cells"], 16)
        sizes = {str(int(k)): int(np.sum(labels == k)) for k in np.unique(labels)}
        exact(name + ":sizes", sizes, row["cluster_sizes"])
        inside = labels[upper[0]] == labels[upper[1]]
        outside = ~inside
        exact(name + ":inside_pairs", int(inside.sum()), row["inside_pairs"])
        exact(name + ":outside_pairs", int(outside.sum()), row["outside_pairs"])
        numeric(name + ":inside_mean", values[inside].mean(), row["inside_mean_cross_excess"])
        numeric(name + ":outside_mean", values[outside].mean(), row["outside_mean_cross_excess"])
        null = row["size_preserving_random_inside_mean_quantiles"]
        exact(
            name + ":reported_null_order",
            len(null) == 3 and bool(np.isfinite(null).all()) and null[0] <= null[1] <= null[2],
            True,
        )
        # Only interpret saved quantiles; no permutation generation or p-value claim.
        position = (
            "below_reported_lower_quantile"
            if row["inside_mean_cross_excess"] < null[0]
            else (
                "above_reported_upper_quantile"
                if row["inside_mean_cross_excess"] > null[2]
                else "within_reported_quantiles"
            )
        )
        partitions.append(
            dict(
                name=name,
                cluster_sizes=sizes,
                inside_pairs=row["inside_pairs"],
                outside_pairs=row["outside_pairs"],
                inside_mean=row["inside_mean_cross_excess"],
                outside_mean=row["outside_mean_cross_excess"],
                reported_null_quantiles=null,
                null_position=position,
                null_samples_recomputed=False,
            )
        )
        memberships.setdefault(tuple(inside.tolist()), []).append(name)
    a = u["daily_profile_K3_ascending_first"][ids - 1]
    b = u["daily_profile_K3_ascending_second"][ids - 1]
    exact(
        "pair_changes:four_masks",
        [(r["same_group_first"], r["same_group_second"]) for r in t["primary_pair_changes"]],
        [(False, False), (False, True), (True, False), (True, True)],
    )
    for row in t["primary_pair_changes"]:
        mask = ((a[upper[0]] == a[upper[1]]) == row["same_group_first"]) & (
            (b[upper[0]] == b[upper[1]]) == row["same_group_second"]
        )
        label = f"pair_changes:{row['same_group_first']}:{row['same_group_second']}"
        exact(label + ":pairs", int(mask.sum()), row["pairs"])
        numeric(label + ":mean", values[mask].mean(), row["mean_cross_excess"])
    for field in ["new_model_contexts", "new_model_query_rows", "new_RCTL_fits"]:
        exact("transfer:" + field, t[field], 0)

    exact("identity:settings_equal", s["settings"], started)
    exact("identity:calls_equal", s["calls"], calls)
    exact("identity:plan_hash", started["plan_sha256"], CATALOG["SRC-0020950"]["sha256"])
    exact("identity:input_hash", started["input_sha256"], CATALOG["SRC-0023577"]["sha256"])
    exact("identity:IDs", identity["cell_ids"], ids)
    exact("identity:settings_IDs", started["cell_ids"], ids.tolist())
    exact("identity:query_times", identity["query_times"], q)
    exact("identity:settings_query_times", started["query_times"], q.tolist())
    ct = identity["context_times"]
    exact("identity:settings_context_times", started["context_times"], ct.tolist())
    exact("identity:context_count", len(ct), 168)
    exact("identity:context_strict_order", bool(np.all(np.diff(ct) > 0)), True)
    exact("identity:context_bounds", bool(np.all((ct >= 168) & (ct < 672))), True)
    exact("identity:one_per_week_phase", np.sort((ct - 168) % 168), np.arange(168))
    exact("identity:ID_permutation", sorted(started["ID_column_permutation"]), list(range(16)))
    exact("identity:seed", started["seed"], 20260925)
    exact("identity:ensemble", started["ensemble"], 1)
    exact("identity:context_rows", started["context_rows"], 2688)
    exact("identity:query_rows", started["query_rows"], 1024)
    exact("identity:actual_mapping", identity["actual"], Y.ravel())
    models = [
        "TabICL_no_ID",
        "TabICL_cell_ID",
        "TabICL_cell_ID_permuted",
        "Ridge_no_ID",
        "Ridge_cell_ID",
        "HGB_no_ID",
        "HGB_cell_ID",
    ]
    exact(
        "identity:prediction_keys",
        set(identity),
        set(models) | {"actual", "cell_ids", "context_times", "query_times"},
    )
    exact("identity:result_keys", set(s["results"]), set(models))
    exact("identity:partial_keys", set(partial), set(models[:3]))
    for name in models[:3]:
        exact("identity:partial_matches_final:" + name, partial[name], identity[name])
    dayids = q // 24
    metrics = {}
    for name in models:
        pred = identity[name]
        exact(name + ":prediction_shape", pred.shape, (1024,))
        err = np.abs(pred - identity["actual"]).reshape(16, 64)
        result = dict(
            mean_cell_MAE=float(err.mean()),
            cell_MAE=err.mean(1).tolist(),
            day_MAE={
                str(int(day)): float(err[:, dayids == day].mean()) for day in np.unique(dayids)
            },
        )
        numeric(name + ":mean", result["mean_cell_MAE"], s["results"][name]["mean_cell_MAE"])
        numeric(name + ":cell_means", result["cell_MAE"], s["results"][name]["cell_MAE"])
        exact(name + ":day_keys", set(result["day_MAE"]), set(s["results"][name]["day_MAE"]))
        for day, value in result["day_MAE"].items():
            numeric(name + ":day:" + day, value, s["results"][name]["day_MAE"][day])
        metrics[name] = result
    deltas = []
    expected_deltas = {"TabICL_cell_ID", "TabICL_cell_ID_permuted", "Ridge_cell_ID", "HGB_cell_ID"}
    exact("identity:delta_keys", set(s["ID_deltas"]), expected_deltas)
    for name, row in s["ID_deltas"].items():
        base = name.split("_")[0] + "_no_ID"
        m, b = metrics[name], metrics[base]
        change = m["mean_cell_MAE"] - b["mean_cell_MAE"]
        numeric(name + ":delta_mean", change, row["MAE_change_ID_minus_no_ID"])
        cells = np.array(m["cell_MAE"]) - np.array(b["cell_MAE"])
        numeric(name + ":delta_cells", cells, row["cell_changes"])
        days = {day: m["day_MAE"][day] - b["day_MAE"][day] for day in m["day_MAE"]}
        exact(name + ":delta_day_keys", set(days), set(row["day_changes"]))
        for day, value in days.items():
            numeric(name + ":delta_day:" + day, value, row["day_changes"][day])
        worse = [int(ids[i]) for i in np.flatnonzero(cells > 0)]
        deltas.append(
            dict(
                condition=name,
                mean_change=change,
                relative_MAE_reduction_percent=-100 * change / b["mean_cell_MAE"],
                improved_cells=int(np.sum(cells < 0)),
                worse_cells=worse,
                tied_cells=int(np.sum(cells == 0)),
                improved_days=[day for day, value in days.items() if value < 0],
                worse_days=[day for day, value in days.items() if value > 0],
                per_cell_changes=cells.tolist(),
                day_changes=days,
            )
        )
    exact(
        "identity:call_conditions",
        [r["condition"] for r in calls],
        ["no_ID", "cell_ID", "cell_ID_permuted"],
    )
    for row, features in zip(calls, [16, 32, 32], strict=True):
        for field, value in [
            ("context_rows", 2688),
            ("query_rows", 1024),
            ("features", features),
            ("ensemble", 1),
        ]:
            exact(row["condition"] + ":" + field, row[field], value)
    numeric(
        "identity:reported_call_time_sum",
        sum(r["fit_seconds"] + r["predict_seconds"] for r in calls),
        s["TabICL_seconds"],
    )
    exact("identity:finished_status", finished["status"], "completed")
    exact("identity:finished_contexts", finished["contexts"], len(calls))
    exact(
        "identity:finished_query_rows", finished["query_rows"], sum(r["query_rows"] for r in calls)
    )
    exact("identity:finished_RCTL", finished["RCTL_fits"], 0)
    exact("identity:settings_RCTL", started["new_RCTL_fits"], 0)
    exact("identity:RCTL_selection", s["RCTL_results_used_for_clustering"], False)
    numeric("identity:finished_stage_time", finished["stage_seconds"], s["stage_seconds"])
    report = dict(
        batch_id="history-008",
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks_passed=len(checks),
        checks=checks,
        sources=list(accessed.values()),
        tolerances=dict(rtol=1e-7, atol=1e-9, exact_identity_checks=True),
        transfer=dict(
            self_mean=float(np.diag(mae).mean()),
            other_mean=float(mae[other].mean()),
            symmetric_negative_pairs=int(np.sum(values < 0)),
            pair_count=len(values),
            spearman=associations,
            partitions=partitions,
            identical_restricted_partitions=list(memberships.values()),
            primary_pair_changes=t["primary_pair_changes"],
        ),
        identity=dict(
            metrics=metrics,
            deltas=deltas,
            day_query_counts={
                str(int(day)): int(np.sum(dayids == day)) for day in np.unique(dayids)
            },
            context_rows_per_week=[int(np.sum((ct - 168) // 168 == i)) for i in range(3)],
            historical_Tab_contexts=3,
            historical_Tab_query_rows=3072,
            historical_simple_fits=4,
        ),
        models_run=0,
        new_clustering_runs=0,
        new_simulations_run=0,
        original_code_executed=False,
        limitations=[
            "Input support neighbour distances and q95 thresholds remain saved report values; "
            "rank/quantile summaries were checked.",
            "1000-permutation raw samples are not present in saved NPZ; "
            "saved quantiles read, not regenerated or independently verified.",
            "Runtime/RSS are reports; call-time sums and duplicated fields checked, "
            "not independently timed.",
            "ID context-time/column-permutation validity checked "
            "without recreating seeded random draws.",
            "Original model/checkpoint inference and whole UPC pipeline were not rerun. "
            "Literature part15 remains pending.",
            "design_data dates object payload was not loaded; "
            "calendar uses recorded Nov1 start already scoped in history007.",
        ],
    )
    return report


def main() -> None:
    """Write a portable report without changing preserved inputs."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = verify(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(
        (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    )
    print(
        json.dumps(
            {
                key: report[key]
                for key in ["success", "checks_passed", "models_run", "new_simulations_run"]
            }
        )
    )


if __name__ == "__main__":
    main()
