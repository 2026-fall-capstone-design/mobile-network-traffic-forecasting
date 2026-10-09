# 15의 문헌 판단: 범주 효과·계산 비용·시간 context

2026-09-25의 기록15는 교차 예측과 cell 식별 정보 진단 뒤 세 가지 대안을 검토했다. 범주를 합치는 것, 후보를 덜 계산하는 것, 시간에 따라 context를 바꾸는 것에는 이미 관련 원리가 있었다. 당시 기록은 이 요소만으로 새 알고리즘을 추천하지 않았고, 시간에 따른 자료 유효성을 다음 탐색 질문으로 남겼다. 이번 아카이브는 해당 여섯 문헌의 지정 구간을 대조했다. 이것을 전수 신규성 조사나 모든 미래 후보의 기각으로 해석하지 않는다. **H009-C11**

[15 보존 원문](../evidence/0013-0015/originals/SRC-0020972.md.txt)의 §3–4와 [13/14 저장 진단](0013-0015-transfer-cell-identity.md)을 함께 읽는다. [방법 비교](../references/category-cost-time-methods.md), [출처·읽은 범위](../sources/history-009.md), [검수](../verification/history-009.md), [주장별 근거](../verification/history-009-primary-review.json)로 연결한다.

## 어떤 작업을 확인했는가

| 항목 | 확인한 범위 |
|---|---|
| 연구 질문 | 같은 자료의 cell ID 병합, 선택적 비교 계산, 시간 context 관리가 기존 원리와 어떻게 다른가 |
| 당시 실행 | 13/14 진단은 별도 기록에서 검수. 여섯 문헌 방법을 이 프로젝트에서 실행했다는 증거로 세지 않음 |
| 이번 작업 | 텍스트6개 지정 구간·PDF6개 중 지정 내용29쪽·논문 보고표6행·서지와 접근 기록 대조 |
| 새 실험·원 코드 실행 | 모델 학습/추론0, 난수 simulation0, 과거 연구 스크립트 실행/import0 |
| 데이터·분할·seed | 이 묶음의 새로운 프로젝트 실험에는 해당 없음. 각 논문의 문제·정보·평가 범위는 아래에 구분 |
| 결과의 성격 | 논문 방법·가정 확인, 당시 판단의 범위 보완, 원문 표현의 미해결 항목 보존 |
| 비용 | 이 문헌 묶음은 CURE의 보고 시간을 인용. 기록15의 완료39context/23,424query/RCTL29 비용은 [후속 원장](0015-0021-cumulative-costs.md)에서 대조했으며 실패·타이머 밖 전체 비용은 미확인 |

## 범주를 합치는 선행은 무엇을 추정하는가

**Effect fusion**은 선형 회귀에서 다른 공변량의 효과를 조정하면서 범주별 회귀 효과를 묶는다. 범주 효과에 뾰족한 정규 혼합 prior를 주고 MCMC로 회귀 계수와 혼합 소속을 함께 추정한다. 기준 범주의 효과가0인 성분, 변수 안에서 공유하는 분산, 고정 분산과 역감마 hyperprior 선택을 갖는다. 원문15의 ‘식1–6’은 논문의 **식(2.1)–(2.6)**으로 찾아야 한다. 원자료 cell 궤적을 직접 묶는 알고리즘은 아니다. **H009-C01**

최종 소속은 가장 빈번한 partition을 택하거나, label switching에 불변인 posterior co-membership으로 거리 `1−C`를 만든 뒤 PAM과 silhouette로 정한다. 두 선택은 다르며 **PAM/silhouette 방식은 K1을 선택하지 못한다**. 따라서 모든 범주를 기준 효과와 합쳐 변수를 없애는 경우까지 이 선택 규칙이 자동으로 다룬다고 쓰지 않는다. PDF6–8·14–18, §2–3의 확인이다.

**Tree-Structured Modelling**은 범주를 나누는 후보마다 전체 관측을 사용한 GLM을 다시 적합한다. 이전 split 위치는 남지만 이전 계수는 고정하지 않는다. 후보 split은 최소 deviance로 고르고, 중단은 교차검증 deviance 또는 p-value/Bonferroni 방식으로 정한다. 논문은 후자에서 Wald보다 likelihood-ratio 검정을 선호한다. 순서형의 인접 분할과 명목형 범주의 분할도 구분한다. 원문15의 ‘deviance 또는 validation’은 **후보 선택과 중단의 구분 및 p-value 대안**을 생략한 요약이다. **H009-C02**

