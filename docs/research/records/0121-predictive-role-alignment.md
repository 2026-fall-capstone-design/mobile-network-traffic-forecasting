# 원91 공간 입력 역할 정렬의 진입 보류와 선행 모델 적용 범위

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

**상태:** 당시 후보 미채택. 40개 주장·8개 묶음의 작성 후 원문 대조 완료.

[출처와 판독 범위](../sources/history-121.md) · [검수](../verification/history-121.md) · [근거](../evidence/0121-predictive-role-alignment/README.md) · [원47](0045-0046-input-stability.md) · [원75](0072-0075-output-compression.md) · [원81](0090-input-partition-decision.md) · [직전 원90](0120-prescribed-regularity.md)

이 기록은 이웃을 고르는 것, 열의 역할을 맞추는 것, 학습 sample을 함께 쓰는 것, 여러 셀을 한 번에 출력하는 것을 구분한다. 역할 정렬 뒤 단일 global 모델이 충분할 수 있으므로 정렬 이득만으로 별도 RCTL 군집을 추천하지 않았다. 아래 논문 결과는 저자 보고와 이번 원문 검수를 구분하며 새 모델 실험은 수행하지 않았다.

## <a id="claim-01"></a>01. 당시 판단

원91은 2026-09-26에 공간 입력의 열이 맡는 예측 역할을 셀마다 맞추는 후보를 검토했다. 실제 역할 불일치의 손해와 정렬 후에도 필요한 셀 분리의 근거가 없어 채택하지 않았다. 최종 추천안이나 새로운 실험의 성공 기록이 아니다.

