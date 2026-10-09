# 56·58. TabPFN IML — 문맥의 가치를 다른 학습기의 표본 가치로 옮길 수 있는가

58번은 TabPFN의 context Shapley 값을 RCTL 학습 표본 가치로 사용하는 안을 채택하지 않았다. 이번 대조에서도 원문은 **TabPFN 자신의 분류 문맥 선택**을 평가한다. 다른 예측기의 학습 시간·회귀 오차·cell 군집 품질을 검증한 결과는 없다. 이 한계는 전이가 불가능하다는 증명과는 다르다. [58 당시 판단](../evidence/0056-0058-mae-sampling/originals/SRC-0021898.md.txt) · [앞선 학습 압축 검토](0056-0058-mae-sampling.md)

현재 상태는 문헌·고정 코드·저장 결과 검수다. 새 모델 학습·추론, 원 패키지 import/실행, pickle load, 난수 생성은 하지 않았다. 원본 11묶음 22경로와 58 메모를 연결했고, 논문 12쪽 텍스트와 1–11쪽 시각 자료, 저장 README/코드 4개 755줄, 보충 텍스트 6개 1,403줄을 읽었다. 6개 결과 CSV는 선택 필드 독해와 전체 평균 산술 검사 범위를 구분한다. [출처·열람 범위](../sources/history-047.md) · [주장 25개](../verification/history-047-claims.json)

## 논문·코드의 판본

