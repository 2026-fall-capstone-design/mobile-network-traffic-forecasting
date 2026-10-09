# 51·55 — beam 예측의 특징과 도로 정보의 재사용 조건

ITU beam 예측은 시간적 거리에 따라 특징을 다르게 쓰는 강한 표형 기준을, *Cellular Predictions on the Move*는 도로 flow·speed를 추가하는 조건과 반례를 보여 준다. 두 연구를 새 cell clustering이나 RCTL 공동 학습의 검증으로 옮기지 않는다. 특히 두 번째 연구의 target은 실제 도로 관측으로 만든 **모의 통화량**이다.

이번 기록은 [51 계획](../evidence/0051-0055-gotsf-audit/originals/SRC-0021746.md.txt)과 [55 §1–2](../evidence/0052-0054-partial-observation/originals/SRC-0021824.md.txt)의 ITU·Cellular 판단을 원문에 연결한다. 55의 GOTSF 부분은 [앞선 기록](0051-0055-gotsf-audit.md), 작은 부분 관측 실험은 [52·54 기록](0052-0054-partial-observation.md)에 있다. 51·53·55 전체 문헌 검토와 종합은 계속 진행 중이며, 이 아카이브의 새 학습·추론·모의자료 생성은 0회다.

## 문헌과 실제 검토 범위

