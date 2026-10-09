"""Check archived MAE moments and cost ledgers without running research code."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from datetime import UTC, datetime
from fractions import Fraction
from pathlib import Path


def verify(manifest_path: Path) -> dict:
    """Recompute the three stored outcomes and bounded historical cost arithmetic."""
    manifest_path = manifest_path.resolve()
    archive = manifest_path.parents[2]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks: list[str] = []
    errors: list[str] = []

    def check(name: str, condition: bool) -> None:
        """Retain both successful and failed domain checks in the result."""
        checks.append(name)
        if not condition:
            errors.append(name)

    paths = {}
    for source in manifest["sources"]:
        path = (manifest_path.parent / source["archive_path"]).resolve()
        if not path.is_relative_to(archive):
            raise ValueError("Evidence path must stay within the research archive")
        raw = path.read_bytes()
        check(
            source["source_id"] + ":preserved_bytes",
            len(raw) == source["size_bytes"]
            and hashlib.sha256(raw).hexdigest() == source["sha256"],
        )
        paths[source["source_id"]] = path

    def data(source_id: str) -> dict | list:
        """Read a saved JSON artifact; never import a preserved Python source."""
        return json.loads(paths[source_id].read_text(encoding="utf-8"))

    settings = data("SRC-0028244")
    saved = data("SRC-0028241")
    finished = data("SRC-0028242")
    started = data("SRC-0028243")
    before = data("SRC-0028240")
    after = data("SRC-0000838")
    for key, sid in [
        ("code_sha256", "SRC-0022906"),
        ("plan_sha256", "SRC-0021872"),
    ]:
        check(key, settings[key] == hashlib.sha256(paths[sid].read_bytes()).hexdigest())
    check(
        "fixed_intercept_MAE_case",
        settings["prediction"] == 0
        and settings["targets"] == [-1, -1, 10]
        and settings["loss"] == "MAE"
        and settings["model"] == "f_theta(x)=theta; identical inputs",
    )
    check(
        "no_recorded_model_calls",
        all(settings[k] == 0 for k in ["TabICL_contexts", "RCTL_fits", "RCTL_forward"])
        and finished["model_calls"] == 0,
    )
    targets = [Fraction(v) for v in settings["targets"]]
    residuals = [Fraction(settings["prediction"]) - y for y in targets]
    check("nonzero_residuals", all(residuals))
    losses = [abs(v) for v in residuals]
    gradients = [Fraction(1 if v > 0 else -1) for v in residuals]
    n = len(targets)
    distributions = {
        "uniform": [Fraction(1, n)] * n,
        "loss_proportional": [loss / sum(losses) for loss in losses],
    }
    calculated = {}
    for method, probabilities in distributions.items():
        weights = [1 / (n * p) for p in probabilities]
        row = saved["rows"][method]
        check(method + ":probability", row["probability"] == list(map(str, probabilities)))
        check(method + ":weight", row["weight"] == list(map(str, weights)))
        calculated[method] = {}
        for metric, values in [("loss", losses), ("gradient", gradients)]:
            outcomes = [weight * value for weight, value in zip(weights, values, strict=True)]
            mean = sum(p * value for p, value in zip(probabilities, outcomes, strict=True))
            second_moment = sum(
                p * value**2 for p, value in zip(probabilities, outcomes, strict=True)
            )
            variance = second_moment - mean**2
            check(
                method + ":" + metric,
                row[metric]["mean_fraction"] == str(mean)
                and row[metric]["variance_fraction"] == str(variance)
                and row[metric]["mean"] == float(mean)
                and row[metric]["variance"] == float(variance),
            )
            calculated[method][metric] = {"mean": str(mean), "variance": str(variance)}
    ratio = Fraction(calculated["loss_proportional"]["gradient"]["variance"]) / Fraction(
        calculated["uniform"]["gradient"]["variance"]
    )
    check(
        "gradient_variance_ratio",
        ratio == Fraction(121, 40)
        and math.isclose(saved["gradient_variance_ratio"], float(ratio), rel_tol=1e-15),
    )
    check(
        "empirical_means",
        saved["empirical_MAE"] == float(sum(losses) / n)
        and saved["empirical_gradient_fraction"] == str(sum(gradients) / n),
    )
    expected_claims = {
        "unbiased_loss_both": True,
        "unbiased_gradient_both": True,
        "loss_variance_zero_proportional": True,
        "gradient_variance_larger_proportional": True,
    }
    check("four_claim_flags", saved["claims"] == expected_claims)
    check("UTC_start", datetime.fromisoformat(started["utc"]).utcoffset().total_seconds() == 0)
    elapsed = saved["numeric_seconds"]
    check(
        "completion_and_arithmetic_timer",
        finished["status"] == "completed"
        and finished["numeric_seconds"] == elapsed
        and 0 < elapsed < settings["numeric_cap_seconds"] == 1,
    )
    key = "mae_sampling_audit_57"
    check("no_prior_57_charge", key not in before["new_cheap_diagnostic_seconds"])
    expected = copy.deepcopy(before)
    expected["new_cheap_diagnostic_seconds"][key] = elapsed
    check("only_one_ledger_delta", after == expected)
    cheap = sum(after["new_cheap_diagnostic_seconds"].values())
    model_seconds = sum(
        after["used"][k]
        for k in [
            "TabICL_fit_predict_seconds",
            "RCTL_wall_seconds",
            "RCTL_frozen_inference_seconds",
        ]
    )
    check(
        "historical_budgets_unchanged",
        before["used"] == after["used"]
        and before["remaining_count_budgets"] == after["remaining_count_budgets"]
        and after["used"]["RCTL_fits"] == 29
        and after["remaining_count_budgets"]["RCTL_fits"] == 0,
    )
    fits = data("SRC-0030237")
    summary = data("SRC-0027517")
    costs = []
    for method, expected_steps in [("global", 1890), ("tabicl_risk", 2431)]:
        rows = [r for r in fits if r["method"] == method and r["seed"] == 20260925]
        steps = sum(r["epochs_run"] * math.ceil(len(r["members"]) * 672 / 256) for r in rows)
        seen = sum(r["epochs_run"] * len(r["members"]) * 672 for r in rows)
        seconds = sum(r["fit_seconds"] for r in rows)
        aggregate = next(
            r for r in summary["aggregates"] if r["method"] == method and r["seed"] == 20260925
        )
        check(
            method + ":derived_steps",
            steps == expected_steps == aggregate["total_original_optimizer_steps"],
        )
        check(method + ":derived_rows", seen == aggregate["total_original_rows_seen"])
        check(method + ":recorded_seconds", seconds == aggregate["total_fit_seconds"])
        costs.append(
            dict(
                method=method,
                calculated_steps=steps,
                calculated_rows=seen,
                recorded_fit_seconds=seconds,
            )
        )
    return dict(
        success=not errors,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks=len(checks),
        check_names=checks,
        errors=errors,
        exact_moments=calculated,
        gradient_variance_ratio=str(ratio),
        cheap_after_seconds=cheap,
        recorded_modeling_after_seconds=cheap + model_seconds,
        historical_fit_cost=costs,
        new_model_runs=0,
        original_scripts_executed=False,
        random_draws=0,
        scope="보존 바이트·세 고정 결과의 정확 산술·원장 차이·과거 epoch 기반 비용만 검수",
    )


def main() -> None:
    """Write a reviewable report and return failure when evidence disagrees."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = verify(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {"success": result["success"], "checks": result["checks"], "errors": result["errors"]}
        )
    )
    raise SystemExit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
