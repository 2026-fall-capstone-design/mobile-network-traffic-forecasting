# H063 출처·판본 — MMR

[팀 기록](../records/0066-0068-mmr.md) · [명세](../evidence/0066-0068-mmr/manifest.json) · [목록](../catalog/history-063-sources.jsonl) · [검수](../verification/history-063.md)

7원본그룹·14물리경로를 연결한다. 원66·68의 기존 정확사본2개를 재사용하고, PDF/TXT/HTML/PNG2개는 공식 판본 접근 링크를 둔다. 새 원본 복사와 로컬 전체본문/전체JSON 가산은0이다. 같은 논문의 표현5개를 연구5건으로 세지 않는다. H062의 당시 미독해 manifest는 과거 검수 snapshot으로 보존하며 현재 범위는 이 H063이 갱신한다.

| source_id | 팀 접근 | 실제 확인 범위 |
|---|---|---|
| SRC-0022017 | [66_group_protection_review_plan.md](../evidence/0063-0068-synthesis-risk/originals/SRC-0022017.md.txt) | 전체 원66 계획34행 재대조. H062 정확사본/전체독해 재사용. |
| SRC-0022019 | [68_group_protection_findings.md](../evidence/0063-0068-synthesis-risk/originals/SRC-0022019.md.txt) | 전체 원68 판단91행 재대조. 당시 선택검토와 이번 MMR 본문검수를 구분. H062 정확사본/전체독해 재사용. |
| SRC-0062709 | [MMR_2405.01709v2.pdf](https://arxiv.org/pdf/2405.01709v2) | 35쪽 전체 텍스트와 시각·6그림·2표·알고리즘1·40서지항목. 공식v2 PDF 바이트동일. supplement 증명과 원실험 미검증. |
| SRC-0062710 | [MMR_2405.01709v2.txt](https://arxiv.org/pdf/2405.01709v2) | 전체1791행 정적독해. PDF page wrapper/whitespace 제거 후35쪽의 새 pypdf 추출과 모두 일치. 수식 기호 정정 없음. |
| SRC-0062711 | [MMR_abs.html](https://arxiv.org/abs/2405.01709v2) | 전체627행 raw HTML 정적독해. 서지·초록·이력·링크와 site markup 포함. script실행/외부embed 로딩 없음. |
| SRC-0062726 | [MMR_2405.01709v2_p11.png](https://arxiv.org/pdf/2405.01709v2#page=11) | 원PNG11쪽 전체시각. Algorithm1·매끄러움/강한볼록성 조건. PDF의 파생물. |
| SRC-0062727 | [MMR_2405.01709v2_p5.png](https://arxiv.org/pdf/2405.01709v2#page=5) | 원PNG5쪽 전체시각. 계층모형/시험support·regret 정의. PDF의 파생물. |

## 공식 판본

[abs v2](https://arxiv.org/abs/2405.01709v2)의 제목은 Minimax Regret Learning for Data with Heterogeneous Subgroups이고 PDF 제목은 Heterogeneous Sub-populations다. 저자는 Weibin Mo, Weijing Tang, Songkai Xue, Yufeng Liu, Ji Zhu이며 앞의2명이 공동제1저자로 표시된다. v1은2024-05-02, v2는2025-09-27 제출이다.

2026-10-10 확인한 [v2 PDF](https://arxiv.org/pdf/2405.01709v2)는 HTTP200·1,220,147바이트·SHA-256 `7e59170bdf4b66d48f8e8a36f315d92d3672b42fc6e8cca42fd9934314f0c401`로 저장본과 같다. 저장TXT1791행을 전체 읽고 page wrapper와 whitespace만 제거해35쪽 각각의 새pypdf 추출과 일치함을 확인했다. 수식의 깨진 추출기호는 시각 원문으로 확인했으며 원본을 고치지 않았다.

저장abs HTML42,362바이트와 현재v2 응답42,356바이트는 다르다. 전체 diff에서 unversioned/v2 식별자·링크와 site CSS/header 버전 차이를 확인했으며 제목·저자·초록·판본 이력은 같다. 저장HTML627행을 raw 전체로 읽었고 script 실행이나 외부 동적 도구 로딩은 하지 않았다. [응답 증거](../evidence/0066-0068-mmr/external-version-check.json)에 URL·시각·바이트·해시를 남겼다.

논문35쪽 전체 텍스트·시각, Figure2.1/3.1/4.1/6.1/6.2/7.1, Table3.1/7.1, Algorithm1을 확인했다. 참고문헌40항목은 서지 독해이지 인용된40논문 전체 독해가 아니다. 원preview5·11쪽도 전체 시각으로 대조했다. 새렌더35쪽과31쪽220dpi 상세는 개인 작업자료로 두고 외부 논문 원문을 저장소에 재게시하지 않는다.

## TeX·보충자료·구현의 확인 범위

[공식v2 TeX](https://arxiv.org/src/2405.01709v2)는 HTTP200·463,904바이트·SHA-256 `0d6401efc9892bdebd3cd2a544bd7ceb0b2039a90f86b4799f9d80a6b154eb7e`다. 디렉터리1개·파일16개의 경로·크기·해시를 검수했다. 입력파일을 따라가는 main.tex570–615, 알고리즘/표기·caption의 model.tex280–371/520–575를 선택 독해했고, real-data-image.tex1–57과00README.json은 전체로 읽었다. 작성 후 model.tex450–505의 Table3.1·퇴화 설명을 추가 독해했다. 전체 두 번째 대조 범위는 [검수](../verification/history-063.md)에 남겼다. TeX 컴파일은 하지 않았다.

6개.tex의 input/include·proof환경·Supplementary/Supplemental·github/http 검색 결과도 확인했다. 이 묶음에는 본문·그림·서지·컴파일 메타데이터가 있고 별도 supplement 파일이나 실행 구현이 없다. 전체TeX/서지소스 독해나 증명 검증을 뜻하지 않는다. 논문이 보충자료 B/C/D/E.1/F.1–3/G.2/H.1/I/J로 안내한 내용은 원문을 확보하지 못했다. 신장 이식 응용도 J에 대한 안내다.

[Weijing Tang 연구 페이지](https://sites.google.com/andrew.cmu.edu/weijingtang/research)의 MMR 항목은 arXiv 링크만 담았고, [Weibin Mo 연구 페이지](https://sites.google.com/view/weibin-mo/research)의 확인한 목록에는 MMR 항목이 없었다. 두 페이지는 보이는 목록/해당 항목과 링크만 읽었으며 rawHTML 전체를 읽었다고 하지 않는다. 다른 저자 페이지나 외부 동적 code finder를 전수 확인한 것은 아니다. 검색의 구판 초록을 v2 본문으로 치환하지 않았으며 공식 실행 코드가 전혀 없다고 단정하지 않는다.

실제 실행판·config·seed·원예측/반복 배열·전체비용, 보충자료 증명, MRI/qFFL과 나머지 기록 검수는 남아 있다.

후속 [H064 출처·판본](history-064.md)에서 MRI32쪽과 지정 표현·공식 자료를 확인했습니다. 위 H063 당시의 남은 범위 중 MRI 본문 검토만 갱신하며 실행 근거·q-FFL·전체 종합의 공백은 유지합니다.
