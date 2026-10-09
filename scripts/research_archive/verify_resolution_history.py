"""29–32번의 보존 CSV·예측·집계만 검산한다. 모델 및 원 코드는 실행하지 않는다."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from datetime import UTC, datetime
from pathlib import Path

import numpy as np


def verify(manifest_path: Path) -> dict:
    """해시·시간 격자·오차·공유 손해·정정·비용을 보존 사본과 대조한다."""
    manifest_path = manifest_path.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    ROWS = manifest["sources"]
    if len({r["source_id"] for r in ROWS}) != len(ROWS):
        raise ValueError("duplicate_source_ids")

    def date_str(value):
        """역사 JSON과 같은 초 단위의 로컬 시각 문자열을 만든다."""
        return np.datetime_as_string(value, unit="s").replace("T", " ")

    CHECKS = []
    RAW = {}

    def check(name, condition):
        """검사 실패 시 중단하고 성공한 검사 이름을 기록한다."""
        if not condition:
            raise ValueError(name)
        CHECKS.append(name)

    def same(name, got, want, atol=1e-12):
        """두 유한 수치 배열의 형태와 값을 지정 허용오차로 비교한다."""
        a, b = np.asarray(got), np.asarray(want)
        check(
            name,
            a.shape == b.shape
            and a.dtype.kind in "iuf"
            and b.dtype.kind in "iuf"
            and np.isfinite(a).all()
            and np.isfinite(b).all()
            and np.allclose(a, b, rtol=1e-12, atol=atol),
        )

    def obj(sid):
        """해시를 확인한 원본 사본의 바이트를 JSON으로 읽는다."""
        return json.loads(RAW[sid])

    def changes(a, b, path=""):
        """중첩 JSON의 추가 및 변경 항목을 경로와 이전·이후 값으로 모은다."""
        if isinstance(a, dict) and isinstance(b, dict):
            out = []
            for k in sorted(a.keys() | b.keys()):
                if k not in a or k not in b:
                    out.append(
                        dict(path=path + "/" + k, before=a.get(k), after=b.get(k), added=k not in a)
                    )
                else:
                    out.extend(changes(a[k], b[k], path + "/" + k))
            return out
        if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
            return [
                v
                for i, (x, y) in enumerate(zip(a, b, strict=True))
                for v in changes(x, y, path + "/" + str(i))
            ]
        return [] if a == b else [dict(path=path, before=a, after=b)]

    for row in ROWS:
        sid = row["source_id"]
        path = (manifest_path.parent / row["archive_path"]).resolve()
        check(sid + ":bounded_path", path.is_relative_to(manifest_path.parents[2]))
        raw = path.read_bytes()
        check(
            sid + ":identity",
            len(raw) == row["size_bytes"] and hashlib.sha256(raw).hexdigest() == row["sha256"],
        )
        RAW[sid] = raw

    cfg, summary, partial, subset, initial, tree = [
        obj(s)
        for s in [
            "SRC-0030768",
            "SRC-0030769",
            "SRC-0030766",
            "SRC-0032492",
            "SRC-0032493",
            "SRC-0064383",
        ]
    ]
    check("settings_equal", cfg == summary["settings"])
    check("partial_equal", partial == summary["resolutions"])
    check("plan_hash", cfg["plan_sha256"] == hashlib.sha256(RAW["SRC-0021320"]).hexdigest())
    ids = [4159, 4556, 5161]
    check("cell_order", cfg["cells"] == ids)
    check(
        "split_dates",
        cfg["train_targets"] == ["2013-11-08", "2013-11-21"]
        and cfg["diagnostic_targets"] == ["2013-11-21", "2013-12-01"],
    )
    check(
        "new_research_calls_zero",
        all(cfg[k] == 0 for k in ["new_RCTL_fits", "new_RCTL_forward", "new_TabICL_calls"]),
    )
    check(
        "pinned_tree",
        tree["sha"] == subset["commit"] == "6042fb01b0ae6c4ec2e2942d171186d5d6517349"
        and tree["truncated"] is False,
    )
    entries = {x["path"]: x for x in tree["tree"]}
    nov_grid = np.arange(
        np.datetime64("2013-11-01T00", "m"),
        np.datetime64("2013-12-01T00", "m"),
        np.timedelta64(10, "m"),
    ).astype("datetime64[ns]")
    fine, csv_report = [], []
    for cid, sid, record in zip(
        ids, ["SRC-0032494", "SRC-0032495", "SRC-0032496"], subset["records"], strict=True
    ):
        raw = RAW[sid]
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        entry = entries[f"processed/ts_full_square_{cid}.csv"]
        check(
            sid + ":git_blob",
            blob == entry["sha"] == record["git_blob_sha"] and len(raw) == entry["size"],
        )
        reader = csv.DictReader(io.StringIO(raw.decode("utf-8")))
        check(sid + ":columns", reader.fieldnames == ["square_id", "time_ms", "internet", "time"])
        csv_rows = list(reader)
        check(sid + ":ids", all(int(r["square_id"]) == cid for r in csv_rows))
        stamp = np.array([int(r["time_ms"]) for r in csv_rows], dtype="datetime64[ms]").astype(
            "datetime64[ns]"
        )
        rendered = np.array([r["time"] for r in csv_rows], dtype="datetime64[ns]")
        check(sid + ":UTC_time_column", np.array_equal(stamp, rendered))
        times = stamp + np.timedelta64(1, "h")
        expected_times = np.arange(
            np.datetime64("2013-11-01T00", "m"),
            np.datetime64("2014-01-02T00", "m"),
            np.timedelta64(10, "m"),
        ).astype("datetime64[ns]")
        check(sid + ":full_grid", np.array_equal(times, expected_times))
        values = np.array([float(r["internet"]) for r in csv_rows])
        nov_mask = (times >= np.datetime64("2013-11-01")) & (times < np.datetime64("2013-12-01"))
        nov, nov_times = values[nov_mask], times[nov_mask]
        check(sid + ":november_grid", np.array_equal(nov_times, nov_grid))
        fields = dict(
            cell_id=cid,
            bytes=len(raw),
            sha256=hashlib.sha256(raw).hexdigest(),
            git_blob_sha=blob,
            rows=len(csv_rows),
            first_local=date_str(times.min()),
            last_local=date_str(times.max()),
            duplicate_timestamps=int(len(times) - len(np.unique(times))),
            interval_seconds=sorted(set(np.diff(times.astype(np.int64)) / 1e9)),
            november_rows=len(nov),
            november_expected=4320,
            missing_november_timestamps=int(len(np.setdiff1d(nov_grid, nov_times))),
            november_nan=int(np.isnan(nov).sum()),
            november_zero=int((nov == 0).sum()),
            november_negative=int((nov < 0).sum()),
        )
        for k, v in fields.items():
            check(sid + ":" + k, record[k] == v)
        check(sid + ":all_finite_positive", np.isfinite(values).all() and (values > 0).all())
        csv_report.append(
            fields | dict(full_days=len(csv_rows) / 144, all_rows_finite_positive=True)
        )
        fine.append(nov)
    fine = np.stack(fine)
    check(
        "downloaded_bytes",
        subset["bytes_downloaded"] == sum(r["bytes"] for r in csv_report) == 1302989,
    )
    diffs = changes(initial, subset)
    allowed = {"/correction_note"} | {
        f"/records/{i}/{k}"
        for i in range(3)
        for k in ["interval_seconds/0", "timestamp_reporting_correction"]
    }
    check("timestamp_only_semantic_changes", {d["path"] for d in diffs} == allowed)
    for i in range(3):
        check(
            f"timestamp_correction_{i}",
            initial["records"][i]["interval_seconds"] == [0.6]
            and subset["records"][i]["interval_seconds"] == [600.0],
        )

    groups = fine.reshape(3, 720, 6)
    ratio = groups.max(axis=2) / groups.mean(axis=2)
    structure = dict(
        within_hour_variance_fraction=(groups.var(axis=2).mean(axis=1) / fine.var(axis=1)).tolist(),
        within_hour_peak_to_mean_median=np.median(ratio, axis=1).tolist(),
        within_hour_peak_to_mean_p95=np.quantile(ratio, 0.95, axis=1).tolist(),
    )
    for k, v in structure.items():
        same("structure:" + k, summary["structure"][k], v)
    with np.load(io.BytesIO(RAW["SRC-0030767"]), allow_pickle=False) as bank:
        arrays = {k: bank[k] for k in bank.files}
    methods = ["persistence", "daily_naive", "weekly_naive"] + [
        f"{feat}_{est}_{pool}"
        for feat in ["S", "S+L"]
        for est in ["Ridge", "HGB"]
        for pool in ["global", "local"]
    ]
    keys = {
        f"minutes_{step}_{k}" for step in [10, 60] for k in ["y", "scales", "times"] + methods[3:]
    }
    check("NPZ_exact_keys", set(arrays) == keys and len(keys) == 22)
    res_report, pooled, lag_effects = [], [], []
    for step, rec in zip([10, 60], summary["resolutions"], strict=True):
        nday = 1440 // step
        data = fine if step == 10 else groups.sum(axis=2)
        scales = data[:, : 20 * nday].mean(axis=1)
        z = data / scales[:, None]
        start, stop = 20 * nday, 30 * nday
        targets = np.arange(start, stop)
        times = np.arange(
            np.datetime64("2013-11-21T00", "m"),
            np.datetime64("2013-12-01T00", "m"),
            np.timedelta64(step, "m"),
        ).astype("datetime64[ns]")
        prefix = f"minutes_{step}_"
        check(
            prefix + "dtypes",
            all(
                v.dtype == (np.dtype("int64") if k.endswith("_times") else np.dtype("float64"))
                and np.isfinite(v).all()
                for k, v in arrays.items()
                if k.startswith(prefix)
            ),
        )
        same(prefix + "scales_summary", rec["scales"], scales)
        same(prefix + "scales_saved", arrays[prefix + "scales"], scales)
        same(prefix + "y_saved", arrays[prefix + "y"], z[:, targets])
        check(
            prefix + "times_exact", np.array_equal(arrays[prefix + "times"], times.astype(np.int64))
        )
        check(
            prefix + "rows_and_order",
            rec["minutes"] == step
            and rec["train_rows_per_cell"] == 13 * nday
            and rec["query_rows_per_cell"] == 10 * nday
            and [m["method"] for m in rec["methods"]] == methods,
        )
        y = arrays[prefix + "y"]
        errors, reported = {}, []
        for row in rec["methods"]:
            method = row["method"]
            pred = (
                z[
                    :,
                    targets
                    - {"persistence": 1, "daily_naive": nday, "weekly_naive": 7 * nday}[method],
                ]
                if method in methods[:3]
                else arrays[prefix + method]
            )
            check(prefix + method + ":shape", pred.shape == y.shape == (3, 10 * nday))
            error = np.abs(pred - y)
            errors[method] = error
            vals = dict(
                normalized_mae=float(error.mean()),
                per_cell_normalized_mae=error.mean(axis=1).tolist(),
                normalized_mae_halves=[
                    float(error[:, : 5 * nday].mean()),
                    float(error[:, 5 * nday :].mean()),
                ],
                per_cell_raw_mae=(error * scales[:, None]).mean(axis=1).tolist(),
            )
            check(prefix + method + ":metric_keys", set(row) == {"method"} | set(vals))
            for k, v in vals.items():
                same(
                    prefix + method + ":" + k,
                    row[k],
                    v,
                    atol=1e-10 if k == "per_cell_raw_mae" else 1e-12,
                )
            reported.append(dict(method=method, **vals))
        for feat in ["S", "S+L"]:
            for est in ["Ridge", "HGB"]:
                delta = errors[f"{feat}_{est}_global"] - errors[f"{feat}_{est}_local"]
                pooled.append(
                    dict(
                        minutes=step,
                        features=feat,
                        estimator=est,
                        global_minus_local=float(delta.mean()),
                        per_cell=delta.mean(axis=1).tolist(),
                        halves=[
                            float(delta[:, : 5 * nday].mean()),
                            float(delta[:, 5 * nday :].mean()),
                        ],
                    )
                )
        for est in ["Ridge", "HGB"]:
            for pool in ["global", "local"]:
                delta = errors[f"S+L_{est}_{pool}"] - errors[f"S_{est}_{pool}"]
                lag_effects.append(
                    dict(
                        minutes=step,
                        estimator=est,
                        pooling=pool,
                        with_lags_minus_without=float(delta.mean()),
                        per_cell=delta.mean(axis=1).tolist(),
                        halves=[
                            float(delta[:, : 5 * nday].mean()),
                            float(delta[:, 5 * nday :].mean()),
                        ],
                    )
                )
        raw_pcc = np.corrcoef(z[:, start:stop])
        profile = z[:, :start].reshape(3, 20, nday).mean(axis=1)
        residual_pcc = np.corrcoef(z[:, start:stop] - np.tile(profile, (1, 10)))
        same(prefix + "raw_pcc", rec["raw_diagnostic_pcc"], raw_pcc)
        same(prefix + "residual_pcc", rec["daily_profile_residual_diagnostic_pcc"], residual_pcc)
        res_report.append(
            dict(
                minutes=step,
                scales=scales.tolist(),
                train_rows_per_cell=13 * nday,
                train_rows_global=3 * 13 * nday,
                query_rows_per_cell=10 * nday,
                train_first="2013-11-08 00:00:00",
                train_last=date_str(times[0] - np.timedelta64(step, "m")),
                diagnostic_first=date_str(times[0]),
                diagnostic_last=date_str(times[-1]),
                methods=reported,
                raw_pcc=raw_pcc.tolist(),
                residual_pcc=residual_pcc.tolist(),
                feature_dimensions=[8, 16],
                recent_lag_minutes=[8 * step, step],
                actual_fit_X_saved=False,
                model_objects_saved=False,
            )
        )

    records = summary["fit_records"]
    expected_groups = [
        (step, feat, est, pool)
        for step in [10, 60]
        for feat in ["S", "S+L"]
        for est in ["Ridge", "HGB"]
        for pool in ["global", "local"]
    ]
    check(
        "fit_group_order",
        [(r["minutes"], r["features"], r["estimator"], r["pooling"]) for r in records]
        == expected_groups,
    )
    for i, r in enumerate(records):
        check(
            f"fit_record_{i}",
            r["fits"] == (1 if r["pooling"] == "global" else 3)
            and r["train_rows_per_cell"] == 13 * (1440 // r["minutes"])
            and r["query_rows"] == 30 * (1440 // r["minutes"])
            and r["fit_predict_seconds"] > 0,
        )
    check(
        "fits_32",
        sum(r["fits"] for r in records) == summary["new_simple_fits"] == cfg["fit_cap"] == 32,
    )
    fit_sum = sum(r["fit_predict_seconds"] for r in records)
    check("elapsed_scope", 0 < fit_sum < summary["elapsed_seconds"] < cfg["wall_seconds_cap"] == 60)
    check("sampled_rss_scope", 0 < summary["peak_rss_bytes"] < cfg["rss_cap_bytes"] == 2 * 1024**3)
    check(
        "not_representative_not_new_cluster",
        summary["representative_sample"] is False
        and summary["new_clustering_recommended"] is False
        and subset["representative_sample"] is False,
    )
    ledger = obj("SRC-0022700")
    stage = [r for r in ledger["cheap_stage_details"] if r["stage"] == "resolution_diagnostic_31"]
    check("ledger_unique_stage", len(stage) == 1)
    same(
        "ledger_elapsed",
        ledger["new_cheap_diagnostic_seconds"]["resolution_diagnostic_31"],
        summary["elapsed_seconds"],
    )
    check(
        "ledger_stage_cost",
        stage[0]
        == dict(
            stage="resolution_diagnostic_31",
            new_simple_fits=32,
            methods=["Ridge", "HGB"],
            resolutions_minutes=[10, 60],
            entire_stage_seconds=summary["elapsed_seconds"],
            fit_predict_seconds_included_in_stage=fit_sum,
            peak_rss_bytes=summary["peak_rss_bytes"],
            cost_not_counted_twice=True,
        ),
    )
    proof = dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks=len(CHECKS),
        check_names=CHECKS,
        source_identities=len(ROWS),
        source_bytes=sum(len(x) for x in RAW.values()),
        CSV=csv_report,
        timestamp_correction_changes=diffs,
        structure=structure,
        resolutions=res_report,
        pooling_deltas=pooled,
        lag_addition_deltas=lag_effects,
        cost=dict(
            historical_simple_fits=32,
            groups=16,
            fit_predict_seconds_sum=fit_sum,
            stage_elapsed_seconds=summary["elapsed_seconds"],
            sampled_peak_rss_bytes=summary["peak_rss_bytes"],
            times_overlap=True,
            continuous_peak_unverified=True,
        ),
        limitations=[
            "No model fit/predict or original-script import/execution.",
            "Targets/scales/naives reconstructed from CSV; "
            "actual historical fit X and model objects are unavailable.",
            "This checks saved arithmetic, not an independent model reproduction.",
            "10-minute and hourly MAEs use different target aggregations/scales.",
        ],
        new_model_runs=0,
    )
    return proof


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify(args.manifest)
    encoded = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(encoded.encode("utf-8"))
    print(
        json.dumps(
            {
                k: report[k]
                for k in ["success", "checks", "source_identities", "cost", "new_model_runs"]
            },
            ensure_ascii=False,
        )
    )
