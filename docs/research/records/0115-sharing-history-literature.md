# 원86: 결정 이력·저장 검색과 Clustered MTL 후속 독해

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

[출처](../sources/history-115.md) · [검수](../verification/history-115.md) · [근거](../evidence/0115-sharing-history-literature/README.md) · [학습 공유의 핵심 판단](0114-shared-training-scope.md)

팀원이 같은 후보를 다시 검토할 때, 이미 수행한 실험과 조건이 달라지는 제안, 검색만 한 문헌과 본문을 읽은 문헌을 구분할 수 있도록 연결했다.

**상태:** 22개 주장·7개 묶음의 작성 후 원문 대조 완료. 새 모델 실행 0.

## 후보 결정과 연혁의 변경

<a id="c01"></a>**C01.** snapshot27에서 28로 바뀔 때 결정표는 45행에서 46행이 됐다. 새 9행의 “소속 고정 뒤 RCTL 학습 공유”만 추가되었고 나머지 행은 바이트 단위로 같다. 전체 21개 판단 행을 기존 상세 기록에 연결했다. 이는 21개 새 실험이나 모든 후보의 영구 기각을 뜻하지 않는다.

<a id="c02"></a>**C02.** 새 행은 공통 초기화·독립 미세조정, 고정 global 표현, 실제 파라미터 공동 갱신을 구별한다. 소속 고정 후 공유를 자동으로 독립성 위반이라 보지 않으며, 기존 29fit의 독립 학습 실패를 모든 공유 학습의 실패로 확대하지 않는다. 저장 파라미터 수와 서로 다른 입력의 연산량은 별도다. 이 비교의 상세 근거는 H114에 연결한다.

<a id="c03"></a>**C03.** 원86의 다음 질문은 공동 입력·다중 출력에서 인과적 입력 경로의 표현 용량을 확인하는 것이다. flatten 전체 차원과 최신 입력이 통과하는 폭이 다를 가능성을 제시했지만 새 진단·알고리즘으로 채택하지 않았다. 새 Tab/RCTL/수치 pilot은 0이며, 이 후속 질문을 검증된 병목이나 성공한 공유 구조로 쓰지 않는다.

<a id="c04"></a>**C04.** 누적연혁은 433행에서 445행으로 늘었다. 기존 7행 제목을 새 7–19행으로 바꾸어 원86 절을 넣고 원85를 이전 상태로 표시했으며 나머지는 같다. 445행·37절을 모두 읽었다. 최신에서 과거로 내려가는 절들 뒤에 초기 확인과 B2 완료가 이어져 파일 순서가 실험 시간 순서와 같지 않다.

<a id="c05"></a>**C05.** 초기 RCTL 0회와 최종 20일 미열람은 당시 상태이고, 뒤의 29fit 완료·최종 20일 관찰과 함께 읽어야 한다. 원309행의 UPC “1~4 cluster”는 288행의 1,2,4,6,8,12로 정정된다. 원278행의 집합당 최대 68개 열 단위 계산에는 H024의 고정 구현 최대 289개 열별 처리 정정도 연결한다. 이는 실제 모델 호출 수나 실측 시간이 아니다. 과거 원문을 덮어쓰거나 관찰한 기간을 다시 독립 test로 만들지 않는다.

<a id="c06"></a>**C06.** 결정표는 Tab의 직접 예측, 일부 cell의 공간 입력, 일부 앞기간·피크 이득을 다섯 항목으로 보존한다. 직접 예측 이득과 소속·출력 압축·RCTL 이득은 다른 주장이다. 마지막 네 문장은 바뀌는 결정, Tab 값의 추가 정보, 최종 학습에 전달되는 위치, 관찰된 기간·예산을 확인하라는 당시 연구의 진입 조건이다. 현재 정리 작업에 새 실험을 허가하는 명령은 아니다.

## 저장 검색의 실제 내용

<a id="c07"></a>**C07.** Crossref 응답 3개에는 각 3항목, 총 9항목이 있다. total-results는 각각 3,574,641/3,690,583/3,521,026이며 저장·독해한 논문 수가 아니다. 저장 query.search-terms는 null이다. 항목의 제목·저자·DOI·날짜·초록 유무를 보존하되 9편의 방법을 검증했다고 세지 않는다.

