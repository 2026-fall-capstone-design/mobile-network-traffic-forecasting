# 원106 같은 K에서 남는 cell별 오차 전이

**원106은 같은 K4와 모델당 학습행 수를 가진 두 소속을 저장 예측으로 비교한 진단이다.** 두 seed 모두 이후 구간의 평균 손해가 남았지만, 자료 구성·시간 변화·최적화 중 어느 원인이 작용했는지는 식별하지 않았다.

[14출처/31경로](../sources/history-136.md) · [26주장](../verification/history-136-claims.json) · [작성 후 대조](../verification/history-136-second-pass.json) · [수치 검수](../evidence/0136-same-k-cellwise-error-transition/saved-numeric-check.json) · [재검토 안내](../references/same-k-cellwise-error-transition.md)

## 연구 질문과 실제 수행

2026-09-26, [원105의 과거 차단 감사](0135-blocked-audit-and-resume-conditions.md) 이후 계속 진행 기록과 저장 예측 진단을 남겼다. 원106은 Tab-risk 소속의 RCTL이 empirical-risk 소속의 RCTL보다 불리한 차이가 훈련부터 있었는지, 이후에 뒤집혔는지를 물었다. 새로운 추천 알고리즘이나 독립 평가 결과는 아니었다.

기존 16cell 전부와 seed20260925·20260926을 사용했다. 두 방법은 K4·cluster당4cell이며 모델당672×4=2688훈련행이다. 소속과 정규화는 변경하지 않았다. 과거 fit16개와 예측을 재사용했으며 새 RCTL fit·추론·Tab context·데이터 다운로드는0으로 기록됐다. 현재 아카이브에서도 원코드를 실행/import하거나 모델을 생성하지 않았다.

| 고정 target위치 | 길이 | 사용 범위 |
|---|---:|---|
| train168–839 | 672 | 훈련 예측 |
| validation840–1007 | 168 | validation 예측 |
| 이후1008–1487 | 480 | 이미 사용한20일 개발자료 |

이후480시간을 앞·뒤240시간으로 나눴다. 위치값만으로 새 timestamp나 독립 시간 표본을 복구한 것은 아니다. 고정 설정은 MAE·batch256·patience10·lr0.001·Adam epsilon1e-7·최대80epoch이며16개task의 seed/cluster/members가 fits와 일치한다. 기간·학습정책·task는 [pilot 고정설정](../evidence/0003-0007/originals/SRC-0030238.json)과 연결한다. 입력·정규화는 [원33–35의 이전 검수](0033-0035-process-fit-gap.md)를 재사용한다. 그 기록의 Milan internet hourly 16cell·cell별 원시index0–671 평균 정규화·최근8값과8특징(day/week lag·day mean/std·달력4)의 구성, 실제 당시 forward sequence가 저장되지 않았다는 한계를 함께 읽는다. 이번에 원33–35의 원문 전문이나 당시 forward 입력을 새로 복구한 것은 아니다. 현재 새로운 입력이나 단위 복원은 수행하지 않았다.

## 평균과 cell·시간별 결과

차이는 **Tab-risk 소속 RCTL의 scaled MAE − empirical-risk 소속 RCTL의 scaled MAE**다. 양수면 Tab 소속 쪽이 불리하다. 직접 Tab 예측 MAE나 원단위 오차와 구별한다.

| seed | 훈련 평균차이 | validation 평균차이 | 이후 평균차이 | 이후 불리/유리cell |
|---|---:|---:|---:|---|
| 20260925 | +0.003314059 | +0.002773022 | +0.005727739 | 10/6 |
| 20260926 | −0.000738154 | +0.000161813 | +0.004243768 | 9/7 |

| 훈련→이후 부호 조합 | 20260925 | 20260926 |
|---|---:|---:|
| 불리→불리 | 8 | 5 |
| 불리→유리 | 3 | 5 |
| 유리→유리 | 3 | 2 |
| 유리→불리 | 2 | 4 |

