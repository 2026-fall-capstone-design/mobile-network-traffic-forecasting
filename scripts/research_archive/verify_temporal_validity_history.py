"""Verify saved 16/17 diagnostics without running historical models or random draws."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

import numpy as np


def verify(source: Path) -> dict:
    """Check archived inputs, all reported aggregates and derived adverse cases."""
    manifest = json.loads(source.read_text(encoding="utf-8-sig"))
    checks, accessed = [], {}
    registry = {row["source_id"]: row for row in manifest["sources"]}

    def exact(name, actual, expected):
        """Compare identities or exact arrays and reject mismatches explicitly."""
        ok = (
            bool(np.array_equal(actual, expected))
            if isinstance(actual, np.ndarray) or isinstance(expected, np.ndarray)
            else actual == expected
        )
        checks.append(dict(check=name, passed=bool(ok)))
        if not ok:
            raise AssertionError(name)

    def numeric(name, actual, expected):
        """Compare float64 calculations with shape and finite-value requirements."""
        a, b = np.asarray(actual), np.asarray(expected)
        ok = a.shape == b.shape and bool(np.allclose(a, b, rtol=1e-12, atol=1e-12))
        exact(name, ok, True)

    def access(sid, scope):
        """Check archived bytes and record the fields actually accessed."""
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
        """Read saved JSON as data only."""
        return json.loads(access(sid, ["JSON:all_keys"]).read_text(encoding="utf-8-sig"))

    def arrays(sid, keys=None):
        """Read numeric arrays with pickle disabled and check finite values."""
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

    expected_new = {
        "SRC-0020991",
        "SRC-0021004",
        "SRC-0023201",
        "SRC-0032487",
        "SRC-0032488",
        "SRC-0032489",
        "SRC-0032490",
        "SRC-0032491",
    }
    exact(
        "manifest:all_ids",
        sorted(r["source_id"] for r in manifest["sources"]),
        sorted(expected_new | {"SRC-0020972", "SRC-0023589"}),
    )
    exact(
        "manifest:new_ids",
        sorted(
            r["source_id"]
            for r in manifest["sources"]
            if r["preservation"] == "new_byte_identical_archive"
        ),
        sorted(expected_new),
    )
    for sid in ["SRC-0020991", "SRC-0021004", "SRC-0023201", "SRC-0020972"]:
        access(sid, ["sha256_only; original_text_reviewed_separately"])
    started, finished, summary = (
        saved_json(sid) for sid in ["SRC-0032490", "SRC-0032489", "SRC-0032491"]
    )
    data, partial = arrays("SRC-0032487"), arrays("SRC-0032488")
    prior = arrays("SRC-0023589", ["cell_ids"])
    exact(
        "final:keys",
        set(data),
        {"pred", "y", "naive", "cell_ids", "origins", "scales", "X", "Y", "times"},
    )
    exact("partial:keys", set(partial), {"pred", "y", "naive"})
    for key, value in partial.items():
        exact("partial:matches_final:" + key, value, data[key])
    shapes = {
        "pred": (2, 3, 4, 32, 168),
        "y": (4, 32, 168),
        "naive": (3, 4, 32, 168),
        "cell_ids": (32,),
        "origins": (4,),
        "scales": (32,),
        "X": (32, 1176, 16),
        "Y": (32, 1176),
        "times": (1176,),
    }
    for key, shape in shapes.items():
        exact("shape:" + key, data[key].shape, shape)
    ids, origins, times = data["cell_ids"], data["origins"], data["times"]
    for key in ["cell_ids", "origins", "times"]:
        exact("integer:" + key, data[key].dtype.kind in "iu", True)
    exact("cell_ids:unique", len(set(ids)), 32)
    exact("cell_ids:bounds", bool(((ids >= 1) & (ids <= 10000)).all()), True)
    exact("origins", origins, [672, 840, 1008, 1176])
    exact("times", times, np.arange(168, 1344))
    exact("scales:positive", bool((data["scales"] > 0).all()), True)
    exact("plan_hash", started["plan_sha256"], registry["SRC-0020991"]["sha256"])
    exact("settings_match", summary["settings"], started)
    exact("settings:ids", started["cell_ids"], ids.tolist())
    exact("settings:retained", started["retained_prior_ids"], prior["cell_ids"].tolist())
    exact("settings:retained_order", ids[:16], prior["cell_ids"])
    exact("settings:added", started["added_cell_ids"], ids[16:].tolist())
    exact(
        "settings:quartiles",
        started["added_activity_quartiles"],
        np.repeat(np.arange(4), 4).tolist(),
    )
    policies = ["old", "recent", "expanding"]
    models = ["Ridge", "HGB"]
    for key, value in {
        "origins": origins.tolist(),
        "query_hours_per_origin": 168,
        "normalization": "Fixed first 672h mean per cell",
        "model_names": models,
        "policies": policies,
        "seed": 20260925,
        "planned_small_regression_fits": 768,
        "new_TabICL_contexts": 0,
        "new_RCTL_fits": 0,
    }.items():
        exact("settings:" + key, started[key], value)
    exact("summary:models", list(summary["models"]), models)
    for key, value in {
        "small_regression_fits": 768,
        "new_TabICL_contexts": 0,
        "new_RCTL_fits": 0,
        "is_final_validation": False,
        "actual_conditional_drift_established": False,
    }.items():
        exact("summary:" + key, summary[key], value)
    exact("finished:fits", finished["fits_completed"], 768)
    exact("reported:elapsed", summary["elapsed_seconds"], finished["wall_seconds"])
    exact("reported:fit_predict", summary["fit_predict_seconds"], finished["fit_predict_seconds"])
    exact(
        "reported:cost_bounds",
        0 < summary["fit_predict_seconds"] <= summary["elapsed_seconds"] <= 120
        and 0 < summary["peak_RSS_bytes"] <= 2 * 1024**3,
        True,
    )
    exact("query:target_mapping", data["y"], np.stack([data["Y"][:, o - 168 : o] for o in origins]))
    for k, lag in enumerate([1, 24, 168]):
        exact(
            "naive:mapping:" + str(lag),
            data["naive"][k],
            np.stack([data["Y"][:, o - lag - 168 : o - lag] for o in origins]),
        )
    # Later feature rows can also be checked from saved Y without accessing the H5.
    idx = np.arange(168, 1176)
    for col, lag in enumerate([8, 7, 6, 5, 4, 3, 2, 1, 24, 168]):
        exact("X:lag_column:" + str(col), data["X"][:, idx, col], data["Y"][:, idx - lag])
    means = np.stack([data["Y"][:, i - 24 : i].mean(axis=1) for i in idx], axis=1)
    stds = np.stack([data["Y"][:, i - 24 : i].std(axis=1) for i in idx], axis=1)
    numeric("X:mean24_later_rows", data["X"][:, idx, 10], means)
    numeric("X:std24_later_rows", data["X"][:, idx, 11], stds)
    (date_ref,) = manifest["derived_inputs"]
    date_raw = (source.parent / date_ref["archive_path"]).read_bytes()
    exact("dates:hash", hashlib.sha256(date_raw).hexdigest(), date_ref["sha256"])
    exact("dates:size", len(date_raw), date_ref["size_bytes"])
    dates = json.loads(date_raw)["dates"]
    dt = [datetime.fromisoformat(t) for t in dates[:1344]]
    exact("dates:first", dt[0], datetime(2013, 11, 1))
    exact(
        "dates:hourly",
        len(dt) == 1344
        and all((b - a).total_seconds() == 3600 for a, b in zip(dt, dt[1:], strict=False)),
        True,
    )
    hour = np.array([dt[t].hour for t in times])
    weekday = np.array([dt[t].weekday() for t in times])
    calendar = np.column_stack(
        [
            np.sin(2 * np.pi * hour / 24),
            np.cos(2 * np.pi * hour / 24),
            np.sin(2 * np.pi * weekday / 7),
            np.cos(2 * np.pi * weekday / 7),
        ]
    )
    numeric("X:calendar_all", data["X"][:, :, 12:], np.broadcast_to(calendar, (32, 1176, 4)))
    loss = np.abs(data["pred"] - data["y"][None, None])
    day_labels = [dt[t].date().isoformat() for t in range(672, 1344, 24)]
    result = {}

    def contrast(delta, labels):
        """Retain every cell/day delta and counts of both benefit and harm."""
        cell = delta.mean(axis=(0, 2))
        cell_week = delta.mean(axis=2)
        cell_day = (
            delta.reshape(len(labels) // 7, 32, 7, 24)
            .mean(axis=3)
            .transpose(0, 2, 1)
            .reshape(len(labels), 32)
        )
        day = cell_day.mean(axis=1)
        worst = np.unravel_index(int(np.argmax(cell_day)), cell_day.shape)
        best = np.unravel_index(int(np.argmin(cell_day)), cell_day.shape)
        return dict(
            mean=float(delta.mean()),
            cell_deltas=cell.tolist(),
            day_deltas=day.tolist(),
            cell_day_deltas=cell_day.tolist(),
            better_cells=int((cell < 0).sum()),
            worse_cells=int((cell > 0).sum()),
            tied_cells=int((cell == 0).sum()),
            better_cell_weeks=int((cell_week < 0).sum()),
            worse_cell_weeks=int((cell_week > 0).sum()),
            better_days=int((day < 0).sum()),
            worse_days=int((day > 0).sum()),
            better_cell_days=int((cell_day < 0).sum()),
            worse_cell_days=int((cell_day > 0).sum()),
            worst_cell_day=dict(
                cell_id=int(ids[worst[1]]), date=labels[worst[0]], delta=float(cell_day[worst])
            ),
            best_cell_day=dict(
                cell_id=int(ids[best[1]]), date=labels[best[0]], delta=float(cell_day[best])
            ),
        )

    expected_keys = {
        "all_MAE",
        "MAE_by_week",
        "MAE_by_cell",
        "MAE_by_cell_week",
        "recent_minus_old",
        "recent_minus_expanding",
        "fixed_first_week_policy",
        "original16_MAE",
        "added16_MAE",
    }
    for m, name in enumerate(models):
        entry = summary["models"][name]
        exact(name + ":summary_keys", set(entry), expected_keys)
        by = loss[m].mean(axis=-1)
        day = loss[m].reshape(3, 4, 32, 7, 24).mean(axis=4).transpose(0, 1, 3, 2).reshape(3, 28, 32)
        for p, policy in enumerate(policies):
            for key, value in {
                "all_MAE": by[p].mean(),
                "MAE_by_week": by[p].mean(axis=1),
                "MAE_by_cell": by[p].mean(axis=0),
                "MAE_by_cell_week": by[p],
                "original16_MAE": by[p, :, :16].mean(),
                "added16_MAE": by[p, :, 16:].mean(),
            }.items():
                numeric(name + ":" + policy + ":" + key, value, entry[key][policy])
            numeric(
                name + ":" + policy + ":daily_aggregation", day[p].mean(axis=0), by[p].mean(axis=0)
            )
        for label, p in [("recent_minus_old", 0), ("recent_minus_expanding", 2)]:
            difference = by[1] - by[p]
            numeric(name + ":" + label + ":mean", difference.mean(), entry[label]["mean"])
            numeric(
                name + ":" + label + ":negative_fraction",
                (difference < 0).mean(),
                entry[label]["cell_week_fraction_negative"],
            )
            numeric(
                name + ":" + label + ":quantiles",
                np.quantile(difference.mean(axis=0), [0, 0.25, 0.5, 0.75, 1]),
                entry[label]["cell_mean_delta_quantiles"],
            )
        choice = np.where(by[1, 0] < by[2, 0], 1, 2)
        selected_loss = np.stack([loss[m, choice, w, np.arange(32)] for w in range(1, 4)])
        selection = entry["fixed_first_week_policy"]
        exact(name + ":selection_choices", selection["cell_choices"], [policies[p] for p in choice])
        exact(
            name + ":selection_count", selection["recent_selected_count"], int((choice == 1).sum())
        )
        numeric(name + ":selection_MAE", selected_loss.mean(), selection["later3weeks_MAE"])
        numeric(
            name + ":selection_recent_MAE",
            loss[m, 1, 1:].mean(),
            selection["later3weeks_recent_MAE"],
        )
        numeric(
            name + ":selection_expanding_MAE",
            loss[m, 2, 1:].mean(),
            selection["later3weeks_expanding_MAE"],
        )
        result[name] = dict(
            all_MAE=by.mean(axis=(1, 2)).tolist(),
            by_week=by.mean(axis=2).tolist(),
            by_cell=by.mean(axis=1).tolist(),
            by_cell_week=by.tolist(),
            by_cell_day=day.tolist(),
            original16=by[:, :, :16].mean(axis=(1, 2)).tolist(),
            added16=by[:, :, 16:].mean(axis=(1, 2)).tolist(),
            fixed_first_week=dict(
                recent_count=int((choice == 1).sum()),
                exact_ties=int((by[1, 0] == by[2, 0]).sum()),
                choices=[policies[p] for p in choice],
                MAE=float(selected_loss.mean()),
                recent_MAE=float(loss[m, 1, 1:].mean()),
                expanding_MAE=float(loss[m, 2, 1:].mean()),
            ),
            contrasts={
                "recent_minus_old": contrast(loss[m, 1] - loss[m, 0], day_labels),
                "recent_minus_expanding": contrast(loss[m, 1] - loss[m, 2], day_labels),
                "expanding_minus_old": contrast(loss[m, 2] - loss[m, 0], day_labels),
                "fixed_policy_minus_expanding_last3weeks": contrast(
                    selected_loss - loss[m, 2, 1:], day_labels[7:]
                ),
            },
        )
    naive = {}
    for k, lag in enumerate([1, 24, 168]):
        value = float(np.abs(data["naive"][k] - data["y"]).mean())
        numeric("naive:MAE:" + str(lag), value, summary["naive_MAE"][str(lag)])
        naive[str(lag)] = value
    return dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks_passed=len(checks),
        checks=checks,
        sources=list(accessed.values()),
        cell_ids=ids.tolist(),
        policies=policies,
        day_labels=day_labels,
        results=result,
        naive_MAE=naive,
        reported_costs={
            k: summary[k]
            for k in [
                "elapsed_seconds",
                "fit_predict_seconds",
                "peak_RSS_bytes",
                "small_regression_fits",
            ]
        },
        query_periods=[
            dict(
                origin=int(o),
                first=dates[o],
                last=dates[o + 167],
                train_rows=[336, 336, int(o - 168)],
            )
            for o in origins
        ],
        evidence_kind="stored_numeric_consistency_and_derived_diagnostics_not_model_reproduction",
        scope=(
            "All saved summary metrics and nine numeric arrays; selected H5 audit is separate. "
            "No historical code imports, learner fitting, inference, random draws, "
            "or conditional-drift proof."
        ),
        models_run=0,
        random_draws=0,
        record17_literature_verified=False,
    )


def main() -> None:
    """Run the bounded saved-value verifier and optionally store its full report."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).resolve().parents[2]
        / "docs/research/evidence/0016-0017/manifest.json",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify(args.manifest)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(
            (json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        )
    print(
        json.dumps(
            {
                k: result[k]
                for k in ["success", "checks_passed", "models_run", "random_draws", "scope"]
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
