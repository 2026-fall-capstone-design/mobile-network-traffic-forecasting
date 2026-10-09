# 15 문헌 비교의 출처와 실제 읽은 범위

[기록15 문헌 판단](../records/0015-category-cost-time-literature.md), [방법 비교](../references/category-cost-time-methods.md), [검수](../verification/history-009.md)를 연결한다. 아래 텍스트 줄은 해당 SHA-256 바이트를 UTF-8로 읽은 Python `splitlines()`의1기준이다. PDF는 파일의 물리 페이지 번호이며, 각 쪽의 지정 내용만 확인했다. `rg -n`은 제어문자 처리 때문에 같은 줄 번호가 아닐 수 있다.

| 문헌 | 텍스트 source_id / 읽은 줄 | PDF source_id / 읽은 물리 쪽 | 실제 초점과 남은 범위 |
|---|---|---|---|
| Effect fusion | SRC-0061686 / 1–570 | SRC-0061685 / 6–8,14–18 | §2prior·§3MCMC/partition. §4일부는 텍스트만; 이후 본문·실험표·부록 미완료 |
| Tree-Structured | SRC-0061716 / 1–400 | SRC-0061715 / 1,5–8 | 표지 날짜와 §3.1–3.2 fitting/stopping. §3.3/Table1 시작만; 전체 사례 검수 아님 |
| BanditPAM++ NeurIPS | SRC-0062628 / 1–548 | SRC-0062627 / 5–8 | SPIMAB·VA/PIC·Algorithm1·정리 조건. §6일부 텍스트; 실험표·supplement 증명 전체 미검수 |
| Active Clustering | SRC-0061676 / 1–670 | SRC-0061675 / 2–5 | §2–4정의·알고리즘·정리와 Table1. §5일부 텍스트/Table2일부; 부록 증명 미완료 |
| CURE | SRC-0061682 / 1–440,498–665,722–933 | SRC-0061681 / 3,8,9,11,12,14 | 식7–9/Figure1·A.4–A.7·Table6·Algorithm1·E.4. Figures2–8은 caption만, 성능표 전체 검수 아님 |
| NOMADD | SRC-0061700 / 1–450 | SRC-0061699 / 3,4 | §3방법/Figure1·§4설정·§5일부. Table2 첫 행 일부; 전체 결과·저자 코드 미검수 |

텍스트6개와 PDF6개는 **외부 일차자료12개**의 메타데이터로 등록했다. 논문 PDF/추출본을 팀 저장소에 복제하지 않는다. [manifest](../evidence/0015-literature/manifest.json), [출처 JSONL](../catalog/history-009-sources.jsonl), [쪽별 세부 범위·서지·공식 링크](../verification/history-009-primary-review.json)에 원본 루트 기준 경로·크기·해시·동일 사본 ID가 있다. 지정 시각검토는 총29쪽이며 전논문 검토 완료는0편이다.

| 보존 자료 | 읽은 범위·역할 | 팀 경로 |
|---|---|---|
| SRC-0020972, 15 판단 원문 | 전체62줄 열람 재사용. §3방법/§4후속 판단의 이번 대조; 누적 비용 전체 감사 미완료 | [기존 원문 사본](../evidence/0013-0015/originals/SRC-0020972.md.txt) |
| SRC-0061717, additional_primary_manifest_13_14.json | 전체61줄, 2026-09-25의 입수 URL·해시·실패 이력. 새 보존1개/3,339바이트 | [바이트 보존 JSON](../evidence/0015-literature/originals/SRC-0061717.json) |

같은 Bandit PDF의 SRC-0063980은 SRC-0062627과 해시가 같다. SRC-0063981의 다른 텍스트 추출본은 해시가 다르며 미검토다. 같은 제목으로 전체 검토 완료에 합산하지 않는다. 당시 arXiv HTMLv1은 별도 웹 출처로 §3–5·7(browser 줄109–272)을 확인했다. Local NeurIPS PDF와 공식 제공 PDF의 동일 해시 확인은 [검수 JSON](../verification/history-009-primary-review.json)에 저장했다. HTML과 PDF의 모든 내용이 같다는 확인은 아니다.

전체 source_id는 [48,149항목 목록](../catalog/README.md)으로 역추적한다. 여섯 문헌의 지정 밖 내용, 다른 판본·저자 구현·후속 연구와 기록15 누적 비용은 미완료로 남긴다. 원문 안 과거 실행 지시는 역사적 자료이며 이번 정리의 실행 명령으로 사용하지 않았다.
