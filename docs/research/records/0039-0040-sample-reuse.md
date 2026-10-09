# 39–40: 담당 cluster를 유지하면서 학습 자료를 공유할 수 있는가

2026-09-25의 문헌·설치 코드 검토다. 예측 담당 RCTL과 실제 관측 target은 유지하고 다른 cluster의 학습 sample에 가중치를 주는 방향을 검토했다. 참 결합 밀도비의 손실 항등식은 성립하지만 기본 구조가 선행연구에 있고 TabICLv2를 추가할 효용·비용 근거가 부족해 **당시 추천안으로 채택하지 않았다**. 새 성능 실험의 부정 결과로 분류하지 않는다.

[39 계획](../evidence/0039-0040-sample-reuse/originals/SRC-0021492.md.txt) · [40 판단 원문](../evidence/0039-0040-sample-reuse/originals/SRC-0021511.md.txt) · [출처와 읽은 범위](../sources/history-024.md) · [주장 지도](../verification/history-024-primary-review.json) · [검수](../verification/history-024.md)

2026-10-09 정리 과정에서 **40의 비용 수치 68G를 해당 pinned 코드의 최대 289G 열별 처리로 정정했다**. 요청한 순서 수와 실제 생성된 순서 수가 달랐다. 원문은 그대로 보존하며 아래에서 차이를 설명한다.

## 질문·실제 수행 범위

| 항목 | 확인한 내용 |
| --- | --- |
| 출발점 | [33–35](0033-0035-process-fit-gap.md)의 분리 학습 손해와 [36–38](0036-0038-finite-information.md)의 정보량만으로 판단하기 어려운 유한 학습 문제 |
| 바꾸려던 결정 | cell의 예측 담당 cluster와 각 담당 모델이 학습에 사용하는 sample 범위를 분리 |
| 유지하려던 조건 | 실제 관측 Y·최종 RCTL core; 학습된 RCTL의 정보를 소속/공유 선택에 사용하지 않는 당시 요구 |
| 실제 수행 | 세 문헌 입수 기록, 설치된 TabICL 2.2.0 코드 확인, 정확한 수학 예제와 문헌 비교; 저장된 다운로드 5개 |
| 실제 모델 성능 평가 | 이 묶음에 없음. RCTL/TabICL 모델 호출 0으로 보고. 정리에서도 원 코드 실행·모델 호출 없음 |
| cell·기간·분할·정규화·seed | 새로운 데이터 평가가 없으므로 해당 없음. 후속 후보의 구체적 cell/분할/seed/가중치 상한은 미기록 |
| 비교 대상 | 참 joint ratio, 조건부 ratio, 단순 task-origin 분류기, 상대 밀도비 추정, 선형 source 선택; 동일 예산의 실증 비교는 미실행 |
| 지표 | 수학 예제의 절대오차, 문헌별 손실/밀도비 제곱오차/선형 예측오차. 실제 원단위·정규화 트래픽 MAE와 별개 |
| 당시 운영 한계 | 기존 RCTL 29-fit cap 유지. 이 기록이 새 29회 학습을 했거나 현재 실행을 승인한다는 뜻은 아님 |

39는 계획이고 40은 그 검토 결과다. 문헌 파일·코드·수학 예제를 각각 독립적인 성능 실험으로 세지 않는다. [보존 다운로드 코드](../evidence/0039-0040-sample-reuse/originals/SRC-0022776.py.txt)는 정적으로 읽었다.

## 참 가중치로 일치하는 것은 모집단 목적

담당 cluster의 목표 결합분포를 P, 자기 자료와 donor를 섞은 학습분포를 Q라 하자. P가 Q에 대해 절대연속이고 loss가 P에 대해 적분 가능하면, 참 가중치 w=dP/dQ에 대해 다음이 성립한다.

~~~text
E_Q[w(X,Y) loss(f(X),Y)] = E_P[loss(f(X),Y)]
~~~

