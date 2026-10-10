# Task2Vec의 과제 표현과 같은 예측 출력을 공유하는 효과

원래 기록 **78**의 Task2Vec 검토를 보완하는 아카이브 **H080**이다. 원78의 날짜는 2026-09-26이며, 이 문서의 0080은 새 실험 번호가 아니다. [원78 판단 보존본](../evidence/0076-0079-learning-decisions/originals/SRC-0022034.md.txt), [앞선 회귀 전이 검토](0079-regression-transferability.md), [출처 목록](../sources/history-080.md), [근거 묶음](../evidence/0080-task2vec/README.md)을 함께 본다.

핵심 질문은 **비슷한 특징을 필요로 하는 과제끼리, 실제 target도 같은 예측 함수로 학습시켜도 되는가**다. Task2Vec은 과제별 출력층을 적합한 공통 probe의 Fisher 정보로 과제를 표현한다. 원78은 이 표현의 유용성을 부정하지 않고, 특징 재사용을 같은 scalar target의 공동학습으로 바로 해석하는 후보를 채택하지 않았다. 이 정리는 모델을 실행하거나 팀의 최종 예측기를 선정한 결과가 아니다.

검수 상태와 각 문장의 원문 위치는 [주장 지도](../verification/history-080-claims.json)와 [검수 보고서](../verification/history-080.md)에 기록한다. 아래 C 번호는 이 문서 안의 주장 식별자다.

## 확인 범위와 방법의 의미

<a id="c01"></a>**C01.** 이번 범위는 원78이 저장한 Task2Vec 관련 13개 고유 자료와 이미 보존된 원78 판단이다. 논문 본문 10쪽·보충자료 6쪽, README 96행·구현 353행·거리 코드 218행, JSON 3개 전필드, 공식 서지 HTML, TXT 2개와 원 PNG 2개를 확인했다. 문헌 독해·정적 코드 대조이며 새 학습·추론·성능 실험은 없다. 원78의 외부자료 전체 43개 그룹을 이번 묶음 하나로 완료 처리하지 않는다.

<a id="c02"></a>**C02.** 논문 §3.1의 공통 probe는 ImageNet 사전학습 특징을 사용하지만, 각 과제의 classifier를 다시 학습한다. 이후 특징 추출기 파라미터의 Fisher 정보를 구한다. “공통 probe” 또는 “고정 특징”을 과제별 적합이 전혀 없다는 뜻으로 사용하면 안 된다.

<a id="c03"></a>**C03.** 논문과 코드가 정의하는 Fisher의 label 기대값은 모델의 예측분포 `y ~ p_w(y|x)`에 대한 것이다. 실제 label은 먼저 과제별 classifier를 적합하는 데 쓰인다. 실제 정답 label의 gradient만 사용하는 양과 정의상 구별해야 한다.

<a id="c04"></a>**C04.** Task2Vec은 전체 Fisher 대신 대각 성분을 사용하고 같은 filter의 값을 평균해 고정 길이 표현을 만든다. 서로 다른 filter 사이 상관을 무시하는 근사다. label permutation에 불변이고 출력 class 수와 무관한 차원을 갖지만, 이것이 서로 다른 label 의미나 scalar target을 같은 출력으로 강제할 근거는 아니다.

<a id="c05"></a>**C05.** robust Fisher는 classifier 학습 뒤 숫자를 한 번 읽는 절차에 그치지 않는다. 가중치 주변 Gaussian 잡음의 precision과 prior를 변분 목적함수로 적합하는 경로다. 작은 과제에서는 prior 쪽으로 치우치는 trivial embedding을 정의하고, filter 단위 대각 근사를 유지한다.

<a id="c06"></a>**C06.** 표현의 norm은 과제의 난도뿐 아니라 표본 수에도 영향을 받는다. 보충 Figure 2에서 여러 과제의 norm은 표본 수에 따라 커지지만 Short sleeves 곡선은 대체로 감소한다. “표본이 많으면 모든 과제에서 norm이 단조 증가한다”거나 norm만으로 모든 난도를 비교할 수 있다고 확대하지 않는다.

<a id="c07"></a>**C07.** 논문의 대칭 거리는 두 Fisher 벡터를 성분별 합으로 나눈 뒤의 cosine distance다. 비대칭 선택 점수는 여기에 source와 trivial embedding 사이 거리의 보정항을 빼며, ResNet-34에 대해 α=0.15를 보고한다. 음수나 비대칭이 가능한 선택 점수와 수학적 metric을 구분한다. expert를 각각 적합하는 탐색에 대한 O(1) 설명은 모든 과제 쌍의 거리 계산이 상수 시간이 된다는 뜻이 아니다.

