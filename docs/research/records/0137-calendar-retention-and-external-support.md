# 원107 자기 시간자료 보존과 다른 cell 입력의 근접성

**원107은 자기 시간·요일 sample은 남아 있지만, 같은 cluster에서 가까운 다른 cell 입력의 비중은 달랐다는 저장자료 진단이다.** 이 차이를 RCTL 손해의 원인으로 확정하지 않았다. 외부 입력 비중이 가장 큰 PCC 소속은 기존 RCTL 결과에서 가장 낮은 오차를 얻지 못했다.

[13출처/25경로](../sources/history-137.md) · [25주장](../verification/history-137-claims.json) · [작성 후 대조](../verification/history-137-second-pass.json) · [수치 검수](../evidence/0137-calendar-retention-and-external-support/saved-numeric-check.json) · [재검토 안내](../references/calendar-retention-and-external-support.md)

## 질문과 실제 수행

2026-09-26 [원106 같은 K 진단](0136-same-k-cellwise-error-transition.md)의 후속으로, 두 소속의 RCTL 차이를 자기 시간자료 누락 또는 가까운 외부 입력 부족으로 좁힐 수 있는지 물었다. 기존 [원23 조건부 공유 비용](0023-0025-conditional-pooling.md)의 density를 다시 합산했고, 거리 fit/검색·새 TabICL/RCTL·소속 선택은 수행하지 않았다고 기록했다. 현재 아카이브도 원코드 실행/import·모델 생성·훈련·추론·BatchNorm 계산을 수행하지 않았다.

자료는 기존 Milan internet hourly pilot의 고정16cell이다. 원107에서 cell 순서와 시간 범위를 다시 맞췄다. [기존 입력·정규화 기록](0033-0035-process-fit-gap.md)은 원시 index0–671의 cell별 평균 정규화, 최근8개 값과8특징으로 구성한 RCTL 입력을 설명한다. 이 선행 조건을 재사용하며 이번에 원자료/실제 forward 입력 전체를 새로 복구한 것으로 세지 않는다. 원107은 저장 입력의 이웃 비중과 소속을 다뤘다.

| 시간 위치 | 개수/cell | 이 진단의 역할 |
|---|---:|---|
| context168–671 | 504 | 원23 이웃 검색의 과거 입력 |
| query672–839 안 고정시점 | 64 | 저장 density 열의 query;16cell 합1024개 |
| RCTL train168–839 | 672 | 모든 query를 포함하는 훈련 범위 |
| validation840–1007 | 168 | 기존 pilot 설정; 새 평가 없음 |
| 기존test1008–1487 | 480 | 이미 관찰한 RCTL 성능만 재인용 |

고정 소속은 Tab-risk·empirical-risk·KNN-risk·PCC balanced·random balanced의 다섯 K4다. 각각4cluster·4cell/cluster이며 primary seed20260925의20개 task와20개 fit의 members가 일치한다. density를 그 seed로 모델 실행해 새로 만든 것은 아니다. RCTL의 기존 설정은 MAE·batch256·patience10·lr0.001·Adam epsilon1e−7·최대80epoch다. 이를 현재 실행 명령으로 적용하지 않는다.

## 보존된 개수와 달라지는 비중

훈련672시간은28일이다. weekday×hour168개 조합마다 자기cell4행, cluster16행이며 cluster 전체2688행이다. 모든 고정 K4가 각cell의672행을 유지하므로 자기 시간·요일 sample 수의 누락이라는 해석에 한계가 생긴다. 이 개수의 일치가 트래픽 수준·경로 분포의 일치는 아니다. 실제 실행 입력이 빠짐없이 저장됐다는 증명으로 확대하지 않는다.

원23 코드는 context 입력을 표준화한 뒤 가까운64개의 출처cell을 세어 k16/32/64 prefix의 비중을 저장했다. query별16cell 비중 합은1이다. 자기cell의 비중이own, 같은cluster의 다른cell 비중 합이external, 둘의 합이group이다. external은 group으로 다시 나눈 비율이 아니며,16cell×64query를 같은 가중으로 평균했다.

| 고정 소속 | external k16 | external k32 | external k64 | group=0 query k32 |
|---|---:|---:|---:|---:|
| Tab-risk | 10.2844% | 12.0300% | 13.1149% | 3 |
| empirical-risk | 15.1855% | 15.9424% | 16.3773% | 0 |
| KNN-risk | 11.5112% | 12.4908% | 13.4003% | 18 |
| PCC balanced | 22.0947% | 22.9004% | 23.4039% | 2 |
| random balanced | 10.6140% | 11.8591% | 13.1943% | 4 |

