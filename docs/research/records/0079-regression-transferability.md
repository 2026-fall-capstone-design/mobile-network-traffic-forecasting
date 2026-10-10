# 원78 보완: 회귀 전이 점수의 조건과 공식 코드

상태: 40개 핵심 주장의 작성 후 원문 대조 완료.

원78은 **source 표현에서 target 출력층을 다시 맞출 수 있다는 것**과 **여러 cell의 실제 출력을 한 함수로 함께 학습해도 된다는 것**을 구분했다. 이 기록은 그 판단에 사용한 Nguyen 등의 UAI 2023 논문을 본문·보충자료·고정 코드까지 보완한다. 논문의 좋은 결과와 예외를 함께 보존하며, 표기 차이를 당시 미채택 이유로 소급하지 않는다.

[당시 판단 원본](../evidence/0076-0079-learning-decisions/originals/SRC-0022034.md.txt) · [출처와 판본](../sources/history-079.md) · [수치 전사](../evidence/0079-regression-transferability/reported-tables.json) · [주장별 검수](../verification/history-079.md)

## 검토 범위와 이론의 대상

<a id="c01"></a>**C01.** 이번 대상은 *Simple Transferability Estimation for Regression Tasks*의 본문 12쪽·보충자료 11쪽, README 14행·`reg_score.py` 30행, 저장 commit/repository/tree JSON 3개, TXT 2개와 원 PNG 3개다. PDF는 모든 쪽의 텍스트·수식·그림·표·참고문헌을 읽었다. TXT는 PDF 전쪽과 추출문 대응을 확인했고 원 PNG는 직접 열람했다. 원78의 다른 문헌까지 이번 묶음에서 완료한 것은 아니다.

<a id="c02"></a>**C02.** 본문 §3.1의 source 모델은 특징 추출기 `w*`와 head `h*`다. 이론의 target 학습은 `w*`를 고정하고 새 head `k*`를 target 데이터에 적합한다. source·target 출력 차원은 달라도 되며 head는 다층·비선형일 수 있다. 최적화는 global minimum을 가정하고, footnote 2는 실제 알고리즘의 local minimum 가능성을 인정한다. 실험의 half/full fine-tuning은 이 고정 특징 설정과 구별된다.

<a id="c03"></a>**C03.** Definition 3.1의 전이가능성은 target 분포에서의 **음의 기대 제곱 L2 오차**다. 제곱 없는 norm이나 MAE가 아니다. target 표본은 iid로 가정한다. Definition 3.2의 모든 task 쌍에 대한 순위 일치는 추정기가 지향하는 정의이며, 제안 점수가 언제나 정확한 순위를 준다는 증명 결과로 읽지 않는다.

<a id="c04"></a>**C04.** Linear MSE는 source 특징을 target label로 보내는 선형 head를 적합한다. 논문의 점수는 `−min[표본 평균 제곱 잔차의 합 + λ‖A‖F²]`이며 intercept `b`에는 penalty가 적혀 있지 않다. `λ=0`이고 target head가 선형이면 음의 경험 MSE와 연결된다. 추가 적합 없이 특징 유사도만 계산하는 방법은 아니다.

<a id="c05"></a>**C05.** Label MSE는 target 입력에 대한 source 예측을 target label로 선형 변환한다. Shared Inputs Label MSE 특례는 **동일한 입력 벡터**에 source와 target의 실제 label이 함께 있는 경우다. 같은 시각의 관측이라도 cell별 lag 벡터가 다르면 이 특례의 조건을 충족한 것이 아니다.

<a id="c06"></a>**C06.** Lemma 5.1의 증명은 `k(v)=A*h*(v)+b*`를 선택한다. 따라서 이 합성함수가 허용된 target head 집합에 속해야 한다. 본문의 “모든 선형 모델을 포함한다”는 문장만으로 임의의 비선형 `h*`와의 합성까지 자동으로 허용된다고 단정하지 않는다. 원78도 이 조건을 명시했다. 전체 증명이 틀렸다거나 구현이 실패했다는 판정은 아니다.

