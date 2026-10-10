# H077 출처와 읽기 범위

[연구 기록](../records/0077-dynamic-membership-dlm.md) · [출처 목록](../catalog/history-077-sources.jsonl) · [증거 명세](../evidence/0077-dynamic-membership/manifest.json)

원77의 DLM 부분을 보완한다. 2020 arXiv v1 PDF 27쪽, 저장 README·Python 3개, commit/tree JSON 전체를 읽었다. 22개 핵심 주장의 작성 후 원문 대조를 마쳤다. 외부 PDF·라이브러리를 일괄 재게시하지 않고 판본·해시·위치·검토 내용을 연결한다.

| 원문 | 식별자 | 실제 읽기 범위 |
|---|---|---|
| Dynamic Clustering of Time Series Data | SRC-0062029 | PDF1–27쪽의 텍스트·수식·그림·참고문헌·Appendix A |
| dynmix README | SRC-0062038 | 1–10행 |
| dirichlet.py | SRC-0062043 | 1–319행 |
| dlm.py | SRC-0062044 | 1–664행 |
| dynamic.py | SRC-0062045 | 1–277행 |
| 고정 commit 응답 | SRC-0062039 | 전필드와 dynamic.py patch 전체 |
| 고정 tree 응답 | SRC-0062042 | 전필드와19개 항목, truncated=false |
| 원77 findings | SRC-0022032 | H074 독해 재사용,83행 재독해; 새 전체독해 가산 없음 |

저장되지 않은 `common.py`310행과 `independent.py`71행은 [같은 고정 커밋](https://github.com/victhorio/dynmix/tree/bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e)에서 확보했다. 저장 tree의 blob SHA-1과 일치한다. [별도 명세](../evidence/0077-dynamic-membership/external-dependencies.json)에 출처·해시·취득 시각을 남기며 기존 로컬 목록의 완료 수에는 더하지 않는다. source import·설치·모델 실행은 없다.

## 중복과 미완료 범위

해시가 같은 사본은 대표 원문에 연결한다. 이 묶음의 새 고유 본문은 PDF 1개와 README/코드4개, 전체 JSON2개다. 원77 findings와 새 추출 텍스트·렌더 이미지를 별도 독립 원문으로 더하지 않는다.

원77 외부21그룹 중14개는 이번에도 본문 미완료다: Liu·DynaSTar의 PDF/TXT4개, DLM의 저장TXT1개, 원 PNG6개, dynmix PyPI/repository JSON2개, search_outputs JSON1개. DLM의 이번27쪽 렌더 독해가 저장TXT·원PNG의 표현 대응 검사까지 대신하지 않는다. 원77 전체 및 전체 Goal 완료가 아니다.

PDF에서 Link annotation155개 외 주석과 첨부는 없었다. pypdf 회전 텍스트 경고와 Poppler font 경고가 있어27쪽 렌더를 직접 확인했다. 인쇄본의 표기 차이는 원문을 고쳐 쓰지 않고 상세 대조표에 남겼다. [2020 원문](https://arxiv.org/abs/2002.01890v1)
