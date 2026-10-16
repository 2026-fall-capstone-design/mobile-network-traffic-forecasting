# 방향별 시각 이동의 예측 비교와 기간별 가중치

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

기록 ID `0141` · 원기록 `112` · 당시 날짜 2026-09-26 · 아카이브 검수 2026-10-14

[자료와 읽은 범위](../sources/history-141.md) · [주장 검수](../verification/history-141.md) · [원110–111](0140-calendar-alignment-and-input-preflight.md) · [원101](0131-actual-pooled-context-and-rctl-ranking.md)

원112는 정상 완료된 실제 예측 비교에서 사전 진행 기준을 통과하지 못한 기록이다. Tab이 앞 절반에서 고른 시각 이동을 뒤 절반에서 Tab으로 평가하면 무이동보다 MAE가 약0.000549 증가했다. profile 선택보다 나았지만 두 비교군을 모두 이겨야 했으므로 후속 RCTL 확인으로 진행하지 않았다.

원110의 profile 개선, 원111의 입력 지원 검사, 원112의 직접 예측 비교를 구분한다. 현재 세 이동과 고정 context·지원 범위의 결과이며 모든 시각 보정 연구의 실패를 뜻하지 않는다. 이번 정리는 저장 예측의 산술 대조이고 모델을 새로 호출한 실험이 아니다.

## 질문과 실제 수행 범위

질문은 최근 실측 입력과 정답 시점을 유지한 채 달력 좌표를 바꾸면 다른 cell의 context로 예측하는 관계가 개선되는가였다. 원111에서 동결한14방향·11target, 각 방향의 무이동과 두 비영 이동, 공통 mask를 그대로 썼다. 방향별 이동을 확인 구간에 고정했으며 cluster 소속이나 모든cell의 공동좌표φ는 확정하지 않았다.

donor context는 target 시각168–671의504행이다. query는 개발 구간672–839에서 고른64개 위치이며 앞32개로 이동을 선택하고 뒤32개로 확인했다. 확인 시각은756–839 안에서 선택된 위치다. 앞선 설계에 이미 사용된 개발 자료이므로 독립 미래 test나 도시 전체 평가로 해석하지 않는다.

기존 raw 시각0–671의 cell 평균 척도를 유지한다는 계획과, 원101의저장X/Y 첫672행을 재사용한 실제코드를 대조했다. raw 평균이나 입력 특징을 새로 생성하지 않았다. 입력 구성과 척도의 앞선 검수는 [원101](0131-actual-pooled-context-and-rctl-ranking.md)을 재사용한다. 아래 값은 이 cell별 정규화 MAE다.

## 선택자와 평가 예측기를 따로 읽기

행은 이동량 선택법, 열은 그 이동을 평가한 예측기다. 동일한 저장 예측을 조회한15칸이며15번 새 실험을 한 결과가 아니다. 작은 값이 좋다.

| 이동량 선택자 | TabICLv2 MAE | Ridge MAE | HGB MAE |
|---|---:|---:|---:|
| 무이동 | 0.124196578 | 0.100080111 | 0.100334949 |
| 과거 profile | 0.125479058 | 0.099738119 | 0.101291260 |
| TabICL | 0.124745181 | 0.101605372 | 0.100851259 |
| Ridge | 0.124976581 | 0.100432378 | 0.100789795 |
| HGB | 0.122875874 | 0.098535025 | 0.102394748 |

Tab 선택을 Tab으로 평가한 정확한 차이는 무이동 대비`+0.0005486032534057772`, profile 대비`−0.0007338765503965006`이다. 두 값이 모두 음수여야 한다는 기준은 그대로 유지돼 `first_predictive_gate_passes=false`다. HGB 선택이 Tab/Ridge 평가에서 유리했던 경우도 보존하며 이를 Tab 선택 기준의 통과로 바꾸지 않는다.

같은 방향별 확인 mask에서 자기 cell context를 쓴 MAE는 Tab0.08022847123178041/Ridge0.09246672266753775/HGB약0.08430649865212468이다. 이 조건에서의 직접 예측 우위와 다른cell 자료를 사용할 좌표를 고르는 능력은 구분한다. 원101의 실제 혼합 context 결과나 RCTL 성능을 이번 비교로 대체하지 않는다.

## 방향별 손해와 이득

화살표는 **target→사용한 donor context**다. 각 방향의 공통 mask에서 Tab 선택과 무이동을 비교했다. 아래 방향별 오차는 저장 배열에서 다시 집계한 값이다.

