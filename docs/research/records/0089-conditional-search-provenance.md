# 원80 조건부 평균 후보의 검색 근거와 코드 캐시

[출처](../sources/history-089.md) · [검수](../verification/history-089.md) · [근거](../evidence/0089-conditional-search/README.md) · [원80 진단](0088-conditional-graph-diagnostic.md)

원래 연구 기록 번호는 **80**이며 H089는 아카이브 검수 묶음이다. 검색 후보의 적용 조건과 읽은 범위를 원80 진단에 연결한다. 원 연구를 실행하지 않는다. 22개 주장의 작성 후 대조와 출처 검수를 마쳤다.

## 남아 있는 검색 기록

<a id="c01"></a>**C01.** H089는 원80의 문헌 검색 JSON과 CPython 캐시2그룹을 다룬다. 검색 원본68,026바이트와 snapshot22 사본은 SHA-256이 같고, 캐시25,344바이트는 별도 파일이다. 총3경로를 확인했다. 원80 계획·판단·기전·소스는 H088 검수를 재사용한다.

<a id="c02"></a>**C02.** 검색 JSON에는 80_closest_mean_transport와80_probe_literature 두 문자열만 있다. 각각32,654·33,768문자, 합계66,422문자를 모두 읽었다. 제어문자를 구분하는 splitlines의274·272행과 LF만 세는273·226행은 다르다. 근거 위치는 decoded 문자열의0기준 반열린 문자 구간으로 고정한다.

<a id="c03"></a>**C03.** 42개 블록은 모두 search_result 형식이며 대표 URL은 정확 문자열로42종이다. open/find 본문이나 연결된 논문 전문42편을 확보한 기록이 아니다. 저장 응답의 접근 오류 표시는0이지만 각 URL의 현재 접근 성공을 확인한 것은 아니다.

## 문헌 후보와 적용 범위

<a id="c04"></a>**C04.** CLoVE의 두 OpenReview PDF 검색 발췌는 known K의 mixed linear regression, standard Gaussian 입력과 작은 독립 Gaussian 잡음, 제곱손실을 전제로 square-root loss vector를 설명한다. 이는 해당 조건에서의 저자 주장이다. 통신 시계열이나 임의의 비선형 예측기에 대한 일반 보장으로 읽지 않는다.

<a id="c05"></a>**C05.** 두 CLoVE 응답은 URL과 발췌의 논문 행번호가 다르다. 일부 문장이 같아도 원본 PDF 해시 없이 같은 판본으로 합치지 않는다. 과거 under review 표시는 현재 심사 결과가 아니다. 원80의 centered raw-MSE random probe를 CLoVE의 square-root loss vector 알고리즘 재현으로 부르지 않는다.

<a id="c06"></a>**C06.** RCC-PFL 저자 PDF 검색 발췌는 MNIST·Fashion-MNIST·CIFAR-10의 class-independent/dependent label noise와 client 재소속 의사코드 일부를 담았다. HoG 등 label-agnostic feature를 쓰는 구조와 분류 정확도 표는 확인했으나, 이를 통신 회귀 target 잡음에 대한 성능 검증으로 이전하지 않는다. 표 텍스트를 읽은 것은 그림 픽셀 검수가 아니다.

<a id="c07"></a>**C07.** 노이즈 연합학습 survey의 client 선택·가중 설명, Pith의 FedDAA 비판, Moonlight의 coalition 요약, Lacuna의 CBRNet 설명은 각각의 2차 자료로 남긴다. 특히 class별 model-output prototype이 입력 변화와 모델 변화에 의존한다는 FedDAA 비판은 Pith의 주장이다. 여기서 검증한 논문 오류나 공식 심사 결정으로 채택하지 않는다.

<a id="c08"></a>**C08.** LDQ를 이용한 distribution-valued cluster-wise regression은 분포 응답을 함수로 바꾼 회귀다. metric-valued conditional Fréchet mean은 거리 제곱의 조건부 기대값을 최소화하는 대상이다. 두 개념과 scalar 예측값m(x)를 입력x와 짝지은 원80의 graph 분포는 대상·거리·목적을 구별해야 한다.

