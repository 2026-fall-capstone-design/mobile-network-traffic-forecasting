# H078 출처와 읽기 범위

[연구 기록](../records/0078-dynamic-graphs-load-balancing.md) · [22개 자료 그룹](../catalog/history-078-sources.jsonl) · [증거 명세](../evidence/0078-dynamic-graphs-load-balancing/manifest.json)

H077에서 남긴 원77의 외부 자료 14개를 검토했고, 36개 주장의 작성 후 원문 대조를 마쳤다. 아래의 범위는 저장된 특정 판본에 대한 것이며 검색에 등장한 모든 문헌을 읽었다는 뜻은 아니다.

| 원문 | 식별자 | 읽거나 대조한 범위 |
|---|---|---|
| [Liu 논문 PDF](https://bimsa.net/doc/publication/3963.pdf) | SRC-0062025 | 1–16쪽 전체 텍스트·수식·표·그림·참고문헌 |
| [DynaSTar 논문 PDF](https://www.ijcai.org/proceedings/2026/0296.pdf) | SRC-0062027 | 1–9쪽 전체, 인쇄2662–2670; Eq.16 확대 확인 |
| Liu 저장 TXT | SRC-0062026 | 16쪽의 layout text와 전쪽 대응 |
| DynaSTar 저장 TXT | SRC-0062028 | 9쪽의 layout text와 전쪽 대응 |
| DLM 저장 TXT | SRC-0062030 | H077에서 읽은 27쪽의 layout text와 전쪽 대응 |
| Liu 저장 PNG | SRC-0062046 / 0062047 | PDF 4/9쪽의 저장 그림 전체 직접 열람 |
| DynaSTar 저장 PNG | SRC-0062048 / 0062049 | PDF 3/7쪽의 저장 그림 전체 직접 열람 |
| DLM 저장 PNG | SRC-0062050 / 0062051 | PDF 10/11쪽의 저장 그림 전체 직접 열람 |
| dynmix PyPI 응답 | SRC-0062031 | info, 7개 release 파일, urls 등 전필드 |
| dynmix repository 응답 | SRC-0062032 | 소유자·URL template·상태·license 등 전필드 |
| 검색 응답 | SRC-0062037 | 11개 key/value와 내부 문자열·중첩 결과 전체 |
| 원77 findings | SRC-0022032 | 기존 83행 독해 재사용, 관련 판단을 다시 대조 |

같은 SHA-256의 사본은 대표 ID와 연결한다. 식별 정보·해시·원래 경로는 출처 목록에 남긴다. 외부 논문과 저장 검색 응답 전체를 저장소에 재게시하지 않는다.

## TXT와 PNG를 처리한 방법

TXT 3개에는 `PDF PAGE` 표지가 있고 총 52쪽의 추출문이 들어 있다. 해당 PDF에서 같은 layout 방식으로 다시 추출한 각 쪽과 비교했다. CRLF/LF, 끝 개행, 쪽 표지 외에는 본문 문자와 순서가 일치한다. [쪽별 대응 검사](../evidence/0078-dynamic-graphs-load-balancing/text-variant-correspondence.json)

이 검사는 문서의 의미를 추정해서 중복으로 지운 것이 아니다. 먼저 PDF의 텍스트와 이미지를 직접 읽고, 저장 TXT의 추가·누락·변경 내용을 전쪽 비교한 것이다. 회전 글자나 그림 내부 정보는 TXT만으로 보장되지 않으므로 PDF의 시각 검토를 유지한다. PNG 6개도 새 렌더와 이름만 맞춘 것으로 완료하지 않고 원래 파일을 각각 열었다.

Liu PDF의 annotation은 Link 384개, DynaSTar는 Link 64개였고 비링크 주석과 내장 첨부는 없었다. 두 논문에서 재현 코드·원시 run·미공개 데이터가 PDF 내부 첨부로 제공되지는 않았다.

## 집계와 남은 범위

이번에 독립 본문으로 새로 읽은 PDF는 2개이고 전체 JSON은 3개다. TXT 3개의 형식 대응과 PNG 6개의 열람은 별도로 기록하며, 이미 읽은 논문 내용을 새 연구 결과로 중복 가산하지 않는다. H077의 외부7개 및 원77 findings는 재참조다. 그 결과 등록된 원77 외부21개 그룹의 저장 내용은 모두 다루지만 **연관된 모든 논문의 전문·코드·실행 결과**가 확보되었다는 뜻은 아니다.

남은 대표 공백은 2025 DLM 저널 전문, Fuzzy 문헌의 방법·결과 전체, FedCAP 전문/코드, 두 예측 논문의 실제 실험 코드·환경·원시 결과, 원78–79의 다른 외부 자료, 원80 결과와 이후 기록이다. 공식 링크가 있다는 사실과 같은 바이트 원문의 장기 팀 접근도 구분한다.
