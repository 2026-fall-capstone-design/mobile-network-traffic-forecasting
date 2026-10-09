"""저장된 초기 호출·학습 비용을 검산하며 과거 모델 코드를 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

CALL_GROUPS = [
    ("smoke", "SRC-0023607", 4, 256, 64),
    ("B1", "SRC-0023601", 16, 504, 1088),
    ("B2", "SRC-0023586", 16, 504, 168),
    ("cell_identity", "SRC-0024836", 3, 2688, 1024),
    ("broad_cell_information", "SRC-0024349", 4, 2048, 2048),
    ("target_parameterization", "SRC-0032380", 2, 2048, 2048),
]
SUMMARY_SOURCES = {
    "B1": ("SRC-0023604", "total_seconds", None),
    "B2": ("SRC-0023588", "seconds", None),
    "cell_identity": ("SRC-0024841", "stage_seconds", 4),
    "broad_cell_information": ("SRC-0024354", "stage_seconds", 6),
    "target_parameterization": ("SRC-0032385", "stage_seconds", 4),
}


def verify(manifest_path: Path) -> dict:
    """출처 바이트와 호출 단위·합계·종료 기록을 검사해 비용 원장을 반환한다."""
    manifest_path = manifest_path.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    archive = manifest_path.parents[2]
    checks: list[str] = []
    sources: dict[str, bytes] = {}

    def check(name: str, condition: bool) -> None:
        """위반한 불변식의 이름을 남겨 잘못된 비용 해석을 차단한다."""
        if not condition:
            raise ValueError(name)
        checks.append(name)

    def numeric(name: str, value: object, *, positive: bool = True) -> float:
        """불리언·비유한 값·잘못된 부호를 시간 수치에서 제외한다."""
        check(name + ":type", type(value) in (int, float))
        number = float(value)
        check(name + ":finite", math.isfinite(number))
        check(name + ":sign", number > 0 if positive else number >= 0)
        return number

    def same(name: str, actual: float, expected: float) -> None:
        """저장 시간과 재합산 값의 작은 부동소수점 차이만 허용한다."""
        check(name, math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-9))

    def load(sid: str) -> object:
        """검증된 원본 JSON만 읽으며 모듈이나 역사적 코드는 불러오지 않는다."""
        return json.loads(sources[sid].decode("utf-8-sig"))

    check(
        "unique_source_ids",
        len({r["source_id"] for r in manifest["sources"]}) == len(manifest["sources"]),
    )
    for row in manifest["sources"]:
        sid = row["source_id"]
        path = (manifest_path.parent / row["archive_path"]).resolve()
        check(sid + ":inside_archive", path.is_relative_to(archive))
        raw = path.read_bytes()
        check(sid + ":size", len(raw) == row["size_bytes"])
        check(sid + ":sha256", hashlib.sha256(raw).hexdigest() == row["sha256"])
        sources[sid] = raw

    calls_by_group, totals = {}, []
    for group, sid, count, context, query in CALL_GROUPS:
        data = load(sid)
        calls = data["runs"] if group == "smoke" else data
        check(group + ":call_count", len(calls) == count)
        identity = "cell_id" if group in ("smoke", "B1", "B2") else "condition"
        check(group + ":unique_calls", len({r[identity] for r in calls}) == count)
        fit, predict = [], []
        for index, row in enumerate(calls):
            prefix = f"{group}:{index}"
            check(
                prefix + ":context_rows",
                type(row["context_rows"]) is int and row["context_rows"] == context,
            )
            check(
                prefix + ":query_rows",
                type(row["query_rows"]) is int and row["query_rows"] == query,
            )
            check(prefix + ":ensemble1", row.get("ensemble", row.get("n_estimators")) == 1)
            fit.append(numeric(prefix + ":fit_seconds", row["fit_seconds"]))
            predict.append(numeric(prefix + ":predict_seconds", row["predict_seconds"]))
        calls_by_group[group] = calls
        totals.append(
            dict(
                group=group,
                source_id=sid,
                context_calls=count,
                context_rows_per_call=context,
                query_rows_per_call=query,
                query_rows=count * query,
                fit_seconds=sum(fit),
                predict_seconds=sum(predict),
                fit_predict_seconds=sum(fit) + sum(predict),
            )
        )
    check(
        "B1_B2_same_cells",
        {r["cell_id"] for r in calls_by_group["B1"]}
        == {r["cell_id"] for r in calls_by_group["B2"]},
    )

    stage_costs = []
    for row in totals:
        group = row["group"]
        if group not in SUMMARY_SOURCES:
            continue
        sid, field, simple_fits = SUMMARY_SOURCES[group]
        summary = load(sid)
        stage = numeric(group + ":stage_seconds", summary[field])
        check(group + ":stage_includes_calls", stage >= row["fit_predict_seconds"])
        simple = None
        if simple_fits is not None:
            check(group + ":summary_calls", summary["calls"] == calls_by_group[group])
            check(
                group + ":simple_result_count",
                len([k for k in summary["results"] if k.startswith(("Ridge_", "HGB_"))])
                == simple_fits,
            )
            same(
                group + ":reported_call_seconds",
                numeric(group + ":reported_call_seconds_value", summary["TabICL_seconds"]),
                row["fit_predict_seconds"],
            )
            simple = numeric(group + ":simple_model_seconds", summary["simple_model_seconds"])
            check(
                group + ":stage_includes_simple_models",
                stage >= row["fit_predict_seconds"] + simple,
            )
        stage_costs.append(
            dict(
                group=group,
                source_id=sid,
                source_field=field,
                stage_seconds=stage,
                simple_model_fits=simple_fits,
                simple_model_seconds=simple,
            )
        )

    cumulative = []
    for label, n in [
        ("after_smoke", 1),
        ("record03", 2),
        ("record04", 3),
        ("record15", 4),
        ("record21", 6),
    ]:
        selected = totals[:n]
        cumulative.append(
            dict(
                boundary=label,
                context_calls=sum(r["context_calls"] for r in selected),
                query_rows=sum(r["query_rows"] for r in selected),
                fit_predict_seconds=sum(r["fit_predict_seconds"] for r in selected),
            )
        )
    for label, count, query in [
        ("record03", 20, 17664),
        ("record04", 36, 20352),
        ("record15", 39, 23424),
        ("record21", 45, 35712),
    ]:
        row = next(r for r in cumulative if r["boundary"] == label)
        check(
            label + ":reported_count_and_rows",
            (row["context_calls"], row["query_rows"]) == (count, query),
        )
    check(
        "record21:reported_rounded_seconds",
        round(cumulative[-1]["fit_predict_seconds"], 3) == 223.887,
    )
    addition = sum(r["fit_predict_seconds"] for r in totals[4:])
    check("record21:added_rounded_seconds", round(addition, 3) == 59.672)

    fits, finished = load("SRC-0030237"), load("SRC-0030278")
    check(
        "RCTL:completed_counts",
        len(fits) == finished["fits_completed"] == finished["fits_planned"] == 29,
    )
    check("RCTL:completion_flag", finished["all_fits_complete"] is True)
    expected = {("global", 20260925, 0)}
    for method in ["tabicl_risk", "empirical_risk", "knn_risk", "pcc_balanced", "random_balanced"]:
        expected.update((method, 20260925, k) for k in range(4))
    for method in ["tabicl_risk", "empirical_risk"]:
        expected.update((method, 20260926, k) for k in range(4))
    check(
        "RCTL:method_seed_group_identity",
        {(r["method"], r["seed"], r["cluster"]) for r in fits} == expected,
    )
    grouped = defaultdict(list)
    for index, row in enumerate(fits):
        numeric(f"RCTL:{index}:fit_seconds", row["fit_seconds"])
        check(
            f"RCTL:{index}:epochs",
            type(row["epochs_run"]) is int
            and type(row["best_epoch"]) is int
            and 1 <= row["best_epoch"] <= row["epochs_run"] <= 80,
        )
        grouped[(row["method"], row["seed"])].append(row)
    epochs = sum(r["epochs_run"] for r in fits)
    check("RCTL:total_epochs", epochs == finished["epochs_total"] == 1565)
    wall = numeric("RCTL:wall_seconds", finished["wall_seconds"])
    fit_seconds = sum(r["fit_seconds"] for r in fits)
    check("RCTL:wall_includes_fit_intervals", wall >= fit_seconds)
    rctl = dict(
        fits=len(fits),
        epochs=epochs,
        fit_seconds_sum=fit_seconds,
        stage_wall_seconds=wall,
        stage_minus_fit_seconds=wall - fit_seconds,
        groups=[
            dict(
                method=method,
                seed=seed,
                fits=len(rows),
                epochs=sum(r["epochs_run"] for r in rows),
                fit_seconds=sum(r["fit_seconds"] for r in rows),
            )
            for (method, seed), rows in grouped.items()
        ],
    )
    transfer = load("SRC-0023614")
    check(
        "transfer:reused_predictions",
        all(
            transfer[k] == 0
            for k in ["new_model_contexts", "new_model_query_rows", "new_RCTL_fits"]
        ),
    )
    transfer_seconds = numeric("transfer:elapsed_seconds", transfer["elapsed_seconds"])
    return dict(
        success=True,
        checks=len(checks),
        check_names=checks,
        source_count=len(sources),
        call_groups=totals,
        cumulative=cumulative,
        stage_costs=stage_costs,
        RCTL=rctl,
        transfer_reanalysis_seconds=transfer_seconds,
        new_model_runs=0,
        original_scripts_executed=False,
        failed_attempt_total_seconds=None,
        complete_research_wall_seconds=None,
        scope=(
            "저장 바이트·완료 호출/fit 식별·행 수·epoch·시간 합계를 대조함. "
            "타이머의 의미는 별도 정적 원문 검토이며, "
            "실행시간 재현·전체 실패 비용·전체 연구시간 검증은 아님."
        ),
    )


def main() -> None:
    """저장 근거의 경로와 결과 출력 위치를 받아 검수 결과를 기록한다."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes((json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode())
    print(
        json.dumps({k: result[k] for k in ["success", "checks", "source_count", "new_model_runs"]})
    )


if __name__ == "__main__":
    main()
