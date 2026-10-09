"""모델 실행 없이 저장된 grouping·입력 길이 예측과 회계를 검수한다."""

from __future__ import annotations

import argparse
import copy
import hashlib
import io
import json
import pickletools
import re
import zipfile
from datetime import UTC, datetime
from pathlib import Path

import numpy as np


def read_arrays(path: Path) -> tuple[dict, list[str]]:
    """기본 자료형의 NPY 배열을 읽고 역직렬화 없이 날짜 문자열을 확인한다."""
    arrays = {}
    dates = []
    with zipfile.ZipFile(path) as archive, np.load(path, allow_pickle=False) as saved:
        for key in saved.files:
            stream = io.BytesIO(archive.read(key + ".npy"))
            version = np.lib.format.read_magic(stream)
            if version != (1, 0):
                raise ValueError("예상하지 않은 NPY 헤더 버전")
            shape, fortran, dtype = np.lib.format.read_array_header_1_0(stream)
            if dtype.hasobject:
                if key != "query_timestamps" or shape != (64,) or fortran:
                    raise ValueError("예상하지 않은 object 배열")
                dates = [
                    value
                    for op, value, _ in pickletools.genops(stream.read())
                    if op.name in {"SHORT_BINUNICODE", "BINUNICODE", "UNICODE"}
                    and isinstance(value, str)
                    and re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", value)
                ]
            else:
                arrays[key] = saved[key]
    return arrays, dates


