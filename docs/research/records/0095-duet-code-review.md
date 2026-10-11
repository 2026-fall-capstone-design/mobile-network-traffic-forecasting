# 0095. DUET 저장 코드의 호출 경로·확률 처리·비용 범위

[연구 안내](../README.md) · [전체 흐름](../history.md) · [과거 시도](../prior-attempts.md) · [원81](0090-input-partition-decision.md) · [DUET 논문](0094-duet-literature-review.md) · [출처](../sources/history-095.md) · [근거 묶음](../evidence/0095-duet-code/README.md) · [검수](../verification/history-095.md)

원81이 남긴 “입력 관계 선택도 선행연구에 있고, sparse mask만으로 전체 쌍 계산이 없어지지는 않는다”는 판단을 고정 코드 판본에서 확인한다. 학습 가능한 관계·temporal expert와 고정 UPC 소속·독립 RCTL 학습을 구분하고, 논문과 구현의 세부 차이를 당시 성능의 무효화로 확대하지 않는다.

| 항목 | 확인 범위 |
|---|---|
| 연결 기록 | 원81 「입력 공유와 예측 단위를 바꾸는 방향의 검토」, 2026-09-26 |
| 코드 판본 | 공식 DUET commit `dcc6e6780a9138731b64b9b5398a94a1d97033f0`, 2026-05-12 |
| 논문 판본 | DUET v3, 2025-01-10; 코드와 시점이 다름 |
| 실행 구분 | 원소장 코드·Git 정보 및 같은 판본 의존성의 정적 검토; 새 모델 실행 0 |
| 자료·기간·seed·성능 | 스크립트와 설정의 선언만 확인. 실제 실행 자료·기간·최종 설정·seed별 결과는 미확인 |
| 지표·정규화 | 선언된 MAE/L1·MSE·Huber와 StandardScaler/RevIN의 역할을 구분. 통신 트래픽 성능 비교는 해당 없음 |
| 재사용 | 고정 코드·설정 링크, 함수 위치, 수식·차원 검수. 현재 환경에서 재현 성공으로 표시하지 않음 |

아래 C01–C34의 원문 위치·해시·보충 출처는 [주장별 근거](../verification/history-095-claims.json)에 있다. B는 batch, L은 이력 길이, N은 channel 수, F는 rFFT 주파수 수, E는 attention head의 key 폭이다.

## 원81과 코드 판본

<a id="c01"></a>**C01.** 원 81의 DUET 관찰은 고정 partition과 입력 관계 학습을 구분하고, 모든 channel 쌍의 주파수 차이와 attention score를 먼저 계산한다고 적는다. 당시에도 일부 확률 처리를 논문 Eq.18의 정확한 재현으로 주장하지 않았다. 과거 기록의 판단을 설명한다. 과거 문서의 실행 제한이나 후속 명령을 현재 지시로 실행하지 않는다. [근거](../evidence/0090-input-partition/originals/SRC-0022042.md.txt)

