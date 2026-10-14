# 원110–111: 고정 시각 좌표 후보와 예측 전 입력 지원

2026-09-26의 개발 자료 진단을 정리했다. **profile 절대차9.22% 감소와 입력 지원 통과는 예측 성능 개선이 아니다.** 새 모델 호출·RCTL 적합·고정 좌표/소속 확정 없이 profile과 후속 비교 입력을 마련한 단계였다. 현재 보고서에는 원112가 진행 기준에 실패했다는 후속 안내가 추가됐으며, 원112 실제 예측 결과 검수는 다음 묶음에 남아 있다.

[원109 학습 경로](0139-saved-training-path-and-stopping.md) · [원107 입력지원](0137-calendar-retention-and-external-support.md) · [28개 출처](../sources/history-140.md) · [근거 보관](../evidence/0140-calendar-alignment-and-input-preflight/README.md) · [32개 주장 검수](../verification/history-140-claims.json) · [문헌 비교](../references/calendar-alignment-and-input-preflight.md)

기록 ID `0140`은 아카이브 관리 번호이고 실험 횟수가 아니다. 원문 속 과거 Goal·예산·다음 행동은 역사적 자료다. 정리 과정에서 원코드 실행·import·모델 생성은0이며 전체 과거기록 정리는 진행 중이다.

## 질문·실행·자료와 척도

<a id="claim-01"></a>

**고정 cell 좌표라는 후보.** cell마다 고정된 φ를 두고 달력 시각을 (h−φ) mod24로 표현하되 실제 관측 순서·최근 이력·다음 target·요일을 보존한다는 후보였다. A query의 시각을 donor B의 좌표에 대응시켜도 다른 cell의 미래 관측을 가져오지 않는다는 명세다. 원110–111에서는 φ·cluster 소속을 확정하거나 RCTL 구조를 바꾸지 않았다.

