# 고정 K와 균등 크기 제약: 소속·수정 규칙의 교차 비교

기록 ID `0142` · 원기록 `113` · 당시 날짜 2026-09-26 · 아카이브 검수 2026-10-14

[출처와 실제 범위](../sources/history-142.md) · [검수](../verification/history-142.md) · [원112](0141-calendar-predictive-selection-and-weighting.md) · [원04–07](0004-0007-b2-observed-risk.md) · [원11–12](0010-0012-population-upc-stability.md)

원113은 기존 위험표와 예측을 재사용한 **완료된 배열 진단**이다. 균등 크기 조건을 없애고 순차 병합하면 네 평균 오차는 줄었지만, 같은 수정 규칙에서 소속을 비교해야 했다. Tab 수정 규칙에서는 empirical 소속이 더 낫고, empirical 수정 규칙에서는 Tab 소속이 더 낫다. 당시에는 이를 Tab의 단독 이득이나 UPC 대비 신규성·RCTL 실패 해결로 채택하지 않았다.

질문은 “K4를 유지하는 것”과 “각 group을4cell로 맞추는 것”의 차이다. 원 UPC의 N은 cluster 수이며 균등 cell 수 조건은 아니다. 이번 위험 기반 병합은 원 UPC의 peak/PCC 절차를 재현한 실험이 아니다. 새 RCTL·Tab·Ridge·KMeans fit/predict는 하지 않았으며 현재 아카이브도 모델 실험을 재실행하지 않았다.

## 고정 자료·시간·척도

같은16cell, K4, 64상태, 257수정 후보와 기존129분위수 위험표를 사용했다. 원 자료는 기존 처리된 H5에서 온 hourly activity다. cell별 raw0–671 평균으로 정규화한 X/Y를 상속했으며 아래 MAE는 그 척도다.

| 역할 | 시간 index, 양끝 포함 | 행/cell | 실제 범위 |
|---|---|---:|---|
| f0·상태·Tab 위험표 context | 168–671 | 504 | 원04 자료·모형 재사용 |
| 위험표 clustering query | 672–839 | 168 | empirical 규칙은 이 정답을 이용 |
| 원113 평가 | 840–1007 | 168 | 이미 사용한 개발 기간 |
| 원04 final sealed | 1008–1487 | 480 | 원113 성능으로 평가하지 않음 |

입력16열은 최근8lag·lag24/168·24시간 mean/std·hour/weekday sin/cos다. 기준 예측 f0는 global StandardScaler+Ridge(alpha1), 상태는 context X의 StandardScaler+KMeans(K64,n_init5,seed20260925)다. 이번에는 저장 base_followweek·followweek_bins를 읽었다.

## 소속과 최종 수정 규칙을 분리한4×2표

각 행의 소속에서 각 열의 규칙으로 **수정값을 다시 구한다**. 같은 추정 규칙을 적용한 비교이며, 서로 다른 소속에 동일 숫자 δ를 고정한 비교는 아니다. 예측은 모두 `f0(x)+group의 상태별 상수`다. 최종 RCTL·새 pooled TabICL의 결과가 아니다. 작은 MAE가 좋다.

| 소속을 정한 위험표 / 제약 | group 크기 | Tab 수정 MAE | empirical 수정 MAE |
|---|---|---:|---:|
| Tab / 균등 | 4·4·4·4 | 0.085256860 | 0.085160920 |
| Tab / 크기 제한 없음 | 2·8·2·4 | 0.084497926 | 0.084530505 |
| empirical / 균등 | 4·4·4·4 | 0.084428734 | 0.086252123 |
| empirical / 크기 제한 없음 | 4·5·3·4 | 0.083984986 | 0.085141326 |

같은 Tab 수정 열에서 unrestricted의 Tab−empirical 차이는`+0.00051294022769195`이고, empirical 수정 열에서는`−0.00061082044496190`다. 수정 규칙이 다른 두 대각 숫자로 소속의 우위를 판정하지 않는다. 수정 전 f0 MAE`0.08902209252119064`보다8개 평균은 모두 작았지만, 이는 이 제한 함수군과 개발 주간의 긍정 결과다.

## 평균 개선과 cell별 손해

아래 차이는 같은 소속 결정 rule에서 unrestricted−balanced다. benefit/harm/same는 같은16cell의 차이 부호를 센 값이다.

| 소속 위험표 | 수정 규칙 | 평균 MAE 차이 | benefit / harm / same |
|---|---|---:|---|
| tabicl_risk | tabicl_risk | -0.00075893344889549 | 6 / 5 / 5 |
| tabicl_risk | empirical_risk | -0.00063041458987754 | 7 / 5 / 4 |
| empirical_risk | tabicl_risk | -0.00044374745423502 | 6 / 6 / 4 |
| empirical_risk | empirical_risk | -0.00111079687177086 | 7 / 5 / 4 |

Tab×Tab에서6145는`+0.003249926749577761` 손해,5365는`−0.012091136490328794` 이득이었다. empirical×empirical에서3753은`+0.008617134954072861` 손해,6145는`−0.010445066318219079` 이득이었다. 평균 감소를 모든 cell의 개선이나 통계적 유의성·도시 전체 보장으로 바꾸지 않는다.

