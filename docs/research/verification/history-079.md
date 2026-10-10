# H079 검수: 원78 회귀 전이 문헌·코드

[기록](../records/0079-regression-transferability.md) · [주장 40개와 원문 위치](history-079-claims.json) · [작성 후 대조 범위](history-079-second-pass.json) · [출처](../sources/history-079.md)

40개 주장을 작성한 뒤 같은 에이전트가 관련 원문·공식 코드·저장 metadata와 다시 대조했다. 독립 연구자의 검토나 모델 실행 재현은 아니다. 첫 독해는 PDF 23쪽 전체이며, 두 번째 검토는 주장 관련 구간·표·그림을 대상으로 한다. source import·학습·추론은 0이다.

검수에서 다음을 구별했다.

- 기대 음의 제곱오차와 MAE, 순위의 목표 정의와 일반화 하한, target head 재적합과 같은 scalar 출력 pooling.
- 코드 학습의 penalty와 반환 score의 잔차 MSE, fit 입력과 query/test 평가, 출력 차원 평균과 합.
- Pearson/Kendall/Spearman, pooled 쌍과 source별 상관, top-1과 top-k, Figure 3 적합 RMSE와 실제 test MSE.
- 전반적 개선 서술과 정규화·source별 손해, Table 1/Figure C.3 및 Table 2/4의 값 차이.
- 당시 판단과 이번 정적 관찰, 기존 결과 재인용과 독립 실험, 고정 코드 확인과 전체 환경 재현.

작성 후 Figure 2 오른쪽 가로축을 **target 표본 수**로 고쳤고, 보충 C.1의 score/gap 비율에 원문이 명시하지 않은 “평균”을 붙이지 않도록 수정했다. 하한의 대상도 음의 기대 제곱오차로 분명히 했다. 논문 원문 자체는 변경하지 않았다.

[수치 전사](../evidence/0079-regression-transferability/reported-tables.json)의 1,054개 표시값과 [그림 검토](../evidence/0079-regression-transferability/figure-scope.json)를 원문에 대조했다. 작은 표의 모든 행·열, 보충 C.5/C.6의 96개 행을 확인했으며 원시 scatter 점을 역산하지 않았다. OpenMonkey head에서 LabMSE1이 LabLogME보다 낮은 source가 17개라는 확인은 저장 표의 비교 산술이다.

[원본·사본 보존 검사](../evidence/0079-regression-transferability/provenance-check.json)와 [문서·링크 검사](history-079-document-check.json)를 별도로 제공한다. PDF2·README·score의 새 독립 본문4개, 전체JSON3개와 PNG3개를 구분하고 TXT2/재참조 findings는 독립 본문에 중복 가산하지 않는다.

남은 범위는 원78의 Task2Vec·NTKMTL·검색/접근 자료, 실제 전체 실행 환경·원시 결과, 원79 외부/원80 결과·이전 부분 검토와 이후 기록, 원자료 장기 팀 접근, 최종 원본 변경분과 대표 질문 검색 검수다. 이번 12개 그룹 검수는 전체 Goal 완료를 의미하지 않는다.