<a id="c09"></a>**C09.** DQC arXiv2608.25467의 저장 초록은 여러 참 출력 모드 중 최소 오차를 보는 minMSE를 쓴다. 저장 표기 K=5·nx=500에서0.19, oracle0.09, random1.08, mean1.33은 저자의 합성자료 주장이다. 하나의 조건부 평균을 평가하는 MSE와 같지 않으며 TabICL이나 최종 RCTL 결과가 아니다. Prismix 재소개도 독립 재현으로 세지 않는다.

<a id="c10"></a>**C10.** finite mixture regression의 꼬리 연구는 조건부 평균에서 정한 그룹을 고정하는 경우와 quantile마다 달라지는 그룹을 구별한다. mean-shift outlier를 쓰는 robust mixture regression, resolution-wise regression과 quantile mixture도 관련 후보로 남긴다. 검색 발췌만으로 전체 방법·가정·코드·실험을 검수한 것은 아니다.

<a id="c11"></a>**C11.** OTCP/VQR 발췌의 conditional transport map과 mean-independence 제약은 conformal 불확실성 및 분포 표현 맥락이다. coverage와 영역 크기를 통신 예측 오차나 gradient 수렴률로 바꾸지 않는다. 발췌도 conditional map 계산 부담을 언급하며, 반환 제목의 Published in Transactions on Machine Learning Research (04/2026)는 이 논문의 정식 제목 확인을 대신하지 않는다.

<a id="c12"></a>**C12.** NeurIPS2024 PDF 발췌는 추정한 counterfactual mean vector로 hierarchical/density causal clustering을 수행한다. Assumption A1에는 Donsker 조건 또는 같은 크기의 별도 독립 표본으로 만든 추정기를 요구하는 대안이 있다. 원80의 기존 개발 구간을 자동으로 독립 표본이라고 할 수 없다. 인과 식별 조건 전체와 Scribd2405.03083v2의 판본 관계는 추가 확인 대상이다.

<a id="c13"></a>**C13.** cluster별 fixed/random effects와 상관을 고려한 추론, hierarchical shrinkage, O3 시계열의 quantile slope 기반 군집은 서로 다른 질문이다. cluster-robust 추론이나 regression tree 후처리를 최종 예측기를 위한 client partition 선택과 동일하게 취급하지 않는다.

<a id="c14"></a>**C14.** 학회 채택 목록·목차·다운로드 목록과 backdoor 방어, 임상 causal discovery, 금융·volatility·모형 선택, Reddit·Wikipedia 등도 인덱스에 남겼다. 제목에 conditional·mean·clustering이 함께 나오는 것만으로 원80과 같은 방법이라고 묶지 않는다. label noise·privacy noise·concept drift·volatility clustering도 구별한다.

## 검색 자체의 한계

<a id="c15"></a>**C15.** R009·R025 두 응답에는 비표준 제어문자가 섞여 수식이 손상돼 있다. 이를 임의 복원해 정확한 식 검수로 등록하지 않는다. 이미지 설명이 있는 응답1개도 저장된 픽셀은 없다. R027처럼 본문 문단이 반환 제목으로 들어간 경우, 인덱스의 returned_heading을 정식 논문명으로 쓰지 않는다.

<a id="c16"></a>**C16.** 두 필드명은 남아 있지만 실제 검색어 문장·검색 시각별 결과 모집단은 저장되지 않았다. 과거 Published/Crawled 상대 날짜는 현재 날짜나 확정 발표일이 아니다. 후보가 검색되지 않았다는 사실로 같은 연구가 없거나 신규성이 입증됐다고 결론 내릴 수 없다.

## 코드 캐시의 관계