| target→donor | 선택/확인 query 수 | Tab 선택 이동(h) | 무이동 MAE | Tab 선택 MAE | 차이 |
|---|---:|---:|---:|---:|---:|
| 3737→3745 | 32/31 | 0 | 0.074044604 | 0.074044604 | +0.000000000 |
| 3745→3737 | 31/26 | 1 | 0.127518151 | 0.135751602 | +0.008233451 |
| 3753→5337 | 31/32 | -1 | 0.160465594 | 0.164643943 | +0.004178349 |
| 3765→5365 | 20/21 | 0 | 0.108136086 | 0.108136086 | +0.000000000 |
| 3765→5353 | 28/30 | 0 | 0.120590736 | 0.120590736 | +0.000000000 |
| 4545→5337 | 32/32 | -1 | 0.117736644 | 0.105379951 | -0.012356693 |
| 4565→6153 | 32/32 | 0 | 0.132987639 | 0.132987639 | +0.000000000 |
| 5345→3737 | 32/32 | -1 | 0.089340009 | 0.095407490 | +0.006067481 |
| 5353→3765 | 31/29 | 0 | 0.136704377 | 0.136704377 | +0.000000000 |
| 5353→6153 | 32/32 | 0 | 0.186739255 | 0.186739255 | +0.000000000 |
| 6145→5337 | 32/29 | 0 | 0.120385430 | 0.120385430 | +0.000000000 |
| 6153→4565 | 30/26 | -2 | 0.106950179 | 0.133383185 | +0.026433006 |
| 6153→4553 | 20/18 | -1 | 0.194593852 | 0.194907190 | +0.000313338 |
| 6165→5365 | 22/32 | 1 | 0.116827041 | 0.103365917 | -0.013461124 |

7개의 비영 변경 방향은 손해5·이득2였다. 나머지7방향은 같았다. 같은target 안에서 donor를 동등평균한 cell 단위에서는 손해4·이득2·동일5다. 가장 큰 방향 손해6153→4565의증가약0.026433과 cell6153의평균증가약0.013373을 함께 남긴다.

| target cell | 무이동 MAE | Tab 선택 MAE | 차이 |
|---|---:|---:|---:|
| 3737 | 0.074044604 | 0.074044604 | +0.000000000 |
| 3745 | 0.127518151 | 0.135751602 | +0.008233451 |
| 3753 | 0.160465594 | 0.164643943 | +0.004178349 |
| 3765 | 0.114363411 | 0.114363411 | +0.000000000 |
| 4545 | 0.117736644 | 0.105379951 | -0.012356693 |
| 4565 | 0.132987639 | 0.132987639 | +0.000000000 |
| 5345 | 0.089340009 | 0.095407490 | +0.006067481 |
| 5353 | 0.161721816 | 0.161721816 | +0.000000000 |
| 6145 | 0.120385430 | 0.120385430 | +0.000000000 |
| 6153 | 0.150772015 | 0.164145187 | +0.013373172 |
| 6165 | 0.116827041 | 0.103365917 | -0.013461124 |

## 기간별 평균을 합쳐 읽으면 생기는 오류

주 지표는 방향 안의query 평균 → target 안의donor 동등평균 → 11target 동등평균이다. 한query의 펼친 가중치는 `1/(해당기간 target 수 × 해당target donor 수 × 해당방향 기간query 수)`다. donor가 다른 방향에서 같은target·시점의 정답을 반복하므로 방향×query 수를 독립 표본 수로 세지 않는다.

| 기간 | 방향×query | 서로 다른 target×query | target / 방향 |
|---|---:|---:|---:|
| 이동 선택 | 405 | 339 | 11/14 |
| 뒤 절반 전체 확인 | 402 | 336 | 11/14 |
| 확인 앞쪽 | 210 | 167 | 11/14 |
| 확인 뒤쪽 | 192 | 169 | 11/14 |

확인 앞쪽과 뒤쪽을 각각 새로 정규화한 Tab 선택−무이동 평균은 둘 다 음수다. 그런데 사전 전체 평균은 양수다. 각 방향의 남은query 비율이 다르기 때문에 두 하위 평균을 단순 평균하거나 하나의 공통 기간비율로 합칠 수 없다. 예를 들어6153의 두donor 방향은 확인 뒤쪽에 각각10개와2개의query만 남아 있다.

| 계산 | 확인 앞쪽 | 확인 뒤쪽 | 합계/전체 |
|---|---:|---:|---:|
| 각 기간을 새로 정규화한 평균 차이 | -0.001539002173 | -0.000451904490 | 단순 합산 대상 아님 |
| 원래 전체 가중치로 나눈 기여 | -0.000469051401 | +0.001017654655 | +0.000548603253 |

원래 전체 가중치의 기여 합계는 주 지표 증가와 부동소수 허용오차 안에서 일치한다. 이 집계 차이를 이유로 사전 지표나 기각 기준을 바꾸지 않았다. 여기서336개의 서로 다른 확인target×query와 원101에서 사용하지 않은 미래336행/cell은 다른 단위다.

## 실행 상태, 비용과 원장 판본

14context 요청은 자기 기준675행과 cross2421행을 합한3096행이었다. Tab14로그와 Ridge/HGB각14로그가 모두 완료됐고, 이름이predictions_partial인 최종저장본의예상finite/NaN범위도 맞았다. 세모델의저장예측9288값은 독립관측 수가 아니다.

