# 원79 EMD-CFL 구현: 논문과 저장 코드의 조건 대조

[출처](../sources/history-085.md) · [검수](../verification/history-085.md) · [코드 경로 근거](../evidence/0085-emd-cfl-code/README.md) · [논문 검수](0084-emd-cfl-embedding-distributions.md)

저장된 고정 commit의 전체 첫 정적 독해 후36개 주장을 원문과7묶음으로 다시 대조했다. 정적 관찰·조건부 위험과 실제 실행 결과를 구분한다. H085는 정리용 ID이며 새 실험 번호가 아니다.

## 범위와 고정 판본

<a id="c01"></a>**C01.** H085는 원79의 공식 EMD-CFL 저장 구현 묶음7개(README1·Python4·commit/tree JSON2)를 정적으로 검토한 기록이다. README11행, runner89행, center289행, trainer1901행, utils167행과 JSON2 전체를 읽었다. 원연구 코드 실행·import·학습·추론·성능 재현은0이며, 새 독립 텍스트5개와 전체 JSON2개를 구분한다.

<a id="c02"></a>**C02.** 저장 commit은 f48a2cfe53079cc6bc1d89f4771cb7a5a62804c5, 기록된 시각은2025-06-09T10:40:09Z이고 변경 메시지는 README 추가다. parent와 root tree를 보존하고 README/Python4의 Git blob SHA·크기가 tree 항목과 일치함을 확인했다. 현재 저장소 최신 코드나 논문 모든 실험의 실제 실행 판본이라고 확정하지 않는다.

<a id="c03"></a>**C03.** tree JSON은35항목(34blob·1directory), truncated=false다. 최상위 sha는 commit ID로 저장돼 있지만 entries로 재구성한 root tree c217ff388c72be60ddc78e0555de50e36cfc6d5c는 commit.tree.sha와 일치하며 src subtree도 일치한다. GitHub의 verified=true는 저장된 서비스 판정이고 PGP 서명을 이번에 독립 검증했다는 뜻은 아니다.

<a id="c04"></a>**C04.** README는 config.yaml, src의 코드, data 디렉터리와 test.py/test_config.yaml을 안내한다. 저장 tree에는 LICENSE·config·data.py·model.py·test.py·부분 참여 runner·다른 runner·데이터 notebook이 있으나 이7개 묶음에 해당 본문은 없다. 목록의 해시·크기는 파일을 읽었다는 증거가 아니며 전체 외부 저장소를 재현 가능한 상태로 확보했다고 쓰지 않는다.

## 설정과 전체 참여

<a id="c05"></a>**C05.** runner는 config의 seed로 torch·NumPy·Python random을 초기화하고 device·model_type·학습률·batch·worker·global/local epoch·저장주기·tolerance·num_clusters·proj_ratio를 전달한다. 기본 config 경로는 있지만 실험별 실제 값과 seed ID가 이 묶음에 없어 논문3회 실행을 복원하지 못한다. CUDA 사용 가능 시 지정 device를 선택하고 아니면 CPU로 분기한다.

<a id="c06"></a>**C06.** Center는 optimizer 인자를 저장하나 get_optimizer는 SGD를 직접 생성한다(momentum0.9, weight_decay10^-6). update_weights마다 optimizer를 다시 만들어 이전 optimizer 상태를 이어받지 않는다. 기본 local_step은 cross-entropy 분류 학습이다. 이를 RCTL 회귀의 loss·optimizer 설정이나 고정 TabICL 추론과 같다고 간주하지 않는다.

<a id="c07"></a>**C07.** runner와 trainer는 한 프로세스에서 모든 client/server 모델 사본과 각 client train/validation 객체를 사용한다. 이 코드의 계산 흐름은 논문을 이해하는 근거지만, 실제 네트워크 encoder 교환·비밀 projection 공유·서버 접근 통제·통신량 측정을 구현하거나 검증했다는 근거는 아니다.

<a id="c08"></a>**C08.** fit_emdcfl은 client별 모델 ID로 시작하고 clustering_epochs={0}으로 둔다. 첫 global round에서 각 client의 local 학습을 끝낸 뒤 encoder 사본에 feature_extraction=True를 설정해 거리를 계산한다. 이후 저장한 이웃집합을 유지하면서 매 round local 학습과 이웃별 자료수 가중 집계를 이어간다.

<a id="c09"></a>**C09.** 기준 τ는 자신의 train 대 자신의 validation이며, 상대 거리는 자신의 train 대 각 상대 validation을 자신의 encoder로 비교한다. 모든 c와 상대 client를 순회하므로 역방향은 상대 encoder의 별도 호출에서 계산된다. 논문 Algorithm1의 c′ loop 누락·역방향 인자 표기를 그대로 실행한 코드라고 단정하지 않는다.

