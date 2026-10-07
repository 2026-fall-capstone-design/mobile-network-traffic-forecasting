"""Hourly observations with explicit time and missing-data checks."""

import csv
import math
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path


@dataclass(frozen=True)
class Observation:
    cell_id: str
    timestamp: datetime
    value: float


def parse_time(value: str) -> datetime:
    timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if timestamp.tzinfo is None:
        raise ValueError("Timestamp must include a timezone.")
    return timestamp.astimezone(UTC)


def iso_time(value: datetime) -> str:
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


def load_hourly(path: Path) -> list[Observation]:
    observations = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["cell_id", "timestamp", "value"]:
            raise ValueError("Expected CSV columns: cell_id,timestamp,value.")
        for row in reader:
            cell_id = row["cell_id"].strip()
            if not cell_id or not row["value"].strip():
                raise ValueError("Cell ID and value are required; missing values are not zero.")
            timestamp = parse_time(row["timestamp"])
            value = float(row["value"])
            if not math.isfinite(value) or value < 0:
                raise ValueError("Traffic values must be finite and non-negative.")
            if timestamp.minute or timestamp.second or timestamp.microsecond:
                raise ValueError("Hourly observations must be aligned to the hour.")
            observations.append(Observation(cell_id, timestamp, value))
    if not observations:
        raise ValueError("Input contains no observations.")
    observations.sort(key=lambda item: (item.cell_id, item.timestamp))
    groups = defaultdict(list)
    for item in observations:
        groups[item.cell_id].append(item)
    for cell_id, rows in groups.items():
        for previous, current in zip(rows, rows[1:], strict=False):
            if current.timestamp - previous.timestamp != timedelta(hours=1):
                raise ValueError(f"Duplicate or missing hourly observation for {cell_id}.")
    return observations
