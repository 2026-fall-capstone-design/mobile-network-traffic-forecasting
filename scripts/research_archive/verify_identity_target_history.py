"""Check stored broad-cell and residual-target results without running learners."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

import numpy as np


def verify(source: Path) -> dict:
    """Check identities, schemas, recorded conditions, metrics and adverse cases."""
    manifest = json.loads(source.read_text(encoding="utf-8-sig"))
    registry = {r["source_id"]: r for r in manifest["sources"]}
    checks, accessed = [], {}

    def exact(name, actual, expected):
        ok = (
            bool(np.array_equal(actual, expected))
            if isinstance(actual, np.ndarray) or isinstance(expected, np.ndarray)
            else actual == expected
        )
        if not ok:
            raise AssertionError(name)
        checks.append(name)

    def numeric(name, actual, expected):
        a, b = np.asarray(actual), np.asarray(expected)
        exact(
            name,
            a.shape == b.shape
            and np.isfinite(a).all()
            and np.isfinite(b).all()
            and np.allclose(a, b, rtol=1e-12, atol=1e-12),
            True,
        )

    def match(name, actual, expected):
        if isinstance(actual, dict):
            exact(name + ":keys", set(actual), set(expected))
            for key, value in actual.items():
                match(name + "." + key, value, expected[key])
        elif isinstance(actual, (str, bool, int)):
            exact(name, actual, expected)
        else:
            numeric(name, actual, expected)

    def access(sid, scope):
        row = registry[sid]
        path = source.parent / row["archive_path"]
        if sid not in accessed:
            raw = path.read_bytes()
            exact(sid + ":size", len(raw), row["size_bytes"])
            exact(sid + ":sha256", hashlib.sha256(raw).hexdigest(), row["sha256"])
            accessed[sid] = {k: row[k] for k in ["source_id", "path", "size_bytes", "sha256"]}
            accessed[sid]["read_scope"] = scope
        return path

    def saved(sid):
        return json.loads(access(sid, "JSON:all_keys").read_text(encoding="utf-8-sig"))

    def arrays(sid, keys=None):
        with np.load(
            access(sid, "NPZ:all" if keys is None else "NPZ:" + ",".join(keys)), allow_pickle=False
        ) as d:
            a = {k: d[k] for k in (d.files if keys is None else keys)}
        for k, v in a.items():
            exact(sid + ":finite:" + k, v.dtype.kind in "bifu" and np.isfinite(v).all(), True)
        return a

    def schema(name, obj, keys):
        exact(name + ":keys", set(obj), set(keys))

    text_ids = ["SRC-0021049", "SRC-0021073", "SRC-0022531", "SRC-0023197", "SRC-0023187"]
    new_ids = text_ids + [
        "SRC-0023579",
        "SRC-0024349",
        "SRC-0024350",
        "SRC-0024351",
        "SRC-0024352",
        "SRC-0024353",
        "SRC-0024354",
        "SRC-0032380",
        "SRC-0032381",
        "SRC-0032382",
        "SRC-0032383",
        "SRC-0032384",
        "SRC-0032385",
    ]
    exact(
        "manifest:ids",
        sorted(r["source_id"] for r in manifest["sources"]),
        sorted(new_ids + ["SRC-0021095", "SRC-0032487"]),
    )
    exact(
        "manifest:new_ids",
        sorted(
            r["source_id"]
            for r in manifest["sources"]
            if r["preservation"] == "new_byte_identical_archive"
        ),
        sorted(new_ids),
    )
    for sid in text_ids + ["SRC-0021095"]:
        access(sid, "hash_only; static_text_read_separately")
    b, r = arrays("SRC-0024350"), arrays("SRC-0032381")
    t = arrays("SRC-0032487", ["X", "Y", "times", "cell_ids", "scales"])
    models = ["TabICL", "Ridge", "HGB"]
    names_r = [m + "_" + v for m in models for v in ["no_ID", "cell_ID"]]
    names_b = names_r + [m + "_past_summary" for m in models] + ["TabICL_cell_ID_permuted"]
    common = dict(actual=(2048,), cell_ids=(32,), context_times=(64,), query_times=(64,))
    for label, a, shapes in [
        (
            "broad",
            b,
            {**common, **dict.fromkeys(names_b, (2048,)), "past_summary_features": (32, 4)},
        ),
        (
            "residual",
            r,
            {
                **common,
                **dict.fromkeys(names_r, (2048,)),
                **dict.fromkeys(["latest_input", "context_actual", "context_latest"], (2048,)),
            },
        ),
        (
            "prior",
            t,
            dict(X=(32, 1176, 16), Y=(32, 1176), times=(1176,), cell_ids=(32,), scales=(32,)),
        ),
    ]:
        schema(label, a, shapes)
        for key, shape in shapes.items():
            exact(label + ":shape:" + key, a[key].shape, shape)
        for key in set(a) & {"cell_ids", "times", "context_times", "query_times"}:
            exact(label + ":integer:" + key, a[key].dtype.kind in "iu", True)
    ids, qt, ct = b["cell_ids"], b["query_times"], b["context_times"]
    exact("ids:unique_bounds", len(set(ids)) == 32 and ((ids >= 1) & (ids <= 10000)).all(), True)
    exact("ids:residual", ids, r["cell_ids"])
    exact("ids:prior", ids, t["cell_ids"])
    exact("prior:times", t["times"], np.arange(168, 1344))
    exact("prior:positive_scales", (t["scales"] > 0).all(), True)
    for label, times, lo, hi in [("context_times", ct, 168, 671), ("query_times", qt, 672, 1007)]:
        exact(label + ":selection", times, np.rint(np.linspace(lo, hi, 64)).astype(int))
        exact(label + ":residual", times, r[label])
    ci, qi = np.searchsorted(t["times"], ct), np.searchsorted(t["times"], qt)
    cy, qy, latest = t["Y"][:, ci].ravel(), t["Y"][:, qi].ravel(), t["X"][:, qi, 7].ravel()
    exact("broad:target", b["actual"], qy)
    for key, value in dict(
        actual=qy, latest_input=latest, context_actual=cy, context_latest=t["X"][:, ci, 7].ravel()
    ).items():
        exact("residual:" + key, r[key], value)
    days = np.unique(qt // 24)
    weights = [int(np.sum(qt // 24 == day)) for day in days]
    exact("day:sample_counts", weights, [5, 4, 5, 4, 5, 4, 5, 5, 4, 5, 4, 5, 4, 5])

    def describe(pred, median=False):
        loss = np.abs(pred - qy).reshape(32, 64)
        by = loss.mean(1)
        result = dict(
            MAE=float(loss.mean()),
            MAE_original16=float(loss[:16].mean()),
            MAE_added16=float(loss[16:].mean()),
            MAE_by_cell=by.tolist(),
            MAE_by_day={str(int(day)): float(loss[:, qt // 24 == day].mean()) for day in days},
            max_cell_loss_fraction=float(by.max() / by.sum()),
            max_loss_cell_id=int(ids[np.argmax(by)]),
        )
        if median:
            result["cell_MAE_median"] = float(np.median(by))
        numeric(
            "metric:weighted_days",
            result["MAE"],
            np.average(list(result["MAE_by_day"].values()), weights=weights),
        )
        return result

    reports, results, reported_costs = {}, {}, {}
    groups = [
        (
            "broad",
            b,
            names_b,
            "SRC-0021049",
            "SRC-0024353",
            "SRC-0024354",
            "SRC-0024349",
            "SRC-0024352",
            "SRC-0024351",
        ),
        (
            "residual",
            r,
            names_r,
            "SRC-0021073",
            "SRC-0032384",
            "SRC-0032385",
            "SRC-0032380",
            "SRC-0032383",
            "SRC-0032382",
        ),
    ]
    for label, a, names, plan, start_id, summary_id, calls_id, finish_id, partial_id in groups:
        start, summary, calls, finish = (
            saved(sid) for sid in [start_id, summary_id, calls_id, finish_id]
        )
        broad = label == "broad"
        common_settings = dict(
            plan_sha256=registry[plan]["sha256"],
            cell_ids=ids.tolist(),
            context_times=ct.tolist(),
            query_times=qt.tolist(),
            context_rows=2048,
            query_rows=2048,
            seed=20260925,
            ensemble=1,
            development_only=True,
            new_RCTL_fits=0,
        )
        extra_settings = (
            ["input_sha256", "summary_statistics", "ID_column_permutation"]
            if broad
            else ["target", "raw_results_sha256"]
        )
        schema(label + ":settings", start, list(common_settings) + extra_settings)
        for key, value in common_settings.items():
            exact(label + ":settings:" + key, start[key], value)
        exact(label + ":settings_match", summary["settings"], start)
        exact(label + ":calls_match", summary["calls"], calls)
        if broad:
            exact("broad:input_hash", start["input_sha256"], registry["SRC-0032487"]["sha256"])
            exact("broad:statistics", start["summary_statistics"], b["past_summary_features"])
            perm = np.asarray(start["ID_column_permutation"])
            exact("broad:permutation_integer", perm.dtype.kind in "iu", True)
            exact("broad:permutation_bijection", np.sort(perm), np.arange(32))
        else:
            exact(
                "residual:raw_hash", start["raw_results_sha256"], registry["SRC-0024350"]["sha256"]
            )
            exact(
                "residual:target_description",
                start["target"],
                "Y minus latest observed input; add that same available input after prediction",
            )
        variants, features = (
            (["no_ID", "cell_ID", "cell_ID_permuted", "past_summary"], [16, 48, 48, 20])
            if broad
            else (["no_ID", "cell_ID"], [16, 48])
        )
        exact(label + ":call_order", [c["condition"] for c in calls], variants)
        memory_key = "RSS_peak_so_far" if broad else "RSS_bytes_after_call"
        for call, variant, n in zip(calls, variants, features, strict=True):
            schema(
                label + ":call:" + variant,
                call,
                [
                    "condition",
                    "context_rows",
                    "query_rows",
                    "features",
                    "fit_seconds",
                    "predict_seconds",
                    memory_key,
                    "ensemble",
                ],
            )
            for key, value in dict(
                condition=variant, context_rows=2048, query_rows=2048, features=n, ensemble=1
            ).items():
                exact(label + ":call:" + variant + ":" + key, call[key], value)
            for key in ["fit_seconds", "predict_seconds", memory_key]:
                exact(
                    label + ":cost_positive:" + variant + ":" + key,
                    np.isfinite(call[key]) and call[key] > 0,
                    True,
                )
        schema(
            label + ":finished",
            finish,
            ["contexts", "query_rows", "new_RCTL_fits", "stage_seconds", "TabICL_seconds"],
        )
        for key, value in dict(
            contexts=len(variants), query_rows=2048 * len(variants), new_RCTL_fits=0
        ).items():
            exact(label + ":finished:" + key, finish[key], value)
        numeric(
            label + ":call_seconds",
            sum(c["fit_seconds"] + c["predict_seconds"] for c in calls),
            summary["TabICL_seconds"],
        )
        for key in ["stage_seconds", "TabICL_seconds"]:
            exact(label + ":finished:" + key, finish[key], summary[key])
        exact(
            label + ":stage_cost_order",
            0 < summary["simple_model_seconds"]
            and summary["TabICL_seconds"] + summary["simple_model_seconds"]
            <= summary["stage_seconds"]
            <= (360 if broad else 180),
            True,
        )
        flags = (
            dict(new_RCTL_fits=0, clustering_benefit_established=False)
            if broad
            else dict(
                new_RCTL_fits=0,
                clustering_improvement_established=False,
                novel_method_established=False,
            )
        )
        schema(
            label + ":summary",
            summary,
            [
                "settings",
                "calls",
                "results",
                "TabICL_seconds",
                "simple_model_seconds",
                "stage_seconds",
            ]
            + list(flags)
            + (
                ["changes", "peak_RSS_bytes"]
                if broad
                else ["raw_comparison", "last_value_baseline"]
            ),
        )
        for key, value in flags.items():
            exact(label + ":flag:" + key, summary[key], value)
        if broad:
            exact(
                "broad:RSS_monotonic",
                [c[memory_key] for c in calls],
                sorted(c[memory_key] for c in calls),
            )
            exact("broad:RSS_final", calls[-1][memory_key], summary["peak_RSS_bytes"])
        computed = {name: describe(a[name], broad) for name in names}
        match(label + ":results", computed, summary["results"])
        partial = arrays(partial_id)
        schema(
            label + ":partial",
            partial,
            ["TabICL_" + v for v in variants] + ["actual", "cell_ids", "query_times"],
        )
        for key, value in partial.items():
            exact(label + ":partial:" + key, value, a[key])
        reports[label], results[label] = summary, computed
        reported_costs[label] = dict(
            contexts=len(variants),
            query_rows=2048 * len(variants),
            small_fits=6 if broad else 4,
            calls=calls,
            **{k: summary[k] for k in ["TabICL_seconds", "simple_model_seconds", "stage_seconds"]},
        )
    broad_changes, raw_comparison = {}, {}
    for key in names_b:
        if key.endswith("_no_ID"):
            continue
        value, ref = results["broad"][key], results["broad"][key.split("_")[0] + "_no_ID"]
        delta = np.array(value["MAE_by_cell"]) - ref["MAE_by_cell"]
        broad_changes[key] = dict(
            MAE_change=value["MAE"] - ref["MAE"],
            relative_MAE_change=value["MAE"] / ref["MAE"] - 1,
            cell_changes=delta.tolist(),
            cells_improved=int((delta < 0).sum()),
            day_changes={
                d: value["MAE_by_day"][d] - ref["MAE_by_day"][d] for d in ref["MAE_by_day"]
            },
        )
    match("broad:changes", broad_changes, reports["broad"]["changes"])
    for key in names_r:
        value, ref = results["residual"][key], results["broad"][key]
        delta = np.array(value["MAE_by_cell"]) - ref["MAE_by_cell"]
        raw_comparison[key] = dict(
            raw_MAE=ref["MAE"],
            residual_MAE=value["MAE"],
            change=value["MAE"] - ref["MAE"],
            cell_changes=delta.tolist(),
            cells_improved=int((delta < 0).sum()),
            day_changes={
                d: value["MAE_by_day"][d] - ref["MAE_by_day"][d] for d in ref["MAE_by_day"]
            },
        )
    match("residual:comparison", raw_comparison, reports["residual"]["raw_comparison"])
    baseline = describe(latest)
    match("last_value", baseline, reports["residual"]["last_value_baseline"])
    concentration = saved("SRC-0023579")
    rawcell = np.abs(b["TabICL_no_ID"] - qy).reshape(32, 64).mean(1)
    rescell = np.abs(r["TabICL_no_ID"] - qy).reshape(32, 64).mean(1)
    j = int(np.argmax(rawcell))

    def bounds(values):
        return [float(values.min()), float(values.max())]

    derived = dict(
        input_sha256={
            k: registry[sid]["sha256"]
            for k, sid in [
                ("temporal_validity", "SRC-0032487"),
                ("broad_cell_information", "SRC-0024350"),
                ("target_parameterization", "SRC-0032381"),
            ]
        },
        development_only=True,
        all_cells_retained=ids.tolist(),
        max_raw_loss_cell=int(ids[j]),
        max_raw_loss_fraction=float(rawcell[j] / rawcell.sum()),
        max_cell_scale=float(t["scales"][j]),
        max_cell_context_target_range=bounds(cy.reshape(32, 64)[j]),
        all_context_target_range=bounds(cy),
        max_cell_query_target_range=bounds(qy.reshape(32, 64)[j]),
        max_cell_query_latest_range=bounds(latest.reshape(32, 64)[j]),
        max_cell_fraction_query_above_own_context_target_max=float(
            (qy.reshape(32, 64)[j] > cy.reshape(32, 64)[j].max()).mean()
        ),
        max_cell_raw_MAE=float(rawcell[j]),
        max_cell_residual_MAE=float(rescell[j]),
        raw_MAE=float(rawcell.mean()),
        residual_MAE=float(rescell.mean()),
        relative_mean_MAE_reduction=float(1 - rescell.mean() / rawcell.mean()),
        cells_improved=int((rescell < rawcell).sum()),
        cells_worsened=int((rescell > rawcell).sum()),
        original16_raw_MAE=float(rawcell[:16].mean()),
        original16_residual_MAE=float(rescell[:16].mean()),
        cell_MAE_changes={
            str(int(cid)): float(v) for cid, v in zip(ids, rescell - rawcell, strict=True)
        },
        new_model_calls=0,
    )
    schema(
        "concentration",
        concentration,
        list(derived) + ["largest_target_examples", "elapsed_seconds", "interpretation"],
    )
    for key, value in derived.items():
        match("concentration:" + key, value, concentration[key])
    examples = []
    for k in np.argsort(qy.reshape(32, 64)[j])[-6:]:
        example = dict(
            target_time=int(qt[k]),
            actual=float(qy.reshape(32, 64)[j, k]),
            latest_input=float(latest.reshape(32, 64)[j, k]),
            raw_prediction=float(b["TabICL_no_ID"].reshape(32, 64)[j, k]),
            residual_prediction=float(r["TabICL_no_ID"].reshape(32, 64)[j, k]),
        )
        examples.append(example)
    exact("concentration:examples", examples, concentration["largest_target_examples"])
    exact(
        "concentration:elapsed",
        np.isfinite(concentration["elapsed_seconds"]) and concentration["elapsed_seconds"] > 0,
        True,
    )
    exact(
        "concentration:interpretation",
        concentration["interpretation"],
        "Concentrated development finding, not general improvement or a new clustering method. "
        "No cell was removed. Observed saturation does not imply a mathematical output bound.",
    )

    (date_ref,) = manifest["derived_inputs"]
    raw = (source.parent / date_ref["archive_path"]).read_bytes()
    exact("dates:sha", hashlib.sha256(raw).hexdigest(), date_ref["sha256"])
    exact("dates:size", len(raw), date_ref["size_bytes"])
    dates = json.loads(raw)["dates"]
    dt = [datetime.fromisoformat(x) for x in dates[:1008]]
    exact("dates:count", len(dt), 1008)
    exact("dates:origin", dt[0], datetime(2013, 11, 1))
    exact(
        "dates:hourly",
        all((y - x).total_seconds() == 3600 for x, y in zip(dt, dt[1:], strict=False)),
        True,
    )
    day_labels = [dates[int(day) * 24][:10] for day in days]

    def contrast(pred, ref):
        delta = (np.abs(pred - qy) - np.abs(ref - qy)).reshape(32, 64)
        cells = delta.mean(1)
        cell_days = np.stack([delta[:, qt // 24 == day].mean(1) for day in days], axis=1)
        daily = cell_days.mean(0)
        numeric("contrast:weighted_days", delta.mean(), np.average(daily, weights=weights))
        return dict(
            mean=float(delta.mean()),
            unweighted_daily_mean=float(daily.mean()),
            cell_changes=cells.tolist(),
            cell_day_changes=cell_days.tolist(),
            day_changes=daily.tolist(),
            better_cells=int((cells < 0).sum()),
            tied_cells=int((cells == 0).sum()),
            worse_cells=int((cells > 0).sum()),
            worse_days=int((daily > 0).sum()),
            worse_cell_days=int((cell_days > 0).sum()),
        )

    contrasts = {}
    for model in models:
        for variant in ["cell_ID", "past_summary"] + (
            ["cell_ID_permuted"] if model == "TabICL" else []
        ):
            contrasts["raw:" + model + "_" + variant + "_minus_no_ID"] = contrast(
                b[model + "_" + variant], b[model + "_no_ID"]
            )
        for variant in ["no_ID", "cell_ID"]:
            name = model + "_" + variant
            contrasts["residual_minus_raw:" + name] = contrast(r[name], b[name])
            contrasts["residual_minus_last:" + name] = contrast(r[name], latest)
        contrasts["residual:" + model + "_ID_minus_no_ID"] = contrast(
            r[model + "_cell_ID"], r[model + "_no_ID"]
        )
    contrasts["raw:TabICL_ID_permutation_minus_ID"] = contrast(
        b["TabICL_cell_ID_permuted"], b["TabICL_cell_ID"]
    )
    return dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks_passed=len(checks),
        checks=checks,
        accessed_sources=list(accessed.values()),
        results=results,
        contrasts=contrasts,
        baseline=baseline,
        concentration=derived,
        examples_verified=examples,
        cell_ids=ids.tolist(),
        day_labels=day_labels,
        queries_per_day=weights,
        reported_costs=reported_costs,
        reported_additional_cost=dict(
            contexts=6,
            query_rows=12288,
            small_fits=10,
            TabICL_seconds=sum(v["TabICL_seconds"] for v in reported_costs.values()),
        ),
        models_run=0,
        random_draws=0,
        historical_code_imported=False,
        limitations=[
            "Expanded model X was not saved; recipe and separate local H5 checks "
            "do not prove actual consumed X.",
            "Costs are historical reports, not new measurements or "
            "full preprocessing/continuous RSS peaks.",
            "No per-run checkpoint/package hash; no independent prediction reproduction.",
            "Cumulative older ledger and primary-literature synthesis "
            "remain outside this bounded audit.",
        ],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes((json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode())
    print(json.dumps({k: result[k] for k in ["success", "checks_passed", "models_run"]}))
