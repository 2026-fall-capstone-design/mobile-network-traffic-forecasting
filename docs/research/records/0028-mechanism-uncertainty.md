# 28 · 관계 차이와 추정 불확실성의 적용 조건

2026-09-25의 [원문 28](../evidence/0028-mechanism-uncertainty/originals/SRC-0021257.md.txt)은 네 문헌과 고정 코드의 검토 기록이다. 새 알고리즘을 채택하거나 실행한 결과가 아니다. [26·27](0026-0027-observable-states.md)의 상태별 손해를 출발점으로, **단순 방법이 남긴 손해 → TabICL이 제공하는 추가 정보 → 바뀌는 소속 결정 → RCTL 평가**를 연결할 근거를 요구했다. 문헌 이름이나 모듈을 추가하는 것만으로 이 연결이 성립했다고 보지 않았다. [C01·C14]

이번 아카이브는 원문 66행, 원 manifest 두 개, 저자 코드 세 개를 읽고 문헌의 지정 구간과 대조했다. PDF 세 편의 선택 텍스트 21쪽·시각 13쪽, CLT HTML의 지정 절을 확인했으며 논문 전체·모든 증명·실험을 검증한 것은 아니다. Vario 첫 페이지의 서지 구간도 추가 확인했다. [출처와 읽은 범위](../sources/history-020.md), [주장별 근거](../verification/history-020-primary-review.json), [검수](../verification/history-020.md)를 함께 본다.

## 무엇을 물었고 어디까지 수행했는가

| 항목 | 확인한 범위 |
|---|---|
| 연구 질문 | 관측된 예측 손해가 cell 간 관계 차이인지, 추정 부족인지, 공통 예측기가 놓친 정보인지 구별할 수 있는가? |
| 실제 수행 | 문헌·정적 코드 검토, 적용 가정 비교, 반례의 논리·산술 확인 |
| 자료·분할·입력 | 새로운 실험 자료나 TRAIN/VAL/TEST를 만들지 않았다. 앞선 26·27의 고정 개발 자료는 연결된 기록에서 확인한다. |
| 모델·seed·비교군 | 이 기록에서 실행한 모델·seed·성능 비교군은 해당 없음. 아래 모델 설정은 문헌 보고값 또는 정적 코드값이다. |
| 성능 결과 | 신규 TabICL·RCTL 성능값 없음. 논문 보고값을 우리 트래픽의 결과로 옮기지 않았다. |
| 비용 | 문헌 보고 시간과 prefix 규모의 산술만 확인. 당시 검토 작업 자체의 실측 총시간은 미기록. 이번 모델 실행·무작위 실험 0회. |
| 당시 판단 | posterior 생성, CLT 병합 확신도, residual 분할의 단순 대입안을 추천하지 않음. 모든 관련 방법을 영구 기각한 판단은 아님. |

## 후보가 제공하는 정보와 남은 연결

| 방법 | 제공하는 정보·바뀌는 대상 | 당시 판단의 근거 | 다시 검토하려면 |
|---|---|---|---|
| TabMGP | 예측 규칙에서 유도한 분포의 통계량 posterior | 생성 X·Y가 context에 누적되고 비용·시계열 가정이 추가됨 | 필요한 관계 통계량과 소속 결정의 연결, 충분한 정밀도와 실제 비용을 입증 |
| predictive CLT / UD | 고정 query CDF의 prefix 변화로 추정한 covariance | TabICL adapter가 이미 있음. prefix 비용·모델 오차·정리 조건·RCTL 연결이 남음 | 어떤 결정이 달라지는지, 적용 조건과 대조군, 비용을 명시 |
| Vario | 환경별 회귀 계수의 공통 부분·차이를 MDL로 분할 | 관계 clustering·전체에서 분할·설명 비용은 기존 요소 | 비선형 정보가 기존 선형 추정과 비교해 필요한 이유와 개선 근거를 제시 |
| two-stage global forecasting | global residual 특징으로 묶고 예측기를 보완 | residual 분할 자체는 선행 구조. 공통 모델 오류와 cell 차이를 구별해야 함 | RCTL과 독립인 소속 정보, reference 오류의 대조, 고정 RCTL 효용을 확인 |

세부 방법과 공식 링크는 [문헌 비교](../references/mechanism-uncertainty.md)에 있다. 이것은 현재 연구의 추천안·실행 계획을 승인한 표가 아니다. [C02–C10·C14]

## 예측 폭과 통계량 posterior는 다른 질문이다

