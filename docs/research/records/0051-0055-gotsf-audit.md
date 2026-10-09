# 51·55 — GOTSF의 목적별 예측과 재사용 조건

GOTSF는 요청한 **target 값의 범위**에 맞춰 예측을 바꾸는 선행연구다. 새로운 cell 소속을 선택하거나 RCTL 공동 학습의 이득을 검증한 방법으로 읽지 않는다. 55번 기록의 구간별 지표·손실·운영 목적 해석을 원논문과 실제 호출 코드로 확인했고, 평균 이득뿐 아니라 악화하는 조건과 재현 공백을 함께 남겼다.

이번 범위는 51번 계획과 55번 종합 중 GOTSF에 해당한다. 다른 network·telemetry 문헌과 55 전체 신규성 판단은 미완료다. [52·54 부분 관측 진단](0052-0054-partial-observation.md)의 부정 결과와도 구분한다. 새 모델 실행·원 연구 코드 실행은 모두 0이다.

## 당시 질문과 확인한 자료

[51 계획](../evidence/0051-0055-gotsf-audit/originals/SRC-0021746.md.txt)은 실제 cell의 연속 트래픽인지, 달력·lag·PCC·global 이후 남는 문제가 무엇인지, 입력 변경과 공동 학습 단위 변경이 어떻게 다른지, TabICLv2가 무엇을 더 알려주는지 물었다. [55의 §1–2](../evidence/0052-0054-partial-observation/originals/SRC-0021824.md.txt)는 공개 데이터의 단위·시간 간격과 GOTSF의 운영 목적을 검토했다. 해당 기록의 과거 명령과 예산은 이 아카이브 작업의 실행 지시가 아니다.

