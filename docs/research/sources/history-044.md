# H044 출처와 저장 자료별 읽은 범위

[종합 기록](../records/0051-0055-synthesis.md) · [명세](../evidence/0051-0055-synthesis/manifest.json) · [전체 범위 JSON](../evidence/0051-0055-synthesis/scope-matrix.json) · [원본 행](../catalog/history-044-sources.jsonl) · [검수](../verification/history-044.md).

최초 경로 조사 195개/97고유 묶음에서 직접 관련된 수집·렌더링 스크립트 누락을 보완해 **207경로/103고유 바이트 묶음**으로 확장했다. 98묶음은 기존 명세의 실제 read_scope를 대조했고, 신규 코드 5개 209줄을 전부 읽었다. 이름이 비슷한 파일을 동일 사본으로 처리하지 않았으며 모든 경로의 SHA256을 다시 확인했다. 이는 51–55 주변의 명시된 저장 자료 범위이며 전체 원본이나 모든 외부 의존성의 분모가 아니다.

아래 표의 판독은 과거 H029·H031–H043과 이번 H044를 연결한 상태다. 재독·동일 사본·PDF 추출문·미리보기를 새로운 독립 본문이나 실험으로 가산하지 않는다. 신규 local fulltext는 수집/렌더 코드 5개뿐이고 whole JSON·selected-only 증분은 0이다.

| 분류 | 고유 바이트 묶음 수 | 범위 |
|---|---:|---|
| 기존 정적 본문 | 27 | 기존 본문 독해 재사용. README 연결 그림은 H041/H043 후속 범위를 확인 |
| 배열 통계·접근 한계 | 1 | Beijing NPZ 모든 member 통계·hash 확인; 원소 전부의 수동 독해/팀 바이너리 접근 아님 |
| 신규 정적 코드 | 5 | 전체 본문 정적 독해; import/실행하지 않음 |
| 기존 전체 JSON | 28 | 전체 필드/항목 독해 재사용. tree 목록≠파일 본문 |
| 저장 배열 수치 검사 | 2 | 예측 member별 지표·partial/final 일치 검수; 원소 전부의 수동 열람 아님 |
| notebook 연구내용·runtime 제외 | 1 | 33 source cell·text output·PNG12개; cell0 생성 Bokeh/PyViz runtime 제외 |
| 파생 텍스트 계보 | 9 | PDF8개 추출문과 notebook source1개; 바이트상 다른 파일이며 파생 관계로 연결 |
| 과거 HTML 그림 공백 | 3 | Frontiers·Zindi·TabICL의 과거 이미지 동일성 미확인. 현재 그림/PDF로 대체하지 않음 |
| 가시 HTML·runtime 제외 | 3 | 가시 의미본문을 읽고 script/style/runtime 제외. raw HTML 전체 판독 아님 |
| 논문 본문·시각 자료 | 8 | 각 PDF 전체 본문과 도표·수식 페이지. 정확 페이지·판본은 기존 명세에 보존 |
| 파생 미리보기 | 16 | 저장 PNG16개 전체 시각 판독 이력·원 PDF page/hash 연결; 독립 연구결과 아님 |

## 자료별 연결

각 행은 대표 원본이다. snapshot을 포함한 모든 별칭 경로·크기·SHA256·기존 명세의 원 read_scope는 범위 JSON에 있다. 링크가 보존 사본으로 가는 63개는 신규5/재사용58이며, 나머지40개는 기존 공식 출처 명세로 연결한다. 공식 URL이 있다는 사실만으로 모든 팀원의 바이너리 접근을 완료 처리하지 않는다.

