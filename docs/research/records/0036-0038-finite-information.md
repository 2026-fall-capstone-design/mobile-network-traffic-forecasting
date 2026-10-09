# 36–38: 분할의 이득을 학습 전에 판단할 수 있는가

[연구 안내](../README.md) · [출처와 실제 읽은 구간](../sources/history-023.md) · [검수](../verification/history-023.md) · [보존 근거](../evidence/0036-0038-finite-information/README.md)

**당시 결론은 정보이론 점수의 추가 채택을 보류하고, 최종 담당 RCTL 소속과 학습에 참고할 sample 범위를 따로 생각해 보자는 것이었다.** 새 후보 확정이나 새 RCTL 실행 결과가 아니다. 36은 세 문헌을 확인하는 계획, 37은 정보이론 주장에 대한 유한 반례 계획, 38은 문헌·계산을 연결한 판단이다. 확인일은 2026-09-25다.

직전 [33–35](0033-0035-process-fit-gap.md)의 일곱 K=4 조건은 같은 고정 checkpoint에서 global보다 train 평균 MAE가 작고 validation 평균 MAE는 컸다. 관계 차이를 더 잘 찾는 것만으로 분리 학습의 손해까지 해결된다고 할 수 없어서, 36–38은 **분할로 얻는 정보와 자료 공유를 포기하는 손해를 사전에 함께 계산할 수 있는지** 물었다. 이 관측만으로 과적합 하나를 원인으로 확정하지 않았다.

## 실제로 한 일과 하지 않은 일

| 구분 | 범위 |
| --- | --- |
| 문헌 | Khan의 정보량·중복성, Pesaran 등의 선형 panel 추정, Cakiroglu 등의 context 가치에 관한 지정 식·가정 |
| 37 저장 계산 | 공정하고 독립인 두 bit A,B의 네 상태를 각각 확률 1/4로 열거; 네 사례·8개 판정 |
| 데이터·척도 | 정보량 단위 bit. 네트워크 cell·시간 분할·정규화·MAE는 이 계산에 해당 없음 |
| 모델·seed | TabICL context 0, RCTL fit 0, RCTL forward 0으로 저장됨. 난수와 seed에 의존하지 않는 정확 계산 |
| 현재 아카이브 검산 | 같은 저장 상태를 확률비 정의의 MI/조건부 MI로 다시 계산. 과거 entropy 구현을 실행하거나 import하지 않음 |
| 아직 아닌 것 | 논문 전체 검토, 저자 코드 재현, 네트워크 성능 검증, 새 clustering 채택, 추천 알고리즘·최종 Word 완료 |

코드·시작 표식·결과가 함께 남아 있지만 결과에 당시 코드와 계획의 해시가 묶여 있지는 않다. 현재의 바이트 보존과 산술 일치가 과거 실행 환경 전체를 독립 재현했다는 뜻은 아니다.

## Khan: 성립하는 항등식과 강하게 적용하면 안 되는 주장

