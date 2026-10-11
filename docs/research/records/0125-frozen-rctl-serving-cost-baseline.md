# 원95 저장 RCTL의 실제 호출 비용과 기본 batch 비교

**상태:** 2026-09-26 보존 모델의 CPU frozen inference 측정. 이번 정리는 저장 결과 검산·32주장/6묶음의 원문 대조이며 새 모델 실행0이다.

[출처·판독 범위](../sources/history-125.md) · [검수](../verification/history-125.md) · [근거와 저장 배열](../evidence/0125-frozen-rctl-serving-cost-baseline/README.md) · [비교 조건](../references/serving-cost-baseline.md) · [원93 조건 감사](0123-candidate-gates-comparison-scope.md)

같은 가중치를 사용하는 cell을 한 번에 처리하면 호출 overhead가 줄었다. 이를 Tab의 연구 기여로 세지 않는다. K1과K4 모두 시점당16행을 예측했고, 모델 저장량·호출 수·실제 시간을 별도로 기록했다. 기존 B2 판정과 새 정확도 실험을 구별한다. 입력 전처리·정규화는 보존 design_data와 원93 조건 감사의 재사용 범위이며 이번 측정에서 새로 학습하지 않았다. 원95는 실제 달력시각 대신840..1007의 기존 개발 시각 번호를 제시한다.

