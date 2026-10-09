# 33–35 process 식별과 고정 RCTL의 훈련·validation 차이

[과거 시도 색인](../prior-attempts.md) · [출처와 열람 범위](../sources/history-022.md) · [저장 근거](../evidence/0033-0035-frozen-fit/README.md) · [검수](../verification/history-022.md)

2026-09-25의 33은 문헌 확인 계획, 34는 기존 checkpoint 진단 계획·실행, 35는 결과와 판단이다. 이 묶음은 **관계를 식별하는 능력과 자료를 나눈 최종 예측기의 이득이 같은 주장이 아니라는 진단**을 남긴다. 당시 새 알고리즘 채택이나 최종 Word 완료 선언은 없다. 현재 정리에서도 모델을 실행하지 않았다. 주요 주장 C01–C14의 원문 위치와 한계는 [주장 지도](../verification/history-022-primary-review.json)에 있다. [C01]

## 1 질문과 실제 수행 범위

기존 균형 K=4 소속이 global RCTL보다 나빴던 이유를 점검했다. 같은 저장 가중치에서 dropout을 끄고 train과 validation을 각각 예측하여, 과거의 online training loss와 validation loss를 비교할 때 섞이던 조건 차이를 줄이는 것이 34의 목적이었다. 소속을 다시 정하거나 새로운 RCTL을 적합한 기록이 아니다. [C01,C03,C04]

[33 계획](../evidence/0033-0035-frozen-fit/originals/SRC-0021362.md.txt), [34 계획](../evidence/0033-0035-frozen-fit/originals/SRC-0021383.md.txt), [35 판단](../evidence/0033-0035-frozen-fit/originals/SRC-0021407.md.txt)과 [34 코드](../evidence/0033-0035-frozen-fit/originals/SRC-0022860.py.txt)를 대조했다. 저장 결과는 29 checkpoint, 251 forward, 107,520행이며 추가 RCTL fit·TabICL 호출·test forward는 각각 0이다. 주 seed 20260925는 global 하나와 다섯 K=4 소속의 20개 모델, 보조 seed 20260926은 TabICL/empirical의 8개 모델이다. 보조 seed의 global은 없다. 현재 아카이브 검산의 모델 실행도 0회다. [C03]

## 2 자료·분할·입력·학습 조건

Milan internet hourly pilot의 고정 16cell 순서는 3737, 3745, 3753, 3765, 4537, 4545, 4553, 4565, 5337, 5345, 5353, 5365, 6137, 6145, 6153, 6165이다. 32cell design 자료에서 이 순서로 선택했다. 정규화는 cell별 원시 시간 index 0–671의 평균을 사용한 기존 정의이며, RCTL train 전체 평균으로 다시 정규화하지 않았다. [초기 자료](0001-0002-initial-design.md)와 [기존 B2/RCTL](0004-0007-b2-observed-risk.md)의 같은 자료를 재사용한다. [C02]

train target은 168–839(각 cell 672개), validation은 840–1007(168개)이다. 기존 test 1008–1487의 480개/cell 지표는 fit_results에서 복사된 값으로만 연결하며 이번 진단에서 test를 예측하지 않았다. validation은 이미 best checkpoint 선택에 쓰였고 train은 학습 자료이므로 독립 최종 평가가 아니다. 이전에 확인한 test를 새 평가용 미사용 자료처럼 취급하지 않는다. [C02,C04]

선택 design X의 shape는 16×840×16이다. 코드가 만드는 sequence는 16×840×8×9로, 최근 8개 값이 첫 채널에 들어가고 나머지 8개 특징(day/week lag, day mean/std, 달력 4개)은 각 timestep에 반복된다. 정답·cell·시간은 보존 design과 정확히 대조했다. **실제 당시 forward에 투입한 sequence X 자체는 저장되지 않았다.** 코드의 구성과 저장 자료 일치를 실제 실행 입력의 완전한 복원으로 표시하지 않는다. [C02]

