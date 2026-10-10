# 72–75: 출력 압축의 작은 확인과 입력 공유 재진입 중단

40개 주장을 작성 후 원문·저장 수치에 다시 대조했다. [주장별 근거](../verification/history-070-claims.json)와 [문서 검사](../verification/history-070-document-check.json)를 확인할 수 있다. 같은 에이전트의 별도 대조이며 독립 심사나 원실험 재현은 아니다. [출처·읽은 범위](../sources/history-070.md) · [검수](../verification/history-070.md) · [보존 명세](../evidence/0072-0075-output-compression/manifest.json)

## 판단과 실제 수행 범위

[C01] 이 묶음의 질문은 **TabICLv2가 예측 가능한 출력 방향을 골라, 적은 수의 실제 target을 학습하면서 개별 cell 예측을 복원할 수 있는가**이다. 74의 네 cell에서는 Tab 직접 예측이 두 단순 모델보다 좋았지만, 일곱 출력 압축 조건은 비압축 HGB보다 전체·양쪽 시간 절반의 MSE가 나빴다. 당시 압축 후보를 확대하지 않은 판단과 일부 cell·날짜의 긍정 예외를 함께 보존한다.

[C02] 원72·73은 문헌·정적 코드 검토, 원74는 계획 후 저장된 모델 실행 결과와 정확 산술, 원75는 중복 확인 후 **모델 실행 전에 중단**한 검토다. 번호 네 개를 실험 네 번으로 세지 않는다. 이번 아카이브 작업은 저장 자료의 읽기·비교·작은 재계산만 수행했으며 역사 코드·모델 실행은 없다.

[C03] 72–73의 findings가 “논문을 읽었다”고 보고하는 범위와 이번 본문 검수를 구분한다. Globalization의 계수 기반 clustering, ForeCA의 스펙트럼 목적, response dimension reduction, GNN의 pooling·예측·복원은 당시 검토 경로로 연결한다. **이 묶음은 연결 논문 전체의 수식·표·그림을 재검수한 기록이 아니다.** 해당 과학적 주장과 신규성 판단은 후속 일차자료 검수 대상으로 남긴다.

[C04] 수집 기록에는 Globalization의 6,291,456바이트 잘린 PDF가 파싱에 실패한 뒤 7,874,852바이트·65쪽의 다른 다운로드가 확보됐다고 남아 있다. KBS 출판본은 metadata, TMLR 논문 PDF는 미확보, ForeCA는 9쪽, CRAN manual은 10쪽이라는 당시 상태를 구분한다. 저장 파일·해시와 수집 코드의 정적 대조를 했지만, manifest의 쪽수나 렌더 목록을 이번 논문 독해·시각 검수로 가산하지 않는다.

## 데이터·입력·학습 조건

[C05] 실험 cell은 `3737, 3765, 6137, 6165` 네 개로 고정돼 있다. 저장 HDF `data`의 shape은 `[1488,10000,3]`이고, 활동량 채널 index 2에서 `cell_id−1`을 선택했다. `idx`의 실제 시간 문자열과 저장 배열을 연결했다. 파일의 시간대는 확인되지 않았으며 자료 단위를 bytes·Mbps로 바꾸지 않는다.

[C06] index 0–671, 즉 **2013-11-01 00:00–11-28 23:00**의 cell별 평균으로 활동량을 나눈다. 척도는 차례로 `608.1437886904755, 720.8976502976186, 161.30894791666674, 4768.912587797625`다. 중심 μ는 아래 256개 context target의 평균이다. 새로 추출한 HDF 선택값과 저장 `scales`, `center`, `actual`은 정확히 일치했고 `raw_all` 모멘트 차이는 최대 약 `5.55e−17`이었다.

[C07] teacher context는 index168–671에서 `rint(linspace(168,671,256))`로 고른 시점이다. query는672–1007의336시간이며 앞168시간은 calibration, 뒤168시간은 assessment다. 이후 실제 target HGB의 훈련은168–839의672시점이다. 시점 수·cell당 context 수·전체 query 행 수를 혼동하지 않는다.

| 역할 | index | 실제 저장 시간 | 사용 목적 |
|---|---|---|---|
| 정규화 | 0–671 | 11/01–11/28 | cell 평균 척도 |
| teacher context | 168–671 중256개 | 11/08–11/28 | cell별 teacher fit |
| calibration | 672–839 | 11/29–12/05 | 출력 공간 추정 |
| 실제 target HGB 훈련 | 168–839 | 11/08–12/05 | 비압축·latent 회귀 |
| assessment | 840–1007 | 12/06–12/12 |168시간·4cell 지표 |

