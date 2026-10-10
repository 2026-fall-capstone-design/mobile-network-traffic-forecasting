# 원78 검색·접근 기록과 실제 검토 범위

[출처](../sources/history-082.md) · [검수](../verification/history-082.md) · [근거](../evidence/0082-transferability-access/README.md) · [당시 판단](0076-0079-learning-decisions.md)

원래 기록 번호는 **78**이다. H082는 아카이브 검수 묶음 ID이며 새 실험 번호가 아니다. 저장된 검색 발췌와 직접 접근 로그를 전체 문헌 검수에 연결해, 자료가 있다는 사실과 실제로 확인한 범위를 구분한다.

## 무엇을 확인했는가

<a id="c01"></a>**C01.** 이번 묶음은 원78에 남은 검색 JSON·접근 로그 JSON·빈 HEAD 응답의 3개 그룹과 사본 6개 경로를 확인한다. 두 JSON의 모든 필드와 중첩 문자열을 읽었다. 빈 응답은 읽을 본문이 없어 본문 수에 더하지 않는다. 기존 원78 판단은 재참조하며 새 실험이나 독립 재현은 없다.

<a id="c02"></a>**C02.** 원78 transferability_78 소장 자료 43개 그룹은 H074의 수집·열람 명세 4개, H079 회귀 전이 12개, H080 Task2Vec 13개, H081 NTKMTL 11개와 이번 3개로 연결한다. H074 목록에 등록됐다는 이유로 당시 외부본문 검수를 완료한 것으로 소급하지 않는다. 이 연결은 소장 packet의 범위이며 미소장 의존 파일과 전체 연구기록 완료를 뜻하지 않는다.

<a id="c03"></a>**C03.** 검색 JSON에는 보존 목적을 밝힌 note와 5개 records가 있다. 검색 문자열 3개와 status/value 형태의 접근 결과 2개를 구분한다. fulfilled는 바깥 작업이 결과를 반환했다는 표시이며, 내부 웹페이지가 완전히 열렸거나 모든 논문을 확보했다는 뜻으로 사용하지 않는다.

<a id="c04"></a>**C04.** 저장된 5개 payload는 각각 33,595·25,271·32,407·27,163·14,856문자다. JSON escape를 푼 문자열 기준이며 파일 바이트 수가 아니다. 이 범위를 전부 읽은 것과 발췌가 가리키는 웹페이지·논문 전체를 읽은 것은 구분한다. 예를 들어 UAI PDF의 메타정보는 12쪽·1,202줄이지만 methods_lookup에는 L0–285까지만 남아 있다.

## 검색 결과의 내용과 한계

<a id="c05"></a>**C05.** M3L 자료의 제목은 Exploring Task Affinities through NTK Alignment and Early Training Dynamics in Multi-Task Learning이다. 저장된 VUB 서지는 NeurIPS24의 M3L workshop과 2024-12-14 행사, 2024-12-02 출판 표시를 함께 기록한다. PDF 검색 발췌 하단의 NeurIPS 문구만으로 본회의 논문으로 분류하지 않는다.

<a id="c06"></a>**C06.** 남아 있는 M3L 초록·서론·수식 일부는 초기 학습의 gradient 기반 task affinity를 여러 실행에 걸쳐 평균하고, 합성 데이터의 선형·비선형 관계를 살폈다는 저자 설명이다. 이 발췌로 논문 전체 증명·코드·실험 조건을 검수했다고 하거나 실제 통신 cell의 RCTL 이득을 확인했다고 쓰지 않는다.

<a id="c07"></a>**C07.** 같은 M3L PDF의 검색 발췌가 존재하지만, methods_lookup의 OpenReview forum/PDF 접근은 challenge 주소와 Verifying your browser 화면을 남겼다. 검색 발췌 확보와 해당 접근 시도의 실패는 서로 다른 범위다. 원78도 M3L을 전문 검토 목록에 포함하지 않았다.

<a id="c08"></a>**C08.** PMLR·arXiv·논문 발췌의 12–36% 개선과 최소 27% 속도 향상은 회귀 전이 논문의 초록 수준 저자 요약이며 원78의 새 성능 실험이 아니다. 규제항을 포함한 음의 MSE 설명, head retraining 이론과 fine-tuning 실험의 차이, 표별 반례와 공식 score 구현은 H079의 전체 원문 검수를 함께 확인한다.

<a id="c09"></a>**C09.** task2vec_ntk_lookup 마지막에는 CVF 웹 도구의 Internal Error가 남아 있다. 별도 접근 로그의 CVF 직접 GET은 status200과 5,313바이트 HTML을 저장했다. 둘을 같은 요청의 모순으로 처리하지 않으며, 저장 HTML·논문·코드 검수는 H080으로 연결한다.

<a id="c10"></a>**C10.** access_0의 NTKMTL GitHub 페이지는 메타정보의 271줄 전체가 아니라 L0–52 앞부분만 저장됐다. access_1은 NTK 논문 3쪽 후반부터 6쪽 4.1 도입까지의 기존 추출 출력이다. Eq2–18과 알고리즘 일부의 깨진 수식은 H081의 전체 PDF·그림 검수로 연결하며, 이 발췌를 새 논문 본문이나 별도 실험으로 더하지 않는다.

