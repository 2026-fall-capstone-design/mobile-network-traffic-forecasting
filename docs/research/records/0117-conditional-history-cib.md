# 원87 후속: 결정 이력과 CIB 실험표·평가 경로

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

[출처](../sources/history-117.md) · [검수](../verification/history-117.md) · [근거](../evidence/0117-conditional-history-cib/README.md) · [원87 핵심 판단](0116-causal-capacity-reference.md) · [이전 결정표](0115-sharing-history-literature.md)

같은 연구를 다시 시작하기 전에 이미 검토한 결정과 남은 조건을 찾을 수 있도록 연결했다. 논문이 보고한 성능, 인쇄값의 산술 대조, 저장 코드의 정적 발견을 구별한다.

**상태:** 26개 주장·7개 묶음의 작성 후 원문 대조 완료. 새 모델 실행 0.

## 판단표·연혁과 원88의 당시 계획

<a id="c01"></a>**C01.** snapshot28→29에서 후보 결정표는 46행에서 47행이 됐다. 기존 12행의 공동 입력·다중 출력 판단을 보완하고 새 13행의 조건 보존 표본 비교를 추가했으며 나머지 행은 같다. 전체 22개 판단을 상세 기록에 연결했다. 이는 새 실험 22개나 모든 후보의 영구 기각을 뜻하지 않는다.

<a id="c02"></a>**C02.** 보완된 12행은 원81의 산술 비용 비교를 유지하면서 원87의 causal core·선형 head·고정 BN에서 최신 입력 변화가 지나는 폭16 조건을 덧붙인다. 원래 cell별 scalar 모델과 최신값 출력 skip은 구별한다. 연혁 57행의 flatten 폭16L와 9행의 최신 입력 폭16은 서로 다른 경로의 설명이다. 실제 트래픽 손해나 Tab의 유용한 소속 결정은 아직 입증하지 않았다.

<a id="c03"></a>**C03.** 새 판단은 조건을 남긴 무조건 shuffle과 조건에 맞춘 재추출이 다른 기준 분포라는 원87 검토를 연결한다. 원88 계획은 TabPFN+CRT(2603.06609v1)의 본문·알고리즘·가정에서 예측 통계량과 조건부 생성기 역할을 구분하고, 가까운 conditional permutation/randomization 및 조건부 MI 원문을 최대 3편 추가로 확인하려는 내용이다. 추정기 교체만으로 신규성을 주장하지 않고 실제 바뀌는 결정·RCTL 연결·간단한 대안이 필요하다고 적었다. 이 계획 문서를 읽은 것이 원88의 후속 문헌 검수나 새 실험 수행은 아니다.

<a id="c04"></a>**C04.** 누적연혁은 445행에서 456행으로 늘었다. 새 원87 절은 7–17행이며 이전 원86 제목이 18행으로 이동했다. 나머지 기존 8–445행은 새 19–456행과 같다. 456행·38절 전체를 읽고 위치를 연결했다. 최신→과거 절들 뒤에 초기 확인과 B2 완료가 이어지므로 파일의 아래쪽을 무조건 최신 상태로 읽지 않는다.

<a id="c05"></a>**C05.** RCTL 0회와 최종 20일 미열람은 초기 상태이며, 뒤의 29fit 완료·최종 20일 관찰과 함께 보존한다. UPC의 구 1~4 cluster 표현은 같은 연혁의 1,2,4,6,8,12 확인으로 정정된다. 원289행의 최대 68개 열 계산에는 H024의 고정 구현 최대 289개 열별 처리 정정을 연결한다. 이는 모델 호출 수나 실측 시간이 아니다. 당시 예산을 초기화하거나 이미 관찰한 기간을 새 독립 test로 간주하지 않는다.

