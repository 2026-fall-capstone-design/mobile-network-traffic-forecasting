# 10–12의 원문과 저장 진단

[정리 기록](../../records/0010-0012-population-upc-stability.md), [읽은 범위](../../sources/history-007.md), [검수](../../verification/history-007.md)에서 질문·결과·한계를 확인한다. [manifest](manifest.json)는 원본 루트 기준 경로·SHA-256·동일 사본·실제 검토 범위를 연결한다.

| 원문 | 검토 범위 | 팀 접근 |
|---|---|---|
| `SRC-0020863` / `10_population_scope_plan.md` | 본문1–13행 전체 | [보존 원문](originals/SRC-0020863.md.txt) |
| `SRC-0020887` / `11_upc_core_stability_plan.md` | 본문1–20행 전체 | [보존 원문](originals/SRC-0020887.md.txt) |
| `SRC-0020908` / `12_population_and_upc_findings.md` | 본문1–39행 전체 | [보존 원문](originals/SRC-0020908.md.txt) |
| `SRC-0022978` / `population_scope_diagnostic.py` | 본문1–114행 전체 | [보존 원문](originals/SRC-0022978.py.txt) |
| `SRC-0023208` / `upc_core_stability.py` | 본문1–82행 전체 | [보존 원문](originals/SRC-0023208.py.txt) |
| `SRC-0023595` / `population_scope_diagnostic.json` | JSON 모든 필드 구조 읽기; 숫자는 검산/보고값 구분 | [보존 원문](originals/SRC-0023595.json) |
| `SRC-0023613` / `upc_core_stability.json` | JSON 모든 필드 구조 읽기; 숫자는 검산/보고값 구분 | [보존 원문](originals/SRC-0023613.json) |
| `SRC-0023596` / `population_scope_values.npz` | NPZ:all_numeric_arrays_for_arithmetic | [보존 원문](originals/SRC-0023596.npz) |
| `SRC-0023612` / `upc_core_labels.npz` | NPZ:all_24_saved_label_vectors | [보존 원문](originals/SRC-0023612.npz) |
| `SRC-0023589` / `observed_risk_tables.npz` | array:cell_ids | [보존 원문](../0003-0007/originals/SRC-0023589.npz) |
| `SRC-0023580` / `finite_sample_information.json` | JSON:elapsed_seconds | [보존 원문](../0008-0009/originals/SRC-0023580.json) |

새 보존 파일9개는581,091bytes이며 기존 B2 배열과08 JSON 두 개는 이전 사본을 재사용했다. 보존 원문의 개인 경로·과거 명령은 역사적 내용이다. `.md.txt`와 `.py.txt`를 현재 실행 지시로 사용하지 않는다. 원문 바이트를 보정하거나 재배치하지 않았다.

population NPZ의12개 수치 배열은 ID/eligibility/scale/CV/peak 요약/PCC/lag별 오차다. UPC NPZ에는2파형×3K×2순서×2기간의24개10,000cell 소속 배열이 있다. `-1`은 미배정이다. 별도 NPZ cell-ID 열이 없으므로 코드의 행 순서1–10,000과 population `cell_ids`를 대조했다. 두 자료를 임의 row 순서로 합치지 않는다.

다음 명령은 저장값과 소속만 검산한다. H5 원자료·모델·과거 스크립트를 실행하지 않는다. 저장소 루트에서 실행한다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_population_upc_history.py \
  --source docs/research/evidence/0010-0012/manifest.json \
  --output .research-archive/recheck-0010-0012.json
```

[검산 결과](../../verification/history-007-arithmetic.json)는562개 확인과24개 비교의 전체 값을 담는다. 필수 신규 보존 원문9개의 ID 목록도 검사한다. 원 계획·코드·결과의 실제 재실행 성공을 뜻하지 않는다. 동점 수·raw 품질·실행 시간/RSS는 저장 보고값으로 구분했다. H5의 별도 로컬 해시·날짜 확인은 [이 파일](../../verification/history-007-local-data-check.json)이며 위 명령이나 CI에서 수행되지 않는다.

대용량 H5의 출처·해시와 고정 GECOS 코드 주소는 manifest의 `primary_sources`다. 원 UPC의 지정 쪽 검토는 [일차자료 검토](../../verification/history-007-primary-review.json)에 연결했고 논문 전체를 재게시하지 않았다. 모든 후속 UPC 연구의 완료나 본문 전체 문헌 검토를 뜻하지 않는다.
