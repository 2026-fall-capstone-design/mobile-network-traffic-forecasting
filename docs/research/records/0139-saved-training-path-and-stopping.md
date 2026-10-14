# 원109: 저장 학습 경로와 조기 종료 확인

2026-09-26 원기록을 정리했다. **새 학습·추론 없이 기존 로그를 확인한 진단**이다. 29개 모두 patience10으로 끝났고 epoch 상한 절단의 증거는 없었다. 두 K4의 경로 우열은 바뀌었으며, 수렴·원인·새 소속의 우위를 증명한 결과로 해석하지 않는다.

[원108 BN 통계](0138-fixed-weight-bn-statistics.md) · [원106 같은 K4 전이](0136-same-k-cellwise-error-transition.md) · [원107 입력지원](0137-calendar-retention-and-external-support.md) · [41개 출처](../sources/history-139.md) · [근거 보관](../evidence/0139-saved-training-path-and-stopping/README.md) · [26개 주장 검수](../verification/history-139-claims.json)

기록 ID `0139`는 아카이브 관리 번호이며 과거 실험 횟수가 아니다. 원109의 코드는 실행 가능한 지시 대신 역사적 자료로 보관했다. 전체 과거기록 정리는 계속 진행 중이다.

## 질문과 실제 수행

<a id="claim-01"></a>

**질문과 선행 기록.** 원109는 원108의 BN 통계 재계산 뒤, 같은 K4의 차이가 epoch 상한 절단이나 저장된 종료 규칙의 불일치 때문인지 기존 학습 경로로 확인한 기록이다. 원34의 최종 train/validation, 원106의 최종 cell 전이, 원108의 BN 상태 변경과 서로 다른 확인이다.

