# history-007 출처와 읽은 범위

[10–12 기록](../records/0010-0012-population-upc-stability.md)의 주장은 [11개 보존 경로 안내](../evidence/0010-0012/README.md), [기계 판독 목록](../catalog/history-007-sources.jsonl), [manifest](../evidence/0010-0012/manifest.json)에서 원문과 연결된다. 고유 원문을9개 추가하고 기존2개를 재사용했다. 바이트가 다른 판본은 완료된 사본으로 처리하지 않는다.

| source_id | 원본 루트 기준 경로 | 읽기·검산 범위 |
|---|---|---|
| `SRC-0020863` | `tmp/redesign_20260925/10_population_scope_plan.md` | 1–13행 전체 |
| `SRC-0020887` | `tmp/redesign_20260925/11_upc_core_stability_plan.md` | 1–20행 전체 |
| `SRC-0020908` | `tmp/redesign_20260925/12_population_and_upc_findings.md` | 1–39행 전체 |
| `SRC-0022978` | `tmp/redesign_20260925/population_scope_diagnostic.py` | 1–114행 전체 |
| `SRC-0023208` | `tmp/redesign_20260925/upc_core_stability.py` | 1–82행 전체 |
| `SRC-0023595` | `tmp/redesign_20260925/results/population_scope_diagnostic.json` | JSON 전체 키; 원문 보고값과 재계산 항목을 구분 |
| `SRC-0023613` | `tmp/redesign_20260925/results/upc_core_stability.json` | JSON 전체 키; 원문 보고값과 재계산 항목을 구분 |
| `SRC-0023596` | `tmp/redesign_20260925/results/population_scope_values.npz` | NPZ:all_numeric_arrays_for_arithmetic |
| `SRC-0023612` | `tmp/redesign_20260925/results/upc_core_labels.npz` | NPZ:all_24_saved_label_vectors |
| `SRC-0023589` | `tmp/redesign_20260925/results/observed_risk_tables.npz` | array:cell_ids |
| `SRC-0023580` | `tmp/redesign_20260925/results/finite_sample_information.json` | JSON:elapsed_seconds |

본문 전체는 계획·판단3개와 코드2개다. JSON2개의 모든 키를 읽었으며, UPC JSON의 처음 줄 번호 출력이 잘려 모든 키를 보존하는 compact JSON으로 다시 읽었다. 전체 JSON을 읽은 것과 모든 수치를 raw 자료에서 독립 재계산한 것은 다르다. 저장 population12배열과 UPC24소속 벡터의 지정 산술을 확인했다. 이전 B2의 `cell_ids`와08의 `elapsed_seconds`만 추가 재사용했다.

외부 metadata2건은 기존 자료의 새 지정 검토다. `SRC-0023485` H5의 SHA·크기·shape·처음840개 `idx`를 확인했다. H5의 전체 traffic tensor를 새로 읽거나 upstream 전처리를 재실행하지 않았다. `SRC-0020622` 고정 GECOS `main.py`1–134행은 정적으로 재확인했고, 앞서 확인한 공식 commit 바이트 일치를 재사용했다. [자산 출처](../evidence/0001-0002/manifest.json), [고정 코드](https://github.com/Superint-Lab/GECOS/blob/a7519dde9d6f5deb3006689df047d99ea0dac7b7/main.py).

목록 밖 제공 논문 `EXT-P005-UPC`는 SHA-256 `d8b720fe96f4d2da8ebcbe9dc779c0b4512dec0b2f4823295f908fcd639ae622`,7,721,301bytes다. PDF 물리4·5쪽의 §III.A/Algorithm1을 텍스트·이미지로 다시 확인했다. 기존 검토의 재사용이며 새 논문 한 편의 전체 완료로 집계하지 않는다. [공식 DOI](https://doi.org/10.1109/TNSM.2025.3599168), [일차자료·주장10개](../verification/history-007-primary-review.json).

10–12의 계획/저장 산출물/당시 판단을 통합했다. 이후13–15, 회귀 TabPFN의 후속 이력과 다른 UPC 판본·실험의 연결은 대기 중이다. 번호별 plan/findings의 검색 위치를 찾은 것만으로 본문·실행 검토를 완료하지 않는다. 원문 속 과거 예산·다음 행동·Goal은 정리 대상이며 이 작업의 명령이 아니다.
