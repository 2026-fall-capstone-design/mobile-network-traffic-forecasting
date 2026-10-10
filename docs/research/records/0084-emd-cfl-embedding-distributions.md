# 원79 EMD-CFL: embedding 분포 군집의 근거와 적용 조건

[출처](../sources/history-084.md) · [검수](../verification/history-084.md) · [표·절차 근거](../evidence/0084-emd-cfl/README.md) · [당시 판단](0076-0079-learning-decisions.md)

local 학습 뒤 embedding 분포로 한 번 군집을 만드는 선행연구다. 군집 회복과 최종 학습 성능, 이론의 가정과 인쇄 표기의 공백, 초기 비용과 전체 비용을 구분해 같은 연구의 반복을 줄인다. H084는 정리용 ID이며 새 실험 번호가 아니다.

## 범위와 당시 기록

<a id="c01"></a>**C01.** H084는 원래 기록79의 EMD-CFL HTML·파생 TXT 2그룹과 기존 findings·plan을 연결한 검수 ID다. HTML 전체 본문·수식·표·참고문헌·부록을 읽고 TXT 대응 및 같은 판본의 보충 PDF24쪽을 확인했다. 신규 독립 본문은 HTML1개이며 TXT·사본4경로·보충 PDF·그림을 중복 가산하지 않는다. 새 모델 실험은 없다.

<a id="c02"></a>**C02.** 논문은 Dekai Zhang·Matthew Williams·Francesca Toni의 Clustered Federated Learning via Embedding Distributions, arXiv:2506.07769v1(2025-06-09)이다. 보충 PDF 표지는 Preprint, Under review로 표시한다. 이 검수로 최신 판본이나 학회 채택 여부까지 확정하지 않는다.

<a id="c03"></a>**C03.** 원79는 HTML §2–4와 비용절·지정 코드를 읽었으나 부록 전체를 검증하지 않았고, PDF406 및 다른 주소의16,010,450bytes가 당시15MB수집상한을 넘었다고 기록했다. 이번 공식 v1 PDF의 성공 취득과 부록 검토를 과거 작업의 완료로 소급하지 않는다. 당시 새 실험0·비용 원장 변경0이라는 범위도 유지한다.

## 방법과 공유되는 정보

<a id="c04"></a>**C04.** EMD-CFL은 초기 local 학습을 거친 encoder로 client 자료의 embedding 분포를 만들고, 쌍별 EMD를 한 번 계산해 군집별 학습을 이어간다. 고정 FM만으로 학습 전에 군집을 만드는 FMCL과 정보·비용이 다르다. one-shot은 쌍별 군집 계산을 가리키며 전체 학습이나 통신이 한 번이라는 뜻이 아니다.

<a id="c05"></a>**C05.** client 쌍은 두 encoder를 교환하고 공통 random projection R을 합의한 뒤 server에 projection한 embedding들과 자기 train–validation 기준 거리 τ를 보낸다. 상대 거리에서 τ를 뺀 보정값을 양방향으로 비교한다. 논문 의사코드의 표본·projection 표기와 실제 구현의 own train/other validation·호출별 projection 조건은 후속 코드 검수에서 대조해야 한다.

<a id="c06"></a>**C06.** 두 방향 모두 보정 거리가 ε보다 작을 때 대칭 adjacency를 만들고, 동일한 이웃집합을 같은 모델 index로 연결해 자료량 가중 FedAvg를 한다. 원79는 서로 다른 이웃집합이 겹칠 수 있다고 기록했다. 이를 UPC의 일반적인 서로소 cell partition과 바로 동일시하지 않으며, 구현 전체를 이번 논문 독해로 재검증했다고 쓰지 않는다.

<a id="c07"></a>**C07.** Algorithm1 line10에는 c에 대한 loop만 보이는데 뒤에서 c′를 사용한다. line16의 역방향 W[c′][c]에는 Z_c′|c와 Z_c′|c′가 들어간다. 이 표기는 HTML 수식과 PDF5쪽에서 모두 확인했다. 어떤 encoder/표본 쌍을 비교하는지 실제 코드와 대조할 항목이며, 실행 코드의 오류나 성능 실패를 확정한 결과는 아니다.

## 이론식의 조건과 확인할 표기

<a id="c08"></a>**C08.** §2.2는 이진 분류, 공통 입력의 label 함수 ψ, encoder g와 head h, embedding에서 L-Lipschitz인 head를 가정한다. 분포 간 head 불일치 bound에는 2L·W1 항이 있고, mixture risk bound에는 이에 더해 두 도메인의 이상적 공동 오차 λ가 있다. EMD가 작다는 사실만으로 label 관계·최종 test 오차·RCTL 출력 공유의 이득이 같다고 결론 내리지 않는다.

