# 원96 RCTL 가중치 병합의 적용 범위

**상태:** 2026-09-26 당시 문헌·기존 코드·기호 검토 후 후보 미채택. 실제 병합 모델의 성능 실험은 없었다. 32개 주장과 6개 검수 묶음을 작성 후 원문에 대조했다.

[출처와 실제 판독 범위](../sources/history-126.md) · [검수](../verification/history-126.md) · [보존 근거](../evidence/0126-rctl-parameter-merging-scope/README.md) · [네 문헌 비교](../references/parameter-merging.md) · [직전 원95 비용 기준](0125-frozen-rctl-serving-cost-baseline.md)

Tab이 추정한 cell의 예측 관계와 RCTL 내부 파라미터의 병합 가능성은 별도로 확인해야 한다. 같은 무작위 초기화를 사용했다는 코드 조건을 보존하며, 소속을 먼저 고정한 뒤의 학습·병합은 재검토 가능한 대안으로 남겼다. 이번 미채택을 모델 병합 전체의 성능 실패로 읽지 않는다.

새 실험 전에는 [공통 초기화](#claim-06), [정렬·BN 처리](#claim-10), [출력 혼합](#claim-15), [수식 적용 범위](#claim-18), [소속 확정 순서](#claim-21), [강한 비교군](#claim-22), [재검토 조건](#claim-25)을 먼저 확인한다. 원문 속 Goal·예산·명령은 역사 자료다.

| 항목 | 이번 기록의 범위 |
|---|---|
| 실제 질문 | Tab의 예측 관계로 병합 대상을 정하는 것이 RCTL에 유용한가 |
| 새 자료·분할·정규화·seed·성능 지표 | 새 모델 실험이 없어 해당 없음. 기존 RCTL 코드의 조건만 정적으로 확인 |
| 검토한 연산 | 파라미터 평균·좌표 정렬·BN 처리·출력 혼합·task-vector 병합 |
| 성능·latency 결과 | 새 병합 결과 없음. 동일 시각 batch 비용은 원95의 기존 근거 |
| 실제 현재 읽기 | 새 원문791행/기존 코드203행, 논문 텍스트23페이지·원 PNG6개 |

## <a id="claim-01"></a>01. 미실행 후보를 정리한 문헌·기호 검토

원96(2026-09-26)은 TabICLv2가 추정한 cell 간 예측 관계를 학습된 RCTL의 가중치 병합으로 연결할 수 있는지 검토한 기록이다. 논문·기존 코드·기호 반례를 확인한 뒤 이번 후보를 채택하지 않았다. 병합 checkpoint를 만들어 성능을 측정한 실행 실패가 아니다.

근거: [SRC-0001822](../sources/history-126.md#src-0001822) [[1, 34]]행, [SRC-0001825](../sources/history-126.md#src-0001825) [[1, 9], [56, 67]]행, [SRC-0001826](../sources/history-126.md#src-0001826) [[1, 28]]행.

## <a id="claim-02"></a>02. 예측값 혼합과 파라미터 평균의 대상

여러 모델의 출력에 가중치를 주는 예측값 혼합과, 파라미터를 평균해 하나의 모델로 만드는 병합은 계산 대상이 다르다. TIMEFUSE의 출력 혼합과 Model soups의 가중치 평균을 같은 한 모델 실행으로 부르지 않는다.

근거: [SRC-0001836](../sources/history-126.md#src-0001836) PDF [3, 4, 5]페이지, [SRC-0001840](../sources/history-126.md#src-0001840) PDF [3]페이지, [SRC-0001825](../sources/history-126.md#src-0001825) [[11, 20]]행.

## <a id="claim-03"></a>03. Tab의 예측 관계가 hidden 좌표를 식별하지 않는다

cell의 예측값·조건부 예측 관계가 비슷하다는 관찰만으로 RCTL 내부 채널·LSTM 상태의 대응이나 파라미터 평균의 손실을 알 수는 없다. 원96은 그 연결을 별도로 확인할 필요를 제시했으며, 실제 RCTL에서 병합 손해를 측정했다고 주장하지 않았다.

근거: [SRC-0001825](../sources/history-126.md#src-0001825) [[22, 40]]행, [SRC-0001828](../sources/history-126.md#src-0001828) [[66, 70]]행, [SRC-0001832](../sources/history-126.md#src-0001832) [[15, 60]]행.

## <a id="claim-04"></a>04. 같은 함수의 파라미터 평균이 다른 함수가 되는 예

원문의 f(x)=a·ReLU(w·x)에서 (a,w)=(1,1)과 (1/2,2)는 모든 입력에서 같은 ReLU(x)를 계산한다. 좌표별 평균은 (3/4,3/2)이므로 9/8·ReLU(x)가 된다. 입력·출력의 동등함만으로 파라미터 평균의 동등함을 보장할 수 없다는 기호 예다.

근거: [SRC-0001825](../sources/history-126.md#src-0001825) [[24, 30]]행, [SRC-0001831](../sources/history-126.md#src-0001831) [[7, 14]]행.

## <a id="claim-05"></a>05. 기호 반례를 실제 RCTL의 실패로 확대하지 않는다

이 ReLU 예는 실제 RCTL 구조·SGD 학습·공통 초기화 후 궤적에 대한 실증 결과가 아니다. 채널 scaling이나 순열을 먼저 정렬하는 방법, 특정 학습 조건에서의 성공까지 부정하는 반례로 사용하지 않는다. 단순 평균과 출력 평균이 언제나 같다는 주장에 한정한다.

근거: [SRC-0001825](../sources/history-126.md#src-0001825) [[30, 32]]행, [SRC-0001838](../sources/history-126.md#src-0001838) PDF [6, 7, 8]페이지.

## <a id="claim-06"></a>06. 각 fit의 같은 seed와 무작위 초기화

보존된 train_rctl_pilot.py는 각 fit 안에서 random.seed, numpy seed, torch.manual_seed를 다시 설정한 다음 같은 shape의 RCTL을 생성한다. 따라서 같은 seed인 fit의 출발 무작위 가중치는 같다는 코드 조건이다. 공통 사전학습 가중치를 불러오는 설계는 아니다. 이 정적 확인을 새 모델 초기화·실행으로 세지 않는다.

근거: [SRC-0001834](../sources/history-126.md#src-0001834) [[78, 90]]행, [SRC-0001832](../sources/history-126.md#src-0001832) [[32, 48]]행, [SRC-0001825](../sources/history-126.md#src-0001825) [[34, 40]]행.

## <a id="claim-07"></a>07. 같은 출발점과 학습된 상태의 동일함을 구분한다

같은 seed여도 cluster별 학습·검증자료가 다르고, batch 순서·epoch 진행·선택된 checkpoint가 달라질 수 있다. 코드의 validation MAE로 best_state를 선택해 저장하는 조건과 공통 출발점은 별개다. 초기화가 같다는 사실만으로 최종 BN buffer·LSTM 가중치나 병합 성능이 같다고 쓰지 않는다.

근거: [SRC-0001834](../sources/history-126.md#src-0001834) [[79, 127]]행, [SRC-0001832](../sources/history-126.md#src-0001832) [[15, 30]]행.

## <a id="claim-08"></a>08. Model soups가 출발하는 공통 사전학습

Model soups §2는 공통 pretrained θ0에서 서로 다른 설정으로 fine-tuning한 θi를 평균한다. 같은 random seed로 처음부터 RCTL을 학습하는 현재 보존 코드와 구별한다. 이 논문의 이미지·텍스트 분류 결과를 현재 RCTL 회귀의 성능 보장으로 옮기지 않는다.

근거: [SRC-0001840](../sources/history-126.md#src-0001840) PDF [3]페이지, [SRC-0001834](../sources/history-126.md#src-0001834) [[78, 90]]행.

## <a id="claim-09"></a>09. Greedy soup가 사용하는 validation 판단

Greedy soup는 개별 모델의 validation 성능으로 후보를 정렬하고, 후보를 평균에 넣었을 때 held-out validation 성능이 유지·개선되는지 평가한다. 이를 cell 소속 결정 전에 RCTL 결과로 쓰면 당시 독립성 조건이 바뀐다. 소속을 먼저 고정한 뒤 내부 학습·병합을 비교하는 절차는 별도로 검토할 수 있다.

근거: [SRC-0001840](../sources/history-126.md#src-0001840) PDF [3]페이지, [SRC-0001825](../sources/history-126.md#src-0001825) [[15, 16], [42, 44]]행, [SRC-0001828](../sources/history-126.md#src-0001828) [[70, 70]]행.

## <a id="claim-10"></a>10. Git Re-Basin의 세 정렬 방법

Git Re-Basin은 hidden unit 대응을 찾은 뒤 가중치를 정렬한다. activation matching은 자료의 activation을, weight matching은 학습된 가중치를 사용한다. STE 방식은 병합 loss를 이용한 gradient 최적화를 포함한다. 셋을 모두 자료·gradient가 필요 없는 단순 평균으로 요약하지 않는다.

근거: [SRC-0001838](../sources/history-126.md#src-0001838) PDF [4, 5, 6]페이지.

## <a id="claim-11"></a>11. Git Re-Basin의 성공과 적용 한계

해당 논문은 특정 구조·자료에서 순열 정렬 후 interpolation의 손실을 줄이지만 모든 모델의 zero-barrier를 보장하지 않는다. §4의 반례는 비SGD 해를 다루며, §5.4의 split-data 병합은 combined-data 학습 및 ensemble보다 약했다. 이를 RCTL 병합 전체의 불가능성이나 union-data 기준의 불필요함으로 바꾸지 않는다.

근거: [SRC-0001838](../sources/history-126.md#src-0001838) PDF [6, 8]페이지.

## <a id="claim-12"></a>12. RCTL의 BN 상태와 recurrent·잔차 연결

현재 RCTL은 Conv→BatchNorm→ReLU·dropout, LSTM, 여러 잔차/projection 연결을 갖는다. hidden 채널을 재배열한다면 연결된 입출력·LSTM gate와 recurrent 좌표·잔차 경로의 대응을 함께 보존해야 한다. 원96은 이 구조의 실제 정렬·병합 성공을 검증하지 않았다.

근거: [SRC-0001832](../sources/history-126.md#src-0001832) [[15, 60]]행, [SRC-0001825](../sources/history-126.md#src-0001825) [[34, 40]]행.

## <a id="claim-13"></a>13. BatchNorm 통계 재추정의 역할과 비용

Git Re-Basin Appendix A.3–A.4는 CIFAR의 LayerNorm 변형과 ImageNet ResNet50의 BN 통계 재계산을 구별한다. 학습된 BN affine 파라미터와 running mean/variance는 다르다. 앞단 가중치를 바꾼 뒤 통계를 단순 평균하는 것을 올바른 보정으로 가정하지 않으며, 자료로 통계를 다시 맞추는 과정은 모델 상태 갱신과 준비 비용이다.

근거: [SRC-0001838](../sources/history-126.md#src-0001838) PDF [21]페이지, [SRC-0001832](../sources/history-126.md#src-0001832) [[18, 29]]행, [SRC-0001825](../sources/history-126.md#src-0001825) [[38, 40]]행.

## <a id="claim-14"></a>14. 고정 BN folding의 가능성과 남는 비선형 문제

고정된 inference BN을 앞선 Conv의 계수·bias에 접어 넣는 변환은 가능하다. 이 변환은 통계 재추정 없이 같은 고정 함수를 표현하는 조건부 대안이다. 그러나 두 모델의 비선형·LSTM·잔차 가중치를 평균해 같은 함수를 얻는 보장은 별개다. 원96에서 실제 folding 또는 병합을 실행하지 않았다.

근거: [SRC-0001825](../sources/history-126.md#src-0001825) [[38, 40]]행, [SRC-0001832](../sources/history-126.md#src-0001832) [[15, 60]]행.

## <a id="claim-15"></a>15. TIMEFUSE는 입력별 출력 혼합이다

TIMEFUSE는 입력 시계열의 24개 요약 특징을 한 층 fusor와 softmax에 넣어 base 모델별 혼합 비중을 정한다. 최종값은 여러 base 모델 예측의 가중합이다. 모델 zoo를 하나의 RCTL 파라미터로 압축한 방법이 아니며, 기존 cell당 지정 모델 하나 실행보다 싸다는 근거도 아니다.

근거: [SRC-0001836](../sources/history-126.md#src-0001836) PDF [3, 4, 5]페이지, [SRC-0001825](../sources/history-126.md#src-0001825) [[17, 18], [46, 48]]행.

## <a id="claim-16"></a>16. TIMEFUSE의 meta-training 자료와 평가 범위

Fusor는 base 모델 학습에 쓰지 않은 validation 입력의 특징·base 예측·실제 정답으로 학습하며 논문은 Huber loss를 사용한다. 이 예측·정답을 사용한 meta-training과 단순 input-only 규칙을 구분한다. 논문 benchmark 결과는 현재 Milan/TabICLv2/RCTL의 재현·개선 결과가 아니다.

근거: [SRC-0001836](../sources/history-126.md#src-0001836) PDF [4, 5]페이지.

## <a id="claim-17"></a>17. 확률적 병합의 task vector 출발점

UAI2026의 보존 판본은 공통 pretrained W0에서 fine-tuning한 Wi의 task vector θi=Wi−W0를 PoE energy/MAP로 합치는 문제를 정의한다. 현재 RCTL의 무작위 초기화와 동일한 전제라고 가정하지 않으며, conditional prediction 유사도를 이 파라미터 energy로 바로 치환하지 않는다.

근거: [SRC-0001842](../sources/history-126.md#src-0001842) PDF [2, 5]페이지, [SRC-0001825](../sources/history-126.md#src-0001825) [[18, 18], [50, 54]]행.

## <a id="claim-18"></a>18. 같은 PDF의 residual 분모 표기 차이

보존 UAI PDF6의 Eq23은 residual 제곱+γ²를 사용하지만 Algorithm1 line7은 residual 제곱+γ·‖θi‖²를 쓴다. Appendix의 식에서도 γ²·γ·η 표기가 달라지는 부분이 있다. 원96의 지적을 실제 이미지로 대조했다. 공식 구현·정오표를 확인해 하나의 식으로 해소한 상태는 아니다.

근거: [SRC-0001842](../sources/history-126.md#src-0001842) PDF [5, 6, 13, 14]페이지, [SRC-0001825](../sources/history-126.md#src-0001825) [[50, 54]]행.

## <a id="claim-19"></a>19. Conditioning 항과 원 energy의 정지점

Eq22의 energy와 Eq24의 양의 ηI를 포함한 mapping은 인쇄된 식 그대로는 같은 정지점 관계를 갖지 않는다. θ=γ=1인 1차원 예에서 Eq22는 log(1+(ζ−1)²)로 ζ=1이 정지점이지만, Eq24는 F(1)=1/(1+η)이다. η>0이면 F(1)≠1이다. 이 기호 대조를 실제 RCTL 병합 실험이나 모든 논문 결과의 무효 판정으로 쓰지 않는다.

근거: [SRC-0001842](../sources/history-126.md#src-0001842) PDF [5, 6, 13]페이지, [SRC-0001825](../sources/history-126.md#src-0001825) [[50, 54]]행.

## <a id="claim-20"></a>20. Local contraction과 전체 RCTL 보장의 차이

해당 판본의 Assumption5.2·5.3은 task vector의 유계성과 fixed point 주변의 iterate 조건을 둔다. AppendixB는 미분 bound와 논문 실험에서의 L<1을 제시한다. Eq24의 ηI와 AppendixA Eq31의 pseudoinverse 및 표기 차이를 해결하지 않은 채 현재 RCTL에 global 수렴·정확도 보장을 적용하지 않는다.

근거: [SRC-0001842](../sources/history-126.md#src-0001842) PDF [6, 13, 14]페이지, [SRC-0001825](../sources/history-126.md#src-0001825) [[50, 54]]행.

## <a id="claim-21"></a>21. 소속을 먼저 고정한 뒤의 학습·병합

RCTL의 학습된 가중치·activation·병합 loss를 보고 cell 소속을 정하면 당시 RCTL 독립 소속 조건이 바뀐다. 반면 소속을 먼저 고정하고 cluster 내부에서 학습·병합하는 순서는 검토 가능한 대안이다. 두 순서를 혼동해 모델 병합을 전부 금지한 기록으로 읽지 않는다.

근거: [SRC-0001825](../sources/history-126.md#src-0001825) [[42, 48]]행, [SRC-0001828](../sources/history-126.md#src-0001828) [[66, 70]]행, [SRC-0001823](../sources/history-126.md#src-0001823) [[1, 51]]행, [SRC-0001824](../sources/history-126.md#src-0001824) [[1, 73]]행.

## <a id="claim-22"></a>22. Union-data 단일 RCTL과 Tab의 유용한 결정

함께 쓸 자료를 이미 모을 수 있다면 해당 union-data로 RCTL 하나를 직접 학습하는 비교군이 필요하다. 모델 병합 방법에 Tab을 붙인다는 사실만으로 효용이 생기지는 않는다. 원93에서 보완한 기준처럼, 새로운 소속 결정 또는 같은 유용한 결정을 더 적은 계산·추정 변동으로 얻는 경로를 구별한다. 기존 global·경험적 소속·공유 학습 대안과 달라지는 점 및 Tab의 기여를 특정한다.

근거: [SRC-0001825](../sources/history-126.md#src-0001825) [[42, 48], [56, 60]]행, [SRC-0001824](../sources/history-126.md#src-0001824) [[1, 73]]행, [SRC-0001828](../sources/history-126.md#src-0001828) [[66, 70]]행, [SRC-0001838](../sources/history-126.md#src-0001838) PDF [8]페이지, [SRC-0001828](../sources/history-126.md#src-0001828) [[42, 58]]행.

## <a id="claim-23"></a>23. 모델 수 K와 예측 입력 수 N의 구분

모델 상태가 K개에서 한 개로 줄어도 서로 다른 cell 입력 N개가 사라지는 것은 아니다. 기존 cell별 scalar 예측은 입력마다 지정 모델 하나를 사용한다. 원95의 동일 시각 batch 기준을 유지하며, 저장량·호출 수·예측 행·실측 latency·입력 준비·Tab 준비를 분리한다.

근거: [SRC-0001825](../sources/history-126.md#src-0001825) [[46, 48]]행, [SRC-0001828](../sources/history-126.md#src-0001828) [[60, 70]]행.

## <a id="claim-24"></a>24. 학습 처리량과 병합 준비 비용

자료를 분할해 여러 모델을 학습하는 비용은 무조건 전체 자료 K회 학습과 같지 않다. 실제 학습 sample·update·epoch 및 정렬/validation/BN 처리 비용으로 비교한다. 최종 가중치를 합친다고 이미 수행한 학습이 없어지지 않는다. 기존 누적 예산의 수치는 역사적 운영 기록이며 현재 아카이브의 실험 허가로 사용하지 않는다.

근거: [SRC-0001825](../sources/history-126.md#src-0001825) [[46, 48], [62, 67]]행, [SRC-0001834](../sources/history-126.md#src-0001834) [[79, 137]]행.

## <a id="claim-25"></a>25. 후보 미채택의 이유와 재검토 조건

이번 미채택은 예측 관계에서 파라미터 좌표로 이어지는 근거, Tab의 유용한 결정, union-data 강한 기준 대비 이득이 확보되지 않았기 때문이다. 실제 자료의 병합 필요성·좌표 처리·학습/검증 순서·전체 비용 및 달라진 질문이 구체화되면 별도 탐색을 검토할 수 있다. 작은 pilot에서 알아낼 성능 차이를 진입 전에 이미 입증하라고 요구하지 않으며, 같은 유용한 결정의 효율 개선도 가능하다. 완전한 보장 부재만으로 모든 병합을 기각하지 않는다.

근거: [SRC-0001822](../sources/history-126.md#src-0001822) [[1, 34]]행, [SRC-0001825](../sources/history-126.md#src-0001825) [[5, 9], [56, 60]]행, [SRC-0001828](../sources/history-126.md#src-0001828) [[42, 70]]행.

## <a id="claim-26"></a>26. 원96의 추가 모델 실행은 없었다

계획·판단·읽기 범위·검수 코드·진행 기록은 새 Tab context/query, RCTL fit/gradient, BN update, frozen inference가 모두0이라고 남긴다. 이번에는 원 연구 코드 실행/import도0이며, 문헌 추출·기호와 저장 metadata 대조만 수행했다. 기존 결과의 hash 확인을 병합 모델 재현으로 표시하지 않는다.

근거: [SRC-0001826](../sources/history-126.md#src-0001826) [[1, 28]]행, [SRC-0001827](../sources/history-126.md#src-0001827) [[1, 104]]행, [SRC-0001835](../sources/history-126.md#src-0001835) [[1, 103]]행, [SRC-0001831](../sources/history-126.md#src-0001831) [[7, 14]]행.

## <a id="claim-27"></a>27. 확보·실제 판독·전문 검증을 구분한다

보존 PDF4개는 총104페이지·7,829,802bytes다. 이번 실제 전체 페이지 텍스트 판독은23페이지이며 관련 원 PNG6개를 전체 시각 대조했다. 나머지81페이지의 텍스트와 다른 시각 내용, 공식 구현 감사·실행은 남아 있다. 당시 읽기 범위 flag, 추출 완료, 파일 크기만으로 전문 검증을 완료 처리하지 않는다.

근거: [SRC-0001844](../sources/history-126.md#src-0001844) [[1, 57]]행, [SRC-0001827](../sources/history-126.md#src-0001827) [[1, 104]]행, [SRC-0001845](../sources/history-126.md#src-0001845) [[1, 32]]행, [SRC-0001836](../sources/history-126.md#src-0001836) PDF [3, 4, 5]페이지, [SRC-0001838](../sources/history-126.md#src-0001838) PDF [3, 4, 5, 6, 7, 8, 21]페이지, [SRC-0001840](../sources/history-126.md#src-0001840) PDF [2, 3, 4, 8, 9]페이지, [SRC-0001842](../sources/history-126.md#src-0001842) PDF [2, 3, 4, 5, 6, 13, 14, 15]페이지.

## <a id="claim-28"></a>28. 다운로드·렌더링의 도구 이력

원문은 PDF 확보 URL/hash와 관련6페이지 렌더 metadata를 보존했다. dotted filename을 suffix로 처리한 첫 렌더 오류를 고치고 기존2개를 재사용해 나머지4개를 생성한 것은 문서 변환 이력이다. 모델 병합·추론의 구현 실패나 연구자료 손실로 분류하지 않는다. 원 fetch/render/verify 스크립트는 이번에 실행하지 않았다.

근거: [SRC-0001830](../sources/history-126.md#src-0001830) [[1, 40]]행, [SRC-0001833](../sources/history-126.md#src-0001833) [[1, 21]]행, [SRC-0001835](../sources/history-126.md#src-0001835) [[1, 103]]행, [SRC-0001844](../sources/history-126.md#src-0001844) [[1, 57]]행, [SRC-0001845](../sources/history-126.md#src-0001845) [[1, 32]]행.

## <a id="claim-29"></a>29. Snapshot38과 기존 원본의 보존 범위

Snapshot38은 manifest가 열거한30개 파일10,954,157bytes에 manifest6,511bytes를 더한 실제31개 파일10,960,668bytes다. 별도 원 archive 검수 receipt는394bytes다. 사본 hash와 보호된 기존 원본은 대조하지만, 별도로 남은 중간 Word의 hash 확인을 본문·layout 검수로 세지 않는다.

근거: [SRC-0001821](../sources/history-126.md#src-0001821) [[1, 160]]행, [SRC-0001835](../sources/history-126.md#src-0001835) [[1, 103]]행, [SRC-0022098](../sources/history-126.md#src-0022098) [[1, 9]]행.

## <a id="claim-30"></a>30. 후보 인덱스와 연혁의 판본

이번 후보 인덱스1828은 전체1–70행을 읽었고 이전1803의64행 판본과 대조했다. 현재 연혁1831은1–66/545행만 읽어67–545행이 남는다. 직전1805의58–536행도 직접 미독이다. 새 원96 항목의 추가와 기존 내용의 기계 대응을 후반 연혁의 독해 완료로 바꾸지 않는다.

근거: [SRC-0001828](../sources/history-126.md#src-0001828) [[66, 70]]행, [SRC-0001831](../sources/history-126.md#src-0001831) [[7, 14]]행.

## <a id="claim-31"></a>31. PDF 추출 TXT·PNG는 독립 연구 결과가 아니다

TXT4개와 PNG6개는 같은 PDF의 파생 자료이므로 별도 독립 내용 가산은0이다. 새 추출과 원 TXT의 기계 대조에서 UAI PDF14만 빈줄 한 줄 차이가 있었고 nonblank 내용은 같았다. 추출 일치와 기계 비교를 literal TXT 전문의 직접 판독이나 독립 재현으로 집계하지 않는다.

근거: [SRC-0001830](../sources/history-126.md#src-0001830) [[1, 40]]행, [SRC-0001833](../sources/history-126.md#src-0001833) [[1, 21]]행, [SRC-0001845](../sources/history-126.md#src-0001845) [[1, 32]]행, [SRC-0001842](../sources/history-126.md#src-0001842) PDF [14]페이지.

## <a id="claim-32"></a>32. 남은 연구 범위와 미완료 판단

당시 최종 추천 방향과 최종 Word는 미완료였다. 이번 원96 기록의 검수·병합도 전체 연구기록 정리 완료를 뜻하지 않는다. 원97 이후·이전 고유 판본, 문헌과 연혁의 미독, FedPPBC/DOCX 공백, 전체 통합·장기 팀 접근·최종 원본 변경분·대표 질문 검색 검수는 이어서 처리한다.

근거: [SRC-0001822](../sources/history-126.md#src-0001822) [[1, 34]]행, [SRC-0001825](../sources/history-126.md#src-0001825) [[56, 67]]행, [SRC-0001831](../sources/history-126.md#src-0001831) [[7, 14]]행, [SRC-0001828](../sources/history-126.md#src-0001828) [[51, 58]]행.

## 팀 재검토 안내

[원86 학습 공유](0114-shared-training-scope.md), [원93 탐색 기준](0123-candidate-gates-comparison-scope.md), [원95 batch 비용](0125-frozen-rctl-serving-cost-baseline.md)을 함께 읽는다. 새로운 소속 결정과 같은 유용한 결정의 효율 개선을 구분하고, union-data 비교군·소속 확정 시점·정렬/BN 준비 및 전체 비용을 이슈에 적는다. 당시 새 fit0 상한을 미래 팀 실험 전체의 금지로 해석하지 않는다.

현재 연혁67–545행·직전58–536행, 네 PDF의 나머지81페이지 텍스트와 다른 시각 내용·literal TXT 전문 직접 판독, 원97 이후와 이전 고유 판본, FedPPBC·DOCX 공백, 전체 문헌·실패·비용 통합, 장기 팀 접근, 최종 원본 변경분과 대표 질문 검색 검수.

후속 [원97](0127-forecast-time-reuse-diagnostic.md)은 가중치 병합을 실행하지 않고 고정된 모델의 과거 최종 출력/증가량을 재사용했다. 내부 정확한 delta 계산과 출력 근사를 구별하고, global 재사용·persistence·기본 batch를 후속 비용 후보의 기준에 추가했다.
