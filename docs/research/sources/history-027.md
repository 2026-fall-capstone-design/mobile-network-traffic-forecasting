# H027 출처와 실제 열람 범위

[45–46 정리 기록](../records/0045-0046-input-stability.md)의 원문 17개 참조를 [목록](../catalog/history-027-sources.jsonl)과 [해시 manifest](../evidence/0045-0046-input-stability/manifest.json)에 연결한다. 새 보존 10개·90,808 bytes, 기존 사본 재사용 6개, HDF5 metadata 1개다. 원본 바이트와 줄바꿈을 보존했다. `.py.txt`는 역사 자료이며 실행하지 않았다.

| 원본 ID·팀 접근 | 원본 루트 기준 경로 | 실제 검토 범위 |
|---|---|---|
| [SRC-0021616](../evidence/0045-0046-input-stability/originals/SRC-0021616.md.txt) | `tmp/redesign_20260925/45_input_sharing_review_plan.md` | 45 계획 전체 40행; 문헌은 검토 대상으로만 식별 |
| [SRC-0021660](../evidence/0045-0046-input-stability/originals/SRC-0021660.md.txt) | `tmp/redesign_20260925/47_input_sharing_findings.md` | 47 전체 105행 초독; §2와 §7 수치/보존만 주장 검수. 나머지 대기 |
| [SRC-0022883](../evidence/0045-0046-input-stability/originals/SRC-0022883.py.txt) | `tmp/redesign_20260925/input_sharing_stability_46.py` | 46 코드 전체 91행 정적 독해; 실행하지 않음 |
| [SRC-0023219](../evidence/0045-0046-input-stability/originals/SRC-0023219.py.txt) | `tmp/redesign_20260925/update_budget_after_input_sharing_46.py` | 원장 갱신 코드 전체 20행 정적 독해; 실행하지 않음 |
| [SRC-0027916](../evidence/0045-0046-input-stability/originals/SRC-0027916.json) | `tmp/redesign_20260925/results/input_sharing_stability_46/result.json` | 선택 scalar·표·cell 목록 수동 열람; 모든 model 수치 필드 산술 대조. JSON 개별 값 전수 수동 독해 아님 |
| [SRC-0027917](../evidence/0045-0046-input-stability/originals/SRC-0027917.json) | `tmp/redesign_20260925/results/input_sharing_stability_46/run_finished.json` | 완료 표시 모든 키/값 |
| [SRC-0027918](../evidence/0045-0046-input-stability/originals/SRC-0027918.json) | `tmp/redesign_20260925/results/input_sharing_stability_46/run_started.json` | 시작 표시 모든 키/값 |
| [SRC-0027919](../evidence/0045-0046-input-stability/originals/SRC-0027919.json) | `tmp/redesign_20260925/results/input_sharing_stability_46/settings.json` | 설정 모든 키/값 |
| [SRC-0000661](../evidence/0045-0046-input-stability/originals/SRC-0000661.json) | `output/research/redesign_20260925_snapshot_10/tmp/redesign_20260925/cumulative_execution_budget.json` | 스냅샷 10의 원장 전체 키/항목; 후속 누적 원장과 다른 버전 |
| [SRC-0000657](../evidence/0045-0046-input-stability/originals/SRC-0000657.json) | `output/research/redesign_20260925_snapshot_10/manifest.json` | 스냅샷 manifest의 32개 metadata 행과 나머지 키 전체; 연결 파일 전체 본문 검토와 구별 |
| [SRC-0031959](../evidence/0045-0046-input-stability/../0018-0021/originals/SRC-0031959.npz) | `tmp/redesign_20260925/results/spatial_information/predictions.npz` | 18의 NPZ 재사용; pred/y/cell_ids/query_times 및 이웃 ID 대조 |
| [SRC-0031962](../evidence/0045-0046-input-stability/../0018-0021/originals/SRC-0031962.json) | `tmp/redesign_20260925/results/spatial_information/summary.json` | 18의 summary 재사용; 8개 기존 평균 MAE와 설정/비용 |
| [SRC-0023177](../evidence/0045-0046-input-stability/../0018-0021/originals/SRC-0023177.py.txt) | `tmp/redesign_20260925/spatial_information_diagnostic.py` | 18 코드 전체 101행 재독; 신규 전체 독해 수에 다시 넣지 않음 |
| [SRC-0031961](../evidence/0045-0046-input-stability/../0018-0021/originals/SRC-0031961.json) | `tmp/redesign_20260925/results/spatial_information/run_started.json` | 18의 cell·이웃·입력 폭·시간·seed metadata |
| [SRC-0032487](../evidence/0045-0046-input-stability/../0016-0017/originals/SRC-0032487.npz) | `tmp/redesign_20260925/results/temporal_validity/predictions.npz` | 시간 진단의 cell_ids/times/Y 중 같은 query 구간 재사용; 전체 파일 신규 독해 아님 |
| [SRC-0022700](../evidence/0045-0046-input-stability/../0642/originals/SRC-0022700.json) | `tmp/redesign_20260925/cumulative_execution_budget.json` | 현재 원장의 첫 6개 모델 호출과 46까지의 cheap prefix만 대조; 전체 원장 독해 아님 |
| SRC-0023485 | `tmp/redesign_20260925/assets/data_git_version.h5` | 이번에는 크기/해시. H012의 지정 HDF5 검수를 연결; 원본 binary 팀 접근 미완료 |

새 전체 검토로 집계하는 텍스트는 45 계획·46 코드·원장 갱신 코드 3개다. 47은 전체 문장을 읽었어도 문헌 등의 근거 검수가 남아 전체 통합으로 세지 않는다. 작은 JSON 전체 5개와 결과 JSON의 선택 수치 1개를 별도 집계한다. 큰 수치 배열의 프로그램 대조를 모든 개별 값의 수동 독해로 바꾸지 않는다.

스냅샷 manifest의 모든 행을 읽었다는 것은 연결된 32개 파일의 내용을 모두 읽었다는 뜻이 아니다. 이번 묶음에서는 포함한 계획·코드·결과·원장의 9개 해시 행과 보존 시 코드 해시를 대조했다. 나머지 문헌·그림·보고서·운영 기록은 후속 검토 범위다. 47 §7의 웹 접근·문헌 페이지 주장도 이번 수치 범위에 포함하지 않는다.

H012의 큰 JSON 출력은 이번 재독 중 일부 잘려 필요한 identity·범위·날짜 필드만 따로 읽었다. 기존 완료 검수 재사용으로 기록하며 새 전체 JSON 독해를 집계하지 않았다. 현재 누적 원장도 46 이전의 선택 필드만 사용했다. [계보 검수](../verification/history-027-lineage-check.json)에 실제 의존한 이전 검수 파일의 해시가 있다.

후속 업데이트: 위 H027 수행 시점에 대기였던 47의 문헌·입력 역할·논리·작업량·종합은 [H028 기록](../records/0047-input-sharing-roles.md)으로 검수했다. H027의 원래 수치 검수 범위는 그대로이며, 후속75와 전수 범위는 남아 있다.