## 변경한 병합 방식과 정답 접근

기존 두 위험표 소속은16→8→4 round에서 비용이 낮은 순서로 disjoint pair를 골랐다. 원113은 기존 balanced label을 재사용했고, 대안만 현재 최소 비용 pair 하나씩 합쳐 다시 비용을 계산했다. 크기 제약과 병합 일정이 함께 바뀌었으므로 크기 숫자만의 인과효과를 분리한 비교로 쓰지 않는다. 같은12회 병합이라도 pair 점수는 rule당148에서670으로 늘었다.

group 비용은 cell의 상태별 위험 곡선을 합한 뒤 후보별 최소값을 합한다. Tab 목적 합은1.533121846266442→1.5291419639317874, empirical은1.2384055069737308→1.2331233875906207이다. 다른 추정분포의 비용을 서로 직접 비교해 최종 예측 우열을 선언하지 않는다.

공통 action 격자는 원04의 Tab·empirical·KNN·median·median/IQR residual 범위에서 왔다. empirical residual은672–839의 실제 query 정답을 참조한다. **구현의 정답 접근과 이번 수치의 영향은 다르다.** 저장 격자16448값은 재계산과 정확히 같았고, 관측된58상태에서 empirical이 엄격히 최소·최대 범위를 결정한 상태는0개였다.6개 비관측 상태는0이다. 정답이 이번 격자를 바꿨다고 주장하거나, 다른 자료의 label-free 보장·정답 제거 후 새 소속 성능 실험으로 확대하지 않는다.

## 실제 비용과 가정한 RCTL 비용

| 소속 | 가정한 group 훈련 행 | group batch/epoch | 합 |
|---|---|---|---:|
| Tab / 균등 | 2688·2688·2688·2688 | 11·11·11·11 | 44 |
| Tab / 크기 제한 없음 | 1344·5376·1344·2688 | 6·21·6·11 | 44 |
| empirical / 균등 | 2688·2688·2688·2688 | 11·11·11·11 | 44 |
| empirical / 크기 제한 없음 | 2688·3360·2016·2688 | 11·14·8·11 | 44 |

이 표는672행/cell과 batch256의 `ceil(group_rows/256)` 가정이다. 위험표 context504와 다르며 RCTL train set을 새로 생성한 값이 아니다. 합10752행과44batch가 같아도 실제 종료 epoch·메모리·학습 시간·RCTL MAE는 미측정이다.

| 비용 항목 | 기록값 / 조건 | 해석 |
|---|---|---|
| 배열 timer | 0.10643169999821112초 | imports/hash/settings/start 뒤부터 predictions.npz 저장까지 |
| 이후 작업 | timer 밖 | RSS·최종 rehash·result/원장·finish 기록 |
| 단일 RSS | 38,719,488 bytes | 종료 부근 한 관측; peak·sample max 아님 |
| guard | 10초 / RSS1GiB | 코드의 한도·종료 시 검사 |
| thread 환경 | OMP/MKL/OpenBLAS4 | 실제 전체 thread 수·CPU 기종·원113 버전은 별도 미기록 |

입력 원장`7f6ca2…`와 후 원장`e1d20d…`의 정확한 판본을 대조했다. 후 판본은 원117의 두 backup에 남았으며 현재 root 원장으로 대체하지 않았다. 차이는 배열 비용 한 항목과 stage details 한 append뿐이다. 당시 Tab92context/58584행, optimizer29+statistics9=통합38, 잔여Tab18/13288·통합RCTL9·reset0은 그대로다. 이미 RCTL wall에 든 adaptation 시간은 다시 더하지 않는다.

## 검수·재사용·남은 범위

22SHA/36원본 경로와38주장을 연결했다. MAE136값·예측 산식21504값·격자16448값·16scale·정규화 Y5376값을 대조했다. MAE/예측/격자/scale 차이는0이고 Y는float32 cast 뒤 정확히 같았다. 목적4값 차이0, 기록된24merge cost max5.551115123125783e−17이다. 모든 현재 pair의 minimum을 재선택하거나 모델을 다시 호출하지 않았다.

첫 literal14자료749행·큰 JSON3개 값 전체, 작성 후 literal14자료709행·result 전체값/선택 pointer/NPZ31headers와 실제 primary PDF4–5쪽을 구분한다. 전체 산술의 작성 후 재실행이나 독립 인간 검증을 주장하지 않는다. dates.npy object는 header만 읽었다.

보존 original11사본과 기존9사본을 이용할 수 있다. 원 논문의 파생 text/metadata2개는 위치·hash·선택 범위와 DOI로 연결하고 전문을 재게시하지 않았다. 같은8비교를 새 모델 실험으로 반복하기 전에 소속·예측·risk·규칙을 확인한다. 바뀌는 데이터·독립 평가·병합 일정/제약·수정 규칙·실제 RCTL 효용을 새 질문에 명시한다.

