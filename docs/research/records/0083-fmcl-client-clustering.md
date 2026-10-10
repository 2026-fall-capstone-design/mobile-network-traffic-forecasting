# 원79 FMCL: 사전 군집화의 조건과 보고 결과

[출처](../sources/history-083.md) · [검수](../verification/history-083.md) · [표·절차 근거](../evidence/0083-fmcl/README.md) · [당시 판단](0076-0079-learning-decisions.md)

H083은 원래 연구기록 **79**의 외부 근거를 보완하는 검수 ID다. 새 실험 번호가 아니다. 고정 FM으로 사전 군집을 만들고 별도 모델을 학습하는 선행 구조와, 이미지 분류에서 확인한 조건·수치·미기재 사항을 함께 남긴다.

## 검수 범위와 당시 판단

<a id="c01"></a>**C01.** 이번 검수는 원79 외부 소장21그룹 중 FMCL PDF·파생 TXT·원 PNG3의 5그룹을 다룬다. PDF16쪽을 본문과 이미지로 읽고 TXT16블록 대응 및 PNG3을 확인했다. 사본10경로와 기존 findings·plan을 새 독립 본문으로 중복 가산하지 않는다. 원79의 나머지 외부 자료와 새 실험은 이번 범위 밖이다.

<a id="c02"></a>**C02.** 검수 판본은 Mahad Ali·Laura J. Brattain의 FMCL: Class-Aware Client Clustering with Foundation Model Representations for Heterogeneous Federated Learning, arXiv:2604.27510v1이다. PDF 여백은 2026-04-30을 표시하고 실제 파일은 참고문헌을 포함해16쪽이다. 원79의 arXiv 메타14쪽과 실제16쪽을 구분하며 다른 판본 전체를 대조한 것으로 쓰지 않는다.

<a id="c03"></a>**C03.** 원79는 분산 보관·분산 학습이 사용자 확정 조건이 아니라고 기록했고 새 모델·pilot을 실행하지 않았다. 고정 FM으로 사전 군집을 만든 뒤 별도 모델을 학습하는 구조 자체는 FMCL에 있으므로 그 구조만으로 새로움을 주장하지 않았다. 이번 검수에서 발견한 표의 예외를 당시 판단 이유로 소급하지 않는다.

## 군집화에 쓰는 정보와 계산

<a id="c04"></a>**C04.** FMCL은 각 client의 고정 FM 표현으로 signature를 만들고, server에서 client 쌍의 거리를 구성해 계층 군집화한 뒤 군집별로 독립적인 FL 모델을 학습한다. 군집 결정을 학습 전에 한 번 수행한다는 설명과 후속 FL 학습·통신이 계속 필요하다는 사실은 함께 보존한다.

<a id="c05"></a>**C05.** client i의 각 관측 class c에 대해 평균 embedding μ_i,c와 class 비율 w_i,c=n_i,c/n_i를 보낸다. encoder φ는 고정되어 있고 signature는 {(μ_i,c,w_i,c)}다. 정답 class 정보가 필요하며 client의 실제 군집 정답을 요구하지 않는다는 설명을 무라벨 방식으로 바꾸지 않는다.

<a id="c06"></a>**C06.** 평균 prototype과 class 비율은 표본별 embedding 분포 전체가 아니다. 이는 분류 label 조건의 표현 요약으로, 연속 target의 조건부 평균이나 UPC cell들이 같은 scalar 출력을 공유해도 된다는 조건을 직접 증명하지 않는다. 이 적용 범위 구분은 수식과 원79의 문제 정의를 함께 읽은 해석이다.

<a id="c07"></a>**C07.** 공통 class에서 min(w_i,c,w_j,c)를 가중치로 cosine 거리를 평균하고 총 겹침 Ω_ij의 역수 계열 배율을 곱한다. Algorithm3의 cosine 분모에는 norm 곱+ε, 가중 평균 분모에는 가중치 합+ε가 있다. 기본 α=1, β=100, ε=10^-3이며 이 α는 label-skew Dirichlet α와 별개다.

<a id="c08"></a>**C08.** 공통 class가 없는 client 쌍은 처음에 무한대로 두고 유한한 비대각 거리의 95·99 percentile로 D_big=min(2P95,P99)를 만들어 대체한다. 대각 원소는0으로 정한다. 고정된 임의 상수로 대체한 것과 구분하며, D_big을 반드시 모든 유한 거리보다 큰 값이라고 설명하지 않는다.

<a id="c09"></a>**C09.** Algorithm3에서 유한 거리 집합이 비는 경우의 percentile 처리와, 뒤의 CV 계산에서 평균 거리가0인 경우의 처리가 명시돼 있지 않다. 이는 인쇄된 의사코드의 명세 공백이며 실행 코드의 오류나 논문 성능 실패를 확인한 결과가 아니다.