<a id="c11"></a>**C11.** KDD higher-order task affinities 초록, OT·TaskEmb·Dataset2Vec 및 주변 검색 결과는 관련 후보를 다시 찾기 위한 포인터다. 여기 남은 abstract·snippet만으로 해당 논문 전체를 읽었다거나 같은 연구가 세상에 없다는 결론을 내릴 수 없다. 완전한 검색식·검색 시점별 결과 집합이 없어 체계적 문헌 검색의 완전성을 보증하지 않는다.

## 직접 접근·저장 결과

<a id="c12"></a>**C12.** 접근 로그에는 2026-09-25 20:36:44–47 UTC의 요청 11건이 있다. 세 GitHub 저장소의 repo·commit·tree GET 9건, UAI 보충 PDF의 HEAD 1건, CVF HTML GET 1건이며 당시 status는 모두 200이다. 이는 이 배열의 요청에 대한 기록이고 모든 이전 다운로드와 웹 도구 접근이 성공했다는 뜻이 아니다.

<a id="c13"></a>**C13.** 로그 11건의 bytes·SHA-256을 실제 저장 파일과 대조했고 모두 일치했다. API metadata 9개는 H079/H080/H081의 고정 판본 근거로 연결된다. 이 검사는 파일의 보존을 확인하며 논문 결과의 재현이나 외부 서버의 현재 상태를 검증한 것은 아니다.

<a id="c14"></a>**C14.** UAI 보충자료 HEAD 응답은 application/pdf, Content-Length 8,940,178과 status200을 기록하지만 저장 body는 0바이트다. HEAD 요청이 남긴 본문 없는 응답으로 해석하며 PDF 손상이나 다운로드 실패로 분류하지 않는다. 실제 보충 PDF는 H079의 별도 출처다. 같은 빈 파일 해시가 다른 곳에도 있다는 이유로 다른 연구의 접근 맥락까지 완료 처리하지 않는다.

<a id="c15"></a>**C15.** 검색의 상대적인 게시·크롤링 시각, GitHub star·fork 수와 헤더의 API 잔여량은 저장 당시 정보다. access_1의 wall_time_seconds 0.5760461과 exit_code0은 기존 텍스트 추출 도구의 응답 메타이며 모델 학습 시간·GPU 비용이나 논문 알고리즘의 검증 성공으로 쓰지 않는다.

<a id="c16"></a>**C16.** 기관 성과 목록·ORCID에는 같은 M3L 자료가 반복되고 다른 논문도 함께 등장한다. 특허·문학·TOIT 목차 같은 무관한 검색 내용도 남아 있다. 이를 별도 과제 affinity 근거나 추가 독해 논문으로 세지 않으며, 이웃 항목의 DOI를 M3L에 붙이지 않는다.

## 재사용과 남은 질문

<a id="c17"></a>**C17.** 이 묶음은 검색·접근·보존의 기록 검수다. cell 집합·예측 시간 분할·seed·RCTL 지표는 새 실험의 필드로는 해당 없음이다. 검색에 포함된 README 명령이나 원78의 다음 행동을 실행하지 않았다. 과거 판단·실제 고정 코드·원문 결과를 재사용할 때는 H074와 H079–H081의 적용 범위를 먼저 확인한다.

<a id="c18"></a>**C18.** M3L을 근거로 새 설계를 제안하려면 전문·판본·실제 비교 조건을 추가로 확보해 초기 gradient 정보가 허용되는지와 최종 예측기 독립성을 명시해야 한다. 현재 소장 자료의 연결이 끝나도 미소장 helper·환경·원시 결과, 문헌 안의 표기 차이 원인, 원79 이후와 전체 실패·비용 통합, 장기 팀 접근은 남는다.

## 자료별로 이어 읽기

| 검토 | 자료와 적용 범위 |
|---|---|
| [H074](../verification/history-074.md) | 원76–79 당시 판단·수집 명세, 실행 상태 |
| [H079](0079-regression-transferability.md) | 회귀 전이 점수·head 재적합·저자 표시 결과와 코드 |
| [H080](0080-task2vec-task-and-output-sharing.md) | Task2Vec·Fisher·expert 선택과 같은 출력 공유의 차이 |
| [H081](0081-ntkmtl-training-balance.md) | NTKMTL 학습 중 weighting·고정 코드·부록·비교군 |
| 이 문서 | 남은 검색·접근 JSON과 빈 HEAD 응답, 소장43그룹 연결 |

공식 탐색 위치: [M3L 저장 서지의 논문 링크](https://openreview.net/forum?id=HxT9EuHdXW), [VUB 서지](https://researchportal.vub.be/en/publications/exploring-task-affinities-through-ntk-alignment-and-early-trainin/), [UAI PMLR](https://proceedings.mlr.press/v216/nguyen23a.html), [Task2Vec CVF](https://openaccess.thecvf.com/content_ICCV_2019/html/Achille_Task2Vec_Task_Embedding_for_Meta-Learning_ICCV_2019_paper.html). 이 링크들은 저장 근거의 탐색 주소이며 이번에 원격 재조회한 결과가 아니다.
