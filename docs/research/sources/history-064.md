# H064 출처·판본 — MRI

[팀 기록](../records/0066-0068-mri.md) · [명세](../evidence/0066-0068-mri/manifest.json) · [목록](../catalog/history-064-sources.jsonl) · [검수](../verification/history-064.md)

원66·68의 기존 정확사본2개와 MRI 표현4개를 연결한다. 총6원본그룹·12물리경로다. 새 원본 복사와 로컬 전체본문·전체JSON·선택필드 가산은0이다. H062의 당시 미독해 명세는 과거 snapshot으로 보존하고 현재 검토 범위는 H064에 기록한다.

| source_id | 팀 접근 | 실제 확인 범위 |
|---|---|---|
| SRC-0022017 | [66 계획](../evidence/0063-0068-synthesis-risk/originals/SRC-0022017.md.txt) | 전체34행 재대조. 기존 H062 독해·정확사본 재사용. |
| SRC-0022019 | [68 판단](../evidence/0063-0068-synthesis-risk/originals/SRC-0022019.md.txt) | 전체91행 재대조. MRI의 당시 선택 검토와 이번 전체 논문 검토를 구분. |
| SRC-0062712 | [MRI v2 PDF](https://arxiv.org/pdf/2602.04155v2) | 전체32쪽 텍스트·시각, 그림10·표2·서지30항목. 부록 A–G 포함. |
| SRC-0062713 | [TXT의 대응 PDF](https://arxiv.org/pdf/2602.04155v2) | 총3009행의32본문 모두를 실제 읽은 PDF 본문과 대응 검사. wrapper·whitespace 외 차이0. raw3009행 별도 전수 재독해는 아님. |
| SRC-0062714 | [abs v2](https://arxiv.org/abs/2602.04155v2) | 저장HTML633행에서 전체 가시 텍스트·메타데이터·주석·inline script 정적 독해, 관련 링크와 현재판 전체 diff 확인. 모든 raw 태그 행의 수동 독해는 아님. |
| SRC-0062728 | [원 preview의 대응8쪽](https://arxiv.org/pdf/2602.04155v2#page=8) | 원PNG 전체 시각. 공리비교표와 경험 추정의 조건·식18–19 확인. |

## 공식 판본

제목은 *Maximin Relative Improvement: Fair Learning as a Bargaining Problem*, 저자는 Jiwoo Han·Moulinath Banerjee·Yuekai Sun이다. arXiv v1은2026-02-04, v2는2026-06-16이다. [PMLR 출판 페이지](https://proceedings.mlr.press/v306/han26a.html)는 ICML2026, volume306, 39539–39570쪽을 확인해 준다. 페이지 메타데이터의 게시일2026-09-29와 학회 개최 월을 판본 제출일과 혼동하지 않는다.

2026-10-10 받은 [arXiv v2 PDF](https://arxiv.org/pdf/2602.04155v2)는 2,524,215바이트, SHA-256 `a4521ecee5ce59e1e7e4d3bb05bdb2d6da1c47ba3c3b019ccc208a20107c23d0`로 원본과 바이트동일하다. [PMLR PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/han26a/han26a.pdf)는 2,329,238바이트, SHA-256 `90504fb4d0da54615b95ce8240e37b95551055efbc8e7085c9d03239e9628314`로 바이트는 다르다. 32쪽 텍스트를 각각 비교하면1쪽의 arXiv 판본 표시와 whitespace를 제외한 본문이 모두 같다. 출판본1쪽은 시각으로도 확인했으며, 출판본 전체32쪽을 별도로 시각 재독해한 것은 아니다.

저장abs HTML40,780바이트와 현재v2 HTML40,774바이트의 diff는 unversioned/v2 식별자·링크와 CSS/header 버전 차이다. 제목·저자·초록·판본 이력은 같다. HTML의 code finder는 일반 사이트 기능이며 저자 구현 링크가 확인됐다는 뜻이 아니다. script나 외부 동적 embed를 실행하지 않았다. [판본 검수 JSON](../evidence/0066-0068-mri/external-version-check.json)에 요청 URL·시각·해시를 남겼다.

PDF의 수식·표·그림은 추출 텍스트에만 의존하지 않고 모든 페이지를 시각으로 확인했다. 작은 그림9는240dpi 확대와 source 안의 대응 그림6개에서 인쇄값을 대조했다. 참고문헌30항목을 읽은 것은 인용 논문30편의 본문을 읽은 것과 다르다.

## TeX·구현·접근 공백

[arXiv v2 TeX](https://arxiv.org/src/2602.04155v2)는 3,333,580바이트, SHA-256 `bbed4ff1c1adea761d5d64f0450ceb45515463d030e312c93c1ae0cff30a7376`다. 디렉터리2개와 파일35개의 목록·크기·해시를 확인했다. 실행 구현·원결과 배열은 이 묶음에 없다. 전체 source를 실행하거나 컴파일하지 않았다.

수동으로 읽은 source는 `draft.tex`205–251·645–775행, `appendix.tex`476–733·875–924·968–1193행, `00README.json`전체다. 정의·추정·실험·baseline·증명 중간 식·퇴화 설명·표와 그림의 연결을 대조했다. source 전체의 정적 독해를 완료했다고 표시하지 않는다. 두 TeX의 절 제목과 네트워크·code 문자열 검색은 탐색일 뿐 전수 독해가 아니다. README는 컴파일 메타데이터이며 실험 환경 명세가 아니다.

PMLR 페이지는 [OpenReview](https://openreview.net/forum?id=9KOJdlFH82)를 연결한다. 웹 요청은 접근 검증 화면, 공개 API 요청은403으로 끝나 본문·리뷰·첨부자료를 읽지 못했다. 이 공백 때문에 원래 논문에 코드가 전혀 없다고 단정하지 않는다. 접근 제한을 우회하지 않았으며 다른 원문·수치 검수는 진행했다.

저자의 실제 구현·설정·seed·데이터 분할·원결과 배열·전체 시간과 비용은 미확인이다. q-FFL 원문과66–68의 최종 통합, 나머지 과거기록은 후속 범위다.