TabMGP의 대상은 다음 Y의 범위 자체가 아니라 한계 예측분포에 대한 통계량 `θ(F)`다. v3 Algorithm 1은 확장되는 `X₁:ᵢ`의 경험분포를 사용한다. 코드의 `get_x_new(x_prev)`도 이미 생성된 X를 포함하므로, 매 단계 원래 X만 고정해 뽑는 방식이라고 요약하지 않는다. 생성 Y와 X를 다음 context에 넣고 adapter가 `fit`을 호출하는 것은 이 코드에서 ICL context를 준비하는 절차다. foundation model의 가중치를 재학습했다는 뜻으로 세지 않는다. [C02]

§3.2의 경로 안정성·coverage·수축 진단은 고용량 모델에서 martingale 조건을 증명한 결과가 아니다. 논문 자체도 느린 수렴과 작은 표본 수/차원 비(n/p)에서의 분류 undercoverage를 남긴다. 이 근거를 겹치는 트래픽 lag 행의 자동 보장으로 옮기지 않는다. 참 조건부분포를 정확히 알아도 미래 잡음의 분산은 남으므로, 넓은 예측 구간만으로 “함께 학습할 상대를 모른다”고 판단할 수 없다. 마지막 문장은 원문 28의 적용 추론이다. [C03·C13]

## CLT 정리와 실제 코드의 범위를 구별한다

논문 §4는 `γ∈(0,1]`의 covariance 추정식을 제시하고 적용에서는 `γ=1`을 가정한다. 이 상수가 TabICLv2 트래픽에서 확인됐다는 뜻이 아니다. 고정 query의 CDF를 각 context prefix에서 계산하는 `Vₙ` 방식과, 다음 행을 생성하는 별도 `Uₙ` Monte Carlo 경로도 구별한다. 전체 자료의 행 순서 불변성이 prefix 경로의 순서 불변성을 보장하지 않으며, 논문은 context 순열을 사용한다. [C04·C06]

고정 commit의 `posterior.py`는 `g₀=NaN`을 두고 실제 `compute_vn`에서 `k=2,…,n`의 `k² ΔₖΔₖᵀ`를 **n−1로 평균**한다. 초기·상수 target prefix는 별도 처리한다. `tabicl_adapter.py`의 `TabICLRegressorPPD`는 이미 `raw_quantiles` → `QuantileDistribution` → CDF를 구현한다. 세 코드의 전체 텍스트와 원격 고정 commit의 바이트를 확인했으며, import·실행·현재 패키지 호환성 확인은 하지 않았다. “TabICL에 불확실성 분해를 추가”한 사실만으로 새로운 원리를 주장하기 어렵다는 것이 당시 판단이다. [C04]

Theorem 5.2는 5.1의 조건에 `Xₙ₊₁ ⟂ Y₁:ₙ | X₁:ₙ`을 추가한다. 일반적인 lag 행에서 `Xₙ₊₁,last=Yₙ`이고 조건부 분산이 유한하고 양수이면,

`Cov(Xₙ₊₁,last, Yₙ | X₁:ₙ) = Var(Yₙ | X₁:ₙ) > 0`.

따라서 이 추가 조건을 자동 충족한다고 할 수 없다. 그러나 **Theorem 5.3은 5.2의 추가 독립 조건을 요구하지 않는다.** 5.1의 수렴 조건과 별도의 drift 속도·moment·양의 정부호 극한 등의 조건을 사용한다. 부호 있는 drift 꼬리합 조건, L1 지배와 moment 조건을 유한 경로의 진단만으로 확인한 것도 아니다. 이 lag 반례로 5.3 전체를 반박했다고 쓰지 않는다. [C05·C11]

## residual 자기상관은 서로 다른 관계의 충분조건이 아니다

Vario의 context는 환경·domain이다. TabICL의 입력 sample 묶음과 다르다. 같은 DAG와 잡음 독립 조건 아래 공변량 부분집합별 선형 계수를 추정하고, 공통 계수와 환경별 편차의 설명 비용으로 partition을 비교한다. top-down 분할도 기존 절차다. 조건부 선형 근사의 정리를 임의의 비선형 관계·유한 표본의 보장으로 확장하지 않는다. [C07·C08]