이 두 선행은 ‘자료 전체를 유지하며 범주 ID를 묶는다’는 설명만으로 신규성을 확보하기 어렵다는 당시 판단을 뒷받침한다. TabICL을 쓰는 모든 범주 병합이 무의미하거나 동일한 구현이라는 뜻은 아니다. 새 검토에는 추정 대상·사용 정보·결정 규칙이 무엇을 더 바꾸는지와 최종 예측기의 효용을 명시해야 한다.

## 계산을 줄이는 보장을 옮길 수 있는가

**BanditPAM++**은 PAM의 greedy BUILD와 local SWAP을 빠르게 수행한다. Virtual arms는 한 reference에 대한 거리 계산을 여러 swap 후보 갱신에 재사용하고, permutation-invariant caching은 공통 reference 순열과 거리 값을 반복 사이에 공유한다. 공통 reference, 시간에 따라 변하지 않는 거리, 그 거리로부터 후보 손실을 계산하는 관계가 필요하다. **H009-C03**

같은 PAM 해를 높은 확률로 얻는다는 조건부 결과는 전역 최적해 보장이 아니다. §5의 비용에는 sub-Gaussian scale, 후보 gap, SWAP 횟수 상한과 숨은 `c(k)` 의존성이 남는다. 판별이 어려운 후보는 전체 reference 계산으로 돌아갈 수 있다. TFM에서는 context를 바꾸면 예측 자체가 달라질 수 있으므로, 이 거리를 그대로 cache할 수 있는지와 context 준비·query 추론 비용을 따로 확인해야 한다. 거리 평가 수 감소를 우리 모델의 총 실행시간 감소로 바꾸어 쓰지 않는다.

**Active Clustering**은 symmetric similarity와 binary hierarchy의 tight clustering(TC) 조건 아래 tree를 복원한다. TC는 관련된 모든 triple에서 같은 cluster의 similarity가 두 cross similarity보다 큰 조건이다. Theorem3.1은 최대 `3N log_(3/2) N` 관측을 제시한다. 점수를 대칭화한 것만으로 TC를 충족하지는 않는다. **H009-C04**

Robust 방식은 pair별 독립 오염을 가정한다. `q<1/2` 외에도 Theorem4.1의 오염률·균형·threshold 조건이 필요하며, Theorem4.2의 `O(N log²N)` 복원은 크기 `>2m`인 cluster와 조상들의 균형 조건을 대상으로 한다. 모든 singleton까지 복원한다는 주장으로 확대하지 않는다. 실제 traffic 교차 손해가 이 조건들을 만족하는지 확인한 결과는 없다.

## 시간 context의 판단 신호와 평가 문제

**CURE**는 frozen 분류 TFM을 대상으로 먼저 예측하고 label을 받은 뒤 context를 갱신한다. 예측 시점의 정규화 class entropy를 한 번 저장하며, short FIFO에서 밀려난 항목을 long bank로 보낼 때 사용한다. Long bank가 차기 전에는 warm fill하고, 이후 entropy threshold로 admission을 정한다. 넘친 bank에서는 가장 많은 class의 입력상 가까운 쌍을 찾고 최근 short bank의 같은 class centroid에서 먼 항목을 제거한다. 같은 class가 short bank에 없으면 전체 short bank centroid를 사용한다. **H009-C05**

entropy가 유용성의 보편적 척도라는 정리는 아니다. 부록은 국소 분포 안정성·entropy consistency·label coherence를 조건으로 두고, 정보량 하한에 `α(H−δ−ε)`를 남긴다. 잡음이 크면 이 하한은 약해진다. 가까운 같은 class 항목의 중복성도 A.7의 가정이다. 회귀 예측분포가 넓다는 사실을 곧 유용한 표본으로 해석하지 말자는 기록15의 경계는 이 조건과 맞지만, 논문이 traffic 회귀나 RCTL에서 그 실패를 실험했다는 뜻은 아니다.

**NOMADD**는 과거 전체의 pooled anchor와 기간별 모델 차이를 공통 좌표로 만든다. TFM에는 고정 query에서 얻은 class log-probability를 사용한다. 낮은 차원의 시간 궤적을 damped ridge로 외삽하고 변화량을 shrink한다. Logistic/MLP 파라미터, 구조를 고정한 tree의 leaf 값, TFM 예측장은 서로 다른 좌표 구성이다. **H009-C06**

Forward validation은 마지막3개 학습 위치마다 더 이전 자료만으로 anchor를 포함한 전체 pipeline을 다시 만든다. 변화량0인 `α=0`도 선택 후보지만, 이것만으로 미래 손해를 방지하지는 않는다. 논문의 18분류 dataset·78분할 결과와 OVR macro AUC는 traffic 회귀 MAE나 cell 병합 효용의 증거가 아니다. Domain index를 입력으로 받는 frozen 비교군과 NOMADD 내부의 index 없는 pooled anchor도 구분해야 한다. 매끄럽고 낮은 차원의 drift라는 적용 조건이 남는다.

