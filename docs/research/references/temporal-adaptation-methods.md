# 기록17의 세 적응 방법 비교

[당시 판단](../records/0017-adaptation-literature.md)과 [출처 manifest](../evidence/0017-literature/manifest.json)를 연결한다. 아래는 지정 방법의 비교다. 논문 전체의 옳고 그름이나 성능 순위를 판정한 문서가 아니다. DOI·날짜는 [공식 판본 metadata](../sources/history-011.md)에 따른다.

## MGSTC — 손실 감시와 가중치 갱신

Fu·Liu·Xie·Huang의 [v1](https://arxiv.org/html/2508.08281v1#S4.SS3)은 최근 표본 memory B와 과거 H를 사용한다. Fine-tuning은 현재 labeled 표본과 B replay의 가중 MSE로 한 번 갱신하고, aggressive 단계는 B·H와 변형한 과거 입력으로 여러 epoch를 수행한다. 감시는 손실 분포에 의존한다. §3.2의 drift는 joint `P(X,Y)` 변화이며, Fig3의 휴일 차이를 조건부 변화 증명으로 읽지 않는다. **H011-C02·H011-C03**

Table2/§5.1의 Milan은900개 series·8,928개10분 표본이며 SMS in/out·call in/out·Internet을 합한다. Train/validation/test는5/2/55일이다. 기록16–17의 입력·척도·분할과 다르다. **H011-C04**

재사용 전 확인할 표기는 세 가지다. §4.3.1은 평균이라 부른 `bar_mu`를1/B 없는 합으로 표시하고, σ를 variance라 하면서 σ/√B를 쓰며, 식16은 표준화량에 inverse Gaussian CDF를 적용한다. 이를 검증된 통계 검정으로 채택하지 않았다. 본문 감시용 B는 손실, Algorithm1의 B/H는 표본 FIFO(100/256)로 설명돼 역할 구분이 필요하다. PDF Fig5의 손실식 번호14/15는 본문17/18과 다르다. HTML 수식도 대조했지만 Fig5 HTML 이미지 자체의 표기까지 확인한 것은 아니다.

## PID — 고정 예측기에 출력 보정

Sengendo·Bettouche·Ali·Kassler·Granelli의 [v1](https://arxiv.org/html/2608.08332v1#S3)은 관측한 과거 오차의 현재값·누적·차분으로 다음 HiSTM 출력에 보정값을 더한다. Online backpropagation은 없지만 예측과 실제 target이 필요하다. 본문 §III.A/Fig1은 truth−corrected prediction, Algorithm1의9/19행은 반대 부호다. `Correct`의 구현을 확인하기 전에는 부호를 통일하지 않는다. **H011-C05**

§III.C의 cell당200 Optuna trials는 목적함수의 평가 길이 `N_c=min(|T_c|,200)`와 다른 수다. §IV.B의 backbone 분할은 시간순70/15/15다. **PID 계수 선택과 최종 평가가 별도 기간인지**는 읽은 방법 절에서 확정하지 못했다. 누수가 있다고 단정한 결과도 아니다. **H011-C06**

| TableIV 항목의 검색용 별칭 | 주입 방식 |
|---|---|
| HotspotLinearLocal | 국소 hotspot의 점진적 변화 |
| HotspotSuddenGlobal | 전역 hotspot의 급격한 변화 |
| JointSTSuddenGlobal | 회전하는 시공간 변화·급격한 발생 |
| JointSTLinearGlobal | 회전하는 시공간 변화·점진적 발생 |
| JointSTRecurring | 반복 시공간 변화·sinusoidal 패턴 |

검색용 별칭은 category·type·scope를 이어쓴 표현이며 저자 코드의 구현 ID로 확인한 것은 아니다. Nominal severity는0.05/0.15/0.30이며 실제 변화량을 측정한 값과 구분한다. 이 시나리오는 자연 drift의 증명이 아니다. TableIII 성능 수치와 Figure3 결과 그래프의 전수 검수·재현은 하지 않았다. **H011-C07**

## Joint QoS — 소속과 예측 모델의 교대 최적화

Stenhammar·Fodor·Fischione의 [v1](https://arxiv.org/html/2604.12903v1#S3)은 MSE·분포 일관성·cluster수 벌점을 결합한다. 공유 base는 고정하고 cluster별 마지막층과 소속 A를 교대 갱신한다. A를 행별 simplex로 완화하고 cluster수 대신 nuclear norm을 사용한 뒤 argmax로 소속을 정한다. 따라서 모델 손실에 의존하는 완화 문제다. **H011-C08**

§IV.C의 수렴 진술은 가정1–5 아래 critical point에 관한 것이며 전역최적 보장이 아니다. §V.A는 Hellinger kernel K에서 `D=diag(K1)-K`인 graph Laplacian을 만든다. 임의의 쌍별 거리행렬이 PSD라고 주장한 것으로 바꾸지 않는다. **H011-C09**

실험 조건은 ns-3/Sionna의 12cell·30차량, 1초 수집, 이전15분 통계와 현재 측정으로1시간 뒤 QoS 분포 예측이다. Latency·jitter·RSRP를 대상으로 하며 covariance는 Cholesky로 구성한다. 70/10/20 분할의 시간 순서와 고정 seed의 숫자는 확인되지 않았다. **H011-C10**

식6의 penalty는 β‖A‖*지만 식11은 계수1로 표시되고 Algorithm1에는 threshold τ가 등장한다. 같은 τ를15분 update period에도 써서 **β·step size·threshold·주기의 대응**을 구현 전에 확인해야 한다. 해당 PDF와 HTML에서 같은 표기를 확인했으며, 저자 코드의 오류를 판정한 것은 아니다. §IV.D의 통신량은 파라미터 수에 따른 예시 산술이며 TabICL/RCTL의 실측 실행 비용으로 인용하지 않는다.

## 이 기록에서 남기는 판단

세 문헌은 적응을 위해 서로 다른 정보를 사용하고 다른 대상을 갱신한다. 기록17의 제한적 결론은 유지하되, 새로운 실험의 조건·비용·재배정 근거가 무엇인지 별도로 명시한다. [검수와 미완료 범위](../verification/history-011.md)에는 논문 전체 검토와 성능 재현을 완료로 세지 않은 이유가 있다. **H011-C11**
