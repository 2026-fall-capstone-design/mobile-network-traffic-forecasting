"""Simple reference forecasts; research models can produce the same Prediction records."""

from dataclasses import dataclass
from datetime import datetime, timedelta

from traffic_forecasting.data import Observation


@dataclass(frozen=True)
class Prediction:
    cell_id: str
    origin_time: datetime
    timestamp: datetime
    actual: float
    predicted: float


def lag_forecast(
    observations: list[Observation], test_start: datetime, lag_hours: int
) -> list[Prediction]:
    if lag_hours < 1:
        raise ValueError("A forecast must use a positive lag.")
    lookup = {(item.cell_id, item.timestamp): item.value for item in observations}
    if len(lookup) != len(observations):
        raise ValueError("Duplicate cell/timestamp observations.")
    predictions = []
    for item in observations:
        if item.timestamp < test_start:
            continue
        key = (item.cell_id, item.timestamp - timedelta(hours=lag_hours))
        if key not in lookup:
            raise ValueError(f"Insufficient historical context for {item.cell_id}.")
        predictions.append(
            Prediction(
                cell_id=item.cell_id,
                origin_time=item.timestamp - timedelta(hours=1),
                timestamp=item.timestamp,
                actual=item.value,
                predicted=lookup[key],
            )
        )
    if not predictions:
        raise ValueError("Test interval contains no observations.")
    return predictions