<a id="c06"></a>**C06.** 후보표의 다섯 긍정 결과 항목과 네 진입 질문은 이전 판본과 같다. Tab의 직접 예측 이득, 일부 cell의 공간 입력 이득, 기존 K4의 부분 이득을 전체 판단과 함께 남긴다. 좋은 직접 예측이 새로운 소속 결정이나 출력 압축의 성공을 자동으로 뜻하지 않는다. 마지막 문장도 최종 방향·Word가 당시 미완료라고 명시하며, 원문 지시를 현재 작업의 실행 허가로 쓰지 않는다.

## CIB 실험표와 전문 독해

<a id="c07"></a>**C07.** H116에서 읽은 CIB PDF 1–6쪽에 7–9쪽의 본문과 전체 페이지 이미지 확인을 더해 9쪽 전체를 읽었다. 저장 TXT 1,128행도 전부 읽었고 페이지 머리글·양끝 공백을 제외하면 9쪽별 새 추출과 같다. 참고문헌 목록은 35개 항목이다. 이 35편의 방법이나 논문의 모든 증명·실험을 검증했다는 뜻은 아니며 TXT·렌더를 별도 독립 본문으로 세지 않는다.

<a id="c08"></a>**C08.** Table1은 9개 자료의 4개 예측 길이에 MSE·MAE를 기록해 36조건·72지표를 비교한다. ILI의 예측 길이는 24/36/48/60, 다른 자료는 96/192/336/720이다. 본문이 적은 입력 길이는 Exchange 96, ILI 60, 나머지 336이다. 이 실험의 지표와 시간 단위·자료 조건을 우리 트래픽의 MAE 실험과 동일하게 취급하지 않는다.

<a id="c09"></a>**C09.** 인쇄된 Table1 값을 대조하면 67개 지표에서 단독 최소, 3개에서 공동 최소, 2개에서 둘째로 작아 본문 순위 개수와 일치한다. 동률은 Weather720 MAE 0.327, ETTm1 720 MAE 0.417, ETTm2 192 MSE 0.213이다. Exchange336/720 MSE에서는 CIB 0.304/0.769보다 MICN 0.272/0.714가 작다. 이를 모든 조건에서 엄격한 개선이나 통계적 유의성으로 확대하지 않는다.

<a id="c10"></a>**C10.** Table1의 HDMixer 대비 감소율을 현재 별도로 계산했다. 36조건의 행별 감소율 평균은 MSE 3.860975%, MAE 4.620860%이고, 각 지표 합계의 감소율은 4.742600%, 6.123755%다. 본문이 적은 4.26%/6.12% 중 MAE는 후자 반올림과 맞지만 MSE는 두 계산 모두와 다르다. 원래 집계 방식·가중치·더 정밀한 원결과는 미확인이므로 저자의 실제 산식을 추정하거나 인쇄값을 고치지 않는다.

<a id="c11"></a>**C11.** Table2는 ILI 열에도 96/192/336/720을 인쇄해 Table1의 24/36/48/60과 다르다. 같은 열 위치를 비교하면 ILI 둘째 MSE는 Table1 1.299 대 Table2 1.239, 셋째 MAE는 0.644 대 0.624다. 예측 길이가 같은 ETTm1 720 MAE도 0.417 대 0.416이다. ILI의 열 위치 비교를 동일한 실제 예측 조건의 비교로 단정하거나 표기를 임의로 정규화하지 않는다.

<a id="c12"></a>**C12.** Table2의 세 제거 방식×12조건×2지표 중 71개 값은 Ours보다 크고 하나는 같다. 동률은 W/O-Lk의 Weather192 MAE 0.237이다. 현재 계산한 개별 상대 증가율과 본문의 최대·평균 증가율도 구분한다. 예를 들어 ILI 셋째 열의 W/O-Ls MAE는 0.624→0.671로 약 7.532% 증가하지만 본문은 MAE 최대 2.8%라고 적었다. 원집계 정의와 실제 horizon이 미확인이므로 불일치를 남기고 유의성이나 재현 성능을 만들지 않는다.

## 대조 손실·표현·평가 상태

