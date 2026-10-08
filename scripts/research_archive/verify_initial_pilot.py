"""초기 01–02의 저장 배열·오차·날짜 대응을 대조한다. 연구 모델은 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import UTC, datetime
from itertools import pairwise
from pathlib import Path

import numpy as np

BASE = "tmp/redesign_20260925/"
H5_SHA = "4371f984d6ff235ce1760869eb8fe44e10b5b0214196158f8fb8dea8b324e65e"


def verify(source: Path, dates_path: Path | None = None) -> dict:
    """보존 manifest 또는 원본 루트와 별도 H5 날짜 발췌를 읽는다."""
    manifest = json.loads(source.read_text(encoding="utf-8")) if source.is_file() else None
    mapping = {r["path"]: r for r in manifest["sources"]} if manifest else {}
    accessed, checks, differences = {}, Counter(), []

    def check(name, condition):
        checks[name] += 1
        if not condition:
            raise AssertionError((name, checks[name]))

    def close(name, actual, expected):
        actual, expected = np.asarray(actual), np.asarray(expected)
        check(name + "_shape", actual.shape == expected.shape)
        diff = float(np.max(np.abs(actual.astype(float) - expected.astype(float))))
        differences.append(diff)
        check(name, np.isfinite(diff) and diff <= 1e-7)

    def path(relative, scopes):
        key = BASE + relative
        p = source.parent / mapping[key]["archive_path"] if manifest else source / key
        if key not in accessed:
            data = p.read_bytes()
            accessed[key] = dict(
                path=key,
                sha256=hashlib.sha256(data).hexdigest(),
                size_bytes=len(data),
                read_scope=[],
            )
            if manifest:
                check(
                    "portable_source_identity",
                    accessed[key]["sha256"] == mapping[key]["sha256"]
                    and len(data) == mapping[key]["size_bytes"],
                )
        accessed[key]["read_scope"] = sorted(set(accessed[key]["read_scope"]) | set(scopes))
        return p

    def arrays(relative, keys):
        with np.load(path(relative, ["array:" + k for k in keys]), allow_pickle=False) as stored:
            return {k: stored[k].copy() for k in keys}

    def fields(relative, keys):
        p = path(relative, ["json_parsed"])
        data = json.loads(p.read_text(encoding="utf-8"))
        selected = {}
        for key in keys:
            selected[key] = data[key]
            path(relative, ["json_top_level:" + key])
        return selected

    design = arrays("results/design_data.npz", ["X", "Y", "raw", "scales", "cell_indices", "times"])
    x, y, raw, scale, ids, times = [
        design[k] for k in ["X", "Y", "raw", "scales", "cell_indices", "times"]
    ]
    check("design_shape", x.shape == (32, 840, 16) and y.shape == (32, 840))
    check("raw_shape", raw.shape == (1008, 32))
    fixed_ids = [r * 100 + c for r in [37, 45, 53, 61] for c in [36, 40, 44, 48, 52, 56, 60, 64]]
    check("fixed32cell_grid", np.array_equal(ids, fixed_ids))
    check("design_time_indices", np.array_equal(times, np.arange(168, 1008)))
    close("first672mean", scale, raw[:672].mean(axis=0))
    check("raw_quality", np.isfinite(raw).all() and (raw >= 0).all() and (scale > 0).all())
    norm = raw / scale
    close("target_identity", y, norm[times].T.astype(np.float32))
    expected = np.array(
        [
            [
                np.r_[
                    norm[t - 8 : t, j],
                    norm[t - 24, j],
                    norm[t - 168, j],
                    norm[t - 24 : t, j].mean(),
                    norm[t - 24 : t, j].std(),
                ]
                for t in times
            ]
            for j in range(32)
        ],
        dtype=np.float32,
    )
    close("first12feature_columns", x[:, :, :12], expected)

    if manifest:
        artifact = manifest["derived_artifacts"]["H5_timestamps"]
        dates_path = source.parent / artifact["archive_path"]
        date_bytes = dates_path.read_bytes()
        check("derived_dates_hash", hashlib.sha256(date_bytes).hexdigest() == artifact["sha256"])
        check("derived_dates_size", len(date_bytes) == artifact["size_bytes"])
    elif dates_path is None:
        raise ValueError("원본 모드에는 --dates로 별도 H5 날짜 발췌를 지정해야 한다.")
    dates_data = json.loads(dates_path.read_text(encoding="utf-8"))
    check("date_extraction_source", dates_data["source_sha256"] == H5_SHA)
    dates = [datetime.fromisoformat(value) for value in dates_data["dates"]]
    check("timestamp_count", len(dates) == 1488 and len(set(dates)) == 1488)
    check("hourly_timestamps", all((b - a).total_seconds() == 3600 for a, b in pairwise(dates)))
    hours = np.array([dates[t].hour for t in times])
    weekdays = np.array([dates[t].weekday() for t in times])
    calendar = np.column_stack(
        [
            np.sin(2 * np.pi * hours / 24),
            np.cos(2 * np.pi * hours / 24),
            np.sin(2 * np.pi * weekdays / 7),
            np.cos(2 * np.pi * weekdays / 7),
        ]
    ).astype(np.float32)
    close("calendar_features", x[:, :, 12:16], np.broadcast_to(calendar, (32, 840, 4)))

    smoke = fields("results/smoke.json", ["python", "torch", "runs", "interpretation"])
    q = np.arange(672, 736)
    context = np.arange(168, 672)[np.rint(np.linspace(0, 503, 256)).astype(int)]
    check("smoke_cell_order", [r["cell_id"] for r in smoke["runs"]] == [3737, 3765, 6137, 6165])
    for r in smoke["runs"]:
        cell = r["cell_id"]
        j = int(np.flatnonzero(ids + 1 == cell)[0])
        a = arrays(
            f"results/smoke_cell_{cell}.npz", ["pred", "y", "context_indices", "query_indices"]
        )
        check(
            "smoke_indices",
            np.array_equal(a["context_indices"], context) and np.array_equal(a["query_indices"], q),
        )
        check("smoke_array_shapes", a["pred"].shape == (64,) and a["y"].shape == (64,))
        close("smoke_y", a["y"], y[j, q - 168])
        check("smoke_finite", np.isfinite(a["pred"]).all() and r["finite_prediction"])
        check(
            "smoke_counts",
            r["context_rows"] == 256 and r["query_rows"] == 64 and r["n_estimators"] == 1,
        )
        check("smoke_device", r["device"] == "cpu")
        close("smoke_Tab_MAE", np.abs(a["pred"] - a["y"]).mean(), r["median_mae"])
        for k, column in [("last_mae", 7), ("daily_mae", 8)]:
            close("smoke_" + k, np.abs(x[j, q - 168, column] - a["y"]).mean(), r[k])

    diagnostic = fields(
        "results/data_diagnostic.json",
        [
            "data_shape",
            "timestamps_unique",
            "hourly_increments",
            "negative_count",
            "zero_fraction",
            "cell_ids",
            "ridge_results",
            "raw_correlation_quantiles",
            "ridge_residual_correlation_quantiles",
            "scope",
        ],
    )
    check(
        "diagnostic_shape_ids",
        diagnostic["data_shape"] == list(raw.shape)
        and diagnostic["cell_ids"] == (ids + 1).tolist(),
    )
    check(
        "diagnostic_calendar_flags",
        diagnostic["timestamps_unique"] and diagnostic["hourly_increments"],
    )
    check(
        "diagnostic_raw_quality",
        diagnostic["negative_count"] == int((raw < 0).sum())
        and diagnostic["zero_fraction"] == float((raw == 0).mean()),
    )
    corr = arrays(
        "results/diagnostic_correlations.npz", ["raw_corr", "residual_corr", "ridge_errors"]
    )
    check("diagnostic_error_shape", corr["ridge_errors"].shape == (32, 336))
    check("diagnostic_error_finite", np.isfinite(corr["ridge_errors"]).all())
    check("diagnostic_results_count", len(diagnostic["ridge_results"]) == 32)
    for j, r in enumerate(diagnostic["ridge_results"]):
        check("diagnostic_cell_id", r["cell_id"] == ids[j] + 1)
        close(
            "diagnostic_Ridge_saved_error_MAE",
            np.abs(corr["ridge_errors"][j]).mean(),
            r["ridge_mae"],
        )
        for k, column in [("last_mae", 7), ("daily_mae", 8), ("weekly_mae", 9)]:
            close(
                "diagnostic_" + k,
                np.abs(x[j, times >= 672, column] - y[j, times >= 672]).mean(),
                r[k],
            )
    tri = np.triu_indices(32, 1)
    close("raw_correlations", np.corrcoef(y[:, times >= 672]), corr["raw_corr"])
    close("residual_correlations", np.corrcoef(corr["ridge_errors"]), corr["residual_corr"])
    for stored, reported in [
        ("raw_corr", "raw_correlation_quantiles"),
        ("residual_corr", "ridge_residual_correlation_quantiles"),
    ]:
        close(
            reported, np.quantile(corr[stored][tri], [0, 0.25, 0.5, 0.75, 1]), diagnostic[reported]
        )

    if manifest:
        for key in mapping:
            if key not in accessed:
                path(key.removeprefix(BASE), ["sha256_only"])
        for key, row in accessed.items():
            check(
                "declared_automated_read_scope",
                set(row["read_scope"]) == set(mapping[key]["automated_read_scope"]),
            )

    return dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks=dict(checks),
        max_absolute_difference=max(differences),
        model_executions=0,
        historical_code_executed=False,
        H5_read_during_this_run=False,
        NPZ_object_dates_loaded=False,
        numpy_version=np.__version__,
        date_extract_source_sha256=H5_SHA,
        time_boundaries={
            str(i): dates[i].isoformat(sep=" ")
            for i in [0, 168, 671, 672, 735, 839, 840, 1007, 1008, 1487]
        },
        smoke_fit_predict_seconds=sum(
            r["fit_seconds"] + r["predict_seconds"] for r in smoke["runs"]
        ),
        contexts=4,
        query_rows=256,
        sampled_peak_RSS=max(r["rss_peak_bytes"] for r in smoke["runs"]),
        smoke_runs=smoke["runs"],
        historical_python=smoke["python"],
        historical_torch=smoke["torch"],
        raw_correlation_quantiles=diagnostic["raw_correlation_quantiles"],
        residual_correlation_quantiles=diagnostic["ridge_residual_correlation_quantiles"],
        accessed=list(accessed.values()),
        limits=[
            "H5 바이트/선택값의 검수는 별도 로컬 증거. 이 검사는 보존 배열과 날짜 발췌를 대조한다.",
            "4cell smoke Ridge 예측은 저장되지 않아 Ridge MAE는 보고값이다. 재학습하지 않았다.",
            "32cell 진단은 저장 Ridge 오차의 검산이며 학습 알고리즘의 독립 재현이 아니다.",
            "0.2초 간격 RSS 표본이며 연속 측정 최대값/모델 전용 메모리가 아니다.",
            "02의 위험함수/RCTL은 계획. 후속 실행 여부의 전체 검토는 별도 기록으로 이어진다.",
        ],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--dates", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = verify(args.source, args.dates)
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
                    "max_absolute_difference",
                    "smoke_fit_predict_seconds",
                    "sampled_peak_RSS",
                    "time_boundaries",
                ]
            },
            ensure_ascii=False,
            indent=2,
        )
    )
