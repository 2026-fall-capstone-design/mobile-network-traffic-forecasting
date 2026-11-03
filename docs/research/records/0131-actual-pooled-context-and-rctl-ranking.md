# 원101 — 실제 pooled context와 RCTL 소속 순위

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

**TabICL은 이 구간에서 직접 예측이 좋았지만, 같은 K4 소속 두 개의 순위는 저장된 RCTL 결과와 반대였다.** 2026-09-26 원101은 B2의 대리 위험식만 살핀 이전 진단을 보완해 실제 학습 sample을 context로 주었다. 직접 예측의 긍정 근거와 소속 대리점수의 한계를 함께 보존한다.

[36출처/153사본](../sources/history-131.md) · [36주장](../verification/history-131-claims.json) · [작성 후 원문 대조](../verification/history-131-second-pass.json) · [실제 읽기 범위](../evidence/0131-actual-pooled-context-and-rctl-ranking/read-scopes.json) · [917수치 검산](../evidence/0131-actual-pooled-context-and-rctl-ranking/numeric-check.json) · [재사용·비교 안내](../references/pooled-context-and-learner-ranking.md)

## 질문과 실제 수행

질문은 같은 소속의 실제 sample을 TabICL context로 주면 RCTL이 선호한 소속의 순위와 일치하는가였다. 이전 B2는 group-average 휴리스틱이었다. 이번 context도 504→672시간으로 달라져, 결과 차이를 위험식 제거 하나의 효과로 분해할 수 없다.

당시 Tab context 9개/총 query16,128행과 Ridge·HGB fit18개를 실행했다. 기존 RCTL5개 저장 예측을 같은 구간으로 잘라 비교했으며 새 RCTL 학습은 0이었다. 현재 정리는 저장 배열의 산술과 원문·보관 코드만 확인했다. 원코드를 실행하거나 import하지 않았다.

## 자료·시간·입력 조건

| 항목 | 조건과 비교 한계 |
|---|---|
| 대상 | 고정16cell, global K1 / Tab-risk K4 / empirical-risk K4 |
| 학습 context | 시간 index168–839, cell당672행 |
| query | index1008–1343, cell당336행·14일; 이미 살핀 개발 자료 |
| early-stop 구간 | RCTL의840–1007 정답을 Tab context/query 정답에서 제외; 이후 query의 lag에는 과거 실측을 사용 |
| Tab/Ridge/HGB | 최근8lag, lag24/168, 최근24시간 평균·표준편차, hour/weekday sin·cos의16열; cellID 없음 |
| 저장 RCTL | 같은16개 기초값에서 lag8개를 순서축으로, 나머지8값을 각 step에 반복해8step×9channel 입력 |
| 정규화·척도 | 기존 최초28일 cell 평균 척도; cell별 정규화 MAE와 cell 동등 비중 |
| 예측 단위 | 매 시점 과거 실측 lag를 쓰는 rolling one-step; 336시간 open-loop 재귀 예측은 아님 |
| 독립성 | 소속과 RCTL 결과를 계획 전에 알고 있던 사후 비교; 새 독립 test/눈가림/유의성 검정은 아님 |

저장된672행 학습 prefix와 scales는 기존32cell design의 같은16cell 부분과 정확히 일치한다. 최종 actual/RCTL5배열은 기존16×480 예측의 첫336시점 slice와 정확히 일치한다. 입력의 기초 정보가 겹쳐도 표현·학습방식·validation 사용은 다르므로, Tab↔RCTL 차이를 사전학습 목적 하나의 영향으로 단정하지 않는다.

## 직접 예측과 소속 순위

낮은 정규화 MAE가 좋다. 아래는 같은16cell·336시점의 전체 평균이다. secondary RCTL seed의 global은 이번 진단에 없다.

| 방법 | global K1 | Tab-risk K4 | empirical-risk K4 |
|---|---:|---:|---:|
| TabICL | 0.0661831498 | 0.0732450262 | 0.0754066780 |
| Ridge | 0.0792279392 | 0.0867867023 | 0.0824412778 |
| HGB | 0.0715707839 | 0.0917004198 | 0.0845967904 |
| RCTL seed20260925 | 0.0728736073 | 0.0860022232 | 0.0798649788 |
| RCTL seed20260926 | 미실행 | 0.0880958885 | 0.0836716741 |

Tab global은 HGB보다7.5277%, Ridge보다16.4649% 낮은 MAE였고 앞/뒤7일에도 직접 예측의 우열이 같았다. 이 직접 예측 결과와, Tab의 점수로 다른 learner의 소속을 선택할 수 있는가는 별도다.

아래 delta는 Tab-risk minus empirical-risk다. 음수면 Tab-risk가 좋다. 전체 평균과 기간·cell의 예외를 함께 읽는다.

| 방법 | 전체14일 | 앞7일 | 뒤7일 | Tab-risk 우위 cell | Tab-risk 우위 day |
|---|---:|---:|---:|---:|---:|
| TabICL | -0.0021616463 | +0.0001634610 | -0.0044867527 | 6/16 | 10/14 |
| Ridge | +0.0043454198 | +0.0004083271 | +0.0082825124 | 5/16 | 2/14 |
| HGB | +0.0071036257 | +0.0029659546 | +0.0112412972 | 6/16 | 2/14 |
| RCTL25 | +0.0061372463 | +0.0031368041 | +0.0091376882 | 5/16 | 2/14 |
| RCTL26 | +0.0044242158 | +0.0013330898 | +0.0075153420 | 6/16 | 4/14 |