Tab−empirical 차이는 k16/32/64에서−4.9011/−3.9124/−3.2623 percentage points다. 세 k 모두16cell 중10개가 낮고6개가 높았다. k32에서4537/4565/5365/6137/6145/6165는 높았다. 반대 방향의 cell도 [전체 결과](../evidence/0137-calendar-retention-and-external-support/originals/SRC-0032345.json)의15조건·240개 cell별 비중에 보존했다. 이 부호를 RCTL 손해cell의 부호와 같은 지표로 합치지 않는다.

각cell의 앞32·뒤32 query를16cell에 평균한 차이는 두절반에서 모두 음수이며 k32는−3.2288/−4.5959 percentage points다. 개별cell마다 두절반이 음수라는 주장은 하지 않는다. query 절반은 훈련기간 안의 고정시점이며 원106의 이후 두10일 구간과 다르다. group=0 query도1024개 분모에 포함했고, k16/64의0 사례도 제거하지 않았다.

own 비중은 모든 소속에서 같지만 k16/32/64에 따라38.0981/32.3181/27.0462%다. 자기cell의 학습행 점유672/2688=25%와 이 이웃 비중은 다른 분모이며 독립 정보량의 비율도 아니다.

## RCTL 반례와 당시 판단

다음 값은 기존 primary seed20260925의4개 balanced cluster fit 평균을 같은 가중으로 합친 scaled MAE다. 새 예측이나 독립 재평가가 아니며 입력 비중과 척도가 다르다.

| 고정 소속 | 기존 RCTL scaled test MAE |
|---|---:|
| empirical-risk | 0.081600400 |
| KNN-risk | 0.084073085 |
| random balanced | 0.085597711 |
| Tab-risk | 0.087328134 |
| PCC balanced | 0.089877101 |

가장 큰 외부 근접 입력 비중을 가진PCC는 이 다섯에서 기존 오차가 가장 컸다. 이 반례는 가까운 다른cell sample을 많이 모으기만 하면 학습이 좋아진다는 주장을 지지하지 않는다. 조건부정답의 일치·독립적인 정보량·최종 RCTL 이득을 대신 측정한 결과는 아니다. 관계충돌·유한표본추정·최적화·평가절차 중 원인은 여전히 미식별이다.

당시 다음 후보를 단순히 '자료를 더 남긴다' 또는 '가까운 sample을 더 모은다'로 정하지 않았다. findings29행은 block당2개·전체12개 BatchNorm을 보고하고, 가중치와 소속을 고정한 훈련입력 통계 재계산을 다음 비교로 제안했다. 이 architecture 주장과 후속 비교를 이번 packet에서 새로 실행/검증하지 않았으며 원107 density 결과를 BN 성능 결과나 Tab/clustering 신규성으로 세지 않는다. 성능을 본 cell선택·혼합비율 tuning도 하지 않았다.

## 실패·비용·판본 한계

보고서와 결과는 처음에 RCTL로 검증하지 않은 추가 소속까지 읽어 균형검사 assertion으로 멈췄고, 원래계획의 다섯으로 대상을 정정한 뒤 한 번 완료했다고 남겼다. 현재 코드33–34행의 다섯 선택은 확인했으나 초기 실패 code판본·traceback·도구 로그는 미복구다. 정확한 실패소속/행을 독립 확정하지 않으며 이 범위 오류를 과학적 기각으로 세지 않는다.

실패process0.3895649초와 완료배열분석0.026969499987899326초를 합하면0.4165343999878993초다. 당시 보고 시간이며 현재 재측정한 모델시간이 아니다. 수정코드는 initialhash 뒤부터 로드/산술을 재고 finalhash/출력 전에 시간을 저장한다. 실패process 타이머의 상세 범위는 미복구다. plan의30초는 상한이다.

원108활성화전98972… 원장에는107 항목이 없다. 후속 원109회계전300d59…와 현재root17a549… 원장의 비용key 및 stage9 하나는 같은 실패포함비용·새fit/forward/call0을 보존했다. 한 사건이 두 위치에 남은 것이며 두번 합치지 않는다. 정확한 기입시점·원108의 다른 회계변경·전체원장 불변을 선택필드 확인으로 주장하지 않는다.

결과가 저장한 hash는 density/risk_predictions/partitions/training_settings/plan 다섯이며 실행코드 hash는 없다. 현재 보존code77598a…와 저장산술의 일치를 실행시점 코드판본의 독립 pin으로 표시하지 않고, code변경을 증명한 것으로도 읽지 않는다. risk 예측값은 이번 진단에서 읽지 않았다. [판본/로그 한계](../evidence/0137-calendar-retention-and-external-support/source-version-limits.json)를 함께 남겼다.

