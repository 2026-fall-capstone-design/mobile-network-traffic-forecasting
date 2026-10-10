# 원79 검색 이력과 확인한 문헌의 범위

[출처](../sources/history-087.md) · [검수](../verification/history-087.md) · [근거](../evidence/0087-distributed-search/README.md) · [당시 판단](0076-0079-learning-decisions.md)

원래 연구 기록 번호는 **79**이며 H087은 아카이브 검수 묶음이다. 팀원이 후보를 다시 찾고 기존 판단을 확인할 수 있도록 검색 흔적을 전문·코드 검수와 연결한다. 새 실험은 없다. 전체 첫 독해와 핵심20개 주장의 작성 후 대조를 마쳤다.

## 저장된 내용과 접근 결과

<a id="c01"></a>**C01.** H087은 원79의 web_results.json 한 그룹을 다룬다. 원본262,261바이트와 snapshot22 사본의 SHA-256이 같으며 두 경로를 확인했다. 9개 응답의 모든 문자열을 읽었고 원79 판단51행을 재참조했다. 검색 파일 전체 독해를 연결된 논문 전체 독해로 바꾸지 않는다.

<a id="c02"></a>**C02.** 최상위 필드는 문자열7개와 status/value 객체2개다. JSON escape를 푼 본문은 합계252,361문자이며 파일 바이트 수와 다르다. 두 객체의 status는 fulfilled이지만 내부 내용의 접근 성공 여부는 별도로 판단한다.

<a id="c03"></a>**C03.** 저장된 구분자를 기준으로137개 응답 블록을 식별했다. 검색 결과118개, open12개, find7개이며 응답마다 붙은 대표 URL을 정확 문자열로 세면121종이다. 같은 논문의 abs·HTML·PDF, 반복 검색과 다른 판본이 섞여 있으므로121편의 독립 논문이나137건의 연구 성과로 세지 않는다.

<a id="c04"></a>**C04.** 본문 행이 없는 open 응답은4개다. FMCL HTML528행, EMD-CFL HTML782행, Toso abs161행과 HTML872행이라는 전체 페이지 표시는 남아 있지만 이 네 응답에는 L행 본문이 없다. full_methods라는 필드 이름도 전문 확보의 근거가 아니다.

<a id="c05"></a>**C05.** 접근 오류3개는 FedCAP 출판사 HTML의429, EMD-CFL PDF의400(응답16,010,450바이트가 도구 허용 크기를 넘었다는 메시지), FedCAP PDF의 웹 도구 접근 불가다. 마지막 두 오류는 fulfilled 객체 안에 있다. 원79의 별도 PDF406·15MB 수집 상한 기록과 이 웹 도구 오류를 같은 요청으로 합치지 않는다. 이후 H084에서 PDF를 확보했다고 과거 실패를 지우지 않는다.

## 문헌별로 실제 확인한 범위

<a id="c06"></a>**C06.** 여기서 통신 예측 대안은 Parameter-Efficient Personalized Federated Learning for Accurate Cellular Traffic Prediction, DOI10.3390/telecom7040104다. 원79는 학술지명을 IoT에서 Telecom7(4),104로 정정했다. 검색에는 2024년의 다른 FedCAP: Robust Federated Learning via Customized Aggregation and Personalization도 나오므로 약칭만으로 같은 논문으로 묶지 않는다.

<a id="c07"></a>**C07.** 출판사 검색 발췌는 training-only 일별 profile K-means→cluster별 LSTM FedAvg→고정 backbone 뒤 client별 residual adapter의 순서를 설명한다. adapter4241개·backbone/head68483개와6.19%는 학습 parameter 비교이며, 업데이트 전송0은 마지막 개인화 단계의 설명이다. cluster backbone 학습의 통신 비용까지0이라고 읽지 않는다.

<a id="c08"></a>**C08.** seed42의11방법·4데이터셋 비교와5개 shared seed의 개선율·paired t/Wilcoxon 설명은 저장 검색 발췌의 저자 주장이다. 원실험 재현이나 전문 검증으로 등록하지 않는다. notes 검색에는2026-08-12 원본 HTML/PDF와09-04 HTML 갱신이 함께 남아 있어 검색 발췌·PDF·이후 웹페이지를 자동으로 동일 판본으로 단정하지 않는다.

<a id="c09"></a>**C09.** CoLEDS의 Springer open은 전체785행 중 L0–103만 담았다. 무라벨 dataset profile을 위한 client 간 contrastive 목적과 server의 loss/gradient 조정, server 학습 parameter 없음이라는 서론 설명을 확인했다. 이 발췌만으로 방법·실험 전체와 비용을 검수했다고 하지 않는다.

<a id="c10"></a>**C10.** OCFL 관련 검색에는 arXiv2503.04231과2509.01587의 서로 다른 식별자가 있다. 제목·저자가 겹치지만 초록의30여 과제·3데이터셋과40여 과제·5데이터셋 설명도 다르다. 판본 관계를 추가 확인하기 전까지 같은 파일의 중복으로 합치지 않는다.

<a id="c11"></a>**C11.** FMCL abs 페이지는 서지·초록이며 Method find는 떨어진 행들, complexity find는 L415의 visual complexity 한 행을 반환한다. 이 검색어가 맞았다는 사실로 연산 복잡도 분석을 확인했다고 쓰지 않는다. 실제 PDF16쪽·그림·방법·표 검수는 H083으로 연결한다.

