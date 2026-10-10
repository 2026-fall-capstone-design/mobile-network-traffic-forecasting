# H071 출처·판본 — Globalization의 학습 기반 군집화

[팀 기록](../records/0072-globalization-audit.md) · [명세](../evidence/0072-globalization/manifest.json) · [목록](../catalog/history-071-sources.jsonl) · [검수](../verification/history-071.md)

원72–73의 findings와 수집 manifest는 H070의 정확사본2개를 재사용한다. 논문·파생표현11개는 공식 접근 링크와 저장본의 크기·해시·원경로를 연결한다. 합계13개 원본그룹·27개 물리경로를 다시 확인했으며 새 원본 복사는0이다. 과거에 일부 절만 읽었다는 기록과 이번 추가 독해 범위는 구분한다.

| source_id | 팀 접근 | 실제 확인 범위 |
|---|---|---|
| SRC-0022023 | [72–73 findings](../evidence/0072-0075-output-compression/originals/SRC-0022023.md.txt) | 전체52행 재독해. 당시 판단·미실행·부분 독해 범위 |
| SRC-0063077 | [당시 수집 manifest](../evidence/0072-0075-output-compression/originals/SRC-0063077.json) | 전체 JSON의5개 요청·해시·잘린 PDF 실패 |
| SRC-0063074 | [arXiv v1 PDF](https://arxiv.org/pdf/2507.11729v1) | 65쪽 텍스트·시각, 그림22·표5·수식11·의사코드2·서지60항목 |
| SRC-0063075 | [대응 PDF](https://arxiv.org/pdf/2507.11729v1) | TXT65개 페이지 본문이 읽은 PDF 추출문과 `strip` 후 정확히 같음. 독립 원실험이 아님 |
| SRC-0063072 | [정상 판본 접근](https://arxiv.org/pdf/2507.11729v1) | 불완전 PDF6,291,456바이트가 정상 파일의 정확한 앞부분. 별도 완전한 판본으로 세지 않음 |
| SRC-0063073 | [arXiv 서지](https://arxiv.org/abs/2507.11729) | 전체 가시 내용·메타·주석·inline script 정적 독해, 현재 제출 이력 확인 |
| SRC-0063076 | [arXiv HTML](https://arxiv.org/html/2507.11729v1) | 본문 문단146·표5·수식11·의사코드2·캡션29·서지60을 PDF에 대응. 아래 형식별 범위 참고 |
| SRC-0063080–SRC-0063083 | [PDF16쪽](https://arxiv.org/pdf/2507.11729v1#page=16), [18쪽](https://arxiv.org/pdf/2507.11729v1#page=18), [35쪽](https://arxiv.org/pdf/2507.11729v1#page=35), [42쪽](https://arxiv.org/pdf/2507.11729v1#page=42) | 저장 PNG4개 전체 시각과 현재 추출 페이지를 대조 |
| SRC-0063070 | [KBS Crossref](https://api.crossref.org/works/10.1016/j.knosys.2025.113649) | 전체 JSON의 서지·메타·참고문헌61항목. 현재 응답과 바이트 동일 |
| SRC-0063071 | [KBS 관련 arXiv 서지](https://arxiv.org/abs/2305.00473) | 전체 가시 내용·메타·주석·inline script 정적 독해. 출판본 전체 방법 대조는 미완료 |

TXT·PNG·불완전 PDF에 붙인 링크는 대응 논문으로 접근하기 위한 것으로, 그 파생 파일 자체의 다운로드 주소가 아니다. 저장 PDF는7,874,852바이트, SHA-256 `d5da2f19f6bace2f1ff0b6ef612f69d454c6f4e92d5e781a36bc2dc2110998d4`다. 나머지 파일의 해시와 모든 동일사본 경로는 명세·목록에서 찾을 수 있다.

## 판본과 HTML의 범위

2026-10-10 확인한 arXiv 이력은 v1, 제출2025-07-15 20:58:14 UTC다. 서지의63pages·22figures와 저장 PDF65쪽·본문 하단2025-07-17을 구분한다. PDF 앞의 graphical abstract와 highlights를 포함한 파일 페이지로 인용한다. 현재 PDF를 새로 내려받아 동일 해시까지 확인한 것은 아니다.

HTML 문단146개 중94개는 공백·악센트·줄바꿈 등을 정규화하면 PDF 본문에 대응했고,52개는 내용 전체를 따로 읽어 수식 중복·표현·참조 차이를 확인했다. 표390개 숫자 문자열은 PDF에서 전사한 값과 전부 같았다. 캡션29개 중25개·서지60개 중57개는 정규화 대응했고, 부록 접두사와 악센트 등으로 맞지 않은4개 캡션·3개 서지 항목도 읽었다. 수식의 TeX 표현11개와 의사코드2개의 모든 단계를 확인했다.

HTML3개의 메타·head 링크·주석·inline script는 정적으로 읽었다. 모든 raw HTML 태그를 줄별로 독립 독해한 것은 아니며 외부 JS/CSS·연결 그림 픽셀을 별도로 내려받거나 script를 실행하지 않았다. 시각 검수 대상은 저장 PDF 전체와 원PNG4개다. [형식 감사](../evidence/0072-globalization/format-audit.json)에 대응 방식·한계를 남겼다.

## KBS 출판본의 남은 범위

[출판본 DOI](https://doi.org/10.1016/j.knosys.2025.113649)는 Knowledge-Based Systems323(2025),113649에 연결된다. 저장 Crossref JSON23,070바이트와 현재 응답의 SHA-256은 `7ac21beb6df549f4e897c9c109b3a2be460dd0b9a6968f6dc47901c94b85ed29`로 같다. Crossref의 출판 월은2025-07이다.

현재 출판본 서지와 arXiv의 가시 저자·citation 메타는 모두 López-Oriona·Montero-Manso·Vilar의3저자를 나타낸다. 저장 arXiv의 PDF 접근 설명에 있는 “1 other authors”와3저자 메타의 차이는 보존하되, 실제 공동저자 변경을 입증하는 것으로 읽지 않는다. 원72의 저자·판본 차이 메모도 당시 기록으로 남긴다.

[출판사 검색 미리보기](https://www.sciencedirect.com/science/article/pii/S0950705125006951)의 제목·저자·서지·초록 및 section preview 일부를 확인했다. 직접 페이지는403, 공개 API 요청은429였다. 출판본 전체 방법·결과·그림과 preprint의 실질적인 변경을 대조한 상태가 아니다. [접근·판본 검사](../evidence/0072-globalization/external-version-check.json)에 요청 결과와 실제 확인 범위를 구분했다.

이 묶음은 인용논문60편/61편의 본문, 저자의 원예측·전체 코드·모든 seed·실제 비용을 확인한 것이 아니다. 원73의 ForeCA·mbrdr·GNN과72–75 저장 검색자료도 이번 범위에 가산하지 않는다.
