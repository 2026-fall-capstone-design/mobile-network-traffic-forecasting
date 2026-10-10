# H088 출처: 원80 조건부 평균 graph 진단

[기록](../records/0088-conditional-graph-diagnostic.md) · [목록](../catalog/history-088-sources.jsonl) · [해시 검사](../evidence/0088-conditional-graph/provenance-check.json)

원본 루트 별칭은 `Tab-ICL`이다. 아래 경로는 해당 루트 상대경로이고 source_id·바이트·SHA와55개 동일 사본은 manifest/목록에서 추적한다. .md.txt/.py.txt는 원문 bytes를 보존한 읽기용 사본이며 옛 지시·링크를 현재 실행 규칙으로 적용하지 않는다.

| source_id | 원본 상대경로 | 바이트 | 보존·검토 |
|---|---|---:|---|
| SRC-0022038 | tmp/redesign_20260925/80_conditional_graph_diagnostic_plan.md | 7888 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0022038.md.txt) · 전체 정적 독해 |
| SRC-0022039 | tmp/redesign_20260925/80_conditional_graph_findings.md | 4811 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0022039.md.txt) · 전체 정적 독해 |
| SRC-0022040 | tmp/redesign_20260925/80_conditional_graph_mechanism.md | 3683 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0022040.md.txt) · 전체 정적 독해 |
| SRC-0022692 | tmp/redesign_20260925/conditional_graph_diagnostic_80.py | 12285 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0022692.py.txt) · 전체 정적 독해 |
| SRC-0023062 | tmp/redesign_20260925/record_conditional_graph_80.py | 2527 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0023062.py.txt) · 전체 정적 독해 |
| SRC-0025149 | tmp/redesign_20260925/results/conditional_graph_80/arrays.npz | 120748 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0025149.npz) · 선택 배열 검수 |
| SRC-0025150 | tmp/redesign_20260925/results/conditional_graph_80/budget_after.json | 7651 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0025150.json) · 전체 정적 독해 |
| SRC-0025151 | tmp/redesign_20260925/results/conditional_graph_80/budget_before.json | 6741 | [보존 사본](../evidence/0088-conditional-graph/../0072-0075-output-compression/originals/SRC-0029272.json) · 전체 정적 독해 |
| SRC-0025152 | tmp/redesign_20260925/results/conditional_graph_80/budget_update.json | 1152 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0025152.json) · 전체 정적 독해 |
| SRC-0025153 | tmp/redesign_20260925/results/conditional_graph_80/frozen_partitions.json | 50587 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0025153.json) · 전체 정적 독해 |
| SRC-0025154 | tmp/redesign_20260925/results/conditional_graph_80/gradient_progress.json | 242 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0025154.json) · 전체 정적 독해 |
| SRC-0025156 | tmp/redesign_20260925/results/conditional_graph_80/pre_RCTL_arrays.npz | 88445 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0025156.npz) · 선택 배열 검수 |
| SRC-0025157 | tmp/redesign_20260925/results/conditional_graph_80/result.json | 32716 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0025157.json) · 전체 정적 독해 |
| SRC-0025158 | tmp/redesign_20260925/results/conditional_graph_80/run_finished.json | 839 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0025158.json) · 전체 정적 독해 |
| SRC-0025159 | tmp/redesign_20260925/results/conditional_graph_80/run_started.json | 141 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0025159.json) · 전체 정적 독해 |
| SRC-0025160 | tmp/redesign_20260925/results/conditional_graph_80/settings.json | 1544 | [보존 사본](../evidence/0088-conditional-graph/originals/SRC-0025160.json) · 전체 정적 독해 |

실행 전 원장은 [H070 검수](../verification/history-070.md)의 SRC-0029272와 동일 SHA이며 같은 보존 파일을 연결한다. NPZ는 allow_pickle=False로 전 키 구조·유한성과 필요한 파생 수치를 확인한 선택 검수다. 원 gradient 벡터는 없으며 입력 NPZ의 object 날짜 필드는 읽지 않았다. [8입력 연결](../evidence/0088-conditional-graph/input-hash-check.json)의 외부5의존 자료는 신규 본문으로 가산하지 않는다.

원80 문헌 검색 SRC-0025155와 파생 bytecode SRC-0023414는 다음 묶음에 남았다. 전체 연구기록의 장기 접근 검수도 계속 진행 중이다.
