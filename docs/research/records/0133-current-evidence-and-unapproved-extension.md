# 원103 현재 근거의 중간 보고와 미승인 실행 범위

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

**직접 예측의 이점은 확인했지만 최종 RCTL 소속 선정의 개선 근거는 남아 있었다.** 원103은 그 차이와 연구 완료 조건을 최신 중간 보고서에 반영한 문서화 기록이다. 추가18fit은 아직 승인·실행하지 않은 상한 제안으로 남겼다.

[30출처/65사본](../sources/history-133.md) · [33주장](../verification/history-133-claims.json) · [작성 후 대조](../verification/history-133-second-pass.json) · [읽기용 보고서](../evidence/0133-current-evidence-and-unapproved-extension/readable-report.md) · [재사용 조건](../references/current-evidence-and-unapproved-extension.md)

## 질문과 실제 수행

2026-09-26 [원101](0131-actual-pooled-context-and-rctl-ranking.md)의 실제 pooled context 결과와 [원95](0125-frozen-rctl-serving-cost-baseline.md)의 CPU serving 비용을 [원84 중간 Word](0111-interim-document-history.md) 이후의 보고서에 반영했다. [원102](0132-architecture-kernel-and-joint-risk.md)의 구조 기반 점수 보류도 함께 설명했다. 새 모델·traffic 실험은0이고, 새로운 추천안의 완료로 바꾸지 않았다.

같은16개 Milan Internet activity cell, context target168–839/672행과 query1008–1343/336행의 개발 자료를 비교했다. Tab/Ridge/HGB의 입력은16열이다. RCTL의 validation840–1007, 입력 표현과 학습 절차를 함께 확인해야 한다. 연속14일의 관찰된 입력을 평가한 결과를336시간 open-loop 예측의 성과로 읽지 않는다. 자세한 구현과 조건은 원101에 연결했다.

## 저장 결과와 남은 연결

| 예측기 | Global K1 | Tab risk K4 | 관측값 risk K4 |
|---|---:|---:|---:|
| TabICLv2 | 0.06618 | 0.07325 | 0.07541 |
| Ridge | 0.07923 | 0.08679 | 0.08244 |
| HGB | 0.07157 | 0.09170 | 0.08460 |
| 저장 RCTL seed20260925 | 0.07287 | 0.08600 | 0.07986 |
| 저장 RCTL seed20260926 | 미실행 | 0.08810 | 0.08367 |

정규화 활동량의 cell 평균 MAE이며 작을수록 좋다. 표시14값은 저장JSON·Word·PDF와 반올림 대조했다. Tab의 직접 예측 이점과 두K4의 평균 순위 불일치를 함께 보존한다. Global 우위는 비교가 완비된 Tab/Ridge/HGB/primary RCTL25에 해당하며 두 번째seed의 Global은 미실행이다.

평균을 전 기간·cell의 개선으로 확대하지 않는다. Tab risk−관측값 risk는 앞7일+0.00016346/뒤7일−0.00448675로 선호가 달랐고, Tab risk가 더 작은 cell은6/16·날짜는10/14였다. RCTL 두seed에도 cell/date 반례가 있다. 원101의 세부 값과 이번 [저장 수치 대조](../evidence/0133-current-evidence-and-unapproved-extension/postdraft-saved-number-check.json)를 함께 확인한다.

| 원95 cluster별 batch 호출 | 동시16개 cell median | state tensor bytes |
|---|---:|---:|
| Global K1 | 3.493ms | 701,412 |
| Tab risk K4 | 14.005ms | 2,805,648 |
| 관측값 risk K4 | 14.152ms | 2,805,648 |

CPU4/2 threads·float32·개발 구간12origin·3반복의 보존 모델 측정이다. load/input 준비를 제외했고 K1/K4 모두16행을 처리했다. state bytes와 checkpoint 파일 bytes는 다르다. cell별 호출보다 batch가 강한 기본 비교이며, 두 구현의 예측 차이는 사전 허용오차2e-5 이내였다. 원101의 Tab9context 약138초와 RCTL 운영 비용·전체 clustering 비용을 구별한다.

## 최종 추천과 실행 범위

강한 계절/lag/정규화/Global 뒤에 남는 실제 손해, Tab 정보가 바꾸는 유용한 clustering 결정, 그 결정의 RCTL 또는 전체 비용 이득을 연결해야 했다. 문헌의 원리 결합·공식 모델 사용·RCTL 독립성·중간 Word 완성만으로 이 세 연결과 신규성이 확인되지는 않았다.