| 비용/계측 | 기록값 | 실제 범위 |
|---|---:|---|
| Tab charged timer | 18.724957200초 | 각context fit/predict와그안의기록·검사;객체생성/archive/gc 제외 |
| cheap 잔여 시간 | 3.972640900초 | 단계시간−Tabtimer;순수단순회귀시간이아님 |
| Ridge/HGB 별도 timer | 1.306363500초 | cheap 잔여 안에 포함된fit/predict timer |
| 전체 단계 | 22.697598100초 | imports/settings/초기hash 이후;최종rehash/정산 제외 |
| sampled RSS max | 707,563,520 bytes | 약0.2초sampling과종료관측;연속진짜peak 미확인 |

최초 추가 회차 활성화와 이번 예약·정산을 구별했다. 원112 전`084b70…` → 예약후·정산전`799466…` → 정산후`7f6ca2…`의세판본을 대조했다. 정산후 정확한hash는원113의정산전사본에보존돼있으며 현재root원장으로대체하지 않았다.

과거 누적 사용량을 보존해 Tab92context/58,584행이 됐고 남은값은18context/13,288행이었다. 기존RCTL optimizer29+통계적합9=통합38과관련시간·epochs는유지됐으며 통합remaining9였다. 통계적합시간은이미RCTLwall에포함돼추가합산하지 않는다. 역사적허용량·명령은이아카이브의새실험지시로사용하지 않았다.

## 검수 범위와 남은 작업

저장된 선택·calibration·15칸/4기간의전체cell평균·자기context·기간기여854값의최대차이는4.163336342344337e−17(허용1e−12)이었다. array/boolean exact대조192800값과NPZ34member header를확인했다. 모델예측재생성이나독립인간검토는하지 않았다. 작성후에는813행과선택된JSON/배열을다시읽었으며전체산술을다시실행했다고하지 않는다.

원112source25SHA/26물리alias를연결한다. 생성pyc는같은Python3.12.14의정적compile payload가정확히일치해생성cache로분류했다. sourcecode를실행/import하거나codeobject를호출하지 않았다. checkpoint114,324,594bytes는hash만확인하고모델로로드하지 않았다.

현재보고서의55행을읽었지만원113–115의과학적판단은아직그주요근거와대조하지않았다. 원101입력의미래336행/cell도이번의미검토범위에없다. 다른자료·이동후보·support/context·공동좌표명세로재검토하려면바뀐질문과독립평가를분명히하고같은K의RCTL확인은별도로설계해야한다. 전체과거기록Goal은진행중이다.

## 주장별 출처와 적용 범위

<a id="h141-c01"></a>

### H141-C01 · 앞선 두 검사를 예측 실행과 구별한다

