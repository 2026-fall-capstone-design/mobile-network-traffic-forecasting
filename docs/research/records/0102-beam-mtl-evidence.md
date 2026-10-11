# Beam GRU-MTL의 발생·양 결합과 성능 근거 대조

[출처](../sources/history-102.md) · [검수](../verification/history-102.md) · [표](../evidence/0102-beam-mtl/table-review.json) · [개선율 계산](../evidence/0102-beam-mtl/scalar-check.json)

**핵심:** 공유GRU와 발생·양head는 확인되지만 hard gate의 학습 경로·평가 척도와 일부 성능 수치는 미확인 또는 원문 내부 차이가 남는다. 팀의 새 설계는 이 구조와 실제로 다른 공유 결정부터 설명해야 한다.

[원82의 판단](0099-intermittence-decision.md)을 잇는 문헌 검수다. H102는 정리 ID이며 새 모델 실행이나 독립 성능 재현이 아니다.

**상태:** 34개 주장·6개 묶음의 작성 후 원문·그림 대조 완료.

## 당시 질문과 데이터

<a id="c01"></a>**C01.** 원82는 간헐 트래픽을 새 모듈로 추가하기 전에 기존 발생/양 공동 학습과 실제 데이터 문제를 검토했다. H102는 그때 확보한 Beam GRU-MTL 논문을 대조한 정리용 기록이다. 새 실험102회, 현재 TabICL 학습, 독립 재현이나 연구 방향 변경으로 세지 않는다.

<a id="c02"></a>**C02.** Israel Tommy·Taoreed Akinola·Xiangfang Li·Lijun Qian의 논문은 Frontiers in Communications and Networks6:1658461, 2025-10-24, DOI10.3389/frcmn.2025.1658461이다. 저장 HTML 메타데이터의 2026-09-25 수정일을 발표일로 쓰지 않는다. 당시 manifest는 HTML 확보 기록이며 PDF의 입수 URL·시각을 증명하지 않는다. PDF는 저장 파일의 해시·17쪽을 확인했다.

<a id="c03"></a>**C03.** 본문은 ITU AI for Good의 30BS×3cells×32beams=2,880beams,5주·840시간과 DLThpVol·DLThpTime·DLPRB·MR_number 네 자료를 기술한다. 각 자료의2,419,200은2,880×840 관측 수이며 같은 수의 학습 window를 뜻하지 않는다. 실제 날짜·시간대·다운로드 파일을 이번에 검증하지 않았다.

<a id="c04"></a>**C04.** 평균915개zero·1,965개nonzero라는 보고를2,880으로 나누면 약31.77%다. 논문의32%·31.8%는 beam–time 관측의0 빈도에 관한 설명이며 항상0인beam의 비율이나 조건부 발생확률 P(Y>0|x)가 아니다. 본문은 대략20%에서40%초과라고 서술하고 Fig.5b의 세로축에는25–50% 눈금이 표시되어 있다. 그림의 정확한 최솟값·최댓값을 역산하지 않았다.

<a id="c05"></a>**C05.** Fig.1의 caption·도식은 BS당3users와 user당32beams를 쓰지만 §1.1 본문은 BS당3cells와 cell당32beams를 쓴다. 이 차이를 보존하며 사용자를cell과 동일한 관측 단위로 확정하지 않는다.

<a id="c06"></a>**C06.** Fig.2–4는 여섯beam의 네 metric을 각각 보여 준다. 가로축은 시간 index, 세로축은0–1 범위로 표시되어 있고0구간·peak·일부 긴 저활동 구간이 보인다. 이것만으로 모든0의 실제 원인, 학습용 scaler의 fit 범위나 모든beam의 규칙성을 확인하지 않는다.

## 구조·학습·평가 조건

<a id="c07"></a>**C07.** Fig.6과 Eq.1–4는 GRU의 update/reset gate 및 hidden state 갱신, 최종 hidden state를 공유하는 회귀·분류head를 설명한다. 입력 설명의 T=672·F=2880은4주 training matrix이며 Table1의 개별 입력 길이168/24/8과 구별한다. 모든feature의 동시 사용이나 실제 network 구현은 도식만으로 검증되지 않는다.

<a id="c08"></a>**C08.** Eq.5는 linear regression, Eq.6은 round(sigmoid(...))로0/1 activation map, Eq.7은 두 출력의 원소곱이다. 이 hard gate를 연속 발생확률 p(x)와 양수일 때의 조건부 평균을 곱한 모형으로 자동 해석하지 않는다. 회귀head가 양수 자료에만 학습되는지는 미확인이다.

