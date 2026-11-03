# 원99 — 학습 단위와 clustering의 비용 효과

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

선행연구에서 clustering이 좋아졌다는 사실을 현재 cell별 RCTL의 직접 성능 근거로 쓰려면 **한 sample·출력·소속 결정·비교 조건**이 맞아야 한다. Cash는 여러 OD flow의 입력·출력 벡터를 나누고, Ma는 여러 센서를 포함한 하루 기록의 소속을 정한다. 현재 RCTL은 cell별8×9 입력에서 한 값을 예측하고 같은 가중치로 학습할 row를 묶는다.

2026-09-26 원99는 이 차이와 고정 조건의 용량/작업량을 문헌·보존 코드·정수 산술로 확인했다. 새 모델 실행·traffic 통계 재계산은0이고 최종 추천안/Word는 미완료였다. 기록의 판단을 미래 팀 연구 전체의 금지로 해석하지 않는다.

[34출처/88사본](../sources/history-129.md) · [32주장](../verification/history-129-claims.json) · [작성 후 대조](../verification/history-129-second-pass.json) · [읽은 범위](../evidence/0129-learning-units-and-clustering-cost/read-scopes.json) · [수치·보존 검산](../evidence/0129-learning-units-and-clustering-cost/numeric-check.json) · [문헌 비교](../references/learning-unit-and-clustering-cost.md)

## 질문·방법·실제 수행 범위

원05의 random/global 대조군 원칙과 원98의 단일 target/전체 평균 목적 구분을 이어, 다른 단위의 예측 문제 분할을 현재 cell pooling과 연결할 수 있는지 물었다. 기존 결과를 유지하면서 새로 확인한 것은 학습 단위·입출력·소속/K 선정·모델 용량·고정 epoch의 row/update·Tab 준비/cache다. 원97 저장 예측 재사용이나 원95 CPU serving의 후속 성능 실험이 아니다.

| 구조 | 묶는 대상 | 한 모델의 예측 | 비교 시 함께 바뀌는 것 |
|---|---|---|---|
| 현재 scalar RCTL | cell sample | 한 cell의 다음 값1개 | 함께 학습할 row 집합·모델 수 |
| Cash traffic matrix | OD flow | cluster의 여러 다음 flow 값 | 입출력 차원·공동 입력·recurrent core 수 |
| Ma validation-driven | 하루 MTS | 그날 여러 센서의 다음 벡터 | 하루 소속·반복 prototype 학습·VAL routing |

원99의 대규모 산술에는 새 dataset/time split/정규화/seed/accuracy가 **해당 없음**이다. T672/batch256은 기존 pilot 조건을 확대했다. 논문 author code/head·Cash Kneedle의 split/runtime 전체 경계는 **미확인**이며 정확한 성공 다운로드 URL은 **미기록**이다. 아래 계산으로 실제 RCTL 성능을 확정하지 않는다.

## 고정 조건의 계산과 실측의 경계

한 층 단방향 GRU·hidden H·PyTorch bias2개·H→d_k linear head·Σd_k=D를 가정하면 `P_K=K(3H²+6H)+(4H+1)D`다. H200/D144의 K1/21은236544/2660544개, D529의 K1/40은544929/5271729개다. 작은 입출력 여러 개가 전체 용량까지 작다는 뜻은 아니다. 저자 checkpoint의 정확한 측정도, 용량만이 개선 원인이라는 증명도 아니다.

| cell 수 N | 완전 epoch 총 row | K1 update | K4 | K16 | K32 |
|---:|---:|---:|---:|---:|---:|
| 128 | 86016 | 336 | 336 | 336 | 352 |
| 1024 | 688128 | 2688 | 2688 | 2688 | 2688 |
| 10000 | 6720000 | 26250 | 26252 | 26256 | 26256 |

균형 분할과 고정672행/cell/batch256의 산술이다. 서로 다른 epoch/early-stop·hardware·호출 overhead에 따라 실제 시간은 달라진다. 시각마다 모든 cell을 예측하면 row/출력은 N개다. 원95의16cell CPU latency를10000cell 실측으로 바꾸지 않는다.

