# DGCformer의 channel 군집과 원81 판단 검토

[원81 방향 검토](0090-input-partition-decision.md) · [출처와 읽은 범위](../sources/history-091.md) · [검수](../verification/history-091.md)

DGCformer는 관련 channel을 묶고 같은 그룹 안에서 정보를 교환하도록 예측기를 구성한 선행연구다. 따라서 원81에서 검토한 공동 입력·다중 출력 후보는 기존 분할 방식과 무엇이 달라지는지 설명해야 한다. 다만 논문이 clustering과 forecasting을 구분해 설명한다는 사실만으로 군집 선택이 예측 성능과 완전히 독립적이라고 단정할 수는 없다. 손실의 결합, K 선택 절차, 성능표의 집계에 남은 확인사항을 함께 보존한다.

## 판본과 과거 기록의 관계

<a id="c01"></a>**C01.** 검토 판본은 Qinshuo Liu, Yanwen Fang, Pengtao Jiang, Guodong Li의 *DGCformer: Deep Graph Clustering Transformer for Multivariate Time Series Forecasting*, arXiv 2405.08440v1, 2024년 5월 14일이다. 저장된 논문 HTML·TXT와 서지 HTML·TXT 네 그룹은 각각 같은 바이트의 스냅샷 사본을 가진다. 이번에 보충한 같은 v1의 PDF 14쪽은 원81 당시 보관한 파일로 소급하지 않는다.

<a id="c02"></a>**C02.** 원81은 지정된 방법 절과 부록·결론을 읽었다고 보고했다. 이번 정리는 저장된 네 그룹의 연구 본문·수식·표·참고문헌·부록과 대응하는 PDF 그림을 확인한 후속 검토다. 표에 인쇄된 수치의 재계산은 수행했지만 모델 학습·추론·논문 실험 재현은 수행하지 않았다. 네 파일 형식과 두 시점의 검토를 독립 연구 네 건으로 세지 않는다.

## 군집이 예측에 전달되는 과정

<a id="c03"></a>**C03.** 논문의 질문은 모든 channel을 함께 쓰는 channel-dependent 방식과 channel별로 처리하는 channel-independent 방식의 절충이다. 관련 channel끼리는 정보를 교환하고 다른 그룹 사이의 attention은 제한한다. Figure 1의 Informer 비교도 CI가 모든 데이터셋·지표에서 낫다는 결과는 아니다. 여기서 CI라는 명칭만으로 channel마다 별도 RCTL 가중치를 학습한다고 해석하지 않는다.

<a id="c04"></a>**C04.** RFL은 GRU와 선형 변환으로 시계열의 잠재 표현을 만들고, decoder로 원 시계열을 복원하는 모듈이다. 부록 C는 잠재 차원 32를 선형 투영으로 10까지 줄여 군집과 목표 분포에 사용한다고 적는다. 이는 이미 계산된 단순 상관계수만으로 소속을 정하는 절차와 다르다.

<a id="c05"></a>**C05.** 잠재 표현과 중심 사이의 Student-t 형태 유사도에서 소속 분포 q를 계산하며, 자유도 t는 선택하는 값으로 통상 1을 쓴다고 설명한다. 목표 분포 P는 q를 제곱하고 cluster별 빈도 항으로 나눈 뒤 정규화한다. P는 다음 GCL의 분포를 지도하는 목표로 사용된다. 논문에 적힌 이 목표 분포를 실제 미래 target이나 TabICL 예측값으로 바꾸어 설명하지 않는다.

<a id="c06"></a>**C06.** GCL의 초기 graph는 시계열의 상관행렬과 사용자가 정하는 threshold로 만든다. 논문은 이를 directed graph라고 부르지만, 실제 threshold 값·선정 절차를 제시하지 않는다. 따라서 동일한 graph를 재생성할 설정이 모두 확보됐다고 볼 수 없다.

<a id="c07"></a>**C07.** GCN은 self-loop를 더한 adjacency의 정규화와 학습 가중치를 사용하고, 중간 표현을 RFL의 잠재 표현과 결합한다. 이 결합의 ε는 0.5로 기재돼 있다. GCN의 최종 분포를 P와 비교하는 KL 손실과, decoder의 복원 손실은 역할이 다르다.

