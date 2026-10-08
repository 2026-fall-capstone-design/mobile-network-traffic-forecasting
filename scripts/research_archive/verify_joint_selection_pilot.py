"""633의 저장 예측·동일 입력·고정 소속 RCTL 효용을 검산한다. 모델은 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import numpy as np

PERIODS = {"first240": (0, 240), "last240": (240, 480), "all480": (0, 480)}


def verify(source: Path) -> dict:
    archive_manifest = json.loads(source.read_text(encoding="utf-8")) if source.is_file() else None
    mapping_sources = (
        {r["path"]: r for r in archive_manifest["sources"]} if archive_manifest else {}
    )
    base = "tmp/redesign_20260925/"
    stage = "results/same_data_joint_Tab_633/"
    accessed = {}
    checks = Counter()
    diffs = []

    def check(name, ok):
        checks[name] += 1
        if not ok:
            raise AssertionError((name, checks[name]))

    def close(name, a, b, tol=1e-10):
        a, b = np.asarray(a), np.asarray(b)
        check(name + "_shape", a.shape == b.shape)
        d = float(np.max(np.abs(a.astype(float) - b.astype(float))))
        diffs.append(d)
        check(name, np.isfinite(d) and d <= tol)

    def path(key, scopes):
        key = base + key
        p = (
            source.parent / mapping_sources[key]["archive_path"]
            if archive_manifest
            else source / key
        )
        if key not in accessed:
            raw = p.read_bytes()
            accessed[key] = dict(
                path=key, sha256=hashlib.sha256(raw).hexdigest(), size_bytes=len(raw), read_scope=[]
            )
            if archive_manifest:
                check(
                    "portable_source_identity",
                    accessed[key]["sha256"] == mapping_sources[key]["sha256"]
                    and len(raw) == mapping_sources[key]["size_bytes"],
                )
        accessed[key]["read_scope"] = sorted(set(accessed[key]["read_scope"]) | set(scopes))
        return p

    def fields(key, keys):
        data = json.loads(path(key, ["json_parsed"]).read_text(encoding="utf-8-sig"))
        out = {}
        for k in keys:
            out[k] = data[k]
            path(key, ["json_top_level:" + k])
        return out

    def sequence(key):
        return json.loads(path(key, ["json_full_list"]).read_text(encoding="utf-8-sig"))

    def arrays(key, keys):
        with np.load(path(key, ["array:" + k for k in keys]), allow_pickle=False) as data:
            return {k: data[k].copy() for k in keys}

    def sha(key):
        path(key, ["sha256_only"])
        return accessed[base + key]["sha256"]

    def digest(a):
        return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()

    cfg = fields(
        stage + "frozen_settings.json",
        [
            "cohorts",
            "tie_order",
            "limits",
            "seed",
            "context_rows",
            "planned_unique_groups",
            "reserved_new_contexts",
            "reserved_new_query_rows",
            "all_periods_development",
            "RCTL_access",
            "output_type",
            "source_cohorts",
            "source_hashes",
            "HGB_params",
        ],
    )
    plan = fields(
        "633_same_data_joint_Tab_groups.json", ["cohorts", "contexts_cap", "query_rows_cap"]
    )
    native = fields(
        stage + "result.json",
        [
            "records",
            "new_Tab_contexts",
            "new_Tab_query_rows",
            "reused_Tab_contexts",
            "reused_Tab_query_rows",
            "HGB_new_fits",
            "RCTL_new_fits",
            "new_candidate_adopted",
            "all_periods_development",
        ],
    )
    bridge = fields(
        stage + "bridge_result.json",
        [
            "records",
            "native_choices_modified",
            "new_memberships",
            "new_models",
            "new_predictions",
            "all_periods_development",
        ],
    )
    check("fixed_cohorts", cfg["cohorts"] == plan["cohorts"])
    check(
        "protocol",
        cfg["seed"] == 20260925
        and cfg["tie_order"] == ["UPC", "HGB", "Tab"]
        and cfg["output_type"] == "median"
        and not cfg["RCTL_access"],
    )
    check(
        "planned_counts",
        plan["contexts_cap"] == cfg["planned_unique_groups"] == 22
        and plan["query_rows_cap"] == 6016
        and cfg["context_rows"] == 47376,
    )
    reused = []
    all_group_rows = 0
    native_table = []
    rctl_table = []
    for ci, co in enumerate(cfg["cohorts"]):
        ids = co["cell_ids"]
        check("cohort_cardinality", len(ids) == 16 and len(set(ids)) == 16)
        inputkey = f"results/fixed_reference_vs_joint_pool_616/inputs_{ci}.npz"
        inp = arrays(inputkey, ["train_X", "train_y", "query_X", "query_times", "cell_ids"])
        x, y, q, qt = (
            inp["train_X"],
            inp["train_y"],
            inp["query_X"].reshape(16, 64, 16),
            inp["query_times"],
        )
        check("inputshape", x.shape == (16, 504, 16) and y.shape == (16, 504))
        check("input_ids", inp["cell_ids"].tolist() == ids)
        check(
            "input_times",
            len(qt) == 64 and qt[0] == 672 and qt[-1] == 839 and np.all(np.diff(qt) > 0),
        )
        origin_truth = arrays(
            f"results/fixed_reference_vs_joint_pool_616/errors_{ci}.npz",
            ["truth", "cell_ids", "query_times"],
        )
        errors = arrays(
            stage + f"errors_{ci}.npz",
            ["truth", "cell_ids", "query_times"]
            + [f"{a}_{b}" for a in ["Tab", "HGB"] for b in ["UPC", "Tab", "HGB"]],
        )
        check(
            "truth_ID_time",
            errors["cell_ids"].tolist() == origin_truth["cell_ids"].tolist() == ids
            and np.array_equal(qt, errors["query_times"])
            and np.array_equal(qt, origin_truth["query_times"]),
        )
        close("truth_identity", errors["truth"], origin_truth["truth"])
        manifest = sequence(stage + f"group_manifest_{ci}.json")
        check("group_count", len(manifest) == len(co["groups"]) == (12 if ci == 0 else 10))
        bank = {}
        for item, g in zip(manifest, co["groups"], strict=True):
            key = item["path"]
            check("group_file_hash", sha(key) == item["sha256"])
            a = arrays(key, ["Tab", "HGB", "group_cell_ids", "members", "query_times"])
            members = g["members"]
            group = tuple(g["cell_ids"])
            check(
                "group_identity",
                list(group)
                == item["group"]
                == a["group_cell_ids"].tolist()
                == [ids[j] for j in members]
                and members == item["members"] == a["members"].tolist(),
            )
            check(
                "group_shape_time",
                a["Tab"].shape == a["HGB"].shape == (len(members), 64)
                and np.array_equal(qt, a["query_times"]),
            )
            check(
                "context_contract",
                digest(x[members].reshape(-1, 16)) == item["train_X_sha256"]
                and digest(y[members].reshape(-1)) == item["train_y_sha256"]
                and digest(q[members].reshape(-1, 16)) == item["query_X_sha256"],
            )
            check(
                "group_rows",
                g["context_rows"] == 504 * len(members) and g["query_rows"] == 64 * len(members),
            )
            all_group_rows += g["context_rows"]
            hkey = item["HGB_source"]
            check("HGB_source_hash", sha(hkey) == item["HGB_source_sha256"])
            h = arrays(hkey, ["pred", "group_cell_ids", "predicted_cell_ids", "query_times"])
            check(
                "HGB_group_time",
                h["group_cell_ids"].tolist() == list(group)
                and np.array_equal(qt, h["query_times"]),
            )
            predicted = h["predicted_cell_ids"].tolist()
            close(
                "HGB_exact_source_reuse",
                a["HGB"],
                np.stack([h["pred"][predicted.index(cell)] for cell in group]),
            )
            if item["Tab_reused"]:
                check("only_two_Tab_singletons", ci == 1 and list(group) in [[6565], [7337]])
                reused.append(list(group))
            bank[group] = a
        rec = native["records"][ci]
        seal = fields(
            stage + f"selection_sealed_{ci}.json", ["cohort", "Tab", "HGB", "RCTL_read", "labels"]
        )
        check(
            "native_labels",
            rec["cell_ids"] == ids
            and rec["labels"] == seal["labels"] == co["labels"]
            and not seal["RCTL_read"],
        )
        for model in ["Tab", "HGB"]:
            means = {}
            for name, labels in co["labels"].items():
                check("K4", len(labels) == 16 and set(labels) == {0, 1, 2, 3})
                predictions = []
                for j in range(len(ids)):
                    members = [i for i, label in enumerate(labels) if label == labels[j]]
                    group = tuple(ids[i] for i in members)
                    predictions.append(bank[group][model][members.index(j)])
                # Historical aggregation used np.empty without dtype, hence float64.
                pred = np.stack(predictions).astype(np.float64)
                truth = errors["truth"].astype(np.float64)
                err = np.abs(pred - truth)
                close("saved_error_identity", err, errors[model + "_" + name])
                for lo, hi, tag in [(0, 64, "MAE"), (0, 32, "first32"), (32, 64, "last32")]:
                    scalar = math.fsum(
                        abs(float(pred[j, t]) - float(truth[j, t]))
                        for j in range(16)
                        for t in range(lo, hi)
                    ) / (16 * (hi - lo))
                    close("native_MAE", scalar, rec["risks"][model]["scores"][name][tag])
                close(
                    "native_cell_MAE",
                    err.mean(axis=1),
                    rec["risks"][model]["scores"][name]["per_cell_MAE"],
                )
                means[name] = float(err.mean())
            chosen = min(cfg["tie_order"], key=lambda n: (means[n], cfg["tie_order"].index(n)))
            check("selection", chosen == seal[model] == rec["risks"][model]["selected"])
            native_table.append(dict(cohort=ci, model=model, MAE=means, choice=chosen))
        rrkey = (
            "results/"
            + ("nonempty_assignment_RCTL_581" if ci == 0 else "refreshed_HGB_RCTL_bridge_632")
            + "/result.json"
        )
        rr = fields(rrkey, ["cohorts", "partitions", "metrics"])
        tag = "A" if ci == 0 else "B"
        mapping = dict(
            UPC=tag + "_UPC",
            Tab=tag + "_Tab_free",
            HGB=tag + ("_HGB_free" if ci == 0 else "_HGB_refreshed"),
        )
        check("RCTL_record_ids", rr["cohorts"][tag]["cell_ids"] == ids)
        for name, key in mapping.items():
            check("RCTL_partition_identity", rr["partitions"][key] == co["labels"][name])
        br = bridge["records"][ci]
        check(
            "bridge_mapping",
            br["selected_RCTL"] == {model: mapping[seal[model]] for model in ["Tab", "HGB"]},
        )
        for window in ["first240", "last240", "all480"]:
            t = rr["metrics"][mapping[seal["Tab"]]][window]
            h = rr["metrics"][mapping[seal["HGB"]]][window]
            u = rr["metrics"][mapping["UPC"]][window]
            b = br["metrics"][window]
            close(
                "RCTL_reported_values",
                [t["mean_cell_MAE"], h["mean_cell_MAE"], u["mean_cell_MAE"]],
                [b["Tab_choice_MAE"], b["HGB_choice_MAE"], b["UPC_MAE"]],
            )
            delta = np.array(t["per_cell_MAE"]) - h["per_cell_MAE"]
            close("RCTL_percell_deltas", delta, b["per_cell_deltas"])
            close("RCTL_mean_delta", delta.mean(), b["Tab_minus_HGB"])
            close(
                "RCTL_percent",
                100 * (t["mean_cell_MAE"] - h["mean_cell_MAE"]) / h["mean_cell_MAE"],
                b["relative_percent"],
            )
        rctl_table.append(
            dict(
                cohort=ci,
                reported_relative_percent={
                    w: br["metrics"][w]["relative_percent"]
                    for w in ["first240", "last240", "all480"]
                },
                all480_harmed_cells=sum(v > 0 for v in br["metrics"]["all480"]["per_cell_deltas"]),
                all480_helped_cells=sum(v < 0 for v in br["metrics"]["all480"]["per_cell_deltas"]),
            )
        )
    check("overall_rows", all_group_rows == 47376)
    check("reused_singletons", sorted(reused) == [[6565], [7337]])
    check(
        "new_counts",
        native["new_Tab_contexts"] == 20
        and native["new_Tab_query_rows"] == 5888
        and native["reused_Tab_contexts"] == 2
        and native["reused_Tab_query_rows"] == 128,
    )
    settled = fields(
        stage + "settled.json",
        [
            "seconds",
            "Tab_seconds",
            "other_seconds",
            "new_Tab_contexts",
            "new_Tab_query_rows",
            "HGB_new_fits",
            "RCTL_new_fits",
            "success",
        ],
    )
    bs = fields(
        stage + "bridge_settled.json", ["seconds", "new_models", "new_predictions", "success"]
    )
    close("cost_sum", settled["seconds"], settled["Tab_seconds"] + settled["other_seconds"])
    check(
        "no_new_HGB_RCTL",
        settled["HGB_new_fits"]
        == settled["RCTL_new_fits"]
        == bs["new_models"]
        == bs["new_predictions"]
        == 0,
    )

    # Resolve 616 input lineage and exact singleton cache reuse.
    lineage = []
    for ci, co in enumerate(cfg["cohorts"]):
        oldstage = "results/" + cfg["source_cohorts"][ci]["source"] + "/"
        inp = arrays(
            f"results/fixed_reference_vs_joint_pool_616/inputs_{ci}.npz",
            ["train_X", "train_y", "query_X", "query_times", "cell_ids"],
        )
        sample_keys = [
            "cell_ids",
            "context_X",
            "context_Y",
            "query_X",
            "context_times",
            "context_cell_indices",
            "query_times",
        ]
        if ci == 0:
            sample_keys += ["selected_cells"]
        sample = arrays(oldstage + "sample_provenance.npz", sample_keys)
        ids = co["cell_ids"]
        qt = inp["query_times"]
        check(
            "lineage_ids_times",
            sample["cell_ids"].tolist() == ids
            and np.array_equal(qt, sample["query_times"])
            and np.array_equal(qt, np.rint(np.linspace(672, 839, 64)).astype(int)),
        )
        close("original_query_identity", inp["query_X"], sample["query_X"])
        rows = sample["context_cell_indices"]
        times = sample["context_times"]
        check("sample_time_boundaries", times.min() >= 168 and times.max() <= 671)
        close("sample_context_X_identity", inp["train_X"][rows, times - 168], sample["context_X"])
        close("sample_context_Y_identity", inp["train_y"][rows, times - 168], sample["context_Y"])
        truth = arrays(oldstage + "assignment_query_truth.npz", ["y", "cell_ids", "query_times"])
        native_truth = arrays(stage + f"errors_{ci}.npz", ["truth"])["truth"]
        check(
            "original_truth_labels",
            truth["cell_ids"].tolist() == ids and np.array_equal(truth["query_times"], qt),
        )
        close("original_truth_identity", native_truth, truth["y"])
        contract = fields(
            oldstage + "input_contract.json",
            [
                "group_hashes",
                "ensemble",
                "kv_cache",
                "seed",
                "n_jobs",
                "context_target_times",
                "query_times",
                "input_columns",
                "query_targets_passed_to_model",
                "query_targets_used_for_assignment",
            ],
        )
        check(
            "cache_parameters",
            contract["ensemble"] == 1
            and contract["kv_cache"]
            and contract["seed"] == 20260925
            and contract["n_jobs"] == 1
            and contract["context_target_times"] == [168, 671]
            and contract["input_columns"] == 16,
        )
        check(
            "target_role_metadata",
            not contract["query_targets_passed_to_model"]
            and contract["query_targets_used_for_assignment"],
        )
        if ci == 0:
            d = arrays("results/design_data.npz", ["X", "Y", "scales", "cell_indices", "times"])
            selected = sample["selected_cells"]
            scales = d["scales"][selected]
            check(
                "A_source_selection",
                (d["cell_indices"][selected] + 1).tolist() == ids
                and np.array_equal(d["times"], np.arange(168, 1008)),
            )
            close("A_full_train_X", inp["train_X"], d["X"][selected, :504])
            close("A_full_train_Y", inp["train_y"], d["Y"][selected, :504])
            close("A_full_query_X", inp["query_X"], d["X"][selected][:, qt - 168].reshape(-1, 16))
            close("A_query_truth", truth["y"], d["Y"][selected][:, qt - 168])
        else:
            f = arrays(
                oldstage + "feature_inputs_frozen.npz",
                [
                    "X",
                    "feature_times",
                    "scales",
                    "context_Y",
                    "context_times",
                    "cell_ids",
                    "feature_latest_traffic_times",
                    "feature_lag24_times",
                    "feature_lag168_times",
                    "query_times",
                ],
            )
            scales = f["scales"]
            t = np.arange(168, 840)
            check(
                "B_source_times",
                np.array_equal(f["feature_times"], t)
                and np.array_equal(f["context_times"], np.arange(168, 672))
                and f["cell_ids"].tolist() == ids
                and np.array_equal(f["query_times"], qt),
            )
            for k, lag in [
                ("feature_latest_traffic_times", 1),
                ("feature_lag24_times", 24),
                ("feature_lag168_times", 168),
            ]:
                check("B_lag_times", np.array_equal(f[k], t - lag))
            close("B_full_train_X", inp["train_X"], f["X"][:, :504])
            close("B_full_train_Y", inp["train_y"], f["context_Y"])
            close("B_full_query_X", inp["query_X"], f["X"][:, qt - 168].reshape(-1, 16))
            raw = arrays(
                oldstage + "UPC_inputs_frozen.npz",
                ["raw_first672", "cell_ids", "h5_cell_positions"],
            )
            check(
                "B_raw_labels",
                raw["cell_ids"].tolist() == ids
                and np.array_equal(raw["h5_cell_positions"], np.array(ids) - 1),
            )
            close("B_scale_mean_first672", scales, raw["raw_first672"].mean(axis=0))
            close(
                "B_train_truth_scale",
                inp["train_y"],
                (raw["raw_first672"][168:672] / scales).T.astype(np.float32),
            )
            oldcfg = fields(
                oldstage + "frozen_settings.json",
                ["source_hashes", "application_scope", "known_spatial_input_exposure", "cell_ids"],
            )
            check(
                "B_scope",
                oldcfg["application_scope"]
                == "same_city_same_time_development_not_independent_holdout"
                and oldcfg["known_spatial_input_exposure"] == [5753],
            )
            frozen = arrays(
                oldstage + "Tab_predictions_frozen.npz", ["prediction", "cell_ids", "query_times"]
            )
            check(
                "cache_prediction_bank",
                frozen["prediction"].shape == (4, 16, 64)
                and frozen["cell_ids"].tolist() == ids
                and np.array_equal(frozen["query_times"], qt),
            )
            caches = fields(
                stage + "cache_contract.json",
                [
                    "native_reused",
                    "HGB_groups",
                    "new_HGB",
                    "new_RCTL",
                    "full_context_not_subsampled",
                ],
            )
            found = []
            for item in contract["group_hashes"]:
                members = item["members"]
                if members not in [[6565], [7337]]:
                    continue
                j = ids.index(members[0])
                g = item["group"]
                close("singleton_full_X", sample["context_X"][g], inp["train_X"][j])
                close("singleton_full_Y", sample["context_Y"][g], inp["train_y"][j])
                check(
                    "singleton_all504_times",
                    np.array_equal(sample["context_times"][g], np.arange(168, 672)),
                )
                check(
                    "singleton_ordered_hash",
                    digest(inp["train_X"][j]) == item["X_sha256"]
                    and digest(inp["train_y"][j]) == item["Y_sha256"],
                )
                ni = next(k for k, gp in enumerate(co["groups"]) if gp["cell_ids"] == members)
                new = arrays(stage + f"groups/c1_g{ni}.npz", ["Tab"])
                close("singleton_prediction_exact_reuse", new["Tab"], frozen["prediction"][g, [j]])
                receipt = next(r for r in caches["native_reused"] if r["group"] == members)
                check(
                    "singleton_receipt",
                    receipt["source_sha256"] == sha(oldstage + "Tab_predictions_frozen.npz")
                    and receipt["context_X_sha256"] == item["X_sha256"]
                    and receipt["context_Y_sha256"] == item["Y_sha256"],
                )
                found.append(members[0])
            check("cache_exactly_two", sorted(found) == [6565, 7337])
            model_hashes = {
                k: v
                for k, v in oldcfg["source_hashes"].items()
                if k.startswith("runtime/Lib/site-packages/tabicl/") or k.startswith("assets/")
            }
            check(
                "cache_implementation_metadata",
                len(model_hashes) == 7
                and all(cfg["source_hashes"].get(k) == v for k, v in model_hashes.items()),
            )
        lineage.append(
            dict(
                cohort=ci,
                cell_ids=ids,
                scales=scales.tolist(),
                query_times=qt.tolist(),
                source=oldstage,
            )
        )

    # Reassemble all six fixed RCTL partitions from saved group outputs.
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
    rctl_metrics = {}
    rctl_provenance = []
    rctl_comparisons = []
    for ci, tag, rstage in [
        (0, "A", "nonempty_assignment_RCTL_581"),
        (1, "B", "refreshed_HGB_RCTL_bridge_632"),
    ]:
        pre = "results/" + rstage + "/"
        rc = fields(
            pre + "frozen_settings.json",
            list(fixed)
            + [
                "cohorts",
                "partitions",
                "tasks",
                "source_hashes",
                "training_core_sha256",
                "architecture",
                "all_periods_development",
                "RCTL_results_used_for_clustering",
            ],
        )
        check(
            "RCTL_fixed_protocol",
            all(rc[k] == v for k, v in fixed.items())
            and rc["architecture"] == "unchanged rctl_torch.RCTL"
            and rc["training_core_sha256"]
            == "232f3304ac3f0cdf868fcd4cf63a0ea7b9fa70e41498756d90c7732aeb916920",
        )
        check(
            "RCTL_development_scope",
            rc["all_periods_development"] and not rc["RCTL_results_used_for_clustering"],
        )
        co = rc["cohorts"][tag]
        ids = co["cell_ids"]
        prepkeys = ["seq", "y", "times", "cell_ids", "scales"] + (["flat"] if ci else [])
        prep = arrays(co["prepared_arrays"], prepkeys)
        check(
            "RCTL_prepared_shape_time",
            prep["seq"].shape == (16, 1320, 8, 9)
            and prep["y"].shape == (16, 1320)
            and np.array_equal(prep["times"], np.arange(168, 1488))
            and prep["cell_ids"].tolist() == ids,
        )
        check("RCTL_prepared_finite", all(np.isfinite(prep[k]).all() for k in prepkeys))
        close("RCTL_scale_identity", prep["scales"], lineage[ci]["scales"])
        check("RCTL_scale_positive", np.all(prep["scales"] > 0))
        nativeinp = arrays(
            f"results/fixed_reference_vs_joint_pool_616/inputs_{ci}.npz", ["train_y", "query_times"]
        )
        close("RCTL_native_train_target_identity", prep["y"][:, :504], nativeinp["train_y"])
        nt = arrays(stage + f"errors_{ci}.npz", ["truth"])["truth"]
        close("RCTL_native_query_truth_identity", prep["y"][:, nativeinp["query_times"] - 168], nt)
        if ci:
            features = arrays(
                "results/fixed_cohort_application_567/feature_inputs_frozen.npz", ["X"]
            )
            close("B_RCTL_flat_feature_identity", prep["flat"][:, :672], features["X"])
        truth = prep["y"][:, 840:].astype(float)
        for name in [pre + "evaluation_" + tag + ".npz", co["evaluation_reference"]]:
            ev = arrays(name, ["test_y", "cell_ids", "scales", "test_times"])
            check(
                "RCTL_evaluation_labels",
                ev["cell_ids"].tolist() == ids
                and np.array_equal(ev["test_times"], np.arange(1008, 1488)),
            )
            close("RCTL_evaluation_truth", ev["test_y"], truth)
            close("RCTL_evaluation_scales", ev["scales"], prep["scales"])
        mapping = {
            "UPC": tag + "_UPC",
            "Tab": tag + "_Tab_free",
            "HGB": tag + ("_HGB_free" if ci == 0 else "_HGB_refreshed"),
        }
        reported = fields(pre + "result.json", ["metrics", "partitions", "cohorts", "at"])
        fits = sequence(pre + "fit_results.json")
        bank = {m: np.full((16, 480), np.nan) for m in mapping.values()}
        for task in rc["tasks"]:
            method = task["method"]
            if method not in bank:
                continue
            group = task["cluster"]
            members = task["members"]
            stem = f"{method}_{fixed['seed']}_cluster{group}"
            key = pre + stem + ".npz"
            z = arrays(key, ["prediction", "y", "cell_ids", "members"])
            check(
                "RCTL_task_labels",
                task["seed"] == fixed["seed"]
                and members == [j for j, g in enumerate(rc["partitions"][method]) if g == group]
                and task["cell_ids"] == [ids[j] for j in members],
            )
            # Some byte-identical aliases retain origin member indices. Cell IDs align truth.
            check(
                "RCTL_output_labels",
                z["cell_ids"].tolist() == task["cell_ids"]
                and z["prediction"].shape == (len(members), 480),
            )
            close("RCTL_task_truth", z["y"], truth[members])
            bank[method][members] = z["prediction"]
            fit = next(f for f in fits if f["method"] == method and f["cluster"] == group)
            check(
                "RCTL_fit_identity",
                all(fit[k] == task[k] for k in ["method", "seed", "cluster", "members"]),
            )
            if task["reuse"]:
                rec = task["reuse"]["record"]
                origin = rec["artifacts"][".npz"]
                check(
                    "RCTL_exact_prediction_reuse",
                    fit["reused"]
                    and sha(key)
                    == sha(origin["relative_path"])
                    == sha(rec["completed_bridge_npz"])
                    == origin["sha256"],
                )
                old = fields(rec["source_settings"], [])
                # Read only the protocol/data fields actually present in older metadata.
                all_old = json.loads(
                    path(rec["source_settings"], ["json_parsed"]).read_text(encoding="utf-8-sig")
                )
                ks = [k for k in list(fixed) + ["prepared_arrays", "cohorts"] if k in all_old]
                old = fields(rec["source_settings"], ks)
                check("RCTL_reuse_protocol", all(old[k] == v for k, v in fixed.items() if k in old))
                check(
                    "RCTL_reuse_data_source",
                    old.get("prepared_arrays") == co["prepared_arrays"]
                    or old.get("cohorts", {}).get(tag, {}).get("prepared_arrays")
                    == co["prepared_arrays"],
                )
                check(
                    "RCTL_reuse_settings_hash",
                    sha(rec["source_settings"]) == rec["source_settings_sha256"],
                )
                history = sequence(rec["artifacts"]["_history.json"]["relative_path"])
                metadata = rec["fit_metadata"]
                origin_name = origin["relative_path"]
                missing = [k for k in fixed if k not in old]
            else:
                check("RCTL_original_fit_metadata", not fit["reused"])
                history = sequence(pre + stem + "_history.json")
                metadata = fit
                origin_name = key
                missing = []
            vals = np.array([h["val_mae"] for h in history])
            best = int(np.argmin(vals))
            check(
                "RCTL_validation_checkpoint",
                np.isfinite(vals).all()
                and len(history) == metadata["epochs_run"]
                and best + 1 == metadata["best_epoch"],
            )
            check(
                "RCTL_stopping_rule",
                (metadata["stop_reason"] == "validation_patience" and len(history) - best - 1 == 10)
                or (metadata["stop_reason"] == "epoch_cap" and len(history) == 80),
            )
            close("RCTL_best_validation", vals[best], metadata["best_val_mae"])
            rctl_provenance.append(
                dict(
                    method=method,
                    cluster=group,
                    cell_ids=task["cell_ids"],
                    origin=origin_name,
                    reused_in_source_stage=bool(task["reuse"]),
                    source_stage=rstage,
                    epochs=len(history),
                    best_epoch=best + 1,
                    protocol_fields_missing_from_origin_settings=missing,
                )
            )
        for name, method in mapping.items():
            check(
                "RCTL_frozen_labels",
                rc["partitions"][method]
                == reported["partitions"][method]
                == cfg["cohorts"][ci]["labels"][name],
            )
            pred = bank[method]
            check("RCTL_complete_coverage", np.isfinite(pred).all())
            rctl_metrics[method] = {}
            for window, (lo, hi) in PERIODS.items():
                per = np.abs(pred[:, lo:hi] - truth[:, lo:hi]).mean(axis=1)
                met = dict(
                    mean_cell_MAE=float(per.mean()),
                    mean_cell_raw_MAE=float(np.mean(per * prep["scales"])),
                    per_cell_MAE=per.tolist(),
                )
                for field, value in met.items():
                    close(
                        "RCTL_recomputed_" + field,
                        value,
                        reported["metrics"][method][window][field],
                    )
                rctl_metrics[method][window] = met
        native_rec = native["records"][ci]
        tabchoice = mapping[native_rec["risks"]["Tab"]["selected"]]
        hgbchoice = mapping[native_rec["risks"]["HGB"]["selected"]]
        comp = {}
        for window in PERIODS:
            a = rctl_metrics[tabchoice][window]
            b = rctl_metrics[hgbchoice][window]
            u = rctl_metrics[mapping["UPC"]][window]
            delta = np.array(a["per_cell_MAE"]) - b["per_cell_MAE"]
            comp[window] = dict(
                relative_percent=100 * (a["mean_cell_MAE"] / b["mean_cell_MAE"] - 1),
                raw_relative_percent=100 * (a["mean_cell_raw_MAE"] / b["mean_cell_raw_MAE"] - 1),
                Tab_minus_UPC=a["mean_cell_MAE"] - u["mean_cell_MAE"],
                Tab_minus_HGB=float(delta.mean()),
                harmed_cell_ids=[ids[j] for j in np.flatnonzero(delta > 0)],
                helped_cell_ids=[ids[j] for j in np.flatnonzero(delta < 0)],
            )
            close(
                "bridge_recomputed_percent",
                comp[window]["relative_percent"],
                bridge["records"][ci]["metrics"][window]["relative_percent"],
            )
        stable = (
            comp["all480"]["relative_percent"] >= 1
            and comp["first240"]["Tab_minus_HGB"] > 0
            and comp["last240"]["Tab_minus_HGB"] > 0
        )
        check("stable_harm_condition", stable and bridge["records"][ci]["branch"] == "stable_harm")
        check(
            "native_accuracy_positive_evidence",
            all(
                native_rec["risks"]["Tab"]["scores"][name]["MAE"]
                < native_rec["risks"]["HGB"]["scores"][name]["MAE"]
                for name in mapping
            )
            and bridge["records"][ci]["native_Tab_lower_MAE_on_all_candidates"],
        )
        rctl_comparisons.append(
            dict(cohort=ci, Tab_choice=tabchoice, HGB_choice=hgbchoice, periods=comp)
        )

    bridge_plan = fields(
        stage + "bridge_plan.json",
        ["at", "source_hashes", "new_models", "new_predictions", "all_development"],
    )
    for ci in [0, 1]:
        forecasts = fields(stage + f"forecasts_sealed_{ci}.json", ["at", "groups"])
        sel = fields(stage + f"selection_sealed_{ci}.json", ["at", "RCTL_read"])
        check(
            "sealed_before_RCTL_bridge",
            datetime.fromisoformat(forecasts["at"])
            < datetime.fromisoformat(sel["at"])
            < datetime.fromisoformat(bridge_plan["at"])
            and not sel["RCTL_read"],
        )
        check(
            "sealed_group_identity",
            forecasts["groups"] == sequence(stage + f"group_manifest_{ci}.json"),
        )
    hgb616 = fields(
        "results/fixed_reference_vs_joint_pool_616/frozen_settings.json",
        ["params", "source_hashes", "cohorts"],
    )
    hgb631 = fields("results/refreshed_HGB_assignment_631/frozen_settings.json", ["source_hashes"])
    check("HGB_fixed_params", cfg["HGB_params"] == hgb616["params"])
    check("HGB_input_cohorts", cfg["source_cohorts"] == hgb616["cohorts"])
    for hashes in [
        cfg["source_hashes"],
        bridge_plan["source_hashes"],
        hgb616["source_hashes"],
        hgb631["source_hashes"],
    ]:
        for key, expected in hashes.items():
            if base + key in accessed:
                check("bound_source_hash", accessed[base + key]["sha256"] == expected)
    check(
        "no_post_selection_changes",
        not bridge["native_choices_modified"]
        and bridge["new_memberships"] == bridge["new_models"] == bridge["new_predictions"] == 0,
    )
    check(
        "all_development",
        cfg["all_periods_development"]
        and native["all_periods_development"]
        and bridge["all_periods_development"],
    )
    run = fields(
        stage + "run_finished.json", ["success", "peak_process_tree_RSS_bytes", "seconds", "meter"]
    )
    close("settled_vs_run_seconds", run["seconds"], settled["seconds"])
    check(
        "meter_counts",
        run["success"]
        and all(
            run["meter"][n + "_attempted"] == run["meter"][n + "_completed"] == v
            for n, v in [("contexts", 20), ("query_rows", 5888)]
        ),
    )
    if archive_manifest:
        for key in mapping_sources:
            if key not in accessed:
                path(key.removeprefix(base), ["sha256_only"])
        for key, row in accessed.items():
            check(
                "declared_automated_scope",
                set(row["read_scope"]) == set(mapping_sources[key]["automated_read_scope"]),
            )

    return dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks=dict(checks),
        max_absolute_difference=max(diffs),
        model_executions=0,
        historical_code_executed=False,
        numpy_version=np.__version__,
        accessed=list(accessed.values()),
        native_table=native_table,
        RCTL_metrics=rctl_metrics,
        RCTL_comparisons=rctl_comparisons,
        RCTL_provenance=rctl_provenance,
        input_lineage=lineage,
        total_recorded_stage_and_bridge_seconds=settled["seconds"] + bs["seconds"],
        sampled_peak_tree_RSS_bytes=run["peak_process_tree_RSS_bytes"],
        limits=[
            "저장 예측과 정답·입력·메타데이터의 검산. "
            "모델 학습/추론이나 원자료 처리 재현이 아니다.",
            "B도 같은 도시·기간의 개발 자료이고 cell5753의 과거 입력 노출이 기록돼 있다.",
            "이전 RCTL 설정에서 생략된 프로토콜 필드는 provenance에 별도 기록한다.",
            "원단위 MAE 비교는 보존된 scale을 적용한 이번 아카이브의 추가 산술 대조이다.",
            "단일 seed와 고정 후보 메뉴의 두 개발 집단이다. "
            "stable_harm은 코드의 판정 규칙이며 유의성 검정이 아니다.",
            "RSS는 과거 controller의 0.1초 간격 표본이다.",
        ],
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
            dict(
                success=report["success"],
                checks=sum(report["checks"].values()),
                max_difference=report["max_absolute_difference"],
                model_executions=0,
                accessed_sources=len(report["accessed"]),
            )
        )
    )