근거: [SRC-0001661](../sources/history-121.md#src-0001661) [[3, 11]]행, [SRC-0001662](../sources/history-121.md#src-0001662) [[57, 65]]행, [SRC-0001663](../sources/history-121.md#src-0001663) [[21, 21]]행.

## <a id="claim-02"></a>02. 열의 역할 대응

후보는 이웃 집합·관측 시간축·자기 셀의 실제 target을 유지하고 입력 열의 대응만 셀별로 고른다. 이웃 선택, target 좌표 변경, 공동 입력·다중 출력, 학습 sample의 공동 사용과 각각 다르다. TabICLv2로 어떤 역할 대응을 정하고 그 결정이 최종 RCTL에 어떻게 전달되는지는 아직 검증하지 않았다.

근거: [SRC-0001663](../sources/history-121.md#src-0001663) [[7, 11]]행, [SRC-0001665](../sources/history-121.md#src-0001665) [[13, 13]]행, [SRC-0021660](../sources/history-121.md#src-0021660) [[7, 11]]행, [SRC-0022042](../sources/history-121.md#src-0022042) [[17, 23]]행.

## <a id="claim-03"></a>03. 공통 순열과 표현 함수

모든 셀에 같은 순열을 적용하고 원입력을 읽는 모든 projection의 입력 계수를 함께 재배열하면 같은 표현 함수를 구성할 수 있다는 원91의 기호 논리를 확인한다. 저장 RCTL에서는 첫 c1·첫 s1·첫 s2·final_shortcut이 해당한다. 이는 함수 표현의 동등성에 관한 조건부 설명이며 초기화·BN·dropout·확률적 학습 경로의 동등성이나 실제 정확도 개선이 아니다.

근거: [SRC-0001662](../sources/history-121.md#src-0001662) [[52, 52]]행, [SRC-0023048](../sources/history-121.md#src-0023048) [[18, 30], [35, 39], [49, 60]]행.

## <a id="claim-04"></a>04. 정렬 뒤 global 대안

셀 A가 Y=u, 셀 B가 Y=v를 요구하는 기호 예시에서는 B의 두 입력 역할을 바꾸면 하나의 global 함수가 충분할 수 있다. 셀별 정렬이 공통 순서 변경보다 다른 결정이라는 사실과, 정렬 뒤 별도 clustering이 필요하다는 사실은 별개다. 실제 traffic에 이 예시가 성립한다는 증거는 아니다.

근거: [SRC-0001662](../sources/history-121.md#src-0001662) [[53, 53]]행.

## <a id="claim-05"></a>05. 대칭화와 중요도 반례

역할을 지운 unordered 입력은 Y=u 같은 target의 정보를 잃을 수 있다. 또한 Y=uv와 Y=-uv는 입력 중요도의 크기나 순위가 같아도 순열만으로 같은 함수가 되지 않는다. 이 기호 예시들은 중요도·순서 복구·정렬 점수를 곧바로 같은 예측 함수의 소속 점수로 해석할 수 없음을 보여주며, 모든 역할 정렬의 무용성을 증명하지 않는다.

근거: [SRC-0001662](../sources/history-121.md#src-0001662) [[54, 55]]행.

## <a id="claim-06"></a>06. 탐색 비용

d개 역할의 모든 순열을 찾는 후보 수는 셀당 d!이며 모든 셀 쌍의 순열 비교는 단순한 경우 O(N²d!)가 된다. 정해진 대응을 N셀·T시점에 적용하는 O(NTd)는 대응을 찾는 비용을 포함하지 않는다. 이들은 작업량의 기호 설명이며 TabICLv2 실제 context·query 비용, 실행시간, 모든 가능한 효율적 탐색의 하한은 아니다.

근거: [SRC-0001662](../sources/history-121.md#src-0001662) [[61, 63]]행.

## <a id="claim-07"></a>07. 실행과 과거 예산

원91은 새 Tab·RCTL·자료 수치 실행을 보고하지 않았다. 남은 Tab 11 context·20,640 query행과 추가 RCTL fit 0은 당시 원장의 상태이며 현재 아카이브 작업의 실행 지시나 Goal 예산이 아니다. 과거 Goal·스크립트 명령도 역사적 자료로 읽고 원 연구 코드의 실행·import는 하지 않았다.

근거: [SRC-0001661](../sources/history-121.md#src-0001661) [[29, 29]]행, [SRC-0001669](../sources/history-121.md#src-0001669) [[14, 15]]행, [SRC-0001664](../sources/history-121.md#src-0001664) [[4, 7]]행, [SRC-0025150](../sources/history-121.md#src-0025150) 판본·보존 범위.

## <a id="claim-08"></a>08. 원47·75·81과의 차이

원47은 입력 열 추가와 학습 행의 공동 사용을 구분하고 일부 셀의 공간 입력 이득을 보존했다. 원75는 같은 입력 공유 행동의 재진입을 모델 실행 전에 중단했다. 원81은 공동 입력·셀별 다중 출력으로 규격을 바꾸므로 원47의 scalar 공유 반례를 그대로 기각 근거로 쓰지 않았다. 원91은 이 세 판단을 이어 역할 대응을 별도 행동으로 검토한다.

근거: [SRC-0021660](../sources/history-121.md#src-0021660) [[7, 34]]행, [SRC-0022029](../sources/history-121.md#src-0022029) [[1, 18]]행, [SRC-0022042](../sources/history-121.md#src-0022042) [[7, 23]]행, [SRC-0001665](../sources/history-121.md#src-0001665) [[13, 13]]행.

## <a id="claim-09"></a>09. 당시와 이번 판독 범위

당시 수집 기록의 PDF 세 개·65쪽·10,173,209 bytes와 지정 section·기존 이미지 여섯 개의 확인은 서로 다른 범위다. 이번 첫 독해에서는 CPiRi 22쪽·1,698행, CRAFT 12쪽·1,352행, TIDES 31쪽·1,212행과 각각 모든 페이지 이미지를 실제 확인했다. 추출·렌더·출력 자체를 독해로 세지 않고 논문 재현과도 구별한다.

근거: [SRC-0001664](../sources/history-121.md#src-0001664) [[9, 56]]행, [SRC-0001686](../sources/history-121.md#src-0001686) [[1, 55]]행, [SRC-0001674](../sources/history-121.md#src-0001674) 판본·보존 범위, [SRC-0001677](../sources/history-121.md#src-0001677) 판본·보존 범위, [SRC-0001682](../sources/history-121.md#src-0001682) 판본·보존 범위.

## <a id="claim-10"></a>10. CPiRi 구조와 판본

검토한 CPiRi는 arXiv 2601.20318v2, 2026-02-27 판본이다. frozen Sundial의 채널별 시간 표현을 공간 Transformer에서 결합하고 다시 채널별 decoder로 예측한다. 입력과 target에 같은 순열을 쓰는 F(PX)=PF(X) 대응은 자기 target을 고정한 채 이웃 열의 역할만 맞추는 원91의 행동과 다르다.

근거: [SRC-0001671](../sources/history-121.md#src-0001671) [[120, 172]]행, [SRC-0001674](../sources/history-121.md#src-0001674) PDF [3, 4, 5]쪽, [SRC-0001689](../sources/history-121.md#src-0001689) [[55, 79]]행, [SRC-0001692](../sources/history-121.md#src-0001692) [[171, 192]]행.

## <a id="claim-11"></a>11. CPiRi 이론 설명의 범위

CPiRi §3.5의 only stable solution, DeepSets 분해와 content-based relational reasoning 설명은 저자의 이론적 논의로 남긴다. 이번에 인용 DeepSets의 모든 가정이나 셔플이 유일한 해·실제 역할 의미를 보장한다는 정리를 독립 인증하지 않았다. 결정적인 공간 함수의 순열 대응과 확률적 decoder·dropout·학습 경로도 구별한다.

근거: [SRC-0001674](../sources/history-121.md#src-0001674) PDF [5]쪽, [SRC-0001675](../sources/history-121.md#src-0001675) [[525, 566]]행, [SRC-0001689](../sources/history-121.md#src-0001689) [[40, 79]]행.

## <a id="claim-12"></a>12. CPiRi 주표의 이득과 예외

CPiRi Table1은 본문의 five 표현과 달리 Electricity를 포함한 여섯 데이터셋 열이다. METR-LA WAPE는 CPiRi 9.14보다 STID 8.48·Crossformer 8.84가 낮고, PEMS-BAY MAE 2.36은 STID와 같으며 SD MAE도 STID 26.64가 CPiRi 26.85보다 낮다. 다른 데이터셋의 개선과 이 예외를 함께 보존하며 모든 지표 최상을 주장하지 않는다.

근거: [SRC-0001674](../sources/history-121.md#src-0001674) PDF [6, 14]쪽.

## <a id="claim-13"></a>13. CPiRi 셔플 조건

CPiRi Table2의 Test 값은 Table4의 w/o regularization 및 Table10의 full-data without strategy 값과 같다. Table3의 셔플 결과와 Appendix Figure8 설명, delta<.25% 문구를 모든 조건의 같은 실험으로 연결할 근거는 불충분하다. 인쇄된 값과 조건의 차이를 남기며 실제 코드 오류나 연구 결과 전체의 무효로 단정하지 않는다.

근거: [SRC-0001674](../sources/history-121.md#src-0001674) PDF [7, 8, 15, 18]쪽.

## <a id="claim-14"></a>14. CPiRi fine-tuning 손익

CPiRi Table4의 마지막 10 epoch fine-tuning은 METR-LA WAPE/MAE 8.81/4.46 및 SD 12.00/26.47로 기본 조건보다 좋지만 나머지 세 교통 데이터셋에서는 나빠진다. 약 다섯 배 학습 메모리는 저자 보고다. UMAP의 분리 감소는 정성 근거이며 역할 정렬이나 별도 소속의 실제 이득을 인증하지 않는다.

근거: [SRC-0001674](../sources/history-121.md#src-0001674) PDF [8, 10]쪽.

## <a id="claim-15"></a>15. CPiRi unseen 평가

CPiRi의 unseen-channel 실험은 일부 채널로 학습하고 전체 채널로 시험하는 조건이다. 25% 채널 학습의 긍정 결과를 유지하되 직접적인 architecture별 online add/remove benchmark는 향후 과제로 구별한다. 일부 채널 학습 결과나 frozen backbone을 모든 센서 변동에 대한 무학습·무비용 보장으로 바꾸지 않는다.

근거: [SRC-0001674](../sources/history-121.md#src-0001674) PDF [9, 16, 18]쪽.

## <a id="claim-16"></a>16. CPiRi 측정 비용

CPiRi Table6의 CA 8,600 채널·T336 compiled 평균 초는 CPiRi/Sundial/iTransformer/Timer 순서로 .41/.40/.20/1.07이다. 평균 GPU GB는 8/5.17/17.69/75.68, maximum batch는 4/4/2/1이다. 메모리 장점과 일부 시간 비교를 구별하고 모든 모델보다 빠르다고 쓰지 않는다. 이 측정을 원91 소속 탐색이나 RCTL의 총비용으로 이전하지 않는다.

근거: [SRC-0001674](../sources/history-121.md#src-0001674) PDF [9]쪽.

## <a id="claim-17"></a>17. CPiRi 반복과 유의성

CPiRi의 다섯 번 반복 평균·표준편차 설명과 Table11의 검정을 구별한다. Table11은 다섯 교통 데이터셋에 대한 one-tailed Wilcoxon이며 fixed-channel STID·Crossformer 비교는 p=.156으로 유의하지 않다. 이를 다섯 seed의 검정이나 모든 비교에서 유의한 우위로 서술하지 않고, seed ID와 다중 비교 보정의 독립 확인도 주장하지 않는다.

근거: [SRC-0001674](../sources/history-121.md#src-0001674) PDF [16, 18]쪽.

## <a id="claim-18"></a>18. 고정된 여섯 코드

CPiRi 저장 코드는 commit 3f1e00f62b42782062c3484792f47fe905e5b743의 README·METR-LA 설정·arch·datas·mds·runner 여섯 파일이다. 전체 1,286행을 정적으로 읽고 manifest와 실제 hash를 대조했다. 이는 저장 시점의 고정 판본이며 현재 upstream이나 논문 표에 사용한 정확한 실행 판본을 독립 확인한 사실은 아니다.

근거: [SRC-0001685](../sources/history-121.md#src-0001685) [[1, 49]]행, [SRC-0001687](../sources/history-121.md#src-0001687) [[1, 35]]행, [SRC-0001688](../sources/history-121.md#src-0001688) 판본·보존 범위, [SRC-0001689](../sources/history-121.md#src-0001689) 판본·보존 범위, [SRC-0001690](../sources/history-121.md#src-0001690) 판본·보존 범위, [SRC-0001691](../sources/history-121.md#src-0001691) 판본·보존 범위, [SRC-0001692](../sources/history-121.md#src-0001692) 판본·보존 범위.

## <a id="claim-19"></a>19. 저장 설정과 논문의 차이

보관 METR-LA 설정은 50 epoch 중 11번째의 첫 iteration에 backbone requires_grad를 켜도록 지정한다. TRAIN/VAL/TEST 채널 셔플 True 옵션은 주석이고 runner의 기본값은 False다. sample loader SHUFFLE=True는 채널 셔플과 다르다. 논문의 frozen+shuffle 기본 조건 및 마지막 10 epoch fine-tuning과 저장 기본 설정은 다르며, 실행 override·부모 optimizer의 parameter 포함·실제 가중치 갱신은 확인하지 못했다.

근거: [SRC-0001688](../sources/history-121.md#src-0001688) [[24, 38], [104, 162]]행, [SRC-0001692](../sources/history-121.md#src-0001692) [[81, 114]]행, [SRC-0001674](../sources/history-121.md#src-0001674) PDF [8]쪽.

## <a id="claim-20"></a>20. 확률 출력과 정규화

저장 arch는 초기 frozen Sundial·외부 공간 Transformer(dropout .3), train decoder 1 sample 및 eval 20 sample 평균을 사용한다. runner는 inputs와 target의 node축2를 같은 순열로 바꾼다. 결정적 함수의 대응과 stochastic output의 pointwise 동일성은 다르며, 셔플 뒤 per-channel scaler의 identity 대응도 실제 정규화 설정·부모 호출 순서를 확인해야 한다.

근거: [SRC-0001689](../sources/history-121.md#src-0001689) [[15, 79]]행, [SRC-0001692](../sources/history-121.md#src-0001692) [[171, 192], [263, 316]]행, [SRC-0001688](../sources/history-121.md#src-0001688) [[24, 29], [73, 78]]행.

## <a id="claim-21"></a>21. 별도 코드 분기

HiddenDataset의 고정 cached-hidden 형태와 CombinedTimeSeriesDataset의 값>100 처리·같은 dataset batch sampler는 보관 코드에 있으나 METR-LA 기본 설정이 선택한 class와 다르다. 설정 파일의 __main__에는 cached-hidden 작성과 보관 arch에 없는 forward_hid 호출도 있다. 별도 branch를 기본 학습의 동작이나 표 재현 결과로 취급하지 않고 실행 가능성·부모 구현은 미확인으로 남긴다.

근거: [SRC-0001690](../sources/history-121.md#src-0001690) [[62, 79]]행, [SRC-0001691](../sources/history-121.md#src-0001691) [[22, 45], [87, 105]]행, [SRC-0001688](../sources/history-121.md#src-0001688) [[57, 68], [171, 259]]행, [SRC-0001689](../sources/history-121.md#src-0001689) [[1, 158]]행.

## <a id="claim-22"></a>22. CRAFT의 학습형 재정렬

CRAFT WWW2026은 shared trend/seasonal embedding의 점수를 정렬해 P개씩 묶고 그룹 안팎의 attention으로 공동 예측한다. rank loss·position loss·forecast MSE를 결합한다. 학습된 채널 재정렬·고정 크기 attention 그룹은 알려진 예측 구조이며, 자기 target 고정 이웃의 역할 대응이나 cluster별 완전한 RCTL 모델 학습과 동일하지 않다.

근거: [SRC-0001677](../sources/history-121.md#src-0001677) PDF [1, 4, 5]쪽.

## <a id="claim-23"></a>23. CRAFT 비용식 해석

CRAFT는 linear complexity라고 설명하지만 식의 attention 항은 O(GP²+PG²), GP≈C다. padding을 제외한 대입은 O(C(P+C/P))이며 P≈√C인 균형에서 O(C^1.5)가 된다. 이는 인쇄된 식에서의 자체 대수 추론으로, 모든 비용이 C에 선형이라는 일반 인증이나 실제 wall time 측정은 아니다. 정렬 O(C logC), embedding O(CT), layer·hidden·탐색 비용도 별도로 보아야 한다.

근거: [SRC-0001677](../sources/history-121.md#src-0001677) PDF [5, 6]쪽, [SRC-0001662](../sources/history-121.md#src-0001662) [[32, 32]]행.

## <a id="claim-24"></a>24. CRAFT smoothing의 조건

CRAFT의 normalized Laplacian smoothing은 대칭 Abar를 쓰면서 D의 degree를 A로 표기한다. 모든 비영 고유 성분 감쇠에는 |1-alpha*lambda|<1 조건이 필요하다는 자체 수식 해석을 남기고 alpha>0만으로 보장하지 않는다. mean subtraction을 u1 projection으로 보는 degree 조건, 반복 지수의 인덱스, 작은 spectral gap에서 여러 성분이 남는 한계도 구별하며 구현 오류나 항상 Fiedler 순서가 된다는 결론은 단정하지 않는다.

근거: [SRC-0001677](../sources/history-121.md#src-0001677) PDF [5, 10, 11, 12]쪽.

## <a id="claim-25"></a>25. CRAFT 주표

CRAFT Table2의 저자 best-count는 MSE 14/MAE 13이다. Solar MAE는 TSMixer .216이 CRAFT .217보다 낮고, Measles MSE .010은 인쇄 정밀도에서 iTransformer·U-CAST와 동률이다. Wiki20k의 10.138/.290 같은 긍정 결과와 OOM 표시를 함께 남긴다. 서로 다른 데이터·평가 단위의 결과를 TabICLv2·Milan·RCTL 성능으로 바꾸지 않는다.

근거: [SRC-0001677](../sources/history-121.md#src-0001677) PDF [7]쪽.

## <a id="claim-26"></a>26. CRAFT ablation과 P

CRAFT Table3에서 rank loss 제거는 Atec .682 vs full .272, TrafficCA .206 vs .054, Solar .284 vs .153으로 손해가 있다. position loss 제거의 일부 표시값은 full과 같아 모든 경우 strictly worse라 쓰지 않는다. Figure3의 최저 P는 Atec16·Solar64·Wiki128이며, 재정렬 감독과 그룹 크기의 긍정 효과가 별도 모델 공유 partition의 필요성을 증명하지는 않는다.

근거: [SRC-0001677](../sources/history-121.md#src-0001677) PDF [7]쪽.

## <a id="claim-27"></a>27. CRAFT 비용 측정 범위

CRAFT Figure5는 log축의 training ms/iteration과 GPU memory GB를 비교한다. Wiki20k에서 iTransformer 대비 메모리 92%·시간 75% 감소는 p2의 저자 보고이며 주석 없는 막대에서 새 정확한 값으로 재계산하지 않았다. Meter의 일부 baseline보다 느린 예외와 OOM에 따른 batch 절반 조정·hardware/동일 batch 미확인을 남기고, 총 탐색·학습 wall time으로 확대하지 않는다.

근거: [SRC-0001677](../sources/history-121.md#src-0001677) PDF [2, 6, 8]쪽.

## <a id="claim-28"></a>28. CRAFT 재현 공백

CRAFT의 chronological split은 7:1:2이며 latent dimension·P·input length를 탐색한다. Appendix Eq28의 Pearson은 1-correlation으로 인쇄됐지만 본문 설명은 [-1,1]·높을수록 일치하는 correlation이다. 지표의 범위·방향을 말없이 고치지 않는다. seed·반복 STD·확정 설정과 target 순열 복구/padding mask의 실제 구현도 이 PDF만으로 확인하지 못했다.

근거: [SRC-0001677](../sources/history-121.md#src-0001677) PDF [4, 5, 6, 11]쪽.

## <a id="claim-29"></a>29. TIDES 군집 특징

TIDES arXiv2512.22178v1의 clustering feature는 위도·경도·평균·AM·PM·NIGHT·local Moran I 일곱 개다. Haversine kNN의 1/d 가중치와 표준화 특징의 ordinary Kmeans squared-distance 목적을 사용한다. 이것은 지역·트래픽 이질성에 따른 군집 사례이며 원91의 같은 역할·함수 소속 점수를 직접 검증한 방법은 아니다.

근거: [SRC-0001682](../sources/history-121.md#src-0001682) PDF [11, 12]쪽, [SRC-0001686](../sources/history-121.md#src-0001686) [[47, 55]]행.

## <a id="claim-30"></a>30. TIDES 자료와 학습 조건

TIDES는 한 중국 도시의 약19,000개 4G sector·2024-07-28~08-25·15분 데이터를 지역 단위로 합쳐 K4 Zone을 만든다. sector 수를 모델의 regional node 수나 Milan cell 수와 동일하게 쓰지 않는다. 96시점→4시점, DeepSeek-R1-Distill-Llama-8B32층, 주변 모듈 학습·core frozen, AdamW LR.001·batch16·최대100 epoch/early stop·A100 네 대 조건이며 총 학습비용·split dates/ratio·seed·actual code는 미확인이다.

근거: [SRC-0001682](../sources/history-121.md#src-0001682) PDF [17, 18, 19, 28]쪽.

## <a id="claim-31"></a>31. TIDES 주표의 이득과 예외

TIDES TableI는 12개 Zone별 지표 중 10개에서 최저이며 모든 네 Zone MAPE가 가장 작다. ZoneB에서는 Time-LLM MAE/RMSE .3567/.5401이 TIDES .4208/.6459보다 낮다. Autoformer ZoneB MAPE는 표 2.6243인데 본문은 2.6294로 다르다. 개선과 예외를 함께 남기며 모든 Zone·지표 최상 문구나 다른 단위의 RCTL 비교로 확대하지 않는다.

근거: [SRC-0001682](../sources/history-121.md#src-0001682) PDF [17, 19, 20, 21]쪽.

## <a id="claim-32"></a>32. TIDES Zone 전이 조건

TIDES TableII는 같은 도시의 source Zone에서 학습해 destination ZoneA를 추가 fine-tuning 없이 시험하는 축소 비교다. 본문은 다섯 region을 표본으로 사용했다고 쓰지만 각 region에서 다섯 region을 뽑는다는 표현은 모호하다. B→A의 MAE/RMSE는 성능이 15.0%/11.5% 나빠지지만 MAPE는 10.3% 좋아지고, D→A도 MAE/RMSE 악화와 MAPE 개선이 함께 있다. 대부분10%이내 문구의 예외와 지역/Zone 표현의 모호함을 보존한다. 축소 표본 비교의 A→A와 주표 ZoneA를 같은 실험으로 단정하지 않고 cross-city 일반화는 향후 과제로 남긴다.

근거: [SRC-0001682](../sources/history-121.md#src-0001682) PDF [27, 28]쪽.

## <a id="claim-33"></a>33. TIDES prompt 표기

TIDES Eq21 PAR은 MAX/(MAX+epsilon)으로 PDF와 저장 HTML 모두에 인쇄됐으며 peak-to-average 설명의 average 분모와 다르다. RevIN 뒤 같은 x 표기를 사용해 prompt 통계를 계산하는 범위도 구현 확인이 필요하다. DeepSeek embedding dimension의 인쇄4068을 별도 checkpoint 확인 없이4096으로 고치지 않는다. 표기 불일치를 실제 학습 오류·누출로 단정하지 않는다.

근거: [SRC-0001682](../sources/history-121.md#src-0001682) PDF [13, 14, 16]쪽, [SRC-0001683](../sources/history-121.md#src-0001683) [[812, 976]]행, [SRC-0001681](../sources/history-121.md#src-0001681) 판본·보존 범위.

## <a id="claim-34"></a>34. TIDES graph mask 표기

TIDES Eq25는 M=(1-Lsym)*(-1000) mask를 설명한다. non-connected pair를 막는 목적과 literal 식의 1·부호·graph binarization이 어떻게 대응하는지, kNN graph의 대칭화·zero-distance 처리, multi-head 구현은 미확인이다. PDF와 HTML에 같은 식이 있어 추출 오류로 보정하지 않고 actual code의 잘못된 실행이라고 단정하지도 않는다.

근거: [SRC-0001682](../sources/history-121.md#src-0001682) PDF [12, 15, 16]쪽, [SRC-0001683](../sources/history-121.md#src-0001683) [[920, 970]]행, [SRC-0001681](../sources/history-121.md#src-0001681) 판본·보존 범위.

## <a id="claim-35"></a>35. TIDES 정성 비교

TIDES Figure3/p22의 forecast correlation은 Time-LLM .792·DLinear .959·TIDES .973이다. 정규화 scatter·error density·도시 map의 긍정 관찰은 유지하지만 선택한 baseline과 예시에서의 결과다. correlation이나 이웃 attention을 실제 예측 역할 label·TabICLv2 소속 수정·모든 지역의 인과적 영향 증명으로 바꾸지 않는다.

근거: [SRC-0001682](../sources/history-121.md#src-0001682) PDF [19, 20, 21, 22, 23]쪽.

## <a id="claim-36"></a>36. TIDES 시간별 그림

TIDES Figure5의 여러 시간 막대에서 이득이 보이지만 모든 시점 strictly lowest라고 인증하지 않는다. Figure6는 선택 ZoneA/ZoneC의 정규화 예측이며 x축20~26Aug2024와 자료 종료Aug25 사이에 apparent date 차이가 있다. timezone·경계·plot 구성은 미확인으로 남기고 실제 누출/실행 오류나 모든 지역의 peak 정렬 성공을 단정하지 않는다.

근거: [SRC-0001682](../sources/history-121.md#src-0001682) PDF [17, 21, 24, 25, 26]쪽.

## <a id="claim-37"></a>37. TIDES 지역 개선 그림

TIDES Figure7은 선택한25지역의 improvement-over-TimeLLM과 저자의 up-to.8 보고를 보여준다. 그림의 최대는 WangGuanZhuang 부근이고 본문 예시 QuanFu/DongGuan는 이 labels에 없다. metric·상대 개선식·선택 기준을 확인하지 못해 .8을 MAE의 단위나 모든 지역80%개선 보장으로 읽지 않는다.

근거: [SRC-0001682](../sources/history-121.md#src-0001682) PDF [25, 26, 27]쪽.

## <a id="claim-38"></a>38. 현재 판본 변경

현재 후보표는 원90의48행에서49행으로 바뀌며 역할 대응13행만 추가됐다. 연혁은488→498행이고 옛7행을 현재7–17행의11행으로 대체했다. 현재 연혁1–55행은 실제 읽었고 나머지 대응은 기계 비교다. 동일한 누적 본문을 새 실험이나 전체 연혁의 독립 재검수로 가산하지 않는다.

근거: [SRC-0001665](../sources/history-121.md#src-0001665) [[1, 49]]행, [SRC-0001669](../sources/history-121.md#src-0001669) [[1, 55]]행, [SRC-0001639](../sources/history-121.md#src-0001639) 판본·보존 범위, [SRC-0001643](../sources/history-121.md#src-0001643) 판본·보존 범위.

## <a id="claim-39"></a>39. snapshot 보존과 파생물

snapshot33은 manifest에 나열된38파일13,945,266 bytes와 manifest7,994 bytes를 합친39파일13,953,260 bytes다. root archive JSON213 bytes는 별도다. 원 PDF와 TXT는 내용 대응을 검사하되 독립 본문으로 중복 가산하지 않고, CRAFT TXT의p11 추가 빈행3개도 기록한다. 기존 PNG6개의 실제 전체 시각 확인과 새 PDF 렌더65개의 확인은 각각의 판독 범위로 남긴다.

근거: [SRC-0001660](../sources/history-121.md#src-0001660) [[1, 198]]행, [SRC-0022079](../sources/history-121.md#src-0022079) [[1, 7]]행, [SRC-0001676](../sources/history-121.md#src-0001676) 판본·보존 범위, [SRC-0001678](../sources/history-121.md#src-0001678) 판본·보존 범위, [SRC-0001684](../sources/history-121.md#src-0001684) 판본·보존 범위.

## <a id="claim-40"></a>40. 다시 열 조건과 남은 범위

이 후보를 다시 검토할 때는 실제 관측에서 역할 불일치가 만든 손해, 단순 대응/순열 대응 모델과의 차이, 정렬 뒤 global 대안에 남는 손해, Tab이 바꾸는 별도 소속 결정과 탐색 비용을 먼저 확인해야 한다. 이것은 당시 미채택 이유와 다시 열 조건이며 새 실험 지시가 아니다. 현재 연혁56–498·선택범위 밖 HTML/TXT·부모/외부 구현과 전체 과거 기록의 후속 검수도 미완료로 남긴다.

근거: [SRC-0001661](../sources/history-121.md#src-0001661) [[25, 31]]행, [SRC-0001662](../sources/history-121.md#src-0001662) [[57, 65]]행, [SRC-0001665](../sources/history-121.md#src-0001665) [[40, 49]]행.

## 팀 재검토 안내

같은 이름의 후보를 다시 시작하기 전에 실제 관측에서 역할 불일치의 손해가 있었는지, 단순 순열 대응과 차이가 있는지, 정렬한 global 모델에 어떤 손해가 남는지, TabICLv2 점수가 어떤 소속 결정을 바꾸는지 확인한다. 이는 과거 판단을 찾기 위한 조건표다. 새 연구 실행을 지시하거나 당시 예산을 재개하는 문서는 아니다.

현재 연혁56–498행의 직접 재독, 선택범위 밖 raw HTML/TXT의 고유 내용 확인, CPiRi 부모 optimizer/scaler·정확 실행판본 및 CRAFT/TIDES 실제 구현·원자료, 역할 불일치의 실제 손해·정렬 후 분리 필요성, 원92 이후와 이전 고유판본, 원83FedPPBC/원84DOCX 공백, 전체 실패·비용 통합과 장기 팀 접근·최종 원본 delta/대표 검색 검수.