전체14일 평균은 global이 가장 좋았지만 앞7일에는 Tab empirical, Ridge의 두K4, HGB empirical이 global보다 조금 좋았다. Tab의 두K4 순위도 앞/뒤주에 뒤집혔다. 전체 평균을 모든 cell·시점·다른 소속의 보편적 실패로 확대하지 않는다. cell/day별 저장 차이는 [summary 원문](../evidence/0131-actual-pooled-context-and-rctl-ranking/originals/SRC-0001984.json)에 남아 있다.

## 구현·비용을 재사용할 때

당시 seed20260925/ensemble1/CPU batch1/kv_cache=False, AMP·FA3·offload·auto-download=False와 median 출력을 사용했다. fit은 checkpoint와 context 변환을 준비하며 가중치 재학습 optimizer가 아니다. query 정답은 평가용이며 driver의 predict 인자에 없다.

설정의 초기 PyTorch intra/inter-op은4/2지만 driver의 n_jobs=1 때문에 보관 regressor는 predict 중 intra-op을1로 바꾸고 정상 종료 시 복원한다. 호출별 thread 로그는 없으므로138.2582초를 “4thread 추론 실측”으로 쓰지 않는다. OMP/MKL/OPENBLAS 환경값과 이 코드 범위도 구별한다.

Tab accounted fit/predict138.2582043초, cheap2.2270844초, stage140.4852887초였다. simple fit1.0048376초는 cheap에 포함된다. 초기 import·설정·source hash는 측정 전이며 sampled RSS최대2,602,754,048bytes는0.2초 간격 관측값이다. global Tab69.1113초와 K4합34.4148/34.7321초는 이번 context 크기/설정의 비용이다. RCTL 운영 속도나10,000cell 비용으로 외삽하지 않는다.

보관 공식 구현4파일의 고정 Git commit 바이트를 대조했다. default embed_with_test=False, context target embedding, 일부 context K/V 제한과 median 경로를 확인했다. 선택 밖 preprocessing·ICLearning·attention·inference-manager의 전체 호출 경로는 미검증이므로 전체 누수 감사로 쓰지 않는다.

## 당시 판단과 재검토 조건

실제 context 진단은 대리 위험식만의 문제로 한계를 좁힐 수 없다는 관찰을 추가했다. 공통 context 검사를 다시 붙이는 것, 단순 점수 혼합, attention 거리나 새 모듈을 곧바로 최종안으로 추천하지 않았다. 좋은 직접 예측 근거는 유지했고, 유용한 소속 결정 또는 같은 결정의 추정·계산 효율에서 Tab의 기여를 특정하는 것이 남았다. 당시 최종 추천과 Word는 미완료였다.

같은 질문을 다시 실험하기 전에 저장 입력·소속·예측·주간/cell별 차이·설정·시간 범위를 읽는다. 미래 관측의 유무, 입력 표현, validation 사용, 기준 learner와 K1 비교 중 무엇을 바꾸는지 명시한다. 원문 속 Goal·다음 행동·명령·예산은 역사적 자료다.

## 주장별 근거

<a id="claim-01"></a>

### H131-C01 · 원101의 실제 진단과 현재 정리 작업

