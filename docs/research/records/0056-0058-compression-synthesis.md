# 56–58. 학습량을 줄이는 다섯 문헌과 재제안 전에 확인할 조건

56–58번의 결론은 **TabICLv2의 큰 예측 오차나 context 가치를 곧바로 RCTL 학습 표본 가치로 쓰는 안을 채택하지 않는다**는 것이었다. 자료 압축·표본추출 전체가 실패했다는 결론은 아니다. 다섯 문헌은 선택 대상, 점수를 계산하는 학습기, 유지하는 목적, 준비 비용이 서로 다르다. 이 차이를 지우면 이미 검토한 원리를 새 방법처럼 제안하거나 다른 모델의 이득을 RCTL의 이득으로 바꾸게 된다. [56 계획](../evidence/0056-0058-mae-sampling/originals/SRC-0021848.md.txt) · [58 판단](../evidence/0056-0058-mae-sampling/originals/SRC-0021898.md.txt)

이 페이지는 H045–H049의 원문 대조를 종합하고 누락된 수집 경로를 연결한다. 새 학습·추론·원 스크립트 실행·난수 생성은 0이다. 과거의 계획과 다음 행동은 역사적 기록으로 보존한다. [실제 읽은 범위](../sources/history-050.md) · [주장 검수](../verification/history-050.md)

## 세 기록이 한 판단으로 이어진 과정

| 기록 | 질문과 실제 수행 | 상태를 읽는 기준 |
|---|---|---|
| 56 | 실제 입력·정답 쌍을 유지하며 학습량을 줄일 수 있는지 검토. TimeDC·importance sampling·TabPFN IML을 먼저 지정하고 SCott·SGD-as를 직접 인접 연구로 추가 | 문헌 계획과 조건의 고정. 다섯 개의 새 모델 실험이 아님 |
| 57 | 같은 입력 세 개, θ=0, 정답 `[-1,-1,10]`에서 손실·gradient 평균과 분산을 유리수로 열거 | 저장 결과가 있는 산술 작업. 실제 통신 자료의 학습·예측 실험이 아님 |
| 58 | 원문·코드 관찰과 57의 반례를 연결하여 네 종류의 제안을 채택하지 않음 | 당시 제약 아래의 판단. 최종 Word 추천안이나 새로운 RCTL 방법의 완료가 아님 |

57의 손실은 `[1,1,10]`, θ 방향 gradient는 `[1,1,−1]`이다. 균등 추출과 loss 비례 추출에 각각 역확률 가중을 적용하면 평균 손실 4와 평균 gradient 1/3은 같다. 하지만 loss 비례의 손실 분산은 0으로 줄고 gradient 분산은 `8/9 → 121/45`, 즉 **121/40=3.025배**가 된다. [57 저장 결과](../evidence/0056-0058-mae-sampling/originals/SRC-0028241.json) · [계산 조건과 실행 증거](0056-0058-mae-sampling.md)

이 반례는 손실 추정 효율에서 학습 효율로 바로 넘어가는 일반적 논리를 반박한다. RCTL의 시간·예측 오차·압축 비율을 측정한 결과가 아니다. 다른 입력의 Jacobian과 실제 training-mode BatchNorm·dropout까지 이 세 고정 결과에 포함됐다고 볼 수도 없다.

## 무엇을 바꾸고 어떤 학습기에 대한 근거인가

| 방법과 상세 기록 | 바꾸는 대상 | 점수·목적이 속한 학습기 | 검토한 근거의 경계 |
|---|---|---|---|
| [Importance sampling, ICML 2018](0056-0058-mae-sampling.md) | 실제 표본의 추출 확률과 역확률 가중 | 현재 학습기의 gradient norm 상한 | 평균 gradient 보존과 효율적인 확률은 별도 조건. 다른 모델의 큰 loss를 같은 점수로 대체하지 않음 |
| [TimeDC, PVLDB 18(2)](0056-0058-timedc.md) | 작은 **합성** 시계열 자료 | 원 자료로 준비한 TSOperator expert의 표현·학습 경로 | 원 X/y 부분집합 선택과 다름. 교차 구조 평가가 있으나 각 구조의 원 자료 대비 보존율 표는 아님 |
| [TabPFN IML, arXiv v2](0056-0058-tabpfn-iml.md) | 실제 관측 중 TabPFN context | TabPFN의 validation 손실과 weighted surrogate | 별도 test에서 분류 AUC를 평가. RCTL 회귀 표본 가치나 cell 소속의 실증은 아님 |
| [SCott, ICML 2021](0056-0058-scott.md) | 같은 예측기의 학습 창을 뽑는 strata와 update | 가중 snapshot·같은 표본의 gradient 차이 | 한 학습기의 gradient 추정. 최종 예측기를 여러 cell 모델로 나누는 결정과 다름 |
| [SGD-as, arXiv v1](0056-0058-sgd-as.md) | 함께 뽑을 표본의 대응표 | 이진 logistic/SVM의 label·입력 내적 proxy | permutation이 평균을 유지하고 음의 공분산이 분산을 줄임. 두 조건을 합쳐 무조건 개선이라고 하지 않음 |

