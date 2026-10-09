# 51·55 STK-Diff: 생성 코드의 재사용 범위와 평가 조건

STK-Diff의 공개 Beijing 자료와 구현은 **기지국별 전체 시계열 생성**을 검토할 근거다. 읽은 기본 실행 경로에는 관측 과거 값을 고정하는 mask나 미래 구간만 평가하는 시간 분할이 없다. 이를 바로 cell clustering 또는 RCTL 미래 예측의 성능 근거로 사용하지 않는다. 과거 52번에서 실제 실행한 것은 자료 스키마 검사이며, STK-Diff 모델 학습·추론 결과는 이 연구기록에 없다.

이 기록은 [52·54의 자료/실험 검수](0052-0054-partial-observation.md)를 이어서 README 그림 4개와 모델·평가·설정 등 6개 텍스트 647줄을 읽은 후속이다. 과거 51·55 전체 종합은 미완료다. [출처와 읽은 범위](../sources/history-041.md), [34개 주장 검수](../verification/history-041.md), [근거 명세](../evidence/0051-stkdiff-audit/manifest.json)를 함께 본다.

## 당시 질문과 확보 계보

51번은 다른 데이터에서도 남는 예측 문제와 TabICLv2의 추가 정보가 있는지 조사했다. 공개 자료가 바뀐 사실만으로 신규성을 주장하지 않았으며, 자료 단위·입력 가용 시점·원문 실패 조건을 먼저 확인하도록 계획했다. 계획 속 예산과 다음 행동은 역사적 자료다.

당시 `fetch_stkdiff_metadata_51.py`는 `commits/main` 응답에서 얻은 SHA로 tree와 README·loader·entry·LICENSE를 고정했다. 저장 commit은 `e1faed12aa7abb33d801fe9483026769ffaeeed3`이다. 스크립트에는 기존 로그 존재 시 종료, 응답당 5,000,000바이트 한도가 있고, 저장 로그는 2026-09-26 여섯 응답의 HTTP 200·크기·SHA를 남겼다. 스크립트만으로 성공을 추정하지 않고 저장 응답과 대조했다.

H031은 그 텍스트·JSON과 Beijing NPZ의 멤버 통계·Git blob을 이미 검수했다. H041은 같은 commit의 그림·의존 텍스트 10개, 총 593,839바이트를 확보해 당시 `truncated=false` tree의 Git blob SHA1과 모두 일치함을 확인했다. 현재 main의 코드로 과거 버전을 교체하지 않았다. 새로 읽고 복사한 로컬 원문은 fetch 스크립트 28줄 1개이며, 기존 원문 9개와 NPZ 검수는 재사용했다.

## 데이터와 분할: 기지국 생성 설정

| 항목 | 확인한 범위 | 재사용할 때의 한계 |
| --- | --- | --- |
| 공개 자료 | `bs_record=(960,168)`, `bs_kge=(960,32)`; NPZ 1,413,636바이트 | README는 Beijing 일부 지역의 aggregated base-station traffic이라고 설명한다. physical cell, MobiGPT 전체 자료로 바꾸어 부르지 않는다. |
| 파일명 | README 예제는 `traffic_data/bs_beijing.npz`; 실제 tree·loader는 `traffic_data/beijing.npz` | 실행 경로와 파일 해시를 함께 확인한다. |
| 시각·단위 | NPZ에 timestamp·station ID·측정 단위가 없다. loader의 timepoints는 `arange(eval_length)` | 168개 위치만으로 실제 날짜·관측 간격·시간별 합산을 확정하지 않는다. |
| 분할 | station row를 무작위 순열로 80/20 분할, `test_indices = valid_indices` | 같은 기지국의 과거/미래 분할이 아니다. |
| 정규화 | 학습 station의 모든 시점을 1열로 펴서 MinMaxScaler를 fit, 전체 자료에 transform | 읽은 경로는 test 값으로 scaler를 fit하지 않는다. 생성 분할이므로 미래 예측의 누수 여부 판정을 그대로 옮기지 않는다. |
| 기본 배치 | batch 64, 세 loader 모두 `drop_last=True`; train만 shuffle | 960개면 768/192개, 학습 12·평가 3배치로 나머지 0이다. 구조 계산이며 실행 횟수 로그가 아니다. |

`--seed=1`은 loader와 Dataset 인자로 전달되지만 읽은 entry·loader·model·utils 경로에는 NumPy/Torch seed 초기화 호출이 없다. 외부 환경의 초기화 여부는 미확인이다. 같은 CLI seed 숫자를 재현 가능한 순열·잡음·가중치의 증거로 삼지 않는다. 도시 지식 임베딩의 원 학습 범위와 두 그래프의 실제 행·열 순서는 이번에 검증하지 않았다.

## 그림과 실제 코드의 연결