<a id="c09"></a>**C09.** Eq.8–10은 가중 MSE+BCE를 제시하고 BCE의 예측값은 발생확률이라고 설명한다. Eq.6의 반올림이 추론에만 쓰이는지, MSE가 gate 전후 어느 출력에 적용되는지는 코드 대조가 필요하다. 문서의 hard gate만으로 gradient가0인 구현 오류나 예측 실패를 단정하지 않는다.

<a id="c10"></a>**C10.** 본문은 λ_reg=λ_cls=1이라고 쓰지만 Table4와 ablation 본문은 가장 낮은 MAE의 balanced 설정을 각각0.5로 표시한다. 두 설정의 비율은1:1로 같고 합산 loss의 공통배율은 다르다. 같다고 합치거나 성능 차이의 원인으로 확정하지 않는다.

<a id="c11"></a>**C11.** Algorithm1은 GRU-MTL의 regression head만, GRU-Linear, XGBoost(GRU(X))의 출력을 α+β+γ=1인 가중평균으로 합친다. 입력 normalize/scale 단계도 있다. 실제 가중치는 제시되지 않았고, regression head only라는 명시는 Eq.7의 gate를 통과한 MTL 출력과 구별된다.

<a id="c12"></a>**C12.** §3.2.8 뒤쪽 문단은 ensemble 가중치를 training weeks에서만 배우고 test에는 고정한다고 보고한다. §4.2.5의 dynamic weighting이라는 후속 설명도 남아 있다. 실제 선정 로그·검증 분할·test 누출 여부는 확인하지 않았으며, 이 문장들을 같은 구현의 검증 결과로 합치지 않는다.

<a id="c13"></a>**C13.** 처음4주로 학습하고5주차를 평가한다. training에서는8/24/168 길이 window를 이동시키며, test는4주차 마지막 window에서 시작해 예측값을 다시 입력하는 recursive rollout을 설명한다. Fig.8의 예측 재입력도 확인했다. 입력 길이168시간과 예측 대상5주차, 관측값을 매번 갱신하는1-step 평가를 구별한다.

<a id="c14"></a>**C14.** 명시적 timestamp가 없어 같은 index가 같은 시간이라는 pre-alignment를 가정한다. 네 metric을 확보했다는 설명, 입력 F=2880, 추가 PRB·시간·user feature 활용을 future work로 둔 설명을 함께 보존한다. 실제로 네 metric을 모두 함께 넣었다고 확정하지 않는다.

<a id="c15"></a>**C15.** §4.1.1은 명시적 normalization/standardization·imputation·수동 feature engineering을 하지 않았다고 기술한다. Algorithm1의 normalize/scale과 Fig.2–4의0–1 축도 확인된다. 적용 대상과 척도를 코드로 확인하기 전에는 train-only 정규화나 누출을 확정하지 않는다.0이 의미 있는 inactivity라는 저자 해석은 관측 누락 원인을 직접 검증한 결과와 구별한다.

<a id="c16"></a>**C16.** 비교군은 Linear·DLinear·XGBoost·ESN·LSTM·MTL이다. §3.2 도입부의 ESN raw sequence 설명과 §3.2.4의 GRU embedding을 reservoir에 전달한다는 설명에 차이가 있다. Table1의 ESN core 표기까지 연결하고 특정 구현으로 임의 통일하지 않는다.

<a id="c17"></a>**C17.** Table1은 모든 열에 hidden1024·batch128·Adam을 적고, Linear/DLinear/XGBoost/ESN/LSTM/MTL 순서로 학습률0.01/0.0001/0.1/0.000001/0.0001/0.001, epochs1500/500/1500/5000/1500/1500을 보고한다. XGBoost 열의 optimizer가 어느 구성요소에 적용되는지도 미확인이다. 표의 설정을 독립 실행으로 검증한 값으로 표시하지 않는다.

<a id="c18"></a>**C18.** 보고 지표는 MAE·MSE·RMSE이며 MAPE는0에 가까운 분모 때문에 불안정하다고 설명한다. 표의 손실 척도·전체 시각/beam 집계 순서·선택 mask는 충분히 특정되지 않았다. 이 MAE를 현재 Internet 원단위·Tab 직접 예측·최종 RCTL 성능과 직접 비교하지 않는다.

