"""08·09의 저장 진단을 검산한다. 원 실험 코드·새 난수·모델은 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import numpy as np


def verify(source: Path) -> dict:
    """Check stored design diagnostics and aggregate identities without rerunning the toy."""
    manifest = json.loads(source.read_text(encoding="utf-8")) if source.is_file() else None
    mapping = {r["path"]: r for r in manifest["sources"]} if manifest else {}
    base = "tmp/redesign_20260925/"
    accessed, max_by_check = {}, {}
    checks = Counter()

    def check(name, condition):
        """Count a named assertion and identify the failing occurrence."""
        checks[name] += 1
        if not condition:
            raise AssertionError((name, checks[name]))

    def close(name, actual, expected):
        """Compare shape and finite absolute error using a 1e-10 tolerance."""
        a, b = np.asarray(actual), np.asarray(expected)
        check(name + "_shape", a.shape == b.shape)
        diff = float(np.max(np.abs(a.astype(float) - b.astype(float))))
        max_by_check[name] = max(max_by_check.get(name, 0), diff)
        check(name, np.isfinite(diff) and diff <= 1e-10)

    def path(key, scope):
        """Resolve a file, verify portable bytes, and record only its actual access scope."""
        key = base + key
        p = source.parent / mapping[key]["archive_path"] if manifest else source / key
        if key not in accessed:
            raw = p.read_bytes()
            accessed[key] = dict(
                path=key,
                sha256=hashlib.sha256(raw).hexdigest(),
                size_bytes=len(raw),
                read_scope=[],
            )
            if manifest:
                check(
                    "portable_source_identity",
                    accessed[key]["sha256"] == mapping[key]["sha256"]
                    and len(raw) == mapping[key]["size_bytes"],
                )
        accessed[key]["read_scope"] = sorted(set(accessed[key]["read_scope"]) | set(scope))
        return p

    def arrays(key, names):
        """Read only named arrays, explicitly disallowing pickle deserialization."""
        with np.load(path(key, ["array:" + k for k in names]), allow_pickle=False) as z:
            return {k: z[k].copy() for k in names}

    saved = json.loads(
        path(
            "results/finite_sample_information.json",
            [
                "json:plan_sha256",
                "json:synthetic_contract_and_aggregate_identities",
                "json:synthetic_MC_means_and_SE_reported_not_recomputed",
                "json:real_data_numeric_fields_and_execution_flags",
                "json:new_model_contexts",
                "json:new_model_query_rows",
                "json:new_RCTL_fits",
                "json:elapsed_seconds",
            ],
        ).read_text(encoding="utf-8")
    )
    plan = path("08_finite_sample_information_plan.md", ["sha256_only"])
    check("plan_hash", hashlib.sha256(plan.read_bytes()).hexdigest() == saved["plan_sha256"])
    s = saved["synthetic"]
    check(
        "toy_contract",
        s["seed"] == 20260925
        and s["replicates"] == 20000
        and s["cells"] == 3
        and s["samples_per_cell"] == 31
        and s["loss"] == "absolute error",
    )
    close("population_Bayes_risk", s["same_oracle_population_Bayes_risk"], math.sqrt(2 / math.pi))
    close(
        "reported_toy_difference",
        s["independent"]["pooled_MAE"] - s["independent"]["local_MAE"],
        s["independent"]["pooled_minus_local"],
    )
    for kind in ["local", "pooled"]:
        close(
            "reported_excess",
            s["independent"][kind + "_MAE"] - s["same_oracle_population_Bayes_risk"],
            s["independent"][kind + "_excess_over_Bayes"],
        )
    close("shared_report_equal", s["shared"]["local_MAE"], s["shared"]["pooled_MAE"])
    check(
        "shared_report_zero",
        s["shared"]["pooled_minus_local_exact"] == 0
        and s["shared"]["identical_medians_verified"] is True,
    )
    # Repeating each of 31 observations three times maps pooled order 47 to order 16.
    check("shared_order_statistic_identity", math.ceil(((31 * 3 + 1) // 2) / 3) == (31 + 1) // 2)

    d = arrays("results/design_data.npz", ["Y", "times", "cell_indices"])
    r = arrays(
        "results/observed_risk_tables.npz",
        [
            "selected_cells",
            "predicted_quantiles",
            "base_query",
            "query_bins",
            "cell_ids",
        ],
    )
    real = saved["real_data"]
    mask = (d["times"] >= 672) & (d["times"] < 840)
    check("query_times", np.array_equal(d["times"][mask], np.arange(672, 840)))
    check(
        "selected_cells",
        np.array_equal(
            r["selected_cells"],
            np.array([0, 2, 4, 7, 8, 10, 12, 15, 16, 18, 20, 23, 24, 26, 28, 31]),
        ),
    )
    y = d["Y"][r["selected_cells"]][:, mask]
    p = r["predicted_quantiles"]
    check(
        "real_identity",
        p.shape == (16, 168, 129)
        and y.shape == (16, 168)
        and real["cell_ids"]
        == r["cell_ids"].tolist()
        == (d["cell_indices"][r["selected_cells"]] + 1).tolist()
        == [
            3737,
            3745,
            3753,
            3765,
            4537,
            4545,
            4553,
            4565,
            5337,
            5345,
            5353,
            5365,
            6137,
            6145,
            6153,
            6165,
        ]
        and real["query_target_indices"] == [672, 839]
        and real["observations_per_cell"] == 168,
    )
    check("quantile_order", np.isfinite(p).all() and (np.diff(p, axis=2) >= -1e-12).all())
    check(
        "query_bins",
        r["query_bins"].shape == (16, 168)
        and np.issubdtype(r["query_bins"].dtype, np.integer)
        and (r["query_bins"] >= 0).all()
        and (r["query_bins"] < 64).all(),
    )
    check(
        "base_query",
        r["base_query"].shape == (16, 168)
        and np.isfinite(r["base_query"]).all()
        and np.isfinite(y).all(),
    )
    median = p[:, :, 64]
    levels = (np.arange(129) + 0.5) / 129

    def quantile(q):
        """Interpolate the saved midpoint quantiles at a requested coverage boundary."""
        return np.apply_along_axis(lambda v: np.interp(q, levels, v), 2, p)

    def corr(v):
        """Calculate upper-triangle Pearson correlations by centered cross-products."""
        a = v.astype(float) - v.astype(float).mean(1, keepdims=True)
        cross = a @ a.T
        denom = np.sqrt(np.diag(cross)[:, None] * np.diag(cross)[None, :])
        check("nonconstant_streams", (denom > 0).all())
        return (cross / denom)[np.triu_indices(16, 1)]

    def ranks(v):
        """Assign mean ranks to exact ties without importing historical SciPy code."""
        order = np.argsort(v, kind="stable")
        out, start = np.empty(len(v), float), 0
        while start < len(v):
            stop = start + 1
            while stop < len(v) and v[order[stop]] == v[order[start]]:
                stop += 1
            out[order[start:stop]] = (start + stop - 1) / 2
            start = stop
        return out

    def describe(v):
        """Summarize the finite stored-design diagnostics with the original conventions."""
        return dict(
            min=float(np.nanmin(v)),
            median=float(np.nanmedian(v)),
            max=float(np.nanmax(v)),
            finite_count=int(np.isfinite(v).sum()),
        )

    streams = dict(
        raw=y,
        ridge_residual=y - r["base_query"],
        TabICL_median_residual=y - median,
        TabICL_median_exceedance=(y > median).astype(float),
    )
    for name, v in streams.items():
        full, first, last = corr(v), corr(v[:, :84]), corr(v[:, 84:])
        row = real["correlations"][name]
        close("pair_correlations_" + name, full, row["pair_values"])
        a, b = ranks(first), ranks(last)
        a -= a.mean()
        b -= b.mean()
        spearman = float(a @ b / np.sqrt((a @ a) * (b @ b)))
        close(
            "half_rank_correlation_" + name,
            spearman,
            row["first84h_vs_last84h_pair_rank_correlation"],
        )
        for key, value in [
            ("all_168h_pair_correlations", full),
            ("pair_abs_difference_between_halves", np.abs(first - last)),
        ]:
            for stat, answer in describe(value).items():
                close("pair_summary_" + stat, answer, row[key][stat])
    close(
        "median_calibration",
        (y <= median).mean(1),
        real["calibration"]["per_cell_fraction_Y_le_median"],
    )
    for coverage, lo, hi in [(0.5, 0.25, 0.75), (0.8, 0.1, 0.9)]:
        inside = (y >= quantile(lo)) & (y <= quantile(hi))
        row = real["calibration"][str(coverage)]
        close("coverage_percell", inside.mean(1), row["per_cell_coverage"])
        close("coverage_overall", inside.mean(), row["overall_coverage"])
    counts = np.stack([np.bincount(b, minlength=64) for b in r["query_bins"]])
    occ = real["state_occupancy"]
    close("occupied_states", (counts > 0).sum(1), occ["occupied_states_per_cell"])
    close(
        "sparse_cell_states",
        (counts[counts > 0] <= 2).mean(),
        occ["fraction_occupied_cell_states_with_at_most_2_samples"],
    )
    close(
        "sparse_queries",
        counts[(counts > 0) & (counts <= 2)].sum() / counts.sum(),
        occ["fraction_queries_in_states_with_at_most_2_samples"],
    )
    for stat, value in describe(counts[counts > 0]).items():
        close("occupancy_summary_" + stat, value, occ["nonempty_cell_state_counts"][stat])
    check(
        "historical_execution_flags",
        real["RCTL_outputs_used"] is False
        and saved["new_model_contexts"]
        == saved["new_model_query_rows"]
        == saved["new_RCTL_fits"]
        == 0
        and 0 < saved["elapsed_seconds"] < 30,
    )
    if manifest:
        for key in mapping:
            if key not in accessed:
                path(key.removeprefix(base), ["sha256_only"])
        for key, row in accessed.items():
            check(
                "declared_automated_scope",
                set(row["read_scope"]) == set(mapping[key]["automated_read_scope"]),
            )
    return dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks=dict(checks),
        max_absolute_difference=max(max_by_check.values()),
        max_by_check=max_by_check,
        absolute_tolerance=1e-10,
        numpy_version=np.__version__,
        model_executions=0,
        Monte_Carlo_resimulations=0,
        historical_code_executed=False,
        accessed=list(accessed.values()),
        reported_synthetic=s,
        real_summaries={
            k: {a: b for a, b in v.items() if a != "pair_values"}
            for k, v in real["correlations"].items()
        },
        calibration=real["calibration"],
        state_occupancy=occ,
        elapsed_seconds_reported=saved["elapsed_seconds"],
        limits=[
            "Synthetic Monte Carlo draws/medians are not in the inspected saved JSON. "
            "MC means and SE are reported, not independently recomputed.",
            "Bayes risk and shared-median order-statistic identity are mathematical checks; "
            "no new random samples.",
            "Real diagnostics use the same B2 design week; "
            "no innovation identification, causality or independent validation.",
            "Plan hash links content, not an independently attested execution timestamp. "
            "Memory cap is not a measured peak.",
            "Primary literature requires separate semantic review; "
            "this program verifies no theorems or novelty claims.",
        ],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = verify(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            dict(
                success=report["success"],
                checks=sum(report["checks"].values()),
                max_difference=report["max_absolute_difference"],
                model_executions=0,
                Monte_Carlo_resimulations=0,
                accessed_sources=len(report["accessed"]),
            )
        )
    )
