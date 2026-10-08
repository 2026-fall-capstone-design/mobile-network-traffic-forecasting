"""Inventory research sources without executing or changing their contents.

This pass records metadata and ZIP member names. It deliberately does not claim
that sources have been read, that duplicate contents are known, or that a
third-party-looking path has already been excluded from the archive.
"""

from __future__ import annotations

import argparse
import json
import os
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from zipfile import BadZipFile, ZipFile


def write_json(path: Path, value: object) -> None:
    temporary = path.with_name(path.name + ".part")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def role_hint(path: str) -> str:
    parts = {part.lower() for part in Path(path).parts}
    suffix = Path(path).suffix.lower()
    if "__pycache__" in parts or suffix in {".pyc", ".pyo"}:
        return "generated_cache_candidate"
    if parts & {"site-packages", "dist-packages", ".venv", "node_modules"}:
        return "dependency_candidate"
    if suffix in {".md", ".txt", ".docx", ".pdf", ".pptx", ".hwp", ".hwpx"}:
        return "document_candidate"
    if suffix in {".py", ".ps1", ".sh", ".ipynb", ".js", ".mjs"}:
        return "code_candidate"
    if suffix in {".json", ".jsonl", ".csv", ".tsv", ".npy", ".npz", ".log"}:
        return "evidence_candidate"
    if suffix in {".zip", ".tar", ".gz", ".7z", ".xz", ".bz2"}:
        return "archive_candidate"
    return "unclassified"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = args.source.resolve(strict=True)
    output = args.output.resolve()
    if output == source or source in output.parents:
        raise SystemExit("The inventory output must be outside the source tree.")
    output.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC)
    version = timestamp.strftime("%Y%m%dT%H%M%S%fZ")
    version_dir = output / "inventories" / version
    version_dir.mkdir(parents=True, exist_ok=False)

    registry_path = output / "source-registry.json"
    registry = (
        json.loads(registry_path.read_text(encoding="utf-8"))
        if registry_path.exists()
        else {"source_root": str(source), "next_id": 1, "sources": {}}
    )
    if registry["source_root"] != str(source):
        raise SystemExit("The existing source registry belongs to a different root.")

    def source_id(key: str) -> str:
        if key not in registry["sources"]:
            registry["sources"][key] = f"SRC-{registry['next_id']:07d}"
            registry["next_id"] += 1
        return registry["sources"][key]

    errors: list[dict[str, object]] = []
    rows: list[dict[str, object]] = []
    archives: list[tuple[Path, str]] = []

    def record_error(path: str, operation: str, exc: Exception) -> None:
        errors.append(
            {"path": path, "operation": operation, "error": type(exc).__name__, "message": str(exc)}
        )

    def walk_error(exc: OSError) -> None:
        record_error(str(exc.filename), "enumerate_directory", exc)

    for directory, dirs, files in os.walk(source, followlinks=False, onerror=walk_error):
        dirs.sort()
        files.sort()
        for name in dirs[:]:
            path = Path(directory) / name
            if path.is_symlink() or path.is_junction():
                relative = path.relative_to(source).as_posix()
                try:
                    target = os.readlink(path)
                except OSError as exc:
                    record_error(relative, "read_directory_link", exc)
                    target = None
                rows.append(
                    {
                        "source_id": source_id("directory_link:" + relative),
                        "path": relative,
                        "kind": "directory_link",
                        "link_type": "junction" if path.is_junction() else "symlink",
                        "target": target,
                        "content_review": "not_started",
                        "disposition": "pending_review",
                        "note": "Directory link registered; target not traversed.",
                    }
                )
                dirs.remove(name)
        for name in files:
            path = Path(directory) / name
            relative = path.relative_to(source).as_posix()
            row: dict[str, object] = {
                "source_id": source_id("file:" + relative),
                "path": relative,
                "kind": "physical_file",
                "extension": path.suffix.lower(),
                "role_hint": role_hint(relative),
                "disposition": "pending_review",
                "content_review": "not_started",
                "hash_status": "pending",
                "sha256": None,
                "is_symlink": path.is_symlink(),
            }
            try:
                stat = path.lstat()
                row.update(size_bytes=stat.st_size, mtime_ns=stat.st_mtime_ns)
            except OSError as exc:
                record_error(relative, "stat", exc)
                row["metadata_error"] = type(exc).__name__
            rows.append(row)
            if path.suffix.lower() == ".zip" and not row["is_symlink"]:
                archives.append((path, str(row["source_id"])))

    zip_summaries: list[dict[str, object]] = []
    for path, container_id in archives:
        relative = path.relative_to(source).as_posix()
        try:
            with ZipFile(path) as archive:
                entries = archive.infolist()
                member_count = 0
                for index, member in enumerate(entries):
                    if member.is_dir():
                        continue
                    member_count += 1
                    key = f"zip:{relative}!{index}:{member.filename}"
                    rows.append(
                        {
                            "source_id": source_id(key),
                            "kind": "zip_member",
                            "container_id": container_id,
                            "container_path": relative,
                            "member_index": index,
                            "path": member.filename,
                            "extension": Path(member.filename).suffix.lower(),
                            "size_bytes": member.file_size,
                            "compressed_bytes": member.compress_size,
                            "zip_crc32": member.CRC,
                            "zip_datetime": list(member.date_time),
                            "encrypted": bool(member.flag_bits & 1),
                            "nested_archive": Path(member.filename).suffix.lower() == ".zip",
                            "role_hint": role_hint(member.filename),
                            "disposition": "pending_review",
                            "content_review": "not_started",
                            "hash_status": "pending",
                            "sha256": None,
                        }
                    )
                zip_summaries.append(
                    {
                        "container_id": container_id,
                        "path": relative,
                        "file_members": member_count,
                        "directory_entries": len(entries) - member_count,
                    }
                )
        except (OSError, BadZipFile, NotImplementedError, RuntimeError) as exc:
            record_error(relative, "list_zip_members", exc)

    ids = [str(row["source_id"]) for row in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate source IDs detected; inventory was not finalized.")

    metadata_path = version_dir / "sources.jsonl"
    temporary = metadata_path.with_name(metadata_path.name + ".part")
    with temporary.open("w", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    temporary.replace(metadata_path)
    physical = [row for row in rows if row["kind"] == "physical_file"]
    members = [row for row in rows if row["kind"] == "zip_member"]
    summary = {
        "schema_version": 1,
        "version": version,
        "started_at_utc": timestamp.isoformat(),
        "finished_at_utc": datetime.now(UTC).isoformat(),
        "source_root": str(source),
        "pass": "metadata_and_zip_central_directory_only",
        "total_rows": len(rows),
        "physical_files": len(physical),
        "physical_bytes": sum(int(row.get("size_bytes", 0)) for row in physical),
        "zip_containers_listed": len(zip_summaries),
        "zip_file_members": len(members),
        "nested_zip_members_pending": sum(bool(row["nested_archive"]) for row in members),
        "directory_links_not_traversed": sum(row["kind"] == "directory_link" for row in rows),
        "extensions_physical": dict(Counter(str(row["extension"]) for row in physical)),
        "role_hints_physical": dict(Counter(str(row["role_hint"]) for row in physical)),
        "top_level_physical": dict(Counter(str(row["path"]).split("/")[0] for row in physical)),
        "errors": len(errors),
        "sha256_completed": 0,
        "content_review_completed": 0,
        "disposition_finalized": 0,
        "next_required": [
            "review_dependency_candidates",
            "hash_research_sources",
            "inspect_other_and_nested_archives",
            "read_unique_research_contents",
        ],
    }
    write_json(version_dir / "summary.json", summary)
    write_json(version_dir / "errors.json", errors)
    write_json(version_dir / "zip-containers.json", zip_summaries)
    write_json(registry_path, registry)
    write_json(output / "latest-inventory.json", {"version": version, "path": str(version_dir)})
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