[Capacity and Redundancy Trade-offs in Multi-Task Learning](https://proceedings.mlr.press/v337/khan26a.html), Asif Khan, UAI 2026, PMLR 337:2934–2957. 이 기록은 공통 입력 X, task label Y, 압축 표현 Z의 정보량을 다룬다. 파라미터 수와 정보량 예산은 단위가 다르다.

두 target에서 TC는 두 target 사이의 상호정보량이다. 일반적으로는 각 target의 entropy 합에서 joint entropy를 뺀 의존성 양이다. 조건부 TC는 Z를 안 뒤에도 남는 의존성이다. 저장 반례에 사용하는 정확한 식은 다음과 같다.

$$
\sum_t I(Z;Y_t)
=I(Z;Y_{\mathrm{joint}})+TC(Y)-TC(Y\mid Z).
$$

| 사례 | 정의·핵심 값(bit) | 대조한 주장과 판단 |
| --- | --- | --- |
| XOR | X=(A,B), Y1=A, Y2=B, Z=A XOR B. 주변 정보 합 0, joint 정보 1, TC 0, 조건부 TC 1 | PDF3 Lemma3.1의 일반 하한 joint≤주변 합은 성립하지 않음. 위 항등식과 TC≥0에서 얻는 상한은 성립 |
| 정보 추가 | 처음 Z는 상수, 추가 표현은 XOR. 조건부 TC 0→1 | PDF5의 조건부 TC 단조 감소를 일반적으로 사용할 수 없음. 조건부 entropy 감소와 TC 감소는 다른 주장 |
| 중복 label | Y1=Y2=A, global Z=(A,B), C=2; singleton Z1=Z2=A, C1=C2=1. global/cluster 주변 정보 합 모두 2 | 실제 이득 0. joint 항을 뺀 축약식은 −1, joint 차이 +1을 포함하면 0 |
| 포화되는 대조 사례 | 독립 label A,B; global X, local A와 B. global/cluster 합 모두 2, joint 차이 0 | 실제·전체 식·축약식 모두 0. 조건이 맞는 축약식까지 부정하지 않음 |

중복 label 사례에서 global 입력 정보 I(Z;X)=2로 예산이 active지만, joint-label 정보 I(Z;Yjoint)=1이다. label 정보를 이미 모두 보존하므로 예측 정보에 관해 최적이어도 입력 예산 2가 예측 정보 2를 뜻하지 않는다. singleton은 각각 입력·예측 정보 1이다.

위 표현들은 모두 X의 결정적 함수이므로 해당 예의 Y−X−Z Markov 조건도 만족한다. 정보이론 가정 밖의 네트워크 관측을 반례로 대신 사용한 것이 아니다.

Appendix S4.37의 전체 이득식에는 다음 항이 남는다.

$$
G=(\Delta_s-\sum_k\Delta_k)-TC_{\mathrm{between}}
  +[\sum_k I(Z_k;Y_{G_k})-I(Z_s;Y)].
$$

여기서 Δs와 Δk는 각각 shared/local 표현에 조건을 둔 label TC다. 중복 label 사례는 앞 괄호 0, between TC 1, 마지막 joint-predictive 차이 1이므로 0−1+1=0이다. **논문은 S4.38에 예측 정보가 각 예산에 도달하는 saturation 조건을 실제로 명시한다.** 조건이 논문에 없다는 비판이 아니라, 총 입력 예산이 맞는다는 이유만으로 그 항을 없애면 안 된다는 확인이다. 네 사례의 [저장 결과](../evidence/0036-0038-finite-information/originals/SRC-0027888.json)와 8개 판정이 일치한다.

실제 방법도 무료 사전 점수는 아니다. PDF18은 rank-1 LoRA probe, task-head 200-step 준비, gradient similarity 후 average-linkage를 설명한다. GoEmotions/GLUE는 gradient 수집량과 평가 지표가 다르다. PDF7의 residual 상관 기반 −0.5 logdet 지표는 학습한 예측기의 validation 잔차를 쓰는 Gaussian 사후 근사다. Gaussian gradient 순위 대응은 whitening과 noise·signal-power 조건을 확인해야 하며 raw cosine의 일반 정리가 아니다. 이 조건들을 확보하지 않은 채 단일 출력 RCTL의 MAE 보장으로 옮기지 않았다.

## Panel: 이질성과 추정 오차를 둘 다 계산해야 한다

[Forecasting with panel data: Estimation uncertainty versus parameter heterogeneity](https://doi.org/10.3982/QE2589), M. Hashem Pesaran, Andreas Pick, Allan Timmermann, Quantitative Economics 17(2026), 342–393. 저장 자료는 2026 출판본 52쪽이다.

선형 모형 yit=θi′wit+εit에서 individual OLS와 pooled OLS를 비교한다. N은 단위 수, T는 단위별 시점 수다. Assumptions1–9에는 외생성·정상성·모멘트·역행렬 조건 등이 있으며, 단위 간 평균 MSFE 전개에는 독립성 또는 설명한 약한 의존 조건이 필요하다. lagged dependent variable을 포함하는 약한 외생성을 다루지만 임의 의존성 전체를 허용하지 않는다. **계수의 이질성이 regressor와 상관될 수 있다는 말과 단위 간 noise가 아무렇게나 상관되어도 된다는 말은 다르다.**

Propositions1–2의 큰 N, 고정 T 전개에서 individual MSFE에는 T⁻¹hNT라는 추정 오차 항이, pooled MSFE에는 ΔNT라는 이질성 항이 붙는다. 식24의 상대 차이는 다음 형태다.

$$
\frac{MSFE_{\mathrm{pooled}}-MSFE_{\mathrm{individual}}}
     {MSFE_{\mathrm{individual}}}
\ \longrightarrow\
\frac{\Delta-T^{-1}h_T}{\bar\sigma^2+T^{-1}h_T}.
$$

따라서 관계 차이 Δ만 재서 분할 이득이라고 선언할 수 없다. 그렇다고 이 식이 현재 RCTL에서 이미 측정된 비용은 아니다.

| 식·절 | 필요한 값·행동 | 이 연구로 옮길 때의 경계 |
| --- | --- | --- |
| Eq32 / Proposition3 | 공통 혼합 가중치 (Δ−T⁻¹ψ)/(Δ+T⁻¹h−2T⁻¹ψ); ψ는 추가 상관 항. strict exogeneity이면 ψ=0 | squared forecast error를 최소화하는 조건부 근사. MAE 최적 가중치와 같다고 할 수 없음 |
| Eq40–41 | individual/pooled 계수, 잔차 분산, regressor 공분산의 역행렬과 다음 입력 | 관측량의 추정 절차가 필요. TabICL 분위수 폭을 h나 계수 추정 분산에 그대로 대입하지 않음 |
| Eq42–43 | OLS 잔차의 직교성 때문에 단순 대입은 ψ를 0으로 만듦. 두 절반 OLS를 이용한 half-jackknife로 편향 추정 | 전체 추정치의 2배에서 두 절반 추정치 평균을 빼는 보정. 충분한 T와 N,T 증가 조건이 추가됨 |
| §4.4 Eq44–45 | individual OLS를 mean-group 쪽으로 수축하는 empirical Bayes의 행렬 가중치 | forecast 혼합의 공통 스칼라 가중치와 구별. 적용 조건을 생략하지 않음 |

이 묶음에서 panel 계수·가중치를 새로 추정하지 않았다. 부록의 전체 증명과 저자 코드도 검토 완료로 세지 않는다.

## Context: 최적 예측의 한계와 실제 유한 학습을 구별한다

[The Spectrum Is Not Enough: When Context Helps Time-Series Forecasting](https://arxiv.org/abs/2607.13006v2), Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban, **v2, 2026-07-15**, 저장 PDF21쪽을 사용했다.

Theorem1과 A.4는 같은 정보집합 I에서 최적 선형 MSE σ²lin과 Bayes MSE σ²* 사이 차이 Δ=σ²lin−σ²*를 사용한다. σ²lin>0이고 h가 I에 대해 측정 가능하며 MSE가 유한할 때,

$$
\frac{\sigma^2_{\mathrm{lin}}(I)-MSE(h)}
     {\sigma^2_{\mathrm{lin}}(I)}
\leq
\frac{\Delta(I)}{\sigma^2_{\mathrm{lin}}(I)}.
$$

이것은 같은 정보에 접근하는 **최적 선형 예측기 대비 초과 개선의 상한**이다. 유한 train 자료로 학습한 Ridge 또는 RCTL의 실제 오차를 σ²lin 자리에 넣어도 같은 보장이 생긴다는 뜻은 아니다. 더 긴 window가 선형 정보 자체를 늘리는 이득과 그 위의 비선형 이득도 구분한다.

A.8은 고정한 training memory에 조건을 두고 현재 window를 key로 삼는 retrieval을 정의한다. 이때 반환값은 key의 함수이므로 oracle의 조건부 정보집합을 새로 늘리지 않는다. 이 사실만으로 유한 표본에서 학습된 모델의 자료 공유·사전학습 이득이 없다고 결론 내릴 수는 없다.

Gaussian endpoint에서는 적절한 같은 좌표 정보에 대한 조건부 평균이 선형이어서 Δ=0이다. 그러나 유한 길이 phase surrogate가 항상 정확한 Gaussian이라는 주장은 아니다. A.5의 Lindeberg 조건, 고정 차수 다항식과 전체 measurable predictor의 차이, 전체 Bayes-risk 수렴에 필요한 조건부 평균의 L² 수렴 조건(M)을 구별한다. A.3에서 정확히 보존하는 것은 circular sample autocovariance이며 일반 sample 경계항·IAAFT spectrum 잔차·cross-channel coherence를 같은 것으로 취급하지 않는다.

실제 진단 Δnl은 training 내부에서 시간 순서 60/40 분할로 AR(d) 최소제곱 예측과 k=4 최근접 이웃 예측의 one-step MSE를 비교한다. test label을 쓰지 않는다는 설명이 training target이나 추정 계산도 필요 없다는 뜻은 아니다. A.9의 lower-bound 해석은 선형 오차가 population 최적값에 접근하는 조건 아래의 설명이고, 유한 표본의 확정 하한으로 쓰지 않는다.

원문38의 “fixed-k에서의 비일관성”은 더 좁게 읽어야 한다. 논문은 **고정 k에서 일관성을 주장하지 않는다**고 명시하며, 그 문장 자체가 모든 경우의 비일관성 증명은 아니다. A.9–A.10은 기본 motif embedding과 주 E2/E4의 operating-window embedding d=S=12도 구분한다. LODO의 threshold와 방향은 다른 여섯 dataset의 context-value 부호로 정한다. 최종 진단은 개선의 크기보다 부호를 다루며, univariate·정상성·embedding 길이·단위 간 의존성의 한계가 남는다. 저자 [코드 링크](https://github.com/KurbanIntelligenceLab/SINE)는 출처로만 연결하며 실행·재현하지 않았다.

## 접근 실패·계산 비용·당시 결정

| 저장 항목 | 보고된 시간(초) | 상태와 해석 |
| --- | --- | --- |
| 37 exact finite 계산 | 0.0002907999987655785 | result와 ledger의 해당 key가 같음. 현재 재측정한 당시 실행시간이 아님 |
| Khan HTML / PDF | 0.321120800 / 0.387885200 | 각각 HTTP200, 크기·SHA가 저장 metadata와 일치 |
| Cambridge repository HTML | 4.162340400 | HTTP200으로 저장됨 |
| 2025 author manuscript | 0.258925400 | HTTP404. 확보한 PDF로 세지 않음 |
| Spectrum abs / v2 HTML / v2 PDF | 0.252261800 / 0.247916300 / 0.330363800 | 각각 HTTP200 |
| Cambridge 2026 published PDF | 5.174044900 | 별도 manifest의 HTTP200·정식 bitstream |

5초는 37 계산의 계획 상한이고, 10MiB/30초는 36의 파일 입수 제한이다. 사용시간과 같은 숫자가 아니다. 문헌 다운로드 시간을 모델 실행시간에 합치지 않았다. 38에 쓰인 이후 Cambridge web parser timeout도 기존 HTML/PDF의 성공한 입수를 취소하지 않는다. timeout의 독립 console 근거와 전체 작업시간은 이 묶음에서 확인하지 않았다. ledger는 해당 계산 key만 연결하며, 이후 누적 used를 36–38 당시 사용량으로 읽지 않는다.

37 코드의 timer는 시작 marker를 쓴 다음부터 네 사례와 판정값을 계산한 지점까지다. 뒤의 PDF 해시 읽기와 result 파일 저장, 바깥 process 시간은 포함하지 않으므로 전체 실행 벽시계로 해석하지 않는다.

당시 유지한 결정은 다음과 같다.

1. 학습한 표현·gradient·잔차와 추가 조건이 필요한 정보이론 점수를 RCTL 독립 사전 점수로 바로 채택하지 않는다.
2. 최종 cell 담당 소속과 실제 학습 sample의 공유 범위가 꼭 같아야 하는지 다시 검토한다.
3. global 사전학습·가중치 공유·sample reweighting 자체를 신규성으로 세지 않는다. TabICLv2가 단순한 밀도비 추정이나 기존 공유 방법보다 어떤 추가 정보를 주는지 먼저 확인한다.

이는 당시 다음 질문이며 현재 실행 지시가 아니다. 자료 공유 전략과 두 종류 이득이 현재 clustering에서 확인됐다는 결론도 아니다. 초록 수준으로 발견한 Sonnleitner ESWA2025, measurement-error clustering, CLOSE, Barnes–Dubrawski2019는 상세 방법 검토 완료로 세지 않는다.

## 팀에서 재사용할 때

같은 정보이론 주장을 확인하려면 [보존 결과와 모델 없는 검산](../evidence/0036-0038-finite-information/README.md)을 먼저 사용한다. 새 fit으로 이 네 반례를 다시 확인할 필요는 없다. 다른 가정에서의 정리를 제안한다면 입력 정보 예산, 예측 정보 saturation, 실제 추정 절차, 손실 척도를 명시해야 한다.

새 공유 방법을 설계한다면 기존 33–35의 고정 checkpoint 결과를 먼저 연결하고, 소속·sample 범위·자료량·손실 중 무엇이 달라지는지 적는다. 공유 또는 분할 자체를 새로 발견한 방법처럼 제시하지 않는다. 이후 39번부터의 채택·기각·실행 여부는 아직 연결하지 않았으므로, 이 페이지가 전체 후속 결론을 대표하지 않는다.
