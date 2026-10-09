# 조건부 공유 비용의 출처와 읽은 범위

[23·25 정리 기록](../records/0023-0025-conditional-pooling.md)은 새 원본9개(651,213bytes)와 기존 보존6개를 사용한다. 새 보존물은 원본 바이트 그대로이며 코드·Markdown의 확장자는 자료임을 드러내기 위해 `.py.txt`·`.md.txt`로 표시했다. [manifest](../evidence/0023-0025-pooling/manifest.json)와 [기계 판독 목록](../catalog/history-016-sources.jsonl)에 정확한 원경로·해시·동일 사본·읽은 구간이 있다. 아래 경로는 원본 루트 별칭 `Tab-ICL` 기준이다.

| 출처 | 원본 경로 | 실제 읽기·검수 범위 |
|---|---|---|
| [SRC-0021137](../evidence/0023-0025-pooling/originals/SRC-0021137.md.txt) | `tmp/redesign_20260925/23_conditional_pooling_cost_plan.md` | 계획43행 전체. 질문·식·toy·개발 자료·고정 비교·비용 상한 |
| [SRC-0021188](../evidence/0023-0025-pooling/originals/SRC-0021188.md.txt) | `tmp/redesign_20260925/25_pooling_and_horizon_findings.md` | 61행 전체 열람. 주장 검수는 §1의1–17행과 조건부 비용의 판단 경계; §2/§3는 대기 |
| [SRC-0022693](../evidence/0023-0025-pooling/originals/SRC-0022693.py.txt) | `tmp/redesign_20260925/conditional_pooling_cost_diagnostic.py` | 수정 코드163행 전체 정적 검토. 원 코드 실행·import 없음 |
| [SRC-0025173](../evidence/0023-0025-pooling/originals/SRC-0025173.npz) | `tmp/redesign_20260925/results/conditional_pooling_cost/arrays.npz` | 114개 저장 배열 전체의 형태·유한성·집계. Tab36조건 최적성과 입력 연결; KNN/density 생성은 미재현 |
| [SRC-0025174](../evidence/0023-0025-pooling/originals/SRC-0025174.json) | `tmp/redesign_20260925/results/conditional_pooling_cost/numeric_fix_resumed.json` | 9행 전체. 실패 exit·시간 보고와 코드 해시; 원 실패 콘솔 증거와 구분 |
| [SRC-0025175](../evidence/0023-0025-pooling/originals/SRC-0025175.json) | `tmp/redesign_20260925/results/conditional_pooling_cost/run_finished.json` | 4행 전체. 완료 시간·모델 호출 수 |
| [SRC-0025176](../evidence/0023-0025-pooling/originals/SRC-0025176.json) | `tmp/redesign_20260925/results/conditional_pooling_cost/run_started.json` | 16필드 및 배열 전체. context/query·고정 소속·설정 사본 |
| [SRC-0025177](../evidence/0023-0025-pooling/originals/SRC-0025177.json) | `tmp/redesign_20260925/results/conditional_pooling_cost/scores_before_outcome_comparison.json` | 전체 settings와54행. start/summary 사본 및 frozen 해시 대조 |
| [SRC-0025178](../evidence/0023-0025-pooling/originals/SRC-0025178.json) | `tmp/redesign_20260925/results/conditional_pooling_cost/summary.json` | 전체 필드,54개 결과행과9개 순위행. toy·시간·한계 포함 |
| [SRC-0022703](../evidence/0023-0025-pooling/../0001-0002/originals/SRC-0022703.py.txt) | `tmp/redesign_20260925/data_and_smoke.py` | 1–34행 정적 재대조. 정규화·16특징·저장 방식; 기존 전문 검수 재사용 |
| [SRC-0023577](../evidence/0023-0025-pooling/../0001-0002/originals/SRC-0023577.npz) | `tmp/redesign_20260925/results/design_data.npz` | raw/scales/X/Y/cell_indices/times 및 dates의 시각 문자열. 선택16cell×840시점의16특징; 객체 역직렬화 없음 |
| [SRC-0023116](../evidence/0023-0025-pooling/../0003-0007/originals/SRC-0023116.py.txt) | `tmp/redesign_20260925/risk_table_pilot.py` | 60–89행 정적 재대조. cell 선택·rint query·129격자·저장 예측 |
| [SRC-0023605](../evidence/0023-0025-pooling/../0003-0007/originals/SRC-0023605.npz) | `tmp/redesign_20260925/results/risk_table_predictions.npz` | selected_cells/cell_ids/context_times/query_times/quantiles/median. 앞64anchor 제외·혼합 최적성 |
| [SRC-0030238](../evidence/0023-0025-pooling/../0003-0007/originals/SRC-0030238.json) | `tmp/redesign_20260925/results/rctl_pilot/frozen_settings.json` | 전체 JSON·29개 task 재열람. primary21task의6소속·기간 연결 |
| [SRC-0030280](../evidence/0023-0025-pooling/../0003-0007/originals/SRC-0030280.json) | `tmp/redesign_20260925/results/rctl_pilot/summary.json` | metrics의method/seed/mean_scaled_mae 선택. seed20260925의6평균 순위; 나머지는 기존 H001 검수 재사용 |

이번의 새 본문 검토는 텍스트3개, 전체 구조·값을 읽은 JSON5개, 신규 배열 파일1개로 구분한다. 기존 출처6개를 다시 본 것은 새 고유 본문 수로 더하지 않는다. 25 전체 열람을 전체 주장 검수로 바꾸지 않으며, 별도로 읽은24 계획도 이번 공개 묶음의 완료량에 넣지 않는다.

시각은 객체형 `dates.npy`의 pickle 명령을 실행하지 않고 문자열 리터럴만 추출했다. 시간별1,008개 문자열의 개수·고유성·간격을 대조했다. 수치 NPZ는 `allow_pickle=False`로 읽었다. 현재의 검산 스크립트만 실행했고 과거 진단 코드는 실행/import하지 않았다.

[주장별 위치와 한계](../verification/history-016-primary-review.json), [저장 수치 대조](../verification/history-016-pooling-check.json), [의도적으로 잘못 만든 사본의 거부 검사](../verification/history-016-negative-check.json)로 이어진다. 24·25 후반·문헌·최초 실패 콘솔과 후속515/521/524의 전체 연결은 미완료다. 원문 속 실행 명령·Goal·예산은 역사적 자료다.