따라서 “sample을 묶는다”라는 말만으로 같은 연구라고 볼 수 없다. **cell의 소속**, **학습 창의 추출**, **PFN context**, **합성 자료**를 먼저 지정해야 한다. 반대로 시간대 strata나 반대 방향 표본 짝짓기에 Tab이라는 이름만 더한 것은 새로운 선택 원리를 입증하지 않는다. [58 §1·4](../evidence/0056-0058-mae-sampling/originals/SRC-0021898.md.txt)

## 공통으로 남는 조건과 각 방법의 예외

Importance sampling의 불편성은 양의 추출 확률과 올바른 역확률 가중으로 얻는다. 원문 §3.2의 norm 상한은 **현재 학습기**의 출력 gradient·활성값에 연결되고 학습 중 변한다. 같은 평균 목적을 유지한다는 사실이 TabICL의 loss 순위가 효율적인 추출 확률이라는 증거는 아니다. 원문의 이미지·sequence 분류에서의 유효 사례도 보존한다.

TimeDC는 실제 X/y를 그대로 남기는 당시 제약과 다르다. DDFM의 frequency라는 이름은 실제 연산을 생략하는 근거가 아니다. 주논문은 moving-average로 trend와 seasonal 표현을 분해하며, 이를 Fourier 변환이라고 바꾸어 설명하지 않는다. 합성 자료의 교차 구조 결과가 있다는 사실과, 원 자료 학습보다 일부 오차가 커지는 사실을 함께 읽어야 한다. 고정 코드의 X/y pairing·optimizer 연결·평가 구간 등에 남은 정적 관찰은 [상세 검토](0056-0058-timedc.md)에 있다. 이를 저자 실험 전체의 무효나 검증된 재현 baseline으로 바꾸지 않는다.

TabPFN IML의 Data Shapley는 무작위 context의 validation risk에 surrogate를 맞추는 방법이다. “exact retraining”이 모든 coalition과 모든 Shapley 값을 정확히 열거했다는 뜻은 아니다. 원문 규모는 후보 3,072개, 최종 context 512개, M=9,216이며, 별도 test 1,024개에서 ROC AUC를 평가한다. 저장 코드의 debug 기본 설정은 이 규모와 다르다. 다른 해석 도구의 query 묶기·PD 시간 절감도 Data Shapley 선택의 총비용 감소로 옮기지 않는다.

SCott의 strata 크기 가중·동일 표본에서의 두 gradient·수렴 가정과 실제 조기 종료 규칙은 모두 방법의 일부다. snapshot의 불편성을 모든 inner update의 조건부 불편성으로 일반화하지 않는다. 기본 SCott이 Exchange Rate의 일부 조건에서 SGD/SCSG보다 높은 손실을 보인 표의 반례도 남긴다. MAE·ReLU에 smooth 정리를 그대로 적용하거나, 논문의 Traffic을 이동통신 트래픽이라고 설명하지 않는다.

SGD-as의 greedy 대응표는 permutation을 만들지만 대칭인 서로소 쌍이나 모든 step의 음의 공분산을 보장하지 않는다. 고정 이진 label의 내적 조건과 현재 예측값에 따라 바뀌는 MAE residual 부호는 다르다. SVM의 non-smooth hinge 사례가 실제로 있으므로 “비미분 손실에서는 전부 사용할 수 없다”는 반대 방향의 단정도 피한다.