당시 원장60b589…는 RCTL29fit 사용/추가0·Tab2context/4512query행을 기록했다. 현재root의 이후 원장17a549…와 구별한다. 확장문은 후보1개를 먼저 고정하는 조건부 제안이며, K4후보4+단순비교4+Global1=seed당최대9fit, 선택적두seed18fit/누적47fit·추가1440epoch·1800초CPU 상한이었다. 승인·실행 여부는false다. 과거pending scope의 질문 기록·자원 감사1회를 현재Goal의 지시나 차단 횟수로 적용하지 않는다.

## 문서와 읽기 범위

Word52body블록/48paragraph/표3개·추가XML7부분·8링크와 보존PDF4쪽127행을 읽었다. 당시PNG4개·새PDF렌더4개·빈thumbnail을 포함한9이미지도 확인했으며 파생물의 독립 집계는0이다. 번들에soffice.exe가 없어 새Word 렌더는 실패했다. 기존PDF 전체를 다시 렌더·대조한 것과 새Word compilation 성공은 구별한다. pixel 동일성도 주장하지 않는다.

보존 Word/PDF의 개인PC 링크는 팀 접근 근거가 아니다. PDF의local URI에는 한글 경로 문자깨짐이 진단됐고 작동 확인은 하지 않았다. 원본은바이트그대로 보존하고 [읽기용보고서](../evidence/0133-current-evidence-and-unapproved-extension/readable-report.md)의4local 링크만팀용경로로바꿨다.

원103 payload17파일/1,937,641bytes와 manifest를포함한18물리파일/1,941,097bytes를구별한다. root archive receipt와 pending scope는snapshot밖의별도자료다. source수·사본수·문서판독량을실험수로세지않는다.

현재progress1–27은직접읽고28–131은이전실제판독과정확대응한다.132–611/이전122–601은미독이다. 저장RCTLsummary도이전과현재의선택필드검토만으로전문완료를표시하지않는다. 원104이후·다른고유판본/형식·전체통합/장기접근/최종delta/검색10+와전체Goal은미완료다.

## 주장별 근거

<a id="claim-01"></a>

### H133-C01 · 당시 작업은 최신 근거의 중간 문서화

2026-09-26 원103은 원101의 실제 pooled context 결과와 원95의 저장 RCTL 호출 비용을 원84 이후의 중간 보고서에 반영하고, 연구 완료 조건을 감사한 기록이다. 새 추천 후보·새 clustering 알고리즘·새 성능 실험을 완성한 기록으로 세지 않는다.

