# 59–62. cell을 나누면 최근 입력을 줄일 수 있는가

60번의 고정된 네 cell에서는 **grouping으로 짧은 입력의 이득을 얻는다는 판단을 지지하지 못했다.** 동시에 TabICLv2의 global·L2 직접 예측이 Ridge/HGB보다 좋았던 결과도 남는다. 이 두 결과는 함께 성립한다. Tab의 예측력을 clustering 또는 RCTL의 성능으로 바꾸어 해석하지 않는다. [60 사전 계획](../evidence/0059-0062-history-grouping/originals/SRC-0021940.md.txt) · [62 당시 판단](../evidence/0059-0062-history-grouping/originals/SRC-0021984.md.txt)

2026-09-26에 작성된 59의 문헌·논리 검토 계획, 60의 실제 예측, 61의 별도 산술, 62의 종합 판단을 구분한다. H051은 **60의 저장 예측과 실행·회계, 62의 해당 판단**을 검수했다. 61 산술은 [후속 H052](0061-history-logic-cost.md)에서 별도로 검수했다. ALW는 [후속 H053](0059-alw.md)에서 논문·고정 코드·비용을 대조했다. Optimal Look-back 문헌과 62 전체 종합은 후속 범위다. 현재 정리 과정의 모델 호출·원 코드 실행은 0이다.

## 질문과 비교 단위

가설은 cell을 합칠 때 발생 과정을 구별하는 데 더 긴 이력이 필요하고, 나누면 최근 입력을 줄일 수 있다는 것이었다. 당시 RCTL은 8시점 입력이 마지막 Dense 크기에도 연결되므로, 기존 RCTL 입력만 잘라 짧은 모델의 성능처럼 보고할 수 없었다. RCTL 추가 fit을 하지 않는 조건에서 Tab·Ridge·HGB로 중간 현상만 확인했다. [59 계획](../evidence/0059-0062-history-grouping/originals/SRC-0021920.md.txt)

grouping은 학습된 새 clustering이 아니다. `global`은 네 cell 통합, `geo2`는 `{3737,3765} / {6137,6165}`, `local`은 cell별, `global+ID`는 통합 입력에 cell one-hot 네 열을 더한 대안이다. UPC 전체 알고리즘이나 소속 최적화의 결과가 아니다.

## 자료·시간·정규화

STCNet 배포 HDF5의 Internet 활동량 채널 2를 사용했다. 현재 파일의 전체 SHA와 크기, 지정 네 열과 날짜를 확인했다. byte·Mbps 단위로 바꾸지 않는다. HDF5의 shape는 `1488×10000×3`이며 날짜 레이블은 2013-11-01 00시–2014-01-01 23시다. 날짜의 시간대는 원 파일에서 확정하지 않았다. [기존 자료 출처·입수 안내](../evidence/0001-0002/README.md) · [현재 입력 대조](../evidence/0059-0062-history-grouping/input-audit.json)

| 항목 | 실제 조건 |
|---|---|
| cell | 첫 smoke와 같은 3737, 3765, 6137, 6165. 새 결과로 교체하지 않는 계획 |
| 정규화 | cell별 처음 672시간(11/01–11/28)의 평균으로 나눔. 이후 query로 scale을 맞추지 않음 |
| context target | 0-based 168–839에서 `rint(linspace(...,256))`; cell당 256개. 날짜 범위 11/08 00시–12/05 23시 |
| query target | day index 43,47,51,55, 각 날짜의 0–23시 중 16개. 실제 날짜 12/14,12/18,12/22,12/26. cell당 64개 |
| target | t−1까지의 입력으로 시점 t의 실제 활동량을 예측 |
| 시간 분리 | 마지막 context target 839, 첫 query 1032. 최근 8값뿐 아니라 최장 168 lag도 첫 query에서 864로 context 끝 이후 |
| 평가 지위 | 이전에 접근한 개발 자료. 독립 test 또는 통계적 유의성 검사가 아님 |

scale은 cell 순서대로 약 `608.143789, 720.897650, 161.308948, 4768.912588`이다. 저장 scale·정답 256개·시간 인덱스와 원자료를 대조했다. 각 시점의 관측된 과거값을 쓰므로, 네 날짜를 한 번에 내다보는 recursive/open-loop 예측이 아니다.

L2/L8의 차이는 최근 연속 값 2개와 8개다. **두 조건 모두** 하루·일주일 전 값, 직전 24시간 평균·표준편차, target 시각/요일 sin·cos를 갖는다. 따라서 전체 과거를 2시간으로 제한한 실험이 아니다. 기본 특징 수는 10/16, ID 대안은 14/20이다. [설정](../evidence/0059-0062-history-grouping/originals/SRC-0027868.json) · [실행 코드 보존본](../evidence/0059-0062-history-grouping/originals/SRC-0022879.py.txt)

각 grouping·길이의 고유 context는 총 1,024행으로 같지만, 한 context의 크기는 global 1,024 / geo2 512 / local 256행이다. pooling에 따른 공유량도 함께 바뀐다. 동일 context 크기에서 소속만 바꾼 효과로 해석하지 않는다.

