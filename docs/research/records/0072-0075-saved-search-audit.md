# 72–75 저장 검색: 같은 이름과 실제 연구 역할 구분

원72–75의 저장 검색 11개를 전구간 읽은 후, 핵심 주장과 출처를 다시 대조한 기록이다. [출처와 좌표](../sources/history-073.md) · [응답 목록](../evidence/0072-0075-saved-search/response-ledger.json) · [주장별 검수](../verification/history-073-claims.json) · [검수 범위](../verification/history-073.md). 작성한 에이전트가 관련 원문을 다시 대조했으며 독립 심사나 연결 논문 전체 독해를 뜻하지 않는다.

## 무엇을 확인한 기록인가

<a id="c01"></a>**C01.** 원72–73은 학습 구조·출력 압축의 문헌을 검토했고, 원75는 다른 cell의 과거를 입력에 추가하는 경로가 [47](0047-input-sharing-roles.md)과 겹친다고 판단해 실행 전에 중단했다. 두 findings 모두 당시 새 모델 실행·자료 수치 계산이 없다고 기록한다. 검색에 발견된 방법을 새 실험이나 추천안으로 세지 않는다. [72–73 당시 기록](../evidence/0072-0075-output-compression/originals/SRC-0022023.md.txt) · [75 당시 기록](../evidence/0072-0075-output-compression/originals/SRC-0022029.md.txt)

<a id="c02"></a>**C02.** 이번 독해 단위는 TXT 8개와 JSON 3개에 저장된 **159개 응답 블록**이다. 검색 노출143개, 성공 형태의 open/find 응답13개, 내부 오류2개, 브라우저 확인 화면1개다. 159편의 논문이나 159회 실험이 아니다. JSON의 `fulfilled`는 저장된 호출 상태이며 본문 확보·과학적 검증·실험 성공을 뜻하지 않는다.

<a id="c03"></a>**C03.** [목록](../evidence/0072-0075-saved-search/response-ledger.json)은 응답마다 원본 ID·파일/JSON `value` 좌표·짧은 제목·URL·분류·해시를 연결한다. JSON 원파일은 각각4행이지만 `value`에 긴 응답을 담고 있으므로, 실제 읽기는 문자 구간으로 기록했다. 파일 제목에서 정확한 검색 질의나 검색한 날짜를 추정하지 않는다. 이 자료는 체계적 문헌 검색의 완전성을 입증하지 않는다.

<a id="c04"></a>**C04.** `Total lines`, PDF 쪽수, `Download PDF`, 그림 캡션은 실제 포함된 본문·그림과 다르다. 이 11개에는 외부 그림의 픽셀이 없고, 수식이 `Image`로 빠진 발췌도 있다. Globalization 전체는 [H071](0072-globalization-audit.md), ForeCA·mbrdr의 추가 일차자료와 GNN 코드는 [H072](0073-forecastable-output-audit.md)의 별도 검수로 연결한다. 검색 발췌를 읽은 사실로 이 범위를 소급 확대하지 않는다.

## 72: 군집 단위·재인용·코드 공개의 경계

<a id="c05"></a>**C05.** `72_source_web.txt`의 Globalization 발췌는 지역별 학습 계수를 묶는 whole-series 방식과, 전체 sample의 거리를 중요도로 가중하는 instance 방식을 나눠 제시한다. 둘 다 군집별 global model을 학습하지만 군집 단위와 필요한 학습 정보가 다르다. 후자를 고정 cell 소속을 직접 산출하는 방법으로 바꾸어 설명하지 않는다. 가중치의 정의·부호·척도와 비용 한계는 H071을 함께 확인한다.

<a id="c06"></a>**C06.** `72_read_b1.json`은 HTML의 L124–168·L290–321·L330–358과 PDF 메타데이터를 담는다. `72_read_c1.json`에는 서로 겹치는 Table2 발췌, 비연속 검색 결과, PDF에서 `training`을 찾다 난 내부 오류가 있다. 반복된 표를 독립 결과로 세거나 검색 오류를 “학습이 없다”는 근거로 쓰지 않는다. 표·본문 수치의 차이는 H071에서 보존한 판단을 따른다.

<a id="c07"></a>**C07.** `github` 검색에서 나온 arXiv의 문제 신고 UI와 `Links to Code`, Hugging Face, Demos 등의 일반 메뉴는 저자가 연구 코드를 공개했다는 증거가 아니다. 원72 findings도 공개 코드를 확인하지 못했다고 적는다. 메뉴 문구나 과거 `Submit` 안내를 지금 실행할 지시로 취급하지 않는다.

