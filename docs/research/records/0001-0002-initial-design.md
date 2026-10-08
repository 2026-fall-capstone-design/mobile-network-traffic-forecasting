# 01–02 — 자료 진단·첫 CPU 동작 확인과 조건부 MAE 후보 설계

2026-09-25의 01은 **32cell 자료 진단과 네 모서리 cell의 TabICLv2 동작 확인**, 02는 이를 바탕으로 작성한 **후보 비교와 제한 실행 계획**이다. 01의 저장 예측·오차·지표는 대조했지만, 02에 적힌 위험함수 clustering과 RCTL 계획을 이 결과로 실행 완료 처리하지 않는다. 후속 03–09의 자료가 별도로 존재하며 그 실행·수정 관계는 이어서 검토한다. [01 원문](../evidence/0001-0002/originals/SRC-0020822.md.txt), [02 원문](../evidence/0001-0002/originals/SRC-0020823.md.txt), [출처와 읽은 범위](../sources/pilot-006.md)

## 무엇을 확인하려 했는가

첫 질문은 “공개 가공 Milan 자료로 고정 checkpoint의 CPU 추론이 정상 동작하며 비용을 기록할 수 있는가”였다. 당시 계획부터 4cell 결과를 clustering 효과나 논문 성능의 증거로 쓰지 않겠다고 명시했다. 자료 진단의 Ridge와 Tab 직접 예측은 최종 소속별 RCTL 평가와 다른 작업이다.

| 기록 | 실제 확인한 범위 | 완료로 세지 않은 범위 |
|---|---|---|
| 01 자료 진단 | 32cell의 저장 입력·정답·정규화·기본 지표와 Ridge 오차 | 전체 10,000cell의 품질 조사, 원자료 전처리 재현 |
| 01 CPU 동작 확인 | 4context·256query, 유한한 예측, 당시 시간·메모리 기록 | clustering/RCTL 효용, 추정기의 일반적 우위 |
| 02 후보·후속 설계 | 조건부 MAE 곡선, 비교군, 사전 판정과 과거 실행 상한을 문서로 확인 | 02만 보고 위험함수/RCTL 실행 성공 또는 전체 미실행을 확정 |

## 자료와 시간 구간

