# H058 출처와 판본 — PLOS copula 군집화

[팀 기록](../records/0064-0065-plos-copula.md) · [명세](../evidence/0064-0065-plos-copula/manifest.json) · [목록](../catalog/history-058-sources.jsonl) · [검수](../verification/history-058.md)

7개 원본 그룹은 14개 물리 경로에 대응한다. 기존64·65 정확 사본 2개를 재사용하고 수집 코드·manifest의 정확 사본 2개(3,586바이트)를 추가했다. 새 로컬 본문은 코드 1개, 전체 JSON은 manifest 1개다. 외부 PDF·TXT·PNG 참조 3개는 같은 논문의 표현이며 독립 문헌이나 실험으로 중복 계산하지 않는다.

| source_id | 팀 접근 경로 | 실제 확인 범위 |
|---|---|---|
| SRC-0022015 | [64_conditional_transform_review_plan.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022015.md.txt) | H055 전체독해 재사용, 이번에도64전체본문과PLOS질문 재대조. 신규본문가산0. |
| SRC-0022016 | [65_residual_and_transform_findings.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022016.md.txt) | H055 전체독해 재사용, 이번에도65전체본문/§4의당시판단 재대조. 다른3문헌·65전체종합미완료. |
| SRC-0022664 | [collect_transform_sources_64.py](../evidence/0064-0065-plos-copula/originals/SRC-0022664.py.txt) | 수집코드 전체33줄 정적독해·AST확인. URL/20MB·5MB/35초/3worker/기존폴더guard·PDFsignature·wrapper·오류기록. 실행/import없음. |
| SRC-0062152 | [manifest.json](../evidence/0064-0065-plos-copula/originals/SRC-0062152.json) | manifest 전체4항목: PLOS/GP-PDF성공,TACTiS-PDF403,arxiv초록저장. 대상전체독해아님. |
| SRC-0062143 | [Copula_clustering_PLOS2018.pdf](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0206753&type=printable) | 22쪽본문·시각·9그림·38참고문헌독해. 공식PDF와바이트동일;인쇄군집43개label과Sim검산. 원실험재현아님. |
| SRC-0062144 | [Copula_clustering_PLOS2018.txt](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0206753&type=printable) | 22쪽wrapper/외곽공백/LF정규화후새PDF추출과문자동일. 독립문헌아님. |
| SRC-0063857 | [Copula_clustering_PLOS2018_p5.png](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0206753&type=printable#page=5) | 원PNG5쪽전체시각독해;Proposition1/전체pairwise/LanceWilliams. PDF파생물이며독립실험아님. |

원 경로·크기·SHA-256과 같은 바이트의 다른 경로는 명세에 보존했다. TXT·PNG의 공식 링크는 내용 출처인 PDF이며 해당 파생 파일의 다운로드 또는 해시 검증 URL이 아니다. 원문64·65의 링크는 H055에서 보존한 정확 사본이다.

## 판본·형식·접근 확인

[판본 확인](../evidence/0064-0065-plos-copula/external-version-check.json)은 2026-10-10 공식 PDF의 HTTP200, 2,331,597바이트 및 SHA-256 일치를 기록한다. 저장 원문의 SHA-256은 `77aa6ab879d9a8b09f0295dcd2d13dabbf8a2ecef8da943d19a2ef641a8b6750`이다. PLOS 발행일은2018-11-12, DOI는10.1371/journal.pone.0206753이다.

PDF22쪽의 텍스트·시각·9그림·38참고문헌을 읽었다. 시각5쪽은 저장 원PNG로도 확인했다. 원TXT22쪽은 page wrapper, 외곽 공백, CRLF→LF를 정규화한 뒤 이번 PDF 추출과 같다. PDF의 깨진 추출 기호는 시각으로 대조했다. 인쇄 국가·주 라벨43개를 전사했으며 plot raw 반복값과 병합높이·silhouette의 정확y값은 복원하지 않았다.

공식 HTML은 서지·링크를, XML은 article-meta, Example2 전체와 MathML M36–40, 인구 Case2 전체, AppendixC 전체 및 첨부 요소 존재를 확인했다. **공식HTML/XML 전체를 읽은 것으로 세지 않았다.** 읽은 landing/XML에서 연구 코드나 보충자료 첨부를 식별하지 못했지만 공개 코드의 전역적 부재를 확인한 것은 아니다. 외부 그림asset의 파일별바이트와 제3자 GDP·인구자료의 현재 접근·버전은 미검증이다. XML 저장 경로의 일시 서명 query는 게시하지 않는다.

수집 manifest4항목에는 PLOS/GP-PDF의 저장 성공, TACTiS OpenReview403, arxiv 초록 저장이 함께 있다. 이 취득 기록을 다른 문헌의 본문 완료로 바꾸지 않는다. GP-Copula·TACTiS-2·conditional normalization와65전체종합은 남아 있다.
