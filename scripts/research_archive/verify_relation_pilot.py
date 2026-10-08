"""Check saved 635–638 evidence without importing or running research scripts.

Requires NumPy. Reads saved numeric arrays with allow_pickle=False. The source
is either the original Tab-ICL root or a portable bundle's manifest.json.
"""

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
FOLDERS = {
    635: "bounded_relation_graph_635",
    636: "bounded_relation_storage_recovery_636",
    637: "bounded_relation_cache_resume_637",
    638: "bounded_relation_precision_638",
}


def verify(source: Path) -> dict:
    manifest = json.loads(source.read_text(encoding="utf-8")) if source.is_file() else None
    mapping = {r["path"]: r for r in manifest["sources"]} if manifest else {}
    accessed: dict[str, dict] = {}
    checks: Counter = Counter()
    failures = []

    def check(name, condition):
        checks[name] += 1
        if not bool(condition):
            failures.append({"check": name, "occurrence": checks[name]})

    def path(relative):
        key = BASE + relative
        p = source.parent / mapping[key]["archive_path"] if manifest else source / key
        if key not in accessed:
            digest = hashlib.sha256(p.read_bytes()).hexdigest()
            accessed[key] = {"path": key, "sha256": digest, "size_bytes": p.stat().st_size}
            if manifest:
                check("portable_source_hash", digest == mapping[key]["sha256"])
        return p

    def read(relative):
        return json.loads(path(relative).read_text(encoding="utf-8-sig"))

    def array(relative):
        with np.load(path(relative), allow_pickle=False) as z:
            return {k: z[k].copy() for k in z.files}

    def prefix(stage):
        return "results/" + FOLDERS[stage] + "/"

    runs = {n: read(prefix(n) + "run_finished.json") for n in FOLDERS}
    settlements = {n: read(prefix(n) + "settled.json") for n in FOLDERS}
    worker = read(prefix(635) + "worker_finished.json")
    check("635_storage_exception", "multiple values for argument 'p'" in worker["trace"])
    check("636_read_exception", "PermissionError" in runs[636]["failure"]["trace"])
    check("execution_outcomes", [runs[n]["success"] for n in FOLDERS] == [False, False, True, True])
    check(
        "no_RCTL_or_new_638_models",
        all(settlements[n]["RCTL_new_fits"] == 0 for n in [635, 636, 637])
        and settlements[638]["new_models"] == 0,
    )
    check("635_unsaved_probability_meter", runs[635]["meter"]["propensity_query_rows"] == 0)
    check(
        "636_attempted_completed_distinct",
        (runs[636]["meter"]["query_rows_attempted"], runs[636]["meter"]["query_rows_completed"])
        == (1984, 1856),
    )
    for n in FOLDERS:
        check("settled_cost_matches_run", settlements[n]["seconds"] == runs[n]["seconds"])

    # Compare the two implementations statically; never import historical code.
    trees = [
        ast.parse(path(name).read_text(encoding="utf-8-sig"))
        for name in ["bounded_relation_graph_635.py", "bounded_relation_cache_resume_637.py"]
    ]
    for name in ["cdf_pdf", "relationship", "assign"]:
        bodies = [
            next(x for x in t.body if isinstance(x, ast.FunctionDef) and x.name == name)
            for t in trees
        ]
        check("unchanged_numeric_function_" + name, ast.dump(bodies[0]) == ast.dump(bodies[1]))

    inputs = array("results/fixed_reference_vs_joint_pool_616/inputs_0.npz")
    errors = array("results/fixed_reference_vs_joint_pool_616/errors_0.npz")
    ids = inputs["cell_ids"].tolist()
    times = inputs["query_times"]
    check(
        "input_shapes",
        inputs["train_X"].shape == (16, 504, 16)
        and inputs["train_y"].shape == (16, 504)
        and inputs["query_X"].shape == (1024, 16),
    )
    check(
        "query_times_and_identity",
        np.array_equal(times, errors["query_times"])
        and ids == errors["cell_ids"].tolist()
        and len(times) == 64
        and times[0] == 672
        and times[-1] == 839
        and np.all(np.diff(times) > 0),
    )

    def enough(mask):
        return all(
            np.sum(mask[o + lo : o + hi]) >= 8
            and len(np.unique(times[lo:hi][mask[o + lo : o + hi]] // 24)) >= 2
            for o in [0, 64]
            for lo, hi in [(0, 32), (32, 64)]
        )

    retrieval = read(prefix(636) + "retrieval_sealed.json")
    retained = []
    for rec in retrieval["records"]:
        i, j = rec["i"], rec["j"]
        name = f"edges/p_{i}_{j}.npz"
        a, b = path(prefix(636) + name), path(prefix(637) + name)
        check("reused_propensity_bytes", a.read_bytes() == b.read_bytes())
        z = array(prefix(636) + name)
        check(
            "propensity_mask_and_support",
            np.array_equal(z["mask"], (z["p"] >= 0.1) & (z["p"] <= 0.9))
            and enough(z["mask"]) == rec["retained"],
        )
        if rec["retained"]:
            retained.append((i, j))
    check(
        "retrieval_counts",
        len(retrieval["records"]) == retrieval["initial_edges"] == 79
        and len(retained) == retrieval["retained_edges"] == 22,
    )
    active = sorted({i for edge in retained for i in edge})
    cells = {i: array(prefix(637) + f"cells/c{i}.npz") for i in active}
    for i in [0, 1, 2, 3, 5]:
        check(
            "reused_cell_bytes",
            path(prefix(636) + f"cells/c{i}.npz").read_bytes()
            == path(prefix(637) + f"cells/c{i}.npz").read_bytes(),
        )
    for i, z in cells.items():
        check(
            "quantile_identity_and_order",
            int(z["cell_id"]) == ids[i] and np.array_equal(z["query_times"], times),
        )
        check(
            "original_quantile_dtypes",
            z["Tab"].dtype == np.float32 and z["HGB"].dtype == np.float64,
        )
        check(
            "sorted_finite_quantiles",
            all(
                np.isfinite(z[m]).all() and np.all(np.diff(z[m], axis=-1) >= 0)
                for m in ["Tab", "HGB"]
            ),
        )

    results = {n: read(prefix(n) + "result.json") for n in [637, 638]}
    recovered = Counter(Tab=0, HGB=0)
    root_max = 0.0
    root_count = 0
    supported = {637: [], 638: []}
    cost_tables = {n: {m: [] for m in ["Tab", "HGB"]} for n in [637, 638]}
    for i, j in retained:
        probability = array(prefix(636) + f"edges/p_{i}_{j}.npz")
        versions = {
            n: {m: array(prefix(n) + f"edges/{m}_{i}_{j}.npz") for m in ["Tab", "HGB"]}
            for n in [637, 638]
        }
        for model in ["Tab", "HGB"]:
            old, new = versions[637][model], versions[638][model]
            recovered[model] += int(np.sum(new["valid"] & ~old["valid"]))
            knots = []
            for source_cell in [i, j]:
                z = cells[source_cell]
                knots.append(
                    np.concatenate(
                        [z[model][z["target_indices"].tolist().index(t)] for t in [i, j]]
                    ).astype(np.float64)
                )
            for t in range(128):
                # Solve a linear interval from the union of knot locations.
                grid = np.unique(np.r_[knots[0][t], knots[1][t]])
                p = float(probability["p"][t])
                mixed = p * np.interp(
                    grid, knots[0][t], np.arange(1, 10) / 10, left=0.1, right=0.9
                ) + (1 - p) * np.interp(
                    grid, knots[1][t], np.arange(1, 10) / 10, left=0.1, right=0.9
                )
                pos = int(np.searchsorted(mixed, 0.5))
                check("root_bracket", 0 < pos < len(grid) and mixed[pos] > mixed[pos - 1])
                root = grid[pos - 1] + (0.5 - mixed[pos - 1]) * (grid[pos] - grid[pos - 1]) / (
                    mixed[pos] - mixed[pos - 1]
                )
                diff = abs(float(root) - float(new["q"][t]))
                root_max = max(root_max, diff)
                root_count += 1
                check("saved_root_vs_linear_solution", diff < 1e-8)
            check(
                "score_identity",
                np.allclose(
                    new["score"],
                    new["w"] * (new["d"] - new["a"]) * (0.5 - (new["y"] <= new["q"])),
                    atol=1e-15,
                    rtol=0,
                ),
            )
            check("score_bound", np.max(np.abs(new["score"])) <= 0.5 + 1e-12)
            check(
                "truth_and_probability_identity",
                np.array_equal(new["y"], np.r_[errors["truth"][i], errors["truth"][j]])
                and np.array_equal(new["p"], probability["p"]),
            )
        for n in [637, 638]:
            v = versions[n]
            mask = probability["mask"] & v["Tab"]["valid"] & v["HGB"]["valid"]
            check("saved_common_mask", all(np.array_equal(mask, v[m]["mask"]) for m in v))
            if enough(mask):
                supported[n].append((i, j))
                for model in v:
                    values = [
                        max(
                            0.0,
                            float(
                                np.mean(
                                    [
                                        np.mean(
                                            v[model]["score"][o + lo : o + hi][
                                                mask[o + lo : o + hi]
                                            ]
                                        )
                                        for o in [0, 64]
                                    ]
                                )
                            ),
                        )
                        for lo, hi in [(0, 32), (32, 64)]
                    ]
                    cost_tables[n][model].append(values)
    check(
        "recovered_row_count",
        dict(recovered) == results[638]["recovered_rows"] == {"Tab": 1853, "HGB": 0},
    )
    for n in [637, 638]:
        graph = array(prefix(n) + "graph_scores.npz")
        check("common_edge_count", len(supported[n]) == results[n]["common_valid_edges"])
        check(
            "saved_graph_identity",
            graph["edges"].tolist() == [list(e) for e in supported[n]]
            and graph["cell_ids"].tolist() == ids,
        )
        for model in ["Tab", "HGB"]:
            costs = np.asarray(cost_tables[n][model])
            check("saved_graph_costs", np.allclose(costs, graph[model], atol=1e-14, rtol=0))
            assignment = results[n]["assignments"][model]
            labels = graph["initial_labels"].copy()
            edges = np.asarray(supported[n])

            def objective(lab, costs=costs, edges=edges):
                return costs[lab[edges[:, 0]] == lab[edges[:, 1]]].sum(axis=0)

            check(
                "initial_objective",
                np.allclose(objective(labels), assignment["initial_objective"], atol=1e-14, rtol=0),
            )
            for move in assignment["moves"]:
                index = ids.index(move["cell_id"])
                dest = move["destination"]
                neighbor = [b if a == index else a for a, b in supported[n] if index in (a, b)]
                check(
                    "move_support_nonempty",
                    labels[index] == move["source"]
                    and np.sum(labels == labels[index]) > 1
                    and sum(labels[j] == dest for j in neighbor) >= 2,
                )
                before = objective(labels)
                labels[index] = dest
                delta = objective(labels) - before
                check(
                    "move_both_halves_decrease",
                    np.all(delta < -1e-12)
                    and np.allclose(delta, move["change"], atol=1e-14, rtol=0),
                )
            check(
                "final_assignment",
                labels.tolist() == assignment["labels"] and set(labels.tolist()) == {0, 1, 2, 3},
            )
            check(
                "final_objective",
                np.allclose(objective(labels), assignment["final_objective"], atol=1e-14, rtol=0),
            )

    return {
        "created_at_utc": datetime.now(UTC).isoformat(),
        "success": not failures,
        "scope": (
            "Saved artifact and arithmetic checks only; "
            "no model rerun or independent scientific replication"
        ),
        "check_categories": dict(checks),
        "failures": failures,
        "linear_roots_compared": root_count,
        "maximum_root_difference": root_max,
        "recovered_pair_query_rows": dict(recovered),
        "common_edges": {str(n): len(supported[n]) for n in supported},
        "prediction_contexts_used": len(cells),
        "completed_quantile_query_rows": sum(len(z["target_indices"]) * 64 for z in cells.values()),
        "seconds_635_through_637": sum(runs[n]["seconds"] for n in [635, 636, 637]),
        "seconds_638": runs[638]["seconds"],
        "accessed_sources": list(accessed.values()),
        "unverified_upstream": [
            "616 raw data generation and normalization",
            "633 initial membership provenance",
            "634 literature and novelty claims",
            "639 downstream RCTL performance",
        ],
    }


def main():
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
        json.dumps({k: v for k, v in report.items() if k != "accessed_sources"}, ensure_ascii=False)
    )
    if not report["success"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
