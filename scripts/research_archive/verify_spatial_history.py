"""Verify archived spatial diagnostic outputs without running historical learners."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

import numpy as np


def verify(source: Path) -> dict:
    """Validate source identities, recorded selection and all stored metric fields."""
    manifest = json.loads(source.read_text(encoding="utf-8-sig"))
    checks, accessed = [], {}
    registry = {row["source_id"]: row for row in manifest["sources"]}

    def exact(name, actual, expected):
        """Reject exact schema, identity or array disagreements."""
        ok = (
            bool(np.array_equal(actual, expected))
            if isinstance(actual, np.ndarray) or isinstance(expected, np.ndarray)
            else actual == expected
        )
        checks.append(dict(check=name, passed=bool(ok)))
        if not ok:
            raise AssertionError(name)

    def numeric(name, actual, expected):
        """Compare finite values with explicit shape and tolerance requirements."""
        a, b = np.asarray(actual), np.asarray(expected)
        exact(
            name,
            a.shape == b.shape
            and bool(np.isfinite(a).all())
            and bool(np.isfinite(b).all())
            and bool(np.allclose(a, b, rtol=1e-12, atol=1e-12)),
            True,
        )

    def access(sid, scope):
        """Verify original bytes before reading a specifically declared field."""
        row = registry[sid]
        path = source.parent / row["archive_path"]
        if sid not in accessed:
            raw = path.read_bytes()
            exact(sid + ":size", len(raw), row["size_bytes"])
            exact(sid + ":sha256", hashlib.sha256(raw).hexdigest(), row["sha256"])
            accessed[sid] = {k: row[k] for k in ["source_id", "path", "sha256", "size_bytes"]}
            accessed[sid]["read_scope"] = []
        accessed[sid]["read_scope"] = sorted(set(accessed[sid]["read_scope"]) | set(scope))
        return path

    def saved_json(sid):
        """Read historical JSON as inert evidence."""
        return json.loads(access(sid, ["JSON:all_keys"]).read_text(encoding="utf-8-sig"))

    def arrays(sid, keys=None):
        """Read numeric NPZ values with pickle disabled and reject nonfinite data."""
        scope = ["NPZ:all_numeric_arrays" if keys is None else "NPZ:" + ",".join(keys)]
        with np.load(access(sid, scope), allow_pickle=False) as data:
            values = {key: data[key] for key in (data.files if keys is None else keys)}
        for key, value in values.items():
            exact(
                sid + ":finite:" + key,
                value.dtype.kind in "bifu" and bool(np.isfinite(value).all()),
                True,
            )
        return values

    new_ids = {
        "SRC-0021026",
        "SRC-0021095",
        "SRC-0023177",
        "SRC-0031959",
        "SRC-0031960",
        "SRC-0031961",
        "SRC-0031962",
    }
    exact(
        "manifest:ids",
        sorted(r["source_id"] for r in manifest["sources"]),
        sorted(new_ids | {"SRC-0021004", "SRC-0032487"}),
    )
    exact(
        "manifest:new_ids",
        sorted(
            r["source_id"]
            for r in manifest["sources"]
            if r["preservation"] == "new_byte_identical_archive"
        ),
        sorted(new_ids),
    )
    for sid in ["SRC-0021026", "SRC-0021095", "SRC-0023177", "SRC-0021004"]:
        access(sid, ["sha256_only; static_text_read_separately"])
    started, finished, summary = (
        saved_json(sid) for sid in ["SRC-0031961", "SRC-0031960", "SRC-0031962"]
    )
    data = arrays("SRC-0031959")
    temporal = arrays("SRC-0032487", ["cell_ids", "times", "Y", "pred"])
    shapes = {
        "pred": (2, 4, 32, 336),
        "y": (32, 336),
        "cell_ids": (32,),
        "query_times": (336,),
        "neighbor_cell_ids": (32, 8),
    }
    exact("NPZ:keys", set(data), set(shapes))
    for key, shape in shapes.items():
        exact("shape:" + key, data[key].shape, shape)
    for key in ["cell_ids", "query_times", "neighbor_cell_ids"]:
        exact("integer:" + key, data[key].dtype.kind in "iu", True)
    ids, times, neighbors = data["cell_ids"], data["query_times"], data["neighbor_cell_ids"]
    exact("ids:unique", len(set(ids)), 32)
    exact("ids:bounds", bool(((ids >= 1) & (ids <= 10000)).all()), True)
    exact("ids:previous_order", ids, temporal["cell_ids"])
    exact("times:query", times, np.arange(672, 1008))
    exact("times:prior", temporal["times"], np.arange(168, 1344))
    exact("prior:Y_shape", temporal["Y"].shape, (32, 1176))
    exact("prior:pred_shape", temporal["pred"].shape, (2, 3, 4, 32, 168))
    exact("target:prior", data["y"], temporal["Y"][:, 504:840])
    exact(
        "own:first_week_matches_previous_expanding",
        data["pred"][:, 0, :, :168],
        temporal["pred"][:, 2, 0],
    )
    variants = ["own", "neighbor_mean", "PCC_neighbor", "all_neighbor_directions"]
    models = ["Ridge", "HGB"]
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    exact("plan:hash", started["plan_sha256"], registry["SRC-0021026"]["sha256"])
    exact("settings:summary_matches_started", summary["settings"], started)
    for key, val in {
        "cell_ids": ids.tolist(),
        "neighbor_cell_ids": neighbors.tolist(),
        "direction_offsets": [list(x) for x in offsets],
        "variants": variants,
        "features": [16, 24, 24, 80],
        "train_rows_per_cell": 504,
        "query_rows_per_cell": 336,
        "seed": 20260925,
        "development_only": True,
        "new_TabICL_contexts": 0,
        "new_RCTL_fits": 0,
    }.items():
        exact("settings:" + key, started[key], val)
    for key in ["padded_directions", "train_PCC"]:
        exact("settings:shape:" + key, np.asarray(started[key], dtype=object).shape, (32, 8))
    exact("settings:choice_shape", np.asarray(started["chosen_PCC_direction_index"]).shape, (32,))
    expected_neighbors, expected_padding, choices, ties = [], [], [], []
    for j, cid in enumerate(ids):
        row, col = divmod(int(cid) - 1, 100)
        n, pad, corr = [], [], []
        for k, (dr, dc) in enumerate(offsets):
            valid = 0 <= row + dr < 100 and 0 <= col + dc < 100
            n.append(100 * (row + dr) + col + dc + 1 if valid else int(cid))
            pad.append(not valid)
            value = started["train_PCC"][j][k]
            if valid:
                exact(
                    f"PCC:finite_range:{cid}:{k}",
                    value is not None and np.isfinite(value) and -1 <= value <= 1,
                    True,
                )
                corr.append(value)
            else:
                exact(f"PCC:padding_null:{cid}:{k}", value, None)
                corr.append(float("-inf"))
        selected = int(np.argmax(corr))
        exact("PCC:first_max:" + str(cid), started["chosen_PCC_direction_index"][j], selected)
        tied = np.flatnonzero(np.array(corr) == max(corr)).tolist()
        if len(tied) > 1:
            ties.append(dict(cell_id=int(cid), direction_indices=tied, selected=selected))
        choices.append(selected)
        expected_neighbors.append(n)
        expected_padding.append(pad)
    exact("neighbors:grid_and_padding", neighbors, expected_neighbors)
    exact("padding:matches", started["padded_directions"], expected_padding)
    exact("summary:model_names", list(summary["models"]), models)
    for key, value in {
        "small_regression_fits": 256,
        "new_TabICL_contexts": 0,
        "new_RCTL_fits": 0,
        "physical_spatial_causality_established": False,
        "clustering_improvement_established": False,
    }.items():
        exact("summary:" + key, summary[key], value)
    exact("finished:fits", finished["fits_completed"], 256)
    exact("cost:elapsed", summary["elapsed_seconds"], finished["wall_seconds"])
    exact("cost:fit_predict", summary["fit_predict_seconds"], finished["fit_predict_seconds"])
    exact(
        "cost:reported_cap",
        0 < summary["fit_predict_seconds"] <= summary["elapsed_seconds"] <= 60
        and 0 < summary["peak_RSS_bytes"] <= 2 * 1024**3,
        True,
    )
    (date_ref,) = manifest["derived_inputs"]
    raw = (source.parent / date_ref["archive_path"]).read_bytes()
    exact("dates:sha", hashlib.sha256(raw).hexdigest(), date_ref["sha256"])
    exact("dates:size", len(raw), date_ref["size_bytes"])
    dates = json.loads(raw)["dates"]
    dt = [datetime.fromisoformat(t) for t in dates[:1008]]
    exact("dates:length", len(dt), 1008)
    exact("dates:start", dt[0], datetime(2013, 11, 1))
    exact(
        "dates:hourly",
        all((b - a).total_seconds() == 3600 for a, b in zip(dt, dt[1:], strict=False)),
        True,
    )
    day_labels = [dt[t].date().isoformat() for t in range(672, 1008, 24)]
    loss = np.abs(data["pred"] - data["y"][None, None])
    results = {}

    def contrast(delta):
        """Retain complete cell/day differences and separate their denominators."""
        cells = delta.mean(-1)
        weeks = delta.reshape(32, 2, 168).mean(-1)
        cell_days = delta.reshape(32, 14, 24).mean(-1)
        days = cell_days.mean(0)
        worst = np.unravel_index(int(np.argmax(cell_days)), cell_days.shape)
        best = np.unravel_index(int(np.argmin(cell_days)), cell_days.shape)
        return dict(
            mean=float(delta.mean()),
            cell_deltas=cells.tolist(),
            cell_week_deltas=weeks.tolist(),
            cell_day_deltas=cell_days.tolist(),
            day_deltas=days.tolist(),
            better_cells=int((cells < 0).sum()),
            tied_cells=int((cells == 0).sum()),
            worse_cells=int((cells > 0).sum()),
            worse_cell_weeks=int((weeks > 0).sum()),
            worse_days=int((days > 0).sum()),
            worst_cell_day=dict(
                cell_id=int(ids[worst[0]]), date=day_labels[worst[1]], delta=float(cell_days[worst])
            ),
            best_cell_day=dict(
                cell_id=int(ids[best[0]]), date=day_labels[best[1]], delta=float(cell_days[best])
            ),
        )

    for mi, model in enumerate(models):
        by = loss[mi].mean(-1)
        computed = dict(
            MAE=dict(zip(variants, by.mean(1).tolist(), strict=True)),
            MAE_original16=dict(zip(variants, by[:, :16].mean(1).tolist(), strict=True)),
            MAE_additional16=dict(zip(variants, by[:, 16:].mean(1).tolist(), strict=True)),
            MAE_by_cell=dict(zip(variants, by.tolist(), strict=True)),
            MAE_by_week={
                n: loss[mi, vi].reshape(32, 2, 168).mean((0, 2)).tolist()
                for vi, n in enumerate(variants)
            },
            delta_vs_own_by_cell={n: (by[vi] - by[0]).tolist() for vi, n in enumerate(variants)},
            cells_improved_vs_own={n: int((by[vi] < by[0]).sum()) for vi, n in enumerate(variants)},
            all_minus_mean_by_cell=(by[3] - by[1]).tolist(),
            all_minus_PCC_by_cell=(by[3] - by[2]).tolist(),
        )
        saved = summary["models"][model]
        exact(model + ":field_keys", set(saved), set(computed))
        for key, value in computed.items():
            if isinstance(value, dict):
                exact(model + ":keys:" + key, set(saved[key]), set(value))
                for n, v in value.items():
                    numeric(model + ":" + key + ":" + n, v, saved[key][n])
            else:
                numeric(model + ":" + key, value, saved[key])
        computed["archive_added_contrasts"] = {
            variants[vi] + "_minus_own": contrast(loss[mi, vi] - loss[mi, 0]) for vi in [1, 2, 3]
        }
        for vi in [1, 2]:
            computed["archive_added_contrasts"]["all_minus_" + variants[vi]] = contrast(
                loss[mi, 3] - loss[mi, vi]
            )
        results[model] = computed
    return dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks_passed=len(checks),
        checks=checks,
        accessed_sources=list(accessed.values()),
        results=results,
        cell_ids=ids.tolist(),
        day_labels=day_labels,
        query_periods=[dict(first=dates[o], last=dates[o + 167], hours=168) for o in [672, 840]],
        PCC_exact_ties=ties,
        chosen_PCC_directions=choices,
        boundary_cells=[
            dict(cell_id=int(ids[j]), padded_direction_indices=[k for k, v in enumerate(row) if v])
            for j, row in enumerate(expected_padding)
            if any(row)
        ],
        reported_costs={
            k: summary[k]
            for k in [
                "small_regression_fits",
                "elapsed_seconds",
                "fit_predict_seconds",
                "peak_RSS_bytes",
            ]
        },
        models_run=0,
        random_draws=0,
        historical_code_imported=False,
        feature_verification_limit=(
            "Expanded spatial X is not stored. This portable check verifies recorded neighbor "
            "selection and targets; the separate local H5 audit checks correlations and "
            "reconstructs the recipe, not actual historical model inputs."
        ),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes((json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode())
    print(
        json.dumps(
            {
                "success": result["success"],
                "checks_passed": result["checks_passed"],
                "models_run": 0,
            }
        )
    )
