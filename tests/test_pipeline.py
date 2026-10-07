from dataclasses import replace
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

from traffic_forecasting.data import Observation, load_hourly, parse_time
from traffic_forecasting.evaluation import summarize
from traffic_forecasting.export import read_json, run_demo, write_json
from traffic_forecasting.export.validation import validate_export
from traffic_forecasting.forecasting import Prediction, lag_forecast

ROOT = Path(__file__).resolve().parents[1]
START = datetime(2026, 1, 1, tzinfo=UTC)


@pytest.mark.parametrize("tail", ["", "nan", "inf", "-1"])
def test_invalid_value_is_not_replaced_with_zero(tmp_path, tail):
    path = tmp_path / "input.csv"
    path.write_text(f"cell_id,timestamp,value\nA,2026-01-01T00:00:00Z,{tail}\n")
    with pytest.raises(ValueError):
        load_hourly(path)


@pytest.mark.parametrize("second_hour", [0, 2])
def test_duplicate_or_missing_hours_are_rejected(tmp_path, second_hour):
    path = tmp_path / "input.csv"
    path.write_text(
        f"cell_id,timestamp,value\nA,2026-01-01T00:00:00Z,0\nA,2026-01-01T0{second_hour}:00:00Z,1\n"
    )
    with pytest.raises(ValueError, match="Duplicate or missing"):
        load_hourly(path)


def test_zero_is_valid_and_naive_time_is_not(tmp_path):
    path = tmp_path / "input.csv"
    path.write_text("cell_id,timestamp,value\nA,2026-01-01T00:00:00Z,0\n")
    assert load_hourly(path)[0].value == 0
    with pytest.raises(ValueError, match="timezone"):
        parse_time("2026-01-01T00:00:00")


def test_split_boundary_and_future_values_cannot_change_earlier_forecasts():
    observations = [Observation("A", START + timedelta(hours=i), float(i)) for i in range(48)]
    boundary = START + timedelta(hours=24)
    predictions = lag_forecast(observations, boundary, 24)
    assert len(predictions) == 24
    assert predictions[0].timestamp == boundary
    assert predictions[0].origin_time == boundary - timedelta(hours=1)
    assert [item.predicted for item in predictions] == list(range(24))
    changed = observations[:47] + [replace(observations[-1], value=99999)]
    assert [item.predicted for item in lag_forecast(changed, boundary, 24)] == [
        item.predicted for item in predictions
    ]


def test_insufficient_context_is_not_silently_dropped():
    with pytest.raises(ValueError, match="Insufficient"):
        lag_forecast([Observation("A", START, 1)], START, 24)


def test_pooled_and_macro_rmse_have_distinct_definitions():
    predictions = [
        Prediction("A", START, START + timedelta(hours=1), 0, 0),
        Prediction("A", START + timedelta(hours=1), START + timedelta(hours=2), 0, 0),
        Prediction("B", START, START + timedelta(hours=1), 0, 3),
    ]
    metrics = summarize(predictions)
    assert metrics == {"n_points": 3, "n_cells": 2, "mae": 1, "rmse": 1.732051, "macro_rmse": 1.5}


def test_demo_export_is_valid_and_numeric_results_are_reproducible(tmp_path):
    left, right = tmp_path / "left", tmp_path / "right"
    run_demo(ROOT / "configs/demo.yaml", left)
    run_demo(ROOT / "configs/demo.yaml", right)
    validate_export(left, ROOT / "schemas")
    for file in left.rglob("*.json"):
        if file.name != "manifest.json":
            assert read_json(file) == read_json(right / file.relative_to(left))


@pytest.mark.parametrize("mutation", ["metric", "identity", "future_origin", "traversal", "sample"])
def test_export_validation_rejects_inconsistent_data(tmp_path, mutation):
    run_demo(ROOT / "configs/demo.yaml", tmp_path)
    manifest = read_json(tmp_path / "manifest.json")
    run = manifest["runs"][0]
    if mutation == "metric":
        path = tmp_path / run["metrics_path"]
        metrics = read_json(path)
        metrics["rows"][0]["rmse"] = 999
        write_json(path, metrics)
    elif mutation == "traversal":
        run["models"][0]["series"][0]["path"] = "../outside.json"
        write_json(tmp_path / "manifest.json", manifest)
    else:
        path = tmp_path / run["models"][1]["series"][0]["path"]
        series = read_json(path)
        if mutation == "identity":
            series["cell_id"] = "wrong-cell"
        elif mutation == "future_origin":
            series["points"][0]["origin_time"] = series["points"][0]["timestamp"]
        else:
            series["points"][0]["actual"] += 1
        write_json(path, series)
    with pytest.raises(ValueError):
        validate_export(tmp_path, ROOT / "schemas")
