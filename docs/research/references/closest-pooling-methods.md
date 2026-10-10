# 05의 가까운 선행: 무엇을 묶고 어떤 손실을 계산하는가

[05 부분 정리](../records/0005-closest-methods-audit.md)의 다섯 방법 비교다. 지정 절을 읽은 결과이며 전체 논문 재현이나 신규성 전수 조사에 해당하지 않는다. [원문 판본·해시·실제 열람 범위](../sources/history-003.md).

| 선행과 확인 위치 | 정보·소속 결정 | 적용 범위와 현재 후보의 차이 |
|---|---|---|
| López-Oriona·Sun·Vilar, **HCP**, *Improving the prediction accuracy of statistical models: A new hierarchical clustering approach*, Statistics and Computing35:168(2025). §1.1,§2.3 식7–8·S0–S2·Theorems1–2. [공식 원문](https://link.springer.com/article/10.1007/s11222-025-10683-x) | 알려진 집단마다 train/validation을 두고 separate/pool 모델을 실제 적합한다. 양의 validation gain이 가장 큰 쌍을 합치며 개선이 없으면 종료한다. | A2/A3의 집단 내 iid·집단 간 독립이 필요하다. Theorem2의 O(N³p²t)는 OLS/RMSE·동일 train크기t·validation v<t·N−1병합·한 pool이 계속 자라는 조건이다. 선택한 validation 최소값은 별도 test 성능이 아니며 greedy 감소를 전역 최적성으로 해석하지 않는다. |
| Sadeghkhani, **Population-HCP**, *Prediction-guided hierarchical clustering for population-level regression*, IJDSA22:223(2026). §2.3 식2.9–2.13,§3,§4 fitting,§5·§6. [공식 원문](https://link.springer.com/article/10.1007/s41060-026-01197-4) | formal objective는 검증 posterior predictive log loss다. 후보 group을 공동 적합해 separate보다 나아질 때 병합한다. Gaussian/mixed 실험은 OLS/logistic plug-in이며 소속 확정 후 train+validation으로 재적합한다. | 실제 결과는 global보다 유리하되 local 대비 이득은 제한적이고 Gapminder에서는 악화된다. fully Bayesian partition uncertainty는 후속 과제다. 원문 내부의 이전 HCP 대상 설명 및 random split 최저 모델 서술 불일치는 [05 기록](../records/0005-closest-methods-audit.md)에 보존했다. |
| Emami·Hernández-Lobato·Martínez-Muñoz, **RMB-CLE**, *Robust multi-task boosting using clustering and local ensembling*, arXiv2602.14231v1(2026-02-15). §3.1–3.3.1·Algorithm1·AppendixA.1. [공식 v1](https://arxiv.org/html/2602.14231v1) | 식5의 교차오차 → 역수 affinity profile → cosine distance → average linkage. 식10–11의 silhouette로 K를 고르고, 식13의 cluster별 모델에는 task ID도 넣는다. | 회귀 위험은 대상 task 입력분포에서 함수 불일치와 noise를 함께 포함한다. 모든 task 쌍을 평가하는 규모와 실제 wall-time은 다르다. A.1은 별도 holdout residual 벡터 비교를 채택하지 않은 이유를 설명한 절이며, 그것을 모든 validation의 불필요성으로 확대하지 않는다. |
| Ayman·Mukhopadhyay·Laszka, **ETAP**, *Ensemble Prediction of Task Affinity for Efficient Multi-Task Learning*, arXiv2602.18591v1(2026-02-20), 보존 PDF의 ICLR2026 표기. §2,§3.1,§3.2.1–3.2.3. [공식 v1](https://arxiv.org/html/2602.18591v1) | 전체 task 공동 모델의 공유 parameter gradient로 affinity를 얻는다. 실제 group 학습 gain으로 B-spline mapping과 task multi-hot 기반 ridge 잔차를 학습한다. 예산 B 안에서 task를 cover하는 group을 선택한다. | gradient proxy의 scale·고차 상호작용 한계를 실제 gain으로 보정한다. 최종 learner 정보를 쓰므로 RCTL 독립 후보의 직접 대체가 아니다. group cover 문제와 현재의 균등 크기 disjoint partition도 구분해야 한다. |
| Bolfarine·Lopes·Carvalho, **posterior projection**, *Lower-dimensional posterior density and cluster summaries for overparameterized Bayesian models*, Statistics and Computing36:107(2026-03-15). §2 식3–5,§3 식13–15,§4 식16–28. [공식 원문](https://link.springer.com/article/10.1007/s11222-026-10859-z) | 유연한 reference posterior predictive의 기대 손실로 단순 density summary를 구한다. predictive sample에 k-means를 적합하고 원 관측을 centroid에 배정하며, posterior별 투영으로 소속 불확실성을 요약한다. | reference 분포·surrogate·loss를 선택하는 결정 원리가 선행이다. 하나의 밀도 및 관측 allocation 요약을 여러 cell의 조건부 회귀 공유와 동일시하지 않는다. 기대 손실의 최적 point estimate와 posterior별 최적화의 평균도 일반적으로 다르다. |

05의 RMB-CLE 비교 근거는 확보한 arXiv v1이다. 현재 abs의 journal 관련 DOI가 있어도 출판본과의 동일성을 확인한 것으로 표시하지 않는다. 당시 미래 권호를 별도 실험 증거로 세지 않았다는 원문 판단도 유지한다.

현재 후보는 cell별 비용표를 한 번 만든 뒤 덧셈·최소값으로 공유 보정을 비교한다. 이 계산 절약은 **문제를 바꾼 결과**다. pooled learner gain이나 cross-error matrix와의 동등 정확도, ETAP 수준의 실제 gain 정보, RCTL MAE 개선은 별도 검증 대상이다. [B2의 실제 기각 결과](../records/0004-0007-b2-observed-risk.md)와 [08·09의 유한 표본 한계](../records/0008-0009-finite-sample-pooling.md)를 함께 확인한다.

## 72에서 추가 검토한 모델 기반 군집화

[Globalization의 H071 대조](../records/0072-globalization-audit.md)는 위05의 다섯 방법과 별도로 확인한 후속 문헌이다. 이 논문의 두 방법은 소속에 사용하는 학습 정보와 군집 단위가 다르다.

| 방법 | 먼저 필요한 정보 | 군집 단위·재사용 조건 |
|---|---|---|
| Model-based whole TSC | 각 series의 local 예측기 계수 | series를 K-means로 묶고 군집별 pooled model을 적합. 최종 RCTL계수를 쓰면 RCTL 독립 소속 조건과 충돌 |
| Weighted instance TSC | pooled global 예측기의 feature 중요도 | sample 간 가중거리의 M×M행렬로 군집화. cell소속으로 옮기는 정의·θ의 부호 처리·새 query배정·실제 비용은 별도 확인 |

평균 nMAE의 개선과 최대 MAPE·월별 피크의 반례를 함께 읽어야 한다. 같은 논문의 local200/global1000 trees, 목표 시각 t+1의 예보 입력 가정도 비교 조건이다. [KBS 판본 확인](../sources/history-071.md)은 서지·미리보기 범위이며 출판본 전체 방법 대조와 구분한다.

## 73에서 검토한 예측 가능한 출력 표현

[H072의 원문·구현 대조](../records/0073-forecastable-output-audit.md)는 다음 세 계열의 목적과 정보 의존을 구분한다.

| 계열 | 사용하는 정보·목적 | 현재 연구에 옮길 때 확인할 조건 |
|---|---|---|
| ForeCA | whitening한 다변량 시계열의 스펙트럼 엔트로피를 줄이는 선형 방향 | 특정 horizon·관측 X·최종 예측 손실을 직접 최적화하지 않는다. 연속 밀도와 이산 질량의 정규화·순차 추출·초기화를 구분 |
| mbrdr response DR | 조건부 평균 보존을 위한 출력 부분공간; yc/prr/pfrr/upfrr의 가정·추정량이 다름 | choose.fx의 표준화/원 X 분기, rank 조건, stats·evalues·검정 자유도를 구분. 설명분산 비율이나 자동 차원 선택으로 재사용하지 않음 |
| GNN의 static assignment | 공유 학습 파라미터 S로 pool/lift하며 예측 손실·군집 regularizer를 공동 최적화 | 최종 RCTL 독립 소속과 다름. 전체 N 인코더 비용·split 이전 adjacency·최소 CLI의 고정 MinCut·미실행 반환 경로를 확인 |

2024 MBRDR 본문은 이번에 확보했으나 GNN/2008 원논문 전체와 원실험·비용은 미확인이다. 문헌의 오류 가능성과 정적 코드 차이를 해당 연구 전체의 과학적 실패로 확대하지 않는다.

## 저장 검색에서 비슷한 이름으로 발견된 다른 역할

[H073](../records/0072-0075-saved-search-audit.md)은 context 선택·입력 변수 축소·cell 소속·출력 복원·설명 지표를 구분한다. GFSM의 입력 중복 조절, ScaleMoR의 공유 expert, COSA의 출력 adapter, SHAP/fippy의 특징 기여는 같은 소속 수정 알고리즘이 아니다. TabICL을 참고문헌에 넣었거나 패키지 모델 목록과 군집 기능을 한 페이지에 실었다는 사실도 직접 구현 근거가 되지 않는다. 세부 단서는 [159응답의 출처·역할](../evidence/0072-0075-saved-search/response-ledger.json)에 연결했다.

## 76–79에서 검토한 학습 연결의 차이

[판단 기록](../records/0076-0079-learning-decisions.md): Sobolev/Jacobian/TabDistill은 반응·상호작용 전달, DLM은 소속과 모델의 공동 추정, DynaSTar는 graph와 forecast의 공동학습, Liu는 예측 후 자원 배분을 다룬다. Task2Vec/회귀 전이는 task head를 허용하며 NTKMTL은 학습 중 균형을 조절한다. FMCL/EMD는 표현·통신·local 학습 조건을 비교해야 한다. 이는 당시 검토 기록의 분류이며 저장 일차본문의 후속 검수를 마친 것으로 표시하지 않는다. FedCAP 학술지 정정과 전문 미확보 범위도 함께 본다.

## 반응 전달의 직접 원문 대조

[세 논문 비교](0076-response-transfer.md)와 [76의 상세 검수](../records/0076-response-transfer-audit.md)에서 Sobolev·Jacobian·TabDistill의 저장 원문을 확인했다. Jacobian의 자료량별 결과 반전과 TabDistill의 F1·variance 예외, 자기 기준 overlap, Fiat 표의 설명 차이를 함께 읽는다. 위의 77–79 문헌까지 검수를 완료했다는 의미는 아니다.

[TabDistill 상호작용 표](../records/0076-tabdistill-interaction-audit.md)는 삭제 patch에 남은 27개 PMLB CSV를 보완한다. 항 수 증가가 항상 유리하지 않고 MAE·MSE의 비교 방향이 달라질 수 있다. 원 상호작용 표의 조건과 그 목록을 읽어 다시 학습하는 후속 코드의 조건을 구별한다.


## 77의 동적 소속 근거

[77 DLM의 직접 대조](../records/0077-dynamic-membership-dlm.md)에서 시간별 확률·EDP·전체구간 smoothing을 확인했다. 이는 시간적 안정화의 선행 사례이며 RCTL 학습 자료 partition의 우위까지 입증하지 않는다. 같은 고정코드의 정적 차이는 별도 조건으로 보존한다. [H078의 두 논문 대조](../records/0078-dynamic-graphs-load-balancing.md)에서 DynaSTar의 예측기 내부 관계와 Liu의 예측 후 참여 셀 군집을 보완했다. 도로 MAE, 통신 예측 오차, RL 복합 보상과 UPC 공유 이득을 서로 대체하지 않는다.

## 회귀 전이의 직접 원문·코드 대조

[H079](../records/0079-regression-transferability.md)에서 Nguyen 등의 UAI2023 본문·보충자료23쪽과고정score를 확인했다. 이론은 target head 재적합과 iid·bounded ReLU 조건을 사용한다. 높은 전이 점수는 같은 scalar target pooling의 충분조건이 아니며, code의반환잔차와논문의regularized objective도구분한다. Task2Vec·NTKMTL의후속본문검수는별도로계속한다.