<a id="c08"></a>**C08.** MODEL2VEC은 `m_i = F_i + b_i`의 bias를 과제·모델 성능에서 학습한다. 보충자료는 다른 과제들의 test error로 만든 soft label을 사용하고, leave-one-out으로 남긴 과제에서 평가한다고 설명한다. query 과제의 정답 성능을 학습에 넣었다고 단정해서도 안 되고, 모델 성능 정보가 전혀 필요 없는 방법이라고 설명해서도 안 된다. TASK2VEC과 MODEL2VEC을 분리한다.

## 저자가 확인한 조건과 결과

<a id="c09"></a>**C09.** 전체 task collection은 iNaturalist 207개, CUB 25개, iMaterialist 228개, DeepFashion 1,000개로 총 1,460개다. 자연 이미지의 분류 과제와 같은 의류 입력에서 속성을 달리하는 과제를 포함한다. 1,460개 각각에 모든 expert를 적합한 완전한 직교 실험표를 제공했다는 뜻은 아니다.

<a id="c10"></a>**C10.** 논문의 약 1,300 GPU시간은 4,100개 classifier, 156개 feature extractor, 1,460개 embedding을 다룬 저자의 전체 작업 비용이다. Task2Vec 한 번의 비용, 모든 expert 조합의 비용, 이 아카이브나 TabICL·RCTL의 실행 비용으로 옮겨 적지 않는다.

<a id="c11"></a>**C11.** iNat+CUB 선택 평가는 과제 50개와 그에 대응하는 expert를 사용한다. 보충자료는 iNat 25개와 CUB 25개로 설명하고, 같은 평가 과제의 데이터에서 학습한 expert를 제외하는 leave-one-out 조건을 명시한다. 전체 collection, 50개 선택 평가, 표본 수가 많은 상위 10개 평가는 서로 다른 범위다.

<a id="c12"></a>**C12.** Mixed의 규모는 자료끼리 일치하지 않는다. 본문 §4의 실험 설명은 임의 과제 50개·curated expert 26개라고 적지만, 보충 §3은 과제 40개·expert 25개로 설명한다. 보충 Figure 3 오른쪽도 40행×25열이며 과제는 CUB 5·iNat 15·iMaterialist 15·DeepFashion 5개다. generic ImageNet expert의 포함 여부만으로 모든 차이가 해소됐다고 판단하지 않는다. 표 1이 어느 과제 목록과 정확히 대응하는지는 저장 자료로 확정하지 못했다.

<a id="c13"></a>**C13.** 보충 §4의 expert 훈련은 ImageNet ResNet-34의 head를 Adam으로 10 epochs 적합한 뒤 전체를 SGD로 60 epochs 조정한다. weight decay는 5e−4, 초기 learning rate는 0.001이며 40 epochs 뒤 10분의 1로 줄인다. expert 위 평가 classifier는 Adam 16 epochs·learning rate 1e−4·weight decay 5e−4다. 기본 실험의 epoch당 10,000개 복원추출과 class 균형 조건도 함께 보존한다.

<a id="c14"></a>**C14.** 같은 보충자료의 embedding 계산은 classifier를 Adam으로 2 epochs 적합한 다음 classifier와 log precision을 함께 최적화한다. 이 단계에서 classifier learning rate는 1e−4, log precision은 1e−2다. 전문가 모델을 만드는 훈련, 전문가 위 성능을 측정하는 classifier, embedding을 위한 classifier 적합을 같은 비용·설정으로 합치지 않는다.

<a id="c15"></a>**C15.** 본문 Table 1의 수치는 optimal 모델 대비 **상대 오차 증가율**이다. iNat+CUB에서 optimal error는 31.24이고 ImageNet +30.18%, 대칭 TASK2VEC +42.54%, 비대칭 +9.97%, MODEL2VEC +6.81%다. Mixed에서는 optimal 22.90에 각각 +75.73%, +40.30%, +29.23%, +27.81%다. 대칭 TASK2VEC이 iNat+CUB에서 ImageNet보다 나쁜 사례도 보존한다. 증가율을 감소율이나 percentage point 차이로 바꾸지 않는다.

<a id="c16"></a>**C16.** Table 2는 표본이 많은 상위 10개 과제와 전체 과제를 구분한다. 마지막 열의 optimal 대비 상대 증가율은 상위 10개 +0.00%, 전체 +9.97%이며, 열 제목은 인쇄상 `ResNet-13`이다. 본문의 ResNet-34 설명과 다르므로 제목을 조용히 고치지 않는다. +0.00%를 모든 과제의 무오차 예측이나 개별 과제별 완전 일치로 해석하지 않는다.

