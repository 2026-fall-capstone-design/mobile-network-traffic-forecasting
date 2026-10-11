# 원81 CCM 저장 구현: 확률·손실·입력 차원 대조

[출처](../sources/history-093.md) · [주장별 근거](../verification/history-093-claims.json) · [검수](../verification/history-093.md) · [논문 검토](0092-ccm-source-review.md)

원81의 CCM 구현 관찰을 고정 판본과 대조한다. 코드의 동작 명세, 그 명세에서 도출한 조건부 위험, 실제 실험 결과를 구분한다. 이 기록은 정적 검토이며 새 모델 실험이나 재현 성공 보고가 아니다. 아래에서 B는 batch 크기, L은 입력 길이, C는 채널 수, K는 군집 수, d는 embedding 차원, H는 출력 길이다.

## 판본과 확인 범위

<a id="c01"></a>**C01.** 원소장 자료는 exp_ccm.py 379행, Dlinear.py 100행, attention.py 149행, layers.py 393행과 commit/tree JSON 전체다. 여섯 고유 그룹·동일 사본 열두 경로를 대조했다. 코드 1,021행 전체를 읽었으며 연구 코드 import·실행·학습·추론은 0이다. H093은 정리용 ID로 실험 횟수가 아니다.

<a id="c02"></a>**C02.** 저장 판본은 TimeSeriesCCM의 commit `e4769baa7f8457358eb9b4614af2de1fbfba2257`, 기록 시각 2024-10-30T22:54:50Z, 메시지 Update README.md다. 코드 네 파일의 Git blob SHA와 크기가 저장 tree에 일치한다. 이를 최신 코드나 논문 모든 결과의 실제 실행 판본으로 확정하지 않는다.

<a id="c03"></a>**C03.** tree JSON에는 71항목과 truncated=false가 있다. 응답 최상위 sha는 commit ID이며, 직접 자식 항목으로 재구성한 root tree `f33abc065c96498c145beefeee8a509dec232810`은 commit.tree.sha와 일치한다. GitHub verified=true는 저장된 서비스 판정이다. 나머지 tree 항목의 본문 독해나 서명 독립 검증을 뜻하지 않는다.

<a id="c04"></a>**C04.** Dlinear의 wildcard import를 확인하기 위해 같은 commit의 models/patch_layer.py 376행을 새 보충 자료로 읽었다. SHA-256과 Git blob을 확인했으며 원목록 독해 수에는 추가하지 않는다. main·data_loader·exp_basic·utils, 다른 모델의 본문, 실제 config·checkpoint·seed별 결과·M4/Stock 실행 경로는 이 묶음에서 확인하지 않았다.

## 실제 이름과 예측 경로

<a id="c05"></a>**C05.** Dlinear는 layers 다음 patch_layer를 wildcard import한다. patch_layer는 layers를 다시 import하고 Cluster_assigner를 재정의하지 않으며 __all__도 없다. 따라서 확인한 정의는 layers의 공개 Cluster_assigner와 patch_layer의 Cluster_wise_linear다. layers의 두 `_Cluster_assigner` 정의 및 주석 처리한 대안은 이 공개 클래스의 활성 구현과 구분한다.

<a id="c06"></a>**C06.** DLinearC는 양 끝값을 반복해 padding한 kernel 25 이동평균을 trend로, 원입력에서 뺀 값을 seasonal로 만든다. individual='i'는 채널별 선형층, 'c'는 군집별 혼합 선형층, 그 외는 공유 선형층이다. seasonal/trend 출력을 더해 [B,H,C]로 돌려준다. 이 분기를 전체 RCTL 모델 K개를 따로 적합하는 절차와 동일시하지 않는다.

<a id="c07"></a>**C07.** 생성 시 channels는 args.data가 대문자 'M4'이면 batch_size, 아니면 data_dim이다. 군집 수·입력/출력 길이·embedding 차원도 args에서 받는다. 실제 entrypoint와 인자 값이 없어 이 조건이 논문의 M4나 Stock 실험에서 선택되었는지는 미확인이다. 코드 기본값과 논문별 실행 설정을 섞지 않는다.

<a id="c08"></a>**C08.** 활성 Cluster_assigner는 각 채널의 길이 L 입력을 단일 Linear(L,d)에 넣고 L2 정규화 후 prototype과 cosine 내적한다. 주석의 MLP와 ReLU 경로를 실행 구현으로 읽으면 안 된다. 초기 prototype은 K×d의 일반 Tensor를 Kaiming uniform으로 초기화하며 이 위치의 nn.Parameter는 주석이다.

<a id="c09"></a>**C09.** [B,C,K] cosine 점수를 batch 축으로 평균한 다음 정규화해 [C,K] 확률을 만든다. 먼저 계산한 prob_temp의 정규화 결과는 이후 사용하지 않는다. 같은 채널 위치의 확률은 함께 들어온 batch 자료에 의존하므로, 이 식을 각 sample의 독립 posterior 또는 전체 학습자료에서 한 번 고정한 소속으로 설명하지 않는다.

