"""고정 RCTL의 저장 다중 시점 예측을 검산하며 모델을 로드하거나 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path

import numpy as np


def verify(manifest_path: Path) -> dict:
    """보존 근거의 식별·지표·첫 시점·단순 기준과 보고된 비용을 대조한다."""
    manifest_path = manifest_path.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks = []
    raw_by_id = {}

    def check(name, condition):
        """불일치 자료를 거부하고 확인한 항목 이름을 보존한다."""
        if not condition:
            raise ValueError(name)
        checks.append(name)

    def same(name, a, b, atol=1e-12):
        """형태와 유한성을 먼저 확인한 뒤 수치 배열을 비교한다."""
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

    def npz(sid, keys=None):
        """객체 역직렬화를 금지하고 필요한 저장 배열만 읽는다."""
        with np.load(io.BytesIO(raw_by_id[sid]), allow_pickle=False) as bank:
            return {key: bank[key] for key in (bank.files if keys is None else keys)}

    def json_source(sid):
        """해시를 대조한 JSON 바이트를 읽는다."""
        return json.loads(raw_by_id[sid])

    required = {
        "SRC-0021163",
        "SRC-0022867",
        "SRC-0027709",
        "SRC-0027710",
        "SRC-0027711",
        "SRC-0027712",
        "SRC-0027713",
        "SRC-0021188",
        "SRC-0030238",
        "SRC-0030236",
        "SRC-0023577",
    }
    rows = manifest["sources"]
    check(
        "32_unique_sources",
        len(rows) == len({r["source_id"] for r in rows}) == len({r["path"] for r in rows}) == 32
        and required <= {r["source_id"] for r in rows},
    )
    for row in rows:
        sid = row["source_id"]
        path = (manifest_path.parent / row["archive_path"]).resolve()
        check(sid + ":bounded_path", path.is_relative_to(manifest_path.parents[2]))
        raw = path.read_bytes()
        check(sid + ":size", type(row["size_bytes"]) is int and len(raw) == row["size_bytes"])
        check(sid + ":hash", hashlib.sha256(raw).hexdigest() == row["sha256"])
        raw_by_id[sid] = raw
    by_name = {Path(r["path"]).name: r for r in rows}
    cfg = json_source("SRC-0027712")
    s = json_source("SRC-0027713")
    finish = json_source("SRC-0027710")
    started = json_source("SRC-0027711")
    frozen = json_source("SRC-0030238")
    bank = npz("SRC-0027709")
    ev = npz("SRC-0030236")
    for field, sid in [
        ("plan_sha256", "SRC-0021163"),
        ("code_sha256", "SRC-0022867"),
        ("frozen_settings_sha256", "SRC-0030238"),
    ]:
        check(field + ":identity", cfg[field] == hashlib.sha256(raw_by_id[sid]).hexdigest())
    check(
        "declared_integer_settings",
        all(
            type(cfg[k]) is int and cfg[k] == v
            for k, v in [
                ("horizon", 24),
                ("primary_horizon", 6),
                ("seed", 20260925),
                ("max_forward_calls", 504),
                ("max_predicted_rows", 110592),
                ("wall_cap_seconds", 300),
                ("ram_cap_bytes", 2 * 1024**3),
            ]
        ),
    )
    check(
        "positive_start_metadata",
        type(started["pid"]) is int
        and started["pid"] > 0
        and type(started["unix"]) in (int, float)
        and np.isfinite(started["unix"])
        and started["unix"] > 0,
    )
    check(
        "finite_time_fields",
        all(
            type(v) in (int, float) and np.isfinite(v) and v > 0
            for v in [s["wall_seconds"], finish["wall_seconds"]]
        ),
    )
    check(
        "integer_RSS_fields",
        all(type(v) is int and v > 0 for v in [s["peak_rss_bytes"], finish["peak_rss_bytes"]]),
    )
    check(
        "origin_id_dtypes",
        np.issubdtype(bank["origins"].dtype, np.integer)
        and np.issubdtype(bank["cell_ids"].dtype, np.integer),
    )
    check(
        "six_methods",
        cfg["methods"]
        == [
            "global",
            "tabicl_risk",
            "empirical_risk",
            "knn_risk",
            "pcc_balanced",
            "random_balanced",
        ],
    )
    primary = [t for t in frozen["tasks"] if t[1] == 20260925]
    check(
        "primary_seed", type(frozen["seed_primary"]) is int and frozen["seed_primary"] == 20260925
    )
    check(
        "original_time_splits",
        frozen["train_targets"] == [168, 839]
        and frozen["validation_targets"] == [840, 1007]
        and frozen["test_targets"] == [1008, 1487],
    )
    groups = {}
    expected_predictions = set()
    expected_checkpoints = set()
    for method, seed, cluster, members in primary:
        check(
            method + ":task_index:" + str(cluster),
            type(seed) is int and type(cluster) is int and cluster == len(groups.get(method, [])),
        )
        check(
            method + ":members:" + str(cluster),
            all(type(i) is int for i in members) and len(set(members)) == len(members),
        )
        groups.setdefault(method, []).append(members)
        expected_predictions.add(f"{method}_{seed}_cluster{cluster}.npz")
        expected_checkpoints.add(f"{method}_{seed}_cluster{cluster}.pt")
    check("21_tasks_six_partitions", len(primary) == 21 and list(groups) == cfg["methods"])
    for method, partition in groups.items():
        check(
            method + ":partition",
            sorted(i for group in partition for i in group) == list(range(16))
            and len(partition) == (1 if method == "global" else 4),
        )
    check(
        "21_prior_prediction_sources",
        {Path(r["path"]).name for r in rows if r["source_id"] not in required}
        == expected_predictions,
    )
    checkpoint_rows = manifest["hash_only_sources"]
    checkpoint_by_name = {Path(r["path"]).name: r for r in checkpoint_rows}
    check(
        "21_checkpoint_metadata_rows",
        len(checkpoint_rows) == len({r["source_id"] for r in checkpoint_rows}) == 21
        and set(checkpoint_by_name) == expected_checkpoints == set(cfg["checkpoints"]),
    )
    for name, row in checkpoint_by_name.items():
        check(
            name + ":metadata_scope",
            row["distribution"] == "metadata_only_checkpoint_not_published"
            and row["team_access_verified"] is False
            and row["team_location"] is None,
        )
        check(name + ":checkpoint_hash_reference", row["sha256"] == cfg["checkpoints"][name])
    check(
        "H5_metadata_scope",
        len(manifest["primary_sources"]) == 1
        and manifest["primary_sources"][0]["source_id"] == "SRC-0023485"
        and manifest["primary_sources"][0]["sha256"]
        == "4371f984d6ff235ce1760869eb8fe44e10b5b0214196158f8fb8dea8b324e65e",
    )

    check("settings_copies", s["settings"] == cfg)
    check("planned_horizons", cfg["horizon"] == 24 and cfg["primary_horizon"] == 6)
    check(
        "retrospective_inference_scope",
        cfg["inference_only"] is True
        and cfg["changed_partitions"] is False
        and cfg["future_actuals_used_in_recursive_inputs"] is False
        and cfg["independent_test"] is False,
    )
    check(
        "no_new_fit_Tab_calls",
        all(
            type(v) is int and v == 0
            for v in [cfg["new_fits"], cfg["new_TabICL_calls"], finish["new_fits"]]
        )
        and s["no_new_RCTL_fits"] is True
        and s["no_new_TabICL_calls"] is True,
    )
    check("complete_without_error", finish["complete"] is True and finish["error"] is None)
    origins = bank["origins"]
    ids = bank["cell_ids"]
    scales = bank["scales"]
    methods = bank["methods"].tolist()
    prediction, y = bank["prediction"], bank["y"]
    check(
        "array_keys", set(bank) == {"prediction", "y", "methods", "cell_ids", "scales", "origins"}
    )
    check(
        "method_order", methods == cfg["methods"] + ["persistence", "daily_naive", "weekly_naive"]
    )
    check(
        "origin48",
        origins.tolist() == cfg["origins"] == np.linspace(1008, 1464, 48, dtype=int).tolist(),
    )
    check("cell_identity", ids.tolist() == cfg["cell_ids"] == ev["cell_ids"].tolist())
    same("cell_scales", scales, ev["scales"], atol=0)
    check("scales_positive", scales.shape == (16,) and (scales > 0).all())
    check(
        "prediction_shape_finite",
        prediction.shape == (9, 16, 48, 24)
        and prediction.dtype.kind == "f"
        and np.isfinite(prediction).all(),
    )
    check(
        "truth_shape_finite",
        y.shape == (16, 48, 24) and y.dtype.kind == "f" and np.isfinite(y).all(),
    )
    tt = origins[:, None] + np.arange(24)[None, :]
    same(
        "prior_targets_at_float32_precision",
        y.astype(np.float32),
        ev["test_y"][:, tt - 1008],
        atol=0,
    )
    check("all_480_times_covered", np.array_equal(np.unique(tt), ev["test_times"]))
    unique_y = np.empty((16, 480))
    for t in range(1008, 1488):
        values = y[:, tt == t]
        check(f"truth_overlap:{t}", (values == values[:, 0, None]).all())
        unique_y[:, t - 1008] = values[:, 0]

    check(
        "9_unique_metrics",
        len(s["metrics"]) == 9 and [r["method"] for r in s["metrics"]] == methods,
    )
    err = np.abs(prediction - y[None])
    small = []
    for i, row in enumerate(s["metrics"]):
        name = row["method"]
        check(
            name + ":metric_fields",
            set(row)
            == {
                "method",
                "scaled_mae_by_horizon",
                "raw_activity_mae_by_horizon",
                "per_cell_mae_by_horizon",
                "origin_mean_mae_by_horizon",
                "negative_prediction_count",
            },
        )
        for key, expected in [
            ("scaled_mae_by_horizon", err[i].mean((0, 1))),
            ("raw_activity_mae_by_horizon", (err[i] * scales[:, None, None]).mean((0, 1))),
            ("per_cell_mae_by_horizon", err[i].mean(1)),
            ("origin_mean_mae_by_horizon", err[i].mean(0)),
        ]:
            same(name + ":" + key, row[key], expected)
        check(
            name + ":negative_count",
            type(row["negative_prediction_count"]) is int
            and row["negative_prediction_count"] == int((prediction[i] < 0).sum()),
        )
        small.append(
            dict(
                method=name,
                scaled={str(h): row["scaled_mae_by_horizon"][h - 1] for h in [1, 6, 12, 24]},
                raw={str(h): row["raw_activity_mae_by_horizon"][h - 1] for h in [1, 6, 12, 24]},
                negative_predictions=row["negative_prediction_count"],
            )
        )
    check(
        "20_unique_comparisons",
        len(s["comparisons"]) == 20
        and all(type(r["horizon"]) is int for r in s["comparisons"])
        and {(r["method"], r["horizon"]) for r in s["comparisons"]}
        == {(m, h) for m in cfg["methods"] if m != "global" for h in [1, 6, 12, 24]},
    )
    gi = methods.index("global")
    for row in s["comparisons"]:
        name, h = row["method"], row["horizon"]
        check(name + ":reference:" + str(h), row["reference"] == "global")
        dif = err[methods.index(name), :, :, h - 1] - err[gi, :, :, h - 1]
        for key, value in [
            ("mean_mae_difference", dif.mean()),
            ("first_half_origin_difference", dif[:, :24].mean()),
            ("second_half_origin_difference", dif[:, 24:].mean()),
        ]:
            same(f"{name}:{h}:{key}", row[key], value)
        for key, value in [
            ("cells_with_lower_mae", int((dif.mean(1) < 0).sum())),
            ("origins_with_lower_mae", int((dif.mean(0) < 0).sum())),
        ]:
            check(f"{name}:{h}:{key}", type(row[key]) is int and row[key] == value)

    tasks = [t for t in frozen["tasks"] if t[1] == cfg["seed"]]
    check("21_primary_tasks", len(tasks) == 21 and cfg["seed"] == 20260925)
    reports = {r["checkpoint"]: r["max_abs_difference"] for r in s["first_step_reproduction"]}
    check("21_first_step_reports", len(reports) == len(s["first_step_reproduction"]) == 21)
    maximum = 0
    for method, seed, cluster, members in tasks:
        key = f"{method}_{seed}_cluster{cluster}"
        old_prediction = npz(by_name[key + ".npz"]["source_id"], ["cell_ids", "prediction"])
        check(key + ":cells", old_prediction["cell_ids"].tolist() == ids[members].tolist())
        values = prediction[methods.index(method), members, :, 0]
        diff = float(np.max(np.abs(values - old_prediction["prediction"][:, origins - 1008])))
        same(key + ":first_step", diff, reports[key], atol=0)
        check(key + ":first_step_tolerance", diff <= 2e-5)
        maximum = max(maximum, diff)
        check(
            key + ":checkpoint_metadata",
            checkpoint_by_name[key + ".pt"]["sha256"] == cfg["checkpoints"][key + ".pt"],
        )
    check(
        "forward_counts",
        all(
            type(v) is int and v == len(tasks) * 24
            for v in [s["forward_calls"], finish["forward_calls"]]
        ),
    )
    check(
        "row_counts",
        all(
            type(v) is int and v == 6 * 16 * 48 * 24
            for v in [s["predicted_rows"], finish["predicted_rows"]]
        ),
    )
    check("time_boundary", 0 < s["wall_seconds"] < finish["wall_seconds"] < cfg["wall_cap_seconds"])
    check(
        "RSS_copies",
        s["peak_rss_bytes"] == finish["peak_rss_bytes"]
        and type(s["peak_rss_bytes"]) is int
        and 0 < s["peak_rss_bytes"] < cfg["ram_cap_bytes"],
    )

    # 초기 저장 관측값과 반복 target으로 단순 기준의 산술을 대조한다.
    # 원 H5나 실제 recursive 중간 입력의 독립 검사는 별도 범위다.
    design = npz("SRC-0023577", ["raw", "scales", "cell_indices"])
    selection = [int(np.flatnonzero(design["cell_indices"] + 1 == c)[0]) for c in ids]
    same("early_scales", design["scales"][selection], scales, atol=0)
    same("raw_first672_means", design["raw"][:672, selection].mean(0), scales, atol=0)
    z = np.concatenate([design["raw"][:, selection] / scales, unique_y.T])
    check("saved_raw_and_truth_cover1488", z.shape == (1488, 16))
    for name, expected in [
        ("persistence", np.broadcast_to(z[origins - 1].T[:, :, None], (16, 48, 24))),
        ("daily_naive", z[tt - 24].transpose(2, 0, 1)),
        ("weekly_naive", z[tt - 168].transpose(2, 0, 1)),
    ]:
        same(name + ":saved_history_formula", prediction[methods.index(name)], expected, atol=0)
    check(
        "daily_and_persistence_same_at24",
        np.array_equal(
            prediction[methods.index("daily_naive"), :, :, 23],
            prediction[methods.index("persistence"), :, :, 23],
        ),
    )
    for lag in [24, 168]:
        check(f"lag{lag}:always_before_origin", bool(((tt - lag) < origins[:, None]).all()))

    cell_comparisons = []
    for name in methods[:6]:
        if name == "global":
            continue
        for horizon in [6, 24]:
            dif = (err[methods.index(name), :, :, horizon - 1] - err[gi, :, :, horizon - 1]).mean(1)
            cell_comparisons.append(
                dict(
                    method=name,
                    horizon=horizon,
                    cell_ids=ids.tolist(),
                    cell_mae_differences=dif.tolist(),
                    better_cell_ids=ids[dif < 0].tolist(),
                    worse_cell_ids=ids[dif > 0].tolist(),
                    worst_cell_id=int(ids[np.argmax(dif)]),
                    worst_cell_difference=float(dif.max()),
                )
            )
    ranks = []
    for horizon in [6, 12, 24]:
        ranks.append(
            dict(
                horizon=horizon,
                scaled_order=sorted(
                    methods,
                    key=lambda n: s["metrics"][methods.index(n)]["scaled_mae_by_horizon"][
                        horizon - 1
                    ],
                ),
                raw_order=sorted(
                    methods,
                    key=lambda n: s["metrics"][methods.index(n)]["raw_activity_mae_by_horizon"][
                        horizon - 1
                    ],
                ),
            )
        )
    return dict(
        success=True,
        checks=len(checks),
        check_names=checks,
        preserved_sources=32,
        checkpoint_hash_references=21,
        checkpoint_bytes_checked_in_this_run=False,
        checkpoint_team_access_verified=False,
        methods=small,
        comparisons=s["comparisons"],
        cell_comparisons=cell_comparisons,
        scale_rank_comparisons=ranks,
        first_step_max_difference=maximum,
        reported_forward_calls=s["forward_calls"],
        reported_predicted_rows=s["predicted_rows"],
        reported_peak_sampled_RSS_bytes=s["peak_rss_bytes"],
        summary_wall_seconds=s["wall_seconds"],
        finish_wall_seconds=finish["wall_seconds"],
        all_cell_and_origin_metric_values_compared=True,
        new_model_runs=0,
        original_scripts_executed=False,
        original_H5_reopened=False,
        actual_recursive_intermediate_inputs_saved_or_verified=False,
        independent_scientific_review=False,
        scope=(
            "보존 자료의 전체 수치 지표·20대조·21첫시점과 단순 기준 산술. "
            "checkpoint는 metadata 대조이며 실제 바이트/H5 검사는 별도로 기록; "
            "모델 추론이나 실제 중간 X 재현 아님."
        ),
    )


def main() -> None:
    """보존 근거 위치를 받아 검산 결과를 별도 파일에 저장한다."""
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
                    "preserved_sources",
                    "checkpoint_hash_references",
                    "first_step_max_difference",
                    "new_model_runs",
                ]
            }
        )
    )


if __name__ == "__main__":
    main()