원135의 원113 절만 이번에 과학 근거를 대조했다. 원114–115, 긴 root·과거 판본·다른 문서 형식·전체 통합/장기 팀 접근/최종 원본 변경분·대표 질문 검색 검수는 남았다. 전체 Goal은 미완료다.

## 주장별 출처와 적용 범위

<a id="h142-c01"></a>
### H142-C01 · 원113의 상태와 질문

2026-09-26의 원113은 원112의 시각 보정 기준 실패 뒤, 기존 pilot의 같은 cluster 크기 제약을 진단한 완료된 저장 배열 분석이다. 원112의 후속 RCTL이나 더 유연한 시각 보정을 실행하지 않았고, 원113의 새 모델 호출·fit도 0이다. 현재 아카이브에서도 원 연구 코드를 실행하거나 모델을 만들지 않았다.

근거: [SRC-0020870](../sources/history-142.md#src-0020870) 행[1, 11] · [SRC-0020871](../sources/history-142.md#src-0020871) 행[1, 9] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /complete, /new_model_calls, /RCTL_performance_measured · [SRC-0025011](../sources/history-142.md#src-0025011) JSON /complete

<a id="h142-c02"></a>
### H142-C02 · UPC의 N은 균등 크기 조건이 아니다

원 UPC는 weekday peak mode로 cell을 먼저 시간별 group에 모은 뒤 group의 PCC로 N개 cluster를 구성한다. Algorithm 1과 pp.6263–6264는 N을 정하지만 cluster마다 같은 cell 수를 요구하지 않는다. θ는 PCC 계산에 쓰는 초기 group의 최소 cell 수 조건이며, 같은 크기 조건을 뜻하지 않는다. 작은 group·None 처리와 공개 코드 차이는 기존 11·12의 미확인 범위로 남긴다.

근거: [SRC-0064599](../sources/history-142.md#src-0064599) 행[348, 397] · [SRC-0064599](../sources/history-142.md#src-0064599) 행[419, 488] · [SRC-0020870](../sources/history-142.md#src-0020870) 행[7, 11]

<a id="h142-c03"></a>
### H142-C03 · 두 기존 위험표 분할의 제약

이번에 가져온 Tab·empirical 두 위험표 소속은 원04의 16→8→4 round에서 비용이 낮은 순서로 disjoint pair를 고른 결과로, 각 group이 4 cell이다. 원04의 모든 과거 소속이 균등했다는 주장으로 넓히지 않는다. copied cross-error-profile 등은 같은 두 위험표 분할과 구분한다.

근거: [SRC-0020825](../sources/history-142.md#src-0020825) 행[11, 18] · [SRC-0022942](../sources/history-142.md#src-0022942) 행[45, 59] · [SRC-0022942](../sources/history-142.md#src-0022942) 행[72, 83] · [SRC-0023588](../sources/history-142.md#src-0023588) JSON /partitions/tabicl_risk, /partitions/empirical_risk

<a id="h142-c04"></a>
### H142-C04 · balanced 소속은 재선정하지 않았다

원113은 기존 소속 label을 읽어 group으로 변환하고 위험 비용과 기존 수치를 대조했다. balanced 병합 알고리즘이나 f0·KMeans·TabICL을 새로 적합한 실행이 아니다. 두 저장 소속과 변경한 순차 소속을 같은 위험표·기준 예측·query에서 평가했다.

근거: [SRC-0020870](../sources/history-142.md#src-0020870) 행[15, 20] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[34, 57] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /settings/new_model_calls · [SRC-0025014](../sources/history-142.md#src-0025014) JSON /balanced_results_reproduce_previous_stage

<a id="h142-c05"></a>
### H142-C05 · 고정한 대상과 자료

기존 16 cell·K4·64 상태·257 수정 후보·Tab 129 midpoint 분위수에서 만든 위험표를 유지했다. cell IDs와 selected index는 저장 NPZ·기존 결과에 연결되며, 이번에 다른 cell이나 기간을 골라 성능을 높이지 않았다. 원113의 정보 단위는 이 고정 16 cell에 한정된다.

근거: [SRC-0020870](../sources/history-142.md#src-0020870) 행[15, 19] · [SRC-0022942](../sources/history-142.md#src-0022942) 행[15, 23] · [SRC-0023588](../sources/history-142.md#src-0023588) JSON /cell_ids · [SRC-0023589](../sources/history-142.md#src-0023589) NPZ cell_ids, selected_cells, actions · [SRC-0025013](../sources/history-142.md#src-0025013) JSON /K, /all_cells, /query_period

<a id="h142-c06"></a>
### H142-C06 · 정규화와 원단위

기존 data_and_smoke.py는 처리된 H5의 data[:1008,ids,2]를 읽고 cell별 raw 0–671 평균으로 나눈 뒤 X/Y를 float32로 저장했다. 이번 저장 raw에서 선택 16 cell의 scale을 재계산한 차이는 0이고, 시간 672–1007의 Y5376 값은 그 나눗셈을 float32로 cast한 값과 정확히 같다. MAE는 이 cell별 정규화 척도이며 Mbps나 원 CDR 부피로 해석하지 않는다. 원 H5 자산을 이번에 다시 열지는 않았다.

근거: [SRC-0022703](../sources/history-142.md#src-0022703) 행[13, 29] · [SRC-0023577](../sources/history-142.md#src-0023577) NPZ raw[:,selected16], scales[selected16], Y[selected16,times672:1007], times, cell_indices[selected16] · [SRC-0022703](../sources/history-142.md#src-0022703) 행[40, 40]

<a id="h142-c07"></a>
### H142-C07 · 시간 분할과 개발 평가

위험표의 context는 168–671의 504 행/cell, clustering query는 672–839의 168 행/cell, 이번 비교는 840–1007의 168 행/cell이다. 평가 주간은 이미 사용한 개발 구간으로 독립 미래 test가 아니다. 원04의 final_sealed1008–1487을 원113 결과로 평가한 것으로 쓰지 않는다.

근거: [SRC-0020825](../sources/history-142.md#src-0020825) 행[11, 11] · [SRC-0022942](../sources/history-142.md#src-0022942) 행[15, 19] · [SRC-0023588](../sources/history-142.md#src-0023588) JSON /input_boundary · [SRC-0020870](../sources/history-142.md#src-0020870) 행[19, 20] · [SRC-0025013](../sources/history-142.md#src-0025013) JSON /query_period, /independent_test · [SRC-0023577](../sources/history-142.md#src-0023577) NPZ times

<a id="h142-c08"></a>
### H142-C08 · 입력16열

입력은 최근 8 lag·lag24·lag168·최근 24시간 mean/std·hour와weekday sin/cos의 16열을 상속한다. cell ID를 f0의 feature로 새로 넣지 않았고, 새 입력 설계나 시간 이동은 수행하지 않았다. 이번 수치 검수는 저장 labels·예측·위험표를 확인했으며 모든 X feature를 원 H5에서 다시 생성하지 않았다.

근거: [SRC-0022703](../sources/history-142.md#src-0022703) 행[20, 29] · [SRC-0020825](../sources/history-142.md#src-0020825) 행[11, 13] · [SRC-0022942](../sources/history-142.md#src-0022942) 행[15, 19]

<a id="h142-c09"></a>
### H142-C09 · 기준 예측과 상태 모델

기준 f0는 전체 context를 합친 StandardScaler+Ridge(alpha1)이고, 상태는 context X의 StandardScaler+KMeans(K64,n_init5,seed20260925)이다. 원113은 두 모델을 새로 적합하거나 호출하지 않고 base_followweek와 followweek_bins를 읽었다. RCTL의 입력이나 정답을 이 기준 예측으로 대체했다는 뜻이 아니다.

근거: [SRC-0020825](../sources/history-142.md#src-0020825) 행[12, 16] · [SRC-0022942](../sources/history-142.md#src-0022942) 행[15, 19] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[34, 44] · [SRC-0023589](../sources/history-142.md#src-0023589) NPZ base_followweek, followweek_bins

<a id="h142-c10"></a>
### H142-C10 · 상속한 Tab 설정

위험표의 Tab 분포는 원04의 cell별 context 504/query 168과 129 개 midpoint 분위수에서 왔다. 원04 코드는 local checkpoint·CPU·ensemble1·batch_size1·seed20260925·n_jobs1·AMP/FA3/offload/auto_download 비활성 설정을 명시한다. 원113은 이 Tab 모델을 생성하지 않았다. 원04 코드에서 kv_cache 값이 명시되지 않았으므로 후속 112의 값을 소급하지 않는다.

근거: [SRC-0022942](../sources/history-142.md#src-0022942) 행[20, 30] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[34, 41] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /new_model_calls · [SRC-0023585](../sources/history-142.md#src-0023585) JSON /observed_risk_pilot.py

<a id="h142-c11"></a>
### H142-C11 · 위험 비용의 의미

위험표는 cell별 clustering query 168 개에서 상태별 손실을 합하고 168로 나눈 곡선이다. group 비용은 cell 곡선을 더한 뒤 상태별 후보 257 개의 최소값을 합하고, 전체 목적은 group 비용의 합이다. Tab 추정분포와 empirical 관측 target의 손실표를 참 conditional law가 확인된 것으로 부르지 않으며, 이 합을 최종 RCTL MAE나 모든 RCTL 함수의 위험으로 바꾸지 않는다.

근거: [SRC-0020825](../sources/history-142.md#src-0020825) 행[14, 17] · [SRC-0022942](../sources/history-142.md#src-0022942) 행[27, 43] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[50, 57] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[80, 81]

<a id="h142-c12"></a>
### H142-C12 · 순차 unrestricted 병합

대안은 16 singleton에서 현재 모든 pair의 위험 증가를 비교해 하나만 합치고, group을 최소 구성원 index 순서로 정렬한 뒤 다시 비교하여 K4에서 멈춘다. 크기 벌점은 없고 exact tuple min의 비용·최소 index로 동점을 처리한다. −1e−10 guard는 음수 roundoff 허용이며 새 tie/성능 통과 tolerance가 아니다.

근거: [SRC-0020870](../sources/history-142.md#src-0020870) 행[17, 18] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[58, 81]

<a id="h142-c13"></a>
### H142-C13 · 크기와 병합 일정의 변화

균등 round에서 disjoint pair를 함께 고르던 방식이 한 pair씩 합치고 비용을 다시 계산하는 방식으로 바뀌었다. 따라서 이 비교를 크기 숫자만 바꾼 인과 실험으로 축소하지 않는다. 매 rule의 병합 12 회는 같지만 후보 pair 점수는 기존 148=120+28에서 현재 670=Σ(n choose2,n5..16)으로 늘었다. 위험 함수 호출 총수나 새 모델 호출 수를 670으로 세지 않는다.

근거: [SRC-0022942](../sources/history-142.md#src-0022942) 행[45, 59] · [SRC-0023588](../sources/history-142.md#src-0023588) JSON /surrogate_validation/tabicl_risk/pair_scores, /surrogate_validation/empirical_risk/pair_scores · [SRC-0022585](../sources/history-142.md#src-0022585) 행[61, 81] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /pair_scores

<a id="h142-c14"></a>
### H142-C14 · 네 소속의 크기

두 balanced 소속은 4·4·4·4이고 Tab unrestricted는 2·8·2·4, empirical unrestricted는 4·5·3·4다. 각 분할은 16 cell을 빠짐·중복 없이 네 group에 배정하며, group index와 실제 cell ID를 저장했다. 크기 해제 뒤 정해진 소속은 현재 비교의 고정 결과다.

근거: [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results · [SRC-0020871](../sources/history-142.md#src-0020871) 행[13, 18] · [SRC-0025009](../sources/history-142.md#src-0025009) NPZ cell_ids

<a id="h142-c15"></a>
### H142-C15 · 소속과 수정 규칙의 교차 평가

네 소속을 각각 Tab·empirical 수정 규칙으로 평가한 4×2표다. 각 group의 64 상태에서 그 규칙의 합산 곡선 argmin257로 수정값을 구하고, 합산 곡선 전체가 0인 상태에는 0을 쓴다. 비교는 같은 수정값 추정 규칙을 쓰는 것이며, 서로 다른 소속에 동일한 숫자 δ를 그대로 고정한 실험은 아니다.

근거: [SRC-0020870](../sources/history-142.md#src-0020870) 행[18, 19] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[83, 109] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results

<a id="h142-c16"></a>
### H142-C16 · 최종 예측 함수

모든 표의 예측은 저장 f0(x)에 소속 group의 상태별 상수를 더한 제한 함수군이다. group이나 수정값 규칙을 바꾸어도 같은 기준 예측·state bin·정규화·16 cell·168시간을 사용한다. 이 함수군의 결과를 새 pooled TabICL이나 최종 RCTL 성능으로 쓰지 않는다.

근거: [SRC-0020871](../sources/history-142.md#src-0020871) 행[7, 9] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[94, 106] · [SRC-0023588](../sources/history-142.md#src-0023588) JSON /function_class · [SRC-0023589](../sources/history-142.md#src-0023589) NPZ base_followweek, followweek_bins

<a id="h142-c17"></a>
### H142-C17 · 동일 평가 labels와 저장 배열

MAE는 각 cell168 개 absolute error의 평균을 구한 뒤 16 cell을 동일 가중으로 평균한다. 저장 predictions.npz는 actual·cell_ids와 8 개 비교 예측의 10키다. actual의 2688 개 cell-query labels를 8비교에서 재사용하므로 21504비교 예측을 독립 관측이나 새 모델 호출로 세지 않는다.

근거: [SRC-0022585](../sources/history-142.md#src-0022585) 행[83, 110] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results · [SRC-0025009](../sources/history-142.md#src-0025009) NPZ actual, cell_ids, all8comparison_matrices

<a id="h142-c18"></a>
### H142-C18 · 주 결과의 원 숫자

Tab balanced의 Tab/empirical 수정 MAE는 0.0852568598694495/0.08516091991466108이고 unrestricted는 0.08449792642055401/0.08453050532478354다. empirical balanced는 0.08442873364709708/0.0862521226415163이고 unrestricted는 0.08398498619286206/0.08514132576974544다. 보고서의 6자리 반올림과 저장 원 숫자를 함께 보존한다.

근거: [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results · [SRC-0020871](../sources/history-142.md#src-0020871) 행[13, 18]

<a id="h142-c19"></a>
### H142-C19 · 같은 규칙에서의 네 개선

balanced→unrestricted의 MAE 차이는 Tab소속×Tab수정 −0.00075893344889549, Tab소속×empirical수정 −0.00063041458987754, empirical소속×Tab수정 −0.00044374745423502, empirical소속×empirical수정 −0.00111079687177086이다. 네 평균은 모두 줄었지만 cell별 모든 손해가 사라졌다는 뜻은 아니다.

근거: [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results

<a id="h142-c20"></a>
### H142-C20 · 수정 규칙에 따라 뒤집히는 순위

unrestricted 소속끼리 같은 Tab 수정 규칙에서는 empirical 소속이 더 낫다(Tab−empirical MAE=+0.00051294022769195). 같은 empirical 수정 규칙에서는 Tab 소속이 더 낫다(Tab−empirical=−0.00061082044496190). 서로 다른 수정 규칙의 대각 숫자만 비교해 Tab이 더 좋은 소속을 찾았다고 선언하지 않는다.

근거: [SRC-0020871](../sources/history-142.md#src-0020871) 행[20, 22] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results/tabicl_risk_unrestricted/MAE_by_correction_rule, /results/empirical_risk_unrestricted/MAE_by_correction_rule · [SRC-0000135](../sources/history-142.md#src-0000135) 행[25, 29]

<a id="h142-c21"></a>
### H142-C21 · cell별 손해를 보존한다

balanced→unrestricted의 benefit/harm/same cell 수는 Tab×Tab 6/5/5, Tab×empirical 7/5/4, empirical×Tab 6/6/4, empirical×empirical 7/5/4다. 평균 개선을 모든 cell의 개선으로 바꾸지 않고 동일 16 cell의 차이를 남긴다.

근거: [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results · [SRC-0023588](../sources/history-142.md#src-0023588) JSON /cell_ids

<a id="h142-c22"></a>
### H142-C22 · 구체적 반례

Tab소속×Tab수정에서 6145의 손해는+0.003249926749577761이고 5365의 이득은−0.012091136490328794다. empirical소속×empirical수정에서 3753은+0.008617134954072861 손해,6145는−0.010445066318219079 이득을 보인다. 이는 같은 개발 주간의 cell별 차이이며 통계적 유의성이나 다른 도시의 보장이 아니다.

근거: [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results · [SRC-0023588](../sources/history-142.md#src-0023588) JSON /cell_ids

<a id="h142-c23"></a>
### H142-C23 · 단순 기준 예측과 긍정 결과의 한계

같은 개발 주간의 수정 전 f0 MAE0.08902209252119064를 저장 base_followweek/actual에서 재확인했다. 이번 8 개 수정 비교의 평균은 모두 이 기준보다 작다. 제한 함수군에서 수정이 유용했던 결과는 보존하되, 이것을 Tab만의 이득·같은 K의 RCTL 비교·독립 미래 개선으로 승격하지 않는다.

근거: [SRC-0023588](../sources/history-142.md#src-0023588) JSON /global_ridge_followweek_mae · [SRC-0023589](../sources/history-142.md#src-0023589) NPZ base_followweek · [SRC-0025009](../sources/history-142.md#src-0025009) NPZ actual · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results

<a id="h142-c24"></a>
### H142-C24 · 네 위험 목적값

Tab 위험 합은 balanced1.533121846266442→unrestricted1.5291419639317874, empirical 위험 합은 1.2384055069737308→1.2331233875906207이다. 같은 rule 내부의 감소와 평가 MAE를 구분하고, 서로 다른 추정분포의 목적값 크기로 Tab/empirical의 최종 예측 우열을 판정하지 않는다.

근거: [SRC-0025010](../sources/history-142.md#src-0025010) JSON /objectives · [SRC-0022585](../sources/history-142.md#src-0022585) 행[54, 57] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[80, 81] · [SRC-0020825](../sources/history-142.md#src-0020825) 행[14, 17]

<a id="h142-c25"></a>
### H142-C25 · 가정한 RCTL 훈련 행

RCTL을 새로 학습했다면 672 행/cell을 쓴다는 산술 가정에서 네 분할 모두 10752 행이다. 이 672는 위험표 context 504와 다른 가정이며 실제 원113의 RCTL train set이 생성됐다는 증거가 아니다. Tab unrestricted의 group 행은 1344·5376·1344·2688, empirical은 2688·3360·2016·2688이다.

근거: [SRC-0020870](../sources/history-142.md#src-0020870) 행[20, 20] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[89, 93] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results

<a id="h142-c26"></a>
### H142-C26 · 44batch가 시간 같음을 뜻하지 않는다

batch 256에서 group마다 ceil(rows/256)을 합한 가정은 네 소속 모두 44batch/epoch다. balanced는 11·11·11·11, Tab unrestricted는 6·21·6·11, empirical은 11·14·8·11이다. 실제 종료 epoch·학습 시간·메모리·RCTL MAE를 측정하지 않았으므로 동일 K·행·batch 합을 동일 실제 비용으로 바꾸지 않는다.

근거: [SRC-0020871](../sources/history-142.md#src-0020871) 행[26, 26] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[89, 93] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /RCTL_performance_measured, /results

<a id="h142-c27"></a>
### H142-C27 · 실제 배열 처리 시간과 경계

기록된 0.10643169999821112 초는 imports·초기 hash·settings·start marker 뒤에 시작해 기존 JSON/NPZ load·배열 계산·최종 predictions.npz 저장까지 포함한다. 뒤의 RSS 관측·최종 입력 rehash·result 기록·원장 backup/정산·finish marker는 이 timer 밖이다. 전 과정이나 새 모델 처리 시간으로 부르지 않는다.

근거: [SRC-0022585](../sources/history-142.md#src-0022585) 행[20, 44] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[110, 128] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /elapsed_seconds

<a id="h142-c28"></a>
### H142-C28 · 메모리와 실행 환경의 기록 한계

38719488bytes는 elapsed를 잰 뒤의 단일 process RSS 관측값이다. 연속 peak나 주기 sample max가 아니다. 코드의 배열 10 초/RSS1GiB와 OMP·MKL·OpenBLAS4는 guard·환경 설정이며 실제 전체 CPU thread 수를 측정한 값은 아니다. 원113의 Python/NumPy 버전·CPU 기종은 설정/로그에 별도 미기록으로 남긴다.

근거: [SRC-0020870](../sources/history-142.md#src-0020870) 행[26, 26] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[1, 4] · [SRC-0022585](../sources/history-142.md#src-0022585) 행[111, 119] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /sampled_rss_bytes · [SRC-0025013](../sources/history-142.md#src-0025013) JSON /wall_cap_seconds, /rss_cap_bytes

<a id="h142-c29"></a>
### H142-C29 · 판본과 완료 근거

settings의 6 개 입력 hash와 plan/code·기존 risk/pilot/design·입력 원장 판본을 현재 원본에 대조했다. start의 settings hash와 finish의 result hash도 연결된다. 원04의 code/plan/result hash는 보존 pre-RCTL capture와 같다. 이 해시 일치를 독립적인 봉인 시각이나 독립 연구자 검증으로 부르지 않는다.

근거: [SRC-0025013](../sources/history-142.md#src-0025013) JSON /source_hashes · [SRC-0025012](../sources/history-142.md#src-0025012) JSON /settings_sha256 · [SRC-0025011](../sources/history-142.md#src-0025011) JSON /result_sha256 · [SRC-0023585](../sources/history-142.md#src-0023585) JSON /observed_risk_pilot.json, /04_observed_query_risk_plan.md, /observed_risk_pilot.py

<a id="h142-c30"></a>
### H142-C30 · 당시 정산 전후 원장

정산 전 7f6ca2…는 원113 ledger_before_accounting.json, 후e1d20d…는 원117의 두 보존 backup 파일에서 같은 바이트로 확보했다. 현재 root17a…로 당시 원장을 대체하지 않았다. 후 원장의 478 행 JSON 값 전체를 읽고, 전 값에 한 stage를 더한 구조와 Windows CRLF477 개의 실제 후 바이트가 정확히 일치함을 확인했다. 재구성 바이트를 새 원본으로 집계하지 않는다.

근거: [SRC-0025011](../sources/history-142.md#src-0025011) JSON /ledger_after_sha256 · [SRC-0025008](../sources/history-142.md#src-0025008) JSON /new_cheap_diagnostic_seconds, /cheap_stage_details · [SRC-0030185](../sources/history-142.md#src-0030185) JSON /new_cheap_diagnostic_seconds, /cheap_stage_details

<a id="h142-c31"></a>
### H142-C31 · 배열 비용의 단일 정산

원장 차이는 new_cheap_diagnostic_seconds에 cluster_size_constraint_113=0.10643169999821112를 추가하고 cheap_stage_details에 같은 비용의 항목을 한 번 append한 것뿐이다. 모델 사용량·cap·잔여·reservation·RCTL adaptation·기존 cheap 항목은 모두 그대로다.

근거: [SRC-0022585](../sources/history-142.md#src-0022585) 행[120, 126] · [SRC-0030185](../sources/history-142.md#src-0030185) JSON /new_cheap_diagnostic_seconds/cluster_size_constraint_113, /cheap_stage_details

<a id="h142-c32"></a>
### H142-C32 · 유지한 모델 예산의 의미

당시 Tab used92 contexts/58584 query rows와 optimizer 29·statistics adaptation9=합산 38은 변하지 않았다. 잔여는Tab 18/13288, combined RCTL9, reset0이다. combined allowance의 잔여는 optimizer 29와 stats9를 함께 세어 계산하며, 이미 RCTL wall에 든 adaptation 시간을 별도로 다시 더하지 않는다. 원장 속 허용·Goal 상태는 역사적 자료이며 현재 재실행 권한이 아니다.

근거: [SRC-0025008](../sources/history-142.md#src-0025008) JSON /used, /caps, /remaining_count_budgets · [SRC-0030185](../sources/history-142.md#src-0030185) JSON /used, /caps, /remaining_count_budgets, /budget_resets, /RCTL_count_accounting_note

<a id="h142-c33"></a>
### H142-C33 · 당시 판단과 실패의 적용 범위

크기 해제로 소속과 평균은 바뀌었으나 수정 규칙에 따라 소속 순위가 뒤집혔다. 원113은 이를 Tab의 우위·UPC 대비 신규성·기존 RCTL 실패 해결로 채택하지 않았고 새 RCTL 적합으로 진행하지 않았다. 고정 16 cell의 이 진단으로 모든 크기 제약이나 모든 Tab 관계 추정이 실패했다고 주장하지 않는다.

근거: [SRC-0020871](../sources/history-142.md#src-0020871) 행[20, 22] · [SRC-0025010](../sources/history-142.md#src-0025010) JSON /novelty_established, /used_to_reclassify_previous_failure_as_success, /RCTL_performance_measured · [SRC-0000135](../sources/history-142.md#src-0000135) 행[23, 29]

<a id="h142-c34"></a>
### H142-C34 · 이번 저장 수치의 검수 범위

8macro와 128 cell MAE=136 값의 저장 예측 재계산 차이는 0이다. 저장 risk/action으로 예측 산식 21504 값을 대조한 차이도 0, 목적 4 값 차이 0, 기록된 24merge cost 차이는최대 5.551115123125783e−17이다. 모든 현재 후보 pair의 minimum 선택을 새로 실행하지 않았으므로 greedy trajectory 전수 재실행 성공으로 부르지 않는다.

근거: [SRC-0025010](../sources/history-142.md#src-0025010) JSON /results, /objectives, /merge_history · [SRC-0025009](../sources/history-142.md#src-0025009) NPZ all10_numeric_members · [SRC-0023589](../sources/history-142.md#src-0023589) NPZ tabicl_risk, empirical_risk, actions, base_followweek, followweek_bins

<a id="h142-c35"></a>
### H142-C35 · 공통 action 격자의 정답 접근

원04의 action 격자는 Tab·empirical·KNN·median·median/IQR의 residual 범위를 함께 사용한다. empirical residual에는 672–839의 실제 query 정답이 들어가므로 Tab 위험 곡선을 쓴 절차 전체가 일반적으로 query 정답에 접근하지 않는 구현이라고 단정하지 않는다. 원113은 이 공통 격자를 그대로 상속했다.

근거: [SRC-0022942](../sources/history-142.md#src-0022942) 행[27, 43] · [SRC-0023585](../sources/history-142.md#src-0023585) JSON /observed_risk_pilot.py · [SRC-0022585](../sources/history-142.md#src-0022585) 행[35, 41] · [SRC-0023589](../sources/history-142.md#src-0023589) NPZ actions, predicted_quantiles, knn_quantiles, base_query, query_bins

<a id="h142-c36"></a>
### H142-C36 · 격자 설계와 실제 수치 의존성

보존한 5 개 residual source로 action 16448 값을 다시 대조한 차이는 0이다. 64 상태 중query가 있는 58 상태에서 empirical 정답 residual이 다른 source보다 엄격하게 최소·최대 범위를 결정한 상태는 0 개였고, 나머지 6 개 비관측 상태의 격자는 0이다. 이 구현의 정답 참조와 실제 범위 변화는 구분하며, 이 자료에서 정답 때문에 격자가 바뀌었다고 주장하지 않는다. 다른 데이터의 label-free 보장이나 정답을 제거한 새 소속/예측 실험은 확인한 것이 아니다.

근거: [SRC-0022942](../sources/history-142.md#src-0022942) 행[27, 43] · [SRC-0023589](../sources/history-142.md#src-0023589) NPZ actions, predicted_quantiles, knn_quantiles, base_query, query_bins · [SRC-0023577](../sources/history-142.md#src-0023577) NPZ Y[selected16,times672:839], times

<a id="h142-c37"></a>
### H142-C37 · 현재 아카이브의 재분석과 범위

현재 검수는 저장 arrays·raw/scales의 작은 산술과 원본 hash·본문 대조다. 원 연구 code/import·fit/predict·새 partition 선택·대안 격자 성능 실험은 0이다. source ID를 재인용한 것과 새 원본 내용 검토를 구분하고, PDF-derived text/metadata·기존 자료 재사용은 새 content credit로 올리지 않는다.

근거: [SRC-0025009](../sources/history-142.md#src-0025009) NPZ actual, all8comparison_matrices · [SRC-0023577](../sources/history-142.md#src-0023577) NPZ selected_raw/scales/Y · [SRC-0020870](../sources/history-142.md#src-0020870) 행[15, 26]

<a id="h142-c38"></a>
### H142-C38 · 재사용·후속 확인 조건

팀은 이 고정 16 cell·두 risk rule·balanced/unrestricted·두 수정 규칙의 8비교를 저장 소속·예측·risk와 코드 판본으로 먼저 찾아 재사용할 수 있다. 새 질문은 달라지는 데이터·독립 평가·병합 제약/일정·수정 규칙·실제 RCTL 효용과 비용을 명시해야 한다. 원113만으로 새 RCTL이나 novelty를 자동 진행하지 않으며 보고서의 이후 114–115 과학 근거는 별도 미완료다.

근거: [SRC-0020870](../sources/history-142.md#src-0020870) 행[9, 11] · [SRC-0020870](../sources/history-142.md#src-0020870) 행[22, 26] · [SRC-0020871](../sources/history-142.md#src-0020871) 행[22, 30] · [SRC-0000135](../sources/history-142.md#src-0000135) 행[23, 39]
