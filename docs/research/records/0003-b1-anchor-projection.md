# 03 — 대표 상태의 예측을 옮긴 B1과 입력 축약 실패

2026-09-25 초기 설계 흐름의 기록이다. [02 계획](0001-0002-initial-design.md)을 실제 16cell에서 실행한 B1은 **직접 Tab median보다 대표 입력의 예측을 옮긴 값의 오차가 컸고, 최근값 수준을 복원해도 격차가 남았다.** 03·04는 이 후보에 RCTL을 연결하지 않고 [B2의 실제 query 방식](0004-0007-b2-observed-risk.md)으로 바꿨다고 기록한다. 이는 입력 축약 후보의 판단이며 모든 Tab clustering의 기각은 아니다. [03 원문](../evidence/0003-0007/originals/SRC-0020824.md.txt), [04 원문](../evidence/0003-0007/originals/SRC-0020825.md.txt)

## 질문과 실제 수행

각 cell의 조건부 분포에서 공통 예측값을 쓸 때 증가하는 절대손실을 추정하면 좋은 소속을 만들 수 있는지 물었다. 공통 상태를 대표하는 실제 입력 64개를 정하고, 그 입력에서 얻은 분포로 cell별 위험함수를 만들었다. 같은 상태의 실제 query에도 대표 입력의 예측을 옮겨 쓰는 과정이 충분히 정확한지가 핵심 전제였다.

저장 파일에는 16개 Tab context의 전체 17,408query 예측, 네 위험함수 변형의 소속·병합 이력, PCC/random/교차오차 profile 비교, cell별 직접·대표 예측 오차가 있다. 이후 03은 저장 분위수에 최근값 차이를 더하는 산술 진단을 했다. 다른 partition 생성이나 분포 차이 자체를 성능 성공으로 세지 않았다. [실행 코드](../evidence/0003-0007/originals/SRC-0023116.py.txt), [결과](../evidence/0003-0007/originals/SRC-0023604.json), [추가 진단 코드](../evidence/0003-0007/originals/SRC-0023041.py.txt)

## 자료와 설정

| 항목 | 실행 근거에서 확인한 조건 |
|---|---|
| 자료 | Milan 가공 H5의 시간별 internet activity, 채널2. [초기 자료 출처](0001-0002-initial-design.md)의 32cell 중 고정16개 |
| cell ID | 3737, 3745, 3753, 3765, 4537, 4545, 4553, 4565, 5337, 5345, 5353, 5365, 6137, 6145, 6153, 6165 |
| 정규화 | 각 cell 원자료 시점0–671의 평균으로 나눔. cell별 정규화 MAE를 같은 비중으로 평균 |
| context | target168–671, cell당504행. [초기 특징](0001-0002-initial-design.md)의 최근8값·lag24/168·24시간 평균/표준편차·달력4열, 총16열 |
| 상태 | context만으로 StandardScaler와 KMeans64, n_init5, seed20260925. 각 중심에 가장 가까운 실제 context행을 anchor로 선택 |
| query | 공통 anchor64개 + 각16cell의672–839에서 rint(linspace)로 택한64개씩, 총1088행/context |
| Tab | 경로상 v2-20260212 regressor, ensemble1, batch_size1, CPU, seed20260925, n_jobs1, AMP/FA3/offload/자동다운로드False |
| 분포 | 129 midpoint 분위수 `(j+0.5)/129`; 같은 호출의 median·mean도 저장. native999개 전체와 구분 |
| 비교 | KNN32, median만, median/IQR uniform, PCC-balanced, random-balanced, 교차 MAE profile의 cosine/average-linkage |
| 소속 | K4, disjoint pair 병합16→8→4. 각 위험함수 변형에서148쌍 점수·12병합, 최종4cell씩4group |

코드는 시작 시 torch threads4/inter-op2와 BLAS4를 설정하지만 estimator에는 n_jobs1을 준다. 호출 중 실효 스레드 수를 추적한 근거는 이 묶음에 없다. 경로상 checkpoint와 초기 자산 안내는 연결되나 B1의 봉인 JSON은 결과·02계획·실행 코드의 해시만 담는다. 실행 시점의 전체 패키지·가중치 환경을 재현했다고 주장하지 않는다. [B1 봉인 해시](../evidence/0003-0007/originals/SRC-0023597.json), [대형 자산 안내](../evidence/0001-0002/README.md)

