# 학습 단위·clustering·전체 비용 — 원99 문헌 비교

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

[원99](../records/0129-learning-units-and-clustering-cost.md) · [34출처](../sources/history-129.md) · [실제 판독/미독](../evidence/0129-learning-units-and-clustering-cost/literature-scope.json)

| 판본 | 대상·결정·비교 | 현재 cell pooling에 옮길 때의 경계 |
|---|---|---|
| Cash·Wyglinski2509.15072v1 | OD flow histogram/JSD 계층 군집·K9/47, GRU30, normalized RMSE/MAE·MLU | 전체6쪽 text/image;92/75%는 ARCNN/TE-Prophet 대비, random 대조는 이 판본에 없음. local 평균오차가 낮음 |
| Cash·Fowler·Wyglinski2604.26081v1 | OD flow hist/ACF/PSD/naive·GRU200, Kneedle 운영점·matchedK 구조분석 | 전체12쪽 text/image; 운영K와matchedK 다름, TableII Mbps. head/code·K선택split·전체runtime 미확인 |
| Ma 등2604.13748v1 | 하루 MTS·TRAIN fit·VAL 소속/K/fallback·refit·TEST |27/43쪽 text·18이미지; sensor grouping 아님. 반복 최종forecaster 사용·하루내 split·cluster VAL 기준의 범위 |

Martha Cash, Alexander Wyglinski, **Improving Internet Traffic Matrix Prediction via Time Series Clustering**. [공식 v1](https://arxiv.org/abs/2509.15072v1) · [PDF](https://arxiv.org/pdf/2509.15072v1), 제출2025-09-18. 현재 arXiv comment는 accepted ICMLA2025라고 표시한다. 원99는 conference program도 확인했다고 기록했으나 이번에는 그 program을 독립 재확인하지 않았다. TableI의 정규화 RMSE92/75%는 다른 비교군이다. Prophet은 TE 중심 GRU framework이며 동명의 일반 예측 package가 아니다. MLU bias=예측TM MLU/ground-truthTM MLU, 기준1이고 topology가 필요하다.18/21% 표현을 raw bias 비율 감소로 바꾸지 않는다. 저자 linkage/head/seed·실제 normalization/clustering fit 구간/코드 실행은 확정하지 않았다.

Martha Cash, Charlotte Fowler, Alexander M. Wyglinski, **On the Role of Time Series Clustering in Traffic Matrix Prediction**. [공식 v1](https://arxiv.org/abs/2604.26081v1) · [PDF](https://arxiv.org/pdf/2604.26081v1), 제출2026-04-28. arXiv comment의 IEEE 제출은 게재 확정이 아니다. histogram50bins/JSD/complete linkage, ACF/PSD Euclidean/average linkage, PSD Welch다. 운영점 Abilene21/21/41/21·GéANT40/100/100/50, NMI/ARI 별도matchedK21/40을 분리한다. 비슷한 운영점 error나 low ARI는 모든K/데이터에서 grouping이 무용하다는 증명이 아니다. local GRU의 낮은RMSE·높은runtime를 함께 남기고 Abilene120–150분/150–200분의 본문 차이를 임의 통일하지 않는다. Kneedle split 미확인만으로 leakage를 단정하지 않는다.

Ziling Ma, Ángel López-Oriona, Hernando Ombao, Ying Sun, **Forecasting Multivariate Time Series under Predictive Heterogeneity: A Validation-Driven Clustering Framework**. [공식 v1](https://arxiv.org/abs/2604.13748v1) · [PDF](https://arxiv.org/pdf/2604.13748v1), 제출2026-04-15. PEMS-BAY180개의288×325 하루 MTS·PEMS-SF440개의144×963 하루 MTS를 묶는다. TRAIN-only 전처리/공유 encoder·decoder/GRU prototype·warm-start, VAL 손실 재배정/penalizedK 선택/cluster평균fallback 고정, TRAIN+VAL refit/한 번 TEST다. BAY 선택K7의 Ben84/86/92%, Fb0은 모든TEST 하루의 무손해를 뜻하지 않는다. 검토한페이지1–21/23–24/36–39, 실제wholeimage1–9/12–14/18–21/37/39 외 다른 시각내용과16텍스트쪽·공식 구현/전체 재현은 남는다.

외부 PDF/TXT/PNG를 게시하지 않는다. 현재 공식 서지와 과거 로컬PDF SHA·다운로드 경위를 분리한다. 원99 첫HTTP406/재시도 후 성공 URL 미기록, arXiv renderer issue 링크를 저자코드로 보지 않은 당시 검색 한계를 남긴다. 세 저자 구현이 존재하지 않는다고 판단하지 않는다.

[공식 GRU tensor shape](https://docs.pytorch.org/docs/2.14/generated/torch.nn.modules.rnn.GRU.html)에 따른 원99 H200 식은 명시한 한층/단방향/bias2/head 가정의 산술이다. Ma의 shared encoder나 현재 RCTL(LSTM 포함·extra bias frozen)에 그대로 대입하지 않는다. 소속 품질, 전체 용량, sample/update, 예측row/호출, Tab 준비/cache를 나누어 같은 조건의 재실험을 설계한다.

후속 [원100](../records/0130-pretraining-objective-and-time-conditioning.md)과 [사전학습·시간 조건 비교](pretraining-objective-and-time-conditioning.md)는 다른 학습 단위의 성공을 현재 cell 공유에 적용할 때 학습 정답, K1, 최종 learner의 학습 관계도 확인한다. 새 모델 실행 없이 문헌·보관 공식 코드·제한된 기호를 대조했다.
