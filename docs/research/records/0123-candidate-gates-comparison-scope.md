# 원93 후보 판정 기준 보완과 기존 RCTL 비교의 적용 범위

**상태:** 2026-09-26 당시 기준 보완·새 후보 미추천. 30개 주장·6개 묶음의 작성 후 원문 대조 완료. 새 모델 실행0.

[출처와 판독 범위](../sources/history-123.md) · [검수](../verification/history-123.md) · [근거](../evidence/0123-candidate-gates-comparison-scope/README.md) · [직전 원92](0122-prequential-sharing-objective.md)

같은 K4에서 Tab risk가 empirical보다 나빴던 결과는 유지한다. global 비교의 모델당 자료량·update 수 차이를 모든 clustering의 불가능성으로 확대하지 않는다. 소속 변경과 입력/target 변경을 탐색의 필수 조건으로 두었던 문구를 보완하고, 미검증·기각·긍정 증거를 분리했다.

새 실험을 설계하기 전에는 [기준 보완](#claim-02), [강한 대안 비교](#claim-09), [평균 밖의 cell 반례](#claim-10), [모델당 자료량](#claim-13), [탐색 계획](#claim-25), [최종 추천 조건](#claim-26)을 먼저 읽는다. 원본 속 Goal·예산·실행 명령은 역사 자료다.

## <a id="claim-01"></a>01. 기준을 고친 감사이며 새 성능 실험은 아니다

원93(2026-09-26)은 기존 학습 코드·설정·결과·history 등 37개 근거 파일의 정합성을 감사하고 후보 진입 문구를 수정한 기록이다. 저장 결과는 새 모델 호출·새 수치 실험0, 후보 추천False, 당시 Goal 완료False로 명시한다. 기존 pilot의 29fit을 93번째 새 실험으로 세지 않는다. 이번 정리에서도 원 연구코드 실행/import와 모델 실행은0이다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[1, 3]]행, [SRC-0001731](../sources/history-123.md#src-0001731) [[88, 104]]행, [SRC-0001738](../sources/history-123.md#src-0001738) JSON 지정 필드.

## <a id="claim-02"></a>02. 탐색의 과도한 진입 조건 두 가지를 보완했다

원93은 소속이 반드시 달라져야 한다는 조건과 RCTL에 새 입력·target·모듈을 반드시 추가해야 한다는 조건을 보완했다. 연구 기여의 대상은 유용한 예측 결정 또는 그 결정을 얻는 계산·추정 과정일 수 있다. 이 수정은 새 후보를 합격시키거나 기존 실패를 지우는 조치가 아니다.

근거: [SRC-0001728](../sources/history-123.md#src-0001728) [[5, 13]]행, [SRC-0001730](../sources/history-123.md#src-0001730) [[5, 12]]행, [SRC-0001732](../sources/history-123.md#src-0001732) [[41, 57]]행.

## <a id="claim-03"></a>03. 같은 소속을 얻는 방법의 기여도 따로 확인한다

같은 유용한 소속을 더 적은 계산이나 더 작은 추정 변동으로 얻는 방법도 검토 대상이다. 같은 소속이 나왔다는 관측만으로 효율 이득이 생긴 것은 아니다. 원74·80에서는 추가 Tab 계산을 상쇄하는 그런 이득이 확인되지 않았으므로, 이 기준 변경이 두 후보의 성공을 뜻하지 않는다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[9, 9]]행, [SRC-0001730](../sources/history-123.md#src-0001730) [[54, 57]]행, [SRC-0001732](../sources/history-123.md#src-0001732) [[53, 55]]행.

## <a id="claim-04"></a>04. 함께 학습할 sample의 구성이 전달 경로다

clustering에 따라 각 RCTL이 함께 학습할 실제 sample의 묶음이 달라지는 것 자체가 학습에 영향을 주는 경로다. 새 입력·target·loss·학습 단위·모듈을 추가하는 것을 필수로 요구하지 않는다. 어느 자료를 함께 쓰면 왜 나아지는지 확인해야 한다는 조건과, RCTL 학습 결과를 clustering 결정에 쓰지 않는 당시 조건은 유지한다.

근거: [SRC-0001728](../sources/history-123.md#src-0001728) [[11, 11]]행, [SRC-0001730](../sources/history-123.md#src-0001730) [[10, 10]]행, [SRC-0001732](../sources/history-123.md#src-0001732) [[47, 47]]행.

## <a id="claim-05"></a>05. 작은 탐색과 최종 추천의 기준을 구별한다

탐색 전에는 확인할 현상·관찰 가능한 예측·강한 대안·판정 규칙·비용을 구체적으로 정한다. 그 탐색에서 알아낼 성능 차이를 이미 입증하라고 요구하지 않는다. 최종 추천에서는 핵심 원리의 직접 근거와 가까운 선행연구 대비 차이·실현 가능성·전체 비용이 필요하며, 모든 확인을 본 실험으로 미룰 수 없다.

근거: [SRC-0001728](../sources/history-123.md#src-0001728) [[13, 13]]행, [SRC-0001730](../sources/history-123.md#src-0001730) [[12, 12]]행, [SRC-0001732](../sources/history-123.md#src-0001732) [[43, 48]]행, [SRC-0001732](../sources/history-123.md#src-0001732) [[55, 55]]행.

## <a id="claim-06"></a>06. 기존 RCTL의 입력·척도·시간 분할

보존 학습 코드는 cell별 scale로 나눈 target과 같은 입력 구성을 모든 소속 조건에 사용한다. 최근8시간 sequence×9채널이며 lag24/168·24시간 평균/표준편차·달력 특징을 각 step에 반복한다. target 기준 train168–839(672시점), validation840–1007(168), test1008–1487(480)이다. MAE·Adam lr0.001/eps1e−7·batch256·최대80epoch·validation patience10을 고정했다. 코드와 설정의 정적 연결을 확인한 것이며, 이번에 원자료나 모델을 다시 실행해 검증한 것은 아니다.

근거: [SRC-0001736](../sources/history-123.md#src-0001736) [[33, 41]]행, [SRC-0001736](../sources/history-123.md#src-0001736) [[46, 70]]행, [SRC-0001736](../sources/history-123.md#src-0001736) [[84, 118]]행, [SRC-0001750](../sources/history-123.md#src-0001750) [[1, 28]]행.

## <a id="claim-07"></a>07. 두 seed의 실행 대상은 대칭이 아니다

seed20260925에는 Tab risk·empirical risk·KNN risk·PCC balanced·random balanced의 K4 각4fit과 global K1 1fit, 총21fit이 있다. seed20260926에는 Tab risk·empirical risk의 각4fit만 추가해 전체29fit이다. 따라서 저장 조건은8개이며 global·KNN·PCC·random의 두 번째 seed 결과는 미실행이다. 동일 자료·cell·기간의 seed 반복을 독립 데이터셋 두 개로 세지 않는다.

근거: [SRC-0001736](../sources/history-123.md#src-0001736) [[26, 39]]행, [SRC-0001750](../sources/history-123.md#src-0001750) [[29, 361]]행, [SRC-0001764](../sources/history-123.md#src-0001764) [[1, 9]]행.

## <a id="claim-08"></a>08. 저장된8조건의 MAE와 과거 학습 시간

| 조건 | seed | 모델 수 | mean-scaled MAE | 당시 fit 시간 합(초) |
|---|---:|---:|---:|---:|
| global | 20260925 | 1 | 0.07106777 | 269.590 |
| Tab risk | 20260925 | 4 | 0.08732813 | 177.553 |
| empirical risk | 20260925 | 4 | 0.08160040 | 196.390 |
| KNN risk | 20260925 | 4 | 0.08407308 | 202.044 |
| PCC balanced | 20260925 | 4 | 0.08987710 | 201.111 |
| random balanced | 20260925 | 4 | 0.08559771 | 199.011 |
| Tab risk | 20260926 | 4 | 0.08776006 | 224.211 |
| empirical risk | 20260926 | 4 | 0.08351629 | 182.267 |

MAE는 같은480시점·16cell의 mean-scaled 척도다. 시간은 기존 pilot의 개별 fit 기록을 합한 값이며 원93 감사 시간이나 새 속도 측정이 아니다. Tab의 소속 추정 비용까지 포함한 전체 비용표로 해석하지 않는다.

근거: [SRC-0001738](../sources/history-123.md#src-0001738) JSON 지정 필드, [SRC-0001765](../sources/history-123.md#src-0001765) JSON 지정 필드.

## <a id="claim-09"></a>09. 같은 K4의 부정 결과는 유지된다

같은16cell·입력·시간 구간·학습 정책과 모델 수를 사용한 K4 비교에서 Tab risk의 전체 MAE는 empirical보다 두 seed 모두 컸다(약7.02%,5.08%). 첫 seed의 PCC 대비 이득만 취하면 더 강한 단순 대안을 누락한다. 해당 risk-table 알고리즘을 추천하지 않은 판단은 유지하되 모든 Tab 기반 partition·다른 자료·모든 K의 실패로 확대하지 않는다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[18, 22]]행, [SRC-0001730](../sources/history-123.md#src-0001730) [[40, 40]]행, [SRC-0001738](../sources/history-123.md#src-0001738) JSON 지정 필드.

## <a id="claim-10"></a>10. 평균 악화와 모든 cell의 악화는 다르다

이번 정리의 저장 fit 산술에서는 empirical 대비 Tab의 전체기간 cell별 MAE가 첫 seed6cell, 두 번째7cell에서 작고 나머지10·9cell에서 컸다. 원93의 새로운 성능 실험이 아니다. 기존 정리 H001도 전후240시점과 cell별 이득·손해를 보존했으므로 평균 악화를 전체 cell의 악화로 요약하지 않는다. 두 seed의 일부 이득만 골라 전체 후보의 성공으로 바꾸지 않는다.

근거: [SRC-0001749](../sources/history-123.md#src-0001749) JSON 지정 필드, [SRC-0001732](../sources/history-123.md#src-0001732) [[38, 39]]행.

[기존 B2의 기간·cell·척도별 반례와 저장 산술](0004-0007-b2-observed-risk.md), [이번 저장 fit 산술](../evidence/0123-candidate-gates-comparison-scope/accounting-check.json)을 함께 사용한다.

## <a id="claim-11"></a>11. 29fit 종료와 checkpoint의 정합성

29fit은 모두 validation_patience로 종료했으며 전체 epoch 합1565, 모든 fit의 실행 epoch는80 미만이다. 원 감사는 history 길이·선택 epoch의 val_mae·fit 기록과 요약의 정합성을 검사했다. 이번에는 고정 설정의 tasks와 fit의 method/seed/cluster/members 대응도 대조하고 history의 epoch 연속성과 저장 최솟값을 기계적으로 확인했다. 이 검사는 최적 수렴이나 모든 구현의 재현 성공을 증명하지 않는다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[16, 16]]행, [SRC-0001731](../sources/history-123.md#src-0001731) [[21, 43]]행, [SRC-0001764](../sources/history-123.md#src-0001764) JSON 지정 필드, [SRC-0001749](../sources/history-123.md#src-0001749) JSON 지정 필드.

## <a id="claim-12"></a>12. 원 감사 코드의 실제 검사 범위

원 감사는 조건별 members를 펼쳐0–15가 정확히 한 번씩 나타나는지, 모델 수와 모델당 cell 수, cell 수로 가중한 fit MAE와 summary MAE의 차이가1e−7 미만인지 검사한다. 선택된 epoch의 val_mae가 best_val_mae와 같은지도 확인한다. 이런 기록 정합성 검사를 원자료의 모든 누출 가능성·모든 최적화 경로·통계적 인과의 전체 감사로 바꾸지 않는다.

근거: [SRC-0001731](../sources/history-123.md#src-0001731) [[35, 55]]행, [SRC-0001736](../sources/history-123.md#src-0001736) [[109, 133]]행.

## <a id="claim-13"></a>13. 모델당 자료량과 epoch당 update 수

유효 train target672개를 각 cell에 적용하므로 global의 모델당 train 행은16×672=10,752, K4 각 모델은4×672=2,688이다. batch256의 끝 batch도 쓰는 보존 loop에서 update/epoch는 ceil(10,752/256)=42와 ceil(2,688/256)=11이다. global과 K4는 모델 수·모델당 자료량·update 수가 달라 동일 모델 수·동일 update 대조가 아니다. global은 강한 실용적 기준으로 유지하되 이 비교만으로 모든 clustering을 기각할 수 없다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[19, 24]]행, [SRC-0001731](../sources/history-123.md#src-0001731) [[45, 65]]행, [SRC-0001736](../sources/history-123.md#src-0001736) [[84, 106]]행.

## <a id="claim-14"></a>14. 기록된 epoch에서 계산한 update 회수

| 조건 | seed | 실행 update 합 | 선택 checkpoint까지의 update 합 |
|---|---:|---:|---:|
| global | 20260925 | 1890 | 1470 |
| Tab risk K4 | 20260925 | 2431 | 1991 |
| empirical risk K4 | 20260925 | 2453 | 2013 |
| KNN risk K4 | 20260925 | 2255 | 1815 |
| PCC balanced K4 | 20260925 | 2321 | 1881 |
| random balanced K4 | 20260925 | 2299 | 1859 |
| Tab risk K4 | 20260926 | 2585 | 2145 |
| empirical risk K4 | 20260926 | 2376 | 1936 |

각 fit의 update/epoch에 epochs_run 또는 best_epoch를 곱해 합했다. 전체8조건의 합은18,610/15,110이다. K4의 합은 서로 다른 네 모델의 합이며 한 모델이 그만큼 학습했다는 뜻이 아니다. 선택 checkpoint까지의 값은 새로 수행한 학습이 아니라 저장 epoch의 정수 계산이다.

근거: [SRC-0001731](../sources/history-123.md#src-0001731) [[57, 75]]행, [SRC-0001738](../sources/history-123.md#src-0001738) JSON 지정 필드.

## <a id="claim-15"></a>15. 같은 early stopping은 같은 학습 경로가 아니다

같은 patience 정책은 같은 실행 epoch·update 수·최적화 경로를 보장하지 않는다. 첫 seed에서 empirical의 update 합은 Tab보다22회 많지만, 두 번째에서는209회 적으면서 MAE도 작다. 따라서 empirical에 항상 더 많은 학습을 주었기 때문에 결과가 좋았다는 설명으로 기존 부정 결과를 무효화할 근거는 없다. 차이의 원인을 인과적으로 확정한 분석도 아니다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[24, 34]]행, [SRC-0001738](../sources/history-123.md#src-0001738) JSON 지정 필드.

## <a id="claim-16"></a>16. 과거 fit 시간은 전체 소속 추정 비용과 다르다

첫 seed에서는 empirical의 fit 시간이 Tab보다 길고(196.390 vs177.553초), 두 번째에서는 더 짧다(182.267 vs224.211초). 과거 전체 pilot의 wall은1658.139초다. 이런 시간 기록을 새로 측정한 계산 효율이나 Tab clustering의 추가 비용을 상쇄한 증거로 해석하지 않는다. 같은 소속을 더 효율적으로 얻는 새 후보라면 필요한 전체 단계의 비용을 별도로 직접 확인해야 한다.

근거: [SRC-0001738](../sources/history-123.md#src-0001738) JSON 지정 필드, [SRC-0001764](../sources/history-123.md#src-0001764) JSON 지정 필드, [SRC-0001730](../sources/history-123.md#src-0001730) [[54, 57]]행.

## <a id="claim-17"></a>17. 저장 기록 산술과 모델 재현을 구별한다

이번 검수는 저장된8조건과29fit의 MAE·cell 수·epoch·batch loop를 대조해 정수 update와 가중 평균을 다시 계산했다. history는 선택 epoch의 epoch/val_mae 필드를 실제 읽고 길이·연속성·최솟값을 기계 검사했으며 전체 epoch 본문의 새 전문 판독으로 세지 않는다. 과거 예측을 다시 만들거나 모델을 다시 학습한 독립 재현은 아니다.

근거: [SRC-0001731](../sources/history-123.md#src-0001731) [[35, 76]]행, [SRC-0001749](../sources/history-123.md#src-0001749) JSON 지정 필드, [SRC-0001738](../sources/history-123.md#src-0001738) 판본·해시·판독 범위.

## <a id="claim-18"></a>18. 37개 해시 일치는 실행 시점이나 인과를 증명하지 않는다

원 감사의 verified_evidence_hashes37개는 설정/fit/summary/finished4개, 코드2개, history29개, 원74·80 결과2개다. 예산 원장은 별도 동일 해시 검사다. 이번에 스냅샷의 해당 바이트와 설정에 기록된 코드 해시의 대응을 확인했다. 같은 바이트와 기록의 연결 증거이며 실제 실행 시점·모든 외부 의존성·예측값의 독립 재현까지 증명하지 않는다.

근거: [SRC-0001731](../sources/history-123.md#src-0001731) [[15, 32]]행, [SRC-0001731](../sources/history-123.md#src-0001731) [[78, 99]]행, [SRC-0001738](../sources/history-123.md#src-0001738) JSON 지정 필드, [SRC-0001727](../sources/history-123.md#src-0001727) 판본·해시·판독 범위.

## <a id="claim-19"></a>19. 원74의 직접 예측 이득과 압축 판정

원74의 저장 teacher MSE는 Tab0.00957982, HGB0.01192481, Ridge0.01435985로 Tab의 직접 예측 이득을 유지한다. 하지만 해당 출력 압축은 실제 target HGB를 다뤘고 최종 RCTL을 학습/검증하지 않았다(RCTL_validated=False, independent_test=False). 압축 후보의 실패를 Tab 직접 예측의 실패로 바꾸거나 새 partition의 최종 RCTL 결과로 읽지 않는다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[41, 41]]행, [SRC-0001740](../sources/history-123.md#src-0001740) JSON 지정 필드.

[원74 출력 압축의 기존 상세 검수](0072-0075-output-compression.md).

## <a id="claim-20"></a>20. 원80의 같은 소속과 고정 gradient 진단

원80의 input_only/raw_joint/TabICL/Ridge/HGB는 저장 ARI_vs_TabICL이 모두1이다. teacher query MSE는 Tab0.01304348, Ridge0.01583903, HGB0.01586167로 Tab이 작다. 그러나 final_RCTL_performance_validated·weights_or_buffers_updated·clustering_uses_RCTL·independent_test는 모두False다. 고정 RCTL gradient를 살핀 범위이며 해당 소속의 전체 RCTL 학습·최종 예측 성능을 확인한 것이 아니다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[42, 42]]행, [SRC-0001739](../sources/history-123.md#src-0001739) JSON 지정 필드.

[원80 조건부 graph의 기존 상세 검수](0088-conditional-graph-diagnostic.md).

## <a id="claim-21"></a>21. 좋은 직접 예측을 소속 개선과 동일시하지 않는다

원74·80의 Tab 직접 예측 이득은 보존하지만, 이번 기준 보완으로 유용한 다른 소속이나 계산·추정 효율의 개선이 새로 입증되지는 않았다. 두 결과의 teacher MSE와 기존 최종 RCTL의 mean-scaled MAE는 자료·모델·목적이 다른 지표이므로 하나의 성능 순위에 섞지 않는다. 이미 확인한 구간은 후속 연구에서 개발자료로 유지한다.

근거: [SRC-0001728](../sources/history-123.md#src-0001728) [[21, 27]]행, [SRC-0001732](../sources/history-123.md#src-0001732) [[35, 39]]행, [SRC-0001732](../sources/history-123.md#src-0001732) [[48, 57]]행, [SRC-0001738](../sources/history-123.md#src-0001738) JSON 지정 필드.

## <a id="claim-22"></a>22. 문헌·기호 검토의 미추천은 실험 실패와 다르다

원93의 분류는 원86의 초기화 복사/고정 표현/지속 공유, 원89의 group 정보 추가와 별도 모델 분할, 원91의 공통 permutation과 cell별 의미 대응, 원92의 잡음 분포와 점 예측 함수 차이를 각각 구분한다. 이 제한된 이론·설계 판단을 모든 공유/정렬/순차 방법의 실험 실패로 묶지 않는다. 이번에는 원93의 그 분류를 검수했으며 연결 문헌 전체를 새로 독립 판독했다고 주장하지 않는다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[43, 48]]행, [SRC-0001732](../sources/history-123.md#src-0001732) [[54, 54]]행.

## <a id="claim-23"></a>23. train/validation gap만으로 원인을 확정하지 않는다

원93은 원34의 저장 checkpoint 진단에서 train 오차 감소와 validation 악화가 함께 관찰된 사실을 인용해 학습·일반화의 절충을 살펴야 한다고 적었다. 과적합 하나가 원인이라고 확정하거나 공유 모듈을 붙이면 해결된다고 단정하지 않았다. 이 항목은 원93의 인용/해석 범위를 검수한 것이며 원34의 checkpoint 진단을 이번에 새로 실행한 결과가 아니다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[22, 22]]행, [SRC-0001737](../sources/history-123.md#src-0001737) [[27, 28]]행.

## <a id="claim-24"></a>24. global 표현 가능성과 유한 학습의 우열

group 정보를 넣은 global 모델로 표현할 수 있다는 주장은 실제 유한 자료·최적화에서 분할의 이득이 없다는 증명이 아니다. 동시에 그 가능성만으로 미검증 분할 후보를 유망하다고 승격하지 않는다. 예측 기여라면 실제 함께 학습할 sample 구성이 강한 단순 대안이 놓치는 어떤 상황을 개선하는지 직접 확인해야 한다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[44, 48]]행, [SRC-0001730](../sources/history-123.md#src-0001730) [[52, 59]]행, [SRC-0001732](../sources/history-123.md#src-0001732) [[54, 55]]행.

## <a id="claim-25"></a>25. 탐색 계획에서 적을 네 가지

당시 수정된 후보 색인은 ①Tab을 넣기 전부터 있는 중요한 문제와 바꿀 결정/효율, ②Tab 계산의 기여·강한 대안·관찰 가능한 예측, ③실제 sample 묶음을 포함한 RCTL 전달 경로와 RCTL 결과의 clustering 독립성, ④누적 비용 안의 구체적인 비교·판정 규칙을 먼저 작성하도록 한다. 과거 계획은 보존 자료이며 현재 정리 작업에 새 모델 실행을 허용하는 명령이 아니다.

근거: [SRC-0001732](../sources/history-123.md#src-0001732) [[41, 48]]행, [SRC-0001729](../sources/history-123.md#src-0001729) [[9, 15]]행.

## <a id="claim-26"></a>26. 실패를 빠르게 계산하는 것만으로 추천하지 않는다

최종 추천에는 문제·선행연구 대비 차이·강한 대안 대비 개선 원리·Tab의 기여·RCTL 전달 경로·직접 확인·전체 비용을 연결한다. 같은 유용한 결정을 더 효율적으로 얻는다면 그 효율 이득을 직접 보여야 한다. 기존에 실패한 B2를 빠르게 구현하거나 같은 결과를 더 비싸게 얻은 원74·80에 이름을 바꾸는 것만으로 다시 채택하지 않는다.

근거: [SRC-0001730](../sources/history-123.md#src-0001730) [[54, 59]]행, [SRC-0001732](../sources/history-123.md#src-0001732) [[52, 57]]행.

## <a id="claim-27"></a>27. snapshot35와 별도 검증 기록

snapshot35 manifest는46개 파일578,394bytes를 열거한다. manifest 자체9,947bytes를 포함한 물리 스냅샷은47파일588,341bytes이고 별도 원93 archive 검증 JSON은212bytes다. 이번 선택의 새10고유 자료는14핵심 별칭+2후속 별칭, 기존38자료는145물리 별칭으로 연결했고 이전 판본 기준2개/2별칭도 별도로 대조했다. 해시·사본 수를 연구 시도나 새 독해 수로 세지 않는다.

근거: [SRC-0001727](../sources/history-123.md#src-0001727) 판본·해시·판독 범위, [SRC-0022088](../sources/history-123.md#src-0022088) 판본·해시·판독 범위.

## <a id="claim-28"></a>28. 후보 색인과 연혁의 버전 차이

후보 색인은 직전50행에서57행이 되었고41·43·45–48·50–57행에 진입/추천 기준 수정이 있다. 현재57행 전체와 직전40–50행을 직접 읽었다. 연혁은508→517행이며 직전7행을 새7–16행으로 바꾸고 나머지 대응 부분은 기계 비교상 같다. 현재 연혁은1–36행만 직접 읽어37–517행을 미독으로 남긴다. 직전 연혁은 이전 H122의1–65행 판독을 재사용하며66–508행의 직접 미독을 유지한다. 기계적 동일성을 전문 독해로 바꾸지 않는다.

근거: [SRC-0001732](../sources/history-123.md#src-0001732) [[41, 57]]행, [SRC-0001704](../sources/history-123.md#src-0001704) [[40, 50]]행, [SRC-0001734](../sources/history-123.md#src-0001734) [[1, 36]]행, [SRC-0001708](../sources/history-123.md#src-0001708) [[1, 25]]행, [SRC-0001734](../sources/history-123.md#src-0001734) 판본·해시·판독 범위.

## <a id="claim-29"></a>29. 이번 묶음의 판독과 재사용 범위

핵심8자료1019행과 추가/재사용 구간을 합해 실제 raw1729행을 읽었고, compact fit JSON29항목의 모든 필드는 별도로 읽었다. 29history는 선택 epoch/val_mae와 기계 검사를 구분하고 summary·원74·80은 지정 필드만 재참조했다. 새10고유 자료의 집계 후보는 본문6·전체JSON3·부분연혁1이다. 이전40자료·별칭·재독·기계 검사는 중복 가산0이며 작성 후 검수와 저장 확인을 마칠 때만 단회 집계한다.

근거: [SRC-0001727](../sources/history-123.md#src-0001727) 판본·해시·판독 범위, [SRC-0001734](../sources/history-123.md#src-0001734) 판본·해시·판독 범위, [SRC-0001749](../sources/history-123.md#src-0001749) 판본·해시·판독 범위.

## <a id="claim-30"></a>30. 당시 보류와 전체 정리의 남은 범위

원93은 최종 추천 방향과 Word를 미완료로 남겼다. 당시 예산 원장은 변하지 않았고 추가 RCTL fit0·Tab 잔여11context/20,640행이라는 과거 상태를 기록했다. 이 예산·Goal 문구는 역사 자료다. 현재 아카이브도 연혁의 미독 구간, 원94 이후/이전 고유 판본, FedPPBC·DOCX 공백, 전체 실패·비용 통합, 장기 팀 접근, 최종 원본 변경분과 대표 질문 검색 검수가 남아 있어 전체 Goal 미완료다.

근거: [SRC-0001728](../sources/history-123.md#src-0001728) [[25, 29]]행, [SRC-0001730](../sources/history-123.md#src-0001730) [[59, 59]]행, [SRC-0001734](../sources/history-123.md#src-0001734) [[9, 14]]행, [SRC-0001738](../sources/history-123.md#src-0001738) JSON 지정 필드.

## 팀 재검토 안내

기존 소속을 반복 실행하기 전에는 해결할 문제가 같은지, 새 후보가 바꾸는 sample 구성 또는 비용/추정 과정을 구체적으로 적는다. 실험으로 불리했던 조건과 미검증 설계를 구분하고, 강한 empirical/global 기준·cell별 손해·전체 비용·독립 기간을 함께 검토한다.

현재 연혁37–517행·직전66–508행의 직접 미독, 원94 이후와 이전 고유 판본, 원83 FedPPBC·원84 DOCX 판독 공백, 전체 문헌·실패·비용 통합, 장기 팀 접근, 최종 원본 변경분과 대표 질문 검색 검수.