<a id="c09"></a>**C09.** Theorem2.4는 인쇄상 scalar loss의 M-Lipschitz 조건을 적고 expected loss의 gradient 차이 bound를 제시한다. embedding z에 대한 loss 조건과 parameter gradient에 필요한 조건을 동일한 것으로 단정할 수 없어 원출전·가정을 추가 확인할 항목으로 남긴다. 이번 작업은 해당 정리의 독립 증명·반증을 수행한 것이 아니다.

<a id="c10"></a>**C10.** §2.3과 AppendixA.1의 CorollaryA.3 증명은 parameter update에 loss 기대값을 쓰며 gradient 기호를 표시하지 않는다. Cor2.5/A.3의 계수는 M/κ로 인쇄돼 있다. 같은 초기 모델이라는 설명은 있지만, 서로 달라진 현재 parameter·여러 local step·유한 batch 잡음까지 포함한 일반 보장으로 이 식을 가져오지 않는다. HTML 변환만의 문제로 지우지 않고 후속 이론 검토 항목으로 둔다.

<a id="c11"></a>**C11.** Eq1의 분포 아래첨자는 client 인자가 없는 π*이고 Eq2의 왼쪽 합은 k=c부터 C로 표시된다. AppendixA.2는 ε_JL을 제시하면서 dimension/probability 식에 λ_JL을 사용한다. 이 표기들은 HTML·PDF에서 함께 확인했으며 임의 교정한 식을 원문인 것처럼 게시하지 않는다.

## privacy·비용·데이터 조건

<a id="c12"></a>**C12.** 원자료를 중앙화하지 않고 R을 server에 공개하지 않는 절차와 trusted central server 가정을 함께 남긴다. 논문의 privacy 설명을 정형 DP 보장이나 공격 내성 실험으로 확대하지 않는다. DP는 추가할 수 있는 수단으로 언급되고, 이번 논문 결과에 실제 적용됐다는 확인은 없다.

<a id="c13"></a>**C13.** 논문은 EMD 군집 계산을 O(C²N³log N), encoder 교환 통신을 O(C²|ω|)로 설명하며 표본은10%와512 중 작은 수로 제한한다. 학습 epoch 수 T와 무관한 것은 한 번의 군집 계산 비용이다. 수십 client의 cross-silo를 주 대상으로 하며 server에 표본을 두는 O(C|ω|) 대안은 실제 비교에서 가정하지 않은 후속 제안이다.

<a id="c14"></a>**C14.** Table4의 비교는 정답 군집을 미리 아는 Oracle7.47시간 대 EMD-CFL8.11시간이다. 표시값 차이는0.64시간, 약8.57%로 본문의 약9%와 대응한다. §3.1의 군집화하지 않는 경우라는 표현을 단일 global FedAvg와의 실측 비교로 해석하지 않는다. D.1은 T=10/E=10을 명시하지만 이 시간 측정의 데이터셋·GPU개수·반복 오차를 명시하지 않아 모든 설정의 고정9%비용으로 일반화하지 않는다.

<a id="c15"></a>**C15.** Rotated MNIST와 Rotated CIFAR10은0·90·180·270도 회전의 K=4, C=40이며 client를 군집에 균등 배치한다. 기존 train/test split을 유지하고 train의10%를 validation으로 쓴다. §4.1은 두 데이터셋 각각240000이미지라고 적는다. 이 수를 임의 교정하거나 통신 트래픽의 시간 분할·누수 통제로 바꾸지 않는다.

<a id="c16"></a>**C16.** PACS는9991이미지·7class·photo/art/cartoon/sketch 4domain이다. domain당 client에500개 이상을 배분해 총18client(3/4/4/7)를 만들고 train/validation/test는80/10/10으로 설명한다. domain cluster의 정답과 회귀 cell의 소속 정답은 다른 대상이다.

<a id="c17"></a>**C17.** Backdoor MNIST는30client·3group의 균일 green/label과 상관된 green강도/purple 자료이고, Backdoor CIFAR10은15client·3group의 class분할 및 작은 색상 patch 조건이다. target client의 clean accuracy와 변조된 feature에서의 accuracy를 비교하는 방어 평가다. 특정한 합성 설정의 격리 결과를 모든 공격이나 자연 시계열 변화에 대한 보장으로 확대하지 않는다.

## 설정과 평가