현재 추가 정적 검산은 RCTL 등록174433/학습 가능173537개를 구분했다.896개 LSTM 추가 recurrent bias는 zero/frozen이다. float32 parameter697732bytes+BN buffer/counter3680bytes=state701412bytes는 기존9checkpoint metadata와 일치했다. 모델 생성이나 가중치 역직렬화 없이 source shape를 셌으며 optimizer·파일크기·peak RAM은 포함하지 않는다.

기존 B2 M504/Q168/R1·129분위수 float32 가정의 N10000 cache는866880000bytes(약0.87GB)다. context 준비10000회/5040000행, query1680000행이며 첫 추론·activation·ensemble·I/O·검색 비용을 지우지 않는다. 모든21저장 계산행을 자체 산술과 대조했지만 대규모 실행·총 비용 실측·B2 채택은 아니다.

## 문헌에서 유지할 사실과 한계

[문헌 비교](../references/learning-unit-and-clustering-cost.md)는 Cash2025의 H30/K9·47/정규화 RMSE와2026의 H200/다른 운영 K/Mbps를 분리한다.92%·75%의 비교군은 ARCNN/TE-Prophet이고 MLU는1에 가까운 비율이 좋다. local 평균 오차가 더 낮다는 결과도 남겼다.

Cash2026의 matched-K NMI/ARI와 운영점 RMSE/runtime는 같은 비교가 아니다. naive grouping의 개선을 모든 grouping이 무용하다는 주장으로 확대하지 않으며, K 선택 split 미확인을 곧바로 test leakage로 단정하지 않는다. 당시 원문/검색에서 author code를 검증하지 못했다는 것은 코드가 없다는 증명이 아니다.

Ma의 BAY180×288×325/SF440×144×963은 **하루 개체×시점×센서**다. 하루 내부 TRAIN/VAL/TEST, 반복 GLOBAL/prototype fitting, VAL 소속/K/fallback 고정, TRAIN+VAL refit, single TEST 절차는 방법론 참고다. BAY K7의 TEST MSE 개선18.12/19.24/23.75%와 Ben84/86/92%, Fb0은 저자 인쇄값이며 모든 하루의 무손해나 현재 RCTL 실익의 보장이 아니다.

## 당시 판단·재사용·새 실험 전 확인

현재 cell pooling에서 Tab이 바꾸는 유용한 결정 또는 그 판단 비용을 먼저 특정한다는 원99 판단을 보존한다. 같은 K·scalar output·sample/학습 조건의 소속 비교와 별도의 K별 정확도/비용 곡선을 나눈다. 기존 global/naive·K4 두 seed 결과는 유지한다. 새로운 모델/소속 성능은 이 기록에서 만들지 않았다.

기존 조건을 바꿔 재검토한다면 sample·관측 개체·출력/손실·시간 분할·정규화·K·seed·전체 용량을 적는다. 감소할 비용이 모델 저장량인지 update인지 예측 row인지 Tab 준비/검색인지 명시한다. 관련 이전 결과와 차이를 실험 이슈 양식에 연결한다. 모든 원코드는 자료로 보존하며 이번 환경에서 재현 성공을 주장하지 않는다.

## 보존·판독·남은 범위

작은 내부 원문14개를 byte 그대로 보존하고 이전 사본8개를 재사용했다. 외부 PDF/TXT/PNG는 정식 링크·SHA·검토 범위만 제공한다. snapshot41의 listed25/4663812bytes와 manifest5412+verification461을 포함한 물리27/4669685bytes를 분리했다. root99 receipt는 같은SHA 사본이다.

역사 snapshot 원장807600…와 현재 원본root 원장17a549…는 다른 판본이다. 현재root와 보호 원본6개는 처음 baseline과 일치한다. 잔여Tab11context/20640행·추가RCTLfit0은 당시 상태이며 원장/기존 상태는 수정하지 않았다. Word4f1112…는 hash-only로 본문/layout 검토가 남는다.