[C08] 각 target 시점 t에 공통 입력28열을 쓴다. 네 cell의 t−2·t−1·t−24·t−168 값16열, 직전24시간의 cell별 평균·표준편차8열, hour·day-of-week의 sin/cos4열이다. 모든 값은 실제로 관측된 과거다. assessment가 진행되면서 직전 관측을 이용하는 1시간 예측이며, 168시간을 한 번에 재귀 예측한 결과가 아니다.

[C09] teacher는 cell별256개 context에서 StandardScaler+Ridge(`alpha=1`), HGB(`squared_error`,100iter,15leaf,min_leaf20,l2=1,early_stopping=False), TabICLv2를 비교한다. seed는20260925다. Tab은 고정 checkpoint, ensemble1, batch1, CPU4 threads, **`output_type='mean'`**이며 자동 다운로드·AMP·FA3·offload를 끈 설정이다. 단순 모델의 중앙값 목적이나 이전60의 Tab median과 같은 조건으로 쓰지 않는다.

[C10] 모든 수치는 이미 접근한 개발 자료의 결과다. calibration 정답으로 기저·partition을 정한 뒤 뒤168시간을 평가했지만, 이 구간을 연구 전체에서 처음 보는 독립 test로 바꾸지 않는다. 평가의 앞뒤 절반은84시간씩이며, 일별 구간은24시간씩7개다. 시간상 앞서 학습했다는 사실만으로 조건부 독립이나 누출 부재의 모든 가정을 증명한 것은 아니다.

## 압축이 실제로 바꾼 것

[C11] 출력은 cell 평균으로 정규화하고 μ를 뺀 좌표다. 일곱 기준은 `raw_all`, `raw_calibration`, `Ridge_plugin`, `Ridge_corrected`, `HGB_plugin`, `Tab_plugin`, `Tab_corrected`다. `raw_all`은 훈련672시점, 나머지는 calibration168시점의 실제 target 또는 teacher 예측을 쓴다. HGB corrected는 실제 비교 목록에 없다.

[C12] 중심화한 정답 z와 예측 g에서 plugin은 `mean(ggᵀ)`, corrected는 `mean(gzᵀ+zgᵀ−ggᵀ)`다. 모집단에서 `m=E[z|X]`이고 g가 X에 대해 결정되며 잔차의 조건부 평균이0이면 corrected의 기대값은 `E[mmᵀ]−E[(g−m)(g−m)ᵀ]`다. 이 가정 아래의 대수 항등식을 모든 시간 의존 자료·추정기에서 성립하는 무편향 보정이나 RCTL 성능 보장으로 쓰지 않는다. g가 별도 학습 자료에 의존하면 그 자료까지 조건으로 둔 가정을 따로 확인해야 한다.

[C13] 저장 합성 산술은 shrinkage 계수 `2/5,1/10,1` 세 가지다. 신호4와 비교 신호1에서 계수2/5의 plugin은16/25로 잘못 고르고 corrected는64/25로 바로잡는다. 계수1/10에서는1/25와19/25로 둘 다 잘못 고르며, 계수1에서는 둘 다4다. 정확 유리수 예이며 실제 트래픽의 개선 증거가 아니다.

[C14] 계획74에는 isotropic noise 대조도 제시됐지만 실행 코드·저장 toy에는 그 별도 비교가 없다. 수행한 세 shrinkage 산술과 미수행 계획을 구분한다. 코드와 결과에 없는 실험을 계획 문장만으로 완료 처리하지 않는다.

[C15] 네 cell을 비어 있지 않은 두 그룹으로 나누는 무표지 partition은7개이며 각 그룹에서 rank1 방향을 택한다. 합계 rank2·지지집합이 분리된4×2 기저다. retained score 최대값으로 선택하고 동률이면 미리 정렬한 순서를 따른다. `raw_calibration`만 `{3737,6165}/{3765,6137}`을 택했고 나머지6기준은 `{3737}/{3765,6137,6165}`였다. 소속 일치는 기저의 수치 동일성이나 모든 방법의 예측 동일성을 뜻하지 않는다.