근거: [SRC-0020861](../sources/history-139.md#src-0020861) 줄1–9 · [SRC-0020862](../sources/history-139.md#src-0020862) 줄1–7

<a id="claim-02"></a>

**실제 수행과 재현 범위.** 원109의 완료 결과·시작/종료 marker·입력 hash가 연결되며 새 fit와 모델 호출은 0으로 기록됐다. 이번 아카이브는 원본 코드를 실행·import하거나 모델을 만들지 않고 저장 자료와 작은 산술로 대조했다. 저장값 일치는 원래 모델 실행을 독립 재현한 성과가 아니다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /complete, /new_fits, /new_model_calls, /input_files_unchanged_before_accounting · [SRC-0032510](../sources/history-139.md#src-0032510) JSON (전체 값) · [SRC-0032509](../sources/history-139.md#src-0032509) JSON (전체 값) · [SRC-0023204](../sources/history-139.md#src-0023204) 줄26–45 · [SRC-0023204](../sources/history-139.md#src-0023204) 줄113–135

## 조건·입력·종료 정의

<a id="claim-03"></a>

**자료·입력·지표.** 원학습의 target index는 train168–839의672개, validation840–1007의168개, 기존 test1008–1487의480개였다. 코드에서 선택한 traffic 채널(index2)을 저장 scales로 나누고 8step×9channel RCTL 입력을 만들었다. 본 기록의 MAE는 정규화된 validation 오차이며 원단위 MAE·Tab 직접 예측·소속 점수와 합치지 않는다. scale 산출과 실제 cell ID 대응은 선행 자료의 조건을 함께 읽는다.

근거: [SRC-0030238](../sources/history-139.md#src-0030238) JSON /train_targets, /validation_targets, /test_targets · [SRC-0023202](../sources/history-139.md#src-0023202) 줄46–70 · [SRC-0023202](../sources/history-139.md#src-0023202) 줄84–90

<a id="claim-04"></a>

**핵심16개와 보조13개.** 핵심 비교는 TabICL risk·empirical risk의 두 seed20260925/20260926×4cluster=16모델이다. 각 cluster는 고정된16cell 중4cell이고 저장 members는 cell ID가 아닌0–15 내부 index다. global1개와 첫 seed의 KNN/PCC/random12개는 총29개의 종료 일관성 확인에만 쓰며 같은 K 핵심 순위에 섞지 않는다.

근거: [SRC-0020861](../sources/history-139.md#src-0020861) 줄5–17 · [SRC-0030238](../sources/history-139.md#src-0030238) JSON /tasks · [SRC-0032508](../sources/history-139.md#src-0032508) JSON /records

<a id="claim-05"></a>

**원래 학습·종료 정의.** 원학습은 MAE, Adam lr0.001/eps1e-7, batch256, 최대80epoch, patience10, threads4였다. validation이 이전 best보다 엄격히 작을 때만 best와 stale을 갱신하고 아니면 stale을 늘려10에서 멈춘다. max_fits29/max_total_epochs2320, wall3000초/RAM20GiB는 과거 설정이며 현재 실행 허가나 예산이 아니다.

근거: [SRC-0030238](../sources/history-139.md#src-0030238) JSON /max_epochs, /patience, /learning_rate, /adam_eps, /batch_size, /loss, /threads, /max_fits, /max_total_epochs, /wall_cap_seconds, /ram_cap_bytes · [SRC-0023202](../sources/history-139.md#src-0023202) 줄95–118 · [SRC-0023204](../sources/history-139.md#src-0023204) 줄55–70

<a id="claim-06"></a>

**로그의 실제 확인 범위.** 원본29개 history의 전체 본문9,448행을 읽고 epoch/train_mae/val_mae/seconds_from_fit_start 네 필드를 확인했다. 총1,565epoch·6,260숫자 필드이며 epoch는1부터 연속되고 유한·비음수 값과 증가하는 누적 시간을 저장했다. 끝 시간은 해당 fit_seconds 이하였으며 step별 실행 trace를 복구한 것은 아니다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /records · [SRC-0030237](../sources/history-139.md#src-0030237) JSON (전체 값) · [SRC-0023204](../sources/history-139.md#src-0023204) 줄47–84

<a id="claim-09"></a>

**epoch당 작업량과 파생횟수.** 정적 batch loop에서 global의 epoch당 명목 update는ceil(16×672/256)=42, K4 각 모델은ceil(4×672/256)=11이며 K4의 마지막 batch는128행이다. 저장 epoch 수로 얻은 총 명목 update18,610회는 파생값이다. 실제 optimizer.step별 trace를 독립 복원한 수가 아니고 같은 epoch의 global과 K4를 같은 작업량으로 세지 않는다.

근거: [SRC-0023202](../sources/history-139.md#src-0023202) 줄84–110 · [SRC-0020861](../sources/history-139.md#src-0020861) 줄17–17 · [SRC-0032508](../sources/history-139.md#src-0032508) JSON /records

## 종료와 남은 변동

<a id="claim-07"></a>

**종료와 최저점의 일치.** 29개 모두 validation_patience 종료다. 각 로그는 best_epoch+10에서 끝나고 마지막 stale=10, 중간에 stale=10에 먼저 도달한 곳이나 마지막10개의 새 best는 없었다. 실제 길이는42–70epoch로80상한에 닿지 않았다. 저장 종료 이유와 정적 규칙은 일치하지만 RAM peak나 전체 실행 과정을 별도로 재현한 검사는 아니다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /records, /stop_counts_all29, /all_records_consistent · [SRC-0023202](../sources/history-139.md#src-0023202) 줄95–118 · [SRC-0023204](../sources/history-139.md#src-0023204) 줄55–84

<a id="claim-08"></a>

**하강하는 마지막 구간도 보존.** 마지막10개 validation의 fitted slope가 음수인 모델은15/29, 끝 값이 첫 값보다 낮은 모델은17/29, 인접 감소는136/261구간이다. 예를 들어 empirical/첫 seed/cluster3은 best41·종료51이며 slope≈−0.003415904, 마지막10개 첫끝 차이≈−0.000781886이다. 하강·변동이 있어도 이전 best를 갱신하지 않았다는 사실을 보존하며 수렴·추가 학습 이득의 증명으로 바꾸지 않는다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /records · [SRC-0023204](../sources/history-139.md#src-0023204) 줄71–84

<a id="claim-19"></a>

**global과 보조 비교군의 한계.** global의 sample/update 수는 local K4와 다르고 KNN/PCC/random은 둘째 seed가 없다. 보조13개의 종료 일관성을 핵심 두 방법×두 seed의 효과크기·일반 우위·학습량 통제 실험으로 바꾸지 않는다. 개별 첫·best·마지막값과 tail 변동은 결과표에 그대로 보존한다.

근거: [SRC-0020861](../sources/history-139.md#src-0020861) 줄7–17 · [SRC-0030238](../sources/history-139.md#src-0030238) JSON /tasks · [SRC-0032508](../sources/history-139.md#src-0032508) JSON /records

## 같은 K4의 두 seed 경로

<a id="claim-10"></a>

**공통 epoch 집계 정의.** 같은 seed의 두 K4 여덟 로그 중 가장 짧은 길이까지만 각 방법4모델의 validation을 평균했다. 모든 cluster가4cell이라 동일 cell 비중이며 종료 뒤 값 복제·padding·보간·외삽은 없다. 전체 공통 gap 배열은 저장된 경로의 기술 통계이고 새 test 성능이나 독립 반복실험 표본이 아니다.

근거: [SRC-0020861](../sources/history-139.md#src-0020861) 줄13–17 · [SRC-0023204](../sources/history-139.md#src-0023204) 줄87–111 · [SRC-0032508](../sources/history-139.md#src-0032508) JSON /comparisons

<a id="claim-11"></a>

**첫 seed의 경로.** seed20260925의 공통 구간은42epoch다. Tab−empirical validation 차이가 음수인20epoch, 양수인22epoch,0인0epoch이고 부호는25번 바뀌었다. Tab이 학습 시작부터 종료까지 일관되게 나빴다고 해석할 수 없으며 인접 epoch를 독립 표본으로 세어 유의성을 주장하지 않는다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /comparisons/0 · [SRC-0020862](../sources/history-139.md#src-0020862) 줄9–16

<a id="claim-12"></a>

**둘째 seed의 경로.** seed20260926의 공통 구간은43epoch다. Tab이 낮은21epoch·높은22epoch·같은0epoch이며 부호는16번 바뀌었다. 이 seed에서도 한 시점만 골라 새 후보의 성능으로 발표하거나 공통 구간 밖의 경로를 덧붙이지 않는다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /comparisons/1 · [SRC-0020861](../sources/history-139.md#src-0020861) 줄15–15 · [SRC-0020862](../sources/history-139.md#src-0020862) 줄9–16

<a id="claim-13"></a>

**첫 seed의 서로 다른 요약.** 첫 seed의 마지막 공통 epoch gap은−0.00009810179471969604, 마지막5개 공통 epoch 평균 gap은+0.00038709938526153563, 각 모델의 선택 checkpoint 평균 gap은+0.0027730241417884827이다. 서로 다른 가중치·시점·집계라 부호가 달라도 모순이 아니며 유리한 요약을 골라 최종 성능을 교체하지 않는다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /comparisons/0 · [SRC-0023204](../sources/history-139.md#src-0023204) 줄95–111

<a id="claim-14"></a>

**둘째 seed의 서로 다른 요약.** 둘째 seed의 마지막 공통 epoch gap은+0.00037717074155807495, 마지막5개 평균 gap은−0.0015455834567546845, 선택 checkpoint 평균 gap은+0.00016181357204914093이다. 마지막5개 평균에서 Tab이 낮다는 관측과 선택 checkpoint 평균에서 높다는 관측은 비교 대상이 다르다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /comparisons/1 · [SRC-0023204](../sources/history-139.md#src-0023204) 줄95–111

<a id="claim-15"></a>

**첫 seed의 실제 epoch.** 첫 seed에서 Tab 각 cluster의 실제 epoch는[65,42,55,59] 합221, best는[55,32,45,49]이고 empirical은[69,55,48,51] 합223, best[59,45,38,41]이다. 명목 update 합은각2,431/2,453회다. 두 방법의 최대 설정이 같아도 실제 수행량이나 선택 시점이 동일했던 것은 아니다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /comparisons/0 · [SRC-0030237](../sources/history-139.md#src-0030237) JSON /1, /2, /3, /4, /5, /6, /7, /8

<a id="claim-16"></a>

**둘째 seed의 실제 epoch.** 둘째 seed에서 Tab 실제 epoch는[69,58,60,48] 합235, best[59,48,50,38]이고 empirical은[48,55,43,70] 합216, best[38,45,33,60]이다. 명목 update 합은2,585/2,376회다. 첫 seed와 차이가 작은 둘째 seed를 하나의 보편적 학습량 효과로 합치지 않는다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /comparisons/1 · [SRC-0030237](../sources/history-139.md#src-0030237) JSON /21, /22, /23, /24, /25, /26, /27, /28

<a id="claim-17"></a>

**선택 checkpoint 평균의 의미.** 첫 seed의 선택 validation 평균은Tab0.08165614493191242/empirical0.07888312079012394, 둘째는0.07929670810699463/0.07913489453494549다. 각 모델의 서로 다른 best_epoch에서 validation으로 고른 최소값4개를 평균했으며 동시 epoch·공통 가중치·새 held-out 평가의 평균이 아니다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /comparisons/0, /comparisons/1 · [SRC-0023202](../sources/history-139.md#src-0023202) 줄107–126 · [SRC-0023204](../sources/history-139.md#src-0023204) 줄95–111

## train 곡선을 읽는 조건

<a id="claim-18"></a>

**online train과 eval의 차이.** train_mae는 model.train 상태의 각 배치 loss를 배치 크기로 가중해 모은 값이다. 배치 사이 가중치가 갱신되고 dropout·BN은 train mode였다. validation은 epoch 종료 뒤 model.eval과 no_grad로 계산한다. 따라서 두 곡선 차이는 고정 checkpoint의 일반 과적합 gap이 아니며 원34/106/108의 고정 가중치 train 평가와 구별한다.

근거: [SRC-0020861](../sources/history-139.md#src-0020861) 줄8–16 · [SRC-0023202](../sources/history-139.md#src-0023202) 줄73–76 · [SRC-0023202](../sources/history-139.md#src-0023202) 줄100–118 · [SRC-0032511](../sources/history-139.md#src-0032511) JSON /train_loss_semantics · [SRC-0032508](../sources/history-139.md#src-0032508) JSON /comparisons

## 당시 판단과 재검토 조건

<a id="claim-20"></a>

**판단 변경의 경계.** 당시 판단은 epoch 상한 절단이나 종료 불일치를 근거로 기존 비교를 무효화할 자료가 없다는 것이다. optimizer가 전역적으로 수렴했거나 patience10이 모든 분할에 가장 공정한 설정이었다는 증명, 오차 차이의 원인 규명, 추가 학습을 하면 복구된다는 증명은 아니다.

근거: [SRC-0020862](../sources/history-139.md#src-0020862) 줄18–22 · [SRC-0032508](../sources/history-139.md#src-0032508) JSON /claims_optimizer_convergence · [SRC-0020861](../sources/history-139.md#src-0020861) 줄9–23

<a id="claim-21"></a>

**소속 선택으로 되먹이지 않음.** 원109의 RCTL loss는 기존 실패의 해석에 쓰였고 새 cell 소속·시각 이동·병합 threshold의 입력으로 쓰지 않았다고 기록됐다. 설정과 결과의 selection_uses_test/RCTL_results_used_for_clustering/used_to_select_clustering은false다. 새 분할 설계에는 달라지는 질문과 입력·선정 규칙을 먼저 명시한다는 과거 판단을 보존한다.

근거: [SRC-0020862](../sources/history-139.md#src-0020862) 줄20–22 · [SRC-0020861](../sources/history-139.md#src-0020861) 줄21–25 · [SRC-0030238](../sources/history-139.md#src-0030238) JSON /selection_uses_test, /RCTL_results_used_for_clustering · [SRC-0032508](../sources/history-139.md#src-0032508) JSON /used_to_select_clustering

<a id="claim-26"></a>

**재사용과 다시 검토할 조건.** 29개 원로그, frozen settings, fit summary, 정적 학습·진단 코드, 완료marker와 두 원장 판본을 재사용 근거로 연결한다. 원fit summary에 있는 test 값은 기존 학습의 저장 결과이고 원109에서 새 test를 계산한 결과가 아니다. 같은 조건의 재학습을 반복하기 전에 입력지원·소속·optimizer 또는 종료규칙 중 무엇을 바꿔 어떤 가설을 구별하는지와 독립 평가 조건을 설계한다. 과거 다음 행동·예산·Goal 문구는 현재 실행 지시가 아니다.

근거: [SRC-0020861](../sources/history-139.md#src-0020861) 줄19–25 · [SRC-0020862](../sources/history-139.md#src-0020862) 줄18–29 · [SRC-0030237](../sources/history-139.md#src-0030237) JSON (전체 값) · [SRC-0032508](../sources/history-139.md#src-0032508) JSON /new_model_calls, /used_to_select_clustering

## 비용·판본·회계와 공백

<a id="claim-22"></a>

**진단 비용과 측정 범위.** 원109가 기록한 저장 로그 읽기·수치 요약은0.01929139999265317초, sampled RSS는33,890,304bytes다. timer는history 처리·요약을 포함하고 imports·입력hash·마지막hash 재검사·결과와 원장 직렬화를 제외한다. RSS는 한 번 읽은 값이며 peak가 아니다. 아카이브 산술과 문서 작업을 이 과거 비용에 더하지 않는다.

근거: [SRC-0032508](../sources/history-139.md#src-0032508) JSON /elapsed_seconds, /sampled_rss_bytes, /timing_scope · [SRC-0023204](../sources/history-139.md#src-0023204) 줄38–45 · [SRC-0023204](../sources/history-139.md#src-0023204) 줄113–135

<a id="claim-23"></a>

**marker와 입력 판본.** 시작marker의 settings SHA와 종료marker의 result/after-ledger SHA가 정확히 일치한다. 두 unix 시각 차이는0.05562114715576172초로 진단 산술 timer와 범위가 다르다. settings가 기록한35개의 입력hash를 실제 판본에 연결했으며 현재 root 원장과 옛 입력 원장은 서로 다른 버전이다.

근거: [SRC-0032510](../sources/history-139.md#src-0032510) JSON (전체 값) · [SRC-0032509](../sources/history-139.md#src-0032509) JSON (전체 값) · [SRC-0032511](../sources/history-139.md#src-0032511) JSON /source_hashes · [SRC-0024508](../sources/history-139.md#src-0024508) JSON (전체 값)

<a id="claim-24"></a>

**실제 전후 원장과 한 번의 정산.** 분석전300d59… 원장과 정산후989194… 원장의 전체 JSON 값을 비교한 차이는 /new_cheap_diagnostic_seconds/training_path_109와 /cheap_stage_details/10 두 위치뿐이다. 둘은 같은0.01929139999265317초 사건의 요약·상세이며 두 번 과금한 것이 아니다. 나머지 값은 같고 optimizer29회+BN 통계 적합9회=combined38회, 남은9회·Tab78호출/55,488query행·reset0을 그대로 보존한다.

근거: [SRC-0032507](../sources/history-139.md#src-0032507) JSON (전체 값) · [SRC-0024508](../sources/history-139.md#src-0024508) JSON (전체 값) · [SRC-0023204](../sources/history-139.md#src-0023204) 줄126–135 · [SRC-0020862](../sources/history-139.md#src-0020862) 줄24–29

<a id="claim-25"></a>

**복구한 판본과 남은 공백.** 정산후989194…의 바이트 일치 원본은 다음 원110 디렉터리의 ledger_before_accounting.json에 남아 있었다. 이 파일로 원109 정산 판본을 연결했으며 원110 실험 내용을 검토·실행한 것으로 세지 않는다. 실제 원장 쓰기 도구 응답·정확한 정산 시각은 미복구다. historical hash와 현재root 원장hash 차이를 자료 훼손으로 단정하지 않는다.

근거: [SRC-0020862](../sources/history-139.md#src-0020862) 줄27–29 · [SRC-0032509](../sources/history-139.md#src-0032509) JSON /ledger_after_sha256 · [SRC-0024508](../sources/history-139.md#src-0024508) JSON (전체 값) · [SRC-0032511](../sources/history-139.md#src-0032511) JSON /source_hashes

## 결과표: 비교 단위별 요약

값은 정규화된 validation MAE의 `Tab−empirical`이다. 아래 세 요약은 동일한 가중치나 선택 시점의 비교가 아니다. 원본 전체 경로는 결과 JSON에 남겼다.

| seed | 공통 epoch | Tab 낮음/높음 | 부호 변경 | 마지막 공통 gap | 마지막5개 평균 gap | 선택 checkpoint 평균 gap |
|---|---:|---:|---:|---:|---:|---:|
| 20260925 | 42 | 20/22 | 25 | -0.000098102 | +0.000387099 | +0.002773024 |
| 20260926 | 43 | 21/22 | 16 | +0.000377171 | -0.001545583 | +0.000161814 |

## 결과표: 29개 모델의 저장 validation

처음·best·마지막은 해당 모델의 다른 epoch 값이다. 모든 종료 이유는 `validation_patience`다. 핵심16개 외 비교군은 종료 점검에만 쓰였다. 표시 값은 소수9자리로 반올림했으며 전체 정밀도·last10·개선 epoch 목록은 원본 JSON을 따른다.

| 방법/seed/cluster · 로그 | 실제 epoch | best epoch | 처음 | best | 마지막 |
|---|---:|---:|---:|---:|---:|
| [global/20260925/0](../sources/history-139.md#src-0030241) | 45 | 35 | 0.288424641 | 0.075371467 | 0.076617345 |
| [tabicl_risk/20260925/0](../sources/history-139.md#src-0030283) | 65 | 55 | 0.367384732 | 0.082204685 | 0.091776617 |
| [tabicl_risk/20260925/1](../sources/history-139.md#src-0030286) | 42 | 32 | 0.405251592 | 0.091856271 | 0.101075739 |
| [tabicl_risk/20260925/2](../sources/history-139.md#src-0030289) | 55 | 45 | 0.398446321 | 0.068587080 | 0.072260723 |
| [tabicl_risk/20260925/3](../sources/history-139.md#src-0030292) | 59 | 49 | 0.421930581 | 0.083976544 | 0.086204588 |
| [empirical_risk/20260925/0](../sources/history-139.md#src-0030214) | 69 | 59 | 0.329065412 | 0.074898064 | 0.079200335 |
| [empirical_risk/20260925/1](../sources/history-139.md#src-0030217) | 55 | 45 | 0.378396660 | 0.076785631 | 0.091052137 |
| [empirical_risk/20260925/2](../sources/history-139.md#src-0030220) | 48 | 38 | 0.365940690 | 0.083724126 | 0.088909402 |
| [empirical_risk/20260925/3](../sources/history-139.md#src-0030223) | 51 | 41 | 0.458347380 | 0.080124661 | 0.090620466 |
| [knn_risk/20260925/0](../sources/history-139.md#src-0030244) | 51 | 41 | 0.392353117 | 0.081457891 | 0.087331213 |
| [knn_risk/20260925/1](../sources/history-139.md#src-0030247) | 58 | 48 | 0.375717312 | 0.077590220 | 0.080765471 |
| [knn_risk/20260925/2](../sources/history-139.md#src-0030250) | 51 | 41 | 0.335382700 | 0.066139974 | 0.073588833 |
| [knn_risk/20260925/3](../sources/history-139.md#src-0030253) | 45 | 35 | 0.365621269 | 0.088957377 | 0.095548809 |
| [pcc_balanced/20260925/0](../sources/history-139.md#src-0030256) | 47 | 37 | 0.281584382 | 0.068839662 | 0.074248157 |
| [pcc_balanced/20260925/1](../sources/history-139.md#src-0030259) | 47 | 37 | 0.348782867 | 0.085488006 | 0.105593599 |
| [pcc_balanced/20260925/2](../sources/history-139.md#src-0030262) | 59 | 49 | 0.378374904 | 0.080984682 | 0.085958943 |
| [pcc_balanced/20260925/3](../sources/history-139.md#src-0030265) | 58 | 48 | 0.468850911 | 0.077474914 | 0.096927747 |
| [random_balanced/20260925/0](../sources/history-139.md#src-0030268) | 51 | 41 | 0.385877252 | 0.069549859 | 0.072352014 |
| [random_balanced/20260925/1](../sources/history-139.md#src-0030271) | 52 | 42 | 0.354944736 | 0.081850283 | 0.083922967 |
| [random_balanced/20260925/2](../sources/history-139.md#src-0030274) | 53 | 43 | 0.426179618 | 0.090151854 | 0.090288557 |
| [random_balanced/20260925/3](../sources/history-139.md#src-0030277) | 53 | 43 | 0.298845202 | 0.081290066 | 0.086411044 |
| [tabicl_risk/20260926/0](../sources/history-139.md#src-0030295) | 69 | 59 | 0.460470647 | 0.082223415 | 0.082874440 |
| [tabicl_risk/20260926/1](../sources/history-139.md#src-0030298) | 58 | 48 | 0.451694310 | 0.087269954 | 0.105129898 |
| [tabicl_risk/20260926/2](../sources/history-139.md#src-0030301) | 60 | 50 | 0.454677433 | 0.064553916 | 0.076430291 |
| [tabicl_risk/20260926/3](../sources/history-139.md#src-0030304) | 48 | 38 | 0.493652076 | 0.083139546 | 0.085752912 |
| [empirical_risk/20260926/0](../sources/history-139.md#src-0030226) | 48 | 38 | 0.455066919 | 0.075977676 | 0.091215499 |
| [empirical_risk/20260926/1](../sources/history-139.md#src-0030229) | 55 | 45 | 0.442946106 | 0.078972541 | 0.081810892 |
| [empirical_risk/20260926/2](../sources/history-139.md#src-0030232) | 43 | 33 | 0.440060854 | 0.083261989 | 0.086779423 |
| [empirical_risk/20260926/3](../sources/history-139.md#src-0030235) | 70 | 60 | 0.473424822 | 0.078327373 | 0.090752617 |

## 검수 범위와 재사용

41개 고유 SHA의110개 경로를 연결했다. 새 정확사본8개 `93,777bytes`, 기존 사본33개를 재사용한다. 새 본문 검토38개12,798행 중29개 로그는9,448행이다. 이미 전문 검토됐던 train143/fit722/settings369의 재독1,234행은 추가 credit이 아니다. 기존 선택 범위30개를 JSON 전문 검토로 승격하는 것과 새 파일8개를 보관하는 것은 다른 집계다.

[저장 산술1,141건](../evidence/0139-saved-training-path-and-stopping/saved-numeric-check.json)의 최대 절대 차이는 `1.1102230246251565e-16`이다. validation 경로·gap·checkpoint 평균은 정확히 일치하며 online train 평균과 last10 slope의 차이는 부동소수점 반올림 범위였다. 이 검수 보고서는 당시 생성 단계의 범위를 보존한다. 이후 완료한 literal 읽기와 작성후 대조는 [읽기 범위](../evidence/0139-saved-training-path-and-stopping/read-scopes.json)에 별도로 남겼다.

작성후335raw행·완전한29개 result 노드/두 비교 경로·29개 fit 노드·29개 로그의87선택노드/290tail validation·전후 원장 전체 JSON 값을 다시 대조했다. 2,317행 result와9,448행 로그를 literal로 한 번 더 출력한 검사는 아니다. 같은 에이전트의 두 번째 대조이며 독립 연구자 검증이나 원모델 재현은 아니다.

기존 scale/cell 대응·실제 입력지원·고정 checkpoint의 train/eval 조건은 선행 [RCTL 기초](0004-0007-b2-observed-risk.md)와 원106–108을 함께 읽는다. 과거 코드·로그만으로 더 큰 범위의 수렴이나 clustering 신규성을 주장하지 않는다. 원110 이후·옛 고유 판본·다른 형식·전체 통합과 최종 검색/접근 검수는 남아 있다.
