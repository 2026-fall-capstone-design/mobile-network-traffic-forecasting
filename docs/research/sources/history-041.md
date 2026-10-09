# H041 출처와 실제 읽은 범위

[팀 기록](../records/0051-stkdiff-audit.md) · [검수](../verification/history-041.md) · [manifest](../evidence/0051-stkdiff-audit/manifest.json) · [로컬 원본 10행](../catalog/history-041-sources.jsonl)

H031/H032에서 읽은 원본 9개를 재사용하고, 새 로컬 전체본문은 fetch script 28줄 1개다. 아래 범위는 실제 읽기와 저장근거 대조이며 원 연구 코드 실행은 없다. 과거 H031의 그림/전체 구현 미검토 표시는 당시 범위로 보존하고 현재 후속 읽기를 여기에 연결한다.

| 원본 | 현재 범위 | 팀 사본 |
| --- | --- | --- |
| SRC-0021746 `tmp/redesign_20260925/51_network_data_problem_review_plan.md` | 기존 전체본문/JSON 읽기 재사용;STK-Diff 관련 경로 후속 대조 | [보존본](../evidence/0051-stkdiff-audit/../0051-0055-gotsf-audit/originals/SRC-0021746.md.txt) |
| SRC-0021824 `tmp/redesign_20260925/55_network_and_telemetry_findings.md` | 기존 전체본문/JSON 읽기 재사용;STK-Diff 관련 경로 후속 대조 | [보존본](../evidence/0051-stkdiff-audit/../0052-0054-partial-observation/originals/SRC-0021824.md.txt) |
| SRC-0063295 `tmp/redesign_20260925/sources/network_scope_51/stkdiff_LICENSE` | 기존 전체본문/JSON 읽기 재사용;STK-Diff 관련 경로 후속 대조 | [보존본](../evidence/0051-stkdiff-audit/../0052-0054-partial-observation/originals/SRC-0063295.txt) |
| SRC-0063296 `tmp/redesign_20260925/sources/network_scope_51/stkdiff_README.md` | 기존 전체본문/JSON 읽기 재사용;STK-Diff 관련 경로 후속 대조 | [보존본](../evidence/0051-stkdiff-audit/../0052-0054-partial-observation/originals/SRC-0063296.md.txt) |
| SRC-0063297 `tmp/redesign_20260925/sources/network_scope_51/stkdiff_commit.json` | 기존 전체본문/JSON 읽기 재사용;STK-Diff 관련 경로 후속 대조 | [보존본](../evidence/0051-stkdiff-audit/../0052-0054-partial-observation/originals/SRC-0063297.json) |
| SRC-0063298 `tmp/redesign_20260925/sources/network_scope_51/stkdiff_dataset_loader.py` | 기존 전체본문/JSON 읽기 재사용;STK-Diff 관련 경로 후속 대조 | [보존본](../evidence/0051-stkdiff-audit/../0052-0054-partial-observation/originals/SRC-0063298.py.txt) |
| SRC-0063299 `tmp/redesign_20260925/sources/network_scope_51/stkdiff_fetch_log.json` | 기존 전체본문/JSON 읽기 재사용;STK-Diff 관련 경로 후속 대조 | [보존본](../evidence/0051-stkdiff-audit/../0052-0054-partial-observation/originals/SRC-0063299.json) |
| SRC-0063300 `tmp/redesign_20260925/sources/network_scope_51/stkdiff_stkdiff_main.py` | 기존 전체본문/JSON 읽기 재사용;STK-Diff 관련 경로 후속 대조 | [보존본](../evidence/0051-stkdiff-audit/../0052-0054-partial-observation/originals/SRC-0063300.py.txt) |
| SRC-0063301 `tmp/redesign_20260925/sources/network_scope_51/stkdiff_tree.json` | 기존 전체본문/JSON 읽기 재사용;STK-Diff 관련 경로 후속 대조 | [보존본](../evidence/0051-stkdiff-audit/../0052-0054-partial-observation/originals/SRC-0063301.json) |
| SRC-0022780 `tmp/redesign_20260925/fetch_stkdiff_metadata_51.py` | 신규 전체28줄;원 script 미실행 | [보존본](../evidence/0051-stkdiff-audit/originals/SRC-0022780.py.txt) |

Beijing NPZ `SRC-0023487`은 H031의 전체 member 통계/Gitblob 검수를 재사용하며 새 배열 실험이나 새 고유 metadata 읽기로 가산하지 않는다. SHA256은 `59def18b603d5d2a293af279cf2fe2dd3b2634de3c0930bf0cbabf8142ecf64a`다. [고정 원본](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/traffic_data/beijing.npz)을 받은 뒤 크기와 해시를 확인해야 한다. 대용량 원자료의 영구 팀 접근 완료를 주장하지 않는다.

## 고정 commit의 추가 자료

commit `e1faed12aa7abb33d801fe9483026769ffaeeed3`. 아래 10개 응답은 총593,839바이트이며 저장 tree의 Git blob SHA1과 일치한다. 원래 파일을 수정하지 않고 개인 작업 영역에 보존했다. 공개 저장소에는 URL·SHA256·크기·Gitblob·읽은 범위 metadata를 기록한다. MIT 고지는 [당시 LICENSE](../evidence/0052-0054-partial-observation/originals/SRC-0063295.txt)에 남아 있다.

| ID | 고정 원본 | 읽은 범위 |
| --- | --- | --- |
| EXT-H041-01 | [introduce_figs/framework1.png](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/introduce_figs/framework1.png) | 그림 전체 시각 열람 |
| EXT-H041-02 | [introduce_figs/flowchart.png](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/introduce_figs/flowchart.png) | 그림 전체 시각 열람 |
| EXT-H041-03 | [introduce_figs/TE_module.png](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/introduce_figs/TE_module.png) | 그림 전체 시각 열람 |
| EXT-H041-04 | [introduce_figs/sc_module.png](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/introduce_figs/sc_module.png) | 그림 전체 시각 열람 |
| EXT-H041-05 | [config/base.yaml](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/config/base.yaml) | 전체 26줄;import/실행 없음 |
| EXT-H041-06 | [main_model_upload.py](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/main_model_upload.py) | 전체 137줄;import/실행 없음 |
| EXT-H041-07 | [diff_model.py](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/diff_model.py) | 전체 312줄;import/실행 없음 |
| EXT-H041-08 | [utils.py](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/utils.py) | 전체 141줄;import/실행 없음 |
| EXT-H041-09 | [requirements.txt](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/requirements.txt) | 전체 10줄;import/실행 없음 |
| EXT-H041-10 | [res_plot.py](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/res_plot.py) | 전체 21줄;import/실행 없음 |

투명 PNG의 검정 글씨가 기본 검수 화면에서 가려져 원본 픽셀을 흰 배경에 합성한 개인 검수용 preview로 4개 전체를 다시 읽었다. 원본 bytes는 변경하지 않았으며 preview를 원문으로 배포하지 않는다. 6개 텍스트 합계는647줄이다. 논문 PDF 본문·성능표, 두 공간 NPZ의 실제 값, UKG 구축 자료, 설치 및 학습 성공 여부는 검수하지 않았다.

`citydata/dis_nor_beijing.npz`, `citydata/poi_nor_beijing.npz`는 각각7,373,060바이트라는 tree metadata만 읽었다. Gitblob SHA1은 각각 `4b5733006266cc50fbdc216f2ffc9d2ff6165f4d`, `2c848859b3caf81cfcdf6b3a00ba9038845ff10b`다. 다운로드·내용 열람·모델 import를 하지 않았다. 과거51 event 접근과55 종합도 미완료다.
