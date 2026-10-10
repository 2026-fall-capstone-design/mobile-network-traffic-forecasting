# 43–44: 학습 후 성능 예측과 국소 설명은 공유 학습 이득을 알려 주는가

2026-09-26의 기록 43은 문헌 확인 계획, 44는 저장 예측 진단과 문헌 검토의 종합 판단이다. 이 페이지는 43과 44 §3–5를 정리한다. 44 §1–2의 cell별 손해·사후 경로 선택과 §6의 42 실행 비용은 [41–42 기록](0041-0042-cell-harm.md)에서 검수했다. **당시 두 대체 경로를 새 추천안으로 채택하지 않았으며, 이 검토로 새 RCTL·TabICL 성능 결과를 만들지 않았다.** [원문·읽은 범위](../sources/history-026.md), [주장 지도](../verification/history-026-primary-review.json)

## 질문과 판단의 범위

기존 분할에서 평균에 가려진 안정적인 cell 이득이 확인되지 않고, 저장된 여섯 경로의 사후 선택도 제한적이었다. 그래서 예측 관계 점수에 보정항을 더하기 전에 Tab 모델이 제공하는 정보 자체를 바꿀 수 있는지 물었다. 당시 목표의 ‘RCTL 독립성’은 소속을 정할 때 RCTL의 손실·내부 상태를 관찰하지 않는 조건이다. 팀의 모든 미래 연구에 적용되는 금지 규칙으로 해석하지 않는다.

| 경로 | 필요한 관측과 정답 | 얻는 결과 | 당시 판단 |
| --- | --- | --- | --- |
| 기존 conditional traffic predictor | 과거 입력과 이후 실제 트래픽 | 조건부 예측 관계 | 같은 점수의 이름·보정만 바꾸어 계속하지 않음 |
| TimeTic형 meta predictor | 모델·자료 특징, zero-shot 성능, 실제 fine-tuning 후 성능 | 학습 후 성능의 예상값·순위 | RCTL 결과를 관측하면 당시 독립 조건이 바뀜 |
| local distillation | teacher 예측·OOF 손실과 실제 관측의 response | 국소 선형 예측·설명·선택 확률 | 계수 군집화는 선행연구에 이미 있고 pooling 이득과 다른 대상 |

근거는 보존한 [43 계획](../evidence/0043-0044-predictor-roles/originals/SRC-0021568.md.txt) 3–10행과 [44 판단](../evidence/0041-0042-cell-harm/originals/SRC-0021588.md.txt) 38–78행이다. 다음 행동을 적은 원문의 명령은 당시 계획이며 이번 정리에서 실행하지 않았다.

## TimeTic: 실제 학습 결과를 정답으로 사용한다

