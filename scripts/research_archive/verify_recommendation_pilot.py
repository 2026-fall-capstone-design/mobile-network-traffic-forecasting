"""642 저장 문서의 수치·출처·완료 범위를 대조한다. 연구 모델은 실행하지 않는다."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

BASE = "tmp/redesign_20260925/"
STAGE = BASE + "results/bounded_relation_recommendation_642/"
REPORT = "output/research/TabICLv2_UPC소속수정_연구방향과근거_20261004.md"
WORD = "output/docx/TabICLv2_UPC소속수정_연구방향_20261004.docx"
LEDGER = BASE + "cumulative_execution_budget.json"
RCTL = BASE + "results/bounded_relation_RCTL_bridge_639/result.json"


def verify(source: Path) -> dict:
    """원본 루트 또는 보존 manifest를 읽어 문서 인용과 저장 결과의 관계를 검사한다."""
    manifest = json.loads(source.read_text(encoding="utf-8")) if source.is_file() else None
    mapping = {r["path"]: r for r in manifest["sources"]} if manifest else {}
    accessed, decoded, checks = {}, {}, Counter()

    def check(name, condition):
        """검사가 실패하면 불완전한 성공 보고서를 남기지 않고 중단한다."""
        checks[name] += 1
        if not condition:
            raise AssertionError((name, checks[name]))

    def path(key, scope="sha256_only"):
        """실제 파일을 해시하고 접근 구간을 기록한다."""
        p = source.parent / mapping[key]["archive_path"] if manifest else source / key
        if key not in accessed:
            raw = p.read_bytes()
            accessed[key] = dict(
                path=key, sha256=hashlib.sha256(raw).hexdigest(), size_bytes=len(raw), read_scope=[]
            )
            if manifest:
                check(
                    "portable_source_identity",
                    accessed[key]["sha256"] == mapping[key]["sha256"]
                    and len(raw) == mapping[key]["size_bytes"],
                )
        accessed[key]["read_scope"] = sorted(set(accessed[key]["read_scope"]) | {scope})
        return p

    def digest(key):
        """파일에 기록된 해시가 아닌 실제 바이트의 해시를 돌려준다."""
        path(key)
        return accessed[key]["sha256"]

    def field(key, name):
        """조회한 JSON 최상위 값과 전체 파싱을 구분하며 하위 트리는 한 단위로 기록한다."""
        if key not in decoded:
            decoded[key] = json.loads(path(key, "json_parsed").read_text(encoding="utf-8-sig"))
        value = decoded[key][name]
        path(key, "json_top_level:" + name)
        return value

    evidence = STAGE + "evidence_manifest.json"
    review = STAGE + "document_review.json"
    audit = STAGE + "completion_audit.json"
    complete = STAGE + "archive_complete.json"
    settled = STAGE + "settled.json"
    native = STAGE + "native_goal_completion.json"
    for key, expected in field(evidence, "sources").items():
        check("historical_dependency_hash", digest(key) == expected)
    for key, tag in [(REPORT, "report"), (WORD, "docx")]:
        actual = digest(key)
        for metadata in [evidence, review, complete]:
            check("document_identity", actual == field(metadata, tag + "_sha256"))
    final_pdf = STAGE + "render_final/TabICLv2_UPC소속수정_연구방향_20261004.pdf"
    check("pdf_identity_only", digest(final_pdf) == field(review, "pdf_sha256"))
    page_hashes = field(review, "page_hashes")
    check("seven_pages", len(page_hashes) == field(review, "docx_pages") == 7)
    for name, expected in page_hashes.items():
        check("render_page_identity", digest(STAGE + "render_final/" + name) == expected)

    for metadata in [audit, complete]:
        check(
            "direction_complete", field(metadata, "direction_design_deliverables_complete") is True
        )
        check("science_incomplete", field(metadata, "full_scientific_validation_complete") is False)
    check("main_study_unexecuted", field(native, "main_study_executed") is False)
    check("historic_goal_scope", field(native, "full_scientific_validation_complete") is False)
    for name in ["new_models", "new_predictions", "new_traffic_numerical_experiments"]:
        check("no_new_research", field(evidence, name) == 0)
    check("settled_success", field(settled, "success") is True)
    check("no_new_model_or_traffic", field(settled, "research_models") == 0)
    check("no_new_model_or_traffic", field(settled, "new_traffic_numeric_seconds") == 0)
    check("render_cost_separate", field(settled, "document_render_outside_research_model_ledger"))
    check("caps_unchanged", field(settled, "cap_changes") == {})
    ledger_hash = digest(LEDGER)
    for metadata, key in [
        (evidence, "ledger_sha256_before"),
        (evidence, "ledger_sha256_after"),
        (complete, "ledger_sha256"),
        (settled, "ledger_sha256"),
    ]:
        check("ledger_unchanged", field(metadata, key) == ledger_hash)
    used = field(LEDGER, "used")
    check("budget_snapshot_exact", used == field(evidence, "budget_used_snapshot"))
    cheap = sum(field(LEDGER, "new_cheap_diagnostic_seconds").values())
    check(
        "cheap_sum",
        math.isclose(
            cheap, field(evidence, "cheap_seconds_sum_bookkeeping"), rel_tol=0, abs_tol=1e-9
        ),
    )

    report = path(REPORT, "full_text_parsed_table_checked").read_text(encoding="utf-8")
    section = report.split("## 6 실제 확인 결과와 주장별 근거", 1)[1].split("## 7", 1)[0]
    rows = [line for line in section.splitlines() if line.startswith("| ")][1:5]
    check("report_table_shape", len(rows) == 4)
    xml_path = path(WORD, "OOXML:word/document.xml:third_table")
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(xml_path) as archive:
        document = ET.fromstring(archive.read("word/document.xml"))
    tables = document.findall(".//w:tbl", ns)
    check("five_word_tables", len(tables) == 5)
    word_rows = [
        ["".join(cell.itertext()) for cell in row.findall("w:tc", ns)]
        for row in tables[2].findall("w:tr", ns)
    ][1:]
    check("word_result_table_shape", len(word_rows) == 4 and all(len(r) == 4 for r in word_rows))
    methods = ["A_UPC", "A_HGB_free", "A_HGB_relation", "A_Tab_relation"]
    names = ["작은 UPC θ=0", "강한 기존 HGB 소속", "같은 관계 점수와 HGB", "제안한 Tab 관계 소속"]
    parts = ["first240", "last240", "all480"]
    metrics = field(RCTL, "metrics")
    table = []
    for row, word_row, method, name in zip(rows, word_rows, methods, names, strict=True):
        check("method_row_identity", name in row and word_row[0] == name)
        values = re.findall(r"\d+\.\d{6}", row)
        expected = [f"{metrics[method][part]['mean_cell_MAE']:.6f}" for part in parts]
        check("report_rounded_values", values == expected)
        check("word_rounded_values", word_row[1:] == expected)
        table.append(dict(method=method, normalized_MAE=expected))
    comparisons = []
    for baseline in methods[:3]:
        for part in parts:
            row = dict(baseline=baseline, period=part)
            for metric in ["mean_cell_MAE", "mean_cell_raw_MAE"]:
                row[metric + "_percent_change"] = 100 * (
                    metrics["A_Tab_relation"][part][metric] / metrics[baseline][part][metric] - 1
                )
            comparisons.append(row)
            if baseline == "A_HGB_free" or part == "all480":
                displayed = f"{row['mean_cell_MAE_percent_change']:+.2f}%".replace("-", "−")
                check("reported_percent_change", displayed in section)
    harms = {}
    for baseline in ["A_UPC", "A_HGB_free"]:
        differences = [
            a - b
            for a, b in zip(
                metrics["A_Tab_relation"]["all480"]["per_cell_MAE"],
                metrics[baseline]["all480"]["per_cell_MAE"],
                strict=True,
            )
        ]
        harms[baseline] = dict(
            improved=sum(v < -1e-12 for v in differences),
            harmed=sum(v > 1e-12 for v in differences),
            equal=sum(abs(v) <= 1e-12 for v in differences),
        )
    check(
        "reported_cell_counts",
        harms
        == {
            "A_UPC": {"improved": 9, "harmed": 4, "equal": 3},
            "A_HGB_free": {"improved": 10, "harmed": 6, "equal": 0},
        },
    )
    result = dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        scope="642 문서 인용·완료 범위·출처 및 원장 대조. 새 모델과 RCTL MAE 배열 재계산 없음.",
        normalized_table=table,
        comparisons_from_saved639_scalars=comparisons,
        normalized_cell_counts=harms,
        budget_used=used,
        cheap_seconds_sum=cheap,
        unexecuted_main_studies=field(audit, "not_completed_main_study"),
        historic_goal_record_thread=field(native, "thread_id"),
        historical_code_executed=False,
        new_model_executions=0,
        visual_review_is_separate=True,
        read_scope_note=(
            "JSON 조회 최상위 값은 하위 트리 단위이며 중첩 키 추적이 아니다. "
            "Word는 세 번째 표만 자동 검사했다. 전 페이지 판독은 별도 검토 기록을 따른다."
        ),
    )
    if manifest:
        check("all_accesses_declared", set(accessed) <= set(mapping))
        for key, row in mapping.items():
            check(
                "declared_read_scope",
                set(row["automated_read_scope"])
                == set(accessed.get(key, {}).get("read_scope", [])),
            )
    result["checks"] = dict(checks)
    result["accessed"] = list(accessed.values())
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    report = verify(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "success": True,
                "checks": sum(report["checks"].values()),
                "sources_accessed": len(report["accessed"]),
                "model_executions": 0,
            }
        )
    )
