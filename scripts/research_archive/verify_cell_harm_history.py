"""Verify saved cell-harm arithmetic and selection lineage without model execution."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
from pathlib import Path

import numpy as np

PRIMARY = [
    "global_20260925",
    "tabicl_risk_20260925",
    "empirical_risk_20260925",
    "knn_risk_20260925",
    "pcc_balanced_20260925",
    "random_balanced_20260925",
]
CELLS = [
    3737,
    3745,
    3753,
    3765,
    4537,
    4545,
    4553,
    4565,
    5337,
    5345,
    5353,
    5365,
    6137,
    6145,
    6153,
    6165,
]
SIMPLE = ["global_Ridge", "global_HGB", "persistence", "daily_naive", "weekly_naive"]


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    """Reject duplicate JSON keys rather than silently discard evidence."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(raw: bytes) -> object:
    """Decode stored JSON without importing historical code."""
    return json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object)


def verify(manifest_path: Path) -> dict:
    """Check identity, saved losses, validation alignment, selection and cost."""
    manifest_path = manifest_path.resolve()
    manifest = read_json(manifest_path.read_bytes())
    checks = []

    def check(name: str, condition: bool) -> None:
        """Stop at the first named discrepancy."""
        if not condition:
            raise ValueError(name)
        checks.append(name)

    def same(name: str, actual: object, expected: object, tolerance: float = 1e-12) -> None:
        """Compare finite numeric values with matching shapes and no Boolean coercion."""
        a, b = np.asarray(actual), np.asarray(expected)
        check(
            name,
            a.shape == b.shape
            and a.dtype.kind in "fiu"
            and b.dtype.kind in "fiu"
            and np.isfinite(a).all()
            and np.isfinite(b).all()
            and np.allclose(a, b, rtol=0, atol=tolerance),
        )

    def integer(name: str, actual: object, expected: int) -> None:
        """Require an integer count, rejecting Boolean or floating-point substitutes."""
        check(name, type(actual) is int and actual == expected)

    check("batch", manifest["batch_id"] == "history-025")
    rows = manifest["sources"]
    raw, by_path = {}, {}
    check("16_distinct_sources", len(rows) == len({r["source_id"] for r in rows}) == 16)
    for row in rows:
        content = (manifest_path.parent / row["archive_path"]).read_bytes()
        check(
            row["source_id"] + ":identity",
            len(content) == row["size_bytes"]
            and hashlib.sha256(content).hexdigest() == row["sha256"],
        )
        raw[row["source_id"]] = content
        by_path[row["path"]] = row
    integer("new_preserved_files", manifest["new_preserved_files"], 7)
    integer("reuse_references", manifest["reused_references"], 9)
    check("44_remains_partial", manifest["partial_record_ids"] == ["0044"])
    check("no_original_execution", manifest["original_scripts_executed"] is False)
    integer("current_model_runs", manifest["current_model_runs"], 0)
    result = read_json(raw["SRC-0024832"])
    settings = read_json(raw["SRC-0024835"])
    finish = read_json(raw["SRC-0024833"])
    start = read_json(raw["SRC-0024834"])
    check(
        "result_top_level_schema",
        set(result)
        == {
            "complete",
            "settings",
            "cell_ids",
            "methods",
            "oracle",
            "numeric_wall_seconds",
            "observed_rss_bytes",
            "input_files_unchanged",
            "research_recommendation_selected",
        },
    )
    check("settings_match", result["settings"] == settings)
    check("primary_order", settings["primary_order"] == PRIMARY)
    for field, sid in [("code_sha256", "SRC-0022569"), ("plan_sha256", "SRC-0021529")]:
        check(field, settings[field] == hashlib.sha256(raw[sid]).hexdigest())
    check("three_direct_inputs", len(settings["inputs"]) == 3)
    for rel, digest in settings["inputs"].items():
        path = "tmp/redesign_20260925/" + rel.replace("\\", "/")
        check("input_hash:" + rel, by_path[path]["sha256"] == digest)
    for field in ["new_RCTL_fits", "new_RCTL_forward", "new_TabICL_contexts", "new_simple_fits"]:
        integer(field, settings[field], 0)
    check(
        "no_repartition_or_independent_test",
        settings["change_partitions"] is False and settings["independent_test"] is False,
    )
    check(
        "completion_reports",
        result["complete"] is True
        and finish["complete"] is True
        and finish["error"] is None
        and result["input_files_unchanged"] is True
        and result["research_recommendation_selected"] is False,
    )
    check(
        "start_marker",
        type(start["pid"]) is int
        and start["pid"] > 0
        and type(start["unix"]) in (int, float)
        and math.isfinite(start["unix"]),
    )
    integer("wall_cap", settings["wall_cap_seconds"], 30)
    integer("rss_cap", settings["rss_cap_bytes"], 1024**3)
    check(
        "reported_timers",
        all(
            type(v) in (int, float) and math.isfinite(v)
            for v in [result["numeric_wall_seconds"], finish["elapsed_seconds"]]
        )
        and 0 < result["numeric_wall_seconds"] < finish["elapsed_seconds"] < 30,
    )
    check(
        "end_observed_RSS",
        type(result["observed_rss_bytes"]) is int and 0 < result["observed_rss_bytes"] < 1024**3,
    )

    with (
        np.load(io.BytesIO(raw["SRC-0030211"]), allow_pickle=False) as src,
        np.load(io.BytesIO(raw["SRC-0029142"]), allow_pickle=False) as aux,
        np.load(io.BytesIO(raw["SRC-0027514"]), allow_pickle=False) as frozen,
        np.load(io.BytesIO(raw["SRC-0023577"]), allow_pickle=False) as design,
    ):
        y = src["y"].astype(np.float64)
        check("development_shape", y.shape == (16, 480))
        for label, ids in [
            ("result", result["cell_ids"]),
            ("rctl", src["cell_ids"]),
            ("aux", aux["cell_ids"]),
            ("frozen", frozen["cell_ids"]),
            ("proposal", read_json(raw["SRC-0023588"])["cell_ids"]),
        ]:
            same(label + ":cell_order", ids, CELLS, 0)
        same("aux_target", aux["y"], y, 0)
        same("development_times", aux["times"], np.arange(1008, 1488), 0)
        same("design_times", design["times"], np.arange(168, 1008), 0)
        same("aux_scales", aux["scales"], src["scales"], 0)
        selected = np.asarray(
            [np.flatnonzero(design["cell_indices"] == c - 1).item() for c in CELLS]
        )
        same("same_normalization", design["scales"][selected], src["scales"], 0)
        same("first672_raw_mean_scale", design["raw"][:672].mean(axis=0), design["scales"], 1e-9)
        same("validation_targets", design["Y"][selected, 672:], frozen["validation_y"], 0)
        check("positive_scales", np.isfinite(src["scales"]).all() and (src["scales"] > 0).all())
        predictions = {
            k: src[k].astype(np.float64) for k in src.files if k not in ["y", "scales", "cell_ids"]
        }
        for k, p in predictions.items():
            same("aux_reuses:" + k, aux[k], p, 0)
        predictions.update({k: aux[k] for k in SIMPLE})
        expected_methods = set(
            PRIMARY + ["tabicl_risk_20260926", "empirical_risk_20260926"] + SIMPLE
        )
        check(
            "13_methods",
            set(predictions) == expected_methods
            and len(result["methods"]) == 13
            and {r["method"] for r in result["methods"]} == expected_methods,
        )
        losses = {}
        for k, p in predictions.items():
            check("prediction_shape_finite:" + k, p.shape == y.shape and np.isfinite(p).all())
            losses[k] = np.abs(p - y)
        global_loss = losses[PRIMARY[0]]
        methods = []
        method_fields = {
            "method",
            "overall_mae",
            "per_cell_mae",
            "overall_delta_vs_global",
            "per_cell_delta_vs_global",
            "per_cell_half_deltas",
            "better_cells",
            "both_halves_better_cells",
            "both_halves_better_cell_ids",
        }
        for row in result["methods"]:
            k = row["method"]
            check(k + ":schema", set(row) == method_fields)
            loss = losses[k]
            delta = loss - global_loss
            halves = np.column_stack([delta[:, :240].mean(axis=1), delta[:, 240:].mean(axis=1)])
            for field, value in dict(
                overall_mae=loss.mean(),
                per_cell_mae=loss.mean(axis=1),
                overall_delta_vs_global=delta.mean(),
                per_cell_delta_vs_global=delta.mean(axis=1),
                per_cell_half_deltas=halves,
            ).items():
                same(k + ":" + field, row[field], value)
            integer(k + ":better_cells", row["better_cells"], int((delta.mean(axis=1) < 0).sum()))
            both = np.all(halves < 0, axis=1)
            integer(k + ":both_halves", row["both_halves_better_cells"], int(both.sum()))
            same(k + ":both_ids", row["both_halves_better_cell_ids"], np.asarray(CELLS)[both], 0)
            methods.append(
                {
                    key: row[key]
                    for key in [
                        "method",
                        "overall_mae",
                        "overall_delta_vs_global",
                        "better_cells",
                        "both_halves_better_cells",
                        "both_halves_better_cell_ids",
                    ]
                }
                | dict(
                    first240_delta=float(halves[:, 0].mean()),
                    last240_delta=float(halves[:, 1].mean()),
                )
            )

        fit = read_json(raw["SRC-0027517"])
        check(
            "validation_time_settings", fit["settings"]["validation_target_indices"] == [840, 1007]
        )
        check(
            "validation_design_identity",
            fit["settings"]["design_data_sha256"] == hashlib.sha256(raw["SRC-0023577"]).hexdigest(),
        )
        check(
            "validation_code_identity",
            fit["settings"]["code_sha256"] == hashlib.sha256(raw["SRC-0022860"]).hexdigest(),
        )
        validation = []
        checkpoint_count = 0
        for name in PRIMARY:
            aggregate = [r for r in fit["aggregates"] if f"{r['method']}_{r['seed']}" == name]
            check(name + ":one_validation_aggregate", len(aggregate) == 1)
            per_cell = np.full(16, np.nan)
            for row in fit["records"]:
                if f"{row['method']}_{row['seed']}" != name:
                    continue
                members = np.asarray(row["members"])
                check(
                    name + f":cluster{row['cluster']}:members",
                    members.dtype.kind in "iu"
                    and members.ndim == 1
                    and len(np.unique(members)) == len(members)
                    and ((members >= 0) & (members < 16)).all()
                    and np.isnan(per_cell[members]).all(),
                )
                p = frozen[f"{name}_cluster{row['cluster']}_validation_prediction"]
                check(
                    name + f":cluster{row['cluster']}:shape",
                    p.dtype == np.float32
                    and p.shape == (len(members), 168)
                    and np.isfinite(p).all(),
                )
                values = np.abs(p - frozen["validation_y"][members]).mean(axis=1)
                same(
                    name + f":cluster{row['cluster']}:validation",
                    values,
                    row["validation_per_cell_mae"],
                    0,
                )
                per_cell[members] = values
                checkpoint_count += 1
            same(
                name + ":validation_cell_lineage",
                per_cell,
                aggregate[0]["per_cell_validation_mae"],
                0,
            )
            validation.append(per_cell)
        check("21_primary_validation_checkpoints", checkpoint_count == 21)
        stack = np.stack([losses[k] for k in PRIMARY])
        hindsight_choice = stack.mean(axis=2).argmin(axis=0)
        val_choice = np.asarray(validation).argmin(axis=0)
        cell_oracle = stack[hindsight_choice, np.arange(16)].mean()
        val_selected = stack[val_choice, np.arange(16)].mean()
        oracle = result["oracle"]
        values = dict(
            global_mae=global_loss.mean(),
            cell_hindsight_oracle_mae=cell_oracle,
            cell_hindsight_oracle_relative_gain_percent=100
            * (global_loss.mean() - cell_oracle)
            / global_loss.mean(),
            sample_hindsight_oracle_mae=stack.min(axis=0).mean(),
            validation_chosen_development_mae=val_selected,
            validation_chosen_relative_change_percent=100
            * (val_selected - global_loss.mean())
            / global_loss.mean(),
        )
        for field, value in values.items():
            same("oracle:" + field, oracle[field], value)
        integer(
            "validation_global_count",
            oracle["validation_global_count"],
            int((val_choice == 0).sum()),
        )
        integer(
            "validation_hindsight_same",
            oracle["validation_hindsight_same_choice_count"],
            int((val_choice == hindsight_choice).sum()),
        )
        check(
            "hindsight_choices",
            oracle["cell_hindsight_choices"] == [PRIMARY[i] for i in hindsight_choice],
        )
        check(
            "validation_choices", oracle["validation_choices"] == [PRIMARY[i] for i in val_choice]
        )
        check("no_valid_clustering", oracle["no_valid_clustering_method_derived"] is True)
        check(
            "six_path_scope",
            oracle["scope"]
            == (
                "Only the six already-fitted primary conditions; "
                "unattainable hindsight diagnostics, not a bound on arbitrary clustering."
            ),
        )
        selections = [
            dict(
                cell_id=c,
                hindsight=PRIMARY[int(hindsight_choice[i])],
                validation=PRIMARY[int(val_choice[i])],
                hindsight_mae=float(stack[hindsight_choice[i], i].mean()),
                validation_chosen_mae=float(stack[val_choice[i], i].mean()),
            )
            for i, c in enumerate(CELLS)
        ]

    ledger = read_json(raw["SRC-0022700"])
    tab_names = [
        "smoke",
        "B1_anchor_and_cross_query",
        "B2_observed_query",
        "cell_identity_information_diagnostic",
        "broad_cell_information",
        "target_parameterization",
    ]
    stages = [r for r in ledger["model_calls_by_stage"] if r["stage"] in tab_names]
    check(
        "six_historical_Tab_stages",
        len(stages) == 6 and {r["stage"] for r in stages} == set(tab_names),
    )
    same("historical_Tab_contexts", sum(r["contexts"] for r in stages), 45, 0)
    same("historical_Tab_rows", sum(r["predicted_query_rows"] for r in stages), 35712, 0)
    frozen_stages = [
        r
        for r in ledger["inference_only_stages"]
        if r["stage"] in ["frozen_recursive_horizon", "frozen_fit_gap_34"]
    ]
    check(
        "two_historical_frozen_stages",
        len(frozen_stages) == 2 and len({r["stage"] for r in frozen_stages}) == 2,
    )
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
        "information_claim_audit_37",
        "cell_harm_envelope_42",
    ]
    cheap = ledger["new_cheap_diagnostic_seconds"]
    same("one_42_ledger_value", cheap["cell_harm_envelope_42"], result["numeric_wall_seconds"], 0)
    training = read_json(raw["SRC-0030280"])["execution"]
    integer("historical_RCTL_fits", training["fits_completed"], 29)
    costs = dict(
        TabICL_seconds=sum(r["fit_predict_seconds"] for r in stages),
        RCTL_training_wall_seconds=training["wall_seconds"],
        frozen_seconds=sum(r["wall_seconds"] for r in frozen_stages),
        cheap_seconds_through42=sum(cheap[k] for k in cheap_names),
    )
    costs["reported_modeling_seconds_through42"] = sum(costs.values())
    same("modeling_prefix", costs["reported_modeling_seconds_through42"], 1947.6963812, 1e-9)
    costs.update(
        numeric_wall_seconds=result["numeric_wall_seconds"],
        finish_elapsed_seconds=finish["elapsed_seconds"],
        observed_end_RSS_bytes=result["observed_rss_bytes"],
        cheap_prefix_names=cheap_names,
        TabICL_contexts=45,
        TabICL_query_rows=35712,
        RCTL_fits=29,
    )
    return dict(
        success=True,
        batch_id="history-025",
        checks=len(checks),
        check_names=checks,
        methods=methods,
        oracle=oracle,
        cell_selections=selections,
        cost=costs,
        source_files=16,
        validation_checkpoints_reconciled=21,
        new_model_runs=0,
        original_scripts_imported=False,
        checkpoint_loaded_or_executed=False,
        limits=[
            "Saved numeric reconciliation, not refitting or independent empirical replication.",
            "Validation was already used for checkpoint selection; "
            "development outcomes already observed.",
            "Six existing prediction paths only; hindsight selection is not deployable clustering.",
            "Historical timers and end RSS are not remeasured process wall "
            "or continuous peak memory.",
            "Record 44 literature and role synthesis remain separately pending.",
        ],
    )


def main() -> None:
    """Write a portable audit report for the supplied archive manifest."""
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
                    "source_files",
                    "validation_checkpoints_reconciled",
                    "new_model_runs",
                ]
            }
        )
    )


if __name__ == "__main__":
    main()