두seed의 이후 평균이 모두 불리한cell은3765/4545/5353/5365/6145/6153/6165의7개다. 두seed와 두10일 구간을 모두 만족한 것은3765/4545/5353/6153의4개다. seed별 두반구간 손해는9/6cell이고, 불리한 날짜는15/14일·두seed 공통11일이다. 반대 방향의 cell·날짜도 [32행 CSV](../evidence/0136-same-k-cellwise-error-transition/originals/SRC-0024873.csv)와 [원결과](../evidence/0136-same-k-cellwise-error-transition/originals/SRC-0024874.json)에 함께 남겼다. 손해가 큰cell만 다음 평가에 고르지 않으며 날짜20개를 독립실험20회로 세지 않는다. 1e-10은 수치동점 기준이며 동등성 검정이 아니다.

## 이 결과로 판단할 수 있는 범위

같은 모델당 sample 개수는 두 분할의 순위 차이를 자료 수 감소 하나로 설명하는 해석에 한계를 준다. 실제 epoch 합은 첫seed Tab221/empirical223, 둘째235/216으로 달랐다. 같은 설정과 K가 같은 자료 구성이나 최적화 경로까지 통제한 것은 아니다. '잘못 합쳤다'·'불필요하게 나눴다'·'과적합 때문이다' 중 하나의 인과 원인을 확정하지 않는다.

`이후차이 = 훈련차이 + 두방법의 이후−훈련 변화량 차이`는 산술 항등식이다. 평균 변화량 차이0.002413680/0.004981922를 원인 기여율로 쓰지 않는다. globalK1 대비K4의 앞선 손해는 모델 수·자료량도 달라진 비교이며 이번 동일K 진단과 구별한다. 보고서는 원UPC의10분·대규모 실험 재현도 아니라고 명시했다.

## 재검토와 과거 운영 상태

당시 후속은 기존16cell·모든훈련sample에서 조건별 자료 구성의 차이를 확인하고 원인 구별 계획1개를 고정하는 것이었다. 기존13/14/19/23/25/80의 입력지원·조건위험 결과를 재사용하도록 했다. 이 연결 자료들을 이번에 전문 재검토한 것으로 세지 않는다. 직접Tab의 낮은 MAE, 비슷한cell 묶기, 이미 있는 달력·일/주lag 추가만으로 RCTL 공동학습의 이득이나 신규성을 대신하지 않는다.

후보 진입에는 실제 손해와 적용범위, 경쟁 원인·식별 한계, Tab이 추정할 정보와 달라지는 소속 결정, 큰학습 전 최소 판별 비교가 필요했다. 지원 차이를 설명할 근거가 없으면 retrieval·거리·겹침 보정을 추천하지 않고 학습 정책·자료량 통제의 필요성을 검토한다. 차이가 있어도 가까운 조건부전이 방법과 결정 차이를 비교하기 전 신규성으로 쓰지 않는다. 성공 결과를 미리 요구한 조건은 아니었다.

상태JSON은 과거 nativeGoal blocked·재개false·새Goal생성false·goal완료false·heartbeat ACTIVE를 보고했다. 당시 도구응답은 별도로 복구하지 않았다. 수정전Goal250행은 확인했지만 수정후9.1절의 정확판본은 미복구다. 작은 실행정책의 ledger활성화는false이고 새18fit을 시작하지 않았다고 기록했다. 추가RCTL18fit/80epoch/1800초, 기존잔여를 포함한 다음Tab32context/16384행, 별도 다음Tab시간600초는 실제사용량과 구별한다. 현재 Goal·자동화·모델 실행 권한으로 적용하지 않는다.

## 재사용 자료·비용과 이번 검수

early753997…/laterf2d5c4…/fits5531c0…/plan81b7a1…/beforeledger60b589…가 원106 저장hash와 일치한다. 보존 코드112행은 읽기만 했다. 보고서는 경로만 연결했고 원결과에는 코드SHA가 없어 실행 당시 코드판본을 독립 고정하지 못했다. 기존NPZ의 필요한41배열을 stdlib로 해석해 scaled MAE·32CSV행·날짜별값 등250개 수치를 대조했고 maxCSVdiff0, 과거fit평균 최대차이1.013201350597015e-8을 확인했다. 이는 저장자료 산술 검수이며 새 모델 실행·독립 모델 재현·모든NPZ 배열 전문검토가 아니다.

