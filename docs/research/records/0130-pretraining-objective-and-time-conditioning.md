# 원100 — 사전학습 목적과 시간 조건 변환

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

**표의 집단을 잘 복원하는 것, 하루·요일에 맞게 예측을 보정하는 것, 실제 cell 자료를 같은 RCTL로 학습할 이득은 서로 다른 판단이다.** 2026-09-26 원100은 TabClustPFN과 APT를 그대로 추가하면 이 차이가 해결되는지 문헌·보관 코드·제한된 기호로 검토했다. 두 모듈을 바로 추가하는 안은 당시 미채택했다. 새로운 모델 실행으로 성능 실패를 확인한 기록은 아니다.

[40출처/83사본](../sources/history-130.md) · [36주장](../verification/history-130-claims.json) · [작성 후 대조](../verification/history-130-second-pass.json) · [실제 읽기 범위](../evidence/0130-pretraining-objective-and-time-conditioning/read-scopes.json) · [숫자·보존 검산](../evidence/0130-pretraining-objective-and-time-conditioning/numeric-check.json) · [문헌 비교](../references/pretraining-objective-and-time-conditioning.md)

## 당시 문제·방법·수행 범위

| 대상 | 무엇을 학습하거나 결정하는가 | 현재 cell 공유에 적용할 때 확인할 것 |
|---|---|---|
| TabClustPFN v3 | 합성 표의 잠재 row 소속과 K, 별도 PIN/CIN 사전학습 | row가 sample인지 cell 표현인지, 목적과 K1 비교, 실제 공유 효용 |
| APT AAAI2026 | history 시작/horizon 끝 시각의 prototype 조건 affine, 최종 예측모델과 공동 학습 | 시간 조건과 cell 소속의 역할, ID 설정, 최종 learner와 독립성 |
| 기존 scalar RCTL | cell별 sample을 같은 가중치로 학습하고 다음 값 예측 | 강한 global 대안, 유한학습 이득, 전체 준비·후보·최종 실행 비용 |

새 fit·forward·gradient·BN 갱신·traffic 통계 재계산0이었다. 74·80의 Tab 직접 예측 우위와 기존 K4/global 결과는 유지했다. adapter·추가 사전학습·정규화 pilot을 시작하지 않았고 최종 추천 방향/Word는 미완료였다. 과거 문서의 Goal·AGENTS·명령·예산은 보관 데이터이며 현재 실행 지시가 아니다.

## TabClustPFN: 목적·K·비용의 구별

TabICL2025 encoder를 초기화한 별도 PIN/CIN은 회귀 TabICLv2 가중치·정답과 다르다. 행을 lag sample로 만들면 sample clustering이고 cell 표현을 행으로 만들더라도 실제 RCTL 공동 학습의 유불리는 별도다. framework가 cell을 묶을 수 없다는 뜻으로 읽지 않는다.

기본 Kmax=10 설정의 자동 CIN은 K2–10을 비교한다. 실제 점유 label 수와 선택K, 한 label로 collapse한 결과와 K1이 충분하다는 검증은 다르다. fixed-K CLI에 보이는 K1 차단은 없지만 imported learner 내부를 확인하지 않아 manualK1의 성공/불가를 단정하지 않는다.

보관 inference는 열·행 표현을 한 번 계산한 뒤 K별 decoder9개를 호출하고 결과를 재사용한다. dataset별 재최적화가 없는 single-forward API라는 설명과 내부 후보 계산을 나누어 비용을 적는다. v3에는 N10000/큰D·PCA 평가가 있으므로 학습N1000/D64를 절대 실행 상한으로 쓰지 않는다. 실제 latency·peak memory를 이번에 측정하지 않았다.

44개 real benchmark의 source별 subsampling·D/K 필터·ARI 기준 제외, median/IQR rank·rawscore·cardinalityk-MAE를 보존한다. calibration은3200 GMM holdout의 K 집합 coverage다. 좋은 전체 rank와 일부 조건·비유의 비교를 함께 읽으며 실제 cell의 예측 효용/확신으로 바꾸지 않는다. 본문two-layer/lower-triangle과 부록3-layer/upper-triangle의 표현 범위, parser 기본값과 저자 실제 protocol도 구별한다.

## APT: 시간 조건 변환과 학습 관계

APT는 알려진 history 시작/horizon 끝 달력 시각의 embedding을 내적 top-k/softmax로 prototype에 대응시켜 W/B를 만든다. 미래 달력 시각과 미래 traffic 정답을 구별한다. 선택 밖 model wrapper/normalizer의 전체 data path는 미검증이다.