| 대표 source ID·파일 | 판독 분류 | 검토 이력 |
|---|---|---|
| [SRC-0021746 · 51_network_data_problem_review_plan.md](../evidence/0051-0055-gotsf-audit/originals/SRC-0021746.md.txt) | 기존 정적 본문 | H032, H033, H034, H041, H042, H043 |
| [SRC-0021765 · 52_beijing_data_schema_plan.md](../evidence/0052-0054-partial-observation/originals/SRC-0021765.md.txt) | 기존 정적 본문 | H031 |
| [SRC-0021782 · 53_telemetry_review_plan.md](../evidence/0053-moghadas-thesis/originals/SRC-0021782.md.txt) | 기존 정적 본문 | H035, H036, H037, H038, H039, H040 |
| [SRC-0021802 · 54_partial_observation_pilot_plan.md](../evidence/0052-0054-partial-observation/originals/SRC-0021802.md.txt) | 기존 정적 본문 | H031 |
| [SRC-0021824 · 55_network_and_telemetry_findings.md](../evidence/0052-0054-partial-observation/originals/SRC-0021824.md.txt) | 기존 정적 본문 | H031, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043 |
| [SRC-0023487 · assets/stkdiff_beijing_e1faed12.npz](../evidence/0052-0054-partial-observation/manifest.json) | 배열 통계·접근 한계 | H031, H041 |
| [SRC-0022525 · beijing_data_schema_52.py](../evidence/0052-0054-partial-observation/originals/SRC-0022525.py.txt) | 기존 정적 본문 | H031 |
| [SRC-0022754 · fetch_gotsf_code_51.py](../evidence/0051-0055-synthesis/originals/SRC-0022754.py.txt) | 신규 정적 코드 | H044 신규 |
| [SRC-0022764 · fetch_network_methods_51.py](../evidence/0051-0055-synthesis/originals/SRC-0022764.py.txt) | 신규 정적 코드 | H044 신규 |
| [SRC-0022765 · fetch_network_scope_51.py](../evidence/0051-0055-gotsf-audit/originals/SRC-0022765.py.txt) | 기존 정적 본문 | H032 |
| [SRC-0022780 · fetch_stkdiff_metadata_51.py](../evidence/0051-stkdiff-audit/originals/SRC-0022780.py.txt) | 기존 정적 본문 | H041 |
| [SRC-0022782 · fetch_telemetry_sources_53.py](../evidence/0051-0055-synthesis/originals/SRC-0022782.py.txt) | 신규 정적 코드 | H044 신규 |
| [SRC-0022797 · finish_network_sources_51.py](../evidence/0051-0055-synthesis/originals/SRC-0022797.py.txt) | 신규 정적 코드 | H044 신규 |
| [SRC-0022964 · partial_observation_pilot_54.py](../evidence/0052-0054-partial-observation/originals/SRC-0022964.py.txt) | 기존 정적 본문 | H031 |
| [SRC-0022965 · partial_observation_pilot_54_preflight_v0.py](../evidence/0052-0054-partial-observation/originals/SRC-0022965.py.txt) | 기존 정적 본문 | H031 |
| [SRC-0023101 · render_telemetry_sources_53.py](../evidence/0051-0055-synthesis/originals/SRC-0023101.py.txt) | 신규 정적 코드 | H044 신규 |
| [SRC-0023904 · results/beijing_schema_52/budget_before_accounting.json](../evidence/0048-0049-aggregation-recovery/originals/SRC-0000695.json) | 기존 전체 JSON | H029, H031 |
| [SRC-0023905 · results/beijing_schema_52/result.json](../evidence/0052-0054-partial-observation/originals/SRC-0023905.json) | 기존 전체 JSON | H031 |
| [SRC-0023906 · results/beijing_schema_52/run_finished.json](../evidence/0052-0054-partial-observation/originals/SRC-0023906.json) | 기존 전체 JSON | H031 |
| [SRC-0023907 · results/beijing_schema_52/run_started.json](../evidence/0052-0054-partial-observation/originals/SRC-0023907.json) | 기존 전체 JSON | H031 |
| [SRC-0023908 · results/beijing_schema_52/settings.json](../evidence/0052-0054-partial-observation/originals/SRC-0023908.json) | 기존 전체 JSON | H031 |
| [SRC-0029386 · results/partial_observation_54/budget_before_accounting.json](../evidence/0052-0054-partial-observation/originals/SRC-0029386.json) | 기존 전체 JSON | H031 |
| [SRC-0029387 · results/partial_observation_54/calls.json](../evidence/0052-0054-partial-observation/originals/SRC-0029387.json) | 기존 전체 JSON | H031 |
| [SRC-0029388 · results/partial_observation_54/predictions.npz](../evidence/0052-0054-partial-observation/originals/SRC-0029388.npz) | 저장 배열 수치 검사 | H031 |
| [SRC-0029389 · results/partial_observation_54/predictions_partial.npz](../evidence/0052-0054-partial-observation/originals/SRC-0029389.npz) | 저장 배열 수치 검사 | H031 |
| [SRC-0029390 · results/partial_observation_54/preflight_correction.json](../evidence/0052-0054-partial-observation/originals/SRC-0029390.json) | 기존 전체 JSON | H031 |
| [SRC-0029391 · results/partial_observation_54/result.json](../evidence/0052-0054-partial-observation/originals/SRC-0029391.json) | 기존 전체 JSON | H031 |
| [SRC-0029392 · results/partial_observation_54/run_finished.json](../evidence/0052-0054-partial-observation/originals/SRC-0029392.json) | 기존 전체 JSON | H031 |
| [SRC-0029393 · results/partial_observation_54/run_started.json](../evidence/0052-0054-partial-observation/originals/SRC-0029393.json) | 기존 전체 JSON | H031 |
| [SRC-0029394 · results/partial_observation_54/settings.json](../evidence/0052-0054-partial-observation/originals/SRC-0029394.json) | 기존 전체 JSON | H031 |
| [SRC-0063261 · sources/network_scope_51/Viz_Wireless.ipynb](../evidence/0051-0055-gotsf-audit/manifest.json) | notebook 연구내용·runtime 제외 | H032 |
| [SRC-0063262 · sources/network_scope_51/Viz_Wireless.source.txt](../evidence/0051-0055-gotsf-audit/originals/SRC-0063262.txt) | 파생 텍스트 계보 | H032 |
| [SRC-0063263 · sources/network_scope_51/beam_multitask_frontiers_2025.html](../evidence/0051-frontiers-beam-audit/manifest.json) | 과거 HTML 그림 공백 | H034 |
| [SRC-0063264 · sources/network_scope_51/cellular_move_abs.html](../evidence/0051-0055-network-forecasting/manifest.json) | 가시 HTML·runtime 제외 | H033 |
| [SRC-0063265 · sources/network_scope_51/cellular_move_v1.pdf](../evidence/0051-0055-network-forecasting/manifest.json) | 논문 본문·시각 자료 | H033 |
| [SRC-0063266 · sources/network_scope_51/cellular_move_v1.txt](../evidence/0051-0055-network-forecasting/manifest.json) | 파생 텍스트 계보 | H033 |
| [SRC-0063267 · sources/network_scope_51/code_fetch_log.json](../evidence/0051-0055-gotsf-audit/originals/SRC-0063267.json) | 기존 전체 JSON | H032 |
| [SRC-0063268 · sources/network_scope_51/data_provider__data_factory.py](../evidence/0051-0055-gotsf-audit/originals/SRC-0063268.py.txt) | 기존 정적 본문 | H032 |
| [SRC-0063269 · sources/network_scope_51/data_provider__data_loader.py](../evidence/0051-0055-gotsf-audit/originals/SRC-0063269.py.txt) | 기존 정적 본문 | H032 |
| [SRC-0063270 · sources/network_scope_51/experiments__exp.py](../evidence/0051-0055-gotsf-audit/originals/SRC-0063270.py.txt) | 기존 정적 본문 | H032 |
| [SRC-0063271 · sources/network_scope_51/experiments__exp_long_term_forecasting_discrete.py](../evidence/0051-0055-gotsf-audit/originals/SRC-0063271.py.txt) | 기존 정적 본문 | H032 |
| [SRC-0063272 · sources/network_scope_51/fetch_log.json](../evidence/0051-0055-gotsf-audit/originals/SRC-0063272.json) | 기존 전체 JSON | H032, H033, H034, H042 |
| [SRC-0063273 · sources/network_scope_51/gotsf_AAAI_2026.pdf](../evidence/0051-0055-gotsf-audit/manifest.json) | 논문 본문·시각 자료 | H032 |
| [SRC-0063274 · sources/network_scope_51/gotsf_AAAI_2026.txt](../evidence/0051-0055-gotsf-audit/manifest.json) | 파생 텍스트 계보 | H032 |
| [SRC-0063275 · sources/network_scope_51/gotsf_arxiv_abs.html](../evidence/0051-0055-gotsf-audit/manifest.json) | 가시 HTML·runtime 제외 | H032 |
| [SRC-0063276 · sources/network_scope_51/gotsf_arxiv_v3.pdf](../evidence/0051-0055-gotsf-audit/manifest.json) | 논문 본문·시각 자료 | H032 |
| [SRC-0063277 · sources/network_scope_51/gotsf_arxiv_v3.txt](../evidence/0051-0055-gotsf-audit/manifest.json) | 파생 텍스트 계보 | H032 |
| [SRC-0063278 · sources/network_scope_51/gotsf_card.md](../evidence/0051-0055-gotsf-audit/originals/SRC-0063278.md.txt) | 기존 정적 본문 | H032, H043 |
| [SRC-0063279 · sources/network_scope_51/gotsf_code_README.md](../evidence/0051-0055-gotsf-audit/originals/SRC-0063279.md.txt) | 기존 정적 본문 | H032, H043 |
| [SRC-0063280 · sources/network_scope_51/gotsf_code_tree.json](../evidence/0051-0055-gotsf-audit/originals/SRC-0063280.json) | 기존 전체 JSON | H032, H043 |
| [SRC-0063281 · sources/network_scope_51/gotsf_commit.json](../evidence/0051-0055-gotsf-audit/originals/SRC-0063281.json) | 기존 전체 JSON | H032 |
| [SRC-0063282 · sources/network_scope_51/gotsf_info.json](../evidence/0051-0055-gotsf-audit/originals/SRC-0063282.json) | 기존 전체 JSON | H032, H043 |
| [SRC-0063283 · sources/network_scope_51/gotsf_script_stats.py](../evidence/0051-0055-gotsf-audit/originals/SRC-0063283.py.txt) | 기존 정적 본문 | H032 |
| [SRC-0063284 · sources/network_scope_51/gotsf_script_train.py](../evidence/0051-0055-gotsf-audit/originals/SRC-0063284.py.txt) | 기존 정적 본문 | H032 |
| [SRC-0063285 · sources/network_scope_51/gotsf_tree.json](../evidence/0051-0055-gotsf-audit/originals/SRC-0063285.json) | 기존 전체 JSON | H032, H043 |
| [SRC-0063286 · sources/network_scope_51/gotsf_utils__metrics.py](../evidence/0051-0055-gotsf-audit/originals/SRC-0063286.py.txt) | 기존 정적 본문 | H032 |
| [SRC-0063287 · sources/network_scope_51/imdea_Moghadas_thesis_2026.pdf](../evidence/0053-moghadas-thesis/manifest.json) | 논문 본문·시각 자료 | H035 |
| [SRC-0063288 · sources/network_scope_51/imdea_Moghadas_thesis_2026.txt](../evidence/0053-moghadas-thesis/manifest.json) | 파생 텍스트 계보 | H035 |
| [SRC-0063289 · sources/network_scope_51/imdea_thesis_page.html](../evidence/0053-moghadas-thesis/manifest.json) | 가시 HTML·runtime 제외 | H035 |
| [SRC-0063290 · sources/network_scope_51/itu_beam_forecast_2025.pdf](../evidence/0051-0055-network-forecasting/manifest.json) | 논문 본문·시각 자료 | H033 |
| [SRC-0063291 · sources/network_scope_51/itu_beam_forecast_2025.txt](../evidence/0051-0055-network-forecasting/manifest.json) | 파생 텍스트 계보 | H033 |
| [SRC-0063292 · sources/network_scope_51/methods_fetch_log.json](../evidence/0051-0055-gotsf-audit/originals/SRC-0063292.json) | 기존 전체 JSON | H032, H033, H034 |
| [SRC-0063305 · sources/network_scope_51/previews/cellular_move_v1_p04.png](../evidence/0051-0055-network-forecasting/manifest.json) | 파생 미리보기 | H033 |
| [SRC-0063306 · sources/network_scope_51/previews/cellular_move_v1_p10.png](../evidence/0051-0055-network-forecasting/manifest.json) | 파생 미리보기 | H033 |
| [SRC-0063307 · sources/network_scope_51/previews/gotsf_AAAI_2026_p04.png](../evidence/0051-0055-gotsf-audit/manifest.json) | 파생 미리보기 | H032 |
| [SRC-0063308 · sources/network_scope_51/previews/gotsf_AAAI_2026_p07.png](../evidence/0051-0055-gotsf-audit/manifest.json) | 파생 미리보기 | H032 |
| [SRC-0063309 · sources/network_scope_51/previews/gotsf_arxiv_v3_p05.png](../evidence/0051-0055-gotsf-audit/manifest.json) | 파생 미리보기 | H032 |
| [SRC-0063310 · sources/network_scope_51/previews/gotsf_arxiv_v3_p09.png](../evidence/0051-0055-gotsf-audit/manifest.json) | 파생 미리보기 | H032 |
| [SRC-0063311 · sources/network_scope_51/previews/itu_beam_forecast_2025_p05.png](../evidence/0051-0055-network-forecasting/manifest.json) | 파생 미리보기 | H033 |
| [SRC-0063293 · sources/network_scope_51/render_log.json](../evidence/0051-0055-gotsf-audit/originals/SRC-0063293.json) | 기존 전체 JSON | H032, H033 |
| [SRC-0063294 · sources/network_scope_51/scripts__multivariate_forecasting__Wireless__train.sh](../evidence/0051-0055-gotsf-audit/originals/SRC-0063294.sh.txt) | 기존 정적 본문 | H032 |
| [SRC-0063295 · sources/network_scope_51/stkdiff_LICENSE](../evidence/0052-0054-partial-observation/originals/SRC-0063295.txt) | 기존 정적 본문 | H031, H041 |
| [SRC-0063296 · sources/network_scope_51/stkdiff_README.md](../evidence/0052-0054-partial-observation/originals/SRC-0063296.md.txt) | 기존 정적 본문 | H031, H041 |
| [SRC-0063297 · sources/network_scope_51/stkdiff_commit.json](../evidence/0052-0054-partial-observation/originals/SRC-0063297.json) | 기존 전체 JSON | H031, H041 |
| [SRC-0063298 · sources/network_scope_51/stkdiff_dataset_loader.py](../evidence/0052-0054-partial-observation/originals/SRC-0063298.py.txt) | 기존 정적 본문 | H031, H041 |
| [SRC-0063299 · sources/network_scope_51/stkdiff_fetch_log.json](../evidence/0052-0054-partial-observation/originals/SRC-0063299.json) | 기존 전체 JSON | H031, H041 |
| [SRC-0063300 · sources/network_scope_51/stkdiff_stkdiff_main.py](../evidence/0052-0054-partial-observation/originals/SRC-0063300.py.txt) | 기존 정적 본문 | H031, H041 |
| [SRC-0063301 · sources/network_scope_51/stkdiff_tree.json](../evidence/0052-0054-partial-observation/originals/SRC-0063301.json) | 기존 전체 JSON | H031, H041 |
| [SRC-0063302 · sources/network_scope_51/supplement_fetch_log.json](../evidence/0051-0055-gotsf-audit/originals/SRC-0063302.json) | 기존 전체 JSON | H032, H033 |
| [SRC-0063303 · sources/network_scope_51/utils__delta_specific_utils.py](../evidence/0051-0055-gotsf-audit/originals/SRC-0063303.py.txt) | 기존 정적 본문 | H032 |
| [SRC-0063304 · sources/network_scope_51/zindi_original_challenge.html](../evidence/0051-0055-network-forecasting/manifest.json) | 과거 HTML 그림 공백 | H033, H034 |
| [SRC-0064355 · sources/telemetry_53/fetch_log.json](../evidence/0053-moghadas-thesis/originals/SRC-0064355.json) | 기존 전체 JSON | H035, H036, H037, H038, H039, H040 |
| [SRC-0064356 · sources/telemetry_53/netnomos_NSDI2026.pdf](../evidence/0053-netnomos/manifest.json) | 논문 본문·시각 자료 | H038 |
| [SRC-0064357 · sources/telemetry_53/netnomos_NSDI2026.txt](../evidence/0053-netnomos/manifest.json) | 파생 텍스트 계보 | H038 |
| [SRC-0064366 · sources/telemetry_53/previews/imdea_thesis_p109.png](../evidence/0053-moghadas-thesis/manifest.json) | 파생 미리보기 | H035 |
| [SRC-0064367 · sources/telemetry_53/previews/imdea_thesis_p113.png](../evidence/0053-moghadas-thesis/manifest.json) | 파생 미리보기 | H035 |
| [SRC-0064368 · sources/telemetry_53/previews/imdea_thesis_p115.png](../evidence/0053-moghadas-thesis/manifest.json) | 파생 미리보기 | H035 |
| [SRC-0064369 · sources/telemetry_53/previews/netnomos_NSDI2026_p12.png](../evidence/0053-netnomos/manifest.json) | 파생 미리보기 | H038 |
| [SRC-0064370 · sources/telemetry_53/previews/sensor_selection_AAAI2016_p03.png](../evidence/0053-srsss/manifest.json) | 파생 미리보기 | H036 |
| [SRC-0064371 · sources/telemetry_53/previews/sensor_selection_AAAI2016_p06.png](../evidence/0053-srsss/manifest.json) | 파생 미리보기 | H036 |
| [SRC-0064372 · sources/telemetry_53/previews/zoom2net_SIGCOMM2024_p05.png](../evidence/0053-zoom2net/manifest.json) | 파생 미리보기 | H037 |
| [SRC-0064373 · sources/telemetry_53/previews/zoom2net_SIGCOMM2024_p07.png](../evidence/0053-zoom2net/manifest.json) | 파생 미리보기 | H037 |
| [SRC-0064374 · sources/telemetry_53/previews/zoom2net_SIGCOMM2024_p12.png](../evidence/0053-zoom2net/manifest.json) | 파생 미리보기 | H037 |
| [SRC-0064358 · sources/telemetry_53/render_log.json](../evidence/0053-moghadas-thesis/originals/SRC-0064358.json) | 기존 전체 JSON | H035, H036, H037, H038 |
| [SRC-0064359 · sources/telemetry_53/review_scope.json](../evidence/0053-moghadas-thesis/originals/SRC-0064359.json) | 기존 전체 JSON | H035, H036, H037, H038, H039, H040 |
| [SRC-0064360 · sources/telemetry_53/sensor_selection_AAAI2016.pdf](../evidence/0053-srsss/manifest.json) | 논문 본문·시각 자료 | H036 |
| [SRC-0064361 · sources/telemetry_53/sensor_selection_AAAI2016.txt](../evidence/0053-srsss/manifest.json) | 파생 텍스트 계보 | H036 |
| [SRC-0064362 · sources/telemetry_53/tabicl_imputation_docs.html](../evidence/0053-tabicl-imputation/manifest.json) | 과거 HTML 그림 공백 | H039 |
| [SRC-0064363 · sources/telemetry_53/thesis_render_log.json](../evidence/0053-moghadas-thesis/originals/SRC-0064363.json) | 기존 전체 JSON | H035 |
| [SRC-0064364 · sources/telemetry_53/zoom2net_SIGCOMM2024.pdf](../evidence/0053-zoom2net/manifest.json) | 논문 본문·시각 자료 | H037 |
| [SRC-0064365 · sources/telemetry_53/zoom2net_SIGCOMM2024.txt](../evidence/0053-zoom2net/manifest.json) | 파생 텍스트 계보 | H037 |
| [SRC-0023222 · update_budget_after_partial_observation_54.py](../evidence/0052-0054-partial-observation/originals/SRC-0023222.py.txt) | 기존 정적 본문 | H031 |
| [SRC-0023224 · update_budget_after_schema_52.py](../evidence/0052-0054-partial-observation/originals/SRC-0023224.py.txt) | 기존 정적 본문 | H031 |

H044는 기존 false scope를 덮어쓰지 않는다. GOTSF tree의 whole JSON 승격과 연결 그림, STK README 그림은 후속 검토로 연결하되 미확인인 과거 HTML 그림과 notebook runtime을 그에 편승해 완료 처리하지 않는다. source hash·로그 대조는 독립 실행 재현이 아니다.