[C16] 비압축 HGB는 실제 정답의 네 출력을 각각 학습한다. 압축 HGB는 실제 정답을 `Uᵀ(z)`로 변환한 두 좌표를 학습하고 `μ+U×latent`로 복원한다. **teacher의 예측을 새 학습 정답으로 사용하는 distillation이 아니다.** simple fit은 teacher Ridge4+HGB4, 비압축 HGB4, 일곱 압축×2의14, 합26회다.

## 저장 결과와 반례

[C17] 동일 context256·입력28열에서 Tab의 직접 예측은 아래와 같다. 저장 배열로 전체·cell별4개·날짜별7개·시간 절반별2개의 MSE를 다시 계산했고, Tab은 두 teacher보다 각 비교에서 낮았다. 전체 MAE도 낮다. 이 직접 예측의 긍정 결과를 압축의 실패 때문에 삭제하지 않는다.

| 직접 teacher | MSE | MAE | 앞84시간 MSE | 뒤84시간 MSE |
|---|---:|---:|---:|---:|
| Ridge |0.0143598472|0.0895649238|0.0126240110|0.0160956835|
| HGB |0.0119248073|0.0784002755|0.0100871215|0.0137624930|
| TabICLv2 mean |0.0095798159|0.0668277261|0.0082153009|0.0109443308|

[C18] 네 cell·한 seed·고정 checkpoint·ensemble1·한 개발 주간에서 관찰한 우열이다. 여러 cell의 입력을 쓴 Tab과 **같은 조건의 자기 cell 입력만 쓴 Tab**을 비교하지 않았다. 따라서 공간 입력이 Tab의 개선 원인이라고 확정하지 않는다. 일반적인 Tab 우월성·UPC 소속 수정 성공·최종 RCTL 개선도 확인하지 않았다.

[C19] 아래 비압축 HGB 기준은 훈련672시점을 사용하므로 위의 context256 HGB와 다르다. 비압축 기준의 MSE는0.0124458567, MAE는0.0771721이다. 훈련 구간이 늘었는데 MSE는 context256 HGB보다 높고 MAE는 낮다. 다른 훈련 범위·목적 지표를 합쳐 단순한 우열이나 단조적인 학습 효과로 설명하지 않는다.

[C20] 일곱 압축의 assessment MSE는 모두 비압축 기준보다 크고 양쪽84시간에서도 같은 방향이다. Tab plugin은 raw_all보다 전체 MSE가 조금 작지만 corrected는 그렇지 않다. 이런 작은 차이를 새 압축 방향의 통과 기준으로 삼지 않았다는 당시 판단을 보존한다.

| 실제 target을 학습한 HGB | MSE |
|---|---:|
| 비압축4출력 |0.0124458567|
| raw_all |0.0198714056|
| raw_calibration |0.0236124925|
| Ridge plugin |0.0200354643|
| Ridge corrected |0.0200173221|
| HGB plugin |0.0198627746|
| Tab plugin |0.0197991680|
| Tab corrected |0.0200536405|

[C21] “모든 cell·모든 날짜에서 나빴다”는 결론은 틀리다. 단일 cell3737을 둔6조건은 그 cell에서 비압축과 같은 오차를 보였고, raw_calibration의 cell6137은0.0141355438로 비압축0.0143902746보다 작았다. 또 assessment의 **여섯째 날(12/11)**에는 그6조건이 비압축 MSE0.0239970772보다 낮았다. raw_calibration의 cell3737은0.042848563으로 크게 나빴다. 전체·절반의 기각과 국소 이득은 양립한다.

[C22] 이미 만든 teacher 예측을 기저에 투영한21조건의 MSE는0.0181527056–0.0248652140으로 각 원래 직접 예측보다 높았다. 실제 미래 target을 기저에 투영한 reconstruction MSE는 최소0.0137290708이었다. 후자는 미래 정답을 사용하는 **복원 손실 진단**이며 실행 가능한 예측 성능이 아니다. 같은 고정 affine 출력공간의 제곱오차 하한으로 해석할 수 있어도 임의의 다른 decoder·입력·MAE에 확장하지 않는다.

[C23] 전역 rank2의 unconstrained 기저와 retained score도 저장돼 있고, 각 기준에서 두 그룹 rank1 목적값 이상이었다. 그러나 그 전역 기저로 학습한 HGB 예측 결과는 없다. 또한 저장 일곱 행렬은 모두 양의 정부호였다. corrected가 일반적으로 부정부호일 수 있다는 이론적 가능성과 이번 자료에서 실제로 그랬다는 주장을 구분한다.

