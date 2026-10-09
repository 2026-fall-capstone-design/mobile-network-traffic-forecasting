# 범주 효과·계산 비용·시간 context: 여섯 방법 비교

[기록15의 문헌 판단](../records/0015-category-cost-time-literature.md)을 재사용하기 위한 비교다. 문헌의 관련 원리와 이번 프로젝트의 실제 성능은 다른 근거다. [검수 출처](../sources/history-009.md)의 지정 구간만 확인했고, 전체논문·저자 구현·성능 재현 완료를 뜻하지 않는다.

## 입력·추정·결정과 적용 조건

| 문헌·고정 판본 | 사용하는 정보와 대상 | 바꾸는 결정 | 이 연구에 옮기기 전에 확인할 점 |
|---|---|---|---|
| H009-P01 [Effect fusion using model-based clustering](https://arxiv.org/abs/1703.07603v1), Malsiner-Walli·Pauger·Wagner, 2017v1 | 선형 회귀의 연속Y·범주X·조정 공변량 | 범주 효과의 mixture 소속을 MCMC로 추정; modal partition 또는 posterior similarity/PAM | raw traffic cell의 거리와 범주 효과는 다름. prior·공유 분산·최종 K 선택, PAM/silhouette의 K1 제외를 명시 |
| H009-P02 [Tree-Structured Modelling of Categorical Predictors in Regression](https://arxiv.org/abs/1504.04700v1), Tutz·Berger, 2015v1 | GLM의 Y·범주X·다른 공변량, 전체 자료 | 후보 split마다 전 계수 재추정; 최소 deviance 선택, CV 또는 p-value 중단 | split 위치 유지와 계수 고정을 혼동하지 않음. 같은 자료에서 ID를 합친다는 설명을 신규성으로 삼지 않음 |
| H009-P03 [BanditPAM++: Faster k-medoids Clustering](https://proceedings.neurips.cc/paper_files/paper/2023/file/e885e5bc6e13b9dd8f80bc5482b1fa2f-Paper-Conference.pdf), Tiwari 등7명, NeurIPS2023 | 고정 reference에 대한 dissimilarity와 BUILD/SWAP 후보 손실 | 한 거리로 virtual arms를 갱신하고 reference 순열/cache 재사용 | metric일 필요는 없지만 재사용할 거리·mapping이 유지돼야 함. sub-Gaussian/gap/반복 조건, PAM local 해, TFM 준비·추론 비용 구분 |
| H009-P04 [Active Clustering](https://proceedings.mlr.press/v15/eriksson11a.html), Eriksson·Dasarathy·Singh·Nowak, AISTATS2011 | symmetric similarity와 binary hierarchy | adaptive triple 관측으로 tree 복원; 오염 시 voting/split | TC 및 오염·균형·최소 크기 조건. 실제 교차 예측 손해가 이를 충족하는지 별도 확인 |
| H009-P05 [Bounded Context Management for Tabular Foundation Models on Stream Learning](https://arxiv.org/abs/2606.18677v1), Lee·Choi·Choi·Yoo, 2026v1(CURE) | 분류 stream의 예측 후 label, 예측 시 entropy, 정규화 raw feature | short FIFO/long bank의 admission과 같은 class pair의 eviction | label 가용 시점·warm fill·class centroid fallback·국소 정보량 가정. 분류 entropy를 회귀 분산으로 치환하지 않음 |
| H009-P06 [NOMADD: Numerical Optimization of Models Adapting to Data Drift](https://arxiv.org/abs/2608.02845v1), Shah·Burghardt, 2026v1 | 과거 pooled anchor와 기간별 모델; TFM은 고정 query의 class log-probability | 공통 좌표의 SVD 궤적 외삽과 shrinkage | 매 forward-validation 위치의 earlier-only 재구성, smooth/low-dimensional drift, classification 평가. α0 후보가 미래 무손해 보장은 아님 |

H009-P03 저자는 PDF 기준 Mo Tiwari, Ryan Kang, Donghyun Lee, Sebastian Thrun, Chris Piech, Ilan Shomorony, Martin Jinye Zhang의7명이다. 전체 서지와 고정 자료의 해시는 [검수 JSON](../verification/history-009-primary-review.json)에 있다.

## 보장과 비용의 정확한 범위

Effect fusion의 두 최종 partition 규칙을 한 알고리즘으로 합치지 않는다. PAM/silhouette의 선택을 전역 최적 보장으로 읽지 않는다. Tree-Structured의 ‘전체 자료 사용’은 매 단계 이전 추정치를 그대로 둔다는 의미가 아니다. PDF7은 이전 split 위치를 유지하면서 모든 파라미터를 다시 추정한다고 설명한다.

BanditPAM++의 SPIMAB 설정은 공통 reference와 시간 불변 거리, 그 거리 및 행동으로부터 손실을 계산하는 알려진 함수를 둔다. 후보 간 gap과 sub-Gaussian scale의 조건, SWAP 반복 상한 `T` 및 숨은 `c(k)`가 계산량 주장의 범위를 정한다. 예측 context를 바꿀 때 같은 거리 값을 쓸 수 있는지는 TFM 적용에서 새로 확인할 질문이다. [당시 인용 HTMLv1](https://arxiv.org/html/2310.18844v1)은 지정 §3–5·7만 읽었고, NeurIPS PDF와 모든 내용을 동일하다고 처리하지 않았다.

Active의 exact recovery는 TC하의 binary tree를 대상으로 한다. Robust 결과에서는 independent corruption, Theorem4.1의 A1/A2, threshold γ와 balance η 조건이 필요하다. RAcluster는 크기≤2m에서 재귀를 멈추며, Theorem4.2는 크기>2m인 cluster의 복원을 다룬다. 비교 수를 줄인다는 일반 설명만으로 임의 교차 손해나 유한 RCTL의 비용 보장을 얻을 수 없다.

아래는 Active PDF4 Table1의 **논문 보고값**이다. 네 행을 모두 보존하고 원문 비율과 별도 산술을 나눴다. 우리 실험이나 원 simulation 재현은 아니다.

| N | n_agg | n_outlier | 원문 비율 % | count로 계산한 비율 % |
|---:|---:|---:|---:|---:|
| 128 | 8128 | 876 | 10.78 | 10.77756 |
| 256 | 32640 | 2206 | 6.21 | 6.75858 |
| 512 | 130816 | 4561 | 3.49 | 3.48658 |
| 768 | 294528 | 8490 | 2.88 | 2.88258 |

N256의 인쇄 비율이 맞지 않는 이유는 미확인이다. 원자료의 어느 값도 정정하지 않았다. [보고표와 산술](../evidence/0015-literature/paper-reported-tables.json), [미해결 항목 H009-I03](../records/0015-category-cost-time-literature.md).

CURE의 normalized class entropy는 label 관측 이전에 계산하지만, 이후 context에는 관측한 label을 넣는다. Appendix A의 하한에서 δ·ε·지역 질량 α를 지우면 정보량 해석이 달라진다. 최근 centroid는 우선 같은 class를 기준으로 하며 없을 때 전체 short bank로 대체한다. Table6의 total은 세 구성시간의 합이다. [CURE 시간표](../records/0015-category-cost-time-literature.md)를 우리 CPU/RCTL 시간으로 재인용하지 않는다.

NOMADD는 내부 validation의 binary AUC/multiclass accuracy와 보고 OVR macro AUC가 다르다. Forward validation의 rank·damping·ridge·shrinkage 선택은 각 시점에서 이전 자료만 사용하며 마지막 V=3 위치를 이용한다. 위치가2개 미만이면 α를0.25 이하로 제한한다. Pooled anchor와 domain-index-feature frozen baseline은 다른 비교군이다. §3.4의 SVD 좌표 표현과 tree 서술의 공백은 [H009-I02·I04](../records/0015-category-cost-time-literature.md)에 남겼다.

## 새 설계에서 먼저 적을 차이

| 다시 검토하는 방향 | 기존 기록에서 재사용할 근거 | 새 실험이 답해야 할 질문 |
|---|---|---|
| cell ID 병합 | 14의 동일 자료/ID 대조, Effect fusion·Tree-Structured의 효과/분할 원리 | ID 수준의 변경 외에 어떤 추정·선택 결정을 개선하고, 어떤 조건의 최종 learner가 이득을 얻는가 |
| 적응적 비교·cache | Bandit의 공유 거리 조건, Active의 TC/오염 조건, 실제 TFM 준비·query 비용 구분 | 재사용하는 값이 동일한가, 중단 오차와 context 변화 비용을 어떻게 반영하는가 |
| 시간 context·예측장 drift | CURE의 label 시점/정보량 조건, NOMADD의 공통 좌표/forward validation | 회귀 traffic에서 남은 시간 유효성 문제가 무엇이며 단순 시간 특징과 비교해 어떤 결정을 추가하는가 |

이 항목은 정리된 과거 판단을 재사용하는 안내다. 후보 채택이나 새 실행 계획으로 승인된 문서는 아니다. [15 기록](../records/0015-category-cost-time-literature.md)·[과거 시도 색인](../prior-attempts.md)으로 돌아간다.