<a id="c07"></a>**C07.** Theorem 5.2는 음의 target 기대 제곱오차에 대해 `Tr ≥ T_label − C/√n_target`의 하한을 제시한다. ReLU feed-forward 모형, bounded 입력·출력과 모형의 제한, iid 및 앞선 head/최적화 조건이 붙는다. 공유 입력 정리는 `2T_shared − 2‖A‖F²×source 경험오차 − C/√n` 형태다. 하한의 순위가 실제 성능 순위와 항상 같다는 보장이나 MAE·BN·LSTM RCTL의 pooling 보장으로 확대하지 않는다.

<a id="c08"></a>**C08.** 표기는 원문 그대로 보존한다. 본문 p4의 `A` 차원 표기와 `Aw`/`Az` 곱의 방향은 벡터 관례가 명료하지 않다. 보충 p2에서는 `M`으로 모형 출력을 제한하므로 이를 단순한 파라미터 개수 조건으로 축약하지 않는다. 같은 쪽의 `F_j` 정의와 잔차 제곱 contraction 단계도 표기 확인이 필요하다. 이 관찰만으로 실제 실행 결과를 무효화하지 않으며, 인용된 일반화 이론 논문 전체를 검증했다고 표시하지 않는다.

## 고정 공식 코드와 재사용 조건

<a id="c09"></a>**C09.** `reg_score.py:5–16`은 `LinearRegression().fit(y_source,y_target)` 후 **같은 `y_source`**를 예측해 음의 MSE를 반환한다. `18–30`행의 Ridge 경로도 같다. 입력은 target 표본의 특징, source 예측 또는 공유 입력의 source label일 수 있다. 함수 자체에는 별도 query/test 분할, 시간 분할, cell별 holdout이나 seed 반복이 없다.

<a id="c10"></a>**C10.** Ridge는 `alpha=n*alpha`, 기본 `solver='svd'`로 적합하지만 반환값은 음의 잔차 MSE이며 **penalty를 더하지 않는다**. 논문 Definition 4.1/4.2의 regularized objective와 반환 score를 구분한다. 이것은 원78의 34행에도 기록된 주의점이다. 이 차이가 논문의 각 성능표에 미친 크기나 우열 변화는 저장된 점수 함수만으로 알 수 없다.