<a id="c10"></a>**C10.** 활성 sinkhorn 함수는 exp(score/0.05)를 행 합으로 나눈다. sinkhorn_iterations=3 인자를 실제 반복에 사용하지 않고 열 질량을 맞추는 문장도 없다. 반복 균형화 코드는 주석이다. 따라서 함수명만으로 balanced optimal transport나 균등한 군집 크기를 보장한다고 쓰지 않는다.

<a id="c11"></a>**C11.** prototype 계산의 mask는 [C,K] 확률에 logistic 잡음과 temperature 0.07을 적용한 연속 sigmoid 값이다. one-hot 배정이 아니며 주석의 [B,C,K]와 실제 반환 차원을 구분한다. 평가 모드에서 이 난수 생성을 건너뛰는 조건은 없다.

<a id="c12"></a>**C12.** layers의 CrossAttention은 별도 학습 q/k/v projection 없이 한 head로 prototype을 query, 채널 embedding을 key/value로 사용한다. 활성 MaskAttention은 softmax와 dropout 이후 mask를 곱하고 다시 합이 1이 되도록 정규화하지 않는다. 논문 Eq.3의 학습 projection과 마스킹 후 Normalize 표기와 구분한다. attention.py의 projection을 가진 별도 MaskAttentionLayer나 주석의 선마스킹 대안을 이 경로로 바꾸지 않는다.

<a id="c13"></a>**C13.** Cluster_wise_linear는 K개 선형층의 출력을 [B,C,H,K]로 쌓아 [C,K] 확률로 가중합한다. Dlinear의 두 분해 성분에 각각 적용된다. 이 구현 위치는 예측값 혼합이며, 주석 처리한 선형층 가중치 평균 코드와 구분한다. 새 backbone K개를 독립 학습했다는 근거가 아니다.

## prototype과 실행 조건

<a id="c14"></a>**C14.** Dlinear의 c 경로는 if_update=False여도 assigner와 prototype attention을 계산한다. if_update=True일 때만 반환 prototype으로 self.cluster_emb를 새 nn.Parameter로 교체한다. 따라서 prototype 갱신을 끄는 것과 계산 자체를 생략하는 것은 다르다. 갱신하지 않는 현재 forward의 예측 혼합에는 prob_avg를 쓰므로 mask 난수만으로 그 예측값이 바뀐다고 단정하지 않는다.

<a id="c15"></a>**C15.** 확인한 p2c 반환은 [B,K,d]이고 Dlinear의 저장 위치 전에는 batch 평균이나 squeeze가 없다. 이를 교체한 뒤 다음 assigner 호출이 cluster_emb.t()와 torch.mm에 전달하는 흐름은 2차원 prototype 계약과 충돌한다. 이는 해당 c·갱신 경로를 따를 때의 정적 차원 위험이며 실제 논문 실행에서 관측한 예외 로그가 아니다.

<a id="c16"></a>**C16.** train은 첫 forward 전에 model.parameters()로 Adam을 만든다. 이후 Dlinear가 새 Parameter를 교체하는 위치는 있지만 이 파일들에는 해당 optimizer의 parameter group에 추가하거나 optimizer를 다시 만드는 문장이 없다. Module에 Parameter가 등록되는 것과 이미 생성한 optimizer가 새 객체를 갱신하는 것을 구별해야 한다. 실제 환경의 optimizer 상태는 미소장이다.

<a id="c17"></a>**C17.** Dlinear.py에는 RevIN 호출이 없다. 보충 Patch_backbone에는 RevIN norm/denorm 호출이 있고 TimeVarAttentionLayer에는 cluster_emb.mean(0)이 있지만 이는 다른 경로다. 그 평균을 Dlinear의 prototype 반환에 있다고 간주하면 안 된다. loader 전처리와 다른 backbone은 미확인이라 모든 모델이 논문의 정규화 조건을 어긴다고 일반화하지 않는다.

## 입력과 군집 손실

<a id="c18"></a>**C18.** 공통 _process_one_batch는 train·validation·test 여부와 관계없이 채널 randperm을 만들고 x와 y를 같이 재배열한다. 반환값에는 원채널 순서나 permutation이 없고 역변환 분기에도 채널 순서 복원은 없다. 저장 pred/true의 마지막 축을 batch 사이에 같은 cell ID로 해석하기 전에 이 순서 정보를 확인해야 한다.

