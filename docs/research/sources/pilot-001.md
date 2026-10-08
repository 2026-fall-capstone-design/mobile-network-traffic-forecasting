# 시범 묶음 1의 출처

대상은 기존 번호 635–638이다. 정리본은 [635–637의 실행·복구](../records/0635-0637-execution-recovery.md)와 [638의 수치 정정](../records/0638-numeric-precision.md)이다. source_id는 원본의 식별자이며 실험 번호가 아니다.

| 구간 | 계획 원문 | 당시 결과 원문 | 주요 저장 근거 |
|---|---|---|---|
| 635 | [SRC-0021998](../evidence/0635-0638/originals/SRC-0021998.md.txt) | [SRC-0021997](../evidence/0635-0638/originals/SRC-0021997.md.txt) | [오류 trace](../evidence/0635-0638/originals/SRC-0024140.json), [정산](../evidence/0635-0638/originals/SRC-0024137.json) |
| 636 | [SRC-0022000](../evidence/0635-0638/originals/SRC-0022000.md.txt) | [SRC-0021999](../evidence/0635-0638/originals/SRC-0021999.md.txt) | [부분 실행](../evidence/0635-0638/originals/SRC-0024248.json), [정산](../evidence/0635-0638/originals/SRC-0024250.json) |
| 637 | [SRC-0022002](../evidence/0635-0638/originals/SRC-0022002.md.txt) | [SRC-0022001](../evidence/0635-0638/originals/SRC-0022001.md.txt) | [결과](../evidence/0635-0638/originals/SRC-0023965.json), [소속](../evidence/0635-0638/originals/SRC-0023958.json), [검사](../evidence/0635-0638/originals/SRC-0023972.json) |
| 638 | [SRC-0022004](../evidence/0635-0638/originals/SRC-0022004.md.txt) | [SRC-0022003](../evidence/0635-0638/originals/SRC-0022003.md.txt) | [결과](../evidence/0635-0638/originals/SRC-0024153.json), [소속](../evidence/0635-0638/originals/SRC-0024149.json), [검사](../evidence/0635-0638/originals/SRC-0024160.json) |

원래 위치는 원본 `Tab-ICL` 아래 `tmp/redesign_20260925/`이며, 근거 묶음은 개인 PC 경로 없이 접근할 수 있는 저장소 사본이다. [전체 매핑과 해시](../evidence/0635-0638/manifest.json), [검색용 JSONL 목록](../catalog/pilot-001-sources.jsonl).

검토 상태는 구분한다. `human_full_text_review` 30개는 계획·결과·코드·작은 JSON의 전체 텍스트를 확인한 자료다. `settings_review_and_hash_crosscheck` 4개는 설정 필드를 읽고 기록된 원천 해시를 목록의 실제 해시와 대조했다. 나머지 270개는 수치 검수에 쓰인 배열·지원 목록 등의 **지정 필드**를 프로그램으로 대조했으며, 관련 없는 모든 필드의 의미 검토를 완료했다고 세지 않는다.

원문 문서와 코드가 동일한 주장을 담더라도 독립 검증 두 건으로 세지 않는다. 같은 에이전트가 원문을 다시 대조한 검수이며, 독립 연구자의 심사나 새 모델 재현은 수행하지 않았다. [검수 범위와 남은 항목](../verification/pilot-001.md).