<a id="c08"></a>**C08.** branching_metadata에는 CMA-BP의 2024년 branch predictor 논문, 2015년 Learning Multi-Level Task Groups in Multi-Task Learning, 2020년 Multi-task Learning 항목이 있다. Learning to Branch의 정확한 제목 항목은 이 세 결과에 없다. 2015년 항목의 MeTaG 초록은 다층 task grouping을 설명하지만 그 방법·보장·코드를 이번에 전문 검증한 것은 아니다.

<a id="c09"></a>**C09.** clustered_mtl_metadata의 세 결과는 2019년 A Convex Formulation of SVM-Based Multi-task Learning, 2007년 SSRN Convex Multi-Task Feature Learning, 2008년 동명 journal 항목이다. Jacob·Bach·Vert 논문의 정확한 항목은 없다. SSRN에는 초록이 있고 journal에는 본문 링크가 있으며, Pontil의 이름은 각각 Massimo와 Massimiliano로 기재돼 있다. 두 판본의 내용 동일성이나 독립 연구 두 편 여부를 이 metadata만으로 확정하지 않는다.

<a id="c10"></a>**C10.** regularized_mtl_metadata의 첫 항목은 Evgeniou·Pontil의 2004년 Regularized multi-task learning, DOI 10.1145/1014052.1014067이다. 다른 항목은 Task Variance Regularized Multi-Task Learning과 Manifold Regularized Multi-Task Learning이다. 세 항목 모두 abstract 필드가 없으므로 이 JSON으로 수식이나 실제 공유 알고리즘을 읽었다고 할 수 없다.

<a id="c11"></a>**C11.** 저장된 CVPR HTML 58행 전체를 정적으로 읽었다. 53–54행에는 paper database 접근 실패와 Error 1525, DATE 값 all 오류가 있다. H114에서는 원86 문서가 보고한 오류로 남겼지만 이번에는 해당 HTML 본문까지 대조했다. 별도 추정 URL의 404와 이 HTTP 200 오류 본문은 다른 접근이다. bs4 실패 터미널 원본은 아직 독립 대조하지 않았다.

<a id="c12"></a>**C12.** 저장 arXiv HTML은 방법 전문이 아니라 초록·서지 페이지다. v1 제출 시각은 2008-09-11 19:01:39 UTC이며 논문 첫 페이지의 2018-10-22 조판 날짜와 구별한다. 이 저장판에는 v1만 표시되지만 현재의 최신성까지 조회한 결과는 아니다. PDF/HTML 링크나 일반적인 Code Finder 위젯을 공식 구현 확보의 증거로 쓰지 않는다.

## Jacob 논문의 남은 방법·실험

<a id="c13"></a>**C13.** H114의 PDF 1–8쪽 독해에 이번 9–14쪽 텍스트·전체 페이지 이미지 확인을 더해 14쪽 전체를 읽었다. 저장 TXT 708행도 전부 읽었고, 페이지 구분 머리글과 양끝 공백을 제외하면 새 추출의 14쪽 각각과 정확히 같다. TXT를 별도 독립 연구나 추가 독립 본문으로 세지 않는다. 원문 PDF·TXT·렌더 이미지는 새로 공개 복사하지 않는다.

<a id="c14"></a>**C14.** 논문 9쪽은 주어진 특이값에 대해 Σ의 고유값 λ_i를 α≤λ_i≤β, 합 γ로 제한하고 ∑_i σ_i²/λ_i를 최소화하는 계산을 설명한다. 양의 ν에서 λ_i는 σ_i/√ν를 범위 안으로 제한한 형태이며, Algorithm 1은 임계점 사이에서 쌍대식의 정지점을 찾는다. 10쪽은 특이값에 대한 미분 2σ_i/λ_i를 제시한다. 이는 선형 task 규제의 계산이며 Tab의 소속 점수나 RCTL 구현이 아니다.

