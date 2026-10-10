# 76 보완: TabDistill의 저장된 상호작용 비교표

[문헌·구현 검토](0076-response-transfer-audit.md) · [출처와 범위](../sources/history-076.md) · [수치 자료](../evidence/0076-tabdistill-interactions/README.md) · [주장 검수](../verification/history-076.md)

TabDistill을 다시 검토할 때는 상호작용을 선택한 표와 그 목록으로 모델을 다시 학습한 표를 구분해야 한다. 같은 항 수라도 목록·순서·고유 항 수가 다르고, MAE와 MSE가 다른 비교 결과를 낼 수 있다. 이 기록은 원76의 참고 구현에서 남아 있던 CSV를 읽어, 과거 결과를 재사용할 때 확인할 조건을 보완한다.

**20개 핵심 주장의 작성 후 원문 대조를 완료했다.** 저장 결과만 읽었으며 새 모델 학습·추론은 하지 않았다.

## 자료의 출처와 검토 범위

<a id="c01"></a>**C01.** `SRC-0063879`의 삭제 patch에 남은 PMLB 상호작용 CSV 27개, 데이터 2,253행을 모두 읽었다. H075에서 읽었던 나머지 61개 patch와 합치면 커밋 응답의 88개 patch를 읽은 범위가 된다. 이번에는 최상위 메타데이터와 파일별 메타데이터도 확인했다. 이 범위는 저장된 커밋 JSON이며 외부 저장소 전체나 연결된 모든 논문의 검토가 아니다. [명세](../evidence/0076-tabdistill-interactions/source-manifest.json)

