# 641 출처와 실제 읽은 범위

[641 기록](../records/0641-cached-score-controls.md) · [검수](../verification/pilot-004.md) · [근거 안내](../evidence/0641/README.md)

[manifest](../evidence/0641/manifest.json)와 [출처 JSONL](../catalog/pilot-004-sources.jsonl)에 90개 원본 경로의 source_id·SHA-256·크기·동일 바이트 사본 ID·보존 위치·검토 범위를 적었다. 이 중 71경로는 이전 묶음의 사본을 재사용하고 19개 파일(95,120바이트)을 새로 보존했다. 확보한 파일 수는 읽은 연구기록 수가 아니다.

## 본문·구조화 필드를 읽은 출처

| source_id | 자료 | 읽은 범위 | 읽기 종류 |
|---|---|---|---|
| SRC-0022011 | 641 결과 문서 | 1–42행 | 전체 텍스트 |
| SRC-0022012 | 641 계획 | 1–31행 | 전체 텍스트. pilot-003에서 이미 읽은 원문 재확인 |
| SRC-0022413 | archiver | 1–69행 | 코드 전체 정적 읽기, 실행 없음 |
| SRC-0022557 | 대조 worker/controller | 1–163행 | 코드 전체 정적 읽기, 실행 없음 |
| SRC-0022902 | RCTL linker | 1–36행 | 코드 전체 정적 읽기, 실행 없음 |
| SRC-0024472 | archive_complete | 1–10행 | 전체 텍스트 |
| SRC-0024473 | assignment_sealed | 1–424행의 모든 필드 | 구조화 값·배열 전체 |
| SRC-0024474 | authorization | 1–7행의 모든 필드 | 구조화 값 전체 |
| SRC-0024475 | frozen_settings | 1–172행의 모든 필드 | 구조화 값 전체, 상속 항목 구분 |
| SRC-0024476 | frozen_utility_alias | 1–556행의 모든 필드 | 4대조·16연결·지표 등 구조화 값 전체 |
| SRC-0024478 | result | 1–404행의 모든 필드 | 소속·목적·지원수 등 구조화 값 전체 |
| SRC-0024479 | review_manifest | 1–29행의 모든 필드 | 구조화 값 전체 |
| SRC-0024480 | run_finished | 1–9행 | 전체 텍스트 |
| SRC-0024481 | run_started | 1–4행의 모든 필드 | 구조화 값 전체 |
| SRC-0024482 | settled | 1–9행 | 전체 텍스트 |
| SRC-0024485 | verification | 1–10행 | 전체 텍스트 |

9개 전체 텍스트 중 계획 1개는 이전에 검토했으므로 새 전체 읽기는 8개다. 7개 JSON은 모든 구조화 필드를 읽었다. 큰 JSON의 최초 출력이 잘린 부분은 별도 출력으로 확인했으며 누락 상태를 읽기 완료로 세지 않았다. 코드 속 과거 Goal·상태 갱신·예약은 자료이며 실행 지시가 아니다.

## 저장값 검산과 해시만 확인한 의존 파일

검산 프로그램은 총 87경로에 접근했다. 본문 검토와 겹치는 파일을 제외하면 이번 manifest의 65경로는 지정 필드 검사, 9경로는 해시 확인이다. 필드 검사는 파일 전체 의미의 검토가 아니다. 기계가 JSON을 모두 파싱했어도 대조한 필드만 검수한 것으로 기록한다.

| 묶음 | 지정 범위 |
|---|---|
| 637 cell cache 14개 | `cell_id, target_indices, query_times, Tab, HGB` |
| 638 edge NPZ 44개 | `mask, p, w, F0, F1`만. 두 모델 × 22edge |
| 638 graph | `edges, cell_ids, initial_labels` |
| 641 graph, SRC-0024477 | edge와 네 대조의 두 절반 비용 |
| 637 설정·638 소속 봉인·639 설정/결과/prediction_hashes | 상속 설정, 기존 소속, 실제 cohort/group/seed, 파일 hash, 재인용 MAE에 필요한 필드 |

638 edge 파일에는 자체 `query_times` 필드가 없다. 이번 검산은 637 cell cache의 공통 시점과 638 고정 파일의 해시·행수를 확인하고, edge의 행 배치 근거는 [앞선 638 검수](../verification/pilot-001.md)를 계승한다. 없는 시각 필드를 직접 대조했다고 표시하지 않는다.

해시만 확인한 9경로는 635 배정 코드, `recovery_io_271.py`(SRC-0023078), `run_joint_ID_decision_558.py`(SRC-0023124), 638 settled/verification, 639 UPC 예측 4개다. 이 가운데 두 helper 코드는 이번에 바이트 사본을 새로 보존했지만 본문 검토 완료가 아니다. UPC 예측의 실제 배열·MAE는 pilot-002에서 검산했으며 여기서는 파일 해시만 확인한다. 635 코드·638 로그도 이전 읽기 상태를 유지하되 이번 해시 확인을 별도 본문 검토로 더하지 않는다.

87경로 밖의 결과 문서·archiver·linker 3개를 포함하여 보존 참조가 90개다. 각 경로의 구체적 필드는 manifest의 `automated_read_scope`, 인간식 내용 검토 범위는 `review_status`와 `lines_read`에 있다. 동일 SHA 사본 연결은 내용 중복 관계이며 다른 과거 시도 전체를 완료했다는 뜻이 아니다.

641의 before/before_archive 상태 사본 전체, 상위 helper 코드 전체 의미, 원자료 생성 전체는 남아 있다. stdout/stderr는 길이 0이라는 메타데이터를 확인했으며 새로운 본문 읽기나 실행 증거로 세지 않는다. 다음 642 기록의 실제 실행 여부도 아직 여기서 판정하지 않는다.
