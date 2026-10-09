"""Check archived sample-reuse equations and the pinned-code cost correction."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    """Reject ambiguous duplicate fields in original or derived evidence."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> object:
    """Read JSON without running archived Python or importing a model."""
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def absolute_uniform_mean(center: Fraction, halfwidth: Fraction) -> Fraction:
    """Integrate absolute error exactly using its piecewise antiderivative."""
    low, high = center - halfwidth, center + halfwidth
    return (high * abs(high) - low * abs(low)) / (4 * halfwidth)


def verify(manifest_path: Path) -> dict:
    """Recompute fixed mathematical examples and reconcile their evidence scopes."""
    base = manifest_path.resolve().parent
    manifest = read_json(manifest_path)
    checks = []

    def check(name: str, condition: bool) -> None:
        """Fail at the first named mismatch and retain successful checks."""
        if not condition:
            raise ValueError(name)
        checks.append(name)

    def numeric(name: str, value: object, expected: float) -> None:
        """Reject Boolean and nonfinite values before numerical comparison."""
        check(
            name,
            type(value) in (int, float)
            and math.isfinite(value)
            and math.isclose(value, expected, rel_tol=1e-13, abs_tol=1e-14),
        )

    check("batch", manifest["batch_id"] == "history-024")
    all_rows = manifest["sources"] + manifest["primary_sources"] + manifest["hash_only_sources"]
    by_id = {v["source_id"]: v for v in all_rows}
    check("17_distinct_source_identities", len(all_rows) == len(by_id) == 17)
    check(
        "5_preserved_8_primary_4_identity_only",
        tuple(len(manifest[k]) for k in ["sources", "primary_sources", "hash_only_sources"])
        == (5, 8, 4),
    )
    raw_sources = {}
    for row in manifest["sources"]:
        sid = row["source_id"]
        path = (base / row["archive_path"]).resolve()
        check(sid + ":boundary", path.is_relative_to(base))
        raw = path.read_bytes()
        check(
            sid + ":identity",
            len(raw) == row["size_bytes"] and hashlib.sha256(raw).hexdigest() == row["sha256"],
        )
        raw_sources[sid] = raw
    for row in manifest["primary_sources"]:
        check(
            row["source_id"] + ":bounded_primary",
            bool(row["read_scope"])
            and not row["read_scope"].get("whole_paper_read", False)
            and not row["read_scope"].get("whole_text", False),
        )
    tables = read_json(base / "document-tables.json")
    check(
        "table_source",
        tables["source_id"] == "SRC-0021511"
        and tables["source_sha256"] == by_id["SRC-0021511"]["sha256"],
    )
    note = raw_sources["SRC-0021511"].decode("utf-8")
    for token in ["0.145", "0.525", "1.8", "0.2", "68G", "exp(-a²/2)"]:
        check("original_report:" + token, token in note)
    case = tables["uniform_example"]
    p, donor, share, width = [
        Fraction(case[k])
        for k in ["target_x1", "donor_x1", "target_mixture_share", "noise_halfwidth"]
    ]
    check(
        "fixed_original_integral_inputs",
        (p, donor, share, width)
        == (Fraction(1, 10), Fraction(9, 10), Fraction(1, 2), Fraction(1, 10)),
    )
    numeric("constant_prediction", case["prediction"], 0)
    numeric("equal_conditionals_ratio", case["conditional_ratio"], 1)
    q = share * p + (1 - share) * donor
    conditional = [absolute_uniform_mean(Fraction(x), width) for x in [0, 1]]
    check(
        "exact_conditional_integrals",
        conditional == [Fraction(v) for v in case["conditional_absolute_errors"]],
    )
    target = (1 - p) * conditional[0] + p * conditional[1]
    mixture = (1 - q) * conditional[0] + q * conditional[1]
    weights = [(1 - p) / (1 - q), p / q]
    weighted = (1 - q) * weights[0] * conditional[0] + q * weights[1] * conditional[1]
    for key, value in [
        ("target_mae", target),
        ("mixture_mae", mixture),
        ("joint_weighted_mae", weighted),
    ]:
        check(key, value == Fraction(case[key]))
    check("joint_weights", weights == [Fraction(v) for v in case["joint_weights"]])
    check("target_recovered_mixture_differs", target == weighted and target != mixture)
    check("weights_integrate_to_one", (1 - q) * weights[0] + q * weights[1] == 1)

    gaussian = tables["gaussian_example"]
    check(
        "fixed_gaussian_formula",
        gaussian["unit_variance"] is True
        and gaussian["means"] == "-a,+a"
        and gaussian["geometric_mass_formula"] == "exp(-a*a/2)",
    )
    check(
        "gaussian_table_shape", gaussian["a_values"] == [0, 1, 2] and len(gaussian["masses"]) == 3
    )
    check("gaussian_a_integer_values", all(type(a) is int for a in gaussian["a_values"]))
    masses = []
    for a, saved in zip(gaussian["a_values"], gaussian["masses"], strict=True):
        # Completing the square gives sqrt(phi(x+a)phi(x-a))=exp(-a²/2)phi(x).
        # Checking fixed evaluation points is arithmetic, not random sampling.
        mass = math.exp(-(a * a) / 2)
        numeric(f"gaussian_mass:a={a}", saved, mass)
        masses.append(mass)
        for x in [-2, 0, 2]:
            log_geometric = -((x + a) ** 2 + (x - a) ** 2) / 4 - math.log(2 * math.pi) / 2
            log_completed = -(x * x) / 2 - (a * a) / 2 - math.log(2 * math.pi) / 2
            numeric(f"gaussian_square:a={a},x={x}", log_geometric, log_completed)
    check("normalization_not_universal", masses[0] == 1 and masses[1] < 1 and masses[2] < masses[1])

    code = read_json(base.parents[1] / "verification/history-024-code-check.json")
    check(
        "static_code_proof_scope",
        code["success"] is True
        and code["mode"] == "static_ast_and_manual_induction_no_original_execution"
        and code["new_model_runs"] == 0,
    )
    check(
        "code_binding_ids",
        set(code["source_sha256"]) == {"SRC-0047550", "SRC-0047582", "SRC-0047572"},
    )
    check(
        "static_latin_configuration",
        code["default_method"] == "latin"
        and type(code["dimensions"]) is int
        and code["dimensions"] == 17
        and type(code["requested_orders"]) is int
        and code["requested_orders"] == 4,
    )
    for sid, sha in code["source_sha256"].items():
        check(sid + ":code_metadata_binding", by_id[sid]["sha256"] == sha)
    cost = tables["cost_correction"]
    for key, value in [
        ("dimensions", 17),
        ("requested_orders", 4),
        ("actual_latin_orders", 17),
        ("reported_column_visits", 17 * 4),
        ("corrected_column_visits", 17 * 17),
    ]:
        numeric(key, cost[key], value)
    numeric("static_actual_order_count", code["actual_order_count"], cost["actual_latin_orders"])
    numeric(
        "static_max_column_visits", code["maximum_column_visits"], cost["corrected_column_visits"]
    )
    check(
        "cost_not_measured_runtime",
        cost["measured_runtime"] is False
        and cost["units"] == "maximum conditional-loop visits per group",
    )

    downloads = json.loads(raw_sources["SRC-0063937"], object_pairs_hook=unique_object)
    check(
        "five_successful_archived_downloads",
        len(downloads) == 5
        and all(row["status"] == "saved" and row["http_status"] == 200 for row in downloads),
    )
    name_index = {Path(row["path"]).name: row for row in all_rows}
    for row in downloads:
        identity = name_index[row["name"]]
        check(
            row["name"] + ":download_identity",
            row["bytes"] == identity["size_bytes"] and row["sha256"] == identity["sha256"],
        )
        if row["name"].endswith(".pdf"):
            check(row["name"] + ":pages", row["pages"] == identity["read_scope"]["pdf_pages"])
    pdfs = [row for row in downloads if row["name"].endswith(".pdf")]
    computed_downloads = dict(
        pdf_count=len(pdfs),
        pdf_pages=sum(row["pages"] for row in pdfs),
        pdf_bytes=sum(row["bytes"] for row in pdfs),
        http200_saved_rows=len(downloads),
        wall_seconds=None,
    )
    check("download_table", computed_downloads == tables["downloads"])
    started = json.loads(raw_sources["SRC-0063938"], object_pairs_hook=unique_object)
    numeric("historical_model_calls", started["model_calls"], 0)
    numeric("table_historical_calls", tables["historical_model_calls"], 0)
    return dict(
        success=True,
        checks=len(checks),
        check_names=checks,
        computed=dict(
            conditional_absolute_errors=[str(v) for v in conditional],
            target_mae=str(target),
            mixture_mae=str(mixture),
            joint_weights=[str(v) for v in weights],
            joint_weighted_mae=str(weighted),
            gaussian_masses=masses,
            reported_column_visits=68,
            corrected_maximum_column_visits=289,
        ),
        downloads=computed_downloads,
        new_model_runs=0,
        original_scripts_executed=False,
        scope=(
            "Exact deterministic equations and preserved metadata; code semantics from bounded "
            "local static review, no online code retrieval or paper-proof validation in CI."
        ),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify(args.manifest)
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
