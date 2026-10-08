# 05 — 가까운 다섯 방법과 후보의 차이를 검토한 기록

05는 조건부 손실표 후보를 추천하기 전에 **기존 방법과 무엇이 같고, 어떤 계산을 생략했으며, 그 대가로 무엇을 확인해야 하는가**를 검토했다. 실제 공동 학습의 예측 이득, 교차 예측 오차, 학습 gradient, posterior 요약은 서로 다른 정보다. 손실표를 더하는 구현만으로 이 정보를 모두 대신했다고 판단하지 않았다.

이 페이지는 05 중 **가까운 다섯 방법과 후보의 주장 범위**를 정리한다. 원문 전체69행은 읽고 보존했지만, 네트워크·시계열9개 및 TabICL·관련6개 비교의 근거 통합은 후속 작업이다. 05 전체 완료나 전수 신규성 조사로 집계하지 않는다. [보존 원문](../evidence/0005/originals/SRC-0020826.md.txt), [출처·읽은 구간](../sources/history-003.md), [검수 범위](../verification/history-003.md)

| 항목 | 당시 기록과 이번 확인 |
|---|---|
| 기록 시점 | 원문 검색·확인일2026-09-25. 후보의 성능·신규성 확정 전 근거라고 명시 |
| 질문 | cell별 조건부 absolute-loss를 합산하는 소속 결정이 선행의 pooled prediction과 어떻게 다른가 |
| 당시 후보 | 각 cell 자신의 실제 query에서 분포를 추정하고, 같은 상태의 공유 보정값 비용을 합산. 후보 pair마다 pooled learner를 다시 학습하지 않음 |
| 당시 가설 | 조건부 분포가 정확하면 단일 관측 target보다 손실의 조건부 변동을 줄일 여지가 있음. 실제 추정오차가 있으므로 통계 효율 보장은 미확정 |
| 수행 종류 | 문헌·설계 비교 기록. 05만으로 새 모델 실행을 확정하지 않음. 이번 아카이브에서는 모델 학습·추론·논문 실험0 |
| 자료·분할·설정 | 독립적인 새 실험 조건은 해당 없음. 인용한 후보는 [B2의16cell·개발 query·손실표와 RCTL 조건](0004-0007-b2-observed-risk.md)으로 연결 |
| 당시 판단 | full distribution의 필요성, 실제 learner 효용, 신규성은 미확정. 검토 중이라는 문구를 보존 |
| 문헌 검토 비용 | 원문에 경과시간·메모리 미기록. 관련 traffic 계산 비용은 B2 기록의 별도 실행 범위 |

## 다섯 방법이 요구하는 정보

[문헌 비교표](../references/closest-pooling-methods.md)에 판본과 식 위치를 모았다. 핵심 차이는 이름보다 소속 결정에 사용하는 정보에 있다.

| 방법 | 실제 결정에 사용하는 정보 | 05 후보와의 차이 |
|---|---|---|
| HCP2025 | 알려진 출처의 집단을 분리/공동 적합하고 validation 손실이 가장 크게 줄어드는 쌍을 병합 | 손실표 후보는 이 pooled fit을 그대로 빠르게 계산한 것이 아님. HCP는 개선이 없으면 멈추지만 B2는 제한된 공유 보정의 증가 비용으로16→8→4를 구성 |
| Population-HCP2026 | 후보 population group의 posterior predictive 손실과 양의 pooling gain. 실제 실험은 단순 OLS/logistic plug-in | 수식의 Bayesian 계층과 실제 계산을 구분해야 함. 현재 손실표에 같은 불확실성 처리나 공동 적합 효과가 있다고 볼 근거 없음 |
| RMB-CLE | task별 predictor를 다른 task의 X/Y에서 평가한 cross-error profile | 자기 query만 쓰는 후보가 교차 예측 행렬을 정확히 재현한 것은 아님. 모든 쌍 평가를 줄이면 측정하는 대상도 달라짐 |
| ETAP | 전체 task 공동 모델의 gradient와 실제 subset 학습에서 얻은 MTL gain | 이 정보를 학습하는 절차를 RCTL 독립 후보에 그대로 도입할 수 없음. gradient 없이 같은 정보량을 확보했다는 주장은 미확정 |
| Posterior projection | 한 reference model의 posterior predictive sample을 단순 밀도·관측별 cluster 요약으로 투영 | cell별 회귀 자료의 공유나 RCTL 학습 이득을 직접 최적화하는 문제와 다름. 분포를 손실 기준으로 요약한다는 원리만으로 신규성을 주장하지 않음 |