def verify(manifest_path: Path) -> dict:
    """저장 지표·실행 수·입력 발췌와 원장 한 번의 변화를 다시 계산한다."""
    manifest_path = manifest_path.resolve()
    archive_root = manifest_path.parents[2]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks, errors = [], []

    def check(name: str, condition: bool) -> None:
        """개별 검사 결과를 기록하며 성공을 모델 재현으로 해석하지 않는다."""
        checks.append(name)
        if not condition:
            errors.append(name)

    def numeric(name: str, actual: object, expected: object) -> None:
        """명시한 작은 부동소수점 허용 오차로 저장 산술을 대조한다."""
        check(name, np.allclose(actual, expected, rtol=1e-12, atol=1e-12))

    paths = {}
    for source in manifest["sources"]:
        path = (manifest_path.parent / source["archive_path"]).resolve()
        if not path.is_relative_to(archive_root):
            raise ValueError("근거 경로가 연구 아카이브 밖을 가리킴")
        raw = path.read_bytes()
        check(
            source["source_id"] + ":bytes",
            len(raw) == source["size_bytes"]
            and hashlib.sha256(raw).hexdigest() == source["sha256"],
        )
        paths[source["source_id"]] = path

    def data(sid: str) -> dict | list:
        """저장 JSON만 해석하며 과거 코드 파일은 import하지 않는다."""
        return json.loads(paths[sid].read_text(encoding="utf-8"))

    settings, saved = data("SRC-0027868"), data("SRC-0027865")
    calls, start, finish = data("SRC-0027862"), data("SRC-0027867"), data("SRC-0027866")
    before, after = data("SRC-0027861"), data("SRC-0027869")
    check("same_settings", settings == saved["settings"])
    check(
        "declared_model_scope",
        settings["lengths"] == [2, 8]
        and settings["seed"] == 20260925
        and settings["ensemble"] == 1
        and settings["median"]
        and settings["development_only"]
        and settings["RCTL_fits"] == settings["RCTL_calls"] == 0
        and settings["feature_covariates"]
        == [
            "day_lag",
            "week_lag",
            "past24mean",
            "past24std",
            "hour_sin",
            "hour_cos",
            "dow_sin",
            "dow_cos",
        ],
    )
    check(
        "settings_start_hash",
        start["settings_sha256"] == hashlib.sha256(paths["SRC-0027868"].read_bytes()).hexdigest(),
    )
    for key, sid in [("plan", "SRC-0021940"), ("code", "SRC-0022879")]:
        check(
            key + "_hash",
            settings["sha256"][key] == hashlib.sha256(paths[sid].read_bytes()).hexdigest(),
        )
    for key, sid in [("data", "SRC-0023485"), ("checkpoint", "SRC-0023488")]:
        entry = next(x for x in manifest["hash_only_sources"] if x["source_id"] == sid)
        check(key + "_recorded_identity", settings["sha256"][key] == entry["sha256"])
    pred, dates = read_arrays(paths["SRC-0027863"])
    partial, partial_dates = read_arrays(paths["SRC-0027864"])
    check(
        "partial_keys",
        set(partial) == set(pred) - {"context_times", "scales"} and not partial_dates,
    )
    for key, array in partial.items():
        check("partial:" + key, np.array_equal(array, pred[key]))
    models = ["Ridge", "HGB", "TabICL"]
    groups = {
        "global": [[0, 1, 2, 3]],
        "geo2": [[0, 1], [2, 3]],
        "local": [[0], [1], [2], [3]],
        "global_ID": [[0, 1, 2, 3]],
    }
    expected_names = {
        f"{model}_{group}_L{length}" for model in models for group in groups for length in [2, 8]
    }
    check(
        "24_conditions",
        set(saved["results"]) == expected_names
        and set(pred)
        == expected_names | {"actual", "context_times", "query_times", "cell_ids", "scales"},
    )
    check(
        "fixed_cells_groups",
        settings["cell_ids"] == [3737, 3765, 6137, 6165] and settings["groups"] == groups,
    )
    ct = np.rint(np.linspace(168, 839, 256)).astype(int)
    hours = np.rint(np.linspace(0, 23, 16)).astype(int)
    qt = np.concatenate([day * 24 + hours for day in [43, 47, 51, 55]])
    for key, expected in [
        ("context_times", ct),
        ("query_times", qt),
        ("cell_ids", settings["cell_ids"]),
    ]:
        check(key, np.array_equal(pred[key], expected) and np.array_equal(settings[key], expected))
    check(
        "target_time_boundary",
        len(set(ct)) == 256 and len(set(qt)) == 64 and ct.max() < qt.min() - 8,
    )
    check("longest_lag_time_boundary", ct.max() < qt.min() - 168)
    slice_entry = manifest["derived_files"][0]
    slice_path = (manifest_path.parent / slice_entry["archive_path"]).resolve()
    if not slice_path.is_relative_to(archive_root):
        raise ValueError("입력 발췌 경로가 아카이브 밖을 가리킴")
    check(
        "derived_slice_bytes",
        hashlib.sha256(slice_path.read_bytes()).hexdigest() == slice_entry["sha256"],
    )
    raw, _ = read_arrays(slice_path)
    check("input_shape", raw["raw_activity"].shape == (1488, 4))
    check("input_cell_order", np.array_equal(raw["cell_ids"], pred["cell_ids"]))
    timestamps = raw["timestamps"].astype("datetime64[s]")
    check("hourly_index", np.all(np.diff(timestamps) == np.timedelta64(1, "h")))
    scale = raw["raw_activity"][:672].mean(axis=0)
    numeric("first672_scale", pred["scales"], scale)
    numeric("actual_from_input", pred["actual"], (raw["raw_activity"] / scale)[qt].T)
    check(
        "timestamp_literals",
        len(dates) == 64 and dates == [str(v).replace("T", " ") for v in timestamps[qt]],
    )
    actual = pred["actual"]
    check("actual_valid", actual.shape == (4, 64) and np.isfinite(actual).all())
    calculated, absolute_errors = {}, {}
    for name in sorted(expected_names):
        array = pred[name]
        check(
            name + ":shape_finite_clipped",
            array.shape == (4, 64) and np.isfinite(array).all() and (array >= 0).all(),
        )
        err = np.abs(array - actual)
        absolute_errors[name] = err
        row = dict(
            MAE=float(err.mean()),
            cell_MAE=err.mean(axis=1).tolist(),
            block_MAE=err.reshape(4, 4, 16).mean(axis=(0, 2)).tolist(),
            half_MAE=err.reshape(4, 2, 32).mean(axis=(0, 2)).tolist(),
            raw_activity_MAE=float((err * scale[:, None]).mean()),
        )
        check(name + ":metric_keys", set(row) == set(saved["results"][name]))
        for metric, value in row.items():
            numeric(name + ":" + metric, value, saved["results"][name][metric])
        calculated[name] = row
    check(
        "effect_keys",
        set(saved["grouping_history_interactions"])
        == {f"{m}_{g}" for m in models for g in ["geo2", "local"]},
    )
    for model in models:
        for group in ["geo2", "local"]:
            name = model + "_" + group
            effect = (
                absolute_errors[model + "_global_L2"]
                - absolute_errors[model + "_global_L8"]
                - absolute_errors[name + "_L2"]
                + absolute_errors[name + "_L8"]
            )
            values = dict(
                interaction=float(effect.mean()),
                half_interaction=effect.reshape(4, 2, 32).mean(axis=(0, 2)),
                block_interaction=effect.reshape(4, 4, 16).mean(axis=(0, 2)),
            )
            for metric, value in values.items():
                numeric(
                    name + ":" + metric, value, saved["grouping_history_interactions"][name][metric]
                )
            for alt in ["global", "global_ID"]:
                diff = absolute_errors[name + "_L2"] - absolute_errors[model + "_" + alt + "_L2"]
                halves = diff.reshape(4, 2, 32).mean(axis=(0, 2))
                row = saved["screening"][name][alt]
                numeric(
                    name + ":screen:" + alt,
                    [diff.mean(), *halves],
                    [row["short_partition_minus_short_alternative"], *row["halves"]],
                )
                check(
                    name + ":decision:" + alt,
                    row["partition_worse_overall_and_both_halves"]
                    == bool(diff.mean() > 0 and (halves > 0).all()),
                )
    cost = saved["cost"]
    expected_calls = [
        (f"{group}_L{length}", [settings["cell_ids"][i] for i in members])
        for length in [2, 8]
        for group, partitions in groups.items()
        for members in partitions
    ]
    check("16_call_order", [(c["condition"], c["cells"]) for c in calls] == expected_calls)
    for i, call in enumerate(calls):
        group, length = call["condition"].rsplit("_L", 1)
        check(
            f"call:{i}",
            call["status"] == "complete"
            and call["ensemble"] == 1
            and call["context_rows"] == len(call["cells"]) * 256
            and call["query_rows"] == len(call["cells"]) * 64
            and call["features"] == int(length) + 8 + (4 if group == "global_ID" else 0)
            and call["fit_seconds"] > 0
            and call["predict_seconds"] > 0,
        )
    check(
        "counts",
        len(calls) == cost["TabICL_contexts"] == 16
        and sum(c["query_rows"] for c in calls) == cost["TabICL_query_rows"] == 2048
        and cost["simple_fits"] == 2 * len(calls) == 32,
    )
    numeric(
        "Tab_timer_sum",
        cost["TabICL_seconds"],
        sum(c["fit_seconds"] + c["predict_seconds"] for c in calls),
    )
    numeric(
        "nonduplicate_stage_partition",
        cost["stage_seconds"],
        cost["TabICL_seconds"] + cost["cheap_numeric_seconds_including_simple"],
    )
    check(
        "simple_in_cheap",
        0 < cost["simple_fit_seconds"] < cost["cheap_numeric_seconds_including_simple"],
    )
    check("recorded_completion", finish["cost"] == cost and finish["hashes_unchanged"])
    check(
        "bounded_observation",
        cost["TabICL_seconds"] < 240
        and cost["simple_fit_seconds"] < 30
        and cost["stage_seconds"] < 300
        and cost["observed_rss_bytes_max"] < 8 * 1024**3
        and cost["rss_sampling"] == "between calls, not continuous peak",
    )
    check(
        "no_RCTL_or_new_algorithm_validation",
        cost["RCTL_fits"] == cost["RCTL_forward_calls"] == 0
        and not any(
            saved[k]
            for k in ["independent_test", "RCTL_validated", "new_clustering_algorithm_validated"]
        ),
    )
    expected = copy.deepcopy(before)
    stage = "history_grouping_60"
    check(
        "not_previously_accounted",
        not any(x["stage"] == stage for x in before["model_calls_by_stage"]),
    )
    expected["model_calls_by_stage"].append(
        dict(
            stage=stage,
            contexts=16,
            predicted_query_rows=2048,
            fit_predict_seconds=cost["TabICL_seconds"],
            ensemble=1,
        )
    )
    for key, delta in [
        ("TabICL_contexts", 16),
        ("TabICL_query_rows", 2048),
        ("TabICL_fit_predict_seconds", cost["TabICL_seconds"]),
    ]:
        expected["used"][key] += delta
    expected["remaining_count_budgets"]["TabICL_contexts"] -= 16
    expected["remaining_count_budgets"]["TabICL_query_rows"] -= 2048
    expected["new_cheap_diagnostic_seconds"][stage] = cost["cheap_numeric_seconds_including_simple"]
    expected["cheap_stage_details"].append(
        dict(
            stage=stage,
            new_simple_fits=32,
            methods=["Ridge", "HGB"],
            entire_stage_seconds=cost["stage_seconds"],
            TabICL_seconds_accounted_separately=cost["TabICL_seconds"],
            fit_predict_seconds_included_in_cheap_stage=cost["simple_fit_seconds"],
            cost_not_counted_twice=True,
        )
    )
    check("whole_ledger_transition", after == expected)
    check(
        "budget_transition",
        before["used"]["TabICL_contexts"] == 49
        and after["used"]["TabICL_contexts"] == 65
        and before["used"]["TabICL_query_rows"] == 35968
        and after["used"]["TabICL_query_rows"] == 38016
        and after["used"]["RCTL_fits"] == 29
        and after["remaining_count_budgets"]["RCTL_fits"] == 0,
    )
    cheap = sum(after["new_cheap_diagnostic_seconds"].values())
    total = cheap + sum(
        after["used"][k]
        for k in [
            "TabICL_fit_predict_seconds",
            "RCTL_wall_seconds",
            "RCTL_frozen_inference_seconds",
        ]
    )
    return dict(
        success=not errors,
        checks=len(checks),
        check_names=checks,
        errors=errors,
        checked_at_utc=datetime.now(UTC).isoformat(),
        metric_values_checked=288,
        interaction_values_checked=42,
        screening_numeric_values_checked=36,
        screening_flags_checked=12,
        saved_prediction_values_checked=6144,
        calculated_metrics=calculated,
        cheap_after60_seconds=cheap,
        recorded_modeling_after60_seconds=total,
        source_groups=len(paths),
        new_model_runs=0,
        original_scripts_executed=False,
        pickle_loaded=False,
        independent_reproduction=False,
        scope=(
            "보존한 출력의 산술과 과거 원장 한 번의 변화를 검수했다. "
            "원 HDF5의 동일성은 별도로 확인하며, 당시 모델 실행을 재현한 검사가 아니다."
        ),
    )


def main() -> None:
    """검수 근거를 저장하고 일치하지 않는 결과가 있으면 실패로 종료한다."""
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
            {
                k: report[k]
                for k in [
                    "success",
                    "checks",
                    "errors",
                    "metric_values_checked",
                    "interaction_values_checked",
                    "screening_numeric_values_checked",
                ]
            }
        )
    )
    raise SystemExit(0 if report["success"] else 1)


if __name__ == "__main__":
    main()