<a id="c15"></a>**C15.** H114에서 구별한 행렬 차원 문제가 9–10쪽의 ΠW와 WᵀΠW 표기에도 이어진다. W가 d×m, Π가 m×m이면 일반 d≠m에서 이 곱을 그대로 쓸 수 없다. task 방향 중심화는 WΠ로 해석해야 하며 그 해석을 원문 인쇄식과 혼동하지 않는다. Algorithm 1은 열린 구간의 정지점을 적었고 경계·영특이값 처리의 실제 구현은 검증하지 않았다. 전문 독해가 모든 증명과 구현의 승인이라는 뜻은 아니다.

<a id="c16"></a>**C16.** 합성 실험은 두 cluster에 각 두 task, 특징 30개다. 각 task에 2,000개 점을 만들고 cluster별 학습 자료를 두 task에 5/6와 1/6로 나누었다. 3개 training fold를 구성하고 나머지 점을 test에 사용했으며 quadratic loss로 학습하고 task 평균 RMSE를 비교한다. 시간 순서가 있는 트래픽 MAE 실험으로 옮겨 설명하지 않는다.

<a id="c17"></a>**C17.** Figure 1·2와 본문에서 CN은 적은 학습점에서 k-means 방식보다 유리하지만, 자료가 늘어 k-means가 cluster를 복원하면 k-means가 완화 방식보다 좋다. 28점에서는 올바른 cluster를 복원하지 못하고 50점에서는 CN이 일부 구조를 찾는다고 보고한다. Reprojected와 CNinit의 동작도 구별한다. 초록의 포괄적인 우위 표현을 모든 표본수·방법에 대한 일률적 승리로 쓰지 않는다.

<a id="c18"></a>**C18.** MHC-I 실험은 양성마다 음성 하나를 남긴 15,236점·35개 분자 task의 결합 분류이며 logistic loss를 쓴다. 결과표는 알려진 ligand가 200개 미만인 10개 분자의 평균 오류다. 내부 교차검증으로 파라미터를 고르지 않고 작은 후보 집합을 사용했으며 cluster 수는 2 또는 10으로 제한했다. 전체 35task의 동일한 평가값이나 실제 통신자료 결과로 확대하지 않는다.

<a id="c19"></a>**C19.** Table 1의 오류는 Pooling 26.53±2.0%, Frobenius 11.62±1.4%, MT kernel 10.10±1.4%, Trace norm 9.20±1.3%, Cluster Norm 8.71±1.5%다. 인쇄표를 이미지와 대조했다. CN의 평균값이 가장 작지만 ±의 통계적 정의와 유의성 검정을 임의로 채우지 않으며 트래픽 성능 개선율이나 계산량 절감률을 만들지 않는다.

<a id="c20"></a>**C20.** MHC에서 학습한 Σ는 알려진 supertypes를 복원하지 못했고 Reprojected와 CNinit도 성능을 개선하지 못했다. 예측오류 감소, 의미 있는 집단 복원, 이산 소속으로 다시 투영할 때의 효과는 구별해야 한다. 결론의 비선형 확장은 후속 연구로 제시되며 이 논문 자체가 비선형 RCTL 공유층을 검증한 것은 아니다.

## 검수 범위와 다음 작업

<a id="c21"></a>**C21.** 이번 묶음은 원86 후속 8표현물 1,904행과 남은 PDF 6쪽을 읽고, 결정표·37절 연혁·9개 검색항목을 연결한다. snapshot28의 20파일 437,553bytes 보존 대조는 H114 근거로 재사용하고 현재 해시도 확인했다. 새 모델 실행·원본 연구코드 실행·import는 0이다. 과거 Goal·예산·handle과 next step 문장은 연구기록의 내용으로 보존한다.

<a id="c22"></a>**C22.** 새 집계는 본문 5개(MD 2·HTML 2·Jacob PDF 완독 1), 전체 JSON 3개이며 기존 Jacob 부분자료 1개를 선택 전용 집계에서 뺀다. 대응 TXT·사본·재독·렌더는 독립 본문으로 추가하지 않는다. H114가 남긴 9개 후속 그룹의 내용 읽기는 끝났지만 bs4 터미널·외부 구현·인용 문헌·후속 판본과 원87 이후, 전체 통합·장기 팀 접근·최종 검색 검수는 남아 있다. 전체 Goal 완료가 아니다.

