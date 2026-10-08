"""Audit saved 641 controls and 639 result aliases without running research code."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import numpy as np

BASE = "tmp/redesign_20260925/"
CACHE = "results/bounded_relation_cache_resume_637/"
PRECISION = "results/bounded_relation_precision_638/"
STAGE = "results/cached_relation_score_ablation_641/"
RCTL = "results/bounded_relation_RCTL_bridge_639/"
MODELS = ["Tab", "HGB"]
CONTROLS = ["median_distance", "plugin_conflict"]


def verify(source: Path) -> dict:
    """Recompute frozen control costs and assignments, then audit existing RCTL aliases.

    Accept the original source root or a portable evidence manifest. RCTL prediction
    files are hashed, not loaded; their MAE was checked in the separate 639 audit.
    Historical scripts are never imported. Read scopes are included in the report.
    """
    manifest = json.loads(source.read_text(encoding="utf-8")) if source.is_file() else None
    mapping = {r["path"]: r for r in manifest["sources"]} if manifest else {}
    accessed, counts, differences = {}, Counter(), []

    def check(name, condition):
        """Stop on a failed invariant instead of emitting a successful partial report."""
        counts[name] += 1
        if not bool(condition):
            raise AssertionError((name, counts[name]))

    def path(relative, fields=None):
        """Resolve a source, hash its bytes, and record the fields actually accessed."""
        key = BASE + relative
        p = source.parent / mapping[key]["archive_path"] if manifest else source / key
        if key not in accessed:
            data = p.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            accessed[key] = dict(path=key, sha256=digest, size_bytes=len(data), read_scope=[])
            if manifest:
                check(
                    "portable_source_identity",
                    digest == mapping[key]["sha256"] and len(data) == mapping[key]["size_bytes"],
                )
        accessed[key]["read_scope"] = sorted(
            set(accessed[key]["read_scope"]) | set(fields or ["sha256_only"])
        )
        return p

    def read(relative):
        """Decode a historical JSON document without executing its instructions."""
        return json.loads(
            path(relative, ["json_loaded_selected_fields_checked"]).read_text(encoding="utf-8-sig")
        )

    def digest(relative):
        """Return the digest of the actual file, not a claimed digest in a result."""
        path(relative)
        return accessed[BASE + relative]["sha256"]

    def arrays(relative, keys):
        """Load only named arrays; disallow object-array deserialization."""
        with np.load(path(relative, ["array:" + k for k in keys]), allow_pickle=False) as data:
            return {key: data[key].copy() for key in keys}

    def close(name, actual, expected):
        """Compare finite numeric arrays at the frozen audit tolerance."""
        actual, expected = np.asarray(actual, dtype=float), np.asarray(expected, dtype=float)
        check(name + "_shape", actual.shape == expected.shape)
        difference = float(np.max(np.abs(actual - expected)))
        differences.append(difference)
        check(name, np.isfinite(difference) and difference < 1e-12)

    cfg = read(STAGE + "frozen_settings.json")
    result = read(STAGE + "result.json")
    sealed = read(STAGE + "assignment_sealed.json")
    alias = read(STAGE + "frozen_utility_alias.json")
    log_names = [
        "authorization",
        "run_started",
        "run_finished",
        "settled",
        "verification",
        "archive_complete",
        "review_manifest",
    ]
    logs = {name: read(STAGE + name + ".json") for name in log_names}
    for relative, expected in cfg["source_hashes"].items():
        check("frozen_source_hash", digest(relative) == expected)
    check(
        "settings_hash",
        digest(STAGE + "frozen_settings.json") == logs["authorization"]["settings_sha256"],
    )
    check("assignment_hash", digest(STAGE + "assignment_sealed.json") == alias["assignment_sha256"])
    check("result_success", result["success"] and alias["success"])
    check(
        "execution_success",
        all(
            logs[n]["success"]
            for n in ["run_finished", "settled", "verification", "archive_complete"]
        ),
    )
    check(
        "new_models_zero",
        all(
            v["new_models"] == 0
            for v in [
                cfg,
                result,
                sealed,
                alias,
                logs["run_finished"],
                logs["settled"],
                logs["verification"],
            ]
        ),
    )
    check("new_forecasts_zero", result["new_forecasts"] == alias["new_forward"] == 0)
    check(
        "no_RCTL_MAE_recalculation",
        not alias["new_MAE_computation"] and not alias["raw_prediction_arrays_loaded"],
    )
    check(
        "no_query_labels_or_RCTL_in_controls",
        not cfg["read_query_y"]
        and not cfg["read_RCTL"]
        and all(
            not v["query_y_read"] and not v["RCTL_read"]
            for v in [result, sealed, logs["verification"]]
        ),
    )
    check(
        "development_scope", all(v["all_periods_development"] for v in [cfg, result, sealed, alias])
    )
    check(
        "fixed_controls",
        cfg["models"] == MODELS
        and cfg["controls"] == CONTROLS
        and cfg["sweeps"] == 3
        and cfg["seed"] == 20260925,
    )
    check("quantile_levels", cfg["levels"] == [i / 10 for i in range(1, 10)])
    median_index = cfg["levels"].index(0.5)
    ordered = [
        logs["authorization"]["at"],
        logs["run_started"]["at"],
        sealed["at"],
        logs["verification"]["at"],
        result["at"],
        logs["run_finished"]["at"],
        logs["settled"]["at"],
        alias["at"],
        logs["archive_complete"]["at"],
    ]
    check(
        "chronology",
        all(
            datetime.fromisoformat(a) <= datetime.fromisoformat(b)
            for a, b in zip(ordered, ordered[1:], strict=False)
        ),
    )
    check(
        "assignment_then_alias",
        datetime.fromisoformat(sealed["at"]) < datetime.fromisoformat(alias["at"]),
    )
    check(
        "settlement",
        logs["run_finished"]["seconds"] == logs["settled"]["seconds"]
        and 0 <= logs["run_finished"]["seconds"] < cfg["seconds_cap"] == 12,
    )
    check(
        "cleanup", logs["run_finished"]["worker_reaped"] and logs["run_finished"]["failure"] is None
    )
    check(
        "ledger_chain",
        logs["settled"]["ledger_sha256"]
        == alias["ledger_sha256"]
        == logs["archive_complete"]["ledger_sha256"],
    )
    check(
        "no_cap_changes",
        logs["settled"]["cap_changes"] == logs["authorization"]["cap_changes"] == {},
    )
    inherited = read(CACHE + "frozen_settings.json")
    check(
        "inherited_637_metadata",
        all(
            cfg[k] == inherited[k]
            for k in [
                "at",
                "limits",
                "cell_ids",
                "initial_labels",
                "seed",
                "neighbors",
                "sweeps",
                "levels",
                "support_p",
                "min_each_half",
                "min_days",
            ]
        ),
    )

    graph = arrays(PRECISION + "graph_scores.npz", ["edges", "cell_ids", "initial_labels"])
    ids, initial = cfg["cell_ids"], cfg["initial_labels"]
    edges = [tuple(map(int, row)) for row in graph["edges"]]
    check(
        "graph_identity",
        graph["cell_ids"].tolist() == ids
        and graph["initial_labels"].tolist() == initial
        and len(ids) == 16
        and len(edges) == 22,
    )
    check(
        "unique_edges_and_K4",
        len(set(edges)) == 22
        and set(initial) == set(range(4))
        and all(0 <= i < j < 16 for i, j in edges),
    )
    active = sorted({i for edge in edges for i in edge})
    check("14_cache_cells", len(active) == 14)
    cells = {
        i: arrays(CACHE + f"cells/c{i}.npz", ["cell_id", "target_indices", "query_times", *MODELS])
        for i in active
    }
    times = cells[active[0]]["query_times"]
    check("64_ordered_queries", len(times) == 64 and np.all(np.diff(times) > 0))
    for i, data in cells.items():
        check(
            "cache_identity",
            int(data["cell_id"]) == ids[i] and np.array_equal(times, data["query_times"]),
        )
        check(
            "cache_shape",
            all(data[m].shape == (len(data["target_indices"]), 64, 9) for m in MODELS),
        )
    costs = {f"{m}_{c}": [] for m in MODELS for c in CONTROLS}
    mask_rows = []
    for i, j in edges:
        saved = {
            m: arrays(PRECISION + f"edges/{m}_{i}_{j}.npz", ["mask", "p", "w", "F0", "F1"])
            for m in MODELS
        }
        mask = saved["Tab"]["mask"]
        check(
            "same_support",
            mask.shape == (128,)
            and mask.dtype == bool
            and np.array_equal(mask, saved["HGB"]["mask"]),
        )
        # 638 edge files do not contain their own query timestamps. Their row order
        # follows the frozen 637 caches and is inherited from the separate 638 audit.
        check(
            "edge_field_shapes", all(a.shape == (128,) for z in saved.values() for a in z.values())
        )
        mask_rows.append(dict(cells=[ids[i], ids[j]], common_rows=int(mask.sum())))
        for off in [0, 64]:
            for begin in [0, 32]:
                selected = mask[off + begin : off + begin + 32]
                check(
                    "support_count_and_days",
                    selected.sum() >= 8
                    and len(np.unique(times[begin : begin + 32][selected] // 24)) >= 2,
                )
        for model in MODELS:
            z = saved[model]
            check("supported_probabilities", np.all((z["p"][mask] >= 0.1) & (z["p"][mask] <= 0.9)))
            check(
                "sign_from_frozen_CDF",
                np.array_equal(z["w"][mask], np.sign(z["F0"][mask] - z["F1"][mask])),
            )
            for name in CONTROLS:
                halves = []
                for begin in [0, 32]:
                    means = []
                    for off, target in [(0, i), (64, j)]:
                        first = cells[i]["target_indices"].tolist().index(target)
                        second = cells[j]["target_indices"].tolist().index(target)
                        terms = []
                        for t in range(begin, begin + 32):
                            k = off + t
                            if not mask[k]:
                                continue
                            if name == "median_distance":
                                value = abs(
                                    float(cells[i][model][first, t, median_index])
                                    - float(cells[j][model][second, t, median_index])
                                )
                            else:
                                p = float(z["p"][k])
                                value = (
                                    float(z["w"][k])
                                    * p
                                    * (1 - p)
                                    * (float(z["F0"][k]) - float(z["F1"][k]))
                                )
                            terms.append(value)
                        means.append(math.fsum(terms) / len(terms))
                    halves.append(max(0.0, math.fsum(means) / 2))
                costs[f"{model}_{name}"].append(halves)
    check("edge_records", mask_rows == result["edge_records"])
    stored = arrays(STAGE + "graph_scores.npz", ["edges", *costs])
    check("saved_edge_order", stored["edges"].tolist() == [list(pair) for pair in edges])

    assignments = {}
    for name, weights in costs.items():
        close("all_edge_costs", weights, stored[name])
        labels, moves = list(initial), []

        def objective(partition, weights=weights):
            """Recompute the entire within-group sum for each proposed partition."""
            return [
                math.fsum(
                    weights[k][half]
                    for k, (i, j) in enumerate(edges)
                    if partition[i] == partition[j]
                )
                for half in [0, 1]
            ]

        for sweep in range(cfg["sweeps"]):
            any_move = False
            for cell in range(len(ids)):
                src = labels[cell]
                if labels.count(src) == 1:
                    continue
                before = objective(labels)
                neighbors = {j if i == cell else i for i, j in edges if cell in (i, j)}
                candidates = []
                for destination in sorted(set(initial) - {src}):
                    if sum(labels[j] == destination for j in neighbors) < 2:
                        continue
                    proposal = list(labels)
                    proposal[cell] = destination
                    after = objective(proposal)
                    delta = [after[h] - before[h] for h in [0, 1]]
                    if max(delta) < -1e-12:
                        candidates.append((math.fsum(delta) / 2, destination))
                if candidates:
                    dest = min(candidates)[1]
                    moves.append((sweep, ids[cell], src, dest))
                    labels[cell], any_move = dest, True
            if not any_move:
                break
        expected = result["assignments"][name]
        check("control_labels", labels == expected["labels"] == initial)
        check("control_sealed", expected == sealed["assignments"][name])
        groups = [sorted(ids[i] for i, label in enumerate(labels) if label == g) for g in range(4)]
        check("control_groups", groups == expected["groups"])
        check(
            "control_no_moves",
            moves == expected["moves"] == expected["changed_cell_ids"] == []
            and expected["stop"] == "no_admissible_move",
        )
        close("initial_objective", objective(initial), expected["initial_objective"])
        close("final_objective", objective(labels), expected["final_objective"])
        assignments[name] = dict(
            labels=labels, groups=groups, objective=objective(labels), moves=moves
        )
    old_seal = read(PRECISION + "assignment_sealed.json")
    check("original_seal", sealed["original_assignments"] == old_seal["assignments"])
    equality = {
        name: sorted(a["groups"])
        == sorted(old_seal["assignments"][name.split("_", 1)[0]]["groups"])
        for name, a in assignments.items()
    }
    check(
        "different_from_observed_score",
        not any(equality.values())
        and equality == sealed["same_as_original"] == result["same_as_original"],
    )
    check(
        "decision_branch",
        sealed["branch"] == result["branch"] == "both_Tab_controls_different_assignment",
    )

    rcfg, rr = read(RCTL + "frozen_settings.json"), read(RCTL + "result.json")
    hashes = read(RCTL + "prediction_hashes.json")
    check(
        "RCTL_source_paths",
        alias["RCTL_protocol"] == BASE + RCTL + "frozen_settings.json"
        and alias["source_result"] == BASE + RCTL + "result.json",
    )
    check(
        "RCTL_source_hashes",
        digest(RCTL + "frozen_settings.json") == alias["RCTL_protocol_sha256"]
        and digest(RCTL + "result.json") == alias["source_result_sha256"],
    )
    check("same_actual_cohort", ids == rcfg["cohorts"]["A"]["cell_ids"])
    tasks = sorted([t for t in rcfg["tasks"] if t["method"] == "A_UPC"], key=lambda t: t["cluster"])
    check("four_control_aliases", set(alias["aliases"]) == set(assignments) and len(tasks) == 4)
    unique_artifacts = set()
    for name, entry in alias["aliases"].items():
        check("UPC_metrics_reused", entry["metrics"] == rr["metrics"]["A_UPC"])
        check(
            "UPC_groups_match",
            entry["same_partition_as"] == "A_UPC"
            and assignments[name]["groups"] == [g["cell_ids"] for g in entry["groups"]],
        )
        for group, task in zip(entry["groups"], tasks, strict=True):
            check(
                "UPC_task_identity",
                task["seed"] == 20260925
                and task["cluster"] == group["cluster"]
                and sorted(task["cell_ids"])
                == group["cell_ids"]
                == sorted(ids[i] for i in task["members"]),
            )
            relative = RCTL + f"A_UPC_20260925_cluster{group['cluster']}.npz"
            check("UPC_artifact_path", group["artifact"] == BASE + relative)
            check(
                "UPC_artifact_hash",
                digest(relative) == group["sha256"] == hashes[Path(relative).name],
            )
            unique_artifacts.add(relative)
    check("four_unique_UPC_files", len(unique_artifacts) == 4 and alias["group_alias_checks"] == 16)
    check("Tab_metrics_reused", alias["Tab_score_metrics"] == rr["metrics"]["A_Tab_relation"])
    if manifest:
        # Compare the final union, including human-only sources whose automatic
        # scope must remain empty. Catch both omitted and overstated field reads.
        for key, entry in mapping.items():
            actual = set(accessed.get(key, {}).get("read_scope", []))
            declared = set(entry["automated_read_scope"])
            check("declared_read_scope", actual == declared)
    return dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        scope=(
            "Saved 641 control arithmetic and 639 metric aliases; "
            "no new research or full-corpus review"
        ),
        checks=dict(counts),
        max_absolute_difference=max(differences),
        source_count=len(accessed),
        accessed=list(accessed.values()),
        assignments=assignments,
        edge_costs=costs,
        alias_slots=16,
        unique_UPC_artifacts=4,
        reused_metrics={
            name: rr["metrics"][name]
            for name in ["A_UPC", "A_Tab_relation", "A_HGB_relation", "A_HGB_free"]
        },
        seconds=logs["settled"]["seconds"],
        seconds_cap=cfg["seconds_cap"],
        historical_checks=logs["verification"]["checks"],
        historical_scalar_difference=logs["verification"]["max_scalar_difference"],
        timestamps=dict(
            zip(
                [
                    "authorized",
                    "started",
                    "sealed",
                    "verified",
                    "result",
                    "finished",
                    "settled",
                    "alias",
                    "archived",
                ],
                ordered,
                strict=True,
            )
        ),
        inherited_settings_metadata={
            "at": cfg["at"],
            "limits": cfg["limits"],
            "origin": CACHE + "frozen_settings.json",
        },
        no_historical_scripts_imported=True,
        new_model_executions=0,
        new_RCTL_MAE_computation=False,
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
                key: report[key]
                for key in [
                    "success",
                    "source_count",
                    "max_absolute_difference",
                    "alias_slots",
                    "unique_UPC_artifacts",
                    "seconds",
                ]
            },
            ensure_ascii=False,
        )
    )
