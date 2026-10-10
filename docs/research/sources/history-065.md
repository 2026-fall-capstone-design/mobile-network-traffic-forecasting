# H065 출처·판본 — 통신 트래픽 q-FFL

[팀 기록](../records/0066-0068-qffl.md) · [명세](../evidence/0066-0068-qffl/manifest.json) · [목록](../catalog/history-065-sources.jsonl) · [검수](../verification/history-065.md)

원66·68의 기존 정확사본2개와 논문의 표현7개를 연결한다. 총9원본그룹·18물리경로다. 새 원본 복사와 로컬 전체본문·전체JSON·선택필드 가산은0이다. H062 당시의 미독해 명세는 역사적 snapshot으로 보존하며 현재 범위는 H065에 기록한다.

| source_id | 팀 접근 | 실제 확인 범위 |
|---|---|---|
| SRC-0022017 | [66 계획](../evidence/0063-0068-synthesis-risk/originals/SRC-0022017.md.txt) | 전체34행 재대조, 기존 정확사본·독해 재사용 |
| SRC-0022019 | [68 판단](../evidence/0063-0068-synthesis-risk/originals/SRC-0022019.md.txt) | 전체91행 재대조, 과거 결과와 현재 검수를 구분 |
| SRC-0062706 | [arXiv v2 PDF](https://arxiv.org/pdf/2502.06743v2) | 전체7쪽 텍스트·시각, 그림4·표2·서지40항목 |
| SRC-0062707 | [TXT 대응 PDF](https://arxiv.org/pdf/2502.06743v2) | 682행의7본문을 실제 읽은 PDF와 전수 대응. raw682행 별도 독해 아님 |
| SRC-0062708 | [abs v2](https://arxiv.org/abs/2502.06743v2) | 저장HTML650행의 전체 가시 내용·메타·주석·inline script 정적 독해와 관련 링크·현재판 diff 확인. 모든 raw 태그행 수동 독해 아님 |
| SRC-0062722 | [원preview 대응3쪽](https://arxiv.org/pdf/2502.06743v2#page=3) | 원PNG 전체 시각, 데이터·분할·학습 |
| SRC-0062723 | [원preview 대응4쪽](https://arxiv.org/pdf/2502.06743v2#page=4) | 원PNG 전체 시각, TableI·Fig1–2·Eq3 |
| SRC-0062724 | [원preview 대응5쪽](https://arxiv.org/pdf/2502.06743v2#page=5) | 원PNG 전체 시각, 부호·Eq4–5·RSA |
| SRC-0062725 | [원preview 대응6쪽](https://arxiv.org/pdf/2502.06743v2#page=6) | 원PNG 전체 시각, TableII·Fig3–4·결론 |

## 공식 판본과 출판 메타데이터

arXiv v1은2025-02-10, v2는2025-02-17이다. 2026-10-10 받은 [v2 PDF](https://arxiv.org/pdf/2502.06743v2)는418,864바이트, SHA-256 `673c4e452ac3e017d65433fe0d62ebfd49ffcfbf45811cd58de36b3882108ff9`로 원본과 바이트동일하다. 현재 abs44,816바이트와 저장 abs44,804바이트의 전체 diff는5개 hunk이며 unversioned/v2 표지 식별자·description·breadcrumb·PDF/source URL 차이다. 연구 제목·저자·초록·판본 이력·DOI는 같다. code finder는 일반 사이트 기능이며 연구 구현 발견의 근거가 아니다. 외부 script나 동적 embed를 실행하지 않았다.

[Crossref DOI 메타데이터](https://api.crossref.org/works/10.1109/ICC52391.2025.11161740)는 IEEE, *ICC 2025 - IEEE International Conference on Communications*, 1438–1444쪽, published-print 2025-06-08과 저자4명을 기록한다. 이 날짜는 arXiv 판본 제출일과 구분한다. IEEE 문서 페이지는 직접 요청에서202/빈0바이트였고 웹 열람에서도 본문을 확보하지 못했다. 최종 출판 PDF와 arXiv의 식·표가 같거나 다르다고 판정하지 않는다. 접근 제한을 우회하지 않았다.

## TeX·원알고리즘·통신 구현의 구분

[공식 v2 TeX 묶음](https://arxiv.org/src/2502.06743v2)은517,725바이트, SHA-256 `c1b909da162d6ca69a155e8445a1662929e183463be665cca168009d91766f05`다. 파일19개의 목록·크기·해시를 확인했다. `main_v3.tex`271행 중76–106·132–175·189–234행을 읽어 식·설정·표·자원 가정·주장을 대조했다. 그림 변형 파일·EPS 좌표·전체 bib·클래스까지 읽은 것은 아니며 컴파일하지 않았다. 이 묶음에는 실험 실행 코드가 확인되지 않는다.

Li et al. ICLR2020의 [공식 q-FFL 저장소 고정 commit](https://github.com/litian96/fair_flearn/tree/f09797113147b5ae66eb0348e93f575d5d63baed)에서 README151행·LICENSE21행·requirements6행·main170행·qffedavg70행·fedbase215행·client112행·tf_utils145행, 총8파일890행을 전체 정적으로 읽었다. 코드 파일은 그중5개다. 파일별 URL·해시·시각과 확인한 함수는 [코드 감사](../evidence/0066-0068-qffl/upstream-code-audit.json)에 있다. MIT 표기를 확인했으며 public archive에 원코드를 복사하지 않고 고정 링크와 분석을 남긴다. 전체 model/data/의존경로 독해나 실행은 아니다.

OpenReview의 원알고리즘 PDF 요청은403으로 끝났으며 이번에는 그 논문 전체를 읽었다고 세지 않는다. 원알고리즘 repo의 존재와 Panda 통신 실험의 구현 확인은 서로 다른 상태다. 논문·abs·TeX 목록·지정 본문과 제목/저자/코드 검색의 확인 범위에서 통신 구현 연결은 찾지 못했다. 전 세계 코드 부재를 주장하지 않는다.

요청·해시·판본 범위는 [외부 판본 JSON](../evidence/0066-0068-qffl/external-version-check.json), 표현별 범위는 [형식 감사](../evidence/0066-0068-qffl/format-audit.json)에 보존했다. 참고문헌40항목 독해는 인용 논문40편의 본문 독해가 아니다. 실제 통신 구현·원배열·seed·분할/전처리·전체 비용과 최종 IEEE 본문은 미확인이다.

후속 [H066 통합 범위](history-066.md)에서 66–68 세 목적의 본문 비교를 연결했습니다. 위의 통합 대기는 당시 상태이며 각 논문의 실제 실행·원배열·비용 공백은 유지합니다.