보관 ETTh1/iTransformer는 L336/H96, normalizationNone, TiD/DiW,prototype30/top-k3,embedding20/hidden32,independentFalse,maskedMAE다. prototype 개수·선택 top-k·Tab의K·RCTL 모델 수는 별개다. 같은 timestamp pair의 시간 W/B가 같아도 채널별 normalization 통계와 최종 예측이 모두 같다는 뜻은 아니다. 선택적 ID 경로도 별도로 기록한다.

논문은 준비 후 공동 학습을 설명한다. 보관 일반 runner는 APT 준비 뒤 동결된 backbone에 예측 loss를 사용하는 한epoch를 거쳐 공동 학습한다. 초기 동결을 최종 learner와 독립이라는 근거로 쓰지 않는다. L2affine의 식과 논문 regularizer를 동일시하지 않고 loss import binding의 미독 범위, unused fused_proto의 보조 코드 관찰을 전체 논문 결함으로 확대하지 않는다.

## Table2: 인쇄값 비교와 실제 실험의 경계

출판본 물리PDF5쪽의 Table2는6dataset×5normalization×4backbone, L336와 H96/192/336/720 평균이다. Traffic은 도로 센서862개/hourly/7:1:2 자료로 telecom cell과 다르다. 단일H96 ETTh1 설정과 Table2 평균을 직접 재현으로 연결하지 않는다.

| 인쇄값 기준 APT 전후 비교 | 개선 | 악화 | 인쇄 동률 | 합계 |
|---|---:|---:|---:|---:|
| MAE |106|12|2|120|
| MSE |95|18|7|120|

480개 metric값/240개 전후 비교를 정수로 대조했다. 악화30개는 metric 비교 수이며 독립적인30조건이라는 뜻이 아니다. Traffic/iTransformer/+RevIN의 MAE .289→.293, MSE .412→.415도 보존한다. 저자 footer의16개 first-count는 반올림값의 동률만으로 유일하게 복원할 수 없다. 많은 개선과 일부 악화를 함께 남기며 raw prediction·유의성·telecom 실험의 재현으로 확대하지 않는다.

## 제한된 직접 추론과 다음 설계

서로 떨어진 입력0–1/2–3에서도 y=10+2x+공통 독립잡음이라는 같은 예측 함수가 가능하다. 이는 입력 집단 수와 필요한 예측모델 수를 구별하는 예시이며 유한 global RCTL의 우위 보장이 아니다. 반대 방향의 원78 예시는 재사용 근거다.

고정된 같은 γ≠0/β를 input/target에 적용하면 y=ax+b는 γy+β=a z+γb+(1−a)β가 되어 a가 유지된다. 계수 identity와12개 Fraction witness·공통함수의 잡음0인6점을 확인했다. 시간마다 달라지는 변환·서로 다른 normalization/de-normalization·비선형 backbone을 포함한 전체 APT에 대한 불가능성 증명은 아니다.

다시 검토할 때는 묶는 객체·학습 정답·명시적K1 비교·최종 learner와의 관계·준비/후보 비용을 먼저 설명한다. 기존의 유용한 공유 결정을 더 잘 정하거나 더 효율적으로 얻는 실제 차이가 필요하다. global 표현 가능성만으로 유한 분할 이득을 불가능하다고 결론 내리지 않는다.

## 보존·실제 판독·남은 범위

Snapshot42는38물리파일/10,608,846bytes다. manifest 목록36파일/10,600,120bytes와 manifest8,178bytes·receipt548bytes의 관계를 검산했다. 40출처/83물리별칭에서 root100의4후보는 같은SHA의 사본이다. 자체 기록15개/224,030bytes를 정확하게 보존하고 기존3사본을 재사용한다. 외부22자료는 sourceSHA·실제읽기범위·정식URL로 연결한다.

최초 새raw4,633행(core900/official3529/candidateprogress204),PDF44쪽/3,307행과44파생 whole-page image를 실제 읽었다. 작성 후 원문1,715행/PDF17쪽1,318행·5이미지를 다시 대조하고 수정한36주장 저장본을 읽었다. 공식11코드/README·2metadata는 전문 읽었으며11파일은 pinned official Git blobSHA/size도 대조했다. 각 imported파일 전체·checkpoint 실행·원실험 재현은 남는다.

APT TXT는 줄끝 정규화 후 literal일치다. Tab TXT는 빈줄2개 차이로 literal불일치이며44page header/모든nonemptyline 일치와 구별한다. TabTXT1–12행 외 전TXT 직접 판독은 미완료다. 파생PNG·동일사본·재사용TabPDF/TXT/원장 재독에 새 독립credit을 주지 않는다. 본문20/전체JSON7/선택2의 새 범주에는 읽은 외부 코드/metadata도 포함하며 보존 사본 개수와 다르다.

