"""Audit saved 639 predictions and reuse provenance without model execution."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import numpy as np

BASE = "tmp/redesign_20260925/"
STAGE = "results/bounded_relation_RCTL_bridge_639/"
PERIODS = {"first240": (0, 240), "last240": (240, 480), "all480": (0, 480)}


def verify(source: Path) -> dict:
    manifest = json.loads(source.read_text(encoding="utf-8")) if source.is_file() else None
    mapping = {r["path"]: r for r in manifest["sources"]} if manifest else {}
    accessed, dependencies, skipped = {}, [], []
    counts, failures, differences = Counter(), [], []

    def check(name, condition):
        counts[name] += 1
        if not bool(condition):
            failures.append({"check": name, "occurrence": counts[name]})

    def close(name, actual, expected, tolerance=1e-12):
        delta = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
        differences.append(delta)
        check(name, np.isfinite(delta) and delta < tolerance)

    def path(relative):
        key = BASE + relative
        p = source.parent / mapping[key]["archive_path"] if manifest else source / key
        if key not in accessed:
            data = p.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            accessed[key] = {"path": key, "sha256": digest, "size_bytes": len(data)}
            if manifest:
                check("portable_hash", digest == mapping[key]["sha256"])
        return p

    def read(relative):
        return json.loads(path(relative).read_text(encoding="utf-8-sig"))

    def array(relative):
        with np.load(path(relative), allow_pickle=False) as z:
            return {k: z[k].copy() for k in z.files}

    cfg = read(STAGE + "frozen_settings.json")
    reported = read(STAGE + "result.json")
    fits = read(STAGE + "fit_results.json")
    run = read(STAGE + "run_finished.json")
    started = read(STAGE + "run_started.json")
    settled = read(STAGE + "settled.json")
    contract = read("639_execution_contract.json")
    for relative, expected in cfg["source_hashes"].items():
        key = BASE + relative
        if manifest and not mapping.get(key, {}).get("archive_path"):
            skipped.append(key)
            continue
        p = source.parent / mapping[key]["archive_path"] if manifest else source / key
        with p.open("rb") as stream:
            actual = hashlib.file_digest(stream, "sha256").hexdigest()
        dependencies.append({"path": key, "sha256": actual, "matches": actual == expected})
        check("frozen_dependency_hash", actual == expected)
    for key in ["tasks", "cohorts", "partitions", "comparison_pairs"]:
        check("contract_matches_frozen", cfg[key] == contract[key])
    fixed = dict(
        seed=20260925,
        steps=8,
        channels=9,
        max_epochs=80,
        batch_size=256,
        patience=10,
        learning_rate=0.001,
        adam_eps=1e-7,
        loss="MAE",
        train_targets=[168, 839],
        validation_targets=[840, 1007],
        test_targets=[1008, 1487],
    )
    check("fixed_protocol", all(cfg[k] == v for k, v in fixed.items()))
    check(
        "development_scope",
        cfg["all_periods_development"]
        and not cfg["RCTL_results_used_for_clustering"]
        and cfg["new_Tab_calls"] == 0,
    )
    co = cfg["cohorts"]["A"]
    prepared = array(co["prepared_arrays"])
    evaluation = array(STAGE + "evaluation_A.npz")
    prior_evaluation = array(co["evaluation_reference"])
    ids, scales = prepared["cell_ids"], prepared["scales"]
    truth = prepared["y"][:, prepared["times"] >= 1008].astype(np.float64)
    check(
        "prepared_arrays",
        prepared["seq"].shape == (16, 1320, 8, 9)
        and prepared["y"].shape == (16, 1320)
        and prepared["times"].tolist() == list(range(168, 1488)),
    )
    check(
        "prepared_finite",
        np.isfinite(prepared["seq"]).all()
        and np.isfinite(prepared["y"]).all()
        and np.isfinite(prepared["y"]).all()
        and np.isfinite(scales).all()
        and np.all(scales > 0),
    )
    check("cohort_identity", ids.tolist() == co["cell_ids"])
    for ev in [evaluation, prior_evaluation]:
        check(
            "evaluation_identity",
            np.array_equal(ev["test_y"], truth)
            and np.array_equal(ev["cell_ids"], ids)
            and np.array_equal(ev["scales"], scales)
            and ev["test_times"].tolist() == list(range(1008, 1488)),
        )
    selection = read("results/bounded_relation_precision_638/result.json")
    old_cfg = read("results/nonempty_assignment_RCTL_581/frozen_settings.json")
    for model in ["Tab", "HGB"]:
        check(
            "frozen_membership",
            cfg["partitions"]["A_" + model + "_relation"]
            == selection["assignments"][model]["labels"],
        )
    for name in ["A_UPC", "A_HGB_free"]:
        check("baseline_membership", cfg["partitions"][name] == old_cfg["partitions"][name])
    prior_path = read("results/frozen_adaptive_paths_rctl_367/frozen_settings.json")
    check(
        "historical_partition_alias",
        cfg["partitions"]["A_HGB_relation"] == prior_path["partitions"]["Tab_path"],
    )
    check(
        "sealed_before_training",
        datetime.fromisoformat(selection["at"])
        < datetime.fromisoformat(cfg["at"])
        < datetime.fromisoformat(started["at"]),
    )
    cores = []
    for name in [
        "fixed32_downstream_reference_336.py",
        "nonempty_RCTL_worker_581.py",
        "frozen_T_RCTL_recovery_325.py",
    ]:
        text = path(name).read_text(encoding="utf-8-sig")
        function = next(
            n for n in ast.parse(text).body if isinstance(n, ast.FunctionDef) and n.name == "train"
        )
        body = ast.get_source_segment(text, function)
        cores.append(body[body.index("            method, seed, cluster, members =") :])
    check(
        "training_core_identity",
        cores[0] == cores[1] == cores[2]
        and hashlib.sha256(cores[0].encode()).hexdigest() == cfg["training_core_sha256"],
    )

    predictions = {m: np.full((16, 480), np.nan) for m in cfg["partitions"]}
    provenance, new_epochs = [], []
    check(
        "receipts_consistent",
        len(fits) == len(cfg["tasks"]) == 16
        and fits == run["state"]["results"]
        and run["success"]
        and settled["success"],
    )
    for task, fit in zip(cfg["tasks"], fits, strict=True):
        method, group, members = task["method"], task["cluster"], task["members"]
        stem = f"{method}_{cfg['seed']}_cluster{group}"
        z = array(STAGE + stem + ".npz")
        check(
            "task_identity",
            all(task[k] == fit[k] for k in ["method", "seed", "cluster", "members"])
            and members == [i for i, g in enumerate(cfg["partitions"][method]) if g == group]
            and task["cell_ids"] == ids[members].tolist(),
        )
        check(
            "prediction_identity",
            z["members"].tolist() == members
            and z["cell_ids"].tolist() == ids[members].tolist()
            and z["prediction"].shape == (len(members), 480)
            and np.array_equal(z["y"], truth[members]),
        )
        predictions[method][members] = z["prediction"]
        if task["reuse"]:
            rec = task["reuse"]["record"]
            origin = rec["artifacts"][".npz"]
            check(
                "exact_prediction_reuse",
                fit["reused"]
                and path(STAGE + stem + ".npz").read_bytes()
                == path(origin["relative_path"]).read_bytes()
                == path(rec["completed_bridge_npz"]).read_bytes(),
            )
            old = read(rec["source_settings"])
            check("reuse_protocol", all(old[k] == v for k, v in fixed.items() if k in old))
            compared_fields = [k for k in fixed if k in old]
            missing_fields = [k for k in fixed if k not in old]
            check(
                "reuse_data_source",
                (
                    old.get("prepared_arrays") == co["prepared_arrays"]
                    or old.get("cohorts", {}).get("A", {}).get("prepared_arrays")
                    == co["prepared_arrays"]
                ),
            )
            history = read(rec["artifacts"]["_history.json"]["relative_path"])
            metadata = rec["fit_metadata"]
            origin_name = rec["stage"] + "/" + Path(origin["relative_path"]).name
        else:
            check(
                "new_group_scope",
                method == "A_Tab_relation" and group in [1, 2, 3] and not fit["reused"],
            )
            history, metadata = read(STAGE + stem + "_history.json"), fit
            new_epochs.append(len(history))
            origin_name = "new_in_639"
            compared_fields, missing_fields = list(fixed), []
        vals = np.array([h["val_mae"] for h in history])
        best = int(np.argmin(vals))
        check(
            "validation_checkpoint",
            len(history) == metadata["epochs_run"]
            and best + 1 == metadata["best_epoch"]
            and len(history) - best - 1 == 10
            and metadata["stop_reason"] == "validation_patience"
            and np.isfinite(vals).all(),
        )
        close("best_validation_value", vals[best], metadata["best_val_mae"])
        provenance.append(
            dict(
                method=method,
                cluster=group,
                cell_ids=task["cell_ids"],
                reused=bool(task["reuse"]),
                origin=origin_name,
                epochs=len(history),
                best_epoch=best + 1,
                protocol_fields_compared=compared_fields,
                protocol_fields_missing_from_settings=missing_fields,
            )
        )
    check(
        "fit_and_epoch_counts",
        new_epochs == [66, 53, 46]
        and sum(new_epochs)
        == run["state"]["epochs_started"]
        == run["state"]["epochs_completed"]
        == settled["RCTL_epochs"]
        == 165
        and sum(t["reused"] for t in provenance) == 13
        and run["state"]["fits_started"]
        == run["state"]["fits_completed"]
        == settled["RCTL_fits"]
        == 3,
    )
    close("training_seconds", settled["RCTL_seconds"], run["wall_seconds"])
    metrics, comparisons = {}, {}
    for method, pred in predictions.items():
        check("prediction_coverage", np.isfinite(pred).all())
        metrics[method] = {}
        for period, (lo, hi) in PERIODS.items():
            per = np.abs(pred[:, lo:hi] - truth[:, lo:hi]).mean(axis=1)
            normalized = float(per.mean())
            raw = float(np.mean(per * scales))
            values = dict(
                mean_cell_MAE=normalized, mean_cell_raw_MAE=raw, per_cell_MAE=per.tolist()
            )
            for field in values:
                close("metric_" + field, values[field], reported["metrics"][method][period][field])
            metrics[method][period] = values
    for key, candidate, baseline in cfg["comparison_pairs"]:
        comparisons[key] = {}
        for period in PERIODS:
            a, b = metrics[candidate][period], metrics[baseline][period]
            difference = np.asarray(a["per_cell_MAE"]) - b["per_cell_MAE"]
            delta = a["mean_cell_MAE"] - b["mean_cell_MAE"]
            values = dict(
                delta_MAE=delta,
                relative_delta=delta / b["mean_cell_MAE"],
                per_cell_delta_MAE=difference.tolist(),
                improved_cells=int(np.sum(difference < 0)),
                worsened_cells=int(np.sum(difference > 0)),
                equal_cells=int(np.sum(difference == 0)),
            )
            for field in values:
                close("change_" + field, values[field], reported["changes"][key][period][field])
            values["raw_relative_delta"] = a["mean_cell_raw_MAE"] / b["mean_cell_raw_MAE"] - 1
            comparisons[key][period] = values
        changes = comparisons[key]
        rel, front, back = (
            changes["all480"]["relative_delta"],
            changes["first240"]["delta_MAE"],
            changes["last240"]["delta_MAE"],
        )
        branch = (
            "stable_gain"
            if rel <= -0.01 and front < 0 and back < 0
            else "stable_harm"
            if rel >= 0.01 and front > 0 and back > 0
            else "mixed_or_small"
        )
        check("decision_branch", branch == reported["branches"][key])
    return dict(
        created_at_utc=datetime.now(UTC).isoformat(),
        success=not failures,
        check_categories=dict(counts),
        failures=failures,
        maximum_numeric_difference=max(differences),
        new_model_calls=0,
        cell_ids=ids.tolist(),
        scales=scales.tolist(),
        metrics=metrics,
        comparisons=comparisons,
        provenance=provenance,
        new_epochs=new_epochs,
        accessed_sources=list(accessed.values()),
        verified_dependency_hashes=dependencies,
        external_dependencies_not_rechecked=skipped,
        scope=(
            "Saved predictions, metadata, histories and static training-core comparison; "
            "no model execution or upstream data-generation replication"
        ),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = verify(args.source)
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
                    "failures",
                    "maximum_numeric_difference",
                    "new_epochs",
                    "new_model_calls",
                ]
            }
        )
    )
    if not report["success"]:
        raise SystemExit(1)
