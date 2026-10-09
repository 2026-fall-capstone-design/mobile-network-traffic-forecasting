# H030 출처와 열람 범위

[50번 정리 기록](../records/0050-aggregation-literature.md)은 [21개 출처 목록](../catalog/history-030-sources.jsonl)과 [manifest](../evidence/0050-aggregation-literature/manifest.json)를 연결한다. 새 정확 사본 5개·8,808 bytes, 기존 사본 2개 재사용, 외부 자료 metadata 14개다. PDF·그림 원문을 저장소에 새로 배포한 것으로 세지 않는다.

| 출처·팀 접근 | 원본 루트 기준 경로 | 실제 검토 범위 |
|---|---|---|
| [SRC-0022728](../evidence/0050-aggregation-literature/originals/SRC-0022728.py.txt) | `tmp/redesign_20260925/fetch_aggregation_sources_48.py` | fetch 코드 전체 41행 정적 독해. 역사적 다운로드 명령을 실행하지 않음 |
| [SRC-0023087](../evidence/0050-aggregation-literature/originals/SRC-0023087.py.txt) | `tmp/redesign_20260925/render_aggregation_sources_48.py` | render 코드 전체 16행 정적 독해. 역사적 코드 실행 없음 |
| [SRC-0061745](../evidence/0050-aggregation-literature/originals/SRC-0061745.json) | `tmp/redesign_20260925/sources/aggregation_48/fetch_log.json` | fetch log 4개 항목·전체 키. 각 URL·HTTP 200·bytes·SHA·PDF쪽수 대조 |
| [SRC-0061760](../evidence/0050-aggregation-literature/originals/SRC-0061760.json) | `tmp/redesign_20260925/sources/aggregation_48/render_log.json` | render log 7개 항목·전체 키. exit_code 0·빈 stderr·PNG identity 연결 |
| [SRC-0061761](../evidence/0050-aggregation-literature/originals/SRC-0061761.json) | `tmp/redesign_20260925/sources/aggregation_48/review_scope.json` | 검토 범위 JSON 전체. 3편 검토/5편 발견·접근 보고·코드 미검토 구분 |
| [SRC-0021681](../evidence/0050-aggregation-literature/../0048-0049-aggregation-recovery/originals/SRC-0021681.md.txt) | `tmp/redesign_20260925/48_aggregation_review_plan.md` | 48 계획 43행의 기존 전체 검토 재사용 |
| [SRC-0021725](../evidence/0050-aggregation-literature/../0048-0049-aggregation-recovery/originals/SRC-0021725.md.txt) | `tmp/redesign_20260925/50_aggregation_findings.md` | 50 원문 66행 전체·주장 2차대조. H029 저장 수치/비용 검수 재사용 |
| [SRC-0061746](https://proceedings.mlr.press/v235/cini24a.html) | `tmp/redesign_20260925/sources/aggregation_48/higp_icml2024.pdf` | HiGP 1–15쪽 텍스트 전체. 시각 2/3/4/5/7/8/13/15쪽 |
| SRC-0061747 | `tmp/redesign_20260925/sources/aggregation_48/higp_icml2024.txt` | PDF와 page-labelled 텍스트 대조; 독립 새 논문/새 본문 수로 가산하지 않음 |
| SRC-0061748 | `tmp/redesign_20260925/sources/aggregation_48/higp_icml2024_page04.png` | 원래 저장된 PNG를 시각 열람; 해당 PDF 쪽에 연결 |
| SRC-0061749 | `tmp/redesign_20260925/sources/aggregation_48/higp_icml2024_page05.png` | 원래 저장된 PNG를 시각 열람; 해당 PDF 쪽에 연결 |
| [SRC-0061750](https://arxiv.org/abs/2205.14104v1) | `tmp/redesign_20260925/sources/aggregation_48/multilevel_clustering_abs.html` | 저장 HTML의 보이는 연구 metadata·초록·버전 정보 전체. raw script/style 미실행·전체 raw HTML 독해 아님 |
| [SRC-0061751](https://arxiv.org/abs/2205.14104v1) | `tmp/redesign_20260925/sources/aggregation_48/multilevel_clustering_v1.pdf` | HTS-Cluster v1 1–17쪽 텍스트 전체. 시각 3/5/6/7/8/9/10/11/15/16쪽 |
| SRC-0061752 | `tmp/redesign_20260925/sources/aggregation_48/multilevel_clustering_v1.txt` | PDF와 page-labelled 텍스트 대조; 독립 새 논문/새 본문 수로 가산하지 않음 |
| SRC-0061753 | `tmp/redesign_20260925/sources/aggregation_48/multilevel_clustering_v1_page07.png` | 원래 저장된 PNG를 시각 열람; 해당 PDF 쪽에 연결 |
| SRC-0061754 | `tmp/redesign_20260925/sources/aggregation_48/multilevel_clustering_v1_page10.png` | 원래 저장된 PNG를 시각 열람; 해당 PDF 쪽에 연결 |
| SRC-0061755 | `tmp/redesign_20260925/sources/aggregation_48/multilevel_clustering_v1_page11.png` | 원래 저장된 PNG를 시각 열람; 해당 PDF 쪽에 연결 |
| [SRC-0061756](https://dl.ifip.org/db/conf/ondm/ondm2023/1570874472.pdf) | `tmp/redesign_20260925/sources/aggregation_48/ondm2023.pdf` | ONDM 1–3쪽 텍스트·시각 전체 |
| SRC-0061757 | `tmp/redesign_20260925/sources/aggregation_48/ondm2023.txt` | PDF와 page-labelled 텍스트 대조; 독립 새 논문/새 본문 수로 가산하지 않음 |
| SRC-0061758 | `tmp/redesign_20260925/sources/aggregation_48/ondm2023_page02.png` | 원래 저장된 PNG를 시각 열람; 해당 PDF 쪽에 연결 |
| SRC-0061759 | `tmp/redesign_20260925/sources/aggregation_48/ondm2023_page03.png` | 원래 저장된 PNG를 시각 열람; 해당 PDF 쪽에 연결 |

세 PDF의 본문·부록·참고문헌 텍스트 35쪽과 그림·표·관련 수식 21쪽을 읽었다. 세 편의 내용 읽기 완료는 공식 구현 검토, 모든 증명 검증 또는 재현 성공과 다르다. 논문 Table의 선택 19행·128개 인쇄 수치를 다시 추출하여 시각 열람값과 비교했다. 나머지 표도 읽었지만 모든 수치를 프로그램으로 검산했다고 표현하지 않는다.

HiGP의 일반 assignment 설명과 주 실험의 고정 hierarchy, ONDM의 multioutput과 모델 개수, HTS-Cluster의 대표 조합과 clustering 목적함수를 구분했다. ONDM pair 방향 표기, HTS 본문과 Table 4 정확도 설명의 불일치, HiGP 비용 차수·lift 인덱스의 실행 명세는 임의 수정하지 않았다. HTS 부록 A를 읽은 범위와 전체 정리 인증은 구분한다.

파생 TXT 세 개는 page header를 포함한 재추출과 비교했다. 두 개의 decoded text는 같고 HiGP는 CR/LF 제어문자 차이만 있었다. 실제 읽은 PDF 텍스트와 추가 연구 문장이 없음을 확인했으며 바이트 중복으로 분류하지 않았다. 저장 HTML의 보이는 연구 정보는 공식 arXiv v1 metadata와 대조했다. HTML의 탐색·스타일·스크립트를 연구 지시로 실행하지 않았다.

당시 fetch log 네 건의 HTTP 200과 현재 IFIP timeout을 별도 사실로 보존했다. 검토 범위 파일의 OpenReview verification 보고는 보존된 성공 로그만으로 증명되지 않는다. 발견 목록 HSeq2Seq 등 5편은 방법 열람으로 집계하지 않았다. 공식 구현·관련 후속 기록·별도 보고서와 전체 원본은 계속 검토 대상이다.