최초 원문1090행·이전 근거687재독행, PDF45텍스트쪽3120행/36파생 이미지다. Cash6/12쪽은 전체 text/image, Ma27/43쪽 text와18image를 확인했다. 작성 후 원문655행·이전근거238행·PDF21쪽1610행·2이미지를 별도 대조하고 정정 저장본을 읽었다. 재독/파생 이미지/동일SHA 사본은 새 독립 완료로 늘리지 않는다.

현재progress94–573/이전85–563, Ma16텍스트쪽과 다른 시각내용·각 전TXT 직접 판독·공식 구현/전체 재현은 미완료다. candidate의8행 추가와progress 최신절 치환의 기계 비교를 tail 의미 판독으로 세지 않는다. 원100 이후·이전고유판본/FedPPBC/DOCX·전체통합/장기접근/최종delta/대표질문10+ 검수도 남아 이 묶음의 병합은 전체 Goal 완료가 아니다.

## 검수된 주장과 원문 위치

<a id="claim-01"></a>

### H129-C01 원99의 실제 수행 범위

원99(2026-09-26)은 문헌·보존 코드·정수 산술로 학습 단위와 비용 효과를 검토했다. 새 모델 fit·predict·gradient·BN 갱신과 실제 traffic 통계 재계산은0이며 최종 추천안·Word는 미완료였다. 이번 아카이브도 원 연구 코드를 실행/import하거나 모델을 만들지 않았다.

