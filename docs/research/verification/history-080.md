# H080 검수: Task2Vec과 공동 예측의 적용 범위

[기록](../records/0080-task2vec-task-and-output-sharing.md) · [주장 40개](history-080-claims.json) · [작성 후 대조](history-080-second-pass.json) · [출처](../sources/history-080.md)

13개 자료를 먼저 읽고 40개 주장을 작성한 뒤, 같은 에이전트가 관련 원문 위치를 9개 검수 묶음으로 다시 대조했다. 첫 독해는 PDF 16쪽과 명시한 저장 자료 전체이며, 두 번째 검토는 주장에 연결된 구간·수식·표·코드·metadata를 대상으로 한다. 독립 연구자 검토나 모델 실행 재현은 아니다.

task head 적합과 고정 특징, 모델 분포 Fisher와 실제 label gradient, TASK2VEC과 MODEL2VEC, expert 선택과 같은 scalar target pooling을 구분했다. 수치에서는 optimal error와 상대 증가율, corpus 규모와 선택 평가 규모, 정수 표시와 반올림 전 결과, 저자 GPU 비용과 이번 작업 비용을 대조했다.

[표시 결과](../evidence/0080-task2vec/reported-tables.json)의 20개 값은 표 전체와 시각 대조했다. [보충 행렬](../evidence/0080-task2vec/supplement-figure3-matrices.json)은 600dpi 세 영역에서 격자·행열명·숫자·색을 읽은 뒤, 표시 정수 3,500개를 PDF와 대응하는 plain 텍스트 및 개별 셀 추출과 대조해 저장했다. 작성 후 손해 사례와 반올림상 같은 숫자에 서로 다른 expert가 표시된 행도 다시 확인했다. 원시 예측·반올림 전 값·색의 거리값이나 논문 평균의 실행 재현으로 표시하지 않는다.

대조 중 Table 1의 출처를 PDF p8로 바로잡고, 기호 반례에 두 cell의 비중이 같다는 조건을 명시했다. cache의 batch 계산식에는 loader 길이와의 최솟값을 보완했다. 보충 loss의 `−log` 누락만 제시하지 않고 본문에는 `−log`가 있다는 사실도 함께 남겼다. 원문 자체의 Mixed 수량·모델명·수식 차이는 보존했으며 실행 오류로 판정하지 않았다.

[원본 보존](../evidence/0080-task2vec/provenance-check.json), [고정 코드](../evidence/0080-task2vec/static-code-version-check.json), [TXT 대응](../evidence/0080-task2vec/text-variant-correspondence.json), [문서·링크 검사](history-080-document-check.json)를 의미 검수와 별도로 제공한다. 새 독립 본문 5개·전체 JSON 3개·원 PNG 2개를 구분하며 TXT·서지 HTML·재참조 findings를 별도 독립 본문으로 중복 가산하지 않는다. helper/설정 본문, Mixed 수량 차이의 원인, 실행 환경과 실제 seed, 장기 원자료 공유, 원78의 NTKMTL 및 나머지 과거 기록은 미완료다.