기존 RCTL 설정은 MAE, Adam(lr 0.001, eps 1e−7), train batch 256, 최대 80 epochs, patience 10, CPU threads 4/inter-op 2다. 34의 추론 batch는 512다. global의 train/validation 호출은 21+6, 각 local은 6+2여서 27+28×8=251이다. seed·예산·설정은 당시 조건이며 새 실행 지시가 아니다. [C02,C03]

## 3 같은 가중치에서 본 평균과 cell별 손해

정규화 MAE다. 각 cell의 float32 평균을 구하고 이를 float64로 동일 가중 평균한 집계를 보존했다. checkpoint 전체 배열의 float32 평균과는 약 1e−8 차이가 날 수 있다. 보존 예측으로 다시 계산한 29개 train/validation MAE 및 저장 best validation과의 최대 차이는 0이다. 저장 숫자를 확인한 것이며 모델 forward를 재현한 것은 아니다. [C04]

<!-- table:metrics -->
| 조건 | seed | train MAE | validation MAE | validation − global | train 개선 cell/16 | validation 악화 cell/16 |
| --- | --- | --- | --- | --- | --- | --- |
| global K=1 | 20260925 | 0.079981377 | 0.075371472 | +0.000000000 | 0 | 0 |
| TabICL risk K=4 | 20260925 | 0.078401441 | 0.081656144 | +0.006284672 | 12 | 16 |
| empirical risk K=4 | 20260925 | 0.075087383 | 0.078883120 | +0.003511649 | 14 | 14 |
| KNN risk K=4 | 20260925 | 0.076485101 | 0.078536364 | +0.003164893 | 15 | 12 |
| PCC balanced K=4 | 20260925 | 0.076402376 | 0.078196817 | +0.002825345 | 14 | 10 |
| random balanced K=4 | 20260925 | 0.077315060 | 0.080710514 | +0.005339043 | 14 | 15 |
| TabICL risk K=4 | 20260926 | 0.075340635 | 0.079296705 | +0.003925234 | 14 | 11 |
| empirical risk K=4 | 20260926 | 0.076078790 | 0.079134893 | +0.003763421 | 12 | 13 |
<!-- /table:metrics -->

일곱 K=4 조건 모두 train 평균은 낮고 validation 평균은 높다. 주 seed TabICL은 train 12/16cell 개선, validation 16/16cell 악화다. 다른 조건은 validation이 좋아진 cell도 있으므로 모든 분할이 모든 cell에서 나빴다고 일반화하지 않는다. 보조 seed 두 조건의 기준도 주 seed global이어서 완전한 seed 반복 비교가 아니다. [C05]

## 4 저장 validation의 앞·뒤 구간 확인

아래는 **정리 중 추가한 산술 분해**이며 35 원문 표가 아니다. 같은 validation 168시간을 앞 84시간과 뒤 84시간으로 나눠 global 대비 오차 차이를 계산했다. float32 절대오차를 float64로 평균해 위의 원 집계와 마지막 자릿수가 다를 수 있다. 새로운 기간이나 독립 검증 자료가 아니다. [C06]

<!-- table:validation_halves -->
| 조건 | seed | 앞 84시간 ΔMAE | 뒤 84시간 ΔMAE | 앞 악화 cell/16 | 뒤 악화 cell/16 |
| --- | --- | --- | --- | --- | --- |
| TabICL risk K=4 | 20260925 | +0.002708355 | +0.009860983 | 13 | 16 |
| empirical risk K=4 | 20260925 | +0.003908237 | +0.003115057 | 12 | 10 |
| KNN risk K=4 | 20260925 | +0.001863336 | +0.004466445 | 10 | 13 |
| PCC balanced K=4 | 20260925 | +0.002976175 | +0.002674513 | 12 | 11 |
| random balanced K=4 | 20260925 | +0.005165134 | +0.005512950 | 14 | 13 |
| TabICL risk K=4 | 20260926 | +0.003678500 | +0.004171964 | 11 | 14 |
| empirical risk K=4 | 20260926 | +0.005184824 | +0.002342014 | 13 | 11 |
<!-- /table:validation_halves -->