<a id="c13"></a>**C13.** 논문 4쪽 식8은 두 벡터의 norm으로 나눈 cosine 유사도를 사용한다. 저장 backbone의 contrastive_loss 143·159행은 특징 차원의 곱을 합한 내적이며 이 함수에 명시적인 L2 정규화 분모가 없다. 예를 들어 (2,0)과 (1,0)의 내적은 2, cosine은 1이다. 임의의 임베딩에서 두 계산을 같다고 볼 수 없으며 실제 학습 임베딩이나 예측오차를 측정한 결과는 아니다.

<a id="c14"></a>**C14.** 저장 코드는 양성 점수와 음성 점수의 최대값을 각각 빼고 지수화한다. 두 집합에 같은 상수를 빼는 경우와 달리 일반적으로 식9 형태의 비율을 보존하지 않는다. 양성 점수 1, 음성 점수 −1, 온도 1인 한 쌍에서 원식과 공통 이동의 손실은 약 0.126928이지만 별도 최대값 이동은 log2≈0.693147이다. 이는 현재 수행한 스칼라 산술 대조이며 원 모델 실행이나 논문 전체 결과의 반증이 아니다.

<a id="c15"></a>**C15.** contrastive_loss는 설정된 batch_size와 채널 수에서 고정 anchor를 정하고, 다른 채널 중 select_channel개를 무작위로 고른다. 음성 인덱스도 실제 tensor batch 크기 대신 self.batch_size로 구성한다. 유효한 batch·채널 수 및 마지막 batch 처리 조건이 필요하지만 data loader의 drop_last와 실제 실행 설정은 이번 두 코드의 전문 독해만으로 확인되지 않는다. 모든 설정에서 실패한다고 단정하지 않는다.

<a id="c16"></a>**C16.** backbone의 forward는 KL·contrastive·CMI 보조 항을 계산하는 구간에 self.training 분기가 없다. 모델을 eval로 둬도 다른 채널 선택과 CMI shuffle을 포함한 보조 항 계산 경로가 남는다. TSTiEncoder의 flag=True/False는 생성 때 정한 두 분기이며 train/eval 전환 자체가 아니다. 이 사실만으로 유한한 예측 tensor가 오염되거나 평가 데이터 누출이 발생했다고 확정하지 않는다.

<a id="c17"></a>**C17.** TSTiEncoder의 mu_avg와 logvar_avg는 일반 속성으로 초기화되며 forward의 NaN 대체와 평균 갱신에도 학습 모드 조건이 없다. 360–363행의 momentum 평균 계산은 곧바로 366–367행의 현재 평균 대입으로 덮인다. 따라서 이 구간을 지속적인 momentum 평균 유지라고 설명할 수 없다. 실제 NaN 발생 여부나 그에 따른 예측·checkpoint 영향은 실행 검증하지 않았다.

<a id="c18"></a>**C18.** Flatten_Head는 individual=True에서 채널별 Linear를, False에서 공유 Linear를 사용한다. TSTiEncoder는 batch와 변수 축을 접어 공유 patch encoder에 전달한다. BatchNorm을 사용하는 학습 경로에서는 접힌 batch·채널에 걸친 정규화 통계도 공유하므로 주석의 channel-independent를 모든 의미의 채널 간 독립성으로 확대하지 않는다. 이를 Tab 기반 소속이나 공유 모델의 효과 증거로 쓰지 않는다.

<a id="c19"></a>**C19.** 논문은 Algorithm1의 시간 복잡도를 O(M d²+L d)로 적는다. 저장 코드의 patch encoder에서는 q·k 곱으로 patch 수×patch 수 attention 점수 배열을 만든다. 따라서 그 문장만으로 저장 구현 전체의 계산량이나 RCTL과의 비용 우열을 확정하지 않는다. 실제 설정의 차원·layer·batch 및 연산 횟수와 실행 시간은 측정하지 않았다.

## Validation·test·predict의 차이