## 거리·projection·집계 조건

<a id="c10"></a>**C10.** 자기 기준 거리 호출은 proj_ratio를 전달하지 않아 기본1을 쓰고, 상대 거리 호출은 config의 proj_ratio를 전달한다. get_wd는 ratio1에서도 새 정사각 random projection을 만들므로 identity 연산이 아니다. 논문의 τ 식은 R이 없는 Z끼리의 거리로 표기되어 있다. 이 차이를 남기되 논문이 τ와 상대 거리에 같은 R을 쓴다고 임의로 가정하지 않는다.

<a id="c11"></a>**C11.** 검토한 EMD 전체/부분 참여 호출은 max_sample=512를 전달한다. 이때 get_wd는 source와 target 각각이 상한을 초과하면 각자 새 randperm으로512개를 선택한다. 함수 자체의 기본 max_sample은 None이다. 이 함수에는10%를 계산하는 분기가 없다. 논문§3.1의 min(10%,512) 설명과 구분해야 하며 data.py의 사전 분할이나 별도 설정을 확인하지 않고 모든 실행 표본 수가 논문과 달랐다고 확정하지 않는다.

<a id="c12"></a>**C12.** 각 get_wd 호출은 d×int(proj_ratio·d)의 randn 행렬을 만든 뒤 각 행을 L2 정규화하며 source와 target에 같은 행렬을 적용한다. 호출 사이에는 R을 저장·재사용하지 않는다. τ·자기쌍·상대쌍·역방향의 표본과 projection이 같다는 보장이 이 경로에는 없다. 비율과 출력 차원이 유효한지도 실제 config와 함께 확인해야 한다.

<a id="c13"></a>**C13.** 기본 경로는 cosine ground cost의 ot.dist와 균등 질량 a,b에 대한 ot.emd2를 사용한다. 저장 get_wd에는 Sinkhorn 분기가 없다. cosine 기반 계산을 Euclidean 거리의 이론식·JL 보장이나 gradient 유사성의 직접 검증으로 바꾸지 않는다. 논문의 Sinkhorn 부록 결과를 이 함수만으로 재현한 것으로 표시하지 않는다.

<a id="c14"></a>**C14.** get_embeddings에는 model.eval()이나 no_grad 문맥이 없고 forward 결과를 detach해 CPU로 옮긴다. Center의 validation 호출은 끝에서 train()으로 돌아가므로 복사한 encoder가 학습 모드를 유지할 수 있다. BatchNorm·dropout 등이 있다면 추출 결과/상태에 영향이 생길 수 있으나 model.py와 실행을 확인하지 않아 실제 영향은 미확인이다.

<a id="c15"></a>**C15.** 전체 참여는 other_wd−τ를 소수4자리로 반올림한 값에 strict < tolerance를 적용한다. 부분 참여는 표시용 값만 반올림하고 판정은 원래 mean_distance로 한다. 따라서 두 경로의 경계 판정이 완전히 같다고 가정하지 않으며 tolerance의 실제 값도 config 없이는 확정하지 않는다.

<a id="c16"></a>**C16.** find_neighborhoods는 adjacency와 transpose의 원소별 곱으로 양방향 edge만 남기고, Graph의 각 이웃집합을 frozenset으로 만든다. cluster_neighborhoods는 이웃집합이 정확히 같은 client에 같은 model ID를 준다. 연결요소를 구하거나 서로소 UPC partition을 직접 만드는 절차와는 다르다.

<a id="c17"></a>**C17.** average_weights_clusterwise는 모델 ID를 받은 client 목록 자체가 아니라 해당 이웃집합에 들어 있는 client들의 weights와 자료 수를 취한다. 서로 다른 이웃집합이 겹치면 같은 client의 weights가 여러 집계에 들어갈 수 있다. 저장 membership의 모델 ID와 집계 구성원을 구분해서 읽어야 한다.

<a id="c18"></a>**C18.** 전체 참여의 자기쌍도 새로운 표본·projection으로 다시 계산되며 대각 원소를 항상 True로 강제하는 문장은 없다. 만약 어떤 이웃집합이 비게 되면 average_weights의 weights[0]에 빈 목록이 전달되는 경로가 있다. 이는 입력 조건을 검토할 정적 위험이며 논문 실험에서 실제 발생한 오류나 실패로 기록하지 않는다.

<a id="c19"></a>**C19.** fit_emdcfl의 num_clusters는 find_distance_threshold가 연속 client ID를 같은 크기 블록으로 나누어 거리 진단 CSV를 쓰는 데 사용한다. 이 함수는 threshold를 반환하지 않고, 군집 판정에는 입력 tolerance와 이웃집합을 쓴다. 따라서 runner에 K 인자가 있다는 이유만으로 정답 K로 군집 수를 강제했다고 해석하지 않는다.

