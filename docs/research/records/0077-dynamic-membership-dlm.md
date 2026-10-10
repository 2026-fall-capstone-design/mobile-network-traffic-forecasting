# 77 보완: 동적 소속 DLM의 원문과 저장 구현

[당시 판단](0076-0079-learning-decisions.md) · [출처](../sources/history-077.md) · [구현 대조표](../evidence/0077-dynamic-membership/implementation-review.md) · [검수](../verification/history-077.md)

시간에 따라 cell 소속을 바꾸는 아이디어를 다시 검토한다면, 전체 구간을 보고 복원한 소속과 예측 시점에 사용할 수 있는 배정을 먼저 구분해야 한다. 이 논문은 시간별 소속과 시간적 안정화의 선행 사례다. 우리 트래픽에서 별도 RCTL을 함께 학습할 cell을 선택하는 효과까지 입증한 자료는 아니다.

**22개 핵심 주장의 작성 후 원문 대조를 완료했다.** 아래 코드 관찰은 정적 독해이며 설치·import·모델 실행으로 얻은 결과가 아니다.

## 무엇을 읽었는가

<a id="c01"></a>**C01.** 원77의 DLM 논문 27쪽을 본문·수식·그림·참고문헌·Appendix A까지 읽었다. 저장 README 10행과 Python 3개 파일 1,260행, commit/tree JSON 전체를 대조했다. 저장되지 않은 보조 코드 2개·381행은 같은 고정 커밋에서 보완했다. 원77의 다른 두 논문과 저장 검색·TXT·원 PNG·PyPI/repository JSON은 이번 완료 범위에 포함하지 않는다. [자료 범위](../sources/history-077.md)