이 다섯 방법의 외부 실험·이론을 직접 RCTL 효과로 대체할 수는 없다. 당시에는 소속·표본 선택을 최종 RCTL의 손실이나 gradient에 맞추지 않는 독립성 조건도 있었다. 이는 **당시 문제의 제약**이다. 후속 연구가 다른 제약을 채택한다면 바뀐 질문과 평가 설계를 먼저 적어야 하며, 기존 조건에서 입증된 방법이라고 소급해서 기록하면 안 된다.

## 비용을 비교할 때의 분모

| 방법 | 원문에서 확인한 비용 단위·준비 단계 | 총비용으로 사용할 때 필요한 정보 |
|---|---|---|
| Importance sampling | 큰 후보 batch B의 추가 forward와 작은 batch b의 update; 이득이 작으면 균등 추출 유지 | 현재 학습기의 점수 산출·가중·전송·학습 비용. 같은 품질에 도달하는 총시간 |
| TimeDC | expert 준비, 압축, 합성 자료 학습이 별도 단계. Table 4는 **초/epoch** | 각 단계 epoch·종료 조건·준비비·후속 재학습 횟수 |
| TabPFN IML | M=9,216개 validation context 평가와 surrogate 적합. 논문은 거의 1만 forward 비용을 명시 | 모델 준비·전처리·ensemble·중간 test 평가·WLS·선택 후 사용까지의 실제 시간 |
| SCott | strata·snapshot 준비와 inner gradient 차이. Table 3은 MLP 0.5시간, N-BEATS 3시간의 학습 예산 | 전처리·튜닝을 포함한 같은 총예산인지, 각 optimizer의 설정과 품질 |
| SGD-as | 대응표의 사전 계산과 재사용. 실험 가로축은 Epoch | 실제 검색 구현·짝짓기 시간·재사용 횟수·학습과 평가 시간 |

