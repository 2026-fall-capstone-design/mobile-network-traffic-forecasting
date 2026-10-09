# 19·20·21의 출처와 읽은 범위

[ID 진단](../records/0019-broad-cell-identity.md)·[잔차 진단](../records/0020-0021-target-parameterization.md)·[manifest](../evidence/0019-0021/manifest.json)·[목록](../catalog/history-013-sources.jsonl)·[검수](../verification/history-013.md)를 연결한다.

새 원본18개495,076bytes를 바이트 보존하고 기존21종합·시간진단NPZ2개를 재사용했다. 새 전체 텍스트5개,전체 JSON9개,전체 수치 배열 파일4개다. 원문 줄 번호는 해당 SHA의 UTF-8 `splitlines()` 1기준이다. 코드와 과거명령은 읽기용 자료이며 실행/import하지 않았다.

| Source ID | 원본 루트 아래 경로 | 실제 열람·대조 범위 |
|---|---|---|
| SRC-0021049 | `tmp/redesign_20260925/19_broad_cell_information_plan.md` | 전체31행 정적 열람 |
| SRC-0021073 | `tmp/redesign_20260925/20_target_parameterization_plan.md` | 전체25행 정적 열람 |
| SRC-0022531 | `tmp/redesign_20260925/broad_cell_information_diagnostic.py` | 전체110행 정적 열람 |
| SRC-0023197 | `tmp/redesign_20260925/target_parameterization_diagnostic.py` | 전체83행 정적 열람 |
| SRC-0023187 | `tmp/redesign_20260925/summarize_error_concentration.py` | 전체55행 정적 열람 |
| SRC-0023579 | `tmp/redesign_20260925/results/error_concentration.json` | JSON 전체 키·값 |
| SRC-0024349 | `tmp/redesign_20260925/results/broad_cell_information/calls.json` | JSON 전체 키·값 |
| SRC-0024352 | `tmp/redesign_20260925/results/broad_cell_information/run_finished.json` | JSON 전체 키·값 |
| SRC-0024353 | `tmp/redesign_20260925/results/broad_cell_information/run_started.json` | JSON 전체 키·값 |
| SRC-0024354 | `tmp/redesign_20260925/results/broad_cell_information/summary.json` | JSON 전체 키·값 |
| SRC-0032380 | `tmp/redesign_20260925/results/target_parameterization/calls.json` | JSON 전체 키·값 |
| SRC-0032383 | `tmp/redesign_20260925/results/target_parameterization/run_finished.json` | JSON 전체 키·값 |
| SRC-0032384 | `tmp/redesign_20260925/results/target_parameterization/run_started.json` | JSON 전체 키·값 |
| SRC-0032385 | `tmp/redesign_20260925/results/target_parameterization/summary.json` | JSON 전체 키·값 |
| SRC-0024350 | `tmp/redesign_20260925/results/broad_cell_information/predictions.npz` | NPZ:all_numeric_arrays |
| SRC-0024351 | `tmp/redesign_20260925/results/broad_cell_information/predictions_partial.npz` | NPZ:all_numeric_arrays |
| SRC-0032381 | `tmp/redesign_20260925/results/target_parameterization/predictions.npz` | NPZ:all_numeric_arrays |
| SRC-0032382 | `tmp/redesign_20260925/results/target_parameterization/predictions_partial.npz` | NPZ:all_numeric_arrays |
| SRC-0021095 | `tmp/redesign_20260925/21_diagnostic_synthesis.md` | 전체72행 정적 열람;이번31–54·65–72행의지정주장,문헌·누적원장미완료 |
| SRC-0032487 | `tmp/redesign_20260925/results/temporal_validity/predictions.npz` | NPZ:X,Y,times,cell_ids,scales |

대용량 H5 SRC-0023485는 전체 SHA/size와 `data.shape`, `idx[:1008]`, 고정 32cell의 `data[:1008,indices,2]`를 읽었다. 자기 정규화·정답·최근 입력·과거 통계와 날짜를 44개 항목으로 대조했다. static 통계 최대 차는 6.661338147750939e-16이다. 실제 확장 X가 따로 저장돼 있지는 않다.

설치 metadata SRC-0047644의 1–35행에서 Name/Version 2.2.0을 재확인하고 전체 SHA/size를 대조했다. checkpoint SRC-0023488은 이번 SHA/size만 대조했으며 모델을 로드하지 않았다. 기존 [공식 TabICL 검수](../verification/history-005-official-check.json)의 고정 upstream와 config 확인을 재사용한다. 현재 동일 바이트와 당시 실제 로딩은 별개이며 실행별 해시는 없다. 팀용 입수 근거는 manifest의 primary_sources에 있다.

22 본문 22행은 앞서 읽었으나 일차 문헌 검수 완료로 세지 않았고 이번 새 보존 자료에 넣지 않았다. 21 문헌과 누적 비용, 393 공간 후속 및 나머지 고유 기록은 계속 처리할 대상이다.