<a id="c18"></a>**C18.** 기본 ε=0.025, dim(R)=0.9·dim(Z)는90%차원을 유지하는10%축소다. 논문은 ε가 데이터셋·encoder·projection차원에 의존한다고 명시한다. 90%까지 축소해도 작동하는 일부 범위의 결과를 모든 ε와 모델에서 같은 threshold가 최적이라는 결론으로 바꾸지 않는다.

<a id="c19"></a>**C19.** 모든 모델은 T=10 global epoch, E=10 local epoch로 설명한다. MNIST는 convolution64/128·hidden128의 단순 CNN, CIFAR10/PACS는 ImageNet 초기화 ResNet18이다. SGD momentum0.9·weight decay10^-6, PyTorch2.5·POT0.9.5·NVIDIA L40S HPC를 보고한다. Table5의 모델별 learning rate와 native dimension은 전사표에 보존했다.

<a id="c20"></a>**C20.** §5.1은 ResNet18의 dim(Z)=768이라고 적지만 Table5의 CIFAR10·PACS ResNet18은512이고 ViTB16이768이다. HTML과 PDF에도 같은 차이가 있다. Table5 조건과 본문을 구분해 보존하고, 실제 코드 확인 전에 어느 하나를 구현의 확정값으로 선택하지 않는다.

<a id="c21"></a>**C21.** 16개 baseline에는 Oracle이 포함된다. D.3은8개 방법에 정답 K를 주고 CFL은 문헌의 partition 규칙을 사용하며 PACFL/FedClust threshold는 첫 epoch의 적절한 분할에 맞췄다고 설명한다. 이 조건을 모든 방법이 정보 없이 K를 알아낸 실험으로 쓰지 않는다. E.9의 별도 K=2 조건은 아래에서 구분한다.

<a id="c22"></a>**C22.** 평가는 client 평균·최악 accuracy와 최종 epoch의 hard-clustering ARI이며3회 평균을 보고한다. 표의 ± 값은 그대로 보존하되, 읽은 본문·부록에는 SD/SE/CI 중 무엇인지 명시되지 않았다. 정확한 seed ID도 미기재다. ARI의 dash는 보고하지 않은 값으로 남기고0으로 바꾸지 않는다.

## 결과·반례·부록

<a id="c23"></a>**C23.** Table1에서 EMD-CFL은 MNIST98.86/97.58, CIFAR10 94.84/93.03의 평균/최악 accuracy와 두 데이터셋 모두 ARI1을 보고한다. 그러나 MNIST PACFL의 최악 accuracy97.73은 EMD-CFL97.58보다 높다. FedClust는 MNIST ARI1이어도 평균96.93이다. 정답 군집 회복·학습 경로·최종 accuracy를 하나의 성과로 합치지 않는다.

<a id="c24"></a>**C24.** Table2와 전체17방법을 담은 Table7의 공통9행은 동일하다. EMD-CFL은 평균92.47±0.32/최악86.31±1.36/ARI1, Oracle은92.43±0.19/85.76±0.07/ARI1이다. FedClust는 ARI1이면서87.63/75.74를 보고한다. 비슷한 평균을 통계적 동등성 검정이나 정확히 같은 결과라고 표현하지 않는다.

<a id="c25"></a>**C25.** Table3와 전체17방법 Table8의 공통9행은 동일하다. EMD-CFL은 두 데이터셋 모두 ARI1과 높은 clean/backdoor accuracy를 보고하지만 MNIST clean 평균은 IFCA98.54가 EMD-CFL98.40보다 높다. FlexCFL은 MNIST ARI1이면서 clean39.51±51.12다. 최종 ARI만으로 초기 격리나 안정적 학습 성능을 확정하지 않고, 이 예외를 함께 보존한다.

<a id="c26"></a>**C26.** Table6은 매 epoch40client 중10·20·30client가 무작위로 참여하는 조건이다. 10client 조건에서는 Oracle과 EMD-CFL 모두 두 데이터셋 ARI0.93±0.03이고20/30에서는1.00±0.00이다. 성능이 Oracle에 가깝다는 설명을 모든 참여 조건의 완전 군집 회복으로 바꾸지 않으며0.93의 원인을 표만으로 확정하지 않는다.

<a id="c27"></a>**C27.** E.9의 Min은 회전{-3,-1,1,3}의 K=1, Two는{-3,3,177,183}의 K=2, Base는 회전 없는 자료다. K를 입력받는 baseline에는 FedAvg로의 축약을 피하려고 K=2를 주므로 main 비교와 조건이 다르다. EMD-CFL의6조건 ARI는1이지만 MNIST Two의 최악97.27은 Oracle97.73보다 낮고 CIFAR10 Base의 평균96.26도 Oracle96.34보다 낮다.

