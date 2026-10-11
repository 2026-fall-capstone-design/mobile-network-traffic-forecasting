# 정답 지연·PPI·예측기 적응을 구분하는 문헌 비교

[원94 기록](../records/0124-delayed-target-inference-boundaries.md)과 [실제 판독 범위](../sources/history-124.md)를 함께 사용한다. 표의 방법은 당시 확보한 판본 기준이다. 현재 자료에서 구현·재현하거나 전체 proof를 독립 검증한 것은 아니다.

| 자료와 확인 위치 | 실제 추정·행동 | 현재 적용할 때 확인할 점 |
|---|---|---|
| [PPCI2603.05575v2](https://arxiv.org/abs/2603.05575v2), §2.4/3/4/5/6.1–6.2·AppendixE | RKHS 국소 weight, 표지 잔차와 미표지 예측 moment, 조건부 functional 추론; ω로 예측기 기여 조절 | iid·같은 입력 marginal·분리/cross-fit, abundance·식별·bias 조건. shared-design 분석은 일반 serial-dependence 보장이 아님. v2 simulation의 f_q는 입력만 사용함. |
| [Reliable Algorithm Selection, ICML2025](https://proceedings.mlr.press/v267/fannjiang25a.html), §2–3/Algorithm1–5·A.1·B.2·D.1 | 후보 design의 예측 평균에 held-out density-ratio 가중 잔차를 더하고 여러 population criterion을 검정 | 공통 P(Y\|X), 모델 학습 자료와 독립인 표지 자료. 유한 표본 범위/D, 알려진 ratio, 미지 정규화 상수의 점근 절차, 추정 ratio 실험을 구분. 아직 학습하지 않은 RCTL risk와는 다른 대상. |
| [ADAPT-Z2509.03810v2](https://arxiv.org/abs/2509.03810v2), §3/4/5·B/C/G/H/I | 현재 feature와 관측 후 과거 gradient로 feature correction; cache·adapter/head 갱신 및 frozen online 변형 | encoder/head 구조와 학습된 feature 사용. RCTL 결과로 clustering하는 것은 당시 조건 변경. horizon12/24/48와1/24/48 표기 차이 미확인. 비용은 논문 환경의 결과이며 전 조건 우수·현재Tab/RCTL 실측은 아님. |

입력분포만 바뀌고 조건부 정답 법칙이 유지되는 covariate shift와, 같은 입력 뒤의 미래 정답 관계가 바뀌는 conditional drift를 구별한다. 정확한 입력 밀도비로 잔차를 가중해도 후자의 변화 항은 남는다. 현재 h1의 실제 대기 입력은 cell당 한 행이며, 공간·시간 pooling은 독립 표본을 자동 생성하지 않는다.

모델에 정답을 제공하지 않는 offline query와 정답 자체가 아직 관측되지 않은 운영 시점을 구분한다. 재검토 시에는 실제 관측시각, target horizon/부분 완성, 미표지 입력의 대표성과 의존성, 추정 대상에서 소속 결정으로 이어지는 경로와 전체 비용을 적는다. 작은 탐색의 진입 기준은 [원93](../records/0123-candidate-gates-comparison-scope.md), 모든 정답이 있는 같은 query 보정은 [기존09](finite-sample-pooling.md)에 연결한다.

원94의 현재 후보 보류는 모든 PPI·지연 예측의 실험 실패가 아니다. PDF174page 중 선택49page를 읽었고 나머지125page와 literalTXT 직접 판독은 남아 있다. 논문 공식 코드 실행/감사와 새 모델 실행은0이다.
