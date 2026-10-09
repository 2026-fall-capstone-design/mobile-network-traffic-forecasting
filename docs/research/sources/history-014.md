# 21·22 출처와 실제 읽은 범위

[기록](../records/0021-0022-literature-scope.md)·[manifest](../evidence/0021-0022-literature/manifest.json)·[원본 매핑](../catalog/history-014-sources.jsonl)을 연결한다. 줄 번호는 해당 SHA의 UTF-8 `splitlines()` 기준1부터다.

| 원문 | 실제 읽은 범위 | 보존·검수 범위 |
|---|---|---|
| SRC-0021095:21 종합 |1–72행|H012 원본 재사용; 이번은57–62행 문헌,누적 비용 전체는 남음|
| SRC-0021116:22 접근 범위 |1–22행|새 원본 보존; 당시 읽기·미검토·운영 보고의 한계까지 연결|
| SRC-0000455:초기 AGENTS |1–9행|새 원본 보존;같은 바이트의15개 목록 항목을 별칭 연결|
| SRC-0000001:현재 AGENTS |1–27행|642 보존본 재사용;초기 사본과 다른 후속 개정 이력. 과거 명령은 실행 지시가 아님|

새 원본2개는3,768바이트다. 기존2개를 재사용하며 논문·외부 라이브러리 코드는 일괄 복사하지 않았다.

| 문헌 | 저자·공식 제출일 | 판본 | 실제 확인 범위 |
|---|---|---|---|
| FSA: Feature to Dynamics: Feature-space to Autoregression strategy for Zero-shot Time Series Forecasting | Wu, Yifan; Wu, Junjie; Wu, Kai; Zhang, Xiaoyu; Lou, Jian · 2026/05/31 | [v1](https://arxiv.org/html/2606.01289v1) · [PDF](https://arxiv.org/pdf/2606.01289v1) | 초록; HTML S3, S4, S5.SS1; PDF 3,4,5,6,7 |
| CDE: Benchmarking Tabular Foundation Models for Conditional Density Estimation in Regression | Izbicki, Rafael; Rodrigues, Pedro L. C. · 2026/03/27 | [v1](https://arxiv.org/html/2603.26611v1) · [PDF](https://arxiv.org/pdf/2603.26611v1) | 초록; HTML S1, S2; PDF 시각 열람 없음 |
| TabularMath: TabularMath: Evaluating Computational Extrapolation in Tabular Learning via Program-Verified Synthesis | Cheng, Zerui; Liu, Jiashuo; Yao, Jianzhu; Viswanath, Pramod; Zhang, Ge; Huang, Wenhao · 2026/01/25 | [v1](https://arxiv.org/html/2602.02523v1) · [PDF](https://arxiv.org/pdf/2602.02523v1) | 초록; HTML 본문 없음; PDF 시각 열람 없음 |

FSA의 지정 HTML 수식은 MathML alttext에 대조했고 PDF 물리3–7쪽을 시각 확인했다. §5.3은7쪽 이후로 계속되므로 전체 절 완료가 아니다. Tables1–3을 본 것과 모든 성능 수치를 전사·검산한 것은 구분한다. CDE의 Figure1은 텍스트 caption만 접근했고 그림을 평가 근거로 사용하지 않았다. TabularMath는 본문 방법·프로토콜을 읽지 않았다. **전체 논문 검토 완료는0편**이다.

세 PDF의 정확한 SHA는 기존 목록에 없었다. 이것으로 다른 로컬 판본의 부재를 단정하지 않는다. 공식 서지·HTML·PDF·추출문 hash와 확보 시각을 manifest에 기록하고 외부 자료에 가상 SRC 번호를 부여하지 않았다.

TabPFN-TS는 세 commit의 README133행·CHANGELOG51행·pyproject134/135행을 정적으로 읽었다. 동일 바이트를 재사용하면 고유 텍스트 버전은4개다. 링크된 method-overview 이미지와 실제 모델 코드·checkpoint는 미검수다. tag·날짜 이전 후보·조회 시 main을 서로 구분한다.

TabICL `_seasonality.py` SRC-0047594 전체443행과 `_calendar.py` SRC-0047592의149–190행은 설치본·ZIP member·고정 공식 코드 바이트를 대조했다. `_forecaster.py` SRC-0047586의254–266행과 설치metadata SRC-0047644의Name/Version은 H005 검수 범위를 재사용한다. 현재 설치본이 모든 과거 실행의 로드 자산을 증명하지는 않는다.

MGSTC/PID/QoS는 [H011 지정 구간](history-011.md)을 재사용한다. 공식 AGENTS 문서는 도입·guidance discovery·project instructions 절만 현재 시점에 확인했다. 과거 앱 동작과 미래 자동 재개 시험은 미확인이다. 원래22의 확인 범위를 이번 추가 열람과 혼동하지 않는다.
