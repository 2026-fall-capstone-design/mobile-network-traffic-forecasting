# H052 출처와 실제 열람 범위

[팀 기록](../records/0061-history-logic-cost.md) · [manifest](../evidence/0061-history-logic-cost/manifest.json) · [출처 목록](../catalog/history-052-sources.jsonl)

10개 바이트 묶음과 31개 원본 경로를 연결한다. 새 정확 사본은 6개·11,865bytes, 기존 보존본 재사용은 4개다. 코드·메모의 본문 독해와 JSON의 전체 키·항목 독해를 구별하며, 모델 실행이나 과거 스크립트 실행은 하지 않았다.

| source_id | 팀 접근 | 실제 범위·이번 집계 |
|---|---|---|
| SRC-0021961 | [보존 원문](../evidence/0061-history-logic-cost/../0059-0062-history-grouping/originals/SRC-0021961.md.txt) | 전체 텍스트 정적 독해, 1–7줄; 기존 독해·사본 재사용 |
| SRC-0021984 | [보존 원문](../evidence/0061-history-logic-cost/../0059-0062-history-grouping/originals/SRC-0021984.md.txt) | 전체 텍스트 정적 독해, 1–76줄; 기존 독해·사본 재사용 |
| SRC-0022880 | [보존 원문](../evidence/0061-history-logic-cost/originals/SRC-0022880.py.txt) | 전체 텍스트 정적 독해, 1–39줄; 새 본문 |
| SRC-0023215 | [보존 원문](../evidence/0061-history-logic-cost/originals/SRC-0023215.py.txt) | 전체 텍스트 정적 독해, 1–11줄; 새 본문 |
| SRC-0027870 | [보존 원문](../evidence/0061-history-logic-cost/originals/SRC-0027870.json) | 전체 JSON 키·항목, 1–65줄; 새 전체 JSON |
| SRC-0027871 | [보존 원문](../evidence/0061-history-logic-cost/originals/SRC-0027871.json) | 전체 JSON 키·항목, 1–1줄; 새 전체 JSON |
| SRC-0027872 | [보존 원문](../evidence/0061-history-logic-cost/originals/SRC-0027872.json) | 전체 JSON 키·항목, 1–8줄; 새 전체 JSON |
| SRC-0023048 | [보존 원문](../evidence/0061-history-logic-cost/../0639/originals/SRC-0023048.py.txt) | 전체 텍스트 정적 독해, 1–60줄; 기존 독해·사본 재사용 |
| SRC-0027869 | [보존 원문](../evidence/0061-history-logic-cost/../0059-0062-history-grouping/originals/SRC-0027869.json) | 전체 JSON 키·항목, 1–192줄; 기존 독해·사본 재사용 |
| SRC-0000901 | [보존 원문](../evidence/0061-history-logic-cost/originals/SRC-0000901.json) | 전체 JSON 키·항목, 1–193줄; 새 전체 JSON |

61 계획 7줄과 62 보고 76줄은 H051에서 이미 읽었다. 62의 §3·5를 이번 산술·원장 근거와 대조했으나 ALW·horizon 일차자료와 전체 종합까지 완료한 것은 아니다. RCTL port 60줄도 기존 전체 독해를 재사용하고, 채널·층·projection·Dense·고정 bias를 다시 대조했다.

새 본문은 산술 코드 39줄과 회계 코드 11줄이다. 새 전체 JSON은 결과 65줄, 시작 8줄, 종료 1줄, 이후 snapshot 원장 193줄의 네 개다. 직전 원장 SRC-0027869는 H051에서 이미 전체 읽었으므로 다시 가산하지 않는다.

이후 원장 SRC-0000901은 snapshot 14·15, snapshot 16 안의 67 직전 원장, 현재 보존된 67 직전 원장과 바이트가 같다. 정확 사본 네 경로를 source_id로 연결했고, 전후 전체 차이가 61의 cheap 항목 한 번 반영과 같은지 확인했다.

탐색 중 SRC-0024872의 106 직전 원장 전체 299줄도 읽었다. 그러나 74·80·95·97·101 등 후속 연구를 포함하므로 그 단계의 과학적 검수를 이번 완료에 포함하지 않는다. 해당 독해는 별도 대기 기록에 보존하며 H052 새 JSON 수에 가산하지 않았다.

새 계산은 저장된 확률 예와 구조적 비용의 검산이다. 실제 fitted model·가중치·프로파일을 재현하지 않았으며, 모형 가정과 코드 버전을 바꾸면 현재 수치를 그대로 적용할 수 없다.
