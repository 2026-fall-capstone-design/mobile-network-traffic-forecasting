"""Recalculate printed CCM table values without network, training, or original code."""

import argparse
import json
from collections import Counter
from decimal import Decimal, getcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "docs/research/evidence/0092-ccm"


def calculate(data):
    getcontext().prec = 40

    def expand(rows):
        occupied = {}
        for ri, row in enumerate(rows):
            ci = 0
            for cell in row:
                while (ri, ci) in occupied:
                    ci += 1
                for dr in range(cell["rowspan"]):
                    for dc in range(cell["colspan"]):
                        key = ri + dr, ci + dc
                        assert key not in occupied, key
                        occupied[key] = cell
                ci += cell["colspan"]
        width = max(c for _, c in occupied) + 1
        assert all((r, c) in occupied for r in range(len(rows)) for c in range(width))
        return [[occupied[r, c] for c in range(width)] for r in range(len(rows))]

    grids = {t["figure_id"]: expand(t["rows"]) for t in data["tables"]}
    models = ["TSMixer", "DLinear", "PatchTST", "TimesNet"]
    D = Decimal

    def paired(table, start, offset, descriptor_cols, stride, enhanced_delta, metrics):
        out = []
        for ri, row in enumerate(grids[table][start:], start + 1):
            for mi, model in enumerate(models):
                for ki, metric in enumerate(metrics):
                    a = row[offset + stride * mi + ki]
                    b = row[offset + stride * mi + ki + enhanced_delta]
                    av, bv = D(a["text"]), D(b["text"])
                    out.append(
                        dict(
                            table=table,
                            html_row=ri,
                            condition=[row[c]["text"] for c in descriptor_cols],
                            model=model,
                            metric=metric,
                            base=a["text"],
                            ccm=b["text"],
                            outcome="improved" if bv < av else "tied" if bv == av else "worse",
                            relative_reduction_pct=str((av - bv) / av * 100),
                            base_bold=a["bold"],
                            ccm_bold=b["bold"],
                            base_underline=a["underline"],
                            ccm_underline=b["underline"],
                        )
                    )
        return out

    def summarize(rows):
        return dict(
            n=len(rows),
            outcomes=dict(Counter(r["outcome"] for r in rows)),
            average_relative_reduction_pct=str(
                sum(D(r["relative_reduction_pct"]) for r in rows) / len(rows)
            ),
        )

    t4 = paired("S5.T4", 2, 2, [0, 1], 4, 2, ["MSE", "MAE"])
    t7 = paired("S5.T7", 2, 2, [0, 1], 4, 2, ["MSE", "MAE"])
    t6 = []
    for ri, row in enumerate(grids["S5.T6"][1:], 2):
        for mi, model in enumerate(models):
            a, b = row[2 + mi * 2]["text"], row[3 + mi * 2]["text"]
            av, bv = D(a), D(b)
            t6.append(
                dict(
                    table="S5.T6",
                    html_row=ri,
                    condition=[row[0]["text"]],
                    metric=row[1]["text"],
                    model=model,
                    base=a,
                    ccm=b,
                    outcome="improved" if bv < av else "tied" if bv == av else "worse",
                    relative_reduction_pct=str((av - bv) / av * 100),
                )
            )
    t11 = []
    for row in grids["A3.T11"][1:]:
        values = [D(c["text"]) for c in row[2:]]
        t11.append(
            dict(
                condition=[c["text"] for c in row[:2]],
                cd=str(values[0]),
                ci=str(values[1]),
                prreg=str(values[2]),
                ccm=str(values[3]),
                outcome="improved"
                if values[3] < values[2]
                else "tied"
                if values[3] == values[2]
                else "worse",
                ccm_is_minimum_all_four=values[3] == min(values),
            )
        )
    t17 = []
    for row in grids["A4.T17"][1:]:
        base = D(row[2]["text"])
        for col in range(3, 9):
            value = D(row[col]["text"])
            t17.append(
                dict(
                    condition=[row[0]["text"], row[1]["text"]],
                    ratio=grids["A4.T17"][0][col]["text"],
                    base=str(base),
                    ccm=str(value),
                    outcome="improved" if value < base else "tied" if value == base else "worse",
                )
            )
    t18 = []
    g = grids["A4.T18"]
    for mi, model in enumerate(models):
        for col in range(1, 13):
            a, b = g[3 + mi * 2][col]["text"], g[4 + mi * 2][col]["text"]
            av, bv = D(a), D(b)
            t18.append(
                dict(
                    model=model,
                    horizon=g[0][col]["text"],
                    lookback=g[1][col]["text"],
                    metric=g[2][col]["text"],
                    base=a,
                    ccm=b,
                    outcome="improved" if bv < av else "tied" if bv == av else "worse",
                    relative_reduction_pct=str((av - bv) / av * 100),
                )
            )

    summary = {}
    for key, rows in [("table4", t4), ("table7", t7), ("table6", t6)]:
        summary[key] = dict(
            all=summarize(rows),
            by_metric={
                k: summarize([r for r in rows if r["metric"] == k])
                for k in sorted({r["metric"] for r in rows})
            },
            by_model={m: summarize([r for r in rows if r["model"] == m]) for m in models},
        )
        summary[key]["by_model_metric"] = {
            m: {
                k: summarize([r for r in rows if r["model"] == m and r["metric"] == k])
                for k in sorted({r["metric"] for r in rows})
            }
            for m in models
        }
    summary["table11"] = {
        "n": len(t11),
        "outcomes": dict(Counter(r["outcome"] for r in t11)),
        "ccm_minimum_all_four": sum(r["ccm_is_minimum_all_four"] for r in t11),
    }
    summary["table17"] = {"n": len(t17), "outcomes": dict(Counter(r["outcome"] for r in t17))}
    summary["table18"] = {"n": len(t18), "outcomes": dict(Counter(r["outcome"] for r in t18))}
    imp = []
    for table, rows in [("S5.T4", t4), ("S5.T7", t7), ("S5.T6", t6)]:
        for ri in sorted({r["html_row"] for r in rows}):
            rr = [r for r in rows if r["html_row"] == ri]
            calculated = sum(D(r["relative_reduction_pct"]) for r in rr) / len(rr)
            displayed = D(grids[table][ri - 1][-1]["text"])
            imp.append(
                dict(
                    table=table,
                    row=ri,
                    condition=rr[0]["condition"],
                    displayed=str(displayed),
                    calculated=str(calculated),
                    absolute_gap_pct_points=str(abs(calculated - displayed)),
                )
            )

    out = dict(
        source_html_sha256=data["HTML_sha256"],
        scope=(
            "printed values only, Decimal arithmetic; "
            "not an experiment reproduction or a significance test"
        ),
        table4_pairs=t4,
        table6_pairs=t6,
        table7_pairs=t7,
        table11_pairs=t11,
        table17_pairs=t17,
        table18_pairs=t18,
        summary=summary,
        IMP_checks=imp,
        source_code_executed=False,
        model_runs=0,
    )
    highlights = []
    for table in ["S5.T4", "S5.T7"]:
        for ri, row in enumerate(grids[table][2:], 3):
            for k, metric in enumerate(["MSE", "MAE"]):
                cells = [row[2 + 2 * j + k] for j in range(8)]
                minimum = min(D(c["text"]) for c in cells)
                for j, c in enumerate(cells):
                    if c["underline"] != (D(c["text"]) == minimum):
                        highlights.append(
                            dict(
                                table=table,
                                row=ri,
                                condition=[row[0]["text"], row[1]["text"]],
                                metric=metric,
                                model=models[j // 2],
                                variant="CCM" if j % 2 else "base",
                                value=c["text"],
                                minimum=str(minimum),
                                underline=c["underline"],
                            )
                        )
    out["underline_vs_displayed_minimum_disagreements"] = highlights
    m4 = [r for r in t6 if r["condition"][0].startswith("M4")]
    out["M4_aggregation_scopes"] = {
        "four_frequency_rows_excluding_aggregate_Avg": summarize(
            [r for r in m4 if r["condition"][0] != "M4 (Avg.)"]
        ),
        "aggregate_Avg_only": summarize([r for r in m4 if r["condition"][0] == "M4 (Avg.)"]),
        "five_rows_including_aggregate_Avg": summarize(m4),
        "five_rows_by_model": {m: summarize([r for r in m4 if r["model"] == m]) for m in models},
        "mean_of_15_displayed_IMP_cells": str(
            sum(
                D(x["displayed"])
                for x in imp
                if x["table"] == "S5.T6" and x["condition"][0].startswith("M4")
            )
            / 15
        ),
        "warning": (
            "Avg. repeats an aggregate, so five-row equal-weight averages are "
            "diagnostic bookkeeping, not 60 independent experimental settings."
        ),
    }
    out["table18_IMP_checks"] = []
    for col in range(1, 13):
        rr = [
            r
            for r in t18
            if r["horizon"] == g[0][col]["text"]
            and r["lookback"] == g[1][col]["text"]
            and r["metric"] == g[2][col]["text"]
        ]
        calculated = sum(D(r["relative_reduction_pct"]) for r in rr) / 4
        shown = D(g[-1][col]["text"])
        out["table18_IMP_checks"].append(
            dict(
                horizon=rr[0]["horizon"],
                lookback=rr[0]["lookback"],
                metric=rr[0]["metric"],
                displayed=str(shown),
                calculated=str(calculated),
                absolute_gap_pct_points=str(abs(shown - calculated)),
            )
        )
    out["table6_stock_table18_exact_value_pair_matches"] = []
    for r in [r for r in t6 if r["condition"][0].startswith("Stock")]:
        horizon = "7" if "Horizon 7)" in r["condition"][0] else "24"
        matches = [
            s["lookback"]
            for s in t18
            if s["model"] == r["model"]
            and s["metric"] == r["metric"]
            and s["horizon"] == horizon
            and s["base"] == r["base"]
            and s["ccm"] == r["ccm"]
        ]
        out["table6_stock_table18_exact_value_pair_matches"].append(
            dict(
                model=r["model"],
                horizon=horizon,
                metric=r["metric"],
                base=r["base"],
                ccm=r["ccm"],
                matching_lookbacks=matches,
                scope="matching displayed values only; not proof of run/config identity",
            )
        )
    out["table14_vs_table4_mean_mismatches"] = []
    for mi, model in enumerate(models):
        for vi, variant in enumerate(["base", "ccm"]):
            for ki, metric in enumerate(["MSE", "MAE"]):
                row = grids["A3.T14"][1 + mi * 4 + vi * 2 + ki]
                for di, cell in enumerate(row[2:]):
                    dataset = grids["A3.T14"][0][di + 2]["text"]
                    expected = [
                        r
                        for r in t4
                        if r["model"] == model
                        and r["metric"] == metric
                        and r["condition"] == [dataset, "24" if dataset == "ILI" else "96"]
                    ][0]
                    mean = cell["text"].split("\\pm")[0].strip()
                    if D(mean) != D(expected[variant]):
                        out["table14_vs_table4_mean_mismatches"].append(
                            dict(
                                model=model,
                                variant=variant,
                                metric=metric,
                                dataset=dataset,
                                table14=mean,
                                table4=expected[variant],
                            )
                        )

    def transpose(a):
        return list(map(list, zip(*a, strict=True)))

    def mul(a, b):
        return [
            [sum(x * y for x, y in zip(row, col, strict=True)) for col in zip(*b, strict=True)]
            for row in a
        ]

    def trace(a):
        return sum(a[i][i] for i in range(len(a)))

    S = [[D(1), D(".5")], [D(".5"), D(1)]]
    out["equation4_static_algebra"] = {
        "identity": "-Tr(M^T S M)+Tr((I-MM^T)S)=Tr(S)-2Tr(M^T S M)",
        "assumption": (
            "ordinary trace and compatible real CxK / CxC matrices; S fixed when comparing M"
        ),
        "scope": "audit inference about printed Eq4, not verification of historical implementation",
        "examples": [],
    }
    for label, M in [("same_cluster", [[1, 0], [1, 0]]), ("separate_clusters", [[1, 0], [0, 1]])]:
        term = trace(mul(mul(transpose(M), S), M))
        mmt = mul(M, transpose(M))
        complement = [[int(i == j) - mmt[i][j] for j in range(len(S))] for i in range(len(S))]
        second = trace(mul(complement, S))
        printed_loss = -term + second
        assert printed_loss == trace(S) - 2 * term
        out["equation4_static_algebra"]["examples"].append(
            dict(
                label=label,
                S=[[str(x) for x in row] for row in S],
                M=M,
                within_trace=str(term),
                second_term=str(second),
                printed_loss=str(printed_loss),
            )
        )
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads((EVIDENCE / "displayed-tables.json").read_text(encoding="utf-8"))
    result = calculate(data)
    if args.check:
        expected = json.loads((EVIDENCE / "table-audit.json").read_text(encoding="utf-8"))
        if result != expected:
            raise SystemExit("CCM printed-table audit differs from the saved report")
        print("CCM: 19 tables, printed-value comparisons and aggregation scopes match")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