## 모델과 실제 수행 근거

TabICLv2는 저장 `tabicl-regressor-v2-20260212.ckpt`, ensemble 1, median, seed 20260925, CPU를 쓴다. 코드에는 torch 4 threads/interop 2, batch size 1, n_jobs 1, AMP·FA3·offload·자동 다운로드 비활성 설정이 있다. `fit`은 고정 가중치에 context를 제공하는 동작이며 새 gradient 학습 횟수로 세지 않는다. 현재 checkpoint의 SHA를 확인했으나 객체를 불러오거나 당시 패키지 환경을 독립 재현하지 않았다.

Ridge는 StandardScaler + alpha 1, HGB는 absolute_error, 100 iterations, 15 leaves, min samples 20, l2=1, early_stopping=False, 같은 seed다. 코드가 세 모델의 예측을 0 이상으로 clip한다. 저장된 적합 X·단순 모델 객체·clip 이전 예측은 별도로 없으므로 그 상태까지 복원한 검수는 아니다.

각 길이에서 1+2+4+1=8 contexts, 두 길이 합 **16 contexts·2,048 query행**이다. 호출 로그의 완료 16건, 순서·cell·행·특징 수와 합계를 확인했다. 단순 모델은 각 context에서 두 개, 총 32 fits가 코드·완료 결과·원장에 연결된다. RCTL fit/forward는 0이다. 시작/종료 marker와 최종 결과가 있으며 현재 결과 폴더에 중단 marker는 없다. 원 콘솔의 exit code·외부 시도 이력 전체를 확보한 것은 아니다. [호출 기록](../evidence/0059-0062-history-grouping/originals/SRC-0027862.json) · [종료 기록](../evidence/0059-0062-history-grouping/originals/SRC-0027866.json)

## 저장 예측에서 다시 계산한 결과

아래는 cell별 처음 672시간 평균으로 정규화한 MAE다. 각 조건은 4cell×64시점의 동일 가중 평균이며 작을수록 좋다. raw 활동량 MAE는 별도 값으로 보존한다. 전체 24조건의 전체·cell별·날짜별·전후반·raw MAE 288개를 저장 예측에서 대조했다. [결과 JSON](../evidence/0059-0062-history-grouping/originals/SRC-0027865.json) · [재계산 검수](../verification/history-051-numeric-check.json)

| grouping / 최근 길이 | TabICLv2 | Ridge | HGB |
|---|---:|---:|---:|
| global / 2 | 0.067327 | 0.090199 | 0.102476 |
| geo2 / 2 | 0.084254 | 0.090577 | 0.118711 |
| local / 2 | 0.095156 | 0.096073 | 0.122249 |
| global+ID / 2 | 0.069716 | 0.090250 | 0.102210 |
| global / 8 | 0.072282 | 0.088344 | 0.110615 |
| geo2 / 8 | 0.086142 | 0.090386 | 0.119553 |
| local / 8 | 0.097600 | 0.094176 | 0.126342 |
| global+ID / 8 | 0.073877 | 0.088219 | 0.107802 |

Tab global·L2는 두 단순 모델보다 전체·양쪽 시간 절반·네 날짜 블록 모두 낮은 MAE다. 그러나 모든 cell에서 이긴 것은 아니다. **3737에서는 두 단순 모델보다 나쁘다.**

| cell, global·L2 | TabICLv2 | Ridge | HGB |
|---|---:|---:|---:|
| 3737 | 0.056775 | 0.054888 | 0.055692 |
| 3765 | 0.060333 | 0.095455 | 0.111309 |
| 6137 | 0.084967 | 0.123187 | 0.134494 |
| 6165 | 0.067235 | 0.087266 | 0.108411 |

Tab global·L2의 raw 활동량 MAE는 103.090788, Ridge는 134.557562, HGB는 163.201805다. 이 척도는 큰 원 활동량 cell의 영향이 다르므로 정규화 MAE와 같은 값으로 합치지 않는다.

Tab global에서 L2는 L8보다 전체 MAE가 약 0.004955 낮지만, 3737은 `0.056775 > 0.052353`, 12/22 블록은 `0.057201 > 0.054287`이다. 따라서 모든 cell·날짜에서 짧은 입력이 더 낫다는 결론도 성립하지 않는다.

## grouping의 기각 범위와 상호작용

Tab geo2·L2와 local·L2는 global·L2뿐 아니라 global+ID·L2보다 전체와 양쪽 시간 절반에서 모두 나쁘다. global·L2 대비 geo2 차이는 앞 `+0.000227`, 뒤 `+0.033626`, local은 `+0.001942 / +0.053715`다. 뒤쪽에서 손해가 더 크다. 날짜별로는 geo2가 12/14·12/22에서 global·L2보다 낮은 오차를 보여, 전 구간 동일한 손해라는 표현도 피한다.

