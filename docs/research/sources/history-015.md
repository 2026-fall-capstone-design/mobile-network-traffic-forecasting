# 초기 누적 비용의 출처와 읽은 범위

[15·21 비용 기록](../records/0015-0021-cumulative-costs.md)은 기존 원본28개를 재사용한다. 새 원본을 복제하지 않았으며, 모든 참조의 원본 해시·크기와 기존 보존 바이트를 다시 확인했다. [기계 판독 목록](../catalog/history-015-sources.jsonl), [manifest](../evidence/0015-0021-costs/manifest.json)에 정확한 사본 관계와 SHA256이 있다.

아래는 이번 비용 감사에서 실제로 다시 읽은 구간이다. 이전 묶음의 전문 검토와 이번의 선택 필드 대조를 구분하며 같은 파일을 새 본문 검토량으로 중복 집계하지 않는다. Python 원문은 자료로 읽었고 실행/import하지 않았다. 여섯 호출군은 모든 비용 행, RCTL은29개 fit의 식별·epoch·시간 필드를 대조했다. JSON의 나머지 성능 내용은 기존 검수 범위를 재사용한다.

| 원문 | 원본 루트 기준 경로 | 이번 읽기 범위 |
|---|---|---|
| [SRC-0023607](../evidence/0001-0002/originals/SRC-0023607.json) | `tmp/redesign_20260925/results/smoke.json` | {"entries": "저장된 모든 호출 행", "fields": ["context_rows", "query_rows", "fit_seconds", "predict_seconds"], "scope": "호출 식별·비용 필드를 재대조하고 기존 전문 검수를 재사용"} |
| [SRC-0023601](../evidence/0003-0007/originals/SRC-0023601.json) | `tmp/redesign_20260925/results/risk_table_calls.json` | {"entries": "저장된 모든 호출 행", "fields": ["context_rows", "query_rows", "fit_seconds", "predict_seconds"], "scope": "호출 식별·비용 필드를 재대조하고 기존 전문 검수를 재사용"} |
| [SRC-0023586](../evidence/0003-0007/originals/SRC-0023586.json) | `tmp/redesign_20260925/results/observed_risk_calls.json` | {"entries": "저장된 모든 호출 행", "fields": ["context_rows", "query_rows", "fit_seconds", "predict_seconds"], "scope": "호출 식별·비용 필드를 재대조하고 기존 전문 검수를 재사용"} |
| [SRC-0024836](../evidence/0013-0015/originals/SRC-0024836.json) | `tmp/redesign_20260925/results/cell_identity/calls.json` | {"entries": "저장된 모든 호출 행", "fields": ["context_rows", "query_rows", "fit_seconds", "predict_seconds"], "scope": "호출 식별·비용 필드를 재대조하고 기존 전문 검수를 재사용"} |
| [SRC-0024349](../evidence/0019-0021/originals/SRC-0024349.json) | `tmp/redesign_20260925/results/broad_cell_information/calls.json` | {"entries": "저장된 모든 호출 행", "fields": ["context_rows", "query_rows", "fit_seconds", "predict_seconds"], "scope": "호출 식별·비용 필드를 재대조하고 기존 전문 검수를 재사용"} |
| [SRC-0032380](../evidence/0019-0021/originals/SRC-0032380.json) | `tmp/redesign_20260925/results/target_parameterization/calls.json` | {"entries": "저장된 모든 호출 행", "fields": ["context_rows", "query_rows", "fit_seconds", "predict_seconds"], "scope": "호출 식별·비용 필드를 재대조하고 기존 전문 검수를 재사용"} |
| [SRC-0022703](../evidence/0001-0002/originals/SRC-0022703.py.txt) | `tmp/redesign_20260925/data_and_smoke.py` | {"lines": [[1, 61]], "scope": "과거 코드의 타이머 경계 정적 재검토; 실행·import 없음"} |
| [SRC-0023116](../evidence/0003-0007/originals/SRC-0023116.py.txt) | `tmp/redesign_20260925/risk_table_pilot.py` | {"lines": [[60, 96], [110, 122]], "scope": "과거 코드의 타이머 경계 정적 재검토; 실행·import 없음"} |
| [SRC-0022942](../evidence/0003-0007/originals/SRC-0022942.py.txt) | `tmp/redesign_20260925/observed_risk_pilot.py` | {"lines": [[1, 31], [80, 90]], "scope": "과거 코드의 타이머 경계 정적 재검토; 실행·import 없음"} |
| [SRC-0023202](../evidence/0003-0007/originals/SRC-0023202.py.txt) | `tmp/redesign_20260925/train_rctl_pilot.py` | {"lines": [[28, 143]], "scope": "과거 코드의 타이머 경계 정적 재검토; 실행·import 없음"} |
| [SRC-0022570](../evidence/0013-0015/originals/SRC-0022570.py.txt) | `tmp/redesign_20260925/cell_identity_diagnostic.py` | {"lines": [[33, 59], [67, 76]], "scope": "타이머와 비용 필드의 앞뒤3행을 포함한 선택 구간을 실제 출력하여 재열람; 전문 재독으로 세지 않음"} |
| [SRC-0023210](../evidence/0013-0015/originals/SRC-0023210.py.txt) | `tmp/redesign_20260925/upc_transfer_diagnostic.py` | {"lines": [[11, 17], [64, 82]], "scope": "타이머·비용 필드와 두 번째 대조에서 실제 열람한 선택 구간; 전문 재독으로 세지 않음"} |
| [SRC-0022531](../evidence/0019-0021/originals/SRC-0022531.py.txt) | `tmp/redesign_20260925/broad_cell_information_diagnostic.py` | {"lines": [[46, 83], [97, 110]], "scope": "타이머와 비용 필드의 앞뒤3행을 포함한 선택 구간을 실제 출력하여 재열람; 전문 재독으로 세지 않음"} |
| [SRC-0023197](../evidence/0019-0021/originals/SRC-0023197.py.txt) | `tmp/redesign_20260925/target_parameterization_diagnostic.py` | {"lines": [[32, 62], [71, 83]], "scope": "타이머와 비용 필드의 앞뒤3행을 포함한 선택 구간을 실제 출력하여 재열람; 전문 재독으로 세지 않음"} |
| [SRC-0030237](../evidence/0003-0007/originals/SRC-0030237.json) | `tmp/redesign_20260925/results/rctl_pilot/fit_results.json` | {"entries": "29개 fit 모두", "fields": ["method", "seed", "cluster", "epochs_run", "best_epoch", "fit_seconds"], "scope": "이번 재열람은 식별·비용·epoch 필드이며 다른 성능 필드 전문 재검토는 기존 H001 근거를 재사용"} |
| [SRC-0030278](../evidence/0003-0007/originals/SRC-0030278.json) | `tmp/redesign_20260925/results/rctl_pilot/run_finished.json` | {"lines": [[1, 9]], "scope": "전문"} |
| [SRC-0030279](../evidence/0003-0007/originals/SRC-0030279.json) | `tmp/redesign_20260925/results/rctl_pilot/run_started.json` | {"lines": [[1, 1]], "scope": "전문"} |
| [SRC-0020823](../evidence/0001-0002/originals/SRC-0020823.md.txt) | `tmp/redesign_20260925/02_candidate_and_pilot_plan.md` | {"lines": [[43, 56]], "scope": "이번 비용 문장 재대조 범위; 이전 전문 검토는 기존 묶음을 재사용"} |
| [SRC-0020824](../evidence/0003-0007/originals/SRC-0020824.md.txt) | `tmp/redesign_20260925/03_projection_diagnostic_plan.md` | {"lines": [[1, 13]], "scope": "이번 비용 문장 재대조 범위; 이전 전문 검토는 기존 묶음을 재사용"} |
| [SRC-0020825](../evidence/0003-0007/originals/SRC-0020825.md.txt) | `tmp/redesign_20260925/04_observed_query_risk_plan.md` | {"lines": [[35, 41]], "scope": "이번 비용 문장 재대조 범위; 이전 전문 검토는 기존 묶음을 재사용"} |
| [SRC-0020972](../evidence/0013-0015/originals/SRC-0020972.md.txt) | `tmp/redesign_20260925/15_transfer_identity_and_literature_findings.md` | {"lines": [[54, 62]], "scope": "이번 비용 문장 재대조 범위; 이전 전문 검토는 기존 묶음을 재사용"} |
| [SRC-0021095](../evidence/0018-0021/originals/SRC-0021095.md.txt) | `tmp/redesign_20260925/21_diagnostic_synthesis.md` | {"lines": [[64, 72]], "scope": "이번 비용 문장 재대조 범위; 이전 전문 검토는 기존 묶음을 재사용"} |
| [SRC-0023604](../evidence/0003-0007/originals/SRC-0023604.json) | `tmp/redesign_20260925/results/risk_table_pilot.json` | {"fields": ["total_seconds"], "scope": "비용·호출 상태의 선택 필드; 나머지 성능 본문은 이전 검수 재사용"} |
| [SRC-0023588](../evidence/0003-0007/originals/SRC-0023588.json) | `tmp/redesign_20260925/results/observed_risk_pilot.json` | {"fields": ["seconds"], "scope": "비용·호출 상태의 선택 필드; 나머지 성능 본문은 이전 검수 재사용"} |
| [SRC-0023614](../evidence/0013-0015/originals/SRC-0023614.json) | `tmp/redesign_20260925/results/upc_transfer_diagnostic.json` | {"fields": ["elapsed_seconds", "new_model_contexts", "new_model_query_rows", "new_RCTL_fits"], "scope": "비용·호출 상태의 선택 필드; 나머지 성능 본문은 이전 검수 재사용"} |
| [SRC-0024841](../evidence/0013-0015/originals/SRC-0024841.json) | `tmp/redesign_20260925/results/cell_identity/summary.json` | {"fields": ["TabICL_seconds", "simple_model_seconds", "stage_seconds"], "scope": "비용·호출 상태의 선택 필드; 나머지 성능 본문은 이전 검수 재사용"} |
| [SRC-0024354](../evidence/0019-0021/originals/SRC-0024354.json) | `tmp/redesign_20260925/results/broad_cell_information/summary.json` | {"fields": ["TabICL_seconds", "simple_model_seconds", "stage_seconds", "new_RCTL_fits"], "scope": "비용·호출 상태의 선택 필드; 나머지 성능 본문은 이전 검수 재사용"} |
| [SRC-0032385](../evidence/0019-0021/originals/SRC-0032385.json) | `tmp/redesign_20260925/results/target_parameterization/summary.json` | {"fields": ["TabICL_seconds", "simple_model_seconds", "stage_seconds", "new_RCTL_fits"], "scope": "비용·호출 상태의 선택 필드; 나머지 성능 본문은 이전 검수 재사용"} |

[기존01–02](pilot-006.md), [B1/B2/RCTL](history-001.md), [13/14](history-008.md), [19/20](history-013.md)의 보존 원문으로 직접 연결된다. 지침·상한·다음 행동이 있는 문장은 역사적 자료다. 현재 연구를 실행하라는 지시가 아니다. 전체 progress·예산 원장의 모든 사건을 읽었다고 표시하지 않았으며, 이 범위 밖 실패·재시도·후속 비용은 미확인으로 남긴다.
