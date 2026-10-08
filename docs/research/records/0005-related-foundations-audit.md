# 05 관련 여섯 연구 — context 선택·환경 진단·사전학습 clustering

2026-09-25의 [05 문헌 판단 원문](../evidence/0005/originals/SRC-0020826.md.txt) 41–47행을 여섯 일차문헌의 지정 구간과 대조했다. 문헌 검토 기록이며 이 프로젝트에서 여섯 방법을 실행했다는 보고가 아니다. 05의 다른 부분은 [가까운 방법](0005-closest-methods-audit.md), [네트워크·시계열](0005-network-timeseries-audit.md), [공식 구현](0005-official-tabicl-audit.md)에 연결된다.

핵심 구분은 **query의 context를 고르는 일, 관측 행을 clustering하는 일, cell별 학습자료 공유를 결정하는 일**이다. 모두 clustering 또는 표현 재사용이라는 말을 쓰지만, 필요한 정보와 최종 목적이 다르다. 논문의 분류 정확도·ARI·진단 점수·추론 속도가 현재 소속의 RCTL MAE를 직접 입증하지는 않는다.

## 당시 검토한 역할과 실제 방법

| 방법 | 원문에서 확인한 결정 | 학습·정답·평가 조건 | 현재 연구와 연결할 때의 한계 |
|---|---|---|---|
| Localized TabICLv2 | 같은 training context에서 앞 단계 표현을 공유하고, query와 가까운 행을 골라 Stage3 context를 축소 | classifier의 `kv_cache='repr'`; Stage2/3 미세조정; 38개 분류 자료 | 서로 다른 cell context의 cache를 그대로 교환하거나 frozen 회귀 효과를 보장하지 않음 |
| TL-ANDI | 입력 거리와 source/target 조건부 평균 차이로 source anchor를 고르고, 라벨을 kernel 평균으로 증류한 뒤 target 잔차 보정 | source/target Y, test X, calibration/validation 분할; target-only도 선택 후보 | 최종 RCTL에 실제 Y를 넘기는 현재 경로와 다름. validation 정리에는 가정과 오차항이 있음 |
| CRUMB | test query의 X를 k-means로 묶고 각 묶음에 MMD가 작은 train subset을 선택하여 배치 추론 | context 선택식은 X를 사용; PFN에는 선택된 train Y 제공; 추가 가중치 학습 없음 | query 묶음과 cell 고정 소속이 다름. 배치 context 공유가 내부 cache의 임의 교환을 의미하지 않음 |
| Entangled by Design | 환경별 context 구성과 S-swap으로 가짜 상관에 대한 예측 민감도 진단·완화 | ridge 이론과 TabPFN 관측; S의 식별/추정 및 여러 환경 필요 | 환경을 나누는 것만으로 새 방법이 되지 않으며, 진단 지표 감소가 예측오차 감소를 뜻하지 않음 |
| TabClustPFN v3 | PIN으로 행 소속을, CIN으로 K를 추론 | TabICL encoder 초기화 후 전체 파라미터를 합성 cluster 정답으로 학습; ARI/NMI·K 오차 평가 | frozen regression checkpoint를 거리로 쓰는 방법이 아님. K=1도 선택 범위에서 제외 |
| Amortized TS clustering | ACF/QAF 특징으로 모든 시계열 쌍의 동일 cluster 확률을 학습한 뒤 spectral/Louvain으로 분할 | 별도 합성 collection 학습·pairwise BCE·ARI 평가 | 통계 특징과 사전학습 clustering 자체를 신규성으로 삼을 수 없음. pairwise 계산과 후처리를 비용에서 빼면 안 됨 |

판본·수식·정보 접근 범위는 [여섯 방법 비교](../references/related-tabular-clustering.md)에, source ID와 읽은 구간은 [출처 안내](../sources/history-006.md)에 있다. 위 비교는 H006-C01–C09의 범위 한정 주장이다.

## 좋은 중간 점수가 최종 이득은 아니다

다음은 **Entangled 논문이 보고한 값**이다. PDF의 Tables6/7과 대조했으며 저자의 원출력 재현이나 우리의 교통 실험이 아니다. CSR은 가짜 성분 변경에 대한 민감도와 인과 성분 변경에 대한 민감도의 비율이고, OOD RMSE는 예측오차다.

| 논문 조건 | 방법 | CSR | OOD RMSE |
|---|---|---:|---:|
| 합성 high-spurious, TabPFN | Standard | 5.777 | 3.486 |
| 합성 high-spurious, TabPFN | Env-stratified | 2.170 | 3.176 |
| 합성 high-spurious, TabPFN | S-swap | 0.067 | 3.539 |
| scIB pancreas, semi-synthetic target | Standard ICL | 3.416 | 1.74 |
| scIB pancreas, semi-synthetic target | Env-stratified | 3.403 | 1.64 |
| scIB pancreas, semi-synthetic target | S-swap estimated S | 0.379 | 9.12 |

