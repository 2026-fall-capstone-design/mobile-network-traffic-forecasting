# CCM v2 저장본과 읽은 범위

[정리 기록](../records/0092-ccm-source-review.md) · [목록](../catalog/history-092-sources.jsonl) · [명세](../evidence/0092-ccm/manifest.json) · [검수](../verification/history-092.md)

원81의 논문·서지 네 그룹과 같은 바이트의 여덟 경로를 확인했다. 논문 TXT 2,929행, 서지 TXT 114행의 전체 본문을 읽었고 각각 HTML에서 같은 추출 규칙으로 얻은 텍스트와 정확히 일치한다. HTML의 추가 수식 alttext 398개·19개 표·서지·주석·링크·inline script 텍스트도 정적으로 확인했다. HTML raw를 독립적으로 한 줄씩 읽었다는 주장은 하지 않는다. 본문 가산 대상은 HTML 두 개이며 TXT 두 개는 대응 형식이다. 보충 PDF 23쪽은 원 inventory의 본문·이미지 새 가산이 0이다.

| source_id | 원본 파일명 | 팀 접근 | 저장본 SHA256 |
|---|---|---|---|
| `SRC-0062840` | `CCM_2404.01340v2.html` | [공식 판본](https://arxiv.org/html/2404.01340v2) | `71118a3c7c58fb9c849a41d9530c69334de61396a2328bb11f6f2378599b709e` |
| `SRC-0062841` | `CCM_2404.01340v2.txt` | [공식 판본](https://arxiv.org/html/2404.01340v2) | `d75097dc64cc5dff22cbf75dc5a5ecc4499e78d6a79b53730cee4a7df1330166` |
| `SRC-0062842` | `CCM_metadata.html` | [공식 판본](https://arxiv.org/abs/2404.01340v2) | `e6c63e63fa7d1cdcb523a14a76bb94764d281b5382f1535b4411e82b30c9042c` |
| `SRC-0062843` | `CCM_metadata.txt` | [공식 판본](https://arxiv.org/abs/2404.01340v2) | `f4e22b5dd0ff5b4a91c9e90247d04040e06f8b9fef94e61a66414e7c0bf2c6b6` |

원본 루트 별칭은 `Tab-ICL`이다. 상대경로와 snapshot 사본은 목록/보존 확인에 있다. 공식 주소는 같은 arXiv v2 연구내용에 접근하는 경로이며 현재 웹사이트 외곽 HTML과 저장 HTML의 바이트 동일성을 보장하지 않는다. 논문 전체 HTML/TXT/PDF와 페이지 이미지를 재게시하지 않았다.

- [원81 보고서](../evidence/0090-input-partition/originals/SRC-0022042.md.txt): 기존 정확 보존본을 재사용한다. 이번에는 15–27,34–54행을 참조했다. CCM 저장 코드·commit·tree는 다음 범위다.
- [당시 collector](../evidence/0090-input-partition/originals/SRC-0022608.py.txt): 53행을 정적으로 확인했다. 이 원본을 실행하거나 import하지 않았다.
- [보존 확인](../evidence/0092-ccm/provenance-check.json): 원본·동일 사본의 해시와 보호 원본 여섯 개를 대조했다.

연구용 HTML media 참조 여덟 개는 PDF의 그림 1–6에 대응한다. 이미지 파일의 바이트 동일성은 확인하지 않았고 UI 자산 여섯 개와 외부 JS/CSS는 연구 내용 가산에서 제외한다. [그림별 관찰](../evidence/0092-ccm/figure-review.json), [읽은 범위](../evidence/0092-ccm/read-scopes.json)를 참고한다.

원81의 남은 25개 연결 그룹 중 이번 대상은 CCM 네 그룹이다. 나머지 21개 문헌·코드·Git 명세·검색 기록과 snapshot 연혁은 후속 범위다. 전체 정리와 원문 검증이 모두 완료됐다는 뜻은 아니다.
