# 예측 방법과 구현 버전을 재사용할 때의 경계

[21·22 기록](../records/0021-0022-literature-scope.md)과 [주장별 근거](../verification/history-014-primary-review.json)를 연결한다. 아래 내용은 지정 판본의 정적 검토이며 실행 결과가 아니다.

## FSA: 특징에서 생성하는 대상

[공식 v1](https://arxiv.org/html/2606.01289v1#S4)의 전역 추세·주기·잔차 통계와 국소 특징은22차원이다. MLP가 계수를 출력하며 Eq6은 AR 항만 재귀 적용한다. MA 계수·innovation scale을 출력한다는 사실만으로 완전한 확률적 ARIMA라고 부르지 않는다.

Eq7은 H 전체 평균 제곱 오차다. §4.4의 재추정에는 자체 생성한 예측값을 사용하고 추론 중 gradient 갱신은 하지 않는다. AR·MA 계수의 크기를0.96 한도로 제한하는 것은 일반 AR 정상성의 증명이 아니다. Figure2의 policy box는 `(c, ε, θ, σ, τ)`로 보이지만 caption·Eq3은 `(c, φ, θ, σ)`다. 원문 표기를 임의로 통일하지 않았고 저자 코드는 미확인이다.

[§5.1](https://arxiv.org/html/2606.01289v1#S5.SS1)은6개 source의104,807표본과7개 target,같은 source에서 처음부터 학습한 축소 baseline을 설명한다. T=96,H=24/48/96,p=3,K=3이며 다변량 자료도 독립 차원별 예측이다. 전체 성능표 수치 검산·공개 대형 checkpoint 비교·cross-series 상호작용 검증은 이번 근거가 아니다.

## TabICL: detrending과 target 변환

설치 자료·보존 ZIP·[고정 공식 코드](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/forecast/transforms/_seasonality.py)의 바이트가 같다. `_prepare_signal`은 추세를 제거한 신호를 FFT에 전달하고 `detect_periodicities`는 주기·크기 쌍을 반환한다. `AutoPeriodicEncoder`는 원 target과 sin/cos 열을 반환한다. [FourierEncoder](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/forecast/transforms/_calendar.py#L149)는 시간 행 위치에서 그 열을 만든다.

| 호출 경로 | detrend_type | max_top_k | exclude_zero |
|---|---|---|---|
| 기본 PeriodicDetectionConfig → AutoPeriodicEncoder | linear |5|True|
| detect_periodicities의 옵션 인자를 생략한 직접 호출 | first_diff |10|False|

따라서 이 detrending을 `Y−최근 관측`으로 적합 후 복원하는20번 기능과 혼용하지 않는다. [기존 설치 metadata 검수](../verification/history-005-primary-review.json)의2.2.0은 파일의 버전 확인이며 개별 과거 호출의 환경 lock을 새로 확보했다는 뜻이 아니다.

## TabPFN-TS: 고정한 세 commit

| 이번 확인 대상 | commit | commit 시각 UTC | pyproject의 tabpfn 하한 |
|---|---|---|---|
| v1.3.0 tag가 가리킨 commit |[4549578734ed](https://github.com/PriorLabs/tabpfn-time-series/commit/4549578734ed9786dc201005396dd8bc20161681)|2026-09-17 15:53:13|9.0.0|
| 2026-09-25 UTC 끝 이전 조회 후보 |[23c5e238670a](https://github.com/PriorLabs/tabpfn-time-series/commit/23c5e238670a1228b454f1306e909f1ddc07841e)|2026-09-18 12:03:09|9.0.0|
| 이번 조회의 main |[2c04a3486859](https://github.com/PriorLabs/tabpfn-time-series/commit/2c04a34868596b3cbb88c173759418a09994881c)|2026-10-02 10:00:11|9.1.0|

후보는 `until=2026-09-25T23:59:59Z` 조회 결과이며 원22가 실제 읽은 commit의 증거가 아니다. 세 [README](https://github.com/PriorLabs/tabpfn-time-series/blob/4549578734ed9786dc201005396dd8bc20161681/README.md)는 바이트가 같고 v1.3.0 news 날짜는9월15일이다. 같은 바이트의 [CHANGELOG](https://github.com/PriorLabs/tabpfn-time-series/blob/4549578734ed9786dc201005396dd8bc20161681/CHANGELOG.md)는9월16일,tag commit은9월17일이다. 어느 하나를 검증된 package 게시 시각으로 선택하지 않았다. 현재 pyproject 하한이 달라졌어도 README의9.0.0 설명은 같았다.

README는 LOCAL/CLIENT 기본 모델을 TabPFN-3.5로 설명하고 과거 TS-3 checkpoint를 별도로 선택할 수 있다고 안내한다. known-future covariate는 사용하고 past-dynamic/static은 버리며 다변량 target은 독립 단변량으로 나눈다고 명시한다. 이는 문서 확인이다. 실제 입력 처리 코드,3.5 모델 구조·checkpoint,표의 성능은 검증하지 않았으며 실행 예제도 수행하지 않았다. 예전 [TabPFN-TS 논문 검수](../records/0005-network-timeseries-audit.md)의 조건을 새 기본 모델로 소급 변경하지 않는다.

## 발견 단계 문헌과 운영 설명

[CDE v1](https://arxiv.org/html/2603.26611v1)의 초록·§1–2는 조건부 밀도 정확도와 calibration을 구분한다. methods·appendix와 그림은 아직 검수하지 않았으므로 분포 출력이 있다는 사실을 모든 조건에서의 calibration 보장으로 확대하지 않는다. [TabularMath v1](https://arxiv.org/abs/2602.02523v1)은 초록만 읽었다. 그 수치 보고를 우리 트래픽의 외삽 실패나 RCTL 공유 손해에 대한 직접 실험으로 인용하지 않는다.

[현재 공식 AGENTS 안내](https://learn.chatgpt.com/docs/agent-configuration/agents-md)의 프로젝트 지침 설명은 원22의 수정 종류를 이해하는 보조 근거다. 현재 문서는 당시 실행 로그가 아니며 파일을 만들었다는 사실로 미래 재개 성공을 보증할 수 없다.
