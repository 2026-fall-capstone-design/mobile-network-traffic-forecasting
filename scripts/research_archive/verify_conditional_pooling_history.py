"""보존된 조건부 공유 비용·입력·예측의 산술을 검사하며 모델을 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import pickletools
import re
import zipfile
from datetime import datetime
from pathlib import Path

import numpy as np


def verify(manifest_path: Path) -> dict:
    """저장 결과의 식별·집계·순위·입력과 Tab 혼합 예측 최적성을 대조한다."""
    manifest_path = manifest_path.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks = []
    raw_by_id = {}

    def check(name, condition):
        """실패한 근거 항목의 이름을 남기고 잘못된 자료를 거부한다."""
        if not condition:
            raise ValueError(name)
        checks.append(name)

    def same(name, a, b, atol=1e-12):
        """비유한 값을 거부하며 저장 수치와 재집계 값을 대조한다."""
        check(
            name,
            bool(
                np.isfinite(a).all()
                and np.isfinite(b).all()
                and np.allclose(a, b, rtol=1e-11, atol=atol)
            ),
        )

    def get(sid):
        """해시를 검사한 원본 바이트만 반환한다."""
        return raw_by_id[sid]

    def npz(sid):
        """객체 역직렬화를 금지하고 보존된 수치 배열만 읽는다."""
        return np.load(io.BytesIO(get(sid)), allow_pickle=False)

    def rank(values):
        """동점에는 평균 순위를 부여해 저장된 순위 상관을 검산한다."""
        values = np.asarray(values)
        order = np.argsort(values, kind="stable")
        result = np.zeros(len(values))
        for value in np.unique(values):
            positions = np.flatnonzero(values[order] == value)
            result[order[positions]] = positions.mean() + 1
        return result

    def spearman(a, b):
        """순위의 상관만 계산하며 유의성 검정으로 해석하지 않는다."""
        return float(np.corrcoef(rank(a), rank(b))[0, 1])

    def date_literals(raw):
        """객체 배열을 역직렬화하지 않고 보존된 시각 문자열 리터럴만 읽는다."""
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            stream = io.BytesIO(archive.read("dates.npy"))
        check("dates_header_version", np.lib.format.read_magic(stream) == (1, 0))
        shape, fortran, dtype = np.lib.format.read_array_header_1_0(stream)
        check("dates_header_shape", shape == (1008,) and not fortran and dtype.hasobject)
        literals = [
            arg
            for op, arg, _pos in pickletools.genops(stream.read())
            if op.name in {"UNICODE", "BINUNICODE", "SHORT_BINUNICODE", "BINUNICODE8"}
            and isinstance(arg, str)
            and re.fullmatch(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}", arg)
        ]
        check("dates_literal_count", len(literals) == len(set(literals)) == 1008)
        parsed = [datetime.fromisoformat(value) for value in literals]
        check(
            "dates_hourly_order",
            all(
                (b - a).total_seconds() == 3600
                for a, b in zip(parsed[:-1], parsed[1:], strict=True)
            ),
        )
        return parsed

    expected_ids = {
        "SRC-0021137",
        "SRC-0021188",
        "SRC-0022693",
        "SRC-0025173",
        "SRC-0025174",
        "SRC-0025175",
        "SRC-0025176",
        "SRC-0025177",
        "SRC-0025178",
        "SRC-0022703",
        "SRC-0023577",
        "SRC-0023116",
        "SRC-0023605",
        "SRC-0030238",
        "SRC-0030280",
    }
    check(
        "15_unique_sources",
        len(manifest["sources"]) == 15
        and {r["source_id"] for r in manifest["sources"]} == expected_ids,
    )
    for row in manifest["sources"]:
        sid = row["source_id"]
        path = (manifest_path.parent / row["archive_path"]).resolve()
        check(sid + ":inside_archive", path.is_relative_to(manifest_path.parents[2]))
        raw = path.read_bytes()
        check(sid + ":size", type(row["size_bytes"]) is int and len(raw) == row["size_bytes"])
        check(sid + ":sha256", hashlib.sha256(raw).hexdigest() == row["sha256"])
        raw_by_id[sid] = raw

    started, scores, summary = [
        json.loads(get(sid)) for sid in ["SRC-0025176", "SRC-0025177", "SRC-0025178"]
    ]
    fix, finished = [json.loads(get(sid)) for sid in ["SRC-0025174", "SRC-0025175"]]
    check("settings_copies", started == scores["settings"] == summary["settings"])
    check("score_rows_copied", scores["records"] == summary["records"])
    check(
        "frozen_score_hash",
        summary["frozen_score_sha256"] == hashlib.sha256(get("SRC-0025177")).hexdigest(),
    )
    check("plan_identity", started["plan_sha256"] == hashlib.sha256(get("SRC-0021137")).hexdigest())
    check(
        "revised_code_identity",
        fix["code_sha256"] == hashlib.sha256(get("SRC-0022693")).hexdigest(),
    )
    prediction_raw = get("SRC-0023605")
    check(
        "saved_B1_prediction_identity",
        hashlib.sha256(prediction_raw).hexdigest() == started["saved_predictions_sha256"],
    )
    prediction = npz("SRC-0023605")
    check("context_504", started["context_times"] == list(range(168, 672)))
    check(
        "B1_context_query_ids",
        started["query_times"] == prediction["query_times"].tolist()
        and started["context_times"] == prediction["context_times"].tolist()
        and started["cell_ids"] == prediction["cell_ids"].tolist(),
    )
    check(
        "query_64_after_context",
        len(started["query_times"]) == 64
        and len(set(started["query_times"])) == 64
        and min(started["query_times"]) > max(started["context_times"]),
    )
    check(
        "density_settings",
        (
            started["density_k_primary"],
            started["density_k_sensitivity"],
            started["distribution_KNN_k"],
        )
        == (32, [16, 64], 32),
    )
    check(
        "known_development_scope",
        started["retrospective_development_only"] is True
        and started["RCTL_outcomes_previously_observed"] is True
        and started["RCTL_used_to_change_score_or_partition"] is False,
    )
    check(
        "no_new_models_reported",
        all(
            type(value) is int and value == 0
            for value in [
                started["new_TabICL_contexts"],
                started["new_RCTL_fits"],
                summary["new_TabICL_contexts"],
                summary["new_RCTL_fits"],
                finished["new_model_calls"],
                fix["new_model_calls_before_failure"],
            ]
        ),
    )
    check(
        "no_new_partition_validation",
        summary["new_partition_RCTL_validation"] is False
        and summary["novelty_established"] is False,
    )
    check(
        "reported_failure_marker",
        type(fix["prior_exec_exit_code"]) is int
        and fix["prior_exec_exit_code"] == 1
        and fix["plan_unchanged"] is True,
    )
    check(
        "reported_time_types",
        all(
            type(value) in (int, float) and np.isfinite(value) and value > 0
            for value in [
                summary["elapsed_seconds"],
                finished["elapsed_seconds"],
                summary["failed_attempt_seconds_included"],
                fix["prior_command_wall_seconds_charged"],
            ]
        ),
    )
    same("elapsed_copies", summary["elapsed_seconds"], finished["elapsed_seconds"])
    same(
        "failed_elapsed_copies",
        summary["failed_attempt_seconds_included"],
        fix["prior_command_wall_seconds_charged"],
    )
    check(
        "positive_resumed_time",
        summary["elapsed_seconds"] > summary["failed_attempt_seconds_included"] > 0,
    )
    check(
        "historical_caps",
        type(summary["peak_sampled_RSS_bytes"]) is int
        and 0 < summary["peak_sampled_RSS_bytes"]
        and summary["elapsed_seconds"] < started["cheap_wall_cap_seconds"]
        and summary["peak_sampled_RSS_bytes"] < started["RSS_cap_bytes"],
    )
    toy_expected = {
        "disjoint_support": [0, 0],
        "same_input_different_target": [1],
        "same_median_different_spread": [0],
    }
    check("three_toy_cases", set(summary["toy_checks"]) == set(toy_expected))
    for name, value in toy_expected.items():
        same(name + ":stored_toy_cost", summary["toy_checks"][name]["cost"], value)
        same(
            name + ":stored_shift_invariance",
            summary["toy_checks"][name]["input_dependent_shift_error"],
            0,
        )

    get("SRC-0025173")
    bank = npz("SRC-0025173")
    actual, ids, times = bank["actual"], bank["cell_ids"], bank["query_times"]
    check(
        "ids_and_times",
        ids.tolist() == started["cell_ids"] and times.tolist() == started["query_times"],
    )
    check("actual_shape_finite", actual.shape == (1024,) and np.isfinite(actual).all())
    owner = np.repeat(np.arange(16), 64)
    expected = {"actual", "cell_ids", "query_times"} | {f"density_k{k}" for k in [16, 32, 64]}
    for k in [16, 32, 64]:
        density = bank[f"density_k{k}"]
        check(
            f"density{k}:shape_finite", density.shape == (16, 1024) and np.isfinite(density).all()
        )
        check(f"density{k}:range", (density >= 0).all() and (density <= 1).all())
        same(f"density{k}:sum", density.sum(0), np.ones(1024))
        same(f"density{k}:frequency_grid", density * k, np.round(density * k))
        same(
            f"density{k}:owner_zero",
            float((density[owner, np.arange(1024)] == 0).mean()),
            summary["query_owner_zero_probability"][str(k)],
        )
    estimators = ["TabICL_distribution", "TabICL_median_only", "empirical_KNN_distribution"]
    partitions = started["partitions"]
    check(
        "six_fixed_partitions",
        set(partitions)
        == {
            "global",
            "tabicl_risk",
            "empirical_risk",
            "knn_risk",
            "pcc_balanced",
            "random_balanced",
        },
    )
    for name, groups in partitions.items():
        check(
            name + ":partition",
            sorted(i for g in groups for i in g) == list(range(16))
            and len(groups) == (1 if name == "global" else 4),
        )
    rows = summary["records"]
    check(
        "54_unique_rows",
        len(rows) == 54
        and {(r["estimator"], r["density_k"], r["partition"]) for r in rows}
        == {(e, k, n) for e in estimators for k in [16, 32, 64] for n in partitions},
    )
    for row in rows:
        label = f"{row['estimator']}_k{row['density_k']}_{row['partition']}"
        cost, pred = bank[label + "_cost"], bank[label + "_prediction"]
        expected.update([label + "_cost", label + "_prediction"])
        check(
            label + ":arrays",
            cost.shape == pred.shape == (1024,)
            and np.isfinite(cost).all()
            and np.isfinite(pred).all()
            and (cost >= 0).all(),
        )
        same(label + ":cost", float(cost.mean()), row["mean_intrinsic_cost"])
        same(
            label + ":first_half",
            float(cost.reshape(16, 64)[:, :32].mean()),
            row["first_half_cost"],
        )
        same(
            label + ":second_half",
            float(cost.reshape(16, 64)[:, 32:].mean()),
            row["second_half_cost"],
        )
        same(
            label + ":query_MAE", float(np.abs(pred - actual).mean()), row["mixture_prediction_MAE"]
        )
        groups = partitions[row["partition"]]
        check(label + ":K", type(row["K"]) is int and row["K"] == len(groups))
        w = bank[f"density_k{row['density_k']}"]
        fallback = sum(int((w[g].sum(0)[np.isin(owner, g)] == 0).sum()) for g in groups)
        check(
            label + ":fallback",
            type(row["zero_group_mass_fallback_queries"]) is int
            and fallback == row["zero_group_mass_fallback_queries"],
        )
    check("all_array_keys", set(bank.files) == expected and len(expected) == 114)

    raw = get("SRC-0030280")
    prior = json.loads(raw)
    rctl = {r["method"]: r["mean_scaled_mae"] for r in prior["metrics"] if r["seed"] == 20260925}
    check(
        "RCTL_six_primary_means",
        set(rctl) == set(partitions)
        and all(type(v) in (int, float) and np.isfinite(v) and v >= 0 for v in rctl.values()),
    )
    check(
        "nine_rank_comparisons",
        len(summary["retrospective_checks"]) == 9
        and {(r["estimator"], r["density_k"]) for r in summary["retrospective_checks"]}
        == {(e, k) for e in estimators for k in [16, 32, 64]},
    )
    for row in summary["retrospective_checks"]:
        selected = [
            r
            for r in rows
            if r["estimator"] == row["estimator"]
            and r["density_k"] == row["density_k"]
            and r["K"] == 4
        ]
        label = row["estimator"] + ":" + str(row["density_k"])
        check(label + ":five_partitions", row["partition_count"] == len(selected) == 5)
        observed = [rctl[r["partition"]] for r in selected]
        same(
            label + ":intrinsic_RCTL",
            spearman([r["mean_intrinsic_cost"] for r in selected], observed),
            row["intrinsic_vs_saved_RCTL_spearman"],
        )
        same(
            label + ":mixture_RCTL",
            spearman([r["mixture_prediction_MAE"] for r in selected], observed),
            row["mixture_MAE_vs_saved_RCTL_spearman"],
        )
        same(
            label + ":half_ranks",
            spearman(
                [r["first_half_cost"] for r in selected], [r["second_half_cost"] for r in selected]
            ),
            row["intrinsic_first_vs_second_half_spearman"],
        )
        check(
            label + ":rank_order",
            row["partition_order_by_intrinsic"]
            == [r["partition"] for r in sorted(selected, key=lambda r: r["mean_intrinsic_cost"])],
        )

    cfg = started
    pred = prediction
    design = npz("SRC-0023577")
    settings = json.loads(get("SRC-0030238"))
    sel, times = pred["selected_cells"], design["times"]
    check("fixed16_selection", sel.tolist() == [r * 8 + c for r in range(4) for c in [0, 2, 4, 7]])
    check(
        "cell_ids",
        bank["cell_ids"].tolist() == cfg["cell_ids"] == (design["cell_indices"][sel] + 1).tolist(),
    )
    same("scales_training_mean", design["scales"], design["raw"][:672].mean(axis=0))
    same(
        "normalized_Y", design["Y"], (design["raw"][times] / design["scales"]).T.astype(np.float32)
    )

    check("saved_X_shape", design["X"].shape == (32, 840, 16) and np.isfinite(design["X"]).all())
    z = (design["raw"] / design["scales"])[:, sel]
    saved_dates = date_literals(get("SRC-0023577"))
    dates = [saved_dates[t] for t in times]
    hours = np.array([d.hour for d in dates])
    weekdays = np.array([d.weekday() for d in dates])
    cal = np.column_stack(
        [
            np.sin(2 * np.pi * hours / 24),
            np.cos(2 * np.pi * hours / 24),
            np.sin(2 * np.pi * weekdays / 7),
            np.cos(2 * np.pi * weekdays / 7),
        ]
    )
    lag8 = np.stack([z[times - offset] for offset in range(8, 0, -1)], axis=2)
    daily_mean = np.stack([z[t - 24 : t].mean(0) for t in times])
    daily_std = np.stack([z[t - 24 : t].std(0) for t in times])
    features = (
        np.concatenate(
            [
                lag8,
                z[times - 24, :, None],
                z[times - 168, :, None],
                daily_mean[:, :, None],
                daily_std[:, :, None],
                np.repeat(cal[:, None, :], 16, axis=1),
            ],
            axis=2,
        )
        .transpose(1, 0, 2)
        .astype(np.float32)
    )
    feature_max_difference = float(np.max(np.abs(design["X"][sel] - features)))
    check(
        "saved_X_feature_identity",
        bool(np.allclose(design["X"][sel], features, rtol=1e-6, atol=1e-7)),
    )

    qi = np.searchsorted(times, bank["query_times"])
    same("actual_query_Y", bank["actual"], design["Y"][sel][:, qi].ravel(), atol=0)
    check(
        "query_rint_sampling",
        bank["query_times"].tolist() == np.rint(np.linspace(672, 839, 64)).astype(int).tolist(),
    )
    check("contexts_before_query", cfg["context_times"] == list(range(168, 672)))
    check(
        "query_inside_RCTL_training",
        min(bank["query_times"]) >= settings["train_targets"][0]
        and max(bank["query_times"]) <= settings["train_targets"][1],
    )
    parts = {}
    for method, seed, k, group in settings["tasks"]:
        if seed == settings["seed_primary"]:
            check(
                method + ":cluster_index:" + str(k),
                type(k) is int and k == len(parts.get(method, [])),
            )
            parts.setdefault(method, []).append(group)
    check("partitions_frozen_primary", parts == cfg["partitions"])
    check(
        "original_RCTL_periods",
        settings["train_targets"] == [168, 839]
        and settings["validation_targets"] == [840, 1007]
        and settings["test_targets"] == [1008, 1487],
    )
    owner = np.repeat(np.arange(16), 64)
    certified = []

    # 과거 코드는 중앙값을 고른 뒤 절대손실을 더했다. 여기서는 저장 atom 사이의
    # min(F, mass-F)를 적분해 같은 최솟값을 검사한다. 예측 모델은 생성하지 않는다.
    for estimator, atoms in [
        ("TabICL_distribution", pred["quantiles"][:, 64:].astype(float)),
        ("TabICL_median_only", pred["median"][:, 64:, None].astype(float)),
    ]:
        n, q, b = atoms.shape
        check(
            estimator + ":shape",
            (n, q) == (16, 1024) and b == (129 if estimator == "TabICL_distribution" else 1),
        )
        sorted_local = np.sort(atoms, axis=2)
        levels = np.arange(1, b) / b
        local_loss = (np.diff(sorted_local, axis=2) * np.minimum(levels, 1 - levels)).sum(2)
        for name, groups in parts.items():
            prepared = []
            for group in groups:
                vals = atoms[group].transpose(1, 0, 2).reshape(q, len(group) * b)
                order = np.argsort(vals, axis=1, kind="stable")
                sorted_values = np.take_along_axis(vals, order, axis=1)
                prepared.append((group, order, np.diff(sorted_values, axis=1)))
            for k in [16, 32, 64]:
                weight = bank[f"density_k{k}"]
                total = np.zeros(q)
                label = f"{estimator}_k{k}_{name}"
                saved_prediction = bank[label + "_prediction"]
                for group, order, intervals in prepared:
                    mass = weight[group].sum(0)
                    atom_weight = np.repeat(weight[group].T / b, b, axis=1)
                    cdf = np.cumsum(np.take_along_axis(atom_weight, order, axis=1), axis=1)[:, :-1]
                    total += (intervals * np.minimum(cdf, mass[:, None] - cdf)).sum(1)
                    query_rows = np.flatnonzero(np.isin(owner, group))
                    action = saved_prediction[query_rows]
                    active = mass[query_rows] > 0
                    local_atoms = atoms[group][:, query_rows]
                    below = (
                        (local_atoms < action[None, :, None]).mean(2) * weight[group][:, query_rows]
                    ).sum(0)
                    above = (
                        (local_atoms > action[None, :, None]).mean(2) * weight[group][:, query_rows]
                    ).sum(0)
                    check(
                        label + ":median_certificate:" + str(group[0]),
                        bool(
                            (
                                (below <= mass[query_rows] / 2 + 1e-12)
                                & (above <= mass[query_rows] / 2 + 1e-12)
                            )[active].all()
                        ),
                    )
                    zero = query_rows[~active]
                    if len(zero):
                        same(
                            label + ":fallback_value:" + str(group[0]),
                            saved_prediction[zero],
                            np.median(atoms[owner[zero], zero], axis=1),
                            atol=0,
                        )
                expected = np.maximum(total - (local_loss * weight).sum(0), 0)
                actual = bank[label + "_cost"]
                same(label + ":integrated_minimum_cost", actual, expected)
                certified.append(
                    dict(
                        estimator=estimator,
                        density_k=k,
                        partition=name,
                        queries=q,
                        max_abs_cost_difference=float(np.max(np.abs(actual - expected))),
                    )
                )

    comparison = []
    truth = bank["actual"].reshape(16, 64)
    for name in parts:
        tab = bank[f"TabICL_distribution_k32_{name}_prediction"].reshape(16, 64)
        knn = bank[f"empirical_KNN_distribution_k32_{name}_prediction"].reshape(16, 64)
        ta, ka = np.abs(tab - truth), np.abs(knn - truth)
        dif = ta.mean(1) - ka.mean(1)
        comparison.append(
            dict(
                partition=name,
                Tab_query_MAE=float(ta.mean()),
                KNN_query_MAE=float(ka.mean()),
                Tab_worse_cells=int((dif > 0).sum()),
                Tab_better_cells=int((dif < 0).sum()),
                ties=int((dif == 0).sum()),
                worst_cell_id=int(bank["cell_ids"][np.argmax(dif)]),
                worst_cell_MAE_difference=float(dif.max()),
                first_half_difference=float(ta[:, :32].mean() - ka[:, :32].mean()),
                second_half_difference=float(ta[:, 32:].mean() - ka[:, 32:].mean()),
                scope="같은저장query예측의현재산술재집계;새추론아님;RCTL성능비교아님",
            )
        )

    return dict(
        success=True,
        checks=len(checks),
        check_names=checks,
        source_count=15,
        saved_array_keys=len(bank.files),
        result_rows=54,
        rank_rows=9,
        primary_RCTL_means=rctl,
        retrospective_checks=summary["retrospective_checks"],
        query_owner_zero_probability=summary["query_owner_zero_probability"],
        toy_checks=summary["toy_checks"],
        primary_records=[r for r in rows if r["density_k"] == 32],
        certified_Tab_conditions=36,
        queries_per_condition=1024,
        maximum_cost_integral_difference=max(r["max_abs_cost_difference"] for r in certified),
        feature_max_difference=feature_max_difference,
        primary_saved_query_comparison=comparison,
        reported_elapsed_seconds=summary["elapsed_seconds"],
        reported_failed_seconds=summary["failed_attempt_seconds_included"],
        reported_resumed_seconds=summary["elapsed_seconds"]
        - summary["failed_attempt_seconds_included"],
        reported_peak_sampled_RSS_bytes=summary["peak_sampled_RSS_bytes"],
        new_model_runs=0,
        original_scripts_executed=False,
        independent_scientific_review=False,
        KNN_atom_reconstruction=False,
        density_neighbor_reconstruction=False,
        original_H5_reopened=False,
        scope=(
            "보존된54개결과행·9개순위행·입력·36개Tab조건의혼합최적성을검산함. "
            "원H5·KNNatom·density근접이웃재생성,독립실행시간재현과실패콘솔증명은아님."
        ),
    )


def main() -> None:
    """보존 근거 경로를 받아 검산 결과를 별도 파일로 저장한다."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes((json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode())
    print(
        json.dumps(
            {
                k: result[k]
                for k in [
                    "success",
                    "checks",
                    "source_count",
                    "result_rows",
                    "certified_Tab_conditions",
                    "new_model_runs",
                ]
            }
        )
    )


if __name__ == "__main__":
    main()
