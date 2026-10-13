# 원108 고정 가중치에서 BatchNorm 통계만 다시 계산한 결과

**이 조건에서는 훈련입력으로 BN 통계를 다시 계산해도 Tab-risk K4의 손해가 해결되지 않았다.** 세 방식의 14일 평균 오차는 모두 늘었지만, 개선된 cell과 날짜도 있었다. BN의 모든 영향이나 TabICL을 일반적으로 기각하는 근거로 쓰지 않는다.

[39출처/72경로](../sources/history-138.md) · [26주장](../verification/history-138-claims.json) · [작성 후 대조](../verification/history-138-second-pass.json) · [저장 수치 검사](../evidence/0138-fixed-weight-bn-statistics/saved-numeric-check.json) · [재사용·문헌 안내](../references/fixed-weight-bn-statistics.md)

## 질문·조건·결과

2026-09-26 [원106 같은 K 비교](0136-same-k-cellwise-error-transition.md)와 [원107 입력지원 진단](0137-calendar-retention-and-external-support.md)의 후속이다. 최종 가중치와 소속을 고정하고 BN 통계만 바꿨다. 당시에는 모델상태 적합 9회와 forward 계산을 수행했다. 현재 정리는 저장 배열·tensor byte·원장 산술을 확인한 것이며 원코드 실행, 모델 생성·학습·추론·BN 계산은 수행하지 않았다.

Milan hourly 고정 16cell, primary seed 20260925이다. global 1개, Tab-risk 4개, empirical-risk 4개의 기존 checkpoint를 사용했다. train은 index168–839의672시간, validation은840–1007의168시간, check는1008–1343의336시간이다. check는 이미 사용한 14일 개발구간으로 독립 최종평가가 아니다. 원106의20일 결과와 구별한다.

입력과 cell별 척도는 [원33–35](0033-0035-process-fit-gap.md)의 조건을 재사용한다. flat16열을8step×9channel로 바꾸는 정의와 저장 trainX/Y/scales의 일치를 확인했다. 실제 forward sequence 입력이나 원시자료 전체를 이번에 재현한 것은 아니다.

scaled MAE는 각cell·각시간을 같은 가중으로 평균했다. subtraction/abs는 float32, 평균은 float64다. 원단위 MAE와 섞지 않는다.

| 방식 | train 기존→재계산 | validation 기존→재계산 | 14일 check 기존→재계산 |
|---|---:|---:|---:|
| global K1 | 0.079981379 → 0.080073427 | 0.075371473 → 0.075727369 | 0.072873612 → 0.073333726 |
| Tab-risk K4 | 0.078401441 → 0.078393915 | 0.081656142 → 0.082472792 | 0.086002226 → 0.089940461 |
| empirical-risk K4 | 0.075087383 → 0.074852858 | 0.078883120 → 0.079552410 | 0.079864979 → 0.083497946 |

Tab−empirical 차이는14일에서+0.006137247→+0.006442515다. 앞7일은+0.003136804→+0.002995205로 줄고, 뒤7일은+0.009137689→+0.009889824로 늘었다. 각모델9개 모두 check 평균이 나빠졌지만, Tab cluster2·3의 train/validation은 개선됐다.

| 방식 | 14일 평균이 개선된 cell | 개선된 날짜(1부터14) | cell×day 개선/악화(224개) |
|---|---|---|---:|
| global | 3745, 5337 | 2, 9, 13, 14 | 94 / 130 |
| Tab-risk | 4553, 5337 | 없음 | 78 / 146 |
| empirical-risk | 4565, 5365 | 3 | 69 / 155 |

이전 후보를 이 단순 보정으로 복구하는 방향은 당시 채택하지 않았다. 이 단일 seed·고정 가중치·유한 훈련입력 통계의 부정결과이며, 원인 식별이나 새 클러스터링의 성능 검증은 아니다. 겹치는 cell/day를 독립 반복으로 세지 않는다.

## 저장 근거와 재사용

원checkpoint9개와 재계산 buffer9개를 팀용 정확 사본으로 연결했다. 새buffer 파일에는 파라미터가 없다. 원checkpoint와 함께 사용해야 재계산 상태를 복원할 수 있으며 이번 정리에서 실행 재현은 확인하지 않았다. 이전에는 이 checkpoint의 hash/크기만 연결돼 있었다.