<a id="c08"></a>**C08.** §3.2가 실제 그룹 결정으로 설명하는 것은 RFL의 잠재 표현 H²에 대한 K-means다. 그 결과로 예측 모듈의 mask를 만든다. 이를 GCN 최종 소속 분포의 argmax로 정하는 구현과 같다고 바꾸지 않는다. Figure 4에서도 잠재 표현·K-means·mask의 연결을 확인할 수 있다.

<a id="c09"></a>**C09.** 예측 모듈은 정규화·patching 후 시간 방향 attention과 channel 방향 masked attention을 사용하고 선형층으로 N개 channel의 S-step 출력을 만든다. 같은 군집의 channel 사이에만 교환을 허용하는 mask와, 군집마다 완전한 RCTL 모델을 별도로 적합하는 것은 다른 설계다. mask의 존재만으로 실제 연산이나 메모리 사용이 그 비율만큼 줄었다고 계산하지 않는다.

## 손실과 K 선택에서 남는 해석의 한계

<a id="c10"></a>**C10.** §3.4의 Eq.10은 전체 손실을 `0.1 × L_DS + 1 × L_REC + L_PRED`로 적는다. 반면 결론은 adaptive clustering을 포함하는 통합 end-to-end 모델을 미래 과제로 둔다. 두 서술을 함께 보존해야 한다. 모듈을 나눠 설명한 것을 근거로 모든 최적화·모델 선택이 예측 목표에서 독립적이라고 단정하거나, 반대로 K-means까지 예측 gradient가 전달되는 공동 학습을 구현했다고 단정하지 않는다.

<a id="c11"></a>**C11.** §4.4는 batch마다 최적 cluster 수를 동적으로 고르는 adaptive 방식을 실험에 채택했다고 적고, 부록 C는 최적 cluster 수를 grid search로 결정했다고 적는다. Figure 5의 최적선만으로 선택 지표·검증 분할·batch별 갱신 규칙을 복원할 수 없다. 따라서 원81이 남긴 “K 선택이 예측 성능과 완전히 독립적인지는 미확인”이라는 제한은 유지한다. 이 공백 자체가 test 누수의 증거는 아니다.

<a id="c12"></a>**C12.** Eq.6과 Eq.11은 i에 대한 합 안에 전체 행렬의 Frobenius norm을 적는다. Eq.8은 쌍별 mask 조건으로 벡터 성분 M_i·M_j의 값을 정해 적용 범위가 모호하고, Eq.9 마지막 MLP의 입력 표기도 직전 중간 표현과 다르다. 저장 HTML의 수식과 같은 v1 PDF에서 확인되는 표기이며, 본 정리에서 의도한 구현을 추정해 식을 고치지 않는다. 구현과 원 결과의 영향은 미확인이다.

## 자료와 평가 조건

<a id="c13"></a>**C13.** 주 실험의 여덟 데이터셋은 ETTh1·ETTh2·ETTm1·ETTm2·Exchange(EXC)·Weather(WTH)·Illness(ILI)·Electricity(ECL)다. Table 1과 Table 5는 이 목록을 사용한다. ETT 네 판본을 한 데이터셋으로 합쳐 비교 항목 수를 다시 계산하지 않는다.

<a id="c14"></a>**C14.** 원81의 DGCformer 단락에 적힌 “도로 교통 등을 포함한 여덟 자료”는 이 v1의 실험 목록과 맞지 않는다. 해당 목록에는 Traffic 데이터셋이 없다. 원81의 원문은 보존하고 이 부분을 후속 정정으로 연결한다. DGCformer의 표를 도로 교통 또는 모바일 통신 트래픽에서 검증한 결과로 인용하지 않는다.

<a id="c15"></a>**C15.** 본문 주 실험은 look-back 96, ILI는 104를 사용하고, 예측 길이는 일반적으로 96·192·336·720, ILI는 24·36·48·60이다. train의 평균과 표준편차를 이용해 train·validation·test를 zero-mean 정규화한다고 명시한다. 이 표의 MSE·MAE를 Milan cell 평균으로 나눈 과거 TabICL 오차와 같은 척도로 합치지 않는다.

<a id="c16"></a>**C16.** Table 5는 ETT 각 7변수, EXC 8변수, WTH 21변수, ILI 7변수, ECL 321변수를 적고 분할 크기·주기를 제시한다. 예를 들어 ETTh의 분할 크기는 8545/2881/2881, ETTm은 34465/11521/11521이다. 표의 분할 수와 부록 본문의 전체 시계열 길이를 자동으로 같은 분모로 해석하지 않는다. 나머지 값은 보존한 [표 구조](../evidence/0091-dgcformer/tables-2-5.json)에서 확인할 수 있다.