원래0.02850919999764301초는 현재 다시 측정한 시간이 아니다. 원코드는 최초hash 뒤부터 배열로드/수치대조를 재고 마지막hash와 파일출력 전에 시간을 저장한다. 회계 전60b589…와 후98972…는 진단비용 키와 같은 사건의 상세항목 두 위치만 달랐다. 사건은1회이고 모델사용·상한·잔여·reset은 그대로다. 후SHA는 원108 활성화 전 보관본에 남은 정확판본이다. 원108을 실행하지 않았고, 현재root17a549… 원장은 해시만 보호했다.

14고유SHA/31물리경로에 새정확사본9개65970bytes·기존5사본을 연결했다. 최초8raw687행과 설정72행/필드30·fits16항목8필드·원장7/9·NPZ41배열 범위를 구별한다. 작성후8raw520행(Goal은83행 선택)·JSON113pointer·NPZ41header와 기존산술근거로26주장/6그룹을 대조했다. 원본37고유경로·보호6개는 불변이다. 신규내용은 비JSON전문5·literalJSON3·선택1이며 공개검수 뒤 한 번 집계하고 재독/재사용은 집계하지 않는다.

progress132–611/old122–601·RCTLsummary literal전문·긴고유판본·원107이후/옛고유판본/다른형식·통합/장기접근/최종delta/검색10+가 남아 있다. 진단 complete와 연구 Goal 완료, 이 기록의 게시와 전체 아카이브 완료를 구별한다.

## 주장별 근거

<a id="claim-01"></a>

### H136-C01 · 원106의 계속 진행 기록과 과거 도구 보고

2026-09-26 원106 상태JSON은 목표파일 수정true·기존nativeGoal blocked·native재개false·새Goal생성false·goal완료false와 과거heartbeat ACTIVE/creation_confirmed_by_tool=true를 기록했다. 이는 JSON의 당시 보고이며 도구반환 로그나 현재 자동화 상태를 별도로 복구한 것은 아니다. 현재 아카이브에서 Goal재개·자동화생성·예약작업을 실행하지 않는다.

