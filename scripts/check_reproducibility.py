"""Detect stale or edited demo results without comparing execution-specific metadata."""

from pathlib import Path
from tempfile import TemporaryDirectory

from traffic_forecasting.export import read_json, run_demo

root = Path(__file__).resolve().parents[1]
with TemporaryDirectory() as temporary:
    output = Path(temporary)
    run_demo(root / "configs/demo.yaml", output)
    for path in output.rglob("*.json"):
        expected = read_json(path)
        committed = read_json(root / "web/data" / path.relative_to(output))
        if path.name == "manifest.json":
            for manifest in (expected, committed):
                for run in manifest["runs"]:
                    run.pop("generated_at")
                    for key in ("commit", "dirty", "python"):
                        run["provenance"].pop(key)
        if expected != committed:
            raise SystemExit(f"Stale demo result: {path.relative_to(output)}. Run the demo again.")
print("Committed demo predictions and metrics are reproducible.")
