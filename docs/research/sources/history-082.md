# H082 출처: 원78 검색·접근 기록

[기록](../records/0082-search-and-access-provenance.md) · [4개 출처 목록](../catalog/history-082-sources.jsonl) · [소장 packet 연결](../evidence/0082-transferability-access/packet-coverage.json) · [보존 검사](../evidence/0082-transferability-access/provenance-check.json)

원본 루트 별칭은 `Tab-ICL`이다. 경로는 루트 기준 상대경로로 보존하며 팀용 문서는 개인 PC의 클릭 경로에 의존하지 않는다.

| source_id | transferability_78 아래 위치 | 바이트 | 실제 검토 단위 |
|---|---|---:|---|
| `SRC-0064482` | `web_results.json` | 140,774 | 전체 JSON/중첩값 독해 |
| `SRC-0064494` | `metadata/access_log.json` | 22,600 | 전체 JSON/중첩값 독해 |
| `SRC-0064498` | `metadata/regression_supp_head.bin` | 0 | 본문 없음·HEAD metadata 대조 |

세 그룹은 snapshot21 사본과 원본을 연결한 6개 경로다. 원78 판단 `SRC-0022034`의1–80행은 기존 [보존 사본](../evidence/0076-0079-learning-decisions/originals/SRC-0022034.md.txt)과 [H074 검수](../verification/history-074.md)를 재참조한다. 새 독립 본문 가산은0, 전체 JSON은2, 이미지와 새 모델 실행은0이다. 빈 파일과 검색에 등장하는 미확보 논문은 본문 수에 추가하지 않는다.

검색 payload 전부를 읽어도 원격 페이지 전체 저장을 뜻하지 않는다. 출력 끝이 잘렸거나 challenge·Internal Error가 포함된 구간은 [범위표](../evidence/0082-transferability-access/search-record-scopes.json)에 남겼다. URL은 당시 근거의 탐색 주소이고 현재 접근 성공을 주장하지 않는다. 외부 원자료의 장기 팀 공유는 아직 별도 과제다.