## 이미 검토한 결정을 찾는 표

아래 링크는 해당 결정의 상세 기록으로 이동한다. 21행의 원문 판단과 위치는 [결정표 대응](../evidence/0115-sharing-history-literature/candidate-map.json), 모든 절의 위치는 [연혁 대응](../evidence/0115-sharing-history-literature/chronology-map.json)에 있다.

| 바꾸려는 결정 | 원 연구 번호 | 상세 검토 |
|---|---|---|
| 공유할 함수/모델 소속 | 02–09,23–28 | [기록](0004-0007-b2-observed-risk.md) |
| subgroup의 유한학습 손해 | 33–38 | [기록](0033-0035-process-fit-gap.md) |
| 소속 고정 뒤 RCTL 학습 공유 | 28,38,86 | [기록](0114-shared-training-scope.md) |
| cell 정보·target 좌표 | 14–22 | [기록](0020-0021-target-parameterization.md) |
| 입력 cell 선택·공유 | 18,45–47,75 | [기록](0047-input-sharing-roles.md) |
| 공동 입력·cell별 다중 출력으로 학습 단위 변경 | 47,74–75,81 | [기록](0090-input-partition-decision.md) |
| 학습 sample 재사용·고정 처리량 배분 | 39–40,85 | [기록](0039-0040-sample-reuse.md) |
| 학습 sample 압축 | 56–58,85 | [기록](0056-0058-mae-sampling.md) |
| 그룹 보호·피크 목적 | 41–44,66–71 | [기록](0066-0068-group-risk.md) |
| 관측 자료·해상도 | 29–32,51–55 | [기록](0029-0032-resolution-diagnostic.md) |
| 실제 무통신과 양의 트래픽을 구별한 공유 | 82 | [기록](0099-intermittence-decision.md) |
| 합계·대표예측으로cell복원 | 48–50 | [기록](0048-0049-aggregation-recovery.md) |
| 필요한 입력길이 | 59–62 | [기록](0059-0062-history-grouping.md) |
| baseline·residual·조건부분포변환 | 63–65 | [기록](0063-0065-synthesis.md) |
| 학습기 계수/중요도로clustering | 72–73 | [기록](0072-globalization-audit.md) |
| 예측 가능한 출력공간 압축 | 73–74 | [기록](0072-0075-output-compression.md) |
| 관계를 최종 학습 loss에 전달 | 43–44,76 | [기록](0076-response-transfer-audit.md) |
| 시간 조건별 cell 소속·모델 배정 | 17,27,32,77 | [기록](0077-dynamic-membership-dlm.md) |
| 정적 cluster의 공동 갱신 비용 | 17,77,83 | [기록](0105-joint-update-cost.md) |
| 공통 probe의 task 표현·전이 점수 | 28,35–38,63–65,72–74,78 | [기록](0079-regression-transferability.md) |
| 분산 학습의 local gradient 불일치 | 79–80 | [기록](0088-conditional-graph-diagnostic.md) |

## 수치·정정·읽기 범위를 함께 확인하기

[원85 이후의 이전 연혁 정리](0113-decision-history-sources.md) · [Tab 열별 처리 상한 68→289 정정](0039-0040-sample-reuse.md) · [논문 표와 읽은 페이지](../evidence/0115-sharing-history-literature/literature-scope.json) · [원 검색의 9항목](../evidence/0115-sharing-history-literature/search-results.json) · [판본의 변경행](../evidence/0115-sharing-history-literature/version-comparison.json) · [남은 확인](../evidence/0115-sharing-history-literature/packet-coverage.json)

원문 수집 실패는 새 모델 실패가 아니다. 논문의 분류 오류·RMSE, 기존 트래픽 MAE, 기호 비용을 하나의 성공률로 합치지 않는다. 원86의 후속 문장을 실행 가능한 새 계획으로 쓰려면 아직 없는 직접 근거와 비교 조건부터 채워야 한다.
