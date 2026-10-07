"""Validate both JSON structure and scientific consistency of the exported results."""

import math
from datetime import timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

from jsonschema import Draft202012Validator, FormatChecker

from traffic_forecasting.data import parse_time
from traffic_forecasting.evaluation import summarize
from traffic_forecasting.export import read_json
from traffic_forecasting.forecasting import Prediction


def safe_file(directory: Path, relative: str) -> Path:
    if not relative or "\\" in relative or urlsplit(relative).scheme:
        raise ValueError(f"Expected a relative file reference: {relative!r}.")
    candidate = directory / relative
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError(f"File reference escapes export directory: {relative!r}.")
    if not candidate.resolve().is_relative_to(directory.resolve()) or not candidate.is_file():
        raise ValueError(f"Missing or unsafe file reference: {relative!r}.")
    return candidate


def validate_export(directory: Path, schemas: Path) -> None:
    validators = {
        name: Draft202012Validator(
            read_json(schemas / f"{name}.schema.json"), format_checker=FormatChecker()
        )
        for name in ("manifest", "metrics", "predictions")
    }

    def load(relative: str, name: str) -> dict:
        value = read_json(safe_file(directory, relative))
        validators[name].validate(value)
        return value

    manifest = load("manifest.json", "manifest")
    run_ids = set()
    for run in manifest["runs"]:
        if run["id"] in run_ids:
            raise ValueError("Duplicate run ID.")
        run_ids.add(run["id"])
        start, end = parse_time(run["test_start"]), parse_time(run["test_end"])
        if end < start:
            raise ValueError("Invalid test interval.")
        metrics = load(run["metrics_path"], "metrics")
        if metrics["run_id"] != run["id"]:
            raise ValueError("Metrics run ID does not match manifest.")
        metric_rows = {row["model_id"]: row for row in metrics["rows"]}
        model_ids = [model["id"] for model in run["models"]]
        if (
            len(set(model_ids)) != len(model_ids)
            or len(metric_rows) != len(metrics["rows"])
            or set(metric_rows) != set(model_ids)
        ):
            raise ValueError("Metrics and model IDs must be unique and match.")
        reference = None
        for model in run["models"]:
            predictions = []
            actuals = {}
            cell_ids = set()
            for series in model["series"]:
                if series["cell_id"] in cell_ids:
                    raise ValueError("Duplicate cell ID for a model.")
                cell_ids.add(series["cell_id"])
                payload = load(series["path"], "predictions")
                if (payload["run_id"], payload["model_id"], payload["cell_id"]) != (
                    run["id"],
                    model["id"],
                    series["cell_id"],
                ):
                    raise ValueError("Prediction identity does not match manifest.")
                previous = None
                for point in payload["points"]:
                    origin = parse_time(point["origin_time"])
                    target = parse_time(point["timestamp"])
                    if target - origin != timedelta(hours=1):
                        raise ValueError("Expected a one-hour forecast horizon.")
                    if not start <= target <= end:
                        raise ValueError("Prediction is outside the test interval.")
                    if previous is not None and target - previous != timedelta(hours=1):
                        raise ValueError("Predictions must be unique, ordered, and hourly.")
                    previous = target
                    key = (series["cell_id"], origin, target)
                    actuals[key] = point["actual"]
                    predictions.append(
                        Prediction(
                            series["cell_id"], origin, target, point["actual"], point["predicted"]
                        )
                    )
                if parse_time(payload["points"][0]["timestamp"]) != start or previous != end:
                    raise ValueError("Each cell must cover the complete declared test interval.")
            if reference is not None and actuals != reference:
                raise ValueError("Models must use identical evaluation samples and actuals.")
            reference = actuals
            expected = summarize(predictions)
            for name, value in expected.items():
                observed = metric_rows[model["id"]][name]
                if not math.isclose(value, observed, rel_tol=0, abs_tol=1e-6):
                    raise ValueError(f"Metric {name} does not match the prediction files.")


class AssetReferences(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if value and (
                (tag == "script" and name == "src") or (tag == "link" and name == "href")
            ):
                self.references.append(value)


def validate_site(site: Path) -> None:
    parser = AssetReferences()
    parser.feed((site / "index.html").read_text(encoding="utf-8"))
    for reference in parser.references:
        parts = urlsplit(reference)
        if parts.scheme or parts.netloc:
            continue
        safe_file(site, parts.path)