<a id="c17"></a>**C17.** pyc의16바이트 header는 magic cb0d0d0a, flags0, timestamp1790370733, source size12,285를 기록한다. timestamp와 크기는 H088의 원 소스와 일치한다. 검색 JSON의 SHA와 캐시 SHA는 서로 다른 원자료 식별자이며 파생 캐시를 바이트 동일 사본으로 표시하지 않는다.

<a id="c18"></a>**C18.** CPython3.12.13에서 원 소스를 compile만 한 code object와 캐시를 비교했을 때12개 객체의 bytecode·상수·이름·행/예외 표 등 검사 필드가 일치했다. co_filename은 같은 조건의 compile에만 사용했고 공개하지 않는다. 원 소스를 import하거나 exec하지 않았으므로 이 관계는 당시 실행 환경·결과·성능의 재현 증거가 아니다.

## 기존 판단을 재사용하는 방법

<a id="c19"></a>**C19.** H088에서 검수한 원80은16cell의 기존 예측과 두 고정 모델 상태의 저장 gradient 진단이다. TabICL 직접 예측 오차의 이득, input/raw/Tab/Ridge/HGB의 같은 소속, PCC 대비 기간별 gradient 이득의 반전을 함께 보존했다. 이 검색 파일은 새 FedAvg 학습이나 최종 RCTL 성능 향상을 추가로 입증하지 않는다.

<a id="c20"></a>**C20.** 원80의 연결 자료18그룹은 H088의 계획·판단·기전·코드·JSON·NPZ16개와 이번 검색·pyc2개로 추적한다. NPZ는 선택 수치 검수, pyc는 정적 파생 관계이며18개 모두를 새 전문 독해로 세지 않는다. 검색에 언급된 모든 외부 논문·의존 자료를 확보했다는 뜻도 아니다.

<a id="c21"></a>**C21.** 새 후보를 설계할 때 먼저 출력이 scalar mean·분포·다중 모드·인과 평균 중 무엇인지, grouping 단위와 거리, 사용 가능한 입력/target, 독립 표본 및 시간 분할, 최종 예측기와 비용을 명시한다. CLoVE·DQC·OTCP·인과 clustering의 정확한 조건을 확인하고 H088의 반례와 달라지는 점을 적어야 같은 발상을 새 실험처럼 반복하지 않을 수 있다.

<a id="c22"></a>**C22.** H089의 새 내용 가산은 검색 전체JSON1개다. 연결된 논문 전문·그림·새 모델 실행은0이고, 캐시는 이미 검토한 소스의 파생 관계로 처리해 독립 본문·선택 결과로 중복 가산하지 않는다. 원81이후·이전 부분 기록·전체 실패/비용 통합·원자료 장기 팀 접근·최종 원본 변경과 대표 질문 검수는 남는다.

## 다시 찾을 문헌과 근거

아래 링크는 저장 검색에 나타난 주소다. 이 묶음에서 현재 웹페이지를 재조회하지 않았다.

| 대상 | 저장 당시 탐색 주소와 근거 |
|---|---|
| CLoVE | [R001 PDF](https://openreview.net/pdf?id=eZcJZliYws), [R003 PDF](https://openreview.net/pdf/2544b2e42fd71ce2d8d7d251775e0bb24bd52424.pdf) |
| RCC-PFL | [저자 PDF](https://webpages.charlotte.edu/aarafa/icc25.pdf), R002 |
| DQC | [arXiv2608.25467](https://arxiv.org/abs/2608.25467), R021 |
| OTCP/VQR 발췌 | [OpenReview PDF](https://openreview.net/pdf?id=LrXAq63eT7), R023 |
| counterfactual mean clustering | [NeurIPS2024 PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/35f4adf1bfca0a5c99d6c87967282e26-Paper-Conference.pdf), R027 |
| 전체 후보 | [42개 응답 인덱스](../evidence/0089-conditional-search/response-index.json) |
| 원80 실제 검토 범위 | [18그룹 연결](../evidence/0089-conditional-search/packet-coverage.json) |