| 자료 | 그림에서 읽은 역할 | 고정 코드와 대조한 결과 |
| --- | --- | --- |
| Framework | 도시 배치·문맥 → 생성 모델 → `official`/residential/commercial 지역의 트래픽 패턴 예시 | 0–7 Time/Day 예시는 개념도다. 실제 시각 분할·정량 성능표가 아니다. `official`은 원 그림 표기를 보존했다. |
| Flowchart | Urban Knowledge Graph → KGE → Temporal Extraction; Urban Spatial Relations → Spatial Connection | KGE·관계 그래프를 조건 정보로 사용한다. 군집 소속 수정 정책이나 RCTL 비교 실험을 제시한 그림은 아니다. |
| TE module | FFT·stepped window·basis별 attention·weighted recovery와 residual | `extract_frequency`는 크기가 큰 주파수 bin 4개를 골라 빼는 과정을 `freq_select`번 반복한다. 명시적인 연속 stepped window 구현으로 단정하지 않는다. |
| SC module | 거리/POI 그래프의 집계와 MLP, 두 가지 결과를 더한 뒤 Linear | 실제 코드는 `yd`, `yp`를 **concat → Linear(2C,C)**로 결합한다. 거리 경로는 MLP 전, POI 경로는 MLP 후 residual을 더한다. 그림의 단순 합과 구분한다. |

코드는 KGE와 확산 중인 시계열을 rFFT한다. 길이 168이면 주파수 bin은 85개이며, 기본 `freq_select=4`는 명목상 4×4 선택이다. 0값·동률 때문에 16개의 서로 다른 비영 bin을 항상 선택한다고 보장할 수 없다. 선택 결과와 남은 주파수를 attention·가중 복원 후 합친다.

복소 Linear는 q/KGE, k/KGE, k/KGE를 각각 Q/K/V로 만든다. `v` 인자는 읽히지 않지만 현재 호출은 `v=k`다. 내적에는 명시적인 복소 켤레가 없고 `sqrt(E)`로 나눈 뒤 절댓값 softmax를 적용한다. 이는 읽은 연산 경로의 설명이며 논문 수식의 정확한 재현 판정은 아니다.

두 인접 행렬은 `>0` 위치를 edge로 만들고 `copy_u`와 `sum`으로 집계한다. 읽은 경로에서는 행렬 원래 값을 edge weight로 전달하지 않는다. 각 residual block은 현재 minibatch의 station index로 만든 induced subgraph를 사용한다. 따라서 전체 960개 이웃을 항상 함께 이용하는 구조가 아니며 배치 구성에 따라 사용 가능한 이웃이 달라질 수 있다. 실제 그래프 밀도·가중치 값·성능 영향은 미확인이고, 이를 데이터 누수나 모델 실패의 입증으로 쓰지 않는다.

## 학습·생성·평가에서 실제로 쓰는 것

`main_model_upload.py`는 무작위 확산 시점의 잡음을 예측하는 MSE로 학습한다. `impute`는 관측값의 **shape와 `randn_like`**를 사용해 초기 잡음을 만들고 station index를 denoiser에 전달한다. 관측 과거 값을 끼워 넣거나 고정하는 mask는 없다. 함수 이름 `impute`만으로 부분 관측 복원이나 미래 예측을 수행했다고 해석하지 않는다. `observed_tp`도 평가 반환값으로 보존되지만 예측의 실제 달력 입력으로 전달되지 않는다.

설정은 epochs 100, batch 64, lr 0.001, residual layers 8, channels 64, heads 8, diffusion embedding 64, beta 0.0001→0.01, quad schedule, num_steps 1000, freq_select 4, kg_emb 32다. 학습 optimizer는 Adam/weight_decay 0.000001, LR milestone은 75·90, gamma 0.1이다. 이는 기본 설정과 코드의 구조이며 이 연구에서 실행한 설정 로그가 아니다.

`calc_loss_valid` 함수는 전체 1000시점을 순회하도록 정의되어 있다. 하지만 실제 `utils.train`은 `valid_loader`와 `valid_epoch_interval`을 사용하지 않고 epoch 종료 뒤 최종 가중치를 저장한다. 따라서 loader의 validation=test 사실만으로 이 실행 경로가 test 성능으로 checkpoint를 선택했다고 단정할 수 없다. 별도의 논문 학습·튜닝 절차는 미확인이다.

역확산은 `reversed(range(1,num_steps))`, 즉 기본 999→1이다. 성공적으로 끝난다는 조건에서 **샘플 1개·배치 1개당 denoiser 999회**, 기본 test 3배치·nsample 1이면 2997회다. 이는 전체 모델 실행 시간·GPU 비용의 실측이 아니며, 모델 안의 residual 연산·전처리·학습·저장 비용과도 구분한다.

