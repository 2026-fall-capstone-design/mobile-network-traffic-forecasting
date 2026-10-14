# 입력 미분으로 task 관계를 정하는 선행연구와 적용 조건

아카이브 H143은 과거 **원114(2026-09-26)**의 문헌·공식 구현 검토다. 입력 미분으로 관계를 표현한다는 원리와 실제 RCTL의 공유 학습 이득을 구분한다. 당시에는 새 추천안으로 채택하지 않았으며, 문헌 검토를 트래픽 성능 실험으로 세지 않는다.

[출처·읽은 구간](../sources/history-143.md) · [문헌 비교](../references/signed-input-gradients-and-task-relations.md) · [근거](../evidence/0143-signed-input-gradients-and-task-relations/README.md) · [주장 검수](../verification/history-143.md)

## 질문·실제 수행 범위

| 항목 | 원114에서 확인한 범위 |
|---|---|
| 질문 | 예측 함수의 입력 반응으로 cell 관계를 정하는 원리가 새로우며, RCTL 학습 전 소속 결정에 적용될 수 있는가? |
| 방법 | SRDML 저자본·공식 서지·고정 commit 코드의 수식, 미분 좌표, 관계 가중치 갱신과 적용 조건을 정적으로 대조 |
| 실제 실행 | 당시 기록은 모델 호출·fit·수치 실험·RCTL 학습 0을 명시. 이번에도 원 연구 코드 실행/import·모델 생성 0 |
| 트래픽 데이터·시간 분할·정규화·seed | 이번 문헌 검토의 새 실험 항목으로는 해당 없음. 논문/demo의 설정은 아래 별도로 표시 |
| 비교군·최종 RCTL MAE | 새 측정 없음. 저자 benchmark를 우리 소속 또는 최종 예측 성능으로 옮기지 않음 |
| 비용·원장 | 모델 비용 0으로 기록. 문헌 획득·검토의 실행 시간·peak RSS는 미기록. 원장 유지 진술과 전후 판본의 독립 대조를 구별 |
| 당시 판단·후속 | 입력 미분의 부호 자체를 차별점으로 세지 않음. 원115의 task grouping 상세 검토는 후속 범위 |

## 같은 미분·같은 함수·같이 학습할 이득

논문의 정리 1은 함수족과 기준값, 정의역 전체의 미분 등식을 다룬다. 일부 입력에서 비슷한 반응을 얻었다는 관측은 그 정리와 다르다. `f_A(x)=x+1`, `f_B(x)=x+100`은 같은 미분과 다른 출력값의 기호 예다. 독립 데이터나 새 모델로 측정한 결과가 아니다.

SRDML의 관계는 공통 표현과 task별 head를 학습하는 규제항이다. RCTL 이전에 고정 소속을 만들려면 미분의 좌표·입력 지지집합·출력 의미를 먼저 정하고, 그 결정이 실제 공유 학습에 필요한 이유를 별도로 설명해야 한다.

## 논문과 공개 합성 demo의 설정

| 항목 | 소장 저자본 §5.1 | 고정 commit의 synthetic_train.py |
|---|---|
| task 수 / 입력 차원 | 12 / 20 | 12 / 20 |
| task당 sample | 100 | 10 |
| base 계수 | 서로 다른 10차원 영역의 `(1;0)`와 `(0;1)` | 전체 20좌표의 양·음 상수 벡터; 배수 1·2·3을 각각 두 task에 사용 |
| 입력 분포 | 평균 벡터 η_i, 공분산 I인 정규분포 | mean 0.5, std 1인 정규분포로 공통 X 생성 |
| label noise | `N(0,0.1·I)`로 표기 | 정규분포 std 인자 0.01 |
| demo test / seed / 반복 | 이 표의 코드 실행 조건과 동일함을 검증하지 않음 | test_size 40 / TensorFlow seed 111 / 150 반복 |
| demo optimizer / 관계항 | 논문 전체 실험의 완전한 재현 설정은 미확보 | SGD 0.01 두 개; `i>10`에서 μ=1 |