plan24행의 당시 goalactive·원106progress·차단감사 새시작 문장은 운영상태 보고다. [원106 과거상태](0136-same-k-cellwise-error-transition.md)와 함께 보존하며 nativeGoal 전환 도구응답을 이번에 복구하지 않았다. 현재 정리 Goal·감사·예산·자동화·모델 권한으로 적용하지 않는다.

## 재사용과 검수 범위

같은자료·같은소속의 반복 계산 전에 원23 density·원106 오차·원107 결과를 찾는다. 새 질문은 지원/조건부관계/유한표본/최적화·평가 중 무엇을 구별하며 입력·기간·정규화·소속의 무엇이 달라지는지 적는다. 저장 재분석과 새 모델 실험을 구별하고, 기존 달력/근접성 값을 바꿔 성능에 맞춘 소속을 고르지 않는다.

13고유SHA/25물리경로, 새정확사본5개73415bytes·기존8사본이다. 처음4literal전문3204행(결과JSON3067행)·원23code선택107행·연결JSON146pointer·NPZ8키를 읽었다. 저장 density 산술로15조건·모든2520calendar 원소·240cellmass·3comparison 등을2921회 대조해 차이0이었다. 이는 저장자료 검수이며 원모델 재현이 아니다.

작성후3원107raw137행+원23code34행=171행·결과의모든30compact node·연결JSON146pointer·NPZ8header/기존산술근거로25주장6그룹을 대조했다. 결과의 전체필드를 다시 읽었으나 literal3067행 새재독으로 세지 않는다. 원109/root 원장·fits/settings 전체literal 새독도 아니다. 원본30고유경로·보호6개는 불변이고 새모델0이다. 공개저장 실제읽기/문서QA 뒤 신규내용3비JSON전문·1literalJSON·1선택만 단회 집계한다.

308고유 원장의 자동 선택키 검색은308본문 완료가 아니다. 원108이후·긴고유판본/다른형식·전체통합/장기팀접근/최종원본delta/대표질문10+ 검색검수가 남아 있다. 이 작은 진단의complete·게시·병합을 전체 아카이브 완료와 구별한다.

## 주장별 근거

<a id="claim-01"></a>

### H137-C01 · 같은 K의 RCTL 차이를 묻는 저장 재분석

2026-09-26 원107은 동일 K4에서 Tab-risk와 empirical-risk 소속의 RCTL 차이를 자기 시간자료 누락 또는 가까운 외부 입력 부족으로 좁힐 수 있는지 물었다. 기존23 density를 재집계하는 후향 개발 진단이며 새 소속 선정이나 독립 성능 실험은 아니다. 원106의 같은K 비교를 연결하되 기록번호를 실험횟수로 세지 않는다.

