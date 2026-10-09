# 39–40 검수 범위

[연구 기록](../records/0039-0040-sample-reuse.md) · [출처](../sources/history-024.md) · [재사용](../evidence/0039-0040-sample-reuse/README.md)

메모 2개·정적 다운로드 코드 1개 전체와 작은 JSON 2개 전체 키를 확인했다. 새 보존 원문 5개, 일차자료 metadata 8개, 해시만 확인한 자료 4개다. 세 논문은 텍스트 22쪽·시각 9쪽, 설치 코드 3개와 metadata는 선택 구간만 읽었다. 전체 논문/전체 일차코드 완료는 0개다.

- [산술·metadata 검사](history-024-portable-check.json) 80개: 유리수 적분과 joint weight, Gaussian 기하평균의 정규화, 비용 정정·입수 기록 대조. 새 성능 실험이 아니다.
- [정적 코드 대조](history-024-code-check.json): 고정 ZIP과 같은 설치 코드의 선택 범위, AST 및 Latin square 크기 귀납. 요청 4가 실제 17순서가 되어 원문 68G를 최대 289G로 정정했다. 실제 forward/실행시간은 미측정이다.
- [잘못된 사본 검사](history-024-negative-check.json) 12건: 입력 질량·MAE·가중치·조건부 ratio·기하평균 정규화·Boolean 수치·68 정정 오류·실측 시간 오표기·모델 호출·코드 해시 연결·중복 JSON을 거부했다. 모델 호출 변경 사본은 해시도 갱신하여 의미 검사까지 도달했다.
- [원본 보존](history-024-source-check.json): 17개 identity·통제파일 6개 불변. 지정 코드의 ZIP 3항목 대조와 외부 파일 metadata 검사는 별도다.

[핵심 주장 16개](history-024-primary-review.json)를 원문 위치에 연결했다. [문서 2차 대조](history-024-document-check.json)는 같은 정리 에이전트의 수동 원문 대조와 자동 수치·링크 확인을 구분한다. 독립 연구자의 재현으로 표시하지 않는다.

Bickel prior 부호, Cherkaoui의 Cantelli 방향·Algorithm1 gate·가정 범위 공백을 보존하고 유효한 손실 항등식까지 기각하지 않았다. 기존 연구의 판단·실행 범위와 정리에서 발견한 비용 정정을 구별했다. 새 모델 실행은 0회다. 41이후·나머지 문헌/코드·전체 실패 비용·팀 접근 검수는 남아 있다.