원checkpoint의 파라미터 SHA와 보고된 before/after SHA는 일치하고 저장buffer의24변경키/12불변 batch counter를 확인했다. 적합후 live 파라미터 tensor가 따로 없으므로 실제 파라미터 불변은 보고/assertion 범위를 넘지 않는다. 당시 복원 검사도 모델별 첫16행, 총144행으로 제한됐다.

원장96e00…는 파생 재구성 byte의SHA가 저장settings와 일치했다. [파생 사본](../evidence/0138-fixed-weight-bn-statistics/derived-reservation-snapshot.json)은 복구된 원본 파일이 아니다. 정산 전체JSON 값은 보존된300d59… 원장과 맞지만 정확한 쓰기시각과 실행도구 응답은 미복구다. optimizer29+통계적합9=combined38/cap47/잔여9이고8.635802초는RCTL wall의 부분시간이다.

주요 결과3665행·부분결과1507행을 포함한 첫11literal5833행을 읽었다. 별도 작성 후478raw행·9개 완전record node·주장 관련JSON·61NPZ header/기존저장검수를 대조했다. 부분결과 records는 원결과와 전체값이 같음을 비교했고, 고유elapsed/RSS를 따로 읽었다. 결과전체의literal 재독이나 NPZ값 재계산을 새로 한 것은 아니다.

저장산술2208대조 중1776aggregate/comparison은 정확히 일치했다. BN variance 평균의 최대3.259629e−8 차이는 reduction 반올림 범위다. 원본78경로/보호6개는 불변이다. 과거 Goal·예산·다음109행동은 역사자료이며 현재 실행 지시가 아니다. 원109이후·긴고유판본·다른형식·통합/장기접근/최종delta/검색검수와 전체아카이브는 미완료다.

## 주장별 근거

<a id="claim-01"></a>

### H138-C01 · 질문과 선행 기록

원108은 원106 같은 K의 손해와 원107 입력지원 진단 다음에, 저장된 최종 RCTL 가중치·소속을 고정하고 훈련입력만으로 BN 통계를 다시 계산하면 차이가 줄어드는지 확인한 기록이다. 새 클러스터링 알고리즘을 검증한 기록으로 세지 않는다.