Two-stage 방법은 global residual의 Ljung–Box 검사와 특징을 사용한다. 그러나 모든 cell이 같은 AR(1) 관계를 가져도 lag를 무시하는 공통 reference의 residual에 자기상관이 남을 수 있다. 원문 28의 이 논리를 수치 없이도 확인할 수 있으며, [산술 기록](../verification/history-020-logic-check.json)은 `φ=1/2`, innovation variance `1`, reference `0`인 정상 과정으로 특수화했다. 이때 residual variance `4/3`, lag-1 covariance `2/3`, 자기상관 `1/2`다. 이는 당시 추론의 결정적 예시이며 새로운 simulation 결과가 아니다. [C09·C12]

RCTL residual로 소속을 고르면 소속 판단에 학습된 RCTL이 들어가므로 당시 독립성 조건과 맞지 않는다. TabICL residual로 바꾼 경우에도 그 소속이 고정 RCTL을 개선한다는 근거가 별도로 필요하다. [C09·C14]

또한 원문 28의 손실 반례를 재계산했다. 실제값 `1`에 대해 예측 `0.5→1.9`이면 제곱 로그 오차는 `0.480453013918→0.411976411195`로 감소하지만 원래 제곱 오차는 `0.25→0.81`로 증가한다. 이는 two-stage Proposition 1의 로그 손실 개선에서 원 단위 MSE 개선으로 넘어가는 함의의 반례다. 모든 residual 방법을 무효화하지는 않는다. [C10·C13]

## 비용의 단위를 바꾸지 않는다

| 근거 | 수치 | 해석 범위 |
|---|---|---|
| TabMGP E.1 | 추가 500 steps × 100 posterior draws = 50,000 prediction steps | 초기 context 한 묶음에 대한 산술. ensemble 내부 연산을 별도 API 호출 수로 더하지 않음 |
| TabMGP 본문 | 회귀 posterior sample 하나 약 200초, L40S | 100개 전체의 측정 시간이 아님. v2 checkpoint / TabPFN 2.0.6, 회귀 ensemble 8·분류 4 |
| CLT Appendix A | coverage 전체 약 700 GPU-hours, L40S | 단일 호출·cell 비용이 아님. v2.5 checkpoint / TabPFN 6.2.0, coverage ensemble 16·그 외 64 |
| CLT Appendix J.1 | `Uₙ` 실험 1,000 Monte Carlo draws | 코드 helper 기본값 100과 다름. `Vₙ` prefix 경로와 혼합하지 않음 |
| 원문 28, context 504 | 128 cells: 64,512 prefixes | 산술이며 실제 모델 호출·측정 시간이 아님 |
| 동일 조건 | 1,024 cells: 516,096 prefixes | 상수 target prefix의 우회가 있으므로 모든 prefix가 모델 호출은 아님 |
| 동일 조건 | 10,000 cells: 5,040,000 prefixes | TabPFN의 점근 비용 설명만으로 TabICLv2의 전체 시간을 확정하지 않음 |

위 수치는 [산술 기록](../verification/history-020-logic-check.json)과 지정 문헌 구간에 연결된다. 원문 28의 TabMGP 실험 위치 표기 `§5.1`은 보존했지만, 확보한 v3에서는 본문 **§5 Experiments**와 Appendix E.1을 실제 locator로 사용한다. [C03·C06·C14]

## 재사용 자료와 미완료 범위

팀은 [원문·원 manifest](../evidence/0028-mechanism-uncertainty/README.md), [고정 판본과 코드 링크](../sources/history-020.md), [검수 근거](../verification/history-020-primary-review.json)를 재사용할 수 있다. PDF·HTML·외부 코드 전체는 재게시하지 않고 identity와 공식 링크를 제공한다. 기존 세 `.txt`는 PDF와 이름이 대응하지만 바이트 중복이 아니며, 고유 주석·추출 차이 확인을 완료하지 않았다.

원문에서 CIRM, CRT `2603.06609`, NTK task-affinity, PreqTorch는 초록·검색 결과 단계였다. 이번 H020도 이들을 원리 검토 완료로 올리지 않는다. 네 문헌이 모든 선행을 포괄하거나 세계 최초성을 판정한다고 주장하지 않는다. 저자 전체 구현·실험 재현, 정리 가정의 실제 트래픽 충족 여부, 새로운 소속 결정과 RCTL 효용, 이후 판단의 전체 연결은 미완료다. [C15]

원문 마지막의 연구 Goal·예산·Word 미완료 문구는 당시 운영 상태다. 현재 아카이브의 실행 명령이나 전체 정리 완료 상태로 읽지 않는다. 다음 기록을 정리하면서 판단의 유지·변경을 이어서 연결한다. [C01·C15]