합성 조건은 `rhoS=0.7, rhoC=0.3, alpha=1.0`이다. scIB 부분은 실제 sequencing batch 자료에 `beta=0.5`의 Y-confounding을 주입한 조건이며, 자연 발생한 교통 자료의 인과 검증이 아니다. S-swap은 두 표에서 CSR을 크게 낮추지만 RMSE는 Standard보다 높다. 환경 층화는 같은 표에서 더 낮은 RMSE를 보인다. 특정 설정의 결과를 모든 환경으로 확대하지 않는다. [원문 v1](https://arxiv.org/abs/2607.25532v1), [21개 논문 보고 행](../evidence/0005-related/paper-reported-tables.json)

이 구분은 이미 정리한 [B2의 surrogate와 RCTL 차이](0004-0007-b2-observed-risk.md), [633의 Tab 직접 정확도와 소속 효용 차이](0633-joint-selection-negative.md)를 읽을 때도 유용하다. 서로 다른 자료의 같은 실패 원인을 입증한 것은 아니며, 최종 목적에 대한 별도 확인이 필요하다는 비교상의 교훈이다.

## 속도·안전성·사전학습을 옮길 때 보존할 조건

Localized의 Table1은 미세조정 전 모델과 8개 자료의 비교다. k가 커지면 정확도 보존은 높아지지만 k128의 평균 speedup은0.66으로 느려진다. 앞 단계와 retrieval 비용, 작은 호출의 overhead가 남으므로 Stage3의 점근적 비용 감소를 전체 속도 개선으로 옮기지 않는다.

TL-ANDI의 ‘no-negative-transfer’는 target-only를 포함한 유한 후보에서 독립 validation으로 선택할 때의 확률적 bound다. bounded loss와 validation 표본 수에 따른 양의 허용 오차가 있다. 논문 실험의 선택 후 full-target refit까지 동일 정리가 보장한다고 쓰지 않는다. 시계열의 의존성과 시간 분할을 별도 확인해야 한다. [정리의 범위](../references/related-tabular-clustering.md)

TabClustPFN은 TabICL 가중치로 초기화한 encoder도 포함해 전체 파라미터를 학습한다. Amortized TS는 지정 설정당200,000개 합성 collection을 학습하고 새10,000개 collection에서 평가한다. 이 학습 규모는 논문의 보고 조건이다. 이번에는 저자 checkpoint의 현재 재사용 가능성을 확인하지 않았으므로 모든 적용자가 처음부터 다시 학습해야 한다고 단정하지 않는다.

## 같은 제안을 다시 검토할 때

| 제안의 이름이 비슷할 때 | 먼저 확인할 기존 차이 | 새 조건으로 명시할 것 |
|---|---|---|
| nearest context, 국소화, cache 재사용 | Localized의 같은 context와 미세조정, 초기 B1/B2의 기본 cache=False | 어느 단계의 cache인지, context가 같은지, 실제 준비·검색·추론 비용 |
| 분포 매칭, anchor 선택, label distillation | CRUMB의 X-only MMD와 TL-ANDI의 조건부 평균 차이·의사 라벨은 다른 방법 | 사용 가능한 X/Y, source/target, test X의 시점, validation/재적합 여부 |
| 환경 균형, 가짜 상관 제거 | Entangled의 환경 층화와 S-swap에 필요한 정보가 다름 | 환경과 S를 어떻게 정의/추정했는지, 진단 점수와 최종오차 각각의 평가 |
| pretrained clustering, nonlinear feature affinity | TabClustPFN의 별도 목적과 Amortized의 pairwise 학습 | 추가 학습·prior·K 범위·후처리·최종 learner와의 연결 |

초기 B1/B2의 고정 회귀 가중치·129분위수·호출 비용은 [이미 검수한 저장 근거](../verification/history-005.md)를 재사용한다. 이번 논문 비교를 새 모델 실험으로 집계하지 않았다. 05의 회귀 TabPFN 미실행 서술은 당시 범위에 한정하며, 이후 전체 연구의 미실행을 증명하지 않는다.

**05 전체와 모든 문헌의 전구간 검토는 아직 미완료**다. 이번에는 여섯 논문의 지정 구간, PDF의 지정 내용17쪽, 원문05와의 연결을 확인했다. 다른 개정본·저자 코드·원실험 출력·회귀 TabPFN 후속 이력은 남아 있다. [검수 범위](../verification/history-006.md), [근거 목록](../evidence/0005-related/README.md), [과거 시도 색인](../prior-attempts.md)