Yao 등의 [*Estimating Time Series Foundation Model Transferability via In-Context Learning*, v1](https://arxiv.org/abs/2509.23695v1)은 2025-09-28 제출판이다. 저장한 submission history와 2026-10-09 공식 서지 조회에서 v1을 확인했다. 검토한 PDF는 22쪽이다.

§3의 회귀 정답은 미래 트래픽 값이 아니라 **실제로 fine-tuning한 모델의 MASE**다. 다른 자료에서 관측한 전이 결과를 context로 사용하며, 정답이 없는 초기 상황에도 소수 자료에서 먼저 fine-tuning하라고 설명한다. 통계 특징 20개와 모델 특징 6개를 쓰고, 모델 특징은 layer별 activation의 entropy profile에서 구성한다. 따라서 ‘사전학습 모델이므로 학습 결과를 관찰할 필요가 없다’는 해석은 맞지 않는다. PDF 3–6쪽을 확인했다.

Appendix B.3의 정답 수집 조건은 전체 parameter를 1 epoch 학습, batch 32, AdamW learning rate 1e-5, 최대 sequence 2560, H100이다. §4.1은 마지막 10%를 test로, 나머지 90%를 fine-tuning·validation에 사용한다고 설명한다. 온라인 TabPFN 추론만 보고 과거 정답 수집·모델 activation 산출 비용을 0으로 셀 수 없다. 이번 아카이브는 저자 실험을 재실행하지 않았다.

아래는 PDF 7쪽 Table 1과 21쪽 Tables F/G의 **10개 자료에 걸쳐 보고된 mean 행**이다. 각 열은 별도의 순위 지표이며 RCTL MAE 개선율이 아니다. few-shot은 대상 자료의 training time window 100개로 전이 가능성을 추정하는 설정이다.

| 설정 | 예측 구간 | weighted Kendall: TimeTic | zero-shot | Spearman: TimeTic | zero-shot |
| --- | --- | ---: | ---: | ---: | ---: |
| standard | short | 0.305 | 0.157 | 0.353 | 0.257 |
| standard | medium | 0.429 | 0.329 | 0.600 | 0.467 |
| standard | long | 0.319 | 0.279 | 0.418 | 0.381 |
| few-shot | short | 0.320 | 0.131 | 0.399 | 0.236 |
| few-shot | medium | 0.383 | 0.262 | 0.469 | 0.379 |
| few-shot | long | 0.323 | 0.320 | 0.451 | 0.413 |

초록의 ‘약 0.6’은 PDF 8쪽 §4.2에서 **medium-horizon Spearman**으로 구체화된다. 이 값을 세 구간 전체의 평균이나 weighted Kendall로 옮기지 않는다. 초록의 약 30% 문구도 모든 구간·지표의 동일한 개선으로 확장하지 않는다. §4.3의 알려진/새 모델·자료 조합은 서로 다른 context 구성이고, 관측된 전이 사례를 계속 필요로 한다. 실제 RCTL 공동 학습의 이득을 증명한 비교가 아니다.

### 구현 전에 확인할 표기와 수학적 범위

- PDF 6쪽 §3.3은 특징을 26개로 설명한 뒤 zero-shot·fine-tuned 열을 붙여 n×28 표를 만든다. online query는 m×26으로 기술하지만 PDF 15쪽 Figure A에는 query의 zero-shot 열도 보인다. 실제 입력·정답 열 구성은 구현 확인이 필요하다.
- Appendix A.1의 TotalVariance는 표준화·PCA 2차원·100개 그룹의 성능 분산으로 계산하는 proxy다. 실제 fine-tuned 성능이 특징 선택에도 쓰인다. 표본 proxy를 줄인 사실을 참 조건부 분산이나 추정 불확실성의 일반적인 감소 보장으로 바꾸지 않는다.
- PDF 15쪽 Algorithm 1은 후보 `f`를 순회하면서 `X_sel`에 아직 확정되지 않은 `f*`를 사용한다. 원문의 변수 표기 불일치이며 실제 저자 코드의 실행 오류를 확인한 것은 아니다.
- PDF 22쪽 Appendix D의 두 번째 부등식은 좌변을 `X=x`에 조건화한 채 우변을 더 거친 특징 `φ(X)`의 조건부 분산으로 둔다. 이 **점별 하한은 일반적으로 성립하지 않는다.**

마지막 항목은 두 점으로 정확히 확인할 수 있다. `P(X=0)=P(X=1)=1/2`, `Y=X`, `φ(X)=0`, 예측 `g(φ)=0`이면 `X=0`에서 제곱오차는 0인데 `Var(Y|φ)=1/4`이다. 올바른 하한은 유한한 이차 모멘트 아래 **같은 특징에 조건화한** `E[(Y−g(φ(X)))² | φ(X)] ≥ Var(Y|φ(X))`다. 평균을 취하면 `E Var(Y|φ(X)) ≥ E Var(Y|X)`도 성립한다. [정확한 유리수 검사](../evidence/0043-0044-predictor-roles/document-tables.json)는 난수·모델 없이 이 구분만 확인한다. 이 표기 정정으로 TimeTic의 실증 결과나 방법 전체를 반증한 것은 아니다.

저장 HTML의 GitHub 링크는 TabPFN·arXiv 도구를 가리켰다. 이번 제한된 공식 자료·검색 확인에서도 TimeTic 자체의 구현은 확인하지 못했다. 저자의 다른 scaling-laws 저장소에 있는 논문 인용을 TimeTic 코드로 세지 않으며, **공개 코드가 없다고 단정하지 않는다.**

## Local distillation: 예측값으로 국소성을 만들고 계수를 군집화한다

Craig·Huang·Panigrahi의 [*Interpretable AI with Local Distillation*, v2](https://arxiv.org/abs/2608.23538v2)를 검토했다. arXiv 이력은 v1 2026-08-24, v2 2026-09-22이며 PDF 표지에는 September 23, 2026이라고 적혀 있다. 제출판 날짜와 본문 표지 날짜를 구분한다. v1을 읽었다거나 두 판 전체를 비교했다는 뜻은 아니다.

§2 Algorithm 1은 teacher의 OOF 예측과 query 예측의 **scalar 차이**가 작을수록 실제 학습 관측에 높은 가중치 `S_j`를 준다. teacher의 query 예측은 하나의 pseudo-observation으로 추가한다. 주된 response는 실제 관측의 y이며, 최종 예측은 국소 elastic-net student가 만든다.

`μ = student OOF MSE / teacher OOF MSE`가 1 이하이면 global linear student로 돌아간다. `n_eff = 1 / Σ S_j²`이고 teacher anchor의 가중치는 **`μ / √n_eff`**다. 목적함수에 제곱오차의 1/2까지 포함하면 계수는 `μ / (2√n_eff)`다. PDF 추출 텍스트의 분수 줄바꿈을 곱셈으로 읽지 않도록 7쪽 원 도식을 대조했다. 이 global gate가 모든 query의 국소 개선 가능성을 판정하는 정리는 아니다.

### 이미 제시된 계수 군집화와 안정성의 대상

§4.3, PDF 13쪽의 Auto MPG 예는 157개 query 각각에서 8차원 계수 벡터를 만든다. k-means와 silhouette로 k=3을 고른 후, 독립 randomization vector 100개마다 157개 국소 모델을 다시 맞추고 군집화한다. 따라서 설명된 단계에는 **100×157=15,700개의 query별 무작위 재적합**이 있으며 ‘student 100개만 학습’과 다르다. 100개 군집 결과의 공동 소속 비율에 average linkage를 적용해 다시 3개 집단을 만든다. 이 작업은 논문에 보고된 절차이고 이번에 실행한 횟수가 아니다.

§4.1–4.2의 무작위화는 Gaussian 항을 student 목적함수에 더한다. teacher 예측과 locality 가중치는 재적합 동안 고정한다. randomization scale을 정할 때 사용하는 OOF median squared error의 **5% 허용오차는 신뢰수준이 아니다.** context를 다시 추출해 teacher·locality까지 바꾸는 절차와도 구별된다.

§5의 정리는 다음 조건에서 **response 변화에 대한 feature 선택 확률**의 민감도를 다룬다.

| 고정하거나 가정한 것 | 의미 |
| --- | --- |
| locality 가중치·μ·λ를 고정, lasso α=1 | 가중치나 정규화 선택까지 매번 다시 하는 전체 절차의 정리가 아님 |
| 가중 design의 general position | lasso 해의 유일성을 위한 조건 |
| `n_eff S_max` 유계, design·μ 유계 | 가중치 집중과 입력 크기 제한 |
| 유효 이웃에서 관련 design의 최소 특이값 하한 | 지역적으로 거의 선형 종속인 입력을 배제 |
| teacher가 training response에 대해 C¹, 미분의 supremum 유계 | context y 의존성을 포함한 민감도 제어 |

Theorem 1의 크기는 상수와 `1/τ`를 제외하면 `n_eff^(−1/2) + L_teacher n_eff^(−1/4)` 형태다. Corollary 1은 response 한 좌표의 변화에 대한 선택 확률 차이를 제한한다. teacher가 training sample에 전혀 의존하지 않을 때만 `L_teacher=0` 특수화를 쓸 수 있다. **TabICLv2의 parameter가 고정됐다는 사실만으로 context y에 대한 미분을 0으로 둘 수 없다.** 군집 소속 자체의 안정성, 시간 변화, 미래 MAE, pooling 이득의 보장으로 옮기지 않는다. 정리문·가정·설명을 확인했으며 Appendix A의 전체 증명을 재검증한 것은 아니다.

### 같은 예측값이 같은 입력 관계를 뜻하지 않는 반례

Appendix D는 `f(x)=x₁+x₂+(2+x₁−x₂)x₃`인 모의 자료에서 gradient boosting teacher와 lasso student를 사용한다. Gaussian 입력의 공분산은 `0.3^|j−k|`, query는 40개, 설정당 50반복이다. 세 번째 참 국소 계수 `2+x₁−x₂`는 teacher 예측이 비슷한 관측들 사이에서도 달라질 수 있다. PDF 38쪽 Table 2의 관련 보고값은 아래와 같다.

| n | p | σ | global로 돌아간 반복 / 50 | β₃ 상관 평균 | 표준편차 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 400 | 100 | 0.3 | 0 | 0.34 | 0.13 |
| 400 | 100 | 1 | 0 | 0.30 | 0.13 |
| 400 | 100 | 2 | 11 | 0.24 | 0.16 |
| 400 | 100 | 3 | 40 | 0.14 | 0.14 |
| 200 | 100 | 0.3 | 0 | 0.33 | 0.17 |
| 400 | 800 | 0.3 | 0 | 0.34 | 0.15 |
| 200 | 500 | 0.3 | 0 | 0.25 | 0.17 |

상관은 **μ>1이어서 local fit을 유지한 반복만** 집계한다. σ=3 행의 상관은 50번 모두가 아니라 나머지 10번의 값이다. 0.14–0.34 범위는 이 예의 β₃에 대한 보고이며 모든 관계 추정의 정확도 상한이 아니다. 원시 모의 결과를 확보해 다시 계산하거나 새 모의를 실행하지 않았다.

## 저장된 저자 구현과 비용 경계

[공식 저장소의 고정 커밋](https://github.com/erincr/local-distillation-benchmark/tree/f8ea1e71f19afd3167ba7ca0984ed34294d40823)에서 README와 `common.py`, `method_ld.py`, `method_ld_ablation.py`를 정적으로 읽었다. 저장된 네 파일의 SHA-256과 Git blob SHA-1이 당시 repository tree 및 2026-10-09 공개 API의 같은 커밋과 일치했다. [바이트 대조](../verification/history-026-code-check.json)

- `common.py`의 scalar teacher 거리, μ gate, `μ/√n_eff` anchor, query pseudo-observation은 본문과 연결된다. teacher 기본 선택은 이 코드의 TabPFN V3이고, 우리 연구의 TabICLv2 실행 결과가 아니다.
- `method_ld.py`는 shuffled 5-fold OOF를 사용한다. 공통 자료 분할도 기본 shuffled 80/20이며 StandardScaler는 train에서 맞춘다. 시간 순서가 필요한 트래픽 예측에 그대로 적용하면 안 된다.
- `local_distill`은 λ가 전달돼도 global Adelie CV를 다시 호출한다. 호출부도 global CV를 수행하므로 비용 계산에서는 두 호출을 구분해야 한다. 전달하는 λ rescale은 확인했지만 Adelie 내부 가중치 정규화까지 수학적으로 동일한 목적임을 검증한 것은 아니다.
- `method_ld.py`의 elapsed는 stability diagnostic까지 포함한다. ablation은 두 조건을 함께 계산한 시간을 같은 값으로 기록하고 각 stability diagnostic은 그 뒤에 수행한다. 두 행의 시간을 독립 실행 시간처럼 합산하면 안 된다.

네 파일을 읽은 것은 저장소 전체·notebook·randomized clustering 구현 전부의 검토가 아니다. 의존성 설치, 원 코드 import, 학습·추론·무작위 재적합을 하지 않았다.

## 당시 결정과 다시 검토할 조건

44는 TimeTic형 설계에 RCTL 성능·activation을 넣으면 당시 독립 조건이 바뀐다고 판단했다. cheap Ridge/HGB 결과로 대체하면 정답이 cheap learner의 공유 효과로 바뀌므로 RCTL로 옮기는 근거가 따로 필요하다. TabPFN을 TabICLv2로 교체하는 것만으로 새로운 연구 기여나 pooling 성능 보장을 얻지는 않는다.

local explanation clustering은 선행 구조가 이미 있고, 설명이 안정적이라는 사실만으로 함께 학습할 이득을 새로 관측한 것은 아니라고 판단했다. 따라서 **문헌 검토 후 당시 설계에서 미채택**으로 기록한다. 두 방법을 직접 실행해서 RCTL 성능이 나빴음을 입증한 과학적 부정 결과로 분류하지 않는다.

다시 검토한다면 새로 얻는 정보, 그 정보가 바꾸는 실제 학습 행동, 기존 meta-regression·local explanation과 다른 점을 먼저 적는다. RCTL 정보를 허용할지, 허용하지 않는다면 어떤 검증 가능한 연결 가정이 필요한지 명시해야 한다. 안정성의 대상·조건과 목표 손실을 맞추고, 같은 기존 여섯 예측 경로의 재선택인지 새로운 학습 비교인지도 구분한다. [새 실험 전 색인](../prior-attempts.md)

## 실행·보존·남은 범위

43의 다운로드 코드는 시작 표시·HTTP 입수·PDF 텍스트 추출·HTML 링크 수집을 수행하는 코드다. 보존 manifest의 여섯 항목은 HTTP 200과 저장 상태를 기록하며, 두 PDF는 총 64쪽·5,063,783 bytes다. `run_started`는 2026-09-25 15:05:22.524099 UTC와 `model_calls=0`을 기록한다. 30초 timeout·10 MiB 상한·thread 3개는 다운로드 설정이며 측정된 실행 시간이 아니다. 소요시간은 미기록이다. 42의 0.031521초를 43의 문헌 수집 시간으로 재사용하지 않는다.

메모·코드·작은 JSON의 원 바이트 5개를 추가 보존했고, 44는 [앞 묶음의 동일 원본](../evidence/0041-0042-cell-harm/originals/SRC-0021588.md.txt)을 재사용한다. PDF·외부 코드는 정식 링크·고정 버전·해시·읽은 구간으로 연결했다. 이번 범위는 PDF 텍스트 34쪽·시각 확인 9쪽이며 전체 논문 완료는 0편이다. 원 HTML·과거 추출본·렌더 사본의 미열람 구간도 남겨 두었다. [검수와 한계](../verification/history-026.md)

45 이후의 후속 판단, 다른 과거 기록, 전체 실패 비용과 최종 접근·변경 검수는 이어서 처리한다. 이번 기록의 정리·게시를 전체 아카이브 완료로 세지 않는다.

후속 [76의 반응 전달 검토](0076-0079-learning-decisions.md#c04)는 기존 국소 계수 clustering을 재사용하고, 예측 반응을 실제 target의 보조 loss로 전달하는 결정과 구분했다. 이번 형태의 미채택 이유와 global distillation 대비 재진입 조건을 연결한다.