## 성능 표와 본문 차이

<a id="c19"></a>**C19.** Table2에서 MTL의168시간 MAE/MSE/RMSE는0.213631/0.249026/0.499025로 같은168시간의 여섯모델 중 가장 낮다. MTL의24시간 MAE는0.300096,8시간은0.282097이며 두 길이에서는 XGBoost의 MAE가 더 낮다. 모든모델에서168시간이 최상이라는 서술은 XGBoost·LSTM 등의 행과 일치하지 않는다. 전체 셀은 근거 표에 보존했다.

<a id="c20"></a>**C20.** Table2의 MTL8시간0.282097에서168시간0.213631로 바뀐 감소율은8시간 값을 분모로 약24.27%다. 반대로168시간을 분모로8시간의 증가율을 계산하면 약32.05%다. 초록의56%감소와 §4.2.3의56%증가는 이 두 표시값으로 재현되지 않는다. 다른 분모·별도 실행 여부는 미확인으로 남긴다.

<a id="c21"></a>**C21.** 초록은 LSTM MAE0.3223을 쓰지만 Table2의168시간 LSTM은0.355919다. 같은 표의24/8시간은0.301782/0.316045다. 또한 ESN·LSTM이 모든조건에서 다른모델보다18–23% 나쁘다는 문장은 비교모델·분모가 특정되지 않고, ESN24시간은 MTL보다 낮은 MAE를 보인다. 차이를 임의 정정하거나 보편적인 모델 순위로 쓰지 않는다.

<a id="c22"></a>**C22.** Table3는 Historical Average·iTransformer·PatchTST·DLinear·Transformer의 Test1/2 점수를 별도로 싣는다. 예를 들어 iTransformer는0.1967/0.2348, MTL168은 Table2의0.213631이다. 두 표가 같은 평가 집합·척도·protocol인지 충분히 특정되지 않으므로 통합 순위나 MTL의 모든Transformer 대비 우위를 주장하지 않는다. 본문도 Table3 대비 MTL 오차가 다소 높다고 적었다.

<a id="c23"></a>**C23.** 분류 전용 MAE/MSE/RMSE는0.398/0.667/0.816, 회귀 전용은0.257/0.405/0.636, balanced0.5/0.5는0.213/0.249/0.499다. λ_reg=1을 고정하고 λ_cls=0.1/0.5/2로 바꾼 MAE는0.218/0.219/0.224다. 이 표는 공동 학습에 대한 저자 보고이며 현재 cell 공유나 확률 calibration의 성능 검증이 아니다. 발생 분류의 precision/recall 수치도 여기에는 없다.

<a id="c24"></a>**C24.** Table5의 without ensemble은 MAE0.218503·MSE0.249026·RMSE0.499025, with ensemble은0.210520/0.246709/0.496698이다. without의 MAE는 Table2의 Linear168 값과, 나머지 두 지표는 MTL168 값과 일치한다. 이 행의 단일 모델 정체를 확정하거나 MAE를0.213631로 고쳐 쓰지 않는다.

<a id="c25"></a>**C25.** Table2의 MTL168 MAE0.213631을 분모로 Table5의0.210520까지 감소한 비율은 약1.456%로, 저자의1.45% 보고에 가깝다. Table5의 without MAE0.218503을 분모로 쓰면 약3.653%다. 서로 다른 기준을 동일한 개선율로 합치지 않으며 반올림 표시값의 산술을 새 모델 평가로 세지 않는다.

<a id="c26"></a>**C26.** §4.2.1은24/8시간을 ensemble 분석에서 제외했다고 쓰지만 §4.2.5는8시간 MAE60%감소를 설명한다. Table5에는168시간 행만 있어60%의 수치 근거가 부족하다. 같은 절의1.45% variance 감소는 MAE 감소와 다른 통계다. ensemble168을 Table2의 LSTM·ESN168 각각과 비교한 MAE 감소는 약40.85%·20.30%여서 둘을45%로 묶을 근거도 미확인이다.

## 반례·비용·재사용

<a id="c27"></a>**C27.** Fig.11–13은 Sample111의 첫100dimensions를 비교한 그림으로,100개 연속시간의 예측 곡선이 아니다. Ground Truth는 파랑, Prediction은 주황이다. MTL·ensemble도 일부 높은peak를 과소예측하며 다른dimension에서는 과대예측이 보인다. 한 표본 그림을 모든beam의 개선, 기간별 손해 분포나 반복 실행의 유의성으로 확대하지 않는다.

