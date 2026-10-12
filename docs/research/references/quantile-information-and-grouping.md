# 중앙값 정보·source 선택·grouping — 원98 문헌 비교

[원98](../records/0128-quantile-information-and-pooling-objective.md) · [당시/현재 범위](../evidence/0128-quantile-information-and-pooling-objective/literature-scope.json) · [출처](../sources/history-128.md)

| 논문/판본 | 묶거나 선별하는 대상·실제 절차 | 확인 범위·현재 traffic 적용의 경계 |
|---|---|---|
| Bai 등2411.19933v2 | 고정τ 희소 target β와 source 대비δ; 관계·n×잔차밀도 선별; 보정 공동 QR | PDF1–17/39–41 텍스트·7/16 이미지; 독립source/설계·밀도·분리 조건. 한 target 목적을 전체cell clustering과 구별 |
| Gu·Volgushev1801.05041v2 | 공통slope 아래 절편fusion; 원자료 refit 손실+K벌점; pooled잔차 분위수 폭 | PDF1/4–10 텍스트·5/6 이미지; 내부IID/개체간독립·분리/pointwise. 일반 inverse-density 합과 공통f 단순화 구별 |
| Yang 등2303.13218v1 | Z조건 slope함수 grouping/complete linkage; R선택용 계수평균; 최종 원자료 local QR | PDF1/6–17 텍스트·9/15 이미지; α개별효과 미병합. knownR1–4/unknownR5/CLT1–7을 분리 |

Ruiqi Bai, Yijiao Zhang, Hanbo Yang, Zhongyi Zhu, **Transfer Learning for High-dimensional Quantile Regression with Distribution Shift**, arXiv2411.19933v2. [공식 v2](https://arxiv.org/abs/2411.19933v2) · [PDF](https://arxiv.org/pdf/2411.19933v2). arXiv 개정일2025-11-25와 PDF표제일2025-11-26은 다른 역할이다. PDF8 식2의 정보비는 n0E[f0]/(nkE[fk])이고, PDF15 식7은 잔차 주변 빈도/(2bk nk)다. PDF8 식3의 joint score 제약, PDF16 Algorithm1의 fixedδ pooled QR, PDF40 Algorithm3의 교대 추정을 혼합하지 않는다. 저자의 조건부 rate 연결/반복 설명은 전체 증명·공식 구현 검증이 아니다.

v2 PDF7 문장의 f0/f1 방향은 뒤의 식과 맞지 않는다. 공통Σ/양의밀도에서 r=n1/n0,s=f1/f0라 두면 분산 주항의 비가(1+r)/(1+rs)^2이며 s<1/(sqrt(1+r)+1)이 strict 손해다. 경계는 주항 동일이다. 이 국소적인 문장/경계 확인을 논문 전체의 무효나 RCTL 실패로 확대하지 않는다.

현재 비교용 [v1](https://arxiv.org/abs/2411.19933v1) · [PDF](https://arxiv.org/pdf/2411.19933v1)은53페이지773,918bytes, SHA9ac6f6…다. arXiv제출2024-11-29/PDF표제2024-12-02를 구별한다. 실제 확인은1/9/10페이지 텍스트와9/10이미지다. v1 PDF10 식3은 밀도비와 균형 sample 단순화를 적고, 다른 손실/이론에서 sample 수가 사라진 논문은 아니다. 원98 당시 로컬 자료와 별개의 현재 검증 자료이며 새 과거 내용 완료0이다.

Jiaying Gu, Stanislav Volgushev, **Panel Data Quantile Regression with Grouped Fixed Effects**, arXiv1801.05041v2. [공식 판본](https://arxiv.org/abs/1801.05041v2). arXiv개정2018-08-05/PDF표제Version2018-08-07. group과K는τ별로 다를 수 있다. 초기절편차 역제곱 가중fusion, 실제sample refit/IC이며 모델 가중치 단순 평균이 아니다. PDF6의 일반 역밀도합과 공통 잔차밀도 아래 sparsity 추정 단순화를 분리한다. 모든 증명/실험·최적화 구현은 미검증이다.

Xiaorong Yang, Jia Chen, Degui Li, Runze Li, **Functional-Coefficient Quantile Regression for Panel Data with Latent Group Structure**, arXiv2303.13218v1, 제출2023-03-23. [공식 판본](https://arxiv.org/abs/2303.13218v1). 개별α와 group slope함수를 구별하고 R선택용 계수평균을 최종 rawsample refit로 바꾸어 읽지 않는다. knownR group회복에는 별도 cross-sectional 독립 제약이 없고, postgroup CLT에는 jointmixing/공분산·group크기 조건이 추가된다. smooth t/T·개별Zit 변형 설명을 임의 급변 traffic 보장으로 확대하지 않는다.

Xu 등의 **A Grouped GEE Framework for Quantile Regression in Heterogeneous Longitudinal Data Analysis**는 [당시 출판사 URL](https://onlinelibrary.wiley.com/doi/abs/10.1002/sta4.70051)에서 초록으로 연결됐다고 기록했다. 이번 요청은 이 도구에서 접근되지 않았으며 전문 알고리즘을 읽지 않았다. 과거 PMC 확인 화면도 현재 access결과와 구분한다. 출판사/논문 전체가 원천적으로 접근 불가하다는 판단은 아니다.

외부 PDF/TXT/PNG와 설치 라이브러리를 재배포하지 않는다. 정식 링크·버전·SHA·실제 판독 위치를 제공하며, 원PDF 나머지137페이지·현재v1 나머지50페이지·모든 공식 코드/증명·다른 시각 내용은 미완료다. Tab의 구간 밀도 추정과 실제 calibration/RCTL 학습 정보 연결은 후속 질문이다.