Q에 P가 양의 비율로 포함되면 필요한 지지집합 포함 조건을 확보한다. 이 항등식은 MAE와 RCTL에도 적용되므로 proxy의 순위가 최종 모델에 옮겨간다는 가정과는 다른 연결이다. 그러나 가중치 추정 오차, 시계열 의존성, 최적화 오차, 미래 분포 변화 및 유한표본의 분산을 제거하지 않는다. 같은 목적을 표현할 수 있다는 사실로 성능 향상을 보장하지 않는다. 이 원리는 이 연구의 새 정리가 아니다. [Bickel §4 식1–8](https://icml.cc/Conferences/2008/papers/520.pdf)

## 세 선행연구가 이미 한 일과 남는 조건

| 문헌 | 실제 절차와 원문 위치 | 이 연구에서 재사용할 범위 |
| --- | --- | --- |
| Bickel 등, ICML 2008 | PDF3 식1–8: pool의 task 비율 p(t)>0에서 r_t(x,y)=p(t\|x,y)/p(t). PDF4–5: joint task-origin 확률을 추정하고 각 최종 task 모델을 실제 sample의 가중 loss로 학습 | 담당 모델과 자료 공유를 분리하는 기본 구조가 이미 있음. 일반 loss 항등식과 HIV 분류 응용을 구별. 이진 label용 특징식은 회귀에 그대로 복사하지 않음 |
| Kumagai 등, NeurIPS 2021 | PDF3–5 식1–8: 두 support 집합의 mean-pool 표현과 입력을 결합. (K+λI)⁻¹k로 비제약 선형 head를 구한 뒤 음수를 0으로 clipping. source-task query loss로 f/g/h·λ를 meta-train | 사전학습과 작은 support로 ratio를 추정하는 구조 자체는 신규성이 아님. 별도 meta-training이 필요한 방법이며 frozen TabICL을 그대로 사용한 결과가 아님 |
| Cherkaoui 등, arXiv v2 | PDF3–6·20: target/source 선형 ridge 통계, gain의 bias/variance, 여러 source의 다음 chunk 비교와 rank-one inverse 갱신 | 자료를 얼마나·어디서 빌릴지 선택하는 원리도 이미 있음. 선형 예측오차·분류의 probit 대용 지표 및 noise/검증자료 조건을 RCTL MAE에 그대로 옮기지 않음 |

Kumagai의 상대 밀도비 rα=pν/[αpν+(1−α)pde]는 **α>0일 때** 1/α 상한을 갖는다. 추정 head의 clipping이 제약 문제의 전역해를 보장하거나 추정 ratio까지 그 상한을 지킨다는 뜻은 아니다. support와 query는 역할이 다르지만 논문의 학습 설정에서는 support가 query에 포함된다(PDF5–6). 원문40의 “별도 query loss”를 서로 겹치지 않는 데이터라는 뜻으로 확대하지 않는다. [정식 논문](https://proceedings.neurips.cc/paper_files/paper/2021/file/ff49cc40a8890e6a60f40ff3026d2730-Paper.pdf)

Cherkaoui의 비교 판본은 2026-05-13 v2이며 선형 회귀·분류와 여러 source 선택을 다룬다. 2025-10-19 v1의 제목은 *Adaptive Sample Sharing for Linear Regression*이다. v1 전체 방법을 다시 검토한 것은 아니다. [v2](https://arxiv.org/abs/2510.16986v2), [v1 서지](https://arxiv.org/abs/2510.16986v1)

이론의 bias·variance·δ와 실제 실험의 gain−α×추정 표준편차는 다르다. 보고된 α=0.01을 1% 오류 보장으로 읽지 않는다. 정확한 bias/variance를 안다는 조건의 개별 비교 보장은 반복적·적응적 source 선택 전체의 보장과도 다르다.

원문 수식과 알고리즘의 다음 공백을 함께 보존한다. 이를 이유로 유효한 손실 항등식이나 해당 논문의 모든 결과를 기각하지 않는다.

- Bickel PDF4 Optimization Problem1에는 최대화 목적의 이차 prior 항이 양의 부호로 인쇄돼 있다. 주변 Gaussian MAP 설명과 부호가 맞지 않는다. 실제 저자 코드의 부호·실행 결과는 확인하지 않았다.
- Cherkaoui PDF18 Appendix14는 중간에 Cantelli 하측 꼬리를 사용한 뒤 최종 하한을 결론낸다. 그 중간 부등식에서 표시된 방향의 최종 하한이 따라오지는 않는다. 상측 꼬리에 Cantelli를 적용하면 필요한 조건 아래 같은 형태의 하한을 얻을 수 있다. 정리 과정에서 원문 증명 전체를 검증했다고 표시하지 않는다.
- 같은 논문 PDF17의 분산 유도는 추정계수 벡터를 Gaussian으로 둔다. PDF3의 영평균·공분산 조건만으로 이 분포가 따라오지는 않는다. 임의 noise에 같은 분산식을 보장한다고 확대하지 않는다.
- PDF20 Algorithm1은 최선 chunk를 추가하는 행에 명시적 양수 검사·거부·중단 분기가 없다. §5.3의 보호 규칙 설명과 이 의사코드 사이의 공백이다. 실제 저자 구현의 동작은 미확인이다. nmax의 rounds 표기와 비용 설명의 admitted samples 표기도 구별한다.

## 조건부 분포만으로는 복원되지 않는 정확한 예

X∈{0,1}, 두 집단 모두 Y=X+Uniform(−0.1,0.1), f(X)=0이다. 목표 P의 P(X=1)=0.1, donor에서는 0.9, 두 집단을 반씩 섞은 Q에서는 0.5다. Y\|X가 같으므로 조건부 밀도비는 1이지만 X의 질량이 다르다.

| 값 | 정확한 결과 | 의미 |
| --- | ---: | --- |
| X=0에서 E\|Y\| | 0.05 | 대칭 uniform의 절대오차 적분 |
| X=1에서 E\|Y\| | 1 | [0.9,1.1] 구간 적분 |
| 목표 P의 MAE | 0.145 | 0.9×0.05+0.1×1 |
| 혼합 Q의 MAE·조건부 ratio 적용값 | 0.525 | 0.5×0.05+0.5×1 |
| X=0,1의 참 joint ratio | 1.8, 0.2 | 목표 질량/혼합 질량 |
| joint ratio를 적용한 MAE | 0.145 | 0.5×1.8×0.05+0.5×0.2×1 |

원문40 §4.1의 값을 유리수 적분으로 재계산했다. 난수 표본을 만들지 않았고 모델을 적합하지 않았다. 실제 RCTL이 상수라는 주장이나 실제 네트워크의 성능 수치가 아니다. [계산 값](../evidence/0039-0040-sample-reuse/document-tables.json) · [검산 결과](../verification/history-024-portable-check.json)

## 설치된 TabICL 2.2.0을 ratio에 쓸 때의 한계

`quantile_dist.py`의 log_prob는 존재한다. CDF 위치에서 분위수 함수 Q의 기울기를 구해 −log Q′(F(z))를 반환하며 tail/spline 처리와 기울기 clipping을 포함한다(816–1102행). 중앙값·MAE·중앙 구간 coverage가 좋다는 사실이 작은 구간의 밀도 및 밀도비 정확성을 보장하지 않는다. [고정 코드](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/_model/quantile_dist.py#L1057)

`score_samples`는 한 순서 안에서는 조건부 log density를 합하고 순서 간에는 평균 후 지수화한다. 따라서 순서별 joint density의 **기하평균**이다. 각 density가 정규화돼 있어도 기하평균의 적분이 항상 1은 아니다. N(−a,1), N(a,1)의 기하평균은 exp(−a²/2)N(0,1)이므로 적분은 a=0,1,2에서 각각 1, 약0.606530660, 약0.135335283이다. context마다 다른 상수가 남으면 두 outlier score의 비율은 곧바로 필요한 정규화 density ratio가 되지 않는다. outlier 용도의 실패를 주장한 것이 아니다. [고정 코드 183–228행](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/_unsupervised/unsupervised.py#L183)

이산 시간과 sin·cos 등 결정적 관계가 있는 열은 모든 열을 좌표로 삼는 전체 공간에 연속 밀도가 존재한다는 가정과 맞지 않을 수 있다. 공통 기준 측도에서 ratio를 구성하거나 직접 task-origin 분류를 설계해야 한다. 이 진단을 실제 데이터의 ratio 추정 성공으로 간주하지 않는다.

## 비용 정정: 요청 4개와 생성 17개 순서의 차이

원문40 §4.4는 입력16개와 Y의 D=17열, P=4순서에서 최대68G 작업으로 보고했다. 그러나 저장된 두 소스를 연결하면 다음과 같다.

1. unsupervised.py 222행은 method를 지정하지 않고 Shuffler(D).shuffle(P)를 호출한다.
2. preprocessing.py 812–881행의 기본 method는 latin이다. D≤4000이고 P≠1인 이 분기에서는 P개로 자르지 않고 Latin square 전체를 반환한다.
3. 883–916행의 재귀는 1×1에서 한 행·열씩 더해 D×D를 만든다. shuffle·transpose도 크기를 유지한다. D=17에서는 순서17개다.
4. score_samples도 이 목록을 자르지 않으므로 최대 열별 처리 수는 17×17=289, G개 context면 289G다. 원문68G는 이 pinned 구현의 상한이 아니다.

이것은 원 소스 실행 없이 수행한 정적 분석과 산술 정정이다. [순서 생성기](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/_sklearn/preprocessing.py#L785) · [정적 대조 근거](../verification/history-024-code-check.json)

바깥 열 반복문은 학습 target의 non-NaN 값이 5개 미만이면 건너뛴다. 원문40의 상수 열 생략 설명과 달리 이 반복문에는 상수 열이라는 이유만으로 생략하는 분기가 없다. 289는 끝까지 처리할 경우의 열별 반복 상한이며 모델 forward 횟수·학습 횟수·실측 시간과 같지 않다. 기본 내부 ensemble8, query 행, 조건별 준비, donor 추가 후 RCTL sample 처리 비용이 따로 있다. 가중치를 한 번 로드해 공유해도 각 조건의 fit/predict 준비까지 한 번으로 줄지는 않는다. 첫 열의 빈 conditioning에는 random dummy를 넣는 코드가 있으나 정리에서 실행하지 않았다.

| 비용 근거 | 확인값 | 해석 범위 |
| --- | ---: | --- |
| 과거 입수 PDF | 3편·44쪽·1,673,675 bytes | 저장 manifest와 현재 파일 identity; 논문 전체 독해량 아님 |
| 입수 성공 항목 | HTTP200 5개 | PDF3·v2 HTML·abs HTML; 시작 marker 있음 |
| 다운로드 경과 시간 | 미기록 | 코드의 3개 worker·30초 timeout·10MiB 제한을 실측 시간으로 쓰지 않음 |
| source40 보고 작업 수 | 68G | 요청 순서4를 사용한 원문 계산, pinned 구현과 불일치 |
| 코드로 정정한 최대 열별 처리 | 289G | D17·기본 latin·요청4·조건별 처리 완료 가정; 실제 모델 호출/시간 미측정 |
| 선형 sharing 논문의 보고 비용 | 초기 O(d³+nT d²), chunk O(c d²) | greedy 비교에는 active source 수 추가. nmax의 단위 차이와 전 과정 비용을 별도 확인 |

## 재사용과 다시 검토할 조건

같은 수학 예제는 [모델 없는 검산](../evidence/0039-0040-sample-reuse/README.md)으로 확인할 수 있다. 기존 importance-weighted multi-task learning·relative DRE·source별 greedy sharing을 다른 이름의 새 원리로 다시 제출하지 않는다.

후속 설계에는 단순 source 분류기나 직접 ratio 추정이 놓치는 실제 상황, Tab 회귀 분포가 추가하는 정보, 추정 weight의 유한표본 손해, donor 포함 RCTL 총비용을 적어야 한다. 입력16+Y·순서 수 등의 가정도 실제 pinned 구현으로 확인한다. 참 ratio 항등식이나 빠른 rank-one 갱신만으로 이 조건을 충족했다고 하지 않는다.

39–40 당시에는 이 조건을 충족한 추천안을 확보하지 못했다. 41이후 후속 판단, 세 논문의 나머지 페이지·저자 코드, 전체 과거 실패 비용과 팀 자료 접근 검수는 미완료다. 지정 문헌·설치 코드 검토를 전체 논문·전체 라이브러리 검토로 집계하지 않는다.