[C24] 직교기저의 저장 예측에 대해 각 평가 행의 squared error가 공간 밖 복원 오차와 공간 안 예측 오차의 합으로 나뉨을 확인했다. 이는 **고정 기저·제곱오차의 대수**다. MAE의 동일 분해, rank 축소에 따른 유한 표본 학습 개선, RCTL이 latent 함수를 쉽게 배운다는 결론은 따르지 않는다.

## 연산량·실제 비용·보존

[C25] 정적 RCTL port의 폭은16·32·64·64·32·16이다. 각 block의 두 kernel3 convolution, 두1×1 shortcut,4gate LSTM을 세면 시점당 `5×입력폭×출력폭+11×출력폭²` MAC이다. 세1×1 projection·마지막 shortcut·dense head를 더한 **L=2, 공통 channels=24 가정**의 결과는 아래와 같다.

| 가정한 출력 방식 | MAC |
|---|---:|
|4개 scalar core |1,376,384|
|두 그룹 rank1 core+희소 decoder |688,196|
|두 그룹에서 총4개 출력 |688,256|
|단일 core에서4개 출력 |344,192|

[C26] 원 JSON의 `two_cluster_full_rank2_calls`는 두 head가2개씩인 합계4출력 계산이다. 실제 선택된1/3개 cell 그룹에1+3개 head를 주어도 이 단순 MAC 합은 같다. decoder의4 MAC에는 중심을 더하는4회 덧셈이 빠져 있다. bias·활성화·BN·dropout·메모리 이동·훈련 비용도 제외했다. 실제28열 입력을 L2/channels24 RCTL에 연결한 구현이나 RCTL fit/forward·속도 측정은 없다. rank 감소보다 core 수의 영향이 컸다는 **가정 산술**만 확인한다.

[C27] 과거74 실행 기록은 Tab4 contexts·1,344 query행·simple26 fits·RCTL fit/forward0이다. Tab5.2815415000초, simple fit2.3038001000초, cheap2.6676498000초, stage7.9491913000초다. simple 시간은 cheap 안에 포함된다. stage timer는 입력 해시·일부 준비 뒤에 시작했고 RSS494,415,872바이트는 호출 사이 관측 최대다. 전체 준비를 포함한 종단 시간이나 연속 측정 메모리 최대라고 쓰지 않는다.

[C28] 전후 원장은 stage를 한 번 추가했다. Tab 누적65→69 contexts,38,016→39,360 query행, 잔여15→11 contexts·21,984→20,640행이다. cheap 누적64.0769553→66.7446051초이며 RCTL 누적29 fits·잔여0 및 기존 상한은 그대로다. 이것은 **과거 연구 예산**이며 현재 정리 Goal의 토큰 예산이나 새 실험 허가가 아니다.

[C29] 계획·실행 코드·HDF·checkpoint·RCTL port의 현재 해시가 실행 settings에 저장된 값과 일치한다. 현재 checkpoint는 해시만 읽었고 역직렬화하지 않았다. 원목록의 루트 `data_git_version.h5` 별칭은 현재 없지만 실제 사용된 `tmp/redesign_20260925/assets/data_git_version.h5`는 일치한다. 사라진 별칭까지 현재 검증한 경로로 세지 않는다. 누가 언제 이동·삭제했는지는 미확인이다.

[C30] `arrays.npz`와 `arrays_partial.npz` 및 스냅샷 사본은 같은 바이트다. 따라서 final/partial을 별도 실험으로 세지 않는다. 저장39개 numeric array는 유한값이고,32지표군(직접3·비압축1·압축7·투영21)의7항목을 대조했다. 해당 assessment 예측의 음수 개수는 모두0이라 clipping MSE도 같다. 다른 기간까지 같은 사실이라고 일반화하지 않는다.

## 같은 연구를 다시 시작하기 전에

[C31] 75는 Tab 직접 예측의 긍정 결과를 보고 입력 공유·Granger 경로를 다시 탐색했지만, 47에서 이미 다룬 역할이라는 판단으로 중단됐다. 원75에 남은 일부 후보는 검색·metadata·초록 수준이다. 그 문헌의 전체 방법을 확인했거나 새 입력 공유 성능을 얻은 것으로 기록하지 않는다.

