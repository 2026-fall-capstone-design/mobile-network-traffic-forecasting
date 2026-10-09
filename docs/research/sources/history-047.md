# H047 출처와 실제 열람 범위

[연구 기록](../records/0056-0058-tabpfn-iml.md) · [manifest](../evidence/0056-0058-tabpfn-iml/manifest.json) · [기계 판독 목록](../catalog/history-047-sources.jsonl)

원본 루트 별칭은 `Tab-ICL`이다. TabPFN IML 11개 바이트 묶음·22개 동일 사본 경로와58번 메모2경로를 연결한다. 동일 PDF의 TXT/preview는 독립 연구나 새 전체본문으로 중복 가산하지 않는다. 외부 문헌·코드는 공식 URL/고정commit·hash를 제공하고58메모는 기존 사본을 재사용한다.

| source_id | 파일 | 실제 열람·팀 접근 |
|---|---|---|
| SRC-0064428 | `TabPFN_IML_2403_10923v2.pdf` | [공식 자료](https://arxiv.org/pdf/2403.10923v2) — 12쪽 텍스트 전체/1–11쪽 시각;참고문헌12쪽 텍스트 독해;독립 재현 아님 |
| SRC-0064429 | `TabPFN_IML_2403_10923v2.txt` | [공식 자료](https://arxiv.org/pdf/2403.10923v2) — PAGE header/공백 제외 현재 PDF 추출과 전체 내용 동일;독립 가산 없음 |
| SRC-0064430 | `TabPFN_IML__README.md` | [공식 자료](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/README.md) — 전체 정적 독해;원 코드 import/실행 없음;1–123줄 |
| SRC-0064431 | `TabPFN_IML__experiments__context_optimization__analyze_results_data_shapley.py` | [공식 자료](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/experiments/context_optimization/analyze_results_data_shapley.py) — 전체 정적 독해;원 코드 import/실행 없음;1–106줄 |
| SRC-0064432 | `TabPFN_IML__experiments__context_optimization__optimize_data_shapley.py` | [공식 자료](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/experiments/context_optimization/optimize_data_shapley.py) — 전체 정적 독해;원 코드 import/실행 없음;1–123줄 |
| SRC-0064433 | `TabPFN_IML__tabpfniml__methods__data_shapley.py` | [공식 자료](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/tabpfniml/methods/data_shapley.py) — 전체 정적 독해;원 코드 import/실행 없음;1–403줄 |
| SRC-0064434 | `TabPFN_IML_arxiv_history.html` | [공식 자료](https://arxiv.org/abs/2403.10923v2) — 저장 HTML 보이는 본문/버전 이력;script/style·스크립트 실행 제외 |
| SRC-0064435 | `TabPFN_IML_commit.json` | [공식 자료](https://api.github.com/repos/david-rundel/tabpfn_iml/commits/7bd39bc2e6b2f7a16602983c01086e962db45c37) — 저장 시점 commit/repo 전체 필드;현재 통계/서명 독립 인증 아님 |
| SRC-0064436 | `TabPFN_IML_repo.json` | [공식 자료](https://api.github.com/repos/david-rundel/tabpfn_iml) — 저장 시점 commit/repo 전체 필드;현재 통계/서명 독립 인증 아님 |
| SRC-0064437 | `TabPFN_IML_tree.json` | [공식 자료](https://api.github.com/repos/david-rundel/tabpfn_iml/git/trees/200c4edd455877b2f4db99a7ec5ccef831f53cd7?recursive=1) — 112항목 path/mode/type/size/SHA와 최상위sha/truncated 대조;각항목URL·연결전체본문 미독해 |
| SRC-0064463 | `TabPFN_IML_2403_10923v2_p11.png` | [공식 자료](https://arxiv.org/pdf/2403.10923v2#page=11) — 과거11쪽preview 전체 시각 열람 |

commit/repo JSON 전체 필드를 읽었다. tree는112개항목의 path/mode/type/size/SHA와최상위sha/truncated를 대조했고 각 URL 필드·연결된 전체파일은 읽지 않았다. 저장 HTML은보이는본문/이력만 추출했다. 보존원본 SHA·alias는manifest에 연결했다. 현재 공식PDF 바이트와 저장본은 같고,4개저장텍스트 및12개추가텍스트/CSV의Gitblob이 고정tree와일치한다.

## 검수 중 추가로 연결한 자료

보충 자료는 원본 corpus의새 연구로 가산하지 않는다. 처음6개는 전체1,403줄 정적 독해,뒤6개CSV는header/M·seed집합과최종15행의seed/RC·OC AUC·차이 선택독해다.165상세행/33평균행/297평균값의자동검산은모든cell사람전수열람과다르다.

| reference_id | 고정 파일·공식 자료 | 열람 범위 |
|---|---|---|
| EXT-H047-01 | [tabpfniml/methods/interpret.py](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/tabpfniml/methods/interpret.py) | 전체 정적 텍스트 |
| EXT-H047-02 | [tabpfniml/datasets/datasets.py](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/tabpfniml/datasets/datasets.py) | 전체 정적 텍스트 |
| EXT-H047-03 | [tabpfniml/tabpfn_interpret/scripts/transformer_prediction_interface.py](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/tabpfniml/tabpfn_interpret/scripts/transformer_prediction_interface.py) | 전체 정적 텍스트 |
| EXT-H047-04 | [requirements.txt](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/requirements.txt) | 전체 정적 텍스트 |
| EXT-H047-05 | [pyproject.toml](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/pyproject.toml) | 전체 정적 텍스트 |
| EXT-H047-06 | [LICENSE](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/LICENSE) | 전체 정적 텍스트 |
| EXT-H047-07 | [experiments/context_optimization/results/data_shapley_1471_20240309_120008.csv](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/experiments/context_optimization/results/data_shapley_1471_20240309_120008.csv) | CSV headers and all 15 M=9216 seed/RC AUC/OC AUC/deltas;all M/seed sets and all mean arithmetic checked by code. Other raw metric cells not all human-read. |
| EXT-H047-08 | [experiments/context_optimization/results/data_shapley_23512_20240309_220238.csv](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/experiments/context_optimization/results/data_shapley_23512_20240309_220238.csv) | CSV headers and all 15 M=9216 seed/RC AUC/OC AUC/deltas;all M/seed sets and all mean arithmetic checked by code. Other raw metric cells not all human-read. |
| EXT-H047-09 | [experiments/context_optimization/results/data_shapley_41147_20240310_083047.csv](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/experiments/context_optimization/results/data_shapley_41147_20240310_083047.csv) | CSV headers and all 15 M=9216 seed/RC AUC/OC AUC/deltas;all M/seed sets and all mean arithmetic checked by code. Other raw metric cells not all human-read. |
| EXT-H047-10 | [experiments/context_optimization/results/data_shapley_mean_1471_20240309_120008.csv](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/experiments/context_optimization/results/data_shapley_mean_1471_20240309_120008.csv) | CSV headers and all 15 M=9216 seed/RC AUC/OC AUC/deltas;all M/seed sets and all mean arithmetic checked by code. Other raw metric cells not all human-read. |
| EXT-H047-11 | [experiments/context_optimization/results/data_shapley_mean_23512_20240309_220238.csv](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/experiments/context_optimization/results/data_shapley_mean_23512_20240309_220238.csv) | CSV headers and all 15 M=9216 seed/RC AUC/OC AUC/deltas;all M/seed sets and all mean arithmetic checked by code. Other raw metric cells not all human-read. |
| EXT-H047-12 | [experiments/context_optimization/results/data_shapley_mean_41147_20240310_083047.csv](https://github.com/david-rundel/tabpfn_iml/blob/7bd39bc2e6b2f7a16602983c01086e962db45c37/experiments/context_optimization/results/data_shapley_mean_41147_20240310_083047.csv) | CSV headers and all 15 M=9216 seed/RC AUC/OC AUC/deltas;all M/seed sets and all mean arithmetic checked by code. Other raw metric cells not all human-read. |
| EXT-H047-13 | [EXT-H047-13](https://arxiv.org/pdf/2403.10923v2) | 공식 PDF 전체 바이트 동일 |
| EXT-H047-14 | [EXT-H047-14](https://api.github.com/repos/david-rundel/tabpfn_iml/commits/7bd39bc2e6b2f7a16602983c01086e962db45c37) | 고정 commit/root tree 선택 계보 필드·112항목 대조;전체 연결 파일 미독해 |
| EXT-H047-15 | [EXT-H047-15](https://api.github.com/repos/david-rundel/tabpfn_iml/git/trees/200c4edd455877b2f4db99a7ec5ccef831f53cd7?recursive=1) | 고정 commit/root tree 선택 계보 필드·112항목 대조;전체 연결 파일 미독해 |
| EXT-H047-16 | [EXT-H047-16](https://link.springer.com/chapter/10.1007/978-3-031-63797-1_23) | 서지:2024-07-10, xAI2024/CCIS2154/465–476/DOI;출판본 유료 본문 미독해 |
| EXT-H047-17 | [EXT-H047-17](https://docs.pytorch.org/docs/2.14/generated/torch.nn.CrossEntropyLoss.html) | 현재2.14 공식API의input logits/class-index loss식;저자 실제설치버전확인 아님 |

[58 원문](../evidence/0056-0058-mae-sampling/originals/SRC-0021898.md.txt)의이전전체68줄열람을재사용하고이번TabPFN대조를추가했다.원문을고치지않는다.논문12쪽중12쪽참고문헌은텍스트만읽었고1–11쪽은시각확인했다.식1–3/표1/그림1–3과과거11쪽preview를확인했다.출판본유료본문과다른IML코드전체·modelhelper·실제가중치/config·원run재현은미완료다.

[검수](../verification/history-047.md)는이범위를제한적으로확인한다. 원문소스·보호원장6개를보존했으며원코드import/실행/forward와난수생성은0이다.
