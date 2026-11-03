# 원92 순차 예측 증거의 미채택과 점 예측 공유 목적의 차이

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

**상태:** 2026-09-26 당시 후보 미채택. 42개 주장·8개 묶음의 작성 후 원문 대조 완료. 새 모델 실행0.

[출처와 판독 범위](../sources/history-122.md) · [검수](../verification/history-122.md) · [근거](../evidence/0122-prequential-sharing-objective/README.md) · [직전 원91](0121-predictive-role-alignment.md)

공유 context와 셀별 context의 분포 점수를 비교할 수 있다는 것과, 최종 RCTL 점 예측에 유용한 소속을 선택한다는 것은 다른 주장이다. 원92는 기술적 가능성을 검토했으나 후자를 확인하지 못해 채택하지 않았다. 같은 중앙값·다른 잡음의 기호 반례는 이 목적 차이를 설명하며 실제 traffic 실험이 아니다.

새 순차 공유 점수를 설계하기 전에는 [당시 판단](#claim-01), [기호 반례](#claim-07), [학습 이득의 공백](#claim-08), [작업량](#claim-38), [다시 열 조건](#claim-42)을 먼저 읽는다. 아래 문헌의 저자 실험, 저장 코드의 정적 동작, 당시 기호 검토와 이번 표기 검수를 구분한다. 과거 Goal·예산·코드 명령은 보존 자료다.

## <a id="claim-01"></a>01. 당시 후보와 미채택 판단

원92는 2026-09-26에 shared context와 셀별 context의 순차 예측 증거로 소속을 정하는 후보를 검토했다. 유한 자료에서 비교할 가능성은 인정했지만, 최종 RCTL 점 예측에 유용한 분할 결정과 기존 BHC·MDL 원리를 넘어서는 기여가 확인되지 않아 채택하지 않았다. 밀도 API가 없거나 베이지안 방법 전체가 불가능하다는 판정은 아니다.

근거: [SRC-0001700](../sources/history-122.md#src-0001700) [[1, 31]]행, [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행, [SRC-0001704](../sources/history-122.md#src-0001704) [[8, 8]]행.

## <a id="claim-02"></a>02. 실행 범위와 과거 원장

원92는 새 TabICL 추론·RCTL 학습·자료 수치 진단을 수행하지 않았다고 기록한다. 당시 잔여 Tab 11 context·20,640 query행과 추가 RCTL fit 0은 보존 원장의 값이다. 이번 정리에서도 원 연구 코드의 실행·import와 모델 실험을 하지 않았다. 과거 Goal·AGENTS·예산 문구를 현재 정리 작업의 실행 명령으로 사용하지 않는다.

근거: [SRC-0001702](../sources/history-122.md#src-0001702) [[1, 19]]행, [SRC-0001708](../sources/history-122.md#src-0001708) [[9, 15]]행, [SRC-0025150](../sources/history-122.md#src-0025150) [[68, 92]]행.

## <a id="claim-03"></a>03. 순차 joint를 정의하는 조건

정규화된 예측 조건부 분포를 각 시점의 사용 가능한 과거 정보에만 의존하도록 정하면 그 곱으로 순차 joint law를 정의할 수 있다. 이 기호 설명에 관측의 iid·교환가능성이 항상 필요한 것은 아니다. 그러나 그 곱이 TabICL 사전학습 prior에서 얻은 exact marginal 또는 실제 공유 함수의 posterior라는 해석은 별도 근거를 요구한다.

근거: [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행, [SRC-0001708](../sources/history-122.md#src-0001708) [[11, 11]]행.

## <a id="claim-04"></a>04. 블록 marginal과 공유 잠재 함수

같은 context에서 블록 안 query를 각각 예측한 marginal의 곱은 일반적으로 같은 잠재 함수를 공유한 joint predictive와 다르다. 공유 잠재 변수를 적분하면 관측들 사이의 의존이 남을 수 있기 때문이다. query별 prefix를 갱신하는 순차 비교와 고정 context에서 블록 손실을 합치는 비교의 범위도 명시해야 한다.

근거: [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행, [SRC-0001710](../sources/history-122.md#src-0001710) PDF [4, 5]쪽, [SRC-0001712](../sources/history-122.md#src-0001712) PDF [2]쪽.

## <a id="claim-05"></a>05. lag와 시간 조건화

미래 query의 lag에 앞 query의 target이 들어가는 경우, 예측 순서와 각 시점에 실제 관측된 정보를 먼저 정해야 한다. 앞 target이 관측된 뒤 쓰는 것과 아직 알려지지 않은 target을 쓰는 것은 다르다. 이 요구만으로 저장 Tab 호출에 실제 정답 누수가 있었다고 단정하지 않으며 원92에는 새 순차 실행 결과가 없다.

근거: [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행, [SRC-0001702](../sources/history-122.md#src-0001702) [[1, 19]]행.

## <a id="claim-06"></a>06. target 좌표와 Jacobian

z=(y-a)/s, s>0인 변환에서 원단위 log density는 변환단위 값에서 log(s)를 빼야 한다. 동일한 고정 scale을 쓰는 비교에서는 공통 항이 소거될 수 있지만 context별·prefix별 scale이면 일반적으로 그렇지 않다. 이미 원단위로 역변환한 quantile에서 밀도를 구성하는 경우에는 같은 보정을 중복 적용하지 않는다.

근거: [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행, [SRC-0001719](../sources/history-122.md#src-0001719) [[417, 434], [737, 752]]행.

## <a id="claim-07"></a>07. 같은 중앙값·다른 잡음의 기호 반례

두 셀이 같은 conditional median m(x)를 갖고 서로 다른 대칭 Gaussian noise를 갖는 이상적 모집단 예시에서는 MAE 최적 점 예측 m(x)를 함께 쓸 수 있다. 반면 각 셀의 참 밀도에 맞춘 log score는 pooled mixture보다 좋으며, 동일 셀 비중에서 그 평균 이득은 두 밀도의 Jensen–Shannon divergence다. 이는 원92의 기호 반례이고 실제 traffic·유한 BHC 판정·새 실험 결과가 아니다.

근거: [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행, [SRC-0001708](../sources/history-122.md#src-0001708) [[12, 12]]행.

## <a id="claim-08"></a>08. 분포 분리와 유한 학습 이득

분포 전체의 차이가 보인다는 사실만으로 최종 RCTL 점 예측을 여러 모델로 나누어야 한다고 결론낼 수 없다. 함수 추정의 불확실성·관측 noise·유한 context에서의 예측 손해·실제 RCTL의 학습 손해는 각각 확인해야 한다. likelihood나 loss 이름을 바꾸는 것만으로 원92의 미채택 사유가 해결되지는 않는다.

근거: [SRC-0001700](../sources/history-122.md#src-0001700) [[1, 31]]행, [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행, [SRC-0001704](../sources/history-122.md#src-0001704) [[7, 9]]행.

## <a id="claim-09"></a>09. BHC의 단일 성분 가설

Heller–Ghahramani ICML2005 BHC의 H1은 같은 성분 parameter를 공유하는 조건부 iid 관측을 가정하고, likelihood와 prior를 명시해 관측 likelihood의 곱을 적분한다. H2는 두 subtree의 주변우도 곱으로 각 subtree와 일치하는 여러 분할을 포함한다. 임의의 Tab 점수에 BHC 식을 붙이는 것만으로 이 생성 가설과 posterior 의미를 물려받지 않는다.

근거: [SRC-0001712](../sources/history-122.md#src-0001712) PDF [2, 3]쪽.

## <a id="claim-10"></a>10. BHC recursion·cut·DPM bound

BHC는 가장 높은 r_k의 쌍을 greedy merge해 tree를 만들고 r_k<.5에서 cut한다. d_leaf=alpha, d_k=alpha*Gamma(n_k)+d_left*d_right로 prior merge weight를 구한다. Corollary1의 DPM lower bound에는 d_k*Gamma(alpha)/Gamma(n_k+alpha)라는 prefactor가 붙는다. p(D|T) 자체를 전체 DPM exact marginal이나 그 lower bound로 바꾸지 않는다.

근거: [SRC-0001712](../sources/history-122.md#src-0001712) PDF [3, 4, 5]쪽.

## <a id="claim-11"></a>11. BHC 데이터와 평가 단위

BHC 주표는 synthetic·newsgroups·spam·digits3·digits10·glass의 여섯 행이다. synthetic/glass에는 Gaussian, 다른 주표 자료에는 binary Bernoulli likelihood를 쓴다. 표의 dendrogram purity는 알려진 class를 이용한 군집 평가이며 평균은 5-fold CV, 오차는 standard error다. Fig6의 news800/50단어는 주표 news120/500단어와 다른 정성 조건이다.

근거: [SRC-0001712](../sources/history-122.md#src-0001712) PDF [5, 6]쪽.

## <a id="claim-12"></a>12. BHC의 이득과 Glass 예외

BHC purity는 synthetic .828±.025, news .465±.016, spam .728±.029, digits3 .807±.022, digits10 .393±.015로 해당 행의 세 linkage보다 높다. Glass .467±.011은 SL .478±.009·CL .476±.009·AL .491±.009보다 낮다. Gaussian 모형 부적합은 저자의 설명 가설이며 독립 원인 검증은 아니다. 주표를 모든 자료·미래 traffic 예측에서 우세한 결과로 확대하지 않는다.

근거: [SRC-0001712](../sources/history-122.md#src-0001712) PDF [5, 6]쪽.

## <a id="claim-13"></a>13. BHC 비용·hyperparameter·한계

BHC 논문은 conjugacy·충분통계를 쓰는 구조에서 tree O(n²), marginal O(n log n), predictive O(n)을 설명한다. fixed tree의 hyperparameter gradient 및 반복 최적화 가능성과 실제 Gaussian 실험의 한 hyperparameter line search를 구분한다. greedy 선택·tree uncertainty 미반영 및 더 큰 모형·빠른 탐색·다른 추론 비교의 미래 과제도 남긴다. 이 비용을 Tab context 준비나 실제 RCTL 전체 탐색 시간으로 옮기지 않는다.

근거: [SRC-0001712](../sources/history-122.md#src-0001712) PDF [5, 7]쪽.

## <a id="claim-14"></a>14. BHC 예측 weight의 표기 검수

이번 정리에서 인쇄 Eq9의 omega_k=r_k*product_ancestor(1-r_i), N=all tree nodes를 다시 확인했다. 두 leaf의 r=1이고 root r=.5인 자체 기호 대입에서는 세 weight 합이1.5다. 따라서 인쇄식만으로 normalized component density들의 정규화된 mixture를 보장한다고 요약하지 않는다. 실제 구현·추가 정규화·다른 판본·해석은 미확인이다. 이를 원92 당시의 기각 근거나 BHC 실험 전체의 무효 판정으로 바꾸지 않는다.

근거: [SRC-0001712](../sources/history-122.md#src-0001712) PDF [5]쪽.

## <a id="claim-15"></a>15. GP-BHC의 공유 시간 함수

Cooke 등 BMC2011은 군집의 G개 gene·T개 시각 관측이 같은 잠재 시간 함수 f와 noise variance를 공유한다고 가정한다. noise는 iid Gaussian이지만 f를 적분한 관측 y의 covariance는 시간 의존을 포함한다. 따라서 시계열 주변 관측 전체가 iid여야 하는 모형으로 설명하지 않는다. 공유 f의 생성 가설과 shared Tab context·같은 RCTL 점 예측 함수의 소속은 자동으로 동치가 아니다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [3, 4]쪽.

## <a id="claim-16"></a>16. GP 정규화·covariance·고정 theta

GP-BHC는 각 gene의 관측 전체 시간축을 mean0/std1로 정규화하고, fixed theta에서 f를 적분해 N(0,Sigma+sigma_epsilon²I)를 계산한다. squared exponential은 signal/noise/length scale, cubic spline은 signal/noise를 둔다. theta 자체를 전부 적분한 exact Bayesian evidence라는 설명은 아니다. retrospective clustering의 전체축 정규화를 causal traffic 예측에 그대로 적용해도 누수 없다고 주장할 수 없다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [4, 5]쪽.

## <a id="claim-17"></a>17. 반복 측정과 empirical Bayes noise

GP-BHC는 replicate 평균 profile을 군집화하고 replicate variation으로 noise Gamma prior를 정한다. noise는 측정오차와 생물학적 변동의 합이라는 가정이다. Omega100으로 약한 prior를 만들고 noise posterior log값을 gradient ascent로 최대화한다. 이 prior를 sigma_m²~1 구간의 hard support로 바꾸지 않는다. 다른 theta는 flat prior이며 replicate 미사용 시 noise도 flat prior다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [3, 4, 5]쪽.

## <a id="claim-18"></a>18. 이상치 mixture의 1차 근사

GP의 원래 outlier joint는 관측별 regular/outlier mixture의 곱을 같은 f prior 안에서 적분한다. 2^N개 항에서 no-outlier와 single-outlier 항만 남기는 1차 근사이며 두 개 이상 outlier 항은 버린다. outlier 상수 B는 dataset Range의 역수다. 자체 조건부 대수 검토에서 남은 계수합은 a^N+N*a^(N-1)*(1-a)이므로 이를 일반적인 exact normalized full mixture marginal로 바꾸지 않는다. 실제 R 코드 오류나 관측 성능 실패를 인증한 것은 아니다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [5, 6]쪽.

## <a id="claim-19"></a>19. GP 식11 판본 공백

저장 GP PDF의 식11은 추출 텍스트와 전체 이미지 모두 sigma_m² 하나만 식 번호 옆에 표시한다. product 전개식을 임의 복원해 원문 인쇄식으로 제시하지 않는다. 주변 설명과 식10·12는 읽을 수 있으며, 추가 판본이나 실제 구현으로 해소할 공백으로 남긴다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [5, 6]쪽.

## <a id="claim-20"></a>20. GP 자료·replicate·시각 수 차이

GP 자료는 S.cerevisiae1 169gene/17시각/no replicate, S.cerevisiae2 440/15/biological2, H.sapiens58/10불균등시각/biological2에technical34+10, E.coli200gene/biological3에technical2씩이다. E.coli 시각 수는 Methods12와 Table2의13이 다르므로 통일하지 않는다. H.sapiens 표의44를 독립 biological replicate44로 바꾸지 않는다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [6, 12]쪽.

## <a id="claim-21"></a>21. GP 비교군의 조건

GP Table1은 outlier mixture와 replicate 정보를 사용하지 않는 비교다. HCL·SSClust·Zhou의 군집 수는 BHC-SE가 얻은13/58/6/24로 고정한다. MCLUST는 spherical/diagonal covariance로 제한하며 Zhou는 first-order random-walk JAGS 구현을 사용한다. 비균등 시각을 반영한 방법과 다른 방법의 조건도 다르므로 모두 동일한 자동 최적화 비교로 요약하지 않는다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [7, 8]쪽.

## <a id="claim-22"></a>22. GP log값·PCC·BHI의 다른 우열

BHC-SE의 log tree marginal은 네 자료에서 -3293/-3956/-633/-2497로 BHC-C의 -3356/-4294/-734/-2622보다 높고 PCC도 높다. 그러나 BHI는 SE .70/.57/.62/.46, C .73/.55/.78/.47로 C가 3/4에서 더 높다. H.sapiens PCC .75는 MCLUST·Zhou와 동률이며 E.coli BHI .47은 C·MCLUST가 같다. 높은 evidence와 한 평가의 우세를 모든 목적의 동일 최적성으로 바꾸지 않는다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [7, 8]쪽.

## <a id="claim-23"></a>23. GP 지표와 오차 표기

BHI는 GO annotation을 공유하는 군집 내 gene pair의 생물학적 homogeneity이고 PCC는 profile 상관이다. BHI는 bootstrap 1000회, PCC는 100회로 불확실성을 계산한다. Methods는 평균의 standard error 추정을 설명하고 표는 ±1stdev라고 명시하므로 해당 표기를 보존한다. seed 간 STD·95% CI·소속 posterior calibration·traffic MAE로 바꾸지 않는다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [6, 7]쪽.

## <a id="claim-24"></a>24. GP synthetic 검사의 범위

이미 BHC-SE에서 추정한 6/13개 GP로 각 1000개의 synthetic dataset을 생성한 검사에서 6clusters 정확80%, 13GP의 11–13clusters 89%를 보고한다. 13clusters 정확89%가 아니다. 비용 때문에 SSClust는 100개만 쓰고 최대 군집 수를 12/20으로 정하며 CAGED는 자동화 불가로 제외한다. noise STD를 절반으로 줄였을 때 항상 6/13을 찾았다는 결과는 data-not-shown 저자 보고다. 이를 독립 traffic 실행으로 가산하지 않는다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [9]쪽.

## <a id="claim-25"></a>25. GP outlier 재배정의 긍정 사례

Fig5의 FSP2/CSM3/WcaC 예시는 mixture를 쓰면 cluster PCC가 .42→.75/.16→.94/.80→.98, BHI가 .46→.50/.42→.68/.22→1로 달라진다. 세 선택 예시를 전체 gene의 평균 개선으로 확대하지 않는다. S.cerevisiae1은 SE에서 169gene 중 4gene을 재배정하고 C의 분할은 불변이며, E.coli C는 WcaC 1gene만 변경한다. caption의 CMS3와 본문의 CSM3 철자 차이도 임의 정정하지 않는다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [9, 10]쪽.

## <a id="claim-26"></a>26. replicate 추가의 이득과 예외

Fig6에서 S.cerevisiae2 parent PCC .91/BHI .74는 child .94/.70 및 .92/.84로 나뉜다. E.coli parent .0023/.28은 child .40/.12·.31/.28·.16/.34가 되고 BHI .12 child에는 over-represented GO가 없다. H.sapiens의 두 gene PCC .90 cluster는 BHI 대신 기능을 직접 보았다고 표시한다. 더 뚜렷한 profile과 모든 child의 BHI 증가를 같은 결과로 설명하지 않는다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [10, 11]쪽.

## <a id="claim-27"></a>27. GP 계산 구조와 실제 비용표

저자는 공유 시간 covariance의 block 구조와 matrix inversion lemma로 GT×GT 대신 T×T inversion을 한 번 수행해 병목을 줄였다고 설명한다. 2.40GHz Xeon의 Table2 SE/mixture runtime은 S.c1 6m3s/38m49s, S.c2 24m8s/5h48m, H.sapiens 19s/49s, E.coli 7m6s/34m39s다. replicate 정보를 추가해도 시간이 늘지 않는다는 것은 저자 보고이며 Tab prefix·RCTL 탐색 비용의 측정값이 아니다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [11, 12]쪽.

## <a id="claim-28"></a>28. GP 구현과 추가 파일의 공백

R/BHC 1.5·Bioconductor 2.9+·R 2.13·GPLv3는 2011년 당시 availability다. 현재 버전이나 실행 재현을 검증하지 않았다. Additional1–4의 priors·gene 목록·큰 GO 그림, 실제 R/C++ 구현·정확한 seed/threads/RAM/optimizer 시작 및 원자료 재현은 이번 저장 PDF 전체 판독의 범위 밖이다.

근거: [SRC-0001710](../sources/history-122.md#src-0001710) PDF [12, 13]쪽.

## <a id="claim-29"></a>29. PreqTorch의 loss 계약

고정 PreqTorch는 opaque batch를 model(batch)에 주고 호출자가 제공하는 loss_fn(batch,output).sum()을 누적한다. 기본 probability density·log base·bits 변환·timestamp 검사는 제공하지 않는다. 손실 예시와 임의 MAE를 Bayesian code로 동일시하지 않는다. target이 batch에 있다고 실제 누수를 확정하는 것은 아니지만 causal 입력과 손실의 의미는 호출자가 보장해야 한다.

근거: [SRC-0001720](../sources/history-122.md#src-0001720) [[43, 61], [95, 111]]행, [SRC-0001721](../sources/history-122.md#src-0001721) [[54, 85], [116, 133]]행.

## <a id="claim-30"></a>30. BlockEncoder의 reset과 학습 순서

BlockEncoder는 각 eval block을 먼저 점수화하고 마지막이 아니면 초기 state_dict를 복원한 뒤 fresh optimizer로 같은 index의 train_loader를 학습한다. 최종 train_loader는 사용하지 않는다. train/eval list 길이를 맞추지만 누적 causal prefix인지는 검사하지 않는다. patience는 training batch loss의 미개선 횟수에 적용되며 best weights 복원은 없다. 이 흐름을 TabICL의 context 준비나 한 번의 fit과 같은 비용으로 세지 않는다.

근거: [SRC-0001720](../sources/history-122.md#src-0001720) [[120, 144]]행, [SRC-0001721](../sources/history-122.md#src-0001721) [[88, 157]]행.

## <a id="claim-31"></a>31. MIR·ModelClass·adapter 범위

MIR은 새 batch의 score를 누적한 뒤 model/replay를 갱신하며 선택 beta/EMA를 처리한다. ModelClass는 torch.nn.Module subclass를 새로 초기화하고 Xavier·bias0·기타 uniform 또는 custom init을 쓴다. sklearn TabICLRegressor의 fit/predict adapter는 이 3파일에 없다. 불러오는 batches/replay/results 모듈과 실제 sampler의 시간 범위를 검수하지 않아 코드만으로 chronological joint나 Tab 지원 실행을 인증하지 않는다.

근거: [SRC-0001720](../sources/history-122.md#src-0001720) [[146, 184]]행, [SRC-0001721](../sources/history-122.md#src-0001721) [[160, 334]]행, [SRC-0001722](../sources/history-122.md#src-0001722) [[1, 89]]행.

## <a id="claim-32"></a>32. density API와 고정 판본

저장 TabICL 2.2.0 quantile_dist에는 log_prob와 pdf가 존재한다. 이번에는 quantile_dist 1543행을 전체 읽고 H005/H024의 선택 범위를 보완했으며 regressor 765행은 H075 전문 판독 자료를 재사용했다. fixed official commit 0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3와 보존 해시의 자료이며 최신 upstream 검수·모델 실행은 아니다.

근거: [SRC-0001714](../sources/history-122.md#src-0001714) [[1, 18]]행, [SRC-0001718](../sources/history-122.md#src-0001718) [[1057, 1102]]행, [SRC-0001719](../sources/history-122.md#src-0001719) 판본·판독 범위, [SRC-0001718](../sources/history-122.md#src-0001718) 판본·판독 범위.

## <a id="claim-33"></a>33. 분위수 grid와 crossing 처리

quantile alpha를 주지 않으면 균등 내부 격자를 만든다. 실제 raw quantile의 level을 명시해야 하며 129개라는 개수만으로 균등이라고 가정하지 않는다. crossing의 default는 sort이고 isotonic/cummax도 허용하며 Numba가 없으면 isotonic도 warning 후 sort로 fallback한다. 보정 방식과 입력 검증 없는 grid를 정확한 원래 posterior와 동일시하지 않는다.

근거: [SRC-0001718](../sources/history-122.md#src-0001718) [[90, 135], [248, 281], [544, 577], [1517, 1543]]행, [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행.

## <a id="claim-34"></a>34. quantile 꼬리와 수치 guard

중앙 quantile은 piecewise linear다. exp tail의 beta는 최대20개 또는 n//4개의 log-alpha 회귀에서 추정하고 [.01,100]에 제한한다. GPD는 spacing ratio 기반 Pickands-like eta를 [-.49,.49]에 제한한다. alpha TOL 1e-6, log ratio/exponent 15 등 guard가 들어가므로 분포 family·grid·guard에 의존하는 구성이다. 이 정적 관찰을 실제 traffic 꼬리 문제의 발생이나 모든 분위수 예측의 실패로 확대하지 않는다.

근거: [SRC-0001718](../sources/history-122.md#src-0001718) [[17, 87], [284, 504], [579, 647], [722, 780]]행.

## <a id="claim-35"></a>35. literal pdf의 양수 floor

log_prob는 cdf(z)에서 Qprime을 구해 -log를 취하고 pdf는 그 exp다. Qprime은 꼬리까지 최종 [1e-6,1e6]에 clamp된다. 정상 finite 계산을 실수 산술로 해석하면 literal pdf에 1e-6의 양수 하한이 생기므로 real 전체에 그대로 적용한 함수를 적분1의 exact density로 보장할 수 없다는 자체 기호 검토를 남긴다. 제한된 support·재정규화를 새로 가정하지 않고 실제 RCTL 성능 실패·Tab prior 불가능성으로 바꾸지 않는다.

근거: [SRC-0001718](../sources/history-122.md#src-0001718) [[953, 1102]]행, [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행.

## <a id="claim-36"></a>36. CRPS와 모멘트의 검수 한계

CRPS는 [0,1e4]로 clamp되고 pinball 999격자 함수는 수치 검사 경로의 존재일 뿐 이번 실행 검증이 아니다. GPD mean/variance는 eta를 최소 .01로 다시 clamp하므로 음수 eta 설정을 그 모멘트에 그대로 쓰지 않는다. 모든 CDF/icdf/pdf 관계·analytic 모멘트·broadcast 정확성을 이번 정적 판독으로 인증하지 않는다.

근거: [SRC-0001718](../sources/history-122.md#src-0001718) [[1131, 1133], [1304, 1328], [1357, 1373], [1408, 1435]]행.

## <a id="claim-37"></a>37. target 역변환과 ensemble quantile

regressor.fit은 주어진 y의 StandardScaler와 feature/ensemble/checkpoint/cache를 준비하며 pretrained weights를 gradient 학습하지 않는다. predict는 각 ensemble 출력을 원target 좌표로 역변환한 뒤 평균한다. 이미 역변환한 quantile에서 density를 구하면 같은 Jacobian을 다시 적용하지 않는다. 평균 quantile의 density와 각 ensemble density의 mixture는 자동 동치가 아니다.

근거: [SRC-0001719](../sources/history-122.md#src-0001719) [[357, 434], [737, 760]]행, [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행.

## <a id="claim-38"></a>38. 순차 비교의 작업량 조건

R개 block·Ncell·P후보쌍·block당 Qquery에서 개별 context N과 shared P를 준비하는 범위는 R(N+P), 개별·두 셀 shared query는 RQ(N+2P)다. 매 query마다 prefix를 갱신하는 exact cost가 아니며 prior·cache/preprocess·탐색·merge 후 재계산을 포함하지 않는다. allpairs P=N(N-1)/2; 대칭화한 top-k 후보 union은 P≤Nk이며 항상 Nk/2라고 할 수 없다. 실행시간 측정이나 pilot 실행은 없다.

근거: [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행, [SRC-0001702](../sources/history-122.md#src-0001702) [[1, 19]]행.

## <a id="claim-39"></a>39. workshop 초록과 과거 403

원92는 TabPFN Bayesian coding ICML Workshop2025의 공식 목록·초록을 확인했으나 전문 PDF403을 기록했다. 이 과거 접근 실패를 현재도 접근 불가라는 주장이나 전체 Goal의 blocker로 확대하지 않는다. 초록만으로 전체 방법·구체 실험·정확한 증거 계산·신규성을 전문 검수한 것으로 표시하지 않는다.

근거: [SRC-0001701](../sources/history-122.md#src-0001701) [[1, 74]]행, [SRC-0001703](../sources/history-122.md#src-0001703) [[1, 104]]행, [SRC-0001717](../sources/history-122.md#src-0001717) [[1, 30]]행.

## <a id="claim-40"></a>40. 원91과 이번 후보의 관계

원91은 이웃 입력의 역할 대응을 바꾸는 결정이었고 원92는 유한 context의 분포 공유·분리 증거다. 둘은 같은 알고리즘은 아니지만 최종 RCTL에 유용한 분할 결정과 global 대안 대비의 필요성이 미확인이라는 진입 조건을 공유한다. 기존 Tab 직접 예측의 긍정 증거와 일부 cell의 공간 입력 이득을 지우거나 이번 clustering 성공으로 세지 않는다.

근거: [SRC-0001661](../sources/history-122.md#src-0001661) [[3, 9], [23, 31]]행, [SRC-0001662](../sources/history-122.md#src-0001662) [[48, 65]]행, [SRC-0001704](../sources/history-122.md#src-0001704) [[7, 14], [33, 50]]행.

## <a id="claim-41"></a>41. snapshot·판독·판본 범위

snapshot34의 listed27files 3,471,029bytes에 manifest 5,718bytes를 더하면 physical28files 3,476,747bytes다. rootarchive 213bytes는 별도다. 이번에는 BHC8쪽 1258행·GP표지포함13쪽 1515행과 21전체이미지, PreqTorch3파일 641행·quantile1543행·재사용 regressor765행을 읽었다. 후보표는 50행 전체를 읽었으며 직전 판본과의 차이는 8행 삽입이다. 연혁 508행은 1–65행만 선택 판독했고 66–508행의 직접 미독을 유지한다. TXT 2개의 기계 대응·선택 판독, PNG 4개의 파생 시각검수·별칭·재독은 독립 내용을 중복 가산하지 않는다.

근거: [SRC-0001699](../sources/history-122.md#src-0001699) [[1, 143]]행, [SRC-0022084](../sources/history-122.md#src-0022084) [[1, 7]]행, [SRC-0001704](../sources/history-122.md#src-0001704) [[1, 50]]행, [SRC-0001708](../sources/history-122.md#src-0001708) [[1, 65]]행, [SRC-0001710](../sources/history-122.md#src-0001710) 판본·판독 범위, [SRC-0001712](../sources/history-122.md#src-0001712) 판본·판독 범위, [SRC-0001718](../sources/history-122.md#src-0001718) 판본·판독 범위, [SRC-0001719](../sources/history-122.md#src-0001719) 판본·판독 범위.

## <a id="claim-42"></a>42. 다시 검토할 조건과 남은 범위

재검토에는 실제 관측 조건의 어떤 손해를 줄이는 partition·정보·학습 결정을 바꾸는지, Tab값이 어떤 다른 결정을 만드는지, 단순 global 대안과 비교해 최종 RCTL에 무엇이 전달되는지를 먼저 명시해야 한다. 완전한 보장이 없다는 이유만으로 모든 실증 후보를 기각하지 않으며 관측되지 않은 운영 제약을 만들어 분리 필요성을 꾸미지 않는다. 원93 이후·이전 고유 판본·FedPPBC/DOCX·전체 실패 비용 통합·장기 접근·최종 원본 변경/검색 검수는 전체 Goal의 후속 범위다.

근거: [SRC-0001704](../sources/history-122.md#src-0001704) [[41, 50]]행, [SRC-0001700](../sources/history-122.md#src-0001700) [[1, 31]]행, [SRC-0001708](../sources/history-122.md#src-0001708) [[13, 15]]행.

## 팀 재검토 안내

동일한 점 예측 함수와 다른 관측 잡음을 구별하는 데 어떤 정보를 쓰는지, 그 구별이 단순 점 예측 비교와 다른 소속 결정을 만드는지, 유한 context의 Tab 이득이 최종 RCTL의 손해에 어떻게 연결되는지부터 작성한다. 같은 후보를 다른 loss나 모델 이름으로 다시 시작하기 위한 실행 지시가 아니다.

현재 연혁66–508행 및 직전 연혁56–498행의 직접 미독, TXT literal 미독 구간과 고유 표현 확인, BHC 기술보고/실제 구현·GP Additional1–4/R·C++/원자료·Preq 의존 모듈·workshop 전문, 원93 이후와 이전 고유 판본, FedPPBC/DOCX 공백, 전체 실패·비용 통합·장기 팀 접근·최종 원본 변경 및 대표 질문 검색 검수.
