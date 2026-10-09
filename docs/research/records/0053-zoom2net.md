# 53·55 — Zoom2Net의 거친 관측 복원과 제약 보정 비용

Zoom2Net은 **여러 거친 관측과 알려진 측정 함수를 이용해 과거의 세밀한 시계열을 복원**한다. 정밀 관측으로 학습한 Transformer, 지식 제약을 포함한 손실, 출력 제약 보정, 모호한 학습 정답의 묶음을 결합한다. 일부 관측으로 다른 cell의 이력을 복원하려는 [53 계획](../evidence/0053-moghadas-thesis/originals/SRC-0021782.md.txt)과 가까운 기존 원리다. 미래 트래픽 예측이나 RCTL 학습 표본 공유의 성능을 검증한 연구는 아니다.

[55 판단 §3](../evidence/0052-0054-partial-observation/originals/SRC-0021824.md.txt)은 이미 학습 필요성·실시간 범위 제외·Transformer와 제약 보정의 비용 차이를 기록했다. 이번 검토는 입력 가용성, 복원의 모호성, 비교 기준과 손해, 비용 및 수식의 적용 조건을 보완한다. **측정값과 일치하는 그럴듯한 이력은 실제 정답 이력과 같다는 보장이 없다.** 이를 [54 복원 진단](0052-0054-partial-observation.md)의 결과나 최종 미래 예측 이득으로 바꾸지 않는다.

## 출처와 실제 읽은 범위

