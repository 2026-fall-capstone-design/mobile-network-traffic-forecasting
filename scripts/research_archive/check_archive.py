"""Check archive evidence hashes, catalog mappings, and local Markdown file links."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def verify(repository: Path) -> dict:
    repository = repository.resolve()
    archive = repository / "docs/research"
    errors, catalog, digests = [], {}, {}
    with gzip.open(archive / "catalog/inventory.jsonl.gz", "rt", encoding="utf-8") as stream:
        for line in stream:
            record = json.loads(line)
            source_id = record["source_id"]
            if source_id in catalog:
                errors.append(f"Duplicate catalog ID: {source_id}")
            catalog[source_id] = record
    source_paths, source_references = set(), 0
    reference_metadata_checks = 0
    for manifest in sorted((archive / "evidence").glob("*/manifest.json")):
        data = json.loads(manifest.read_text(encoding="utf-8"))
        for source in data["sources"]:
            source_references += 1
            source_paths.add(source["path"])
            original = catalog.get(source["source_id"])
            if not original or any(
                original.get(key) != source.get(key) for key in ["path", "sha256", "size_bytes"]
            ):
                errors.append(f"Catalog mismatch: {manifest.name}: {source['source_id']}")
            preserved = (manifest.parent / source["archive_path"]).resolve()
            if not preserved.is_relative_to(archive):
                errors.append(f"Evidence outside archive: {source['source_id']}")
                continue
            if not preserved.is_file():
                errors.append(f"Missing evidence: {source['source_id']}")
                continue
            if preserved not in digests:
                with preserved.open("rb") as stream:
                    digests[preserved] = hashlib.file_digest(stream, "sha256").hexdigest()
            if (
                digests[preserved] != source["sha256"]
                or preserved.stat().st_size != source["size_bytes"]
            ):
                errors.append(f"Evidence hash/size mismatch: {source['source_id']}")

        # Papers are linked, not republished. Validate their catalog identity without
        # claiming that CI downloaded, hashed, or semantically reviewed a remote paper.
        for field in ["primary_sources", "hash_only_sources"]:
            for source in data.get(field, []):
                reference_metadata_checks += 1
                original = catalog.get(source["source_id"])
                if not original or any(
                    original.get(key) != source.get(key) for key in ["path", "sha256", "size_bytes"]
                ):
                    errors.append(f"Reference catalog mismatch: {source['source_id']}")
                if not source.get("distribution", "").startswith("metadata_"):
                    errors.append(f"Missing reference access scope: {source['source_id']}")
                if field == "primary_sources" and not source.get("read_scope"):
                    errors.append(f"Missing reference read scope: {source['source_id']}")

    # Historical .md.txt files intentionally retain old links and are not navigation pages.
    documents = sorted(archive.rglob("*.md")) + [
        repository / "docs/research-archive-plan.md",
        repository / "docs/research-archive-goal-prompt.md",
        repository / "README.md",
        repository / "CONTRIBUTING.md",
        repository / "docs/progress/README.md",
    ]
    checked_links = 0
    for document in documents:
        text = document.read_text(encoding="utf-8")
        # Ignore code examples. Check file existence, not heading-anchor rendering or remote URLs.
        text = re.sub(r"^```.*?^```\s*$", "", text, flags=re.MULTILINE | re.DOTALL)
        for raw in re.findall(r"\]\(([^)]+)\)", text):
            target = raw.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            checked_links += 1
            path = (document.parent / unquote(parsed.path)).resolve()
            if not path.is_relative_to(repository) or not path.exists():
                errors.append(f"Broken local link: {document.relative_to(repository)} -> {target}")
    return dict(
        success=not errors,
        catalog_entries=len(catalog),
        evidence_source_references=source_references,
        evidence_unique_source_paths=len(source_paths),
        evidence_unique_preserved_files=len(digests),
        external_reference_metadata_checks=reference_metadata_checks,
        markdown_documents=len(documents),
        local_file_links_checked=checked_links,
        errors=errors,
        scope="Evidence byte identity and local file links; not semantic or whole-corpus review",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify(args.repository)
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    if not report["success"]:
        raise SystemExit(1)