근거: [SRC-0020866](../sources/history-140.md#src-0020866) 줄1–51 · [SRC-0020867](../sources/history-140.md#src-0020867) 줄1–32 · [SRC-0024512](../sources/history-140.md#src-0024512) JSON /new_partition_chosen, /forecast_performance_measured · [SRC-0024556](../sources/history-140.md#src-0024556) JSON /aggregate

<a id="claim-02"></a>

**실제 수행과 아직 수행하지 않은 비교.** 원110은 저장된 원101 입력으로 평균 profile을 점검하고 직렬화 실패 뒤 저장 profile에서 요약을 복구했다. 원111은 donor·세 이동량·공통 query mask를 동결한 입력 검사였다. 정적 코드·결과·전후 원장에는 두 단계의 새 모델 fit/predict·RCTL 적합·새 소속 선정이 없으며, 이번 정리에서도 원코드를 실행·import하거나 모델을 생성하지 않았다.

근거: [SRC-0024506](../sources/history-140.md#src-0024506) 줄1–133 · [SRC-0022559](../sources/history-140.md#src-0022559) 줄1–165 · [SRC-0022563](../sources/history-140.md#src-0022563) 줄1–185 · [SRC-0024512](../sources/history-140.md#src-0024512) JSON /new_model_calls, /new_fits, /reused_saved_profiles · [SRC-0024556](../sources/history-140.md#src-0024556) JSON /settings

<a id="claim-03"></a>

**16 cell과 이미 쓰인 개발 자료.** cell은 3737,3745,3753,3765,4537,4545,4553,4565,5337,5345,5353,5365,6137,6145,6153,6165다. 저장 target168–839 중 train168–671은504시간/21일, splitA168–503은336시간/14일, splitB504–671은168시간/7일, check672–839은168시간/7일이다. 원111의 query도 이 check 구간에서 골랐으며 이미 사용한 개발 자료라 독립 최종평가가 아니다.

근거: [SRC-0020866](../sources/history-140.md#src-0020866) 줄1–51 · [SRC-0020867](../sources/history-140.md#src-0020867) 줄1–32 · [SRC-0024509](../sources/history-140.md#src-0024509) NPZ cell_ids, hour · [SRC-0029561](../sources/history-140.md#src-0029561) NPZ context_times, X, Y · slice {'X': '[:,0:672,:]', 'Y': '[:,0:672]'} · [SRC-0024512](../sources/history-140.md#src-0024512) JSON /settings, /cell_ids

<a id="claim-04"></a>

**profile 표준화와 입력 표준화를 구별.** 원110은 각 cell의 train504개 target에서 평균·population std를 구해 네 기간의24시간 평균 profile을 비교했다. 이는 profile 거리용 표준화이고 원101의 입력·target 척도를 덮어쓰지 않았다. 원111의 거리 표준화는 각 donor context504행의16개 특징별 평균·std이며 두 표준화와 원래 cell 척도는 서로 다른 단계다.

근거: [SRC-0022559](../sources/history-140.md#src-0022559) 줄60–82 · [SRC-0022563](../sources/history-140.md#src-0022563) 줄74–85 · [SRC-0024509](../sources/history-140.md#src-0024509) NPZ center, scale, train, split_a, split_b, check · [SRC-0024554](../sources/history-140.md#src-0024554) NPZ context_means, context_scales · [SRC-0020868](../sources/history-140.md#src-0020868) 줄11–15

## profile 이득·손해·좌표 일관성

<a id="claim-05"></a>

**24개 이동·MSE·동점과 방향.** 120개 무방향 쌍에서 [0,+1,−1,…,+11,−11,+12]의24개 서로 다른 mod24 이동을 train profile MSE로 비교했다. 최소값+1e−12 이내 중 미리 정한 순서의 첫 이동을 골랐으며 정확히 같은 값에만 적용하는 동점 규칙은 아니다. δij는 j[h+δij]를 i[h]에 맞추며 np.roll(j,−δij)와 대응한다. 역방향은 −δij이고 −12는+12와 같은 잉여류다.

근거: [SRC-0022559](../sources/history-140.md#src-0022559) 줄85–118 · [SRC-0024515](../sources/history-140.md#src-0024515) JSON /shift_priority, /phase_orientation · [SRC-0024512](../sources/history-140.md#src-0024512) JSON /pairs · [SRC-0024509](../sources/history-140.md#src-0024509) NPZ pair_shift_matrix

<a id="claim-06"></a>

**전체120쌍의 profile 결과.** 비영 이동은76/120, 무이동은44/120이며 비영76쌍 중72쌍의 splitA/B 이동 차이가1시간 이내였다. train에서 고른 이동을 check에 고정 적용한 전체120쌍 동일 비중 평균 MAE는0.486019094→0.441194325로9.2228% 감소했다. 이는 표준화된 하루 평균 파형 사이의 절대차 감소이며 다음값 예측·TabICL·RCTL MAE의 개선율이 아니다.

근거: [SRC-0020864](../sources/history-140.md#src-0020864) 줄1–42 · [SRC-0024512](../sources/history-140.md#src-0024512) JSON /aggregate, /pairs

<a id="claim-07"></a>

**MSE 선택과 쌍별 손해.** check MAE는61쌍 개선·15쌍 악화·44쌍 무이동이었다. 가장 큰 악화는3745–4545의δ=−2에서0.684141126→0.767690471(+0.083549345)였다. train에서도 MSE로 선택한 이동 때문에 MAE가 악화된 쌍이6개 있었다. 평균만으로 모든 쌍의 이득이나 통계적 유의성을 주장하지 않으며15개 손해를 함께 보관한다.

근거: [SRC-0024512](../sources/history-140.md#src-0024512) JSON /aggregate, /pairs

<a id="claim-08"></a>

**쌍별 최적 이동의 좌표 불일치.** 560개 삼각형의 abs(((δij+δjk−δik+12) mod24)−12)로 정의한 원형 잔차는0시간232개,1시간226개,2시간62개,3시간32개,4시간8개다. 따라서458개는1시간 이내지만 현재16cell의 모든 쌍별 최적 이동을 동시에 정확히 만족하는 단일 고정 좌표는 없다. 일부 cluster 안에서 다른 공동 최적 좌표를 정하는 가능성을 기각한 결과는 아니며 실제 공동 정렬·소속 최적화는 아직 수행하지 않았다.

근거: [SRC-0020866](../sources/history-140.md#src-0020866) 줄1–51 · [SRC-0022559](../sources/history-140.md#src-0022559) 줄120–138 · [SRC-0024512](../sources/history-140.md#src-0024512) JSON /cycles, /aggregate

<a id="claim-09"></a>

**profile 진행 기준의 범위.** 사전에 적힌 기준은 비영 쌍>60, 그중 절반 초과가 split 차이1시간 이내, 전체120쌍 평균 check MAE 감소였다. 원110 결과는 이 profile 전용 기준을 통과했다. 이는 시각 차이의 존재·반복성 진단이며 예측 효용·신규성·최종 연구 채택이나 원112 통과를 뜻하지 않는다.

근거: [SRC-0020866](../sources/history-140.md#src-0020866) 줄1–51 · [SRC-0024510](../sources/history-140.md#src-0024510) JSON /gate, /phase_only_profile_check_not_forecast_performance · [SRC-0024512](../sources/history-140.md#src-0024512) JSON /aggregate

## 최초 실패·복구·시간과 원장

<a id="claim-10"></a>

**최초 실패와 저장 profile의 복구.** 133행 최초 코드에는 numpy scalar를 처리하는 JSON default가 없었고 profiles.npz를 저장한 뒤 요약 JSON을 쓴다. 기록된 실패 원인은 triangle count의 numpy int64 직렬화였다. 165행 복구 코드는 기존 profiles SHA1fbac28a…를 읽고 쌍·삼각형 요약만 계산하며 새 phase 행렬이 저장 행렬과 같음을 확인한다. 복구를 새로운 모델 실험이나 일반적인 JSON 오류 해결로 표현하지 않는다.

근거: [SRC-0024506](../sources/history-140.md#src-0024506) 줄1–133 · [SRC-0022559](../sources/history-140.md#src-0022559) 줄1–165 · [SRC-0024507](../sources/history-140.md#src-0024507) 줄1–7 · [SRC-0024511](../sources/history-140.md#src-0024511) 줄1–6 · [SRC-0024509](../sources/history-140.md#src-0024509) NPZ pair_shift_matrix

<a id="claim-11"></a>

**실패 요약의 작성 시점과 비용.** initial_failure.json은 최초 프로세스가 남긴 원시 stack trace가 아니라 복구 코드가 나중에 작성하는 요약이다. 최초 실패 비용0.5907747초와 복구 산술0.07503449999785516초를 합친0.6658091999978552초가 원110 비용으로 한 번 정산됐다. 코드 경로·요약·원장은 부합하지만 최초 도구 응답·원시 예외 로그·정확한 정산 쓰기 시각은 복구하지 못했다.

근거: [SRC-0024507](../sources/history-140.md#src-0024507) 줄1–7 · [SRC-0022559](../sources/history-140.md#src-0022559) 줄30–59 · [SRC-0024512](../sources/history-140.md#src-0024512) JSON /elapsed_seconds, /charged_seconds_including_initial_failure · [SRC-0024555](../sources/history-140.md#src-0024555) JSON /new_cheap_diagnostic_seconds/calendar_alignment_110, /cheap_stage_details

<a id="claim-12"></a>

**timer와 RSS가 포함하는 범위.** 원111 산술 시간은0.17921170000045095초다. 원110 복구 timer는 저장 profile 로드·거리·요약 계산을 포함하고, 원111 timer는 입력·profile 로드·거리 계산·frozen archive 쓰기를 포함한다. import·settings·hash·최종 JSON은 제외돼 있으며 원110의 일반 timing_scope에 있는 profile archive 쓰기는 복구 분기에서 새로 수행되지 않는다. RSS34938880/70144000bytes는 각 한 번의 표본이고 peak가 아니다. marker 시각 차이도 이 timer나 전체 과정 비용을 대신하지 않는다.

근거: [SRC-0022559](../sources/history-140.md#src-0022559) 줄59–165 · [SRC-0022563](../sources/history-140.md#src-0022563) 줄48–185 · [SRC-0024511](../sources/history-140.md#src-0024511) 줄1–6 · [SRC-0024513](../sources/history-140.md#src-0024513) 줄1–6 · [SRC-0024558](../sources/history-140.md#src-0024558) 줄1–4 · [SRC-0024557](../sources/history-140.md#src-0024557) 줄1–6 · [SRC-0024512](../sources/history-140.md#src-0024512) JSON /sampled_rss_bytes, /timing_scope · [SRC-0024556](../sources/history-140.md#src-0024556) JSON /sampled_rss_bytes, /timing_scope

<a id="claim-13"></a>

**전후 원장과 입력 판본.** 원110 전/원109 후 원장은989194de…(SRC-0024508), 원110 후/원111 전은4a2f5162…(SRC-0024555), 원111 후는084b70d9…(원112 활성화 전 SRC-0024530)에 남아 있다. 각 차이는 해당 cheap 비용 키 하나와 detail 하나의 추가뿐이다. 당시 Tab78context·55488query행·RCTL optimizer29+통계 적합9=38·잔여9·reset0과 cap/예약 상태가 그대로다. 현재 루트 원장17a549fc…로 과거 판본을 대체하거나 갱신하지 않았다.

근거: [SRC-0024508](../sources/history-140.md#src-0024508) JSON (전체 값) · [SRC-0024555](../sources/history-140.md#src-0024555) JSON (전체 값) · [SRC-0024530](../sources/history-140.md#src-0024530) JSON (전체 값) · [SRC-0024513](../sources/history-140.md#src-0024513) 줄1–6 · [SRC-0024557](../sources/history-140.md#src-0024557) 줄1–6 · [SRC-0024515](../sources/history-140.md#src-0024515) JSON /source_hashes · [SRC-0024510](../sources/history-140.md#src-0024510) JSON /source_hashes · [SRC-0024559](../sources/history-140.md#src-0024559) JSON /source_hashes

## 예측 전 입력 검사의 조건과 결과

<a id="claim-14"></a>

**donor와 세 후보를 고른 규칙.** 각 target의 다른15cell 중 train21일 profile의 최소 MSE가 작은 donor2개를 골랐다. donor 동점은 정확한 최소 비용과 cell ID의 정렬 순서이며 이동량 동점 허용1e−12와 구별한다. 역방향 cost는부호를 반전한 mod24 이동 인덱스로 대응시켰다. 각 방향에서 무이동+train 비용이 작은 비영 이동2개를 남겨32방향×3후보로 만들었고 profile 최적 이동은 이 안에 포함됐다.

근거: [SRC-0022563](../sources/history-140.md#src-0022563) 줄65–107 · [SRC-0020867](../sources/history-140.md#src-0020867) 줄1–32 · [SRC-0024556](../sources/history-140.md#src-0024556) JSON /pairs · [SRC-0024554](../sources/history-140.md#src-0024554) NPZ pair_indices, phase_candidates

<a id="claim-15"></a>

**64시점과 두 절반.** query는168개 위치에서 floor(linspace(0,167,64))로 고른 서로 다른64시점이며 target672–839의 시간순이다. 처음32개는672–754, 뒤32개는756–839에 해당한다. 각각 mask로 남는 시점에서 이후 이동량 선택/고정 확인을 하겠다는 계획이며 원111은 정답으로 이동량을 고르지 않았다. 두 절반을 처음부터 독립 최종 test로 해석하지 않는다.

근거: [SRC-0020867](../sources/history-140.md#src-0020867) 줄1–32 · [SRC-0020868](../sources/history-140.md#src-0020868) 줄11–15 · [SRC-0024554](../sources/history-140.md#src-0024554) NPZ query_positions, query_target_times, common_masks

<a id="claim-16"></a>

**hour 두 열만 바꾼 동결 입력.** 16개 특징 중12/13열의 hour sin/cos만 (h+δ) mod24로 다시 계산했다. 나머지14열의 실제 최근 관측·요약·요일 값은32방향×3후보에서 정확히 보존됐고 시간 순서·target·horizon을 이동시키지 않았다. 무이동의 hour도 float32 저장값에서 float64 삼각함수로 재계산돼 최대1.55436e−8 차이가 있다. 이는 표현 차이이며 별도의 예측 효과를 측정한 결과가 아니다.

근거: [SRC-0022563](../sources/history-140.md#src-0022563) 줄108–117 · [SRC-0024554](../sources/history-140.md#src-0024554) NPZ context_X, query_X, shifted_query_X · [SRC-0029561](../sources/history-140.md#src-0029561) NPZ X · slice {'X': '[:,0:672,:]'}

<a id="claim-17"></a>

**donor 내부에서 정한 지원 반경.** donor context504행의 특징별 평균·population std로 거리 척도를 정했고 zero std는1로 처리하는 규칙이었다. 16특징의 RMS 표준화 Euclidean 거리에서 donor 내부 |행 인덱스 차이|≤8을 제외한 다섯 번째 이웃 거리의95percentile을 반경으로 썼다. context 시점이 연속 시간이라 이 제외는±8시간에 대응한다. query target으로 scaler나 반경을 맞추거나 통과 수에 맞춰 반경을 키우지 않았다.

근거: [SRC-0022563](../sources/history-140.md#src-0022563) 줄74–85 · [SRC-0024559](../sources/history-140.md#src-0024559) JSON /support · [SRC-0024554](../sources/history-140.md#src-0024554) NPZ context_means, context_scales, support_radii

<a id="claim-18"></a>

**같은 query에서 세 이동의 교집합.** 각 이동의 query→donor context 다섯 번째 이웃 거리가 donor 반경 이하여야 하며, 세 이동 모두를 만족하는 교집합 mask만 비교 대상으로 남겼다. 방향별 처음/뒤32시점에서 공통 시점이 각각16개 이상이어야 eligible이다. 예를 들어3737→4553은 개별 이동의 지원 수22/20/19와 달리 공통18개가15/3으로 나뉘어 탈락했다. 개별 지원 수·공통 수·절반 기준은 다른 수다.

근거: [SRC-0022563](../sources/history-140.md#src-0022563) 줄116–130 · [SRC-0024556](../sources/history-140.md#src-0024556) JSON /pairs/1 · [SRC-0024554](../sources/history-140.md#src-0024554) NPZ support_distances, common_masks, eligible_pairs

<a id="claim-19"></a>

**14방향·11target·남긴 반례.** 32방향 중14개가 통과했고 target11cell·donor9cell이었다. 전체의 profile 비영 최적은13/32, 통과 방향 안에서는5/14였다. 전역 입력 기준≥8방향/≥8target은 통과했지만18방향을 제외했으며4537·4553·5337·5365·6137은 eligible target이 없었다. 통과11cell에서의 가능성을 전체16cell·다른 도시·새 기간의 효용으로 확대하지 않는다.

근거: [SRC-0024556](../sources/history-140.md#src-0024556) JSON /aggregate, /pairs · [SRC-0024554](../sources/history-140.md#src-0024554) NPZ eligible_pairs, pair_indices

<a id="claim-20"></a>

**1222와3096의 다른 분모.** 2048=32×64에서 공통 시점1222개가 남은 값은 탈락 방향까지 포함한다. eligible14방향의807공통 시점×3이동=2421교차 추론 행이며, 같은 target 시점의 중복을 합집합으로 제거한 자기 기준은675행이다. 합계3096행, 필요한 target/donor cell의 합집합14context가 후속 비교의 상한이다.14방향이라는 수와14context는 의미가 다르며 원111이 이만큼 모델을 사용·예약한 것은 아니다.

근거: [SRC-0024556](../sources/history-140.md#src-0024556) JSON /aggregate · [SRC-0022563](../sources/history-140.md#src-0022563) 줄137–167 · [SRC-0024554](../sources/history-140.md#src-0024554) NPZ common_masks, eligible_pairs, own_baseline_masks, pair_indices

<a id="claim-21"></a>

**입력 지원과 label-free 범위.** 원111 코드의 입력 검사에는 query target Y를 읽는 경로가 없고 frozen archive15개 key에도 정답이 없다. 하지만 선행 원110 profile에는 train target과 다음 주 check target이 사용됐다. 이 두 단계 전체나 후속 원112의 정답 기반 선택을 label-free 또는 zero-shot clustering으로 부르지 않는다. 인접 context/query 입력은 실제 과거 관측을 공유할 수 있지만 공유 자체를 미래 정답 누출로 해석하지 않는다. 거리 반경 통과는 입력 기하의 필터이며 공통 조건부 분포·미래 예측 관계를 입증하지 않는다.

근거: [SRC-0022563](../sources/history-140.md#src-0022563) 줄1–185 · [SRC-0022559](../sources/history-140.md#src-0022559) 줄68–81 · [SRC-0020868](../sources/history-140.md#src-0020868) 줄15–15 · [SRC-0024559](../sources/history-140.md#src-0024559) JSON /query_targets_read · [SRC-0024560](../sources/history-140.md#src-0024560) 줄1–18 · [SRC-0024554](../sources/history-140.md#src-0024554) NPZ context_X, query_X, shifted_query_X, pair_indices, phase_candidates, common_masks, eligible_pairs, own_baseline_masks, support_distances, support_radii, context_means, context_scales, query_positions, query_target_times, cell_ids

## 당시 후속 계획과 나중의 보고서 판본

<a id="claim-22"></a>

**원112의 세 예측기는 당시 계획.** 원112 계획은 동결14방향·세 이동·공통 query에 TabICLv2, StandardScaler+Ridge(alpha1), 원101과 같은 HGB를 제공하는 비교다. Tab은 median·n_estimators1·batch1·CPU4·seed20260925와 로컬 ckpt를 명시했다. 추가 scaler는 각 donor context로만 맞추고 같은 context를 한 번 준비해 자기/교차 query를 묶겠다는 계획이었다. 이 문서를 읽은 것은 원112 예측 실행·RCTL 개선·구현 재현의 검수가 아니다.

근거: [SRC-0020868](../sources/history-140.md#src-0020868) 줄9–24

<a id="claim-23"></a>

**선택자와 평가 예측기의 분리.** 원112는 처음 절반의 정답 MAE로 이동을 고른 뒤 뒤 절반에서 고정 확인하고, 선택자5개(무이동/profile/Tab/Ridge/HGB)×평가 예측기3개의 저장 결과 표를 계획했다. 주 지표는 donor별 MAE를 cell 안에서 평균한 뒤11target을 같은 비중으로 평균하며 query 수로 가중하지 않는다. 같은 예측기의 저장 결과에서 서로 다른 선택자를 평가하려는 설계이며 모델 자체의 낮은 오차와 더 나은 좌표 선택을 분리한다. 같은 K의 RCTL 효용은 별도다.

근거: [SRC-0020868](../sources/history-140.md#src-0020868) 줄25–38

<a id="claim-24"></a>

**후속 안내가 추가된 보고서 판본.** 원111 verification에 적힌 보고서 SHA81c9716d…는 inventory의 현재 보고서 SHA13b7bfe0…와 다르다. 현재43행의3행 후속 안내와4행 빈 줄만 빼면 당시 SHA와 정확히 일치한다. 해시가 맞는 재구성본과 실제 보존된 당시 원본을 구별하며 재구성본을 새 source_id·본문 credit으로 세지 않는다. 후속 안내는 원112가 진행 기준에 실패했다고 기록하지만, 원112의 실제 예측 배열·결과 검수는 다음 묶음에 남아 있다.

근거: [SRC-0000136](../sources/history-140.md#src-0000136) 줄1–43 · [SRC-0024560](../sources/history-140.md#src-0024560) JSON /documents_sha256

## 선행연구와 재사용 한계

<a id="claim-25"></a>

**소속과 정렬의 공동 목적은 선행 구조.** Lederman·Singer의 원문 식25는 같은 class 안의 쌍별 정렬 비용을 합하며 소속과 group 변환을 공동으로 정한다. 식26은 동일 class 크기의 예이고 식52–55는 소속 일치 indicator로 목적을 다시 쓴다. 따라서 그 비용을 TabICL 오차로 바꾸는 것만으로 공동 결정 구조의 신규성이 생긴다는 주장은 성립하지 않는다. 현재 후보는 공동 최적화를 실행하지 않았으며 문헌의60개 synthetic signal 실험을 우리16cell 결과로 인용하지 않는다.

근거: [SRC-0020865](../sources/history-140.md#src-0020865) 줄1–35 · [1607.03464v1 원문](https://arxiv.org/pdf/1607.03464v1) · 선택 절 범위는 문헌 비교를 따른다

<a id="claim-26"></a>

**TROUT 회전과 실제 시각 이동.** TROUT 식1은 Fourier 벡터 전체에 같은 단위 복소 스칼라를 곱해 정렬하고 식2는 fusion penalty와 결합한다. 실제 cyclic time shift는 주파수마다 다른 phase factor를 주므로 이 연산과 일반적으로 같지 않다는 것은 원문 식에 대한 수학적 대조다. MM/ADMM의 stationary-point 논의와 O(n³) 초기 factorization/O(n²p) 반복 비용은 해당 논문의 범위이며 우리 Tab 후보의 실측·전역 최적 보장으로 쓰지 않았다. 공식 코드는 재현하지 않았다.

근거: [SRC-0020865](../sources/history-140.md#src-0020865) 줄1–35 · [2012.04756v2 원문](https://arxiv.org/pdf/2012.04756v2) · 선택 절 범위는 문헌 비교를 따른다

<a id="claim-27"></a>

**TROUT 정규화 표기를 재사용할 때.** 현재 PDF 본문3쪽과 부록6쪽의 정규화 식은 xᴴu/(||x||||u||)를 단위 복소 회전의 최소해와 연결한다. x=(1,0), u=(1,1)이면 그 비의 modulus는1/√2로1이 아니어서 일반적인 단위 회전 제약과 충돌한다. 이 표기 주의는 이번 아카이브의 작은 대수 대조이며 과거 실험 결과가 아니다. 공식 구현·실험 전체를 오류라고 판정하지 않으며, 식을 그대로 구현하기 전 원문과 단위 phase 정규화를 재확인해야 한다.

근거: [SRC-0020865](../sources/history-140.md#src-0020865) 줄1–35 · [2012.04756v2 원문](https://arxiv.org/pdf/2012.04756v2) · 선택 절 범위는 문헌 비교를 따른다

<a id="claim-28"></a>

**CAPS의 적용 위치.** CAPS는 SO(2)/RoPE 상대 위치 정렬, Clock 가중 softmax·prefix product·baseline의 세 경로를 attention 안에서 학습한다. 원문3.1–3.4와 Figure2의 내부 연산이며, RCTL 밖에서 먼저 고정할 cell별 달력 좌표와 적용 위치가 다르다. 그 모델의 linear/softmax 복잡도와 benchmark 결과를 현재 후보의 예측 성능·비용으로 옮기지 않았다. 비교는 arXiv v1의 선택 절이고 공식 구현은 미검수다.

근거: [SRC-0020865](../sources/history-140.md#src-0020865) 줄1–35 · [2602.02729v1 원문](https://arxiv.org/pdf/2602.02729v1) · 선택 절 범위는 문헌 비교를 따른다

<a id="claim-29"></a>

**AOSNet은 관측 상태를 학습해 보정.** AOSNet은 관측과 학습 prior의 Hilbert 진폭·phase·주파수 descriptor로 gate를 구해 식10에서 (1−G)X+GP로 관측 표현을 보정한다. 같은 phase의 다른 상태와 channel attention 분석은 평균 profile만으로 합치지 않을 이유를 설명하지만 고정 cell 소속의 RCTL 효용을 입증한 자료는 아니다. 우리 후보가 이 gate를 RCTL에 추가한 것은 아니다. 과거 검토 v1을 대조했고 이후 v2의 변경이나 공식 구현 전체는 검수하지 않았다.

근거: [SRC-0020865](../sources/history-140.md#src-0020865) 줄1–35 · [SRC-0020866](../sources/history-140.md#src-0020866) 줄1–51 · [2606.06010v1 원문](https://arxiv.org/pdf/2606.06010v1) · 선택 절 범위는 문헌 비교를 따른다

<a id="claim-30"></a>

**문헌 읽기의 실제 범위.** 네 편의 버전·서지·관련 본문과 핵심 수식/도식8쪽을 공식 PDF에 대조했다. NUG34쪽·TROUT6쪽·CAPS16쪽·AOSNet14쪽을 모두 전수 검토하거나 구현을 재현한 것은 아니다. NUG 제출일7월12일과 표지7월13일, CAPS 제출일2월2일과 표지2월4일도 구별한다. 과거 감사의 다른 abstract-only 후보와 당시 접근 실패를 fulltext 확인으로 승격하지 않았으며, 네 문헌만으로 관련 연구 전체를 조사했거나 신규성을 확정했다고 주장하지 않는다.

근거: [SRC-0020865](../sources/history-140.md#src-0020865) 줄1–35 · [1607.03464v1 원문](https://arxiv.org/pdf/1607.03464v1) · 선택 절 범위는 문헌 비교를 따른다 · [2012.04756v2 원문](https://arxiv.org/pdf/2012.04756v2) · 선택 절 범위는 문헌 비교를 따른다 · [2602.02729v1 원문](https://arxiv.org/pdf/2602.02729v1) · 선택 절 범위는 문헌 비교를 따른다 · [2606.06010v1 원문](https://arxiv.org/pdf/2606.06010v1) · 선택 절 범위는 문헌 비교를 따른다

## 검수 범위와 다음 재검토

<a id="claim-31"></a>

**현재 저장 근거와 재사용 범위.** 28개 고유 SHA/29경로를 연결했다. 새 literal 읽기는19개932행, 결과2개·원장2개는 공백을 생략하되 모든 JSON 값을 손실 없이 읽었고, 새 NPZ2개의9+15member를 저장 산술로 대조했다. 이전109 근거2개와 원101 입력 사본은 재사용하며 원101의 미래336행 전체를 새로 검토한 것으로 세지 않는다. 엄격한 저장 수식/동일성 대조264912개 값의 최대차이는2.66454e−15이고 float32 달력 일치 점검21504값의 오차1.55436e−8은 별도 허용1e−6 범위다. 반복 배열 원소 검사를 독립적인 성능 지표·새 모델 실험 수로 세지 않는다.

근거: [SRC-0020864](../sources/history-140.md#src-0020864) 줄1–42 · [SRC-0024509](../sources/history-140.md#src-0024509) NPZ train, split_a, split_b, check, cell_ids, center, scale, pair_shift_matrix, hour · [SRC-0024554](../sources/history-140.md#src-0024554) NPZ context_X, query_X, shifted_query_X, pair_indices, phase_candidates, common_masks, eligible_pairs, own_baseline_masks, support_distances, support_radii, context_means, context_scales, query_positions, query_target_times, cell_ids · [SRC-0029561](../sources/history-140.md#src-0029561) NPZ X, Y, cell_ids, context_times · slice {'X': '[:,0:672,:]', 'Y': '[:,0:672]'}

<a id="claim-32"></a>

**당시 판단과 다음 재검토.** 원110–111의 당시 판단은 다음 예측 관계 검사에 쓸 시각 차이와 입력을 마련했다는 범위였다. 새 시도 전에 원112 실제 예측 결과와 이후 판단, joint 좌표의 일관성, 동일 K의 RCTL·독립 기간·cell별 손해를 이어 확인해야 한다. profile 이득·입력 지원·예측 관계·좌표 선정·최종 RCTL 효용을 구별하고 기존과 달라지는 질문·조건을 기록한다. 원112 이후·옛 고유 판본·다른 형식·전체 통합/장기 팀 접근/최종 원본 변경분과 검색 검수는 남아 있으며 이번 묶음이 전체 Goal 완료는 아니다.

근거: [SRC-0020864](../sources/history-140.md#src-0020864) 줄1–42 · [SRC-0020868](../sources/history-140.md#src-0020868) 줄1–48 · [SRC-0000136](../sources/history-140.md#src-0000136) 줄1–43

## profile check의 악화15쌍

train MSE로 고른 이동을 뒤7일에 고정했다. 표는 저장된 원110 값이며 소수9자리 표시다. 전체120쌍과24이동 비용은 원본 결과 JSON에 남았다. 쌍별 표준화 profile 사이의 MAE이고 다음값 예측 오차가 아니다.

| cell i–j | δ시간 | 무이동 MAE | 정렬 MAE | 증가 |
|---|---:|---:|---:|---:|
| 3745–4545 | -2 | 0.684141126 | 0.767690471 | +0.083549345 |
| 3745–3753 | -1 | 0.720700572 | 0.795815869 | +0.075115297 |
| 4545–6145 | -1 | 0.331628039 | 0.386346621 | +0.054718581 |
| 3745–4565 | -1 | 0.515746985 | 0.563682687 | +0.047935701 |
| 3745–3765 | -5 | 0.725613450 | 0.767796257 | +0.042182807 |
| 5337–6165 | -1 | 0.167683305 | 0.199585011 | +0.031901706 |
| 3745–5353 | -1 | 0.867063762 | 0.898926781 | +0.031863018 |
| 3737–3753 | -1 | 0.361777498 | 0.391749935 | +0.029972437 |
| 3737–4553 | 1 | 0.184368356 | 0.213664969 | +0.029296613 |
| 4565–6153 | 1 | 0.211485171 | 0.234442223 | +0.022957052 |
| 5365–6137 | -1 | 0.237681284 | 0.258780282 | +0.021098998 |
| 4545–6137 | -1 | 0.428894810 | 0.444147078 | +0.015252269 |
| 3765–5353 | 1 | 0.182074641 | 0.194273359 | +0.012198718 |
| 6137–6145 | 1 | 0.322310965 | 0.333481686 | +0.011170721 |
| 3737–3765 | -2 | 0.471543934 | 0.475106729 | +0.003562795 |

## 원111의32방향 전체

앞/뒤 공통 수는 세 이동 모두의 반경을 통과한 query 수다. 각 절반≥16개여야 통과한다. 세 이동이 같은 query와 target을 비교하며 이 표에는 예측 오차가 없다. 제외18방향도 함께 남긴다.

| target→donor | 세 이동시간 | profile 선택 | 앞/뒤 공통 수 | 입력 검사 |
|---|---|---:|---:|---|
| 3737→3745 | 0, 1, -1 | 0 | 32/31 | 통과 |
| 3737→4553 | 0, 1, 2 | 1 | 15/3 | 제외 |
| 3745→3737 | 0, -1, 1 | 0 | 31/26 | 통과 |
| 3745→4553 | 0, -1, 1 | 0 | 10/12 | 제외 |
| 3753→5337 | 0, -1, 1 | 0 | 31/32 | 통과 |
| 3753→6165 | 0, -1, -2 | -1 | 5/0 | 제외 |
| 3765→5365 | 0, 1, -1 | 0 | 20/21 | 통과 |
| 3765→5353 | 0, 1, 2 | 1 | 28/30 | 통과 |
| 4537→6153 | 0, 2, 1 | 2 | 4/18 | 제외 |
| 4537→3765 | 0, 1, -1 | 0 | 0/0 | 제외 |
| 4545→5337 | 0, -1, 1 | 0 | 32/32 | 통과 |
| 4545→5365 | 0, -1, 1 | 0 | 11/8 | 제외 |
| 4553→3737 | 0, -1, -2 | -1 | 12/26 | 제외 |
| 4553→3745 | 0, 1, -1 | 0 | 12/27 | 제외 |
| 4565→4553 | 0, 1, 2 | 1 | 27/9 | 제외 |
| 4565→6153 | 0, 1, 2 | 1 | 32/32 | 통과 |
| 5337→6145 | 0, -1, 1 | 0 | 9/7 | 제외 |
| 5337→6165 | 0, -1, -2 | -1 | 3/0 | 제외 |
| 5345→3737 | 0, -1, -2 | -1 | 32/32 | 통과 |
| 5345→4553 | 0, -1, 1 | 0 | 17/13 | 제외 |
| 5353→3765 | 0, -1, -2 | -1 | 31/29 | 통과 |
| 5353→6153 | 0, 1, 2 | 0 | 32/32 | 통과 |
| 5365→6145 | 0, -1, 1 | 0 | 9/1 | 제외 |
| 5365→6137 | 0, -1, -2 | -1 | 25/14 | 제외 |
| 6137→5365 | 0, 1, 2 | 1 | 18/13 | 제외 |
| 6137→3765 | 0, 1, 2 | 0 | 7/7 | 제외 |
| 6145→6165 | 0, -1, 1 | 0 | 8/27 | 제외 |
| 6145→5337 | 0, 1, -1 | 0 | 32/29 | 통과 |
| 6153→4565 | 0, -1, -2 | -1 | 30/26 | 통과 |
| 6153→4553 | 0, 1, -1 | 0 | 20/18 | 통과 |
| 6165→6145 | 0, 1, -1 | 0 | 8/30 | 제외 |
| 6165→5365 | 0, 1, -1 | 0 | 22/32 | 통과 |

## 팀 재사용 안내

[정확사본과 member 범위](../sources/history-140.md)에서25개 새 사본 `706,098bytes`와 기존3개 사본을 연다. 원101 입력은 과거672행의 현재 검사와 이전 선택 검토를 연결했으며 미래336행의 새 전수 검토가 아니다. profiles와 frozen queries는 원코드를 재실행하지 않고 기존 배열을 읽는 재사용 근거다. 원110 최초 실패의 원시 tool/stack trace와 정확한 원장 쓰기 시각은 미복구다.

현재 보고서와 [당시 해시와 일치하는 재구성본](../evidence/0140-calendar-alignment-and-input-preflight/derived-report-before-followup.md.txt)을 구별한다. 재구성은 현재 원문3–4행의 제거만으로 당시 검수 SHA와 일치하는 byte 연결이며, 보존된 당시 물리 원본이나 새 연구자료 credit이 아니다. 원112 이후의 실제 실행·결과는 이어서 검수한다.

작성후19개932raw행·원110의120쌍16개 선택 필드·원111의32개 완전 노드/나머지 전체값·전후3원장의 전체 JSON 값·NPZ30개 member header와 선택/수량값을 대조했다. 원110의24이동 cost vectors·560개 개별 triangle 값·전체 배열 산술을 작성후 새로 전부 출력/재계산한 것으로 표현하지 않는다. 문헌의 선택 본문/수식8쪽 검수는 재사용했고 TROUT부록6쪽의 식을 작성후 다시 읽었다. 같은 에이전트의 두 번째 검토이며 독립 연구자 심사나 모델 재현이 아니다.
