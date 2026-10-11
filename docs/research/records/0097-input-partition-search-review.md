# H097 · 원81의 검색 경로와 문헌·코드 근거 연결

입력 분할을 검토하던 당시 검색 기록을 정리했다. 이미 검토한 네 핵심 방법, 아직 후보인 문헌, 저장 범위가 부족한 응답을 구분해 같은 조사를 반복할 때 확인할 출발점을 제공한다.

**상태:** 32개 주장·8개 검수 묶음의 작성 후 원문 대조 완료. 새 모델 실행 0.

[원81 결정](0090-input-partition-decision.md) · [출처](../sources/history-097.md) · [검수](../verification/history-097.md) · [응답 목록](../evidence/0097-input-partition-search/response-index.json)

## 이 기록이 보존하는 조사 범위

<a id="c01"></a>**C01.** 원81의 저장 검색 기록은 JSON 1그룹, 동일 바이트 사본 2경로, 225,455 bytes다. 최상위 메타데이터와 검색 질의 10개, 결과 문자열 8개를 모두 읽었다. JSON 전체 독해는 그 안에 연결된 웹 문서 전체의 독해와 다르다. 본문 35물리행 안에 긴 문자열이 들어 있어 출처는 JSON pointer와 디코딩한 문자열의 1부터 시작하는 문자 구간으로 지정한다.