근거: [SRC-0020856](../sources/history-137.md#src-0020856) 행3–14 · [SRC-0020855](../sources/history-137.md#src-0020855) 행3–3

<a id="claim-02"></a>

### H137-C02 · 저장 완료와 새 모델 0의 근거 범위

원결과 complete=true와 15개 저장 조건이 있으며 입력 density/소속으로 그 조건의 달력개수·비중·비교수치를 대조했다. 원107은 새 TabICL_calls/RCTL_calls/fits=0·inputs_unchanged=true를 기록했고 코드의 분석 경로도 저장 배열/JSON 로드와 산술이다. 당시 모델호출 도구로그나 실행시점 코드hash를 독립 복구한 것은 아니다. 현재 원코드 실행/import·모델생성·학습/추론/BN은0이다.

근거: [SRC-0032345](../sources/history-137.md#src-0032345) JSON /complete, /new_TabICL_calls, /new_RCTL_calls, /new_fits, /inputs_unchanged · [SRC-0023193](../sources/history-137.md#src-0023193) 행19–28 · [SRC-0023193](../sources/history-137.md#src-0023193) 행69–78 · [SRC-0020855](../sources/history-137.md#src-0020855) 행33–33

<a id="claim-03"></a>

### H137-C03 · 입력 SHA와 cell 순서의 고정

result의 density3f3fc7…/risk_predictions8ad282…/partitions4a91e2…/training_settings6467b3…/plan269e66… hash는 보존 원문과 일치한다. 3737/3745/3753/3765/4537/4545/4553/4565/5337/5345/5353/5365/6137/6145/6153/6165 순서는 density·risk metadata·partition·result에서 같다. risk의 실제 예측값은 원107과 이번 진단에서 로드하지 않았다.

근거: [SRC-0032345](../sources/history-137.md#src-0032345) JSON /source_hashes, /cell_ids · [SRC-0023588](../sources/history-137.md#src-0023588) JSON /cell_ids · [SRC-0025173](../sources/history-137.md#src-0025173) NPZ cell_ids, query_times · [SRC-0023605](../sources/history-137.md#src-0023605) NPZ cell_ids, context_times, query_times · [SRC-0023193](../sources/history-137.md#src-0023193) 행23–28

<a id="claim-04"></a>

### H137-C04 · 시간 구간과 개발자료의 경계

density context는168–671의504시간/cell이고 query는672–839 안의 고정64시점/cell·총1024개다. RCTL train168–839/validation840–1007/기존test1008–1487와 구별한다. 모든 density query는 전체 RCTL train 안에 있으며 이후480시간 지원 측정도 새 독립 평가도 아니다. 앞뒤32 query는 고정64시점의 절반이다.

근거: [SRC-0020856](../sources/history-137.md#src-0020856) 행11–14 · [SRC-0020855](../sources/history-137.md#src-0020855) 행23–23 · [SRC-0023193](../sources/history-137.md#src-0023193) 행25–32 · [SRC-0023605](../sources/history-137.md#src-0023605) NPZ context_times, query_times · [SRC-0030238](../sources/history-137.md#src-0030238) JSON /train_targets, /validation_targets, /test_targets

<a id="claim-05"></a>

### H137-C05 · 자기 시간·요일 기록 수의 보존

훈련 target672시간=28일이고 weekday×hour168조합마다 자기cell4행이다. 다섯 소속은 모두4cell/cluster여서 조합당16행·cluster당2688행·각cell672행이다. 15개 결과의 모든168개 calendar 원소가16이며 저장 설정/소속과 일치한다. 이는 명시된 고정 시간 격자와 자료 구성의 개수 검수이고 누락된 실행 입력 전체를 복구한 것은 아니다.

근거: [SRC-0020856](../sources/history-137.md#src-0020856) 행11–11 · [SRC-0020855](../sources/history-137.md#src-0020855) 행7–7 · [SRC-0023193](../sources/history-137.md#src-0023193) 행29–43 · [SRC-0032345](../sources/history-137.md#src-0032345) JSON /records/0, /records/1, /records/2, /records/3, /records/4, /records/5, /records/6, /records/7, /records/8, /records/9, /records/10, /records/11, /records/12, /records/13, /records/14

<a id="claim-06"></a>

### H137-C06 · 기존 입력 이웃 비중의 정의

원23 코드의 저장 density는 context 입력으로 StandardScaler를 맞춘 뒤 가까운64개 입력의 출처cell 빈도를 k16/32/64 prefix로 계산한다. 각query에서16cell 비중 합은1이다. 원107은 이 저장 비중만 재사용하며 거리 fit/검색·Tab/RCTL을 다시 실행하지 않았다. 목표 정답으로 근접성을 정한 진단이 아니다. 입력/정규화 상세는 기존 pilot에서 재사용하며 원107의 새 특징 설계가 아니다.

근거: [SRC-0022693](../sources/history-137.md#src-0022693) 행68–101 · [SRC-0020856](../sources/history-137.md#src-0020856) 행12–14 · [SRC-0025173](../sources/history-137.md#src-0025173) NPZ density_k16, density_k32, density_k64 · [SRC-0023193](../sources/history-137.md#src-0023193) 행44–50

<a id="claim-07"></a>

### H137-C07 · 비교 소속은 기존 훈련된 다섯 K4

tabicl_risk·empirical_risk·knn_risk·pcc_balanced·random_balanced의 고정 labels를 사용했다. 각 소속의4개 member집합은 RCTL seed20260925 task20개와 저장 fit20개에서 같고 소속을 재선택하지 않았다. density 자체는 이 RCTL seed로 모델을 다시 실행한 결과가 아니다. partition파일에는 median_only/median_iqr/cross_error_profile 이름도 있지만 이번 비교의 다섯에 포함하지 않는다.

근거: [SRC-0023193](../sources/history-137.md#src-0023193) 행33–43 · [SRC-0023588](../sources/history-137.md#src-0023588) JSON /cell_ids, /partitions/tabicl_risk, /partitions/empirical_risk, /partitions/knn_risk, /partitions/pcc_balanced, /partitions/random_balanced · [SRC-0030238](../sources/history-137.md#src-0030238) JSON /tasks/1, /tasks/2, /tasks/3, /tasks/4, /tasks/5, /tasks/6, /tasks/7, /tasks/8, /tasks/9, /tasks/10, /tasks/11, /tasks/12, /tasks/13, /tasks/14, /tasks/15, /tasks/16, /tasks/17, /tasks/18, /tasks/19, /tasks/20 · [SRC-0030237](../sources/history-137.md#src-0030237) JSON /1/method, /1/seed, /1/cluster, /1/members, /2/method, /2/seed, /2/cluster, /2/members, /3/method, /3/seed, /3/cluster, /3/members, /4/method, /4/seed, /4/cluster, /4/members, /5/method, /5/seed, /5/cluster, /5/members, /6/method, /6/seed, /6/cluster, /6/members, /7/method, /7/seed, /7/cluster, /7/members, /8/method, /8/seed, /8/cluster, /8/members, /9/method, /9/seed, /9/cluster, /9/members, /10/method, /10/seed, /10/cluster, /10/members, /11/method, /11/seed, /11/cluster, /11/members, /12/method, /12/seed, /12/cluster, /12/members, /13/method, /13/seed, /13/cluster, /13/members, /14/method, /14/seed, /14/cluster, /14/members, /15/method, /15/seed, /15/cluster, /15/members, /16/method, /16/seed, /16/cluster, /16/members, /17/method, /17/seed, /17/cluster, /17/members, /18/method, /18/seed, /18/cluster, /18/members, /19/method, /19/seed, /19/cluster, /19/members, /20/method, /20/seed, /20/cluster, /20/members · [SRC-0020856](../sources/history-137.md#src-0020856) 행14–14

<a id="claim-08"></a>

### H137-C08 · own·external·group 비중의 산술

query 소유cell의 비중이own이며 같은cluster 다른cell 비중을 합한 것이external, 둘의 합이group이다. external을group으로 나눈 조건부비율이 아니다. 각16cell×64query에 같은 가중치로 평균하고16cell별·앞32/뒤32query·group=0을 보존했다. cell별 평균을 다시 평균하면 전체 평균이다.

근거: [SRC-0023193](../sources/history-137.md#src-0023193) 행44–59 · [SRC-0020856](../sources/history-137.md#src-0020856) 행13–13 · [SRC-0032345](../sources/history-137.md#src-0032345) JSON /records/0, /records/1, /records/2, /records/3, /records/4, /records/5, /records/6, /records/7, /records/8, /records/9, /records/10, /records/11, /records/12, /records/13, /records/14

<a id="claim-09"></a>

### H137-C09 · k32 다섯 소속의 외부 비중

같은cluster 다른cell의 평균 비중은 k32에서 Tab12.030029296875%·empirical15.9423828125%·KNN12.4908447265625%·PCC22.900390625%·random11.859130859375%다. 보고서의12.03/15.94/12.49/22.90/11.86% 반올림과 일치하며 비중을 RCTL MAE로 읽지 않는다.

근거: [SRC-0020855](../sources/history-137.md#src-0020855) 행9–17 · [SRC-0032345](../sources/history-137.md#src-0032345) JSON /records/1, /records/4, /records/7, /records/10, /records/13

<a id="claim-10"></a>

### H137-C10 · k16/32/64에서 보존된 음의 차이

Tab−empirical external 차이는 k16 −0.04901123046875, k32 −0.03912353515625, k64 −0.032623291015625로 각각−4.901123/−3.912354/−3.262329 percentage points다. k는 이웃 수이고 소속 K4와 구별한다. 미리 정한 민감도 결과이며 이 값으로 새 k/소속/threshold를 선택하지 않았다.

근거: [SRC-0032345](../sources/history-137.md#src-0032345) JSON /comparisons · [SRC-0032345](../sources/history-137.md#src-0032345) JSON /records/0, /records/1, /records/2, /records/3, /records/4, /records/5 · [SRC-0020855](../sources/history-137.md#src-0020855) 행19–19 · [SRC-0020856](../sources/history-137.md#src-0020856) 행13–14

<a id="claim-11"></a>

### H137-C11 · 평균 아래에 남은 cell별 반대 방향

세 k 모두16cell 중 Tab external이 낮은10개·높은6개이며 동점0이다. main k32에서는4537/4565/5365/6137/6145/6165가 높았고3737/3745/3753/3765/4545/4553/5337/5345/5353/6153은 낮았다. 이 입력비중 부호를 원106의 RCTL 손해cell 부호와 같은 지표로 병합하지 않는다. 240개 cell별 mass와 반대 방향을 함께 보존했다.

근거: [SRC-0032345](../sources/history-137.md#src-0032345) JSON /comparisons · [SRC-0032345](../sources/history-137.md#src-0032345) JSON /records/0, /records/1, /records/2, /records/3, /records/4, /records/5 · [SRC-0020855](../sources/history-137.md#src-0020855) 행19–21

<a id="claim-12"></a>

### H137-C12 · 앞뒤 query 절반의 방향과 한계

각cell의 앞32·뒤32 query를 16cell 전체에 평균한 Tab−empirical external 차이는 세 k 모두 두절반에서 음수다. k32는−0.03228759765625/−0.04595947265625이며 전체차이는 두 값의 평균이다. 개별cell마다 두절반이 음수라는 주장은 하지 않는다. 이 절반은 훈련기간 안의 query이며 원106의 이후 두10일 구간과 다르다.

근거: [SRC-0032345](../sources/history-137.md#src-0032345) JSON /comparisons · [SRC-0023193](../sources/history-137.md#src-0023193) 행58–68 · [SRC-0020855](../sources/history-137.md#src-0020855) 행19–23

<a id="claim-13"></a>

### H137-C13 · 같은 자기자료 점유와 다른 이웃비중

각cluster 학습행에서 자기cell672/2688=1/4이라는 자료개수와 density own_mass는 다른 분모다. own_mass는 소속마다 같지만 k16/32/64에서0.3809814453125/0.32318115234375/0.2704620361328125다. 자기sample 개수의 보존을 가까운 입력비중25% 또는 독립 정보량25%로 바꾸지 않는다.

근거: [SRC-0020856](../sources/history-137.md#src-0020856) 행18–18 · [SRC-0023193](../sources/history-137.md#src-0023193) 행47–55 · [SRC-0032345](../sources/history-137.md#src-0032345) JSON /records/0, /records/1, /records/2, /records/3, /records/4, /records/5, /records/6, /records/7, /records/8, /records/9, /records/10, /records/11, /records/12, /records/13, /records/14

<a id="claim-14"></a>

### H137-C14 · group 비중이0인 query도 유지

group=0 query를 제외하지 않았다. k32의 Tab/empirical/KNN/PCC/random 개수는3/0/18/2/4이고 k16은9/10/37/12/12, k64는0/0/7/1/1이다. 평균 계산의 전체1024개 분모를 그대로 유지한다. 더큰k에서 남은0 사례도 보존하며0이 model 예측 실패를 뜻한다고 추정하지 않는다.

근거: [SRC-0020856](../sources/history-137.md#src-0020856) 행13–13 · [SRC-0023193](../sources/history-137.md#src-0023193) 행45–59 · [SRC-0032345](../sources/history-137.md#src-0032345) JSON /records/0, /records/1, /records/2, /records/3, /records/4, /records/5, /records/6, /records/7, /records/8, /records/9, /records/10, /records/11, /records/12, /records/13, /records/14

<a id="claim-15"></a>

### H137-C15 · PCC의 큰 외부 비중은 RCTL 우위를 주지 않았다

기존 seed20260925의20개 fit평균을 balanced4cell 가중으로 재집계하면 scaled test MAE는 empirical0.08160039968788624·KNN0.08407308533787727·random0.08559771068394184·Tab0.08732813410460949·PCC0.08987710066139698다. k32 external이 가장 큰PCC는 이 다섯의 기존 RCTL MAE가 가장 컸다. 이후480시간의 이미 관찰된 지표이며 새로운 예측/독립 평가가 아니다.

근거: [SRC-0020855](../sources/history-137.md#src-0020855) 행21–23 · [SRC-0030237](../sources/history-137.md#src-0030237) JSON /1/members, /1/test_mean_scaled_mae, /2/members, /2/test_mean_scaled_mae, /3/members, /3/test_mean_scaled_mae, /4/members, /4/test_mean_scaled_mae, /5/members, /5/test_mean_scaled_mae, /6/members, /6/test_mean_scaled_mae, /7/members, /7/test_mean_scaled_mae, /8/members, /8/test_mean_scaled_mae, /9/members, /9/test_mean_scaled_mae, /10/members, /10/test_mean_scaled_mae, /11/members, /11/test_mean_scaled_mae, /12/members, /12/test_mean_scaled_mae, /13/members, /13/test_mean_scaled_mae, /14/members, /14/test_mean_scaled_mae, /15/members, /15/test_mean_scaled_mae, /16/members, /16/test_mean_scaled_mae, /17/members, /17/test_mean_scaled_mae, /18/members, /18/test_mean_scaled_mae, /19/members, /19/test_mean_scaled_mae, /20/members, /20/test_mean_scaled_mae · [SRC-0030238](../sources/history-137.md#src-0030238) JSON /seed_primary, /test_targets

<a id="claim-16"></a>

### H137-C16 · 자료 누락·입력 근접성으로 원인을 확정하지 않음

시간·요일 sample 개수 보존은 이 고정 격자에서 자기자료 제거로 두 소속 차이를 설명하는 해석을 제한한다. 같은 트래픽 수준/경로 분포를 뜻하지 않는다. 가까운 다른cell sample은 조건부정답 일치·독립 정보량·RCTL 개선을 보장하지 않고 관계충돌/유한표본추정/최적화/평가절차 중 원인은 미식별이다.

근거: [SRC-0020855](../sources/history-137.md#src-0020855) 행7–7 · [SRC-0020855](../sources/history-137.md#src-0020855) 행21–29 · [SRC-0032345](../sources/history-137.md#src-0032345) JSON /causal_identification · [SRC-0020856](../sources/history-137.md#src-0020856) 행18–20

<a id="claim-17"></a>

### H137-C17 · 처음의 추가 소속 오류와 정정

보고서와 결과는 처음에 다섯 외의 미훈련 소속까지 읽어 균형검사 assertion으로 멈췄으며 원래계획의 다섯으로 범위를 정정한 뒤 한 번 완료했다고 기록한다. corrected 코드33–34행은 다섯만 선택한다. 초기 실패 code판본/traceback/원도구 로그는 이번 packet에서 복구하지 못했으므로 정확한 실패소속·중단행을 독립 확정하지 않는다. 구현/범위 오류를 근접성 방법의 과학적 기각으로 세지 않는다.

근거: [SRC-0020855](../sources/history-137.md#src-0020855) 행33–33 · [SRC-0032345](../sources/history-137.md#src-0032345) JSON /prior_failure, /prior_failed_process_seconds · [SRC-0023193](../sources/history-137.md#src-0023193) 행33–43 · [SRC-0023193](../sources/history-137.md#src-0023193) 행74–75

<a id="claim-18"></a>

### H137-C18 · 실행시점 코드 판본의 한계

result source_hashes는 density/risk_predictions/partitions/training_settings/plan 다섯이며 실행코드 hash는 없다. 현재 보존 코드77598a…가 산술과 일치하는 것을 실행시점 코드판본의 독립 pin으로 표시하지 않는다. 당시 code가 바뀌었다고 증명한 것도 아니다. 실패 시간/문장은 수정후 코드의 상수와 저장결과/보고에 남아 있다.

근거: [SRC-0032345](../sources/history-137.md#src-0032345) JSON /source_hashes, /prior_failure, /prior_failed_process_seconds · [SRC-0023193](../sources/history-137.md#src-0023193) 행17–18 · [SRC-0023193](../sources/history-137.md#src-0023193) 행69–78 · [SRC-0023193](../sources/history-137.md#src-0023193) 경로/SHA/크기 metadata

<a id="claim-19"></a>

### H137-C19 · 성공·실패 비용과 측정 범위

원결과의 완료 배열분석0.026969499987899326초와 최초 실패process0.3895649초를 합한 비용은0.4165343999878993초다. 현재 다시 측정한 모델시간이 아니다. corrected code는 초기 hash 뒤부터 로드/산술을 재고 finalhash/출력 전에 시간을 저장한다. 최초실패 process의 타이머 범위는 별도 로그로 복구하지 않았다. plan의30초는 상한이며 사용량과 구별한다.

근거: [SRC-0032345](../sources/history-137.md#src-0032345) JSON /arithmetic_seconds, /prior_failed_process_seconds · [SRC-0023193](../sources/history-137.md#src-0023193) 행17–22 · [SRC-0023193](../sources/history-137.md#src-0023193) 행69–78 · [SRC-0020856](../sources/history-137.md#src-0020856) 행24–24 · [SRC-0020855](../sources/history-137.md#src-0020855) 행33–33

<a id="claim-20"></a>

### H137-C20 · 후속 원장의 실패 포함 단일 사건

원108활성화전 ledger98972…의 비용map/상세에 원107 항목은 없다. 후속 원109 회계전300d59…와 현재root17a549…에는 support_composition_107 비용key0.4165343999878993 및 stage9 하나가 같은 실패/성공시간·새fit/forward/call0·cost_not_counted_twice=true로 남아 있다. 두 위치에 기록된 한 사건이며 두번 비용을 합치지 않는다. 정확한 기입시점·원108 관련 다른 회계변경·전체ledger 불변을 이번 선택필드 확인으로 확정하지 않는다.

근거: [SRC-0020858](../sources/history-137.md#src-0020858) JSON /new_cheap_diagnostic_seconds, /cheap_stage_details · [SRC-0032507](../sources/history-137.md#src-0032507) JSON /new_cheap_diagnostic_seconds/support_composition_107, /cheap_stage_details/9 · [SRC-0022700](../sources/history-137.md#src-0022700) JSON /new_cheap_diagnostic_seconds/support_composition_107, /cheap_stage_details/9

<a id="claim-21"></a>

### H137-C21 · 당시 후속 BN 비교는 원107 실행결과가 아님

findings29행은 RCTL 각block 두개·전체12 BatchNorm을 보고하고 기존가중치/소속을 고정해 훈련입력만으로 통계를 다시 계산하는 한요소 비교를 다음 작업으로 제안했다. 이 문장의 architecture 주장과 그 비교를 이번 packet에서 새로 실행/검증하지 않았다. 원107의15 density조건을 BN 성능 결과나 Tab/clustering 신규성으로 세지 않고 성능을 본 cell선택/혼합비율 tuning도 하지 않는다.

근거: [SRC-0020855](../sources/history-137.md#src-0020855) 행25–29 · [SRC-0020856](../sources/history-137.md#src-0020856) 행19–20 · [SRC-0032345](../sources/history-137.md#src-0032345) JSON /new_RCTL_calls, /new_fits

<a id="claim-22"></a>

### H137-C22 · 과거 Goal·감사·예산 문장과 현재 과제

plan24행의 goalactive·원106progress·차단반복감사 새시작은 당시 운영상태 보고다. 이 문장만으로 nativeGoal 상태전환 도구응답을 검증하지 않았다. 앞선 원106의 상태자료와 연결해 이 차이를 보존하며 현재 Goal감사/재개/예산변경/자동화생성/모델권한으로 적용하지 않는다.

근거: [SRC-0020856](../sources/history-137.md#src-0020856) 행24–24

<a id="claim-23"></a>

### H137-C23 · 재사용과 재검토 조건

이 저장분석을 같은자료·같은fiveK4로 다시 수행하기 전에 원23 density/원106 저장오차/원107 결과를 재사용한다. 새 질문은 지원/조건부관계/유한표본/최적화·평가 중 무엇을 구별하고 입력·기간·정규화·소속의 어떤 조건이 달라지는지 적어야 한다. 단순 추가sample·근접입력 수 증가를 원인 해결 또는 Tab 신규성으로 승격하지 않는다. 현재 실험을 수행하라는 지시가 아니다.

근거: [SRC-0020856](../sources/history-137.md#src-0020856) 행18–20 · [SRC-0020855](../sources/history-137.md#src-0020855) 행21–29

<a id="claim-24"></a>

### H137-C24 · 원본 보존과 선택 읽기의 구분

13고유SHA/25물리경로와 보호6개를 대조해 중복을 제거한30원본경로가 불변이었다. 새정확사본 대상은5개73415bytes이며 나머지8개는 기존정확사본을 연결한다. 원107 first4literal전체3204행과 원23code선택107행·JSON146pointer·NPZ8필요키를 구별한다. 원109/root 원장·settings/fits/partitions 전체literal새독을 했다고 세지 않는다.

근거: [SRC-0020856](../sources/history-137.md#src-0020856) 경로/SHA/크기 metadata · [SRC-0020855](../sources/history-137.md#src-0020855) 경로/SHA/크기 metadata · [SRC-0023193](../sources/history-137.md#src-0023193) 경로/SHA/크기 metadata · [SRC-0032345](../sources/history-137.md#src-0032345) 경로/SHA/크기 metadata · [SRC-0032507](../sources/history-137.md#src-0032507) 경로/SHA/크기 metadata · [SRC-0025173](../sources/history-137.md#src-0025173) 경로/SHA/크기 metadata · [SRC-0023605](../sources/history-137.md#src-0023605) 경로/SHA/크기 metadata · [SRC-0023588](../sources/history-137.md#src-0023588) 경로/SHA/크기 metadata · [SRC-0030238](../sources/history-137.md#src-0030238) 경로/SHA/크기 metadata · [SRC-0030237](../sources/history-137.md#src-0030237) 경로/SHA/크기 metadata · [SRC-0022693](../sources/history-137.md#src-0022693) 경로/SHA/크기 metadata · [SRC-0020858](../sources/history-137.md#src-0020858) 경로/SHA/크기 metadata · [SRC-0022700](../sources/history-137.md#src-0022700) 경로/SHA/크기 metadata

<a id="claim-25"></a>

### H137-C25 · 아카이브 전체 완료와 다른 작은 packet

새본문 단회 집계 대상은 비JSON전문3·literalJSON1·선택원장1이며 재독/재사용/저장산술은 신규집계0이다. 308고유 원장판본의 자동 선택키 검색을308개 본문검토 완료로 표시하지 않는다. 원108이후·긴고유판본/다른형식·통합/장기팀접근/최종원본delta/대표질문10+ 검색검수는 남아 있고 원107 complete를 전체 연구Goal 완료로 읽지 않는다.

근거: [SRC-0020856](../sources/history-137.md#src-0020856) 경로/SHA/크기 metadata · [SRC-0020855](../sources/history-137.md#src-0020855) 경로/SHA/크기 metadata · [SRC-0023193](../sources/history-137.md#src-0023193) 경로/SHA/크기 metadata · [SRC-0032345](../sources/history-137.md#src-0032345) 경로/SHA/크기 metadata · [SRC-0032507](../sources/history-137.md#src-0032507) 경로/SHA/크기 metadata