2026-09-26 원101은 기존 16cell의 global K1·Tab-risk K4·empirical-risk K4에 실제 sample을 함께 넣어 비교한 사후 진단이다. 당시 Tab9context/16,128query와 Ridge·HGB18fit은 완료 로그·저장 결과에 연결되고 새 RCTL fit/forward/gradient는0이다. 현재 정리에서는 원코드 실행/import·모델생성·새 학습/추론0이며 당시 수행을 다시 시작하지 않는다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행1–9 · [SRC-0001980](../sources/history-131.md#src-0001980) JSON /success, /contexts_completed, /query_rows_attempted, /simple_fits, /new_RCTL_fits, /new_RCTL_forwards, /new_RCTL_gradients

<a id="claim-02"></a>

### H131-C02 · B2 위험 합산과 실제 context의 차이

B2는 cell별 Tab 분포로 공통 Ridge 예측+상태 수정값의 손해를 합산했으며 실제 pooled Tab을 실행한 결과가 아니다. 원101은 실제 context를 평가하지만 B2의 cell당504행과 원101의672행도 다르므로 달라진 결과를 대리 계산식 제거 하나의 인과 효과로 해석하지 않는다. 과거14·19의 cell 정보/입력 진단과도 세 partition의 직접 비교 범위를 구별한다.

근거: [SRC-0001964](../sources/history-131.md#src-0001964) 행7–17 · [SRC-0001965](../sources/history-131.md#src-0001965) 행11–21

<a id="claim-03"></a>

### H131-C03 · 고정된 소속과 사후 비교의 독립성 한계

세 소속은 원래 RCTL 학습 전에 고정한 global·Tab-risk·실제 관측 정답 risk 구성이고 두K4는 각각4cell씩4그룹이다. 현재 저장 소속은 기존 observed-risk 자료와 일치한다. 원101은 새 점수를 고정한 뒤 저장 RCTL과 대조했지만 RCTL 결과는 계획 전부터 알려져 있었으므로 눈가림·독립 신규 test가 아니다. 기존 소속을 다시 선택한 실험으로 쓰지 않는다.

근거: [SRC-0001964](../sources/history-131.md#src-0001964) 행9–18 · [SRC-0001982](../sources/history-131.md#src-0001982) JSON /groups_local_index, /partition_selection_uses_new_results, /independent_test, /known_scope · [SRC-0023588](../sources/history-131.md#src-0023588) JSON /cell_ids, /partitions/tabicl_risk, /partitions/empirical_risk

<a id="claim-04"></a>

### H131-C04 · 시간 분할과 이미 열람한 평가 기간

context target은168–839의672시간, query는1008–1343의336시간·연속14일이며 cell당 동일하다. query target에서 RCTL early-stopping840–1007을 제외했지만 기존20일 평가의 첫14일로 이미 열람한 개발 기간이다. 학습·validation·query의 구분을 독립 미래 일반화 증거로 승격하지 않는다.

근거: [SRC-0001964](../sources/history-131.md#src-0001964) 행14–18 · [SRC-0001965](../sources/history-131.md#src-0001965) 행17–21 · [SRC-0001982](../sources/history-131.md#src-0001982) JSON /context_targets, /query_targets, /independent_test · [SRC-0001976](../sources/history-131.md#src-0001976) NPZ context_times, query_times

<a id="claim-05"></a>

### H131-C05 · 입력·정규화와 원 자료의 결합

입력은 최근8시간, lag24/168, 최근24시간 평균/표준편차와 query시각의 hour/weekday sin·cos인16열이다. cell ID를 새 입력으로 넣지 않았고 기존 최초28일 cell 평균 척도를 유지했다고 보고했다. 저장X/Y의672학습 prefix와 scales는 기존32cell design에서같은16cell을선택한자료와정확히일치한다. 여기서는 저장 척도를 대조했으며 raw traffic 평균이나 특징을 새로 생성하지 않았다. 이전 RCTL은 같은16개 기초값 중8lag를 순서축으로 놓고 나머지8값을 각step에 반복해8×9 입력으로 만들었다. 따라서 관측값·기초변수와 일치하는 부분이 있어도 Tab/Ridge/HGB의16열 표현과 RCTL의8step×9channel 입력 형식은 다르다.

근거: [SRC-0001964](../sources/history-131.md#src-0001964) 행16–18 · [SRC-0001968](../sources/history-131.md#src-0001968) 행113–134 · [SRC-0001982](../sources/history-131.md#src-0001982) JSON /features · [SRC-0001976](../sources/history-131.md#src-0001976) NPZ X, Y, scales · [SRC-0023577](../sources/history-131.md#src-0023577) NPZ X, Y, cell_indices, scales · [SRC-0023202](../sources/history-131.md#src-0023202) 행59–67 · [SRC-0023202](../sources/history-131.md#src-0023202) 행84–90 · [SRC-0023048](../sources/history-131.md#src-0023048) 행25–60

<a id="claim-06"></a>

### H131-C06 · 학습·query 행 수의 집계 단위

global은context10,752/query5,376행, 각K4는그룹당2,688/1,344행이다. 9context 전체 호출합계는context32,256/query16,128행으로 같은10,752학습행·5,376query를 세소속에서 반복한 값이다. 서로 다른 독립 표본 수가 아니며 context를100행으로 잘라내지 않았다. 같은 cell에672학습행/336query를 보장한다.

근거: [SRC-0001964](../sources/history-131.md#src-0001964) 행17–25 · [SRC-0001968](../sources/history-131.md#src-0001968) 행137–144 · [SRC-0001975](../sources/history-131.md#src-0001975) JSON /0/context_rows, /0/query_rows, /1/context_rows, /1/query_rows · [SRC-0001980](../sources/history-131.md#src-0001980) JSON /contexts_completed, /query_rows_attempted

<a id="claim-07"></a>

### H131-C07 · Tab의 선택 설정과 재학습 없는 fit

진단 코드는 seed20260925, ensemble1, CPU·batch_size1·kv_cache=False·AMP/FA3/offload=False와 allow_auto_download=False를 지정했다. fit은 checkpoint config/state_dict를 읽고 eval과 context 전처리를 준비하며 가중치 최적화가 아니다. 기록 checkpoint SHA와 version정보를 보존하고, 이번 아카이브에서는 checkpoint를 불러오거나 모델을 만들지 않았다.

근거: [SRC-0001968](../sources/history-131.md#src-0001968) 행148–164 · [SRC-0001982](../sources/history-131.md#src-0001982) JSON /seed, /ensemble, /output, /hashes/checkpoint, /versions · [SRC-0001989](../sources/history-131.md#src-0001989) 행346–355 · [SRC-0001989](../sources/history-131.md#src-0001989) 행406–446

<a id="claim-08"></a>

### H131-C08 · 초기 스레드 값과 predict의 임시 변경

settings의 PyTorch intra/inter-op4/2와 계획의CPU4thread는 predict 전에 기록한 값이다. 진단은 n_jobs=1을 넘기며 보관 regressor의 predict는688–703에서 intra-op을1로 바꾸고 정상 종료754–755에서 이전 값으로 복원한다. 따라서138초 측정을4thread 추론 실측이라고 반복하지 않는다. OMP/MKL/OPENBLAS4 및 inter-op2와 구별하고 호출 중 별도 스레드 로그는 미기록으로 남긴다.

근거: [SRC-0001964](../sources/history-131.md#src-0001964) 행23–24 · [SRC-0001968](../sources/history-131.md#src-0001968) 행1–18 · [SRC-0001968](../sources/history-131.md#src-0001968) 행148–160 · [SRC-0001982](../sources/history-131.md#src-0001982) JSON /torch_threads, /torch_interop_threads · [SRC-0001989](../sources/history-131.md#src-0001989) 행688–703 · [SRC-0001989](../sources/history-131.md#src-0001989) 행754–760

<a id="claim-09"></a>

### H131-C09 · 단순 비교군의 고정 손실·설정

Ridge는 StandardScaler+alpha1의 제곱손실 학습이고 MAE로 평가한다. HGB는 absolute_error,100iter,lr.1,leaf15,min_samples20,l2=1,early_stopping=False와 동일seed를 썼다. 같은 context/query에서 각각9fit·총18fit이며 새로운 튜닝이 아니다. Ridge의 학습 손실을 MAE라고 바꾸어 기록하지 않는다.

근거: [SRC-0001964](../sources/history-131.md#src-0001964) 행24–27 · [SRC-0001968](../sources/history-131.md#src-0001968) 행175–197 · [SRC-0001980](../sources/history-131.md#src-0001980) JSON /simple_fits · [SRC-0001983](../sources/history-131.md#src-0001983) 행1–110

<a id="claim-10"></a>

### H131-C10 · context 표적과 query 인자의 구별

driver는fit(cx,cy)에 contextY[:672]를 주고 predict(qx)에 queryX만 준다. qy는 저장·평가에 사용한다. 보관 regressor는 context target scaler와 input/ensemble fit 호출을 분리하고 query에서는 transform을 호출하며 no_grad로 predict_stats를 계산한다. 이는 읽은 인자/호출 경로의 확인이며 수집 밖 preprocessing 전체 구현이나 모든 설정의 누수 없음을 증명한 것은 아니다.

근거: [SRC-0001968](../sources/history-131.md#src-0001968) 행129–164 · [SRC-0001989](../sources/history-131.md#src-0001989) 행417–434 · [SRC-0001989](../sources/history-131.md#src-0001989) 행525–536 · [SRC-0001989](../sources/history-131.md#src-0001989) 행705–735

<a id="claim-11"></a>

### H131-C11 · default embedding·context K/V의 확인 범위

선정4파일에서 predict_stats의 embed_with_test=False 기본, column target embedding의contextprefix 추가와 train_size 전달, ISAB 첫 단계 및 MultiheadAttentionBlock의context K/V 제한을 읽었다. 실제 ICLearning/SetTransformer/attention/inference-manager callee와 preprocessing 본문은 이4파일 밖이므로 완전한 end-to-end 누수 감사로 쓰지 않는다. 분류·mixed-radix·cache 분기를 읽은 사실을 원101의 활성 경로 실행으로 세지 않는다.

근거: [SRC-0001988](../sources/history-131.md#src-0001988) 행524–585 · [SRC-0001986](../sources/history-131.md#src-0001986) 행340–421 · [SRC-0001987](../sources/history-131.md#src-0001987) 행432–454 · [SRC-0001987](../sources/history-131.md#src-0001987) 행625–665

<a id="claim-12"></a>

### H131-C12 · median 예측과 rolling one-step 평가

Tab 출력은 quantile 분포 icdf(.5) median이며 target 역변환 후 ensemble 평균을 낸다. 입력은 각query시점의 직전 실측 lag와 calendar를 사용하므로14일은336개 rolling one-step 평가 구간이다. 336시간 open-loop 재귀 예측이나 mean 출력의 MSE 비교로 바꾸지 않는다. 이번 저장 자료에서 미래 raw-feature를 다시 만들거나 모델 예측을 재실행하지 않았다.

근거: [SRC-0001968](../sources/history-131.md#src-0001968) 행120–134 · [SRC-0001968](../sources/history-131.md#src-0001968) 행152–164 · [SRC-0001988](../sources/history-131.md#src-0001988) 행581–613 · [SRC-0001989](../sources/history-131.md#src-0001989) 행737–752

<a id="claim-13"></a>

### H131-C13 · 14방법 성능표의 구성과 지표

성능표는 Tab/Ridge/HGB 각각3소속의9새예측과 RCTL seed20260925의3소속·20260926의2K4 저장예측인14방법이다. secondary seed의K1은 이 진단에 없다. 척도는 고정cell별 정규화 MAE,16cell 동등 비중·같은336시점이며 원단위MAE나 새로운 RCTL 학습 결과가 아니다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행23–39 · [SRC-0001984](../sources/history-131.md#src-0001984) JSON /metrics · [SRC-0001978](../sources/history-131.md#src-0001978) NPZ actual, RCTL_global_20260925, RCTL_tabicl_risk_20260926, RCTL_empirical_risk_20260926

<a id="claim-14"></a>

### H131-C14 · Tab global의 직접 예측 이득

global K1의 MAE는Tab0.0661831498, HGB0.0715707839, Ridge0.0792279392다. 같은 자료의 기준 오차를 분모로 한 Tab 상대 감소는각각7.5277002%와16.4648854%이고 앞/뒤7일에도 직접 예측 우열이 같다. 이 긍정 결과는 보존하지만 다른 기간·모집단의 일반적 우위나 RCTL 소속 선택 기여로 옮기지 않는다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행29–39 · [SRC-0001977](../sources/history-131.md#src-0001977) JSON /TabICL_global, /HGB_global, /Ridge_global

<a id="claim-15"></a>

### H131-C15 · 같은K4에서 RCTL과 반대인 Tab 순위

같은K4에서 Tab은Tab-risk0.07324503<empirical0.07540668을 선호하지만 RCTL25는0.08600222>0.07986498, RCTL26은0.08809589>0.08367167로 empirical을 선호한다. Ridge0.08678670>0.08244128와 HGB0.09170042>0.08459679도 이 비교에서는 RCTL과 같은 방향이다. 좋은 직접 예측과 다른 learner의partition 순위 대리를 구별한다. 이 결과는 입력 표현·학습방식·validation 사용이 다른 learner 사이의 관찰이다. 순위 차이를 사전학습 목적이나 함수족 하나의 원인으로 분해하지 않는다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행27–39 · [SRC-0001984](../sources/history-131.md#src-0001984) JSON /metrics/TabICL_tabicl_risk/mean_cell_MAE, /metrics/TabICL_empirical_risk/mean_cell_MAE, /metrics/RCTL_tabicl_risk_20260925/mean_cell_MAE, /metrics/RCTL_empirical_risk_20260925/mean_cell_MAE, /metrics/RCTL_tabicl_risk_20260926/mean_cell_MAE, /metrics/RCTL_empirical_risk_20260926/mean_cell_MAE · [SRC-0023202](../sources/history-131.md#src-0023202) 행59–67 · [SRC-0023202](../sources/history-131.md#src-0023202) 행84–90

<a id="claim-16"></a>

### H131-C16 · 전체14일 K1 우위의 범위

K1 결과가 있는 Tab/Ridge/HGB/primary RCTL에서는14일 전체 평균의K1 MAE가 두K4보다 작았다. 이global 선택은 Tab만의 결정 기여가 아니다. secondary RCTL의미실행K1이나 모든cell·시간절반·다른소속·10,000cell까지 K1이 최적이라고 확장하지 않는다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행35–39 · [SRC-0001984](../sources/history-131.md#src-0001984) JSON /metrics/TabICL_global/mean_cell_MAE, /metrics/Ridge_global/mean_cell_MAE, /metrics/HGB_global/mean_cell_MAE, /metrics/RCTL_global_20260925/mean_cell_MAE

<a id="claim-17"></a>

### H131-C17 · Tab의 앞뒤주 순위 반전

Tab-risk minus empirical MAE는전체−0.0021616463, 앞7일+0.0001634610, 뒤7일−0.0044867527다. RCTL25/26은각각전체+0.0061372463/+0.0044242158이며 두시간절반에서도 양수다. 같은14일의고정절반 비교이지 독립 반복·유의성 검정이나 반전 원인의 분해가 아니다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행41–59 · [SRC-0001984](../sources/history-131.md#src-0001984) JSON /differences/TabICL:tabicl_risk_minus_empirical_risk, /differences/RCTL25:tabicl_risk_minus_empirical_risk, /differences/RCTL26:tabicl_risk_minus_empirical_risk

<a id="claim-18"></a>

### H131-C18 · Tab의 cell별 결과와 날짜별 결과

Tab-risk K4가empirical보다작은 평균오차를 낸 비율은cell6/16과day10/14다. 전체 평균의 음수delta를 모든cell 개선으로 쓰지 않고 cell/day paired 차이를 함께 보존한다. 표본16과기간14를 독립 시행 수나 유의성 증거로 세지 않는다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행43–53 · [SRC-0001984](../sources/history-131.md#src-0001984) JSON /differences/TabICL:tabicl_risk_minus_empirical_risk/cells_with_smaller_error_left, /differences/TabICL:tabicl_risk_minus_empirical_risk/days_with_smaller_error_left, /differences/TabICL:tabicl_risk_minus_empirical_risk/cell_differences, /differences/TabICL:tabicl_risk_minus_empirical_risk/day_differences

<a id="claim-19"></a>

### H131-C19 · RCTL 두seed의 평균과 개별 예외

RCTL의두K4 평균은empirical 우위지만 Tab-risk가작은cell/day도 남아 있다. seed25에서5/16cell·2/14day, seed26에서6/16cell·4/14day가Tab-risk 우위다. 두seed 평균·주간방향의일치를 모든cell의일치로 바꾸지 않으며 이 진단에 새 RCTL seed를 추가하지 않았다.

근거: [SRC-0001984](../sources/history-131.md#src-0001984) JSON /differences/RCTL25:tabicl_risk_minus_empirical_risk/cells_with_smaller_error_left, /differences/RCTL25:tabicl_risk_minus_empirical_risk/days_with_smaller_error_left, /differences/RCTL26:tabicl_risk_minus_empirical_risk/cells_with_smaller_error_left, /differences/RCTL26:tabicl_risk_minus_empirical_risk/days_with_smaller_error_left · [SRC-0001978](../sources/history-131.md#src-0001978) NPZ RCTL_tabicl_risk_20260925, RCTL_empirical_risk_20260925, RCTL_tabicl_risk_20260926, RCTL_empirical_risk_20260926

<a id="claim-20"></a>

### H131-C20 · 첫7일의 K1 예외

전체 평균K1 우위와 달리 첫7일에서는 Tab empirical−global=−0.0001507457, Ridge Tab−global=−0.0010319783/empirical−global=−0.0014403055, HGB empirical−global=−0.0001981894로일부K4가좋다. 이 예외와 Tab의직접예측 우위는 서로다른 비교다. 기간을 골라 최종소속을 재선택하거나 평균의기각을 보편적실패로 바꾸지 않는다.

근거: [SRC-0001984](../sources/history-131.md#src-0001984) JSON /differences/TabICL:empirical_risk_minus_global/first7, /differences/Ridge:tabicl_risk_minus_global/first7, /differences/Ridge:empirical_risk_minus_global/first7, /differences/HGB:empirical_risk_minus_global/first7

<a id="claim-21"></a>

### H131-C21 · 입력·소속·RCTL 저장slice의 결합

저장X(16,1008,16)/Y(16,1008)의672학습prefix·scales는기존design에, 세소속은기존observed-risk에연결된다. 실제값(16,336)과5RCTL예측은기존all_predictions의(16,480)자료에서같은16cell·첫336시점을취한slice와정확히같다. 이전자료3개는기존정확보존본을재사용하고새원본/독립재현으로집계하지 않는다.

근거: [SRC-0001976](../sources/history-131.md#src-0001976) NPZ X, Y, cell_ids, scales · [SRC-0001978](../sources/history-131.md#src-0001978) NPZ actual, RCTL_global_20260925 · [SRC-0023577](../sources/history-131.md#src-0023577) NPZ X, Y, cell_indices, scales · [SRC-0023588](../sources/history-131.md#src-0023588) JSON /cell_ids, /partitions/tabicl_risk, /partitions/empirical_risk · [SRC-0030211](../sources/history-131.md#src-0030211) NPZ cell_ids, y, global_20260925, tabicl_risk_20260925, empirical_risk_20260925, tabicl_risk_20260926, empirical_risk_20260926

<a id="claim-22"></a>

### H131-C22 · 새점수 고정과 눈가림의 구별

driver는9새방법점수를 new_scores_frozen에 저장·SHA고정한 뒤 기존RCTL을읽는 순서다. frozen SHA978efa90…와summary에기록한SHA 및9공통metric이일치한다. 저장무결성·코드순서의확인이지 RCTL을계획전부터알았던사후진단을 독립 눈가림 평가로 바꾸는 근거가 아니다.

근거: [SRC-0001968](../sources/history-131.md#src-0001968) 행193–207 · [SRC-0001968](../sources/history-131.md#src-0001968) 행218–223 · [SRC-0001984](../sources/history-131.md#src-0001984) JSON /new_scores_before_RCTL_read_sha256, /RCTL_results_used_to_change_partition · [SRC-0001977](../sources/history-131.md#src-0001977) JSON /TabICL_global/mean_cell_MAE

<a id="claim-23"></a>

### H131-C23 · 저장917수치의 검산과 새실험의 구별

저장14방법의 mean/cell/day/두시간절반33값씩462개와13paired delta의35값씩455개, 총917수치를float32 배열에서재계산했고저장값과최대차0.0이었다. NPZ3개는6/19/14키의shape·dtype·유한/NaN·바이트hash·입력/기준예측 결합도확인했다. 허용오차5e−8의저장산술 검수이며새model실행·rawtraffic통계/feature재생성·checkpoint성능 재현이아니다.

근거: [SRC-0001984](../sources/history-131.md#src-0001984) JSON /metrics, /differences · [SRC-0001976](../sources/history-131.md#src-0001976) NPZ X, Y · [SRC-0001978](../sources/history-131.md#src-0001978) NPZ actual, TabICL_global, HGB_global, Ridge_global

<a id="claim-24"></a>

### H131-C24 · partial NPZ의 의도된 저장 시점

predictions_partial은9Tabcontext 완료후18simplefit이전 저장본이다. Tab3배열은최종배열과같고Ridge/HGB6배열은아직NaNplaceholder이며RCTL배열은없다. 최종predictions에는14방법이모두유한하다. partial파일명/NaN을실패한실험·추가run·재시도증거로해석하지 않는다.

근거: [SRC-0001968](../sources/history-131.md#src-0001968) 행130–134 · [SRC-0001968](../sources/history-131.md#src-0001968) 행163–192 · [SRC-0001979](../sources/history-131.md#src-0001979) NPZ TabICL_global, TabICL_tabicl_risk, TabICL_empirical_risk, Ridge_global, HGB_global · [SRC-0001980](../sources/history-131.md#src-0001980) JSON /success, /error

<a id="claim-25"></a>

### H131-C25 · 단계 시간과 중복 비용 집계

Tab accounted fit/predict는138.2582043초, cheap2.2270844초, stage140.4852887초다. Ridge/HGB총1.0048376초는cheap에포함돼다시더하지않는다. 초기import·설정·sourcehash는측정시작전이고stage는특징구성/결과쓰기등을포함한다. 이전기록의미기록전처리를더해정확한전체프로젝트비용을만들지 않는다.

근거: [SRC-0001980](../sources/history-131.md#src-0001980) JSON /TabICL_seconds, /cheap_seconds, /wall_seconds, /simple_fit_predict_seconds · [SRC-0001982](../sources/history-131.md#src-0001982) JSON /timing_scope · [SRC-0001965](../sources/history-131.md#src-0001965) 행65–80

<a id="claim-26"></a>

### H131-C26 · 소속별 Tab 비용과 활성 설정

Tab의global1context accounted시간69.1113167초, Tab-risk4합34.4148190초, empirical4합34.7320696초다. context10752→그룹당2688 차이가있는이번CPU·ensemble1·batch1·cacheFalse비교이며predict의n_jobs1 스코프를함께적는다. 세소속9호출의시간이고훈련가중치최적화시간이나RCTL운영속도실측이아니다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행69–80 · [SRC-0001975](../sources/history-131.md#src-0001975) JSON /0/accounted_seconds, /1/accounted_seconds, /2/accounted_seconds, /3/accounted_seconds, /4/accounted_seconds, /5/accounted_seconds, /6/accounted_seconds, /7/accounted_seconds, /8/accounted_seconds · [SRC-0001968](../sources/history-131.md#src-0001968) 행148–170 · [SRC-0001989](../sources/history-131.md#src-0001989) 행688–703

<a id="claim-27"></a>

### H131-C27 · sampled RSS와 당시 상한

기록 sampled process RSS최대는2,602,754,048bytes(약2.42GiB)다. guard는0.2초간격으로RSS를보았으므로연속시간진짜peak의증명은아니다. 당시12GiB/Tab1200초/cheap30초/stage1230초 상한과종료success를보존한다. 이역사상한은현재 정리에서 모델을 실행할 권한이나예산이아니다.

근거: [SRC-0001968](../sources/history-131.md#src-0001968) 행79–104 · [SRC-0001982](../sources/history-131.md#src-0001982) JSON /limits · [SRC-0001980](../sources/history-131.md#src-0001980) JSON /success, /rss_peak_bytes, /wall_seconds

<a id="claim-28"></a>

### H131-C28 · Tab 준비 비용과 RCTL 운영 비용의 분리

K4의Tabcontext평가가이번K1보다빨랐어도소속확정뒤RCTL학습/실행의운영속도이득으로바꾸지않는다. 과거95의같은시각cell batch,97의480시간출력재사용과원101의336시간MAE·Tab추론비용은조건/단위가다르다. 16cell CPU실행을10,000cell에선형외삽하거나기본batch효과를Tab신규성으로세지 않는다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행65–82 · [SRC-0001966](../sources/history-131.md#src-0001966) 행61–79

<a id="claim-29"></a>

### H131-C29 · 당시 원장의 단회 증가

before원장807600a7…에서after60b589e8…로Tab9context/16,128query/138.2582043초를한번더해누적78context/55,488query/389.0795223초가됐다. RCTL29fit과budget_resets0은그대로다. 현재root원장17a549fc…는후속판본이므로원101시점의after와다른것을보존실패라고쓰거나역사after로덮어쓰지 않는다.

근거: [SRC-0001974](../sources/history-131.md#src-0001974) JSON /ledger_before_sha256, /ledger_after_sha256, /TabICL_contexts_added, /TabICL_query_rows_added, /TabICL_seconds_added, /budget_resets · [SRC-0001967](../sources/history-131.md#src-0001967) JSON /used, /budget_resets

<a id="claim-30"></a>

### H131-C30 · 남은 역사 예산과 최종 Word

당시remaining은Tab2context/4,512query·추가RCTLfit0이며원장에cheap/modeling집계와시간범위가남아있다. 검증표식의Word SHA4f1112dc…와당시goal_complete=False를보존하되Word본문은hash-only다. 역사Goal/다음행동/프로세스/상한은자료이며현재아카이브Goal이나새실험지시가 아니다.

근거: [SRC-0001974](../sources/history-131.md#src-0001974) JSON /remaining, /recorded_cheap_seconds, /recorded_modeling_seconds · [SRC-0001985](../sources/history-131.md#src-0001985) JSON /prior_word_sha256, /goal_complete · [SRC-0001969](../sources/history-131.md#src-0001969) 행3–14

<a id="claim-31"></a>

### H131-C31 · snapshot 목록과 실제 물리 파일

원101snapshot43은manifest의28listed파일1,182,878bytes에manifest6,324bytes를더한물리29파일1,189,202bytes다. root receipt393bytes는별도다. 현재검토묶음36source/153물리별칭은snapshot자료에기존판본·foundation·RCTL입력구현을연결한수로snapshot파일수와다르다. 코드4개는공식link/metadata로연결하며파일존재·복사를의미검토완료로세지 않는다.

근거: [SRC-0001962](../sources/history-131.md#src-0001962) JSON /files, /verified, /raw_and_checkpoint_assets_not_duplicated · [SRC-0020835](../sources/history-131.md#src-0020835) JSON /files, /bytes, /verified

<a id="claim-32"></a>

### H131-C32 · 후보·연혁 개정본과 미독 tail

candidate는이전102행에서현재103행으로바뀌며공유함수결정행7을보완하고행39에원101직접예측긍정근거를추가했다. progress는582→591행이며현재1–111만실제읽었다. 현재tail112–591과이전103–582의바이트같음은기계대조일뿐미독범위를완료로바꾸지 않는다. 새상태header를이전기록의독립재현으로세지 않는다.

근거: [SRC-0001966](../sources/history-131.md#src-0001966) 행7–7 · [SRC-0001966](../sources/history-131.md#src-0001966) 행34–41 · [SRC-0001969](../sources/history-131.md#src-0001969) 행7–24

<a id="claim-33"></a>

### H131-C33 · 보관 공식 코드와 이전 부분판독

embedding/layers/tabicl/regressor4파일전문3,365행을읽고공식soda-inria/tabicl의고정commit0dbff3ec… Gitblob/size와대조했다. H005에서부분만읽은embedding/tabicl은이번에전문을확인했고기존전독regressor재독은독립새credit0이다. 이4파일일치는최신main·설치runtime전체commit·정확한packageversion의증명이아니며원manifestversion은unknown이다.

근거: [SRC-0001990](../sources/history-131.md#src-0001990) 행1–30 · [SRC-0001989](../sources/history-131.md#src-0001989) 행19–25 · [SRC-0001988](../sources/history-131.md#src-0001988) 행7–12

<a id="claim-34"></a>

### H131-C34 · 당시 연구 방향에 반영한 판단

원101은실제samplecontext를주었어도좋은Tab직접예측이RCTL의같은K4판단과일치하지않은관찰로기존대리점수의적용범위를보완했다. 공통context검사를다시붙이는것만으로B2를복구하거나Tab/단순회귀점수혼합·attention거리·새모듈을최종안으로추천하지않았다. 세소속사후비교를모든pooling/Tab/RCTL의불가능성으로확대하지 않고직접예측긍정근거를유지한다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행55–63 · [SRC-0001965](../sources/history-131.md#src-0001965) 행93–95 · [SRC-0001963](../sources/history-131.md#src-0001963) 행39–51 · [SRC-0001966](../sources/history-131.md#src-0001966) 행7–7 · [SRC-0001966](../sources/history-131.md#src-0001966) 행36–41

<a id="claim-35"></a>

### H131-C35 · 재검토 조건과 현재 미확인 범위

재검토하려면실제RCTL학습에유효한소속결정또는같은유용한결정의추정/계산효율에서Tab이단순방법보다기여하는차이를특정해야한다. 시간분할/같은기초16값과Tab16열·RCTL8×9표현/척도·기준·seed·원예측/비용을재사용해같은조건의중복실험을피한다. 선정밖callee전체감사·원모델독립재현·Word본문·남은연혁tail은미확인이고당시최종추천/Word도미완료였다.

근거: [SRC-0001965](../sources/history-131.md#src-0001965) 행57–63 · [SRC-0001965](../sources/history-131.md#src-0001965) 행80–95 · [SRC-0001963](../sources/history-131.md#src-0001963) 행39–51 · [SRC-0001966](../sources/history-131.md#src-0001966) 행43–59 · [SRC-0001969](../sources/history-131.md#src-0001969) 행14–14 · [SRC-0023202](../sources/history-131.md#src-0023202) 행59–67 · [SRC-0023202](../sources/history-131.md#src-0023202) 행84–90

<a id="claim-36"></a>

### H131-C36 · 읽기·검수·집계와 전체 Goal의 경계

이번최초실제읽기는원문25개7148행(24whole/1selected),보관code4/3365행과NPZ3선택키·917저장수치검산이다. 기존부분code2의이번전독완료를포함해문서 검수 후 단회 집계할 범위는본문10/전체JSON13/선택4/독립이미지0이며범위를 읽은 사본 수와 구별한다. 36주장/9그룹작성후원문대조에기존RCTL코드2개의실제재독109행을추가했고독립새credit0이다. 원102이후/이전고유판본/FedPPBC·DOCX/전TXT·연혁/통합/장기접근/최종delta/대표질문10+가남아전체Goal미완료다.

근거: [SRC-0001969](../sources/history-131.md#src-0001969) 행7–24 · [SRC-0001985](../sources/history-131.md#src-0001985) JSON /goal_complete