근거: [SRC-0002025](../sources/history-133.md#src-0002025) 행1–21 · [SRC-0002032](../sources/history-133.md#src-0002032) 행7–15 · [SRC-0002023](../sources/history-133.md#src-0002023) 행1–5 · [SRC-0002027](../sources/history-133.md#src-0002027) JSON /purpose, /new_model_calls, /new_traffic_numerical_experiments

<a id="claim-02"></a>

### H133-C02 · 새 이름의 Word와 기존 Word 보존

새 보고서는 TabICLv2와 RCTL 연구 재설계의 현재 근거라는 제목의 Markdown과 Word다. 기존 원84 Word를 덮어쓰지 않았고, 기존 Word SHA4f1112…와 새 Word SHA72972f…를 구별한다. 중간 문서의 완성과 최종 추천·최종 연구 산출물의 완료는 별개다.

근거: [SRC-0002029](../sources/history-133.md#src-0002029) 행5–15 · [SRC-0002029](../sources/history-133.md#src-0002029) 행125–127 · [SRC-0002033](../sources/history-133.md#src-0002033) 행26–27 · [SRC-0002026](../sources/history-133.md#src-0002026) JSON /docx_sha256, /previous_word_unchanged, /artifact_is_interim, /final_recommendation_selected, /goal_complete

<a id="claim-03"></a>

### H133-C03 · 원문 묶음과 실제 판독의 구별

현재 묶음은 최초20개 SHA/40물리경로에 이전 progress 판본1개와 추가 재사용 근거9개를 연결한30개 고유 출처/65물리경로다. 실제 현재 literal 원문은17개1092행을 읽었고14개는 전문·3개는 선택 구간이다. 새 principal 전문은 literal11개와 Word/PDF 각1개이며, 재사용·파생 이미지·미독 구간을 새 전문으로 세지 않는다.

근거: [SRC-0002021](../sources/history-133.md#src-0002021) 행1–91 · [SRC-0020842](../sources/history-133.md#src-0020842) 행1–10 · [SRC-0002032](../sources/history-133.md#src-0002032) 행1–27

<a id="claim-04"></a>

### H133-C04 · Word 본문 표 주석과 문서 메타데이터

새 Word의 body52블록(0–51), paragraph48개, 표3개와 footer·문서 relationship을 포함한 추가XML7부분, 링크8개, 빈thumbnail을 확인했다. comments/footnotes/endnotes 부분과 수식·그림·embedded object·tracked insert/delete는 없었다. docProps의2013 template 시각과 app.xml의Pages1을 연구 날짜나 실제1쪽으로 해석하지 않는다. 본문의2026-09-26와 보존PDF4쪽을 기준으로 삼는다.

근거: [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51 · [SRC-0002034](../sources/history-133.md#src-0002034) PDF쪽 1,2,3,4 · [SRC-0002026](../sources/history-133.md#src-0002026) JSON /pages, /page_text_character_counts

<a id="claim-05"></a>

### H133-C05 · 보존 PDF의 전쪽 확인과 새 Word 렌더 한계

보존 PDF4쪽127텍스트행과 당시 PNG4개·새 PDF 렌더4개를 모두 확인했다. 표와 본문·각주성 note·출처·쪽번호를 보존했고 clipping/빈쪽/분리표/고립heading은 관찰하지 않았다. 두 이미지 집합의 pixel은 동일하지 않다. 현재 번들에 soffice.exe가 없어 Word의 새 렌더는 실패했으며, 기존 hidden Word COM adapter를 재실행하거나 새 Word compilation 성공으로 표시하지 않았다.

근거: [SRC-0002034](../sources/history-133.md#src-0002034) PDF쪽 1,2,3,4 · [SRC-0002026](../sources/history-133.md#src-0002026) JSON /pages, /all_pages_visually_reviewed, /visual_result · [SRC-0002032](../sources/history-133.md#src-0002032) 행11–11

<a id="claim-06"></a>

### H133-C06 · progress의 변경 부분과 미독 꼬리

Snapshot44 progress601행에서 old7의 최신102 제목을 new7–17의 최신103/이전102 절로 바꾸고, old8–601은 Snapshot45 new18–611과 정확히 같다. 현재는 new1–27을 직접 읽었고 new28–131은 이전 actual 범위를 정확한 equal 대응으로 재사용한다. new132–611과 old122–601은 여전히 미독이며 전체 progress 완료로 표시하지 않는다.

근거: [SRC-0002032](../sources/history-133.md#src-0002032) 행1–27 · [SRC-0001999](../sources/history-133.md#src-0001999) 행7–7 · [SRC-0002033](../sources/history-133.md#src-0002033) 행100–115

<a id="claim-07"></a>

### H133-C07 · 동일 시각 비교의 실제 자료와 입력

직접 예측 표는 Milan Internet activity16개 고정 cell의 정규화 MAE다. Tab/Ridge/HGB에는 lag8–lag1, lag24/168, mean24/std24, hour·weekday sin/cos의16열을 주었다. context target168–839는 cell당672개, query1008–1343은 연속14일/336개다. RCTL validation840–1007과 분리했고 이미 본 개발 자료다. 같은 query·소속을 맞춘 비교를 모든 모델의 입력 표현·학습·validation 절차까지 동일한 실험으로 쓰지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행9–25 · [SRC-0001965](../sources/history-133.md#src-0001965) 행17–21 · [SRC-0001965](../sources/history-133.md#src-0001965) 행59–59 · [SRC-0001982](../sources/history-133.md#src-0001982) 행12–157 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 4,5,10

<a id="claim-08"></a>

### H133-C08 · 고정된 K1과 두 K4의 의미

Global은16개 cell의 K1, Tab risk와 관측값 risk는4개 cell씩4cluster의 기존 K4다. 실제 sample을 한 context에 합친 것은 원101에서 실행했고, 원103은 이를 문서화했다. 소속은 저장 RCTL 학습 전에 정한 것으로 유지했으며 이번 결과를 보고 바꾸지 않았다. 실제 context 공유와 옛 B2의 예측분포 합산을 같은 실행으로 세지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행11–25 · [SRC-0001965](../sources/history-133.md#src-0001965) 행9–21 · [SRC-0001984](../sources/history-133.md#src-0001984) JSON /RCTL_results_used_to_change_partition · [SRC-0001982](../sources/history-133.md#src-0001982) 행30–103 · [SRC-0001982](../sources/history-133.md#src-0001982) 행145–147

<a id="claim-09"></a>

### H133-C09 · 표의14개 MAE와 미실행 값

보고서·Word·PDF의14개 MAE는 원101 summary와 원103 audit의 저장 mean_cell_MAE를 소수5자리로 반올림한 값과 일치했다. RCTL 두 번째 seed의 Global은 미실행이며0이나 NaN 실패로 채우지 않는다. cell별 고정 척도의 같은 비중 평균으로, 원단위 MAE·clustering 점수·모든 cell의 개선과 구별한다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행13–25 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 6 · [SRC-0002034](../sources/history-133.md#src-0002034) PDF쪽 1 · [SRC-0002027](../sources/history-133.md#src-0002027) JSON /reported_metrics_from_saved_JSON · [SRC-0001965](../sources/history-133.md#src-0001965) 행25–33

<a id="claim-10"></a>

### H133-C10 · 직접 예측과 K4 선택 순위의 불일치

Tab의K4 MAE는 Tab risk0.07325<관측값 risk0.07541이었다. 저장 RCTL은 seed20260925에서0.08600>0.07986, seed20260926에서0.08810>0.08367로 반대 평균 순위를 냈다. 좋은 Tab 직접 예측을 좋은 RCTL 소속 판단의 근거로 바로 승격하지 않으며, 공통 context 확인만 추가해 기존 문제를 해결했다고 하지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행15–21 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 6,8 · [SRC-0001984](../sources/history-133.md#src-0001984) JSON /metrics/TabICL_tabicl_risk/mean_cell_MAE, /metrics/TabICL_empirical_risk/mean_cell_MAE, /metrics/RCTL_tabicl_risk_20260925/mean_cell_MAE, /metrics/RCTL_empirical_risk_20260925/mean_cell_MAE, /metrics/RCTL_tabicl_risk_20260926/mean_cell_MAE, /metrics/RCTL_empirical_risk_20260926/mean_cell_MAE

<a id="claim-11"></a>

### H133-C11 · 유지할 직접 예측의 긍정 근거

Global의 Tab0.06618은 같은16열·학습 자료의 HGB0.07157와 Ridge0.07923보다 작았다. 원101은 각각7.53%/16.46% 감소를 보고했고 앞·뒤7일에서도 우열이 같았다. 이는 해당 개발 자료의 직접 예측 이점이며 사전학습만의 인과효과·모든 도시/기간/partition의 승리·최종 RCTL 대체 결정이 아니다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행23–25 · [SRC-0002023](../sources/history-133.md#src-0002023) 행93–93 · [SRC-0001965](../sources/history-133.md#src-0001965) 행29–39 · [SRC-0001965](../sources/history-133.md#src-0001965) 행59–63 · [SRC-0001984](../sources/history-133.md#src-0001984) JSON /metrics/TabICL_global/mean_cell_MAE, /metrics/HGB_global/mean_cell_MAE, /metrics/Ridge_global/mean_cell_MAE, /metrics/TabICL_global/first7_MAE, /metrics/TabICL_global/last7_MAE, /metrics/HGB_global/first7_MAE, /metrics/HGB_global/last7_MAE, /metrics/Ridge_global/first7_MAE, /metrics/Ridge_global/last7_MAE

<a id="claim-12"></a>

### H133-C12 · Global 우위의 비교 가능한 범위

14일 평균에서 Global이 두 K4보다 좋았다는 결론은 Tab/Ridge/HGB와 primary RCTL seed20260925의 완비된 비교에 해당한다. second seed Global은 없으므로 두 seed 모두의 K1 우위로 확대하지 않는다. Global을 고른 결과 자체는 Tab 고유 기여가 아니며 모든 cell·앞뒤 주의 K1 우위도 아니다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행13–25 · [SRC-0001965](../sources/history-133.md#src-0001965) 행33–39 · [SRC-0001984](../sources/history-133.md#src-0001984) JSON /differences/HGB:empirical_risk_minus_global

<a id="claim-13"></a>

### H133-C13 · 평균 선호 안의 기간 cell 날짜 반례

Tab risk−관측값 risk는 전체−0.00216165였지만 앞7일+0.00016346/뒤7일−0.00448675로 선호가 바뀌었다. Tab risk가 더 작은 cell은6/16, 날짜는10/14다. RCTL 두 seed의 평균·앞뒤 주는 관측값 risk가 좋았지만 Tab risk가 더 작은 cell/date도 각각5/16·2/14와6/16·4/14 있었다. HGB도 앞7일에는 관측값 K4가 Global보다 작았다. 평균 판단을 전 cell·전 날짜의 결과나 독립 유의성 검정으로 쓰지 않는다.

근거: [SRC-0001965](../sources/history-133.md#src-0001965) 행41–53 · [SRC-0001984](../sources/history-133.md#src-0001984) JSON /differences/TabICL:tabicl_risk_minus_empirical_risk, /differences/RCTL25:tabicl_risk_minus_empirical_risk, /differences/RCTL26:tabicl_risk_minus_empirical_risk, /differences/HGB:empirical_risk_minus_global

<a id="claim-14"></a>

### H133-C14 · 같은 예측 정보와 학습 효용의 차이

보고서는 sample 수·시간상 중복·입력의 cell 구별·모델 용량·학습 방식을 공유 효용과 연결할 요인으로 제시했다. 입력이 상황을 구별하면 다른 target을 함께 예측할 수 있고, 유사한 관계라도 충분하거나 중복된 자료의 추가 이득은 작을 수 있다는 설명이다. 이번 순위 차이의 원인을 이 요인 하나로 확정한 실험은 아니다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행29–33 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 13,14 · [SRC-0001965](../sources/history-133.md#src-0001965) 행59–63

<a id="claim-15"></a>

### H133-C15 · CPU batch 비용 표의 실제 측정 조건

원95의 seed20260925 보존 RCTL에서 동시16개 cell을 cluster별 batch로 처리한 median은 K1 3.493ms, Tab riskK4 14.005ms, 관측값 riskK4 14.152ms였다. CPU4 intra-op/2inter-op threads·float32·12origin840–1007·3반복이며 load/input 준비를 제외했다. 같은 기기의 frozen serving 측정으로, 원101의14일 정확도 query나 독립 미래 정확도 평가와 다르다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행35–47 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 16,17,19,20 · [SRC-0001819](../sources/history-133.md#src-0001819) JSON /settings, /metrics, /scope

<a id="claim-16"></a>

### H133-C16 · model 수 행 수 상태와 파일 용량

K1/K4의 예측 행 수는 시점당16개로 같다. cluster별 호출은1/4번이며 state tensor 저장량은701412/2805648bytes로4배다. checkpoint 파일은745123/2980492bytes로 별도 값이다. model 수 감소를 cell 행 감소·프로세스 RAM 비율·1만cell 운영 시간의 선형 외삽으로 바꾸지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행37–47 · [SRC-0001819](../sources/history-133.md#src-0001819) JSON /metrics, /checkpoints

<a id="claim-17"></a>

### H133-C17 · cell별 호출보다 강한 기본 비교와 허용오차

같은 가중치의 cell을 batch로 처리하는 구현은 먼저 포함해야 할 비용 비교다. 원95의 cell별→batch median은 Global33.186→3.493ms, TabK4 33.865→14.005ms, 관측값K4 34.038→14.152ms였다. 최대 예측 차이7.15e-7/1.19e-6/1.07e-6은 사전2e-5 이내였으며 bit 단위 동일성·정확도 향상·Tab clustering 신규성의 증거가 아니다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행37–47 · [SRC-0001819](../sources/history-133.md#src-0001819) JSON /metrics, /within_method_comparisons, /settings

<a id="claim-18"></a>

### H133-C18 · Tab context 비용과 RCTL 운영 비용의 구별

원101의9context/16128query행/ensemble1/median 출력은 Tab fit+predict138.258204초, 단순 모델18fit의 fit+predict1.004838초, 단계전체140.485289초를 남겼다. import와 최초 source hash는 단계 시간에서 제외했다. 원103의약138초 인용은 새 측정이 아니며 Tab의context 비용을 최종 RCTL 운영 속도나 전체 clustering 총비용과 섞지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행69–71 · [SRC-0001965](../sources/history-133.md#src-0001965) 행65–80 · [SRC-0001980](../sources/history-133.md#src-0001980) 행1–16 · [SRC-0001982](../sources/history-133.md#src-0001982) 행130–156 · [SRC-0001984](../sources/history-133.md#src-0001984) JSON /state

<a id="claim-19"></a>

### H133-C19 · 구조 기반 점수의 보류 범위

원102 검토를 반영해 지금은 RNN kernel을 새 점수로 추가하지 않는다고 썼다. LSTM·BN의 이론적 표현 가능성과 초기화·무한폭 결과를 유한 RCTL의 Adam·MAE 학습 결과에 연결할 근거를 구별한다. 새로운 kernel 성능 실패나 모든 구조 기반 이론의 불가능성을 확인한 기록은 아니다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행49–51 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 22 · [SRC-0002034](../sources/history-133.md#src-0002034) PDF쪽 2 · [SRC-0002032](../sources/history-133.md#src-0002032) 행19–24

<a id="claim-20"></a>

### H133-C20 · HCP 비교에서 필요한 공유 결정의 직접 근거

보고서는 HCP가 분리/합친 모델의 실제 학습 손실을 비교하는 관점과, clustering에서 RCTL을 호출하지 않는 현재 조건의 차이를 정리했다. 이 비용을 줄인다는 주장은 다른 정보로 유용한 공유 결정을 내리는 근거를 필요로 한다고 판단했다. 원103 문서의 문헌 요약을 HCP 전체 원문·정리의 새 독립 검증으로 세지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행55–57 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 25 · [SRC-0002034](../sources/history-133.md#src-0002034) PDF쪽 3

<a id="claim-21"></a>

### H133-C21 · RMB CLE와 흐름만으로는 부족한 차별점

보고서는 RMB-CLE의 task별 모델 교차 예측 오차로 관계를 만들고 clustering 뒤 별도 예측기를 학습하는 구조를 비교했다. 예측 관계로 cell을 묶은 뒤 RCTL을 실행하는 흐름만으로 차별점이 되지 않고, 잘못된 소속 판단 감소나 같은 유용한 판단의 계산 감소가 필요하다는 당시 판단이다. 해당 논문 전체의 신규성 전수 감사로 확대하지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행59–61 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 27 · [SRC-0002034](../sources/history-133.md#src-0002034) PDF쪽 3

<a id="claim-22"></a>

### H133-C22 · 시간 입력과 네트워크 문헌을 가져온 범위

원103은 TabPFN-ST-AR의 lag·시간 입력을 참고하고 도로 속도 결과를 통신 활동량의 성과로 옮기지 않았다고 썼다. network traffic-matrix 연구에서 Global·같은K 단순 분할 비교를 가져왔지만 다중 출력 학습과 cell별 scalar RCTL의 비용은 구별했다. 원103에서 외부 논문 전체를 새로 재현한 것은 아니다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행63–65 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 29 · [SRC-0002034](../sources/history-133.md#src-0002034) PDF쪽 3

<a id="claim-23"></a>

### H133-C23 · Tab 사용 가능성과 대체 비교의 미실행

당시 확보한 근거는 공식 회귀 가중치로 context 추론을 실행할 수 있고 작은 자료에서 유용한 직접 예측을 얻었다는 데까지다. 새 context 준비·추론에는 비용이 있고, 더 좋은 RCTL cluster 또는 같은 판단의 비용 감소는 확인되지 않았다. 회귀 TabPFN과의 동일 조건 대체 비교는 미실행이다. 직접 예측 이득만으로 최종 예측기를 Tab으로 바꾸지도 않았다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행67–73 · [SRC-0002023](../sources/history-133.md#src-0002023) 행93–93 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 31,32,33,41

<a id="claim-24"></a>

### H133-C24 · 추천 방향에 남은 세 연결과 완료 조건

최종 추천에는 강한 계절/lag/정규화/Global 뒤에 남은 실제 손해, Tab 정보가 만드는 다른 유용한 clustering 결정, 그 결정의 최종 RCTL 또는 전체 비용 이득을 직접 연결해야 한다고 썼다. Word의5행 완료표와11개 요구사항 audit은 공식 회귀·직접 예측의 확인을 보존하면서 새 문제·유용한 결정·RCTL 연결·신규성과 최종 추천의 공백을 남겼다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행75–85 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 35,36 · [SRC-0002028](../sources/history-133.md#src-0002028) JSON /requirements, /complete, /complete_must_not_be_called · [SRC-0002027](../sources/history-133.md#src-0002027) JSON /completion, /goal_complete

<a id="claim-25"></a>

### H133-C25 · 소진한 원장과 다른 현재 root 판본

당시 pinned 원장SHA60b589…는 RCTL29fit/1565epoch/1658.139163초를 기록하고, 추가RCTL0·Tab2context/4512query행·budget_resets0·research_goal_complete=false였다. 원103은 이 상태를 유지했다. 현재 root 원장SHA17a549…와 candidate의 이후 판본을 당시 같은 원장/색인으로 덮어 읽지 않으며 기존 연구 원장을 갱신하지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행87–93 · [SRC-0002025](../sources/history-133.md#src-0002025) 행19–21 · [SRC-0002031](../sources/history-133.md#src-0002031) JSON /used, /remaining_count_budgets, /budget_resets, /research_goal_complete · [SRC-0002027](../sources/history-133.md#src-0002027) JSON /ledger_unchanged_sha256, /remaining_count_budgets

<a id="claim-26"></a>

### H133-C26 · 18회 추가 학습은 미승인 상한 제안

조건부 확장문은 아직 허용·적용되지 않은 제안이다. 새K4후보4모델+강한 단순 비교4+Global1의seed당최대9fit, 조건을 만족할 때 두seed총18fit, 기존29회 포함 최대47회·fit당80epoch/추가1440epoch·추가RCTL1800초의CPU상한이다. 이 산술을18회 실행·47회 사용·통계적 충분성·좋은 후보의 확보로 표시하지 않는다.

근거: [SRC-0002024](../sources/history-133.md#src-0002024) 행1–23 · [SRC-0002032](../sources/history-133.md#src-0002032) 행14–15 · [SRC-0002028](../sources/history-133.md#src-0002028) JSON /conditional_extension_proposed_not_authorized_or_applied · [SRC-0020848](../sources/history-133.md#src-0020848) JSON /proposal_is_authorized, /existing_RCTL_fits_completed, /new_RCTL_fits_available

<a id="claim-27"></a>

### H133-C27 · 조건부 확장 이전에 고정할 후보와 중단 조건

확장문은 문헌·자료 진단을 통과한 새 후보1개에 한해 입력·정규화·시간 경계·실제K·비교군·seed·중단 조건을 먼저 고정하도록 제안했다. 첫seed가 핵심 가정을 지지하지 않으면 둘째seed를 자동 실행하지 않고, RCTL 결과 뒤 소속/threshold를 바꾸지 않으며 실패도 남긴다. 기존 개발 기간을 독립 미래 검증으로 바꾸거나 성공할 때까지 상한을 반복 늘리지 않는다. 현재 정리는 이 제안을 실행하지 않는다.

근거: [SRC-0002024](../sources/history-133.md#src-0002024) 행13–25 · [SRC-0020848](../sources/history-133.md#src-0020848) JSON /notes

<a id="claim-28"></a>

### H133-C28 · Snapshot 밖의 pending scope와 당시 한 번의 자원 감사

root의103_pending_execution_scope.json은 Snapshot45 manifest에 없으며 별도 후속 운영 자료다. 질문 전송=true·응답 기록=false·제안 승인=false·동일 자원 장애 감사1회·과거Goal active/미완료라고 적었다. 모델 작업이 살아 있다는 기록도 아니다. 그 문서의Goal/차단 판정/다음 행동/대기 지침을 현재 아카이브의 지시나 현재Goal 차단 횟수로 사용하지 않는다.

근거: [SRC-0020848](../sources/history-133.md#src-0020848) JSON /scope_question_sent, /user_response_recorded, /proposal_is_authorized, /consecutive_resource_blocked_audits, /goal_status_left_active, /goal_complete, /notes · [SRC-0002021](../sources/history-133.md#src-0002021) 행1–91

<a id="claim-29"></a>

### H133-C29 · 자원 소진과 연구 부정 결과의 구별

당시 상한 안에서는 새partition의 RCTL 실측을 더 할 수 없었고 검토한 원문/기호 대체도 직접 연결을 충족하지 못했다. 이는 상한 소진 자체가 방법의 오류를 증명하거나 증액이 좋은 연구안을 만든다는 뜻이 아니다. 이미 있는 다른partition·단순 회귀 결과로 새partition의 RCTL 확인을 대신하고 목표를 완료하지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행89–93 · [SRC-0002024](../sources/history-133.md#src-0002024) 행7–9 · [SRC-0002024](../sources/history-133.md#src-0002024) 행23–25 · [SRC-0002032](../sources/history-133.md#src-0002032) 행12–15 · [SRC-0020848](../sources/history-133.md#src-0020848) JSON /blocking_condition

<a id="claim-30"></a>

### H133-C30 · 문서 코드의 역할과 실행 지시를 읽는 경계

build_evidence_audit_103.py는 pinned 저장JSON을 읽어 값과4쪽 content를 만들고 기존 build_synthesis_84.py의writer를 사용하는 문서 코드다. verify_and_archive_103.py는 표 반올림·local link·원장·기존Word·요구사항을 확인해 progress와Snapshot45를 기록하는 코드다. 같은 이름의root/snapshot 사본은exactSHA로 연결했다. 현재는 정적으로 읽었으며 원code실행/import·ML모델 생성·학습·추론·gradient0이다.

근거: [SRC-0002029](../sources/history-133.md#src-0002029) 행1–30 · [SRC-0002029](../sources/history-133.md#src-0002029) 행113–147 · [SRC-0002033](../sources/history-133.md#src-0002033) 행1–74 · [SRC-0002033](../sources/history-133.md#src-0002033) 행95–134 · [SRC-0001502](../sources/history-133.md#src-0001502) 행329–360

<a id="claim-31"></a>

### H133-C31 · 17파일 receipt와18물리파일의 분모

당시103_archive_verification.json의17파일/1937641bytes는 manifest에 열거된payload다. manifest 자체3456bytes를 포함하면 Snapshot45는18물리파일/1941097bytes다. 별도103_archive_verification.json과 root pending scope는 snapshot payload 목록 밖에 남았다. 이 숫자 차이를 누락 실험·독립 결과 증가로 세거나 snapshot만으로 원103 전체 운영 기록을 닫지 않는다.

근거: [SRC-0002021](../sources/history-133.md#src-0002021) 행1–91 · [SRC-0020842](../sources/history-133.md#src-0020842) 행1–10 · [SRC-0002033](../sources/history-133.md#src-0002033) 행117–134 · [SRC-0020848](../sources/history-133.md#src-0020848) 행1–32

<a id="claim-32"></a>

### H133-C32 · 개인 PC 링크와 팀용 읽기 경로

새 Word와 보고서의 출처8개는 개인PC local4개와 공식웹4개다. local 원문은 HCP TXT·원101·원95·원102를 가리킨다. PDF4쪽의8개 URI action도 읽었으며 local URI의 한글 경로는 pypdf와 원시bytes의UTF8 진단에서 문자깨짐으로 나타났다. 링크를 열어 작동 성공을 확인한 것은 아니다. 보존 Word/PDF의 개인PC file link를 팀 접근 확인으로 세지 않는다. 읽기용 Markdown은 기존 검수 기록·공식문헌·정확사본으로 연결하고 보존원본의 바이트는 바꾸지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행95–111 · [SRC-0002022](../sources/history-133.md#src-0002022) DOCX zero-based body 42,43,44,45,46,47,48,49,50 · [SRC-0002033](../sources/history-133.md#src-0002033) 행54–63 · [SRC-0002034](../sources/history-133.md#src-0002034) PDF쪽 4

<a id="claim-33"></a>

### H133-C33 · 재검토 조건과 전체 정리의 남은 범위

팀은 원101의 직접예측과 기간·cell 반례, 원95의 batch 비교, 원102의 이론 경계, 원103의 미완료 조건과 미승인 확장을 함께 재사용한다. 재검토에는 강한 단순방법 뒤의 새 손해, Tab으로 바뀌는 결정, 직접 RCTL 또는 비용 근거와 고정 후속검사를 구체화해야 한다. 현재 progress132–611, 이전 RCTL summary의 전문 미확인, 다른 고유판본·이후기록·Word/PDF/발표/HWP/FedPPBC, 전체통합·장기접근·최종 원본delta·대표질문10개 이상 검색검수는 남아 있다. 일부 문서의 완료나 병합을 전체Goal 완료로 세지 않는다.

근거: [SRC-0002023](../sources/history-133.md#src-0002023) 행77–93 · [SRC-0002024](../sources/history-133.md#src-0002024) 행13–25 · [SRC-0002028](../sources/history-133.md#src-0002028) JSON /complete · [SRC-0020848](../sources/history-133.md#src-0020848) JSON /goal_complete