<a id="c17"></a>**C17.** 본문 Figure 4의 표본 효율 결과는 네 과제에서 선택 expert와 generic ImageNet의 고정·fine-tuning 조건을 비교한 것이다. 기준은 고정된 optimal expert이므로 음의 relative error는 이 기준보다 낮은 오차라는 뜻이다. 절대 오차가 음수이거나 1,460개 과제 전체에서 우수했다는 증거가 아니다.

<a id="c18"></a>**C18.** 보충 Taskonomy 실험은 11개 과제의 거리 행렬을 다루며, 약 5 GPU시간은 그 행렬에 관한 저자 보고다. 분류뿐 아니라 depth 같은 회귀와 segmentation도 포함하고, 공통 사전학습 backbone에 과제별 decoder를 적합한다. 이를 분류만의 연구라고 제외하거나, regression decoder를 학습하지 않는 방법으로 바꾸어 설명하지 않는다.

<a id="c19"></a>**C19.** 보충 Figure 3의 왼쪽 50×50·오른쪽 40×25 행렬에서 배경색은 비대칭 TASK2VEC 거리이고 셀 숫자는 classifier test error다. 빨간 숫자는 선택된 expert, 별도의 파란 숫자는 선택과 다른 최적 expert다. 3,500개 표시 정수와 90개 선택 위치를 보존했다. CUB Laniidae의 선택 28 대 최적 17, Mixed의 IMAT Printed 40 대 17처럼 선택이 손해인 사례도 있다. 같은 정수로 표시되지만 서로 다른 expert가 강조된 행이 있어, 반올림 전 값이나 정확한 표 1 평균을 이 그림만으로 복원하지 않는다.

<a id="c20"></a>**C20.** 본문 Figure 1의 task/domain t-SNE, Figure 2의 분류 체계 거리·norm/error, Figure 3의 expert별 분포와 보충 toy 과제 시각화는 표현의 성질을 설명한다. 그림의 원시 좌표·개별 seed·예측 배열은 확보하지 않았다. 본문 Figure 3 caption의 CUB 표기와 iNat도 포함한 축, Table 2 모델명 등 표시 차이는 남겨 두되 실행 실패로 판정하지 않는다.

## 고정된 구현을 재사용할 때의 조건

<a id="c21"></a>**C21.** 원78이 확보한 공식 코드는 commit `c5795e55ba773f9845498091a90eee2fcba5da31`이며 저장 metadata의 날짜는 2023-07-13이다. README와 Python 2개 파일의 Git blob을 확인했다. 저장 tree 응답의 최상위 sha는 commit ID여서, root entry들로 tree 객체를 재구성한 `696034e080ba45e2224ff4b05b389b18cc2bd803`을 commit의 tree와 대조했다. 논문 발표 시점의 실행환경을 이 사실로 복원한 것은 아니다.

<a id="c22"></a>**C22.** README와 `Task2Vec.__init__`의 기본 방법은 `montecarlo`다. README는 논문에 `variational`을 사용했다고 따로 설명한다. 따라서 현재 저장 코드의 기본 호출을 논문 결과의 동일 설정이라고 부르면 안 된다. README의 예시·다운로드·실행 명령은 읽었으며 실행하지 않았다.

<a id="c23"></a>**C23.** `embed`의 실제 순서는 feature cache → classifier 적합 → Fisher 계산 → embedding 추출이다. `skip_layers`는 중간 특징을 재사용하는 경로를 만들며, `max_samples`는 cache 쪽에 적용된다. 그 값 하나로 모든 후속 Fisher 계산의 실제 표본 수가 동일하게 제한된다고 일반화하지 않는다.

<a id="c24"></a>**C24.** `_fit_classifier`의 기본값은 Adam, 10 epochs, learning rate 0.0004, weight decay 0.0001이다. `model.fc`의 파라미터와 CrossEntropyLoss를 사용한다. 보충자료의 embedding용 2 epochs와 다르지만 저장된 configuration 본문이 없어 당시 각 실행에서 덮어쓴 실제 값을 확인하지 못했다. 기본값 차이는 곧 논문 실험 오류의 증거가 아니다.

<a id="c25"></a>**C25.** Monte Carlo 경로는 모델 출력에서 label을 뽑고 batch loss를 backward한 뒤 파라미터 gradient의 제곱을 누적·평균한다. 저장되는 것은 이 경로의 근사량이다. 코드를 읽었다는 이유로 개별 표본마다 만든 전체 gradient outer product 또는 정확한 Fisher 행렬을 계산했다고 표시하지 않는다.