<a id="c02"></a>**C02.** 저장된 코드 4개는 commit dcc6e6780a9138731b64b9b5398a94a1d97033f0의 Git blob과 바이트 단위로 대응한다. commit 날짜는 2026-05-12로 DUET 논문 v3의 2025-01-10 이후다. 현재 코드 관찰을 논문 당시 구현·실행의 증거로 소급하지 않는다. [근거](https://github.com/decisionintelligence/DUET/commit/dcc6e6780a9138731b64b9b5398a94a1d97033f0)

<a id="c03"></a>**C03.** tree 응답의 sha는 commit 식별자이며 commit JSON의 실제 root tree d9988e8928c8541c108a00df55b31848fc0055d1과 구분한다. 전체 1085항목(973blob·112tree)을 구조적으로 읽고 root 포함 113tree 해시를 재구성했다. 참조된 973blob 본문 전체 독해·실행을 뜻하지 않는다. [근거](https://github.com/decisionintelligence/DUET/commit/dcc6e6780a9138731b64b9b5398a94a1d97033f0)

## 확인한 호출 경로와 temporal expert

<a id="c04"></a>**C04.** DUET wrapper는 DUETModel을 만들고 이 모델은 utils/masked_attention의 FullAttention과 Mahalanobis_mask를 가져온다. 저장된 layers/SelfAttention_Family의 같은 이름 클래스와 실제 확인한 경로를 혼동하지 않는다. 저장소 전체의 모든 import 경로를 분석한 것은 아니다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/duet.py#L1-L68)

<a id="c05"></a>**C05.** CI가 켜지면 B×L×N 입력을 (B·N)×L×1로 바꿔 temporal expert를 공유하고 다시 B×N×d_model로 모은다. N>1일 때 channel transformer를 거치며 N=1이면 이 분기를 건너뛴다. head는 d_model을 pred_len으로 투영한다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/models/duet_model.py#L46-L81)

<a id="c06"></a>**C06.** 기본 학습 wrapper는 train subset에 StandardScaler를 fit하고 norm 조건에서 학습·검증·예측 입력을 변환한다. TCM routing과 CCM 주파수 mask는 내부 RevIN 적용 전 모델 입력을 읽고, RevIN은 원 입력을 in-place 수정하지 않는다. 따라서 내부 RevIN 전이라는 표현을 원 단위 통신 트래픽 그대로라는 뜻으로 쓰지 않는다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/models/duet_model.py#L50-L80)

<a id="c07"></a>**C07.** gate와 noise는 각각 bias 없는 Linear–ReLU–Linear encoder다. encoder의 mean은 마지막 channel 축에 적용되어 CI=True의 길이 1 축에서는 시간 이력을 평균해 없애지 않는다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/models/duet_model.py#L50-L59)

<a id="c08"></a>**C08.** 훈련 중 noisy_gating이 켜지면 Softplus(noise encoder)+0.01을 표준편차로 쓰고 noisy logits에 학습 W_h를 곱한다. 해당 조건이 거짓이면 clean logits를 쓰며 W_h를 적용하지 않는다. 훈련·평가 경로의 차이라는 정적 관찰이다. 성능 영향이나 버그의 실제 발생을 측정하지 않았다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/layers/linear_extractor_cluster.py#L130-L142)

<a id="c09"></a>**C09.** routing은 전체 expert의 softmax 뒤 top-k를 선택하고 선택 점수를 합계+1e-6으로 나눈 뒤 나머지 gate를 0으로 만든다. gate의 합은 이상적인 정확한 1 정규화와 차이가 있다. 유한한 양수 합계에 대한 산술이며 underflow·비정상 k의 동작을 재현하지 않았다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/layers/linear_extractor_cluster.py#L234-L254)

<a id="c10"></a>**C10.** 추가 loss는 importance와 load 각각의 CV² 합이다. noisy_gating=True, 훈련 중, k<M인 경로의 load helper에는 clean/noisy logits와 softmax 이후 top 값이 함께 전달되어 threshold와 비교값이 다른 수치 공간이다. M=2,k=1의 작은 예는 전달값의 차이를 보인다. 실제 확률 추정 오차나 훈련 실패로 단정하지 않는다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/layers/linear_extractor_cluster.py#L144-L169)

<a id="c11"></a>**C11.** 선형 expert는 moving-average 추세와 잔차를 두 선형 투영으로 합친다. 기본 moving_avg=25이며 padding은 양끝 값 반복이다. 공유 linear weight의 초기값은 1/seq_len이다. moving_avg와 폭은 설정값이며 여기서 새 모델을 초기화하거나 실행하지 않았다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/duet.py#L21-L26)

<a id="c12"></a>**C12.** SparseDispatcher는 양의 gate에 해당하는 sample만 모아 expert 입력을 만들고 결과를 gate 가중치와 index_add로 합친다. 빈 expert 입력은 별도 empty 결과 경로를 갖는다. 이 sparse dispatch를 channel 쌍 계산 제거 또는 RCTL 학습 횟수 절감으로 바꾸어 해석하지 않는다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/layers/linear_extractor_cluster.py#L41-L108)

<a id="c13"></a>**C13.** RevIN은 각 채널의 시간축 평균·표준편차를 detach하고 epsilon과 채널별 affine을 사용한다. CI reshape로 채널을 복원해 정규화한 뒤 expert에 보내며 예측 head 이후 denorm한다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/models/duet_model.py#L79-L81)

## Channel mask의 거리·확률·attention

<a id="c14"></a>**C14.** CCM은 rFFT의 절댓값에서 F=floor(L/2)+1 주파수 성분을 만들고 학습 A의 변환 후 제곱합을 거리로 쓴다. 입력 주파수 차이 tensor는 B×N×N×F로 명시적으로 만들어진다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/utils/masked_attention.py#L141-L162)

<a id="c15"></a>**C15.** 거리 d에 1e-10을 더한 값의 역수를 취하고 대각을 0으로 만든 뒤, detach한 행별 최댓값으로 나눈다. 이후 대각 1을 넣고 전체에 0.99를 곱하므로 대각 p도 0.99다. 행별 최대 정규화는 확률합 1 또는 대칭 행렬을 보장하지 않는다. 거리 행렬의 대칭성과 정규화된 행렬의 대칭성을 구분한다. endpoint/underflow의 실제 빈도는 미측정이다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/utils/masked_attention.py#L162-L180)

<a id="c16"></a>**C16.** 저장 코드는 [log(p/(1-p)),log((1-p)/p)]를 hard Gumbel-softmax에 넣는다. torch 2.4.1의 일반 Tensor 경로와 0<p<1의 대수에서 첫 범주 선택 확률은 p²/(p²+(1-p)²)이다. 원 코드/torch를 import하거나 sampling하지 않았다. 유한정밀도 endpoint는 이 수식의 범위 밖이다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/utils/masked_attention.py#L182-L197)

<a id="c17"></a>**C17.** 따라서 p=0.25의 예는 선택확률 0.1이고, p=0.99인 대각도 9801/9802의 확률이 되어 자기 연결을 반드시 보장하지 않는다. 실제 sampling 빈도를 측정하지 않았다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/utils/masked_attention.py#L174-L203)

<a id="c18"></a>**C18.** channel mask의 forward에는 train/eval 분기가 없고 매번 Gumbel sampling 함수를 호출한다. wrapper의 eval/no_grad만으로 이 호출이 사라지지 않는다. seed 재설정·deterministic 설정·실행 순서에 따른 재현 결과는 검증하지 않았다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/utils/masked_attention.py#L182-L207)

<a id="c19"></a>**C19.** FullAttention은 먼저 전체 score를 계산하고 mask=0 위치를 유한한 -log(1e10)으로 만든 뒤 score 전체를 1/sqrt(E)로 줄여 softmax한다. 따라서 mask=0이 attention의 정확한 0을 보장하지 않는다. 유한 실수와 제시한 조건에 대한 수식 해석이다. 부동소수 underflow나 실제 성능을 일반화하지 않는다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/utils/masked_attention.py#L83-L107)

<a id="c20"></a>**C20.** 한 kept score가 0이고 한 masked key만 있는 예에서 masked attention은 E=64일 때 약 0.05324, E=512일 때 약 0.26549다. 모두 masked인 유한 동일 score 행의 softmax는 dropout 전 균등하다. 작은 산술 예이며 실제 row의 연결 수·score·dropout 분포와 attention 관측값이 아니다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/utils/masked_attention.py#L95-L102)

<a id="c21"></a>**C21.** 생성한 mask는 B×1×N×N으로 head에 공유되고, 확인한 conv_layers=None encoder 경로에서는 동일 mask가 각 layer에 전달된다. soft 관계와 per-window sampling은 고정된 서로소 UPC 소속표와 다르다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/utils/masked_attention.py#L35-L65)

## 설정·학습·검증의 선언

<a id="c22"></a>**C22.** Config의 우선순위는 base 기본값→DUET 기본값→kwargs이며 horizon은 pred_len에도 대입된다. DUET 기본 batch256·huber·lr0.02·M4·k1을 실제 실행 설정으로 확정할 수 없다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/duet.py#L5-L54)

<a id="c23"></a>**C23.** 확인한 ETTh1·ILI·Traffic 스크립트의 12개 명령은 모두 MAE·norm=true·CI=1과 deterministic full을 요청한다. base는 loss가 MAE이면 L1Loss, MSE이면 MSELoss, 그 밖에는 HuberLoss(delta=0.5)를 선택한다. 스크립트 선언만 읽었다. CLI loader 전체와 실행 로그를 확인한 것이 아니다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/scripts/multivariate_forecast/ETTh1_script/DUET.sh#L1-L8)

<a id="c24"></a>**C24.** ETTh1의 예측 길이 96/192/336/720에 대해 선언한 batch는 32/64/128/32, lookback은 512/336/512/512, expert수는 2/4/4/4, k는 1/2/3/2다. 2026 commit의 요청값이며 논문 당시 선택 과정이나 성능을 증명하지 않는다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/scripts/multivariate_forecast/ETTh1_script/DUET.sh#L1-L8)

<a id="c25"></a>**C25.** ILI 스크립트는 예측 길이 24/36/48/60과 lookback 104·batch 8을 요청한다. 이 길이들은 H094에서 확인한 본문·표 행에 대응하지만 별도 캡션의 12/24/36/48 표기를 자동 교정하는 근거로 소급하지 않는다. 2026년 스크립트의 선언과 2025년 논문의 표기를 대조한 것이다. 논문의 캡션을 임의로 교정하거나 당시 실행을 확정하지 않는다. [근거](https://arxiv.org/html/2412.10859v3)

<a id="c26"></a>**C26.** Traffic 스크립트는 batch 16·epoch 10·patience 3·M4·k2를 요청하고 lookback은 336/336/512/512다. 추가 normalization=true 키가 실제 읽히는지는 norm=true와 구분한다. 전체 설정 consumer 검수 없이 normalization을 별도 기능으로 단정하지 않는다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/scripts/multivariate_forecast/Traffic_script/DUET.sh#L1-L8)

<a id="c27"></a>**C27.** 저장 rolling config는 tv_ratio 0.8, train_ratio_in_tv의 0.75/기본 0.875, horizon 336, stride 1, 최대 rolling 48000, seed 2021, deterministic efficient를 포함한다. 선언상 train 비율은 0.6 또는 0.7에 해당한다. 실제 split 전략·데이터 길이·CLI 최종 병합과 실행결과는 별도 검수다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/config/rolling_forecast_config.json#L1-L45)

<a id="c28"></a>**C28.** forecast_fit은 covariate 결합 뒤 열이 1개면 train_drop_last=False, 그 밖에는 True를 선택하고 DataLoader까지 전달한다. 검증과 예측은 False다. 이 2026 코드 분기는 README의 no Drop Last 설명과 차이가 있다. 논문 당시 실험이 이 분기를 썼거나 비교가 부당했다는 결론으로 확대하지 않는다. [근거](https://arxiv.org/html/2412.10859v3)

<a id="c29"></a>**C29.** DUET wrapper는 model.training일 때만 auxiliary loss를 반환하고 base 훈련은 task loss에 이를 더한다. 검증은 model.eval과 no_grad를 사용해 이 wrapper의 추가 loss를 받지 않는다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/duet.py#L63-L68)

<a id="c30"></a>**C30.** 검증 loader는 shuffle=True/drop_last=False이고 validation loss는 각 batch의 loss를 단순 평균한다. 기본 delta=0의 EarlyStopping은 첫 평가 및 이전 최선과 같거나 더 나은 점수에서 improved를 반환하며, base는 이때 checkpoint를 저장하고 예측에서 복원한다. batch 크기 차이·sampling·early stopping이 실제 결과에 미친 영향은 측정하지 않았다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/deep_forecasting_model_base.py#L328-L354)

## 계산 범위와 재검토 조건

<a id="c31"></a>**C31.** 주파수 차이와 변환 tensor는 dense B·N²·F이고 A에는 F²개 값이 있다. 현재 명시된 A×diff 곱은 B·N²·F²개의 곱 항을 가진다. attention score도 B·heads·N²로 모두 만든다. 이 산술을 구현의 실측 시간·전체 MAC·RCTL 모델 비용으로 사용하지 않는다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/utils/masked_attention.py#L83-L101)

<a id="c32"></a>**C32.** Traffic의 선언 batch=16과 논문의 N=862를 가정하면 L=336/512에서 float32 diff 한 개의 원소값 저장 공간은 각각 약 7.48482/11.38224 GiB다. 실제 allocator peak·gradient·temp·전체 GPU 메모리·시간을 측정한 값이 아니다. [근거](https://arxiv.org/html/2412.10859v3)

<a id="c33"></a>**C33.** 같은 commit README는 고정 lookback 96의 통일 설정 결과와 여러 lookback의 탐색 결과를 분리하고 bug 수정·재검사 사실을 적지만 특정 수정 diff를 여기서 제공하지 않는다. 연결된 결과 그림·unified 스크립트·이전 commit·retest 결과는 이번 보충 독해 범위 밖이다. [근거](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/README.md#L11-L20)

<a id="c34"></a>**C34.** 이 묶음은 저장 코드 4개 716행, commit/tree 2개와 보충 14파일 2063행·PyTorch 선택함수 60행을 읽은 정적 검토다. 원 81의 입력 선택과 비용 판단을 더 구체화하며 새 통신 트래픽 실험이나 DUET 재현을 제공하지 않는다. 원목록 추가 집계 대상은 코드 본문 4개와 전체 JSON 2개다. 재참조 3개·보충 15개·파생 수식/설정 자료에는 새 원목록 독해 수를 더하지 않는다. 원 81의 나머지 문헌 4·검색 1과 snapshot 연혁 고유 변경은 별도 검토 대상이다. [근거](../evidence/0090-input-partition/originals/SRC-0022042.md.txt)

팀이 이 방향을 다시 제안할 때에는 어떤 입력 관계의 오판이 단순 대안의 예측을 실제로 해치는지, 고정 소속에서 별도 이점이 있는지, 거리·mask·학습까지 포함한 비용 기준이 무엇인지 먼저 연결해야 한다. 비교할 구현은 판본과 최종 설정을 고정하고 위 차이가 결과에 미치는 영향을 별도 연구 질문으로 삼는다. 이 정리 과정에서 해당 실험을 실행한 것은 아니다.

원81의 [잔여 5개 그룹](../evidence/0095-duet-code/packet-coverage.json), snapshot 연혁 고유 변경, 다른 과거 기록 및 전체 실패·비용 통합은 계속 검토한다.
