"""Regenerate the committed synthetic hourly fixture; no external dataset is used."""

import csv
import math
import random
from datetime import UTC, datetime, timedelta
from pathlib import Path

rng = random.Random(17)
destination = Path(__file__).resolve().parents[1] / "data/sample/traffic.csv"
destination.parent.mkdir(parents=True, exist_ok=True)
with destination.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(["cell_id", "timestamp", "value"])
    for index, cell_id in enumerate(("1001", "1002", "1003")):
        for hour in range(96):
            timestamp = datetime(2026, 1, 1, tzinfo=UTC) + timedelta(hours=hour)
            daily = math.sin((hour % 24 - 7 - index) * math.tau / 24)
            value = round(70 + index * 35 + 30 * daily + hour * 0.08 + rng.uniform(-5, 5), 2)
            writer.writerow([cell_id, timestamp.isoformat().replace("+00:00", "Z"), value])
print(f"Wrote {destination}")
