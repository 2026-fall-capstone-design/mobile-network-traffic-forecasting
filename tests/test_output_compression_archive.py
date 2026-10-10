"""Guard archived-result checking against plausible metadata/metric corruption."""

import hashlib
import importlib.util
import json
import shutil
from pathlib import Path

import pytest

pytest.importorskip("numpy")
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/research/evidence/0072-0075-output-compression/manifest.json"
SPEC = importlib.util.spec_from_file_location(
    "output_compression_audit",
    ROOT / "scripts/research_archive/verify_output_compression_history.py",
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


def copy_evidence(tmp_path):
    folder = tmp_path / "docs/research/evidence/test"
    folder.mkdir(parents=True)
    manifest = json.loads(SOURCE.read_text(encoding="utf-8"))
    for row in manifest["sources"]:
        original = SOURCE.parent / row["archive_path"]
        name = row["source_id"] + ".saved"
        shutil.copyfile(original, folder / name)
        row["archive_path"] = name
    for name in ["selected-source-data.npz", "selected-source-data-provenance.json"]:
        shutil.copyfile(SOURCE.parent / name, folder / name)
    path = folder / "manifest.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    return path, manifest


def test_saved_evidence_passes():
    report = AUDIT.verify(SOURCE)
    assert report["success"]
    assert report["arrays"] == 39
    assert report["metric_groups"] == 32


@pytest.mark.parametrize("mutation", ["metric", "cost"])
def test_semantics_detect_corruption_even_with_updated_file_hash(tmp_path, mutation):
    path, manifest = copy_evidence(tmp_path)
    source_id = "SRC-0029276" if mutation == "metric" else "SRC-0029272"
    row = next(r for r in manifest["sources"] if r["source_id"] == source_id)
    saved = path.parent / row["archive_path"]
    data = json.loads(saved.read_bytes())
    if mutation == "metric":
        data["teacher"]["TabICL"]["daily_MSE"][0] += 0.01
        expected = "teacher TabICL daily_MSE"
    else:
        data["used"]["RCTL_fits"] += 1
        expected = "used delta RCTL_fits"
    raw = json.dumps(data).encode()
    saved.write_bytes(raw)
    row.update(sha256=hashlib.sha256(raw).hexdigest(), size_bytes=len(raw))
    if mutation == "cost":
        # Also update the ledger's checksum link; arithmetic must still catch the extra fit.
        update = next(r for r in manifest["sources"] if r["source_id"] == "SRC-0029274")
        update_file = path.parent / update["archive_path"]
        content = json.loads(update_file.read_bytes())
        content["sha256_after"] = row["sha256"]
        update_raw = json.dumps(content).encode()
        update_file.write_bytes(update_raw)
        update.update(sha256=hashlib.sha256(update_raw).hexdigest(), size_bytes=len(update_raw))
    path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(ValueError, match=expected):
        AUDIT.verify(path)