<a id="c28"></a>**C28.** Table9의5데이터셋×head/full model에서 군집 내 평균 pairwise L2거리는 전체 평균보다 모두 작다. 이는10개 집계 비교이며 모든 pair의 부등식, Theorem2.4의 가정, gradient·test 손실의 개선을 검증한 결과가 아니다.

<a id="c29"></a>**C29.** Figures8·9·10·12·13은 ε와 축소율별 ARI 곡선이며 일부 ε범위에서 plateau를 보이고 범위 가장자리에서는 낮아진다. Sinkhorn은 regularization0.1을 썼다고 설명한다. PACS의 본문은 최대50%축소 범위를 언급한다. 그림의 정성 경향을 모든 조합의 성공 또는 읽어내지 않은 raw 수치로 바꾸지 않는다.

<a id="c30"></a>**C30.** Figure1은 server/client 교환 구조, Figures3–7은 자료 예시, Figures2·11·14–17은 쌍별 거리의 정성 비교다. heatmap의 색상만으로 같은 metric·scale·상태의 수치라고 간주하지 않는다. §5.2는 art가 다른 domain을 가깝게 본다고 설명한 뒤 too distant라는 문구도 써 서술 방향의 차이가 남는다. 그림13(b)는 저장 HTML의 src가 비었지만 이번 같은 판본 PDF22쪽에서 확인했다.

<a id="c31"></a>**C31.** Tables1–11의121행·1192개 표시 숫자를 HTML에서 추출하고 같은 판본 PDF의 각 행 문자열과 대조했다. 이 수에는 Table2/7·3/8의 반복 행이 포함된다. 825개 math alttext는 TeX annotation과 모두 일치했고 TXT는 공백 정규화 후65919문자로 대응한다. 이는 표현·전사 검사이며1192개 독립 실험이나 결과 재현이 아니다.

## 후속 연구와 재사용의 조건

<a id="c32"></a>**C32.** 원79는 최종 RCTL encoder를 쓰면 당시 model-independent 조건을 충족하지 않는다고 판단했다. 고정 TabICL의 관측 입력 x와 조건부 평균 m(x)를 비교하는 후보는 EMD-CFL의 local 학습 encoder와 다른 정보를 쓴다. 같은 입력 분포·조건부 평균의 expected gradient 관계를 유한 batch SGD 분산이나 최종 RCTL test 보장으로 바꾸지 않는다.

<a id="c33"></a>**C33.** 현재는 저자 논문 결과와 당시 판단을 검수한 상태다. 저장된 공식 구현 묶음7그룹(README·Python4개·commit/tree JSON2개), 실제 seed별 출력·환경 재현·시간 측정 조건은 아직 후속 검수 대상이다. 참고문헌51개를 읽었다는 것은 서지 목록을 읽었다는 뜻이며51편 전문을 모두 검토한 것이 아니다. 학습·추론·과거 코드 실행은0이다.

<a id="c34"></a>**C34.** 원79 외부21그룹은 기존 명세·Crossref4, FMCL5, 이번 EMD 논문2그룹을 연결했고 EMD 코드7·Toso2·검색1의10그룹이 남는다. EMD나 분산 학습이라는 이름만 바꾸어 기존 proxy를 재제안하지 말고 encoder 정보·자료 이동·K/threshold 선택·총비용·최종 출력 공유의 차이를 명시해야 한다. 원80 계획과 이후 연구는 별도 검수하며 원문 속 과거 예산·Goal을 재개하지 않는다.

## 팀원이 먼저 확인할 자료

| 목적 | 자료 |
|---|---|
| 조건·수식과 구현 확인 항목 | [절차 해석](../evidence/0084-emd-cfl/algorithm-notes.json) |
| 저자 표시값과 반례 | [Table1–11](../evidence/0084-emd-cfl/tables.json) |
| 이번 보충 PDF의 출처 | [취득·검수 범위](../evidence/0084-emd-cfl/supplement-provenance.json) |
| 초기 고정 FM 방식과 비교 | [FMCL](0083-fmcl-client-clustering.md) |
| 당시 후보와 다음 계획 | [원76–79 판단](0076-0079-learning-decisions.md) |

공식 판본: [EMD-CFL HTML v1](https://arxiv.org/html/2506.07769v1) · [PDF v1](https://arxiv.org/pdf/2506.07769v1). 저장된 코드의 [공식 commit](https://github.com/dkaizhang/emdcfl/tree/f48a2cfe53079cc6bc1d89f4771cb7a5a62804c5)은 후속 정적 검수 범위다.