일곱 조건의 평균 손해가 두 절반에 모두 남는다. 주 seed TabICL도 앞 절반에는 개선 cell 3개가 있으나 뒤 절반에는 16개 모두 악화한다. 전체 기간 평균과 cell·기간별 결과를 함께 보아야 한다. 저장된 예측을 다시 사용하면 같은 가중치를 불필요하게 재실행하지 않고 이 질문을 확인할 수 있다. [C06]

## 5 모델 크기와 학습량을 구분한다

[RCTL 구조 코드](../evidence/0033-0035-frozen-fit/../0639/originals/SRC-0023048.py.txt)의 층 구성을 정적으로 계산하면 model당 전체 parameter 174,433, 학습 parameter 173,537, 고정 recurrent bias 896이다. BN float32 buffer 896개와 int64 counter 12개를 합해 buffer 요소 908개이며 parameter·buffer의 tensor 크기는 701,412 bytes다. 직렬화 checkpoint는 각각 745,123 bytes로 다르다. 이 산술은 29개 저장 보고값과 일치하지만 실제 checkpoint tensor를 역직렬화해 센 결과는 아니다. [C07]

35의 표 제목은 “실제 optimizer step”이지만 34 코드의 해당 필드는 **완료 epoch와 ceil(train rows / 256)로 계산한 값**이다. 독립 step 계측 로그가 확보된 것으로 쓰지 않는다. global 한 epoch는 42 step, local 하나는 11 step이므로 네 local의 한 epoch 합은 44 step이다. 모든 모델이 한 epoch씩 처리하는 총 행 수는 같다. 모델 수·학습 parameter가 4배라는 사실과 step 수가 4배라는 주장은 다르다. [C07]

<!-- table:fit_cost -->
| 조건 | seed | 총 학습 parameter | model당 train 행 | 계산 step 합 | 계산 처리 행 합 | 완료 epoch 합 | 과거 fit 초 합 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| global K=1 | 20260925 | 173537 | 10752 | 1890 | 483840 | 45 | 269.589730 |
| TabICL risk K=4 | 20260925 | 694148 | 2688 | 2431 | 594048 | 221 | 177.552920 |
| empirical risk K=4 | 20260925 | 694148 | 2688 | 2453 | 599424 | 223 | 196.389867 |
| KNN risk K=4 | 20260925 | 694148 | 2688 | 2255 | 551040 | 205 | 202.044484 |
| PCC balanced K=4 | 20260925 | 694148 | 2688 | 2321 | 567168 | 211 | 201.110644 |
| random balanced K=4 | 20260925 | 694148 | 2688 | 2299 | 561792 | 209 | 199.011165 |
| TabICL risk K=4 | 20260926 | 694148 | 2688 | 2585 | 631680 | 235 | 224.211009 |
| empirical risk K=4 | 20260926 | 694148 | 2688 | 2376 | 580608 | 216 | 182.267382 |
<!-- /table:fit_cost -->

fit 시간은 기존 fit_results의 기록이다. 실행 순서·warmup·시스템 상태를 통제한 속도 비교가 아니므로 local이 본질적으로 더 빠르다고 결론 내리지 않는다. 모델별 early stopping이 달라 완료 epoch 합도 다르다. [C07,C08]

## 6 실행 시간과 당시 누적 원장

34 summary의 계산 stage는 5.293488300001627초, load/train/validation 소타이머 합은 4.813179500011756초다. 소타이머는 stage에 포함되므로 더하지 않는다. partial RSS 257,744,896 bytes에서 NPZ 저장 후 최종 표본 RSS 257,781,760 bytes로 바뀐다. 연속 계측한 절대 peak임을 검증한 것은 아니다. 35의 process wall 8.546827초와 exit 0은 보고 문장만 확인했으며 해당 console을 별도로 확보하지 못했다. process wall과 stage 역시 겹친다. checkpoint·state 불변 플래그는 저장 보고값이며 당시 실행 내부 상태를 독립 재현한 결과는 아니다. [C08]