cell별로는 local·L2가 global·L2보다 3737에서 좋아지고 다른 세 cell에서 나빠진다. geo2·L2는 네 cell 모두 global·L2보다 나쁘다. 평균 기각과 일부 cell의 이득을 함께 보존한다.

사전 정의한 `I=(global2−global8)−(split2−split8)`는 양수일 때 grouping이 긴 연속 이력의 필요성을 줄인 방향이다. 참 조건부 정보량이나 인과 효과의 추정량은 아니다. 전반은 12/14·12/18, 후반은 12/22·12/26의 저장 query를 묶은 값이다.

| 모델 / grouping | 전체 I | 전반 I | 후반 I |
|---|---:|---:|---:|
| TabICL / geo2 | -0.003066 | +0.000403 | -0.006536 |
| TabICL / local | -0.002511 | +0.002630 | -0.007652 |
| Ridge / geo2 | +0.001665 | +0.002193 | +0.001136 |
| Ridge / local | -0.000042 | +0.000756 | -0.000840 |
| HGB / geo2 | -0.007297 | +0.000137 | -0.014732 |
| HGB / local | -0.004046 | -0.002664 | -0.005428 |

Tab의 두 grouping은 전반 양수·후반 음수다. Ridge geo2는 양쪽 절반 양수지만 Tab/HGB에 유지되지 않고, Ridge geo2도 마지막 날짜 블록에서는 음수다. 사전 계획의 안정성 조건을 통과한 데이터 특성으로 확정하지 않는다. 고정 네 cell·두 길이·한 seed·부분 query의 결과이며, 다른 지역·긴 입력·다른 clustering의 불가능성 증명은 아니다.

## 실행 비용과 원장 시점

| 기록값 | 실제 측정 범위 |
|---|---|
| Tab fit+predict 19.109481초 | 16개 호출의 두 타이머 합. 생성자·일부 준비는 이 타이머 밖 |
| simple_fit_seconds 2.006623초 | 이름과 달리 Ridge/HGB의 fit과 predict를 함께 감싼 타이머 |
| stage 22.312042초 | 입력·checkpoint 해시, 설정/시작 marker 작성 뒤 시작; 최종 JSON/NPZ 저장과 마지막 해시 재검사 전 종료 |
| cheap 3.202561초 | stage−Tab. 단순 모델 시간이 이미 포함되므로 다시 더하지 않음 |
| 관측 RSS 492,646,400bytes | 호출 사이 관측의 최대. 연속 peak 또는 모델만의 메모리가 아님 |

계획의 Tab 240초/simple 30초/stage 300초/RSS 8GiB는 코드에서 호출 사이에 검사한다. 한 호출 도중의 엄격한 강제 중단이나 연속 메모리 제한이라고 설명하지 않는다. 실제 저장값은 이 한도보다 작다.

60 직전 원장과 61 시작 전 원장 사이의 **전체 JSON 차이**가 회계 코드의 단 한 번 반영과 일치했다. Tab 49→65 contexts, 35,968→38,016 query행, 누적 fit+predict 226.4302955→245.5397765초다. RCTL은 29 fits·추가 허용 0으로 그대로다. 60까지 cheap 합 64.0087483초, 기록된 modeling 합 1,977.5555366초다. 62의 총계는 이후 61 산술까지 포함한 시점이므로 이 값과 시점을 구분한다. 이전 전처리·타이머 밖 비용을 포함한 완전한 총시간은 아니다. [60 직전 원장](../evidence/0059-0062-history-grouping/../0056-0058-mae-sampling/originals/SRC-0000838.json) · [60 이후/61 직전 원장](../evidence/0059-0062-history-grouping/originals/SRC-0027869.json) · [회계 코드](../evidence/0059-0062-history-grouping/originals/SRC-0023214.py.txt)

## 재사용과 다음 확인

원본 예측 NPZ 두 개, 계획·코드·설정·호출·결과·전후 원장을 연결했다. partial과 final의 공통 숫자 배열은 모두 같으며, final에는 context 시점·scale·날짜가 추가돼 있다. final의 날짜는 object dtype으로 직렬화돼 있어 숫자 배열은 `allow_pickle=False`로 읽고 날짜 문자열은 정적으로 대조했다. 객체 역직렬화나 모델 로딩은 하지 않았다. [작은 근거와 검수 명령](../evidence/0059-0062-history-grouping/README.md)

재검토하려면 grouping 단위·입력·공유량·새 평가 기간·선택 비용 가운데 무엇이 달라지는지 적어야 한다. 현재 결과로 Tab 예측을 전부 부정하거나, 반대로 global·L2의 좋은 점수만 골라 clustering→RCTL을 채택하면 안 된다. 입력 길이 선택 자체의 선행연구, 61의 논리/MAC 산술, 최종 RCTL의 짧은 모델 학습·성능은 이 묶음에서 검증하지 않았다. [출처별 범위](../sources/history-051.md) · [주장과 검수](../verification/history-051.md) · [과거 시도 색인](../prior-attempts.md)
