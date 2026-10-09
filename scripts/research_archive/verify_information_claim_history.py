"""Verify four archived finite information cases without models or random sampling."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    """Reject duplicate JSON keys, including duplicated cost-stage names."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> object:
    """Read saved JSON while retaining strict duplicate-key validation."""
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def mutual_information(x: list, y: list, probabilities: list[float]) -> float:
    """Calculate discrete MI directly from joint-to-marginal probability ratios."""
    px, py, pxy = defaultdict(float), defaultdict(float), defaultdict(float)
    for xx, yy, probability in zip(x, y, probabilities, strict=True):
        px[xx] += probability
        py[yy] += probability
        pxy[(xx, yy)] += probability
    return sum(p * math.log2(p / (px[xx] * py[yy])) for (xx, yy), p in pxy.items() if p)


def conditional_information(x: list, y: list, z: list, probabilities: list[float]) -> float:
    """Average the within-group MI over each observed conditioning value."""
    result = 0.0
    for zz in set(z):
        indices = [i for i, value in enumerate(z) if value == zz]
        mass = sum(probabilities[i] for i in indices)
        result += mass * mutual_information(
            [x[i] for i in indices],
            [y[i] for i in indices],
            [probabilities[i] / mass for i in indices],
        )
    return result


def verify(manifest_path: Path) -> dict:
    """Check preserved identities, recompute fixed cases, and reconcile reported costs."""
    manifest_path = manifest_path.resolve()
    manifest = read_json(manifest_path)
    checks = []

    def check(name: str, condition: bool) -> None:
        """Record a successful check or fail with its concrete name."""
        if not condition:
            raise ValueError(name)
        checks.append(name)

    def same(name: str, actual: object, expected: object) -> None:
        """Compare every computed field with a saved scalar or numeric list."""
        if isinstance(actual, list):
            check(name, isinstance(expected, list) and len(actual) == len(expected))
            for index, (left, right) in enumerate(zip(actual, expected, strict=True)):
                same(f"{name}[{index}]", left, right)
        else:
            check(
                name,
                type(expected) in (float, int)
                and math.isfinite(expected)
                and math.isclose(actual, expected, rel_tol=0, abs_tol=1e-12),
            )

    check("batch", manifest["batch_id"] == "history-023")
    all_sources = manifest["sources"] + manifest["primary_sources"] + manifest["hash_only_sources"]
    by_id = {r["source_id"]: r for r in all_sources}
    check("source_ids_unique", len(by_id) == len(all_sources) == 26)
    source_bytes = {}
    for row in manifest["sources"]:
        sid = row["source_id"]
        path = (manifest_path.parent / row["archive_path"]).resolve()
        check(sid + ":archive_boundary", path.is_relative_to(manifest_path.parents[2]))
        raw = path.read_bytes()
        check(
            sid + ":identity",
            len(raw) == row["size_bytes"] and hashlib.sha256(raw).hexdigest() == row["sha256"],
        )
        source_bytes[sid] = raw

    def source_json(sid: str) -> object:
        """Parse already hash-checked source bytes without executing any source code."""
        return json.loads(source_bytes[sid], object_pairs_hook=unique_object)

    saved = source_json("SRC-0027888")
    started = source_json("SRC-0027889")
    check(
        "fixed_atoms_unit_probability",
        saved["atoms"] == [[0, 0], [0, 1], [1, 0], [1, 1]]
        and type(saved["atom_probability"]) in (float, int)
        and saved["atom_probability"] == 0.25
        and saved["unit"] == "bits",
    )
    check("bound_paper_hash", saved["source_pdf_sha256"] == by_id["SRC-0062605"]["sha256"])
    atoms = [tuple(v) for v in saved["atoms"]]
    weights = [saved["atom_probability"]] * 4
    a, b = [v[0] for v in atoms], [v[1] for v in atoms]
    parity = [(aa + bb) % 2 for aa, bb in atoms]

    def mi(x: list, y: list) -> float:
        """Evaluate MI using the four saved equiprobable atoms."""
        return mutual_information(x, y, weights)

    def cmi(x: list, y: list, z: list) -> float:
        """Evaluate conditional MI using the same saved atom weights."""
        return conditional_information(x, y, z, weights)

    def gain(y1: list, y2: list, z1: list, z2: list) -> dict:
        """Reconstruct the global-versus-singleton-cluster information identity."""
        pair = list(zip(y1, y2, strict=True))
        shared = mi(atoms, y1) + mi(atoms, y2)
        clustered = mi(z1, y1) + mi(z2, y2)
        slack = cmi(y1, y2, atoms)
        between = mi(y1, y2)
        joint_difference = mi(z1, y1) + mi(z2, y2) - mi(atoms, pair)
        # Each local group has one target, hence its total correlation is exactly zero.
        reduced = slack - between
        return dict(
            global_sum_information=shared,
            cluster_sum_information=clustered,
            actual_gain=clustered - shared,
            shared_conditional_TC=slack,
            sum_cluster_conditional_TC=0.0,
            between_cluster_TC=between,
            reduced_gain_without_joint_term=reduced,
            joint_predictive_difference=joint_difference,
            full_identity_gain=reduced + joint_difference,
            global_input_information=mi(atoms, atoms),
            global_joint_label_information=mi(atoms, pair),
            global_capacity_budget=2,
            cluster_input_information=[mi(z1, atoms), mi(z2, atoms)],
            cluster_capacity_budgets=[1, 1],
        )

    xor = dict(
        sum_marginal_information=mi(parity, a) + mi(parity, b),
        joint_information=mi(parity, atoms),
        TC_unconditional=mi(a, b),
        TC_conditional_XOR=cmi(a, b, parity),
        input_information=mi(parity, atoms),
    )
    duplicate = gain(a, a, a, a)
    saturated = gain(a, b, a, b)
    mono = dict(before_TC=cmi(a, b, [0] * 4), after_TC=cmi(a, b, parity))
    computed = dict(
        xor_case=xor,
        duplicate_labels_gain=duplicate,
        conditional_TC_monotonicity=mono,
        saturated_independent_labels_gain=saturated,
    )
    for case, fields in computed.items():
        check(case + ":keys", set(fields) == set(saved[case]))
        for field, value in fields.items():
            same(case + ":" + field, value, saved[case][field])
    judgments = {
        "xor_lower_bound_violated": xor["joint_information"] > xor["sum_marginal_information"],
        "xor_upper_bound_holds": xor["sum_marginal_information"]
        <= xor["joint_information"] + xor["TC_unconditional"],
        "xor_exact_identity_holds": xor["sum_marginal_information"]
        == xor["joint_information"] + xor["TC_unconditional"] - xor["TC_conditional_XOR"],
        "conditional_TC_can_increase": mono["after_TC"] > mono["before_TC"],
        "duplicate_labels_full_identity_holds": duplicate["actual_gain"]
        == duplicate["full_identity_gain"],
        "duplicate_labels_reduced_identity_fails": duplicate["actual_gain"]
        != duplicate["reduced_gain_without_joint_term"],
        "active_input_budget_not_predictive_saturation": duplicate["global_input_information"]
        == duplicate["global_capacity_budget"]
        and duplicate["global_joint_label_information"] < duplicate["global_capacity_budget"],
        "saturated_example_reduced_identity_holds": saturated["actual_gain"]
        == saturated["reduced_gain_without_joint_term"]
        == saturated["full_identity_gain"],
    }
    check("judgment_keys", set(judgments) == set(saved["checks"]) and len(judgments) == 8)
    for name, value in judgments.items():
        check(name, value and saved["checks"][name] is True)
    check(
        "historical_model_calls_zero",
        all(
            type(v) is int and v == 0
            for v in [
                saved["TabICL_contexts"],
                saved["RCTL_fits"],
                saved["RCTL_forward_calls"],
                started["model_calls"],
            ]
        ),
    )
    check("reported_numeric_time", 0 < saved["numeric_wall_seconds"] < 5)
    ledger = source_json("SRC-0022700")
    same(
        "ledger_exact_stage_time",
        saved["numeric_wall_seconds"],
        ledger["new_cheap_diagnostic_seconds"]["information_claim_audit_37"],
    )
    downloads = source_json("SRC-0062607")
    published = source_json("SRC-0062610")
    check("download_rows", len(downloads) == 7 and len({r["file"] for r in downloads}) == 7)
    failed = [r for r in downloads if "error" in r]
    check(
        "author_manuscript_404",
        len(failed) == 1
        and failed[0]["file"] == "panel_author_20250815.pdf"
        and failed[0]["error"] == "<HTTPError 404: 'Not Found'>"
        and not {"status", "bytes", "sha256"} & set(failed[0]),
    )
    by_filename = {Path(v["path"]).name: v for v in all_sources}
    for row in downloads + [dict(published, file="panel_published_2026.pdf")]:
        check(row["file"] + ":reported_time", math.isfinite(row["seconds"]) and row["seconds"] >= 0)
        if "error" in row:
            continue
        identity = by_filename[row["file"]]
        check(
            row["file"] + ":download_identity",
            row["status"] == 200
            and row["bytes"] == identity["size_bytes"]
            and row["sha256"] == identity["sha256"],
        )
    download_start = source_json("SRC-0062612")
    check("download_planned_byte_cap", download_start["max_bytes_per_file"] == 10 * 1024 * 1024)
    return dict(
        success=True,
        batch_id="history-023",
        checks=len(checks),
        check_names=checks,
        preserved_source_identities=len(source_bytes),
        computed=computed,
        judgments=judgments,
        original_numeric_seconds_reported=saved["numeric_wall_seconds"],
        download_reported_rows=[
            dict(file=v["file"], seconds=v["seconds"], status=v.get("status", "404"))
            for v in downloads + [dict(published, file="panel_published_2026.pdf")]
        ],
        original_scripts_executed=False,
        new_model_runs=0,
        random_samples_generated=0,
        scope=(
            "Direct probability-ratio MI/conditional MI on the four archived atoms; "
            "reported time reconciliation, not historical runtime measurement. "
            "Primary PDF identities are metadata here; mathematical prose requires "
            "the separately recorded manual primary-source review. Not traffic performance."
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
    print(json.dumps({key: report[key] for key in ["success", "checks", "new_model_runs"]}))