[원장](../evidence/0033-0035-frozen-fit/../0642/originals/SRC-0022700.json)에는 frozen_fit_gap_34가 한 번 반영된다. 이미 이후 연구가 누적된 현재 used 총액 대신 당시 stage 이름으로 한정했다. recursive 4.574360099999467초와 34의 5.293488300001627초를 더한 frozen 추론 누적은 9.867848400001094초다. [C09]

35 시점의 기록된 모델링 비용은 TabICL 223.88688630000115초 + RCTL training wall 1,658.1391634000001초 + frozen 9.867848400001094초 + 31까지의 지정 cheap 진단 55.7706712999996초 = 1,947.664569400002초다. RCTL fit 소타이머 합 1,652.1772000999981초는 training wall에 포함된다. 여섯 TabICL 호출군은 45 contexts/35,712행, 기존 RCTL은 29 fit/1,565 epochs다. 35의 잔여 35 contexts/24,288행은 당시 80/60,000 상한에 대한 서술이며 현재 예산 허가가 아니다. [C09]

초기 미기록 전처리, 전체 실패 시도, 문헌 조사·다운로드를 합한 총 연구 시간이 아니다. 구체적인 prefix 선택은 [검산 코드](../../../scripts/research_archive/verify_frozen_fit_history.py)와 [비용 결과](../verification/history-022-portable-check.json)에 남겼다.

## 7 process 식별 논문의 적용 범위

