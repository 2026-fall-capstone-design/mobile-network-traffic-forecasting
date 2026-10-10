# 회귀 전이 근거 묶음

[해석과 재검토 조건](../../records/0079-regression-transferability.md) · [출처](../../sources/history-079.md) · [작성 후 검수](../../verification/history-079.md)

이 묶음은 원78에서 검토했던 회귀 전이 점수의 논문·보충자료·고정 코드와 실제 판단을 연결한다. 논문의 새로운 실행 결과를 만든 것이 아니다.

- [Manifest](manifest.json): 12개 새 검토 그룹과 당시 판단 원문 1개의 경로·SHA·독해 범위.
- [수치 전사](reported-tables.json): 본문 Table 1–4, 보충 Table C.1–C.6의 1,038개 값 및 Figure 2 왼쪽 평균/±16개 값. 총 1,054는 이 범위의 표시값 수이며 λ 머리글·분모·다른 그림 수치를 포함하지 않는다.
- [그림 검토](figure-scope.json): Figure C.1–C.9의 72개 subplot 상관/p 표시, 본문 그림의 해석 범위와 미복구 원시 좌표. 표와 다른 인쇄값을 그대로 보존한다.
- [TXT 대응](text-variant-correspondence.json): 본문 12쪽 layout와 보충 11쪽 plain 추출의 전쪽 대응.
- [코드·판본](static-code-version-check.json): source 실행 없이 Git blob/tree와 저장 metadata를 검증하고 보조 API 문서의 범위를 명시한다.
- [원본 보존](provenance-check.json): 등록 사본과 보호 원본의 해시 확인.

표의 열 순서는 label 기반 4개 뒤 feature 기반 4개다. 보충 scatter 그림은 feature 기반 4개가 먼저 나오므로 `columns`를 따라 읽는다. Table C.5/C.6은 source별 조건부 상관이며 Table 2의 pooled 상관과 다르다. 전사에서 원자료의 굵게·별표 표시를 새 통계적 유의성으로 변환하지 않았다.

논문 목적함수의 penalty와 공식 코드의 반환값, MSE의 출력 합/평균, 상관과 source top-k 선택률, Figure 3의 직선 적합 RMSE와 target test MSE를 각각 구분한다. 원문 표기 차이의 원인, 실제 학습 코드·환경과 원시 점, 장기 공용 원자료 보존은 남은 확인 항목이다.