<a id="c20"></a>**C20.** 진단 CSV의 min_cluster_iidness에는 nanmax, max_cluster_iidness에는 nanmin이 들어간다. 코멘트의 가장 먼/가까운 거리와 열 이름을 함께 확인해야 한다. 이 진단은 PACS의 불균등 domain 전용 분기를 포함하지 않는다. 진단 표기를 실제 군집 판정 로직이나 논문 ARI의 직접 원자료로 간주하지 않는다.

## 부분 참여와 비용

<a id="c21"></a>**C21.** fit_emdcfl_partial은 매 round p_num개 client를 비복원 추출해 선택된 client만 학습한다. 그러나 거리 계산은 한 번이라도 참여한 모든 client 사이에서 매 round 다시 한다. 이는 논문 Algorithm1의 W가 비어 있을 때 쌍별 한 번 계산한다는 절차 및 전체 참여 코드의 첫 round 고정과 구분된다.

<a id="c22"></a>**C22.** 부분 참여는 미참가 client를 초기 singleton으로 두고 누적 참여 집합을 확장한다. 이웃별 집계에서는 현재 round 참가자만 추리는 필터 없이 해당 이웃들의 보유 weights와 전체 train 크기를 사용한다. 과거에 참가했지만 이번 round에는 학습하지 않은 client도 포함될 수 있다. 이 동작만으로 논문 Table6의 ARI0.93 원인을 확정하지 않는다.

<a id="c23"></a>**C23.** fit_gt도 누적 참여 상태로 정답 adjacency를 만들고 이웃별 집계를 한다. get_gt_clustering은 일반 자료를 연속 ID의 같은 크기 블록으로, pacs500을[4,4,3,7]블록으로 만든다. data.py가 없어 이 순서를 논문의 photo/art/cartoon/sketch 순서와 대응시킬 수 없으며 단순한 배열 순서 차이를 domain 수 오류로 단정하지 않는다.

<a id="c24"></a>**C24.** runner의 elapsed_time은 fit_emdcfl 호출 전후의 time.time 차이다. 앞선 모델 생성·자료 적재·writer 준비는 이 구간 밖이며 fit 안의 validation·거리·집계·저장·선택적 embedding 출력은 안에 있다. 측정 위치를 논문 Table4의 모든 환경·통신·준비 비용이나 현재 실행 시간으로 바꾸지 않는다.

<a id="c25"></a>**C25.** --get_embs는 추가 randperm과 encoder forward 및 npy 저장을 fit 안에서 수행한다. 따라서 같은 seed만으로 해당 옵션을 켠 실행과 끈 실행의 거리 표본·projection·시간이 동일하다고 보장할 수 없다. 실제 옵션값·저장 embedding은 이 묶음에서 확인되지 않았다.

<a id="c26"></a>**C26.** `wd_<dataset>.txt`는 w 모드여서 같은 dataset의 후속 실행이 덮어쓴다. runner는 기존 run_record CSV를 읽어 config와 log_dir를 덧붙이며, save_models는 membership CSV와 center/cluster checkpoint 경로를 정의한다. 경로와 저장 코드가 있다는 사실을 결과 파일이 실제 생성되었거나 논문 수치를 재현했다는 증거로 세지 않는다.

## 평가와 비교군의 확인 항목

<a id="c27"></a>**C27.** Trainer.test는 batch별 평균 loss를 batch 수로 나누고 accuracy는 전체 hits를 전체 sample 수로 나눈다. 마지막 batch의 크기가 다를 때 loss는 전체 sample의 가중 평균과 달라질 수 있다. test.py가 이 묶음에 없어 이 함수가 논문 최종 표 전체의 산식이라고 단정하지 않는다.

<a id="c28"></a>**C28.** trainer에는 EMD 전체/부분 참여 외에16개 fit 경로가 들어 있다. 전체 본문을 읽고 함수 위치를 연결했지만 각 baseline 원논문·별도 runner·config·실행 결과를 모두 검증한 것은 아니다. 논문에 비교군이16개 있다는 사실과 이 파일의 함수 수가 같다는 것만으로 평가 조건의 일치를 확정하지 않는다.

<a id="c29"></a>**C29.** 이 스냅샷의 fit_fedclust는 초기 local 학습 뒤 cluster server를 집계한다. 이후 range(1, epochs) 안에는 local 학습·membership·checkpoint 저장이 있지만 server weights를 다시 집계하는 호출은 보이지 않는다. 이 정적 흐름은 재사용 전 확인할 항목이며 저자가 보고한 FedClust 수치의 원인이나 모든 판본의 오류라고 일반화하지 않는다.