<a id="c17"></a>**C17.** 부록 C의 기본 설정은 encoder 3개, attention head 16개, model dimension 128, dropout 0.2다. 일반 데이터의 patch 길이·stride는 16·8이고 ILI는 24·2다. RFL의 차원 32→10과 함께 PyTorch, 단일 NVIDIA V100 32GB 환경을 기재한다. 이 설정은 원81이 제안한 RCTL 다중 출력 모델의 실행 설정이 아니다.

<a id="c18"></a>**C18.** 읽은 v1에는 정확한 seed, learning rate, epoch 수, 반복 실험 분산, 전체 학습 시간·비용이 확인되지 않는다. grid search의 후보·선택 분할과 원시 예측도 확보하지 않았다. 따라서 표의 순위를 독립 재현했다고 표현하거나 오류 차이의 통계적 유의성을 새로 주장할 수 없다.

## 표시된 결과와 집계의 대조

<a id="c19"></a>**C19.** Table 1은 여덟 데이터셋 × 네 예측 길이 × 두 지표로 64개 비교 항목을 만들고 DGCformer·PatchTST·Crossformer·DLinear·Autoformer·Informer·MTGNN을 비교한다. [표시값](../evidence/0091-dgcformer/displayed-table-1.json)과 [재계산](../evidence/0091-dgcformer/table-1-audit.json)은 인쇄된 소수를 Decimal로 비교한 결과다. 반올림 전 수치나 새로운 모델 실행 결과가 아니다.

<a id="c20"></a>**C20.** 본문과 Table 1은 DGCformer가 64개 항목 중 57개에서 1위라고 적는다. 표시값을 그대로 비교하면 동률을 포함한 최저값은 54개이고, 단독 최저값은 48개다. 원문 57을 몰래 54로 교체하지 않고 두 집계의 기준과 차이를 함께 남긴다.

<a id="c21"></a>**C21.** 저장 HTML의 굵은 수를 모델별로 세면 `57/4/1/4/0/0/0`으로 원문의 합계 행과 같다. 하지만 표시값의 최저 수는 동률 포함 `54/9/1/6/0/0/0`이다. DGCformer의 ETTm1·720 MAE 0.439, WTH·720 MSE 0.350, ECL·336 MSE 0.210은 굵게 표시됐지만 각각 PatchTST 0.438, DLinear 0.345, DLinear 0.209보다 크다. 비최저인데 굵은 값 3개와 최저인데 굵지 않은 값 7개를 남겼다. 이는 표시와 집계의 관찰이며 저자의 계산 과정이나 의도를 확정하는 주장은 아니다.

<a id="c22"></a>**C22.** DGCformer가 표시값의 최저에 못 미치는 항목은 10개다. 예를 들어 ECL·720에서 DGCformer의 MSE/MAE는 0.259/0.344이고 DLinear는 0.245/0.333이다. 논문이 많은 항목에서 좋은 값을 보고한 것과 특정 데이터·길이·지표에서 다른 모델이 더 좋은 것은 양립한다. [전체 예외](../evidence/0091-dgcformer/table-1-audit.json)를 평균 우세로 지우지 않는다.

<a id="c23"></a>**C23.** Table 2에서 GCL을 넣은 모델은 제거 모델보다 MSE가 낮지만 MAE는 336·720에서 각각 0.454 대 0.452, 0.468 대 0.466으로 높다. Table 3의 RFL 비교도 MAE 192는 0.432로 같고 336은 0.454 대 0.450으로 높다. Table 4의 DTW 비교 여덟 값은 DGCformer가 모두 낮다. 또한 ablation의 첫 MSE 0.380과 Table 1의 0.379를 같은 실행의 동일 값으로 취급하지 않는다.

<a id="c24"></a>**C24.** Table 5는 일반 데이터셋의 마지막 예측 길이를 512로 적지만, 본문과 Table 1은 720으로 적는다. Table 2–4의 caption은 96–720을 look-back 길이라고 부른다. 따라서 각 열의 길이 조건을 임의로 통일해 ablation과 주 실험을 동일 실행으로 연결하지 않는다. 이 차이는 저장 HTML과 v1 PDF에도 남아 있다.

## 그림과 구현을 재사용할 때의 범위

