"""Read-only source hashing, archive member inventory, and installed RECORD audit."""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import json
import subprocess
import sys
import tarfile
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path
from zipfile import BadZipFile, ZipFile


def now() -> str:
    return datetime.now(UTC).isoformat()


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".part")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def write_rows(path: Path, rows: list[dict]) -> None:
    temporary = path.with_name(path.name + ".part")
    with temporary.open("w", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    temporary.replace(path)


def load_workspace(workspace: Path) -> tuple[Path, dict, list[dict]]:
    latest = read_json(workspace / "latest-inventory.json")
    inventory = Path(latest["path"])
    root = Path(read_json(inventory / "summary.json")["source_root"])
    return root, latest, read_rows(inventory / "sources.jsonl")


def expand_archives(workspace: Path, tar_executable: str) -> None:
    root, latest, physical_rows = load_workspace(workspace)
    registry = read_json(workspace / "source-registry.json")
    additions: list[dict] = []
    errors: list[dict] = []
    for container in physical_rows:
        if container["kind"] != "physical_file" or container["extension"] not in {".tar", ".7z"}:
            continue
        relative = container["path"]
        path = root / relative
        try:
            if container["extension"] == ".tar":
                with tarfile.open(path, "r:*") as archive:
                    items = [
                        {
                            "path": entry.name,
                            "size_bytes": entry.size,
                            "kind": "tar_member",
                            "member_index": index,
                            "is_regular": entry.isfile(),
                            "link_target": entry.linkname or None,
                            "archive_mtime": entry.mtime,
                        }
                        for index, entry in enumerate(archive.getmembers())
                        if not entry.isdir()
                    ]
            else:
                short = subprocess.run(
                    [tar_executable, "-tf", str(path)],
                    capture_output=True,
                    encoding="utf-8",
                    check=True,
                ).stdout.splitlines()
                verbose = subprocess.run(
                    [tar_executable, "-tvf", str(path)],
                    capture_output=True,
                    encoding="utf-8",
                    check=True,
                ).stdout.splitlines()
                items = []
                for index, line in enumerate(verbose):
                    fields = line.split(maxsplit=8)
                    if len(fields) != 9 or fields[8] != short[index]:
                        raise ValueError("Archive list formats do not agree: " + line)
                    if fields[0].startswith("d"):
                        continue
                    items.append(
                        {
                            "path": fields[8],
                            "size_bytes": int(fields[4]),
                            "kind": "seven_zip_member",
                            "member_index": index,
                            "is_regular": fields[0].startswith("-"),
                            "listing_line": line,
                        }
                    )
                if len(short) != len(verbose):
                    raise ValueError("Archive listing entry counts do not agree")
            for item in items:
                key = f"{item['kind']}:{relative}!{item['member_index']}:{item['path']}"
                if key not in registry["sources"]:
                    registry["sources"][key] = f"SRC-{registry['next_id']:07d}"
                    registry["next_id"] += 1
                item.update(
                    source_id=registry["sources"][key],
                    container_id=container["source_id"],
                    container_path=relative,
                    extension=Path(item["path"]).suffix.lower(),
                    content_review="not_started",
                    disposition="pending_review",
                    hash_status="pending",
                    sha256=None,
                )
                additions.append(item)
        except (OSError, ValueError, tarfile.TarError, subprocess.SubprocessError) as exc:
            errors.append(
                {
                    "source_id": container["source_id"],
                    "path": relative,
                    "error": type(exc).__name__,
                    "message": str(exc),
                }
            )
    write_rows(workspace / "archive-members.jsonl", additions)
    write_json(
        workspace / "archive-members-summary.json",
        {
            "created_at_utc": now(),
            "inventory_version": latest["version"],
            "members": len(additions),
            "kinds": dict(Counter(row["kind"] for row in additions)),
            "errors": errors,
            "content_review_completed": 0,
        },
    )
    write_json(workspace / "source-registry.json", registry)
    print(
        json.dumps({"archive_members_added": len(additions), "errors": errors}, ensure_ascii=False)
    )


def hash_stream(stream) -> tuple[str, int]:
    digest = hashlib.sha256()
    count = 0
    while chunk := stream.read(1024 * 1024):
        digest.update(chunk)
        count += len(chunk)
    return digest.hexdigest(), count


def fingerprint(workspace: Path, tar_executable: str) -> None:
    root, latest, rows = load_workspace(workspace)
    rows.extend(read_rows(workspace / "archive-members.jsonl"))
    cache_path = workspace / "hash-journal.jsonl"
    cache = {row["source_id"]: row for row in read_rows(cache_path)}
    containers = {row["source_id"]: row for row in rows if row["kind"] == "physical_file"}
    processed = reused = 0
    failures: list[dict] = []
    with cache_path.open("a", encoding="utf-8", newline="\n") as journal:
        for row in rows:
            if row["kind"] == "directory_link":
                continue
            version = row if row["kind"] == "physical_file" else containers[row["container_id"]]
            path = root / version["path"]
            key = {"size_bytes": version["size_bytes"], "mtime_ns": version["mtime_ns"]}
            old = cache.get(row["source_id"])
            result = {
                "source_id": row["source_id"],
                "kind": row["kind"],
                "inventory_version": latest["version"],
                "container_version": None,
                "checked_at_utc": now(),
                "status": "pending",
            }
            try:
                if row.get("is_symlink") or not row.get("is_regular", True):
                    raise ValueError(
                        "Link or non-regular file must be reviewed without following it"
                    )
                before = path.lstat()
                actual = {"size_bytes": before.st_size, "mtime_ns": before.st_mtime_ns}
                result["container_version"] = actual
                if actual != key:
                    raise ValueError("Source size or modification time changed since inventory")
                if (
                    old
                    and old.get("status") == "hashed"
                    and old.get("container_version") == actual == key
                ):
                    reused += 1
                    continue
                if row["kind"] == "physical_file":
                    with path.open("rb") as stream:
                        digest, count = hash_stream(stream)
                elif row["kind"] == "zip_member":
                    with ZipFile(path) as archive:
                        entry = archive.infolist()[row["member_index"]]
                        if entry.filename != row["path"]:
                            raise ValueError("ZIP member identity changed")
                        with archive.open(entry) as stream:
                            digest, count = hash_stream(stream)
                elif row["kind"] == "tar_member":
                    with tarfile.open(path, "r:*") as archive:
                        entry = archive.getmembers()[row["member_index"]]
                        if entry.name != row["path"]:
                            raise ValueError("TAR member identity changed")
                        with archive.extractfile(entry) as stream:
                            digest, count = hash_stream(stream)
                elif row["kind"] == "seven_zip_member":
                    with subprocess.Popen(
                        [tar_executable, "-xOf", str(path), row["path"]],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                    ) as process:
                        digest, count = hash_stream(process.stdout)
                        stderr = process.stderr.read()
                        if process.wait() != 0:
                            raise OSError(stderr.decode("utf-8", errors="replace"))
                else:
                    raise ValueError("Unrecognized source kind")
                after = path.lstat()
                if after.st_mtime_ns != before.st_mtime_ns or after.st_size != before.st_size:
                    raise ValueError("Source changed while hashing")
                if count != row["size_bytes"]:
                    raise ValueError("Read length does not match inventory")
                result.update(status="hashed", sha256=digest, bytes_read=count)
            except (OSError, ValueError, RuntimeError, tarfile.TarError, BadZipFile) as exc:
                result.update(status="error", error=type(exc).__name__, message=str(exc))
                failures.append(result)
            journal.write(json.dumps(result, ensure_ascii=False) + "\n")
            journal.flush()
            cache[row["source_id"]] = result
            processed += 1
            if processed % 5000 == 0:
                print(
                    json.dumps(
                        {"newly_processed": processed, "reused": reused, "errors": len(failures)}
                    ),
                    flush=True,
                )
    groups: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        result = cache.get(row["source_id"], {})
        if result.get("status") == "hashed":
            groups[result["sha256"]].append(row["source_id"])
    duplicates = [
        {"sha256": digest, "source_ids": members}
        for digest, members in groups.items()
        if len(members) > 1
    ]
    write_rows(workspace / "exact-duplicates.jsonl", duplicates)
    summary = {
        "finished_at_utc": now(),
        "inventory_version": latest["version"],
        "processed_this_run": processed,
        "reused_this_run": reused,
        "hashed_sources": sum(len(members) for members in groups.values()),
        "unique_sha256": len(groups),
        "duplicate_groups": len(duplicates),
        "exact_duplicate_occurrences_beyond_first": sum(
            len(x["source_ids"]) - 1 for x in duplicates
        ),
        "errors_this_run": failures,
        "content_review_completed": 0,
    }
    write_json(workspace / "hash-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)


def audit_dependencies(workspace: Path) -> None:
    root, latest, rows = load_workspace(workspace)
    hashes = {row["source_id"]: row for row in read_rows(workspace / "hash-journal.jsonl")}
    physical = {row["path"]: row for row in rows if row["kind"] == "physical_file"}
    matches: dict[str, list[dict]] = defaultdict(list)
    absent = []
    for record in rows:
        if record["kind"] != "physical_file" or not record["path"].endswith(".dist-info/RECORD"):
            continue
        record_path = root / record["path"]
        base = record_path.parent.parent
        with record_path.open(encoding="utf-8", newline="") as stream:
            for name, encoded, declared_size in csv.reader(stream):
                target = (base / name).resolve()
                if not target.is_relative_to(root):
                    absent.append(
                        {
                            "record_id": record["source_id"],
                            "path": name,
                            "status": "record_target_outside_source",
                        }
                    )
                    continue
                relative = target.relative_to(root).as_posix()
                item = physical.get(relative)
                if item is None:
                    absent.append(
                        {
                            "record_id": record["source_id"],
                            "path": relative,
                            "status": "record_target_absent_from_inventory",
                        }
                    )
                    continue
                current = hashes.get(item["source_id"], {})
                expected = encoded.split("=", 1)[1] if encoded.startswith("sha256=") else None
                actual = (
                    base64.urlsafe_b64encode(bytes.fromhex(current["sha256"])).rstrip(b"=").decode()
                    if current.get("status") == "hashed"
                    else None
                )
                status = "not_checkable_from_record"
                if expected and actual:
                    status = (
                        "matches_installed_record"
                        if expected == actual
                        else "differs_from_installed_record"
                    )
                    if declared_size and int(declared_size) != item["size_bytes"]:
                        status = "differs_from_installed_record"
                matches[item["source_id"]].append(
                    {
                        "record_id": record["source_id"],
                        "record_path": record["path"],
                        "status": status,
                        "expected_hash": encoded or None,
                        "declared_size": declared_size or None,
                    }
                )
    audit_rows = []
    for row in rows:
        if row["kind"] != "physical_file":
            continue
        if "/runtime/" not in row["path"] and not matches.get(row["source_id"]):
            continue
        claims = matches.get(row["source_id"], [])
        statuses = {claim["status"] for claim in claims}
        status = (
            "differs_from_installed_record"
            if "differs_from_installed_record" in statuses
            else "matches_installed_record"
            if "matches_installed_record" in statuses
            else "no_verifiable_installed_record"
        )
        audit_rows.append(
            {
                "source_id": row["source_id"],
                "path": row["path"],
                "status": status,
                "record_claims": claims,
                "sha256": hashes.get(row["source_id"], {}).get("sha256"),
            }
        )
    write_rows(workspace / "dependency-audit.jsonl", audit_rows)
    summary = {
        "created_at_utc": now(),
        "inventory_version": latest["version"],
        "statuses": dict(Counter(row["status"] for row in audit_rows)),
        "changed": [
            {k: row[k] for k in ["source_id", "path", "sha256"]}
            for row in audit_rows
            if row["status"] == "differs_from_installed_record"
        ],
        "record_targets_not_in_inventory": absent,
        "scope": "Local installed RECORD comparison only, not upstream package authenticity",
    }
    write_json(workspace / "dependency-audit-summary.json", summary)
    print(
        json.dumps(
            {
                "statuses": summary["statuses"],
                "changed": summary["changed"],
                "record_targets_not_in_inventory": len(absent),
                "scope": summary["scope"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["expand-archives", "fingerprint", "audit-dependencies"])
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--tar", default="tar")
    args = parser.parse_args()
    if args.command == "expand-archives":
        expand_archives(args.workspace, args.tar)
    elif args.command == "fingerprint":
        fingerprint(args.workspace, args.tar)
    else:
        audit_dependencies(args.workspace)


if __name__ == "__main__":
    main()