<a id="c12"></a>**C12.** EMD-CFL의 가장 긴 open도 L0–238이며 해당 페이지의 총782행 중 일부다. 별도 find에는 이론·의사코드 일부가 반복된다. 논문의 기대 gradient 식과 parameter 상한, pair별 one-shot 설명은 H084 전체 논문과 H085 고정 코드의 적용 범위를 함께 확인한다. 발췌를 코드 실행·일반적인 서로소 partition 검증으로 세지 않는다.

<a id="c13"></a>**C13.** Toso의 find는 regression model 주변의 불연속 행들과 B.8 말미와 nonlinear 부록 도입 L658–663을 반환한다. 전체 proof를 담은 응답이 아니다. 원79 당시 선택 독해, 이번 H086의 저장 HTML 전체 대조, 독립적인 증명 검증은 서로 다른 범위로 기록한다.

## 조건부 평균 후보를 뒷받침하는가

<a id="c14"></a>**C14.** joint_mean_search에 나온 OTDD 설명은 class별 P(X|Y=y)를 이용한 label 거리와 feature-label 운송비용을 다룬다. 이를 회귀의 P(Y|X) 또는 조건부 평균 m(x) 비교와 동일하게 읽지 않는다. OTCE·회귀 전이·sliced OTDD 등은 후속 원문 확인용 후보이며 저장 검색만으로 TabICL–RCTL 관계의 보장이 성립하지 않는다.

<a id="c15"></a>**C15.** CLoVE의 ICLR2026 심사본 검색 발췌는 known K, Gaussian 입력·작은 독립 잡음, 분리된 단위 norm의 참 parameter, round마다 새 iid 자료를 쓰는 mixed linear regression을 전제로 한다. square-root loss vector와 cluster–model matching 설명은 이 조건에서의 저자 주장이다. 원79는 verification 때문에 전문 미확인으로 남겼으며 통신 시계열 일반 보장으로 가져오지 않았다.

<a id="c16"></a>**C16.** gradient partitioning, RCC-PFL, Fielding, LatentFed 등은 다시 찾을 수 있는 후보로 남긴다. label noise·Byzantine 공격·무선 전송 잡음·concept drift는 서로 다른 문제다. 목록형 저장소·특허·Wikipedia·Reddit·무관한 검색 결과와 표/그림의 텍스트 발췌를 새로운 실험·시각 검수·원문의 부재 증명으로 세지 않는다.

## 과거 판단과 후속 작업

<a id="c17"></a>**C17.** 원79의 후보는 관측 입력x와 TabICL이 추정한 조건부 평균m(x)의 쌍 분포를 비교하는 것이다. 고정 함수와 미분·기대값 교환 조건 아래 제곱손실의 기대 gradient 관계를 서술했으며, 유한 batch SGD 분산·학습 경로·최종 test 성능이 같다고 하지 않았다. 이는 검색 결과의 성능 수치가 아니라 당시의 후보 논리이며 새 수치 검증은0이다.

<a id="c18"></a>**C18.** 9개 필드명과 open/find 인자는 남아 있지만 완전한 검색어·검색 시점별 결과 모집단은 없다. 상대 게시·크롤링 날짜를 현재 날짜나 확정 발표일로 바꾸지 않는다. 결과가 반복되거나 후보가 검색되지 않았다는 이유로 연구 중복이 없다고 보증할 수 없다.

<a id="c19"></a>**C19.** 원79 distributed_clustering_79의 소장21그룹은 H074 명세·서지4, H083 FMCL5, H084 EMD 논문2, H085 구현7, H086 Toso2, H087 검색1로 연결한다. 이전 문서에서 남겨 둔 검색1개는 이번 검수로 보완하지만, 미소장 논문·의존 코드·원시 결과와 전체 Goal 완료는 별개다.

<a id="c20"></a>**C20.** 같은 연구를 다시 제안할 때는 해당 문헌의 식별자·실제 읽은 범위와 과거 채택/보류 이유를 먼저 찾는다. 새 설계에는 사용 가능한 입력·target 정보, 최종 RCTL과의 독립성, 시간 분할과 총비용의 차이를 명시해야 한다. 원79는 원80에서 기존16cell 출력을 쓰는 사후 gradient 확인을 계획했을 뿐 이 기록에서 실행하지 않았다. 원80 결과·81이후·이전 부분 기록·실패/비용 통합·장기 팀 접근은 계속 검수한다.

## 다음에 찾아볼 위치

| 대상 | 확인 위치 |
|---|---|
| 원79 판단·FedCAP 서지 정정·실행0 | [H074](../verification/history-074.md) |
| FMCL 전체 논문·그림 | [H083](0083-fmcl-client-clustering.md) |
| EMD-CFL 논문 / 공식 코드 | [H084](0084-emd-cfl-embedding-distributions.md) / [H085](0085-emd-cfl-code.md) |
| Toso 회귀 이론·가정·표기 | [H086](0086-toso-gradient-heterogeneity.md) |
| 검색 후보의 정확한 URL·반환 구간 | [137개 응답 인덱스](../evidence/0087-distributed-search/response-index.json) |
| 원79 소장 파일별 검수 문서 | [21그룹 연결](../evidence/0087-distributed-search/packet-coverage.json) |

응답 인덱스의 URL은 저장 당시 탐색 주소이며 현재 접근 성공을 보증하지 않는다. 원 검색 본문을 재게시하지 않고 source_id·해시·필드·문자 구간으로 추적한다.
