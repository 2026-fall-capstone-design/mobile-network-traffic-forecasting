"""Apply conservative inventory scope rules; never infer content review from them."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path

from catalog import load_workspace, now, read_rows, write_json, write_rows

RUNTIME = "tmp/redesign_20260925/runtime/"


def classify(workspace: Path):
    _, latest, rows = load_workspace(workspace)
    rows.extend(read_rows(workspace / "archive-members.jsonl"))
    hashes = {r["source_id"]: r for r in read_rows(workspace / "hash-journal.jsonl")}
    audit = {r["source_id"]: r for r in read_rows(workspace / "dependency-audit.jsonl")}
    output = []
    for row in rows:
        path = row["path"]
        category = "research_candidate"
        decision = "include_pending_review"
        reason = "Unique research content has not yet been reviewed."
        if row["kind"] == "directory_link":
            category, decision = "external_directory_link", "exclude_external_runtime_link"
            reason = "Shared node_modules target outside source root; location registered only."
        elif "/tabicl/" in path and "/runtime/" in path and path.endswith(".py"):
            category = "dependency_source_reference"
            reason = "TabICL implementation referenced by research; retain despite RECORD match."
        elif path.startswith(RUNTIME):
            if path.endswith(".pyc"):
                category, decision = "runtime_bytecode", "exclude_generated_runtime_cache"
                reason = "Compiled cache in installed runtime; source audit retained separately."
            elif (
                ".dist-info/" in path
                or path.removeprefix(RUNTIME)
                in {
                    "pyvenv.cfg",
                    ".gitignore",
                    ".lock",
                    "CACHEDIR.TAG",
                    "Lib/site-packages/_virtualenv.py",
                    "Lib/site-packages/_virtualenv.pth",
                }
                or "/Scripts/" in path
            ):
                category = "environment_metadata"
                reason = "Retain installation metadata and launch configuration for provenance."
            elif audit.get(row["source_id"], {}).get("status") == "matches_installed_record":
                category, decision = "installed_dependency", "exclude_installed_dependency"
                reason = "SHA-256 and size agree with local installed RECORD; no upstream claim."
            else:
                category = "unresolved_runtime_content"
                reason = "No verifiable installed RECORD; manual disposition required."
        elif row["kind"] != "physical_file":
            category = "archive_member_candidate"
            reason = "Archive member bytes hashed; content review remains pending."
        result = {
            "source_id": row["source_id"],
            "kind": row["kind"],
            "path": path,
            "container_id": row.get("container_id"),
            "sha256": hashes.get(row["source_id"], {}).get("sha256"),
            "category": category,
            "disposition": decision,
            "reason": reason,
            "content_review": "not_started",
        }
        output.append(result)
    groups = defaultdict(list)
    for row in output:
        if row["disposition"] == "include_pending_review" and row["sha256"]:
            groups[row["sha256"]].append(row)
    for members in groups.values():
        members.sort(
            key=lambda r: (
                r["kind"] != "physical_file",
                not r["path"].startswith("tmp/redesign_20260925/"),
                r["path"].count("/"),
                r["path"],
            )
        )
        representative = members[0]["source_id"]
        for row in members:
            row["representative_source_id"] = representative
            if row["source_id"] != representative:
                row["disposition"] = "exact_duplicate_pending_representative_review"
                row["reason"] = "Identical SHA-256; representative content is not yet reviewed."
    write_rows(workspace / "scope.jsonl", output)
    summary = {
        "created_at_utc": now(),
        "inventory_version": latest["version"],
        "metadata_entries": len(output),
        "categories": dict(Counter(r["category"] for r in output)),
        "dispositions": dict(Counter(r["disposition"] for r in output)),
        "included_unique_file_contents": len(groups),
        "unique_research_records": None,
        "scope_rules": "scripts/research_archive/classify.py",
        "note": "File content identities are not research records; review remains separate.",
    }
    write_json(workspace / "scope-summary.json", summary)
    return summary


if __name__ == "__main__":
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True)
    print(json.dumps(classify(parser.parse_args().workspace), ensure_ascii=False, indent=2))
