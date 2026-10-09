# 18·21 공간 진단의 출처와 읽은 범위

[기록](../records/0018-0021-spatial-information.md)·[보존 근거](../evidence/0018-0021/README.md)·[manifest](../evidence/0018-0021/manifest.json)·[목록](../catalog/history-012-sources.jsonl)·[검수](../verification/history-012.md)를 연결한다. 원문 7개807,071bytes를 새로 바이트 보존하고 기존 2개를 재사용했다. 줄 번호는 해당 SHA의 UTF-8에 Python `splitlines()`를 적용한 1기준이다.

| Source ID | 원본 루트 아래 경로 | 실제 열람·검수 범위 |
|---|---|---|
| SRC-0021026 | `tmp/redesign_20260925/18_spatial_information_plan.md` | 전체 27행. 질문·고정 조건·판정·256fit 계획 |
| SRC-0021095 | `tmp/redesign_20260925/21_diagnostic_synthesis.md` | 전체 72행 열람. 이번에는 20–29행 공간 결과를 검수하고,시간 부분은H010 연결. 나머지 주장은 미완료 |
| SRC-0023177 | `tmp/redesign_20260925/spatial_information_diagnostic.py` | 전체 101행 정적 열람. 이웃·PCC·입력·모델·저장·비용. 실행/import하지 않음 |
| SRC-0031961 | `tmp/redesign_20260925/results/spatial_information/run_started.json` | 모든 JSON 키·32cell의 이웃/padding/선택/PCC값. 계획 해시와 실제 저장 조건 |
| SRC-0031960 | `tmp/redesign_20260925/results/spatial_information/run_finished.json` | 모든 3개 키. 완료fit·wall·fit/predict 보고 |
| SRC-0031962 | `tmp/redesign_20260925/results/spatial_information/summary.json` | 모든 키·Ridge/HGB 전체 집계/배열 및 나머지 상위키.60개 저장 성능 필드를 pred/y와 대조 |
| SRC-0031959 | `tmp/redesign_20260925/results/spatial_information/predictions.npz` | 모든 5개 수치 배열의 shape·유한값/ID/시간·이웃·수치. 확장 입력X는 없음 |
| SRC-0021004 | `tmp/redesign_20260925/17_temporal_validity_findings.md` | 기존 전체 26행 열람 재사용. 이번에는 26행 후속 질문 연결 |
| SRC-0032487 | `tmp/redesign_20260925/results/temporal_validity/predictions.npz` | 기존 보존 재사용. cell_ids/times/Y/pred만 읽어 같은32cell·정답·첫 주 예측을 확인 |

대용량 SRC-0023485는 `tmp/redesign_20260925/assets/data_git_version.h5`다. 전체 SHA·크기와 shape,`idx[:1008]`,자기·이웃의 고유 285개 cell에 대한`data[:1008,indices,2]`를 읽었다. 저장 정답·정규화·이웃/PCC를 대조했고 원시 CDR의 전처리 전체는 조사하지 않았다. 팀 접근의 고정 upstream 정보와 기존 보존 날짜 발췌는 manifest에 연결했다.

H5에서 재구성한 확장 입력은 실제 과거 모델 입력의 별도 저장 사본이 아니다. 이 한계와 H5별 계산 오차는 [local 검사](../verification/history-012-local-data-check.json)에 남겼다. 원 논리와 저장값의 연결을 확인했지만 원 학습을 재현하지 않았다.

기록 19·20·22는 각각31·25·22행을 읽어 후속 관계를 파악했으나 이 묶음에서 새로 보존·검수 완료 처리하지 않았다. 기록 21의 광범위 cell ID·target 표현·누적 비용·추가 문헌 판단은 남아 있다.393의 공간 정보 후속 기록은 경로 탐색만 했다. 원문 속 과거 예산·실행 명령은 현재 실행 지시가 아니다.
