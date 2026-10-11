"""Recount DGCformer v1 Table 1 display values without running a model."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from decimal import Decimal
from pathlib import Path


def summarize(data: dict) -> dict:
    """Compare the published decimal strings and HTML bold markers."""
    models = data["models"]
    rows = data["rows"]
    keys = {(r["dataset"], r["horizon"], r["metric"]) for r in rows}
    if len(models) != 7 or len(rows) != 64 or len(keys) != 64:
        raise ValueError("Expected seven models and 64 distinct comparisons")
    counts = {name: Counter(dict.fromkeys(models, 0)) for name in ("ties", "strict", "bold")}
    nonminimum, bold_nonminimum, minimum_not_bold = [], [], []
    for row in rows:
        if set(row["values"]) != set(models) or not set(row["bold_models"]) <= set(models):
            raise ValueError("Inconsistent model columns")
        values = {m: Decimal(row["values"][m]) for m in models}
        minimum = min(values.values())
        winners = [m for m in models if values[m] == minimum]
        base = {k: row[k] for k in ("dataset", "horizon", "metric")}
        for model in models:
            wins = model in winners
            bold = model in row["bold_models"]
            counts["ties"][model] += int(wins)
            counts["strict"][model] += int(wins and len(winners) == 1)
            counts["bold"][model] += int(bold)
            point = dict(
                **base,
                model=model,
                value=str(values[model]),
                minimum=str(minimum),
                minimum_models=winners,
            )
            if model == "DGCformer" and not wins:
                nonminimum.append(point)
            if bold and not wins:
                bold_nonminimum.append(point)
            if wins and not bold:
                minimum_not_bold.append(point)
    return dict(
        source_id=data["source_id"],
        source_sha256=data["source_sha256"],
        scope="인쇄된 소수와 HTML 굵기만 비교한다. 원시 결과나 모델 재현이 아니다.",
        cases=len(rows),
        reported_counts=data["reported_counts"],
        top1_including_ties=dict(counts["ties"]),
        strict_top1=dict(counts["strict"]),
        HTML_bold_counts=dict(counts["bold"]),
        DGCformer_nonminimum=nonminimum,
        bold_but_not_display_minimum=bold_nonminimum,
        minimum_not_bold=minimum_not_bold,
        new_model_runs=0,
    )


def main() -> None:
    """Recompute the stored audit, or compare it with the archived report."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    evidence = root / "docs/research/evidence/0091-dgcformer"
    data = json.loads((evidence / "displayed-table-1.json").read_text(encoding="utf-8"))
    result = summarize(data)
    if args.check:
        expected = json.loads((evidence / "table-1-audit.json").read_text(encoding="utf-8"))
        if result != expected:
            raise ValueError("Recalculated display audit differs from the stored report")
        print("DGCformer Table 1: 64 display comparisons match the stored audit")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