<a id="c08"></a>**C08.** 저장 arXiv 정보의 “63쪽·22그림” 코멘트와 확보 PDF의65쪽 메타데이터는 각각 보존한다. 또 같은 제목의 forecasting-accuracy clustering은 2023 arXiv와 2025 KBS 출판본에서 저자·판본 차이가 있다. 동일 연구 계보로 연결하되 바이트가 같은 사본이나 방법이 완전히 같은 판본이라고 확정하지 않는다. KBS 전체 본문 검수는 남아 있다.

<a id="c09"></a>**C09.** `72_new_candidate_search.txt`에는 tabular embedding, context resampling, 표형 데이터 분류, PFN 목록과 응용 사례가 섞여 있다. Universal Tabular Embeddings의 dummy label·표현 collapse·전처리 설명은 검색 발췌의 주장이다. Credit resampling의 context sample 선택을 최종 예측기 학습에 쓸 cell 소속 결정과 동일하게 다루지 않는다.

<a id="c10"></a>**C10.** CatalyzeX의 저자 목록 발췌는 bandit 연구의 regret·engagement 설명 다음에 TabClustPFN 항목을 보여 준다. 앞 연구의 성능 문장을 TabClustPFN 결과로 옮기면 잘못된 귀속이 된다. ResearchGate·논문 목록·학회권 목록에서도 한 검색 결과 안에 여러 연구가 들어갈 수 있으므로 제목 하나에 모든 문장을 귀속하지 않는다.

<a id="c11"></a>**C11.** ScaleMoR는 두 OpenReview URL로 반복 노출되며, 저장 설명은 공유 선형 가중치·재귀 깊이 expert·다중 척도 정렬을 다룬다. 두 URL을 독립 실험으로 세지 않는다. Small Tabular Datasets의 분류 표와 edge-device K-means·DPO 관련 발췌도 그대로 UPC 소속이나 최종 RCTL 성능의 근거가 되지 않는다.

## 73: 예측 가능성과 차원 축소의 서로 다른 뜻

<a id="c12"></a>**C12.** `73_covariance_search.txt`의 hierarchical forecasting 초록·소개는 군집의 구성원 선택과 계층의 깊이·그룹 크기 등 구조를 구분하고, 구조를 고정한 무작위 재배정 대조를 설명한다. “유사한 시계열을 묶어서 좋아졌다”는 해석을 점검할 단서다. 해당 reconciliation 설정의 결과를 모든 군집화가 무용하다거나 UPC가 기각됐다는 결론으로 확대하지 않는다.

<a id="c13"></a>**C13.** 같은 파일의 validation-driven MTS 원고는 TRAIN에서 prototype을 학습하고 VAL에서 소속·모델을 선택하며 TEST를 평가용으로 남기는 절차를 설명한다. 이는 저장된 원고 발췌의 설계다. 실제 구현의 분할·누수 부재·재현을 확인했다는 뜻은 아니다. GLOBAL warm start와 cluster prototype 학습도 최종 예측기 독립 소속 조건과 별도로 비교해야 한다.

<a id="c14"></a>**C14.** response dimension reduction와 predictor dimension reduction는 축소하는 쪽이 다르다. Yoo–Cook2008·MBRDR는 응답의 조건부 평균 보존을 다루는 경로이고, Kernel SDR·orthoDr·SPCA 검색 결과에는 입력의 축소가 포함된다. 부분 수식이나 `C.1–C.7` 같은 미포함 가정을 본 것만으로 효율성·카이제곱 정리 전체를 검증했다고 쓰지 않는다. 제목이 비슷한 Yoo–Cook2007과2008도 서로 다른 DOI의 논문이다.

<a id="c15"></a>**C15.** ForeCA의 2013 PMLR, 2012 arXiv, CRAN 인용 정보, GitHub, rdrr, 블로그는 원논문·판본·구현 안내·설명의 서로 다른 자료다. 검색 블로그의 Ω 예시 수치를 예측 MAE 개선율로 쓰지 않는다. 저자 초록의 white-noise 분리·수렴·국소 최적성 표현은 H072에서 대조한 가정·정규화·증명 범위와 함께 읽는다. 패키지 설치 문구를 읽었지만 설치·실행하지 않았다.

<a id="c16"></a>**C16.** GNN 검색 발췌는 `X̂ = SZ`의 lift, 예측 MAE와 두 auxiliary loss의 합, 소속을 선명하게 만드는 temperature 조절을 보여 준다. 예측 손실을 군집 품질의 대리값으로 쓰는 설명에는 유사한 동역학과 class의 연관성 가정이 붙는다. 이를 모든 자료에서 MAE와 NMI·HS가 동등하다는 보장으로 쓰지 않는다. class를 요구하는 NMI·HS·CS 평가와 비지도 훈련·검증의 역할도 다르다.