근거: [SRC-0001899 행3–5](../sources/history-129.md#src-0001899) · [SRC-0001899 행43–47](../sources/history-129.md#src-0001899) · [SRC-0001900 행3–3](../sources/history-129.md#src-0001900) · [SRC-0001901 행25–31](../sources/history-129.md#src-0001901) · [SRC-0001906 행7–17](../sources/history-129.md#src-0001906); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-02"></a>

### H129-C02 같은 clustering 이름 아래 다른 단위

현재 RCTL은 cell별 scalar sample의 row pooling, Cash는 OD flow 벡터의 입력·출력 분할, Ma는 여러 센서를 포함한 하루 MTS들의 소속 결정이다. 다른 단위에서의 성공은 방법론 참고이며 현재 cell pooling의 직접 성능 증거가 아니다.

근거: [SRC-0001899 행7–17](../sources/history-129.md#src-0001899) · [SRC-0001900 행7–15](../sources/history-129.md#src-0001900) · [SRC-0001910 PDF2,3쪽](../sources/history-129.md#src-0001910) · [SRC-0001912 PDF3,4쪽](../sources/history-129.md#src-0001912) · [SRC-0001914 PDF17,19,20쪽](../sources/history-129.md#src-0001914); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-03"></a>

### H129-C03 RCTL은 8×9 입력에서 한 값을 출력한다

보존 RCTL/pilot은 한 cell sample을(-1,8,9)로 바꾸고 마지막128차원(8×16) 표현에서 scalar를 출력한다. 같은 group의 cell 수가 늘면 입력 열 대신 학습 row가 늘어난다. global을 큰 다중 출력 벡터의 병목으로 설명하지 않는다.

근거: [SRC-0001900 행44–44](../sources/history-129.md#src-0001900) · [SRC-0023048 행1–60](../sources/history-129.md#src-0023048) · [SRC-0023202 행59–61](../sources/history-129.md#src-0023202) · [SRC-0023202 행78–95](../sources/history-129.md#src-0023202); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-04"></a>

### H129-C04 독립 소속과 최종 learner 손실의 역할

당시 연구는 RCTL과 분리한 cell 소속 결정의 실익을 물었다. Ma의 반복 prototype 학습·validation 재배정은 그 독립 절차를 직접 제공하지 않는다. 소속 판단의 역할을 구분하는 역사적 연구 조건이며 미래 팀 실험 전체의 금지 규칙은 아니다.

근거: [SRC-0001901 행7–23](../sources/history-129.md#src-0001901) · [SRC-0001900 행23–23](../sources/history-129.md#src-0001900) · [SRC-0001900 행68–75](../sources/history-129.md#src-0001900) · [SRC-0001914 PDF5,6,13,14,37쪽](../sources/history-129.md#src-0001914); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-05"></a>

### H129-C05 Cash의 traffic matrix는 joint vector다

Cash 두 판본은 OD flow별 시계열을 묶고 cluster 내 여러 flow의 과거10개 traffic matrix에서 다음 벡터를 함께 예측해 전체 TM을 재구성한다. clustering은 모델 수·각 입출력 차원·공동 입력을 함께 바꾼다. scalar cell sample의 공유와 같은 조작이 아니다.

근거: [SRC-0001910 PDF2,3,4쪽](../sources/history-129.md#src-0001910) · [SRC-0001912 PDF3,4,6쪽](../sources/history-129.md#src-0001912) · [SRC-0001900 행11–15](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-06"></a>

### H129-C06 2025 폭30과 2026 폭200을 구별한다

Cash2025 §V-D의 한 층 GRU hidden width는30, Cash2026 §V-D는200이다. batch32/최대100epoch/Adam.001/patience5/min_delta1e-5가 서술되어 있다. 아래 H200 산술을2025의 checkpoint 규모나 같은 실행 조건의 판본 간 성능 변화로 읽지 않는다.

근거: [SRC-0001910 PDF4쪽](../sources/history-129.md#src-0001910) · [SRC-0001912 PDF6쪽](../sources/history-129.md#src-0001912) · [SRC-0001900 행19–21](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-07"></a>

### H129-C07 2025의 K 선정과 없는 대조군

Cash2025는 histogram/JSD 계층 군집의 dendrogram 절단으로 Abilene K9·GéANT K47을 택했다. 그 판본에는2026의 naive random partition 대조군이 없다. 당시 원05의 random/global 비교 원칙은 Cash2026 근거였으며 판본을 섞지 않는다.

근거: [SRC-0001910 PDF3,4쪽](../sources/history-129.md#src-0001910) · [SRC-0001912 PDF4,5쪽](../sources/history-129.md#src-0001912) · [SRC-0020826 행25–33](../sources/history-129.md#src-0020826) · [SRC-0001900 행15–21](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-08"></a>

### H129-C08 92%·75%의 비교군과 지표 척도

Cash2025가 요약한92%·75%는 histogram의 Abilene ARCNN·GéANT TE-Prophet 대비 RMSE 개선이다. Table I은 정규화 오차이며 현재 RCTL/Milan 활동량 비교가 아니다. 인쇄값 직접 나눗셈은92.1452%·75.8475%로, 요약 표현과 둥근 표를 재계산한 값은 원 예측 재현이 아니다. 이 Prophet은 TE 목적 GRU framework이며 동명의 다른 예측 라이브러리로 해석하지 않는다.

근거: [SRC-0001910 PDF1,4,5,6쪽](../sources/history-129.md#src-0001910) · [SRC-0001900 행19–19](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-09"></a>

### H129-C09 MLU bias의 기준은1이며 topology가 필요하다

Cash2025의 MLU bias는 예측 TM에서 계산한 MLU/ground truth TM에서 계산한 MLU로 기준1이다. raw ratio 자체의 최소화나18%·21% 감소라고 다시 계산하지 않는다. topology·TM 없는 Milan 활동량의 네트워크 활용 이득으로 바꾸지 않는다. local GRU는 Table I의4개 평균 오차 모두 histogram보다 낮으며 시각적 local 유사성을 평균 우위로 확대하지 않는다.

근거: [SRC-0001910 PDF2,4,5쪽](../sources/history-129.md#src-0001910) · [SRC-0001900 행19–19](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-10"></a>

### H129-C10 2026 표현·linkage·random 비교

Cash2026의 histogram은50bins/JSD/complete linkage, ACF·PSD는 Euclidean/average linkage이고 PSD는 Welch로 구한다. naive partition은 무작위 소속 비교다. Table V의 작은 크기 차이는 관측한 분할이며 모든 random 알고리즘의 균형 보장은 아니다. 정확한 seed·author code는 미확인이다.

근거: [SRC-0001912 PDF4,5,9쪽](../sources/history-129.md#src-0001912) · [SRC-0001902 행38–58](../sources/history-129.md#src-0001902); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-11"></a>

### H129-C11 운영 K와 matched-K 유사도 분석

Cash2026 Table I/II의 운영점은 Abilene hist21/ACF21/PSD41/naive21, GéANT hist40/ACF100/PSD100/naive50이다. Table III의 NMI/ARI는 별도로 Abilene21·GéANT40으로 맞췄다. 운영점 RMSE/runtime를 동일 K 소속 품질의 순수 비교로 부르지 않는다.

근거: [SRC-0001912 PDF6,8,9쪽](../sources/history-129.md#src-0001912) · [SRC-0001899 행15–15](../sources/history-129.md#src-0001899) · [SRC-0001900 행21–21](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-12"></a>

### H129-C12 2026의 RMSE와 local 비교의 경계

Cash2026 Table II의 테스트 RMSE는Mbps이며2025 정규화 Table I과 합치지 않는다. moderate 운영 K에서 hist/ACF/PSD/naive의 비슷한 오차는 해당 비교의 관측이다. 모든 표현·K·데이터에서 grouping이 무용하다는 증명이 아니다. 두 dataset 모두 local GRU가 가장 낮은 표 오차이며 global/naive를 유지할 이유와 full-local 비용의 trade-off를 함께 남긴다.

근거: [SRC-0001912 PDF6,7,8,9쪽](../sources/history-129.md#src-0001912) · [SRC-0020826 행25–33](../sources/history-129.md#src-0020826) · [SRC-0001900 행68–75](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-13"></a>

### H129-C13 Kneedle·runtime·공식 구현의 미확인

Cash2026은 K를10씩 늘린 sweep/five trials/errorbars/Kneedle을 설명하지만 선택 곡선이 어느 split인지 본문만으로 확정하지 않았다. 이것만으로 test leakage를 단정하지도 않는다. runtime의 전체 경계·hardware와 author head/seed/code는 미확인이다. 본문 Abilene local120–150분과 뒤150–200분을 임의 통일하거나 현재 CPU latency로 환산하지 않는다.

근거: [SRC-0001912 PDF6,7,9쪽](../sources/history-129.md#src-0001912) · [SRC-0001902 행38–58](../sources/history-129.md#src-0001902) · [SRC-0001900 행21–25](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-14"></a>

### H129-C14 Ma의 관측 개체는 하루이며 센서는 성분이다

Ma v1 PEMS-BAY는 N180개의 하루 MTS, 각각288×325(5분)다. PEMS-SF는 N440개의 하루 MTS, 각각144×963(10분)다. sensor 개수를 cluster 대상 수로 세지 않는다. 전처리 후 논문 개체의 설명이며 원 dataset을 새로 처리한 수치가 아니다.

근거: [SRC-0001914 PDF17,19,20,23쪽](../sources/history-129.md#src-0001914) · [SRC-0001900 행23–23](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-15"></a>

### H129-C15 하루 내부 분할과 절대 미래 날짜의 차이

Ma §2.2.1/Algorithm1은 각 MTS의 시간축을 TRAIN/VAL/TEST로 나누고 TRAIN 통계로 imputation/standardization한다. 현재 모든 기존 cell을 같은 미래 절대 날짜에서 평가하는 문제와 다르다. 논문 전체가 잘못된 목적이라고 판단하지 않으며 정확한 구간 길이·실행 구현은 이번 범위에서 미확인이다.

근거: [SRC-0001914 PDF6,7,19,20,37쪽](../sources/history-129.md#src-0001914) · [SRC-0001900 행73–73](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-16"></a>

### H129-C16 Ma의 공유 encoder와 반복 forecaster 학습

Ma는 learned mixture B·한 층 GRU·linear head/B 전치 reconstruction을 쓴다. GLOBAL을 TRAIN에서 학습하고 encoder/decoder를 공유한 prototype에 warm start와ℓ2-SP를 적용해 반복 학습한다. 한 번의 거리 clustering이나 최종 learner를 호출하지 않는 소속 규칙으로 설명하지 않는다.

근거: [SRC-0001914 PDF5,6,11,12,13,14,37쪽](../sources/history-129.md#src-0001914) · [SRC-0001900 행23–23](../sources/history-129.md#src-0001900); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-17"></a>

### H129-C17 Ma의 validation 소속·K·fallback 절차

Ma는 VAL 예측 손실로 소속을 재배정하고 routed VAL+γK/N으로 K/seed를 고른다. cluster 평균 VAL 손실이 GLOBAL보다 나쁜 경우 fallback을 고정한 뒤 TRAIN+VAL refit과 single-use TEST를 한다. 선택 손실과 TEST 보고 지표를 구분하며 TEST로 fallback을 뒤늦게 정하지 않는다.

근거: [SRC-0001914 PDF5,6,8,13,14,15,18,19,37,38,39쪽](../sources/history-129.md#src-0001914); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-18"></a>

### H129-C18 validation fallback은 모든 개체의 무손해 보장이 아니다

Ma의 PEMS-BAY 선택 K7에서 인쇄된 TEST MSE 개선은 h1/3/6의18.12/19.24/23.75%, Ben은84/86/92%, Fb는0이다. fallback은 cluster 평균 validation 기준이며 각 TEST 하루나 새로운 절대 미래 기간 전부의 무손해 보장은 아니다. VAL Huber 선택·×100 테스트 표·저자 보고치를 현재 RCTL 결과나 원 예측 재현으로 승격하지 않는다.

근거: [SRC-0001914 PDF14,18,19,20,21,39쪽](../sources/history-129.md#src-0001914); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-19"></a>

### H129-C19 GRU 규모식의 명시적 가정

각 cluster d_k입력·H hidden의 한 층 단방향 GRU, PyTorch식 bias2개, H→d_k linear head, 서로 겹치지 않는Σd_k=D를 가정하면 P_K=K(3H²+6H)+(4H+1)D다. 공식 tensor shape와 확장 정수 합을 대조했다. 저자의 head/계층/방향을 검증한 checkpoint 측정식은 아니다.

근거: [SRC-0001900 행29–33](../sources/history-129.md#src-0001900) · [SRC-0001903 JSON/GRU_assumptions,/GRU_capacity](../sources/history-129.md#src-0001903); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-20"></a>

### H129-C20 9개 GRU 저장 계산행의 일치

H200에서 D144/K1은236544, K21은2660544(11.247565배), D529/K1은544929, K40은5271729(9.674158배)다. 원JSON9행의 count와 K1대비 비를 자체 tensor-size 정수 합/Fraction으로 대조했다. 약24만/266만 표현과 저자 checkpoint 실측은 구분한다.

근거: [SRC-0001900 행35–42](../sources/history-129.md#src-0001900) · [SRC-0001903 JSON/GRU_capacity](../sources/history-129.md#src-0001903); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-21"></a>

### H129-C21 입출력 축소와 총 용량·원인 분리

joint-vector 분할은 d_k를 줄이면서 recurrent core를 K개로 늘린다. 위 가정의 전체 용량 증가는 소속 효과와 함께 변하는 요인이지만 관측 개선의 유일한 원인으로 입증하지 않았다. 반대로 정확한 관계 grouping의 인과 이득도 운영점 표만으로 확정하지 않는다.

근거: [SRC-0001900 행21–44](../sources/history-129.md#src-0001900) · [SRC-0001912 PDF6,7,8,9쪽](../sources/history-129.md#src-0001912); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-22"></a>

### H129-C22 등록 parameter와 학습 가능 parameter

현재 보존 RCTL source의 정적 shape 합은 등록174433개다. 각 LSTM의 zero bias_hh가 requires_grad=False여서896개를 제외한 학습 가능 수는173537개다. 후자는 이번 아카이브의 추가 정적 산술이며 원99의 실측 주장이나 모델 생성 결과가 아니다. Cash의GRU 두-bias 가정과 같은 학습 용량 정의로 섞지 않는다.

근거: [SRC-0023048 행1–60](../sources/history-129.md#src-0023048) · [SRC-0023202 행84–95](../sources/history-129.md#src-0023202) · [SRC-0031766 JSON/checkpoints](../sources/history-129.md#src-0031766); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-23"></a>

### H129-C23 state 저장량과 peak memory의 차이

RCTL float32 parameter는697732bytes, BN buffer/counter는3680bytes, state tensor 합은701412bytes다. 이전95의9개 checkpoint metadata와 정적 source 합이 일치한다. K4 state 합2805648bytes는 optimizer state·실제 파일 크기·peak RAM·훈련시간을 포함하지 않는다. checkpoint 가중치를 읽어 모델을 실행하지 않았다.

근거: [SRC-0023048 행1–60](../sources/history-129.md#src-0023048) · [SRC-0031766 JSON/checkpoints](../sources/history-129.md#src-0031766) · [SRC-0001903 JSON/scalar_RCTL_workload](../sources/history-129.md#src-0001903); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-24"></a>

### H129-C24 완전 epoch 처리행은 N×T다

원 pilot train target168–839는 cell당672개, batch256이다. 모든 실제 sample을 한 번 사용하는 완전 epoch이면 분리한 전체 처리행은 N×672이고 update는Σceil(n_k×672/256)다. N128/1024/10000의86016/688128/6720000행은 실제 대규모 학습이 아니라 고정 조건 산술이다.

근거: [SRC-0030238 행1–46](../sources/history-129.md#src-0030238) · [SRC-0023202 행62–106](../sources/history-129.md#src-0023202) · [SRC-0001900 행48–56](../sources/history-129.md#src-0001900) · [SRC-0001903 JSON/scalar_RCTL_workload](../sources/history-129.md#src-0001903); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-25"></a>

### H129-C25 균형 분할 update12행과 반올림 overhead

K1/4/16/32 균형 분할에서 N128 update336/336/336/352, N1024는2688씩, N10000은26250/26252/26256/26256이다. 12행 모두 저장 정수와 일치했다. row 수와 ceil 반올림·모델별 epoch/early-stop·hardware 효율이 다른 총 시간을 구분한다.

근거: [SRC-0001900 행48–56](../sources/history-129.md#src-0001900) · [SRC-0001903 JSON/scalar_RCTL_workload](../sources/history-129.md#src-0001903); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-26"></a>

### H129-C26 N개 예측행과 호출 횟수·이전 latency

같은 시각 모든 cell을 예측하면 scalar row와 출력은 N개다. 호출 batching은 호출 수를 바꾸지만 row를 없애지 않는다. 이전95의16cell/CPU4threads/float32/6route 측정은 load·input 준비 제외이며 이번10000cell 산술의 latency 외삽이나 새로운 forward 결과가 아니다.

근거: [SRC-0001900 행56–56](../sources/history-129.md#src-0001900) · [SRC-0031766 행1–130](../sources/history-129.md#src-0031766) · [SRC-0031766 행177–343](../sources/history-129.md#src-0031766); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-27"></a>

### H129-C27 Tab 준비·query·분위수 cache의 범위

원99에서 가져온 B2의 M504/Q168/R1,129개 float32 분위수 가정이면 N10000은 cell별 준비10000회/context5040000행/query1680000행/cache866880000bytes(약0.87decimalGB)다. context X+y의17열·query16열 배열 산술도 별개로 대조했다. 가중치·activation·ensemble·검색/I/O/첫 추론·peak RAM·총 시간은 포함하지 않으며 B2 채택/새실행 증거가 아니다.

근거: [SRC-0001900 행58–66](../sources/history-129.md#src-0001900) · [SRC-0023202 행59–61](../sources/history-129.md#src-0023202) · [SRC-0001903 JSON/scalar_RCTL_workload](../sources/history-129.md#src-0001903); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-28"></a>

### H129-C28 설계 기준과 최종 미추천의 역할

원99는 같은 scalar 구조/K/sample/학습 조건의 소속 비교와 별도의 K별 정확도·비용 곡선을 구분하라고 판단했다. 기존 global/naive와 K4 두 seed 결과를 유지하며 Tab이 바꾸는 grouping 판단 또는 그 판단 비용을 먼저 특정했다. 이 검토만으로 새 알고리즘의 실익·신규성·최종 추천은 생기지 않았고 clustering 전체의 과학적 기각도 아니다.

근거: [SRC-0001899 행41–47](../sources/history-129.md#src-0001899) · [SRC-0001900 행68–75](../sources/history-129.md#src-0001900) · [SRC-0001901 행18–23](../sources/history-129.md#src-0001901) · [SRC-0001904 행87–94](../sources/history-129.md#src-0001904); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-29"></a>

### H129-C29 판본·다운로드·TXT와 이미지 대응

원99에는 처음HTTP406 후 PDF Accept header/unversioned fallback으로 성공했다는 기록이 있으나 정확한 성공 transport URL은 별도 저장되지 않았다. 현재 공식 v1 서지와 보존 PDF SHA를 구분한다. PDF3편61쪽/TXT의CRLF 정규화 대응과 원PNG6개의110dpi byte 일치는 기계 검증이다. 전TXT 직접 판독·모든 표/코드 재현이나 신규성 검색의 전수 성공이 아니다.

근거: [SRC-0001902 행18–94](../sources/history-129.md#src-0001902) · [SRC-0001902 행117–124](../sources/history-129.md#src-0001902) · [SRC-0001907 행1–84](../sources/history-129.md#src-0001907) · [SRC-0001908 행1–15](../sources/history-129.md#src-0001908) · [SRC-0001916 행1–32](../sources/history-129.md#src-0001916) · [SRC-0001917 행1–32](../sources/history-129.md#src-0001917); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-30"></a>

### H129-C30 snapshot 물리 수와 root receipt 사본

snapshot41 manifest는25파일4663812bytes를 열거한다. manifest5412bytes와 snapshot verification461bytes를 더하면 실제27파일4669685bytes다. 별도 root99 receipt는 동일 SHA 사본이므로 독립 검증 실험으로 늘리지 않는다. manifest/각 파일 크기·SHA를 대조했다.

근거: [SRC-0001897 행1–131](../sources/history-129.md#src-0001897) · [SRC-0001898 행1–11](../sources/history-129.md#src-0001898) · [SRC-0001909 행1–120](../sources/history-129.md#src-0001909); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-31"></a>

### H129-C31 역사 원장과 현재 root 판본·Word 보존

원99 snapshot 원장807600…는 원98 이후 동일 판본이고 잔여Tab11context/20640행·RCTL추가fit0은 당시 상태다. 현재 원본root 원장17a549…는 나중 판본이며 처음 보존 baseline과 일치한다. 둘을 동일 SHA라고 주장하거나 과거 원장으로 덮어쓰지 않는다. 보호 원본6개 불변, Word SHA4f1112…는 hash-only로 본문/layout 미독이다.

근거: [SRC-0001906 행14–17](../sources/history-129.md#src-0001906) · [SRC-0001901 행3–3](../sources/history-129.md#src-0001901) · [SRC-0001909 행1–120](../sources/history-129.md#src-0001909); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.

<a id="claim-32"></a>

### H129-C32 실제 판독·새 완료·남은 범위

최초 원문1090행(core903/candidate94/progress93), 이전 근거687행 재독, PDF45텍스트쪽3120행·36파생 이미지다. Cash6/12쪽은 전체 text/image, Ma27/43쪽 text·18image이며 Ma16쪽과 각 전TXT 직접 판독은 미완료다. 현재progress94–573/이전85–563의 기계 일치를 의미 판독으로 세지 않는다. 새 집계 예정은 기록1/주장32/본문7/전체JSON6/선택2/독립이미지0이며 이 기록의 문서 검수 후 한 번만 집계한다. 원100이후·이전고유판본/FedPPBC/DOCX/통합·접근·최종delta·대표질문10+ 남아 전체 Goal 미완료다.

근거: [SRC-0001906 행1–17](../sources/history-129.md#src-0001906) · [SRC-0001902 행117–124](../sources/history-129.md#src-0001902); 상세 위치·추가 검산은 [주장 목록](../verification/history-129-claims.json) 참조.