cell별 context의 상태 빈도를 가중치로 유지한다. 상태별 action257개는 Tab anchor 분위수와 KNN anchor 분위수의 공통 범위에서 만든다. 각 group 비용은 cell별 손실표를 더하고 각 상태에서 action 최소값을 골라 합친 것이다. 이 비용은 추정 분포의 공통 예측값에 대한 것이며 pooled Tab 재추론이나 실제 RCTL risk가 아니다. PCC는 정규화 전 첫672행 상관, random은 고정 seed 균형 배정이다. 교차오차 profile은 N² 비교군으로서 서로 다른 query 입력을 포함하며, 새 RCTL 결과가 아니다.

## 관측된 오차와 후속 진단

같은 16cell×64query의 정규화 척도다. 소속별 RCTL MAE와 섞지 않는다.

| 저장 예측을 평가한 방식 | mean cell MAE |
|---|---:|
| 각 실제 query의 직접 Tab median | 0.072613972472 |
| 해당 상태 anchor의 median으로 대체 | 0.140444335062 |
| anchor 예측에 실제 query와 anchor의 최근값 차이 추가 | 0.125104261795 |

대표 예측의 MAE는 직접 예측보다 약 93.41% 컸다. 수준 복원 후에도 약 72.29% 컸다. direct conditional quantile과의 평균 절대 차이, 즉 같은 분위수 격자의 W1 근사는 0.124628336169에서 0.119140150957로 줄었으나 차이가 남았다. 수준 이동은 당시 소속이나 같은 anchor의 cell 간 상대 비교를 바꾸는 새 clustering으로 보고되지 않았다. [16cell별 진단과 평균](../evidence/0003-0007/originals/SRC-0023598.json)

단순 분포의 손실 합·최적 action, 같은 median에 spread만 다른 경우의 추가 median 손실0, `[1,1,1.015]`에서 pooled median1과 세 번째 오차0.015도 저장돼 있다. 검산은 이 산술 일관성을 확인했으며 실제 traffic/RCTL 효과의 증거로 올리지 않았다. `[0,1]` 사례의 저장 최적 action0.06은 최소손실1을 달성하는 여러 점 중 하나여서 0으로 임의 정정하지 않았다. [유한 분포 산술 확인](../evidence/0003-0007/originals/SRC-0023606.json)

## 비용·보존·남은 범위

B1은 Tab context16개/query17,408행이다. 로그의 fit7.4334117초와 predict92.8880715초 합은100.3214832초다. 결과의 단계 타이머는109.3704795초이며 anchor 구성을 위한 선행 scaler/KMeans 작업 이전부터 잰 전체 비용이 아니다. 초기 smoke4context/256query를 포함한 당시 누적20context/17,664query와 B1 비용을 구분한다. 03의 수정은 새 Tab/RCTL 호출0으로 기록돼 있다. [16회 호출 로그](../evidence/0003-0007/originals/SRC-0023601.json), [단계 타이머](../evidence/0003-0007/originals/SRC-0023604.json)

소속·분위수·가중치·action·입력은 보존돼 같은 조건의 산술 확인에 재사용할 수 있다. `partial_predictions`의 quantiles/median/mean은 최종 파일의 같은 배열과 완전히 일치함을 확인했다. 부분 파일 이름만으로 실행 중단 사례라고 분류하지 않았다.

검산은 저장 손실표·병합·PCC/random·지표를 대조했다. projection의 상태 배정은 동일 시점에 대한 B2의 저장 bin을 이용했고 두 원 코드의 context/스케일링/KMeans 설정이 같음을 읽었다. KMeans를 재학습해 배정 자체를 독립 확인한 것은 아니다. 교차오차 profile clustering, Tab/KNN 추론도 재실행하지 않았다.

재검토하려면 대표 상태가 실제 조건부 예측을 충분히 보존한다는 근거, 입력 수준·상태 수·함수군·다른 평가 구간 등 달라지는 조건을 제시해야 한다. 같은 예측에 상수 이동만 적용하고 이를 새 소속 알고리즘이나 독립 성공으로 세지 않는다. 실제 query를 유지한 다음 후보의 결과는 [04/06/07 B2](0004-0007-b2-observed-risk.md)에 연결한다.

[원문·실제 열람 범위](../sources/history-001.md), [검수](../verification/history-001.md), [근거와 실행 방법](../evidence/0003-0007/README.md). [과거 시도 색인](../prior-attempts.md).