<a id="c17"></a>**C17.** GNN의 OpenReview ID URL과 PDF 해시 URL에는 각각 본문의 일부가 검색돼 있지만, 별도 forum 열기는 브라우저 확인 화면을 반환했다. 발췌를 읽을 수 있었다는 것과 전체 PDF 확보 실패는 양립한다. 도식의 단어·캡션만 저장된 부분을 그림 시각 검수로 세지 않는다. H072의 정적 코드 확인도 원논문 전체·실제 실험 로그의 빈칸을 대신하지 않는다.

<a id="c18"></a>**C18.** `73_predictable_subspace_search.txt`의 PMLR12개 결과는 학회권 목록이다. 논문 제목·쪽수·PDF/Software 메뉴가 보여도 각 본문·코드를 읽은 것은 아니다. ICML2024의 Cini–Mandic–Alippi 논문과 TMLR2025의 Hansen–Cini–Bianchi 논문을 같은 제목의 사본처럼 합치지 않는다. COSA의 출력 adapter와 STGNN 소속 학습도 다른 연구 역할이다.

<a id="c19"></a>**C19.** `73_mbrdr_access_search.txt`는 같은 MBRDR의 출판사 발췌·기관 서지·교수 페이지·학술지 목록을 반복 보여 준다. 주변의 다른 논문과 학회 발표를 별도 확인한 본문으로 가산하지 않는다. 검색 발췌는 절을 건너뛰고 수식을 `Image`로 대체한 부분이 있다. 당시 직접 접근 실패는 보존하고, 이후 확보한 MBRDR2024 전체 PDF는 H072에 별도로 연결한다.

<a id="c20"></a>**C20.** `73_followup_1.json`의 online debiasing에서 `predictable`은 이전 정보집합에 대한 가측성 조건으로 쓰인다. ForeCA의 스펙트럼 지표나 실측 forecast error와 같은 뜻이 아니다. 전문가 예측의 편향·공분산을 다루는 금융 모형, 기후 model weighting, 기상 오차 보정도 용어가 겹친다는 이유로 cell 출력 압축의 증명으로 가져오지 않는다.

<a id="c21"></a>**C21.** SPCA·PCR·SIR·Kriging 관련 발췌의 반응 정보는 주로 입력 표현이나 선택에 사용된다. 의료·유전·GPS·Sinkhorn 검색 결과도 각각 설명변수 선택·관측 모형·평가 지표 등으로 분류한다. 동일 논문의 저널/기관 PDF 두 URL, 과거 학회 초록의 본문 연도와 검색의 상대 `Published` 표시는 독립 실험 수나 정확한 출판 날짜를 확정하는 근거가 아니다.

## 75: 입력 공유를 새 알고리즘으로 다시 세지 않기

<a id="c22"></a>**C22.** Granger graph clustering·GFSM은 target을 예측할 입력 변수의 중복을 조절하는 경로로 검색됐다. 2025 Ohmori 등의 초록은 pairwise 검사의 한계와 변수 조합 검사를 설명한다. 전체 조합의 계산비를 해결했다거나 예측 의존성이 같은 모델을 공유하기 좋은 충분조건이라고 추정하지 않는다. 원75가 중단한 이유와 47의 sample 공유/입력 열 추가 구분을 함께 확인한다.

<a id="c23"></a>**C23.** geocif0.4.809의 같은 페이지에는 TabICL 모델 목록과 별도 지역 CID 분석이 함께 나온다. 후자의 문서 예시는 PCA→Ward 군집화이며 `max_k=8`, 누적 PCA 분산 `.85`를 제시한다. 이 동시 노출만으로 TabICL이 군집 소속을 결정했거나 해당 분석이 통신 예측을 개선했다고 쓰지 않는다.

<a id="c24"></a>**C24.** IBM 튜토리얼 발췌는 `grangercausalitytests(..., 24)` 다음에 `res_dict[1]`의 p값을 선택한다. 24라는 인자가 보인다고 24개 lag의 결과를 모두 사용해 변수를 채택했다고 요약하지 않는다. 이 기록에서는 API의 변수 방향·분할·실제 실행을 검증하지 않았으므로, 튜토리얼 코드를 검증된 인과 발견이나 실행 가능한 대조군으로 표시하지 않는다.

