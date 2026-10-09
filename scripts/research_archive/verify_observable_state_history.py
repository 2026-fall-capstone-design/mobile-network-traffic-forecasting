"""관측 상태 진단의 저장 결과만 검산한다. 모델·과거 코드를 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path

import numpy as np


def verify(manifest_path: Path) -> dict:
    """상태 경계, 저장 예측, 집계와 비용 근거를 대조한다."""
    manifest_path = manifest_path.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks, raw = [], {}

    def check(name, condition):
        """조건을 확인하고 통과한 검사 이름을 기록한다."""
        if not condition:
            raise ValueError(name)
        checks.append(name)

    def same(name, a, b, atol=1e-12):
        """모양·유한성을 확인한 뒤 수치가 허용 오차 안에서 같은지 대조한다."""
        aa, bb = np.asarray(a), np.asarray(b)
        check(
            name,
            aa.shape == bb.shape
            and aa.dtype.kind in "iuf"
            and bb.dtype.kind in "iuf"
            and np.isfinite(aa).all()
            and np.isfinite(bb).all()
            and np.allclose(aa, bb, rtol=1e-12, atol=atol),
        )

    def scalar(name, got, want):
        """빈 상태의 null과 실제 수치를 구분하여 저장된 스칼라를 검사한다."""
        if want is None:
            check(name, got is None)
        else:
            check(name + ":type", type(got) in (int, float))
            same(name, got, want)

    def arrays(sid):
        """해시를 확인한 NPZ 바이트를 pickle 없이 읽고 파일 핸들을 닫는다."""
        with np.load(io.BytesIO(raw[sid]), allow_pickle=False) as bank:
            return {k: bank[k] for k in bank.files}

    required = {
        "SRC-0021210",
        "SRC-0021235",
        "SRC-0022935",
        "SRC-0029142",
        "SRC-0029143",
        "SRC-0029144",
        "SRC-0029145",
        "SRC-0029146",
        "SRC-0030211",
        "SRC-0021188",
    }
    rows = manifest["sources"]
    check(
        "10_unique_source_ids",
        len(rows) == len({r["source_id"] for r in rows}) == 10
        and {r["source_id"] for r in rows} == required
        and len({r["path"] for r in rows}) == 10,
    )
    for row in rows:
        sid = row["source_id"]
        path = (manifest_path.parent / row["archive_path"]).resolve()
        check(sid + ":bounded_path", path.is_relative_to(manifest_path.parents[2]))
        value = path.read_bytes()
        check(sid + ":size", type(row["size_bytes"]) is int and len(value) == row["size_bytes"])
        check(sid + ":sha256", hashlib.sha256(value).hexdigest() == row["sha256"])
        raw[sid] = value
    cfg, summary, start, finish = [
        json.loads(raw[sid]) for sid in ["SRC-0029145", "SRC-0029146", "SRC-0029144", "SRC-0029143"]
    ]
    saved, previous = arrays("SRC-0029142"), arrays("SRC-0030211")
    for key, sid in [
        ("plan_sha256", "SRC-0021210"),
        ("code_sha256", "SRC-0022935"),
        ("predictions_sha256", "SRC-0030211"),
    ]:
        check(key, cfg[key] == hashlib.sha256(raw[sid]).hexdigest())
    check("summary_settings", summary["settings"] == cfg)
    check(
        "train_and_development_split",
        cfg["train_targets"] == [168, 839]
        and cfg["diagnostic_targets"] == [1008, 1487]
        and cfg["independent_test"] is False,
    )
    check("quantiles", cfg["level_quantiles"] == [0.1, 0.9])
    for key, want in [
        ("new_RCTL_fits", 0),
        ("new_RCTL_forward", 0),
        ("new_TabICL_contexts", 0),
        ("simple_fits_planned", 2),
        ("wall_cap_seconds", 60),
        ("ram_cap_bytes", 2 * 1024**3),
    ]:
        check(key, type(cfg[key]) is int and cfg[key] == want)
    check("completed_without_error", finish["complete"] is True and finish["error"] is None)
    check(
        "reported_no_partition_change",
        summary["partitions_changed"] is False and summary["new_clustering_recommended"] is False,
    )
    for key in ["new_RCTL_fits", "new_TabICL_contexts"]:
        check("finish:" + key, type(finish[key]) is int and finish[key] == 0)
    check(
        "start_pid_time",
        type(start["pid"]) is int
        and start["pid"] > 0
        and type(start["unix"]) in (int, float)
        and np.isfinite(start["unix"])
        and start["unix"] > 0,
    )
    check(
        "two_fit_reports",
        finish["simple_fits"] == summary["simple_fits"]
        and [r["name"] for r in summary["simple_fits"]] == ["global_Ridge", "global_HGB"],
    )
    for row in summary["simple_fits"]:
        check(
            row["name"] + ":fit_time",
            type(row["seconds"]) in (int, float)
            and np.isfinite(row["seconds"])
            and 0 < row["seconds"] < summary["elapsed_seconds"],
        )
    check(
        "nested_finite_timers",
        all(
            type(v) in (int, float) and np.isfinite(v)
            for v in [summary["elapsed_seconds"], finish["elapsed_seconds"]]
        )
        and 0
        < sum(r["seconds"] for r in summary["simple_fits"])
        < summary["elapsed_seconds"]
        <= finish["elapsed_seconds"]
        < cfg["wall_cap_seconds"],
    )
    check(
        "sampled_RSS",
        type(summary["peak_rss_bytes"]) is int
        and summary["peak_rss_bytes"] == finish["peak_rss_bytes"]
        and 0 < summary["peak_rss_bytes"] < cfg["ram_cap_bytes"],
    )

    methods = [
        "empirical_risk_20260925",
        "empirical_risk_20260926",
        "global_20260925",
        "knn_risk_20260925",
        "pcc_balanced_20260925",
        "random_balanced_20260925",
        "tabicl_risk_20260925",
        "tabicl_risk_20260926",
        "persistence",
        "daily_naive",
        "weekly_naive",
        "global_Ridge",
        "global_HGB",
    ]
    metadata = [
        "y",
        "cell_ids",
        "scales",
        "threshold",
        "states",
        "train_summaries",
        "test_summaries",
        "times",
    ]
    check("21_array_fields", set(saved) == set(methods + metadata))
    check(
        "11_original_array_fields", set(previous) == set(methods[:8] + ["y", "cell_ids", "scales"])
    )
    ids = saved["cell_ids"]
    check(
        "integer_ids_times_states",
        all(np.issubdtype(saved[k].dtype, np.integer) for k in ["cell_ids", "times", "states"]),
    )
    expected_ids = [
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
    check("fixed_ids", ids.tolist() == summary["cell_ids"] == expected_ids)
    check("fixed_times", np.array_equal(saved["times"], np.arange(1008, 1488)))
    for name in methods + ["y"]:
        check(
            name + ":prediction_shape_finite",
            saved[name].shape == (16, 480)
            and saved[name].dtype == np.float64
            and np.isfinite(saved[name]).all(),
        )
    check(
        "positive_scales",
        saved["scales"].shape == (16,)
        and saved["scales"].dtype == np.float64
        and np.isfinite(saved["scales"]).all()
        and (saved["scales"] > 0).all(),
    )
    for name in methods[:8] + ["y", "cell_ids", "scales"]:
        check(name + ":unchanged_stored_values", np.array_equal(saved[name], previous[name]))
    for key, shape in [
        ("train_summaries", (3, 16, 672)),
        ("test_summaries", (3, 16, 480)),
        ("threshold", (3, 16, 2)),
    ]:
        check(
            key + ":shape_finite",
            saved[key].shape == shape
            and saved[key].dtype == np.float64
            and np.isfinite(saved[key]).all(),
        )
    # Reconstruct NumPy's default linear quantile using sorted ranks.
    sorted_train = np.sort(saved["train_summaries"], axis=-1)
    cuts = []
    for q in [0.1, 0.9]:
        rank = q * 671
        lo, hi = int(np.floor(rank)), int(np.ceil(rank))
        cuts.append(
            sorted_train[:, :, lo] + (sorted_train[:, :, hi] - sorted_train[:, :, lo]) * (rank - lo)
        )
    cuts = np.stack(cuts, axis=-1)
    same("TRAIN_only_linear_quantiles", saved["threshold"], cuts)
    same("summary_thresholds", summary["thresholds"], saved["threshold"])
    check("ordered_cutpoints", (saved["threshold"][:, :, 0] <= saved["threshold"][:, :, 1]).all())
    # Use the recorded cutpoints for exact floating-point boundary membership.
    low, high = saved["threshold"][:, :, 0, None], saved["threshold"][:, :, 1, None]
    recent = saved["test_summaries"]
    states = 1 + (recent > high).astype(int) - (recent <= low).astype(int)
    check(
        "stored_states",
        saved["states"].shape == (3, 16, 480) and np.array_equal(states, saved["states"]),
    )
    check("persistence_is_recent_level", np.array_equal(saved["persistence"], recent[0]))
    families = ["recent_level", "recent_change", "daily_deviation"]
    labels = ["low", "middle", "high"]
    masks = {"all": np.ones((16, 480), dtype=bool)}
    for j, family in enumerate(families):
        for index, label in enumerate(labels):
            masks[f"{family}:{label}"] = states[j] == index
    for i, a in enumerate(labels):
        for j, b in enumerate(labels):
            masks[f"level_change:{a}_{b}"] = (states[0] == i) & (states[1] == j)
    groups = summary["metrics"]
    check(
        "19_complete_unique_states",
        len(groups) == len({g["state"] for g in groups}) == 19
        and {g["state"] for g in groups} == set(masks),
    )
    truth = saved["y"]
    errors = {name: np.abs(saved[name] - truth) for name in methods}
    baseline = errors["global_20260925"]
    result = []
    for group in groups:
        name, mask = group["state"], masks[group["state"]]
        counts, n = mask.sum(axis=1), int(mask.sum())
        # Count maximal contiguous true runs separately within each cell.
        episodes = [
            int(np.count_nonzero(np.diff(np.r_[0, row.astype(int), 0]) == 1)) for row in mask
        ]
        for key, want in [
            ("total_rows", n),
            ("time_instants_with_any_cell", int(np.count_nonzero(mask.any(axis=0)))),
            ("cells_with_any_rows", int(np.count_nonzero(counts))),
            ("cells_with_at_least_10_rows", int(np.count_nonzero(counts >= 10))),
        ]:
            check(name + ":" + key, type(group[key]) is int and group[key] == want)
        check(name + ":rows_by_cell", group["rows_by_cell"] == counts.tolist())
        check(name + ":episodes_by_cell", group["episodes_by_cell"] == episodes)
        method_rows = group["methods"]
        check(
            name + ":13_unique_methods",
            len(method_rows) == len({m["method"] for m in method_rows}) == 13
            and {m["method"] for m in method_rows} == set(methods),
        )
        out = dict(
            state=name,
            total_rows=n,
            rows_by_cell=counts.tolist(),
            time_instants_with_any_cell=group["time_instants_with_any_cell"],
            episodes_by_cell=episodes,
            methods=[],
        )
        for row in method_rows:
            method = row["method"]
            err = errors[method]
            delta = err - baseline
            tag = name + ":" + method
            vals = [float(err[i, mask[i]].mean()) if counts[i] else None for i in range(16)]
            check(tag + ":16_cell_values", len(row["per_cell_conditional_mae"]) == 16)
            for i, want in enumerate(vals):
                scalar(tag + f":cell{i}", row["per_cell_conditional_mae"][i], want)
            expected = dict(
                conditional_micro_mae=float(err[mask].mean()) if n else None,
                conditional_macro_mae=float(np.mean([v for v in vals if v is not None]))
                if n
                else None,
                mean_underprediction=float(np.maximum(truth[mask] - saved[method][mask], 0).mean())
                if n
                else None,
                mean_overprediction=float(np.maximum(saved[method][mask] - truth[mask], 0).mean())
                if n
                else None,
                contribution_to_overall_mae=float(err[mask].sum() / 7680),
                contribution_delta_vs_global=float(delta[mask].sum() / 7680),
                conditional_delta_vs_global=float(delta[mask].mean()) if n else None,
            )
            for key, want in expected.items():
                scalar(tag + ":" + key, row[key], want)
            halves = []
            for section in [slice(0, 240), slice(240, 480)]:
                take = mask[:, section]
                values = delta[:, section]
                halves.append(float(values[take].mean()) if take.any() else None)
            check(tag + ":two_halves", len(row["conditional_delta_halves_vs_global"]) == 2)
            for j, want in enumerate(halves):
                scalar(tag + f":half{j}", row["conditional_delta_halves_vs_global"][j], want)
            cell_delta = [float(delta[i, mask[i]].mean()) if counts[i] else None for i in range(16)]
            improved = [int(ids[i]) for i, v in enumerate(cell_delta) if v is not None and v < 0]
            harmed = [int(ids[i]) for i, v in enumerate(cell_delta) if v is not None and v > 0]
            check(
                tag + ":improved_cells",
                type(row["cells_with_lower_conditional_mae"]) is int
                and row["cells_with_lower_conditional_mae"] == len(improved),
            )
            check(
                tag + ":both_halves_flag",
                type(row["lower_mae_in_each_half"]) is bool
                and row["lower_mae_in_each_half"] == all(v is not None and v < 0 for v in halves),
            )
            if n:
                same(
                    tag + ":under_over_identity",
                    expected["mean_underprediction"] + expected["mean_overprediction"],
                    expected["conditional_micro_mae"],
                )
                same(
                    tag + ":frequency_weighted_contribution",
                    n / 7680 * expected["conditional_delta_vs_global"],
                    row["contribution_delta_vs_global"],
                )
            out["methods"].append(
                dict(
                    method=method,
                    **expected,
                    halves=halves,
                    per_cell_mae=vals,
                    per_cell_delta=cell_delta,
                    better_cell_ids=improved,
                    worse_cell_ids=harmed,
                )
            )
        result.append(out)
    for method in methods:
        for family in families + ["level_change"]:
            chosen = [r for r in result if r["state"].startswith(family + ":")]
            check(
                method + ":" + family + ":partition_count",
                sum(r["total_rows"] for r in chosen) == 7680,
            )
            total = sum(
                next(v for v in r["methods"] if v["method"] == method)[
                    "contribution_to_overall_mae"
                ]
                for r in chosen
            )
            same(method + ":" + family + ":loss_decomposition", total, errors[method].mean())
    return dict(
        success=True,
        checks=len(checks),
        check_names=checks,
        cell_ids=ids.tolist(),
        methods=methods,
        states=result,
        summary_method_rows=19 * 13,
        train_summary_shape=list(saved["train_summaries"].shape),
        threshold_ties=[
            dict(
                family=family,
                at_low=int(np.count_nonzero(recent[j] == low[j])),
                at_high=int(np.count_nonzero(recent[j] == high[j])),
            )
            for j, family in enumerate(families)
        ],
        negative_predictions={m: int(np.count_nonzero(saved[m] < 0)) for m in methods},
        summary_elapsed_seconds=summary["elapsed_seconds"],
        finish_elapsed_seconds=finish["elapsed_seconds"],
        simple_fit_predict_times=summary["simple_fits"],
        peak_sampled_RSS_bytes=summary["peak_rss_bytes"],
        original_model_fits_reported=2,
        new_model_runs=0,
        original_scripts_executed=False,
        reused_RCTL_predictions_exact=True,
        actual_feature_matrix_saved=False,
        scope=(
            "보존 바이트·TRAIN 요약 기반 경계·19상태/13방법 저장 산술. "
            "실제 H5/과거 모델 적합은 이 검사 밖이다."
        ),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = verify(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {k: report[k] for k in ["success", "checks", "summary_method_rows", "new_model_runs"]}
        )
    )
