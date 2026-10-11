# DGCformer 저장본과 읽은 범위

[정리 기록](../records/0091-dgcformer-source-review.md) · [목록](../catalog/history-091-sources.jsonl) · [명세](../evidence/0091-dgcformer/manifest.json) · [검수](../verification/history-091.md)

원81의 저장 논문·서지 네 그룹과 동일 바이트 사본 여덟 경로를 확인했다. HTML과 TXT는 서로 다른 파일로 보존한다. 논문 1053행, 서지 109행의 가시 본문이 각 HTML의 대응 추출과 정확히 같음을 확인했고, 추가 metadata·수식 alttext·링크·주석·inline JavaScript도 정적으로 읽었다. 본문 집계에는 HTML 두 개를 추가하고, 대조를 마친 TXT 두 개는 형식이 다른 대응 자료로 연결한다. 외부 PDF 14쪽은 보충 검수 자료이므로 원본 목록의 본문·이미지 집계에는 추가하지 않는다.

| source_id | 원본 파일명 | 팀 접근 | 저장본 SHA256 |
|---|---|---|---|
| `SRC-0062844` | `DGCformer_2405.08440v1.html` | [공식 논문](https://arxiv.org/html/2405.08440v1) | `a9e148b828ecb7118b5111cec5421d16407749b2c488a97516d22f4521545d6b` |
| `SRC-0062845` | `DGCformer_2405.08440v1.txt` | [공식 논문](https://arxiv.org/html/2405.08440v1) | `714ce72c8cc181b8fa7317f0a472b0213145d50dcd10b759a09a7efb33281f8e` |
| `SRC-0062846` | `DGCformer_metadata.html` | [공식 서지](https://arxiv.org/abs/2405.08440v1) | `53c5476fc2c1e6bcf2f2b4b02f16b8ebb03b359972f58a0be73f53015061e77d` |
| `SRC-0062847` | `DGCformer_metadata.txt` | [공식 서지](https://arxiv.org/abs/2405.08440v1) | `0fff7847b1e6e401199acbbb8e23c89acda552d400fd5af7b72d51df5048564d` |

원본 루트 별칭은 `Tab-ICL`이며 상대경로와 snapshot 사본은 목록·보존 검사에서 확인할 수 있다. 공개 주소는 같은 arXiv v1의 연구 내용에 접근하는 경로다. 현재 웹사이트의 화면 구성까지 저장 HTML과 바이트가 같다고 보장하지는 않는다. 논문 HTML·TXT·PDF 전체는 재게시하지 않았다.

## 당시 판단과 변환 방법

- [원81 보고서](../evidence/0090-input-partition/originals/SRC-0022042.md.txt): H090의 정확 보존본을 재사용한다. 이번에는 1–15, 27–39, 85–103행을 다시 확인했다. DGCformer를 설명한 31행의 도로 교통 서술을 후속 정정한다.
- [원 collector](../evidence/0090-input-partition/originals/SRC-0022608.py.txt): 53행 전체를 정적으로 다시 읽었다. 저장 HTML에서 script·style·nav와 MathML 중복을 제외하고 math alttext를 본문에 넣는 변환을 확인했다. 이 collector는 실행하지 않았다.
- [보존 확인](../evidence/0091-dgcformer/provenance-check.json): 새 네 그룹의 여덟 경로와 재사용 원문의 동일 사본을 해시로 대조했다. 보호 원본 여섯 개도 그대로다.

## 그림과 검토 상태

HTML의 연구용 media 참조 14개는 같은 v1 PDF의 그림 1–7과 대응했다. arXiv 로고 여섯 개와 외부 UI script·CSS는 연구 자료로 집계하지 않는다. 외부 JavaScript를 가져오거나 실행하지 않았고, HTML 이미지 파일과 PDF의 바이트 동일성도 검사하지 않았다. [그림별 관찰](../evidence/0091-dgcformer/figure-review.json), [읽은 범위](../evidence/0091-dgcformer/read-scopes.json), [주장별 위치](../verification/history-091-claims.json)를 함께 사용한다.

원81에서 남겼던 29개 연결 그룹 중 이번 대상은 DGCformer 네 개다. 다른 25개 문헌·코드·Git 명세·검색 자료와 snapshot 연혁의 고유 변경분은 후속 범위다. 참고문헌에 연결된 모든 논문을 새로 읽거나 DGCformer를 실행한 것은 아니다.
