"""초기 B1/B2의 저장 예측·소속·RCTL 결과를 대조한다. 모델과 옛 코드는 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import numpy as np


def verify(source: Path) -> dict:
    """Check original source files or a portable manifest without running models."""
    manifest = json.loads(source.read_text(encoding="utf-8")) if source.is_file() else None
    mapping = {r["path"]: r for r in manifest["sources"]} if manifest else {}
    base = "tmp/redesign_20260925/"
    accessed = {}
    counts = Counter()
    differences = []
    max_by_check = {}

    def check(name, condition):
        """Count assertions and identify failing occurrences."""
        counts[name] += 1
        if not condition:
            raise AssertionError((name, counts[name]))

    def close(name, a, b, tol=1e-7):
        """Compare array shapes and finite absolute differences within a stated tolerance."""
        a, b = np.asarray(a), np.asarray(b)
        check(name + "_shape", a.shape == b.shape)
        diff = float(np.max(np.abs(a.astype(float) - b.astype(float))))
        differences.append(diff)
        max_by_check[name] = max(max_by_check.get(name, 0), diff)
        check(name, np.isfinite(diff) and diff <= tol)

    def path(k, scope):
        """Resolve a source, check portable byte identity, and register actual access scope."""
        k = base + k
        p = source.parent / mapping[k]["archive_path"] if manifest else source / k
        if k not in accessed:
            raw = p.read_bytes()
            accessed[k] = dict(
                path=k, sha256=hashlib.sha256(raw).hexdigest(), size_bytes=len(raw), read_scope=[]
            )
            if manifest:
                check(
                    "portable_source_identity",
                    accessed[k]["sha256"] == mapping[k]["sha256"]
                    and len(raw) == mapping[k]["size_bytes"],
                )
        accessed[k]["read_scope"] = sorted(set(accessed[k]["read_scope"]) | set(scope))
        return p

    def arr(k, keys):
        """Copy requested arrays without pickle deserialization."""
        with np.load(path(k, ["array:" + s for s in keys]), allow_pickle=False) as z:
            return {s: z[s].copy() for s in keys}

    def fields(k, keys):
        """Extract requested JSON fields and register their checked scope."""
        d = json.loads(path(k, ["json_parsed"]).read_text(encoding="utf-8"))
        o = {}
        for f in keys:
            o[f] = d[f]
            path(k, ["json_top_level:" + f])
        return o

    def sequence(k):
        """Read a saved JSON list for structured result comparisons."""
        return json.loads(path(k, ["json_full_list"]).read_text(encoding="utf-8"))

    d = arr("results/design_data.npz", ["X", "Y", "times", "cell_indices", "scales"])
    b1 = arr(
        "results/risk_table_predictions.npz",
        [
            "quantiles",
            "median",
            "anchors",
            "cell_ids",
            "query_times",
            "context_times",
            "selected_cells",
        ],
    )
    methods = ["tabicl_risk", "empirical_risk", "knn_risk", "median_only", "median_iqr"]
    b2 = arr(
        "results/observed_risk_tables.npz",
        methods
        + [
            "actions",
            "predicted_quantiles",
            "knn_quantiles",
            "base_query",
            "base_followweek",
            "query_bins",
            "followweek_bins",
            "cell_ids",
            "selected_cells",
        ],
    )
    sel = b1["selected_cells"]
    ids = b1["cell_ids"]
    qi = b1["query_times"] - 168
    check(
        "identity",
        np.array_equal(sel, b2["selected_cells"])
        and np.array_equal(ids, b2["cell_ids"])
        and np.array_equal(ids, d["cell_indices"][sel] + 1),
    )
    check("context_times", np.array_equal(b1["context_times"], np.arange(168, 672)))
    y = d["Y"][sel]
    x = d["X"][sel]
    bins = b2["query_bins"][:, b1["query_times"] - 672]
    projection = fields(
        "results/projection_diagnostic.json", ["cells", "averages", "interpretation"]
    )
    projection_rows = []
    for i, cell in enumerate(ids):
        direct = b1["quantiles"][i, 64 + i * 64 : 64 + (i + 1) * 64]
        anchor = b1["quantiles"][i, bins[i]]
        shift = x[i, qi, 7] - b1["anchors"][bins[i], 7]
        corrected = anchor + shift[:, None]
        values = dict(
            direct_mae=float(np.abs(direct[:, 64] - y[i, qi]).mean()),
            anchor_mae=float(np.abs(anchor[:, 64] - y[i, qi]).mean()),
            level_restored_mae=float(np.abs(corrected[:, 64] - y[i, qi]).mean()),
            uncorrected_quantile_W1=float(np.abs(anchor - direct).mean()),
            restored_quantile_W1=float(np.abs(corrected - direct).mean()),
        )
        row = projection["cells"][i]
        check("projection_cell", row["cell_id"] == cell)
        for k, v in values.items():
            close("projection_" + k, v, row[k])
        projection_rows.append(values)
    for k in projection_rows[0]:
        close(
            "projection_mean_" + k,
            np.mean([r[k] for r in projection_rows]),
            projection["averages"][k],
        )
    res = b2["predicted_quantiles"] - b2["base_query"][:, :, None]
    alpha = (np.arange(129) + 0.5) / 129
    iqr = np.apply_along_axis(
        lambda v: np.interp(0.75, alpha, v) - np.interp(0.25, alpha, v), 2, res
    )
    sources = dict(
        tabicl_risk=res,
        empirical_risk=(y[:, 504:672] - b2["base_query"])[:, :, None],
        knn_risk=b2["knn_quantiles"] - b2["base_query"][:, :, None],
        median_only=res[:, :, 64:65],
        median_iqr=res[:, :, 64:65] + iqr[:, :, None] * (2 * alpha - 1)[None, None, :],
    )
    for b in range(64):
        mask = b2["query_bins"] == b
        expected = (
            np.linspace(
                min(float(v[mask].min()) for v in sources.values()),
                max(float(v[mask].max()) for v in sources.values()),
                257,
            )
            if mask.any()
            else np.zeros(257)
        )
        close("actual_action_grid_all5sources", b2["actions"][b], expected, 1e-10)
    for method, v in sources.items():
        table = np.zeros((16, 64, 257))
        for i in range(16):
            for b in range(64):
                vv = v[i, b2["query_bins"][i] == b]
                if not len(vv):
                    continue
                vals = np.sort(vv.reshape(-1).astype(float))
                prefix = np.r_[0, np.cumsum(vals)]
                a = b2["actions"][b]
                n = np.searchsorted(vals, a, side="right")
                table[i, b] = (prefix[-1] - 2 * prefix[n] + a * (2 * n - len(vals))) / (
                    168 * vv.shape[1]
                )
        close("risk_table_" + method, table, b2[method], 1e-10)
        pred = arr("results/observed_surrogate_" + method + ".npz", ["prediction", "y", "cell_ids"])
        check("surrogate_id", np.array_equal(pred["cell_ids"], ids))
        close("surrogate_truth", pred["y"], y[:, 672:])
    summary = fields(
        "results/rctl_pilot/summary.json",
        [
            "metrics",
            "paired_comparisons",
            "execution",
            "partition_sha256",
            "test_period_becomes_development_if_used_for_new_design",
        ],
    )
    ev = arr(
        "results/rctl_pilot/evaluation_data.npz",
        ["cell_ids", "scales", "test_times", "test_y", "peak_threshold"],
    )
    check(
        "RCTL_times_id",
        np.array_equal(ev["cell_ids"], ids)
        and np.array_equal(ev["test_times"], np.arange(1008, 1488)),
    )
    close("RCTL_scale", ev["scales"], d["scales"][sel])
    all_keys = [r["method"] + "_" + str(r["seed"]) for r in summary["metrics"]]
    allpred = arr("results/rctl_pilot/all_predictions.npz", all_keys + ["y", "cell_ids", "scales"])
    check("RCTL_joint_ids", np.array_equal(allpred["cell_ids"], ids))
    close("RCTL_joint_truth", allpred["y"], ev["test_y"])
    close("RCTL_joint_scales", allpred["scales"], ev["scales"])
    metrics = []
    for row in summary["metrics"]:
        key = row["method"] + "_" + str(row["seed"])
        pred = allpred[key]
        err = np.abs(pred - ev["test_y"])
        check("RCTL_shape_finite", pred.shape == (16, 480) and np.isfinite(pred).all())
        close("RCTL_stored_MAE", err.mean(), row["mean_scaled_mae"])
        close("RCTL_percell_MAE", err.mean(axis=1), row["per_cell_mae"])
        close("RCTL_raw_MAE", np.mean(err * ev["scales"][:, None]), row["raw_activity_mae"])
        double = float(np.abs(pred.astype(float) - ev["test_y"].astype(float)).mean())
        metrics.append(
            dict(
                method=row["method"],
                seed=row["seed"],
                reported_float32_mean=row["mean_scaled_mae"],
                independent_float64_mean=double,
            )
        )
    settings = fields(
        "results/rctl_pilot/frozen_settings.json",
        [
            "seed_primary",
            "seed_secondary",
            "max_epochs",
            "batch_size",
            "patience",
            "learning_rate",
            "adam_eps",
            "loss",
            "threads",
            "max_fits",
            "max_total_epochs",
            "wall_cap_seconds",
            "ram_cap_bytes",
            "train_targets",
            "validation_targets",
            "test_targets",
            "selection_uses_test",
            "RCTL_results_used_for_clustering",
            "tasks",
            "source_hashes",
            "training_code_sha256",
            "model_code_sha256",
        ],
    )
    expected = dict(
        seed_primary=20260925,
        seed_secondary=20260926,
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
    check(
        "RCTL_protocol",
        all(settings[k] == v for k, v in expected.items())
        and not settings["selection_uses_test"]
        and not settings["RCTL_results_used_for_clustering"],
    )
    proposal = fields(
        "results/observed_risk_pilot.json",
        [
            "cell_ids",
            "partitions",
            "surrogate_validation",
            "fixed_partition_validation",
            "global_ridge_followweek_mae",
            "input_boundary",
            "seconds",
        ],
    )
    fits = sequence("results/rctl_pilot/fit_results.json")
    check("29_tasks_fits", len(settings["tasks"]) == len(fits) == 29)
    assembled = {k: np.full_like(ev["test_y"], np.nan) for k in all_keys}
    epochs = 0
    for task, fit in zip(settings["tasks"], fits, strict=True):
        method, seed, cluster, members = task
        stem = f"{method}_{seed}_cluster{cluster}"
        expected_members = (
            list(range(16))
            if method == "global"
            else [i for i, g in enumerate(proposal["partitions"][method]) if g == cluster]
        )
        check(
            "task_labels",
            members == expected_members
            and [fit[k] for k in ["method", "seed", "cluster", "members"]] == task,
        )
        p = arr("results/rctl_pilot/" + stem + ".npz", ["prediction", "cell_ids", "y", "members"])
        check(
            "group_ids",
            np.array_equal(p["cell_ids"], ids[members]) and p["members"].tolist() == members,
        )
        close("group_truth", p["y"], ev["test_y"][members])
        assembled[f"{method}_{seed}"][members] = p["prediction"]
        hist = sequence("results/rctl_pilot/" + stem + "_history.json")
        val = np.array([h["val_mae"] for h in hist])
        best = int(np.argmin(val))
        check(
            "validation_patience",
            len(hist) == fit["epochs_run"]
            and best + 1 == fit["best_epoch"]
            and len(hist) - best - 1 == 10
            and fit["stop_reason"] == "validation_patience"
            and len(hist) < 80,
        )
        close("best_validation", val[best], fit["best_val_mae"])
        epochs += len(hist)
    for key, pred in assembled.items():
        close("group_assembled_predictions", pred, allpred[key], 0)
    check("epoch_total", epochs == summary["execution"]["epochs_total"] == 1565)
    close(
        "peak_threshold",
        np.quantile(y[:, :672].astype(float), 0.95, axis=1).astype(np.float32),
        ev["peak_threshold"],
    )
    for name, expected_hash in settings["source_hashes"].items():
        k = ("results/" if name.endswith(".json") else "") + name
        check(
            "frozen_hash",
            hashlib.sha256(path(k, ["sha256_only"]).read_bytes()).hexdigest() == expected_hash,
        )
    for name, key in [
        ("train_rctl_pilot.py", "training_code_sha256"),
        ("rctl_torch.py", "model_code_sha256"),
    ]:
        check(
            "implementation_hash",
            hashlib.sha256(path(name, ["sha256_only"]).read_bytes()).hexdigest() == settings[key],
        )
    resampling = []
    rng = np.random.default_rng(20260925)
    for seed in [20260925, 20260926]:
        candidate = f"tabicl_risk_{seed}"
        for key in all_keys:
            if not key.endswith(str(seed)) or key == candidate:
                continue
            diff = np.abs(allpred[candidate] - ev["test_y"]) - np.abs(allpred[key] - ev["test_y"])
            row = next(
                r
                for r in summary["paired_comparisons"]
                if r["candidate"] == candidate and r["comparison"] == key
            )
            close("paired_mean_delta", diff.mean(), row["mean_delta"])
            close(
                "paired_relative_percent",
                100 * diff.mean() / np.abs(allpred[key] - ev["test_y"]).mean(),
                row["relative_mae_change_percent"],
                1e-5,
            )
            check(
                "paired_cell_count", int(np.sum(diff.mean(axis=1) < 0)) == row["cell_improvements"]
            )
            for width in [48, 96]:
                blocks = diff.reshape(16, 480 // width, width).mean(axis=(0, 2))
                close(
                    "paired_saved_blocks",
                    blocks,
                    row["block_resampling"][str(width)]["observed_block_deltas"],
                )
                means = blocks[rng.integers(0, len(blocks), size=(10000, len(blocks)))].mean(axis=1)
                interval = np.quantile(means, [0.025, 0.975])
                close(
                    "paired_interval",
                    interval,
                    row["block_resampling"][str(width)]["percentile_2_5_97_5"],
                )
            resampling.append(
                dict(
                    candidate=candidate,
                    comparison=key,
                    relative_percent=row["relative_mae_change_percent"],
                    intervals=row["block_resampling"],
                )
            )

    def curve(q, actions, weights):
        """Rebuild absolute-loss tables from saved quantiles using sorted prefix sums."""
        result = np.zeros((16, 64, 257))
        for i in range(16):
            for b in range(64):
                v = np.sort(q[i, b].astype(float))
                prefix = np.r_[0, np.cumsum(v)]
                a = actions[b]
                n = np.searchsorted(v, a, side="right")
                result[i, b] = (
                    (prefix[-1] - 2 * prefix[n] + a * (2 * n - len(v))) / len(v) * weights[i, b]
                )
        return result

    def balanced(cost):
        """Replay the recorded disjoint-pair merge rule using saved costs."""
        groups = [[i] for i in range(16)]
        hist = []
        scores = 0
        while len(groups) > 4:
            edges = [
                (cost(a, b), min(a), min(b), i, j)
                for i, a in enumerate(groups)
                for j, b in enumerate(groups)
                if i < j
            ]
            scores += len(edges)
            used = set()
            new = []
            for delta, _, __, i, j in sorted(edges):
                if i in used or j in used:
                    continue
                used.update([i, j])
                new.append(sorted(groups[i] + groups[j]))
                hist.append(dict(left=groups[i], right=groups[j], delta=delta))
            check("balanced_round", len(used) == len(groups))
            groups = sorted(new, key=min)
        labels = np.empty(16, int)
        for label, g in enumerate(groups):
            labels[g] = label
        return labels, hist, scores

    def risk(tab, g):
        """Sum statewise minima for a group in a saved loss table."""
        return float(np.min(tab[g].sum(0), axis=1).sum())

    def audit_partition(tab, labels, history, score_key):
        """Compare replayed group labels, merge members, and recorded costs."""
        lab, hist, scores = balanced(lambda a, b: risk(tab, a + b) - risk(tab, a) - risk(tab, b))
        check(
            "partition_labels",
            lab.tolist() == labels and len(hist) == len(history) == 12 and scores == 148,
        )
        for a, b in zip(hist, history, strict=True):
            check("merge_members", a["left"] == b["left"] and a["right"] == b["right"])
            close("merge_cost", a["delta"], b[score_key], 1e-10)
        return lab

    def ari(a, b):
        """Compute adjusted Rand agreement directly from the two saved labelings."""
        _, a = np.unique(a, return_inverse=True)
        _, b = np.unique(b, return_inverse=True)
        t = np.zeros((max(a) + 1, max(b) + 1), int)
        np.add.at(t, (a, b), 1)

        def choose(x):
            """Count unordered pairs in each contingency-table entry."""
            return np.sum(x * (x - 1) / 2)

        paired = choose(t)
        ra = choose(t.sum(1))
        cb = choose(t.sum(0))
        expected = ra * cb / (16 * 15 / 2)
        maximum = (ra + cb) / 2
        return 1 if maximum == expected else float((paired - expected) / (maximum - expected))

    b1more = arr(
        "results/risk_table_predictions.npz",
        ["knn_quantiles", "actions", "weights", "table", "mean"],
    )
    b1summary = fields(
        "results/risk_table_pilot.json",
        [
            "cell_ids",
            "K",
            "state_count",
            "alphas",
            "partitions",
            "comparisons",
            "diagnostics",
            "ARI_vs_tabicl",
            "total_seconds",
            "finite_state_and_estimated_distribution_scope",
            "RCTL_used_for_clustering",
        ],
    )
    b1history = fields(
        "results/risk_table_merge_history.json", list(b1summary["comparisons"]) + ["pcc_balanced"]
    )
    check(
        "B1_settings",
        b1summary["cell_ids"] == ids.tolist()
        and b1summary["K"] == 4
        and b1summary["state_count"] == 64
        and not b1summary["RCTL_used_for_clustering"],
    )
    close("quantile_grid", b1summary["alphas"], alpha, 0)
    check(
        "B1_query_times",
        np.array_equal(b1["query_times"], np.rint(np.linspace(672, 839, 64)).astype(int)),
    )
    check(
        "B1_shapes",
        b1["quantiles"].shape == (16, 1088, 129)
        and b1["median"].shape == b1more["mean"].shape == (16, 1088),
    )
    check(
        "B1_quantiles_finite_ordered",
        np.isfinite(b1["quantiles"]).all() and np.min(np.diff(b1["quantiles"], axis=-1)) >= -1e-5,
    )
    close("B1_median_quantile", b1["median"], b1["quantiles"][:, :, 64], 1e-7)
    weights = b1more["weights"]
    close("B1_state_mass", weights.sum(1), np.ones(16), 1e-10)
    close("B1_state_frequency_integer", weights * 504, np.rint(weights * 504), 1e-10)
    context = x[:, :504].reshape(-1, 16)
    check(
        "B1_real_anchors",
        b1["anchors"].shape == (64, 16)
        and all(np.any(np.all(context == a, axis=1)) for a in b1["anchors"]),
    )
    aq = b1["quantiles"][:, :64]
    kq = b1more["knn_quantiles"]
    lo = np.minimum(aq.min(axis=(0, 2)), kq.min(axis=(0, 2)))
    hi = np.maximum(aq.max(axis=(0, 2)), kq.max(axis=(0, 2)))
    close(
        "B1_action_grid",
        b1more["actions"],
        lo[:, None] + (hi - lo)[:, None] * np.linspace(0, 1, 257),
        1e-10,
    )
    spread = np.apply_along_axis(
        lambda v: np.interp(0.75, alpha, v) - np.interp(0.25, alpha, v), 2, aq
    )
    b1sources = dict(
        tabicl_risk=aq,
        knn_risk=kq,
        median_only=aq[:, :, 64:65],
        median_iqr=aq[:, :, 64:65] + spread[:, :, None] * (2 * alpha - 1)[None, None, :],
    )
    b1tables = {name: curve(q, b1more["actions"], weights) for name, q in b1sources.items()}
    close("B1_stored_table", b1tables["tabicl_risk"], b1more["table"], 1e-10)
    for name, tab in b1tables.items():
        lab = audit_partition(tab, b1summary["partitions"][name], b1history[name], "cost")
        row = b1summary["comparisons"][name]
        check("B1_pair_count", row["pair_score_evaluations"] == 148)
        close(
            "B1_own_objective",
            sum(risk(tab, np.flatnonzero(lab == c)) for c in range(4)),
            row["own_table_objective"],
            1e-10,
        )
        close(
            "B1_full_objective",
            sum(risk(b1more["table"], np.flatnonzero(lab == c)) for c in range(4)),
            row["full_table_objective"],
            1e-10,
        )
    raw = arr("results/design_data.npz", ["raw"])["raw"][:, sel]
    corr = np.corrcoef(raw[:672].T)
    lab, hist, scores = balanced(lambda a, b: 1 - float(corr[np.ix_(a, b)].mean()))
    check("B1_PCC_labels", lab.tolist() == b1summary["partitions"]["pcc_balanced"])
    for a, b in zip(hist, b1history["pcc_balanced"], strict=True):
        check("PCC_merge_members", a["left"] == b["left"] and a["right"] == b["right"])
        close("PCC_merge_cost", a["delta"], b["cost"], 1e-10)
    rand = np.empty(16, int)
    rand[np.random.default_rng(20260925).permutation(16)] = np.repeat(np.arange(4), 4)
    check("B1_random_labels", rand.tolist() == b1summary["partitions"]["random_balanced"])
    for name, labels in b1summary["partitions"].items():
        close(
            "B1_ARI",
            ari(b1summary["partitions"]["tabicl_risk"], labels),
            b1summary["ARI_vs_tabicl"][name],
            1e-10,
        )
    for i, row in enumerate(b1summary["diagnostics"]):
        direct = b1["median"][i, 64 + i * 64 : 64 + (i + 1) * 64]
        anchor = b1["median"][i, bins[i]]
        ownq = b1["quantiles"][i, 64 + i * 64 : 64 + (i + 1) * 64]
        values = dict(
            tabicl_direct_mae=np.abs(direct - y[i, qi]).mean(),
            anchor_representative_mae=np.abs(anchor - y[i, qi]).mean(),
            projection_mean_abs_change=np.abs(anchor - direct).mean(),
            quantile_transport_change=np.abs(b1["quantiles"][i, bins[i]] - ownq).mean(),
            own_query_80pct_coverage=np.mean(
                (y[i, qi] >= ownq[:, 12]) & (y[i, qi] <= ownq[:, 116])
            ),
        )
        check("B1_diagnostic_ID", row["cell_id"] == int(ids[i]))
        for k, v in values.items():
            close("B1_diagnostic_" + k, v, row[k])
    b2history = fields("results/observed_risk_history.json", methods)
    extra = fields(
        "results/observed_risk_pilot.json",
        ["ARI_vs_tabicl", "function_class", "RCTL_used_for_clustering"],
    )
    check(
        "B2_boundary",
        proposal["input_boundary"]
        == dict(
            context=[168, 671],
            clustering_query=[672, 839],
            design_followweek=[840, 1007],
            final_sealed=[1008, 1487],
        )
        and not extra["RCTL_used_for_clustering"],
    )
    check(
        "B2_shapes",
        b2["predicted_quantiles"].shape == b2["knn_quantiles"].shape == (16, 168, 129)
        and b2["query_bins"].shape == b2["followweek_bins"].shape == (16, 168),
    )
    check(
        "B2_bins_range",
        all(np.all((b2[k] >= 0) & (b2[k] < 64)) for k in ["query_bins", "followweek_bins"]),
    )

    def action(tab, g):
        """Recover statewise corrections from a saved group loss table."""
        total = tab[g].sum(0)
        a = b2["actions"][np.arange(64), np.argmin(total, axis=1)]
        a[np.sum(total, axis=1) == 0] = 0
        return a

    def surrogate(tab, lab):
        """Reassemble recorded surrogate predictions from saved corrections and bins."""
        return np.stack(
            [
                b2["base_followweek"][i]
                + action(tab, np.flatnonzero(lab == lab[i]))[b2["followweek_bins"][i]]
                for i in range(16)
            ]
        )

    for name in methods:
        lab = audit_partition(b2[name], proposal["partitions"][name], b2history[name], "delta")
        pred = surrogate(b2[name], lab)
        saved = arr("results/observed_surrogate_" + name + ".npz", ["prediction"])
        close("B2_surrogate_prediction", pred, saved["prediction"], 1e-10)
        err = np.abs(pred - y[:, 672:])
        row = proposal["surrogate_validation"][name]
        close("B2_surrogate_MAE", err.mean(), row["mae_design_following_week"], 1e-10)
        close("B2_surrogate_percell", err.mean(1), row["per_cell_mae"], 1e-10)
        close(
            "B2_objective",
            sum(risk(b2[name], np.flatnonzero(lab == c)) for c in range(4)),
            row["predicted_objective"],
            1e-10,
        )
        check("B2_size_scores", row["group_sizes"] == [4] * 4 and row["pair_scores"] == 148)
    for row in proposal["fixed_partition_validation"]:
        lab = np.array(proposal["partitions"][row["partition"]])
        for name in ["tabicl_risk", "empirical_risk"]:
            close(
                "B2_fixed_partition_MAE",
                np.abs(surrogate(b2[name], lab) - y[:, 672:]).mean(),
                row[name + "_followweek_mae"],
                1e-10,
            )
    close(
        "B2_global_ridge_MAE",
        np.abs(b2["base_followweek"] - y[:, 672:]).mean(),
        proposal["global_ridge_followweek_mae"],
    )
    for name, lab in proposal["partitions"].items():
        close(
            "B2_ARI",
            ari(proposal["partitions"]["tabicl_risk"], lab),
            extra["ARI_vs_tabicl"][name],
            1e-10,
        )
        if name in ["pcc_balanced", "random_balanced", "cross_error_profile"]:
            check("B2_fixed_reuse", lab == b1summary["partitions"][name])
    pairrows = sequence("results/loss_table_pair_diagnostic.json")
    diagnostic = fields(
        "results/loss_table_diagnostic.json",
        [
            "fast_curve_max_abs_difference",
            "fast_curve_seconds",
            "prefix_formula",
            "benchmark_parallel_RCTL_cpu_contention",
            "surrogate_pair_diagnostic",
            "cost_extrapolation",
            "new_model_calls",
            "total_seconds",
        ],
    )

    def ranks(v):
        """Assign average ranks to ties for the recorded pair diagnostic."""
        order = np.argsort(v, kind="stable")
        rank = np.empty(len(v), float)
        pos = 0
        while pos < len(v):
            end = pos + 1
            while end < len(v) and v[order[end]] == v[order[pos]]:
                end += 1
            rank[order[pos:end]] = (pos + end - 1) / 2
            pos = end
        return rank

    for name in methods:
        tab = b2[name]
        rows = [r for r in pairrows if r["method"] == name]
        check("pair_count", len(rows) == 120)
        own = np.array(
            [
                np.mean(
                    np.abs(
                        b2["base_followweek"][i]
                        + action(tab, [i])[b2["followweek_bins"][i]]
                        - y[i, 672:]
                    )
                )
                for i in range(16)
            ]
        )
        estimates = []
        actual = []
        for row, (i, j) in zip(
            rows, ((a, b) for a in range(16) for b in range(a + 1, 16)), strict=True
        ):
            a = action(tab, [i, j])
            pred = np.stack(
                [b2["base_followweek"][c] + a[b2["followweek_bins"][c]] for c in [i, j]]
            )
            delta = np.abs(pred - y[[i, j], 672:]).mean(1).sum() - own[i] - own[j]
            estimate = risk(tab, [i, j]) - risk(tab, [i]) - risk(tab, [j])
            check("pair_identity", [row["i"], row["j"]] == [i, j])
            close("pair_estimate", estimate, row["estimated_sum_mae_delta"], 1e-10)
            close("pair_actual", delta, row["actual_sum_mae_delta"], 1e-10)
            estimates.append(estimate)
            actual.append(delta)
        row = next(r for r in diagnostic["surrogate_pair_diagnostic"] if r["method"] == name)
        close(
            "pair_rank_correlation",
            np.corrcoef(ranks(estimates), ranks(actual))[0, 1],
            row["spearman_rank_correlation"],
            1e-10,
        )
        close("pair_mean_delta", np.mean(actual), row["mean_actual_pair_delta"], 1e-10)
        close(
            "pair_positive_fraction",
            np.mean(np.array(actual) > 0),
            row["positive_actual_delta_fraction"],
            1e-10,
        )
    check("pair_diagnostic_total", len(pairrows) == 600 and diagnostic["new_model_calls"] == 0)
    costs = {}
    for name, nquery in [("risk_table", 1088), ("observed_risk", 168)]:
        calls = sequence("results/" + name + "_calls.json")
        check("Tab_call_count", len(calls) == 16)
        for call, cell in zip(calls, ids, strict=True):
            check(
                "Tab_call_identity",
                call["cell_id"] == cell
                and call["context_rows"] == 504
                and call["query_rows"] == nquery
                and call["ensemble"] == 1,
            )
        costs[name] = dict(
            contexts=len(calls),
            query_rows=sum(r["query_rows"] for r in calls),
            fit_seconds=sum(r["fit_seconds"] for r in calls),
            predict_seconds=sum(r["predict_seconds"] for r in calls),
        )
    mean_call = (
        costs["observed_risk"]["fit_seconds"] + costs["observed_risk"]["predict_seconds"]
    ) / 16
    for row in diagnostic["cost_extrapolation"]:
        n = row["cells"]
        check(
            "extrapolation_counts",
            row["TabICL_context_preparations"] == n
            and row["own_query_rows"] == n * 168
            and row["cross_query_rows_if_all_cells"] == n * n * 168
            and row["all_cell_pairs"] == n * (n - 1) // 2
            and row["table_float64_bytes"] == n * 64 * 257 * 8
            and row["quantile_float64_bytes"] == n * 168 * 129 * 8
            and row["cell_knn_directed_edges_upper"] == n * 16,
        )
        close(
            "extrapolation_minutes",
            n * mean_call / 60,
            row["inference_minutes_linear_estimate"],
            1e-10,
        )
    for row in summary["metrics"]:
        pred = allpred[row["method"] + "_" + str(row["seed"])]
        err = np.abs(pred - ev["test_y"])
        mask = ev["test_y"] > ev["peak_threshold"][:, None]
        pm = [float(err[i, mask[i]].mean()) if mask[i].any() else None for i in range(16)]
        check("peak_mask_counts", mask.sum(1).tolist() == row["peak_query_counts"])
        close("peak_mean", np.mean([v for v in pm if v is not None]), row["peak_mean_scaled_mae"])
        for a, b in zip(pm, row["peak_per_cell_mae"], strict=True):
            if a is None or b is None:
                check("peak_no_query", a is b)
            else:
                close("peak_percell", a, b)
        chosen = [f for f in fits if f["method"] == row["method"] and f["seed"] == row["seed"]]
        check(
            "RCTL_metric_fit_counts",
            row["models"] == len(chosen)
            and row["epochs_total"] == sum(f["epochs_run"] for f in chosen)
            and row["validation_patience_fits"] == len(chosen)
            and row["epoch_cap_fits"] == 0,
        )
        close("RCTL_fit_seconds", sum(f["fit_seconds"] for f in chosen), row["fit_seconds"], 1e-10)
    started = fields("results/rctl_pilot/run_started.json", ["unix", "pid", "settings_sha256"])
    check(
        "RCTL_started_settings",
        hashlib.sha256(
            path("results/rctl_pilot/frozen_settings.json", ["sha256_only"]).read_bytes()
        ).hexdigest()
        == started["settings_sha256"],
    )
    finished = fields(
        "results/rctl_pilot/run_finished.json",
        [
            "fits_completed",
            "fits_planned",
            "epochs_total",
            "wall_seconds",
            "all_fits_complete",
            "test_period_now_accessed",
            "RCTL_outputs_not_used_for_clustering",
        ],
    )
    check(
        "RCTL_completion",
        finished == summary["execution"]
        and finished["fits_completed"] == finished["fits_planned"] == 29
        and finished["all_fits_complete"]
        and finished["RCTL_outputs_not_used_for_clustering"]
        and finished["wall_seconds"] < 3000,
    )
    for fit in fits:
        key = f"{fit['method']}_{fit['seed']}"
        err = np.abs(allpred[key][fit["members"]] - ev["test_y"][fit["members"]])
        close("RCTL_fit_report_MAE", err.mean(), fit["test_mean_scaled_mae"])
        close("RCTL_fit_report_percell", err.mean(1), fit["test_per_cell_mae"])
        check("RCTL_sampled_RSS_within_cap", 0 < fit["rss_bytes"] < settings["ram_cap_bytes"])
    freeze = fields(
        "results/pre_RCTL_freeze_hashes.json",
        ["risk_table_pilot.json", "02_candidate_and_pilot_plan.md", "risk_table_pilot.py"],
    )
    for name, expected_hash in freeze.items():
        k = ("results/" if name.endswith(".json") else "") + name
        check(
            "B1_frozen_hash",
            hashlib.sha256(path(k, ["sha256_only"]).read_bytes()).hexdigest() == expected_hash,
        )
    partial = arr("results/risk_table_partial_predictions.npz", ["quantiles", "median", "mean"])
    for key in ["quantiles", "median", "mean"]:
        close("B1_partial_matches_final", partial[key], b1[key] if key in b1 else b1more[key], 0)
    synthetic = fields(
        "results/risk_table_synthetic.json",
        ["discrete_exact_checks", "same_median_extra_loss", "previous_counterexample", "scope"],
    )
    atoms = np.array([[0] * 9, [1] * 9, [0, 0, 0, 0, 2, 4, 4, 4, 4]], float)
    grid = np.linspace(0, 4, 401)
    for group, rec in synthetic["discrete_exact_checks"].items():
        g = json.loads(group)
        loss = np.abs(atoms[g] - rec["optimal_action"]).mean(1).sum()
        optimum = np.abs(atoms[g, :, None] - grid).mean(1).sum(0).min()
        close("synthetic_recorded_loss", loss, rec["exact_sum_mae"], 1e-10)
        close("synthetic_minimum", loss, optimum, 1e-10)
    aa = np.linspace(-1, 1, 101)
    bb = np.linspace(-4, 4, 101)
    widegrid = np.linspace(-4, 4, 801)
    delta = (
        np.min(np.abs(aa[:, None] - widegrid).mean(0) + np.abs(bb[:, None] - widegrid).mean(0))
        - np.abs(aa).mean()
        - np.abs(bb).mean()
    )
    close("synthetic_same_median", delta, synthetic["same_median_extra_loss"], 1e-10)
    close(
        "synthetic_old_median",
        np.median([1, 1, 1.015]),
        synthetic["previous_counterexample"]["chosen_actual_median"],
        0,
    )
    close(
        "synthetic_old_error",
        1.015 - 1,
        synthetic["previous_counterexample"]["third_cell_error"],
        0,
    )
    if manifest:
        for key in mapping:
            if key not in accessed:
                path(key.removeprefix(base), ["sha256_only"])
        for key, row in accessed.items():
            check(
                "declared_automated_scope",
                set(row["read_scope"]) == set(mapping[key]["automated_read_scope"]),
            )
    counterexamples = []
    for seed in [20260925, 20260926]:
        tab = allpred[f"tabicl_risk_{seed}"].astype(float)
        emp = allpred[f"empirical_risk_{seed}"].astype(float)
        truth = ev["test_y"].astype(float)
        for name, (lo, hi) in dict(first240=(0, 240), last240=(240, 480), all480=(0, 480)).items():
            te = np.abs(tab[:, lo:hi] - truth[:, lo:hi])
            ee = np.abs(emp[:, lo:hi] - truth[:, lo:hi])
            delta = (te - ee).mean(1)
            counterexamples.append(
                dict(
                    seed=seed,
                    period=name,
                    Tab_MAE=float(te.mean()),
                    empirical_MAE=float(ee.mean()),
                    relative_percent=float(100 * (te.mean() - ee.mean()) / ee.mean()),
                    harm_cell_ids=ids[delta > 0].tolist(),
                    help_cell_ids=ids[delta < 0].tolist(),
                    per_cell_delta=delta.tolist(),
                    raw_Tab_MAE=float((te * ev["scales"][:, None]).mean()),
                    raw_empirical_MAE=float((ee * ev["scales"][:, None]).mean()),
                )
            )
    out = dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks=dict(counts),
        max_difference=max(differences),
        max_by_check=max_by_check,
        model_executions=0,
        historical_code_executed=False,
        accessed=list(accessed.values()),
        projection_averages=projection["averages"],
        B1_partitions=b1summary["partitions"],
        B2_surrogate=proposal["surrogate_validation"],
        pair_diagnostics=diagnostic["surrogate_pair_diagnostic"],
        Tab_costs=costs,
        RCTL_metrics=metrics,
        RCTL_resampling=resampling,
        fit_count=29,
        epochs=epochs,
        H5_target_proof=(
            "history-001-H5-check.json (separate local audit; not rerun by this verifier)"
        ),
        archive_counterexamples=counterexamples,
        numpy_version=np.__version__,
        RCTL_costs=dict(
            wall_seconds=finished["wall_seconds"],
            fit_seconds_sum=sum(f["fit_seconds"] for f in fits),
            max_fit_end_sampled_RSS_bytes=max(f["rss_bytes"] for f in fits),
        ),
        limits=[
            "B1 투영은 같은 시점의 B2 저장 query_bins를 사용한다. "
            "원 코드 입력·설정은 일치하나 KMeans를 재학습해 bin을 독립 생성하지 않았다.",
            "KMeans/Ridge/KNN/Tab/RCTL 및 교차오차 profile clustering은 재실행하지 않았다. "
            "가중치·anchor는 저장 구조를 대조했다.",
            "B2 action 범위는 실제 query target을 포함한 다섯 대안에서 구성됐다. "
            "04 계획 문구와 실제 코드의 차이를 보존한다.",
            "float32 MAE 허용오차1e-7, 상대변화율1e-5 percentage points, "
            "손실표·병합·쌍별 진단1e-10. 전체 최대차는 서로 다른 단위다.",
            "원 H5 target은 별도 로컬 검사 history-001-H5-check.json에서 대조했다. "
            "이 검산은 H5나 원 CDR 처리·과거 환경을 다시 실행하지 않는다.",
            "05/09 문헌과08 유한표본 자료는 별도 검수 대기다.",
            "cell·전후반 반례는 보존 예측에 대한 아카이브 추가 산술이다. 새 모델 실험이 아니다.",
        ],
    )
    return out


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
            dict(
                success=report["success"],
                checks=sum(report["checks"].values()),
                max_difference=report["max_difference"],
                model_executions=0,
                accessed_sources=len(report["accessed"]),
            )
        )
    )
