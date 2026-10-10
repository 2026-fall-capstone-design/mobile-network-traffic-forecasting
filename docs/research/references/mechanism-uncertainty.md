# 관계 차이·추정 불확실성 문헌 비교

[28번 기록](../records/0028-mechanism-uncertainty.md)의 판단을 지정 원문 구간과 연결한다. 2026-09-25의 검토를 2026-10-09에 대조했으며 최신판 전체 조사나 성능 재현이 아니다. [판본·해시·읽기 범위](../evidence/0028-mechanism-uncertainty/manifest.json)와 [주장별 한계](../verification/history-020-primary-review.json)를 함께 확인한다.

## TabMGP

Ng·Fong·Frazier·Knoblauch·Wei, **TabMGP: Martingale Posterior with TabPFN**, arXiv `2510.25154v3` (2026-05-28), ICML 2026. [고정 PDF](https://arxiv.org/pdf/2510.25154v3)

§2–3와 Algorithm 1은 예측분포에서 정의한 통계량 posterior를 생성한다. X는 확장된 경험분포에서 뽑고 생성 Y를 context에 누적한다. [고정 minimal 코드](https://github.com/weiyaw/tabmgp/blob/bf44db185f75e0d619967e99527dd41d83065868/tabmgp_minimal.py)의 `x_prev`와 일치한다. §3.2의 유한 경로 안정성·coverage·수축과 §6의 한계를 구별한다. 높은 모델 복잡도에 대한 martingale 보장이나 트래픽 lag의 적용 보장은 확인되지 않았다.

E.1의 추가 500 steps·100 draws, 회귀 ensemble 8, 본문 약 200초/회귀 sample/L40S는 같은 단위가 아니다. “관계 추정의 불확실성”이라는 목적만으로 이 비용과 가정을 생략하지 않는다. 원문 28의 `§5.1` 대신 확보한 v3의 실제 §5와 E.1을 참조한다.

## Predictive CLT / UD

Fortini·Ng·Petrone·Rousseau·Wei, **Uncertainty Decomposition for Bayes-Filtered Transformers via Bayesian Predictive Inference**, arXiv `2602.04596v2` (2026-07-19). [버전 정보](https://arxiv.org/abs/2602.04596v2), [HTML 원문](https://arxiv.org/html/2602.04596v2)

§4의 일반 `γ` 추정식과 적용에서의 `γ=1` 가정을 구별한다. Appendix B는 초기 CDF가 정해지지 않은 상황에서 k=2부터의 prefix 차이를 사용한다. [posterior.py](https://github.com/weiyaw/ud4pfn/blob/ccd10bd3aa4b2002a6867e8f854282948c8a6036/predictive_clt/posterior.py)의 분모는 n−1이다. [TabICL adapter](https://github.com/weiyaw/ud4pfn/blob/ccd10bd3aa4b2002a6867e8f854282948c8a6036/predictive_clt/tabicl_adapter.py)는 이미 회귀 분위수로 CDF를 구성한다. 존재 확인과 실행 호환성은 다르다.

Theorem 5.2의 covariate 독립 조건과 5.3의 CLT 조건을 분리한다. 5.1은 compact target 공간·equicontinuity·부호 있는 조건부 drift 꼬리합을 가정한다. 5.3은 이에 별도의 속도·moment·극한 조건을 더하며 5.2의 추가 독립 조건은 요구하지 않는다. F.2/F.3에서 그 역할을 확인했지만 전체 증명을 독립 확증하지 않았다.

Appendix A/B/J.1/J.6의 설정·비용을 확인했다. 700 GPU-hours는 coverage 전체이며, Vₙ의 prefix 방식과 Uₙ의 Monte Carlo 1,000 draws는 별도다. 코드 기본 100을 논문 실험 1,000으로 덮어쓰지 않는다.

## Vario

Sarah Mameche·David Kaltenpoth·Jilles Vreeken, **Discovering Invariant and Changing Mechanisms from Data**, KDD 2022. [저자 PDF](https://www.sarahmm.com/papers/2022-kdd-discovering.pdf), [DOI](https://doi.org/10.1145/3534678.3539479)

Assumption 4.1과 Definition 4.2는 같은 DAG, 부모·환경과 잡음의 독립, group 안에서 조건부분포가 같은 partition을 다룬다. context는 환경이다. local model이 고정되면 데이터 기술 비용은 partition 선택에서 상수이며, 공통 계수·개별 편차·모델 수의 비용으로 공통성과 차이를 비교한다.

Algorithm 1/3은 공변량 부분집합의 환경별 회귀와 partition 탐색을 연결한다. greedy 방식은 이전 k−1 최적 분할의 한 group을 나눈다. Appendix B의 ordered heuristic O(d|C|³), greedy O(d|C|²)는 전체 공변량 부분집합 탐색과 구별해야 한다. Theorem 4.5의 유계 영역·함수 공간·분포 조건을 생략한 임의 비선형 또는 유한 표본 보장은 아니다. Figure 6의 OOD 실험도 관측 환경들에 남아 있는 기전이라는 설정을 갖는다. 저자 구현과 network traffic·RCTL 성능은 이 검수 범위에 없다.

## Two-stage global forecasting

Junru Ren·Shaomin Wu, **Boosting Global Time Series Forecasting Models: A Two-Stage Modelling Framework**, ECAI 2025, pp. 2969–2976. [기관 PDF](https://kar.kent.ac.uk/111229/1/FAIA-413-FAIA251157.pdf), [DOI](https://doi.org/10.3233/FAIA251157)

§3.1–3.2는 global residual의 Ljung–Box 검사, residual 특징·k-means, VAL 제곱 오차와 유지 비용 조건의 분할 선택을 연결한다. 실험은 p<.05, K≤10이며 Type I은 additive/auto-ARIMA, Type II는 multiplicative/추가 층이다. Figure 1/Algorithm 1은 첫 L−1층 복사·고정으로 기술하고 §4.2는 global weights/structure 고정 뒤 dense 한 층 추가라고 쓴다. 마지막 층의 정확한 처리까지 통일해 설명하려면 코드 확인이 필요하다. [코드 링크](https://github.com/R-jr-star/Two-stage-modelling-framework)의 내부는 검토하지 않았다.

월별 Tourism/Hospital/CIF/M3, train의 10% VAL, one-step rolling이다. 보고 지표는 누적 prefix 오차의 평균이므로 Milan 시간별 MAE와 같지 않다. Table 2에도 모든 조건 개선은 아니다.

| 논문 Table 2의 조건 | global MLP | two-stage | 방향 |
|---|---:|---:|---|
| Hospital / mean RMSE / Type II | 20.674 | 20.926 | 악화 |
| Hospital / mean MAE / Type II | 17.651 | 17.816 | 악화 |
| CIF / mean RMSE / Type I | 293090.638 | 308556.696 | 악화 |

이 세 행은 논문 표의 시각 대조이며 실험 재현이 아니다. Friedman p=.096은 논문의 α=.1 기준이며 .05에서 유의하다고 바꾸지 않는다. Proposition 1의 로그 손실 함의는 [원문 28의 산술 반례](../verification/history-020-logic-check.json)와 함께 본다. Proposition 2의 유효 표본 수 대입을 임의 시계열 의존의 보장으로 읽지 않는다. 이 한계들이 모든 residual 방법의 기각을 뜻하지 않는다.

## ECAI 후속 검수 — 63–65

[H055 기록](../records/0063-0065-ecai-interface.md)에서 Fig.3(d)의global forecast입력선행,저장TypeII의normalized실제target·hidden/input Add구조·전후잔차정의차이,표1–6의손해·비용을추가대조했습니다. 위코드미열람은H020당시범위입니다. 공개2파일을정적으로읽었지만Fig.3(c)/(d)전체재현·원실행로그는여전히미확인입니다.