[SRC-0062870](../sources/history-097.md#src-0062870)

<a id="c02"></a>**C02.** 저장 date는 2026-09-26이고 purpose는 원81 입력 분할 방법·공식 코드 조사이며 새 모델·수치 pilot이 없다고 적는다. 원81도 새 TabICLv2 추론·회귀 적합·RCTL 계산 0회를 기록했다. 세 응답 wrapper의 fulfilled는 도구 반환 상태이며 논문 전문 확보나 실행 성공의 증거가 아니다. 이번 정리에서도 원 연구 코드·검색 기록 안의 명령·R 예제를 실행하지 않았다.

[SRC-0062870](../sources/history-097.md#src-0062870) · [원81 1–11행](../sources/history-097.md#src-0022042)

<a id="c03"></a>**C03.** 구분자로 나눈 응답은 101개, 정확히 같은 URL 문자열을 합치면 93개다. 7개 URL이 반복되며 URL 인코딩·미러·판본을 합치는 논문 단위 중복 제거는 하지 않았다. 같은 XGBoost 배포 질문이 Reddit 네 커뮤니티에 실린 사례도 있다. 101응답·93URL·10질의를 독립 논문 수나 연구·실험 수로 세지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R026, R027, R028, R032

<a id="c04"></a>**C04.** 14개 저장 open 응답 중 SCPaT·DUET GitHub·DGCformer HTML 세 응답은 제목과 총행수 헤더만 있고 본문 L행이 없다. CRAN index는 접근 오류 한 행이다. 나머지도 표시 범위가 서로 다르며, 총행수는 저장된 본문 길이가 아니다. 별도 범위표는 웹 응답의 0부터 시작하는 L행과 JSON 문자열의 1부터 시작하는 문자를 구별한다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R033, R034, R035, R073, R074, R075, R076, R077, R078, R079, R080, R081, R100, R101

<a id="c05"></a>**C05.** 응답 101개 모두에 원 JSON pointer·문자 구간·응답 텍스트 SHA-256·URL·표시행 범위를 연결했다. 여기의 URL은 당시 응답을 찾는 출처이며 이번에 모두 다시 접속한 주소가 아니다. 검색 결과 전문은 재게시하지 않고 조사 범위와 분석을 제공한다. URL 목록과 요약을 읽는 것만으로 미수집 문서 본문까지 확인했다고 표시하지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870)

## 후보 문헌과 검색 잡음의 구별

<a id="c06"></a>**C06.** 검색에는 arXiv·출판사·저자 프로젝트/저장소뿐 아니라 서지 집계, AI 요약, ResearchGate 소개, 다른 논문의 참고목록, 위키·Reddit가 함께 있다. 저자 원문을 확인할 수 있는 후보와 2차 소개를 같은 검증 수준으로 사용하지 않는다. Request full-text 표시는 해당 서비스의 상태이지 다른 공식 경로에도 전문이 없다는 증명이 아니다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R002, R003, R007, R012, R017, R023, R037, R038, R058, R059, R060, R064, R066, R067, R070, R071

<a id="c07"></a>**C07.** 당시 탐색 후보에는 global model의 예측 정확도 기반 군집화, TimeCapsule, contextual subsequence 군집화, Cini 등의 계층 예측, STaTS, SCPaT, localized forecasting model이 있다. 검색 발췌로 발견한 후보이며 원81의 네 핵심 방법과 같은 깊이로 검토된 목록이 아니다. 새 설계가 해당 개념에 의존할 때 판본·방법·조건을 추가로 확인해야 한다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R004, R005, R006, R010, R011, R014, R019, R020, R021, R034 · [원81 97–103행](../sources/history-097.md#src-0022042)

<a id="c08"></a>**C08.** 검색어 partition은 서로 다른 대상을 가리켰다. 관측 공간의 데이터 분할, CMI 추정을 위한 구간화, 과거 trajectory를 예측 상태로 압축하는 정보병목, 환경 변수의 정보 분해, channel 집합의 군집화는 같은 결정 규칙이 아니다. CMI 식이 Image 자리표시자로 남은 응답은 식을 실제로 읽은 근거로 사용하지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R040, R041, R042, R043, R044, R047, R050, R055

## DGCformer·DUET 검색과 이미 검토한 근거의 연결

<a id="c09"></a>**C09.** DGCformer의 초록과 방법 응답에는 deep graph clustering 뒤 cluster 내 attention을 허용하는 설명과 64경우 중 57경우 최상위라는 저자 주장이 있다. 검색 발췌만으로 전체 표·K 선택·학습 독립성을 확정하지 않는다. 원81의 분리형 입력 분할 비교는 H091의 전체 문헌 검토, 조건과 반례를 함께 읽어야 한다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R036, R075, R079 · [원81 25–31행](../sources/history-097.md#src-0022042) · [H091-C01](../records/0091-dgcformer-source-review.md#c01) · [H091-C27](../records/0091-dgcformer-source-review.md#c27) · [H091-C28](../records/0091-dgcformer-source-review.md#c28)

<a id="c10"></a>**C10.** DGCformer의 코드 공개 예정 문구, 외부 논문 목록의 None 또는 대시, 원81의 공식 코드 미확인 진술은 각각 당시 자료의 상태다. 현재 공식 코드가 존재하지 않는다는 결론을 내릴 근거는 아니다. H093은 TimeSeriesCCM 코드 검토이며 DGCformer 코드 검토로 연결하지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R036, R039, R048, R075 · [원81 25–31행](../sources/history-097.md#src-0022042) · [H091-C29](../records/0091-dgcformer-source-review.md#c29) · [H093-C01](../records/0093-ccm-code-review.md#c01) · [H093-C02](../records/0093-ccm-code-review.md#c02)

<a id="c11"></a>**C11.** DUET details 응답은 arXiv v2(2024-12-23)의 L0–179/총539행이고, methods 응답은 v3(2025-01-10)의 L171–201/총544행이다. v1 제출일은 2024-12-14다. v2 발췌의 DOI 자리표시자·Woodstock 2018·Received 2009 같은 템플릿 잔재를 실제 서지로 사용하지 않는다. v3 전체 검토와 정식 표기 확인은 H094에 연결한다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R033, R074, R078 · [H094-C01](../records/0094-duet-literature-review.md#c01) · [H094-C02](../records/0094-duet-literature-review.md#c02)

<a id="c12"></a>**C12.** SCPaT v1 응답의 총466행과 DUET GitHub 응답의 총304행은 본문을 저장했다는 뜻이 아니다. 이 두 open 응답에는 L행 본문이 없다. 다른 필드의 DUET README 검색 발췌나 후속에 보존한 코드가 있다는 사실도 이 빈 응답 자체의 읽기 범위를 늘리지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R001, R034, R035

<a id="c13"></a>**C13.** DUET README 검색 발췌에는 버그 수정 뒤 결과를 재검증했다는 저자 설명과 실행 예제가 있다. requirements 위치에 ILI 명령 조각이 반복된 추출 흔적도 보존돼 있다. 이를 설치 명세나 고정 commit 실행 결과로 사용하지 않는다. 당시 수집한 코드의 날짜·해시와 논문 시점의 차이는 H095가 별도로 확인했다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R001 · [H095-C02](../records/0095-duet-code-review.md#c02) · [H095-C25](../records/0095-duet-code-review.md#c25) · [H095-C28](../records/0095-duet-code-review.md#c28)

<a id="c14"></a>**C14.** DUET 검색 수식의 Top-k 후 softmax, 학습 가능한 주파수 거리·mask는 논문 설명이다. H095의 고정 코드에서는 전체 softmax 뒤 Top-k와 재정규화, 전체 channel 쌍의 거리·attention 계산 등 실제 정적 경로를 따로 검토했다. 검색 수식과 코드를 동일한 실행이라고 합치거나 희소 mask만으로 전체 계산 비용 감소를 확정하지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R033, R078 · [원81 33–39행](../sources/history-097.md#src-0022042) · [H094-C07](../records/0094-duet-literature-review.md#c07) · [H095-C09](../records/0095-duet-code-review.md#c09)

## CCM 검색에서 재사용할 수 있는 것

<a id="c15"></a>**C15.** CCM methods의 Table 1 발췌는 ETTh1·ETTm1·Exchange, TSMixer/CD·DLinear/CI·PatchTST/CI·TimesNet/CD의 ΔLoss와 PCC 24개 인쇄값을 담는다. PCC 범위는 −0.68∼−0.47이다. 채널별 MSE 변화 차이와 표준화 시계열 RBF 유사도의 관찰이며, 원 단위 MSE를 최적으로 만드는 partition의 증명이 아니다. 24값은 별도 표에 전사해 저장 응답과 대조한다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R080 · [H092-C03](../records/0092-ccm-source-review.md#c03) · [H092-C05](../records/0092-ccm-source-review.md#c05)

<a id="c16"></a>**C16.** CCM의 확률 행 합이 1이라는 설명과 Bernoulli 근사 membership 설명을 동시에 보존한다. 이것만으로 각 채널이 꼭 한 군집에만 속하는 고정 partition을 보장하지 않는다. prototype 갱신과 cluster별 선형 출력의 가중 결합을 원81의 독립 RCTL core 학습과 구별한다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R061, R063, R080 · [원81 41–49행](../sources/history-097.md#src-0022042) · [H092-C06](../records/0092-ccm-source-review.md#c06) · [H092-C07](../records/0092-ccm-source-review.md#c07) · [H092-C10](../records/0092-ccm-source-review.md#c10)

<a id="c17"></a>**C17.** CCM PDF 검색 발췌 두 응답에는 수식 괄호 주변의 제어문자가 남아 있다. Stanford 응답에는 U+0012·U+0013 각1개, proceedings 응답에는 U+0000·U+0001 각6개가 있다. 이 텍스트를 정확한 수식으로 복사하지 않는다. Eq.4의 인쇄식 대수와 코드의 scalar 1·추가 entropy 차이는 H092·H093의 별도 검수로 연결한다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R061, R063 · [H092-C09](../records/0092-ccm-source-review.md#c09) · [H093-C22](../records/0093-ccm-code-review.md#c22) · [H093-C23](../records/0093-ccm-code-review.md#c23)

<a id="c18"></a>**C18.** CCM 발췌의 O(KCd)는 소속 점수와 prototype cross-attention에 관한 범위이고, 전체 C×C 유사도·기반 모델·전처리 비용이 아니다. README의 장기·zero-shot·M4·stock 실행 예제는 사용법 자료다. 명령이 실렸다는 사실은 원81에서 해당 실험이 수행됐다는 증거가 아니다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R058, R061, R062, R063 · [H092-C07](../records/0092-ccm-source-review.md#c07) · [H092-C11](../records/0092-ccm-source-review.md#c11)

<a id="c19"></a>**C19.** 원81이 정적으로 본 CCM 코드는 commit e4769baa7f8457358eb9b4614af2de1fbfba2257에 연결되며 H093이 저장 파일·Git blob을 대조했다. H093은 prototype 차원·optimizer 등록·채널 순서·유사도 축 등의 정적 위험을 기록했다. README와 검색상의 성능 설명으로 이런 조건을 해결됐다고 판단하거나 실제 논문 실행 실패가 관측됐다고 역으로 단정하지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R062 · [원81 41–49행](../sources/history-097.md#src-0022042) · [H093-C02](../records/0093-ccm-code-review.md#c02) · [H093-C15](../records/0093-ccm-code-review.md#c15) · [H093-C16](../records/0093-ccm-code-review.md#c16) · [H093-C18](../records/0093-ccm-code-review.md#c18) · [H093-C19](../records/0093-ccm-code-review.md#c19) · [H093-C20](../records/0093-ccm-code-review.md#c20)

## Fuchs–Wang과 didec의 판본·API 범위

<a id="c20"></a>**C20.** Fuchs–Wang의 저장 arXiv 서지는 v1 제출일 2023-12-27을 보여주지만 해당 응답은 L0–84/총158행까지만 남아 있다. ScienceDirect 검색 응답은 IJAR 170, July 2024, 109185와 DOI 10.1016/j.ijar.2024.109185, 자료 요청 가능 문구를 제공한다. 이는 원81 서지의 추가 저장 근거이며 출판사 PDF와 arXiv 본문의 동일성이나 현재 자료 접근성을 확인한 결과는 아니다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R053, R056, R072, R077, R083, R085 · [원81 51–57행](../sources/history-097.md#src-0022042) · [H096-C01](../records/0096-predictive-clustering-literature-review.md#c01) · [H096-C02](../records/0096-predictive-clustering-literature-review.md#c02) · [H096-C03](../records/0096-predictive-clustering-literature-review.md#c03)

<a id="c21"></a>**C21.** Fuchs–Wang methods 발췌는 변수 집합의 방향별 분포적 예측 의존성과 군집 간 결합을 다룬다. 공동 정보라는 개념만으로 신규성을 주장할 수 없지만 미래 horizon·raw MSE·UPC 재배정과 같은 방법이라고도 할 수 없다. 전체 논문의 정의·i.i.d. 가정·순열과 병합 비용·실패 조건은 H096을 참조한다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R056, R081, R085 · [원81 51–57행](../sources/history-097.md#src-0022042) · [H096-C04](../records/0096-predictive-clustering-literature-review.md#c04) · [H096-C06](../records/0096-predictive-clustering-literature-review.md#c06) · [H096-C07](../records/0096-predictive-clustering-literature-review.md#c07) · [H096-C09](../records/0096-predictive-clustering-literature-review.md#c09) · [H096-C20](../records/0096-predictive-clustering-literature-review.md#c20) · [H096-C21](../records/0096-predictive-clustering-literature-review.md#c21)

<a id="c22"></a>**C22.** didec의 ETH와 ZJU 미러 검색 발췌에는 API 서명 차이가 있다. ETH 발췌는 trans·estim.method를 포함하다 link.method에서 끝나고, ZJU 발췌는 criterion을 포함한 더 짧은 서명을 보여준다. part.criterion은 별도 공식 refman 응답에서 확인했다. 판본이나 발췌 범위 차이를 확인하기 전에 이들을 합친 호출 명세를 만들지 않는다. 일부 발췌에 인자가 없다는 사실만으로 패키지 전체에 없다고 판단하지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R084, R088, R101

<a id="c23"></a>**C23.** CRAN index 응답은 접근 오류이고 refman은 didec 1.1.0, Packaged 2026-01-30, Date/Publication 2026-02-02를 표시한다. refman 저장 범위는 L0–405/총1,070행이다. 오류 응답의 총1행을 모두 읽었다는 기계 판정은 패키지 소개나 API 전문을 확보했다는 의미가 아니다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R100, R101

<a id="c24"></a>**C24.** 저장 refman의 Codec.Tq.Perm과 Copula.Tq.Perm은 method 기본값 sample, 선택지 sample/increasing/decreasing/full을 명시한다. 이 문서의 기본값만으로 모든 계산이 q! 전체 순열을 실제로 열거했다고 할 수 없다. 표본 순열 수·seed·동률 처리·정확한 비용은 구현과 실행 설정을 확인해야 한다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R101 · [H096-C07](../records/0096-predictive-clustering-literature-review.md#c07) · [H096-C20](../records/0096-predictive-clustering-literature-review.md#c20) · [H096-C21](../records/0096-predictive-clustering-literature-review.md#c21)

<a id="c25"></a>**C25.** 저장 VarClustPartition 서명의 기본값은 trans=FALSE, trans.method=standardization, dist.method=PD, estim.method=copula, linkage=FALSE, link.method=complete, part.method=optimal, part.criterion=Adiam&Msplit, num.cluster=NULL, plot=FALSE다. standardization·complete라는 기본 문자열이 있다는 것과 변환·linkage가 기본으로 켜져 있다는 것은 다르다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R101

<a id="c26"></a>**C26.** VarClustPartition의 설명은 PD/MPD에서 codec·copula 추정법을 선택하고, optimal일 때 Adiam&Msplit 또는 Silhouette, selected일 때 지정 군집 수를 사용한다고 한다. PD/MPD와 kendall/footrule 선택, 전처리 여부와 linkage 여부를 각각 기록해야 한다. 이 API를 미래 오차를 최소화하는 실험 설정으로 바꾸어 기록하지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R101

<a id="c27"></a>**C27.** 저장 refman은 mfoci를 목차·패키지 설명에서 변수 선택 방법으로 소개하지만 해당 함수 본문은 L0–405에 포함되지 않는다. 이 범위에서 읽은 함수 설명과 이름만 나오는 API를 구별한다. 패키지 내부 source·설치·실행·모바일 트래픽 결과는 이번 묶음의 검증 범위 밖이다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R101 · [원81 51–57행,97–103행](../sources/history-097.md#src-0022042)

<a id="c28"></a>**C28.** SMPS 2024 시간표 PDF 검색 응답에는 직전 발표의 fuzzy count-data 군집화 초록과 Fuchs–Wang의 변수 군집화 발표 초록이 이어져 있다. 검색 결과 하나에 붙어 나온 두 초록을 하나의 방법으로 합치지 않는다. 저자·제목·세션 경계를 확인해야 잘못된 방법 귀속을 피할 수 있다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R086, R087

## 후속 연구를 시작할 때의 사용법

<a id="c29"></a>**C29.** STaTS의 성능 유지 비율, 제3자 특허 페이지의 DGCFormer 설명과 MAE 7.1% 개선, 다른 논문의 DUET 인용은 해당 응답에 실린 주장이다. 이를 원81의 실험 수치나 핵심 DGCformer·DUET 논문의 성능으로 옮기지 않는다. 새 실험의 근거로 쓸 때는 해당 원문·자료·비교 조건부터 확인해야 한다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R011, R012, R052

<a id="c30"></a>**C30.** Published/Crawled의 상대 시각, 검색 저장 date, arXiv 제출·개정일, CRAN package publication, Git commit 시각은 서로 다른 날짜다. 검색 응답에 나타난 최근 연도나 Code Finder UI만으로 논문의 실제 발표일·최신판·공식 구현 존재·원81 실행 시점을 정하지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870) · 응답 R001, R074, R075, R076, R077, R101

<a id="c31"></a>**C31.** 원81은 입력 공유를 다중 출력으로 바꾸는 후보에서 추가 실행에 들어가지 않았고, TabICLv2 직접 예측 이득은 유지했다. 단순히 분할·공동 정보를 쓰는 구조와 실제 입력 분할 손해를 줄이는 근거를 구분했으며 단일 global 다중 출력도 비용 비교군으로 요구했다. 이 검색 기록은 그 판단의 조사 경로이지 모든 다변량 군집화가 무용하다는 결론이나 새 성능 실험이 아니다.

[원81 5–11행,75–95행](../sources/history-097.md#src-0022042)

<a id="c32"></a>**C32.** H091–H097로 H090 당시 남아 있던 원81 sources/input_partition_81의 29그룹을 연결했다. 이 패킷의 남은 그룹은 0이지만 snapshot23 연혁의 고유 변경과 이후 기록은 아직 남는다. 후속 설계는 분할 대상·목표 시점·손실 척도·입력 가능 시점·선택에 쓴 시간 구간·강한 비교군·전체 비용을 기존 기록과 비교해 차이를 명시해야 한다. 검색 후보 목록을 전체 연구의 신규성 판정이나 Goal 완료로 사용하지 않는다.

[SRC-0062870](../sources/history-097.md#src-0062870) · [원81 87–103행](../sources/history-097.md#src-0022042) · [H091-C30](../records/0091-dgcformer-source-review.md#c30) · [H096-C03](../records/0096-predictive-clustering-literature-review.md#c03)

## 다음 조사에서 바로 열 자료

| 조사 질문 | 먼저 읽을 기록 |
|---|---|
| 분리된 channel clustering 뒤 예측하는 선행 구조는? | [H091 DGCformer](0091-dgcformer-source-review.md) |
| cluster별 예측 규칙과 소속 확률을 함께 학습했나? | [H092 CCM 문헌](0092-ccm-source-review.md), [H093 저장 코드](0093-ccm-code-review.md) |
| 주파수 mask·expert routing과 실제 계산 비용은? | [H094 DUET 문헌](0094-duet-literature-review.md), [H095 저장 코드](0095-duet-code-review.md) |
| 쌍별 값이 놓치는 공동 의존성과 가정은? | [H096 Fuchs–Wang](0096-predictive-clustering-literature-review.md) |
| 아직 원문 확인이 필요한 검색 후보·API는? | [101응답 목록](../evidence/0097-input-partition-search/response-index.json), [14 open 범위](../evidence/0097-input-partition-search/open-scopes.json) |

데이터·시간 분할·seed·평가 결과는 새 실행이 없으므로 이 검색 정리의 실험 설정에 해당하지 않는다. 관련 논문이 보고한 조건, 원81의 과거 판단, 이번 정리의 검수 범위는 각각의 연결 기록에서 확인한다.
