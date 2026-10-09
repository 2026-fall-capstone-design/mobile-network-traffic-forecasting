# H028 검수: 입력 역할과 문헌을 소속 설계에 연결

[47 팀 문서](../records/0047-input-sharing-roles.md)의 주요 주장17개를 원문과 선택 1차 자료에 대조했다. 같은 에이전트의 두 번째 대조이며 독립 연구자의 실험 재현이 아니다. [기계 판독 주장 목록](history-028-claims.json), [출처](../sources/history-028.md)

[1차 근거 검사](history-028-primary-check.json)는93개 확인을 기록한다. 원본23개 identity·보존7개·기존3개·스냅샷 지정 행·접근/렌더로그·GECOS 기존 검수·통제파일6개·표·대수를 포함한다. 논문 Table2의5행34수치를 PDF에서 다시 추출해 직접 열람한 표와 대조했다. [논리/작업량](history-028-logic-check.json)은 unit-noise 정상공분산과 명시한 비교 방식의3행 산술이다. [문서 검사](history-028-document-check.json)는 본문 숫자 행·파일해시·핵심 범위 문구를 확인하며 문장 의미 검수는 원문 재독으로 수행했다.

| 주장 | 확인 내용 | 근거 | 제한 |
|---|---|---|---|
| H028-C01 | 입력 열과 학습 행·구성원 연결과 상대 역할 구분 | 47§1;45계획 | 구체 입력 구현·RCTL 변경 없음 |
| H028-C02 | GECOS 단일 입력 채널과 UPC cell별 sliding sequence | SRC0061693전체;UPC IV.A6–7쪽;pilot005공식identity | 전체 loader/논문 전처리 재현 아님 |
| H028-C03 | DIC22기지국100일·IMF군집·3성분TE/GCN | DIC6–12/14쪽§3–4 | UPC cell partition과 다른 대상 |
| H028-C04 | DIC Table2 세 조건의 RMSE/MAPE | DIC16쪽Table2 | 논문 척도;원출력 재현0 |
| H028-C05 | DIC 방향/비율/값 자체 문턱·이름 차이 | DIC10식11/13;11Algorithm2;14/16비교군명 | abs 연산으로 바꾸지 않음;실행 명세 미해결 |
| H028-C06 | DIC 시간 절단·계산 규모·접근 범위 | DIC11/14/17쪽;47§3 | 누출 확정·전사이트 코드 부재 결론 아님 |
| H028-C07 | Markov v2와3450합성SCM·6회귀기/n1000 | Markov1–3/10쪽;공식arXivmetadata | 실제통신·모든설정일반화 아님 |
| H028-C08 | MSE Bayes충분성의 가정·모집단/추정 구분 | Markov2–3쪽Assumption2.1/Theorem2.2 | RCTL/MAE 보장 아님 |
| H028-C09 | OLS초과위험과누락/추가비용·상위집합충분성 | Markov4–6쪽Prop3.2/5.1/5.2 | n>p+1 등 OLS조건;모든finite learner 아님 |
| H028-C10 | F200GS/HITON의회귀기별Win과복구지표 | Markov6쪽Table2 | Win은task비율;TabICL열없음 |
| H028-C11 | boundary head/co-learning은후속제안 | Markov9–10쪽§7/한계 | 공개 frozenTabICLv2 API기능으로 확정 못함 |
| H028-C12 | 양방향유용성과동일함수공유의비동등성 | 47§4;history028logiccheck | 정상Gaussian/한시점/identityblind;유한표본실험아님 |
| H028-C13 | 예측시점가용정보집합을먼저고정 | 47§4;Markov정적boundary정의 | 미래target후관측을현재입력으로쓰지않음 |
| H028-C14 | N(k+1)특정비교의context/query산술 | 47§5;logiccheckworkload | runtime/보편하한 아님;2N은다른질문 |
| H028-C15 | 당시미추천3이유와재검토조건 | 47§6;H027의46수치검수 | 모든공간입력기각/새최종방향확정 아님 |
| H028-C16 | 보존로그의403/200과429/challenge보고구분 | 47§7;fetch/static/render/scopeJSON | 429와challenge는이로그로별도검증못함 |
| H028-C17 | 실제열람범위·모델0·역사적Goal/예산의지위 | 47전체;3로컬코드;4JSON;manifest/통제baseline | 전논문/패킷/전체Goal 미완료 |

47의 “절대값”은 Algorithm2의 TE 값 자체 문턱과 연결하고 절대값 연산으로 쓰지 않았다. N(k+1)은 특정 개별 후보 비교의 규모로 제한했다. 논문의 표·이론·후속 제안을 구별하고, 현재 checkpoint/API 기능이나 RCTL 성능 보장으로 바꾸지 않았다. 양방향 입력 의존성의 반례에는 innovation과 입력 schema의 가정을 명시했다.

새 학습·추론·forward·원 코드 실행·난수 생성0. 원 논문 출력 재현0. 기존 archive CI로 바이트·목록·링크를 검사하며, 이번 문서 변경을 위해 연구 모델이나 구현을 그대로 반복하는 새 테스트를 추가하지 않았다. 미독해 논문/변환본문·관련보고서·후속75와 전체기록/실패비용/팀접근/최종원본변경/검색QA는 남아 있다.