[C32] [47 입력 공유](0047-input-sharing-roles.md)는 **B의 sample을 A와 함께 학습하는 것**과 **B의 과거를 A의 입력 열에 더하는 것**을 분리한다. 예측 의존성이 강하다는 사실만으로 같은 RCTL 함수를 공유하기 좋다는 충분조건이 되지 않는 반례와 비용 산술도 이미 있다. 75의 동일 조건 own-only Tab 비교는 수행되지 않았다.

[C33] [48–49 집계·복원](0048-0049-aggregation-recovery.md)과 [50 선행](0050-aggregation-literature.md)은 sample 공유, 여러 출력의 공동 예측, 합계 하나의 예측·배분을 구분했다. 74의 affine rank 압축은 새로 바뀐 학습 target과 복원 오차를 명시해야 한다. “대표만 예측하면 싸다” 또는 “합계가 쉬우면 개별 예측도 좋다”는 말만으로 기존 경로와 구별되지 않는다.

[C34] [60 이력·grouping](0059-0062-history-grouping.md)도 같은4cell에서 Tab의 직접 예측 우위를 보고했지만, context168–839 중256개·다른 날짜 query64개·median·자기 cell의 lag 및 pooled row 구조였다. 74의 context168–671·query336·mean·공통 공간28열과 직접 비교해 공간 입력 효과를 추정하지 않는다. 당시60과 이번74의 데이터 범위·손실 목적을 함께 바꾼 차이를 분리해야 한다.

[C35] snapshot18의 `candidate_decision_index.md` 실제 표는 **13가지 결정**이다. 같은 스냅샷 `progress.md`18행은14가지라고 보고한다. 원본은 보존하고 정리본은 실제 표 행 수13을 사용한다. 이 인덱스의 과거 실행 지시를 현재 작업 지시로 적용하지 않는다.

[C36] snapshot18 manifest의71파일·19,148,054바이트를 현재 사본과 다시 해시 대조했다. 당시 verification의 PDF3개·84쪽·preview7개는 역사적 보관 검사 수치다. 이번에 논문84쪽이나 그림7쪽을 읽었다는 뜻이 아니다. progress는 snapshot17→18의 전체 변경 부분과18의1–30행을 읽었고,327행 전체 독해로 가산하지 않았다.

[C37] 이번 출처 묶음은81개 고유 바이트 그룹이다. 원문 사본 참조45개(신규37·기존 재사용8), 외부·대용량 metadata36개이며 등록 별칭197경로 중 현재196경로가 일치했다. 신규 전체 텍스트19·전체 JSON15·선택 범위2의 검토 범위를 분리한다. metadata만 연결한 파일을 본문 완료·중복 제거로 처리하지 않는다.

[C38] 팀은 [원 결과 JSON](../evidence/0072-0075-output-compression/originals/SRC-0029276.json), [원 배열](../evidence/0072-0075-output-compression/originals/SRC-0029270.npz), [정확사본·재사용 자료 안내](../evidence/0072-0075-output-compression/README.md), [선택 HDF 추출의 출처](../evidence/0072-0075-output-compression/selected-source-data-provenance.json)를 재사용할 수 있다. 선택 NPZ는 정리 과정의 파생물이고 원 HDF 파일 자체가 아니다. 공개 검사에는 torch·TabICL·h5py·checkpoint가 필요 없다.

[C39] 재검토를 제안할 때는 ①기존 실패 원인을 실제로 바꾸는 결정, ②Tab 계산이 단순 대안보다 달리 고르는 것, ③최종 모델 입력·실제 target·학습 단위의 구체적인 변화, ④같은 비용의 비압축 multioutput 대안, ⑤기간·cell별 손해와 개발 구간 재사용을 먼저 명시한다. rank·regularization·지표 이름만 늘리거나 좋은 직접 Tab 예측을 RCTL 개선으로 옮기지 않는다. 이는 과거 기록을 찾기 위한 설계 기준이며 현재 새 실험을 착수하라는 지시가 아니다.

[C40] 남은 일은 72–73 일차 논문·외부 코드·그림,72–75 검색11개와 접근 실패의 실제 범위 검수다. 그 뒤76 이후·이전 partial·실패/비용 통합·대용량 팀 접근·최종 원본 변화·대표 질문 검색 검수도 계속한다. 이 기록·PR의 완료를 전체 아카이브 Goal 완료로 표시하지 않는다.