<a id="c02"></a>**C02.** 논문은 Sartório·Fonseca의 *Dynamic Clustering of Time Series Data*, arXiv:2002.01890v1이며 PDF의 판본 표기는 2020-01-28이다. README가 직접 연결하는 `victhorio/dynmix`의 저장 커밋은 `bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e`다. 2025년 출판본, PyPI 1.1.2, 저장 Git 커밋을 같은 판본으로 합치지 않는다. 뒤의 두 판본은 이번에 본문·배포 파일을 대조하지 않았다. [2020 논문](https://arxiv.org/abs/2002.01890v1) · [고정 README](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/README.md)

## 필터링과 사후 소속은 사용하는 정보가 다르다

<a id="c03"></a>**C03.** §2의 정적 mixture는 시계열 하나의 전체 구간에 소속을 두고, §3은 시점별 소속 확률과 잠재 소속을 둔다. 각 cluster의 관측·상태 전이에는 Gaussian DLM을 사용한다. cluster 수 K는 주어진 조건이며 자동 K 선택이나 시간에 따라 K가 달라지는 문제는 이 논문의 완료된 방법으로 제시되지 않는다. 논문의 K를 우리 UPC 개수나 최종 RCTL 개수와 자동으로 동일시하지 않는다. [논문](https://arxiv.org/abs/2002.01890v1), p3–4·9–12·21

<a id="c04"></a>**C04.** Theorem 1의 forward 갱신은 이전 Dirichlet 모수에 discount δ를 곱한 뒤 현재 잠재 소속의 one-hot 값을 더한다. δ는 소속 변화의 안정성을 조절한다. `dirichlet.forward_filter`도 같은 재귀 형태다. 다만 이 함수의 입력은 잠재 소속 관측이며, 함수 이름만으로 바깥 추정 과정 전체가 예측 당시 정보만 사용한다고 판정할 수 없다. [코드](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/dirichlet.py#L18-L40), 논문 p10–11

<a id="c05"></a>**C05.** Theorem 2는 전체 구간의 정보 D_iT를 조건으로 뒤에서 앞으로 소속을 추정한다. 코드의 `backwards_sampler`와 `backwards_estimator`도 마지막 시점에서 시작해 이후 시점의 소속을 이전 시점 계산에 사용한다. 따라서 전체 평가 구간을 넣어 얻은 과거 소속을 그 시점에서 가능했던 예측 배정으로 취급하면 안 된다. 예측 origin 이전의 학습 구간 안에서 smoothing하는 것 자체를 잘못으로 판정하는 것은 아니다. [역방향 코드](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/dirichlet.py#L43-L67), 논문 p11–12

<a id="c06"></a>**C06.** 논문의 소속 확률은 해당 시점의 관측과 cluster DLM의 likelihood를 사용한다. 소속을 얻는 일과 아직 관측하지 않은 미래 시점에 모델을 배정하는 일은 다르다. 원77의 “미래 배정에는 예측 origin에서 이용 가능한 별도 규칙이 필요하다”는 판단은 이 정보 범위와 부합한다. DLM 소속을 RCTL 학습 자료의 공유 이득으로 연결하려면 추가 근거가 필요하다. [당시 원문](../evidence/0076-0079-learning-decisions/originals/SRC-0022032.md.txt), 17–21행

## 논문이 실제로 보여준 결과

<a id="c07"></a>**C07.** EU 재생에너지 사례는 1990–2015년 연별 자료에서 Malta를 제외하고 K=2 random-walk DLM으로 변화하는 소속을 설명한다. Gapminder 사례는 142개 국가 중 유럽·아프리카 82개, life expectancy와 log GDP의 두 변수, 1952–2007년 5년 간격 자료다. 이런 사례의 분류·평활 곡선은 트래픽 held-out MAE나 RCTL 개선 표가 아니다. [논문](https://arxiv.org/abs/2002.01890v1), p13–20

<a id="c08"></a>**C08.** Gapminder의 n=82, m=2, T=12, K=2 조건에서 점추정 약 2분, MCMC 약 10배라는 시간은 논문 보고다. Appendix A의 정적 인공 예는 시계열 20개에서 5초 대 9분 38초, 전환 시계열 2개를 더한 동적 예는 1분 18초 대 14분 23초를 보고한다. 이는 현재 환경의 실측도, 통신 cell 규모에서의 속도 보장도 아니다. [논문](https://arxiv.org/abs/2002.01890v1), p19·24–26

<a id="c09"></a>**C09.** 동적 인공 예는 기존 20개 시계열에 δ=0.95, 추가한 전환 시계열 2개에 δ=0.5를 사용한다. Figure 20은 전환 부근 t=37–42의 소속 불확실성을, Figure 21은 독립 소속과 EDP의 이상치 처리 차이를 보여준다. 설명 예의 효과를 모든 이상치 제거·일반적인 예측 향상으로 확대하지 않는다. 수렴 진단에 관한 서술도 논문의 보고이며 원체인과 정확한 실행 환경은 이번에 확보하지 않았다. [논문](https://arxiv.org/abs/2002.01890v1), p25–27

## 고정 구현을 그대로 가져오기 전에 확인할 차이

<a id="c10"></a>**C10.** 저장 README와 세 Python 파일은 tree JSON의 Git blob SHA-1과 모두 일치한다. commit JSON은 2020-04-10의 dynamic sampler 수정 한 파일, 12행 추가·2행 삭제를 담는다. “m > 1 수정”이라는 커밋 메시지는 모든 다변량 경로의 정상 동작을 검증한 결과가 아니다. tree의 19개 항목을 읽은 것 역시 전체 저장소의 19개 파일 전문을 읽은 것과 다르다. [출처 검증](../evidence/0077-dynamic-membership/source-identity.json)

<a id="c11"></a>**C11.** 저장 점추정 함수의 기본값은 바깥 반복 10, M-step 최대 반복 100, Monte Carlo 200, 수치 기준 1e-6이다. 소속용 δ는 독립 mixture 결과에서 초기화되고 c0=0.1을 사용한다. DLM 상태 진화의 기본 discount 0.7은 이 소속 δ와 다른 매개변수다. sampler 기본 2,000회도 논문 사례의 실제 반복 수로 소급하지 않는다. [dynamic.py](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/dynamic.py#L18-L93) · [dlm.py](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/dlm.py#L572-L664)

<a id="c12"></a>**C12.** 점추정의 흐름은 잠재 소속 Monte Carlo → Dirichlet forward/backward → 소속 가중 DLM 적합이다. 그런데 같은 커밋의 `common.compute_weights_dyn`은 인자로 받은 η를 likelihood에 곱하지 않고 정규화한다. 논문의 η를 포함한 소속 조건식 및 sampler의 η×density와 차이가 있다. 이를 확인하려고 보조 코드를 보완했으며, 이번에 과거 논문 결과의 실제 생성 경로나 이 차이의 성능 영향을 검증한 것은 아니다. [common.py](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/common.py#L92-L129), 논문 p11–12

<a id="c13"></a>**C13.** `backwards_estimator`의 설명은 mode 추정을 말하지만, 실제 마지막 시점과 각 역방향 시점은 `mod_dirichlet_mean`을 호출한다. 중간 변환의 S에는 mode 계산이 들어가므로 이를 정확한 전체 posterior mean 알고리즘이라고도 단정하지 않는다. 논문 §3.2의 backward modes 설명과 저장 구현의 mean 호출을 분리해 보존한다. [dirichlet.py](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/dirichlet.py#L178-L250)

<a id="c14"></a>**C14.** `dynamic_weighted_mle`는 시점별 소속 weight가 1e-3보다 큰 관측만 남기고, Kalman filter 뒤 smoother로 상태를 갱신한다. 분산 계산은 가중 제곱 잔차에 T를 나눈 뒤 전체 weight 합과 prior 항으로 다시 나눈다. 이 정규화는 재사용 전에 식과 대조해야 할 항목이다. smoothing과 작은 weight 제외는 코드에서 확인했지만, 분산식의 통계적 타당성이나 원 결과에 미친 영향을 실행 검증하지 않았다. [dlm.py](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/dlm.py#L610-L664)

<a id="c15"></a>**C15.** 입력 규격은 T×(n·m)이고 보조 코드가 series i의 m개 열을 묶는 index map을 만든다. 반면 sampler의 likelihood에는 `Y[t,i]`라는 단일 열 접근이 남아 있다. 모든 weight가 0인 경우에도 부호 있는 잔차의 합을 `argmin`하므로 주석의 “가장 가까운 cluster”와 거리 계산이 같지 않다. 다변량 접근과 0-weight 분기의 정적 차이를 남기되 실행 실패를 관측했다고 기록하지 않는다. [sampler](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/dynamic.py#L207-L228) · [입력 규격](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/common.py#L40-L89)

<a id="c16"></a>**C16.** 선택적 `model_delta=True` 경로는 `sample_delta`를 호출한다. 그 하위 marginal 계산은 c0=0.01을 사용하며 과거 Z와 현재 Z의 차가 0이 아닐 때 항을 더한다. 이는 forward 함수의 같은 소속 좌표에 누적하는 재귀 및 sampler의 c0=0.1과 대조할 조건이다. 기본 `model_delta=False`인 실행에 이 선택 분기의 영향을 자동으로 적용하지 않는다. [dirichlet.py](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/dirichlet.py#L253-L303)

<a id="c17"></a>**C17.** sampler는 smoother에서 얻은 시점별 주변 평균·공분산으로 상태를 각각 뽑고, 마지막에는 저장된 chain을 그대로 반환한다. burn-in 제거라는 주석과 달리 그 반환부에 절단은 없고 `means()`도 전체 저장 반복을 평균한다. 따라서 자동 burn-in 제거 또는 상태 경로의 joint backward sampling 구현이라고 단정하지 않는다. 별도로 정밀도 Gamma shape의 `sum(n_j)*T+1`도 관측 수와 대조할 미검증 항목이다. [dynamic.py](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/dynamic.py#L245-L277)

<a id="c18"></a>**C18.** 보완한 `common.initialize`는 전체 Y의 거리로 대표를 고른다. 저장 코드는 대표들과의 거리 중 최댓값을 쓰고, cluster별 F·G가 다를 때의 대표 배정은 TODO로 남긴다. 논문 p8–9의 초기화 절차를 이 코드가 모두 구현했다고 표시하지 않는다. `independent.estimator`도 DLM smoother를 호출하므로 그 이름의 “independent”를 미래 관측과의 독립 또는 시점별 온라인 추정으로 해석하지 않는다. [common.py](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/common.py#L213-L293) · [independent.py](https://github.com/victhorio/dynmix/blob/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e/dynmix/independent.py#L17-L71)

## 원문 차이와 재검토 조건

<a id="c19"></a>**C19.** 인쇄본에서도 남는 차이를 임의로 고치지 않았다. p6의 관측 항 시간 합·cluster 합 상한 표기, p10의 합과 곱 순서, Figure 4의 시작 연도와 축, p20 Morocco의 2017년과 자료 종료 2007년, Figure 13의 캡션과 본문 국가명이 대조 대상이다. 표기 차이의 목록이지 방법 전체가 실패했다는 결론은 아니다. [상세 위치](../evidence/0077-dynamic-membership/implementation-review.md#인쇄본의-미해결-표기)

<a id="c20"></a>**C20.** 이 자료에서 우리 cell·UPC partition·RCTL의 seed, train/validation/test 경계, 정규화, MAE와 전체 비용은 해당 연구 결과로 제공되지 않는다. 외부 논문의 일부 시간은 보고돼 있으나 저장 코드와 각 그림을 연결하는 실행 명세·원체인·환경은 아직 미확인이다. 입력 코드의 기본값, 논문 보고, 현재 검수에서 실행하지 않은 일을 구분한다. [재사용 범위](../evidence/0077-dynamic-membership/README.md)

<a id="c21"></a>**C21.** 원77은 “동적 소속을 새 핵심 구조로 추가하지 않는다”고 판단했으며, 동적 clustering 분야 전체를 부정하지 않았다. 이번 원문 대조는 시간적 안정화의 선행 사례와 예측 시점 정보 구분을 뒷받침한다. 이번에 발견한 저장 코드 차이를 당시 미채택의 원래 이유로 소급하지 않는다. 또한 이 기록만으로 DynaSTar·Liu 등 원77의 다른 근거까지 검수 완료로 바꾸지 않는다. [당시 원문](../evidence/0076-0079-learning-decisions/originals/SRC-0022032.md.txt), 69–77행

<a id="c22"></a>**C22.** 재진입하려면 예측 origin에서 이용 가능한 입력, 조건에 따라 바뀌는 공유 이득, 같은 정보를 받는 global·단순 달력 분할과의 차이, Tab이 바꾸는 결정, 기존 RCTL bank 또는 재학습과의 연결을 명시해야 한다. 동적 소속·EDP·DLM·soft membership·sample routing의 관련 기록을 함께 찾아, 결정 단위가 같은 질문을 이름만 바꿔 반복하지 않도록 이 조건을 먼저 확인한다. 아직 실행한 새 실험은 없으며 나머지 원77 자료와 전체 연구 아카이브 정리는 계속된다. [과거 시도 색인](../prior-attempts.md)
