# 73 문헌 추가 검토 — 예측 가능한 출력과 공동학습의 적용 조건

[72–75 통합 기록](0072-0075-output-compression.md) · [출처와 판본](../sources/history-072.md) · [검토 범위](../evidence/0073-forecastable-output/manifest.json) · [주장별 대조](../verification/history-072-claims.json)

**원문 독해와 작성 후 36개 주장 대조를 마쳤다.** 이 문서는 2026-09-26의 기록73을 보완하는 아카이브 기록이다. 새 모델 선정이나 실험 결과가 아니다.

## 당시 질문과 이번 검토 범위

<a id="c01"></a>**C01.** 원73의 질문은 제한된 자료에서 최종 RCTL을 호출하지 않고 예측에 유용한 cell 출력 방향을 찾을 수 있는가였다. 당시 문서는 ForeCA·GNN 공동학습·response dimension reduction를 검토한 뒤, “예측 가능한 성분”이나 “출력 압축” 자체를 신규성으로 주장하지 않았다. 새 학습·추론·수치 진단은0회였고 추천안도 확정하지 않았다. [당시 findings](../evidence/0072-0075-output-compression/originals/SRC-0022023.md.txt)

<a id="c02"></a>**C02.** 이번에는 ForeCA PDF9쪽·보충1쪽, mbrdr manual10쪽, 추가로 확보한 MBRDR2024 PDF12쪽(본문11쪽·백지1쪽)을 텍스트와 시각 자료로 읽었다. 보관 TXT19쪽과 원PNG3개도 대조했다. GNN 보관 코드3개와 같은 commit의 의존 코드7개를 정적으로 읽었다. 참고문헌 목록을 읽은 것은 그 논문들 전체를 읽은 것과 다르며, 과거의 부분 독해를 소급 변경하지 않는다.

## ForeCA: 스펙트럼 집중도와 조건부 예측 손실