근거: [SRC-0020859](../sources/history-138.md#src-0020859) 행1–38 · [SRC-0020860](../sources/history-138.md#src-0020860) 행1–55

<a id="claim-02"></a>

### H138-C02 · 실제 수행과 현재 정리 구분

완료 결과에는 global1·Tab-risk4·empirical-risk4의 통계 적합9개, optimizer fit/step·gradient0이 남았다. 당시에는 prefix 및 prediction forward를 수행한 모델상태 적합이다. 현재 아카이브는 원code 실행/import·모델 생성/학습/추론/forward/BN 계산0이며 저장값 산술만 수행했다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /complete, /counts · [SRC-0022934](../sources/history-138.md#src-0022934) 행222–278

<a id="claim-03"></a>

### H138-C03 · 자료와 평가 범위

Milan internet hourly pilot 고정16cell, train168–839(672시간/cell), validation840–1007(168), development check1008–1343(14일336)이다. 원106의20일480시간과 다르고 원101에서 이미 사용한 check여서 독립 최종평가가 아니다. cell순서/target/scale를 이전 저장자료와 대조했다.

근거: [SRC-0029136](../sources/history-138.md#src-0029136) JSON /train_target_indices, /validation_target_indices, /development_check_target_indices, /independent_final_evaluation · [SRC-0029561](../sources/history-138.md#src-0029561) NPZ cell_ids, context_times, query_times, Y, scales · [SRC-0029132](../sources/history-138.md#src-0029132) NPZ cell_ids, train_y, validation_y, check_y, scales

<a id="claim-04"></a>

### H138-C04 · 입력 표현과 정규화 출처

flat16열의 앞8값은8step의 channel0, 뒤8특징은 각step의 나머지8channel로 반복해8×9 sequence를 구성한다. 저장 flat trainX가 design과 같고 Y/scales도 일치한다. cell별 원시0–671 평균 정규화는 기존 원33–35 기록의 조건을 재사용하며 원시전체나 실제 sequence forward 입력을 새로 저장·재현한 것은 아니다.

근거: [SRC-0022934](../sources/history-138.md#src-0022934) 행46–51 · [SRC-0022934](../sources/history-138.md#src-0022934) 행193–216 · [SRC-0023577](../sources/history-138.md#src-0023577) NPZ X, Y, scales, cell_indices, times · [SRC-0029561](../sources/history-138.md#src-0029561) NPZ X, Y, scales

<a id="claim-05"></a>

### H138-C05 · 고정 모델과 단일 seed

primary seed20260925의 기존9 checkpoint와 members를 사용한다. Tab/empirical은 각각K4·4cell/cluster, global은16cell이다. 기존 optimizer 설정(max80epoch·batch256·patience10·lr0.001·Adam epsilon1e−7·MAE)과 이번 통계/예측 batch512·threads4를 구별한다. secondary seed·새 소속·혼합/threshold 탐색은 실행 범위에 없다.

근거: [SRC-0029136](../sources/history-138.md#src-0029136) JSON /seed, /methods, /checkpoint_count, /batch, /threads · [SRC-0030238](../sources/history-138.md#src-0030238) JSON /max_epochs, /batch_size, /patience, /learning_rate, /adam_eps, /loss, /tasks/0, /tasks/1, /tasks/2, /tasks/3, /tasks/4, /tasks/5, /tasks/6, /tasks/7, /tasks/8 · [SRC-0030237](../sources/history-138.md#src-0030237) JSON /0, /1, /2, /3, /4, /5, /6, /7, /8

<a id="claim-06"></a>

### H138-C06 · BN 구조와 계산 모드

정의에는 여섯 block에 BN2개씩 총12개, epsilon0.001이 있다. 통계 적합은 eval/inference 모드로 dropout을 끄고, 앞쪽 BN 통계를 먼저 바꾼 상태에서 현재 BN 직전 입력을 모은다. affine 파라미터·epsilon·가중치·partition은 고정한다고 구현과 결과에 기록했다.

근거: [SRC-0023048](../sources/history-138.md#src-0023048) 행1–60 · [SRC-0022934](../sources/history-138.md#src-0022934) 행117–190 · [SRC-0029133](../sources/history-138.md#src-0029133) JSON /records/0/layers, /records/1/layers, /records/2/layers, /records/3/layers, /records/4/layers, /records/5/layers, /records/6/layers, /records/7/layers, /records/8/layers

<a id="claim-07"></a>

### H138-C07 · 분산 식의 범위

float64 sum/square_sum/count로 훈련입력의 유한집합 평균과 E[x²]−E[x]²를 계산하며 작은 음수만0으로 제한한다. N/(N−1) 보정이나 시계열 표본의 iid/불편분산 보장은 없다. 이는 저장 BN 입력을 현재 다시 계산하거나 논문 식2를 그대로 재현했다는 주장이 아니다.

근거: [SRC-0022934](../sources/history-138.md#src-0022934) 행145–190

<a id="claim-08"></a>

### H138-C08 · 기존 예측 일치

새 NPZ의 original train/validation/check 값56,448개가 기존 원34와 원pilot 미래예측의 앞336시간과 정확히 일치한다. 당시 보고된 reproduction maxdiff0·허용1e−5도 일치한다. 이 대조는 저장 예측 간 일치이며 현재 모델 forward의 독립 재현이 아니다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /max_reproduction_abs_difference, /records/0/reproduction_differences, /records/1/reproduction_differences, /records/2/reproduction_differences, /records/3/reproduction_differences, /records/4/reproduction_differences, /records/5/reproduction_differences, /records/6/reproduction_differences, /records/7/reproduction_differences, /records/8/reproduction_differences · [SRC-0022934](../sources/history-138.md#src-0022934) 행238–247 · [SRC-0027514](../sources/history-138.md#src-0027514) NPZ global_20260925_cluster0_train_prediction, global_20260925_cluster0_validation_prediction, tabicl_risk_20260925_cluster0_train_prediction, tabicl_risk_20260925_cluster0_validation_prediction, tabicl_risk_20260925_cluster1_train_prediction, tabicl_risk_20260925_cluster1_validation_prediction, tabicl_risk_20260925_cluster2_train_prediction, tabicl_risk_20260925_cluster2_validation_prediction, tabicl_risk_20260925_cluster3_train_prediction, tabicl_risk_20260925_cluster3_validation_prediction, empirical_risk_20260925_cluster0_train_prediction, empirical_risk_20260925_cluster0_validation_prediction, empirical_risk_20260925_cluster1_train_prediction, empirical_risk_20260925_cluster1_validation_prediction, empirical_risk_20260925_cluster2_train_prediction, empirical_risk_20260925_cluster2_validation_prediction, empirical_risk_20260925_cluster3_train_prediction, empirical_risk_20260925_cluster3_validation_prediction, cell_ids, train_y, validation_y · [SRC-0030211](../sources/history-138.md#src-0030211) NPZ empirical_risk_20260925, global_20260925, tabicl_risk_20260925, y, cell_ids, scales

<a id="claim-09"></a>

### H138-C09 · 파라미터 보존의 증거 한계

각 원checkpoint의142개 저장 tensor 중106개 파라미터 byte와 이름을 등록 순서대로 합쳐 계산한 SHA는 보고된 before/after SHA와 모두 일치한다. 새 파일은36개 buffer만 담아 적합후 파라미터 tensor는 별도 보존되지 않았다. 따라서 실제 적합후 live 파라미터 불변의 독립 확인은 보고/assertion 범위를 넘지 않는다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /records/0/parameter_sha256_before, /records/1/parameter_sha256_before, /records/2/parameter_sha256_before, /records/3/parameter_sha256_before, /records/4/parameter_sha256_before, /records/5/parameter_sha256_before, /records/6/parameter_sha256_before, /records/7/parameter_sha256_before, /records/8/parameter_sha256_before, /records/0/parameter_sha256_after, /records/1/parameter_sha256_after, /records/2/parameter_sha256_after, /records/3/parameter_sha256_after, /records/4/parameter_sha256_after, /records/5/parameter_sha256_after, /records/6/parameter_sha256_after, /records/7/parameter_sha256_after, /records/8/parameter_sha256_after · [SRC-0022934](../sources/history-138.md#src-0022934) 행231–261 · [SRC-0030240](../sources/history-138.md#src-0030240) 저장 tensor byte 선택검수 · [SRC-0030282](../sources/history-138.md#src-0030282) 저장 tensor byte 선택검수 · [SRC-0030285](../sources/history-138.md#src-0030285) 저장 tensor byte 선택검수 · [SRC-0030288](../sources/history-138.md#src-0030288) 저장 tensor byte 선택검수 · [SRC-0030291](../sources/history-138.md#src-0030291) 저장 tensor byte 선택검수 · [SRC-0030213](../sources/history-138.md#src-0030213) 저장 tensor byte 선택검수 · [SRC-0030216](../sources/history-138.md#src-0030216) 저장 tensor byte 선택검수 · [SRC-0030219](../sources/history-138.md#src-0030219) 저장 tensor byte 선택검수 · [SRC-0030222](../sources/history-138.md#src-0030222) 저장 tensor byte 선택검수

<a id="claim-10"></a>

### H138-C10 · 변경 buffer 확인

원checkpoint9와 새buffer9의 저장 byte를 대조해 각 모델에서 running_mean/var24키가 바뀌고 num_batches_tracked12키는 그대로임을 확인했다. 108층의 변화 최대값은 저장 보고와 정확히 일치했고 variance 평균은 reduction 반올림 허용2e−7 안이다. GLOBAL/REDUCE를 호출하거나 pickle unpickle/torch import 없이 symbolic descriptor와 raw storage만 읽었다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /records/0/changed_state_keys, /records/1/changed_state_keys, /records/2/changed_state_keys, /records/3/changed_state_keys, /records/4/changed_state_keys, /records/5/changed_state_keys, /records/6/changed_state_keys, /records/7/changed_state_keys, /records/8/changed_state_keys, /records/0/layers, /records/1/layers, /records/2/layers, /records/3/layers, /records/4/layers, /records/5/layers, /records/6/layers, /records/7/layers, /records/8/layers · [SRC-0030240](../sources/history-138.md#src-0030240) 저장 tensor byte 선택검수 · [SRC-0030282](../sources/history-138.md#src-0030282) 저장 tensor byte 선택검수 · [SRC-0030285](../sources/history-138.md#src-0030285) 저장 tensor byte 선택검수 · [SRC-0030288](../sources/history-138.md#src-0030288) 저장 tensor byte 선택검수 · [SRC-0030291](../sources/history-138.md#src-0030291) 저장 tensor byte 선택검수 · [SRC-0030213](../sources/history-138.md#src-0030213) 저장 tensor byte 선택검수 · [SRC-0030216](../sources/history-138.md#src-0030216) 저장 tensor byte 선택검수 · [SRC-0030219](../sources/history-138.md#src-0030219) 저장 tensor byte 선택검수 · [SRC-0030222](../sources/history-138.md#src-0030222) 저장 tensor byte 선택검수 · [SRC-0029130](../sources/history-138.md#src-0029130) 저장 tensor byte 선택검수 · [SRC-0029137](../sources/history-138.md#src-0029137) 저장 tensor byte 선택검수 · [SRC-0029138](../sources/history-138.md#src-0029138) 저장 tensor byte 선택검수 · [SRC-0029139](../sources/history-138.md#src-0029139) 저장 tensor byte 선택검수 · [SRC-0029140](../sources/history-138.md#src-0029140) 저장 tensor byte 선택검수 · [SRC-0029126](../sources/history-138.md#src-0029126) 저장 tensor byte 선택검수 · [SRC-0029127](../sources/history-138.md#src-0029127) 저장 tensor byte 선택검수 · [SRC-0029128](../sources/history-138.md#src-0029128) 저장 tensor byte 선택검수 · [SRC-0029129](../sources/history-138.md#src-0029129) 저장 tensor byte 선택검수

<a id="claim-11"></a>

### H138-C11 · 복원 검사의 제한

당시 복원은 모델별 check의 첫min(16,행수)개, 총144행과 original_state hash assertion이다. 모든cell/전체 예측을 복원검사한 것이 아니며 복원후 출력은 별도 저장되지 않았다. 보고 maxdiff0을 전체 독립 복원 성공으로 확대하지 않는다.

근거: [SRC-0022934](../sources/history-138.md#src-0022934) 행269–275 · [SRC-0029133](../sources/history-138.md#src-0029133) JSON /max_restoration_abs_difference, /counts, /records/0/restoration_max_abs_difference, /records/1/restoration_max_abs_difference, /records/2/restoration_max_abs_difference, /records/3/restoration_max_abs_difference, /records/4/restoration_max_abs_difference, /records/5/restoration_max_abs_difference, /records/6/restoration_max_abs_difference, /records/7/restoration_max_abs_difference, /records/8/restoration_max_abs_difference

<a id="claim-12"></a>

### H138-C12 · 평균 오차의 방향

14일 scaled MAE는 global0.072873612→0.073333726, Tab-risk0.086002226→0.089940461, empirical-risk0.079864979→0.083497946로 모두 증가했다. validation 평균도 모두 증가했다. Tab/empirical train 평균은 조금 감소하고 global train은 증가했다. float32 subtraction/abs 뒤 float64 평균을 보존하며 원단위 MAE와 합치지 않는다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /aggregates/global/original/train_mae, /aggregates/global/recalibrated/train_mae, /aggregates/tabicl_risk/original/train_mae, /aggregates/tabicl_risk/recalibrated/train_mae, /aggregates/empirical_risk/original/train_mae, /aggregates/empirical_risk/recalibrated/train_mae, /aggregates/global/original/validation_mae, /aggregates/global/recalibrated/validation_mae, /aggregates/tabicl_risk/original/validation_mae, /aggregates/tabicl_risk/recalibrated/validation_mae, /aggregates/empirical_risk/original/validation_mae, /aggregates/empirical_risk/recalibrated/validation_mae, /aggregates/global/original/check_mae, /aggregates/global/recalibrated/check_mae, /aggregates/tabicl_risk/original/check_mae, /aggregates/tabicl_risk/recalibrated/check_mae, /aggregates/empirical_risk/original/check_mae, /aggregates/empirical_risk/recalibrated/check_mae · [SRC-0029132](../sources/history-138.md#src-0029132) NPZ cell_ids, scales, train_y, validation_y, check_y, global_original_train, global_original_validation, global_original_check, global_recalibrated_train, global_recalibrated_validation, global_recalibrated_check, tabicl_risk_original_train, tabicl_risk_original_validation, tabicl_risk_original_check, tabicl_risk_recalibrated_train, tabicl_risk_recalibrated_validation, tabicl_risk_recalibrated_check, empirical_risk_original_train, empirical_risk_original_validation, empirical_risk_original_check, empirical_risk_recalibrated_train, empirical_risk_recalibrated_validation, empirical_risk_recalibrated_check

<a id="claim-13"></a>

### H138-C13 · K4 차이와 반기간 반례

Tab−empirical check차이는+0.006137247→+0.006442515이며 앞7일+0.003136804→+0.002995205로 줄고 뒤7일+0.009137689→+0.009889824로 늘었다. 두기간 모두 평균 순위가 뒤집히지 않았다. 전체gap 증가를 두반기간 모두 증가로 요약하지 않는다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /comparisons/original/check, /comparisons/recalibrated/check, /comparisons/original/first_7_days, /comparisons/recalibrated/first_7_days, /comparisons/original/last_7_days, /comparisons/recalibrated/last_7_days

<a id="claim-14"></a>

### H138-C14 · cell과 날짜의 개선 사례

각방법의14일 cell평균은14개 악화·2개 개선이다. 개선cell은 global3745/5337, Tab4553/5337, empirical4565/5365다. 하루16cell평균 개선은 global2/9/13/14일, empirical3일, Tab0일이다. cell×day224개에서 개선/악화는94/130·78/146·69/155다. 겹치는 시계열 구간을 독립 반복이나 유의성 표본으로 세지 않는다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /aggregates/global/original/check_cell_mae, /aggregates/global/recalibrated/check_cell_mae, /aggregates/tabicl_risk/original/check_cell_mae, /aggregates/tabicl_risk/recalibrated/check_cell_mae, /aggregates/empirical_risk/original/check_cell_mae, /aggregates/empirical_risk/recalibrated/check_cell_mae, /aggregates/global/original/day_mae, /aggregates/global/recalibrated/day_mae, /aggregates/tabicl_risk/original/day_mae, /aggregates/tabicl_risk/recalibrated/day_mae, /aggregates/empirical_risk/original/day_mae, /aggregates/empirical_risk/recalibrated/day_mae · [SRC-0029132](../sources/history-138.md#src-0029132) NPZ global_original_check, global_recalibrated_check, tabicl_risk_original_check, tabicl_risk_recalibrated_check, empirical_risk_original_check, empirical_risk_recalibrated_check, check_y

<a id="claim-15"></a>

### H138-C15 · cluster 평균과 국소 개선

9개 checkpoint 모두 check 평균은 증가했다. Tab cluster2·3은 train/validation이 좋아져도 check는 나빠졌다. cluster 평균의 악화와 일부cell/day 개선을 함께 보존하며 개별 모델 float32 reduction과 전체 float64 평균의 작은 차이를 오류로 취급하지 않는다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /records/0/train_original_mae, /records/0/train_recalibrated_mae, /records/0/validation_original_mae, /records/0/validation_recalibrated_mae, /records/0/check_original_mae, /records/0/check_recalibrated_mae, /records/1/train_original_mae, /records/1/train_recalibrated_mae, /records/1/validation_original_mae, /records/1/validation_recalibrated_mae, /records/1/check_original_mae, /records/1/check_recalibrated_mae, /records/2/train_original_mae, /records/2/train_recalibrated_mae, /records/2/validation_original_mae, /records/2/validation_recalibrated_mae, /records/2/check_original_mae, /records/2/check_recalibrated_mae, /records/3/train_original_mae, /records/3/train_recalibrated_mae, /records/3/validation_original_mae, /records/3/validation_recalibrated_mae, /records/3/check_original_mae, /records/3/check_recalibrated_mae, /records/4/train_original_mae, /records/4/train_recalibrated_mae, /records/4/validation_original_mae, /records/4/validation_recalibrated_mae, /records/4/check_original_mae, /records/4/check_recalibrated_mae, /records/5/train_original_mae, /records/5/train_recalibrated_mae, /records/5/validation_original_mae, /records/5/validation_recalibrated_mae, /records/5/check_original_mae, /records/5/check_recalibrated_mae, /records/6/train_original_mae, /records/6/train_recalibrated_mae, /records/6/validation_original_mae, /records/6/validation_recalibrated_mae, /records/6/check_original_mae, /records/6/check_recalibrated_mae, /records/7/train_original_mae, /records/7/train_recalibrated_mae, /records/7/validation_original_mae, /records/7/validation_recalibrated_mae, /records/7/check_original_mae, /records/7/check_recalibrated_mae, /records/8/train_original_mae, /records/8/train_recalibrated_mae, /records/8/validation_original_mae, /records/8/validation_recalibrated_mae, /records/8/check_original_mae, /records/8/check_recalibrated_mae

<a id="claim-16"></a>

### H138-C16 · 당시 판단의 기각 범위

이 단일조건에서 훈련입력 통계 재계산만으로 Tab K4 손해나 global 대비 손해가 해결되지 않았다. BN이 원인이 아니라는 일반 기각, Tab 자체의 기각, 새 소속 성능 우위나 독립 clustering validation으로 확대하지 않는다. 관계충돌·유한표본·최적화·평가절차 등 경쟁원인은 남는다.

근거: [SRC-0020860](../sources/history-138.md#src-0020860) 행1–55 · [SRC-0029133](../sources/history-138.md#src-0029133) JSON /new_clustering_rule, /partition_changes, /independent_test, /clustering_validation_passed, /comparisons

<a id="claim-17"></a>

### H138-C17 · 호출·행수와 통계 분모

12층×9모델의 prefix828회/387072행, 두mode×3방법×16cell×(672+168+336)=primary112896행, 복원144행, prediction261회가 batch512로 설명된다. moment_count/channel은 global86016·각cluster21504이며 sample×8step이지 독립 관측 수가 아니다. 현재 새 호출은0이다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /counts, /records/0/layers, /records/1/layers, /records/2/layers, /records/3/layers, /records/4/layers, /records/5/layers, /records/6/layers, /records/7/layers, /records/8/layers · [SRC-0029136](../sources/history-138.md#src-0029136) JSON /expected_calibration_prefix_rows, /expected_primary_prediction_rows, /batch · [SRC-0022934](../sources/history-138.md#src-0022934) 행145–177

<a id="claim-18"></a>

### H138-C18 · 시간과 메모리 범위

보고된 entire_stage8.635802399992826초/RSS271278080bytes는 imports/초기hash 이후부터 data load·모델계산·partial쓰기·predictions저장까지이며 최종rehash/summary직렬화는 제외한다. calibration_seconds9개의 합은 이 전체의 부분시간이다. 현재 측정한 모델시간이나 원33 fit시간과 중복 합산하지 않는다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /entire_stage_seconds, /timing_scope, /counts, /records/0/calibration_seconds, /records/1/calibration_seconds, /records/2/calibration_seconds, /records/3/calibration_seconds, /records/4/calibration_seconds, /records/5/calibration_seconds, /records/6/calibration_seconds, /records/7/calibration_seconds, /records/8/calibration_seconds

<a id="claim-19"></a>

### H138-C19 · 부분결과의 고유 내용

partial의9records는 최종records와 같고 current=null이다. partial_elapsed8.607991600001696초/peak271220736bytes와 최종시간/peak는 다르다. 최종 partial을 별도 실험·실패 재시도·전체 바이트 동일사본으로 세지 않는다. 검수 boolean은 당시 보고이며 독립 모델 실행 증명이 아니다.

근거: [SRC-0029131](../sources/history-138.md#src-0029131) JSON /records, /counts, /current, /elapsed_seconds · [SRC-0029141](../sources/history-138.md#src-0029141) JSON /checks, /source_sha256, /result_sha256, /research_goal_complete, /stage109_executed

<a id="claim-20"></a>

### H138-C20 · 9회 상태 적합의 회계

예전 optimizer29회·Tab78context/55488query행은 유지하며 BN상태 적합9회를 같은 allowance에 차감해 combined38/cap47/잔여9가 됐다. 추가18회 예약 중9개를 사용했고 gradient/optimizer0이어도 모델상태 적합 비용은0이 아니다. 8.635802초는 RCTL wall의 부분이며 두번 더하지 않는다. budget_resets0/automatic_recharge=false는 현재 예산 지시가 아니다.

근거: [SRC-0022121](../sources/history-138.md#src-0022121) 행23–107 · [SRC-0020858](../sources/history-138.md#src-0020858) JSON /used, /caps, /remaining_count_budgets, /budget_resets · [SRC-0032507](../sources/history-138.md#src-0032507) JSON /used, /caps, /remaining_count_budgets, /additional_rounds, /RCTL_count_accounting_note, /statistics_adaptation_stages, /budget_resets

<a id="claim-21"></a>

### H138-C21 · 실행전 원장 재구성의 제한

settings의 실행전96e00… 원장 SHA와 같은 JSON byte를 before98972…·저장107비용·정적회계 규칙에서 재구성했고,9회 정산을 적용한 전체JSON 값은 after300d59…와 일치했다. 파생 snapshot이지 발견/복구된 원본파일이 아니며 원본 목록/본문 credit은0이다. 실제 도구회계응답·정확한 쓰기시각은 미복구다.

근거: [SRC-0029136](../sources/history-138.md#src-0029136) JSON /ledger_before_run_sha256, /round_id · [SRC-0022121](../sources/history-138.md#src-0022121) 행23–107 · [SRC-0032507](../sources/history-138.md#src-0032507) JSON /cheap_stage_details/9, /new_cheap_diagnostic_seconds/support_composition_107, /additional_rounds

<a id="claim-22"></a>

### H138-C22 · 입력18hash와 종료 표식

계획·실행code·모델정의·설정/배열·원checkpoint의18개 hash가 현재 보존 byte와 맞고 종료표식의result hash도 일치한다. 원107과 달리108 결과에는 실행code SHA가 기록돼 있다. 이는 보고된 코드 pin이며 당시에 실행된 프로세스의 독립 도구로그 복구는 아니다. 원본78경로/보호6개의 hash도 불변이다.

근거: [SRC-0029136](../sources/history-138.md#src-0029136) JSON /source_hashes · [SRC-0029133](../sources/history-138.md#src-0029133) JSON /source_files_unchanged · [SRC-0029135](../sources/history-138.md#src-0029135) JSON /settings_sha256, /unix · [SRC-0029134](../sources/history-138.md#src-0029134) JSON /result_sha256, /complete, /unix

<a id="claim-23"></a>

### H138-C23 · 선행문헌과 신규성 경계

Wu·Johnson의 Rethinking Batch in BatchNorm v1 §3.2–3.3/A.2–A.3에서 고정모델 통계와 층별절차를 확인했다. §3.2 실험의 모멘트식과 A.2 식2의N/(N−1) 불편분산 보정을 구별한다. 원108은 유한집합 모멘트를 채택한다. 영상분류 결과를 Milan 성능 보장이나 Tab 클러스터링 신규성으로 이전하지 않는다.

근거: [SRC-0020859](../sources/history-138.md#src-0020859) 행1–38 · [SRC-0022934](../sources/history-138.md#src-0022934) 행145–190

문헌: [Wu·Johnson v1 §3.2–3.3/A.2–A.3](https://arxiv.org/pdf/2105.07576v1). 선택절과13쪽 수식을 확인했으며 논문전체 판독/재현이 아니다.

<a id="claim-24"></a>

### H138-C24 · 과거 Goal·다음 행동

당시 continuation_state의 getGoal active·heartbeat 미재생성·차단감사 초기화·next109 logs-only는 역사적 운영 보고다. nativeGoal 도구응답과 정확한 section9.1 판본은 복구하지 않았다. 이 문장을 현재 Goal/자동화/예산/모델 권한으로 실행하지 않는다.

근거: [SRC-0020857](../sources/history-138.md#src-0020857) 행1–22 · [SRC-0020860](../sources/history-138.md#src-0020860) 행1–55

<a id="claim-25"></a>

### H138-C25 · 재사용과 재검토 조건

같은 seed·가중치·K4·train통계·14일check의 단순반복 전에 이 부정결과와 개선cell/day를 찾는다. 새질문은 비교할 원인과 달라진 입력/기간/통계/학습조건을 명시하고, 이미 본14일에 맞춘 통계 혼합·layer/threshold·소속 선택을 독립검증으로 세지 않는다. 원checkpoint와 새buffer를 같이 사용해야 재계산 상태를 복원할 수 있으며 현재 실행 검증은 없다.

근거: [SRC-0020859](../sources/history-138.md#src-0020859) 행1–38 · [SRC-0020860](../sources/history-138.md#src-0020860) 행1–55 · [SRC-0029133](../sources/history-138.md#src-0029133) JSON /independent_test, /clustering_validation_passed

<a id="claim-26"></a>

### H138-C26 · 검수 범위와 남은 기록

첫11개 literal5833행, 모델정의60행 재사용·39SHA/72경로·새NPZ23키와 연결38키, 원checkpoint9/새buffer9의 저장tensor byte를 대조했다. 수치2208회 중 aggregate/comparison1776개는 정확히 일치하고 BN variance reduction의 최대차이는3.259629e−8이다. 원모델 재현/독립 인간심사/전체 과거기록 완료가 아니다. 원109이후·긴고유판본·다른형식·통합·장기팀접근·최종원본delta/검색검수가 남는다.

근거: [SRC-0029133](../sources/history-138.md#src-0029133) JSON /complete · [SRC-0029132](../sources/history-138.md#src-0029132) NPZ cell_ids, scales, train_y, validation_y, check_y, global_original_train, global_original_validation, global_original_check, global_recalibrated_train, global_recalibrated_validation, global_recalibrated_check, tabicl_risk_original_train, tabicl_risk_original_validation, tabicl_risk_original_check, tabicl_risk_recalibrated_train, tabicl_risk_recalibrated_validation, tabicl_risk_recalibrated_check, empirical_risk_original_train, empirical_risk_original_validation, empirical_risk_original_check, empirical_risk_recalibrated_train, empirical_risk_recalibrated_validation, empirical_risk_recalibrated_check