<a id="c10"></a>**C10.** Algorithm4는 single·complete·average linkage와 거리 threshold 또는 목표 K를 설명한다. 보고 실험은 average linkage다. 의사코드에서 가장 가까운 쌍을 찾은 뒤 종료 조건을 검사하는 순서와 마지막 한 군집의 처리는 실제 구현을 추가 확인할 항목으로 남긴다.

<a id="c11"></a>**C11.** CV는 교차검증이 아니라 거리 행렬 비대각 원소의 표준편차/평균이다. CV<0.35이면 K=1–3, 0.35≤CV<0.70이면 K=2–6, 그 외에는 K=3–10을 검사한다. 이 threshold들은 세 데이터셋에서 고정했다고 서술한다.

<a id="c12"></a>**C12.** Algorithm5는 후보 범위의 silhouette를 계산하고 local maximum을 선택하며, 없으면 K=1부터 K_max까지의 argmax로 되돌아간다. largest local maximum과 본문의 dominant local maximum 표현, 후보 범위 밖 score 계산 및 K=1의 silhouette 처리 조건은 인쇄 설명만으로 확정하지 않는다. 실제 선택 K를 재현한 결과도 아니다.

<a id="c13"></a>**C13.** 군집용 고정 encoder와 군집별 학습 모델을 구분한다. FMCL은 사전 군집이 downstream 모델 구조에 의존하지 않는다고 제안하지만, signature를 만드는 FM과 label 정보에는 의존한다. 이 구분 없이 최종 모델·정보·비용 모두와 무관한 방식이라고 확대하지 않는다.

## 저자 실험의 조건

<a id="c14"></a>**C14.** BUSI는780개 초음파 이미지의 benign·malignant·normal 3class, LungHist700은700개 폐 조직 이미지의 squamous cell carcinoma·adenocarcinoma·normal 3class로 설명한다. Imagenette는 ImageNet의10class 부분집합이다. 통신 트래픽 시계열 회귀의 성능 검증으로 옮겨 쓰지 않는다.

<a id="c15"></a>**C15.** 기본 label-skew는 Dirichlet α=0.1이며 의료 두 데이터셋은 각각20client·5seed, Imagenette는30client·3seed로 보고한다. class 비율의 이질성이 다른 도메인·시간 변화·새 client의 모든 이질성을 시험했다는 뜻은 아니다.

<a id="c16"></a>**C16.** 의료 학습기는 ResNet9, Imagenette는 ResNet18을 무작위 초기화해 학습한다. 고정 encoder는 LungHist700의 CHIEF, BUSI의 USFM, Imagenette의 ViT-Tiny이다. FECFL·PACFL의 FM 변형도 같은 encoder를 쓰며, 표에는 원형과 FM 변형이 따로 있으므로 모델 정보가 다른 비교를 하나로 합치지 않는다.

<a id="c17"></a>**C17.** 실험은100 communication rounds, local epoch1, client 참여100%, SGD로 설명한다. 학습률은 두 의료 데이터셋0.0001, Imagenette0.01이다. 참여율이 낮거나 가용 client가 변하는 환경의 결과까지 이 설정으로 입증하지 않는다.

<a id="c18"></a>**C18.** 지표는 accuracy·macro F1·AUC-ROC이고, seed별 결과를 round별로 평균한 뒤 가장 좋은 round의 mean±std를 보고한다고 설명한다. 같은12쪽 §4.6은 최고 평균 validation metric, §5는 validation loss 기준이라고 적어 선택 기준의 서술 차이가 남는다. 이를 임의로 통일하거나 test 누수를 입증한 것으로 쓰지 않는다.

<a id="c19"></a>**C19.** one-shot 방식 FMCL·FECFL·PACFL의 비교에서는 의료 K=3, Imagenette K=5로 고정했다고 적는다. Table1에는 별도로 FMCL Auto-K 행이 있다. 자동 K 절차의 제안, 고정 K 비교, 실제 Auto-K 행의 결과를 구분하며 seed별 선택 K와 군집 구성은 이 표에 보고되지 않는다.

## 보고 결과와 본문·표의 차이

<a id="c20"></a>**C20.** Table1의3데이터셋×10방법×3지표,90개 mean±std 쌍(180표시수)을 전사했다. 이는 저자 요약표이며 seed별 원시 결과나 신뢰구간이 아니다. 적은 seed의 평균·편차만으로 통계적 유의성, 재현 성공 또는 UPC 적용 효과를 확정하지 않는다.