Fengchen Gong, Divya Raghunathan, Aarti Gupta, Maria Apostolaki, *Zoom2Net: Constrained Network Telemetry Imputation*, ACM SIGCOMM 2024. [DOI](https://doi.org/10.1145/3651890.3672225) · [저장본의 취득 URL](https://cs.stanford.edu/~keithw/sigcomm2024/sigcomm24-final114-acmpaginated.pdf). 검토 PDF는 1,120,010bytes, SHA-256 `dcf0b6807d91801ba9f4a7324441563eee0c17083af354e46c94f29e1a6947b9`다. 2026-09-26 취득 로그의 HTTP200·크기·해시·14쪽과 일치한다.

PDF 물리 p1–14(인쇄 764–777)의 텍스트를 모두 읽고 p3–12의 시각 자료를 확인했다. Fig1–12, Table1, Fig3b·4b의 표, 식1, 명명된 제약 11개와 나머지 표시 수식을 포함한다. 참고문헌 54개를 각각 읽었다는 뜻은 아니다. 저장 TXT14쪽은 PAGE 표식과 쪽 앞뒤 공백을 제외한 본문이 현재 추출문과 같다. 과거 p5·7·12 미리보기도 읽었으며 1020×1320의 원 이미지와 1347×1743의 현재 렌더를 바이트 중복으로 세지 않는다.

기존 계획·판단·취득/열람 로그 사본5개를 재사용하고 PDF·TXT·미리보기3장은 metadata와 정식 링크로 연결한다. 새 원문 복사는 없다. [출처 범위](../sources/history-037.md) · [검수](../verification/history-037.md). 저자 모델을 실행하거나 독립 성능 재현을 수행하지 않았다.

## 입력·출력·학습과 운영 조건

| 항목 | 원문에서 확인한 범위 | 재사용할 때 남는 조건 |
|---|---|---|
| 과제 | 측정 함수 S가 만든 거친 시계열 `T_s=S(T_r)`에서 세밀한 이력 `T̂_r` 복원(p3–4) | 미래 관측 없이 다음값을 맞히는 forecasting과 구분 |
| 학습 자료 | 대상 네트워크에서 짧은 기간 수집한 정밀 관측·packet trace와 이를 낮은 해상도로 바꾼 입력 | 정답을 전혀 관측하지 못하는 환경이나 모든 미지 분포에 바로 적용된다는 뜻 아님 |
| 추론 입력 | 같은 분석 구간의 여러 관련 관측. 측정 함수와 제약을 알고 있다고 가정 | 구간 뒤쪽 관측도 이용하는 offline 분석. 실시간 사용은 원문의 비목표 |
| 시간 정렬 | 완전한 동기화·같은 granularity를 요구하지 않는다고 설명(p4·6) | 미지의 시차가 운영 제약을 깨뜨릴 수 있음을 저자도 인정 |
| 분할·정규화 | min–max, 학습80%/평가20%(p8) | 시간순 여부·정규화 적합 범위·window 겹침·seed·검증 분리 미기록; 독립 확인도 미수행 |
| 구조·환경 | encoder1층+linear, attention head4개, decoder 없음. Python3.8/PyTorch2.0, Tesla T4 16GB | 다른 시점 입력을 사용하는 구조를 causal 예측기의 입력 조건으로 옮기지 않음 |
| 최적화 | Adam, 시작 LR=`1e-4`, 10epochs 개선이 없으면 LR×0.1; 사례당 학습 평균20분 | 전체 epochs·모든 계수·반복 수·기본 모델 추가 학습을 포함한 비용 범위 미확인 |

논문은 하나의 거친 입력에 여러 정밀 정답이 대응할 수 있음을 핵심 문제로 둔다. 추가 관측은 가능한 정답을 줄일 수 있지만 유일한 원신호를 보장하지 않는다. Fig3·4의 예시 값도 그대로 보존한다. 아래 값은 예시 신호이며 모델 성능 지표가 아니다.

| 그림·queue | Max Qlen | Packet Drop | Packet Sent |
|---|---:|---:|---:|
| Fig3b Queue1 | 0.895 | 0.05 | 0.74 |
| Fig3b Queue2 | 0.87 | 0.69 | 0.98 |
| Fig4b Queue3 | 0.80 | 0.06 | 0.60 |
| Fig4b Queue4 | 0.92 | 0.086 | 0.64 |

Fig3은 동일한 최대값이라고 설명하지만 인쇄표의 0.895와0.87은 0.025 차이가 있다. Fig4도 거의 같은 입력의 예이지 세 열이 정확히 같은 것은 아니다. 정확한 collision의 개념, 유사한 입력을 묶는 구현 기준, 그림의 근사 예를 구분한다.

## 기존 방법의 구성과 재사용 경계

| 구성 | 실제 역할 | 한계·추가 비용 |
|---|---|---|
| Knowledge Augmented Loss, KAL(p6–7) | MSE+λEMD에 측정 등식·운영 부등식의 벌점을 추가. 증강 Lagrangian으로 학습 | 손실만으로 모든 제약 충족을 보장하지 않음. EMD 가중치 λ와 제약별 승수 λ는 역할이 다름 |
| 제약 갱신(p7) | 벌점 μ=`1e-3`, 제약 승수0에서 시작. 모델 수렴 후 μ×1.5·승수 갱신, 위반 감소가 멈출 때까지 반복 | 정확한 종료 허용치·실행별 반복 수·해의 보장 미확인 |
| Constraint Enforcement Module, CEM(p7) | Gurobi의 ILP로 지정 제약을 맞추면서 Transformer 출력과의 L1 차이를 줄임. 직접 sample된 시점은 이 차이 합에서 제외 | 정수화·논리식 선형화·solver 허용 오차·불가능한 제약 처리와 실제 코드는 미확인. 충족하는 제약의 범위가 실제 정답의 보장과 같지 않음 |
| Target refinement(p7–8) | 기본 Transformer를 먼저 학습. 출력이 가깝고 원 정답이 먼 학습 사례를 묶어 집합 내 가장 가까운 정답과의 손실 사용 | 학습 자료에만 적용. 기본 모델 학습 비용이 필요하며 거리·threshold·정제 비율은 미기록. RCTL 소속 공유와 다른 결정 |

측정 지식은 `Φ(T̂_r,T_s)=T_s−S(T̂_r)=0`, 운영 지식은 `Ψ(T̂_r,T_s)≤0`으로 표현한다. 상관계수를 통해 관련 신호를 찾으라는 설명을 모든 관측에 성립하는 논리 규칙의 증명으로 사용하지 않는다.

| 제약 | 사례와 의미 | 적용 조건 |
|---|---|---|
| C1·C2(p9) | 최대 queue length와 직접 sample한 queue length 일치 | 실제 측정 함수·시각·단위가 맞아야 함 |
| C3(p9) | 비어 있지 않은 ms 수 NE가 해당 구간의 전송 packet 수 이하 | work-conserving scheduler라는 저자 가정에 더해 시간 단위·서비스 조건을 확인해야 함 |
| C4–C6(p9) | 복원 link utilization 합이 측정 합과 같고 재전송·혼잡 traffic 합 이상 | 합산 구간·단위·정규화 대응 확인 필요 |
| C7(p9) | 혼잡 traffic이 있으면 복원 최대값이 bandwidth의 절반 이상 | 논문이 채택한 운영 제약이며 모든 네트워크의 보편 법칙으로 확대하지 않음 |
| C8·C9(p11) | 짧은 측정 구간에 대한 MSS×cwnd 전송량 상한과 receiver-window 대기 시 합0 | RTT·elapsed time·cwnd 단위·대기 시간의 실제 정의 확인 필요 |
| VPN 제약(p11) | 정방향/역방향 inter-arrival time의 최솟값·최댓값, 최대 packet length 일치 | packet trace의 모든 고유 정보를 되찾는다는 뜻 아님 |

## 비교한 자료와 지표

3개 사례가 4개 자료를 사용한다. 아래 수량은 저자가 **학습 자료**라고 보고한 data points이며 원자료 재집계가 아니다. 80:20 설명만으로 미기록 전체 표본 수나 독립 시계열 수를 만들어내지 않는다.

| 사례·자료 | 학습 data points | 거친 입력 → 정밀 출력·다운스트림 과제 |
|---|---:|---|
| Case1 합성 ns-3(p9) | 8000 | TridentII·leaf-spine·Dynamic Thresholds, web search/incast, DCTCP/Cubic. 50ms의 최대/주기 queue length·packet sent/drop → 1ms queue length·burst 특성 |
| Case1 Meta(p9) | 20000 | 50ms 합산 link utilization·재전송·혼잡·connection 수 → 1ms link utilization·burst 특성 |
| Case2 M-Lab(p10–11) | 5000 | 평균250ms NDT/TCPInfo/BBRInfo → 10ms sending rate·300KB–10MB의 10개 웹사이트 loading time 추정 |
| Case3 VPN(p11) | 3300 | trace에서 추출한 집계 특징 → 평균20packet의 도착시각·길이. 복원 duration/rate 특징을 원 특징에 더해 MLP 분류 |

비교군은 coarse data를 IterativeImputer로 크기에 맞춘 방법, KNN, MSE만 쓰는 Plain Transformer, BRITS다. Coarse 기준은 최대값을 구간 중간에 놓고 BRITS는 sum/max를 구간 끝에 배치한다. 따라서 “원 관측 그대로”와 특정 보간·배치 규칙을 구분해야 한다. KNN의 K 선택은 실험으로 조정했다고만 적혀 있다. VPN은 주기 sample이 없어 coarse 기준과 BRITS를 제외했다.

p8의 지표는 `|t−t_real|/t_real`를 test 자료에 평균한 상대 오차다. `t_real=0` 등의 처리는 미확인이다. p9는 시각화를 위해 각 지표의 상대 오차를 [0.1,0.9]로 정규화한다고 설명한다. **정규화한 막대 높이의 비율을 원단위 오차 감소율로 다시 계산하지 않는다.** Fig11에는 0에 가까운 값도 보이므로 적용된 정규화의 정확한 구현은 추가 확인이 필요하다.

## 성능 주장과 반례를 함께 보기

다음 비율은 저자 본문 보고다. 원 배열·정규화 계수·평균 산출표를 확보하지 못했으므로 독립 재계산한 결과로 표시하지 않는다.

| 원문 위치 | 보고된 비교 | 보존할 조건·한계 |
|---|---|---|
| p8–10·Fig8/9 | 구조 관련 지표33–53%, downstream 평균38%, coarse 기준 대비 최대5배 | 자료·지표·비교군이 다른 숫자를 하나의 forecasting 개선율로 합치지 않음 |
| p9–10·Fig8 | EMD·autocorrelation·99th percentile에서 이득, Meta 평균33% | Plain Transformer의 MSE가 더 낮다. MSE 우위까지 주장하지 않음 |
| p10·Fig9a/b | 합성 burst 특성10–88%, 합성 위치 평균 오차4%, Meta 평균30% | Meta의 position 막대에서는 Plain Transformer 오차가 Zoom2Net보다 낮다. 모든 세부 지표의 우위로 확대하지 않음 |
| p10 | 학습에 없던 traffic·혼잡 제어 조합에서 평균30% 더 좋은 결과 | 지정한 합성 조합 비교이며 새로운 실제 네트워크 전체의 일반화 보장 아님 |
| p11·Fig9c | M-Lab loading time 정확도 평균43%, 구조 지표 평균44% | 작은 byte 전송의 변화는 정규화 후 잡기 더 어렵다고 저자가 설명 |
| p11·Fig10 | VPN 복원 특징 추가 시 정답 특징과 비슷한 분류 결과, 구조 지표 평균53% | 원래 특징과 추가 특징의 합을 사용하며 각 경우10회. 모든 median 최고·통계적 유의성·원 trace 정확 복원은 확인되지 않음 |

Zoom factor는 거친/정밀 granularity의 비다. Meta에서25·50·100을 비교했다. p8은 factor가50만큼 커질 때 정확도가0.4%/7% 악화한다고 쓰지만 p12는50→100에서 정확도가 같은 비율로 증가한다고 쓴다. Fig11의 축은 **상대 오차**이며 여러 항목이50→100에서 커진다. 이 문구 차이를 숨기거나 고배율의 보편적 정확도 개선으로 요약하지 않는다. Factor100이 다른 방법의 factor50보다32%/23% 낫다는 문장도 서로 다른 배율의 비교이고 원 배열로 재계산하지 못했다.

## 최초 학습·추론·제약 보정 비용

Table1(p12)의 20개 필드를 전사했다. 아래10개 시간은 저자의 인쇄값이며 현재 환경의 측정이 아니다.

| Window size(초) | Zoom factor | Transformer(초) | Transformer+CEM(초) |
|---:|---:|---:|---:|
| 0.25 | 50 | 0.00054 | 0.145 |
| 0.5 | 50 | 0.00056 | 0.215 |
| 1 | 50 | 0.00094 | 0.394 |
| 1 | 25 | 0.00070 | 0.532 |
| 1 | 100 | 0.00052 | 0.285 |

같은 행의 전체/Transformer 비율은 차례로268.52·383.93·419.15·760.00·548.08배다. 이는 **제약 보정을 포함한 경로와 단독 모델의 비교**이며 다른 방법보다 느린 배율이나 순수 solver 측정값이 아니다. “1ms 미만”은 모델 단독에 해당하고, 표의 전체 경로는0.145–0.532초다. Factor50에서는 window가 커질수록, 1초 window에서는 factor가 작아질수록 전체 시간이 증가한다.

Gurobi는 coarse interval별 여러 process를 사용한다. p8의 예는1ms 출력·1000ms window·factor50에서20process다. 병렬화된 wall time을 총 CPU 작업량으로 바꾸지 않는다. CPU 기종·코어 수·solver 설정과 실제 수집·저장·전력 비용은 미확인이다. 학습 평균20분, refinement용 기본 모델 학습, 제약별 반복 학습의 포함 범위도 분리해 확인해야 한다. 원문의 비목표인 실시간 운영이 입증됐다고 하지 않는다.

p12의 confidence는 입력당 Monte Carlo dropout **100회 forward** 출력의 표준편차다. Fig12의 정제 자료는 불확실성 분포가 더 낮은 쪽으로 이동하지만, 그것만으로 실제 정답 복원·calibration·예측 구간의 신뢰성을 입증하지 않는다. 이100회가 Table1 시간에 포함됐는지도 미확인이다. 이번 아카이브 작업에서 forward나 무작위 생성을 실행하지 않았다.

## 남은 원문 차이와 재검토 조건

위의 Fig3 값과 zoom factor 표현 외에도 p4는 Nyquist보다 높게 sample해서 정보 손실이 난다고 쓴 뒤 같은 쪽에서 낮은 rate의 모호성을 설명한다. p6의 운영 예는 enqueued 수와 sent 수를 비교하지만 p5와 C3는 dequeued·비어 있지 않은 시간의 관계를 쓴다. p12의 합성 Case1 참조는 §6.4로 표기돼 있으나 실제 절은 §6.2다. 이러한 인쇄·조건 차이를 실제 구현 실패로 확정하지 않는다.

동일 연구를 반복하지 않으려면 새 제안은 다음 차이를 먼저 명시해야 한다. **어떤 관측을 생략하고, 어떤 관련 관측과 정밀 학습 정답을 얻을 수 있으며, 복원된 이력의 어느 정보가 최종 미래 예측에 필요한가.** 동일 입력·시간 분리·비용 조건의 단순 복원 기준과 비교하고, 그럴듯한 이력이 최종 예측을 해치는 경우도 남겨야 한다. 이 조건은 후속 설계 기준이며 새 모델 실행 승인이 아니다.

[SRSSS](0053-srsss.md)는 센서 선택·동시값 선형 복원, [Moghadas 학위논문](0053-moghadas-thesis.md)은 선택 입력에서 군집 전체 미래값 예측을 다룬다. 세 과제의 목적·가용 관측·비용이 다르다. NETNOMOS·TabICL imputation·Ciena 접근 문제와53/55 전체 종합은 계속 검토한다. [주장 근거](../verification/history-037-claims.json) · [수치 검사](../verification/history-037-numeric-check.json) · [출처 검사](../verification/history-037-primary-check.json) · [명세](../evidence/0053-zoom2net/manifest.json).
