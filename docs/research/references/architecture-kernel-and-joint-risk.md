# 구조 기반 kernel을 최종 학습기의 위험으로 사용할 때

[원102](../records/0132-architecture-kernel-and-joint-risk.md) · [수식 검수](../evidence/0132-architecture-kernel-and-joint-risk/fixed-affine-identity-check.json) · [비용 산술](../evidence/0132-architecture-kernel-and-joint-risk/cost-arithmetic-check.json) · [서지와 확인 수준](../evidence/0132-architecture-kernel-and-joint-risk/primary-bibliography.json)

| 자료 | 버전·정식 위치 | 이번 확인과 사용 한계 |
|---|---|---|
| The Recurrent Neural Tangent Kernel | [arXiv2006.10246v4](https://arxiv.org/abs/2006.10246v4), 2021-06-15 | 보관26쪽 전문/이미지; simple RNN의 초기화/조건부 학습 연결. stock PTS 예외와 P90/P95의 dataset 비율 보존 |
| Tensor Programs II: Neural Tangent Kernel for Any Architecture | [arXiv2006.14548v4](https://arxiv.org/abs/2006.14548v4), 2020-11-30 | 보관60쪽 전문/이미지; INIT·BP-like/GIA·폭 비율·BN 각주. 독립 증명 감사/유한 Adam·MAE 보장 아님 |
| NTK4A | [고정 commit](https://github.com/thegregyang/NTK4A/tree/db79a5bd9e75e5a15548306d4770951f94883fb7) | Greg Yang의 companion; README/utils/RNN/BN4파일·82셀/6출력/그림15. RNTK 저자 공식code 아님; Transformer/GP4A별도code 미독 |
| Morello·Grégoire·Verboven task affinity | [공식 대학 서지](https://researchportal.vub.be/en/publications/exploring-task-affinities-through-ntk-alignment-and-early-trainin/), [PDF](https://openreview.net/pdf?id=HxT9EuHdXW) | M3L/NeurIPS2024 workshop; metadata/초록/일부만, PDF403. main-track/전체방법검증/정확방법반증 아님 |
| Load Forecasting for Sustainable Demand-Side Energy Management Under User Heterogeneity and Temporal Dynamics | [Sustainability18(16)8165](https://www.mdpi.com/2071-1050/18/16/8165), 2026-08-10 | publication metadata/검색 스크리닝; 직접fetch429. 전문/telecom·RCTL 성능 근거 아님 |
| Pooling Beats Structure on Short Annual Panels: Parameter Sharing and the Forecast Accuracy of Evolutionary Models for Compositional Time Series | [Forecasting8(5)89](https://www.mdpi.com/2571-9394/8/5/89), Aras Yolusever, 2026-09-18 | Eurostat 연간composition/parameter-sharing, metadata·선택검색조각. 직접fetch429/전문 미독; hourly telecom 수치로 이전하지 않음 |

고정 affine smoother의 conditional target 공분산과, Gaussian activation·gradient를 적분하는 kernel recursion의 covariance는 다른 정보다. 개별 Tab 분위수, NTK plot의 seed 평균95%CI, RNTK의 P90/P95 dataset 비율도 구별한다.

새 실험을 설계하기 전에 실제 RCTL의 causal padding·폭/초기화·flatten readout·BN·Adam/MAE·validation, lag/target 공동 조건화, 고정/target 적응 소속·규제값, K1/기존 empirical/Tab 기준과 전체 비용을 적는다. 원101의 직접 예측 이득을 다른 learner의 소속 선택 이득으로 바꾸지 않는다. 고정 코드 보관/정적 판독은 성능 재현 성공이 아니다.