| 문헌 | 고정 서지·읽은 범위 | 사용할 때의 경계 |
|---|---|---|
| Stephen Kolesh·Thomas Basikolo, *Enhancing network resource management through machine learning for spatio-temporal beam-level traffic forecasting* | [ITU 공식 PDF](https://www.itu.int/dms_pub/itu-s/opb/jnl/S-JNL-VOL6.ISSUE4-2025-A27-PDF-E.pdf), Vol.6 Issue4, 2025년 12월, 337–352쪽. SRC-0063290 텍스트 16쪽·시각 확인 12쪽 | 논문의 특징·표·평가 설명 검토. 원 구현·원 예측의 독립 재현 아님 |
| Natalia Vesselinova·Pauliina Ilmonen, *Cellular Predictions on the Move: What about Data?* | [arXiv 2606.25709v1](https://arxiv.org/abs/2606.25709v1), 2026-06-24. SRC-0063265 텍스트 12쪽·시각 확인 10쪽, Figure1–9·TableI–IX 포함 | PDF 상단의 LaTeX 견본 연도 2020은 이 논문의 발표 연도가 아님 |
| ITU 원 challenge | [Zindi 문제 설명](https://zindi.world/competitions/spatio-temporal-beam-level-traffic-forecasting-challenge), 2026-09-26 저장 HTML SRC-0063304 | 보이는 텍스트와 현재 연결 그림 5개 확인. 현재 그림 바이트가 당시 저장 시점과 같다는 증거는 없음 |

전체 텍스트 **28쪽**과 시각 자료가 있는 **22쪽**을 읽고, 주요 결론·선택 수치를 다시 대조했다. 수학적 증명 전체 인증, 저자 코드의 실제 실행, 독립적인 성능 재현을 뜻하지 않는다. 페이지·해시·파생 텍스트·입수 기록은 [출처 안내](../sources/history-033.md), 수치 계산은 [검수](../verification/history-033.md)에 있다.

## ITU: 자료의 단위와 입력 시점을 먼저 고정

논문 §4.1과 Zindi 설명의 단위는 **30 BS × 3 cell × 32 beam = 2,880 beam**이다. 목표는 시간당 DLThpVol이며, DLThpTime·PRB·MR_number가 함께 제공된다. 논문은 이들을 채널 활성 시간·PRB 사용률·사용자 수로 설명하지만, 실제 물리 단위·익명화/정규화·beam 합산의 중복 여부를 이 검토에서 독립 확인하지 않았다. 2,880개를 cell 수로 재명명하지 않는다.

앞 5주를 사용해 week6과 week11을 예측한다. 사이의 관측 공백을 지우고 두 평가 주를 연속 시계열로 잇지 않는다. Zindi 그림의 표준 MAE는 `sum(abs(y - pred)) / (B × T)`이다. GOTSF의 값 구간별 zero-mask 지표와 같은 수치로 합치지 않는다. 저장 설명의 public/private 약 30/70% 구분도 시간순 검증의 증거가 아니며, ITU 논문의 Leaderboard MAE가 어느 leaderboard 부분인지 표만으로 확정하지 않는다.

| 항목 | 원문 조건 | 재사용 시 확인할 것 |
|---|---|---|
| 짧은 horizon | target·PRB·사용자 수의 1–4시간 lag, 168/336시간 rolling, expanding, 집계 특징 | 예측 시점에 실제로 알 수 있는 값인지 확인. week6 전체 예측에 필요한 lag 공급 방식은 원 코드 미확인 |
| rolling | §4.3은 1주를 추가 shift하여 t−168 이전 자료를 쓴다고 설명 | 윈도 길이와 shift를 혼동하지 않음 |
| expanding | 식8은 i=1,…,t−1의 합을 t−1로 나누며 현재 target을 제외 | 본문 표현만 보고 현재 y_t 포함이나 구현 누출을 단정하지 않음 |
| 먼 horizon | 단기 lag·expanding·불안정 encoding을 빼고 달력·안정적 집계 사용 | 실제 적용 특징 목록과 생성 순서를 코드로 확인해야 함 |
| fold-aware target encoding | 각 fold를 나머지 K−1 fold의 통계로 표현하고 test에는 전체 train 통계 사용 | 자기 행 target 제외와 과거 시점만 사용하는 조건은 다름 |
| 성능 CV | §5.2.3의 10-fold는 BS별 층화로 모든 fold에 30개 BS의 표본을 포함 | 기지국 holdout이나 순방향 시간 CV로 읽지 않음 |

sqrt target으로 학습하고 평가 전에 역변환한다. 따라서 MAE는 제공 target의 원 척도에 대한 논문 수치이며, 단위가 bytes/Mbps로 확인된 측정값은 아니다. Table2의 LightGBM은 long learning_rate0.0205·n_estimators1000, short0.0830·5000이며, 두 CatBoost 열은 learning_rate0.020218465729343698·depth9·iterations15000을 포함한 7개 설정이 같다. 별도 Optuna 탐색을 했다는 설명과 동일한 최종 설정을 함께 보존한다. seed·실제 탐색 횟수·patience·전체 학습 시간/하드웨어는 확인되지 않았다. Figure8–9의 fold0 곡선을 총 비용으로 계산하지 않는다.

## ITU: 전체 개선 문구와 표의 반례

Table1의 기준 수치는 주최측 결과를 인용한 것이다. 이번 논문이 모든 기준 모델을 같은 환경에서 다시 학습했다는 증거로 쓰지 않는다. 아래는 Table3·4의 **Leaderboard MAE**다.

| Horizon | 모델 | 단일 특징 pipeline | horizon별 특징 pipeline |
|---|---|---:|---:|
| W6 | LightGBM | 0.1926 | 0.1925 |
| W6 | CatBoost | 0.1918 | 0.1919 |
| W11 | LightGBM | 0.2302 | 0.2262 |
| W11 | CatBoost | 0.2356 | 0.2262 |

Ensemble은 `0.6 CatBoost + 0.4 LightGBM`으로 W6 **0.1919**, W11 **0.2261**이다. W6에서는 단일 CatBoost 0.1918보다 나쁘며, horizon별 CatBoost와 같다. 본문의 모든 개별 모델보다 우수하다는 표현을 그대로 일반화하지 않는다.

W6 ensemble의 **11.40%**는 Transformer **0.2166** 대비이고, 가장 좋은 제공 기준 iTransformer **0.1967** 대비는 **2.44%**다. W11의 가장 좋은 제공 기준 Transformer **0.2331** 대비는 **3.00%**다. Table5의 30개 개선율은 Table1·4의 인쇄값으로 재계산했을 때 소수 둘째 자리까지 일치했다. 이는 원 예측 출력의 검증과 다르다.

해결하지 못한 불일치는 다음과 같다.

- Figure6의 W6 값은 LightGBM0.1919·CatBoost0.1925로 Table4의 0.1925·0.1919와 뒤바뀌어 있다. W11 그림은 세 모델 모두0.2261, 표는 두 개별 모델0.2262·ensemble0.2261이다. 위 비교는 **Table3·4 기준**이라고 명시한다.
- Table4의 W6 LightGBM `LB−CV=0.0012`는 본문의 차이가0.001 미만이라는 문구와 맞지 않는다.
- p2에서 iTransformer/PatchTST/DLinear에 붙인 참고번호19/20/21은 p15 참고목록의 TFT/Informer/Autoformer와 다르다.
- Figure11의 `_7` 특징명과 본문의 ‘과거7시간’, 168/336시간 rolling 설명은 원 코드 없이 같은 뜻으로 통일하지 않는다. Figure1의 관측 profile과 Figure10의 예측 profile은 서로 다른 맥락이므로 BS 순서가 다르다는 이유만으로 오류로 단정하지 않는다.

## Cellular: 실제 도로 관측과 모의 통화 target

실제 PeMS 도로 flow·speed를 쓰되, US50-E 구간의 센서 간 거리를 가상의 BS 범위로 가정하고 통화량을 생성한다. 실제 통신망에서 관측한 bytes·Internet activity·처리량이 아니다. Pollock Pines에서 South Lake Tahoe로의 단방향 도로 흐름을 가정한다. 입력 flow는 해당 5분에 들어온 차량 수이며, cell 안에 남아 있는 전체 차량 수와 구분한다. target은 신규 통화와 handover 통화의 합이다.

각 차량의 신규 통화는 Poisson 과정으로 평균 5분에 1회 생성한다. 통화 지속시간은 평균1분 exponential 또는 같은 비중의 두 lognormal(각각 평균1분과10분, 분산3과30)로 설정하고 속도를 이산화한다. 이 설정을 새로 실행하거나 모의 표본을 생성하지 않았다.

| 항목 | 논문에 기록된 조건 | 남은 확인 |
|---|---|---|
| 자료 | 2022-03-28~09-09, weeks13–36의 24주, 월~금, 하루288개의 5분 관측 | 실제 운영 BS mapping과 원 시뮬레이션 출력 미확인 |
| 모델 | LSTM 1층·16 cells, 선형 1출력, RMSProp·MSE | seed·epochs·batch size·소프트웨어 버전·실행 비용 미확인 |
| 이력/목표 | 과거6개 표본(30분)으로 다음5분 통화량 예측 | 미래 road 관측을 입력으로 제공했다고 단정하지 않음 |
| 기본 분할 | 24주를 시간순12:6:6으로 나눈 후 shuffle | window 생성·정규화 fit 범위·split 내부 shuffle 구현 미확인 |
| 비교 | Calls 이력 vs Calls+flow+speed, 같은 기간·장소·모델 설정 | 수치의 실제 정규화와 원 통화량 척도는 명확히 확인되지 않음 |
| 반복/집계 | TableIII–V는 5회, TableVI–IX는 10회의 min/median/max | 표의 중앙값 차이를 독립 실험 여러 개나 평균 이득으로 세지 않음 |

## Cellular: 개선과 악화가 공존하는 조건

24주 TableIII·IV의 8개 BS×4개 지표×2개 지속시간 분포, **64개 중앙값 비교**는 모두 Calls+flow+speed 쪽이 낮다. “약60%”는 일부 조건의 MSE 이득이며 모든 BS·MAE·학습 기간의 보장이 아니다. 예를 들어 exponential의 BS3054051 MSE 인쇄 중앙값은0.600→0.234로 약61% 감소한다.

정밀도가 낮은 표에서 계산한 값과 저자가 보고한 더 정밀한 개선율은 구분한다. 표시된 마지막 자리의 반올림 범위와 개선율 자체의 반올림 범위를 함께 대조했다. 8개 지표별 최솟값·최댓값 범위 중 **exponential MAE 최댓값**은 설명되지 않는다. 본문35.74%와 달리 BS317706의 TableIV 중앙값0.162→0.103은 **약36.42%**다. 두 MAE가 소수 셋째 자리로 반올림되었다면 이 행의 이득은 약35.91~36.92%로, 본문의35.74%와 겹치지 않는다. 원 출력이 없어 어느 값을 정정해야 할지는 확정하지 않는다.

7주(weeks27–33)를3:2:2로 나눈 짧은 학습에서는 **BS320287**의 금요일 반례가 있다. 아래 수치는 TableVI·VIII의 **중앙값**이며, `Calls → Calls+flow+speed` 순서다.

| 지속시간 분포 | 평가일 | MAE | MSE |
|---|---|---:|---:|
| Lognormal 혼합 | week32 금요일 | 0.235 → 0.363 | 0.100 → 0.522 |
| Lognormal 혼합 | week33 금요일 | 0.219 → 0.209 | 0.087 → 0.114 |
| Exponential | week32 금요일 | 0.232 → 0.348 | 0.105 → 0.518 |
| Exponential | week33 금요일 | 0.230 → 0.200 | 0.099 → 0.123 |

두 번째 금요일에는 MAE가 낮아져도 MSE·RMSE는 나빠진다. TableVI의 week32 Calls MSE에서0.101은 최댓값이고 중앙값은0.100이다. 아카이브 최초 내부 메모의 열 혼동을 공개 전에 바로잡았다.

4:1:2로 바꾸면 학습에 week30이 들어간다. 저자는 이 기간의60mph 미만 속도 구간이 학습에 추가되는 것으로 개선을 설명하며 Figure9에 이를 표시한다. 아카이브에서 이 원인을 통제 실험으로 입증한 것은 아니다. BS320287의 TableVI–IX 전체의 160개 일별 중앙값 쌍은 개선148·악화11·동률1이다. 이는 **표 비교 수**이며 실제 독립 학습 실행 수가 아니다. 4:1:2에서도 TableVII week33 월요일 MAPE는80.98→82.96으로 악화하고, 수요일119.5는 동률이다.

노이즈 실험은 flow에 “5%” Gaussian 오차를 넣되 target은 원래 flow로 만든다. 정확한 σ 정의와 원 난수는 미확인이다. TableV를 Calls 기준과 비교한 64개 중앙값은 모두 개선하지만, noise가 모든 지표를 일률적으로 악화시킨다는 뜻도 아니다. 원 시뮬레이션·학습을 실행하지 않고 표만 대조했다.

추가로 p9 본문의6주 표현은 weeks27–33 및3+2+2의7주와 다르다. p4의 상관 예시 BS320287과 Figure4 왼쪽 caption BS320280도 다르다. TableVII week32 화요일·수요일의 추가 입력 쪽 min/median/max 12개 인쇄값이 동일하며 실제 출력의 출처는 미확인이다. MAPE의 큰 값은 보존하되, 분모0 처리나 원 정규화 구현을 추정하지 않는다.

## 당시 판단과 팀의 재검토 조건

55는 ITU 결과를 달력·lag가 포함된 강한 표형 기준의 근거로 사용했고, Cellular는 실제 입력과 실제 target을 구분하는 근거로 사용했다. 이 범위는 원문과 맞는다. 두 논문을 TabICLv2 소속 점수의 추가 정보나 RCTL pooling 이득으로 승격하지 않는다. 저자가 제안한 자원 배분·지속가능성·에너지 효과와 실제 측정된 운영 이득도 구분한다. ITU의 자원 제어는 구현 결과로 확인되지 않았고, 본문에서 예고한 모델 크기·지연시간의 정량 비용표도 확인하지 못했다.

재사용할 것은 원문이 명시한 비교 질문과 조건이다. 팀 실험에서는 beam/cell·물리 단위, target이 실측인지 모의인지, 예측 시 입력의 가용 시점, 시간순 분할과 정규화 fit 구간, 정확한 feature builder·seed·비용을 먼저 고정한다. 같은 대상·척도에서 달력/lag 기반 단순 회귀와 비교하고, 전체 오차뿐 아니라 cell·기간·지표별 손해를 함께 남긴다. 소속 수정의 질문이라면 같은 정보와 평가 기간을 유지한 채 최종 RCTL 공동 학습 결과까지 별도로 평가해야 한다. 이 문장은 후속 설계 기준이며 새 실험의 실행 지시가 아니다.

원문과 인쇄표 검수로 같은 문헌을 처음부터 다시 요약할 필요는 줄였지만, 구현 재현이 끝난 자료로 사용해서는 안 된다. 51의 Frontiers·event 원문,53의 관측/telemetry 문헌,55의 전체 신규성 종합, 원 데이터/가중치의 팀 접근과 나머지 연구기록은 남아 있다. [주장별 근거](../verification/history-033-claims.json)와 [보존·출처 명세](../evidence/0051-0055-network-forecasting/manifest.json)를 함께 확인한다.
