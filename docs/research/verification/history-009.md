# history-009: 15의 여섯 문헌 방법과 적용 범위 검수

[기록](../records/0015-category-cost-time-literature.md)·[방법 비교](../references/category-cost-time-methods.md)·[출처 범위](../sources/history-009.md)·[manifest](../evidence/0015-literature/manifest.json)를 함께 읽는다. 대상은15§3의 여섯 방법과 §4의 당시 판단이다. 텍스트6개 지정 구간, PDF6개 중 지정 내용29쪽, 논문 보고표6행을 대조했다. 전논문 완료는0편이며 기록15 전체 통합도 미완료다.

## 확인한 근거와 해석

[일차자료 대조 JSON](history-009-primary-review.json)에11개 주장의 source_id·위치·적용 한계를 저장했다. 같은 아카이브 에이전트가 작성 후 원문과 다시 대조했으며 독립 연구자의 과학적 검증으로 표현하지 않는다.

| 검수 대상 | 결과와 범위 |
|---|---|
| 범주 효과 | Effect 식(2.1)–(2.6)·MCMC·최종 두 partition을 구분. Tree의 전 자료/전 계수 재적합, split 선택과 CV/p-value 중단을 구분 |
| 계산 절약 | Bandit VA/PIC의 공유 거리와 sub-Gaussian/gap/T/c(k) 조건, PAM local 해. Active TC·독립 오염·balance·최소 cluster 크기를 유지 |
| 시간 context | CURE의 예측 시 entropy·label 관측 후 갱신·warm fill·centroid fallback 및 정보량 가정. NOMADD의 공통 좌표·각 forward-validation의 earlier-only 재구성 |
| 수치 | Active Table1 네 행의 counts/인쇄 비율 및 CURE Table6 두 행을 텍스트·PDF와 대조. 비율·구성 합·차이는 별도 결정적 산술 |
| 원문 공백 | Bandit 식/알고리즘, NOMADD SVD 좌표/tree 표현, Active 비율 불일치를4항목으로 보존. 저자 코드 확인이나 임의 수정 없음 |
| 서지·접근 | Tree의2015 arXiv/2018 typeset 구분. Bandit HTML/PDF 정리 번호 및 해시 다른 추출본 구분. 공식 PDF와 로컬 PDF 해시 일치 확인 |
| 원본 보존 | 입수 기록1개3,339바이트 새 보존·15원문 재사용. source control6개 보존. 논문 원문은 공식 링크만 제공 |

[문서 검사 결과](history-009-document-check.json)는 원본·목록·보존 해시, 동일 사본 관계, 읽기 범위 경계, 주장 출처 등록, 표의 전사와 Markdown 수치, 정리 파일 해시를 확인한다. 줄/페이지 범위가 유효하다는 자동 검사만으로 실제 열람·해석 정확성을 증명하지 않는다. CI의 공통 archive integrity는 보존 바이트·목록 매핑·로컬 파일 링크만 확인하며 공식 사이트 접근·외부 원문 의미를 다시 검증하지 않는다.

## 미완료와 재사용 조건

지정 밖 본문·그림·표·부록·전체 증명, 다른 판본 및 저자 구현은 남아 있다. 기록15 이후 시간 유효성·회귀 TabPFN의 이력과 누적39context/23,424query/RCTL29 전체 감사도 남는다. 이 묶음의 문헌 대조를15전체·전체 연구기록·신규성 전수 검토 완료로 세지 않는다.

당시 새 후보를 추천하지 않았다는 사실과 미래의 개선 가능성을 구분한다. 새 실험 전 [문제별 색인](../prior-attempts.md)에서 같은 정보·목적·분할·계산 조건인지 확인하고, 달라지는 결정과 재사용할 결과를 명시한다. 이번 정리의 모델 실행·난수 simulation·원 연구 코드 실행은 모두0이다.
