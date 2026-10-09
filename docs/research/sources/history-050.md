# H050 출처와 실제 열람 범위

[종합 기록](../records/0056-0058-compression-synthesis.md) · [manifest](../evidence/0056-0058-compression-synthesis/manifest.json) · [기계 판독 목록](../catalog/history-050-sources.jsonl)

이 묶음은 56/57/58 원문·저장 산술과 다섯 문헌을 종합한다. 새 보존 사본은 수집 script·receipt·tree 2개의 4개 75,531bytes이며, 기존 사본 4개를 재사용한다. manifest는 13묶음 27경로, 별도 저장 폴더 대조는 42묶음 85경로다. 서로 겹치는 범위이므로 둘을 단순 합산하지 않는다.

| source_id | 팀 접근 | 실제 독해·재사용 범위 |
|---|---|---|
| SRC-0022785 | [보존 원문](../evidence/0056-0058-compression-synthesis/originals/SRC-0022785.py.txt) | 수집 script 전체39줄 정적 독해. import/실행 없음. |
| SRC-0064456 | [보존 원문](../evidence/0056-0058-compression-synthesis/originals/SRC-0064456.json) | 2개 repository의 모든 receipt·URL·202 blob 경로를 읽음. 15건의 저장 bytes/SHA 확인;원 수집 script 실행 없음. |
| SRC-0064451 | [보존 원문](../evidence/0056-0058-compression-synthesis/originals/SRC-0064451.json) | H050에서 최상위/각 항목의 모든 키·값·URL까지 독해. tree 응답의 전체 독해이며 연결 repository 전체 독해가 아님. |
| SRC-0064437 | [보존 원문](../evidence/0056-0058-compression-synthesis/originals/SRC-0064437.json) | H050에서 최상위/각 항목의 모든 키·값·URL까지 독해. tree 응답의 전체 독해이며 연결 repository 전체 독해가 아님. |
| SRC-0021848 | [보존 원문](../evidence/0056-0058-compression-synthesis/../0056-0058-mae-sampling/originals/SRC-0021848.md.txt) | H045에서 전체 읽은 계획56/57·판단58 또는57결과의 재사용. 이번 종합에서 해당 주장 재대조. |
| SRC-0021872 | [보존 원문](../evidence/0056-0058-compression-synthesis/../0056-0058-mae-sampling/originals/SRC-0021872.md.txt) | H045에서 전체 읽은 계획56/57·판단58 또는57결과의 재사용. 이번 종합에서 해당 주장 재대조. |
| SRC-0021898 | [보존 원문](../evidence/0056-0058-compression-synthesis/../0056-0058-mae-sampling/originals/SRC-0021898.md.txt) | H045에서 전체 읽은 계획56/57·판단58 또는57결과의 재사용. 이번 종합에서 해당 주장 재대조. |
| SRC-0028241 | [보존 원문](../evidence/0056-0058-compression-synthesis/../0056-0058-mae-sampling/originals/SRC-0028241.json) | H045에서 전체 읽은 계획56/57·판단58 또는57결과의 재사용. 이번 종합에서 해당 주장 재대조. |

두 tree는 H046/H047에서 선택 필드를 읽었던 자료이며, H050에서 모든 키·값·URL까지 읽었다. 전체 JSON +2와 선택 필드 전용 −2로 재분류하며 새 파일 2개를 발견한 것처럼 가산하지 않는다. collector 전체 본문 1개와 code_fetch_log 전체 JSON 1개가 추가된다. 이전 계획·58 판단·57 결과의 재독은 신규 독해로 가산하지 않는다.

## 다섯 주논문과 기존 검수

| source_id | 공식 원문 | 선행 독해 범위 |
|---|---|---|
| SRC-0064458 | [importance_sampling_ICML2018.pdf](https://proceedings.mlr.press/v80/katharopoulos18a/katharopoulos18a.pdf) | [H045의 전체 범위](history-045.md)를 재사용하고 목적·비용 관련 절/표를 재대조 |
| SRC-0064438 | [TimeDC_PVLDB_2024.pdf](https://www.vldb.org/pvldb/vol18/p226-miao.pdf) | [H046의 전체 범위](history-046.md)를 재사용하고 목적·비용 관련 절/표를 재대조 |
| SRC-0064428 | [TabPFN_IML_2403_10923v2.pdf](https://arxiv.org/pdf/2403.10923v2) | [H047의 전체 범위](history-047.md)를 재사용하고 목적·비용 관련 절/표를 재대조 |
| SRC-0064426 | [SCott_ICML2021.pdf](https://proceedings.mlr.press/v139/lu21d/lu21d.pdf) | [H048의 전체 범위](history-048.md)를 재사용하고 목적·비용 관련 절/표를 재대조 |
| SRC-0064453 | [antithetic_1810_03124v1.pdf](https://arxiv.org/pdf/1810.03124v1) | [H049의 전체 범위](history-049.md)를 재사용하고 목적·비용 관련 절/표를 재대조 |

이번 종합에서 importance 논문 §3.1–3.3/Algorithm 1, p3–5, TimeDC §3.1/그림 2와 Table 2–4, p4/10, TabPFN IML §3.4/4.3, p7/10–11, SCott Algorithm 1/Assumption 2/Table 3, p5–7을 다시 대조했다. SCott·SGD-as의 본문/부록·표·수식은 H048/H049의 직접 대조와 현재 종합 문장을 연결한다. 주요 수치와 주장에는 해당 원문 위치를 별도로 남겼다. 같은 논문 재독을 독립 연구로 세지 않는다.

## 저장 폴더 전체의 연결

[42개 파일 범위표](../evidence/0056-0058-compression-synthesis/packet-scope.json)는 각 source_id·SHA·85개 동일 경로·기존 manifest의 시점별 범위와 현재 범위를 보존한다. H045의 hash-only 상태를 덮어쓰지 않고 후속 독해를 연결했다. 같은 PDF의 TXT/preview도 바이트 동일 사본과 구분한 파생물이다.

PDF 5 / TXT 5 / 코드·README 12 / preview 6 / JSON 11 / HTML 3 = 42개다. HTML 3개는 보이는 본문·서지·이력만 읽었으며 raw markup/script/style 전체 독해로 표시하지 않는다. tree의 전체 metadata 독해도 연결된 라이브러리·가중치·모든 논문 본문 확인을 뜻하지 않는다. 원 inventory 밖 연결 자료와 저장 원본의 미열람 부분을 구분한다.

수집 로그의 202개 blob 경로와 15개 receipt는 별도 수치다. 모든 15개 저장 파일의 크기·SHA와 고정 commit URL·선택 순서를 대조했다. 이는 다운로드 기록을 설명하며 코드의 연구 실행을 입증하지 않는다. [수집 검산](../evidence/0056-0058-compression-synthesis/collection-check.json) · [검수](../verification/history-050.md)
