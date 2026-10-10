# H080 출처: 원78의 Task2Vec 검토

[검토 기록](../records/0080-task2vec-task-and-output-sharing.md) · [14개 출처 목록](../catalog/history-080-sources.jsonl) · [전체 SHA·사본·범위](../evidence/0080-task2vec/manifest.json) · [검수](../verification/history-080.md)

원78의 등록 외부 자료 43개 그룹 중 Task2Vec 관련 13개를 이번에 검토했다. 기존 findings 1개는 H074에서 보존한 원문을 재참조한다. 이번 밖의 30개에는 H079에서 이미 검토한 회귀 전이 자료와 H074의 기존 검토도 포함되므로 모두 미독해라고 부르지 않는다. 기존 목록은 당시 상태로 남기고 이번 범위를 H080 목록에 덧붙인다.

| Source ID | 자료 | 이번 첫 독해 범위 | 새 독립 본문/JSON 집계 |
|---|---|---|---|
| SRC-0064474 | Task2Vec_ICCV2019.pdf | main 10쪽 text·visual 전체 | 본문 1 |
| SRC-0064475 | main TXT | 10쪽 layout 추출과 정확 대응 | 0 |
| SRC-0064476 | Task2Vec_ICCV2019_supp.pdf | supp 6쪽 text·visual, 작은 행렬 확대 포함 | 본문 1 |
| SRC-0064477 | supp TXT | 6쪽 plain 추출과 정확 대응 | 0 |
| SRC-0064486 | 공식 README.md | 1–96행 전체 정적 독해 | 본문 1 |
| SRC-0064487 | task2vec.py | 1–353행 전체 정적 독해 | 본문 1 |
| SRC-0064488 | task_similarity.py | 1–218행 전체 정적 독해 | 본문 1 |
| SRC-0064495 | commit JSON | 전필드·patch·commit/tree | JSON 1 |
| SRC-0064496 | repository JSON | 전필드·template metadata | JSON 1 |
| SRC-0064497 | tree JSON | 전필드·42개 entry·root tree/blob 대조 | JSON 1 |
| SRC-0064502 | 공식 CVF HTML | 저장 소스·서지·초록·링크 전체 정적 독해 | 독립 논문 본문 추가 0 |
| SRC-0064509 | 원 PNG main p4 | 저장 이미지 전체 직접 열람 | 이미지 별도 |
| SRC-0064510 | 원 PNG supp p1 | 저장 이미지 전체 직접 열람 | 이미지 별도 |
| SRC-0022034 | 원78 findings | 1–80행 재참조 | 0 |

논문은 Achille 등의 *Task2Vec: Task Embedding for Meta-Learning*, ICCV 2019, pp.6430–6439다. [공식 CVF 페이지](https://openaccess.thecvf.com/content_ICCV_2019/html/Achille_Task2Vec_Task_Embedding_for_Meta-Learning_ICCV_2019_paper.html), [본문 PDF](https://openaccess.thecvf.com/content_ICCV_2019/papers/Achille_Task2Vec_Task_Embedding_for_Meta-Learning_ICCV_2019_paper.pdf), [보충 PDF](https://openaccess.thecvf.com/content_ICCV_2019/supplemental/Achille_Task2Vec_Task_Embedding_ICCV_2019_supplemental.pdf), [공식 고정 코드](https://github.com/awslabs/aws-cv-task2vec/tree/c5795e55ba773f9845498091a90eee2fcba5da31)를 연결한다. 원78의 쪽수 표기와 차이는 기록에서 명시하며 보존 원문을 덮어쓰지 않는다.

[TXT 대응 결과](../evidence/0080-task2vec/text-variant-correspondence.json)는 PDF PAGE 표지와 경계 개행만 뺀 본문 비교다. main은 layout, supp는 plain 모드와 대응한다. supp2의 layout 모드에서는 작은 행렬 숫자가 빠져 별도 확대와 plain 텍스트를 사용했다. 두 TXT를 유사하다는 이유만으로 제외하지 않았으며, 실제 대응을 확인한 뒤 독립 본문 중복 집계를 피했다.

코드의 [판본·확보 범위](../evidence/0080-task2vec/static-code-version-check.json)를 함께 확인한다. 원78에 보존된 것은 README와 Python 2개이며, tree에 적힌 helper·configuration·데이터셋 구현의 본문까지 확보한 상태는 아니다. 공식 링크와 hash는 입수·판본 확인에 쓸 수 있지만 장기 팀 보존이나 현재 환경의 실행 재현 완료를 뜻하지 않는다.