근거: [SRC-0020852](../sources/history-136.md#src-0020852) 행1–18

<a id="claim-02"></a>

### H136-C02 · 수정 전 Goal 판본과 수정 후 증거 공백

106_goal_before_revision.md의 SHA0c36c5… 250행을 읽었다. 기존cell clustering→RCTL·RCTL결과의 소속결정 배제·실제근거/누적상한/완료조건을 담은 수정 전 판본이다. 상태JSON의 goal_file_revised=true와 보고서의 제9.1절 인용은 수정 후 Goal 전문이나 승인도구 응답의 복구를 뜻하지 않는다. 과거Goal 전문은 현재 실행 지시로 쓰지 않는다.

근거: [SRC-0020853](../sources/history-136.md#src-0020853) 행1–34 · [SRC-0020853](../sources/history-136.md#src-0020853) 행181–206 · [SRC-0020853](../sources/history-136.md#src-0020853) 행228–250 · [SRC-0020852](../sources/history-136.md#src-0020852) 행3–8 · [SRC-0020854](../sources/history-136.md#src-0020854) 행41–41

<a id="claim-03"></a>

### H136-C03 · 작은 실행 정책과 당시 원장 활성화를 구별

원106 상태JSON의 작은 정책은 activated_in_model_ledger=false였다. starting29fit/Tab78context·55488행, 추가RCTL18fit·fit당80epoch·1800초, 기존잔여를 포함한 다음Tab32context·16384행과 별도의 다음Tab시간600초와 automatic_recharge_per_run=false를 남겼다. 계획 상한을 실제 사용·자동 증액·현재 아카이브의 모델 실행 권한으로 옮기지 않는다.

근거: [SRC-0020852](../sources/history-136.md#src-0020852) 행19–33 · [SRC-0002031](../sources/history-136.md#src-0002031) JSON /used, /caps, /remaining_count_budgets, /new_RCTL_fits_permitted_under_current_cap

<a id="claim-04"></a>

### H136-C04 · 같은 K와 sample 개수의 비교 질문

원106은 두 소속의 K4·cluster당4cell·모델당2688훈련행을 고정하고, 훈련→validation→이후 구간에서 Tab-risk RCTL과 empirical-risk RCTL의 순위 변화를 16cell·두seed 모두 확인했다. 같은 sample 개수는 자료 구성·난이도·학습 경로까지 같다는 뜻이 아니며 원인의 증명도 아니다.

근거: [SRC-0020851](../sources/history-136.md#src-0020851) 행5–20 · [SRC-0020854](../sources/history-136.md#src-0020854) 행7–18 · [SRC-0022572](../sources/history-136.md#src-0022572) 행29–46 · [SRC-0024874](../sources/history-136.md#src-0024874) 행67–69 · [SRC-0024874](../sources/history-136.md#src-0024874) 행126–128

<a id="claim-05"></a>

### H136-C05 · 저장 예측 재분석과 새 모델 실행의 구별

진단 코드는 기존early/later NPZ와 fitsJSON을 읽어 산술을 수행하도록 작성됐고, 기존 결과가 있으면 반복을 막는다. 이번 아카이브는 그112행을 읽기만 했으며 실행/import하지 않았다. 저장 결과의 새RCTL fit·새추론·새Tabcontext는 모두0이고 새 성능 실험이나 독립 모델 재현으로 세지 않는다. 보고서는 코드경로를 연결했지만 원결과에 코드SHA가 없어 실행 당시 코드판본의 독립고정은 미확인이다.

근거: [SRC-0022572](../sources/history-136.md#src-0022572) 행1–35 · [SRC-0022572](../sources/history-136.md#src-0022572) 행97–112 · [SRC-0024874](../sources/history-136.md#src-0024874) 행165–172 · [SRC-0020854](../sources/history-136.md#src-0020854) 행43–47 · [SRC-0024874](../sources/history-136.md#src-0024874) 행4–10

<a id="claim-06"></a>

### H136-C06 · 해시로 연결한 고정 입력

원106 결과의 early753997…/laterf2d5c4…/fits5531c0…/plan81b7a1…/ledger60b589…는 현재 확인한 정확사본과 일치했다. 기존 보존 NPZ2개와 fits·설정을 재사용한다. 현재root 원장17a549…는 다른 이후 판본의 보호대상으로 해시만 확인하며 당시ledger의 본문과 혼동하지 않는다.

근거: [SRC-0024874](../sources/history-136.md#src-0024874) 행4–10 · [SRC-0022572](../sources/history-136.md#src-0022572) 행18–35 · [SRC-0027514](../sources/history-136.md#src-0027514) 경로/SHA/크기 metadata · [SRC-0030211](../sources/history-136.md#src-0030211) 경로/SHA/크기 metadata · [SRC-0030237](../sources/history-136.md#src-0030237) 경로/SHA/크기 metadata · [SRC-0002031](../sources/history-136.md#src-0002031) 경로/SHA/크기 metadata

<a id="claim-07"></a>

### H136-C07 · 시간 위치와 개발 구간을 고정

고정 설정의 train168–839/validation840–1007/이후1008–1487은 각각672/168/480개 target위치다. 저장 배열은16cell×해당 길이이며 이후480시간을240시간씩 앞·뒤10일로 나눴다. 모든 기간은 이미 사용한 개발자료다. 위치만으로 새 독립시간 표본·새검증 구간이나 실제 timestamp를 추가 복구했다고 주장하지 않는다.

근거: [SRC-0030238](../sources/history-136.md#src-0030238) JSON /train_targets, /validation_targets, /test_targets · [SRC-0027514](../sources/history-136.md#src-0027514) NPZ train_y, validation_y · [SRC-0030211](../sources/history-136.md#src-0030211) NPZ y · [SRC-0020851](../sources/history-136.md#src-0020851) 행14–20 · [SRC-0024874](../sources/history-136.md#src-0024874) 행170–172 · [SRC-0022572](../sources/history-136.md#src-0022572) 행63–67

<a id="claim-08"></a>

### H136-C08 · signed scaled MAE와 예측기 구별

차이는 Tab-risk 소속으로 학습한 RCTL의 scaled MAE에서 empirical-risk 소속 RCTL의 scaled MAE를 뺀 값이다. 양수면 Tab 소속 쪽이 불리하다. 직접Tab 예측 MAE·원단위 MAE·평균과 cell별 손해를 섞지 않으며 현재 독립 단위복원이나 새정규화를 수행하지 않았다.

근거: [SRC-0020854](../sources/history-136.md#src-0020854) 행7–12 · [SRC-0020851](../sources/history-136.md#src-0020851) 행17–19 · [SRC-0030237](../sources/history-136.md#src-0030237) JSON /1/test_mean_scaled_mae, /5/test_mean_scaled_mae · [SRC-0022572](../sources/history-136.md#src-0022572) 행52–62

<a id="claim-09"></a>

### H136-C09 · 고정 학습 정책과 실제 epoch 차이

고정설정에는 MAE·batch256·patience10·lr0.001·Adam epsilon1e-7·최대80epoch가 명시됐다. 16개task의 seed/cluster/members가 선택fit과 일치했다. 실제epoch 합은 첫seed Tab221/empirical223, 둘째235/216이다. 같은 설정·sample 개수를 같은 최적화 경로 또는 자료 구성 원인의 통제로 확대하지 않는다.

근거: [SRC-0030238](../sources/history-136.md#src-0030238) JSON /loss, /batch_size, /patience, /learning_rate, /adam_eps, /max_epochs · [SRC-0030237](../sources/history-136.md#src-0030237) JSON /1/epochs_run, /2/epochs_run, /3/epochs_run, /4/epochs_run, /5/epochs_run, /6/epochs_run, /7/epochs_run, /8/epochs_run, /21/epochs_run, /22/epochs_run, /23/epochs_run, /24/epochs_run, /25/epochs_run, /26/epochs_run, /27/epochs_run, /28/epochs_run · [SRC-0020854](../sources/history-136.md#src-0020854) 행16–16 · [SRC-0030238](../sources/history-136.md#src-0030238) JSON /tasks/1, /tasks/2, /tasks/3, /tasks/4, /tasks/5, /tasks/6, /tasks/7, /tasks/8, /tasks/21, /tasks/22, /tasks/23, /tasks/24, /tasks/25, /tasks/26, /tasks/27, /tasks/28 · [SRC-0030237](../sources/history-136.md#src-0030237) JSON /1/seed, /1/cluster, /1/members, /2/seed, /2/cluster, /2/members, /3/seed, /3/cluster, /3/members, /4/seed, /4/cluster, /4/members, /5/seed, /5/cluster, /5/members, /6/seed, /6/cluster, /6/members, /7/seed, /7/cluster, /7/members, /8/seed, /8/cluster, /8/members, /21/seed, /21/cluster, /21/members, /22/seed, /22/cluster, /22/members, /23/seed, /23/cluster, /23/members, /24/seed, /24/cluster, /24/members, /25/seed, /25/cluster, /25/members, /26/seed, /26/cluster, /26/members, /27/seed, /27/cluster, /27/members, /28/seed, /28/cluster, /28/members

<a id="claim-10"></a>

### H136-C10 · 첫 seed의 평균 손해와 cell 범위

seed20260925의 train/validation/이후 평균차이는 +0.0033140586581/+0.00277302195762/+0.00572773873476이다. Tab 쪽이 불리한cell은 각각11/13/10개이며 이후 유리한6개도 CSV에 남아 있다. 이후 손해10/16만으로 모든cell에 같은 원인을 부여하지 않는다.

근거: [SRC-0024874](../sources/history-136.md#src-0024874) 행13–35 · [SRC-0024873](../sources/history-136.md#src-0024873) 행2–17 · [SRC-0020854](../sources/history-136.md#src-0020854) 행9–16

<a id="claim-11"></a>

### H136-C11 · 둘째 seed의 훈련 우열과 이후 손해

seed20260926의 train평균은 −0.000738153673453이지만 validation/이후는 +0.000161813045408/+0.00424376789209다. 불리한cell10/9/9개와 이후 유리한7개를 함께 보존한다. 음수 훈련평균과 이후 손해의 공존을 과적합 한 원인의 증명으로 쓰지 않는다.

근거: [SRC-0024874](../sources/history-136.md#src-0024874) 행72–94 · [SRC-0024873](../sources/history-136.md#src-0024873) 행18–33 · [SRC-0020854](../sources/history-136.md#src-0020854) 행11–16

<a id="claim-12"></a>

### H136-C12 · 훈련과 이후의 네 부호 조합

첫seed는 train불리/future불리8·불리/유리3·유리/유리3·유리/불리2, 둘째는 각각5·5·2·4cell이다. 1e-10 이내는 수치동점 정의이며 동등성 검정이 아니다. 이미 불리한 경우와 이후 뒤집힌 경우가 함께 있어 실패 원인을 하나로 묶지 않는다.

근거: [SRC-0024874](../sources/history-136.md#src-0024874) 행36–42 · [SRC-0024874](../sources/history-136.md#src-0024874) 행95–101 · [SRC-0022572](../sources/history-136.md#src-0022572) 행71–80 · [SRC-0020851](../sources/history-136.md#src-0020851) 행18–24 · [SRC-0024873](../sources/history-136.md#src-0024873) 행2–33

<a id="claim-13"></a>

### H136-C13 · 두 seed와 두 반구간의 손해를 별도로 보존

두seed에서 이후 평균이 모두 불리한cell은3765/4545/5353/5365/6145/6153/6165의7개다. 두seed와 앞·뒤10일을 모두 만족한 것은3765/4545/5353/6153의4개다. 한seed의 두 반구간 손해9/6개와 구별하고 이cell만 다음 평가에 선택하지 않는다.

근거: [SRC-0024874](../sources/history-136.md#src-0024874) 행149–163 · [SRC-0024874](../sources/history-136.md#src-0024874) 행42–42 · [SRC-0024874](../sources/history-136.md#src-0024874) 행101–101 · [SRC-0020854](../sources/history-136.md#src-0020854) 행14–14 · [SRC-0020851](../sources/history-136.md#src-0020851) 행20–20

<a id="claim-14"></a>

### H136-C14 · 날짜별 우열을 독립 실험으로 세지 않음

20개 날짜에서 Tab 쪽 평균이 불리한 날은 두seed 각각15일/14일이고 두seed 모두 불리한 것은11일이다. 나머지 날짜의 반대 방향도 저장daily_deltas에 남겼다. 날짜20개를 독립 실험20회로 세거나 유의성·원인 식별의 검정으로 바꾸지 않는다.

근거: [SRC-0024874](../sources/history-136.md#src-0024874) 행43–66 · [SRC-0024874](../sources/history-136.md#src-0024874) 행102–125 · [SRC-0024874](../sources/history-136.md#src-0024874) 행164–164 · [SRC-0020851](../sources/history-136.md#src-0020851) 행20–20 · [SRC-0020854](../sources/history-136.md#src-0020854) 행45–45

<a id="claim-15"></a>

### H136-C15 · 오차 차이 분해는 산술 항등식

이후차이=훈련차이+두방법의 이후−훈련 변화량 차이가 cell별로 성립한다. 평균 변화량 차이는0.00241368007666/0.00498192156554다. 이 항등식은 원인 기여율·과적합·자료구성의 인과 분해가 아니다.

근거: [SRC-0020851](../sources/history-136.md#src-0020851) 행19–19 · [SRC-0022572](../sources/history-136.md#src-0022572) 행68–70 · [SRC-0024874](../sources/history-136.md#src-0024874) 행66–66 · [SRC-0024874](../sources/history-136.md#src-0024874) 행125–125 · [SRC-0024873](../sources/history-136.md#src-0024873) 행1–33

<a id="claim-16"></a>

### H136-C16 · 저장 수치 검수와 독립 재현의 경계

기존 보존NPZ의 필요한41배열(early35/later6)을 stdlib로 해석해 scaled MAE·32CSV행·날짜별값 등250개 수치를 대조했다. CSV 최대차이0, 기존fit평균과의 최대차이1.013201350597015e-8로 원106 저장값과 일치했다. 이는 저장자료의 산술 검수이며 원code 실행·새 모델 추론/학습·독립 모델 재현이나 NPZ 모든배열 전문검토가 아니다.

근거: [SRC-0024874](../sources/history-136.md#src-0024874) 행165–172 · [SRC-0022572](../sources/history-136.md#src-0022572) 행29–70 · [SRC-0020854](../sources/history-136.md#src-0020854) 행45–45 · [SRC-0027514](../sources/history-136.md#src-0027514) NPZ cell_ids, train_y, validation_y · [SRC-0030211](../sources/history-136.md#src-0030211) NPZ cell_ids, y, tabicl_risk_20260925, empirical_risk_20260925, tabicl_risk_20260926, empirical_risk_20260926

<a id="claim-17"></a>

### H136-C17 · 보고된 원래 진단 시간과 회계

보고서0.029초/원결과0.02850919999764301초와 accountingJSON의 new_entry_seconds가 일치했다. 원코드는 최초hash 계산 뒤 배열로드/수치대조를 재고, 마지막hash확인·결과파일 출력 전에 시간을 저장한다. 원래 시간을 현재 다시 측정하거나 전체 작업·모델 실행 시간으로 확대하지 않는다.

근거: [SRC-0020854](../sources/history-136.md#src-0020854) 행45–47 · [SRC-0024874](../sources/history-136.md#src-0024874) 행165–169 · [SRC-0024871](../sources/history-136.md#src-0024871) 행1–6 · [SRC-0022572](../sources/history-136.md#src-0022572) 행18–28 · [SRC-0022572](../sources/history-136.md#src-0022572) 행97–110

<a id="claim-18"></a>

### H136-C18 · 변경 전후 원장을 정확SHA로 대조

회계의 before60b589…와 after98972…를 정확판본에 대조했다. 후자는 원108 활성화 전 보관본으로 남은 SHA이며 원108의 실행을 재개하지 않았다. 값의 차이는 진단비용 키1개와 같은 사건의 상세항목1개뿐이다. 사건은1회이고 used/caps/잔여/fit허용/reset/goalfalse는 그대로다. 전체JSON 값차이 검사와 현재 literal전문 판독은 구별한다.

근거: [SRC-0024871](../sources/history-136.md#src-0024871) 행1–6 · [SRC-0002031](../sources/history-136.md#src-0002031) JSON /used, /caps, /remaining_count_budgets, /budget_resets, /new_RCTL_fits_permitted_under_current_cap, /research_goal_complete, /new_cheap_diagnostic_seconds · [SRC-0020858](../sources/history-136.md#src-0020858) JSON /used, /caps, /remaining_count_budgets, /budget_resets, /new_RCTL_fits_permitted_under_current_cap, /research_goal_complete, /cheap_stage_details/8, /new_cheap_diagnostic_seconds/cellwise_transition_106

<a id="claim-19"></a>

### H136-C19 · 같은 sample 수가 설명하지 못하는 것

두K4의 모델당 sample 개수는 같고 훈련 우열도seed/cell에 따라 달랐다. 이는 자료 수 감소 하나로 같은K의 순위 차이를 설명하는 해석에 한계가 있다는 진단이다. input 구별 가능성·함께 학습한 자료 구성·시간 변화·최적화 변동은 여전히 식별되지 않았고 잘못 병합/분할했다는 원인을 증명하지 않는다.

근거: [SRC-0020854](../sources/history-136.md#src-0020854) 행14–18 · [SRC-0020851](../sources/history-136.md#src-0020851) 행7–9 · [SRC-0020851](../sources/history-136.md#src-0020851) 행24–26 · [SRC-0024874](../sources/history-136.md#src-0024874) 행170–172

<a id="claim-20"></a>

### H136-C20 · global 비교와 원UPC 재현을 구별

globalK1 대비K4의 앞선 손해는 모델 수와 자료량도 바뀐 비교다. 원106의 동일K 진단과 섞지 않는다. 보고서는 원UPC의10분·대규모 실험 재현도 아니라고 명시했다. 해당 과거 비교의 재인용을 이번 새실험 또는 독립 재현으로 세지 않는다.

근거: [SRC-0020854](../sources/history-136.md#src-0020854) 행18–18 · [SRC-0020851](../sources/history-136.md#src-0020851) 행9–9

<a id="claim-21"></a>

### H136-C21 · 후보 진입의 네 근거

다음 후보에는 실제 손해와 적용 범위, 경쟁 원인과 식별 한계, TabICLv2가 추정할 정보와 달라질 소속 결정, 큰학습 전에 원인을 구별할 최소 비교가 있어야 한다는 당시 기준을 남겼다. 직접Tab 예측 MAE가 작다는 것만으로 RCTL 공동학습 이득을 대신하지 않으며 성공 결과를 미리 요구하는 기준도 아니다.

근거: [SRC-0020854](../sources/history-136.md#src-0020854) 행20–29

<a id="claim-22"></a>

### H136-C22 · 다음 작업은 조건별 구성의 진단 명세

후속은 기존16cell·모든훈련sample의 조건별 자료 구성과 원인 구별 계획1개 고정이었다. 보고서는 기존13/14/19/23/25/80의 입력지원·조건위험을 재사용하고 같은거리/위험을 반복 계산하지 않도록 적었다. 이 지침은 당시 미완료 후속이며 현재 새연구 실행 지시나 그연결자료 전문재검토 완료가 아니다.

근거: [SRC-0020854](../sources/history-136.md#src-0020854) 행31–38 · [SRC-0020851](../sources/history-136.md#src-0020851) 행26–26

<a id="claim-23"></a>

### H136-C23 · 기본 특징과 신규성, 조건부 후보를 구별

달력·일/주lag가 이미 입력에 있어 새추가를 개선안으로 삼지 않는다던 보고서의 조건을 보존한다. 지원 차이가 미확인이면 threshold없는 기술통계와 두결과별 결정을 먼저 적고, 지원차이로 설명할 근거가 없으면 retrieval/거리/겹침 보정을 추천하지 않는다. 차이가 있더라도 가까운 조건부전이 방법과 결정 차이를 확인하기 전 신규성으로 쓰지 않는다.

근거: [SRC-0020854](../sources/history-136.md#src-0020854) 행35–39

<a id="claim-24"></a>

### H136-C24 · 새18fit을 시작했다는 결과는 아님

보고서는 신규 후보/원인구별 명세 뒤 작은예산을 편성하되 현재 새18fit을 시작하지 않았다고 썼다. 상태JSON의 ledger비활성화와 기존29fit상한·추가fit허용false도 일치한다. 후속 조건부계획과 저장배열 진단을 새 RCTL 검증의 완료로 바꾸지 않는다.

근거: [SRC-0020854](../sources/history-136.md#src-0020854) 행41–47 · [SRC-0020852](../sources/history-136.md#src-0020852) 행19–33 · [SRC-0024874](../sources/history-136.md#src-0024874) 행167–169 · [SRC-0020858](../sources/history-136.md#src-0020858) JSON /caps, /used, /new_RCTL_fits_permitted_under_current_cap

<a id="claim-25"></a>

### H136-C25 · 진단 완료와 연구 완료를 구별

결과JSON의 complete=true/stage106은 해당 저장예측 진단의 완료다. 상태JSON goal_complete=false와 과거Goal의 추천방향/직접근거/착수판단 조건은 별도다. 기각·진단·문서·참고목록/계획만으로 최종 연구 완료를 선언하지 않는다. 현재 전체기록 아카이브Goal도 미완료다.

근거: [SRC-0024874](../sources/history-136.md#src-0024874) 행1–3 · [SRC-0020852](../sources/history-136.md#src-0020852) 행5–8 · [SRC-0020853](../sources/history-136.md#src-0020853) 행238–250 · [SRC-0020854](../sources/history-136.md#src-0020854) 행1–3

<a id="claim-26"></a>

### H136-C26 · 판독·재사용·집계 분모와 미확인

현재14고유SHA/31물리경로·원본37고유경로를 확인했다. 새8raw687행을 전부읽고 settings72행/30선택위치·fit16개항목8필드/128선택위치와 부수적/0·원장7/9선택위치·NPZ41필요배열을 검수했다. 이전5사본 재사용과 literal전문/선택/산술을 구별한다. 이26주장 묶음은 공개문서 검수 뒤 신규내용만 한 번 집계하고 재사용·재독은 집계하지 않는다. 수정후Goal 정확판본·당시자동화/상태도구로그·남은Corpus/통합/접근/finaldelta/검색10+와전체Goal은미완료다.

근거: [SRC-0020851](../sources/history-136.md#src-0020851) 행28–30 · [SRC-0024874](../sources/history-136.md#src-0024874) 행165–173 · [SRC-0020852](../sources/history-136.md#src-0020852) 행3–17
