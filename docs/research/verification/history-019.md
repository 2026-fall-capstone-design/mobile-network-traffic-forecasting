# H019 검수 · 26·27 관측 가능한 상태별 손해

[14개 주장과 원문 위치](history-019-primary-review.json), [저장 검산](history-019-state-check.json), [H5 대조](history-019-H5-check.json), [오류 사본 검사](history-019-negative-check.json), [문서 검사](history-019-document-check.json)를 연결한다.

19개 상태×13개 방법=247개 결과 행의 조건부 micro/macro·cell 값·앞뒤 기간·기여도·under/over와 모든 상태 support를 저장물에서 대조했다. 자동 수치 검사 13,525개, 의미 오류 사본 14개 거부, 원 H5 지정 slice 검사 28개를 수행했다. 이는 학습·성능 실험의 재현이 아니다. 새 모델 실행은 0회다.

원본 26 계획 38행/27 결과 59행/코드 129행과 start/finish/settings 전체 키를 읽었다. 큰 summary와 NPZ의 선언한 필드는 자동 산술 대조했으며, 전체 숫자를 수동으로 읽었다고 표시하지 않았다. 주표·급증 empirical/희소 Tab/HGB의 기간 및 cell 손해·비용을 따로 대조했다. [읽은 범위](../sources/history-019.md)와 [연구 기록](../records/0026-0027-observable-states.md)을 함께 본다.

H5의 scale·상태 요약·3개 naive는 정확히 일치하고, 저장된 float32 y와 H5 double 값은 최대 1.17470539074e-7 차이였다. 실제 fit X·Ridge/HGB 객체·당시 runtime은 이 결과 묶음에 보존되지 않아 독립 적합 재현은 미완료다. 같은 정리 에이전트의 2차 대조와 기계 검사를 독립 연구자의 검증으로 표현하지 않는다.