<a id="c03"></a>**C03.** [Goerg, ICML2013](https://proceedings.mlr.press/v28/goerg13.html)의 ForeCA는 약정상 시계열의 정규화된 스펙트럼 엔트로피를 줄이는 선형 성분을 찾는다. 분산이 크다는 것과 예측 가능성이 높다는 것을 구분하지만, 특정 관측 입력 X·예측 horizon·최종 손실을 지정한 조건부 평균 추정 목적은 아니다. Gaussian 조건에서 스펙트럼이 시간 의존을 충분히 표현한다는 설명과 일반 비Gaussian 과정의 비선형 예측 가능성을 구분해야 한다(PDF2–4).

<a id="c04"></a>**C04.** 입력을 whitening한 뒤 단위벡터 w에 대해 스펙트럼 행렬을 투영한다. 현재 w가 만든 로그 가중 행렬의 최소 고유벡터를 반복 계산하고 여러 초기값 중 낮은 목적값을 고른다. 다음 성분은 앞선 방향의 직교 여공간에서 순차 추출한다(PDF4–6, 식16–27·§4.3). 순차적인 단일 방향 최적화를 모든 K차원 부분공간의 공동 전역 최적화로 설명하지 않는다.

<a id="c05"></a>**C05.** 연속 스펙트럼의 Ω와 유한 주파수 격자의 추정량 Ω-hat은 같은 범위를 갖는 수치가 아니다. 본문은 전자에 `[0,∞]`, 이산 추정량에는 `[0,1]`을 쓴다(식12·15). 모집단 white noise의 평탄한 스펙트럼과 유한 관측으로 추정한 스펙트럼도 구분한다. 실제 유한 표본에서 항상 정확히0이 나오거나 실수 정현파가 모든 양측 주파수 관례에서 정확히1이 된다고 단정하지 않는다.

<a id="c06"></a>**C06.** 수식을 구현할 때 주파수·확률 질량의 정규화를 먼저 확정해야 한다. 식7과18의 지수에는 각각 `ikλ`, `2πikλ`가 나오며, 식23·26·27의 주파수 합과 식24의 시작 인덱스도 다르다. [보충 증명](https://proceedings.mlr.press/v28/goerg13-supp.pdf)의 양의 준정부호 논리는 `−log(투영 스펙트럼) ≥ 0`를 사용한다. 이는 정규화된 이산 확률 질량에서는 성립하지만 임의의 연속 밀도나 다른 FFT 척도에 그대로 적용할 수 없다. 표기 차이를 원문 수정이나 알고리즘 전체의 기각으로 처리하지 않는다.

<a id="c07"></a>**C07.** Property3.2(c)의 혼합 성분 상한과 “등호는 계수0/1에서만 성립”한다는 문장은 구분해야 한다. 서로 독립인 단위분산 white noise 두 개를 `α²+β²=1`로 혼합해도 white noise이므로, 내부 계수에서도 두 Ω와 혼합 Ω가 모두0인 반례가 있다. 이는 확률모형을 새로 생성하지 않은 기호 대조다. 본문의 모든 시차에 대한 비상관 조건보다 보충의 `s≠t` 표기는 약하며, 동시점 공분산 조건도 필요하다. 상한 불등식 자체가 이 반례로 깨지는 것은 아니다(PDF3·보충1).

<a id="c08"></a>**C08.** 목적함수의 단조 감소와 하한은 목적값 수렴의 근거다. 이것만으로 고유벡터의 부호·중복 고유값 문제를 포함한 반복벡터 수렴이나 모든 시작점의 국소 최적성까지 자동 증명되지는 않는다. 본문 수렴 주장을 재사용하려면 정규화·고유값·정지 조건을 함께 명시해야 한다(PDF5, Theorem4.2). 이번 검토는 새 수렴 정리나 구현 실패 실험이 아니다.

<a id="c09"></a>**C09.** Fig1은 S&P500·Mount Campito·Nottingham의 Ω-hat을 각각 `1.25/14.99/34.37%`로 표시한다. 이는 해당 스펙트럼 추정의 지표이며 MAE 개선율이 아니다. PCA·SFA와의 관계도 분산·짧은 시차 상관·스펙트럼 전체라는 목적 차이로 읽어야 한다(PDF1–4).

<a id="c10"></a>**C10.** 금융 예시는8개 주식형 펀드의2002-01-01–2007-05-31 자료1,413관측을 사용한다. 첫 ForeC의 water·energy 계수는 `.72/.58`, 두 번째는 energy `−.53`, water `−.47`, mining `.55`, East Europe `.38`로 설명된다. “India보다 거의 두 배”는 예측 가능성 지표에 대한 서술이다. SFA가 더 단순하고 빠르다는 비교와 일부 긴 시차 구조를 ForeCA가 포착한다는 설명을 함께 보존한다. 이 그림은 통신 예측기의 독립 holdout 비교가 아니다(PDF6).

<a id="c11"></a>**C11.** 다른 예시는 미국48개 주의1982Q1–2011Q4 일인당 소득 성장이다. Fig3 캡션의 분기 성장과 PDF6 본문의 annual growth 표현 사이에는 표기 차이가 남는다. 전체 미국 성장을 뺀 자료에서 지역·연간 주기·저주파 성분을 해석한다. 미국 평균·표준편차 `1.32/.92%`, Ω `4.86%` 등의 수치는 이 자료의 설명값이다. 약30년 창에서 해석한25년 성분을 안정된 장기 주기나 인과 효과의 증명으로 확대하지 않는다. 금융 Fig2의 밀집 관측 인덱스와 소득 Fig4의 모든48성분 좌표를 개별 전사한 것은 아니다(PDF6–8).

<a id="c12"></a>**C12.** 재사용할 핵심은 예측 가능성과 분산을 구분하는 목적, whitening·스펙트럼 추정·순차 추출의 조건이다. WOSA 추정과 반복 초기화가 소개돼도 실제 예제의 모든 seed·재시작 횟수·원관측·실행 비용은 확보되지 않았다. 외부 선형 성분을 최종 RCTL의 출력으로 쓰는 효과와 전체 계산량은 별도 질문이다. [원문과 TXT·판본 대조](../evidence/0073-forecastable-output/format-audit.json)

## mbrdr: 목적·전처리·차원 선택을 분리한다

<a id="c13"></a>**C13.** 보관 manual은 [mbrdr1.1.1](https://cran.r-project.org/web/packages/mbrdr/mbrdr.pdf)이며 표지2026-05-08과 package Date/Publication2022-01-24를 구분한다. 현재 공식 PDF는 보관본과 바이트가 같다. manual의 Yoo2016/2018 표기와 Yoo–Cook2008의 잘못된 저널 표기는 그대로 보존하되, DOI는 *Computational Statistics & Data Analysis*53(2):334–343으로 식별한다. [2008 DOI](https://doi.org/10.1016/j.csda.2008.07.029)

<a id="c14"></a>**C14.** response reduction는 원래 출력의 조건부 평균을 보존할 부분공간을 찾는 문제다. 네 방법을 동일한 추정기로 취급하지 않는다. 공식 R 소스에서 `yc`는 응답·입력 공분산으로 방향을 만들고, `prr`는 응답 공분산의 고유벡터를 사용한다. `pfrr`는 전체·적합·잔차 공분산의 방향 후보를 순차 선택하며, `upfrr`는 잔차 공분산으로 변환한 적합 공분산의 고유방향을 사용한다. 이 계산을 유한 표본 RCTL의 손실 보장이나 무가정 비선형 학습기로 옮기지 않는다. [공식 소스 패키지](https://cran.r-project.org/src/contrib/mbrdr_1.1.1.tar.gz)

<a id="c15"></a>**C15.** `choose.fx`의1·2·3번은 실제로 `scale(X)`, 제곱항, 지수항의 표준화를 사용한다. 단순 중심화만 한다고 재구현하면 다르다. 4번은 **원 X**에 K-means를 적용해 `c−1`개 dummy를 만들며 이 분기에는 `scale(X)` 호출이 없다. 따라서 비선형 입력 basis를 사용할 수 없다는 주장은 틀리지만, 모든 분기가 같은 표준화를 한다는 주장도 틀리다. 이 K-means는 입력 sample의 basis 구성으로, 출력 cell의 소속과 다르다(manual2, R `choose.fx`).

<a id="c16"></a>**C16.** `SIGMAS`는 Y를 내부 중심화하고 `1/n`으로 공분산을 계산한다. 제공된 `fx`는 그대로 두고 `fx(fxᵀfx)⁻¹fxᵀ`로 투영한다. 사용자 입력 `fx`와 dummy에는 자동 중심화가 없으므로, 기본 `scale(X)`와 raw X가 상수항 없이 같은 투영을 만든다고 가정하지 않는다. rank가 부족할 때 자동 ridge나 일반화 역행렬로 보정한다는 근거도 없다(manual8–9, R `SIGMAS`).

<a id="c17"></a>**C17.** manual은 `mbrdr.x`가 rank 부족 열을 제거한다고 설명하지만1.1.1 소스는 `object$x`를 반환하는 accessor다. 전처리의 완전 rank 보장을 문서만 믿고 재사용하면 안 된다. 네 kernel에서 양의 비균등 weights가 가중 공분산에 사용되는 경로도 확인되지 않는다. weights는 행 필터·저장에 쓰이며 계산한 제곱근 변수는 적합에 연결되지 않는다. 이것은 지정 버전의 정적 관찰이며 실행 장애나 과학적 기각을 재현한 결과가 아니다.

<a id="c18"></a>**C18.** 문서의 `numdir=4`와 실제 반환 방향 수를 구분해야 한다. 각 방법은 기본 `num.d=r−1`을 사용하고 적합 결과의 방향 수를 다시 채택한다. 응답4개라고 항상4방향을 반환하는 구현이 아니다. `pfrr/upfrr`의 `evalues`에는 로그우도가 저장되어 `yc/prr`의 고유값과 뜻도 다르다(R `mbrdr.fit.default`, 각 `mbrdr.M.*`).

<a id="c19"></a>**C19.** `yc/prr`의 `stats`는 선택 고유값의 **뒤쪽 누적합에 n을 곱한 값**이다. 첫 항을 그 고유값 합으로 나누면 n이 된다. 따라서 이를0–1 설명분산 비율로 보고 `>.95`를 적용하는 차원 선택은 그대로 재사용할 수 없다. 출력 변수 이름이 같아도 누적 설명분산·검정 통계량·로그우도를 나눠 해석해야 한다(R `mbrdr.M.yc/prr`, `summary.mbrdr`).

<a id="c20"></a>**C20.** 카이제곱 표는 `pfrr/upfrr`에만 제공된다. 자유도는 각각 `q(r−m)`, `(q−m)(r−m)`이고 p값은 소수4자리로 표시한다. 표의 `0.0000`을 수학적 정확한0으로 쓰지 않는다. 함수가 선택 차원까지 자동 확정하는 것은 아니다. UPFRR 구현의 꼬리 로그우도 항은 음수부호이고 합의 상한은 `min(r,q)`다. 수식을 옮길 때 실제 구현과 원정리의 가정을 함께 확인해야 한다.

<a id="c21"></a>**C21.** 이번에 [Ahn·Yoo2024 출판사 PDF](https://pdf.medrang.co.kr/CSAM/2024/031/CSAM031-02-179.pdf)를 확보했다. 과거 TLS 실패는 당시 접근 기록으로 남긴다. 논문은 방법별로 서로 다른 공분산·선형성·정규성·부분공간 불변성 가정을 사용하므로 조건부 평균 보존을 무조건적인 보장으로 읽지 않는다. Table3의 두 번째 p값은 `.0704`, Table4의 네 p값은 `.3288/.4996/.7562/.8327`이다. α=.05에서의 기각 설명이 본문과 맞지 않는다. Table7의 두 번째 자유도5도 해당 공식의6과 다르다. p186의 차원 선택 예제는 C19의 구현과 함께 재검토해야 한다. 표기·설명 차이를 연구 방법 전체의 실패로 확대하지 않는다. 2008 원논문 전체와2018·2019 원정리의 검증은 여전히 별개다.

<a id="c22"></a>**C22.** manual의 학교 예제는1972년 Minneapolis63학교,15변수 중4응답·선택9입력이다. 통신 데이터나 미래 구간 예측 성능을 측정한 예제가 아니다. manual에는 실제 실행 출력·seed·비용이 없으며, 첫 참고문헌 연도·`A6` 설명·예제 주석과 코드의 `fx.choice` 차이는 원문 위치와 함께 남긴다. 패키지 설치·R 예제·원자료 역직렬화는 수행하지 않았다(manual1·6–9).

## GNN: 소속과 예측을 공동학습하는 구현

<a id="c23"></a>**C23.** 원73이 보관한 [공식 구현](https://github.com/NGMLGroup/Time-Series-Clustering-with-GNNs/tree/303c8cc6c5142aa1a4eab06677ce44104bd95355)은 commit `303c8cc6c5142aa1a4eab06677ce44104bd95355`다. README와 core3파일이 현재 그 commit에서 받는 바이트와 일치한다. commit의 README 오탈자 수정·서명 메타데이터는 실제 실험 완료 증거가 아니다. [OpenReview 논문](https://openreview.net/forum?id=MHQXfiXsr3)은 여전히 전체 PDF를 확보하지 못했으므로 다음 내용은 고정 구현의 정적 검토다.

<a id="c24"></a>**C24.** 흐름은 node 입력·시간 인코딩→시간 집계→GNN→pool→latent decoder→assignment로 lift다. `NodeEmbedding(n_nodes,K)`의 공유 학습 파라미터 S가 pool과 lift에 연결된다. 샘플마다 입력에서 새로 계산하는 assignment라고 설명하지 않는다. 예측 손실이 S에도 영향을 주므로 소속과 최종 예측의 공동학습이다. RCTL로 그대로 교체하면 당시 연구가 요구한 RCTL 독립 소속과 충돌한다(model/layers/utils 및 README 구조 그림).

<a id="c25"></a>**C25.** 두 runner가 지정한 예측 손실은 `MaskedMAE`; predictor의 train/validation은 예측 손실과 auxiliary loss를 합한다. `scale_target`에 따라 손실의 공간이 달라지고 test 경로는 역변환도 수행한다. 군집 평가의 NMI·homogeneity·completeness와 이 예측 MAE를 같은 결과로 취급하지 않는다. 이 코드 경로를 읽은 것이 실제 loss 값이나 최종 RCTL 성능을 확인한 것은 아니다.

<a id="c26"></a>**C26.** core는 MinCut·DiffPool·DMoN·asymmetric Cheeger의 네 regularizer를 제공한다. 행 softmax assignment를 군집 질량으로 다시 나눠 feature 평균을 만들고, lift는 온도 softmax 또는 forward에서 hard·역전파에서 soft인 straight-through를 사용한다. 출력이K개여도 인코더는 pooling 이전 모든N node를 처리하며 adjacency를 dense로 만드는 비용이 남는다. 출력 차원 비율만으로 전체 실행 시간·메모리 감소율을 계산하지 않는다.

<a id="c27"></a>**C27.** 저장 runner 설정은 hidden16, TCN2층·kernel3·dilation2, GNN2층, attention 집계,250epochs, Adam lr.001·weight decay.0001, gradient clip5다. synthetic는 window16/horizon1/batch16, CER는72/1/8이다. scaler 축은 `(0,1)`, splitter에는 validation/test 각각.1을 넘긴다. 실제 표본 시각과 scaler 적합 범위는 데이터·tsl 구현의 추가 확인이 필요하다. 이 설정은 실행 계획의 코드이며 실행 결과가 아니다.

<a id="c28"></a>**C28.** trainer는 epoch당 train100·validation50 batch로 제한하고 fit 후 S의 argmax 군집을 평가한다. 전체 runner는 synthetic 6종에서 K=5로 고정하고, CER에서는 K=2/5와 adjacency 6종을 조합한다. 각 설정을 5회 반복하고 점수 평균·`np.std`를 CSV에 쓰도록 되어 있다. 계획된 조합 수를 완료 실험 수로 세지 않는다. 두 runner에는 forecast test 점수 산출 호출·실제 비용 기록·훈련 반복 seed 지정이 없다.

<a id="c29"></a>**C29.** 최소 예제의 `--pool_loss`는 손실 계수 선택에는 쓰이지만 model의 `pool_method`는 `mincut`으로 고정돼 있다. 옵션 이름만 보고 DiffPool 등으로 알고리즘이 전환된다고 재사용하면 안 된다. `nopoolloss`도 auxiliary 계수만0으로 하고 MinCut 연산은 남는다. 전체 실험 runner는 README에서부터 MinCut 전용이므로 같은 옵션 불일치를 그 실험 전체에 적용하지 않는다.

<a id="c30"></a>**C30.** model·`predict_batch`는 예측과 auxiliary2개를 반환하지만 `predict_step/compute_metrics`는2개 변수로 unpack한다. 지정 경로에서 반환 개수가 맞지 않는 정적 불일치다. 그러나 두 runner는 그 메서드나 `trainer.test/predict`를 호출하지 않으므로 이것만으로 저자의 군집 결과가 실패했다고 주장하지 않는다. 실제 예외를 실행·재현한 기록도 아니다(predictor).

<a id="c31"></a>**C31.** CER 원자료는 별도 신청이 필요하다. loader는 결측값을0으로 채우고 실제 hourly resample에는 평균을 쓰며, mask·누락률 필터·거주/사업자 코드·other 제외·subset을 적용한다. 선언된 일반 집계 방식과 이 전처리 단계를 구분한다. 원자료·subset 배열을 읽거나 loader를 실행하지 않았으므로 최종N·기간·결측 비율을 새로 추정하지 않는다(cer_data, runners).

<a id="c32"></a>**C32.** synthetic loader는 저장 series가 없으면 `force_generate=False`여도 새로 생성·저장하는 경로가 있다. 생성 seed는 params에서 그래프·시간모형·잡음에 전달되며 훈련 반복 seed와 다르다. source의 단독 예제 `seed=42`를6개 데이터셋의 공통 seed로 쓰지 않는다. `allow_pickle='TRUE'`를 넘기는 params 로딩도 이번 정리에서는 실행하지 않았다. 코드 존재와 데이터 보존·재현 가능성을 분리한다(synth_data).

<a id="c33"></a>**C33.** CER의 데이터 기반 adjacency는 두 runner에서 시간 split 전에 `set_slice` 없이 만든다. 함수는 제공된 전체 시계열의 거리·상관·correntropy를 사용한다. identity/full/random 그래프는 이 상관 추정과 구분하며 random graph에는 seed0이 있다. 이를 엄격한 미래 구간 예측 평가에 재사용하려면 adjacency의 정보 범위를 다시 정해야 한다. 군집 평가 코드를 읽은 것만으로 논문의 정보 누출이나 무효를 확정하지 않는다(adj_construction, runners).

<a id="c34"></a>**C34.** README·환경은 Python3.12.8, torch2.5.1, PyG2.6.1, tsl0.9.4 등을 지정한다. README의 `main.py` 명령은 고정 tree에 없고 실제 진입 파일은 `run_experiment.py`다. 데이터 경로·신청·params와 손실 계수도 함께 확인해야 한다. 고정 구현의 참조 링크를 제공하는 것이 현재 환경의 설치 성공이나 학습 재현을 뜻하지 않는다. [외부 파일·해시·독해 범위](../evidence/0073-forecastable-output/external-sources.json)

## 팀이 재사용할 판단과 남는 범위

<a id="c35"></a>**C35.** 세 계열은 서로 다른 기존 근거를 제공한다. ForeCA는 분산과 예측 가능성을 구분하고, response DR는 조건부 평균을 보존하는 출력 부분공간을 다루며, GNN은 S와 예측을 공동학습한다. 원73의 남은 제안은 최종 RCTL과 독립적인 선정·동일 과거 정보·관측 target을 통한 추정 오차 보정·고정 비용에서의 효용이다. 보정 모멘트나 출력 압축 자체를 새 정리로 부르지 않고, latent target은 관측 Y의 변환으로 정의한다. [원72–75의 수식·저장 진단](0072-0075-output-compression.md)

<a id="c36"></a>**C36.** 같은 문헌을 다시 요약하기 전에 이 기록의 전처리·정보 의존·반환값·접근 공백을 확인한다. 다른 horizon·최종 예측기·선정 자료·계산 예산이나 수정된 공식 버전이 생기면 관련 주장만 재검토한다. GNN·2008 원논문 전체, 실제 실행 로그·비용·원자료와 저장 검색11개 등은 남아 있다. 새 학습·추론·역사 코드 실행은0이며, 이 문헌 묶음으로 전체 연구기록 정리 완료를 선언하지 않는다.
