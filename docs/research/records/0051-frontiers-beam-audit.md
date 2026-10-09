# 51 — 희소 beam 트래픽의 공동 학습과 비교 조건

Frontiers의 GRU-MTL은 **beam의 0/nonzero 분류와 트래픽량 회귀를 함께 학습**한다. 같은 목적을 다시 제안하기 전에 참고할 선행 방법이지만, cell clustering·관측 대상 선택·TabICLv2 소속 수정·최종 RCTL 성능의 검증은 아니다. 표에서 확인되는 이득과 본문의 과장된 일반화, 서로 다른 평가 조건을 함께 보존한다.

이 자료는 [51 검토 계획](../evidence/0051-0055-gotsf-audit/originals/SRC-0021746.md.txt)에 관련된 `network_scope_51` 수집 묶음에 있다. [55 판단](../evidence/0052-0054-partial-observation/originals/SRC-0021824.md.txt)은 Frontiers를 직접 지명하지 않는다. 이번 원문 검토를 당시 55의 채택·기각 근거였다고 소급하지 않는다. 55의 event 문헌 접근 공백만 이 기록 말미에 연결한다. 기존 [GOTSF](0051-0055-gotsf-audit.md), [ITU·Cellular](0051-0055-network-forecasting.md), [52·54 부분 관측](0052-0054-partial-observation.md) 기록과 함께 읽는다.

## 문헌과 검토 범위