TimeDC Weather의 22.39 / 4.31 / 35.26초는 압축 / 합성 자료 학습 / 원 자료 학습의 **각 한 epoch**다. 4.31과 35.26만으로 expert 준비부터 포함한 총비용 절감을 선언할 수 없다. TabPFN IML에서 3,072개 중 512개를 남긴 비율도 전체 계산량의 절감률은 아니다. [TimeDC Table 4](https://www.vldb.org/pvldb/vol18/p226-miao.pdf#page=10) · [TabPFN IML §4.3](https://arxiv.org/pdf/2403.10923v2#page=10)

SGD-as에서 n=35,000의 남은 후보를 매번 전부 직접 스캔하면 612,517,500번의 내적이 필요하다는 계산은 **조건부 산술**이다. 저자 구현의 실제 시간이나 필수 메모리 크기가 아니다. SCott의 점근 gradient 복잡도, IML의 논리 호출 수, TimeDC의 초/epoch를 같은 열의 속도 배수로 합치지 않는다.

팀의 총비용 기록은 `자료 처리 + 점수/strata/짝/합성 자료 준비 + 튜닝 + 본 학습 + 평가`를 구분해야 한다. 재사용 자산이라면 준비비와 사용 횟수를 함께 적는다. 실제 step·처리 행·모델 수와 wall time도 분리한다. 이전 RCTL의 조건별 값은 [33–35 기록](0033-0035-process-fit-gap.md)과 [56–58 산술 검수](0056-0058-mae-sampling.md)를 재사용한다.

## 수집 목록, 다운로드, 독해를 구분하기

이번에 연결한 [수집 스크립트](../evidence/0056-0058-compression-synthesis/originals/SRC-0022785.py.txt)는 repository의 main commit 응답을 받은 뒤 그 SHA로 tree와 선택 파일을 고정한다. tree의 blob 경로를 전부 기록하지만, 첫 README와 키워드에 맞는 Python 파일 최대 6개만 선택한다. 이 스크립트를 현재 다시 실행하지 않았다.

| 고정 저장소 | tree 전체 항목 | 그중 blob 경로 | 이 수집 로그의 다운로드 receipt | README·코드 / commit·tree metadata |
|---|---:|---:|---:|---:|
| TimeDC `6016968…` | 114 | 109 | 9 | 7 / 2 |
| TabPFN IML `7bd39bc…` | 112 | 93 | 6 | 4 / 2 |
| 합계 | 226 | 202 | 15 | 11 / 4 |

15건 모두에 HTTP 200이 기록돼 있으며, 각 크기·SHA-256을 현재 저장 파일과 대조했다. tree의 모든 필드·URL도 읽었다. **202개 경로를 조회한 것은 202개 파일을 내려받거나 본문을 읽은 것이 아니다.** 15건은 이 수집 단계의 receipt 수이며, 이후 별도로 받은 `process/tools.py`, 논문·이력 HTML·preview나 현재 아카이브의 보충 자료까지 포함한 총수도 아니다. [원 로그](../evidence/0056-0058-compression-synthesis/originals/SRC-0064456.json) · [수집 대조](../evidence/0056-0058-compression-synthesis/collection-check.json)

## 저장 자료의 현재 검토 범위와 남은 범위

`sources/training_compression_56/`에는 42개의 서로 다른 바이트 파일이 있고, 해당 원본과 같은 파일 경로는 원 inventory에서 85개다. 기본 2사본 외에 TabPFN IML PDF가 `related_work/11_Interpretable_TabPFN_Context_Valuation.pdf`에도 같은 바이트로 있다. 파일 경로 수를 독립 연구 수로 세지 않는다. 현재 해당 폴더의 목록과 저장 inventory 사이에서 추가·누락을 발견하지 못했다. 이는 전체 원본 루트의 최종 변경분 검사와는 별도다.

[42개 파일별 범위표](../evidence/0056-0058-compression-synthesis/packet-scope.json)는 다음 상태를 구분한다. 5개 주논문과 파생 TXT 5개, 코드·README 12개, preview 6개, JSON 11개를 해당 독해 기록에 연결했다. HTML 3개는 보이는 본문·서지·이력만 읽은 상태이며 전체 HTML 소스 독해로 표시하지 않는다. 이번에 두 tree JSON을 선택 필드 상태에서 전체 metadata 상태로 전환했지만, 연결된 모든 구현·논문을 읽었다는 뜻은 아니다.

이 밖에 문헌별로 남은 재현 공백은 다음과 같다.

| 자료 | 아직 확인하지 못한 범위 | 이 페이지에서 하지 않는 확대 해석 |
|---|---|---|
| Importance sampling | 보충 증명·저자 구현·raw run의 상세 대조 | 이론의 모든 상수·시간 보장·RCTL 성능을 독립 인증했다고 하지 않음 |
| TimeDC | 확장판·Appendix·Additional_experiment·별도 그림 및 실제 저자 실행 판본 | tree의 제목만으로 읽거나 실행한 자료로 바꾸지 않음 |
| TabPFN IML | 출판본 본문·나머지 IML 구현·checkpoint·원 자료 행·전체 run 중간물 | arXiv/현재 고정 코드/출판본을 같은 판본으로 통합하지 않음 |
| SCott | 정확한 구획·분할·seed·batch/K·정규화·원 run과 증명 전체 독립 대조 | 검토한 본문·부록·인쇄 표를 독립 재현 성공으로 바꾸지 않음 |
| SGD-as | 실제 학습률 수치·scaling·분할·seed·검색 구현·원 run·전처리 시간 | Epoch 축에서 준비비 포함 wall time 이득을 만들지 않음 |

저장 원본의 미열람 구간과 원 inventory 밖의 연결 자료는 따로 관리한다. 링크가 있다는 이유로 외부 repository 전체를 이미 보존한 원본처럼 세지 않는다. 반대로 아직 읽지 않은 저장 자료를 중복·제외로 돌리지 않는다. 이 종합으로 56/58의 모든 관련 경로와 전체 연구 아카이브가 완료됐다고 선언하지 않는다.

## 같은 질문을 다시 제안하기 전

새 제안에는 바꾸는 단위, 점수를 정의하는 학습기·손실, 유지하거나 바꾸는 목적, 시간 분할·정규화, 선택 비용을 포함한 총비용, 기존 안과 다른 직접 근거가 필요하다. 결과를 기록할 때에도 같은 평균 목적, 작은 gradient 분산, 빠른 전체 학습, 낮은 미래 오차, 좋은 cell 소속을 각각 구분한다.

당시 채택하지 않은 것은 큰 Tab loss 순위, TabPFN context 가치의 RCTL 대체, 기존 strata·antithetic sampling의 이름 변경, expert 비용을 뺀 압축 이득 주장이다. 기존 기록을 재사용하되 바뀐 조건과 새 증거를 명시하면 재검토할 질문과 단순 반복을 구별할 수 있다. 이후 59번 이후의 원문과 남은 고유 기록을 이어서 정리한다. [과거 시도 색인](../prior-attempts.md) · [검수와 한계](../verification/history-050.md)