과거 snapshot 원장807600…과 현재 후속root17a549…를 구별했다. Word는hash-only이며 본문/레이아웃 검수가 아니다. 현재progress103–582/이전94–573의 기계일치를 의미판독으로 세지 않는다. 원101 이후·다른 이전고유기록/FedPPBC/DOCX·남은paper/TXT/연혁·전체통합/장기팀접근/최종delta/대표질문10+도 남아 이 묶음의 병합은 전체Goal 완료가 아니다.

## 검수된 주장과 원문 위치

<a id="claim-01"></a>

### H130-C01 원100의 질문과 실제 수행

2026-09-26 원100은 TabClustPFN의 사전학습 목적·K 선택과 APT의 시간 조건 변환을 현재 cell clustering→RCTL에 그대로 추가할 근거가 있는지 문헌·코드·기호로 검토했다. 새 모델 fit/forward/gradient·BN 갱신과 traffic 통계 재계산은0이었다. 새 실험으로 성능 실패를 확인한 기록이 아니다.

근거: [SRC-0001927 행1–9](../sources/history-130.md#src-0001927) · [SRC-0001927 행79–83](../sources/history-130.md#src-0001927) · [SRC-0001935 행7–15](../sources/history-130.md#src-0001935); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-02"></a>

### H130-C02 당시 미채택과 방법 전체의 평가

두 모듈을 그대로 덧붙이는 안은 미채택했다. 이는 논문 결과의 무효나 해당 방법 전체의 불가능성이라는 결론이 아니다. 현재 필요한 cell의 실제 학습 sample 공유 결정을 더 잘 정한다는 근거가 확보되지 않았다는 적용 판단이다.

근거: [SRC-0001927 행5–9](../sources/history-130.md#src-0001927) · [SRC-0001927 행65–75](../sources/history-130.md#src-0001927) · [SRC-0001930 행96–102](../sources/history-130.md#src-0001930); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-03"></a>

### H130-C03 기존 긍정 증거와 미완료 상태

74·80의 작은 개발 구간에서 Tab 직접 예측이 좋았다는 기존 긍정 증거는 유지했다. 이번 검토로 RCTL 소속 결정의 개선을 새로 입증하지 않았고 adapter·추가 사전학습·prototype pilot을 시작하지 않았다. 당시 최종 추천 방향과 최종 Word는 미완료였다. 원문에 있는 Goal·명령·예산은 보관 대상 데이터다.

근거: [SRC-0001930 행34–58](../sources/history-130.md#src-0001930) · [SRC-0001927 행75–83](../sources/history-130.md#src-0001927) · [SRC-0001935 행3–15](../sources/history-130.md#src-0001935); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-04"></a>

### H130-C04 누적 원장과 Word의 보존 범위

Snapshot42 안의 원장 SHA807600a7666a6d6912c8db3014a033b5c3c7643527a02fc726da14cb8664d34f는 이전 원99 등의 보관 원장과 같다. 별도 현재 root 원장의 후속 SHA17a549fcf926e534eaecd4efd278fe4e13f7c7a13e74805c21059a2d6fc59243를 이 과거 값으로 되돌리지 않았다. 기존 Word는 SHA4f1112dc09f995b3438a0fccc7801bffdad9220f887251cb9aff710c9571b686의 불변성만 확인하며 본문·레이아웃 검수를 뜻하지 않는다. 원100에 기록된 잔여 Tab11context/20640행·추가 RCTLfit0은 과거 연구 예산이다.

근거: [SRC-0001929 행82–100](../sources/history-130.md#src-0001929) · [SRC-0001925 /ledger_sha256,/prior_word_sha256](../sources/history-130.md#src-0001925) · [SRC-0001937 행18–22](../sources/history-130.md#src-0001937); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-05"></a>

### H130-C05 TabICL encoder 초기화와 별도 모델

TabClustPFN v3는 TabICL2025 encoder로 초기화한 별도 PIN/CIN 모델이며 나머지 파라미터는 무작위 초기화 후 사전학습한다. 회귀 TabICLv2의 고정 가중치·목적과 같다고 취급하지 않는다. TabICL 계열이라는 명칭만으로 현재 회귀 기능의 성공을 clustering의 성공으로 옮길 수 없다.

근거: [SRC-0001927 행13–20](../sources/history-130.md#src-0001927) · [SRC-0001940 PDF3,5,15쪽](../sources/history-130.md#src-0001940); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-06"></a>

### H130-C06 표의 행과 cell 공유 목적

PIN은 표의 각 행의 잠재 소속을 복원한다. 행을 lag sample로 구성하면 sample clustering이며 cell partition이 자동으로 나오지 않는다. cell별 표현을 행으로 만드는 선택은 가능하지만 그 표현의 집단 복원이 RCTL 공동 학습에 유용한지는 별도로 확인해야 한다. framework가 원리상 cell을 묶을 수 없다고 주장하지 않는다.

근거: [SRC-0001927 행17–20](../sources/history-130.md#src-0001927) · [SRC-0001927 행49–53](../sources/history-130.md#src-0001927) · [SRC-0001940 PDF3,15,17쪽](../sources/history-130.md#src-0001940); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-07"></a>

### H130-C07 합성 prior와 사전학습 정답

v3의 합성 prior는 overlap을 조절한 GMM과 ZEUS 계열의 수치·범주형 변환을 섞고 latent component를 정답으로 쓴다. 논문 사전학습은 N500–1000/D2–64/K2–10, batch512, 매번 새 합성 표다. PIN은 SoftARI, CIN은 참 K의 cross-entropy를 쓰며 CIN gradient는 detached PIN으로 되돌아가지 않는다. traffic 예측 오차나 필요한 RCTL 수가 이 정답은 아니다.

근거: [SRC-0001927 행18–20](../sources/history-130.md#src-0001927) · [SRC-0001940 PDF3,4,5,12,13,14쪽](../sources/history-130.md#src-0001940); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-08"></a>

### H130-C08 CIN의 입력과 선택의 의미

부록B.2.2의 CIN은 후보K마다 G=(1/N)PᵀP의 대각/상삼각 비대각 값을 각각 정렬하고 합쳐 Kmax−1개 logits를 낸다. 부록은 hidden256의3-layer MLP라고 서술하며 본문§3.2는 two-layer/lower-triangle 표현을 쓴다. 그 표기 범위를 구별하고, 선택 밖 model/decision.py의 활성 구현을 확인했다고 하지 않는다. 이 posterior는 표의 latent cardinality 정답에 관한 것으로 RCTL의 유한 공동 학습 효용에 대한 posterior가 아니다.

근거: [SRC-0001940 PDF4,17쪽](../sources/history-130.md#src-0001940) · [SRC-0001927 행18–21](../sources/history-130.md#src-0001927); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-09"></a>

### H130-C09 자동 K 선택에서 K1의 부재

고정 commit의 자동 경로는 range(2,max_classes+1)의 결과에서 K를 선택하며 predict_labels는 argmax+2를 반환한다. 기본 max_classes10에서는 CIN의 선택지가2–10이다. globalK1을 명시적으로 선택하는 항목은 이 자동 경로에 없다.

근거: [SRC-0001956 행208–292](../sources/history-130.md#src-0001956) · [SRC-0001955 행417–440](../sources/history-130.md#src-0001955) · [SRC-0001927 행21–27](../sources/history-130.md#src-0001927); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-10"></a>

### H130-C10 요청 K·점유 label 수·manualK1의 경계

fixed-K 경로는 주어진 K를 모델에 넘기고, predict_labels는 argmax label의 실제 점유 개수를 반환한다. 자동 CIN의 K와 실제 점유 label 수는 다를 수 있다. 한 label로 collapse할 수 있다는 가능성은 K1이 충분하다는 검증이 아니다. CLI에는 보이는 K1 차단 검사가 없지만 선택 밖 ClusterLearningIMAB 내부를 읽지 않았으므로 manualK1의 성공 또는 불가능을 확정하지 않는다.

근거: [SRC-0001953 행80–172](../sources/history-130.md#src-0001953) · [SRC-0001953 행217–222](../sources/history-130.md#src-0001953) · [SRC-0001955 행401–440](../sources/history-130.md#src-0001955) · [SRC-0001956 행436–441](../sources/history-130.md#src-0001956); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-11"></a>

### H130-C11 표현 재사용과 아홉 decoder 호출

inference는 col_embedder/row_interactor로 만든 row_representations를 한 번 공유한 뒤 K별 cluster_learner를 부른다. 기본10에서는9개의 K별 호출과 k_decision이 있고 inference는 그 결과를 재사용한다. training의 true-K 추가 호출과 구별한다. 단일 forward API·dataset별 최적화 없음이 내부 후보 계산 없음이라는 뜻은 아니다. 이번 정리는 wall-clock·메모리 속도 측정이 아니다.

근거: [SRC-0001956 행251–292](../sources/history-130.md#src-0001956) · [SRC-0001956 행334–368](../sources/history-130.md#src-0001956) · [SRC-0001956 행399–440](../sources/history-130.md#src-0001956) · [SRC-0001927 행23–25](../sources/history-130.md#src-0001927); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-12"></a>

### H130-C12 v3의 N10000 평가와 고차원 한계

v3는 학습 범위 밖 N10000까지의 평가와 더 큰D에서 PCA를 쓴 비교를 제시한다. Fig5는 D50을 고정한 큰N 평가이며 Fig6은 큰D 평가다. 논문은 고차원에서 cardinality 오류와 PCA 이후 구조 변화에 따른 한계를 설명한다. N1000/D64 학습 범위를 API의 절대 실행 상한으로 쓰지 않으며 통신 cell 예측의 성능 확인으로 확대하지 않는다.

근거: [SRC-0001927 행29–29](../sources/history-130.md#src-0001927) · [SRC-0001940 PDF6,7,9쪽](../sources/history-130.md#src-0001940); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-13"></a>

### H130-C13 44개 benchmark와 평가 지표의 조건

v3 real benchmark는 OpenML22/UCI22의44개다. D≤64/K≤10로 필터링하고 source별 원래N 필터 또는1000개 subsampling을 하며 max-methodARI<.1인 자료를 제외한다. 표의 원래 행 수와 실제 평가 row 수가 다르다. medianARI/NMI rank, rawmedian/IQR, cardinalityk-MAE와 현재 traffic forecastMAE를 구별한다.

근거: [SRC-0001940 PDF5,7,18,19,20,22,23,31쪽](../sources/history-130.md#src-0001940); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-14"></a>

### H130-C14 cardinality calibration의 한정된 의미

CIN calibration은3200개 GMM holdout(N500–1000/D2–64/Kmax10)에서 posterior 질량으로 만든 K 집합의 참K coverage다. 인쇄된 nominal80/85/90/95/99%와 coverage .875/.907/.937/.968/.993을 보존한다. assignment label의 calibration, RCTL의 유한학습 uncertainty, 실제 cell의 확신으로 대입하지 않는다.

근거: [SRC-0001940 PDF6,29,30쪽](../sources/history-130.md#src-0001940); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-15"></a>

### H130-C15 성능의 긍정과 예외를 함께 보존

저자는 빠른 inference와 좋은 전체 rank를 보고한다. 그러나 모든 dataset·지표에서의 우위를 뜻하지 않는다. 예를 들어 high-difficulty syntheticARI와 일부NMI의 최댓값은 다른 방법에 있고, real paired t/Wilcoxon의 Agg+/KMeans+ 비교는 유의하지 않다. median rank와 평균 rank의 CD 분석도 다른 요약이다. 원실험 출력·checkpoint를 재현한 결과는 아니다.

근거: [SRC-0001940 PDF8,9,22,23,28,29,31쪽](../sources/history-130.md#src-0001940); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-16"></a>

### H130-C16 parser 기본값과 실제 사전학습의 구별

보관 train_config 기본값은 max_steps2000/optimizerSGD/min_features5이고 논문 최종 protocol은10000steps/AdamW/D2–64다. parser 기본값은 override 후 실제 실행 설정과 다를 수 있으므로 이 차이만으로 checkpoint가 잘못 학습됐다고 판정하지 않는다. 선택 밖 base trainer·prior generator·저자 실행 명령의 전체 감사는 미완료다.

근거: [SRC-0001954 행26–69](../sources/history-130.md#src-0001954) · [SRC-0001954 행179–212](../sources/history-130.md#src-0001954) · [SRC-0001940 PDF5,12쪽](../sources/history-130.md#src-0001940); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-17"></a>

### H130-C17 APT 출판본과 현재 서지 확인

원100의 APT는 AAAI2026 출판본9쪽(pp15180–15188), DOI10.1609/aaai.v40i18.38542다. 현재 공식 page의 공개일은2026-03-14, 권호40(18)이다. 출판PDF와 arXiv2511.12945v1의 부록 위치를 구별하고 최신HTML/PDF가 같은 편집·바이트라고 가정하지 않는다. 원 collector에는 download/38542/42504의 실제 transport가 기록되어 있다.

근거: [SRC-0001927 행33–33](../sources/history-130.md#src-0001927) · [SRC-0001942 /files/2](../sources/history-130.md#src-0001942) · [SRC-0001938 PDF1,9쪽](../sources/history-130.md#src-0001938); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-18"></a>

### H130-C18 시각 시작·끝과 미래 정보의 경계

APT는 history 첫 시각과 horizon 마지막 시각의 달력 embedding을 prototype에 대응시켜 scale/offset을 만든다. 미래 달력 시각은 미리 아는 정보이며 미래 traffic 정답과 다르다. 보관된 APT.forward의 timestamp 선택은 확인했지만 선택 밖 model wrapper와 normalizer 전체 경로는 미검증이므로 모든 future_data 사용이 누수 없다고 선언하지 않는다.

근거: [SRC-0001927 행35–35](../sources/history-130.md#src-0001927) · [SRC-0001949 행187–263](../sources/history-130.md#src-0001949) · [SRC-0001950 행612–669](../sources/history-130.md#src-0001950) · [SRC-0001938 PDF3,4쪽](../sources/history-130.md#src-0001938); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-19"></a>

### H130-C19 prototype 수와 top-k의 의미

보관 ETTh1/iTransformer는 TiD/DiW,prototype30/top-k3,embedding20/hidden32,independentFalse다. prototype 수30, 선택 prototype 수3, Tab의 cardinalityK, 현재 RCTL 모델 수는 별개다. 다른 dataset에도 모두 같은 설정이라고 쓰지 않는다.

근거: [SRC-0001927 행39–41](../sources/history-130.md#src-0001927) · [SRC-0001947 행15–85](../sources/history-130.md#src-0001947) · [SRC-0001949 행80–183](../sources/history-130.md#src-0001949) · [SRC-0001938 PDF3,5쪽](../sources/history-130.md#src-0001938); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-20"></a>

### H130-C20 준비 단계와 최종 learner의 공동 학습

APT의 초기 준비는 backbone/normalization을 동결하고 이후 예측 loss로 공동 학습한다. 일반 runner는 tan_epoch까지 APT 준비, 다음 한epoch도 backbone을 동결한 예측 loss, 그다음 공동 학습으로 나뉜다. 초기 동결만으로 최종 learner와 독립인 모듈이라고 하지 않는다. 소속을 먼저 고정한 뒤 사용과 최종 학습 결과로 소속을 정하는 변형도 구별한다.

근거: [SRC-0001927 행37–37](../sources/history-130.md#src-0001927) · [SRC-0001927 행72–72](../sources/history-130.md#src-0001927) · [SRC-0001950 행236–249](../sources/history-130.md#src-0001950) · [SRC-0001950 행325–403](../sources/history-130.md#src-0001950) · [SRC-0001938 PDF4쪽](../sources/history-130.md#src-0001938); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-21"></a>

### H130-C21 cosine·Top5 주석과 활성 계산

APT.py의 prototype matching은 활성 einsum 내적과 torch.topk(k=self.topk),softmax다. 주석의 cosine/Top5를 실제 정규화 cosine 또는 항상k5라는 뜻으로 옮기지 않는다. 현재 설정 top-k3과 구별하여 기록한다. 원 코드를 실행한 관찰은 아니다.

근거: [SRC-0001949 행275–353](../sources/history-130.md#src-0001949) · [SRC-0001947 행53–85](../sources/history-130.md#src-0001947) · [SRC-0001927 행39–39](../sources/history-130.md#src-0001927); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-22"></a>

### H130-C22 같은 시간 변환과 cell별 전체 예측

independentFalse의 시간 모듈은 같은 timestamp pair에 같은 W/B를 채널 방향으로 broadcast한다. 입력별 normalization 통계·backbone 출력이 달라질 수 있으므로 모든 cell의 전체 예측이 같다는 뜻은 아니다. independentTrue에는 ID embedding 경로가 있지만, 그것의 학습과 유용한 공유 소속 결정은 별도다.

근거: [SRC-0001949 행159–183](../sources/history-130.md#src-0001949) · [SRC-0001949 행355–391](../sources/history-130.md#src-0001949) · [SRC-0001927 행41–41](../sources/history-130.md#src-0001927) · [SRC-0001938 PDF4쪽](../sources/history-130.md#src-0001938); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-23"></a>

### H130-C23 paper regularizer와 선택 코드의 경계

runner에는 l2 호출이 있으며 수집된 L2affine.py의 동명 함수는 unbiased sample variance+1e-4·평균 제곱을 사용한다. 논문 Eq12와 같은 식이라고 단정하지 않는다. loss/__init__.py를 읽지 않았으므로 import binding의 전체 확정은 하지 않는다. APT.py independent 분기는 fused_proto를 계산하지만 match_prototypes는 weighted_proto를 반환한다. 이는 보조 코드의 static 관찰이며 논문이 그gate를 사용한다는 주장이나 전체 논문 결함·실행 결과가 아니다. 관련 wrapper/normalizer와 다른 imported loss의 body도 선택 밖이다.

근거: [SRC-0001948 행1–32](../sources/history-130.md#src-0001948) · [SRC-0001950 행1–18](../sources/history-130.md#src-0001950) · [SRC-0001950 행343–345](../sources/history-130.md#src-0001950) · [SRC-0001949 행310–353](../sources/history-130.md#src-0001949) · [SRC-0001938 PDF4쪽](../sources/history-130.md#src-0001938); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-24"></a>

### H130-C24 Traffic·ETTh1·여러 horizon 평균의 구별

APT Table2는6dataset×5normalization×4backbone의 MAE/MSE이고 L336, H96/192/336/720 평균이다. 현재 v1 AppendixC의 Traffic은 California 도로 센서862개/hourly/7:1:2로 통신 cell 자료와 다르다. 보관 ETTh1/iTransformer config는H96/normalizationNone/masked_mae이며 이 Traffic+RevIN 행이나 네horizon 평균의 직접 재현이 아니다.

근거: [SRC-0001938 PDF5쪽](../sources/history-130.md#src-0001938) · [SRC-0001947 행15–46](../sources/history-130.md#src-0001947) · [SRC-0001947 행86–187](../sources/history-130.md#src-0001947) · [SRC-0001927 행43–43](../sources/history-130.md#src-0001927); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-25"></a>

### H130-C25 Table2 인쇄값480개의 비교

원 출판 Table2의30행/480metric값에서 APT 전후240metric 비교(각MAE/MSE120)를 정수로 대조했다. MAE는106개 개선/12개 악화/인쇄동률2개, MSE는95/18/7개다. 세자리 인쇄값 비교이며 원 prediction·seed별 통계·저자 raw score를 재계산한 것이 아니다.

근거: [SRC-0001938 PDF5쪽](../sources/history-130.md#src-0001938); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-26"></a>

### H130-C26 Traffic/iTransformer/RevIN의 악화 예

인쇄된 Traffic/iTransformer/+RevIN은 MAE .289→.293, MSE .412→.415다. 해당 반올림값 기준 증가율은 정확히400/289%=약1.3841%,75/103%=약.7282%다. 전체 방법의 성능·실제 telecom 변화·통계적 유의성을 이 한 조건으로 판정하지 않는다.

근거: [SRC-0001927 행43–43](../sources/history-130.md#src-0001927) · [SRC-0001938 PDF5쪽](../sources/history-130.md#src-0001938); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-27"></a>

### H130-C27 저자의 first-count와 반올림 동률

Table2 하단의 저자 first-count16개 값도 보존한다. 반올림된 표의 동률만으로 저자가 사용한 원점수 순위·tie 처리의 배분을 유일하게 복원할 수 없다. 현재 정수 비교의 동률 집계와 footer를 같은 계산으로 대체하거나 그 불일치만으로 논문 오류라고 하지 않는다.

근거: [SRC-0001938 PDF5쪽](../sources/history-130.md#src-0001938); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-28"></a>

### H130-C28 개선·악화 집계의 단위와 적용 범위

위 악화30개는 MAE12+MSE18의 metric 비교 수다. 서로 다른30개 실험 조건이라는 뜻이 아니며 같은 조건에서 두metric이 악화할 수 있다. 많은 개선도 함께 보존한다. 모든 조합의 개선 또는 방법 전체의 무효·현재 RCTL clustering 성공 중 어느 것으로도 확대하지 않는다.

근거: [SRC-0001938 PDF5쪽](../sources/history-130.md#src-0001938) · [SRC-0001927 행43–43](../sources/history-130.md#src-0001927); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-29"></a>

### H130-C29 분리된 입력과 하나의 공통 함수

원기호 예시는 A입력0–1/B입력2–3이면서 두집단의 관계가 y=10+2x+동일한 독립잡음인 구성이다. 입력 두덩어리 복원과 필요한 예측 함수 수는 다를 수 있다. 현재 exact 산술은 잡음0인6점(10,11,12/14,15,16)만 확인했다. traffic 실험이나 유한global RCTL이 반드시 유리하다는 증명이 아니다.

근거: [SRC-0001927 행47–53](../sources/history-130.md#src-0001927); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-30"></a>

### H130-C30 반대 방향 반례의 재사용

입력분포가 같으나 예측관계가 다른 원78의 반대 예시는 기존 근거를 재사용했다고 원100이 명시한다. 이번의 새 발견·새 모델 호출로 세지 않는다. 입력 similarity·latentK만으로 최종 공유 효용을 판단할 수 없다는 구별에 함께 연결한다.

근거: [SRC-0001927 행51–53](../sources/history-130.md#src-0001927) · [SRC-0001930 행31–31](../sources/history-130.md#src-0001930); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-31"></a>

### H130-C31 제한된 같은 affine의 기울기 보존

동일하고 고정된 γ≠0/β를 input과 target에 적용하고 y=ax+b라면 z=γx+β에서 γy+β=a z+γb+(1−a)β다. 계수 identity와12개 정확한Fraction witness를 대조했다. 이 조건에서a가 유지된다는 사실은 비선형backbone·서로 다른normalization/de-normalization 통계·시간마다 바뀌는 변환을 포함한 전체APT의 불가능성 증명이 아니다.

근거: [SRC-0001927 행55–63](../sources/history-130.md#src-0001927); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-32"></a>

### H130-C32 다시 검토할 때 바뀌어야 할 근거

당시 기준은 묶는 단위·사전학습 정답·명시적K1 비교·최종 learner와의 학습 관계·실제 후보 비용을 먼저 밝히는 것이다. 더 좋은 실제 cell 공유 결정 또는 같은 유용한 결정의 추정 효율/비용 개선과 강한 global 대안을 설명해야 한다. global로 표현 가능하다는 사실만으로 분할의 유한학습 효용을 불가능하다고 판정하지 않는다. 미검증 구조를 새 추천으로 승격하지도 않는다.

근거: [SRC-0001926 행23–35](../sources/history-130.md#src-0001926) · [SRC-0001930 행42–58](../sources/history-130.md#src-0001930) · [SRC-0001930 행96–102](../sources/history-130.md#src-0001930) · [SRC-0001927 행65–75](../sources/history-130.md#src-0001927); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-33"></a>

### H130-C33 물리 snapshot과 출처·사본의 수

Snapshot42 물리 파일은38개/10608846bytes다. manifest의 목록36개/10600120bytes에 manifest8178bytes와 receipt548bytes를 더하면 같다. root100후보4개는 같은SHA의 사본이며 독립 실험이 아니다. 이 묶음의 선택은 새35그룹·재사용3·이전판본2의40출처/83물리별칭이다. 전체폴더 목록을 본문 검토 완료로 세지 않는다.

근거: [SRC-0001924 /files](../sources/history-130.md#src-0001924) · [SRC-0001925 /files,/verified](../sources/history-130.md#src-0001925); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-34"></a>

### H130-C34 공식 소스11개와 pinned 바이트

APT commit98a4c9c017666207b02029f842eff92818f0eab8(2026-01-26),Tab commit5673beaab72d69bb9db30da2740aef90975a3e0c(2026-05-01)의11선정코드/README와2repo metadata를 전문3529행 읽었다.11파일의 Git blob SHA1·size를 현재 공식 pinned tree와 대조했다. 최신main·선택 밖 모든 import·checkpoint 접근/학습/추론을 검증한 것은 아니다. 외부 코드·PDF/TXT/PNG는 원문 통째 재배포 없이 formal metadata/link로 연결한다.

근거: [SRC-0001944 행1–7](../sources/history-130.md#src-0001944) · [SRC-0001951 행1–7](../sources/history-130.md#src-0001951) · [SRC-0001942 /files](../sources/history-130.md#src-0001942); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-35"></a>

### H130-C35 PDF·TXT·그림과 실제 읽기 범위

현재 APT9/재사용Tab35의44PDF쪽·3307text행과44파생 whole-page image를 실제 읽었다. 표/그림을 본 것과 모든curve원값 독립검산·원실험재현은 다르다. APT TXT는 줄끝 정규화 후 literal일치,Tab TXT는 빈줄2개 차이로 literal불일치지만44page header/모든nonemptyline은 일치한다. 별도TXT는Tab1–12행 외 직접읽지 않았으며 기계 대응만으로 전TXT 의미읽기나 독립 새이미지 credit을 주지 않는다.

근거: [SRC-0001942 /files](../sources/history-130.md#src-0001942) · [SRC-0001943 /0/page_1based,/4/page_1based](../sources/history-130.md#src-0001943); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.

<a id="claim-36"></a>

### H130-C36 누적 문서 판본과 완료 집계의 경계

candidate1930전문102행은 원99판본94행 뒤8행 추가이고 progress1935는582행 중1–102만 실제읽었다. tail103–582와 이전94–573의 기계일치는 의미판독이 아니다. 최초 새raw4633행(core900/official3529/candidateprogress204),PDF44쪽/3307행·44파생image를 기록한다. 새 집계 예정은 기록1/주장36/본문20/전체JSON7/선택2/독립이미지0이며 이 기록의 문서 검수 후 한 번만 집계한다. 원101이후·이전고유기록/FedPPBC/DOCX·남은paper/TXT/연혁·통합/장기접근/최종delta/대표질문10+는 남아 전체Goal 미완료다.

근거: [SRC-0001930 행88–102](../sources/history-130.md#src-0001930) · [SRC-0001935 행7–24](../sources/history-130.md#src-0001935); 상세범위·추가검산은 [주장 목록](../verification/history-130-claims.json) 참조.
