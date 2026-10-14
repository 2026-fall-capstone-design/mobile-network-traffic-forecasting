# 시각 정렬·고정 좌표·예측 전 입력 지원의 문헌 비교

[원110–111 기록](../records/0140-calendar-alignment-and-input-preflight.md) · [당시 원문 감사](../sources/history-140.md#src-0020865) · [현재 선택 절/판본 검수](../evidence/0140-calendar-alignment-and-input-preflight/literature-primary-checks.json)

네 편의 선택 본문과 핵심 수식/도식8쪽을 대조했다. 전체 논문·공식 구현·새 benchmark 성능을 전수 재현한 결과가 아니다. 외부 PDF와 렌더링 이미지는 검수 중간물이며 저장소에 원문 전체를 게시하지 않았다.

| 문헌·검토판본 | 현재 읽은 위치 | 후보와 구별할 점 |
|---|---|---|
| [A Representation Theory Perspective on Simultaneous Alignment and Classification](https://arxiv.org/pdf/1607.03464v1) · 1607.03464v1 | PDF 본문쪽1, 2, 14, 17, 22, 26, 27, 28, 29, 30; pixels쪽17, 22 | 같은 class의 pair 정렬 비용과 소속/변환을 함께 정하는 선행 목적. Tab 비용으로 교체하는 것만으로 구조적 신규성을 주장하지 않는다. |
| [Automatic Registration and Clustering of Time Series](https://arxiv.org/pdf/2012.04756v2) · 2012.04756v2 | PDF 본문쪽1, 2, 3, 4, 6; pixels쪽2, 6 | 같은 복소 회전으로 Fourier 벡터를 정렬하는 정의. 실제 time shift와 다르며 그 논문의 계산 비용을 현재 후보의 실측으로 쓰지 않는다. |
| [CAPS: Unifying Attention, Recurrence, and Alignment in Transformer-based Time Series Forecasting](https://arxiv.org/pdf/2602.02729v1) · 2602.02729v1 | PDF 본문쪽1, 3, 4, 5, 6; pixels쪽4, 5 | attention 내부의 상대 회전과 세 학습 경로. RCTL 밖에서 고정할 cell 좌표와 적용 위치가 다르다. |
| [Adaptive Oscillatory-State Alignment for Time Series Forecasting](https://arxiv.org/pdf/2606.06010v1) · 2606.06010v1 | PDF 본문쪽1, 3, 4, 8, 9, 10, 11, 12; pixels쪽3, 4 | Hilbert 상태 descriptor로 관측/prior를 보간하는 학습 모델. 같은 phase를 같은 상태로 간주하지 않지만 고정 cell clustering/RCTL 효용의 검증은 아니다. |

TROUT의 §3/부록A 정규화 표기는 [현재 대수 대조](../records/0140-calendar-alignment-and-input-preflight.md#claim-27)를 함께 확인한다. 이는 현재 검토판본의 표기 주의이며 공식 코드·실험 전체의 오류 판정이 아니다. 원문상의 norm 분모를 그대로 재사용하지 않고 단위 phase 조건을 확인할 필요가 있다.

arXiv 제출/개정일은 NUG2016-07-12, TROUTv2 2021-02-10, CAPS2026-02-02, AOSNetv1 2026-06-04다. NUG표지7월13일·CAPS표지2월4일과 구별한다. AOSNetv2의 존재는 확인했지만 v1 이후 변경은 비교하지 않았다. 과거 ScienceDirect/PMC 접근 문제와 abstract-only 후보를 fulltext 검수로 승격하지 않는다.

## 원112의 실제 예측 비교로 이어짐

[원112](../records/0141-calendar-predictive-selection-and-weighting.md)에서 profile/geometry와 실제예측·선택효과를분리하고 실패기준·긍정례·손해·기간weight·정산을대조했다. [선택자와집계 안내](calendar-predictive-selection-and-weighting.md)는이번회차의새문헌검토가아니다.