새 비용 실험 전에는 [측정 범위](#claim-07), [중앙값·분위수](#claim-08), [행과 모델 수](#claim-16), [warm-up·비용 포함 관계](#claim-17), [Tab 준비비용](#claim-24), [다시 검토할 조건](#claim-27)을 확인한다. 원문 코드·Goal·예산·명령은 역사 자료다.

## <a id="claim-01"></a>01. 저장 모델의 실제 CPU 비용을 확인한 역사 기록

원95(2026-09-26)는 고정한 계획에 따라 보존된 RCTL을 실행한 CPU 비용 측정이다. 새 RCTL 학습, TabICLv2 호출, 소속 선택, optimizer·gradient 갱신은 없었다. 당시 frozen inference 실행과 이번 저장 배열·원장 검산을 구별한다. 이번 정리에서는 모델과 원 연구 코드를 실행하거나 import하지 않았다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[1, 20]]행, [SRC-0001802](../sources/history-125.md#src-0001802) [[1, 38]]행, [SRC-0001816](../sources/history-125.md#src-0001816) [[1, 15]]행.

## <a id="claim-02"></a>02. seed 하나의 1+4+4 checkpoint 비교

기존 seed20260925의 global 1개, tabicl_risk 4개, empirical_risk 4개를 사용했다. 같은 RCTL 구조의 총9개 checkpoint이며 빠른 timing 결과를 보고 새 모델·소속을 선택한 것이 아니다. prepared의 members는16개 cell 목록의 위치0–15다. 이 위치 번호와 실제 cell ID를 구별한다.

근거: [SRC-0001802](../sources/history-125.md#src-0001802) [[11, 16]]행, [SRC-0001815](../sources/history-125.md#src-0001815) [[1, 184]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[41, 45]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[79, 117]]행.

## <a id="claim-03"></a>03. 개발 구간의12시점과 독립 검증의 구별

기존16개 cell의 개발 구간840..1007에서 linspace(840,1007,12,dtype=int)로840/855/870/885/900/915/931/946/961/976/991/1007을 정했다. 이미 관찰한 구간이며 새로운 미래 구간이나 독립 정확도 평가가 아니다. 저장 origins와 준비 기록이 일치했다.

근거: [SRC-0001802](../sources/history-125.md#src-0001802) [[13, 17]]행, [SRC-0001818](../sources/history-125.md#src-0001818) [[7, 21]]행, [SRC-0001801](../sources/history-125.md#src-0001801) [[11, 20]]행, [SRC-0001814](../sources/history-125.md#src-0001814) 해시·판본·저장검사 범위.

## <a id="claim-04"></a>04. 8×9 입력과 고정 평가 모드의 CPU 설정

각 cell의 입력은 float32의8×9 배열이다. 준비 코드에서는 flat의8개 lag를 첫 채널에 넣고 나머지8개 feature를8step에 반복했다. Torch CPU4 intra-op/2 inter-op threads, eval()·requires_grad_(False)·inference_mode를 사용했다. 기존 convolution/LSTM/선형층 및 BatchNorm/Dropout의 Torch port이며 GPU·compile·quantization·hidden-state 변경을 시험하지 않았다.

근거: [SRC-0001808](../sources/history-125.md#src-0001808) [[1, 15]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[83, 111]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[139, 158]]행, [SRC-0001818](../sources/history-125.md#src-0001818) [[22, 54]]행, [SRC-0001806](../sources/history-125.md#src-0001806) [[11, 60]]행.

## <a id="claim-05"></a>05. 같은 시각의 행을 묶은6개 실행 경로

각 방법에서 cell별 호출과 같은 가중치의 묶음 호출을 비교해 총6경로를 실행했다. 시점당16개 cell을 개별 처리하면 모두16번 호출한다. 묶음 경로는 global 16행1번, K4는4행씩4번 호출한다. 서로 다른 미래 시각의 입력을 기다려 batch를 키운 대기시간 이득으로 해석하지 않는다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[13, 20]]행, [SRC-0001802](../sources/history-125.md#src-0001802) [[13, 17]]행, [SRC-0001815](../sources/history-125.md#src-0001815) [[185, 200]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[113, 137]]행.

## <a id="claim-06"></a>06. warm-up2회와 경로별36개 timing

각 경로는 앞의2시점으로2회 warm-up한 뒤12시점×3반복의36개 timing을 남겼다. 반복·시점마다6경로의 순서를 순환시켜 항상 같은 경로부터 실행하지 않았다. 한 기기의 작은 반복 측정이며 독립 표본36개에 대한 신뢰구간이나 무작위 설계 검정으로 부르지 않는다.

근거: [SRC-0001802](../sources/history-125.md#src-0001802) [[19, 23]]행, [SRC-0001801](../sources/history-125.md#src-0001801) [[24, 34]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[160, 170]]행, [SRC-0001818](../sources/history-125.md#src-0001818) [[22, 27]]행.

## <a id="claim-07"></a>07. 입력 준비 뒤 실행과 결과 수집의 시간

시점별 timing은 입력 tensor와 route package를 준비한 뒤 모델 호출, numpy 결과 변환, 원래 cell 순서로 모으는 시간을 잰 것이다. Python 루프와 호출별 카운터·상한 검사도 포함하므로 순수 FLOP 측정이 아니다. 입력 준비·checkpoint 로딩·전처리·프로세스 시작을 포함한 온라인 전체 지연으로 표시하지 않는다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[20, 24]]행, [SRC-0001802](../sources/history-125.md#src-0001802) [[16, 25]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[119, 158]]행.

## <a id="claim-08"></a>08. 저장 배열에서 대조한6경로 중앙값

cell별→묶음 median은 global33.186→3.493ms, Tab risk K4 33.865→14.005ms, empirical risk K4 34.038→14.152ms다. 시점당16개 cell 모두를 처리한 값이며 학습 비용은 포함하지 않는다. timing_seconds(6,3,12)에서6경로의 median을 재계산해 summary와 절대 허용오차1e-12seconds 이내 일치를 확인했다. 새 실행시간 측정은 아니다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[22, 32]]행, [SRC-0001819](../sources/history-125.md#src-0001819) [[57, 153]]행, [SRC-0001814](../sources/history-125.md#src-0001814) 해시·판본·저장검사 범위.

## <a id="claim-09"></a>09. P10–P90와 반복별 median의 범위

묶음 경로의 P10–P90은 global3.337–5.506ms, Tab K4 12.236–15.399ms, empirical K4 12.614–14.757ms다. 저장된 반복별 median도 같은 배열의 재계산과 일치했다. 이 분위수는36개 timing의 관측 요약이며 미래 서비스 latency의 신뢰구간이나 방법 간 유의성 검정이 아니다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[24, 32]]행, [SRC-0001819](../sources/history-125.md#src-0001819) [[74, 153]]행, [SRC-0001814](../sources/history-125.md#src-0001814) 해시·판본·저장검사 범위.

## <a id="claim-10"></a>10. 동일 방법에서 호출 구현을 바꾼 시간비

동일 방법의 cell별/묶음 median 시간비는 global9.501, Tab K4 2.418, empirical K4 2.405다. 같은 checkpoint의 호출 구현을 바꾼 비교이며 Tab clustering의 정확도 기여나 다른 알고리즘 대비 신규성으로 세지 않는다. 각 방법의 두 경로는 같은 시점·입력·가중치를 사용했다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[7, 9]]행, [SRC-0001801](../sources/history-125.md#src-0001801) [[26, 34]]행, [SRC-0001819](../sources/history-125.md#src-0001819) [[155, 170]]행, [SRC-0001814](../sources/history-125.md#src-0001814) 해시·판본·저장검사 범위.

## <a id="claim-11"></a>11. 사전 허용치 안의 동일 방법 예측 차이

cell별/묶음의 최대 절대 예측 차이는 global7.1525574e-7, Tab1.1920929e-6, empirical1.0728836e-6으로 사전2e-5 이내였다. 저장 prediction(6,3,12,16)으로 이 차이를 재계산했다. 서로 다른 세 방법의 예측이 같거나 정확도가 개선됐다는 뜻이 아니며2e-5는 연구 효과의 합격선이 아니다.

근거: [SRC-0001802](../sources/history-125.md#src-0001802) [[21, 25]]행, [SRC-0001801](../sources/history-125.md#src-0001801) [[34, 34]]행, [SRC-0001819](../sources/history-125.md#src-0001819) [[155, 170]]행, [SRC-0001814](../sources/history-125.md#src-0001814) 해시·판본·저장검사 범위.

## <a id="claim-12"></a>12. 상태 불변의 당시 보고와 현재 hash 확인

원 실행은 가중치·모든 buffer·입력·checkpoint가 전후 같았다고 보고했다. 코드는 state_dict tensor hash와 원 파일 hash를 다시 검사한 뒤 성공 summary를 저장한다. 현재 입력10개와 원 RCTL 코드의 raw SHA를 대조했지만 당시 RAM 상태나 예측 호출을 재연하지 않았다. 당시 상태 불변 보고를 현재 독립 실행 검증으로 바꾸지 않는다.

근거: [SRC-0001808](../sources/history-125.md#src-0001808) [[26, 31]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[179, 204]]행, [SRC-0001819](../sources/history-125.md#src-0001819) [[330, 343]]행, [SRC-0001820](../sources/history-125.md#src-0001820) [[1, 56]]행, [SRC-0001806](../sources/history-125.md#src-0001806) 해시·판본·저장검사 범위.

## <a id="claim-13"></a>13. parameter·buffer와 상태 tensor 저장량

prepared는 모델당174433개 parameter,697732parameter bytes,3680buffer bytes,701412state tensor bytes를 기록했다. 현재9개 .pt의 ZIP data storage entry 크기 합도 각각701412bytes로 대조했다. pickle을 역직렬화하거나 tensor 값·trainable parameter를 새 모델로 재구성하지 않았다.

근거: [SRC-0001815](../sources/history-125.md#src-0001815) [[50, 55]]행, [SRC-0001815](../sources/history-125.md#src-0001815) [[66, 183]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[106, 112]]행, [SRC-0001820](../sources/history-125.md#src-0001820) 해시·판본·저장검사 범위.

## <a id="claim-14"></a>14. K1/K4의 상태와 checkpoint 파일 저장량

global K1의 state tensor는701412bytes, K4는2805648bytes다. checkpoint 파일 합은745123bytes와2980492bytes다. 같은 구조4개이므로 각각4배이며 tensor 저장량과 파일 형식 overhead를 구분한다. 이를 라이브러리와 입출력 buffer까지 포함한 프로세스 전체 메모리비로 확대하지 않는다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[36, 47]]행, [SRC-0001819](../sources/history-125.md#src-0001819) [[57, 153]]행, [SRC-0001815](../sources/history-125.md#src-0001815) [[28, 184]]행, [SRC-0001820](../sources/history-125.md#src-0001820) 해시·판본·저장검사 범위.

## <a id="claim-15"></a>15. 9모델을 함께 올린 프로세스의 sampled RSS

sampled_max_rss는233689088bytes이며9모델과 Torch runtime이 함께 있는 프로세스의 값이다. bounds()에서 확인한 표본 시점의 최대치이므로 완전한 연속 메모리 추적이나 방법별 독립 peak가 아니다. K1/K4 전체 메모리4배 또는 대규모 서비스의 메모리 예측에 사용하지 않는다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[42, 47]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[66, 77]]행, [SRC-0001816](../sources/history-125.md#src-0001816) [[5, 12]]행.

## <a id="claim-16"></a>16. 모델 수를 줄여도 시점당16행은 처리한다

global과 K4는 모두 시점당16개8×9 입력 행을 처리한다. 묶음 호출은 호출 overhead와 라이브러리·하드웨어의 처리 효율을 바꾸지만 여러 cell을 하나의 대표 예측으로 치환하지 않았다. convolution/LSTM/선형층의 행별 계산을 생략했다고 주장하지 않으며 모델 수·호출 수·예측 행 수를 별도로 적는다.

근거: [SRC-0001800](../sources/history-125.md#src-0001800) [[15, 19]]행, [SRC-0001801](../sources/history-125.md#src-0001801) [[36, 52]]행, [SRC-0001815](../sources/history-125.md#src-0001815) [[185, 200]]행, [SRC-0001806](../sources/history-125.md#src-0001806) [[49, 60]]행.

## <a id="claim-17"></a>17. 전체 호출과 저장된 측정 구간의 차이

warm-up 포함 총2166forward/3648예측행은 (16+1+16+4+16+4)×(2+12×3) 및6×16×(2+12×3)와 일치한다. NPZ에는 측정 구간의216개 timing과3456개 예측값만 저장됐다. timed 구간은2052forward/3456행, warm-up은114forward/192행이다. 저장 배열을 전체3648행의 literal 결과로 표시하지 않는다.

근거: [SRC-0001808](../sources/history-125.md#src-0001808) [[160, 187]]행, [SRC-0001816](../sources/history-125.md#src-0001816) [[5, 14]]행, [SRC-0001815](../sources/history-125.md#src-0001815) [[191, 199]]행, [SRC-0001814](../sources/history-125.md#src-0001814) 해시·판본·저장검사 범위.

## <a id="claim-18"></a>18. warm-up이 포함된 내부 timing 합

저장 timing 배열 합은4.816830499985372seconds이고 counters.timed_route_seconds는5.10660659999121seconds다. 차이0.2897761000058381seconds는 warm-up 호출도 같은 evaluate() 카운터에 더한 코드와 일치한다. 내부 합은 최종stage5.4455786000035005seconds에 포함되므로 stage와 더해 비용을 이중 계산하지 않는다.

근거: [SRC-0001808](../sources/history-125.md#src-0001808) [[139, 170]]행, [SRC-0001816](../sources/history-125.md#src-0001816) [[4, 11]]행, [SRC-0001813](../sources/history-125.md#src-0001813) [[2, 15]]행, [SRC-0001814](../sources/history-125.md#src-0001814) 해시·판본·저장검사 범위.

## <a id="claim-19"></a>19. summary와 finally 종료 시계의 차이

summary.wall_seconds는5.444760700003826seconds, finally의 run_finished와 원장 stage는5.4455786000035005seconds다. summary의 시계는 summary 저장·출력과 finally보다 앞에서 읽으며 차이는0.0008178999996744seconds다. 최종stage 비용은 run_finished/budget_update를 사용한다. 두 값을 별도 실행 두 번으로 세거나 임의로 같은 값으로 덮어쓰지 않는다.

근거: [SRC-0001819](../sources/history-125.md#src-0001819) [[330, 343]]행, [SRC-0001816](../sources/history-125.md#src-0001816) [[1, 15]]행, [SRC-0001808](../sources/history-125.md#src-0001808) [[200, 211]]행, [SRC-0001813](../sources/history-125.md#src-0001813) [[2, 19]]행.

## <a id="claim-20"></a>20. 원장 입력과 before 사본의 줄바꿈 차이

원장 입력 SHA는f3e370ba0bb39b220a3448daf00ab532729b91b93bce80b6d92a43a7ea71f2a9(7651bytes), budget_before 사본은f60705e1cecd539871c8fdb019d27a25adf007efa7a1ee534f0428802f9b8dfb(7894bytes)다. 두 JSON객체가 같으며 사본의243개CRLF를LF로 바꾸면 전체 바이트가 일치한다. 두 raw 판본과 형식 차이를 보존하며 비용·과학적 내용 변화나 손상으로 해석하지 않는다.

근거: [SRC-0001808](../sources/history-125.md#src-0001808) [[36, 65]]행, [SRC-0001813](../sources/history-125.md#src-0001813) [[17, 18]]행, [SRC-0001812](../sources/history-125.md#src-0001812) [[1, 244]]행, [SRC-0001780](../sources/history-125.md#src-0001780) 해시·판본·저장검사 범위.

## <a id="claim-21"></a>21. after 원장과 budget_after의 같은 바이트

원95 이후 원장 SHA는ad8926ba4ef3517043ce8ddc82afe981307352f7c52fc7c1fd251869a2e5e9b7이다. 보존 cumulative_execution_budget와 budget_after는 같은 바이트이므로 서로 다른 실행 결과로 중복 세지 않는다. before의f60705…와 입력f3e370…는 다른 raw 판본으로 출처를 유지한다.

근거: [SRC-0001799](../sources/history-125.md#src-0001799) [[25, 58]]행, [SRC-0001813](../sources/history-125.md#src-0001813) [[17, 26]]행, [SRC-0001804](../sources/history-125.md#src-0001804) [[1, 259]]행, [SRC-0001804](../sources/history-125.md#src-0001804) 해시·판본·저장검사 범위.

## <a id="claim-22"></a>22. 한 번 추가한 비용과 기록된 누적시간

after 원장은 serving_cost_95 항목을 한 번 추가하고 RCTL_frozen_inference_seconds를 최종stage5.4455786000035005seconds만큼 늘렸다. 기존 항목·fit/context·caps는 그대로다. 같은 계산식의 기록된 modeling은1992.615061800001→1998.0606404000046seconds다. 초기 전처리와 일부 과거시간이 따로 기록되지 않았으므로 완전한 전체 연구시간으로 부르지 않는다.

근거: [SRC-0001807](../sources/history-125.md#src-0001807) [[18, 41]]행, [SRC-0001813](../sources/history-125.md#src-0001813) [[2, 26]]행, [SRC-0001812](../sources/history-125.md#src-0001812) [[68, 125]]행, [SRC-0001804](../sources/history-125.md#src-0001804) [[68, 163]]행.

## <a id="claim-23"></a>23. 역사적 예산과 현재 실행 범위

원95 이후에도 누적Tab69context/39360query행·RCTL29fit/1565epoch, 잔여Tab11context/20640행·추가RCTLfit0이라는 당시 원장 상태가 유지됐다. 원문 Goal·AGENTS·상한·다음 행동은 역사자료다. 현재 정리 작업의 모델 실행 허가로 사용하지 않으며 모델 실행·원장 수정·새 연구 Goal 재개는0이다.

근거: [SRC-0001804](../sources/history-125.md#src-0001804) [[68, 92]]행, [SRC-0001813](../sources/history-125.md#src-0001813) [[20, 26]]행, [SRC-0001802](../sources/history-125.md#src-0001802) [[34, 38]]행, [SRC-0001805](../sources/history-125.md#src-0001805) [[3, 14]]행.

## <a id="claim-24"></a>24. 실행시간 표 밖에 있는 Tab 준비 비용

이번 timing은 준비된 partition과 checkpoint를 사용했고 Tab context/query 호출은0이다. 이 표로 새로운 Tab 소속 결정의 사전 계산 비용까지 절약됐다고 주장할 수 없다. 후속 설계에서는 cluster 수·실제 입력 행·호출/batch·실측시간·가중치 저장·Tab context/query 준비 비용을 따로 적고 전체 비교 범위를 정해야 한다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[47, 67]]행, [SRC-0001800](../sources/history-125.md#src-0001800) [[21, 28]]행, [SRC-0001802](../sources/history-125.md#src-0001802) [[27, 38]]행, [SRC-0001818](../sources/history-125.md#src-0001818) [[32, 44]]행.

## <a id="claim-25"></a>25. 같은 K4의 작은 차이와 Tab 속도 우위

empirical K4−Tab K4 묶음 median 차이는 약0.147ms다. 구조·모델 수·행 수·호출 수가 같고 작은 timing만 확인했다. 이 차이는 Tab clustering의 유의미한 속도 우위나 정확도 개선의 근거가 아니다. 이번에 유의성 검정이나 반복 실행을 추가하지 않았다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[54, 58]]행, [SRC-0001819](../sources/history-125.md#src-0001819) [[106, 153]]행, [SRC-0001814](../sources/history-125.md#src-0001814) 해시·판본·저장검사 범위.

## <a id="claim-26"></a>26. 기존 B2 판단과 새 정확도 실험의 구별

원95는 기존 B2의 같은K 조건에서 불리했던 RCTL 성능 판정을 바꾸지 않았다. 이전 checkpoint 평가에서 global 평균오차가 작았다는 보고를 참조했지만 이 timing은 새 기간의 오차 재검증이 아니다. 현재 방법에 별도 계산 이점이 확보되지 않았다는 판단을 모든 partition·학습 공유의 불가능성으로 넓히지 않는다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[7, 9]]행, [SRC-0001801](../sources/history-125.md#src-0001801) [[54, 62]]행, [SRC-0001803](../sources/history-125.md#src-0001803) [[51, 58]]행.

## <a id="claim-27"></a>27. 기본 batch 구현과 연구 신규성의 구별

당시 향후 비교의 기본 구현은 같은 가중치를 사용하는 동시 cell을 batch로 처리하는 것으로 확정했다. 느린 cell별 호출을 개선한 효과를 Tab의 신규성으로 설명하지 않는다. 이 baseline에서도 실제로 어떤 일을 생략하는지 특정해야 하며 새 후보나 최종 추천안을 채택한 결과는 아니다.

근거: [SRC-0001800](../sources/history-125.md#src-0001800) [[21, 28]]행, [SRC-0001801](../sources/history-125.md#src-0001801) [[54, 70]]행, [SRC-0001802](../sources/history-125.md#src-0001802) [[27, 32]]행, [SRC-0001803](../sources/history-125.md#src-0001803) [[60, 64]]행.

## <a id="claim-28"></a>28. 대표 예측·다중 출력의 이전 검토에 연결

대표 예측·다중 출력·출력 압축은48–50·74·81 등의 이전 검토에 연결한다. 같은 모델의 batch로 묶은 입력을 새 대표 예측으로 바꾸지 않는다. 후보 색인의 긍정 증거와 탐색 진입·최종 추천의 구별도 유지한다. 과거 Tab 직접 예측의 이득을 현재 clustering 성공으로 옮기거나, 과거 실패 때문에 다른 실익의 모든 가능성을 금지하지 않는다.

근거: [SRC-0001801](../sources/history-125.md#src-0001801) [[54, 62]]행, [SRC-0001802](../sources/history-125.md#src-0001802) [[7, 9]]행, [SRC-0001803](../sources/history-125.md#src-0001803) [[23, 27]]행, [SRC-0001803](../sources/history-125.md#src-0001803) [[34, 58]]행.

## <a id="claim-29"></a>29. 후보·연혁의 판본 차이와 미독 범위

후보 색인은58→64행으로 원95의6행이 추가됐고 현재64행을 전체 읽었다. 연혁은527→536행으로 새95블록9행과94제목의 최신→이전 변경이 있다. 현재1–57행을 읽고58–536행은 직접 미독이다. 직전 연혁49–527행도 기계적으로 대응한다는 이유로 전문 판독 완료 처리하지 않는다.

근거: [SRC-0001803](../sources/history-125.md#src-0001803) [[1, 64]]행, [SRC-0001805](../sources/history-125.md#src-0001805) [[1, 57]]행, [SRC-0001779](../sources/history-125.md#src-0001779) 해시·판본·저장검사 범위, [SRC-0001782](../sources/history-125.md#src-0001782) 해시·판본·저장검사 범위.

## <a id="claim-30"></a>30. snapshot37의 파일·용량과 입력 참조

snapshot37은21파일241706bytes를 열거하며 manifest4301bytes를 포함하면22파일246007bytes다. 별도 원95 archive receipt는 snapshot 밖에 있다. 입력/checkpoint10개는 snapshot에 복사하지 않았고9개 checkpoint 각745123bytes와 design_data739949bytes를 경로·hash로 참조했다. 보관 사실을 모델 재현 성공으로 세지 않는다.

근거: [SRC-0001799](../sources/history-125.md#src-0001799) [[1, 114]]행, [SRC-0001820](../sources/history-125.md#src-0001820) [[1, 56]]행, [SRC-0022095](../sources/history-125.md#src-0022095) [[1, 8]]행.

## <a id="claim-31"></a>31. 현재 hash 검수와 팀 자료 접근의 범위

새20개 고유 바이트 자료40물리별칭, 이전 RCTL/설정2그룹16별칭, 직전 판본3그룹19별칭의 총75경로를 현재SHA로 대조했다. 새 보존가능 자료는20개230062bytes다. 보호원본6개·RCTL 동일hash 별칭11개·입력 참조10개도 hash로 확인했다. checkpoint는 pickle 역직렬화·원코드 import 없이 ZIP 저장 크기만 확인했다. 장기 팀 접근은 별도 과제로 남긴다.

근거: [SRC-0001799](../sources/history-125.md#src-0001799) 해시·판본·저장검사 범위, [SRC-0001820](../sources/history-125.md#src-0001820) 해시·판본·저장검사 범위.

## <a id="claim-32"></a>32. 실제 판독·검산과 전체 Goal의 잔여

첫 판독은 새raw1942행과 재사용 RCTL 코드60행으로 총2002행이다. 초안 작성 뒤 원문1645행과 저장 검사 결과를 대조했다. NPZ field/shape/dtype·수치 요약 및 배열 기계검사를 확인했지만 모든 float값의 literal 판독이나 새 timing 실행은 아니다. 문서·링크 검사는 별도 검수 파일에 결과를 기록한다. 원96 이후, 이전 고유판본, FedPPBC/DOCX 공백, 문헌·연혁 후미, 실패·비용 통합, 장기 팀 접근, 최종 원본 변경분·대표 검색이 남아 전체 Goal은 진행 중이다.

근거: [SRC-0001805](../sources/history-125.md#src-0001805) 해시·판본·저장검사 범위, [SRC-0001814](../sources/history-125.md#src-0001814) 해시·판본·저장검사 범위, [SRC-0001801](../sources/history-125.md#src-0001801) [[64, 70]]행.

## 팀 재검토와 재사용

보존된 timing/prediction 배열은 위 수치와 같은 방법의 예측 차이를 검산하는 데 재사용한다. CPU 측정을 다시 실행했다는 뜻은 아니다. [원93](0123-candidate-gates-comparison-scope.md)의 탐색 진입 기준, [원81 공동 입력·다중 출력](0090-input-partition-decision.md), [과거 시도 색인](../prior-attempts.md)을 함께 확인하고 실제로 달라지는 결정·연산과 새 비교 범위를 실험 이슈에 적는다. 과거 상한과 현재 팀 실험 계획을 혼동하지 않는다.

현재 연혁58–536행·직전49–527행 직접 미독,NPZ 모든 float값 literal판독/실행 재현은 하지 않음,기존9checkpoint·원입력의 장기 팀 공유,원96 이후와 이전 고유판본,원83 FedPPBC/원84 DOCX 공백,문헌·실패·비용 통합,최종 원본 변경분·대표 질문 검색 검수.