<a id="c02"></a>**C02.** 저장 커밋은 `64214da0edf7eef6e8bf645332471d78b30345e8`, 부모는 `58bd71068a879c8ee90e62f405d8fb8f6db5e81e`다. 커밋 설명은 비핵심 자료·스크립트의 추적 중단이고, 88개 파일 항목 중 86개가 삭제됐다. `.gitignore`에는 해당 디렉터리가 추가됐다. 이 삭제를 실험 실패나 논문 철회의 증거로 해석하지 않는다. CSV는 삭제 patch로 복원했으며 Git blob SHA-1이 원 응답의 값과 일치한다. [고정 커밋](https://github.com/Clouddelta/tab-distill/commit/64214da0edf7eef6e8bf645332471d78b30345e8)

<a id="c03"></a>**C03.** 표의 방법명은 BII·FBII·FOURIER·FSII·MOBIUS·SII·STII의 SPEX-EBM 7종과 `Baseline-EBM`, `RuleFit-Support-EBM`이다. 열에는 모델명, 명목 항 수, 항 목록, 시간, MSE·RMSE·MAE·R2, 지수 이름, 방법명이 있다. 시간·MSE·RMSE·MAE·R2의 5열, 11,265칸은 유한값이고 2,253행의 RMSE는 저장 MSE의 제곱근과 허용오차 안에서 일치한다. 이 산술 일치는 데이터 누수 부재나 모델의 재현 성공을 증명하지 않는다. [산술 검수](../evidence/0076-tabdistill-interactions/interaction-audit.json)

<a id="c04"></a>**C04.** 27개 데이터셋 × 9개 방법 × 1–10항의 2,430칸 중 177칸은 행이 없다. 예를 들어 pollution에는 FOURIER 행이 전혀 없고, election2000의 FOURIER는 3항까지, chatfield의 FOURIER는 2항까지다. 빈칸을 0점이나 실행 실패로 채우지 않는다. 두 baseline은 각각 270행이지만 FBII는 254행, FOURIER는 200행이므로 모든 저장 행을 한꺼번에 평균 내면 비교 조건과 표본 수가 달라진다. [전체 범위표](../evidence/0076-tabdistill-interactions/dataset-coverage.csv)

## 항 수·순서·중복을 함께 보존한다

<a id="c05"></a>**C05.** 명목 항 수는 모든 행에서 목록 길이와 같지만, RuleFit의 12행은 같은 항을 반복한다. cloud의 6–10항은 고유 항 5개, bodyfat의 7–10항은 6개, sleuth_case1202의 8–10항은 7개다. 각 구간의 오차 지표는 마지막 고유 항을 추가한 행과 같고 시간만 달라진다. 원본을 고쳐 쓰지 않고 명목 항 수와 고유 항 수를 별도 열로 제공한다. [중복 항 12행](../evidence/0076-tabdistill-interactions/repeated-terms.csv)

<a id="c06"></a>**C06.** 같은 데이터셋 안에서 순서까지 같은 항 목록을 가진 복수 행 묶음은 287개다. 각 묶음의 MSE·RMSE·MAE·R2는 모두 같으며, 목록 하나당 한 행만 남기는 방식으로 계산하면 추가 행은 700개다. 시간은 이 비교에서 제외했다. 이 700행을 삭제해야 한다는 뜻도, 각각 독립적인 재현 실험이라는 뜻도 아니다. 방법별 선택이 같은 목록에 도달한 사실과 실제 실행의 독립성을 구분한다. [집계 방법과 데이터별 결과](../evidence/0076-tabdistill-interactions/interaction-audit.json)

<a id="c07"></a>**C07.** 중복 횟수를 유지한 채 항의 순서만 무시하면, 순서가 다르고 오차 지표도 다른 묶음이 207개다. 순서가 달라도 지표가 같은 묶음도 1개 있다. 예를 들어 sleuth_case1202의 2항은 SPEX의 `[(2,4),(0,4)]`와 Baseline의 반대 순서가 같은 지표를 낸다. 따라서 정렬해서 같은 목록으로 만들거나 순서 차이만으로 다른 수치의 원인을 확정하지 않는다. [산술 검수](../evidence/0076-tabdistill-interactions/interaction-audit.json)

<a id="c08"></a>**C08.** 항의 정수 인덱스를 0부터 시작하는 입력 열 번호로 읽으면, 적어도 10개 입력 좌표가 사용된 데이터셋은 12개다. election2000·bodyfat은 적어도 14개, pollution은 15개, chatfield는 12개다. 최대 선택 인덱스로 구한 값은 선택 가능한 입력 좌표 수의 하한이며, 전처리 전 원자료의 정확한 변수 수는 아니다. 이 CSV 묶음 전체를 4월 논문의 ‘변수 10개 미만’ 선별 집합과 동일시하지 않는다. [범위표](../evidence/0076-tabdistill-interactions/dataset-coverage.csv) · [논문의 조건](../records/0076-response-transfer-audit.md#c22)

## 같은 예산에서도 비교 지표에 따라 판단이 달라진다

<a id="c09"></a>**C09.** 명목 4항으로 고정하면 9방법의 저장 행은 238개다. FBII와 두 baseline은 27개 데이터셋 모두에 4항 행이 있어 쌍별 비교가 가능하다. FBII의 MAE는 Baseline보다 작은 경우 12개, 큰 경우 15개다. MSE도 개수는 12개·15개지만 유리한 데이터셋 집합까지 같지는 않다. 이 개수는 저장 표의 기술적 집계이며 통계적 유의성이나 논문 전체 평균 순위가 아니다. [4항 원수치](../evidence/0076-tabdistill-interactions/budget-four.csv)

<a id="c10"></a>**C10.** 같은 4항 조건에서 FBII의 MAE는 RuleFit보다 작은 경우 16개, 큰 경우 11개다. MSE는 작은 경우 14개, 큰 경우 13개다. 이 비교에서는 정확히 같은 수치인 동률이 없다. Baseline과 RuleFit을 하나의 대조군으로 합치거나 MAE의 비교 결과를 MSE에 그대로 적용하지 않는다. [쌍별 집계](../evidence/0076-tabdistill-interactions/interaction-audit.json)

<a id="c11"></a>**C11.** FBII가 두 대조군보다 좋은 사례와 나쁜 사례를 함께 남긴다. `613_fri_c3_250_5`의 4항 MAE/MSE는 FBII `0.1882286775509591/0.0558094980377644`, Baseline `0.1942512331617009/0.0637779120494739`이며 RuleFit보다도 작다. 반대로 `656_fri_c1_100_5`에서는 FBII `0.2148972237992618/0.0695125704050468`, Baseline `0.2107634842930085/0.0660137110576304`, RuleFit `0.1904931399728834/0.0589121075074057`이다. 모든 사례의 정확한 값은 4항 표에 보존한다. [4항 표](../evidence/0076-tabdistill-interactions/budget-four.csv)

<a id="c12"></a>**C12.** `706_sleuth_case1202`의 4항에서 FBII의 MAE `25.055834507002068`은 Baseline의 `26.73257218575734`보다 작지만, MSE `1373.0059755241828`은 Baseline의 `1303.3534664350923`보다 크다. RuleFit 대비로는 두 오차 모두 작다. 이 사례를 단일한 ‘개선’ 또는 ‘악화’로 줄이지 않는다. [4항 표](../evidence/0076-tabdistill-interactions/budget-four.csv)

<a id="c13"></a>**C13.** 같은 방법에서 기존 순서를 그대로 유지하고 마지막에 한 항을 붙인 인접 예산 쌍은 1,833개다. MSE와 MAE가 모두 작아진 쌍은 715개, 모두 커진 쌍은 798개, 서로 반대 방향인 쌍은 308개, 적어도 한 지표가 같은 쌍은 12개다. 이 집계는 다른 목록으로 교체된 예산 쌍을 포함하지 않는다. 항 수 증가가 항상 좋은 결과를 만들지는 않으며, 이 비율을 향후 실험의 성공 확률로 쓰지도 않는다. [집계 정의](../evidence/0076-tabdistill-interactions/interaction-audit.json)

<a id="c14"></a>**C14.** 세 변수 항의 효과도 양쪽 사례가 있다. `635_fri_c0_250_10`에서 FBII의 3→4항은 `(0,2,3)`을 추가하고 MAE `0.2717326673459848→0.2775257572793239`, MSE `0.1190375063368769→0.1290457363797988`로 나빠진다. 같은 데이터의 FOURIER 7→8항은 `(0,1,2)`를 추가하고 MAE `0.2744517533785089→0.2658855096667167`, MSE `0.1254174670698874→0.1174581919300975`로 좋아진다. 같은 명목 항 수도 두 변수 항과 세 변수 항의 구성에 따라 다르다. [원 CSV 위치](../evidence/0076-tabdistill-interactions/source-manifest.json)

## 저장 시간과 후속 모델 비교표의 연결

<a id="c15"></a>**C15.** 저장된 `Train_Time_s`의 범위는 pwLinear의 SII 1항 `0.190408956259489`초부터 `635_fri_c0_250_10`의 STII 10항 `7930.269992701709`초까지다. 같은 목록·지표에도 시간이 다르고, 항을 추가한 뒤 시간이 줄어드는 행도 있다. 원 표 자체에는 측정 구간·하드웨어·교사 질의 횟수·전체 파이프라인 시간이 없어 이 값을 총 비용이나 방법 자체의 속도 순위로 해석하지 않는다. [최솟값·최댓값의 행 위치](../evidence/0076-tabdistill-interactions/interaction-audit.json)

<a id="c16"></a>**C16.** 삭제된 `compare_pmlb_regression_table1.py`는 이 CSV를 만드는 코드가 아니라 읽는 코드다. `Index=fbii`, `Num_Interactions=4`의 첫 행에서 항 목록을 가져오고, PMLB 자료를 불러와 EBM·PyGAM 등을 다시 학습한다. 일반 모델의 시간은 `fit` 호출만 감싸며 예측은 그 밖에 있다. 전체 X의 범주 인코딩 후 seed 42·test 20%로 나누는 조건도 이 후속 코드에 속한다. 이를 원 상호작용 표의 분할·생성 시간 조건으로 소급하지 않는다. [부모 커밋의 소비 코드](https://github.com/Clouddelta/tab-distill/blob/58bd71068a879c8ee90e62f405d8fb8f6db5e81e/experiments/EBM_comparison/compare_pmlb_regression_table1.py)

<a id="c17"></a>**C17.** 상호작용 표의 FBII 4항과 저장 모델 비교표의 `EBM_FBII`는 27개 데이터셋 모두에서 순서 있는 항 목록이 같다. 그러나 엄격한 수치 일치는 MSE 3개, RMSE 6개, MAE 3개, R2 6개이고 시간은 0개다. 일부는 출력 자릿수 수준의 차이지만 machine_cpu의 MAE `32.58984273356018` 대 `33.365936596454105`, pollution의 MAE `44.79908887340702` 대 `43.672431123599274`처럼 더 큰 차이도 있다. 정확한 원인을 확정할 실행 메타데이터는 아직 연결되지 않았으며, 두 표를 동일 실행의 복사본으로 합치지 않는다. [27개 연결표](../evidence/0076-tabdistill-interactions/model-table-bridge.csv)

<a id="c18"></a>**C18.** 저장된 다른 `compare_index_performance.py`에는 목록의 앞부분으로 EBM을 학습하고 `fit` 시간을 재는 구현이 있다. 하지만 이 파일이 해당 PMLB CSV 27개를 만들었다는 실행 연결은 확인되지 않았다. 또한 후속 PMLB 코드의 기본 TabPFN 판본은 v3이고 출력 파일명·열에 판본을 넣지만, 삭제된 모델 결과는 판본 없는 이름과 `TabPFN` 방법명을 쓴다. 코드의 기본값을 근거로 원 표의 교사 판본을 확정하지 않는다. [이전 구현 검토](../records/0076-response-transfer-audit.md#c35) · [코드와 결과의 범위](../sources/history-075.md)

## 재사용할 때 먼저 확인할 것

<a id="c19"></a>**C19.** 이 표의 데이터셋은 PMLB 회귀 과제이며 우리 연구의 cell·기간·UPC 소속·RCTL 성능을 측정한 결과가 아니다. CSV에 seed·train/test 표본 식별자·입력 정규화·교사 판본·패키지 판본·하드웨어는 미기록이다. 원 생성기의 위치와 실행 조건은 아직 미확인으로 남긴다. 후속 코드에서 확인한 조건과 원 표에 적히지 않은 조건을 구분하면, 겉보기에 같은 실험을 다시 설계하거나 다른 실행의 결과를 혼합하는 일을 줄일 수 있다. [조건표](../evidence/0076-tabdistill-interactions/README.md)

<a id="c20"></a>**C20.** 재검토 시에는 데이터셋·방법·명목 예산을 정하고, 행의 존재 여부와 고유 항 수를 확인한 뒤 원 순서를 보존해 목록을 읽는다. MAE·MSE를 함께 보고, 원 상호작용 표와 후속 모델 결과를 구별한다. 실제 재현을 계획한다면 생성 코드 판본, 분할, teacher·EBM 설정, 시간 범위와 반복 조건을 추가로 확보해야 한다. 이 기록은 그 확인을 돕는 저장 근거이며 새 실험이나 트래픽 적용의 성공 보고가 아니다. [재사용 자료](../evidence/0076-tabdistill-interactions/README.md)