<a id="c28"></a>**C28.** 저자는 Python3.8·TensorFlow2.12·scikit-learn1.0.2와 학습용4×A100(각80GB)을 보고한다. 약2.7ms는 단일A100·batch1·입력길이8의 sample 추론이다.168시간 window,5주차 전체 rollout, ensemble, CPU/edge 지연이나 학습시간으로 환산하지 않는다. temporal-only 설명의8–12 길이도 Table1의8/24/168과 구별한다.

<a id="c29"></a>**C29.** 저자 코드·checkpoint·실제 seed·반복수·튜닝 split·모델별 학습시간·메모리 사용량을 이번에 검증하지 않았다. MSE 적용 위치, 분류 threshold와 학습 경로, 양수 조건부 회귀 여부, scaler·feature 입력, ESN 구현, ensemble weights와 표의 평가척도를 확인해야 같은 조건의 재사용이 가능하다. 저장 논문의 실험 보고와 독립 재현을 구별한다.

<a id="c30"></a>**C30.** 논문은 prediction interval·Bayesian 방법·ensemble variance 등을 통한 불확실성 정량화가 포함되지 않았다고 명시한다. 더 세밀한 시간 해상도와 추가features는 후속 방향이다.46개 참고문헌 목록을 읽었으나 해당 논문들을 각각 전문 검토하거나 이 논문의 신규성 주장을 독립 입증하지 않았다.

## 현재 연구의 판단과 남은 범위

<a id="c31"></a>**C31.** 원82가 적은 공유GRU·발생/양head·hard gate·공동 loss라는 선행 구조는 원문에서 확인된다. 그러나5G beam 예측의 수치를 현재 Milan Internet의 간헐성, TabICL 관계 추정이나 UPC/RCTL cell 소속 수정의 효과로 옮길 수는 없다. p(x)와 조건부 양의 평균을 곱한 설명도 이 논문의 hard gate와 동일한 구현이라고 쓰지 않는다.

<a id="c32"></a>**C32.** 원82는 간헐성 모듈을 현재 연구에 추가하지 않는 판단을 남겼다. 재진입에는 관측 누락과 실제 반복 무통신을 구별한 뒤 그것이 예측 손해를 만든다는 증거와, 기존 발생/양 공동 학습과 다른 유용한 공유 결정이 함께 필요하다. H102는 당시 판단의 근거 범위를 보강하며 모든 간헐성 연구를 기각하지 않는다.

<a id="c33"></a>**C33.** PDF17쪽의 본문·참고문헌·13그림·5표·Eq.1–10·Algorithm1, 저장 PDF.TXT1364행·TXT637행, HTML의 전체 연구 본문과 내부 MathML, 기존9/12쪽PNG를 실제 읽었다. HTML/PDF/2TXT 네본문과 기존PNG 두이미지는 한 논문의 표현물이다.12개 바이트 동일 별칭·새렌더·파생JSON·기존 원82 자료3개의 재열람을 추가 연구나 본문으로 세지 않는다.

<a id="c34"></a>**C34.** 원82 일차자료의 남은 대상은 Deep Renewal2그룹이다. snapshot24 후보표·일지의 고유 변경, 별도 코드·재현 조건, 원83 이후와 전체 아카이브 통합도 남는다. 원82 패킷 전체나 전체 Goal을 완료로 표시하지 않는다.

## 같은 조사를 반복하기 전에

| 팀의 질문 | 먼저 확인할 근거 |
|---|---|
| 발생/양 두head가 새로운가 | C07–C11의 기존 구조·hard gate·앙상블 경로 |
| 입력을168시간으로 늘리면56% 좋아지나 | C19–C20의 모델별 표와 분모별 산술 |
| ensemble 이득을 인용해도 되나 | C24–C26의 기준 행·1.456%/3.653% 차이·8시간 근거 부재 |
| 현재 cell 공유 모듈에 적용할까 | C31–C32와 원82의 실제 손해·새 공유 결정 재진입 조건 |

새 실험에는 원문과 같은 점, 달라지는 관측 단위·분할·예측 방식·loss·공유 결정, 비교군과 비용을 먼저 적는다. [후속 자료](../evidence/0102-beam-mtl/packet-coverage.json)는 계속 검토한다.
