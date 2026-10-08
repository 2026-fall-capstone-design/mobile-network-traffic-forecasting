# 유한표본 공유 효과·공분산·예측 보정의 선행 범위

[08·09 기록](../records/0008-0009-finite-sample-pooling.md)의 당시 판단을 확인하기 위해 세 원문의 지정 구간을 대조했다. 아래는 방법 전체의 재현이나 전수 신규성 조사 결과가 아니다. [판본·실제 읽기 범위](../verification/history-002-primary-review.json).

| 원문·확인 위치 | 확인한 선행 | 09와의 관계·적용 한계 |
|---|---|---|
| Maharaj·Inder, *Forecasting Time Series from Clusters*, Monash Working Paper9/99(1999), §2·§3 식3.7 이후 | AR 계수 차이의 pair test로 묶고, 계열 간 disturbance covariance를 반영한 GLS pooling을 다룬다. | 공유 효과와 동시 의존성을 함께 보는 구상에 선행이 있다. 동일 stationary AR(1)/AR(2)·분산·MSFE 논의를 비선형 MAE RCTL의 소속 보장으로 옮기지 않는다. [공식 PDF](https://www.monash.edu/business/ebs/research/publications/ebs/forecasting_time_series_from_clusters.pdf) |
| Hounyo·Lin, *Two-way Clustering Robust Variance Estimator in Quantile Regression Models*, arXiv2602.16376v1(2026), §2.1·§2.2·§3의 구성식 | 주어진 두 군집 차원의 quantile score 의존성과 목표 분위수의 조건부 밀도로 추론의 분산을 구성한다. | 새 cell 소속을 찾아주는 clustering 알고리즘이 아니다. 식2.1의 선형 quantile restriction, Assumptions1–3의 AHK/iid latent·밀도·비특이성·Gaussian regime 등을 현재 시계열이 자동 충족하지 않는다. [공식 v1](https://arxiv.org/html/2602.16376v1) |
| Sui·Zhou·Zhou·Dai, *Prediction-Powered Conditional Inference*, arXiv2603.05575v1(2026), §2.4·§5.1 | labeled sample의 실제−예측 moment 보정과 별도 unlabeled 입력의 예측 moment를 결합한다. 예측항 비중ω=0이면 labeled-only localized estimator로 돌아간다. | iid·서로 독립인 labeled/unlabeled 표본 및 predictor 분리 조건이 있다. 모든 정답이 있는 같은 query에서 같은 예측항을 가감하면 empirical로 상쇄된다는 09의 적용 판단과, 논문의 조건부 추론 기여를 구분한다. [공식 v1 PDF](https://arxiv.org/pdf/2603.05575v1) |

09는 첫 두 문헌을 바탕으로 단순 covariance 추가만으로 신규성이나 RCTL 목적과의 정합성을 확보했다고 주장하지 않았다. 세 번째 문헌에 대해서는 현 자료에 별도의 대량 unlabeled 입력이 필요한 이유가 확인되지 않았다고 판단했다. 이러한 연구 방향 선택은 논문 자체의 부정 결과가 아니다.

2026-10-09 아카이브 확인에서 Monash PDF는 웹 텍스트를 읽었고 직접 파일 수신은403이었다. PPCI HTML 읽기는 도구 오류로 PDF v1을 사용했으며 인쇄19쪽의 가중 보정식을 이미지로 확인했다. 논문 전체를 저장소에 재게시하지 않았다. 09 당시 접근에 실패했다는 xRFM PDF/ScienceDirect 문서는 그 기록의 상세 결과 근거로 채택하지 않았다. 이 항목의 과거 검색어는 연구 이력이며 새 검색·실험 지시가 아니다.
