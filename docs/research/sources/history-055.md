# H055 출처와 실제 읽은 범위

[팀 기록](../records/0063-0065-ecai-interface.md) · [명세](../evidence/0063-0065-ecai-interface/manifest.json) · [기계 판독 목록](../catalog/history-055-sources.jsonl) · [검수](../verification/history-055.md)

2026-09-26의63–65 원문은 전체 읽었지만, 이번 과학적 근거 대조는 ECAI 부분을 중심으로 한다. 다른 여섯 문헌의 본문·수치·코드와65 전체 종합은 미완료다. 과거 열람 기록은 현재의 열람 완료와 구분한다.

| source_id | 팀 접근 경로 | 실제 열람 범위 |
|---|---|---|
| SRC-0022008 | [63_residual_interface_review_plan.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022008.md.txt) | 본문·표·실행 경계·후속 질문 전체 독해 |
| SRC-0022015 | [64_conditional_transform_review_plan.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022015.md.txt) | 본문·표·실행 경계·후속 질문 전체 독해 |
| SRC-0022016 | [65_residual_and_transform_findings.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022016.md.txt) | 본문·표·실행 경계·후속 질문 전체 독해 |
| SRC-0063848 | [implementation_manifest.json](../evidence/0063-0065-ecai-interface/originals/SRC-0063848.json) | implementation_manifest JSON 전체6항목. ECAI2개 byte/commit과 대조; Heatload4개는 수집 메타데이터만 읽음. |
| SRC-0063840 | [code_discovery_manifest.json](../evidence/0063-0065-ecai-interface/originals/SRC-0063840.json) | code_discovery_manifest JSON 전체6항목. arXiv PDF406/html200 및 repo commit/tree 수집 경로 기록. 참조 대상 전체 독해 아님. |
| SRC-0022641 | [collect_residual_code_63.py](../evidence/0063-0065-ecai-interface/originals/SRC-0022641.py.txt) | collect_residual_code_63.py 전체46줄 정적독해. repo.default_branch commit→recursive tree 수집, 406 실패도 manifest에 보존. 실행하지 않음. |
| SRC-0022642 | [collect_residual_implementation_63.py](../evidence/0063-0065-ecai-interface/originals/SRC-0022642.py.txt) | collect_residual_implementation_63.py 전체37줄 정적독해. 고정commit의 selected raw code 수집 및 HTML plain text. 미선택tree내용을 읽었다고 세지 않음. 실행하지 않음. |
| SRC-0022643 | [collect_residual_sources_63.py](../evidence/0063-0065-ecai-interface/originals/SRC-0022643.py.txt) | collect_residual_sources_63.py 전체47줄 정적독해.6공개대상,용량상한·PDFsignature·본문추출/metadata저장; 실행하지 않음. |
| SRC-0023100 | [render_residual_transform_sources_65.py](../evidence/0063-0065-ecai-interface/originals/SRC-0023100.py.txt) | render_residual_transform_sources_65.py 전체37줄 정적독해.6PDF9선택쪽,1600scale,기존PNG재사용,수정후 str(dest)+.png; 실패직전판본은 저장되지 않아 추정복원하지 않음. 실행하지 않음. |
| SRC-0063849 | [manifest.json](../evidence/0063-0065-ecai-interface/originals/SRC-0063849.json) | residual_interface_63/manifest.json 전체6항목: ECAI repo와 다른문헌취득메타데이터. 개별참조본문전체검토 아님. |
| SRC-0063866 | [conditional_normalization_render_log.json](../evidence/0063-0065-ecai-interface/originals/SRC-0063866.json) | conditional_normalization_render_log.json 전체1항목. 과거5쪽PNG/해시/visually_reviewed 표기; 현재해당PNG독해를 했다는뜻 아님. |
| SRC-0063867 | [render_log.json](../evidence/0063-0065-ecai-interface/originals/SRC-0063867.json) | render_log.json 전체9항목. ECAI7/8쪽PNG byte/size는 원본과확인,다른7PNG는 로그범위만 읽음. TACTiS2p4의Popplerligaturewarning과프로세스실패를구분. |
| SRC-0063868 | [review_scope.json](../evidence/0063-0065-ecai-interface/originals/SRC-0063868.json) | review_scope.json 전체7문헌scope·검색6개·접근실패3종·렌더경로수정·과거실행0/goal미완료 확인. 과거다른문헌열람범위를 이번완료로 승계하지 않음. |
| SRC-0021257 | [28_mechanism_and_uncertainty_audit.md](../evidence/0028-mechanism-uncertainty/originals/SRC-0021257.md.txt) | H020에서 전체 읽은28번 원문66줄의 ECAI 방법·정적논리 검수를 재사용. 해당 보존본과 현재 원본/aliases 바이트를 재확인하고 후속65와 연결. 새본문가산0. |
| SRC-0063060 | [Two_stage_global_forecasting_ECAI2025.pdf](https://kar.kent.ac.uk/111229/1/FAIA-413-FAIA251157.pdf) | 표지 포함 9쪽의 본문·참고문헌 전체 독해. 시각 1/2/3/5/7/8/9쪽 직접, 4/6쪽은 같은 SHA의 H020 검수 재사용. 표1–6과 그림1–5를 포함하며 82행·530개 인쇄 숫자의 전사 대조도 완료했다. 원 실험 재현은 아니다. |
| SRC-0063061 | [ECAI PDF — 원 TXT의 추출 대상](https://kar.kent.ac.uk/111229/1/FAIA-413-FAIA251157.pdf); 원 TXT의 SHA-256·크기·원 경로는 명세에 보존 | 원TXT1068줄, PDF page wrapper제외9쪽 전부 새pypdf추출과동일. 독립본문으로중복가산하지않음. |
| SRC-0063864 | [ECAI PDF 7쪽 — 원 PNG의 내용 출처](https://kar.kent.ac.uk/111229/1/FAIA-413-FAIA251157.pdf#page=7); 원 PNG의 SHA-256·크기·원 경로는 명세에 보존 | 저장된원PNG7쪽 직접시각독해. 새120dpi렌더와별도원본. |
| SRC-0063865 | [ECAI PDF 8쪽 — 원 PNG의 내용 출처](https://kar.kent.ac.uk/111229/1/FAIA-413-FAIA251157.pdf#page=8); 원 PNG의 SHA-256·크기·원 경로는 명세에 보존 | 저장된원PNG8쪽 직접시각독해. 새120dpi렌더와별도원본. |
| SRC-0063851 | [two_stage_TS_X_I.py](https://github.com/R-jr-star/Two-stage-modelling-framework/blob/a53e223a4c01259eafe54ea8b0ea40a4ec98dff2/TS_X_I.py) | TS_X_I.py 전체287줄 정적 독해. import/실행 없음. |
| SRC-0063852 | [two_stage_TS_X_II.py](https://github.com/R-jr-star/Two-stage-modelling-framework/blob/a53e223a4c01259eafe54ea8b0ea40a4ec98dff2/TS_X_II.py) | TS_X_II.py 전체434줄 정적 독해. import/실행 없음. |
| SRC-0063853 | [two_stage_commit.json](https://api.github.com/repos/R-jr-star/Two-stage-modelling-framework/commits/a53e223a4c01259eafe54ea8b0ea40a4ec98dff2) | commit JSON 전체: 메타데이터·서명·부모·삭제된 tourism_info.csv 패치367줄 포함. 패치의 데이터는 새 실험으로 해석하지 않음. |
| SRC-0063854 | [two_stage_repo.json](https://api.github.com/repos/R-jr-star/Two-stage-modelling-framework); 과거 API 스냅샷의 해시는 명세에 보존하며 현재 응답과 동일하다는 뜻은 아님 | repo JSON 전체 메타데이터. 당시 public/license null/default main을 확인; 현재 상태로 일반화하지 않음. |
| SRC-0063855 | [two_stage_tree.json](https://api.github.com/repos/R-jr-star/Two-stage-modelling-framework/git/trees/a53e223a4c01259eafe54ea8b0ea40a4ec98dff2?recursive=1) | recursive tree JSON 전체15항목: 코드2개, datasets tree1개, M3 CSV12개. truncated false. CSV 본문 독해 아님. |

ECAI PDF는 표지 포함9쪽 전체를 읽었다. 시각은1·2·3·5·7·8·9쪽을 직접 확인하고4·6쪽은 같은 SHA-256의 H020 검수를 재사용했다. 파생 TXT의 PDF page wrapper를 제외한9쪽은 새 추출과 동일하다. 원PNG7·8쪽은 별도로 확인했다. TXT/PNG를 독립 논문이나 새 성능 실험으로 세지 않는다.

외부 공식 코드 두 개는 고정commit `a53e223a4c01259eafe54ea8b0ea40a4ec98dff2`의 raw 응답과 byte identity를 확인했다. API commit/repo/tree는 전체 저장 JSON을 읽었으며 tree의 CSV 목록 확인은 CSV 본문 열람이 아니다. 과거 tree의 sha 필드와 commit.tree.sha는 서로 다르게 기록돼 있어 동일한 tree object라고 표기를 바꾸지 않았다. 현재 repo API URL은 과거 스냅샷을 보장하지 않는다.

23고유 바이트 그룹·47물리 경로를 연결한다. 새 정확 사본13개44,090B,28번 기존사본1개,외부자료metadata9개다. 로컬 텍스트7개와 전체 JSON9개의 독해 증분은 이전catalog와 해시를 대조하며, 논문/외부코드·파생물의 범위와 분리한다. 같은 에이전트의 원문 대조이며 독립 연구자의 실험 재현이 아니다.

[H056 후속 범위](history-056.md)에서 Heatload를 추가 검수했습니다. 위 다른 여섯 문헌 미완료 표기는 H055 당시 범위이며 현재는 Heatload를 제외한 다른 다섯 문헌·65 전체 종합이 남습니다. 기존 검수 JSON은 당시 snapshot으로 보존합니다.

[H057 후속 범위](history-057.md)는KDD전체본문·표·수식·판본검수를추가합니다. 현재남은다른문헌은PLOS·GP-Copula·TACTiS-2·conditional normalization의네가지이며65전체종합은미완료입니다. 기존범위와해시는당시snapshot으로보존합니다.
