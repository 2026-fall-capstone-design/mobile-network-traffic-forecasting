# H029 출처와 실제 열람 범위

[48–49 정리 기록](../records/0048-0049-aggregation-recovery.md)은 [목록](../catalog/history-029-sources.jsonl)과 [manifest](../evidence/0048-0049-aggregation-recovery/manifest.json)의15개 원본 참조를 연결한다. 새 정확 사본11개·3,725,352 bytes, 기존 사본3개, HDF5 metadata1개다. 새 사본에는3.6MB의 저장 NPZ가 포함된다. 원래 바이트·줄바꿈을 보존했다. `.py.txt`는 역사 자료로만 읽었다.

| 출처·팀 접근 | 원본 루트 기준 경로 | 실제 검토 범위 |
|---|---|---|
| [SRC-0021681](../evidence/0048-0049-aggregation-recovery/originals/SRC-0021681.md.txt) | `tmp/redesign_20260925/48_aggregation_review_plan.md` | 48 계획 전체43행. cell 출처 수정 보고·시간·partition·비중·손실·비용·판단 범위 |
| [SRC-0021725](../evidence/0048-0049-aggregation-recovery/originals/SRC-0021725.md.txt) | `tmp/redesign_20260925/50_aggregation_findings.md` | 50 전체66행 초독; 수치 진단·오차 관계·비용 부분2차대조. 문헌·신규성 종합·접근 보고는 대기 |
| [SRC-0022133](../evidence/0048-0049-aggregation-recovery/originals/SRC-0022133.py.txt) | `tmp/redesign_20260925/aggregation_recovery_diagnostic_49.py` | 49 코드 전체157행 정적 독해. 실행하지 않음 |
| [SRC-0023211](../evidence/0048-0049-aggregation-recovery/originals/SRC-0023211.py.txt) | `tmp/redesign_20260925/update_budget_after_aggregation_49.py` | 원장 갱신 코드 전체19행 정적 독해. 실행하지 않음 |
| [SRC-0023807](../evidence/0048-0049-aggregation-recovery/originals/SRC-0023807.npz) | `tmp/redesign_20260925/results/aggregation_recovery_49/predictions.npz` | 52개 배열의 schema·유한값·값 정의·저장 지표 산술 대조. 개별 원소 전수 수동 독해 아님 |
| [SRC-0023808](../evidence/0048-0049-aggregation-recovery/originals/SRC-0023808.json) | `tmp/redesign_20260925/results/aggregation_recovery_49/result.json` | top keys·설정·scale32개·모든그룹·기준값·12조합의선택지표·toy/비용/한계 수동 열람. 모든 저장 수치 필드 프로그램 대조. JSON개별값 전수 수동 독해 아님 |
| [SRC-0023809](../evidence/0048-0049-aggregation-recovery/originals/SRC-0023809.json) | `tmp/redesign_20260925/results/aggregation_recovery_49/run_finished.json` | 완료 표시 전체 키/값 |
| [SRC-0023810](../evidence/0048-0049-aggregation-recovery/originals/SRC-0023810.json) | `tmp/redesign_20260925/results/aggregation_recovery_49/run_started.json` | 시작 표시 전체 키/값 |
| [SRC-0023811](../evidence/0048-0049-aggregation-recovery/originals/SRC-0023811.json) | `tmp/redesign_20260925/results/aggregation_recovery_49/settings.json` | 설정 전체 키/값; 입력/계획/코드 해시·cell·seed·시간·timer 경계 |
| [SRC-0000690](../evidence/0048-0049-aggregation-recovery/originals/SRC-0000690.json) | `output/research/redesign_20260925_snapshot_11/manifest.json` | snapshot11 manifest 전체33 metadata 행과 모든 나머지 키. 연결파일33개 본문 완료 아님 |
| [SRC-0000695](../evidence/0048-0049-aggregation-recovery/originals/SRC-0000695.json) | `output/research/redesign_20260925_snapshot_11/tmp/redesign_20260925/cumulative_execution_budget.json` | snapshot11 원장 전체 키/항목. 마지막 cheap49 및 snapshot10/현재prefix 연결 |
| [SRC-0031959](../evidence/0048-0049-aggregation-recovery/../0018-0021/originals/SRC-0031959.npz) | `tmp/redesign_20260925/results/spatial_information/predictions.npz` | 18의 cell_ids/query_times/y 재사용. 새 전체파일 독해 집계 없음 |
| [SRC-0000661](../evidence/0048-0049-aggregation-recovery/../0045-0046-input-stability/originals/SRC-0000661.json) | `output/research/redesign_20260925_snapshot_10/tmp/redesign_20260925/cumulative_execution_budget.json` | snapshot10 원장 H027 전체검토 재사용. 11과차이 대조 |
| [SRC-0022700](../evidence/0048-0049-aggregation-recovery/../0642/originals/SRC-0022700.json) | `tmp/redesign_20260925/cumulative_execution_budget.json` | 현재 누적 원장의 첫17cheap·6Tab호출·2고정inference만. 전체 원장 신규 독해 아님 |
| SRC-0023485 | `tmp/redesign_20260925/assets/data_git_version.h5` | 전체파일크기/해시와 data[:1008,지정32cell ID−1,2]. 전체H5내용·원 CDR 전처리 재현 아님;binary팀접근미완료 |

이번 전체 텍스트 검토 집계는48 계획·49 코드·원장 갱신 코드3개다. 50은 전 문장을 읽었어도 문헌 근거 검수가 남아 부분 통합으로 유지한다. 작은 JSON 전체5개와 결과 JSON의 선택 수치1개를 별도 집계한다. NPZ52개 배열의 프로그램 대조를 개별 원소의 수동 독해로 표현하지 않는다.

원자료를 다시 확인한 범위는 첫1,008시간·고정32개cell·3번째채널이다. 이 자료로 정규화 척도·참조 비중·지정 partition·정답과 저장 배열의 관계를 검산했다. H5 전체의 해시는 같지만 모든 채널·cell·시각을 읽은 것은 아니다. 동일 query index의 날짜는 기존 H012/H027의 시간 검수를 연결했다. 과거 환경과 원 CDR에서 H5까지의 전처리 재현도 완료하지 않았다.

[저장 산술 검사](../verification/history-029-saved-check.json)는 총1,025개 확인 중 수치231필드 비교를 포함한다. 배열 비교 하나는 한 필드로 셌다. median의 convex 최적 조건, 48개 복원 배열, normalized/raw/주별/cell별 지표·총량 지표·항등식·원단위 오차 범위·입력 identity 등을 확인했다. 원 연구 코드·모델·난수 생성은 실행하지 않았다. 무작위 seed의 출력 재현은 미확인이고 저장 그룹의 partition만 확인했다. 참조 합계0분기는 실제 구간에서 나타나지 않았다.

[계보 검사](../verification/history-029-lineage-check.json)는 원본15개 identity·사본·과거원장 차이/현재prefix·snapshot11 ledger의 manifest행·당시 비용과 원 연구 통제파일6개의 불변을 연결한다. snapshot33개metadata를 확인한 사실은33개고유본문검수와 다르다. 설정의 사전 hash와 저장 기록의 일관성을 확인했으며 모든 미기록 실행의 부재를 증명한 것은 아니다.

50의 HiGP·ONDM·HTS-Cluster 상세 문헌/신규성 종합·접근/렌더 기록, 별도 요약 보고서·후속191/392와 전체 고유 내용은 남아 있다. 문헌 PDF·그림이 존재한다는 것만으로 읽기 완료로 표시하지 않는다. 원문50의 전체 판단을 이번 수치검수만으로 모두 확정하지 않았다.