원110의 하루 평균 profile 이동과 원111의 입력 지원 검사를 거쳐 원112에서 실제 TabICLv2·Ridge·HGB 예측을 수행했다. 원112는 정상 완료된 예측 비교이며, 원110의 profile MAE 약9.2% 감소나 원111의 geometry 통과를 예측 개선으로 재인용하지 않는다. 이 아카이브에서는 과거 실행을 다시 수행하지 않았다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[3, 11] · [SRC-0020869](../sources/history-141.md#src-0020869) 행[3, 9] · [SRC-0024535](../sources/history-141.md#src-0024535) JSON /success · [SRC-0024534](../sources/history-141.md#src-0024534) JSON /complete · [SRC-0000135](../sources/history-141.md#src-0000135) 행[5, 7]

<a id="h141-c02"></a>

### H141-C02 · 개발 자료 안에서의 선택·확인

각 donor의 실제 target 시각168–671에 대응하는504행 context와, 개발 구간672–839에서 원111이 고른64개 query 위치를 사용했다. 앞32개 위치의 공통 mask로 이동을 고르고 뒤32개 위치에 그 선택을 고정했다. 설계에 이미 사용한 개발 자료이므로 뒤 절반을 독립 미래 test라고 부르지 않는다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[9, 15] · [SRC-0020869](../sources/history-141.md#src-0020869) 행[7, 9] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[89, 107] · [SRC-0024554](../sources/history-141.md#src-0024554) NPZ query_positions, query_target_times, context_X, query_X

<a id="h141-c03"></a>

### H141-C03 · 기존 정규화 척도와 과거 label slice

계획은 raw 시각0–671의 cell 평균으로 정한 기존 척도를 유지하고 query 이후 target으로 다시 척도를 맞추지 않는다고 명시한다. 실행 코드는 원101 Y의첫672행에서 context504행과 선택된query64행을 읽었다. 저장X/Y·identity와 이 slice의 일치를 대조했으며 raw traffic 평균을 새로 계산하지 않았다. MAE는 이 기존 cell별 정규화 척도다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[11, 15] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[97, 103] · [SRC-0029561](../sources/history-141.md#src-0029561) NPZ X, Y, cell_ids, scales

<a id="h141-c04"></a>

### H141-C04 · 방향별 세 이동을 동결했다

원111의32방향 중 통과한14방향·11target을 그대로 사용하고 각 방향의 무이동과 사전에 동결한 두 비영 이동을 비교했다. 뒤 구간에 고정한 방향별 이동 선택이며 모든 cell에 공동으로 일관된φ를 확정한 결과가 아니다. 지원 반경이나 후보를 원112 결과에 맞춰 다시 검색하지 않았다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[7, 15] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[90, 107] · [SRC-0024554](../sources/history-141.md#src-0024554) NPZ pair_indices, phase_candidates, common_masks, eligible_pairs · [SRC-0024534](../sources/history-141.md#src-0024534) JSON /new_partition_chosen

<a id="h141-c05"></a>

### H141-C05 · float32 무이동 입력의 동일성

실행 전에 원111의float64 context/query/shifted query를float32로 바꿨다. 이번 저장배열 대조에서 phase0 입력은 원래query의float32 값과 정확히 같아 최대차이0이었다. 원111의float64 hour 재계산에서 관측한 약1.55e−8 차이를 원112 예측 손해의 원인으로 단정하지 않는다.

근거: [SRC-0022561](../sources/history-141.md#src-0022561) 행[90, 103] · [SRC-0024554](../sources/history-141.md#src-0024554) NPZ shifted_query_X, query_X, pair_indices

<a id="h141-c06"></a>

### H141-C06 · Tab 설정과 환경 기록

Tab은 로컬checkpoint SHA0db9cb538f114e79026bf08f45f41ad8dd7ad2de2aaca9a5ca8cd3bd9748ae7a를 사용했다. n_estimators1/batch_size1/kv_cacheFalse, CPU/seed20260925, AMP·FA3·offload·auto-download 비활성이다. 저장환경은Python3.12.14/Torch2.14.0+cpu/sklearn1.9.1/TabICL package version unknown, Torch4thread·interop2였다. CPU 기종과 전체hardware 사양은 이 기록에 미기록이다.

근거: [SRC-0022561](../sources/history-141.md#src-0022561) 행[42, 56] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[151, 155] · [SRC-0024537](../sources/history-141.md#src-0024537) JSON /versions, /torch_threads, /torch_interop_threads · [SRC-0024526](../sources/history-141.md#src-0024526) JSON /source_hashes/assets\tabicl-regressor-v2-20260212.ckpt

<a id="h141-c07"></a>

### H141-C07 · Ridge와 HGB의 고정 설정

Ridge는 donor context에 적합한 StandardScaler와alpha1 회귀다. HGB는absolute_error/max_iter100/learning_rate0.1/max_leaf_nodes15/min_samples_leaf20/l2_regularization1/early_stoppingFalse/random_state20260925였다. 동일donor context와 query·정답을 사용하며 모델 설정을 결과에 맞춰 바꾼 비교가 아니다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[19, 23] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[156, 169]

<a id="h141-c08"></a>

### H141-C08 · 요청을 묶은14context·3096행

필요한target와donor의 합집합은14context다. 요청은 자기 기준11section과14방향×3이동의42cross section, 총53section으로 구성했다. own query 합집합675행과cross807방향×query×3이동=2421행이 합쳐져3096행이다. 한target의 동일query를 donor마다 반복한 값과 자기 기준 합집합을 구별한다.

근거: [SRC-0022561](../sources/history-141.md#src-0022561) 행[105, 140] · [SRC-0024533](../sources/history-141.md#src-0024533) JSON /total_rows, /requests · [SRC-0024554](../sources/history-141.md#src-0024554) NPZ own_baseline_masks, common_masks, eligible_pairs, pair_indices

<a id="h141-c09"></a>

### H141-C09 · 부분이라는 파일명과 정상 완료

predictions_partial.npz라는 이름은 실행 중 덮어쓰는 저장본에도 최종 완료후에도 사용됐다. 최종13member에서 통과방향의cross2421행과own675행이 각 모델에서finite이고 미사용영역은 예상대로NaN이었다. 세 모델 전체의 저장예측9288값은 서로 다른독립표본9288개가 아니다. 성공marker와 완료된Tab14/simple28로그를 함께 확인했으며 파일명만으로 부분실패로 분류하지 않았다.

근거: [SRC-0022561](../sources/history-141.md#src-0022561) 행[137, 140] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[203, 214] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[268, 297] · [SRC-0024535](../sources/history-141.md#src-0024535) JSON /success, /contexts_completed, /simple_fits_completed · [SRC-0024532](../sources/history-141.md#src-0024532) NPZ cross_TabICL, cross_Ridge, cross_HGB, own_TabICL, own_Ridge, own_HGB

<a id="h141-c10"></a>

### H141-C10 · 실제 관측 단위와 label 중복

선택구간은405방향×query와339서로다른target×query, 확인구간은402와336이었다. 확인구간의앞/뒤하위구간은210/192방향×query 및167/169target×query다. donor가다른방향에서 같은target label을 재사용하므로402를402개의독립관측으로 해석하지 않는다. 여기의336은 원101에서 사용하지 않은 미래336행/cell과 다른단위다.

근거: [SRC-0020869](../sources/history-141.md#src-0020869) 행[7, 9] · [SRC-0024539](../sources/history-141.md#src-0024539) JSON /period_coverage · [SRC-0024532](../sources/history-141.md#src-0024532) NPZ common_masks, eligible_pairs, pair_indices

<a id="h141-c11"></a>

### H141-C11 · MAE의 세 단계 평균

주 지표는 각 방향의 남은query 평균, 각target 안의donor 동등평균, 마지막11target 동등평균이다. 한query의 펼친가중치는1/(해당기간target수×해당target의donor수×해당방향의기간query수)다. query가많은방향을 더크게 세거나14방향을 그대로동등평균하는 지표와 다르다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[29, 31] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[233, 250] · [SRC-0023259](../sources/history-141.md#src-0023259) 행[49, 71]

<a id="h141-c12"></a>

### H141-C12 · 선택자5개와 예측기3개의 역할

none/profile/Tab/Ridge/HGB의5행은 이동량 선택법이고 Tab/Ridge/HGB의3열은 그이동을 평가한예측기다. 교차표는 이미저장한예측을 조회한 결과이며15칸마다 모델을다시호출한 실험이아니다. 같은평가예측기 안에서 선택효과를 비교해야 한다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[25, 31] · [SRC-0020869](../sources/history-141.md#src-0020869) 행[11, 23] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[233, 254] · [SRC-0024534](../sources/history-141.md#src-0024534) JSON /tables/heldout/MAE

<a id="h141-c13"></a>

### H141-C13 · 앞 절반에서 이동량을 정했다

각 방향의앞 절반에서 세 이동의정규화MAE를 계산하고 모델별최솟값의index를 선택했다. 코드의np.argmin은 정확동점에서 첫candidate를 택하며 phase0이먼저다. profile은 원111의고정선택을조회한다. 코드의모델별index계산은앞 절반정답만사용한다. 이전원110에서같은개발구간의검사결과로후보진행을판단한점은남으므로전체설계의독립성을증명하지않으며,label-free 또는zero-shot clustering도아니다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[13, 15] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[216, 231] · [SRC-0023259](../sources/history-141.md#src-0023259) 행[37, 48] · [SRC-0024534](../sources/history-141.md#src-0024534) JSON /pair_results

<a id="h141-c14"></a>

### H141-C14 · 사전에 정한 두 비교군을 모두 이겨야 했다

사전 진행 기준은 Tab이선택한이동을Tab으로평가한뒤 절반MAE가무이동과profile선택보다모두작아야한다는것이다. 실제값은Tab 선택0.12474518095779191/무이동0.12419657770438614/profile0.1254790575081884였다. 무이동대비+.0005486032534057772,profile대비−.0007338765503965006이어서first_predictive_gate_passes=false다. 허용폭을사후추가하거나주 지표를바꾸지 않았다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[33, 38] · [SRC-0020869](../sources/history-141.md#src-0020869) 행[23, 23] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[263, 274] · [SRC-0024534](../sources/history-141.md#src-0024534) JSON /tables/heldout/MAE, /primary_differences, /first_predictive_gate_passes

<a id="h141-c15"></a>

### H141-C15 · 다른 선택자의 이득도 남긴다

HGB 선택은Tab 평가0.12287587405575616과Ridge 평가0.09853502547492693에서각무이동보다낮았다. 반면HGB 평가에서는0.10239474799916044로무이동0.10033494887702275보다높았다. Ridge 선택을Ridge로평가한0.10043237841165119도무이동0.10008011081385716보다높았다. 이교차차이를모든이동이해롭다거나Tab 선택이통과했다는결론으로바꾸지 않는다.

근거: [SRC-0020869](../sources/history-141.md#src-0020869) 행[15, 23] · [SRC-0024534](../sources/history-141.md#src-0024534) JSON /tables/heldout/MAE

<a id="h141-c16"></a>

### H141-C16 · 비영 이동 수는 성능을 뜻하지 않는다

14방향에서비영 선택 수는none0/profile5/Tab7/Ridge7/HGB7이었다. Tab 선택의7변경방향중확인MAE손해5·이득2,나머지7방향은같았다. 대상cell별donor평균으로다시보면11cell중손해4·이득2·동일5다. 방향수와cell수를섞어성과를보고하지 않는다.

근거: [SRC-0024534](../sources/history-141.md#src-0024534) JSON /selected_nonzero_counts, /pair_results, /tables/heldout/cell_MAE · [SRC-0024532](../sources/history-141.md#src-0024532) NPZ cross_TabICL, actual, common_masks, eligible_pairs, pair_indices

<a id="h141-c17"></a>

### H141-C17 · 최대 손해 방향과 평균 손해 cell

Tab 선택의최대 방향 손해는6153→4565의0.10695017874240875→0.13338318467140198(Δ+.026433005928993225)였다.6153→4553도Δ+.0003133383062150774여서6153cell의동등 donor 평균은Δ+.013373172117604137이다.4545와6165의이득을함께보존하며유리한방향만남겨주 지표를고치지 않는다.

근거: [SRC-0024534](../sources/history-141.md#src-0024534) JSON /pair_results/11, /pair_results/12, /tables/heldout/cell_MAE · [SRC-0024532](../sources/history-141.md#src-0024532) NPZ cross_TabICL, actual, common_masks, pair_indices

<a id="h141-c18"></a>

### H141-C18 · 두 하위 구간 평균은 전체 평균과 다른 가중치다

뒤 절반을32–47/48–63query index로나눠각각새로정규화한Tab 선택−무이동은약−.0015390021726489/−.0004519044901385로둘다감소했다. 그런데사전전체 지표는+.0005486032534057772증가했다. 방향마다앞/뒤의남은query수비율이다르고donor를동등평균하므로하위 기간의단순평균이나단일공통기간비율로전체 지표를재조합할수없다.

근거: [SRC-0020869](../sources/history-141.md#src-0020869) 행[27, 31] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[233, 254] · [SRC-0024534](../sources/history-141.md#src-0024534) JSON /tables/heldout_first, /tables/heldout_last, /primary_differences

<a id="h141-c19"></a>

### H141-C19 · 원래 주 지표의 가중치로 나눈 기여

전체 확인 기간의방향별query분모와11cell·donor가중치를그대로고정한오차변화기여는앞쪽−.00046905140134143383와뒤쪽+.0010176546547472152다. 합계는약+.0005486032534057814로주 지표증가와부동소수허용오차안에서일치한다. 이분해와각하위 기간을새로정규화한평균은서로다른계산이며,집계차이를이유로기각기준을바꾸지 않았다.

근거: [SRC-0023259](../sources/history-141.md#src-0023259) 행[72, 88] · [SRC-0020869](../sources/history-141.md#src-0020869) 행[29, 31] · [SRC-0024539](../sources/history-141.md#src-0024539) JSON /primary_weighted_period_contributions

<a id="h141-c20"></a>

### H141-C20 · 자기 context 능력과 관계 선택을 구별한다

동일 방향별확인mask에서자기 cell context를쓴MAE는Tab0.08022847123178041/Ridge0.09246672266753775/HGB약0.08430649865212468이었다. 이조건의Tab직접예측우위는다른 cell의context를활용할이동선택의우위와다르다. 다른 cell만쓴이번cross비교를실제혼합context의손해나RCTL성능으로확대하지 않으며원101혼합context결과도유지한다.

근거: [SRC-0020869](../sources/history-141.md#src-0020869) 행[25, 25] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[255, 262] · [SRC-0024534](../sources/history-141.md#src-0024534) JSON /own_context_MAE_on_same_pair_masks · [SRC-0024532](../sources/history-141.md#src-0024532) NPZ own_TabICL, own_Ridge, own_HGB, actual, common_masks

<a id="h141-c21"></a>

### H141-C21 · 진행 중단의 적용 범위

현재세 이동·고정 donor context·지원 mask·14방향/11target·개발기간에서사전첫예측기준을충족하지못했다. 이동범위를늘리거나유리한cell을선별하거나RCTL학습으로진행하지않겠다는당시판단이다. 모든시각보정연구·다른자료·다른joint좌표모형의실패나통계적유의성·신규성기각으로일반화하지 않는다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[31, 38] · [SRC-0020869](../sources/history-141.md#src-0020869) 행[33, 41] · [SRC-0024534](../sources/history-141.md#src-0024534) JSON /RCTL_improvement_measured, /new_partition_chosen, /novelty_established, /new_RCTL_calls

<a id="h141-c22"></a>

### H141-C22 · 완료 호출과 내부 counter

Tab 로그14개와 Ridge/HGB 로그각14개가 모두completed였으며 모델별3096행 요청과manifest가 일치한다. Tab의predict_stats wrapper counter 합계는14다. 이를 모든내부Torch forward 또는 독립실험14회의개수로바꾸지 않는다. 이counter는 당시관측된method 호출을 세는계측이다.

근거: [SRC-0022561](../sources/history-141.md#src-0022561) 행[142, 214] · [SRC-0024539](../sources/history-141.md#src-0024539) JSON /inner_Tab_stats_calls · [SRC-0024535](../sources/history-141.md#src-0024535) JSON /contexts_completed, /query_rows_attempted, /simple_fits_completed

<a id="h141-c23"></a>

### H141-C23 · 단계 timer와 Tab timer의 범위

단계22.697598099999595초는imports/settings/hashes와run marker 저장 뒤 시작해요청준비·fit/predict·부분archive·결과계산을포함하고 최종source rehash와정산은제외한다. Tab18.724957200000063초는각context의fit/predict와그안의기록·검사를재지만 Tab객체생성·archive저장·gc는그timer밖이다. 전체 연구의초기 전처리·process startup을포함한완전총비용이라고하지 않는다.

근거: [SRC-0022561](../sources/history-141.md#src-0022561) 행[56, 65] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[145, 211] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[281, 297] · [SRC-0024537](../sources/history-141.md#src-0024537) JSON /timing_scope · [SRC-0024535](../sources/history-141.md#src-0024535) JSON /wall_seconds, /Tab_seconds

<a id="h141-c24"></a>

### H141-C24 · cheap은 잔여 시간이지 순수 단순모델 비용이 아니다

cheap_seconds3.972640899999533은단계시간−Tabtimer로계산했다. Ridge/HGB fit/predict timer1.306363500028965초뿐아니라준비·결과계산·archive/gc·Tab객체생성등Tabtimer밖의작업도포함한다. Tab 로그의fit+predict합계18.72482509998372와chargedTabtimer, simple로그합계1.3061330000200542와simpletimer는범위가달라모두동일한숫자로고치지 않는다.

근거: [SRC-0022561](../sources/history-141.md#src-0022561) 행[165, 211] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[282, 291] · [SRC-0024535](../sources/history-141.md#src-0024535) JSON /cheap_seconds, /simple_fit_predict_seconds

<a id="h141-c25"></a>

### H141-C25 · 사전 상한과 RSS sampling

이번단계의한도는Tab14context/3096행/180초,cheap30초,전체210초,simple28fit,RSS4GiB였다. guard는약0.2초마다시간과RSS를관측하고상한도달시hard stop 기록후exit하도록구현됐다. 기록된RSS최대707563520byte는이sampling과종료관측의최댓값이며연속시간의진짜peak를보증하지 않는다. 실제결과는success marker와합치한다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[40, 46] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[42, 85] · [SRC-0022561](../sources/history-141.md#src-0022561) 행[282, 291] · [SRC-0024535](../sources/history-141.md#src-0024535) JSON /success, /rss_peak_bytes

<a id="h141-c26"></a>

### H141-C26 · 허용량의 최초 활성화와 예약

활성화전084b70… 원장에used78context/55488행/389.07952230001183초를보존했다. 기존추가한회차의Tab허용량32context/16384행/600초를처음활성화해누적cap110/71872/989.0795223000118초로맞췄다. 과거 미사용2context·4512행을별도로더하지않았고counts를초기화하지않았다. 이번예약14context/3096행을제외한remaining18/13288은실행전예약시점부터기록돼있다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[40, 46] · [SRC-0022118](../sources/history-141.md#src-0022118) 행[17, 50] · [SRC-0024530](../sources/history-141.md#src-0024530) JSON /used, /additional_rounds · [SRC-0024531](../sources/history-141.md#src-0024531) JSON /used, /caps, /remaining_count_budgets, /additional_rounds · [SRC-0024526](../sources/history-141.md#src-0024526) JSON /remaining_counts_exclude_reservations

<a id="h141-c27"></a>

### H141-C27 · 예약 상태와 실제 정산 상태

예약 후·정산전799466… 원장과정산 후7f6ca2… 원장을전값대조했다.14context/3096행/Tab18.7249572초와cheap3.9726409초,완료상태를한번더하고reservation을settled로바꾼필드·추가로그가정확히일치하며나머지JSON값은유지됐다. attemptedcounts를정산하는정책이며실제이번호출은완료됐다. 재시작·reset으로미사용예산을다시만든기록이아니다.

근거: [SRC-0022118](../sources/history-141.md#src-0022118) 행[51, 99] · [SRC-0024527](../sources/history-141.md#src-0024527) JSON /Tab_contexts_added, /Tab_query_rows_added, /Tab_seconds_added, /cheap_seconds_added, /budget_resets · [SRC-0024531](../sources/history-141.md#src-0024531) JSON /additional_rounds · [SRC-0025008](../sources/history-141.md#src-0025008) JSON /additional_rounds, /used, /cheap_stage_details

<a id="h141-c28"></a>

### H141-C28 · RCTL과 누적 사용량

정산 후Tab누적92context/58584행과remaining18context/13288행이었다. RCTL optimizer fit29·통계적합9=통합38의기존값과관련시간/epochs는이번전후변하지않았으며통합remaining9를유지했다. stage112의RCTL fit/forward/gradient/통계적합은0으로기록됐다. 이미RCTL wall에포함된통계적합시간을전체비용에한번더더하지 않는다.

근거: [SRC-0020869](../sources/history-141.md#src-0020869) 행[37, 41] · [SRC-0022118](../sources/history-141.md#src-0022118) 행[89, 92] · [SRC-0025008](../sources/history-141.md#src-0025008) JSON /used, /remaining_count_budgets, /RCTL_count_accounting_note · [SRC-0024534](../sources/history-141.md#src-0024534) JSON /new_RCTL_calls

<a id="h141-c29"></a>

### H141-C29 · 당시 원장 판본을 정확히 찾았다

원112의정산 후hash7f6ca273e07e8617fb73dd3c885dc9b484233349fb0d9b3748bf932582a87d8e는원113의ledger_before_accounting.json에바이트그대로남아있다. 원112전084b70…·예약 후799466…·정산 후7f6ca2…의세판본을구별한다. 이후비용이추가된현재root원장을원112당시판본으로대체하거나그root를수정하지 않았다.

근거: [SRC-0020869](../sources/history-141.md#src-0020869) 행[43, 43] · [SRC-0024526](../sources/history-141.md#src-0024526) JSON /ledger_before_sha256, /ledger_after_sha256 · [SRC-0024527](../sources/history-141.md#src-0024527) JSON /ledger_after_sha256 · [SRC-0024539](../sources/history-141.md#src-0024539) JSON /ledger_sha256 · [SRC-0025008](../sources/history-141.md#src-0025008) JSON /used

<a id="h141-c30"></a>

### H141-C30 · 저장 예측의 산술 검수 범위

이번에는model/source code 실행없이저장예측과정답에서calibration·선택·전체15칸과4기간별cell평균·자기context·기간기여를재집계했다. 성능관련854값의최대차이는4.163336342344337e−17(허용1e−12),array/boolean exact대조192800값이었다. 원문verifier의2.7755575615628914e−17보고와이번fsum 기반검수를구별하며독립 인간 검토·새예측생성·독립test재현으로세지 않는다.

근거: [SRC-0020869](../sources/history-141.md#src-0020869) 행[27, 31] · [SRC-0023259](../sources/history-141.md#src-0023259) 행[1, 98] · [SRC-0024539](../sources/history-141.md#src-0024539) JSON /independent_flat_weight_MAE_max_difference, /no_models_rerun · [SRC-0024532](../sources/history-141.md#src-0024532) NPZ actual, cross_TabICL, cross_Ridge, cross_HGB, own_TabICL, own_Ridge, own_HGB

<a id="h141-c31"></a>

### H141-C31 · 생성 cache의 판본을 확인한 뒤 제외했다

calendar_predictive_comparison_112.cpython-312.pyc는처음부터제외하지않았다. WSLPython3.12.3의정적compile비교에서bytecode/line/exception정보가달랐으나당시settings와같은WindowsPython3.12.14에서는12codeobject·429field/constant와marshalpayload,mtime/size가정확히일치했다. compile한codeobject를호출하거나원 module을import하지않았다. 이근거로같은원문의생성 cache로분류하며.py와바이트동일한중복이라고하지 않는다.

근거: [SRC-0022561](../sources/history-141.md#src-0022561) 행[1, 300] · [SRC-0024537](../sources/history-141.md#src-0024537) JSON /versions/python

<a id="h141-c32"></a>

### H141-C32 · 후속 보고서의 다른 연구는 별도 미검수다

현재output보고서SRC-0000135는원112의실패판단과원113–115의크기제약·입력반응·taskgrouping문헌을함께서술한다. 원112부분과비용을이번근거로대조하되다른연구절의주요근거검수는뒤묶음으로남긴다. 문서55행을실제로읽었다는사실과보고서전체의과학적검수가끝났다는판정은다르다.

근거: [SRC-0000135](../sources/history-141.md#src-0000135) 행[1, 55] · [SRC-0020869](../sources/history-141.md#src-0020869) 행[23, 43]

<a id="h141-c33"></a>

### H141-C33 · 재사용과 새 연구의 경계

재사용 가능한작은근거는동결입력·선택mask·최종저장예측·설정·요청manifest·로그·세원장판본과저장산술이다.114324594byte checkpoint는SHA를확인했지만이정리에load하거나대용량원문으로게시하지않는다. 같은14방향·세 이동·같은기간의비교는저장자료로먼저찾고,새연구는바뀐자료·context·이동후보·지원조건·공동좌표명세와독립평가계획을분명히해야한다. 좌표/소속선택과같은K의RCTL효용·도시확장비용은별도로남으며이문서는새 모델실행허가가아니다.

근거: [SRC-0020868](../sources/history-141.md#src-0020868) 행[7, 15] · [SRC-0020868](../sources/history-141.md#src-0020868) 행[33, 48] · [SRC-0020869](../sources/history-141.md#src-0020869) 행[35, 43] · [SRC-0024532](../sources/history-141.md#src-0024532) NPZ actual, cell_ids, query_times, pair_indices, phase_candidates, common_masks, eligible_pairs