<a id="c20"></a>**C20.** exp_main.vali는 eval/no_grad 상태에서 예측값과 정답의 마지막 pred_len 및 features 설정에 따른 열을 자르고, MSE에 vaeloss를 더한 값을 batch별로 모아 단순 평균한다. 종료할 때 train 모드로 돌린다. 이 validation 값은 test 메서드가 예측 배열에서 따로 계산하는 MSE·MAE 자체와 구별해야 한다.

<a id="c21"></a>**C21.** 학습 루프는 매 epoch validation과 test loader에 vali를 호출한다. early_stopping에는 vali_loss를 전달하지만 nni.report_intermediate_result에는 test_loss를 전달한다. best checkpoint를 다시 읽는 경로도 있다. 외부 tuner가 이 보고값을 선택에 쓰는지 확인할 필요가 있으나 실제 NNI 설정·시행 내역을 읽지 않았으므로 논문 실험의 데이터 누출을 확정한 것으로 쓰지 않는다.

<a id="c22"></a>**C22.** CIBMTSF의 test 경로는 AMP 사용 여부와 관계없이 (outputs, vaeloss)를 분리하고 예측 tensor를 잘라 numpy 배열로 모은 뒤 metric에 전달한다. pred.npy 저장은 활성화돼 있고 metrics.npy·true.npy·x.npy 저장은 주석이다. metric 구현, 정규화·역변환, 분할, 실행 설정 및 실제 생성 파일은 별도로 확인하지 않았으므로 이 메서드만으로 완전한 재현 자료가 확보됐다고 할 수 없다.

<a id="c23"></a>**C23.** 반면 predict의 CIBMTSF 분기는 AMP/비AMP 모두 모델 반환을 outputs 하나에 받은 뒤 375행에서 detach를 호출한다. H116에서 확인한 고정 커밋의 비decomposition wrapper는 (예측 tensor, 보조 손실) tuple을 반환하므로 이 조합과 맞지 않는다. H116의 학습 AMP tuple slicing 문제와도 별개다. 올바르게 분리하는 test 경로까지 같은 오류라고 쓰지 않으며 실제 호출·오류 재현은 하지 않았다.

## 보존과 검수 범위

<a id="c24"></a>**C24.** 저장 backbone 585행과 exp_main 389행을 모두 읽었다. H116에서 미독한 333행·169행을 이어 읽고 이전 구간 472행도 재독했다. 공식 커밋 ac09a66245f9eaa7371065ec3f7d3673df125c94와 저장 바이트의 줄끝 차이, 외부 wrapper의 고정 버전 근거는 H116 대조를 재사용한다. 원 연구 코드를 실행하거나 import하지 않았으며 이 저장 버전의 정적 발견을 현재 최신 구현 전체에 일반화하지 않는다.

<a id="c25"></a>**C25.** 이번에는 H116의 알려진 후속 7그룹 모두를 읽고 13개 원본 경로의 해시를 대조했다. 계획·후보·연혁 3개는 바이트 동일 사본으로 보존하고, 이전 판본 2개와 snapshot29 manifest는 기존 보존판으로 연결한다. 외부 PDF·TXT·두 코드는 공식 링크·해시·읽은 범위로 연결한다. snapshot29의 24파일 보존 대조는 H116에서 확인한 근거를 재사용하며 파일 수를 연구 완독 수로 바꾸지 않는다.

<a id="c26"></a>**C26.** 이번 검수의 집계 증분은 독립 본문 6개(MD3·기존 부분 코드2·기존 부분 PDF1)의 완료 추가와, 앞서 부분으로 센 3개의 선택 전용 집계 제외다. 전체 JSON·독립 이미지 추가는 없고 TXT·재독·렌더는 중복 가산하지 않는다. 알려진 7그룹의 독해 완료가 원88 이후 문헌·후속 판본·모든 코드 의존성·기존 공백·전체 통합과 팀 접근 검수의 완료는 아니다. 전체 Goal은 계속 진행 중이다.

## 이미 검토한 결정을 찾는 표

22행의 원문 판단·행 위치는 [결정표 대응](../evidence/0117-conditional-history-cib/candidate-map.json), 연혁38절은 [연혁 대응](../evidence/0117-conditional-history-cib/chronology-map.json)에 있다.