Rundel 등, *Interpretable Machine Learning for TabPFN*, arXiv:2403.10923v2(2024-07-23) 12쪽을 읽었다. v1은 2024-03-16이다. 저장 PDF는 현재 공식 v2 응답과 바이트가 같다. [출판사 서지](https://link.springer.com/chapter/10.1007/978-3-031-63797-1_23)는 xAI 2024, CCIS 2154, 465–476쪽, 최초 온라인 2024-07-10, DOI 10.1007/978-3-031-63797-1_23을 확인한다. 출판본 유료 본문은 읽지 않았으며 arXiv와 내용이 같다고 표시하지 않는다.

코드는 [고정 commit](https://github.com/david-rundel/tabpfn_iml/tree/7bd39bc2e6b2f7a16602983c01086e962db45c37) `7bd39bc2e6b2f7a16602983c01086e962db45c37`(2025-07-13)이다. 저장된 README에는 유지보수 종료 안내가 있다. 논문 작성 시점 코드와 동일하다는 뜻은 아니다. 원본 텍스트 4개의 Git blob, root tree `200c4edd455877b2f4db99a7ec5ccef831f53cd7`, 112개 tree 항목을 대조했다. 저장 tree의 최상위 sha는 commit을 반복하므로 실제 root object를 별도로 재구성했다.

## 선택하는 대상과 실제 계산

논문 §2는 iid 자료와 이진 분류에 초점을 둔다. 과거 TabPFN의 고정된 신경망에 context와 query를 넣어 예측하며, 새로운 자료마다 파라미터를 다시 학습하지 않는다. 여기서 권장 1,024개 context 한계와 약 1천만 합성 사전학습 자료는 논문이 설명하는 당시 TabPFN의 조건이다. TabICLv2 또는 모든 현재 PFN의 한계로 일반화하지 않는다.

§3.4의 Data Shapley는 다음 순서다.

1. 후보 학습 관측 3,072개에서 256–512개 크기의 무작위 부분집합을 만든다.
2. 각 부분집합을 TabPFN context로 넣고 validation 512개의 예측 손실을 계산한다.
3. 후보 관측의 포함 여부를 열로 놓은 이진 설계행렬과 손실로 weighted linear surrogate를 적합한다.
4. 손실 증가 기여가 작다고 해석한 **가장 낮은 계수 512개**의 관측을 context로 선택한다.
5. 별도 test 1,024개에서 분류 성능을 측정한다.

원 X/y 쌍 중 일부를 고르는 방법이다. 합성 X/y를 만드는 TimeDC, feature 제거, cell 소속 변경, RCTL lookback 감소와는 선택 대상이 다르다. 전부를 탐색한 최적 부분집합이라는 보장은 없다. [TimeDC와 비교](0056-0058-timedc.md)

“exact retraining”은 각 부분집합에 대한 PFN의 조건부 예측을 직접 계산한다는 뜻이다. Kernel SHAP에서는 제외한 feature를 채워 넣어 전체 feature 모델을 대신 사용하는 근사를 피하고, Data Shapley에서는 각 context의 PFN 예측을 사용한다. M개 부분집합을 샘플링하고 WLS로 Shapley를 추정하는 근사는 남는다. 모든 coalition이나 모든 Shapley 값을 정확 계산했다는 뜻이 아니다. 공개 classifier의 `fit`도 입력과 class를 확인하고 context를 저장하며, 이 함수에서 새 신경망 최적화를 수행하지 않는다. [논문 §3.3–3.4](https://arxiv.org/pdf/2403.10923v2#page=5) · [data_shapley.py](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/tabpfniml/methods/data_shapley.py)

## 논문 설정과 저장 실행 스크립트

| 항목 | 논문 규모 / entrypoint의 else 분기 | 현재 entrypoint의 debug=True 분기 |
|---|---:|---:|
| 후보 관측 / validation / test | 3,072 / 512 / 1,024 | 32 / 8 / 8 |
| 부분집합 최소 / 최대·최종 context | 256 / 512 | 8 / 16 |
| M_factor / M | 3 / 9,216 | 2 / 64 |
| 반복 | 5 | 2 |

기본 파일을 실행하면 논문 규모가 된다고 안내하면 안 된다. entrypoint의 debug 변수는 위 숫자를 정하며, `Data_Shapley(debug=...)`로 전달되지는 않는다. 클래스의 debug 기본값은 False, ensemble 기본값은 16이다. MPS/CUDA/CPU를 고르는 `DEVICE` 변수도 생성자에 전달되지 않아 이 호출은 device 기본값 CPU를 사용한다. 논문 p8 각주는 장치를 “Nvidia GTX A6000 GPU”로 인쇄했다. 이를 임의로 RTX로 정정하거나 현재 CPU 기본값만으로 논문 실제 장치를 부정하지 않는다.

보충 `datasets.py`는 OpenML 자료의 문자열·category를 정수화하고 seed로 전체 행을 섞은 뒤, `train_test_split(..., stratify=y, random_state=42)`를 쓴다. 이어 평가 배열의 앞 512개를 validation, 다음 1,024개를 test로 나눈다. 시간순 예측 분할이 아니다. 학습/평가 row ID와 label 분포는 이번 근거에서 미확인이다. outer loader의 `standardize_features=False`는 전체 모델에 정규화가 없다는 뜻이 아니다. prediction interface에는 context 기준 normalize 호출, context에 fit한 power 변환, outlier/ranking 분기가 있다. 실제 checkpoint config와 그 helper 내부 전체는 확인하지 않았다.

저장 CSV의 seed는 표시 순서대로 **1825, 410, 4507, 4013, 3658**이다. 세 자료에서 같은 목록을 쓴다. 부모 초기화는 NumPy seed를 42로 다시 설정하고 classifier seed도 42로 정한다. 반복마다 모든 난수와 augmentation이 독립이었다고 확대하지 않는다. 실제 원 데이터 행 배열을 재생성하지 않았다.

## 저장된 분류 결과와 수치의 단위

고정 코드의 논문 규모 경로에서 `RC Mean ROC AUC`는 한 run 안에서 3,072개 train 배열을 512개씩 나눈 **6개 비중첩 context**의 test ROC AUC 평균이다. 가장 좋은 무작위 context나 전체 3,072개를 넣은 모델과 비교한 값이 아니다. `RC Std`는 이 6개 값의 NumPy 기본 표준편차이며, 다섯 run 평균의 표준오차가 아니다. 최적 context의 ROC AUC는 같은 run의 test를 사용한다. 저장 CSV에는 각각의 무작위 context 예측과 실제 구성 행이 없어 이 집계 경로를 원 예측까지 복원한 것은 아니다.

아래 값은 M=9,216의 저장 CSV를 Decimal로 다시 계산했다. 새 예측 결과가 아니다. 논문 p11의 0.57%, 3.3%, 1.52%는 저장값의 **차이에 100을 곱한 %p**와 반올림해 일치한다. `OC−RC`를 RC로 나눈 상대 개선율과 구분한다.

| 자료 / OpenML ID | RC 평균 AUC | OC 평균 AUC | 차이(%p) | RC 대비 상대 증가(%) | 이득/손해/동률 run |
|---|---:|---:|---:|---:|---:|
| eeg-eye-state / 1471 | 0.935675999 | 0.941337276 | 0.566128 | 0.605047 | 5/0/0 |
| higgs / 23512 | 0.649732784 | 0.682760315 | 3.302753 | 5.083248 | 5/0/0 |
| albert / 41147 | 0.668908129 | 0.684094030 | 1.518590 | 2.270252 | 5/0/0 |

15개 최종 비교에서는 모두 OC가 RC 평균보다 높다. 다만 최소 차이는 eeg-eye-state의 0.017122%p로 작다. 이 범위를 다른 M·새 seed·모든 자료로 확대하지 않는다. Fig3은 자료별 세로축 범위가 다르고 0에서 시작하지 않는다. plotting 코드가 실제 seed를 run1–5로 치환하므로 아래 대응을 보존한다.

| 표시 run | 실제 seed | eeg-eye-state 차이(%p) | higgs 차이(%p) | albert 차이(%p) |
|---|---:|---:|---:|---:|
| 1 | 1825 | 0.017122 | 6.737169 | 0.040820 |
| 2 | 410 | 0.482372 | 2.575606 | 2.689112 |
| 3 | 4507 | 0.169560 | 1.201962 | 1.813840 |
| 4 | 4013 | 1.299639 | 3.198759 | 2.375334 |
| 5 | 3658 | 0.861945 | 2.800270 | 0.673844 |

[원값·산술](../evidence/0056-0058-tabpfn-iml/stored-results-arithmetic.json)은 15행의 RC/OC 값과 차이, 정확한 소수 표현을 담는다. 상세 CSV 165행과 평균 CSV 33행을 파싱하고 297개 평균값을 검산했다. 최대 차이는 부동소수점 저장 반올림 수준인 1.2e−16이었다. 다른 M의 모든 원 metric cell을 사람이 전수 읽은 것은 아니다. 분산·신뢰구간·통계적 유의성이나 원 예측의 정확성을 새로 검증하지 않았다.

## 이득보다 먼저 필요한 비용 계산

논문은 이 선택에 거의 1만 TabPFN forward가 필요하며 다른 제안 방법보다 비싸다고 명시한다. M=9,216, 후보 3,072개 각각의 계수, WLS 및 전처리·모델 준비 비용이 든다. 후보에서 512개를 남긴 비율을 전체 계산비 감소율로 사용하지 않는다.

고정 코드의 논문 규모 분기가 정상 완료되는 경우, `.predict_proba` 호출은 validation용 9,216회, RC용 6회, M=16부터 9,216까지 11개 checkpoint의 OC 평가 11회로 **run당 9,233회**다. 이것은 정적 경로의 논리 호출 수이고 실제 측정 횟수나 시간은 아니다. 내부 ensemble은 최대 16개 configuration을 batch로 묶으므로 이를 다시 16배의 순차 forward로 계산하지 않는다. 데이터/전처리/행렬적합/메모리·장치에 따라 비용이 달라진다. 전체 wall time, 에너지, 총 GPU 비용과 RCTL의 손익분기 재학습 횟수는 미확인이다.

## 그대로 재현 baseline으로 표시하기 전에 확인할 코드 조건

| 관찰 | 근거와 의미 | 이번에 확정하지 않는 것 |
|---|---|---|
| 확률을 `CrossEntropyLoss` input에 전달 | data_shapley.py 155,187–190,337–338,363–364줄. prediction interface는 softmax 확률을 반환한다. [PyTorch 공식 API](https://docs.pytorch.org/docs/2.14/generated/torch.nn.CrossEntropyLoss.html)는 input logits를 기대한다. 이 경로의 손실은 `−p_y + log(sum(exp(p_c)))`이며 `−log(p_y)`와 다르다. | 계산이 불가능하다는 뜻은 아니다. surrogate 목적과 가중이 달라질 수 있다. 별도로 저장된 ROC AUC 수치를 자동으로 무효화하지 않는다. 실제 설치 버전은 미확인이다. |
| coalition 크기와 kernel의 p가 제한됨 | 118–181줄은 Bernoulli 포함확률 384/3072=0.125로 mask를 만들고 크기 256–512만 받는다. kernel식의 p 인자에는 3072가 아닌 최대 context512가 전달된다. cs=p일 때 weight0이다. 설계행렬 열은 후보3072개다. | 전체3072인 모든 coalition 게임의 정확 Shapley 추정량이라고 보장하지 않는다. 원 실행 행렬을 다시 적합하거나 저자 의도를 추정하지 않았다. |
| 작은 M에서도 WLS 결과를 저장 | 204–224줄은 intercept를 추가하고 M16부터 적합한다. 논문 규모에서 M<3073이면 행 수가 열 수보다 작다. 명시 rank/condition 검사나 M_factor≥1 검사는 없다. | M≥ntrain이라는 논문 조건만으로 full rank가 보장되지는 않는다. 실제 수치 rank·실패·계수의 오류를 실행 확인한 것은 아니다. |
| 단일 class coalition 검사가 sampling 단계에 없음 | 164–188줄은 크기만 재추출한다. classifier는 두 class 미만이면 ValueError를 낸다. | 저장된 15개 run에서 실제 이 문제가 발생했다는 뜻은 아니다. |
| 출력만으로 전체 실행을 복원하기 어려움 | entrypoint는 intermediate CSV와 hyperparameter pickle을 쓰지만 고정 tree에는 해당 실행의 모든 중간 배열·split row ID가 없다. run loop 밖 `np.save`는 마지막 객체의 test 배열만 저장하며 이름이 `.csv`로 끝나므로 `.npy`가 추가되는 경로다. | 원저자가 다른 위치에 결과를 보존하지 않았다고 단정하지 않는다. pickle이나 모델을 로드하지 않았다. |
| 환경과 가중치의 고정이 불완전 | requirements/pyproject는 tabpfn0.1.8과 일부 패키지만 고정하고 다수는 하한이다. interface의 누락 checkpoint 다운로드는 automl/TabPFN의 main URL이다. | 현재 환경에서 작동하는지, 실제 사용 가중치 hash가 무엇인지 미확인이다. |

일반 부모 helper `check_train_set_size`/`find_optimal_train_subset`는 `X_test` 성능으로 subset을 선택하는 별도 경로다. **현재 context entrypoint는 이 helper를 호출하지 않는다.** 본 Data Shapley 경로는 validation 손실로 값을 만들고 별도 test를 평가하므로, 다른 helper의 이름과 행동만으로 본 실험에 test leakage가 있었다고 단정하지 않는다. 재사용자가 helper를 추가한다면 역할을 다시 분리해야 한다.

## 논문의 다른 해석 도구를 함께 읽을 때

Table1은 feature effect(ICE/PD/ALE/Kernel SHAP/SA), feature importance(LOCO/SAGE), data valuation(LOO/Data Shapley/SA), 임상 의사결정 DCA, conformal prediction, counterfactual MOC를 구분한다. ALE는 논문에서 global인데 저장 README 표에서는 Local로 적혔다. 하나로 고쳐 합치지 않는다. SA의 context 입력·label에 대한 loss gradient L2 norm은 이번 WLS Data Shapley와 별도 방법이다. SAGE는 prediction 대신 empirical risk를 설명하고, DCA/CP는 다른 도구의 wrapper, MOC는 진화 다목적 탐색이다. 이들 모든 구현을 코드로 검수한 것은 아니다.

ICE/PD/ALE는 같은 context에서 grid별 query를 묶어 반복되는 context 처리비를 줄인다. §4.1/그림1은 25개 합성 자료(10 feature,1000관측), 7개 OpenML 이진 자료, 80/20 분할, 합성 feature level별5seed를 설명한다. 실제자료 grid는100이다. 이 PD runtime 개선을 Data Shapley 문맥 선택의 사전 비용 절감으로 옮기지 않는다. LOCO는 feature를 context/query 양쪽에서 빼는 비교이고, LOO는 context 관측 하나를 빼는 비교다.

Kernel SHAP §4.2/그림2는 feature 6개인 세 자료(strikes ID 770, delta_elevators ID 819, chscase_census6 ID 900), train 256/query 128, 25반복에서 근사오차를 평가한다. approximate M 6–160/L 1–25, exact M 6–1600을 비교한다. 비용 축은 token connections이며 실측 wall time/FLOPs가 아니다. 식2의 approximate 계산은 모든 query·imputation이 메모리에 들어가는 하한을 가정한다. 식3과 비교해 exact가 싸다는 논의는 ntrain≈ninf, L≥2 조건이고, 낮은 비용의 일부 chscase 설정에서는 approximate가 낫다는 본문 예외도 있다. 결론의 우위 표현을 모든 설정의 엄격한 지배로 읽지 않는다.

## 재사용과 다음 연구의 구별 기준

팀원이 재사용할 것은 원 X/y를 유지하는 context 선택 구조, validation/test 역할, 논문 규모와 debug 규모의 구분, 저장 AUC의 %p 단위, 선택 사전 비용과 고정 소스의 제약이다. 58번의 “TabPFN context 가치를 RCTL 학습 가치로 바로 사용하지 않는다”는 당시 판단은 유지한다.

새 제안은 선택 단위가 관측·시간 window·cell 중 무엇인지, 어떤 학습기의 어떤 손실을 줄이는지, 시간 분할과 정규화, 독립 비교군, 선택 비용을 포함한 총비용, 실제 RCTL 결과와 그 근거를 밝혀야 기존 안과 구별된다. 이 문서는 그러한 새 실험을 실행하라는 지시가 아니다.

출판본 본문, 나머지 IML 구현·노트북·wheel, checkpoint·원 데이터와 전체 run 중간물은 현재 범위 밖 미확인이다. SCott·SGD-as 원문과 나머지56/58 종합,59이후 기록, 전체 원본 변경/팀 접근/검색 검수도 남아 있다. [H047 검수](../verification/history-047.md) · [자료 manifest](../evidence/0056-0058-tabpfn-iml/manifest.json)
