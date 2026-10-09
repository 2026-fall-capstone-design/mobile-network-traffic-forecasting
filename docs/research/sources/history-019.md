# H019 출처와 열람 범위

[26·27 기록](../records/0026-0027-observable-states.md)의 원본 8개와 기존 2개, H5 metadata 1건을 [목록](../catalog/history-019-sources.jsonl)·[manifest](../evidence/0026-0027-observable/manifest.json)에 연결했다. 보존용 md/py는 `.txt`를 덧붙였으며 바이트는 원본과 같다. 과거 명령·Goal·한도는 역사적 자료다.

| source_id | 역할·읽은 범위 |
|---|---|
| SRC-0021210 | 26 계획 전체 1–38행 |
| SRC-0021235 | 27 결과 전체 1–59행 |
| SRC-0022935 | 코드 전체 1–129행 정적 열람; 실행/import 없음 |
| SRC-0029143·0029144·0029145 | finish/start/settings 전체 키 |
| SRC-0029142 | 21개 배열 필드의 shape/dtype·값에 선언한 검사 적용. 모든 숫자의 수동 열람은 아님 |
| SRC-0029146 | 전체 top-level 키·19개 상태 support·247개 method 행의 전 필드 산술 검사. 수동으로 13개 방법 주표/선택 비교/cell 반례를 열람 |
| SRC-0030211 | 기존 all_predictions의 8개 예측·y·cell IDs·scale이 정확히 재사용됐는지 대조 |
| SRC-0021188 | 이전 25의 §4 판단 경계; H018 열람·검수 재사용 |
| SRC-0023485 | H5 파일 identity와 data.shape/idx/고정 16개 cell의 internet 열; 원본 전체 분석 아님 |

수치 검사는 학습·추론 없이 저장 TRAIN 요약의 선형 분위수, 세 요약의 상태/9개 교차 상태, MAE·under/over·기여도·기간 절반·cell 차이·episode를 대조했다. summary 전체 필드를 계산으로 확인한 것과 모든 큰 배열을 사람이 읽은 것은 구분한다. [주장별 위치·한계](../verification/history-019-primary-review.json)를 함께 본다.

단순 모델 학습에 사용한 전체 X와 fit 객체·당시 패키지 버전은 이 결과 묶음에 없다. H5로 저장 상태 요약을 대조했지만 그것만으로 역사적 fit의 독립 재현을 완료했다고 하지 않는다. 원본·연구 상태를 변경하지 않았다.
