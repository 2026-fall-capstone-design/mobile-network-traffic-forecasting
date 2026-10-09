# H032 출처와 실제 열람 범위

[51·55 GOTSF 기록](../records/0051-0055-gotsf-audit.md)은 원본 34경로를 다룬다. 새 정확 사본 23개·236,888 bytes, H031 사본 1개 재사용, 외부 metadata 10개다. 별도 추가 참조 4개 중 코드·LICENSE 3개·15,273 bytes를 보존하고 CSV는 링크·해시·검수 범위를 남겼다. 추가 참조는 원 연구의 원본 목록이나 당시 입수 실적으로 세지 않는다.

[원본별 목록](../catalog/history-032-sources.jsonl)과 [manifest](../evidence/0051-0055-gotsf-audit/manifest.json)에 경로·size·SHA-256·읽기 범위가 있다. 해시가 같은 바이트만 alias로 연결한다. 파생 TXT와 PDF/notebook의 관계는 개행을 고려한 변환 대조이며 byte alias가 아니다.

| source_id·팀 접근 | 원본 루트 기준 경로 | 실제 검토 범위 |
|---|---|---|
| [SRC-0021746](../evidence/0051-0055-gotsf-audit/originals/SRC-0021746.md.txt) | `tmp/redesign_20260925/51_network_data_problem_review_plan.md` | 전체 텍스트 25행 정적 독해; 실행 없음 |
| [SRC-0022765](../evidence/0051-0055-gotsf-audit/originals/SRC-0022765.py.txt) | `tmp/redesign_20260925/fetch_network_scope_51.py` | 전체 텍스트 33행 정적 독해; 실행 없음 |
| [SRC-0063262](../evidence/0051-0055-gotsf-audit/originals/SRC-0063262.txt) | `tmp/redesign_20260925/sources/network_scope_51/Viz_Wireless.source.txt` | 944행 전체·33개 source cell 대조; notebook 저장 출력은 별도 범위 |
| [SRC-0063267](../evidence/0051-0055-gotsf-audit/originals/SRC-0063267.json) | `tmp/redesign_20260925/sources/network_scope_51/code_fetch_log.json` | 전체 JSON 키·항목 독해; 다른 문헌의 fetch/render 행은 metadata만 확인 |
| [SRC-0063268](../evidence/0051-0055-gotsf-audit/originals/SRC-0063268.py.txt) | `tmp/redesign_20260925/sources/network_scope_51/data_provider__data_factory.py` | 전체 텍스트 63행 정적 독해; 실행 없음 |
| [SRC-0063269](../evidence/0051-0055-gotsf-audit/originals/SRC-0063269.py.txt) | `tmp/redesign_20260925/sources/network_scope_51/data_provider__data_loader.py` | 전체 텍스트 539행 정적 독해; 실행 없음 |
| [SRC-0063270](../evidence/0051-0055-gotsf-audit/originals/SRC-0063270.py.txt) | `tmp/redesign_20260925/sources/network_scope_51/experiments__exp.py` | 전체 텍스트 522행 정적 독해; 실행 없음 |
| [SRC-0063271](../evidence/0051-0055-gotsf-audit/originals/SRC-0063271.py.txt) | `tmp/redesign_20260925/sources/network_scope_51/experiments__exp_long_term_forecasting_discrete.py` | 전체 텍스트 417행 정적 독해; 실행 없음 |
| [SRC-0063272](../evidence/0051-0055-gotsf-audit/originals/SRC-0063272.json) | `tmp/redesign_20260925/sources/network_scope_51/fetch_log.json` | 전체 JSON 키·항목 독해; 다른 문헌의 fetch/render 행은 metadata만 확인 |
| [SRC-0063278](../evidence/0051-0055-gotsf-audit/originals/SRC-0063278.md.txt) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_card.md` | 전체 텍스트; 연결된 그림·애니메이션 미열람 |
| [SRC-0063279](../evidence/0051-0055-gotsf-audit/originals/SRC-0063279.md.txt) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_code_README.md` | 전체 텍스트; 연결된 그림·애니메이션 미열람 |
| [SRC-0063280](../evidence/0051-0055-gotsf-audit/originals/SRC-0063280.json) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_code_tree.json` | 181개 tree metadata 파싱, 선택 blob 확인; 전체 tree 의미 독해·181개 파일 본문 독해 아님 |
| [SRC-0063281](../evidence/0051-0055-gotsf-audit/originals/SRC-0063281.json) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_commit.json` | 전체 JSON 키·항목 독해; 다른 문헌의 fetch/render 행은 metadata만 확인 |
| [SRC-0063282](../evidence/0051-0055-gotsf-audit/originals/SRC-0063282.json) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_info.json` | 전체 JSON 키·항목 독해; 다른 문헌의 fetch/render 행은 metadata만 확인 |
| [SRC-0063283](../evidence/0051-0055-gotsf-audit/originals/SRC-0063283.py.txt) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_script_stats.py` | 전체 텍스트 185행 정적 독해; 실행 없음 |
| [SRC-0063284](../evidence/0051-0055-gotsf-audit/originals/SRC-0063284.py.txt) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_script_train.py` | 전체 텍스트 172행 정적 독해; 실행 없음 |
| [SRC-0063285](../evidence/0051-0055-gotsf-audit/originals/SRC-0063285.json) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_tree.json` | 전체 JSON 키·항목 독해; 다른 문헌의 fetch/render 행은 metadata만 확인 |
| [SRC-0063286](../evidence/0051-0055-gotsf-audit/originals/SRC-0063286.py.txt) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_utils__metrics.py` | 전체 텍스트 41행 정적 독해; 실행 없음 |
| [SRC-0063292](../evidence/0051-0055-gotsf-audit/originals/SRC-0063292.json) | `tmp/redesign_20260925/sources/network_scope_51/methods_fetch_log.json` | 전체 JSON 키·항목 독해; 다른 문헌의 fetch/render 행은 metadata만 확인 |
| [SRC-0063293](../evidence/0051-0055-gotsf-audit/originals/SRC-0063293.json) | `tmp/redesign_20260925/sources/network_scope_51/render_log.json` | 전체 JSON 키·항목 독해; 다른 문헌의 fetch/render 행은 metadata만 확인 |
| [SRC-0063294](../evidence/0051-0055-gotsf-audit/originals/SRC-0063294.sh.txt) | `tmp/redesign_20260925/sources/network_scope_51/scripts__multivariate_forecasting__Wireless__train.sh` | 전체 텍스트 507행 정적 독해; 실행 없음 |
| [SRC-0063302](../evidence/0051-0055-gotsf-audit/originals/SRC-0063302.json) | `tmp/redesign_20260925/sources/network_scope_51/supplement_fetch_log.json` | 전체 JSON 키·항목 독해; 다른 문헌의 fetch/render 행은 metadata만 확인 |
| [SRC-0063303](../evidence/0051-0055-gotsf-audit/originals/SRC-0063303.py.txt) | `tmp/redesign_20260925/sources/network_scope_51/utils__delta_specific_utils.py` | 전체 텍스트 47행 정적 독해; 실행 없음 |
| [SRC-0021824](../evidence/0051-0055-gotsf-audit/../0052-0054-partial-observation/originals/SRC-0021824.md.txt) | `tmp/redesign_20260925/55_network_and_telemetry_findings.md` | 전체 텍스트는 H031 재사용; §1 GOTSF 자료·§2 GOTSF 방법/지표/에너지 주장 재대조. 나머지 55 미완료 |
| [SRC-0063261](https://github.com/netop-team/gotsf/blob/31b17e55a0cb6f41bfe25230db3f81567efd58f3/Viz_Wireless.ipynb) | `tmp/redesign_20260925/sources/network_scope_51/Viz_Wireless.ipynb` | 33개 source·저장 text 출력·12개 PNG 독해; cell0 생성 runtime JS 제외; 전체 notebook 검토로 표시하지 않음 |
| [SRC-0063273](https://ojs.aaai.org/index.php/AAAI/article/view/39249) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_AAAI_2026.pdf` | 전체 9쪽 텍스트; 시각 확인 2, 3, 4, 5, 7쪽; 전 증명/성능 재현 아님 |
| SRC-0063274 | `tmp/redesign_20260925/sources/network_scope_51/gotsf_AAAI_2026.txt` | 이미 읽은 PDF 전체 추출과 개행 정규화 후 텍스트 일치; 새 본문 독해 수에 중복 가산하지 않음 |
| [SRC-0063275](https://arxiv.org/abs/2504.17493v3) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_arxiv_abs.html` | 보이는 페이지의 의미 텍스트·서지 독해; script/style 제외, raw HTML 전체 독해 아님 |
| [SRC-0063276](https://arxiv.org/abs/2504.17493v3) | `tmp/redesign_20260925/sources/network_scope_51/gotsf_arxiv_v3.pdf` | 전체 14쪽 텍스트; 시각 확인 2, 3, 4, 5, 6, 7, 9, 10, 11쪽; 전 증명/성능 재현 아님 |
| SRC-0063277 | `tmp/redesign_20260925/sources/network_scope_51/gotsf_arxiv_v3.txt` | 이미 읽은 PDF 전체 추출과 개행 정규화 후 텍스트 일치; 새 본문 독해 수에 중복 가산하지 않음 |
| SRC-0063307 | `tmp/redesign_20260925/sources/network_scope_51/previews/gotsf_AAAI_2026_p04.png` | 저장 그림 4쪽 시각 독해·hash 대조 |
| SRC-0063308 | `tmp/redesign_20260925/sources/network_scope_51/previews/gotsf_AAAI_2026_p07.png` | 저장 그림 7쪽 시각 독해·hash 대조 |
| SRC-0063309 | `tmp/redesign_20260925/sources/network_scope_51/previews/gotsf_arxiv_v3_p05.png` | 저장 그림 5쪽 시각 독해·hash 대조 |
| SRC-0063310 | `tmp/redesign_20260925/sources/network_scope_51/previews/gotsf_arxiv_v3_p09.png` | 저장 그림 9쪽 시각 독해·hash 대조 |

## 아카이브 검수를 위해 추가 확보한 고정 참조

모두 GOTSF commit `31b17e55a0cb6f41bfe25230db3f81567efd58f3`의 파일이며 2026-10-09에 입수했다. 저장 tree와 Git blob을 대조했다.

| ID | 공식 위치·팀 사본 | 읽기/검사 범위 |
|---|---|---|
| EXT-H032-01 | [utils/tools.py](https://raw.githubusercontent.com/netop-team/gotsf/31b17e55a0cb6f41bfe25230db3f81567efd58f3/utils/tools.py) · [정확 사본](../evidence/0051-0055-gotsf-audit/originals/EXT-H032-01.txt) | 전체 텍스트 정적 독해 |
| EXT-H032-02 | [LICENSE](https://raw.githubusercontent.com/netop-team/gotsf/31b17e55a0cb6f41bfe25230db3f81567efd58f3/LICENSE) · [정확 사본](../evidence/0051-0055-gotsf-audit/originals/EXT-H032-02.LICENSE.txt) | 전체 텍스트 정적 독해 |
| EXT-H032-03 | [scripts/multivariate_forecasting/Wireless/stats.sh](https://raw.githubusercontent.com/netop-team/gotsf/31b17e55a0cb6f41bfe25230db3f81567efd58f3/scripts/multivariate_forecasting/Wireless/stats.sh) · [정확 사본](../evidence/0051-0055-gotsf-audit/originals/EXT-H032-03.txt) | 전체 텍스트 정적 독해 |
| EXT-H032-04 | [dataset/wireless/wireless.csv](https://raw.githubusercontent.com/netop-team/gotsf/31b17e55a0cb6f41bfe25230db3f81567efd58f3/dataset/wireless/wireless.csv) | 고정 1026×100 값의 schema/유한성/범위·현재 pandas 날짜 파싱; 전체 공개 HF 원시 자료 대조 아님 |

코드·README·notebook의 11개 Git blob와 데이터 카드 1개를 확인했다. 원코드 실행이나 모델 import·fit·forward는 하지 않았다. 라이선스는 추가 참조 EXT-H032-02의 MIT 원문을 보존했다. 논문 원문은 재게시하지 않고 공식 링크와 저장본 identity로 연결한다.

fetch log의 성공 상태는 당시 입수 근거다. event 원문 요청의 TLS 실패도 보존한다. 다른 논문 fetch가 성공했다는 이유로 그 논문 내용을 읽은 것으로 처리하지 않는다. render log 7행 중 GOTSF의 저장 미리보기 4개만 이번에 시각 확인했다.

[주요 검수 JSON](../verification/history-032-primary-check.json)과 [인쇄 표 검수](../verification/history-032-paper-table-check.json)는 byte identity·고정 산술·읽기 범위를 기록한다. 원 예측·저자 checkpoint·정확한 원 환경을 재현한 증거가 아니다. 51/53 및 55 전체와 나머지 원본의 전수 검토는 계속 진행한다.