| 바꾸려는 결정 | 원 연구 번호 | 상세 기록 |
|---|---|---|
| 공유할 함수/모델 소속 | 02–09,23–28 | [검토](0004-0007-b2-observed-risk.md) |
| subgroup의 유한학습 손해 | 33–38 | [검토](0033-0035-process-fit-gap.md) |
| 소속 고정 뒤 RCTL 학습 공유 | 28,38,86 | [검토](0114-shared-training-scope.md) |
| cell 정보·target 좌표 | 14–22 | [검토](0020-0021-target-parameterization.md) |
| 입력 cell 선택·공유 | 18,45–47,75 | [검토](0047-input-sharing-roles.md) |
| 공동 입력·cell별 다중 출력으로 학습 단위 변경 | 47,74–75,81,87 | [검토](0116-causal-capacity-reference.md) · [기존 비용](0090-input-partition-decision.md) |
| 조건을 보존하는 sample 비교 | 28,47,81,87–88 | [검토](0116-causal-capacity-reference.md) |
| 학습 sample 재사용·고정 처리량 배분 | 39–40,85 | [검토](0039-0040-sample-reuse.md) |
| 학습 sample 압축 | 56–58,85 | [검토](0056-0058-mae-sampling.md) |
| 그룹 보호·피크 목적 | 41–44,66–71 | [검토](0066-0068-group-risk.md) |
| 관측 자료·해상도 | 29–32,51–55 | [검토](0029-0032-resolution-diagnostic.md) |
| 실제 무통신과 양의 트래픽을 구별한 공유 | 82 | [검토](0099-intermittence-decision.md) |
| 합계·대표예측으로cell복원 | 48–50 | [검토](0048-0049-aggregation-recovery.md) |
| 필요한 입력길이 | 59–62 | [검토](0059-0062-history-grouping.md) |
| baseline·residual·조건부분포변환 | 63–65 | [검토](0063-0065-synthesis.md) |
| 학습기 계수/중요도로clustering | 72–73 | [검토](0072-globalization-audit.md) |
| 예측 가능한 출력공간 압축 | 73–74 | [검토](0072-0075-output-compression.md) |
| 관계를 최종 학습 loss에 전달 | 43–44,76 | [검토](0076-response-transfer-audit.md) |
| 시간 조건별 cell 소속·모델 배정 | 17,27,32,77 | [검토](0077-dynamic-membership-dlm.md) |
| 정적 cluster의 공동 갱신 비용 | 17,77,83 | [검토](0105-joint-update-cost.md) |
| 공통 probe의 task 표현·전이 점수 | 28,35–38,63–65,72–74,78 | [검토](0079-regression-transferability.md) |
| 분산 학습의 local gradient 불일치 | 79–80 | [검토](0088-conditional-graph-diagnostic.md) |

## 다시 설계할 때 확인할 차이

| 확인할 항목 | 이번에 확인한 범위 | 남은 범위 |
|---|---|---|
| CIB의 표 우위 | 인쇄72지표의 순위와 증가율 산술 | 원 실행·정밀 결과·집계 정의·seed |
| 조건부 비교 | [H116 분포·반례](0116-causal-capacity-reference.md#c12) | 원88 후속 원문·실제 조건부 생성·소속 결정의 이득 |
| 코드 평가 | 고정 저장판의 validation/test/predict 경로 | data loader·설정·metric 구현·실제 호출 |
| 실험 설계의 독창성 | 이전22판단과 긍정 결과·재진입 조건 | Tab이 바꾸는 결정과 단순 대안 대비 추가 근거 |

[표 산술](../evidence/0117-conditional-history-cib/table-audit.json) · [대조 손실 반례](../evidence/0117-conditional-history-cib/contrastive-audit.json) · [코드 경로](../evidence/0117-conditional-history-cib/code-path-audit.json) · [남은 범위](../evidence/0117-conditional-history-cib/packet-coverage.json)
