# H079 출처: 원78의 회귀 전이 근거

[검토 기록](../records/0079-regression-transferability.md) · [13개 출처 목록](../catalog/history-079-sources.jsonl) · [전체 SHA·사본·독해 범위](../evidence/0079-regression-transferability/manifest.json) · [검수](../verification/history-079.md)

원78의 등록 외부 자료 43개 그룹 중 이번에는 회귀 전이 관련 12개를 검토했다. 당시 findings 1개는 H074에서 검토·보존한 원문을 재참조한다. 파일 번호·원 기록 번호·이번 archive batch 번호를 실험 횟수로 세지 않는다. H074의 기존 목록은 당시 처리 범위를 보존하며, 이번 후속 범위는 H079 목록에서 확인한다.

| Source ID | 자료 | 이번 범위 | 새 독립 본문/JSON 가산 |
|---|---|---|---|
| SRC-0064470 | RegressionTransferability_UAI2023.pdf | 본문 12쪽 text·visual 전체 | 본문 1 |
| SRC-0064471 | 같은 이름 TXT | PDF 12쪽의 layout 추출과 완전 대응 | 0 |
| SRC-0064472 | RegressionTransferability_UAI2023_supp.pdf | 보충 11쪽 text·visual 전체 | 본문 1 |
| SRC-0064473 | 보충 TXT | PDF 11쪽의 plain 추출과 완전 대응 | 0 |
| SRC-0064489 | 공식 README.md | 1–14행 전체 정적 독해 | 본문 1 |
| SRC-0064490 | 공식 reg_score.py | 1–30행 전체 정적 독해 | 본문 1 |
| SRC-0064499 | commit JSON | 전필드·README patch | JSON 1 |
| SRC-0064500 | repository JSON | 전필드 | JSON 1 |
| SRC-0064501 | tree JSON | 전필드·9개 entry, blob/tree 검증 | JSON 1 |
| SRC-0064506 | 원 PNG: main p3 | 저장 이미지 전체 직접 열람 | 이미지 별도 |
| SRC-0064507 | 원 PNG: main p5 | 저장 이미지 전체 직접 열람 | 이미지 별도 |
| SRC-0064508 | 원 PNG: supplement p2 | 저장 이미지 전체 직접 열람 | 이미지 별도 |
| SRC-0022034 | 원78 findings | 1–80행 재참조 | 0 |

논문은 Nguyen 등의 *Simple Transferability Estimation for Regression Tasks*, UAI 2023, PMLR 216:1510–1521이다. [공식 논문·보충자료 페이지](https://proceedings.mlr.press/v216/nguyen23a.html)와 [공식 고정 코드](https://github.com/CuongNN218/regression_transferability/tree/b494b4e56be86229883b039230f708236364b772)를 연결한다. 저장 판본의 상세 상대 경로·크기·SHA·정확 사본 source ID는 manifest에 있다. 외부 파일 전체를 이 저장소에 재게시하지 않았다.

[TXT 대응 결과](../evidence/0079-regression-transferability/text-variant-correspondence.json)는 단순한 비슷함 판정이 아니다. PDF PAGE 표지·CRLF/LF·앞뒤 개행만 제외한 뒤 모든 쪽의 본문 문자열을 대조했다. 그림·수식은 PDF와 원 PNG로 따로 확인했다. 원 PNG 3개와 이번 생성 렌더, TXT·정확 사본을 새 독립 문헌으로 중복 가산하지 않는다.

[코드 판본 검사](../evidence/0079-regression-transferability/static-code-version-check.json)에는 README·score Git blob과 재구성한 Git tree가 저장 commit에 대응한다는 결과를 남겼다. Tree 최상위 sha 필드 차이는 보정하지 않았다. 저장 `requirements.txt`·demo·전체 결과 생성 코드의 내용은 확보되지 않았으므로 실제 논문 실행환경과 재현 성공까지 증명하지 않는다.

정리 중 scikit-learn 1.2.2 공식 API의 [MSE 출력 평균](https://scikit-learn.org/1.2/modules/generated/sklearn.metrics.mean_squared_error.html)과 [Ridge 목적함수](https://scikit-learn.org/1.2/modules/generated/sklearn.linear_model.Ridge.html)를 보조 확인했다. 이는 특정 API 의미에 한정한 새 조회이며, 원78 보존 파일 또는 당시 설치 버전으로 등록하지 않았다. 그 웹 문서 전체를 독립 본문 수에 가산하지도 않는다.

남은 원78 자료에는 Task2Vec·NTKMTL 본문/보충자료·코드·PNG·metadata, 검색·접근 응답 등이 있다. 그중 H074에서 이미 읽은 manifest·read-scope도 있으므로, 이번 밖의 31개를 모두 미독해라고 표시하지 않는다. 이 12개가 완료되어도 원78 전체 packet과 장기 팀 접근은 미완료다.