평가는 생성값과 정답을 scaler로 역변환해 저장하고, 모든 168개 위치의 `calc_quantile_CRPS`를 계산한다. `evalpoints_total`을 누적하지만 지표의 분모로 쓰지 않는다. 별도 `res_plot.py`는 저장 pickle에서 20개 시계열의 샘플 평균과 정답을 그리는 예제다. 이 파일을 실행하거나 pickle을 로드하지 않았으며 그림 예제를 성능표로 보지 않는다.

## 기본 nsample=1에서 CRPS라는 이름이 의미하는 범위

읽은 구현은 q=0.05,0.10,…,0.95의 19개 분위수 loss를 평균하고 **정답 절댓값 합**으로 나눈다. 기본 entry의 `--nsample=1`에서는 각 분위수 예측이 같은 단일 샘플이다. 유한한 값과 양의 분모, 정확한 명목상 대칭 q 격자를 가정하면 `평균 q=1/2`이므로 결과는 다음과 같다.

`sum(abs(prediction - target)) / sum(abs(target))`

정답 `[1,3]`, 생성 `[2,1]`이라는 설명용 예에서는 이 값이 **3/4=0.75**, 통상 MAE는 **3/2=1.5**, 시점별 절대 백분율 오차 평균은 **5/6≈0.833333**이다. 원 연구의 측정값이 아니다. 단순 MAE나 시점별 MAPE, 여러 샘플의 분포 품질 검증과 섞지 않는다.

실제 코드는 NumPy 부동소수 격자를 사용한다. 검수 환경의 float64 격자에서 두 오차 부호의 계수는 1과의 차이가 1e-14 미만임을 확인했다. 원 PyTorch float32 경로의 bit 단위 일치나 저장 metric 재현은 수행하지 않았다. 정답 절댓값 합이 0일 때의 분모 보호도 읽은 함수에는 없다. 샘플 수를 늘린 경우에는 위 단일 샘플 축약을 그대로 적용하지 않는다.

## 실행 전에 알아야 할 설정·구현 공백

| 항목 | 정적 확인 | 판정 범위 |
| --- | --- | --- |
| 사용되지 않는 설정 | config의 `activation=gelu`, `model.timeemb=128` 키는 읽은 Python 경로에서 조회되지 않는다. Transformer의 GELU는 코드에 직접 적혀 있다. | 선언된 설정을 실제 활성 설정으로 보고하지 않는다. |
| 정의만 된 모듈 | `freq_weight_project2`는 정의되지만 읽은 forward에서 사용되지 않는다. | 임의 삭제·실행 시간 이득 추정은 하지 않는다. |
| Attention 분기 | 기본은 softmax. nondefault tanh는 `xqk_ft_`를 할당하지 않고 후속 연산에서 참조한다. | tanh를 선택할 경우의 정적 결함 후보다. 기본 경로가 이 때문에 실패했다고 쓰지 않는다. |
| 장치 | entry는 `CUDA_VISIBLE_DEVICES='5'`; 의존 코드에 `.cuda()`와 `.to('cuda')`가 있다. | `--device=cpu`만으로 CPU 실행을 보장할 수 없다. 하드웨어 검증은 하지 않았다. |
| 환경 | requirements에 `PyYAML==6.0.1`과 `PyYAML==6.0.2`가 동시에 있다. | 서로 다른 exact pin을 함께 만족할 수 없다. 설치·수정·현재 패키지 호환성 시험은 하지 않았다. |
| 원 자료 | distance/POI NPZ 각각 7,373,060바이트는 tree metadata만 확인 | 실제 배열·UKG 구축 입력·논문 본문과 전체 성능표는 미검토다. |

## 같은 연구를 반복하지 않기 위한 사용 기준

기존에 확인한 것은 공개 부분 자료의 스키마와 생성 구현의 구조다. 같은 NPZ를 다시 스키마 검사하는 제안은 [H031 결과](0052-0054-partial-observation.md)를 먼저 재사용한다. 새 예측 또는 clustering 제안에는 다음 차이가 있어야 한다.

1. 기지국/cell 단위, 실제 시각·관측 간격·측정 단위, 예측 때 알 수 있는 KGE/그래프 정보를 확보한다.
2. station 생성 holdout과 미래 시간 holdout을 나누고, 과거 conditioning·예측 horizon·정규화 학습 범위를 고정한다.
3. 단순 lag/calendar/global 예측과 비교하고, 생성 품질과 최종 RCTL 예측 오차를 별도로 평가할 근거를 만든다.
4. commit·자료 SHA·seed 초기화·배치 station 구성·nsample·지표 분모·checkpoint 선택·실측 비용을 기록한다.

이는 재검토 조건이며 새 실험 실행 지시가 아니다. STK-Diff의 논문 우열·clustering 신규성·RCTL 이득을 판정하지 않았다. 이번 정리는 모델 학습·추론, 원 연구 코드 import/실행, pickle load, 난수 생성 모두 0회이며 원본과 연구 예산 원장을 보존했다. 남은 event 원문·자료 버전·55 종합과 이후 과거기록은 계속 정리한다.