[Butera·De Felice·Cini·Alippi, arXiv:2606.01999v1](https://arxiv.org/abs/2606.01999v1)의 저장 v1 제출일은 2026-06-01이다. 읽은 것은 PDF 34쪽 중 지정 텍스트 14쪽과 시각 확인 4쪽이다. 전체 논문·저자 학습 코드·실험 재현을 완료한 상태가 아니다. 상세 페이지는 출처 표에 있다. [C10,C11]

§2는 global forecasting의 transductive/inductive 상황을 구분한다. §3.1 식 3–5는 정적인 latent process 모수와 조건부 예측을 나누며, MSE의 최적 예측을 조건부 평균의 posterior 혼합으로 나타낸다. §3.2 식 6의 정상 order-P 과정, 과거·모수와 독립인 고정 유한 분산의 가산 noise, Assumption 3.1의 최근 P개 이후에도 남는 조건부 평균 모호성이 전제다. Theorem 3.2의 W>P는 irreducible MSE에 도달하기 위한 **필요조건**이지 충분조건이 아니다. 모든 cell, 유한 자료 neural RCTL, MAE 성능에 대한 보장도 아니다. Appendix B.1의 총분산 분해와 지정 수식을 대조했다. [C10]

§4 식 8의 G는 긴 이력을 embedding으로, F는 최근 창과 embedding을 예측으로 바꾼다. 과거 context의 embedding을 재사용하고 drift 시 갱신하는 설명이 있다. 이 G/F 분리·cache를 새 기여로 제안하면 선행과 겹친다. §4의 PatchTST embedding, F.1.2의 embedding 차원 64·architecture별 conditioning, F.2의 MSE/Adam·50 epochs·patience 8은 RCTL 설정과 다르다. E.2의 early stopping도 in-sample/out-of-sample validation 평균이다. [C11]

35는 G와 F를 “함께 학습”한다고 해석한다. 논문의 학습 가능한 모수와 model 학습 설명은 확인했지만 저자 코드의 optimizer 연결·freeze 동작을 대조하지는 않았다. Appendix G의 cache 비용 이점도 고정 historical token과 바뀌는 rolling token의 조건에 따른 설명이며 현재 RCTL의 실측 이득이 아니다. [C11]

## 8 UPC 그림·표의 정정

[원 UPC](https://doi.org/10.1109/TNSM.2025.3599168)의 PDF 8쪽 Fig. 7 cluster 표기는 **1, 2, 4, 6, 8, 12**다. 35는 이전의 “1~4 비교” 축약을 정정했다. 현재 정리 과정에서도 작은 그림을 10 포함으로 잘못 읽은 초안을 발견해 29–32 본문·근거를 수정했고, 이번에는 과거 시도 색인에 남아 있던 10 표기도 고쳤다. 자동 수치 검사만으로 이 시각 오독을 발견했다고 표현하지 않는다. [C12]

본문은 N=1을 UPC 없이 전체 cell을 한 model에 넣는 조건으로 설명하고 MLP·LSTM·RCTL의 두 지표에서 N=2가 가장 좋았다고 보고한다. 모든 곡선 값을 정밀 추출해 재검증한 것은 아니다. PDF 9쪽 Table II의 GECOS with UPC는 MAE 29.8520±0.348, MAPE 0.1000±0.004(99% CI)이며 without UPC의 두 칸은 대시다. 대시는 0이 아니다. 이 표만으로 GECOS/RCTL의 정확한 UPC 전후 개선율을 계산할 수 없다. [C12]

## 9 당시 판단과 다시 검토할 조건

고정 K=4에서 훈련 적합 향상이 validation 이득으로 이어지지 않았다는 관측은 유한 자료 일반화 손해와 양립한다. 하지만 시간별 난이도·분포 변화, optimization, early stopping, 분리 후 자료 수가 함께 달라져 과적합 하나로 원인을 확정하지 못한다. 전역 최적점·모집단 위험을 확인한 것도 아니다. 원 UPC의 10분·10,000cell·불균형 K=2와 hourly 균형 pilot을 같은 재현 실험으로 취급하지 않는다. [C13]

35가 요구한 다음 조건은 (1) 기존 입력 이후에도 cell을 구별해야 할 실제 예측 혼란, (2) 혼란 감소와 분리의 유한 학습 손해를 최종 RCTL 호출 없이 구별할 관측량, (3) 같은 정보·비용의 empirical/KNN/단순 회귀 대비 TabICL이 판단을 바꾸는 역할이다. 당시 (2)·(3)을 충족한 새 알고리즘은 없었다. 이 조건 제시 자체나 단순 uncertainty 보정항을 신규성·채택으로 세지 않는다. [C13]

새 실험을 설계한다면 기존 [조건부 공유 비용](0023-0025-conditional-pooling.md), [관측 상태별 손해](0026-0027-observable-states.md), [관계·불확실성 문헌](0028-mechanism-uncertainty.md)을 먼저 재사용한다. 동일 16cell·소속·가중치의 train/validation 표를 얻기 위한 모델 재실행은 필요 없다. 다른 자료 수·분할·seed·시간 구간을 묻는다면 무엇이 달라지는지 먼저 명시해야 한다. 이는 후속 설계 조건이며 이 정리 작업에서 실행한 연구가 아니다. [C13]

## 10 재사용 자료와 남은 공백

새 보존 사본 13개(578,461 bytes), 기존 사본 참조 7개를 연결했다. 예측 NPZ는 58개 checkpoint/split 출력과 cell_ids·train_y·validation_y의 61배열을 담는다. [팀용 검산](../evidence/0033-0035-frozen-fit/README.md)은 모델 없이 실행할 수 있다. [C14]

29 checkpoint는 로컬 파일의 해시·크기와 저장 metadata를 대조했으며 총 21,608,567 bytes다. 가중치는 이 묶음에 게시하지 않았고 팀 접근 위치 확인은 미완료다. 실제 tensor 내용·forward 입력·당시 상태 불변의 완전한 재현과는 구분한다. 원문 PDF·그림은 정식 링크와 식별값으로 연결한다. HTML/txt의 고유 내용 전체, 논문 전체와 저자 학습 코드는 남아 있다. [C14]

33의 2410.14630·2607.13006은 발견 단계 자료이며 방법 전체를 검토했다고 세지 않는다. OpenReview challenge를 우회하지 않았다. fetch 기록의 세 응답 200과 소요시간, 파일당 10MiB·30초 timeout·자동 재시도 없음은 다운로드 기록과 코드 범위다. 상한을 실제 사용량으로 더하지 않는다. 35가 보고한 pdftotext.exe 부재·UPC font warning은 별도 실패 console 검증과 구분한다. 36 이후와 전체 고유 연구기록 통합도 계속 남아 있다. [C14]