HCP2025의 집단 내 iid·집단 간 독립 조건은 동시 network cell·시간 의존성에 자동으로 성립하지 않는다. 복잡도 정리도 OLS/RMSE와 특정 병합 조건에 한정된다. RMB-CLE의 회귀 위험에는 함수 차이와 target noise가 함께 남는다. 이 차이를 생략해 ‘분포 거리로 모든 negative transfer를 해결한다’고 요약하면 안 된다.

## 원문 대조에서 남긴 정정과 불일치

보존 원문은 수정하지 않았다. 아래 위치를 정리본에서 바로잡았으며, 방법의 실험 결과를 바꾼 정정은 아니다.

| 05의 인용 | 확인한 위치 |
|---|---|
| HCP2025 A2/A3를§2로 표시 | §1.1 |
| Population-HCP limitations를§5로 표시 | §6. §5는 Gapminder 적용 |
| ETAP grouping을§3.3으로 표시 | §3.2.3 |

Population-HCP2026의 소개는 HCP2025를 observation-level covariate clustering으로 설명하지만, 2025 원문은 출처가 알려진 집단을 묶는다. 05가 이미 지적한 이 차이를 원문으로 재확인했다. 후속 논문의 표현으로 이전 방법을 축소하지 않는다. [HCP2025 공식 원문](https://link.springer.com/article/10.1007/s11222-025-10683-x), [Population-HCP 공식 원문](https://link.springer.com/article/10.1007/s41060-026-01197-4)

Population-HCP의 Gaussian simulation은 local RMSE1.034→proposed1.018, mixed simulation은 연속값1.025→1.018·binary 오분류0.252→0.253을 보고한다. Gapminder에서는 proposed가 local보다 두 분할 모두 높다: random3.31/2.91, forward5.21/4.77년 RMSE. **논문에 실린 값의 대조이며 이번에 재현한 실험이 아니다.** 설정과 표 값은 [지정 원문 검토 기록](../verification/history-003-primary-review.json)에 보존했다.

같은 논문의§5.3·§6에 있는 ‘local이 최저’ 서술은 random split의 Table6과도 맞지 않는다. 표에는 mixed-effects2.73이 local2.91보다 낮게 나온다. PDF15쪽의 표와 Figure2를 함께 확인했다. 따라서 clustering이 local보다 높다는 확인과, 모든 방법 중 local이 항상 최저라는 설명을 구분한다. 이 논문의 실험에서 사용한 보수적 pooling을 임의 시계열의 무해성 보장으로 옮기지 않는다.

## 후보의 실제 결과와 연결하는 방법

05는 full distribution이 다음 주 surrogate에서 empirical보다 조금 나았지만 단순 median/IQR 또는 PCC보다 낫지 않았고, pair 손해 순위도 약했다고 적는다. 해당 손실표와 pair 진단은 [04·06·07 기록](0004-0007-b2-observed-risk.md)에서 저장값에 대조했다. 05의 ‘검토 중’ 문구를 RCTL 통과로 읽으면 안 된다. 07에는 empirical 대비 두 seed에서 RCTL이 악화되어 추천에서 제외한 판단이 있다.

05는 각 cell의 실제 입력에서 추론한다는 점을 강조한다. 다만 B2 전체 경로의 정보 사용 범위는 구현까지 보아야 한다. **Tab 추론에는 query Y를 넘기지 않았지만 공통 action 격자에는 query Y가 참여했다.** 05의 설계 설명을 정답 없는 전체 알고리즘으로 확대하지 않는다. 유한 표본에서 pooling이 줄이는 추정 변동을 놓칠 수 있다는 질문은 [08·09](0008-0009-finite-sample-pooling.md)의 반례·진단으로 이어진다.

## 재사용과 재검토 조건

팀원은 같은 원리를 새로 제안하기 전에 다섯 방법의 **묶는 단위, X/Y 접근 범위, 실제 공동 적합 여부, 소속 수 결정, 최종 learner와의 연결**을 비교하면 된다. 선행의 명칭만 바꾸거나 posterior·비선형·계층 병합이라는 표현만 더하는 것은 새 실험의 차이가 아니다.

재검토하려면 기존 labels가 있는 상황에서 추정 분포가 추가로 주는 정보, 제한된 공유 함수군과 실제 RCTL의 차이, 유한 표본 효과 또는 독립 평가 조건을 명시한다. HCP의 validation gain, ETAP의 gradient/gain, RMB-CLE의 cross-error를 생략하면서 같은 보장을 주장하려면 별도 근거가 필요하다. 이 기록은 후보 채택이나 새로운 실험 실행 지시가 아니다.

원문69행·같은 해시 사본 관계·다섯 문헌의 실제 검토 범위를 재사용할 수 있다. 논문 전문·원저자 코드·모든 표·증명은 이번 검수 대상이 아니다. 남은 05의 network/TabICL 비교와 이후 기록은 [과거 시도 색인](../prior-attempts.md)의 미완료 범위로 유지한다.
