"""33–35번의 보존 예측과 집계를 검산한다. 모델·과거 코드는 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
from datetime import UTC, datetime
from pathlib import Path, PurePosixPath

import numpy as np


def verify(manifest_path: Path) -> dict:
    """보존 사본·입력·오차·비용을 대조하며 checkpoint는 metadata만 확인한다."""
    manifest_path = manifest_path.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks = []

    def ck(name, ok):
        """실패한 조건을 식별하고 성공한 검사 이름을 기록한다."""
        if not ok:
            raise ValueError(name)
        checks.append(name)

    def same(name, a, b, atol=1e-12):
        """같은 형태의 유한 배열을 절대 허용오차로 비교한다."""
        aa, bb = np.asarray(a), np.asarray(b)
        ck(
            name,
            aa.shape == bb.shape
            and np.isfinite(aa).all()
            and np.isfinite(bb).all()
            and np.allclose(aa, bb, rtol=0, atol=atol),
        )

    entries = manifest["sources"] + manifest["primary_sources"] + manifest["hash_only_sources"]
    ck("unique_source_ids", len({r["source_id"] for r in entries}) == len(entries))
    ck("unique_source_paths", len({r["path"] for r in entries}) == len(entries))
    all_rows = {r["path"]: r for r in entries}
    raw = {}
    for r in manifest["sources"]:
        path = (manifest_path.parent / r["archive_path"]).resolve()
        ck(r["source_id"] + ":bounded_path", path.is_relative_to(manifest_path.parents[2]))
        content = path.read_bytes()
        ck(
            r["source_id"] + ":identity",
            len(content) == r["size_bytes"] and hashlib.sha256(content).hexdigest() == r["sha256"],
        )
        raw[r["path"]] = content

    def identity(path):
        """해시를 확인한 보존 사본의 바이트를 찾는다."""
        return raw[path.as_posix()]

    def read(path):
        """검증한 보존 JSON을 읽는다."""
        return json.loads(identity(path))

    base = PurePosixPath("tmp/redesign_20260925")
    out = base / "results/frozen_fit_gap_34"
    summary, partial, cfg, started = [
        read(out / name)
        for name in ["summary.json", "partial.json", "settings.json", "run_started.json"]
    ]
    ck("settings_copy", summary["settings"] == cfg)
    ck(
        "settings_hash",
        hashlib.sha256(identity(out / "settings.json")).hexdigest() == started["settings_sha256"],
    )
    hash_names = {
        "plan_sha256": base / "34_frozen_fit_gap_plan.md",
        "code_sha256": base / "frozen_fit_gap_34.py",
        "model_code_sha256": base / "rctl_torch.py",
        "fit_results_sha256": base / "results/rctl_pilot/fit_results.json",
        "design_data_sha256": base / "results/design_data.npz",
    }
    for key, path in hash_names.items():
        ck(key, hashlib.sha256(identity(path)).hexdigest() == cfg[key])
    proposal = base / "results/observed_risk_pilot.json"
    identity(proposal)
    frozen = base / "results/rctl_pilot/frozen_settings.json"
    identity(frozen)
    ck("frozen_model_code", read(frozen)["model_code_sha256"] == cfg["model_code_sha256"])
    fits = read(hash_names["fit_results_sha256"])
    ids = np.asarray(read(proposal)["cell_ids"], dtype=np.int64)
    with np.load(
        io.BytesIO(identity(hash_names["design_data_sha256"])), allow_pickle=False
    ) as archive:
        sel = np.array([np.flatnonzero(archive["cell_indices"] == cid - 1).item() for cid in ids])
        truth = archive["Y"][sel]
        times = archive["times"]
        feature_shape = archive["X"][sel].shape
        ck("design_shapes", feature_shape == (16, 840, 16) and truth.shape == (16, 840))
        ck("design_finite", np.isfinite(archive["X"][sel]).all() and np.isfinite(truth).all())
        ck("design_times", np.array_equal(times, np.arange(168, 1008)))
    splits = {"train": times < 840, "validation": times >= 840}
    ck(
        "fixed_splits",
        cfg["train_target_indices"] == [168, 839]
        and cfg["validation_target_indices"] == [840, 1007],
    )
    ck("split_sizes", sum(splits["train"]) == 672 and sum(splits["validation"]) == 168)
    ck("float32_target", truth.dtype == np.float32)
    ck(
        "counts_config",
        len(fits) == len(summary["records"]) == cfg["checkpoint_count"] == 29
        and cfg["batch"] == 512,
    )
    ck("partial_records", partial["records"] == summary["records"])
    ck(
        "historical_no_newfit",
        summary["complete"]
        and summary["new_RCTL_fits"]
        == summary["new_TabICL_contexts"]
        == cfg["test_forward_calls"]
        == 0
        and summary["partitions_modified"] is False
        and cfg["result_used_to_change_partitions"] is False,
    )
    records = []
    groups = {}
    forward_calls = 0
    rows = 0
    max_mae_diff = 0
    validation_errors = {}
    expected_keys = {"cell_ids", "train_y", "validation_y"}
    with np.load(io.BytesIO(identity(out / "predictions.npz")), allow_pickle=False) as arrays:
        ck(
            "NPZ_ids",
            arrays["cell_ids"].dtype == np.int64 and np.array_equal(arrays["cell_ids"], ids),
        )
        for split, mask in splits.items():
            same(split + ":truth", arrays[split + "_y"], truth[:, mask], atol=0)
        for r, fit in zip(summary["records"], fits, strict=True):
            key = f"{r['method']}_{r['seed']}_cluster{r['cluster']}"
            members = np.asarray(r["members"], dtype=int)
            ck(
                key + ":metadata",
                all(
                    r[k] == fit[k]
                    for k in [
                        "method",
                        "seed",
                        "cluster",
                        "members",
                        "epochs_run",
                        "best_epoch",
                        "fit_seconds",
                    ]
                ),
            )
            ck(
                key + ":members",
                len(set(members)) == len(members) and np.all((0 <= members) & (members < 16)),
            )
            path = base / f"results/rctl_pilot/{key}.pt"
            metadata = all_rows[path.as_posix()]
            ck(
                key + ":checkpoint_metadata",
                metadata["sha256"] == r["checkpoint_sha256"]
                and metadata["size_bytes"] == r["checkpoint_file_bytes"],
            )
            train_rows = len(members) * 672
            steps = r["epochs_run"] * math.ceil(train_rows / 256)
            ck(key + ":training_rows", r["training_rows_per_epoch"] == train_rows)
            ck(key + ":training_steps", r["original_optimizer_steps"] == steps)
            ck(key + ":training_seen", r["original_rows_seen"] == r["epochs_run"] * train_rows)
            same(key + ":test_copy", r["saved_test_mae"], fit["test_mean_scaled_mae"], 0)
            ck(
                key + ":positive_times",
                all(
                    np.isfinite(r[k]) and r[k] >= 0
                    for k in [
                        "fit_seconds",
                        "checkpoint_load_seconds",
                        "train_predict_seconds",
                        "validation_predict_seconds",
                    ]
                ),
            )
            ck(
                key + ":saved_unchanged_reports",
                r["checkpoint_file_unchanged"] is True and r["model_state_unchanged"] is True,
            )
            group = groups.setdefault(
                (r["method"], r["seed"]),
                dict(
                    keys=[],
                    members=[],
                    train=np.full(16, np.nan),
                    validation=np.full(16, np.nan),
                    saved_test=np.full(16, np.nan),
                    records=[],
                ),
            )
            group["keys"].append(key)
            group["members"].extend(members.tolist())
            group["records"].append(r)
            group_id = (r["method"], r["seed"])
            validation_errors.setdefault(group_id, np.full((16, 168), np.nan))
            row = dict(
                key=key,
                members=r["members"],
                epochs=r["epochs_run"],
                best_epoch=r["best_epoch"],
                steps=steps,
                train_rows=train_rows,
            )
            for split, mask in splits.items():
                arrkey = key + "_" + split + "_prediction"
                expected_keys.add(arrkey)
                pred = arrays[arrkey]
                target = truth[members][:, mask]
                ck(
                    arrkey + ":shape_dtype",
                    pred.shape == target.shape
                    and pred.dtype == np.float32
                    and np.isfinite(pred).all(),
                )
                errors = np.abs(pred - target)
                per = errors.mean(1)
                if split == "validation":
                    validation_errors[group_id][members] = errors
                same(key + ":" + split + "_mae", float(errors.mean()), r[split + "_mae"], atol=1e-8)
                same(key + ":" + split + "_per_cell", per, r[split + "_per_cell_mae"], atol=1e-8)
                max_mae_diff = max(
                    max_mae_diff,
                    abs(float(errors.mean()) - r[split + "_mae"]),
                    float(np.max(np.abs(per.astype(float) - r[split + "_per_cell_mae"]))),
                )
                ck(key + ":" + split + "_nonoverlap", np.isnan(group[split][members]).all())
                group[split][members] = per.astype(float)
                row[split + "_mae"] = float(errors.mean())
                nrows = len(members) * int(mask.sum())
                forward_calls += math.ceil(nrows / cfg["batch"])
                rows += nrows
            group["saved_test"][members] = fit["test_per_cell_mae"]
            same(
                key + ":validation_repro",
                abs(r["validation_mae"] - fit["best_val_mae"]),
                r["validation_reproduction_abs_difference"],
                0,
            )
            ck(
                key + ":validation_tolerance",
                r["validation_reproduction_abs_difference"] <= cfg["validation_tolerance"],
            )
            records.append(row)
        ck("NPZ_exact_keys", set(arrays.files) == expected_keys and len(arrays.files) == 61)
    global_group = groups[("global", 20260925)]
    aggregates = []
    for a in summary["aggregates"]:
        key = (a["method"], a["seed"])
        g = groups[key]
        tag = str(key)
        ck(tag + ":partition", sorted(g["members"]) == list(range(16)))
        ck(
            tag + ":clusters",
            a["clusters"] == g["keys"] and a["cluster_count"] == len(g["records"]),
        )
        row = dict(method=a["method"], seed=a["seed"], clusters=a["cluster_count"])
        for split in ["train", "validation", "saved_test"]:
            same(tag + ":" + split + "_per_cell", g[split], a["per_cell_" + split + "_mae"], 1e-8)
            same(tag + ":" + split + "_mean", g[split].mean(), a[split + "_mae"], 1e-8)
            delta = g[split] - global_group[split]
            same(
                tag + ":" + split + "_difference",
                g[split].mean() - global_group[split].mean(),
                a[split + "_difference_vs_primary_global"],
                1e-8,
            )
            row[split + "_mae"] = float(g[split].mean())
            row[split + "_difference"] = float(delta.mean())
            row[split + "_lower_count"] = int((delta < 0).sum())
            row[split + "_higher_count"] = int((delta > 0).sum())
            row[split + "_per_cell_delta"] = delta.tolist()
        same(
            tag + ":val_minus_train",
            g["validation"].mean() - g["train"].mean(),
            a["validation_minus_train"],
            1e-8,
        )
        for field in [
            "original_optimizer_steps",
            "original_rows_seen",
            "fit_seconds",
            "epochs_run",
            "state_tensor_bytes",
            "checkpoint_file_bytes",
            "parameter_count",
            "trainable_parameter_count",
        ]:
            total = sum(r[field] for r in g["records"])
            same(tag + ":total_" + field, total, a["total_" + field], 1e-12)
            row["total_" + field] = total
        aggregates.append(row)
    ck("aggregate_count", len(aggregates) == 8 and len(groups) == 8)
    ck(
        "forward_row_accounting",
        forward_calls == cfg["expected_forward_calls"] == summary["counts"]["forward_calls"] == 251
        and rows == cfg["expected_predicted_rows"] == summary["counts"]["predicted_rows"] == 107520,
    )
    ck(
        "partial_counter_scope",
        all(
            partial["counts"][k] == summary["counts"][k]
            for k in ["forward_calls", "predicted_rows"]
        )
        and partial["counts"]["peak_rss_bytes"] <= summary["counts"]["peak_rss_bytes"],
    )
    ck(
        "stored_repro_max",
        summary["max_validation_reproduction_abs_difference"]
        == max(r["validation_reproduction_abs_difference"] for r in summary["records"])
        == 0,
    )
    ck("stored_checkpoint_report", summary["checkpoints_unchanged"] is True)
    ck(
        "resource_bounds",
        summary["entire_stage_seconds"] < cfg["wall_cap_seconds"]
        and summary["counts"]["peak_rss_bytes"] < cfg["rss_cap_bytes"],
    )
    # The archive adds descriptive halves of the same saved validation period.
    halves = []
    reference = validation_errors[("global", 20260925)]
    for (method, seed), errors in validation_errors.items():
        ck(
            str((method, seed)) + ":half_error_shape",
            errors.shape == (16, 168) and np.isfinite(errors).all(),
        )
        delta = errors - reference
        row = dict(
            method=method,
            seed=seed,
            whole_delta=float(delta.mean()),
            first84_delta=float(delta[:, :84].mean()),
            last84_delta=float(delta[:, 84:].mean()),
            first84_harmed_cells=int((delta[:, :84].mean(1) > 0).sum()),
            last84_harmed_cells=int((delta[:, 84:].mean(1) > 0).sum()),
        )
        same(
            str((method, seed)) + ":half_weighting",
            row["whole_delta"],
            (row["first84_delta"] + row["last84_delta"]) / 2,
            1e-12,
        )
        halves.append(row)
    fs = [16, 32, 64, 64, 32, 16]
    params = (
        sum(5 * inc * c + 11 * c * c + 16 * c for inc, c in zip([9] + fs[:-1], fs, strict=True))
        + sum(c * c + c for c in fs[:3])
        + 9 * 16
        + 16
        + 8 * 16
        + 1
    )
    frozen_bias = 4 * sum(fs)
    float_buffers = 4 * sum(fs)
    integer_buffers = 2 * len(fs)
    parameter_counts = dict(
        parameter_count=params,
        trainable_parameter_count=params - frozen_bias,
        buffer_element_count=float_buffers + integer_buffers,
        state_tensor_bytes=(params + float_buffers) * 4 + integer_buffers * 8,
    )
    for key, value in parameter_counts.items():
        ck(key + ":static_formula", all(r[key] == value for r in summary["records"]))
    ck(
        "fixed_settings",
        cfg["model_mode"] == "eval/inference_mode"
        and cfg["validation_tolerance"] == 1e-6
        and cfg["wall_cap_seconds"] == 300
        and cfg["rss_cap_bytes"] == 2 * 1024**3,
    )
    training = read(frozen)
    ck(
        "training_settings",
        training["batch_size"] == 256
        and training["max_epochs"] == 80
        and training["patience"] == 10
        and training["loss"] == "MAE"
        and training["learning_rate"] == 0.001
        and training["adam_eps"] == 1e-7
        and training["seed_primary"] == 20260925
        and training["seed_secondary"] == 20260926,
    )
    ledger = read(base / "cumulative_execution_budget.json")
    stages = [v for v in ledger["inference_only_stages"] if v["stage"] == "frozen_fit_gap_34"]
    ck("one_ledger_stage", len(stages) == 1)
    stage = stages[0]
    ck(
        "ledger_stage_fields",
        stage["RCTL_fits"] == stage["TabICL_contexts"] == 0
        and stage["forward_calls"] == 251
        and stage["predicted_rows"] == 107520
        and stage["peak_rss_bytes"] == summary["counts"]["peak_rss_bytes"]
        and stage["precommitted_stage_wall_cap_seconds"] == 300
        and stage["counts_toward_total_local_modeling"] is True,
    )
    same("ledger_stage_seconds", stage["wall_seconds"], summary["entire_stage_seconds"], 0)
    initial_inference = [
        v
        for v in ledger["inference_only_stages"]
        if v["stage"] in ["frozen_recursive_horizon", "frozen_fit_gap_34"]
    ]
    ck("initial_inference_two", len(initial_inference) == 2)
    frozen_seconds = sum(v["wall_seconds"] for v in initial_inference)
    same("reported_frozen_prefix", frozen_seconds, 9.8678484, 1e-9)
    tab_names = [
        "smoke",
        "B1_anchor_and_cross_query",
        "B2_observed_query",
        "cell_identity_information_diagnostic",
        "broad_cell_information",
        "target_parameterization",
    ]
    tab_stages = [v for v in ledger["model_calls_by_stage"] if v["stage"] in tab_names]
    ck(
        "initial_tab_stages",
        len(tab_stages) == 6 and {v["stage"] for v in tab_stages} == set(tab_names),
    )
    tab_contexts = sum(v["contexts"] for v in tab_stages)
    tab_rows = sum(v["predicted_query_rows"] for v in tab_stages)
    ck("reported_initial_tab_counts", tab_contexts == 45 and tab_rows == 35712)
    tab_seconds = sum(v["fit_predict_seconds"] for v in tab_stages)
    cheap_names = [
        "finite_sample_information.json",
        "population_scope_diagnostic.json",
        "upc_core_stability.json",
        "upc_transfer_diagnostic.json",
        "cell_identity_simple_Ridge_and_HGB",
        "broad_cell_information_simple_Ridge_and_HGB",
        "target_parameterization_simple_Ridge_and_HGB",
        "temporal_validity",
        "spatial_information",
        "error_concentration",
        "conditional_pooling_cost",
        "observable_state_loss",
        "resolution_diagnostic_31",
    ]
    cheap_seconds = sum(ledger["new_cheap_diagnostic_seconds"][n] for n in cheap_names)
    fit_execution = read(base / "results/rctl_pilot/summary.json")["execution"]
    ck(
        "original_fit_count",
        fit_execution["fits_completed"] == 29
        and fit_execution["epochs_total"] == sum(r["epochs_run"] for r in fits) == 1565,
    )
    total = tab_seconds + fit_execution["wall_seconds"] + frozen_seconds + cheap_seconds
    same("reported_modeling_prefix", total, 1947.6645694, 1e-9)
    cost = dict(
        TabICL_contexts=tab_contexts,
        TabICL_rows=tab_rows,
        TabICL_seconds=tab_seconds,
        RCTL_training_wall_seconds=fit_execution["wall_seconds"],
        RCTL_fit_seconds_sum=sum(r["fit_seconds"] for r in fits),
        RCTL_fits=29,
        RCTL_epochs=1565,
        frozen_seconds_through34=frozen_seconds,
        cheap_seconds_through31=cheap_seconds,
        reported_modeling_seconds_through34=total,
        stage_seconds=summary["entire_stage_seconds"],
        subtimers_seconds=sum(
            r[k]
            for r in summary["records"]
            for k in [
                "checkpoint_load_seconds",
                "train_predict_seconds",
                "validation_predict_seconds",
            ]
        ),
        sampled_RSS_bytes=summary["counts"]["peak_rss_bytes"],
        process_wall_reported_only_seconds=8.546827,
        cost_scope=(
            "Historical prefixes, not current ledger totals or complete work time; "
            "sub-timers overlap stage."
        ),
    )
    return dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks=len(checks),
        check_names=checks,
        preserved_identity_count=len(manifest["sources"]),
        checkpoint_metadata_only_count=29,
        records=records,
        aggregates=aggregates,
        validation_halves=halves,
        static_parameter_counts=parameter_counts,
        cost=cost,
        max_saved_prediction_mae_absolute_difference=max_mae_diff,
        counts=dict(
            forward_calls=forward_calls,
            predicted_rows=rows,
            saved_peak_rss_bytes=summary["counts"]["peak_rss_bytes"],
            partial_peak_rss_bytes=partial["counts"]["peak_rss_bytes"],
            stage_seconds=summary["entire_stage_seconds"],
        ),
        new_model_runs=0,
        original_scripts_imported=False,
        checkpoint_loaded_or_executed=False,
        limits=[
            "Saved arithmetic and cross-references, not model reproduction.",
            "Checkpoint identity here uses metadata; local original-byte audit is separate.",
            "Static architecture formula, not actual tensor metadata inspection.",
            "Test metrics copied from fit_results; no new test predictions.",
            "Timing and unchanged-state flags are historical reports, not remeasured behavior.",
        ],
    )


if __name__ == "__main__":
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
            {
                k: result[k]
                for k in [
                    "success",
                    "checks",
                    "preserved_identity_count",
                    "checkpoint_metadata_only_count",
                    "max_saved_prediction_mae_absolute_difference",
                    "new_model_runs",
                ]
            }
        )
    )