## 보고 시간과 원문 불일치 보존

CURE Table6은7개 stream의 평균 한 시점 처리시간(per-step)을 보고한다. Total은 fit·prediction·eviction의 합이며 전체 process wall time이라는 뜻은 아니다. 해당 실험은 단일 NVIDIA H200을 사용한다. 아래 값은 우리 CPU 측정이나 재현 결과가 아니다. **H009-C07**

| 방법 | Total 초 | Fit 초 | Prediction 초 | Eviction 초 |
|---|---:|---:|---:|---:|
| CURE | 0.0283 | 0.0044 | 0.0226 | 0.0013 |
| DualFIFO | 0.0259 | 0.0040 | 0.0214 | 0.0005 |

구성 합은 각 total과 맞으며 차이는0.0024초다. [원 보고값과 산술](../evidence/0015-literature/paper-reported-tables.json)에 분리했다.

이번 대조에서 다음 미해결 항목을 발견했다. 원문을 고쳐 보존하거나 방법 전체의 실패로 분류하지 않는다. **H009-C08·H009-C09**

| 항목 | 확인한 표현·수치 | 재사용 전에 필요한 확인 |
|---|---|---|
| H009-I01, BanditPAM++ | NeurIPS PDF5 식7의 nearest-medoid 제거 항 `min(d_i−d_2,0)`와 PDF7 Algorithm1 line11의 `min(d_2,d_i)−d_1`이 일반적으로 같지 않음 | 저자 구현·errata·증명의 정의와 일치 여부. 예를 들어 `d_1=1,d_2=3,d_i=2`를 대입하면 각각−1과+1이며, 이는 결정적 식 대조임 |
| H009-I02, NOMADD | PDF3 §3.4에서 `z=U_r Σ_r`로 정의하고 `Σ_r V_rᵀ`로 decode한다고 적어 그대로 읽으면 Σ가 두 번 적용됨 | 실제 latent 좌표 정의와 공식 구현. 임의로 ‘올바른 식’으로 바꾸지 않음 |
| H009-I03, Active | PDF4 Table1의 N256 행은 2,206/32,640과6.21%를 함께 기재. 계산 비율은 약6.75858% | 어느 셀이 잘못됐는지 원 결과 없이 단정하지 않음 |
| H009-I04, NOMADD | 서론의 leaf thresholds 변경과 §3.3의 tree 구조 고정/leaf values 갱신 표현이 다름 | 비교는 구체적 방법 절을 따르되 구현 확인은 미완료로 유지 |

## 판본·당시 접근·남은 범위

Tree PDF 표지의 typeset date는2018-03-12이고 arXivv1은2015-04-18이다. BanditPAM++은 당시 인용한 arXiv HTMLv1과 로컬 NeurIPS2023 PDF의 지정 절을 대조했다. §5 정리 번호는 HTML1–3, PDF2–4로 달라 번호만으로 대응시키지 않는다. 이번 공식 NeurIPS PDF 다운로드는 로컬 PDF와 바이트 해시가 같았다. 전체 판본의 내용 일치를 확인한 것은 아니다. **H009-C10**

[당시 입수 기록](../evidence/0015-literature/originals/SRC-0061717.json)의 HTTP406·verification 화면·HTTP429는2026-09-25의 접근 이력이다. 이번 Bandit 원문 확인의 장애로 남겨두지 않는다. 해시가 같은 Bandit PDF 사본은 연결했으나 다른 텍스트 추출본은 미검토로 유지했다.

여섯 논문의 **지정 방법 검토**가 끝났으며 전체논문 완료는0편이다. 시간 유효성의 후속 저장 진단은 [16–17](0016-0017-temporal-validity.md),17의 추가 문헌은 [후속 문헌 검토](0017-adaptation-literature.md), 공간 정보는 [18·21 진단](0018-0021-spatial-information.md), 완료 호출 누적은 [15·21 비용](0015-0021-cumulative-costs.md)에 연결했다. 지정 밖 본문·표·그림·부록·다른 판본·저자 코드, 회귀 TabPFN과 나머지 후속 관계, 실패·타이머 밖 전체 비용 감사는 남았다. 같은 원리로 새 실험을 설계할 때는 사용 정보·가정·비용·최종 결정 중 무엇을 바꿀지 먼저 적고, [문제별 색인](../prior-attempts.md)에서 관련 저장 결과를 확인한다.