사용한 파일은 STCNet 배포본의 `data_git_version.h5`, shape `1488×10000×3`이다. 채널 2는 Internet 활동량이며 byte/bps로 이름을 바꾸지 않는다. 공식 배포 설명은 소수 세 자리 반올림과 원래 다섯 채널을 `(sms, call, internet)` 세 채널로 묶었다고 설명한다. 공개 전처리 예시와 현재 배포 H5를 처음부터 동일하게 재생성했는지는 미확인이다. [공식 배포 설명](https://github.com/chuanting/STCNet/blob/dc3ff65eb42b099ef8ec281c10282d6c47b533cb/readme.md), [자산·출처·재사용 조건](../evidence/0001-0002/README.md)

정리 중 확인한 H5 날짜 레이블은 **2013-11-01 00:00~2014-01-01 23:00**, 1,488개의 중복 없는 시간별 값이다. 아래 날짜는 저장 레이블을 그대로 해석했으며 시간대는 확정하지 않았다. 원자료의 통상적인 설명만 보고 12월 31일을 마지막 날로 가정하면 이 파일의 구간과 달라진다. [H5 지정 구간 대조](../verification/pilot-006-H5-check.json)

| 사용 목적 | 0-based 시간 인덱스, 양 끝 포함 | 저장 레이블에 따른 기간 |
|---|---|---|
| cell별 평균 scale | 0–671, 672시간 | 11/01 00시–11/28 23시 |
| 진단 Ridge 학습 후보 / smoke context 후보 | 168–671, 504개 | 11/08 00시–11/28 23시 |
| 실제 smoke query | 672–735, 64개 | 11/29 00시–12/01 15시 |
| 32cell 진단 query | 672–1007, 336개 | 11/29 00시–12/12 23시 |
| 당시 전체 설계 자료 | 0–1007, 42일 | 11/01 00시–12/12 23시 |
| 당시 미래 확인용으로 남긴 target | 1008–1487, 20일 | 12/13 00시–2014/01/01 23시 |

32cell은 0-based 행 `[37,45,53,61]`, 열 `[36,40,44,48,52,56,60,64]`의 격자다. `cell_id = row×100 + column + 1`이다. 성능에 따라 고른 집합이 아니라 사전 공간 배치이며, 저장된 실제 ID도 일치했다. 각 cell의 첫 672시간 평균으로 값을 나누고, target 시점 `t`마다 다음 16개 특징을 만든다.

- `t-8…t-1`의 최근 8값, `t-24`, `t-168`, 직전 24값의 평균과 표준편차.
- 예측 시각의 hour 및 weekday에 대한 sin/cos 네 값.

따라서 한 시간 뒤를 계속 예측하는 설정이며, query 시점에 이미 관측된 과거 query의 값도 lag에 들어간다. 64시간을 한 번에 내다보는 열린 루프 예측으로 해석하면 안 된다. 저장 `X`는 `32×840×16`, `Y`는 `32×840`, 시점은 168–1007이다. `raw`는 처음 1008시간의 32cell 값이다. 마지막 20일 target은 이 진단 코드나 이번 H5 값 대조에서 읽지 않았다. 전체 날짜 레이블을 읽은 것과 후반 target을 읽은 것은 구분한다. [실행 코드 원문](../evidence/0001-0002/originals/SRC-0022703.py.txt)

이 지정 raw 구간은 유한하고 음수 수와 0의 비율이 모두 0이며 scale은 양수다. 가공 이전의 결측 여부나 보충값의 타당성까지 확인한 것은 아니다. 01에 적힌 상수 여부 진단도 이 사실만으로 충족됐다고 판단하지 않는다.

## 실제 CPU 동작 확인과 지표

네 cell 각각에서 504개 context 후보 중 `rint(linspace(0,503,256))`으로 256개를 선택했다. query는 공통으로 672–735의 64개다. 공식 regressor checkpoint의 **고정 가중치**에 context를 제공하는 `fit`과 median `predict`를 사용했다. 이를 gradient 학습 4회로 세지 않는다.

당시 설정은 CPU, `n_estimators=1`, `batch_size=1`, `random_state=20260925`, `n_jobs=1`, torch 4 threads/interop 2, AMP·FA3·offload 비활성, 자동 다운로드 비활성이다. 저장 환경은 Python 3.12.14 / torch 2.14.0+cpu다. checkpoint·소스 ZIP의 버전/해시는 [자산 안내](../evidence/0001-0002/README.md)에 있다. 전체 설치환경의 독립 재현은 하지 않았다.

아래 값은 **cell별 첫 672시간 평균으로 정규화한 MAE**다. Tab·최근값·하루 전 값은 저장 배열에서 다시 계산했다. smoke Ridge 예측은 저장되어 있지 않아 그 열은 JSON에 보고된 값이다. 여기의 소규모 우위를 근거로 모델을 선택하지 않는다. [당시 smoke JSON](../evidence/0001-0002/originals/SRC-0023607.json), [검산 결과](../verification/pilot-006-initial-check.json)

| cell | Tab median | Ridge 보고값 | 최근값 | 하루 전 |
|---|---:|---:|---:|---:|
| 3737 | 0.057523 | 0.059659 | 0.082465 | 0.106920 |
| 3765 | 0.071247 | 0.109175 | 0.106855 | 0.203062 |
| 6137 | 0.046166 | 0.060313 | 0.092058 | 0.240018 |
| 6165 | 0.051061 | 0.073416 | 0.115648 | 0.192972 |

모든 저장 Tab 예측은 유한하며 4context·256query가 남아 있다. 당시 `fit+predict` 합은 **4.8401823초**다. 다운로드·전체 자료 처리·32cell Ridge·비교용 Ridge 시간까지 합친 실행 총시간은 아니다. 최대 기록 RSS는 **574,816,256 byte**이며 0.2초 간격의 프로세스 메모리 표본이다. 연속적인 진짜 최대값이나 모델만의 메모리라고 표현하지 않는다.

별도의 32cell 진단 Ridge는 504개 시점에서 StandardScaler + Ridge(alpha=1)를 적합하고 336개 시점에서 평가하는 코드다. 저장된 `32×336` Ridge 오차와 JSON의 cell별 MAE를 대조했다. smoke Ridge는 256개 context·64개 query이므로 두 결과를 같은 실험으로 합치지 않는다. 정규화 target 상관의 중앙값은 약 **0.654166**, Ridge 오차 상관의 중앙값은 약 **0.160402**다. 상관 감소는 기술 통계이며 공동 학습의 효과나 negative transfer의 원인을 입증하지 않는다. [자료 진단 원문](../evidence/0001-0002/originals/SRC-0023576.json)

## 02에서 고른 초기 후보와 보류한 주장

02는 세 방향을 비교했다. 잔차의 동시 상관만으로 grouping하는 안은 상관과 negative transfer를 혼동할 수 있어 핵심 추천에서 제외했다. 교차 예측 오차 profile clustering은 RMB-CLE와 겹친다고 판단해 비교군으로 남겼다. 이는 **당시 문헌 판단**이며 이 묶음에서 RMB-CLE 전체를 새로 검증한 결과는 아니다. 이후의 선행 비교는 [640과 문헌 연결](0640-contribution-boundary.md)에서 별도 확인했다.

선택한 후보는 cell별 고정 context에서 추정한 조건부 분포로 다음 비용표를 만드는 것이다.

`L_i(x,a) = E[|Y-a| | x,i]`, `F(C) = Σ_x min_a Σ_{i∈C} p_i(x)L_i(x,a)`.

각 cell의 관측 상태 빈도 `p_i(x)`를 유지하고, 병합 비용 `F(A∪B)-F(A)-F(B)`를 계산한다. Tab을 pooled context로 다시 실행한 결과가 아니라 **추정한 분포 아래에서 공통 예측값을 선택하는 이상적 비용**이다. RCTL의 용량·추정 오차·학습 경로, 개별 cell 보호와 실제 MAE 개선은 따로 남는다. 원문도 Bayes decision 목적식의 최초성을 주장하지 않는다.

| 02의 사전 고정 항목 | 계획한 내용과 범위 |
|---|---|
| cell/context | 32cell 각 행에서 열 위치 `[0,2,4,7]`을 택한 16cell; context 시점 168–671의 504개 |
| 상태 대표 | context 입력으로 StandardScaler + KMeans, 64중심, seed 20260925, n_init=5; 각 중심에 가까운 실제 입력을 공통 query로 선택 |
| 분포·action | 같은 호출의 median/129 midpoint quantiles; native 999개 전체와 구분. 상태별 분위수 범위의 257개 action grid |
| query 비교 | 672–839에서 고정 간격 64개. 모든 cell context의 교차오차 계산은 소규모 비교군의 N² 비용으로 별도 기록 |
| 소규모 병합 | K=4, 한 round에 각 cluster 최대 한 번 병합, 16→8→4. unrestricted agglomeration과 구분 |
| 대규모 구상 | 입력 요약 k=16 이웃 graph, edge 중복 제거, 남은 singleton을 ID순으로 짝짓는 fallback; 비율·손실 보고, 최적 partition 보장 없음 |
| 비교군 | KNN(k=32) 조건부 경험분포, median, median+IQR uniform, PCC, random, 교차오차 profile+cosine+average-linkage |
| 원 UPC | 16cell에서는 원문의 `\|G\|>10` seed 조건을 충족하기 어려워 핵심 소규모 비교에서 제외. 이를 임의로 완화한 것을 원 UPC라고 부르지 않음 |

원문은 absolute loss의 1-Lipschitz 성질로 action grid 근사 오차를 설명한다. **가중합에 옮길 때의 척도**도 보존해야 한다. 개별 `L_i`의 반간격 오차가 `Δ_x/2`라면, `Σ_i p_i(x)L_i`에는 질량 `Σ_i p_i(x)`가 곱해진다. 이는 정리 과정의 수식 범위 확인이며 새로운 실험 결과가 아니다. 이 오차 제한은 상태 양자화·분포 추정이나 실제 RCTL의 오차를 제한하지 않는다.

사전 판정은 합성 손실의 일치, 상태 양자화로 인한 예측 차이, KNN/median+scale과의 결정 차이를 확인하는 것이었다. 구현 불일치이면 수정하고, 핵심 가정이 무너지거나 추가 정보가 없으면 추천을 보류한다. 다른 partition을 만들었다는 사실과 성능 우위를 구분한다. 합성 확인도 실제 자료의 우수성 증거로 취급하지 않는다.

## 당시 후속 RCTL 계획과 현재의 한계

02의 RCTL 계획은 train targets 168–839(672개), validation 840–1007(168개), test 1008–1487(480개)다. 원문이 train을 “첫 35일”이라고 부르는 것은 자료의 마지막 위치를 포함한 표현이며, 첫 168시간 lag 준비를 뺀 **실제 train target은 28일 분량**이다. 처음 42일 자료 사용 범위와 유효 target 개수를 구분한다.

공식 Keras 구현의 Torch port, 6 TCN-LSTM block과 두 residual 구조, 최근 8시간의 sequence에 나머지 8개 특징 반복을 계획했다. MAE·Adam(lr=0.001)·batch256·최대80epoch·patience10·seed20260925, full risk와 PCC만 사전 seed20260926을 추가할 예정이었다. 5partition×4group + global1, 추가8fit으로 **최대29fit·2320epoch·50분**이다. 이는 기록된 **상한**이며 소비한 fit/epoch 수가 아니다.

주 지표는 cell별 mean-scaled MAE의 균등 평균, 보조 지표는 원단위·cell별·95% 초과 peak query MAE였다. 48시간 paired blocks 10개와 96시간 민감도, partition·hyperparameter 사전 봉인, 설정을 바꾸면 해당 test가 이후 개발 자료가 됨을 명시했다. 원 RCTL의 1000epoch·원자료 재현은 주장하지 않았다. 수렴 부족과 후보 기각도 구분할 계획이었다.

초기 누적 Tab 상한 80context·60,000query·40분, 전체 local modeling 100분 등은 과거 연구 운영 기록이다. 01의 실제 4context·256query와 섞지 않으며 현재 정리 작업의 실행 허가로 사용하지 않는다. 이후 확대·예산 변경·후반 자료 사용 여부는 해당 후속 기록에서 별도로 연결한다.

## 재사용과 재검토 기준

같은 네 cell·checkpoint·context·query의 단순 CPU 동작 확인을 새 clustering 실험처럼 반복할 필요는 없다. 저장된 예측·정답·특징과 비용 기록으로 이미 한 일을 확인할 수 있다. 다른 플랫폼·패키지 버전·ensemble·자료 구간을 확인하려면 그 차이를 새 기록에 적는다. 과거 실행 코드의 보존과 현재 환경에서의 재실행 성공은 다르다.

조건부 위험함수 후보를 다시 검토할 때에는 02의 모델 공유 가정, 상태 양자화, 가중합 척도, N² 비교 비용을 먼저 확인한다. 후속 [03 B1](0003-b1-anchor-projection.md)은 대표 입력 축약으로 오차가 커 RCTL 연결 전에 기각됐고, [04·06·07 B2](0004-0007-b2-observed-risk.md)는 실제 query 방식으로 바꾼 뒤 29 RCTL fit에서 경험적 정답 손실표에 불리했다. 두 번째 seed의 비교 대상도 02의 PCC에서 04의 empirical로 사전에 바뀌었다. 05·08·09의 근거 검수는 별도 진행 중이다. 초기의 잔차 상관 문제와 이후 [635–642 관계 점수 흐름](0635-0637-execution-recovery.md)은 시점과 방법이 다르며, 그 사이 전수 기록의 연결은 진행 중이다.

[검수 범위와 남은 항목](../verification/pilot-006.md), [작은 근거·대용량 자산 접근](../evidence/0001-0002/README.md), [새 실험 전 확인할 색인](../prior-attempts.md)