<a id="c26"></a>**C26.** 변분 경로의 기본값은 1 epoch, β=1e−7이며 optimizer의 기본 learning rate는 1e−2, classifier group은 5e−4다. `variational.make_variational`, `get_variational_vars`, `get_compression_loss`를 호출한다. 보충자료의 classifier learning rate와 차이가 있고 helper 본문도 이 packet에 없다. 실제 precision 매개변수·상수·설정 override까지 동일하다고 검증한 상태가 아니다.

<a id="c27"></a>**C27.** loader는 class별 역빈도에 따른 weight와 기본 `num_samples=10000`, batch size 64, `drop_last=True`를 사용한다. multi-label dataset 표시가 있으면 거부한다. 초기화의 Bernoulli 옵션과 별개로 `_fit_classifier`는 CrossEntropyLoss를 고정 사용하므로, 이 저장 코드가 임의 다중 label·연속 target을 그대로 받는 완성된 범용 API라고 가정하지 않는다.

<a id="c28"></a>**C28.** `extract_embedding`은 classifier 모듈을 제외한다. 변분 경로에서는 `exp(-logvar0)`와 `exp(-loglambda2)`를 담고, Monte Carlo 경로에서는 gradient 제곱을 filter별 평균한 값과 scale 1을 담는다. 두 방법의 배열 이름이 같다고 추정량·정규화·prior의 의미까지 같게 취급하지 않는다.

<a id="c29"></a>**C29.** `task_similarity.cosine`은 두 hessian 벡터를 `h0+h1+1e-8`로 나눈 뒤 SciPy cosine distance를 호출한다. `normalized_cosine`은 variance와 scale을 사용하는 별도 경로다. 분모에 작은 수를 넣었다는 것만으로 모든 영벡터·결측치·형상 조합에 유효한 거리가 보장된다고 판단하지 않는다.

<a id="c30"></a>**C30.** 같은 파일의 `asymmetric_kl`은 두 Gaussian variance의 KL 방향을 계산한다. 논문의 cosine에서 trivial embedding 보정항을 빼는 비대칭 점수와 식이 다르다. 확인한 두 Python 파일에는 MODEL2VEC bias를 학습하는 구현도 없다. 함수 이름의 “asymmetric”만 보고 논문의 비대칭 expert 선택 전체를 제공한다고 연결하지 않는다.

<a id="c31"></a>**C31.** `pdist`는 과제 쌍을 순회하고 대칭값을 복사하거나 비대칭 KL에 대해 모든 순서쌍을 계산한다. `cdist`도 from/to의 모든 조합을 순회한다. `None` embedding이면 해당 칸의 초기 0을 남기므로, 이 0을 관측된 완전 유사성으로 사용하면 안 된다. 전체 거리 계산·결측 처리와 논문 expert 탐색 비용의 설명을 구분한다.

<a id="c32"></a>**C32.** 코드 재사용 전에는 별도로 호출 경로와 설정을 확인해야 한다. 예를 들어 `max_samples`를 지정한 cache의 batch 수는 `min(floor(max_samples/batch_size)-1, loader 길이)`로 정해지고, README의 일부 예시는 저장 모듈의 class API와 다르게 적혀 있다. batch norm을 고정한다는 주석 뒤의 `model.train()`도 probe 구현을 함께 봐야 해석할 수 있다. 이 관찰들을 실행한 오류나 원78의 과학적 기각 이유로 소급하지 않는다.

## 표기 차이, 당시 판단과 재검토 조건

<a id="c33"></a>**C33.** 보충자료에는 설명과 표시식의 차이도 있다. MODEL2VEC의 cross-entropy라고 설명한 식에 `−log`가 보이지 않지만 본문 p6의 목적식에는 `−log`가 있다. 두 층 예시의 혼합 미분 block과 precision/Hessian 전개에도 앞선 식과 대조가 필요한 계수 표기가 있다. 각 식의 위치와 인쇄 내용을 보존한다. 이것만으로 저장 코드나 저자의 실행에서 잘못된 loss를 사용했다고 결론 내리지 않는다.

<a id="c34"></a>**C34.** 공식 CVF 저장 HTML과 논문 인쇄 쪽수는 ICCV 2019, **6430–6439**다. 원78의 `6429–6438`은 서지 범위의 정정 대상으로 표시하며 보존 원문은 바꾸지 않는다. 원78이 Task2Vec의 과제별 head 적합·label 불변성·회귀 적용을 구분한 판단과 이 서지 차이는 별개다.

