# TabICL 관련 여섯 방법의 정보·결정·적용 한계

[05의 문헌 판단](../records/0005-related-foundations-audit.md)을 지원하는 비교다. 아래 원문은 지정 판본의 일부 방법·표·수식만 검토했다. 전논문·저자 코드 검증이나 전수 신규성 조사가 아니다. 각 주장의 위치와 미검토 구간은 [검토 원장](../verification/history-006-primary-review.json)에 있다.

## 1 Localized TabICLv2

Beimnet Bekele Guta, *Localized TabICLv2: Scaling Tabular In-Context Learning through k-NN*, [2608.16429v1, 2026-08-17](https://arxiv.org/abs/2608.16429v1). §3–5, Table1/2, AppendixA의 지정 부분을 확인했다.

같은 training context에서 classifier의 `kv_cache='repr'`로 Stage1/2 표현을 만든다. query 표현과 training row 표현의 cosine similarity로 top-k를 찾고 Stage3에 국소 context를 넣는다. full/local 비교의 앞단 cache가 같다는 것은 그 비교의 조건이다. 서로 다른 cell 자료에서 생성한 표현을 같은 좌표계의 거리나 교환 가능한 cache로 보장한 것이 아니다.

Stage1은 고정하지만 Stage2/3는 합성 `mix_scm` 자료로 미세조정한다. 주요 평가는38개 분류 자료, 80/20층화 분할, 3seeds, k32, A100 조건이다. 회귀는 future work로 남긴다. Table1의 미세조정 전8개 자료는 다음처럼 별도 보존했다.

| k | 정확도 보존(%) | 평균 predict초 | 평균 speedup | 중앙 speedup |
|---:|---:|---:|---:|---:|
| 16 | 96.93 | 6.72 | 2.77 | 3.04 |
| 32 | 97.57 | 9.19 | 1.97 | 2.14 |
| 64 | 98.40 | 15.61 | 1.14 | 1.11 |
| 128 | 98.90 | 27.22 | 0.66 | 0.66 |

이는 논문 보고값이며 우리 실행시간이 아니다. AppendixA는 shared Stage1/2, retrieval, 여러 작은 Stage3 호출의 overhead를 구분한다. Stage3만의 `O(N_train² + N_train N_test)`와 `O(N_test k²)` 비교를 전체 wall-time의 보장으로 읽지 않는다. Table2의 분류 결과도 [별도 보고 행](../evidence/0005-related/paper-reported-tables.json)에 보존했으며 회귀 효과로 전환하지 않았다.

## 2 TL-ANDI

Yijun Lin·Sai Li, *Context-Constrained Transfer Learning for Tabular Foundation Models via Data Distillation*, [2607.04809v1, 2026-07-06](https://arxiv.org/abs/2607.04809v1). §1.1, §2, §3의 명시 가정·정리, §4 시작부를 확인했다.

source/target의 X와 Y, test의 X를 사용할 수 있는 설정이다. source 라벨을 kernel 평균으로 만든 `y_tilde_i(h)`와 target calibration으로 적합한 pilot의 source 위치 예측을 비교한다. §2.2 식3의 anchor 비용은 다음 두 항의 합이다.

`c(j,i) = ||x_test_j - x_source_i||² + lambda × (y_tilde_i(h) - f_target(x_source_i))²`

예산 내 anchor 집합 S가 test 입력을 덮도록 `mean_j min_(i in S) c(j,i)`를 줄이는 source 점을 greedy로 선택한다. 식5의 수송 표현은 test 행의 질량을 선택된 source anchor에 배정한다. source별 동일 질량이나 용량 제약이 추가로 있다고 해석하지 않는다. 선택한 source의 실제 라벨은 kernel-smoothed 의사 라벨로 바뀐다. source 예측에 target calibration의 잔차 예측을 더하는 Algorithm1을 적용한다.

Algorithm2는 target을 calibration과 독립 validation으로 나누고 `(h, lambda)` 후보와 target-only를 비교한다. Theorem3.2가 진술하는 허용 오차는 다음과 같다. M은 transfer 후보 수이며 target-only를 더한 총 후보 수는 M+1이다.

`R(selected) <= R(target-only) + 2 B_n sqrt(log(2(M+1)/delta) / (2 n_val))`

논문은 Assumption1과 bounded validation squared loss를 명시하고 확률 `1-delta`의 정리로 제시한다. §3.1의 별도 context-quality 결과는 source 밀도·smoothness·kernel·target Lipschitz/pilot 정확도·anchor 최적화 오차 등도 포함한다. 이번 검토는 이 명시 조건과 식을 대조한 것이며 증명 전체의 독립 검증은 아니다. 시계열 의존성, validation 선택 오차, 선택 후 full-target refit을 생략한 무조건 비악화 보장으로 인용하지 않는다.

§4는 선택 후 전체 target으로 다시 적합한 실험을 보고한다. 회귀 시뮬레이션의 MSE는 관측 noisy Y가 아닌 true conditional mean에 대한 오차다. 서비스의 `(n_train+n_test)×p<=100000` 제한도 인용된 서비스 조건이며 모든 TFM의 보편 한계가 아니다.

## 3 CRUMB

Jamie Heredge 외, *CRUMB: Efficient Prior Fitted Network Inference via Distributionally Matched Context Batching*, [2606.11473v1, 2026-06-09](https://arxiv.org/abs/2606.11473v1). §3–5.2, Algorithm1, 식2–3과 Tables1/2를 확인했다.

test query의 표준화된 X를 k-means로 묶는다. 각 query cluster에 대해 Gaussian RBF kernel의 MMD를 greedy kernel herding으로 줄이는 train subset을 고른다. 선택된 점 사이의 중복성에 벌점을 주고 query cluster와의 근접성을 보상한다. 이 식은 X를 쓰며 test Y를 요구하지 않는다. 선택된 train Y는 실제 PFN context에 제공한다. 서로 다른 subset은 같은 train 점을 재사용할 수 있다.

각 query cluster가 같은 context를 공유하여 K번의 배치 추론을 한다. 이는 cell들의 고정·배타적 소속을 고르거나, 서로 다른 cell에서 만든 내부 cache를 교환하는 결정과 다르다. weights를 바꾸지 않는 비교이며 MICP 대조에서도 CAPFN fine-tuning을 제외했다. 가속 변형에는 top-B 선택·RFF와 MMD 기반 조기종료가 있으므로 단순한 정확 greedy 계산과 비용을 구분해야 한다.

| Table1 방법 | 평균 순위(낮을수록 좋음) | 보고 ± | context | 호출 수 |
|---|---:|---:|---|---|
| Full Context | 2.202 | 0.098 | N | 1 |
| per-query kNN | 2.782 | 0.107 | 0.1N | T |
| CRUMB | 2.975 | 0.096 | 0.1N | K |
| MICP | 3.304 | 0.105 | 0.1N | K* |
| Uniform | 3.737 | 0.105 | 0.1N | 1 |

Table1은 TabICLv2, 51자료×10seeds에서 분류 accuracy 또는 회귀 RMSE로 구한 순위의 평균이고 CRUMB의 K는20이다. T는 query 수, K*는 test query가 실제 배정된 MICP cluster 수다. Full Context의 예산이 다르며 해당 표에서는 가장 좋은 순위다. kNN과의 보정 p=0.106을 동등성 증명으로 해석하지 않는다. Table2의 세 backbone 비교는 **38개 분류 자료만** 사용한다. 논문의 A100 비용을 초기 B1/B2 CPU 비용과 직접 비교하지 않는다.

## 4 Entangled by Design

Athanasios Vlontzos 외, *Entangled by Design: Spurious Intra-Variable Signal Routing in Tabular In-Context Learners*, [2607.25532v1, 2026-07-28](https://arxiv.org/abs/2607.25532v1). §3–7과 AppendixE의 지정 부분을 확인했다.

`X=[C; alpha S; noise]`의 분리된 성분과 confounder를 둔다. Proposition2의 폐형식은 population ridge(A1), C/S의 직교(A2), context 내 confounding(A3) 조건의 결과다. TabPFN은 별도 실증 대상이며 이 정리를 모든 비선형 모델·TabICLv2의 불가능성으로 확대하지 않는다.

환경 층화는 각 환경에서 context를 균등하게 가져온다. S-swap은 Y를 유지하며 추정된 spurious 성분을 다른 환경의 성분으로 바꾸므로 **S의 식별 또는 추정이 추가로 필요**하다. 합성 실험에서는 C/S를 안다. scIB 부분은 기술별 batch가 있는 실제 자료에 Y-confounding을 주입한 semi-synthetic 평가다. AppendixE는 전체 gene matrix의 PCA와 기술별 평균분산 대비 **cell-type별 평균분산**의 비율을 명시한다. abstract의 약한 환경 라벨만 필요하다는 표현을 임의의 자료에 곧바로 적용할 수 있다는 뜻으로 옮기지 않는다.

Tables6/7의 CSR 감소와 RMSE 악화는 [기록의 반례 표](../records/0005-related-foundations-audit.md)에 함께 실었다. CSR이 작은 모델의 예측오차가 반드시 작은 것은 아니다. 같은 이유로 attention·embedding 거리·관계 점수를 RCTL 공유 이득의 직접 증거로 사용하지 않는다. 이는 평가 목적의 구분이며 서로 다른 연구의 실패 원인이 같다는 인과 결론은 아니다.

## 5 TabClustPFN v3

Tianqi Zhao·Guanyang Wang·Yan Shuo Tan·Qiong Zhang, *TabClustPFN: A Prior-data Fitted Network for Tabular Data Clustering*, [2601.21656v3, 2026-05-14](https://arxiv.org/abs/2601.21656v3). arXiv 서지 제목은 “A Prior-Fitted Network”로 표시된다. 여기서는 로컬 PDF 표지의 v3와 §3–4 지정 내용을 기준으로 했다.

GMM과 비선형 iResNet 변환을 결합한 합성 prior에서 cluster 정답을 만든다. PIN은 TabICL encoder와 cluster prototype의 attention으로 soft assignment를 만들고 SoftARI로 학습한다. CIN은 각 후보 K의 `P^T P` 요약을 받아 K를 추론하며 cross-entropy로 학습한다. CIN gradient는 PIN에 역전파하지 않는다.

§3.4는 pretrained TabICL encoder로 초기화하고 나머지를 무작위 초기화한 뒤 **전체 파라미터를 최적화**한다고 명시한다. batch512, 10,000steps, 4대 RTX5090, 약92GPU-hours는 논문 보고 조건이다. 신규 table에 cluster 정답 없이 적용하는 것과 사전학습 때 정답을 사용하지 않는 것은 다르다. 모델은 K=1을 제외하며 훈련 K는2–10이다. K1 global RCTL과 같은 선택지를 최적화하는 모델로 취급하지 않는다.

평가의 ARI/NMI 및 K 오차는 자료 생성 집단의 회복을 묻는다. conditional regression similarity나 최종 예측기를 함께 학습했을 때의 효용과 같은 목적이 아니다. 별도 보관 v2와 다른 txt 추출본은 고유 내용 미검토로 남겼다.

## 6 Amortized Neural Clustering of Time Series

Ángel López-Oriona·Ying Sun, *Amortized Neural Clustering of Time Series based on Statistical Features*, [2605.13128v1, 2026-05-13](https://arxiv.org/abs/2605.13128v1). §2.2, §3.1.1–3.1.2, §3.2와 §5의 지정 구간을 확인했다.

ACF 또는 QAF 등의 통계 특징을 series별로 embedding하고, 모든 unordered pair의 embedding을 합친 뒤 MLP/sigmoid로 같은 cluster일 확률을 구한다. 합성 자료의 pairwise 정답으로 BCE를 학습한다. QAF는 시차를 둔 분위수 지시함수의 상관이며, 회귀 모델의 조건부 Y 분위수와 다른 정보다.

학습한 affinity에서 spectral clustering 또는 Louvain으로 소속을 얻는다. §3.1.2의 지정 설정은200,000개 합성 collection 학습 후10,000개 새 collection의 ARI를 평가한다. spectral은 실제 K를 제공받고 Louvain은 K를 입력받지 않는다. 학습 network의 한 번 추론이라는 표현이 모든 쌍의 평가와 graph 후처리를 없애지는 않는다.

§2.2는 선택한 특징이 생성 과정들을 충분히 구별한다는 전제를 두며, 합성 prior와 실제 자료의 부합도도 중요하다. 이번에 저자 코드·checkpoint 재사용 가능성은 검증하지 않았다. 사전학습 clustering과 비선형 통계 특징을 새 원리로 주장하지 않는 근거로 쓰되, 해당 방법이 현재 CPU 환경에서 항상 불가능하다는 결론으로 확대하지 않는다.

[실제 읽은 파일·판본](../sources/history-006.md), [원문 대조 범위](../verification/history-006.md), [과거 시도 색인](../prior-attempts.md)
