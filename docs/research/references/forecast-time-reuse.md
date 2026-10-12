# 예측 시간 재사용 — 원97 비교 기준과 문헌 범위

[원97 저장 결과](../records/0127-forecast-time-reuse-diagnostic.md) · [당시/현재 문헌 범위](../evidence/0127-forecast-time-reuse-diagnostic/literature-scope.json) · [원95 동시 batch](serving-cost-baseline.md)

| 방식 | 재사용 대상 | 원97과의 관계/확인 범위 |
|---|---|---|
| 출력 유지/증가량 유지 | 같은 cell의 과거 최종 예측/한 시간 증가량 | 저장예측으로192행 비교; 매시간 현재 관측 유지; 내부 출력 정확성 보장 없음 |
| Delta Networks | 고정 행렬 결과·GRU 내부 preactivation | 공식PDF2–4 전체 이미지/§2–4 확인; 현재 RCTL 구현/논문 전체·공식 코드 검증 없음 |
| Skip RNN | 학습에 따른 recurrent state update 생략 | 공식 제목·저자·초록·판본/서지만 확인; 전체 gate 알고리즘/PDF/공식 코드 미확인 |

Daniel Neil, Jun Haeng Lee, Tobi Delbruck, Shih-Chii Liu, **Delta Networks for Optimized Recurrent Network Computation**, ICML2017/PMLR70:2584–2593. [공식 서지](https://proceedings.mlr.press/v70/neil17a.html) · [공식PDF](https://proceedings.mlr.press/v70/neil17a/neil17a.pdf). §2 식2–5는 고정W의 이전 결과와 입력 변화량으로 같은 선형 결과를 계산한다. §3은 GRU 내부에 적용한다. §4의 양의 threshold는 근사이며 마지막으로 기억한 값과 누적 오차를 다룬다. 출력 오차가 같은 threshold로 제한된다는 보장은 없다. 이 조건을 원97 최종 출력 근사의 정확성이나 RCTL speedup으로 대입하지 않는다.

당시 기록은 web reader 확인/로컬 PDF 다운로드0이었다. 이번 별도 확인에서 공식PDF10페이지877,727bytes의 hash와2–4페이지 이미지를 확인했다. 나머지 페이지·모든 실험/그림·공식 구현의 전수 검증은 아니다. 외부 PDF/PNG/TXT를 저장소에 재배포하지 않고 서지·범위·공식 링크만 제공한다.

Victor Campos, Brendan Jou, Xavier Giro-i-Nieto, Jordi Torres, Shih-Fu Chang, **Skip RNN: Learning to Skip State Updates in Recurrent Neural Networks**, ICLR2018. [공식 arXiv1708.06834v3](https://arxiv.org/abs/1708.06834v3)는2017-08-22 제출/2018-02-05 개정이다. 현재 확인은 제목·초록·서지/판본까지다. 당시 OpenReview 확인 화면을 현재 접근 실패로 쓰지 않으며 상세 알고리즘 재현을 주장하지 않는다.

후속 후보는 fixed clock/최근값/persistence, 하나의global에서 필요한cell만 계산하는 방식과 기본batch를 포함한다. 실행 시점에 사용 가능한 자료, 전체/기간/cell별 손해, Tab이 바꾸는 유용한 결정과 clustering의 필요성, 관측/준비/cache/Tab 추가비용을 함께 적는다. 새 실험은 다른 질문과 조건을 먼저 명시한다.

후속 [원98 정보량/공동 목적](../records/0128-quantile-information-and-pooling-objective.md)은 새로운 모델 계산 없이 유한 자료 추정의 이득을 검토했다. 예측 시간 재사용의 실제 latency와 중앙값 정보의 기호 주항은 다른 근거다. [밀도·grouping 비교](quantile-information-and-grouping.md)에 목적·의존 조건·재추정 범위를 연결한다.
