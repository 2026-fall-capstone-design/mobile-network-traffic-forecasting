# H097 출처와 저장 범위

[연구기록](../records/0097-input-partition-search-review.md) · [목록](../catalog/history-097-sources.jsonl) · [manifest](../evidence/0097-input-partition-search/manifest.json) · [검수](../verification/history-097.md)

원본 경로는 Tab-ICL 루트 기준 식별자다. 검색 응답 전문은 재게시하지 않는다. 공개 URL은 당시 응답의 출처이며 현재 재접속·동일 내용·팀의 원본 전체 접근을 보장하지 않는다.

## <a id="src-0022042"></a>SRC-0022042

- 원본: `tmp/redesign_20260925/81_input_partition_findings.md`
- SHA-256: `576d1423c967735d913325378883a4f4dae6fa61df155146aaa29c9f1c9c3956`; 13,968 bytes.
- 동일 바이트 별칭: SRC-0001394, SRC-0022042.
- 읽기 범위: H090에서 전체 독해한 원81을 H097 작성 전 103행 전부 재참조. 새 본문 집계 0.

## <a id="src-0062870"></a>SRC-0062870

- 원본: `tmp/redesign_20260925/sources/input_partition_81/web_search_record.json`
- SHA-256: `6e6355d89ecffbfc7531b5c12c1411bf7a14fc3594bd0335f2cd2a274a9dc136`; 225,455 bytes.
- 동일 바이트 별칭: SRC-0001433, SRC-0062870.
- 읽기 범위: 최상위 메타데이터·10질의·8결과 문자열을 전부 읽음. 연결된 외부 문서의 전문을 모두 읽었다는 뜻이 아님.

[보존 원81](../evidence/0090-input-partition/originals/SRC-0022042.md.txt) · [검색 응답 101개 식별](../evidence/0097-input-partition-search/response-index.json) · [문자 위치 규칙](../evidence/0097-input-partition-search/read-scopes.json)

## 저장 open의 실제 범위

| 응답 | 대상 | 보고 총행수 | 저장된 L행 |
|---|---|---:|---|
| H097-R033 | [arxiv.org](https://arxiv.org/html/2412.10859v2) | 539 | L0–179 |
| H097-R034 | [arxiv.org](https://arxiv.org/html/2608.19966v1) | 466 | 없음: 헤더만 저장 |
| H097-R035 | [github.com](https://github.com/decisionintelligence/DUET) | 304 | 없음: 헤더만 저장 |
| H097-R073 | [arxiv.org](https://arxiv.org/html/2405.08440v1) | 405 | 없음: 헤더만 저장 |
| H097-R074 | [arxiv.org](https://arxiv.org/abs/2412.10859) | 169 | L0–168 |
| H097-R075 | [arxiv.org](https://arxiv.org/abs/2405.08440) | 162 | L0–161 |
| H097-R076 | [arxiv.org](https://arxiv.org/abs/2404.01340) | 167 | L0–166 |
| H097-R077 | [arxiv.org](https://arxiv.org/abs/2312.16544) | 158 | L0–84 |
| H097-R078 | [arxiv.org](https://arxiv.org/html/2412.10859v3) | 544 | L171–201 |
| H097-R079 | [arxiv.org](https://arxiv.org/html/2405.08440v1) | 405 | L75–99 |
| H097-R080 | [arxiv.org](https://arxiv.org/html/2404.01340v2) | 708 | L92–127 |
| H097-R081 | [arxiv.org](https://arxiv.org/html/2312.16544v1) | 810 | L83–134 |
| H097-R100 | [cran.r-project.org](https://cran.r-project.org/web/packages/didec/index.html) | 1 | L0: 접근 오류 |
| H097-R101 | [cran.r-project.org](https://cran.r-project.org/web/packages/didec/refman/didec.html) | 1070 | L0–405 |

논문·서지·오류를 구별한다. 세 arXiv 서지 응답의 표시행이 모두 있어도 논문 전문을 읽었다는 뜻은 아니다. 새 전체 JSON 집계는 1이며 원81 재참조, 101개 응답, 93개 URL, 표의 24값은 추가 파일 독해·실험으로 세지 않는다.
