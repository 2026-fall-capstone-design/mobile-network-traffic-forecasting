# 639의 출처와 검토 범위

[연구 기록](../records/0639-rctl-bridge.md) · [보존 파일](../evidence/0639/README.md) · [검수](../verification/pilot-002.md)

기준 목록 버전은 `20261008T140216751179Z`다. [전체 출처 목록](../catalog/pilot-002-sources.jsonl)에는 76개 원본 경로와 정확히 같은 사본의 ID, SHA-256, 저장소 경로, 검토 상태가 있다. 원본 루트 아래의 상대경로를 유지하므로 개인 PC 경로 없이 추적할 수 있다. 동일 해시 대표를 보존하는 것이 다른 버전의 검토를 대신하지 않는다.

| 역할 | source_id와 보존 원문 | 실제 확인한 범위 |
|---|---|---|
| 계획·당시 판단 | [SRC-0022006](../evidence/0639/originals/SRC-0022006.md.txt), [SRC-0022005](../evidence/0639/originals/SRC-0022005.md.txt) | 전체 텍스트 |
| 설정 작성·실행·검증 코드 | [SRC-0022532](../evidence/0639/originals/SRC-0022532.py.txt), [SRC-0022526](../evidence/0639/originals/SRC-0022526.py.txt), [SRC-0023257](../evidence/0639/originals/SRC-0023257.py.txt) | 전체 텍스트. 실행하지 않음 |
| 재사용 worker·로컬 모델 | [SRC-0022929](../evidence/0639/originals/SRC-0022929.py.txt), [SRC-0023048](../evidence/0639/originals/SRC-0023048.py.txt) | 전체 텍스트. 원논문 구현 등가성 검증은 아님 |
| 입력 준비의 상위 코드 | [SRC-0023163](../evidence/0639/originals/SRC-0023163.py.txt) | 전체 텍스트. 원자료 재생성은 하지 않음 |
| 결과 수치 | [SRC-0023944](../evidence/0639/originals/SRC-0023944.json) | 모든 JSON 필드·cell/기간별 배열을 구조화 출력으로 확인, 수치 별도 검산 |
| 실행·정산 | [fit](../evidence/0639/originals/SRC-0023938.json), [start](../evidence/0639/originals/SRC-0023947.json), [settled](../evidence/0639/originals/SRC-0023948.json), [process](../evidence/0639/originals/SRC-0023942.json), [supervisor](../evidence/0639/originals/SRC-0023950.json), [review manifest](../evidence/0639/originals/SRC-0023945.json) | 전체 텍스트 |
| 고정 설정·계약·완료 로그 | SRC-0023939, SRC-0022007, SRC-0023946 | 지정 필드·task·재사용 연결·해시 참조 대조. 나머지 내용은 전체 읽기 완료로 세지 않음 |
| 예측·정답 NPZ | manifest의 `.npz` 항목 | 안전한 배열 읽기로 ID·shape·정답·MAE·정확한 재사용 대조 |
| upstream 설정·코드·history | manifest에서 지정 필드 검토로 표시한 항목 | 공통 학습 규약, 실제 cell, 예측 출처, val_mae·epoch·checkpoint, 학습 함수의 해당 부분 |
| 당시 검증 목록 | [SRC-0023952](../evidence/0639/originals/SRC-0023952.json) | 요약과 1,900개 pass 값. 각 검사 설명의 전체 독해는 아님 |

전체 텍스트 확인은 14개 파일이고, 결과 JSON 1개는 전체 필드를 확인했다. 나머지 61개는 지정 필드 검토다. 이 수량을 76개 파일 전체 독해나 76개 연구 기록으로 보고하지 않는다. 정리 에이전트의 검토이며 별도 연구자의 승인을 뜻하지 않는다.

상위 306·325·336·367·388·563·581의 이번 사용 부분을 읽었다는 사실만으로 각 연구 전체를 정리 완료로 처리하지 않는다. 원문에서 이 정리본으로 돌아올 때는 각 출처 행의 `records: ["0639"]`와 이 페이지를 사용한다. 원본 파일 자체는 수정하지 않는다.
