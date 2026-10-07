"""Export versioned results that can be served without a Python backend."""

import hashlib
import json
import platform
import re
import subprocess
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

import yaml

from traffic_forecasting.data import iso_time, load_hourly, parse_time
from traffic_forecasting.evaluation import summarize
from traffic_forecasting.forecasting import lag_forecast

MODELS = (("last-value", "직전 값", 1), ("seasonal-24h", "24시간 전 값", 24))


def read_json(path: Path) -> dict:
    def invalid_constant(value: str) -> None:
        raise ValueError(f"Invalid JSON number: {value}")

    return json.loads(path.read_text(encoding="utf-8"), parse_constant=invalid_constant)


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )


def fingerprint(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_state() -> dict:
    def git(*args: str) -> str | None:
        try:
            return subprocess.check_output(
                ["git", *args], text=True, stderr=subprocess.DEVNULL
            ).strip()
        except (OSError, subprocess.CalledProcessError):
            return None

    status = git("status", "--porcelain")
    return {
        "commit": git("rev-parse", "HEAD"),
        "dirty": status != "" if status is not None else None,
        "python": platform.python_version(),
    }


def run_demo(config_path: Path, output: Path | None = None) -> Path:
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    project = config_path.resolve().parent.parent
    run_id = config["run_id"]
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", run_id):
        raise ValueError("run_id must be a safe identifier.")
    input_path = project / config["input"]
    destination = output if output is not None else project / config["output"]
    observations = load_hourly(input_path)
    test_start = parse_time(config["test_start"])
    metrics = []
    models = []
    for model_id, label, lag in MODELS:
        predictions = lag_forecast(observations, test_start, lag)
        metrics.append({"model_id": model_id, **summarize(predictions)})
        groups = defaultdict(list)
        for item in predictions:
            if not re.fullmatch(r"[a-zA-Z0-9_-]+", item.cell_id):
                raise ValueError("cell_id must be a safe identifier for static files.")
            groups[item.cell_id].append(
                {
                    "origin_time": iso_time(item.origin_time),
                    "timestamp": iso_time(item.timestamp),
                    "actual": item.actual,
                    "predicted": item.predicted,
                }
            )
        series = []
        for cell_id, points in sorted(groups.items()):
            relative = f"predictions/{run_id}/{model_id}/{cell_id}.json"
            write_json(
                destination / relative,
                {
                    "schema_version": "1.0",
                    "run_id": run_id,
                    "model_id": model_id,
                    "cell_id": cell_id,
                    "points": points,
                },
            )
            series.append({"cell_id": cell_id, "path": relative})
        models.append({"id": model_id, "label": label, "series": series})
    metrics_path = f"metrics/{run_id}.json"
    write_json(
        destination / metrics_path,
        {"schema_version": "1.0", "run_id": run_id, "rows": metrics},
    )
    write_json(
        destination / "manifest.json",
        {
            "schema_version": "1.0",
            "dataset": {
                "id": config["dataset_id"],
                "kind": "synthetic",
                "unit": config["unit"],
                "timezone": config["timezone"],
                "description": "구성 확인용 합성 데이터입니다. 실제 연구 성능을 나타내지 않습니다.",
            },
            "runs": [
                {
                    "id": run_id,
                    "label": config["label"],
                    "test_start": iso_time(test_start),
                    "test_end": iso_time(max(item.timestamp for item in observations)),
                    "generated_at": iso_time(datetime.now(UTC)),
                    "provenance": {
                        **source_state(),
                        "data_sha256": fingerprint(input_path),
                        "config_sha256": fingerprint(config_path),
                    },
                    "metrics_path": metrics_path,
                    "models": models,
                }
            ],
        },
    )
    return destination
