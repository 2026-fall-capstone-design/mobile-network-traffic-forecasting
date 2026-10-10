# H080 Task2Vec 근거 묶음

[기록](../../records/0080-task2vec-task-and-output-sharing.md) · [출처](../../sources/history-080.md) · [주장 지도](../../verification/history-080-claims.json)

원78의 Task2Vec 검토를 보완하는 자료다. 논문 결과와 고정 코드를 읽고 정리했으며, 코드 import·실행·새 학습·추론은 하지 않았다. 작성 후 대조 상태는 [검수 문서](../../verification/history-080.md)를 따른다.

| 파일 | 역할과 한계 |
|---|---|
| [manifest](manifest.json) | 새 검토 13개와 기존 판단 재참조 1개의 상대 경로·SHA·사본·실제 독해 범위 |
| [표 1·2](reported-tables.json) | 20개 표시값. optimal error와 상대 오차 증가율을 구분 |
| [보충 그림 3](supplement-figure3-matrices.json) | 50×50·40×25 행렬의 3,500개 표시 정수와 행열명, 빨간 선택·파란 최적 위치 |
| [그림·수식 범위](figure-scope.json) | 본문/보충 그림의 의미, 복구하지 않은 좌표, 표시식의 추가 확인 사항 |
| [고정 코드 판본](static-code-version-check.json) | Git blob 3개와 재구성한 root tree, 본문을 확보하지 못한 의존 파일 |
| [TXT 대응](text-variant-correspondence.json) | main 10쪽 layout·supp 6쪽 plain 추출과 저장 TXT 본문의 정확한 대응 |
| [원본 보존](provenance-check.json) | 26개 사본 경로·보호 원본 6개 hash 확인 |

보충 그림 3은 **배경색의 거리**와 **숫자의 classifier test error**가 다르다. 90개 빨간 선택과 43개 별도 파란 최적 표시를 추출했다. 왼쪽의 같은 task expert를 나타내는 흰 대각선은 선택 평가의 최적값에서 제외한다. 같은 정수로 보이지만 서로 다른 expert가 강조된 행도 있으므로, 반올림 전 순위·정확한 평균·Table 1 재현을 주장하지 않는다. 색으로 표현된 거리 자체의 수치는 확보하지 않았다.

표 1·2의 양수는 optimal 대비 상대 오차 증가율이다. Figure 4에서 고정 optimal expert보다 나은 fine-tuning 결과의 음수와 절대 test error를 섞지 않는다. CUB+iNat와 Mixed의 수량 차이, `ResNet-13` 열 제목, 수식과 설명의 차이는 원문대로 남긴다.

고정 commit은 `c5795e55ba773f9845498091a90eee2fcba5da31`이다. 저장 tree 응답의 최상위 sha에 commit ID가 들어 있으나, 20개 root entry로 재구성한 tree는 commit이 가리키는 `696034e080ba45e2224ff4b05b389b18cc2bd803`과 일치한다. 이 확인은 다운로드한 세 파일의 판본을 뒷받침하며, 전체 논문 실험의 재현을 뜻하지 않는다.

당시 판단은 [원78 보존본](../0076-0079-learning-decisions/originals/SRC-0022034.md.txt)에 있다. 회귀 전이 점수와의 공통 쟁점은 [H079](../../records/0079-regression-transferability.md)로 연결한다. 새 정리에서 발견한 코드·표기 차이를 과거에 실행한 오류나 당시 기각 이유로 바꾸지 않는다.
