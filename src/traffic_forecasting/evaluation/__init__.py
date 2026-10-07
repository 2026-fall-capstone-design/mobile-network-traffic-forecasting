"""Comparable metrics with an explicit distinction between pooled and macro RMSE."""

import math
from collections import defaultdict
from statistics import fmean

from traffic_forecasting.forecasting import Prediction


def summarize(predictions: list[Prediction]) -> dict[str, float | int]:
    if not predictions:
        raise ValueError("Cannot evaluate an empty prediction set.")
    errors = []
    by_cell = defaultdict(list)
    seen = set()
    for item in predictions:
        key = (item.cell_id, item.origin_time, item.timestamp)
        if key in seen:
            raise ValueError("Duplicate prediction.")
        seen.add(key)
        if not math.isfinite(item.actual) or not math.isfinite(item.predicted):
            raise ValueError("Cannot evaluate NaN or infinite values.")
        error = item.predicted - item.actual
        errors.append(error)
        by_cell[item.cell_id].append(error)
    return {
        "n_points": len(errors),
        "n_cells": len(by_cell),
        "mae": round(fmean(abs(error) for error in errors), 6),
        "rmse": round(math.sqrt(fmean(error**2 for error in errors)), 6),
        "macro_rmse": round(
            fmean(math.sqrt(fmean(error**2 for error in group)) for group in by_cell.values()),
            6,
        ),
    }
