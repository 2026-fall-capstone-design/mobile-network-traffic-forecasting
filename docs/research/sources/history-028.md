# H028 출처와 실제 열람 범위

[47 정리 기록](../records/0047-input-sharing-roles.md)은 원문23개 참조를 [목록](../catalog/history-028-sources.jsonl)과 [manifest](../evidence/0047-input-sharing-roles/manifest.json)에 연결한다. 새 정확 사본7개·9,102 bytes, 기존 사본3개, 외부 참조 metadata13개다. UPC 원논문은 기존에 제공된 목록 밖 자료로 별도 명시하며 23개에 더해 inventory 출처인 것처럼 세지 않는다.

| 출처·팀 접근 | 원본 루트 기준 경로 | 실제 검토 범위 |
|---|---|---|
| [SRC-0022760](../evidence/0047-input-sharing-roles/originals/SRC-0022760.py.txt) | `tmp/redesign_20260925/fetch_input_sharing_sources_45.py` | 입수 코드 전체 42행 정적 독해; 현재 실행하지 않음 |
| [SRC-0022744](../evidence/0047-input-sharing-roles/originals/SRC-0022744.py.txt) | `tmp/redesign_20260925/fetch_dic_st_static_45.py` | 출판사 PDF 입수 코드 전체 19행 정적 독해; 현재 실행하지 않음 |
| [SRC-0023092](../evidence/0047-input-sharing-roles/originals/SRC-0023092.py.txt) | `tmp/redesign_20260925/render_input_sharing_sources_45.py` | 렌더 코드 전체 17행 정적 독해; 현재 실행하지 않음 |
| [SRC-0062876](../evidence/0047-input-sharing-roles/originals/SRC-0062876.json) | `tmp/redesign_20260925/sources/input_sharing_45/dic_st_publisher_static.json` | 출판사 정적 PDF URL/status/bytes/hash/pages 등 모든 키 |
| [SRC-0062877](../evidence/0047-input-sharing-roles/originals/SRC-0062877.json) | `tmp/redesign_20260925/sources/input_sharing_45/fetch_log.json` | Markov 성공3건·MDPI403 2건, 모든 항목과 키 |
| [SRC-0062885](../evidence/0047-input-sharing-roles/originals/SRC-0062885.json) | `tmp/redesign_20260925/sources/input_sharing_45/render_log.json` | 6개 렌더 항목과 모든 키; stderr 빈 값 |
| [SRC-0062886](../evidence/0047-input-sharing-roles/originals/SRC-0062886.json) | `tmp/redesign_20260925/sources/input_sharing_45/review_scope.json` | 당시 검토 범위·한계·검색 발견 등 모든 키; 과거 작성자의 보고 |
| [SRC-0021616](../evidence/0047-input-sharing-roles/../0045-0046-input-stability/originals/SRC-0021616.md.txt) | `tmp/redesign_20260925/45_input_sharing_review_plan.md` | 45 계획 전체 검토 H027 재사용; 새 전체 독해 집계 없음 |
| [SRC-0021660](../evidence/0047-input-sharing-roles/../0045-0046-input-stability/originals/SRC-0021660.md.txt) | `tmp/redesign_20260925/47_input_sharing_findings.md` | 47 전체105행. H027의 §2/§7 수치 검수를 재사용하고 이번에 §1/§3–6/§7문헌·접근을 대조 |
| [SRC-0000657](../evidence/0047-input-sharing-roles/../0045-0046-input-stability/originals/SRC-0000657.json) | `output/research/redesign_20260925_snapshot_10/manifest.json` | 스냅샷10 metadata 전체 검토 H027 재사용; 이번 지정 출처의 해시 행만 대조 |
| [SRC-0061693](https://github.com/Superint-Lab/GECOS/blob/a7519dde9d6f5deb3006689df047d99ea0dac7b7/main.py) | `tmp/redesign_20260925/sources/GECOS_main.txt` | GECOS main 전체134행 정적 재독; SRC-0020622와 동일4800B, 기존 pinned 공식 identity 재사용 |
| [SRC-0062871](https://doi.org/10.3390/rs14061439) | `tmp/redesign_20260925/sources/input_sharing_45/dic_st_publisher.pdf` | 19쪽 중 텍스트6–12/14/16/17, 시각10/11/16. 전논문 아님 |
| [SRC-0062880](https://arxiv.org/abs/2605.29411v2) | `tmp/redesign_20260925/sources/input_sharing_45/markov_boundary_v2.pdf` | 12쪽 중 텍스트1–10, 시각2/6/9. 11–12쪽 참고문헌 미독해 |
| SRC-0062873 | `tmp/redesign_20260925/sources/input_sharing_45/dic_st_publisher_page10.png` | 보존된 page10 PNG 직접 시각 열람; PDF 선택 구간과 대조 |
| SRC-0062874 | `tmp/redesign_20260925/sources/input_sharing_45/dic_st_publisher_page11.png` | 보존된 page11 PNG 직접 시각 열람; PDF 선택 구간과 대조 |
| SRC-0062875 | `tmp/redesign_20260925/sources/input_sharing_45/dic_st_publisher_page16.png` | 보존된 page16 PNG 직접 시각 열람; PDF 선택 구간과 대조 |
| SRC-0062882 | `tmp/redesign_20260925/sources/input_sharing_45/markov_boundary_v2_page02.png` | 보존된 page2 PNG 직접 시각 열람; PDF 선택 구간과 대조 |
| SRC-0062883 | `tmp/redesign_20260925/sources/input_sharing_45/markov_boundary_v2_page06.png` | 보존된 page6 PNG 직접 시각 열람; PDF 선택 구간과 대조 |
| SRC-0062884 | `tmp/redesign_20260925/sources/input_sharing_45/markov_boundary_v2_page09.png` | 보존된 page9 PNG 직접 시각 열람; PDF 선택 구간과 대조 |
| SRC-0062872 | `tmp/redesign_20260925/sources/input_sharing_45/dic_st_publisher.txt` | 해시·크기만 확인. TXT/HTML 고유 내용 검토 대기 |
| SRC-0062881 | `tmp/redesign_20260925/sources/input_sharing_45/markov_boundary_v2.txt` | 해시·크기만 확인. TXT/HTML 고유 내용 검토 대기 |
| SRC-0062878 | `tmp/redesign_20260925/sources/input_sharing_45/markov_boundary_abs.html` | 해시·크기만 확인. TXT/HTML 고유 내용 검토 대기 |
| SRC-0062879 | `tmp/redesign_20260925/sources/input_sharing_45/markov_boundary_v2.html` | 해시·크기만 확인. TXT/HTML 고유 내용 검토 대기 |

GECOS는 commit `a7519dde9d6f5deb3006689df047d99ea0dac7b7`의 공식 main.py와 기존 보존본의 identity를 [pilot 검수](../verification/pilot-005-document-review.json)에서 확인한 결과를 재사용했다. 이번에는 두 로컬 사본 SHA-256 `ecdf4f95996eeef8955337c9f4d5a3f3dc073ba961b4a971bdc170eb7459f673`와 해당 검수 파일 해시를 다시 확인했다. 새 원격 코드 실행이나 전체 로더 재현은 아니다.

기존 제공 UPC PDF의 DOI는 [10.1109/TNSM.2025.3599168](https://doi.org/10.1109/TNSM.2025.3599168), SHA-256은 `d8b720fe96f4d2da8ebcbe9dc779c0b4512dec0b2f4823295f908fcd639ae622`다. 이번 IV.A의 6–7쪽 텍스트 재독은 기존 H021 검수와 연결하며 신규 독해 쪽수에 다시 넣지 않는다. 원논문 전체 검토나 표 전체 재검수로 확대하지 않았다.

새 전체 텍스트 검토로 세는 것은 47번과 로컬 입수·렌더 코드3개, 총4개다. GECOS 전체 재독과 45 계획은 재사용이다. 작은 JSON4개는 모든 키/항목을 읽었다. 선택 1차 텍스트22쪽은 신규20쪽+UPC재독2쪽이고, 시각 확인은6쪽, 전논문 완료는0개다. 텍스트 추출 파일을 생성했다는 사실을 페이지 독해로 세지 않았다.

공식 웹 metadata는 2026-10-09에 확인했다. [DIC-ST 출판 이력](https://www.mdpi.com/2072-4292/14/6/1439/notes)의 PDF Version of Record는2022-03-16이며 HTML의2026-08-21 갱신과 구별했다. [arXiv v2](https://arxiv.org/abs/2605.29411v2)는2026-08-19 개정·CIKM2026 accepted·12쪽/2표/9그림으로 표시한다. 긴 웹 출력의 일부가 잘렸으므로 웹 본문 전체를 읽었다고 세지 않고 저장 PDF의 지정 구간을 직접 사용했다.

두 논문의 PDF·PNG 전체를 저장소에 재배포하지 않았다. 공식 링크와 저장본 해시·페이지로 팀이 대상 버전을 식별할 수 있지만 원 연구 자료·전체 실행 환경 접근 완료를 뜻하지 않는다. DIC 나머지 PDF 구간, Markov 참고문헌11–12쪽, 별도 추출 TXT/HTML 고유 내용, 렌더 외의 모든 그림·관련 보고서·후속75는 남아 있다. CLPREM·temporal causal PFN은 검색 발견만 확인했다.

[1차 근거 검사](../verification/history-028-primary-check.json)는 현재 원본23개의 identity, 보존 사본, 지정 스냅샷 행, 접근·렌더 기록, 이전 GECOS 검수 해시와 원 연구 통제파일6개의 불변을 확인했다. PDF에서 다시 추출한 Table2의5행·34개 수치는 시각 열람한 값과 일치한다. 원논문 실험의 독립 재현은 아니다. 역사적 429/challenge 보고, EMD/graph 시간 절단과 전체 로더 등 미확인 항목을 완료로 바꾸지 않았다.