<a id="c30"></a>**C30.** pFedGraph와 FedSAC는 client별 업데이트 loop 안에서 all_weights를 다시 취하고 곧바로 해당 client를 갱신한다. 그래서 뒤 client의 집계는 같은 round 앞 client의 갱신값을 포함할 수 있다. 모든 client가 동일한 사전 snapshot으로 동시에 집계한다고 가정하면 안 된다. 실제 성능 영향과 원논문 일치는 별도 확인 대상이다.

<a id="c31"></a>**C31.** FedCE의 best_cluster 선택과 hist_assoc 증가가 server 후보를 순회하는 loop 안에 있다. 모든 후보를 평가한 뒤 선택된 하나에 한 번만 가산하는 흐름으로 설명하면 코드와 달라진다. 이 위치와 후속 softmax 집계를 보존하며 실행 결과나 baseline 원논문의 의도를 이번 독해로 확정하지 않는다.

<a id="c32"></a>**C32.** IFCA는 validation loss로 model을 고르고, FedSoft는 validation batch의 최소 loss 모델에 sample 수를 배정한다. PACFL 경로는 validation class label별 SVD에서 K=3으로 정하고 앞쪽 최대3개 성분을 취한다. CFL의 EPS1/2는0.4/1.6, FlexCFL의 intergroup_lr는5로 적혀 있다. 이는 저장 경로의 설정이며 모든 논문 실험의 최종 config나 최적값으로 확정하지 않는다.

<a id="c33"></a>**C33.** CenterFedProx는 parameter별 L2 norm의 합을 proximal 항으로 쓰며 제곱 norm으로 인쇄된 코드가 아니다. FeSEM은 round 시작의 server 집계 후 local 학습을 하고 마지막에 server를 저장하는 순서다. EM/RC는 sample posterior를 가중한 CE 경로다. 모델·runner·config가 빠진 상태에서 이 코드를 그대로 공정한 비교군 구현으로 채택하지 않고 해당 선택을 먼저 확인한다.

## 재현 공백과 후속 연구

<a id="c34"></a>**C34.** 원 논문은 이미지 분류 실험이므로 트래픽 시계열의 시간 분할은 해당 없음이다. 저장 자료만으로 학습/평가 전처리, model.feature_extraction 동작·native 차원, 실제 seed·tolerance·projection·epoch 설정, 최종 test 산식과 seed별 결과·오차 정의·하드웨어별 비용은 이 묶음으로 모두 복원되지 않는다. 논문의 ResNet18 차원512/768 차이도 model.py를 읽기 전에는 해소된 것으로 표시하지 않는다.

<a id="c35"></a>**C35.** 원79는 EMD-CFL을 본떠 최종 RCTL encoder를 쓰면 당시의 model-independent 조건을 충족하지 못한다고 판단했다. 관측 x와 고정 TabICL의 조건부 평균 m(x)를 비교하려는 다음 후보는 다른 정보를 쓴다. 이 구현 독해는 expected gradient 관계·유한 batch SGD 잡음·최종 RCTL test 이득을 검증한 새 실험이 아니다.

<a id="c36"></a>**C36.** 원79 외부21그룹 중 기존 명세·Crossref4, FMCL5, EMD 논문2와 이번 구현7을 연결하면18그룹이며 Toso HTML/TXT2와 검색1이 남는다. 나머지 원문과 원80의 저장 결과를 별도로 대조한다. 과거 문서의 Goal·예산·실험 지시를 재개하지 않으며, 같은 연구를 제안할 때 자료/encoder 정보·K와 임계값·참여/갱신·총비용의 차이를 명시한다.

## 팀원이 먼저 확인할 자료

| 목적 | 자료 |
|---|---|
| 주요 데이터·거리·집계 경로 | [호출 경로](../evidence/0085-emd-cfl-code/call-paths.json) |
| 함수별 확인 위치 | [함수 지도](../evidence/0085-emd-cfl-code/function-map.json) |
| 논문과 구현 차이·조건부 위험 | [정적 관찰](../evidence/0085-emd-cfl-code/static-observations.json) |
| 판본과 저장 코드 대응 | [Git 내용 대조](../evidence/0085-emd-cfl-code/git-content-correspondence.json) |
| 당시 연구 후보 | [원76–79 판단](0076-0079-learning-decisions.md) |

공식 고정 판본: [EMD-CFL commit](https://github.com/dkaizhang/emdcfl/tree/f48a2cfe53079cc6bc1d89f4771cb7a5a62804c5). 새로 실행하기 전 누락된 설정·모델·자료와 사용 조건을 확인해야 한다.
