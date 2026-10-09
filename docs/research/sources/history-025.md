# H025 출처와 실제 검토 범위

[기록](../records/0041-0042-cell-harm.md) · [목록](../catalog/history-025-sources.jsonl) · [바이트 식별값](../evidence/0041-0042-cell-harm/manifest.json)

41 계획과 42의 저장 산술, 44 §1–2·§6 수치 부분을 연결했다. 새 보존 7개 59,195 bytes, 기존 참조 9개다. 41 계획과 42 정적 코드, 두 텍스트를 이번 검수 완료로 세며, 44는 전체 84행을 초독했어도 문헌·종합 검수가 남은 부분 기록이다. 작은 JSON 3개 전체와 결과 JSON 1개의 선택 수치 범위를 구분한다. 결과의 schema와 모든 배열값은 검산했지만 모든 cell 숫자를 하나씩 사람이 읽었다고 쓰지 않는다.

| source_id·팀용 보존 원문 | 파일 | 읽은/검수한 범위 |
| --- | --- | --- |
| [SRC-0021529](../evidence/0041-0042-cell-harm/originals/SRC-0021529.md.txt) | 41_cell_harm_envelope_plan.md | 1–31행 전체, 코드 실행 없음 |
| [SRC-0021588](../evidence/0041-0042-cell-harm/originals/SRC-0021588.md.txt) | 44_cell_harm_and_predictor_role_findings.md | 84행 초독·전체 보존, 수치 절만 검수; §3–5/§6문헌 대기 |
| [SRC-0022569](../evidence/0041-0042-cell-harm/originals/SRC-0022569.py.txt) | cell_harm_envelope_42.py | 1–99행 전체, 코드 실행 없음 |
| [SRC-0024832](../evidence/0041-0042-cell-harm/originals/SRC-0024832.json) | result.json | 전체 key/schema·모든 수치 산술 대조; cell별 모든 값의 개별 수동독해 아님 |
| [SRC-0024833](../evidence/0041-0042-cell-harm/originals/SRC-0024833.json) | run_finished.json | 작은 JSON 전체 key·값 |
| [SRC-0024834](../evidence/0041-0042-cell-harm/originals/SRC-0024834.json) | run_started.json | 작은 JSON 전체 key·값 |
| [SRC-0024835](../evidence/0041-0042-cell-harm/originals/SRC-0024835.json) | settings.json | 작은 JSON 전체 key·값 |
| [SRC-0030211](../evidence/0041-0042-cell-harm/../0003-0007/originals/SRC-0030211.npz) | all_predictions.npz | 기존 보존본 재사용·이번 지정 입력/선택/비용 필드 |
| [SRC-0027517](../evidence/0041-0042-cell-harm/../0033-0035-frozen-fit/originals/SRC-0027517.json) | summary.json | 기존 보존본 재사용·이번 지정 입력/선택/비용 필드 |
| [SRC-0029142](../evidence/0041-0042-cell-harm/../0026-0027-observable/originals/SRC-0029142.npz) | arrays.npz | 기존 보존본 재사용·이번 지정 입력/선택/비용 필드 |
| [SRC-0027514](../evidence/0041-0042-cell-harm/../0033-0035-frozen-fit/originals/SRC-0027514.npz) | predictions.npz | 기존 보존본 재사용·이번 지정 입력/선택/비용 필드 |
| [SRC-0023577](../evidence/0041-0042-cell-harm/../0001-0002/originals/SRC-0023577.npz) | design_data.npz | 기존 보존본 재사용·이번 지정 입력/선택/비용 필드 |
| [SRC-0022700](../evidence/0041-0042-cell-harm/../0642/originals/SRC-0022700.json) | cumulative_execution_budget.json | 기존 보존본 재사용·이번 지정 입력/선택/비용 필드 |
| [SRC-0030280](../evidence/0041-0042-cell-harm/../0003-0007/originals/SRC-0030280.json) | summary.json | 기존 보존본 재사용·이번 지정 입력/선택/비용 필드 |
| [SRC-0022860](../evidence/0041-0042-cell-harm/../0033-0035-frozen-fit/originals/SRC-0022860.py.txt) | frozen_fit_gap_34.py | 기존 보존본 재사용·이번 지정 입력/선택/비용 필드 |
| [SRC-0023588](../evidence/0041-0042-cell-harm/../0003-0007/originals/SRC-0023588.json) | observed_risk_pilot.json | 기존 보존본 재사용·이번 지정 입력/선택/비용 필드 |

validation의 cell 순서는 proposal과 34 predictions의 cell_ids, design의 cell_indices를 연결했다. 저장 21개 primary checkpoint의 float32 오차 평균을 membership 위치에 배치한 값이 34 summary에 정확히 일치한다. 개발 예측은 float64로 재집계했다. 서로 다른 정밀도의 마지막 자릿수 차이를 새 예측 결과로 세지 않는다.

비용 원장은 후속 내용이 있는 전체 JSON을 새로 완료 처리하지 않는다. 초기 지정 여섯 Tab 호출군, 두 frozen stage, 42까지 이름을 명시한 15개 cheap 항목과 RCTL training wall만 읽고 더했다. exact alias는 바이트 동일 사본 관계이며 서로 다른 원문 개정본의 검토를 대체하지 않는다.

현재 원본 16개·기존 통제 파일 6개의 해시가 유지되는지 확인했다. 원문 속 명령·예산·완료 문장은 역사 자료이며 새 모델 실행의 지시가 아니다. 43의 두 논문·저자 코드, 44 §3–5 및 §6 문헌 부분, 45 이후와 전체 고유 기록은 계속 남아 있다. 이 묶음의 외부 논문 전체 검수는 0편이다.