<a id="c25"></a>**C25.** Figure 1–7의 HTML media 참조 14개는 같은 v1 PDF의 그림과 번호·설명으로 대응했다. Figure 3의 상관 열지도와 Figure 6의 시계열 곡선은 그룹 구성의 동기를 보여 준다. 그림에서 인과관계, 정확한 원시 수치, 오류 차이의 유의성을 읽어내지는 않는다. HTML 원격 이미지 파일과 PDF 그림의 바이트 동일성을 검사한 것은 아니다.

<a id="c26"></a>**C26.** Figure 7의 caption은 Electricity의 과거 96-step으로 다음 720-step을 예측한 Autoformer·DLinear·PatchTST·DGCformer의 사례라고 설명한다. 네 패널에서 약 550 부근의 큰 spike를 놓치는 모습이 보인다. 다만 그림 축에서 history와 forecast의 경계가 별도로 명시돼 있지 않으며, 이 한 그림을 숫자 오차나 전체 모델 순위로 환산하지 않는다.

<a id="c27"></a>**C27.** 이 논문의 Transformer channel mask와 원81의 cluster별 RCTL 다중 출력은 최종 함수·정보 교환·반복 계산이 다르다. 논문의 성능이나 차원 축소 설명은 RCTL의 실제 속도, 모바일 통신 트래픽의 예측 성능, UPC 소속 수정 효과를 검증한 근거가 아니다. 원81의 기호 MAC 비교와도 측정 대상을 구분해야 한다.

<a id="c28"></a>**C28.** 원81이 “분할 뒤 예측하는 구조 자체로는 차별성이 부족하다”고 보고 입력 기반 분할을 비교 대상으로 둔 방향은 이 선행 구조와 연결된다. 다만 DGCformer를 완전히 예측 독립적인 군집 선택 절차로 취급하는 것은 Eq.10과 K 선택 공백을 넘어선다. 분리된 모듈의 존재와 선택·학습의 독립성을 구분하는 것이 후속 보완이다.

<a id="c29"></a>**C29.** 저장 서지의 코드 공개 예정 문구는 논문 작성 당시의 약속이다. 원81은 당시 공식 실행 코드를 찾지 못했다고 적었다. Appendix B에는 baseline 저장소 링크 여섯 개가 있지만, 이는 DGCformer의 공식 구현을 확보한 것과 다르다. 이번에는 현재 코드 공개 여부를 새로 조사하지 않았으므로 현재 존재하지 않는다고 주장하지 않는다.

<a id="c30"></a>**C30.** 같은 방향을 재검토할 때는 K 선택에 사용한 구간·지표, clustering과 forecasting 손실이 갱신하는 parameter, 예측 시점에 이용 가능한 정보, 고정 입력 분할·단일 global 모델 등의 비교군, 탐색부터 포함한 전체 비용을 먼저 구체화해야 한다. 기존 구조의 이름을 바꾸는 대신 어떤 입력 분할의 실제 손해를 새 결정이 줄이는지 확인해야 한다. 이는 후속 설계 조건이며 이번 정리에서 새 실험을 실행했다는 뜻이 아니다.

## 근거와 남은 범위

| 자료 | 접근과 역할 |
|---|---|
| 논문 v1 | [공식 HTML](https://arxiv.org/html/2405.08440v1), [공식 PDF](https://arxiv.org/pdf/2405.08440v1), [서지](https://arxiv.org/abs/2405.08440v1) |
| 저장본 판본과 사본 | [출처](../sources/history-091.md), [목록](../catalog/history-091-sources.jsonl), [명세](../evidence/0091-dgcformer/manifest.json) |
| 수치와 그림 검수 | [표시값 재계산](../evidence/0091-dgcformer/table-1-audit.json), [표 2–5](../evidence/0091-dgcformer/tables-2-5.json), [그림 대조](../evidence/0091-dgcformer/figure-review.json) |
| 원81 당시 판단 | [보존 보고서](../evidence/0090-input-partition/originals/SRC-0022042.md.txt), [H090 정리](0090-input-partition-decision.md) |

원81의 나머지 문헌·코드·검색 자료와 이후 기록은 계속 정리한다. 논문의 원시 실행·코드·일부 선택 조건이 미확인인 것과 저장 문서의 내용 검토를 끝낸 것은 다른 상태다. 주장별 위치와 작성 후 대조 결과는 검수 문서에서 확인한다.