<a id="c19"></a>**C19.** train/vali는 공통 처리 뒤 군집 유사도를 caller의 원래 batch_x로 계산하지만 model.cluster_prob는 재배열된 x에서 나온다. shape를 맞추더라도 동일한 채널 순서의 S와 membership인지 별도 확인해야 한다. i 분기의 채널별 선형층도 재배열된 위치에 적용된다. 이러한 정적 순서 위험을 실제 성능 손해나 데이터 누수의 관측 증거로 바꾸지 않는다.

<a id="c20"></a>**C20.** 코드에 적힌 입력 [B,L,C]에서 C>1이면 squeeze(-1)는 차원을 줄이지 않는다. 앞쪽 두 축의 차이를 만든 뒤 마지막 축을 합하면 유사도는 [B,B,L]이다. 이를 [C,K] membership과 torch.mm으로 곱하는 경로는 2차원 행렬 계약에 맞지 않는다. C=1일 때는 [B,B]가 되지만 C×C와 호환하려면 B=1이어야 한다. 입력 계약에 대한 차원 추론이며 실행 검증은 아니다.

<a id="c21"></a>**C21.** 유사도 식은 exp(−5·dist_squared/max(dist_squared))다. 논문의 표준화한 채널 시계열과 RBF σ=5를 그대로 구현했다고 볼 수 없다. 최대 거리가 0일 때의 분모 보호도 이 함수에는 없다. 정확한 자료 전처리·배치 구조와 후속 수정판을 확보하기 전, 논문의 유사도 정의나 수치를 이 저장 함수로 재현했다고 표시하지 않는다.

<a id="c22"></a>**C22.** 활성 similarity_loss_batch는 별도의 Concrete mask M을 만들고 −Tr(MᵀSM)+Tr((1−MMᵀ)S)+C에 평균 entropy 항 H(p)를 더한다. 여기서 H(p)는 코드의 −p·log(p+10⁻¹⁵)를 K축 합산한 뒤 C축 평균한 값이다. scalar 1은 모든 원소가 1인 J로 broadcast되며 identity I가 아니다. +C와 entropy 항도 논문 Eq.4의 인쇄식과 구분한다. 주석의 membership=prob와 저장 유사도 파일을 읽는 별도 underscore helper는 활성 호출이 아니다.

<a id="c23"></a>**C23.** S가 호환되는 고정 행렬이라는 가정에서 코드의 trace 부분은 Tr(JS)−2Tr(MᵀSM)+C로 정리된다. 논문의 I 표기에서는 상수 부분이 Tr(S)다. 이 차이는 고정 S에 대해 상수 차이이며 entropy까지 동일하다는 뜻은 아니다. 대수 관계만으로 실제 군집 붕괴나 논문 무효, 최종 RCTL 개선을 결론 내리지 않는다.

## 최적화·선택·평가

<a id="c24"></a>**C24.** 저장 train은 Adam과 MSE 예측 손실을 사용하고 c일 때 β·군집 손실을 더해 backward/step한다. 예측기와 assigner를 함께 조정하려는 흐름은 확인되지만 앞선 차원·등록 조건과 실제 실행 여부는 별개다. 원81이 비교하는 군집별 다중 출력 RCTL의 별도 학습과 같지 않다.

<a id="c25"></a>**C25.** _get_data는 train/val에 data_path·data_split, test에 test_data_path·test_data_split을 전달한다. train/val loader는 shuffle=True, test는 False이고 모두 drop_last=False다. 별도 eval은 data_path·data_split·scale=True·scale_statistic으로 Dataset_MTS를 직접 만든다. 시간 경계·표준화 fit 범위·누수 여부는 실제 인자와 Dataset_MTS 본문이 없어 확정할 수 없다. shuffle 옵션 자체를 시계열 train/test 누수의 증거로 삼지 않는다.

<a id="c26"></a>**C26.** 매 epoch validation과 test를 모두 계산하고 기록하지만 early_stopping에는 vali_loss를 전달한다. c의 vali_loss는 예측+β·군집 손실이다. 코드의 checkpoint 선택을 test 최소값 선택이나 MSE만의 선택으로 바꾸지 않는다. 실제 연구자의 수동 튜닝과 실행별 선택 이력은 이 파일만으로 확인되지 않는다.

<a id="c27"></a>**C27.** vali는 eval/no_grad에서 수행하지만 군집 손실 함수 내부의 Concrete 난수에는 평가 분기가 없다. 따라서 eval/no_grad라는 이유만으로 combined validation loss가 결정적이라고 보장할 수 없다. 이는 C14의 prototype mask가 현재 예측에 쓰이지 않는다는 관찰과 서로 다른 경로다.

<a id="c28"></a>**C28.** vali의 loss는 batch별 값의 단순 평균이고 MSE/MAE 등 반환 metric은 batch 크기를 곱한 뒤 전체 instance 수로 나눈다. drop_last=False이므로 마지막 batch가 작을 때 두 집계의 가중치가 다를 수 있다. 실제 utils.metric 정의와 최종 논문 표의 집계까지 이 위치만으로 확정하지 않는다.