Israel Tommy·Taoreed Akinola·Xiangfang Li·Lijun Qian, *Spatio-temporal beam-level traffic forecasting in 5G wireless systems using multi-task learning*, Frontiers in Communications and Networks 6:1658461, DOI 10.3389/frcmn.2025.1658461, **2025-10-24 발표**. [공식 본문](https://www.frontiersin.org/journals/communications-and-networks/articles/10.3389/frcmn.2025.1658461/full)과 [공식 PDF](https://www.frontiersin.org/journals/communications-and-networks/articles/10.3389/frcmn.2025.1658461/pdf)를 연결한다. 저장 HTML의 `citation_online_date=2025/08/25`는 PDF의 수락일에 해당하며 발표일로 사용하지 않는다.

2026-09-25 저장 HTML의 보이는 텍스트 **805줄**을 읽었다. 빈 span 때문에 추출에서 빠진 수식은 저장된 JSON hydration 자료의 MathML을 정적으로 복구해 읽었다. 118개 항목에는 글머리표·inline 숫자·중복 표시가 포함되며, 서로 다른 방정식 118개가 아니다. 표시 수식 12개를 PDF와 대조했다. 추적 JavaScript를 실행하지 않았다.

2026-10-09 추가 취득한 PDF는 텍스트 **17쪽 전체**, 시각 자료가 있는 **10쪽(2–9·11·12)**을 읽었다. Figure1–13·Table1–5·Algorithm1·식1–10을 포함한다. 현재 PDF를 과거 HTML과 같은 바이트의 사본으로 취급하지 않으며, 과거 원격 그림의 바이트 동일성은 미확인이다. [출처 안내](../sources/history-034.md)와 [검수](../verification/history-034.md)에 원본·추가 취득·실제 열람 범위를 나눠 기록했다. 저자 코드 실행과 독립 성능 재현은 하지 않았다.

## 데이터·시간 분할·입력 가용성

| 항목 | 논문에 기록된 조건 | 재사용 시 남은 확인 |
|---|---|---|
| 관측 단위 | 30 BS × 3 cell × 32 beam = **2,880 beam**, 5주·840시간 | 2,880 cell이나 독립 시간 표본으로 바꾸어 부르지 않음 |
| 크기 | 지표별 2,419,200개 beam-hour 값 | 2,880×840의 산술. 원자료 전체를 재계수한 결과가 아님 |
| 지표 | DLThpVol·DLThpTime·DLPRB·MR_number | 물리 단위·익명화·합산 중복 여부와 실제 활성 입력 채널 미확인 |
| 희소성 | 평균 약915개 zero·1,965개 nonzero beam, 약31.8% | 915/2,880≈31.77%와 부합. 그림의 근삿값이며 원자료 독립 집계 아님 |
| 분할 | **앞 4주 train / 5번째 주 test** | 주최측 week6·week11 평가와 구별 |
| 입력 길이 | 8·24·168시간의 sliding window | 세 값은 입력 이력 길이. 서로 다른 forecast lead를 비교한 표가 아님 |
| 추론 | 4주차 마지막 입력 창에서 시작하여 자기 예측을 다시 넣는 recursive 방식 | 실제 feedback 채널·window 이동·공변량 공급 구현 미확인 |
| 정렬 | 명시적 timestamp가 없어 행 index로 네 파일이 이미 정렬됐다고 가정 | 실제 시각·파일별 정합성 검증 완료로 옮기지 않음 |

Figure1의 caption은 BS당 **3 users·user당32 beams**라고 적지만 본문 §1.1은 **3 cells·cell당32 beams**라고 적는다. 그림은 예시이며 실제 BS/cell/beam mapping의 증거로 쓰지 않는다. Figure2–4의 선택 시계열 축은 0~1로 보이지만 그 사실만으로 물리 단위나 학습용 정규화 방법을 확정할 수 없다.

입력 설명에는 두 공백이 있다. §4.1.1(p13)은 정규화·표준화·결측치 대체 없이 zero를 의미 있는 값으로 유지했다고 설명하지만 **Algorithm1(p11)은 입력 normalize/scale을 명시**한다. 또 네 지표를 모두 설명하면서 Fig6/§3.3의 입력은 `672×2880`이고, p16은 PRB·time·user count 사용 확대를 미래 과제로 둔다. 실제 사용 채널·전처리·그 fitting 범위를 원 구현 없이 통일하지 않는다.

## 모델과 실제 설정

공유 GRU의 마지막 표현에서 회귀 head와 zero/nonzero 분류 head로 갈라진다. 식6은 sigmoid 출력을 반올림한 이진 mask, 식7은 그 mask와 회귀값의 원소별 곱이다. 식8–10은 회귀 MSE와 분류 BCE를 가중 합한다. 이 구조는 beam의 활성 여부를 다루며, 학습할 cell 집단의 소속을 정하는 알고리즘이 아니다. 반올림 경로의 실제 학습·gradient 처리는 코드 미확인이므로 구현 오류로 단정하지 않는다.

Table1의 공통 설정은 hidden dimension1,024·batch128·Adam이며 입력 길이는8·24·168이다. 아래는 **논문 보고 설정**이다.

| 모델 표기 | 구조 설명 | learning rate | epochs |
|---|---|---:|---:|
| GRU-Linear | GRU + Linear | 0.01 | 1500 |
| GRU-DLinear | GRU + Linear 표기, §3.2.2는 trend/seasonality 분해 설명 | 0.0001 | 500 |
| GRU-XGBoost | GRU + XGBoost | 0.1 | 1500 |
| ESN | Table1은 ESN core | 0.000001 | 5000 |
| LSTM | LSTM + Linear, §3.2.5는 FCN 설명 | 0.0001 | 1500 |
| GRU-MTL | GRU + Linear + Classifier | 0.001 | 1500 |

Linear·DLinear·XGBoost를 GRU 없는 값싼 단순 기준으로 인용하지 않는다. p10은 ESN에 GRU embedding을 넣지 않았다고 설명하지만 §3.2.4(p11)는 GRU sequence를 reservoir에 넣는다고 설명한다. Table1의 설정만으로 이 불일치를 해소하지 않는다. 층 수의 최종 값·seed·실제 탐색 횟수·반복별 변동은 확인되지 않았다.

§3.2.8은 `λreg=λcls=1`이고 추가 tuning 없이 사용했다고 설명한다. Table4의 가장 좋은 balanced 행은 `λreg=λcls=0.5`이며 MAE/MSE/RMSE는 **0.213/0.249/0.499**다. 두 설정의 비율은 같아도 loss 전체 배율은 다르다. 0.213은 Table2의 MTL MAE0.213631을 소수 셋째 자리로 통상 반올림한 0.214와도 다르므로 같은 fit의 반올림이라고 확정하지 않는다. [수치 명세](../verification/history-034-numeric-check.json)에 classification-only·regression-only를 포함한 Table4의 여섯 행을 모두 보존했다.

Ensemble은 GRU-MTL·GRU-Linear·GRU-XGBoost의 가중 합이다. Algorithm1에서 합이1인 α·β·γ를 쓰지만 정확한 값·최적화 절차·별도 검증 분할은 미확인이다. p12는 train의 과거 주에서만 가중치를 맞추고 test에 고정했다고 **보고**한다. 이 설명을 독립적인 누출 부재 검증으로 표시하지 않는다. Algorithm1의 MTL 입력은 **회귀 head만 사용**한다고 되어 있어 식7의 분류 mask 적용 결과와 자동으로 같다고 볼 수 없다.

## Table2의 결과와 일반화할 수 없는 부분

아래 MAE는 논문이 제공하는 척도의 인쇄값이며, 실제 bytes/Mbps 단위로 확인한 측정치가 아니다. 입력 길이별로 같은 5번째 주를 평가한다.

| 모델 | 168시간 입력 MAE | 24시간 입력 MAE | 8시간 입력 MAE |
|---|---:|---:|---:|
| GRU-Linear | 0.218503 | 0.239661 | 0.277397 |
| GRU-DLinear | 0.238085 | 0.286313 | 0.274060 |
| GRU-XGBoost | 0.230860 | 0.225731 | 0.227612 |
| ESN | 0.264141 | 0.264349 | 0.268062 |
| LSTM | 0.355919 | 0.301782 | 0.316045 |
| GRU-MTL | 0.213631 | 0.300096 | 0.282097 |

168시간 조건에서는 MTL이 여섯 모델 중 MAE·MSE·RMSE가 가장 낮다. 그러나 “모든 모델에서168시간이 우수”는 Table2로 지지되지 않는다. GRU-XGBoost의 MAE는24시간, MSE/RMSE는8시간이 가장 좋다. LSTM은 세 지표 모두24시간이 좋으며 ESN도 MSE/RMSE는24시간이 좋다. MTL이 모든 입력 길이에서 가장 좋거나 ESN이 언제나 최하위라는 결론도 성립하지 않는다. 예를 들어24·8시간 ESN MAE는 같은 길이의 MTL보다 낮다.

해결하지 못한 주요 숫자 차이는 다음과 같다.

| 원문 주장·위치 | 인쇄값 대조 | 아카이브 판단 |
|---|---|---|
| 초록:168시간은8시간보다 MAE56% 감소 / p15:8시간은168시간보다56% 증가 | MTL0.282097→0.213631은 **24.27% 감소**; 역방향은 **32.05% 증가** | 어느 방향도56%와 맞지 않음. 반올림으로 설명되는 크기가 아님 |
| 초록의 LSTM MAE0.3223 | Table2·p15의168시간 LSTM은 **0.355919** | 다른 실행값인지 오기인지 미확인 |
| Table5 without ensemble MAE0.218503 | Table2에서는 **GRU-Linear**의 값. 같은 Table5 행의 MSE0.249026·RMSE0.499025는 MTL의 값 | 기준 행의 혼합 가능성을 표시하고 임의 정정하지 않음 |
| Ensemble MAE0.210520의1.45% 이득 | Table2 MTL0.213631 대비 **1.45625%**(통상1.46%); 초록0.2136→0.2105로 계산하면 **1.45%** | 표시 정밀도로 설명 가능한 작은 차이. 앞의56% 문제와 구분 |
| Table5 without 기준 이득 | 0.218503→0.210520은 **3.65%** | 어떤 기준을 썼는지 함께 표시 |
| p15:ensemble이 LSTM/ESN보다45% 우수 | 같은168시간 Table2 대비 각각 **40.85%·20.30%** | 두 모델 공통45%로 지지되지 않음 |
| p15:8시간ensemble MAE60% 개선 | p14는24·8시간을 ensemble 분석에서 제외; Table5에는168시간만 있음 | 짧은 입력의 ensemble 결과로 검증하지 못함 |

MAE 감소를 ensemble **분산 감소 측정**으로 부르지 않는다. p15의1.45% variance 문구와 달리 p16은 ensemble variance를 포함한 불확실성 정량화를 수행하지 않았다고 명시한다. MAPE는 zero 부근에서 과도하게 커졌다고 설명하지만 Table2에는 없고 zero 분모 처리 방법도 미확인이다. 유의성 검정·반복 분산이 없는 인쇄표로 통계적 우월성을 확정하지 않는다.

Figure11–13은 **Sample111의 앞100개 공간 차원**을 보여 준다. 100개의 미래 시간점이나 모든 beam/기간의 검증으로 읽지 않는다. Ensemble 그림에서도 약65번째 차원 부근의 큰 peak를 충분히 따라가지 못하는 모습이 보인다. 이는 정성적 시각 확인이며 픽셀로 오차를 계산하거나 전체 peak 성능을 추정하지 않았다.

## 이전 beam 논문과의 점수 비교 경계

Table3의 Hist.Avg·iTransformer·PatchTST·DLinear·Transformer, Test1/2 **10개 숫자**는 [H033의 주최측 baseline 표](../verification/history-033-numeric-check.json)와 일치한다. 예를 들어 Test1 iTransformer0.1967, Test2 Transformer0.2331이다. 그러나 이 논문의 실제 평가 설명은 **week5**, 주최측 설명은 **week6·week11**이다. 수치가 같은 데이터 소개에 놓였다는 이유로 공통 test의 모델 순위로 만들지 않는다. H033의 CatBoost/LightGBM 점수와 Frontiers MTL/ensemble 점수의 직접 우열도 판단하지 않는다.

## 비용·재사용·재검토 조건

논문 §4.1.2는 Python3.8·TensorFlow2.12·Scikit-learn1.0.2, NVIDIA DGX의 A10080GB 네 개를 보고한다. 별도의 단일 A100에서 **batch1·입력 길이8의 평균 추론2.7ms**를 보고하지만 trace·측정 반복·전체 학습 시간·실패/탐색 비용은 미확인이다. 이를168시간 모델·전체 ensemble·실제 망 운영 latency로 바꾸지 않는다. epochs를 fit 수나 총 GPU 시간으로 환산하지 않는다.

같은 제안을 다시 검토하려면 다음 차이를 먼저 명시한다.

1. 새 행동이 zero 판별·추가 입력·공동 loss·ensemble 중 어디인지, 기존 방법과 무엇이 다른지 기록한다. 이 논문만으로 신규 clustering 기여를 주장하지 않는다.
2. 같은 target·단위·test 주·입력 길이·recursive 규칙·공변량의 예측 시점 가용성을 고정한다. 원 코드와 실제 전처리·사용 head·가중치·seed를 확보하기 전에는 원 실험 재현 계획과 확인된 성능을 구분한다.
3. 단순 calendar/lag 기준과 같은 연산 예산의 비교를 설계하고, 전체 평균뿐 아니라 inactive/active·peak·beam·기간별 손해를 남긴다. 새로운 실험을 여기서 실행한 것은 아니다.
4. 최종 RCTL 공동 학습에 적용한다면 추가 정보와 소속 변경 행동, 최종 성능·비용을 별도로 검증한다. 저자의 예측 MAE를 자원 할당 성공·실측 전력 절감으로 옮기지 않는다.

p16에 공개 데이터 Drive 폴더가 연결돼 있지만 이번 검토에서 접속·다운로드·원자료 재현을 완료하지 않았다. 실제 데이터/저자 코드 접근, 설정 불일치 해소, 51·53·55 전체 종합은 계속 남아 있다. 이 아카이브의 새 모델 fit/inference·원 연구 스크립트 실행·무작위 표본 생성은 모두0회다.

## 55의 event 문헌 접근 공백

Andrea Pimpinella·Alessandro E.C. Redondi의 *Generative-aided and context-aware forecasting of mobile network traffic*, Computer Networks282:112147(2026), DOI10.1016/j.comnet.2026.112147은 [저자 저장소](https://re.public.polimi.it/handle/11311/1313047)와 [출판사](https://www.sciencedirect.com/science/article/pii/S1389128626001593) metadata로 식별했다. 원55와 [당시 fetch log](../evidence/0051-0055-gotsf-audit/originals/SRC-0063272.json)의 TLS 검증 실패를 보존했다. 2026-10-09 재시도도 저자 저장소는 TLS 검증을 켠 상태에서403, 출판사 웹 접근은403이었다. 검색에 저자 postprint가 표시됐다는 사실을 원문 입수·방법 검토 완료로 세지 않는다. event·미래에 알려진 정보·augmentation의 실제 구현과 효과는 **본문 미검토**다.

후속 H042에서는 [event AAM44쪽을 확보·검토](0051-event-context.md)했다. 위의 TLS/403·본문 미검토는 H034 당시 상태로 보존하며, 현재 방법·수식·표의 확인 범위와 미해결 사항은 후속 기록에서 확인한다.