<a id="c11"></a>**C11.** 척도에도 조건이 있다. [scikit-learn 1.2.2 MSE API](https://scikit-learn.org/1.2/modules/generated/sklearn.metrics.mean_squared_error.html)는 기본적으로 출력 차원의 오차를 평균하고, [같은 버전의 Ridge API](https://scikit-learn.org/1.2/modules/generated/sklearn.linear_model.Ridge.html)는 잔차 제곱합에 penalty를 더하는 목적을 명시한다. 이 API 조건에서 코드는 `−SSE/(n·d_target)`, 논문 잔차 항은 `−SSE/n`이다. 같은 출력 차원에서 양의 상수배만 다르면 순위가 같지만, 서로 다른 차원·penalty 포함 여부를 섞어 절대 점수를 비교해서는 안 된다. 이 보조 API 확인은 당시 실행 환경이 1.2.2였다는 증거가 아니다.

<a id="c12"></a>**C12.** 저장 commit은 `b494b4e56be86229883b039230f708236364b772`이다. README와 score 파일의 Git blob을 계산해 저장 tree의 각 SHA와 일치함을 확인했다. tree JSON 최상위 `sha`는 commit SHA로 적혀 있어 commit의 실제 `tree.sha`와 다르다. 그러나 7개 최상위 entry로 Git tree를 재구성한 SHA는 `2b310360f7082042fbcb7911665cce7e5413fbe9`로 commit의 tree와 일치한다. 원 metadata를 고치거나 이 필드 차이만으로 코드 판본 불일치를 선언하지 않는다.

<a id="c13"></a>**C13.** README는 requirements 설치와 외부 특징 pickle을 이용한 demo를 안내한다. 저장 tree에는 `requirements.txt`, `demo.ipynb`, `logme.py`, 결과 CSV 등이 보이지만 이번 원78 packet에는 그 내용이 보존되지 않았다. 링크 접근·패키지 설치·pickle 로딩·source import·demo 실행은 하지 않았다. 환경·전체 결과 생성 경로가 검증된 재현 패키지로 취급하지 않는다.

## 데이터·학습·비교 단위

<a id="c14"></a>**C14.** 논문은 이미지 keypoint 회귀를 다룬다. CUB는 11,788장 중 train 9,788/test 2,000, keypoint 15개이며 가려진 keypoint는 source/target 학습에서 제외한다. OpenMonkey는 원 분할 train 66,917/test 22,306, landmark 17개다. 위치 label은 이미지 폭·높이로 `[0,1]`에 맞춘다. 시계열의 rolling-origin 평가나 모바일 트래픽 raw-unit MAE 실험이 아니다.

<a id="c15"></a>**C15.** 기본 backbone은 ResNet34다. Head retraining은 마지막 FC, half fine-tuning은 본문상 마지막 convolution block과 모든 FC, full은 전체 모델을 학습한다. half는 약 13M 파라미터다. 보충자료는 half를 “last convolution layer”로 표현하므로 실제 layer 목록까지 동일하다고 단정하지 않는다. Head retraining은 CUB 15/OpenMonkey 30 epoch, half/full fine-tuning은 15 epoch다.

<a id="c16"></a>**C16.** 보충 B.1의 source 학습은 scratch에서 MSE·AdamW·40 epoch·batch 64·cosine learning-rate schedule을 사용한다. 입력은 256×256이며 affine, Gaussian blur, color jitter를 적용하고 horizontal flip은 사용하지 않는다. 해당 절에서 초기 learning rate 수치는 확인되지 않는다. 이후 dSprites 절의 `1e−3`을 이 실험의 값으로 가져오지 않는다.

<a id="c17"></a>**C17.** 주요 비교는 `λ=0/1`의 LinMSE·LabMSE와 LogME·TransRate 및 label 기반 변형이다. 2D label 실험의 TransRate는 각 차원을 5개 구간으로 나눈다. 주 지표는 전이 점수와 실제 target test 성능인 음의 MSE 사이의 Pearson 상관이다. OpenMonkey 17 source→CUB 15 target의 교차 데이터 실험은 255쌍, 각 데이터 안의 서로 다른 keypoint 쌍은 CUB 210/OpenMonkey 272쌍이다.

## 성능 보고와 함께 남길 예외

<a id="c18"></a>**C18.** Table 1의 교차 데이터 head 조건에서 LabMSE1과 LinMSE1은 각각 `.995`, 비교 LabLogME/LogME는 `.824/.969`다. half에서는 LinMSE0 `.866`이 LogME `.870`보다 낮고, full도 `.855 < .861`이다. 본문의 최대 25.9%·평균 12.9% 개선은 저자가 보고한 **상관 추정 성능의 상대 개선률**이며, 트래픽 예측 MSE 감소율이나 모든 조건의 우세를 뜻하지 않는다.

<a id="c19"></a>**C19.** Table 2의 CUB head는 LabMSE1 `.946`/LinMSE1 `.960`으로 높지만 full에서는 모든 값이 낮다. OpenMonkey head는 LabMSE0 `.973`인 반면 LabMSE1 `.773`이 LabLogME `.890`보다 낮다. half/full에서는 LabMSE1 `.890/.882`가 LabMSE0 `.754/.705`보다 높다. 본문의 최대 113%·평균 36.6% 역시 상관 개선 보고이며, 데이터·학습 방식·정규화 설정별로 결과가 달라진다.

<a id="c20"></a>**C20.** Figure C.6의 CUB full fine-tuning에서 8개 방법의 p값은 `.063–.558` 범위로 모두 `.05`보다 크다. Table 2의 상관 범위는 `.041–.128`이다. 이는 해당 비교에서 유의한 상관을 관찰하지 못했다는 보고다. 모든 전이 방법이 무용하거나 우리 RCTL에서 효과가 없다는 결과로 일반화하지 않는다.

<a id="c21"></a>**C21.** Supplement Table C.1/C.2는 같은 교차 데이터 실험의 Kendall/Spearman 상관이다. 저자는 각각 평균 13%/9.7%, 최대 28.4%/19.9% 개선을 보고한다. 각 표의 24개 값을 보존했다. Pearson과 다른 지표를 한 수치로 합치거나 세 표를 서로 독립된 새 모델 실험으로 세지 않는다.

<a id="c22"></a>**C22.** Table C.3은 OpenMonkey 5개 keypoint의 10D 출력에서 CUB 5개 keypoint 조합 252개로 전이한 결과다. Table C.4는 CUB의 4개 2D source에서 10D target으로 전이한 224쌍이다. 두 경우 TransRate는 차원당 2개 bin을 사용한다. C.3의 “두 λ 모두 우수”라는 서술에는 예외가 있다. LabMSE1 half/full `.943/.863`은 LabLogME `.944/.878`보다 낮고, LinMSE1 full `.881`은 LogME `.892`보다 낮다.

<a id="c23"></a>**C23.** Table C.5/C.6의 모든 source별 행을 보존했다. CUB는 15 source×3학습 방식×8방법=360값, OpenMonkey는 17×3×8=408값이다. 각 행은 **한 source에서 다른 target들로 전이할 때**의 상관이다. 전체 source–target 쌍을 합친 Table 2와 단위가 다르므로, 한 source의 높은 상관과 pooled 상관의 차이를 자동으로 모순으로 처리하지 않는다.

<a id="c24"></a>**C24.** Source별 예외도 실험 설계에 필요하다. CUB full/Left eye는 LabTransRate `.456`이 LabMSE0/1 `.297/.347`보다 높고, LogME `.333`이 LinMSE0/1 `.282/.326`보다 높다. OpenMonkey head/Hip는 LabMSE1 `.325` 대 LabLogME `.922`/LabMSE0 `.989`, Tail은 `.312` 대 `.936/.993`이다. 해당 head 표의 17개 source 모두에서 LabMSE1이 LabLogME보다 낮다. 정규화가 항상 유리하다고 요약하지 않는다.

<a id="c25"></a>**C25.** 작은 target 학습 자료 실험은 100–400개 이미지를 사용하고 10개 random seed의 10회 결과를 평균·band로 보여준다. source는 CUB Belly와 OpenMonkey Right eye이며 test는 전체 test set이다. 정확한 seed 번호와 모든 원시 좌표는 이 자료에서 확보되지 않았다. 그림의 방향을 읽은 것과 각 점의 수치 결과를 복구한 것을 구분한다.

<a id="c26"></a>**C26.** Table 3은 선택한 source의 실제 target test MSE가 후보 중 top-k에 드는 비율이다. 15개 target의 top-1에서는 LogME `11/15`가 LinMSE0 `9/15`, LinMSE1 `10/15`보다 높다. LabMSE1은 `2/15`, LabLogME는 `6/15`다. LinMSE1의 top-3/top-5는 각각 `13/15`이므로 상관·top-1·top-k를 서로 대신하는 성과로 쓰지 않는다.

<a id="c27"></a>**C27.** Table 4는 CUB에서 λ를 `0–20`의 11개 값으로 바꾼 결과다. CUB full의 낮은 상관은 유지된다. 같은 표의 baseline 중 LabLogME full `.120`은 Table 2의 `.128`과, TransRate half `.006`은 `.064`와 다르다. 전사에서 두 값을 모두 보존했다. 반복·집계 차이인지 인쇄 오류인지 확인할 근거가 없으므로 임의 수정하지 않는다.

## 비용·다른 전이 설정·그림의 주의점

<a id="c28"></a>**C28.** Figure 2 왼쪽은 5회 측정의 평균과 ±표시다. Label 기반 4방법의 시간은 `3.55/4.11/2.87/2.58`, feature 기반은 `112.99/94.57/107.48/27.41`이며 caption 단위는 ms다. 순서는 각각 LogME/TransRate/MSE0/MSE1이다. LinMSE0 `107.48`은 TransRate `94.57`보다 크므로 “모두 더 빠르다”는 서술을 모든 bar에 적용하지 않는다. 이 시간은 우리 TabICL 호출·RCTL fit 비용이 아니다.

<a id="c29"></a>**C29.** Figure 2 오른쪽은 target 표본 수와 시간의 관계를 그리지만 세로축은 `Execution Time`, 눈금은 대략 `0–.06`이며 caption의 ms와 어떻게 연결되는지 명확하지 않다. 단위를 추정해 왼쪽 bar와 직접 비교하지 않는다. 실행 장비·라이브러리·특징 추출 포함 범위까지 보존 코드에서 재현한 비용으로 표시하지 않는다.

<a id="c30"></a>**C30.** §6.7/B.2는 ImageNet 분류 사전학습 8개 모델을 dSprites의 x/y 위치·scale·orientation 4D 회귀로 full fine-tuning한다. 모델은 ResNet50/101/152, DenseNet121/169/201, GoogleNet, Inceptionv3다. 737,280장의 60/20/20 train/validation/test 분할, AdamW 10 epoch, 초기 LR `1e−3`과 3 epoch마다 1/10 감소를 보고한다. keypoint 실험이나 우리 시계열 분할과 구분한다.

<a id="c31"></a>**C31.** Figure 3 관련 `0.00612/0.00616/0.00610/0.00546`은 각각 LogME/TransRate/LinMSE0/LinMSE1 점수와 test MSE의 8개 모델 관계에 직선을 맞춘 **적합 RMSE**다. 각 target 예측 모델의 test MSE 자체가 아니다. 추정 점수는 training 자료, 실제 성능은 test 자료에서 얻는다는 차이도 유지한다.

<a id="c32"></a>**C32.** Supplement Figure C.1의 TransRate는 상관 `.121`, `p=.054`; LabTransRate는 `.165`, `p=.008`이다. 후자는 `.05`보다 작지만 `.001`보다 작지는 않다. Figure C.3의 LabTransRate 상관은 `.311`로 인쇄되어 본문 Table 1의 `.410`과 다르다. 표와 그림 중 하나를 선택해 덮어쓰지 않는다. 원시 점·상관 계산 코드를 확보하지 못했으므로 원인이나 부호 관례를 확정하지 않는다.

<a id="c33"></a>**C33.** 보충 C.1은 이론 하한이 충분한 표본 없이는 느슨할 수 있음을 인정한다. `|score|/gap` 비율로 LinMSE0/1 `1.6/2.0`, LabMSE0/1 `2.3/2.3`을 보고하고 gap과 실제 MSE가 유의하게 상관되지 않았다고 서술한다. 해당 주장에 대한 원시 값·CI·p값은 제시된 자료에서 확보하지 못했다. 복잡도 항을 모든 task에서 무시해도 된다는 근거로 쓰지 않는다.

## 당시 판단과 팀의 재검토 조건

<a id="c34"></a>**C34.** 저장 TXT 2개는 총 23쪽 모두 대응했다. main은 layout, supplement는 plain 추출에 대응하며 PDF PAGE 표지·개행 처리만 제외했다. 원 PNG 3개는 main p3/p5, supplement p2다. PDF의 Link 주석은 각각 317/90개이고 그 외 주석과 내장 첨부는 없다. TXT·PNG·새 렌더·정확 사본을 독립 연구 결과나 추가 전문으로 중복 가산하지 않는다.

<a id="c35"></a>**C35.** 팀에는 [공식 논문·보충자료](https://proceedings.mlr.press/v216/nguyen23a.html), [고정 코드](https://github.com/CuongNN218/regression_transferability/tree/b494b4e56be86229883b039230f708236364b772), source ID·상대 경로·SHA와 수치 전사·검수를 제공한다. 저장 repository 응답의 `license`는 null이다. 현재 접근 가능성이나 장기 공용 보존을 이 저장 응답만으로 보장하지 않는다. 외부 특징 데이터·환경·실행 결과의 팀 접근은 별도 확인 대상이다.

<a id="c36"></a>**C36.** 원78은 공통 probe의 task embedding 또는 회귀 전이 점수를 그대로 cell 병합 점수로 쓰는 후보를 채택하지 않았다. 핵심 이유는 원 방법이 **target 출력의 추가 변환·head 재적합**을 허용하는 반면, 당시 목표는 cell들의 실제 target을 같은 예측 함수로 학습하는 것이었다는 점이다. 이번 수치표의 예외나 metadata 표기 차이를 그때의 판단 이유로 추가하지 않는다.

<a id="c37"></a>**C37.** 원78의 `y_A=c+x`, `y_B=c−x` 예시는 조건을 명시한 기호 설명이다. `x`는 `[−1,1]`의 대칭 분포, `c>1`, cell 비중은 같고 입력에 cell을 구분할 정보가 없다. 선형 출력 변환을 허용하면 두 관계의 λ=0 Label MSE 잔차가 모두 0이지만, 같은 scalar 출력의 최적 공통 제곱 손해는 `E[x²]`, MAE는 `E[|x|]`로 남는다. cell ID 등 구분 정보가 추가되면 전제가 달라진다. 논문의 실험값·새 트래픽 실험·새 정리로 세지 않는다.

<a id="c38"></a>**C38.** 당시 판정은 모든 transferability 방법이나 multi-head RCTL의 불가능성을 선언한 것이 아니다. 원78은 기존 작은 확인에서 TabICLv2 직접 예측의 긍정적 증거와 16-cell RCTL의 global 우세를 함께 유지했다. 기존 summary의 raw-unit MAE 재확인은 새 실험·발견으로 세지 않았다. 이 기록도 논문 상관 결과를 Tab 직접 예측, 소속 점수 또는 RCTL 최종 오차와 섞지 않는다.

<a id="c39"></a>**C39.** 재검토할 때는 먼저 공유할 특징·head·target 좌표와 허용할 추가 적합을 명시한다. cell별 head를 추가하면 같은 구조의 global multi-head 비교군을 포함하고, clustering이 별도로 필요한 이유를 설명해야 한다. 원78의 당시 조건은 최종 RCTL 결과로 병합 점수를 맞추지 않는 것이었다. 이는 과거 설계 조건의 기록이며 새 학습 실행 지시가 아니다.

<a id="c40"></a>**C40.** 이번 검토는 원78의 등록 외부 43개 그룹 중 회귀 전이에 관한 12개를 다룬다. 기존 H074의 manifest/read-scope 검토와 다른 문헌의 본문 독해를 혼동하지 않는다. Task2Vec·NTKMTL과 남은 검색·접근 기록, 원79 외부자료·원80 결과 및 이후 기록의 검수는 계속된다. 새 모델 학습·추론·과거 코드 실행은 0이며 전체 아카이브 Goal은 미완료다.

## 찾아 쓸 때

출력 변환을 허용하는 전이 실험은 C02–C13을 먼저 확인한다. 정규화나 source 선택을 설계할 때는 C18–C27의 이득과 손해를 함께 비교한다. 논문 수치를 우리 트래픽 효과로 인용하려면 데이터·학습·평가 단위가 같은지 C14–C17과 C28–C33에서 확인한다. 과거 후보를 다시 제안하기 전에는 C36–C39 및 당시 원문을 읽는다.