위 표는 정적 설정 비교다. 논문 수치 표의 재현 성공, 새 트래픽 실험, RCTL의 권장 설정을 뜻하지 않는다. CIFAR 코드의 Z=1 공간 합, batch 200, epoch 30 등도 그 코드의 기본값으로만 읽는다.

## 범위·서지

<a id="c01"></a>**C01.** 원114는 2026-09-26의 문헌·공식 구현·적용 조건 검토다. 원112의 시각 보정 실패와 원113의 고정 K·크기 제약 진단은 별도 기록이며, 이를 다시 실행한 단계가 아니다. [출처](../sources/history-143.md) — [SRC-0020874 · lines3,7,23](../sources/history-143.md#src-0020874) · [SRC-0020873 · lines45-47](../sources/history-143.md#src-0020873)

<a id="c02"></a>**C02.** 당시 입력 반응 방향을 새 추천안으로 채택하지 않았다. 입력 미분으로 task 관계를 나타내는 원리가 선행연구에 있고, 고정 TabICLv2 probe라는 차이만으로 최종 RCTL의 자료 공유 이득이 설명되지 않는다는 범위의 판단이다. 모든 미분 기반 방법의 불가능성을 판정한 것이 아니다. [출처](../sources/history-143.md) — [SRC-0020873 · lines3,33-35](../sources/history-143.md#src-0020873) · [SRC-0020874 · lines19-21](../sources/history-143.md#src-0020874)

<a id="c03"></a>**C03.** Bai·Zhao의 Saliency-Regularized Deep Multi-Task Learning은 KDD 2022 논문으로 연결한다. arXiv 2207.01117의 제출일은 2022-07-03이며 v1과 DOI 10.1145/3534678.3539442를 공식 arXiv 서지와 고정 코드 README에 대조했다. 현재 웹 수집일을 출판 연도로 쓰지 않는다. [출처](../sources/history-143.md) — [SRC-0020873 · line7](../sources/history-143.md#src-0020873) · [SRC-0063917 · lines3,27-33](../sources/history-143.md#src-0063917)

<a id="c04"></a>**C04.** 검토 대상 저자본은 11쪽 PDF다. 첫 페이지의 DOI는 placeholder이며 공식 서지 DOI와 구별한다. arXiv 페이지의 Comments에 적힌 10 pages와 소장 PDF의 실제 11쪽을 같은 파일의 쪽수 확인으로 합치지 않으며, arXiv PDF나 ACM 출판본을 이번에 내려받아 대조했다고 하지 않는다. [출처](../sources/history-143.md) — [SRC-0063918 · metadata:physical_page_count11;page1bibliography_via_verified_text](../sources/history-143.md#src-0063918) · [SRC-0063919 · lines37-57](../sources/history-143.md#src-0063919) · [SRC-0063921 · lines40-49,63](../sources/history-143.md#src-0063921)

<a id="c05"></a>**C05.** 공식 코드의 검토 판본은 commit b65d6da39a2f92491f0982790a9bd3a3e2d5b9bf다. 저장 commit 응답의 날짜는 2023-09-26이며 README 변경 commit이다. 현재 해당 고정 commit의 README·합성 코드·CIFAR 코드를 읽기 전용 GitHub API로 다시 받아 소장 바이트와 동일함을 확인했다. 이것은 코드 판본 확인이며 논문 실험 재현이 아니다. [출처](../sources/history-143.md) — [SRC-0063920 · /sha,/commit/author/date,/commit/message](../sources/history-143.md#src-0063920) · [SRC-0063928 · /tree:README.md,synthetic_train.py,train.py](../sources/history-143.md#src-0063928) · [SRC-0063921 · lines22-37,46](../sources/history-143.md#src-0063921)

<a id="c06"></a>**C06.** 원 manifest는 Python의 인증서 검증 실패 후 PowerShell의 기본 인증서 검증을 이용해 저자 PDF를 정상 확보했고 우회하지 않았다고 기록한다. 이는 당시 획득 기록의 진술이다. 현재는 소장 PDF·추출문·그림의 해시와 내용 대응을 확인했으며 그 다운로드 과정을 새로 재현하지 않았다. [출처](../sources/history-143.md) — [SRC-0063921 · lines47,65-69](../sources/history-143.md#src-0063921) · [SRC-0020873 · line45](../sources/history-143.md#src-0020873)

## 목적식·미분

<a id="c07"></a>**C07.** SRDML은 공통 표현 h와 task별 head f_t를 합성한 g_t=f_t∘h를 사용한다. 공유 표현과 task 관계를 학습하는 다중 과제 학습 구조로, RCTL 학습 전에 고정 cell 소속을 산출하는 군집화 절차와 결정 대상이 다르다. [출처](../sources/history-143.md) — [SRC-0063919 · lines212-242,385-396](../sources/history-143.md#src-0063919) · [SRC-0063918 · pages3-4,Figure3](../sources/history-143.md#src-0063918) · [SRC-0020873 · line11](../sources/history-143.md#src-0020873)

<a id="c08"></a>**C08.** §3.1과 공개 합성 코드에서는 같은 입력을 task별 함수에 넣어 반응을 비교한다. 논문 Appendix D는 서로 다른 task 분포 μ_t를 포함하는 더 일반적인 정리 표기를 설명하므로, 논문 전체가 오직 동일 분포만 허용한다고 제한하지 않는다. 그 설명이 서로 다른 cell의 좌표·관측 지지집합을 자동 정렬하는 구현을 제공하는 것은 아니다. [출처](../sources/history-143.md) — [SRC-0063919 · lines223-242,1148-1154](../sources/history-143.md#src-0063919) · [SRC-0063926 · lines41-54,114-126](../sources/history-143.md#src-0063926) · [SRC-0063918 · pages3,11](../sources/history-143.md#src-0063918)

<a id="c09"></a>**C09.** 관계항에서 읽는 미분은 head 예측 출력의 입력 또는 공유 feature map에 대한 미분이다. 학습 loss의 파라미터 gradient와 구별한다. CIFAR 코드의 feature map 미분을 raw 입력의 모든 좌표에 대한 미분으로 바꾸어 부르지 않는다. [출처](../sources/history-143.md) — [SRC-0063919 · lines313-335](../sources/history-143.md#src-0063919) · [SRC-0063926 · lines114-126,137-140](../sources/history-143.md#src-0063926) · [SRC-0063927 · lines76-93,102-107](../sources/history-143.md#src-0063927)

<a id="c10"></a>**C10.** 식(4)는 task별 예측 loss와 λΣ_{i<j}(ω_ij/W)dist(∇_A f_i,∇_A f_j)를 함께 최소화하며 W=Σ_{i<j}ω_ij다. 관계 가중치는 학습 대상이다. 본문은 정규화 후 식(3)의 가중치 합 하한이 엄격히 보장되지 않는다고 적는다. 이 연속 관계 행렬을 고정 K의 이산 소속 결과로 읽지 않는다. [출처](../sources/history-143.md) — [SRC-0063919 · lines321-384](../sources/history-143.md#src-0063919) · [SRC-0063918 · page4,Eq2-4](../sources/history-143.md#src-0063918)

<a id="c11"></a>**C11.** synthetic_train.py는 동일한 temp_x에서 task별 출력 gradient를 구한 뒤 두 부호 있는 gradient 벡터의 차이에 L1 norm을 적용한다. 먼저 각 gradient의 절댓값으로 중요도를 만든 뒤 비교하거나 sign만 남기는 코드가 아니다. 부호와 크기가 모두 비교에 남는다. [출처](../sources/history-143.md) — [SRC-0063926 · lines114-126](../sources/history-143.md#src-0063926) · [SRC-0020873 · line17](../sources/history-143.md#src-0020873)

<a id="c12"></a>**C12.** train.py는 공유 feature map에서 task별 head 출력 gradient g_t를 구하고 reduce_sum(g_t,[0,1,2])/Z를 비교 벡터로 사용한다. 소장 코드의 Z 기본값은 1이므로 실제 표기는 공간 합이며 공간 원소 수로 나눈 평균이라고 고쳐 쓰지 않는다. 이 벡터 쌍의 L1 차이에 정규화한 관계 가중치를 곱한다. [출처](../sources/history-143.md) — [SRC-0063927 · lines33-34,76-93](../sources/history-143.md#src-0063927) · [SRC-0020873 · line18](../sources/history-143.md#src-0020873)

<a id="c13"></a>**C13.** 합성 코드의 예측 loss와 미분 관계항은 같은 목적식에 들어가며 모델 가중치와 관계 가중치를 SGD로 갱신하는 구조다. 코드에서는 갱신 뒤 관계 가중치에 ReLU를 적용한다. 현재 아카이브는 그 갱신이나 gradient 계산을 실행하지 않았다. [출처](../sources/history-143.md) — [SRC-0063926 · lines99-143](../sources/history-143.md#src-0063926)

<a id="c14"></a>**C14.** CIFAR 코드도 예측 loss와 관계 규제항으로 모델 두 부분을 갱신하고, 관계 가중치는 별도로 계산한 gradient로 Adam을 사용해 갱신한다. 모델을 고정한 채 사전에 clustering 점수만 읽는 구현으로 취급하지 않는다. 실제 학습 로그나 재현 성능을 확보한 상태가 아니다. [출처](../sources/history-143.md) — [SRC-0063927 · lines95-123](../sources/history-143.md#src-0063927) · [SRC-0063921 · lines48,62](../sources/history-143.md#src-0063921)

## 정리·증명

<a id="c15"></a>**C15.** 정리 1의 함수족은 C1이면서 f(0)=0인 함수이며, 모든 x∈X에서의 미분 일치와 함수 일치를 다룬다. 일부 query에서 가까운 gradient를 관찰한 조건을 이 전역적 등식과 같게 취급하지 않는다. [출처](../sources/history-143.md) — [SRC-0063919 · lines275-288,990-1002](../sources/history-143.md#src-0063919) · [SRC-0063918 · pages3,10](../sources/history-143.md#src-0063918) · [SRC-0020873 · lines13,27](../sources/history-143.md#src-0020873)

<a id="c16"></a>**C16.** 같은 미분만으로 함수 높이가 같아지지는 않는다. 원114의 f_A(x)=x+1, f_B(x)=x+100 예시는 미분은 같아도 출력값이 다른 경우다. 연결된 정의역에서는 한 공통 기준값이 추가로 필요하고, 끊어진 정의역에서는 연결 성분마다 기준이 필요하다. Appendix A.1의 open set 표기만으로 임의의 끊어진 정의역까지 등식을 보장한다고 읽지 않는다. 이는 적용 조건 설명이며 새 정리가 아니다. [출처](../sources/history-143.md) — [SRC-0020873 · line27](../sources/history-143.md#src-0020873) · [SRC-0063919 · lines990-1002](../sources/history-143.md#src-0063919) · [SRC-0063918 · page10,A1](../sources/history-143.md#src-0063918)

<a id="c17"></a>**C17.** 정리 2는 제한된 함수족의 경험위험 최적해와 기대위험 최적해 사이의 차이를 다루는 일반화 오차 bound다. loss의 범위·Lipschitz 조건, 표현 함수족과 task 관계 그래프 등이 등장한다. 관측된 gradient 유사도만으로 UPC 소속 변경이나 RCTL MAE 개선이 보장된다고 옮기지 않는다. [출처](../sources/history-143.md) — [SRC-0063919 · lines403-514](../sources/history-143.md#src-0063919) · [SRC-0063918 · pages4-5,Eq5-11](../sources/history-143.md#src-0063918)

<a id="c18"></a>**C18.** 소장 저자본 Appendix A.2에는 정리 2 전체 증명을 외부 링크로 옮겼다는 문장과 미완성 put link 표기가 남아 있다. 이 판본에서 전체 증명을 확인했다고 하지 않는다. 이는 확보한 판본의 근거 공백이며 모든 논문 판본의 증명이 없다는 주장이나 저자 실험의 반박이 아니다. [출처](../sources/history-143.md) — [SRC-0063919 · lines1003-1065](../sources/history-143.md#src-0063919) · [SRC-0063918 · page10,A2](../sources/history-143.md#src-0063918) · [SRC-0020873 · line13](../sources/history-143.md#src-0020873)

<a id="c19"></a>**C19.** Appendix D는 유한 표본으로 학습한 모형과 이론적 최적 모형의 오차 차이를 설명하고, 동일한 task 분포가 정리 2의 특수 경우라고 서술한다. 그 범위를 cell별 입력 이력과 Tab context가 다른 현재 절차의 독립적인 일반화 보장으로 확대하지 않는다. [출처](../sources/history-143.md) — [SRC-0063919 · lines1140-1154](../sources/history-143.md#src-0063919) · [SRC-0063918 · page11,D](../sources/history-143.md#src-0063918)

<a id="c20"></a>**C20.** 항등 표현과 선형 task 함수에서는 입력 gradient가 기울기 계수와 연결된다. 따라서 부호 있는 입력 미분의 관계라는 설명만으로 알려진 계수·task 관계 학습과 다른 새 원리를 입증했다고 보지 않는다. 이 연결을 모든 비선형 함수나 RCTL 성능의 등가성으로 확장하지 않는다. [출처](../sources/history-143.md) — [SRC-0063919 · lines1066-1078](../sources/history-143.md#src-0063919) · [SRC-0063926 · lines24-39,57-86,114-126](../sources/history-143.md#src-0063926) · [SRC-0020873 · line17](../sources/history-143.md#src-0020873)

## 설정·미실행

<a id="c21"></a>**C21.** 논문 §5.1의 합성 설정은 task 12개·task당 sample 100개·입력 20차원이며 base 벡터는 서로 다른 10차원 영역에 놓인 (1;0)와 (0;1)다. 공개 합성 코드의 기본값은 task 12개·sample 10개·20차원이며 base는 전체 좌표의 양·음 상수 벡터다. 동일한 합성 데이터 설정으로 기록하지 않는다. [출처](../sources/history-143.md) — [SRC-0063919 · lines558-600,1092-1124](../sources/history-143.md#src-0063919) · [SRC-0063918 · pages5,11](../sources/history-143.md#src-0063918) · [SRC-0063926 · lines14-54](../sources/history-143.md#src-0063926)

<a id="c22"></a>**C22.** 합성 demo 코드에는 TensorFlow seed 111, 입력 Normal(mean 0.5,std 1), label noise Normal(std 0.01), test_size 40, 반복 150, SGD learning_rate 0.01 두 개가 적혀 있다. i>10일 때 μ=1을 설정한다. 이는 고정 commit의 코드 기본값이며 우리 트래픽 실험의 seed·분할·정규화 또는 논문 표 재현 설정이 아니다. NumPy 전체 seed나 소장 실행 로그는 확인되지 않았다. [출처](../sources/history-143.md) — [SRC-0063926 · lines14-54,99-143,152-172](../sources/history-143.md#src-0063926)

<a id="c23"></a>**C23.** CIFAR demo 코드의 task 수 10, train_size 2000, test_size 10000, epoch 30, batch 200, μ 0.1, Z 1과 pretrained fork_M1/fork_M2 경로를 보존한다. 데이터 준비 코드·pretraining 본문은 이번 원114 packet에 없고 실행하지 않았다. 코드 설정을 RCTL의 권장 epoch·batch·비용으로 전용하지 않는다. [출처](../sources/history-143.md) — [SRC-0063927 · lines10-53](../sources/history-143.md#src-0063927) · [SRC-0063928 · /tree:generator_cifar10.py,pretrain.py](../sources/history-143.md#src-0063928)

<a id="c24"></a>**C24.** README가 적은 시험 환경은 Windows·Spyder/Anaconda·Python 3.8·TensorFlow-gpu x2.0이다. 이 문구를 모든 패키지의 정확한 lockfile이나 원114가 모델을 실행한 환경으로 취급하지 않는다. 논문 저자 환경의 Xeon W-2123·32 GB·Quadro RTX 5000도 현재 정리용 runtime이나 우리 실험 비용 측정과 다르다. [출처](../sources/history-143.md) — [SRC-0063917 · line9](../sources/history-143.md#src-0063917) · [SRC-0063919 · lines551-557](../sources/history-143.md#src-0063919) · [SRC-0063918 · page5](../sources/history-143.md#src-0063918)

<a id="c25"></a>**C25.** 논문에는 합성 회귀와 CIFAR-MTL·CelebA·COCO의 image task 결과가 있다. 이 저자 결과를 네트워크 트래픽의 사전 cell clustering, TabICLv2 직접 예측, 소속 점수 또는 최종 RCTL 성능으로 바꾸어 인용하지 않는다. 공식 코드를 읽고 판본을 확인한 상태와 전체 실험 재현은 구별한다. [출처](../sources/history-143.md) — [SRC-0063919 · lines551-665,692-809](../sources/history-143.md#src-0063919) · [SRC-0020873 · lines11,15,19,45](../sources/history-143.md#src-0020873)

## 현재 적용

<a id="c26"></a>**C26.** 현재 cell들은 같은 시각에도 최근 lag 입력이 다르다는 원114의 문제를 유지한다. 관측 입력들을 잇는 차분에는 여러 특징 변화가 함께 들어 있고, 시간 sin/cos·평균 등 파생 열을 독립 조작하면 실제 이력에서 만들어지지 않는 입력일 수 있다. 이번 검토에서 그런 probe를 새로 계산하지 않았다. [출처](../sources/history-143.md) — [SRC-0020873 · line29](../sources/history-143.md#src-0020873) · [SRC-0020874 · lines7,19](../sources/history-143.md#src-0020874)

<a id="c27"></a>**C27.** TabICLv2의 점 예측이 정확하다는 근거만으로 입력 미분도 정확하거나 서로 다른 context의 내부 표현 좌표가 비교 가능하다고 결론 내리지 않는다. 미분의 부호를 유지하는 것만으로 이러한 좌표·정규화·출력 의미의 조건이 충족되지는 않는다. [출처](../sources/history-143.md) — [SRC-0020873 · line31](../sources/history-143.md#src-0020873) · [SRC-0020874 · line19](../sources/history-143.md#src-0020874)

<a id="c28"></a>**C28.** SRDML의 관계는 그 규제항을 받는 실제 학습기와 함께 정해진다. 다른 고정 계산기로 RCTL 학습 전에 관계를 추정하는 설계는 가능하지만, 그 소속에서 RCTL을 함께 학습할 때의 이득은 별도로 확인할 대상이다. 함수 반응이 가깝다는 사실만으로 실제 공유 학습 이득을 입증했다고 하지 않는다. [출처](../sources/history-143.md) — [SRC-0020873 · lines11,33](../sources/history-143.md#src-0020873) · [SRC-0000135 · lines33-35](../sources/history-143.md#src-0000135)

<a id="c29"></a>**C29.** 당시에는 입력 미분의 부호 자체를 새 차별점으로 세지 않았고, 설명된 새 자료 공유 결정이 없는 상태에서 미분 추론·보조 loss·attention 모듈을 추가하지 않았다. 원76의 반응 증류와 원78의 task 표현·전이 점수 검토를 관련 과거 이력으로 연결한다. 이는 원114 당시 판단이며 새 모델 실행 지시가 아니다. [출처](../sources/history-143.md) — [SRC-0020873 · line35](../sources/history-143.md#src-0020873) · [SRC-0020874 · lines7,19-23](../sources/history-143.md#src-0020874)

## 중복·후속·보존

<a id="c30"></a>**C30.** 잔차 동시 상관 방향은 원114가 상세 08·09와 Maharaj·Inder 1999의 disturbance covariance pooling을 재참조한 경로다. 원114는 새 계산을 하지 않았으며 기존 Tab 잔차 상관 순위의 기간 간 불안정성을 재인용했다. 이번 묶음은 그 과거 결과를 새로 재계산하거나 모든 잔차 기반 방법을 기각하지 않았다. [출처](../sources/history-143.md) — [SRC-0020873 · line39](../sources/history-143.md#src-0020873)

<a id="c31"></a>**C31.** Towards Principled Task Grouping for Multi-Task Learning은 원114 당시 제목·서지를 탐색한 후속 검토 대상이다. 상세 학습기·입력·정답·추가 적합과 정리의 적용 범위를 원115에서 확인하기로 했다. 제목의 principled를 타당성의 근거로 쓰거나 원114에서 상세 방법 검토가 완료된 것으로 소급하지 않는다. [출처](../sources/history-143.md) — [SRC-0020873 · line41](../sources/history-143.md#src-0020873) · [SRC-0020872 · /next_plan](../sources/history-143.md#src-0020872) · [SRC-0063921 · line77](../sources/history-143.md#src-0063921)

<a id="c32"></a>**C32.** 원114의 plan·findings·verification 기록은 모델 호출·fit·RCTL 학습·수치 실험 0과 원장·상한 유지 상태를 기록하고, manifest도 모델 실행 false를 기록한다. 이는 당시 수행 범위의 일치하는 진술이며, 원114 전후의 별도 원장 두 판본을 확보해 모든 계정 값을 독립 대조한 상태는 아니다. 현재 원본 보호 파일 6개의 불변 검사는 역사적 원장 유지 증명의 대체가 아니다. [출처](../sources/history-143.md) — [SRC-0020874 · line23](../sources/history-143.md#src-0020874) · [SRC-0020873 · line45](../sources/history-143.md#src-0020873) · [SRC-0020872 · /ledger_unchanged_during_114,/models_executed](../sources/history-143.md#src-0020872) · [SRC-0063921 · /models_executed](../sources/history-143.md#src-0063921)

<a id="c33"></a>**C33.** 원114의 최종 추천안과 최종 Word는 당시 미완료로 기록됐다. 원112의 실제 실패, 원113의 내부 조건 진단, 원114의 문헌상 중복 확인을 하나의 새 실험이나 최종 채택 결론으로 합치지 않는다. 후속 연구와 전체 아카이브 정리도 현재 미완료다. [출처](../sources/history-143.md) — [SRC-0020873 · line47](../sources/history-143.md#src-0020873) · [SRC-0020872 · /final_recommendation_complete](../sources/history-143.md#src-0020872)

<a id="c34"></a>**C34.** 이번 첫 읽기는 16개 SHA 그룹·16개 원본 경로에 연결된 원문 12개 1719행과 원 PNG 3개이며, 소장 TXT 1154행의 비어 있지 않은 1133행은 현재 PDF 재추출문과 PAGE 표지·빈줄만 제외하고 정확히 같다. 기존 PNG 3·4·10쪽은 현재 PDF의 새 120dpi 렌더와 바이트·픽셀이 같고, PDF 5·11쪽도 직접 보았다. 전체 PDF 11쪽의 시각 검토나 새 독립 연구자 검증을 주장하지 않으며, 현재 모델 실행·원code import는 0이다. [출처](../sources/history-143.md) — [SRC-0063918 · selected_pages3,4,5,10,11](../sources/history-143.md#src-0063918) · [SRC-0063919 · lines1-1154; content_verified_against_current_PDF](../sources/history-143.md#src-0063919) · [SRC-0063922 · whole_image](../sources/history-143.md#src-0063922) · [SRC-0063923 · whole_image](../sources/history-143.md#src-0063923) · [SRC-0063924 · whole_image](../sources/history-143.md#src-0063924)

## 재사용과 재검토 조건

[원76 반응 전달](0076-response-transfer-audit.md), [원78 Task2Vec](0080-task2vec-task-and-output-sharing.md), [원113의 조건 진단](0142-fixed-k-and-unrestricted-cluster-sizes.md)과 함께 조회한다. 잔차 상관 재진입은 원114의 기존08·09 재참조로 기록하며 이번에 새 성능 실험으로 늘리지 않는다.

새 설계에서는 미분의 대상·입력 좌표·정규화·공통 입력 지지집합·함수 기준값·Tab context의 판본·추가 적합 허용 여부와 비용을 명시해야 한다. 실제 학습기와 공유 대상이 바뀌면 같은 정보를 받는 비교군도 정해야 한다. 이는 과거 연구를 찾는 안내이며 새 학습 실행의 승인이나 실행 기록이 아니다.

원115 이후, PDF 남은 시각 요소와 benchmark 세부 검수, 옛 개정본·다른 문서 형식·긴 root 기록·전체 통합·팀 접근·최종 원본 변경분·대표 질문 검색 검수는 계속된다. 이 기록이나 후속 PR 하나로 전체 Goal 완료를 선언하지 않는다.