<a id="c25"></a>**C25.** TabPFN의 Kernel SHAP, shapiq의 remove-and-recontextualize, feature relevance 목록은 입력의 기여나 상호작용을 다루는 별도 경로다. 예측 기여·조건부 연관성·인과관계·최종 cell 소속 효용을 한 지표로 합치지 않는다. shapiq의 두 도메인 URL은 같은 보충자료의 반복 노출이며, 그 benchmark 설정 수를 이 연구의 실행 수로 쓰지 않는다.

<a id="c26"></a>**C26.** fippy README 발췌는 Permutation/Gaussian sampler를 나열하고 TabPFN sampler는 **계획됨**으로 적는다. 따라서 TabPFN 연동 완료나 실험 재현으로 등록하지 않는다. 저장 검색의 GitHub 코드 조각·예제 플롯도 이번 작업에서 import·실행하지 않았다.

<a id="c27"></a>**C27.** Synthetic Data for Fine-tuning의 두 URL 발췌는 일부 조건에서50개 feature, 실행당10분 제한,32 CPU 병렬화를 설명하고, 목적을 예측 분포의 연관 구조로 한정한다. 이를 인과 입증·이 연구의 실제 비용·추가 실행 허가로 해석하지 않는다. 두 URL을 두 번의 독립 실험으로 가산하지 않는다.

<a id="c28"></a>**C28.** Bayesian Tabular Few-shot과 CausalPFN 결과는 TabICL을 참고문헌에서 언급한 구간이다. 단순 인용을 TabICL 기반 인과 군집화의 구현·실행으로 승격하지 않는다. TabCausal·CDFM·Markov Boundary도 각각 별도 문헌 단서로 남기며, 제목이나 인용 목록만으로 신규성의 채택·기각을 확정하지 않는다.

<a id="c29"></a>**C29.** SFTFormer의 super token, PCFNet의 period/channel 모델, chemical GCN-LSTM·C-TFT·AGAC 등의 다른 도메인 결과는 해당 저자의 보고다. 검색에 등장한 MSE·MAE 개선률, 분류 점수, 속도 비율을 UPC 소속 수정이나 RCTL 성능표에 옮기지 않는다. LinkedIn·Reddit 경험담과 일반 응용 목록도 검증된 연구실 결과와 구분한다.

## 팀에서 재사용할 때

<a id="c30"></a>**C30.** 후보를 다시 검토할 때는 먼저 **바꾸는 대상**을 지정한다: 학습 sample/context, 입력 변수·표현, cell 소속, latent 출력·복원, 예측값 보정, 설명 지표 중 무엇인가. 이어 사용 정보·선택 목적·최종 예측기 의존·실제 실행 자료를 확인한다. 키워드가 같거나 예측 성능이 좋다는 사실만으로 기존 방법과 같은 조건의 실험을 다시 시작하지 않는다. 이 안내는 아카이브 사용 기준이며 새 실험 착수 지시가 아니다.

<a id="c31"></a>**C31.** 저장 검색11그룹과 기존 findings2그룹, 총13그룹·26개 별칭 경로를 보존 명세에 연결한다. 긴 외부 발췌를 새로 게시하지 않고 출처 좌표·URL·해시와 분류를 제공한다. 서명된 CDN 링크는 공개 목록에서 서명 쿼리를 제거했다. 원본과 보호 상태/예산 파일은 보존하며, 링크의 현재 접속 가능성과 원검색 전체의 팀 접근은 별도로 남긴다.

<a id="c32"></a>**C32.** 이 묶음은 저장 검색의 독해·연결을 마치는 범위다. KBS·GNN·Yoo–Cook2008 및2018/2019 원정리 전체, 아직 확인하지 않은 후보의 방법·코드·실행 자료는 별도 공백이다. 이후76번부터의 기록, 이전 부분 기록, 실패·비용 통합, 대용량 팀 접근, 최종 원본 변경분과 대표 질문 검색 검수도 남는다. H070–H072의 당시 미열람 표시는 역사적 상태로 보존하고 이번 후속 검수로 연결한다.

| 바꾸는 대상 | 저장 검색에서의 예 | 먼저 볼 기록 |
|---|---|---|
| context/sample | credit resampling, instance TSC | [72와 H071](0072-globalization-audit.md) |
| 입력 변수·표현 | GFSM, SPCA, geocif CID | [47 입력 공유](0047-input-sharing-roles.md) |
| 소속·예측 공동학습 | STGNN pooling/lift | [73와 H072](0073-forecastable-output-audit.md) |
| 출력 방향·복원 | ForeCA, response DR, 원74 압축 | [72–75 저장 결과](0072-0075-output-compression.md) |
| 예측값 보정·설명 | COSA, debiasing, SHAP/fippy | [응답별 역할 목록](../evidence/0072-0075-saved-search/response-ledger.json) |