<a id="c29"></a>**C29.** test/eval 저장 경로는 metrics.npy·pred.npy·true.npy를 만들고 train은 args·scaler·checkpoint 저장을 명세한다. 이 이름과 파일 작성 코드가 존재한다는 사실은 실제 결과 파일·성능·재현 성공의 증거가 아니다. 채널 재배열과 inverse_transform의 단위/열 대응도 결과 재사용 전에 확인해야 한다.

<a id="c30"></a>**C30.** 이 묶음에는 모델 학습/추론 시간·GPU 사용량·실행별 실패 로그와 총비용 값이 없다. 호출 구조상 K개 선형 출력, 매 batch prototype attention과 군집 손실, 매 epoch validation/test가 있음을 비용 조건으로 남긴다. 출력용 epoch timer는 학습 loop 전부터 validation/test 이후까지이며 초기 자료 적재·모델 준비와 뒤의 checkpoint 선택/저장을 모두 포괄하지 않는다. 논문의 부분 복잡도나 시간 표를 이 저장 코드의 실측 비용으로 옮기지 않는다.

## 과거 판단과 재사용 조건

<a id="c31"></a>**C31.** 원81은 layers 262행의 batch 평균 확률과 exp 154–178행의 joint backward를 CCM 관찰로 적었다. 그 위치는 확인되지만 sinkhorn의 균형 제약, 모든 경로의 정상 작동, 논문 재현까지 뒷받침하지 않는다. 당시 판단을 보존하면서 이번에 확인한 활성 구현과 조건부 위험을 후속 주석으로 연결한다.

<a id="c32"></a>**C32.** 논문의 zero-shot은 훈련된 공유 지식으로 미관측 채널을 다루는 보고이며, 이 네 코드만으로 Stock/M4 평가 프로토콜을 검증하지 못한다. batch 평균 소속, prototype 고정/계산, 입력 정규화, 평가 단위와 채널 ID를 각각 확인해야 한다. CCM 결과를 독립 UPC 모델이나 RCTL의 기대 이득으로 대체하지 않는다.

<a id="c33"></a>**C33.** 재사용 전에는 고정 commit·실제 entrypoint/인자·의존 파일·환경을 확보하고 [B,L,C]→확률→prototype→유사도 차원 및 채널 순서, optimizer 등록과 checkpoint 선택을 점검해야 한다. 변경한다면 보정 사본과 원판본을 분리하고 차이를 기록한다. 이는 후속 실험 설계 조건이며 이번 아카이브 작업에서 모델 실행을 승인하거나 수행한 기록이 아니다.

<a id="c34"></a>**C34.** 원81의 소장 외부 자료 중 이 코드/metadata 여섯 그룹을 추가로 연결하면 미검토는 15그룹(DUET 논문4·predictive-variable-clustering 논문4·DUET 코드4와 commit/tree2·검색1)이다. snapshot23의 연혁 고유 변경분과 원82 이후·이전 부분 기록·전체 실패/비용 통합·장기 팀 접근·최종 검색 검수도 남는다. 같은 내용을 다시 제안할 때 이 검토와 달라지는 정보·모델·배치·선택 기준을 명시한다.

## 팀원이 확인할 근거

| 확인할 내용 | 자료 |
|---|---|
| 원문 SHA·읽기 범위·고정 URL | [출처 명세](../evidence/0093-ccm-code/manifest.json) |
| 함수 정의와 활성/주석 경로 | [정적 함수 지도](../evidence/0093-ccm-code/function-map.json) |
| 확률·prototype·유사도·손실의 차원/대수 | [정적 관찰](../evidence/0093-ccm-code/static-observations.json) |
| 저장 코드와 Git 객체 대응 | [Git 내용 대조](../evidence/0093-ccm-code/git-content-correspondence.json) |

공식 판본: [TimeSeriesCCM commit](https://github.com/Graph-and-Geometric-Learning/TimeSeriesCCM/tree/e4769baa7f8457358eb9b4614af2de1fbfba2257). Python wildcard의 공개 이름 규칙은 [언어 문서](https://docs.python.org/3/reference/simple_stmts.html#import), 차원 제약은 [torch.mm](https://docs.pytorch.org/docs/2.14/generated/torch.mm.html)과 [torch.t](https://docs.pytorch.org/docs/2.14/generated/torch.t.html), 등록의 구별은 [Parameter](https://docs.pytorch.org/docs/2.14/generated/torch.nn.parameter.Parameter.html)와 [optimizer 추가 API](https://docs.pytorch.org/docs/2.14/generated/torch.optim.Optimizer.add_param_group.html)를 참고했다. 이는 현재 공식 API의 의미 확인이며 당시 설치 버전을 검증한 것이 아니다.