<a id="c21"></a>**C21.** Auto-K는 표의9개 평균 모두에서 가장 높다. 고정 FMCL 대비 accuracy/F1/AUC 평균 차이는 BUSI +0.25/+0.31/+1.94, LungHist700 +0.74/+0.93/+0.24, Imagenette +9.87/+9.89/+1.80 percentage points다. 그러나 std는9개 중7개가 커지고2개만 줄어들어13쪽의 전반적인 variance 감소 설명을 모든 지표의 사실로 옮기지 않는다.

<a id="c22"></a>**C22.** 12쪽은 overlap 제거가 일관되게 성능을 낮춘다고 설명하지만, BUSI AUC는 no overlap 94.44±1.62가 고정 FMCL 93.93±1.36보다 높다. 나머지8개 평균은 고정 FMCL이 높다. 이 반례와 Auto-K의9개 평균 최고 결과를 구분하고, 평균 차이의 유의성은 추가 확인으로 남긴다.

<a id="c23"></a>**C23.** Table1에서 PACFL과 FECFL 모두 FM 변형의9개 평균이 각 원형보다 높다. 이 표가 보여 주는 것은 해당 encoder·분할·학습 조건의 저자 보고 결과이며, 고정 FM을 추가하면 모든 데이터나 예측 문제에서 항상 좋아진다는 결론은 아니다.

<a id="c24"></a>**C24.** Figure2는100rounds에 걸친 세 데이터셋의 평균 test accuracy 곡선이며 legend에는8방법이 있다. Auto-K와 no-overlap 곡선은 표시하지 않는다. y축 문구는 Accuracy(%)이지만 눈금은0.2–0.8 등 비율 형태다. 곡선의 빠른 수렴 설명을 벽시계 시간·GPU 비용 감소로 바꾸거나 그림에서 seed별 원시값을 복원하지 않는다.

## 비용·재현·후속 연구의 경계

<a id="c25"></a>**C25.** 학습 중 추가 군집 통신이 없다는 설명은 초기 FM embedding 추출·signature 전달·쌍별 거리 계산과 이후 군집별 FL 학습 비용이 없다는 뜻이 아니다. 이16쪽에서 해당 시간·GPU·메모리·전송량의 실측 표는 확인되지 않았다. 비교 설계에서는 초기 비용과 전체 학습 비용을 따로 기록해야 한다.

<a id="c26"></a>**C26.** raw data를 공유하지 않는다는 설명과 class prototype·비율을 server로 보내는 절차를 함께 남긴다. 이16쪽은 signature 전송의 정형 privacy 보장이나 공격 실험을 제공하지 않으므로 그런 보장이 확인됐다고 쓰지 않는다. 이는 논문의 해당 절차 범위에 대한 기록이다.

<a id="c27"></a>**C27.** 이번 FMCL5그룹에는 실행 코드·checkpoint·seed별 결과가 없다. 실제 분할·전처리·정확 seed ID·encoder 판본·Auto-K 출력·round 선택 기준과 비용을 실행 환경에 연결하는 작업은 남는다. 논문이 인용하는16개 참고문헌을 읽은 것과 각 참고문헌 전문을 직접 검수한 것도 구분한다.

<a id="c28"></a>**C28.** 사전 군집 후 별도 모델 학습이라는 구조는 재사용할 선행연구로 남기되, 연속 target에서 class 역할을 어떻게 정의할지, 관측 가능한 정보만으로 signature를 만들 수 있는지, 동일 입력·출력 공유의 손실 조건과 비용이 무엇인지 먼저 명시해야 한다. FMCL 분류 성능을 UPC 소속 수정이나 RCTL 개선의 직접 근거로 쓰지 않는다.

<a id="c29"></a>**C29.** 원79의 관측 입력과 조건부 평균 결합 후보, gradient 비교와 원80 진단 계획은 당시의 다음 단계다. 이번 기록 정리는 그 계획을 실행하거나 오래된 학습 예산을 다시 승인하는 작업이 아니다. 원79의 EMD·Toso·FedCAP·검색/접근 잔여 자료, 원80 결과와 이후 기록은 계속 검수한다.

## 팀원이 먼저 확인할 자료

| 목적 | 자료 |
|---|---|
| 구조와 수식의 조건 | [절차 해석](../evidence/0083-fmcl/algorithm-notes.json) |
| 평균·편차와 반례 | [Table1 전체 요약값](../evidence/0083-fmcl/table1.json) |
| 당시 분산 학습 판단 | [원76–79 기록](0076-0079-learning-decisions.md) |
| 전이 점수와 실제 출력 공유 | [회귀 전이](0079-regression-transferability.md) · [Task2Vec](0080-task2vec-task-and-output-sharing.md) |

공식 탐색 위치: [FMCL arXiv v1](https://arxiv.org/abs/2604.27510v1). 이번 검수는 저장한 파일을 읽은 것으로, 링크의 현재 원격 상태나 후속 판본을 재조회한 결과가 아니다.
