# 13–15 출처와 검토 범위

[연구 기록](../records/0013-0015-transfer-cell-identity.md), [근거 안내](../evidence/0013-0015/README.md), [출처 목록](../catalog/history-008-sources.jsonl)을 연결한다. 경로는 원본 별칭 `Tab-ICL` 기준이며 팀 열람은 아래 보존 사본을 사용한다. 바이트가 같은 사본만 manifest의 `exact_alias_source_ids`로 연결했다.

| 원문 ID·보존 사본 | 원래 파일 | 읽은 범위·검수 한계 |
|---|---|---|
| [SRC-0020929](../evidence/0013-0015/originals/SRC-0020929.md.txt) | `13_upc_transfer_diagnostic_plan.md` | 전체 1–17행; 정적 검토 |
| [SRC-0020950](../evidence/0013-0015/originals/SRC-0020950.md.txt) | `14_cell_identity_diagnostic_plan.md` | 전체 1–23행; 정적 검토 |
| [SRC-0020972](../evidence/0013-0015/originals/SRC-0020972.md.txt) | `15_transfer_identity_and_literature_findings.md` | 전체 1–62행; 정적 검토; §3 문헌 34–52행은 주장 검수 미완료 |
| [SRC-0023210](../evidence/0013-0015/originals/SRC-0023210.py.txt) | `upc_transfer_diagnostic.py` | 전체 1–85행; 정적 검토 |
| [SRC-0022570](../evidence/0013-0015/originals/SRC-0022570.py.txt) | `cell_identity_diagnostic.py` | 전체 1–76행; 정적 검토 |
| [SRC-0023614](../evidence/0013-0015/originals/SRC-0023614.json) | `upc_transfer_diagnostic.json` | JSON 전체 키; 원문 1035행 |
| [SRC-0024836](../evidence/0013-0015/originals/SRC-0024836.json) | `calls.json` | JSON 전체 키; 원문 32행 |
| [SRC-0024839](../evidence/0013-0015/originals/SRC-0024839.json) | `run_finished.json` | JSON 전체 키; 원문 1행 |
| [SRC-0024840](../evidence/0013-0015/originals/SRC-0024840.json) | `run_started.json` | JSON 전체 키; 원문 281행 |
| [SRC-0024841](../evidence/0013-0015/originals/SRC-0024841.json) | `summary.json` | JSON 전체 키; 원문 654행 |
| [SRC-0023615](../evidence/0013-0015/originals/SRC-0023615.npz) | `upc_transfer_values.npz` | 저장 수치 배열의 지정 필드; 객체 payload 제외 |
| [SRC-0024837](../evidence/0013-0015/originals/SRC-0024837.npz) | `predictions.npz` | 저장 수치 배열의 지정 필드; 객체 payload 제외 |
| [SRC-0024838](../evidence/0013-0015/originals/SRC-0024838.npz) | `predictions_partial.npz` | 저장 수치 배열의 지정 필드; 객체 payload 제외 |
| [SRC-0023577](../evidence/0001-0002/originals/SRC-0023577.npz) | `design_data.npz` | 저장 수치 배열의 지정 필드; 객체 payload 제외 |
| [SRC-0023605](../evidence/0003-0007/originals/SRC-0023605.npz) | `risk_table_predictions.npz` | 저장 수치 배열의 지정 필드; 객체 payload 제외 |
| [SRC-0023612](../evidence/0010-0012/originals/SRC-0023612.npz) | `upc_core_labels.npz` | 저장 수치 배열의 지정 필드; 객체 payload 제외 |

본문 전체 5개·JSON 전체 키 5개·신규 배열 3개를 읽고 이전 배열 3개를 재사용했다. source code는 읽기만 했으며 import/실행하지 않았다. 파일별 산술 읽기 범위는 manifest와 검산 결과의 `read_scope`를 확인한다. source ID가 같더라도 개별 주장의 검수 범위는 다르다.

`design_data.npz`의 수치 6배열은 정답/정규화/PCC와 행 매핑에 사용했다. 날짜 object는 header만 확인하고 역직렬화하지 않았다. B1에서는 `median`의 실제 query 접미부와 `cell_ids`, `query_times`, `context_times`, `selected_cells`를 검산에 썼다. 나머지 분위수·anchor 손실표의 새 방법 검수는 이번 범위가 아니다. UPC 24벡터는 16ID의 소속 비교에 사용했고 도시 clustering을 다시 만들지 않았다.

15의 역사적 문헌 입수 manifest는 별도로 읽었지만 이번 보존 16출처/주장 검수에 더하지 않았다. 여섯 문헌 일차자료와 15 §3의 신규성 판단은 후속 묶음에 남아 있다. 과거 HTTP 오류·다음 실험·예산 문구를 현재 blocker나 실행 지시로 사용하지 않는다.