<a id="c35"></a>**C35.** 원78의 기호 예시는 두 cell이 `−1≤x≤1`의 같은 대칭 입력분포를 공유하고 비중도 같으며, `c>1`에서 실제 관계가 `c+x`와 `c−x`이고 cell을 구분할 정보가 없다는 조건이다. 출력 변환을 허용하면 완전히 전이할 수 있어도, 같은 scalar 함수로 pooling하면 제곱오차의 최적 공통 함수는 c이고 평균 손해가 `E[x²]`로 남는다. 이는 새 트래픽 실험이나 Task2Vec 논문의 실험값이 아니다. cell ID 등 구분 정보가 있으면 전제가 달라진다.

<a id="c36"></a>**C36.** 같은 원78은 공통 특징과 Gaussian working likelihood 아래 feature Fisher가 head 기울기의 제곱 `a²`에 의존하는 예시도 든다. 부호가 반대인 출력 관계가 같은 특징 중요도를 가질 수 있다는 조건부 설명이다. 공식 Task2Vec의 모든 estimator가 모든 자료에서 정확히 같은 embedding을 반환한다고 주장한 것이 아니다.

<a id="c37"></a>**C37.** 당시 채택하지 않은 것은 공통 probe의 embedding이나 회귀 전이 점수를 그대로 cell 병합 점수로 바꾸는 후보였다. 모든 task representation, transfer learning, multi-head RCTL을 불가능하다고 기각한 기록이 아니다. “어떤 파라미터·출력을 공유하고 어느 head를 다시 맞추는가”를 빠뜨린 채 같은 후보를 이름만 바꾸어 되풀이하지 않도록 연결한다.

<a id="c38"></a>**C38.** 재검토하려면 실제 target 좌표와 허용할 추가 적합을 먼저 명시하고, task별 head를 허용할 때는 같은 구조의 global multi-head 모델과 비교할 이유를 세워야 한다. MODEL2VEC 변형의 bias를 최종 RCTL 성능으로 맞추면 현재의 clustering 독립성 조건과 충돌한다는 원78의 판단도 보존한다. 이 문서는 새 실험을 승인하거나 그 설계를 실행한 기록이 아니다.

<a id="c39"></a>**C39.** TXT 본문은 PDF page 경계 표지를 제거한 뒤 main의 layout 추출 10쪽·supplement의 plain 추출 6쪽과 정확히 대응했다. supp2의 layout 추출에서 빠진 작은 행렬은 plain 추출과 600dpi 확대본으로 확인했다. 원 PNG 2개도 직접 확인했다. 이 대응본·이미지·공식 서지 HTML을 별도의 독립 논문이나 재현 횟수로 더하지 않는다.

<a id="c40"></a>**C40.** 재사용 자료에는 공식 논문·보충자료 링크, 고정 commit과 blob, 표시 결과 행렬, 코드 범위·원본 hash를 연결한다. helper·configuration·실행환경 전체, 실제 seed와 per-run 결과 배열, Mixed 수량 차이의 원인, 모든 외부 원자료의 장기 팀 공유는 미완료다. 원78의 NTKMTL 및 남은 외부자료와 이후 과거 기록도 계속 검토해야 한다. 현재 범위의 독해 완료를 전체 아카이브 완료로 표시하지 않는다.

## 재사용 전에 확인할 값

| 항목 | 이 묶음에서 확인한 상태 |
|---|---|
| 질문·방법 | task representation과 feature extractor 선택, 공동 scalar 예측과의 차이 |
| 트래픽 cell·시간 분할·UPC K·최종 RCTL | 이 문헌 검토의 새 실험에는 해당 없음 |
| 저자 데이터·비교군·손해 | 본문/보충의 범위를 분리해 C09–C20 및 표시 결과에 보존 |
| seed·실제 실행 configuration·원시 예측 | 이 packet에서 미확보; 코드 기본값으로 대체하지 않음 |
| 고정 코드 | README·Python 2개와 metadata 확인, import·실행 및 재현 미실시 |
| 후속 질문 | 허용된 head/target 변환, global 대안, 원78의 남은 자료, 자료별 수량·표기 차이 |

새 실험을 기록할 때는 [기존 실험 이슈 양식](../../../.github/ISSUE_TEMPLATE/03_experiment.yml)에 원78/H080, 기존 조건과 달라진 질문, 재사용할 자료를 연결한다. [과거 시도 색인](../prior-attempts.md)과 [가까운 pooling 문헌 비교](../references/closest-pooling-methods.md)에서 관련 기록을 찾을 수 있다.