| 자료 | 고정 버전과 실제 읽은 범위 | 이 기록에서의 역할 |
|---|---|---|
| AAAI 출판본 | [공식 페이지](https://ojs.aaai.org/index.php/AAAI/article/view/39249), 2026-03-14, 40(25), 21065–21073, DOI 10.1609/aaai.v40i25.39249. SRC-0063273 본문 9쪽, 시각 확인 2·3·4·5·7쪽 | 출판본 방법·설정·Table 1 |
| arXiv v3 | [2504.17493v3](https://arxiv.org/abs/2504.17493v3), 2025-08-14. SRC-0063276 본문 14쪽, 시각 확인 2·3·4·5·6·7·9·10·11쪽 | 확장 설명·운영 simulation·민감도·부록 |
| 공식 코드의 저장 사본 | [commit 31b17e55…](https://github.com/netop-team/gotsf/tree/31b17e55a0cb6f41bfe25230db3f81567efd58f3), 2025-06-05 | 코드 9개, README, notebook source·저장 출력 정적 검토. 전체 모델 구현 검토는 아님 |
| 공개 데이터 카드 | [netop/gotsf-ds](https://huggingface.co/datasets/netop/gotsf-ds), 저장 metadata pin `c9ecaf153354b2cc415c64750a966c47c7f3f6ac` | 카드 텍스트와 저장 info/tree 대조. 연결 그림과 전체 공개 CSV 미검토 |

두 PDF 버전의 전체 텍스트 23쪽과 그림·표가 있는 14쪽을 읽었다. 모든 정리를 증명하거나 저자 성능을 재현한 것은 아니다. 코드 11개 항목(9개 코드·README·notebook)과 카드의 저장 Git blob 12개를 대조했다. tree의 181개 항목을 파싱한 것은 181개 파일을 읽은 수가 아니다. 자세한 파일·페이지·해시·예외는 [출처 안내](../sources/history-032.md)에 있다.

## 방법의 결정 단위

입력 이력에서 미래 시계열을 예측하되, 요청 범위 I=[a,b]의 정답에 더 집중한다. 여기서 interval은 target의 **값 구간**이다. 과거·미래의 시간 구간이나 cell 묶음으로 바꾸어 해석하지 않는다.

| 기호·구조 | 원문에서 하는 일 | 팀 연구와 연결할 때의 조건 |
|---|---|---|
| B | 일반 예측 baseline | 같은 데이터·모델·척도의 대조로 사용 |
| E2E | 목적 구간을 고정한 학습 | 요청 구간마다 재학습하는 비용 구분 |
| C | 연속적인 구간 경계를 조건으로 사용 | 추론 시 목적 변경과 입력 가용성 구분 |
| D | 유한한 구간별 예측과 분류 head | 기존 모델 구조·학습 목적의 변경 포함 |
| patching | 분류 확률로 constituent 예측을 가중 평균하거나 가장 큰 확률의 예측 선택 | 값 구간별 모델 조합이며 RCTL 소속 결정과는 다른 행동 |

출판본 §2, v3 §2의 손실은 범위까지의 거리와 decay를 정의한다. 원문의 차원별 가중치 곱과 실제 active 코드의 **원소별 회귀 가중 + 가중하지 않은 BCE**는 동일한 식으로 취급하지 않는다. [active experiment](../evidence/0051-0055-gotsf-audit/originals/SRC-0063271.py.txt)의 회귀 항은 `loss=MAE`일 때 절댓값, 그 외에는 제곱 오차이며 validation은 L1을 사용한다. 모든 학습이 MAE였다고 확대하지 않는다.

## 자료 단위와 시간 분할

| 근거 | 확인한 범위 | 남은 공백·재사용 조건 |
|---|---|---|
| 공개 카드 | 30 BS × 3 cell × 32 beam = **2,880 beam**, DLPRB·DLThpVol·DLThpTime·MR_number | 2,880 cell로 부르지 않음. beam 합산의 중복·물리 단위·cell mapping 미확인 |
| 카드·info | 앞 5주 840시간, week 6 및 week 11 각 168시간. test index는 0–167, 168–335 | 떨어진 두 주를 연속 시간으로 이어 붙이지 않음. 카드의 괄호 `weeks 1–6`는 앞 5주 설명·0–839 범위와 충돌 |
| 논문 BLW 평가 | 100 beam, 출판본 약 10³ step, v3 1025 step·DLPRB 부분집합 | 전체 공개 2,880 beam 자료와 평가 자료를 구분. 출판본의 traffic volume 표현을 물리 단위의 확정으로 사용하지 않음 |
| 고정 코드 CSV | `date,V-0,…,V-98,OT`; **1026행 × 100값**, 102,600개 유한 값, 최솟값 0·최댓값 22.271109619051966 | 논문 1025 step과 1행 차이. 정규화 과정·원 beam ID·공개 자료와의 행 대응 미확인 |
| CSV 날짜 파싱 | 정수 0–1025를 pandas 3.0.1의 기본 `to_datetime`에 넣으면 1970-01-01의 0–1025 ns | 실제 시간축이 확인된 자료가 아님. 이 검사는 현재 저장 값 파싱이며 원 loader 실행·당시 환경 재현이 아님 |

카드와 [info](../evidence/0051-0055-gotsf-audit/originals/SRC-0063282.json)의 config는 `train_0w_5w`, `test_5w_6w`, `test_10w_11w`를 구분한다. 전체 공개 원시 CSV는 내려받아 대조하지 않았다. 위의 작은 코드 CSV는 아카이브 검수를 위해 2026-10-09에 같은 commit에서 추가 확보한 자료다. 당시 연구자가 확보했던 파일로 소급하지 않는다.

논문 분할은 BLW train/validation/test **70/10/20**, 나머지 **66/17/17**이다. 이력/예측 길이는 BLW **96/24**, Synth **48/24**, 나머지 **168/48**이다. 다변량 평가에서는 최대 100채널을 사용하며 Weather는 21채널이고 Synth는 별도의 합성 예다. 정확한 원 beam 선택과 정규화 변환은 확인하지 못했다.

[Dataset_Custom](../evidence/0051-0055-gotsf-audit/originals/SRC-0063269.py.txt)은 70/10/20으로 자르고 validation/test의 이력 창을 앞 구간에서 이어 받는다. 기본 `scale=False`; 켜면 train에 scaler를 적합한다. 날짜에는 별도 unit 없이 `pd.to_datetime`을 적용한다. [data factory](../evidence/0051-0055-gotsf-audit/originals/SRC-0063268.py.txt)는 test 전체를 한 batch로, validation도 전체 batch·shuffle로 설정한다. 이는 저장 코드의 동작 해석이며 실제 실행 입출력 검증은 아니다.

## 구간별 MAE의 분모

active experiment와 [stats entry](../evidence/0051-0055-gotsf-audit/originals/SRC-0063283.py.txt)는 구간 밖 target과 prediction을 모두 0으로 만든 뒤 [MAE 함수](../evidence/0051-0055-gotsf-audit/originals/SRC-0063286.py.txt)에서 전체 원소 수 N으로 나눈다. 같은 구간 조건의 예측을 고정하면 다음 관계다.

`M_I = (1/N) Σ 1[y_j∈I] · abs(pred_I_j−y_j) = (n_I/N) × conditional_MAE_I`

등식의 조건은 n_I>0이다. 빈 구간에서 코드의 zero-mask MAE는 0이지만 조건부 MAE는 정의되지 않는다. 따라서 구간 점수를 재사용할 때 N·n_I·포함률을 함께 남겨야 한다. 구간별로 예측 자체가 달라질 수 있으므로 여러 M_I의 평균을 하나의 전체 예측기의 MAE 개선율로 바꾸지 않는다. 경계는 양끝 포함이어서 경계값이 인접 구간에 중복 포함될 가능성도 있다.

`_test`의 bounds 기본값은 test 최솟값/최댓값이지만 stats 호출부는 학습 구간에서 만든 bounds를 명시적으로 전달한다. 기본 인자만 보고 이 저장 경로에 test 범위 누출이 실제 발생했다고 단정하지 않는다. 실제 helper는 [utils/tools.py](../evidence/0051-0055-gotsf-audit/originals/EXT-H032-01.txt)로 L개 구간을 반환한다. [delta_specific_utils](../evidence/0051-0055-gotsf-audit/originals/SRC-0063303.py.txt)의 전체 범위+L개 반환을 이 호출부에 적용하지 않는다.

## 논문 보고값의 이득과 반례

아래는 양쪽 PDF의 **Table 1, 7쪽**에 인쇄된 값이다. 원 예측을 재계산한 결과가 아니다. 표의 배율은 BLW/Synth ×10³, Traffic ×500, Weather ×2, Electricity ×0.1이다. 이 척도를 Milan 정규화 MAE와 직접 비교하지 않는다. `D1_2L`과 `Dinf_2L`은 원표의 위첨자 1·∞와 아래첨자 2L을 텍스트로 적은 이름이다.

| 데이터·행·모델 | DL | D1_2L | Dinf_2L | B | C0.2 | 원표의 best improvement |
|---|---:|---:|---:|---:|---:|---:|
| BLW I1, PatchTST | 102.8 | 158.2 | 117.8 | 124.1 | 118.1 | 17.2% |
| BLW I1–I8 평균, PatchTST | 22.4 | 28.8 | 25.5 | 50.7 | 26.7 | 55.8% |
| Electricity I1–I4 평균, iTransformer | 5.02 | 4.09 | 4.21 | 1.39 | 1.46 | 0.0% |

BLW I1에서 DL은 B보다 약 **17.16%** 낮지만 D1_2L은 약 **27.48% 악화**한다. 평균 행의 55.8%는 DL의 22.4와 B의 50.7을 비교한 약 55.82%에 해당한다. D1_2L의 평균 개선은 약 43.20%다. Electricity iTransformer 평균은 DL/D1_2L/Dinf_2L이 B보다 각각 약 261.15%/194.24%/202.88% 높다. best 열의 0%를 모든 대안의 동률로 읽지 않는다.

두 버전에서 29행 × 24개 = **696개 인쇄 숫자의 순서가 일치**했다. 이는 추출한 문자 비교이며 696개 원 실험값의 독립 재현이 아니다. 선택한 18개 값·그 값에 대한 9개 정책 비교는 표 제목·열·배율과 함께 시각 대조했다.

100개 policy 평균 셀을 인쇄 자릿수의 반올림 범위로 검사했을 때 한 항목이 맞지 않았다. BLW DLinear DL의 8개 구간 값은 **167.1, 76.0, 56.7, 44.2, 33.5, 28.1, 19.3, 11.1**로 합 436.0, 산술 평균 **54.5**다. 원표 평균은 양쪽 이미지 모두 **54.0**이다. 일반적인 반올림 오차 상한 0.10으로 차이 0.5를 설명하지 못한다. 원 실험 출력·저자 정정은 확인하지 못했으므로 원문을 고치지 않고 미해결로 남긴다. [인쇄 표 검수 JSON](../verification/history-032-paper-table-check.json)에 전체 비교와 계산을 보존했다.

## 논문과 저장 실행 설정의 차이

| 항목 | 논문 설정 설명 | 저장 Wireless train.sh·호출부 |
|---|---|---|
| layers / dimension | 3 / 256 | 2 / 128 |
| batch / epochs | 32 / 50 | 32 / 60 |
| optimizer / 초기 lr | AdamW / 0.001 | 기본 Adam / 0.0001; Lion은 별도 flag |
| learning rate schedule | cosine, 최소 0.00001 | `type3`도 cosine, 최소 0.00001 |
| early stopping patience | 5 | entry 기본 25 |
| channels / input / horizon | BLW 100 / 96 / 24 | 100 / 96 / 24 |
| 구간·decay | 논문의 정책별 설정 | 명칭 discrete4/8에 실제 `nr_intervals=8/16`, decay 37, bounds [0,8] |

[train.sh](../evidence/0051-0055-gotsf-audit/originals/SRC-0063294.sh.txt)는 4모델 × 4종의 16개 background 명령을 정의한다. 16회 완료된 fit의 증거가 아니다. [train entry](../evidence/0051-0055-gotsf-audit/originals/SRC-0063284.py.txt)의 seed는 2023이며 classifier weight 기본값은 0.1이다. [추가 확인한 stats.sh](../evidence/0051-0055-gotsf-audit/originals/EXT-H032-03.txt)는 MAE/MSE·max/expectation 경로를 구분한다. 비교 수치별 실제 checkpoint·명령·seed 반복·원 예측의 대응은 미확인이다.

저장 [experiments/exp.py](../evidence/0051-0055-gotsf-audit/originals/SRC-0063270.py.txt)의 미구현 criterion·validation 경로는 현재 확인한 entry에서 import하지 않는다. 이를 active 학습 실패의 근거로 삼지 않는다. 반대로 stats의 확률 합 0 보호 부재나 metrics의 0 정답 분모도 정적 위험으로만 남긴다. 이 아카이브에서 그 실패를 실행 관측한 것은 아니다.

논문은 V100 6개·각 16GB, Xeon Platinum 8164·104 core 환경을 보고한다. 조건별 실제 wall time·원 학습 비용의 완전한 로그는 확보하지 못했다. 코드 존재·하드웨어 설명·background 명령 수를 완료 횟수나 실측 비용으로 바꾸지 않는다.

## 에너지 예와 notebook의 증거 경계

v3 9쪽은 DLPRB 부하를 **가정한 2-tier 운영 모델**에 넣는 simulation이다. Ccap=100Mbps, Ccov=30Mbps, α=0.5, Eon=1266Wh, Eoff=320Wh, H=24, 총 96h의 rolling, L=4, 목적 범위 [0,0.5], 수면 기준 [0,0.025]를 사용한다. 본문은 sleep-duration error 약 3배 차이·하루 약 1시간, 337W와 약 0.950kW를 보고한다. 이는 실제 통신망 전력 계측이나 clustering의 효과가 아니다. Wh parameter와 W 보고 표현의 차원은 임의로 통일하지 않았다.

고정 [Viz_Wireless notebook](https://github.com/netop-team/gotsf/blob/31b17e55a0cb6f41bfe25230db3f81567efd58f3/Viz_Wireless.ipynb)의 33개 source cell은 [저장 추출 TXT](../evidence/0051-0055-gotsf-audit/originals/SRC-0063262.txt) 944행과 구분 개행을 제외하고 일치한다. 모든 연구 source·저장 text 출력·12개 PNG를 읽었다. cell 0의 Bokeh/PyViz 생성 loader JavaScript는 초기화임을 확인한 뒤 연구 본문 독해에서 제외했다. notebook 전체 바이트를 의미 검토 완료했다고 표시하지 않는다.

- 현재 `MODELS`는 Intdisc8만 가리키지만 cell 5의 저장 출력·그림은 Intdisc4/8을 비교한다. 실행 번호가 비단조이고 cell 6의 Epsilon 자료도 현재 앞선 cell만으로 설명되지 않는다. 하나의 깨끗한 실행 증거로 묶지 않는다.
- cell 13은 0 또는 37을 반환하는 함수의 결과에서 1인 위치를 찾아 빈 배열의 첫 값을 참조한다. 저장 `IndexError`와 부분 그림이 이에 대응한다. 예측 정확도의 부정 결과로 분류하지 않는다.
- cell 12의 weight 0 범례와 rate 37 코드, cell 14의 수동 나열 값 평균을 Accuracy로 부른 표기를 그대로 검증된 성능으로 사용하지 않는다. cell 11 나열 값의 최소 δ=0.1과 논문 Fig. 9의 약 0.05도 동일 실험의 정정으로 단정할 근거가 없다.

## 남긴 모순과 후속 설계 조건

| 위치 | 미해결 내용 | 적용 원칙 |
|---|---|---|
| Synth 정의 | 출판본의 sine/cosine·(s,b)와 v3 식 16–17의 D·k/4 정의, noise 설명이 다름. v3 3.1×10³와 3456 step도 다름 | 판본별로 보존하고 하나의 재현 식으로 합치지 않음 |
| Traffic 자료 설명 | 2015–2016, 48개월, 17,544 points가 함께 기재 | 실제 원 데이터와 시간 범위 확인 전 달력·길이 확정 금지 |
| 출판 Fig. 3 / v3 Fig. 4 | 마지막 (f)의 B caption과 별도 baseline 그림의 차이 | 그림을 추정한 새 policy명으로 바꾸지 않음 |
| v3 Fig. 8 | caption D8·y축 8구간과 본문 D32, legend의 ν=3 포함 여부, ∞의 no-decay 설명과 정의 차이 | formal decay와 실험 설정을 나누어 기록 |
| 코드 README | badge의 arXiv 번호와 실제 링크 번호 불일치, 경계·horizon 설명의 부정확한 표현 | 실제 논문 ID·값 구간·inclusive 코드 기준으로 안내 |

55의 GOTSF 관련 판단은 유지된다. 운영 목적과 전체 MAE는 구분해야 하고, 가중 loss·목적 구간·예측 조합 자체는 이미 선행이 있다. 여기서 TabICL이 RCTL 소속을 더 잘 결정한다는 결과는 나오지 않았다. 그렇다고 GOTSF가 모든 데이터에서 우월하지 않다거나 운영 목적 연구가 무의미하다고 확대하지도 않는다.

새 설계는 먼저 목적(예: 낮은 부하의 운영 결정), 값 구간과 빈도, 입력의 관측 가능 시각, 물리 단위·beam/cell 대응, 시간 분할을 정한다. 같은 조건에서 B·task-specific 학습·patching과 강한 단순 기준을 비교하고, 전체/cell/기간 손해와 실제 비용을 남겨야 한다. TabICL 또는 RCTL을 추가한다면 기존 예측·구간 조합과 달라지는 **정보와 학습 행동**을 설명해야 한다. 이는 후속 실험의 조건이며 이번 정리에서 실행하지 않았다.

재사용 가능한 것은 [보존 원본과 추가 참조](../evidence/0051-0055-gotsf-audit/README.md), 고정 코드의 버전·범위, [주장 대조](../verification/history-032-claims.json), [검수 결과](../verification/history-032.md)다. 논문 원 예측·전체 모델 구현·자료 매핑·연결 그림·당시 실행 환경은 아직 확인되지 않았다. ITU·Cellular Predictions·event·telemetry와 55 전체 종합은 다음 묶음으로 이어진다.
