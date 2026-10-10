"""69–71의 저장 예측·보정값·피크 지표·원장을 모델 실행 없이 대조한다."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from datetime import UTC, datetime
from fractions import Fraction
from pathlib import Path

import numpy as np

TAUS = [0.5, 0.75, 0.9, 0.95]
GLOBAL = "global_20260925"
TAB = ["tabicl_risk_20260925", "tabicl_risk_20260926"]
METHODS = [
    "empirical_risk_20260925",
    "empirical_risk_20260926",
    GLOBAL,
    "knn_risk_20260925",
    "pcc_balanced_20260925",
    "random_balanced_20260925",
    *TAB,
]
IDS = [
    3737,
    3745,
    3753,
    3765,
    4537,
    4545,
    4553,
    4565,
    5337,
    5345,
    5353,
    5365,
    6137,
    6145,
    6153,
    6165,
]
PERIODS = {"all": slice(0, 480), "first_240": slice(0, 240), "last_240": slice(240, 480)}


def order_statistic(values: np.ndarray, tau: float) -> float:
    """inverted_cdf를 np.quantile 호출 없이 정렬과 정확한 순위로 계산한다."""
    flat = np.sort(values.ravel())
    rank = math.ceil(Fraction(str(tau)) * len(flat))
    return float(flat[rank - 1])


def metrics(pred: np.ndarray, target: np.ndarray, threshold: np.ndarray) -> dict:
    """관측치 기여량을 합산하고 서로 다른 분모의 피크 평균을 보존한다."""
    delta = pred - target
    absolute = np.abs(delta)
    under = np.clip(-delta, 0, None)
    over = np.clip(delta, 0, None)
    mask = target > threshold[:, None]
    counts = mask.sum(axis=1)
    cell_peak = [float(absolute[i, mask[i]].sum() / n) if n else None for i, n in enumerate(counts)]
    u = float(under.sum() / target.size)
    o = float(over.sum() / target.size)
    return dict(
        mae=float(absolute.sum() / target.size),
        under_amount=u,
        over_amount=o,
        bias=float(delta.sum() / target.size),
        under_frequency=float(np.count_nonzero(delta < 0) / target.size),
        peak_query_count=int(counts.sum()),
        cells_with_peak=int(np.count_nonzero(counts)),
        peak_macro_mae=float(np.mean([x for x in cell_peak if x is not None])),
        peak_micro_mae=float(absolute[mask].sum() / counts.sum()),
        nonpeak_micro_mae=float(absolute[~mask].sum() / np.count_nonzero(~mask)),
        peak_loss_contribution=float(absolute[mask].sum() / target.size),
        nonpeak_loss_contribution=float(absolute[~mask].sum() / target.size),
        pinball={str(t): t * u + (1 - t) * o for t in TAUS},
        cell_mae=(absolute.sum(axis=1) / target.shape[1]).tolist(),
        cell_under=(under.sum(axis=1) / target.shape[1]).tolist(),
        cell_over=(over.sum(axis=1) / target.shape[1]).tolist(),
        cell_peak_counts=counts.tolist(),
        cell_peak_mae=cell_peak,
        peak_under_amount=float(under[mask].sum() / counts.sum()),
        peak_over_amount=float(over[mask].sum() / counts.sum()),
    )


def verify(manifest_path: Path) -> dict:
    """보존본 해시를 먼저 검사하고 지정된 작은 배열만 결정적으로 재계산한다."""
    manifest_path = manifest_path.resolve()
    archive_root = manifest_path.parents[2]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks, errors, paths = [], [], {}
    numeric_leaves = 0
    max_abs_error = 0.0

    def check(name: str, good: bool) -> None:
        checks.append(name)
        if not good:
            errors.append(name)

    def equal(name: str, computed, stored, atol: float = 1e-12) -> None:
        """필드·목록 길이도 대조하며 수치 불일치를 누락하지 않는다."""
        nonlocal numeric_leaves, max_abs_error
        if isinstance(computed, dict):
            check(name + ":keys", isinstance(stored, dict) and computed.keys() == stored.keys())
            for key, value in computed.items():
                if isinstance(stored, dict) and key in stored:
                    equal(name + "/" + key, value, stored[key], atol)
        elif isinstance(computed, list):
            check(name + ":length", isinstance(stored, list) and len(computed) == len(stored))
            if isinstance(stored, list):
                for i, (a, b) in enumerate(zip(computed, stored, strict=False)):
                    equal(f"{name}/{i}", a, b, atol)
        elif isinstance(computed, (float, int)) and not isinstance(computed, bool):
            numeric_leaves += 1
            numeric = isinstance(stored, (float, int)) and not isinstance(stored, bool)
            difference = abs(computed - stored) if numeric else math.inf
            max_abs_error = max(max_abs_error, difference)
            check(name, numeric and math.isfinite(stored) and difference <= atol)
        else:
            check(name, type(computed) is type(stored) and computed == stored)

    for row in manifest["sources"]:
        path = (manifest_path.parent / row["archive_path"]).resolve()
        if not path.is_relative_to(archive_root):
            raise ValueError("보존 경로가 연구 아카이브 밖을 가리킴")
        raw = path.read_bytes()
        good = len(raw) == row["size_bytes"] and hashlib.sha256(raw).hexdigest() == row["sha256"]
        check(row["source_id"] + ":identity", good)
        if not good:
            raise ValueError("보존본 해시 또는 크기 불일치: " + row["source_id"])
        paths[row["source_id"]] = path

    def data(sid: str):
        return json.loads(paths[sid].read_text(encoding="utf-8"))

    result, settings, frozen = (data(sid) for sid in ["SRC-0029497", "SRC-0029500", "SRC-0029496"])
    equal("settings_copy", settings, result["settings"])
    equal("frozen_settings", settings, frozen["settings"])
    for label, sid in [("plan", "SRC-0022021"), ("code", "SRC-0022971")]:
        equal(
            label + "_hash",
            hashlib.sha256(paths[sid].read_bytes()).hexdigest(),
            settings[label + "_sha256"],
        )
    input_map = {
        "results/rctl_pilot/all_predictions.npz": "SRC-0030211",
        "results/rctl_pilot/evaluation_data.npz": "SRC-0030236",
        "results/rctl_pilot/fit_results.json": "SRC-0030237",
        "results/rctl_pilot/summary.json": "SRC-0030280",
        "results/frozen_fit_gap_34/predictions.npz": "SRC-0027514",
        "results/frozen_fit_gap_34/summary.json": "SRC-0027517",
    }
    equal(
        "input_hashes",
        {k: hashlib.sha256(paths[s].read_bytes()).hexdigest() for k, s in input_map.items()},
        settings["input_sha256"],
    )
    check(
        "fixed_settings",
        settings["taus"] == TAUS
        and settings["quantile_method"] == "inverted_cdf"
        and settings["offset_parameters"] == 98
        and settings["independent_test"] is False
        and settings["changed_partitions"] is False,
    )
    check(
        "zero_new_model_work",
        all(
            settings[k] == 0
            for k in [
                "new_RCTL_fits",
                "new_RCTL_forward",
                "new_Tab_contexts",
                "new_Tab_rows",
                "new_simple_fits",
            ]
        ),
    )

    arrays, array_audit = {}, []
    for sid in ["SRC-0030211", "SRC-0030236", "SRC-0027514"]:
        with np.load(paths[sid], allow_pickle=False) as z:
            arrays[sid] = {k: z[k] for k in z.files}
        for key, a in arrays[sid].items():
            check(
                sid + ":finite:" + key, np.issubdtype(a.dtype, np.number) and np.isfinite(a).all()
            )
            array_audit.append(
                dict(source_id=sid, key=key, shape=list(a.shape), dtype=str(a.dtype))
            )
    check("array_count_77", len(array_audit) == 77)
    predictions, evaluation, validation = (
        arrays[s] for s in ["SRC-0030211", "SRC-0030236", "SRC-0027514"]
    )
    for label, bundle in [
        ("predictions", predictions),
        ("evaluation", evaluation),
        ("validation", validation),
    ]:
        equal(label + ":cell_ids", IDS, bundle["cell_ids"].tolist(), atol=0)
    y = predictions["y"].astype(np.float64)
    vy = validation["validation_y"].astype(np.float64)
    train = validation["train_y"].astype(np.float64)
    threshold = evaluation["peak_threshold"].astype(np.float64)
    check(
        "target_shapes", y.shape == (16, 480) and vy.shape == (16, 168) and train.shape == (16, 672)
    )
    check("evaluation_targets", np.array_equal(y, evaluation["test_y"]))
    check("development_times", np.array_equal(evaluation["test_times"], np.arange(1008, 1488)))
    check(
        "scales_equal_positive",
        np.array_equal(predictions["scales"], evaluation["scales"])
        and np.all(predictions["scales"] > 0),
    )
    equal("result_ids", IDS, result["cell_ids"], atol=0)
    equal("result_threshold", threshold.tolist(), result["peak_threshold"], atol=0)
    # 672개 train target의 95% linear quantile. 저장 임계값은 float32다.
    position = Fraction(95, 100) * (train.shape[1] - 1)
    left = math.floor(position)
    fraction = float(position - left)
    ordered_train = np.sort(train, axis=1)
    calculated_threshold = (
        ordered_train[:, left] * (1 - fraction) + ordered_train[:, left + 1] * fraction
    )
    equal("training_threshold", calculated_threshold.tolist(), threshold.tolist(), atol=1e-6)
    check("methods_exact", set(predictions) - {"y", "cell_ids", "scales"} == set(METHODS))
    pred = {k: predictions[k].astype(np.float64) for k in METHODS}
    check("prediction_shapes", all(v.shape == (16, 480) for v in pred.values()))

    fits = data("SRC-0030237")
    check("29_saved_fits", len(fits) == 29)
    vpred = {k: np.zeros((16, 168), dtype=np.float64) for k in METHODS}
    cover = {k: np.zeros(16, dtype=np.int64) for k in METHODS}
    for row in fits:
        key = f"{row['method']}_{row['seed']}"
        members = row["members"]
        block = validation[f"{key}_cluster{row['cluster']}_validation_prediction"]
        check(
            f"fit_members:{key}:{row['cluster']}",
            len(set(members)) == len(members)
            and all(0 <= i < 16 for i in members)
            and block.shape == (len(members), 168),
        )
        vpred[key][members] = block
        cover[key][members] += 1
    check("validation_each_cell_once", all(np.all(v == 1) for v in cover.values()))
    for row in data("SRC-0027517")["aggregates"]:
        key = f"{row['method']}_{row['seed']}"
        equal(
            "validation_mae:" + key,
            float(np.abs(vpred[key] - vy).mean()),
            row["validation_mae"],
            atol=1e-6,
        )

    offsets = {}
    for key in METHODS:
        for tau in TAUS:
            offsets[f"{key}_pooled_tau{tau}"] = dict(
                source=key,
                type="pooled_validation_residual_quantile",
                tau=tau,
                offset=order_statistic(vy - vpred[key], tau),
                parameters=1,
            )
    for tau in TAUS:
        offsets[f"{GLOBAL}_cell_tau{tau}"] = dict(
            source=GLOBAL,
            type="per_cell_validation_residual_quantile",
            tau=tau,
            offset=[order_statistic(a, tau) for a in vy - vpred[GLOBAL]],
            parameters=16,
        )
    for key in TAB:
        offsets[f"{GLOBAL}_bias_matched_{key}"] = dict(
            source=GLOBAL,
            type="mean_height_match_to_Tab_validation",
            tau=None,
            offset=float((vpred[key] - vpred[GLOBAL]).sum() / vy.size),
            parameters=1,
        )
    equal("98_frozen_offsets", offsets, frozen["offsets"], atol=0)
    check(
        "38_conditions_98_scalars",
        len(offsets) == 38 and sum(v["parameters"] for v in offsets.values()) == 98,
    )
    check(
        "frozen_scope_flags",
        frozen["confirmation_targets_not_used"] is True
        and frozen["RCTL_results_not_used_for_clustering"] is True,
    )

    originals, calibrated, shifts, comparisons = [], [], [], []
    original_by, calibrated_by = {}, {}
    detailed_keys = {
        "cell_mae",
        "cell_under",
        "cell_over",
        "cell_peak_counts",
        "cell_peak_mae",
        "peak_under_amount",
        "peak_over_amount",
    }
    for period, sl in PERIODS.items():
        for method in METHODS:
            value = dict(
                period=period, method=method, **metrics(pred[method][:, sl], y[:, sl], threshold)
            )
            originals.append(value)
            original_by[period, method] = value
            equal(
                f"identity_UO:{period}:{method}",
                value["mae"],
                value["under_amount"] + value["over_amount"],
            )
            equal(
                f"identity_bias:{period}:{method}",
                value["bias"],
                value["over_amount"] - value["under_amount"],
            )
            equal(
                f"identity_contributions:{period}:{method}",
                value["mae"],
                value["peak_loss_contribution"] + value["nonpeak_loss_contribution"],
            )
        for method, meta in offsets.items():
            shift = np.asarray(meta["offset"], dtype=np.float64)
            adjusted = pred[meta["source"]] + (shift[:, None] if shift.ndim else shift)
            m = {
                k: v
                for k, v in metrics(adjusted[:, sl], y[:, sl], threshold).items()
                if k not in detailed_keys
            }
            if meta["tau"] is not None:
                m["target_tau_pinball"] = m["pinball"][str(meta["tau"])]
            value = dict(period=period, method=method, **meta, **m)
            calibrated.append(value)
            calibrated_by[period, method] = value
        for method in TAB:
            shift = (pred[method] - pred[GLOBAL])[:, sl]
            mask = y[:, sl] > threshold[:, None]
            a, g = original_by[period, method], original_by[period, GLOBAL]
            improved = [
                cell
                for cell, x, b in zip(IDS, a["cell_peak_mae"], g["cell_peak_mae"], strict=True)
                if x is not None and b is not None and x < b
            ]
            shifts.append(
                dict(
                    period=period,
                    method=method,
                    mean_prediction_shift=float(shift.mean()),
                    mean_shift_on_peak=float(shift[mask].mean()),
                    mean_shift_on_nonpeak=float(shift[~mask].mean()),
                    peak_improved_cell_ids=improved,
                    peak_macro_delta=a["peak_macro_mae"] - g["peak_macro_mae"],
                    total_mae_delta=a["mae"] - g["mae"],
                    all_time_under_delta=a["under_amount"] - g["under_amount"],
                    all_time_over_delta=a["over_amount"] - g["over_amount"],
                    global_no_worse_for_all_nonnegative_linear_costs=g["under_amount"]
                    <= a["under_amount"]
                    and g["over_amount"] <= a["over_amount"],
                )
            )
        for tau in TAUS:
            for method in TAB:
                a = calibrated_by[period, f"{method}_pooled_tau{tau}"]
                for kind in ["pooled", "cell"]:
                    g = calibrated_by[period, f"{GLOBAL}_{kind}_tau{tau}"]
                    comparisons.append(
                        dict(
                            period=period,
                            tau=tau,
                            Tab_method=method,
                            global_offset=kind,
                            Tab_pinball=a["target_tau_pinball"],
                            global_pinball=g["target_tau_pinball"],
                            difference=a["target_tau_pinball"] - g["target_tau_pinball"],
                            Tab_peak_mae=a["peak_macro_mae"],
                            global_peak_mae=g["peak_macro_mae"],
                        )
                    )
    # 나열 순서 대신 유일한 조건 키로 모든 행과 필드를 대조한다.
    for label, rows, keys in [
        ("originals", originals, ["period", "method"]),
        ("calibrated", calibrated, ["period", "method"]),
        ("Tab_vs_global", shifts, ["period", "method"]),
        ("calibrated_comparisons", comparisons, ["period", "tau", "Tab_method", "global_offset"]),
    ]:
        expected = {str(tuple(x[k] for k in keys)): x for x in rows}
        actual = {str(tuple(x[k] for k in keys)): x for x in result[label]}
        check(label + ":unique", len(rows) == len(expected) and len(result[label]) == len(actual))
        equal(label, expected, actual)
    for row in data("SRC-0030280")["metrics"]:
        key = f"{row['method']}_{row['seed']}"
        value = original_by["all", key]
        for computed, saved in [
            ("mae", "mean_scaled_mae"),
            ("peak_macro_mae", "peak_mean_scaled_mae"),
            ("cell_mae", "per_cell_mae"),
            ("cell_peak_mae", "peak_per_cell_mae"),
        ]:
            equal("old_metric:" + key + ":" + computed, value[computed], row[saved], atol=1e-6)
        equal("old_peak_counts:" + key, value["cell_peak_counts"], row["peak_query_counts"], atol=0)

    toy = []
    for prediction in [Fraction(0), Fraction(10)]:
        terms = [(Fraction(0), Fraction(9, 10)), (Fraction(10), Fraction(1, 10))]
        u = sum(weight * max(actual - prediction, 0) for actual, weight in terms)
        o = sum(weight * max(prediction - actual, 0) for actual, weight in terms)
        toy.append(
            dict(
                prediction=str(prediction),
                mae=str(u + o),
                peak_only_mae=str(abs(prediction - 10)),
                under=str(u),
                over=str(o),
            )
        )
    equal("exact_toy", toy, result["exact_toy"])
    equal("toy_cost_ratio", str(Fraction(9)), result["toy_equal_linear_cost_ratio"])
    before, after, receipt, finished = (
        data(s) for s in ["SRC-0029494", "SRC-0029493", "SRC-0029495", "SRC-0029498"]
    )
    expected_after = copy.deepcopy(before)
    check(
        "no_previous_peak_charge",
        "peak_diagnostic_70" not in before["new_cheap_diagnostic_seconds"],
    )
    expected_after["new_cheap_diagnostic_seconds"]["peak_diagnostic_70"] = result[
        "numeric_wall_seconds"
    ]
    equal("ledger_only_one_added_item", expected_after, after, atol=0)
    cheap = sum(after["new_cheap_diagnostic_seconds"].values())
    total = cheap + sum(
        after["used"][k]
        for k in [
            "TabICL_fit_predict_seconds",
            "RCTL_wall_seconds",
            "RCTL_frozen_inference_seconds",
        ]
    )
    equal("cheap_total", cheap, receipt["cheap_total_seconds"])
    equal("modeling_total", total, receipt["recorded_modeling_total_seconds"])
    equal(
        "charged_numeric_seconds",
        result["numeric_wall_seconds"],
        receipt["new_cheap_seconds"],
        atol=0,
    )
    for when, sid in [("before", "SRC-0029494"), ("after", "SRC-0029493")]:
        equal(
            "receipt_hash:" + when,
            hashlib.sha256(paths[sid].read_bytes()).hexdigest(),
            receipt[when + "_sha256"],
        )
    check(
        "unchanged_model_counts",
        after["used"]["TabICL_contexts"] == 65
        and after["used"]["TabICL_query_rows"] == 38016
        and after["used"]["RCTL_fits"] == 29,
    )
    check(
        "recorded_completion_and_caps",
        result["complete"] is True
        and finished["complete"] is True
        and finished["error"] is None
        and 0
        < result["numeric_wall_seconds"]
        < finished["elapsed_seconds"]
        < settings["wall_cap_seconds"]
        and 0 < result["observed_rss_bytes"] < settings["rss_cap_bytes"],
    )
    check(
        "recorded_scope_flags",
        result["original_metrics_reproduced"] is True
        and result["inputs_unchanged"] is True
        and result["new_objective_selected"] is False
        and result["new_partition_selected"] is False,
    )
    check(
        "input_files_still_identical",
        all(
            hashlib.sha256(paths[s].read_bytes()).hexdigest() == settings["input_sha256"][k]
            for k, s in input_map.items()
        ),
    )
    return dict(
        batch_id="history-066",
        success=not errors,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks=len(checks),
        numeric_leaves_compared=numeric_leaves,
        errors=errors,
        max_abs_error_including_float32_reference_metrics=max_abs_error,
        tolerances=dict(
            saved_diagnostic=1e-12, offsets=0, older_float32_metrics_and_threshold=1e-6
        ),
        check_names=checks,
        input_sha256=settings["input_sha256"],
        arrays=array_audit,
        validation_blocks=29,
        original_rows=24,
        calibrated_rows=114,
        shift_rows=6,
        comparison_rows=48,
        scalar_offsets=98,
        offset_conditions=38,
        exact_toy=toy,
        peak_periods=[
            dict(
                period=period,
                query_count=original_by[period, GLOBAL]["peak_query_count"],
                cells=original_by[period, GLOBAL]["cells_with_peak"],
                total_queries=y[:, sl].size,
            )
            for period, sl in PERIODS.items()
        ],
        Tab_pinball_improvement_exceptions=[x for x in comparisons if x["difference"] < 0],
        cost=dict(
            numeric_wall_seconds=result["numeric_wall_seconds"],
            finished_elapsed_seconds=finished["elapsed_seconds"],
            observed_rss_bytes=result["observed_rss_bytes"],
            cheap_total_seconds=cheap,
            recorded_modeling_total_seconds=total,
        ),
        new_model_runs=0,
        original_scripts_executed=False,
        random_draws=0,
        independent_model_reproduction=False,
        scope="저장 예측의 재집계이며 모델·원코드 실행이나 독립 재현이 아니다.",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {k: result[k] for k in ["success", "checks", "numeric_leaves_compared", "errors"]}
        )
    )
    raise SystemExit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
