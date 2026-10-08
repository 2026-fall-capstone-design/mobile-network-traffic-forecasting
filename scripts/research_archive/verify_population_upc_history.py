"""10–12의 저장 배열·소속만 검산한다. 원 코드·모델·새 clustering을 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from datetime import UTC, datetime
from pathlib import Path

import numpy as np


def verify(source: Path) -> dict:
    """Verify portable historical outputs without loading the raw traffic tensor."""
    manifest = json.loads(source.read_text(encoding="utf-8-sig"))
    catalog = {r["source_id"]: r for r in manifest["sources"]}
    accessed = {}
    checks = []

    def check(name, actual, expected, atol=1e-12):
        """Compare exact identities or same-shape numeric values within stated tolerance."""
        if isinstance(actual, (list, np.ndarray, float, np.floating)):
            a, b = np.asarray(actual), np.asarray(expected)
            ok = a.shape == b.shape and bool(np.allclose(a, b, rtol=1e-12, atol=atol))
        else:
            ok = actual == expected
        checks.append(dict(check=name, passed=bool(ok)))
        if not ok:
            raise AssertionError((name, actual, expected))

    def access(sid, scope):
        """Hash each preserved file and record the fields used, retaining original identity."""
        row = catalog[sid]
        p = source.parent / row["archive_path"]
        if sid not in accessed:
            with p.open("rb") as stream:
                digest = hashlib.file_digest(stream, "sha256").hexdigest()
            check(sid + ":sha256", digest, row["sha256"])
            check(sid + ":size", p.stat().st_size, row["size_bytes"])
            accessed[sid] = {k: row[k] for k in ["source_id", "path", "sha256", "size_bytes"]}
            accessed[sid]["read_scope"] = []
        accessed[sid]["read_scope"] = sorted(set(accessed[sid]["read_scope"]) | set(scope))
        return p

    def saved_json(sid):
        """Parse complete saved JSON without executing any referenced commands."""
        return json.loads(access(sid, ["JSON:all_keys"]).read_text(encoding="utf-8-sig"))

    pop = saved_json("SRC-0023595")
    upc = saved_json("SRC-0023613")
    for output, plan in [(pop, "SRC-0020863"), (upc, "SRC-0020887")]:
        access(plan, ["sha256_only"])
        check(plan + ":result_plan_hash", output["plan_sha256"], catalog[plan]["sha256"])
        for field in ["new_model_contexts", "new_model_query_rows", "new_RCTL_fits"]:
            check(plan + ":" + field, output[field], 0)
        check(plan + ":original_UPC_replication", output["is_original_UPC_replication"], False)

    with np.load(
        access("SRC-0023596", ["NPZ:all_numeric_arrays_for_arithmetic"]), allow_pickle=False
    ) as z:
        vals = {key: z[key] for key in z.files}
    expected_pop = {
        "cell_ids",
        "eligible",
        "scale",
        "cv",
        "peak_concentration",
        "peak_mode_all",
        "peak_mode_first",
        "peak_mode_last",
        "profile_corr",
        "mae_lag_1",
        "mae_lag_24",
        "mae_lag_168",
    }
    check("population:keys", set(vals), expected_pop)
    for key, a in vals.items():
        check("population:shape:" + key, a.shape, (10000,))
        assert a.dtype.kind in "bifu" and np.isfinite(a).all(), key
    check("population:cell_ids", vals["cell_ids"], np.arange(1, 10001))
    check("population:eligible_count", int(vals["eligible"].sum()), 10000)
    check("population:eligible_dtype", vals["eligible"].dtype.kind, "b")
    check("population:total_cells", len(vals["cell_ids"]), pop["total_cells"])
    check("population:reported_eligible", int(vals["eligible"].sum()), pop["eligible_cells"])
    pilot = np.isin(vals["cell_ids"], pop["B2_pilot_ids"])
    check("population:pilot_count", int(pilot.sum()), 16)
    check("population:pilot_unique", len(set(pop["B2_pilot_ids"])), 16)
    with np.load(access("SRC-0023589", ["array:cell_ids"]), allow_pickle=False) as original_pilot:
        check("population:pilot_identity_with_B2", original_pilot["cell_ids"], pop["B2_pilot_ids"])
    descriptions = {
        "first_28d_mean_activity": "scale",
        "first_28d_coefficient_of_variation": "cv",
        "weekday_peak_mode_concentration": "peak_concentration",
        "weekday_profile_half_period_PCC": "profile_corr",
    }
    quantile_keys = ["0", "10", "25", "50", "75", "90", "99", "100"]
    quantile_ps = [0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99, 1]

    def verify_desc(name, a, saved):
        """Compare saved finite-value means and quantiles with their stored arrays."""
        a = a[np.isfinite(a)]
        check(name + ":count", len(a), saved["count"])
        check(name + ":mean", float(a.mean()), saved["mean"])
        for key, value in zip(quantile_keys, np.quantile(a, quantile_ps), strict=True):
            check(name + ":q" + key, float(value), saved["quantiles"][key])

    for scope, mask in [("whole_grid", vals["eligible"]), ("B2_pilot", pilot & vals["eligible"])]:
        report = pop[scope]
        check(scope + ":cells", int(mask.sum()), report["cells"])
        for desc, key in descriptions.items():
            verify_desc(scope + ":" + desc, vals[key][mask], report[desc])
        for lag in [1, 24, 168]:
            verify_desc(
                scope + ":mae_lag_" + str(lag),
                vals["mae_lag_" + str(lag)][mask],
                report["next_week_mean_scaled_MAE"][str(lag)],
            )
        check(
            scope + ":mode_equal",
            float(np.mean(vals["peak_mode_first"][mask] == vals["peak_mode_last"][mask])),
            report["half_period_peak_mode_equal_fraction"],
        )
        diff = np.abs(vals["peak_mode_first"][mask] - vals["peak_mode_last"][mask])
        check(
            scope + ":mode_within1h",
            float(np.mean(np.minimum(diff, 24 - diff) <= 1)),
            report["half_period_peak_mode_within_1h_fraction"],
        )
        check(
            scope + ":pcc_undefined",
            int(np.sum(~np.isfinite(vals["profile_corr"][mask]))),
            report["profile_PCC_undefined_cells"],
        )
    percentiles = [
        float(np.mean(vals["scale"][vals["eligible"]] <= vals["scale"][cell - 1]))
        for cell in pop["B2_pilot_ids"]
    ]
    check(
        "pilot:activity_percentiles",
        percentiles,
        pop["pilot_cell_mean_activity_percentiles_in_whole_grid"],
    )
    above_median = int(np.sum(vals["scale"][pilot] > np.median(vals["scale"][vals["eligible"]])))
    check("pilot:above_population_median", above_median, 15)

    with np.load(
        access("SRC-0023612", ["NPZ:all_24_saved_label_vectors"]), allow_pickle=False
    ) as z:
        labels = {key: z[key] for key in z.files}
    expected_labels = {
        f"{kind}_K{k}_{order}_{period}"
        for kind in ["daily_profile", "weekday_sequence"]
        for k in [3, 4, 5]
        for order in ["ascending", "descending"]
        for period in ["first", "second"]
    }
    check("UPC:keys", set(labels), expected_labels)
    for key, a in labels.items():
        check("UPC:shape:" + key, a.shape, (10000,))
        assert a.dtype.kind in "iu"
        k = int(key.split("_K")[1][0])
        assert np.isin(a, [-1] + list(range(k))).all(), key

    def compare(a, b, k):
        """Calculate ARI and best label matching from saved labels only."""
        keep = (a >= 0) & (b >= 0)
        n = int(keep.sum())
        counts = np.bincount((a[keep] * k + b[keep]).astype(int), minlength=k * k).reshape(k, k)

        def choose2(x):
            """Count unordered pairs within each contingency-table block."""
            return int(np.sum(x * (x - 1) // 2))

        observed = choose2(counts)
        rowpairs, colpairs = choose2(counts.sum(1)), choose2(counts.sum(0))
        expected = rowpairs * colpairs / (n * (n - 1) / 2)
        ari = (observed - expected) / ((rowpairs + colpairs) / 2 - expected)
        best = max(
            sum(int(counts[i, j]) for i, j in enumerate(p))
            for p in itertools.permutations(range(k))
        )
        return dict(
            included_cells=n,
            included_fraction=n / len(a),
            adjusted_Rand_index=ari,
            label_matched_agreement=best / n,
        )

    comparison_rows = []
    check("UPC:record_count", len(upc["records"]), 18)
    actual_contract = {
        (r["waveform"], r["K"], r.get("order", "order_sensitivity")) for r in upc["records"]
    }
    expected_contract = {
        (kind, k, order)
        for kind in ["daily_profile", "weekday_sequence"]
        for k in [3, 4, 5]
        for order in ["ascending", "descending", "order_sensitivity"]
    }
    check("UPC:unique_record_contract", actual_contract, expected_contract)
    for i, record in enumerate(upc["records"]):
        kind, k = record["waveform"], record["K"]
        prefix = f"{kind}_K{k}"
        if "order" in record:
            order = record["order"]
            actual = compare(
                labels[f"{prefix}_{order}_first"], labels[f"{prefix}_{order}_second"], k
            )
            for field, val in actual.items():
                check(
                    f"UPC:record{i}:between_periods:{field}", val, record["between_periods"][field]
                )
            comparison_rows.append(
                dict(waveform=kind, K=k, comparison="between_periods", order=order, **actual)
            )
            for period in ["first", "second"]:
                a = labels[f"{prefix}_{order}_{period}"]
                d = record[period]
                check(
                    f"UPC:record{i}:{period}:cluster_counts",
                    np.bincount(a[a >= 0], minlength=k),
                    d["assigned_cell_counts"],
                )
                check(
                    f"UPC:record{i}:{period}:unassigned", int(np.sum(a < 0)), d["unassigned_cells"]
                )
                mode = vals["peak_mode_" + ("last" if period == "second" else "first")]
                groupsizes = np.bincount(mode, minlength=24)
                check(
                    f"UPC:record{i}:{period}:group_sizes",
                    groupsizes,
                    record["group_sizes_" + period],
                )
                selected_hours = [hour for group in d["cluster_peak_hours"] for hour in group]
                check(
                    f"UPC:record{i}:{period}:unique_group_members",
                    len(set(selected_hours)),
                    len(selected_hours),
                )
                check(
                    f"UPC:record{i}:{period}:threshold_groups",
                    sorted(selected_hours),
                    np.flatnonzero(groupsizes > 10).tolist(),
                )
                # Translate stored group membership; do not recalculate PCC or clustering.
                mapped = np.full(10000, -1, dtype=int)
                for j, hours in enumerate(d["cluster_peak_hours"]):
                    mapped[np.isin(mode, hours)] = j
                    check(f"UPC:record{i}:{period}:seed{j}", d["seed_hours"][j], hours[0])
                check(f"UPC:record{i}:{period}:saved_group_labels", mapped, a)
        else:
            for period in ["first", "second"]:
                actual = compare(
                    labels[f"{prefix}_ascending_{period}"],
                    labels[f"{prefix}_descending_{period}"],
                    k,
                )
                for field, val in actual.items():
                    check(
                        f"UPC:record{i}:{period}:order_sensitivity:{field}",
                        val,
                        record["order_sensitivity"][period + "_period"][field],
                    )
                comparison_rows.append(
                    dict(
                        waveform=kind, K=k, comparison="order_sensitivity", period=period, **actual
                    )
                )

    prior_cost = json.loads(
        access("SRC-0023580", ["JSON:elapsed_seconds"]).read_text(encoding="utf-8-sig")
    )["elapsed_seconds"]
    check("prior_08_diagnostic:reported_rounded_seconds", round(prior_cost, 3), 0.249)
    return dict(
        batch_id="history-007",
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks_passed=len(checks),
        checks=checks,
        accessed=list(accessed.values()),
        original_scripts_executed=False,
        original_modules_imported=False,
        models_run=0,
        new_clustering_runs=0,
        new_simulations_run=0,
        method="Saved values/labels; combinatorial ARI and exhaustive label permutations K<=5.",
        population_arrays={
            k: dict(shape=list(a.shape), dtype=str(a.dtype)) for k, a in vals.items()
        },
        label_arrays={k: dict(shape=list(a.shape), dtype=str(a.dtype)) for k, a in labels.items()},
        comparisons=comparison_rows,
        pilot_above_population_median=above_median,
        prior_cost_reference=dict(source_id="SRC-0023580", elapsed_seconds=prior_cost),
        reported_only_not_recomputed=[
            "raw-data quality flags/zero fraction",
            "peak-mode tie counts",
            "runtime/RSS",
        ],
        limits=[
            "Stored aggregates checked against stored arrays; raw traffic tensor not loaded.",
            "No PCC matrix, seed selection or greedy partition independently regenerated.",
            "Dates/HDF5 identity were separately checked locally; not part of portable CI.",
            "No full UPC reproduction, forecasting benefit or independent scientific validation.",
        ],
    )


def main() -> None:
    """Write a UTF-8 verification report for a portable evidence manifest."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(
        (json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    )
    print(
        json.dumps(
            {
                k: result[k]
                for k in ["success", "checks_passed", "models_run", "new_clustering_runs"]
            }
        )
    )


if __name__ == "__main__":
    main()
