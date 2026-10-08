# 08·09 원문과 실제 검토 범위

[정리 기록](../records/0008-0009-finite-sample-pooling.md), [보존 manifest](../evidence/0008-0009/manifest.json), [JSONL 매핑](../catalog/history-002-sources.jsonl).

6개 원본 경로 가운데 문서2개·코드1개는 전구간을 읽었고, JSON1개와 기존 NPZ2개는 지정 필드를 확인했다. 새 원문4개37,293bytes를 보존하고, 이미 보존한 배열2개는 같은 SHA-256 사본을 재사용한다. 목록·바이트 보존·본문 읽기·독립 수치 검증을 구분한다.

| source_id | 원본 루트 기준 경로 | 보존 사본 | 실제 읽기 |
|---|---|---|---|
| SRC-0020829 | `tmp/redesign_20260925/08_finite_sample_information_plan.md` | [원문](../evidence/0008-0009/originals/SRC-0020829.md.txt) | 전구간 1–32행 |
| SRC-0020830 | `tmp/redesign_20260925/09_additional_path_audit.md` | [원문](../evidence/0008-0009/originals/SRC-0020830.md.txt) | 전구간 1–35행 |
| SRC-0022801 | `tmp/redesign_20260925/finite_sample_information.py` | [원문](../evidence/0008-0009/originals/SRC-0022801.py.txt) | 전구간 1–118행 |
| SRC-0023577 | `tmp/redesign_20260925/results/design_data.npz` | [원문](../evidence/0008-0009/../0001-0002/originals/SRC-0023577.npz) | manifest에 명시한 JSON 필드/NPZ 배열 |
| SRC-0023580 | `tmp/redesign_20260925/results/finite_sample_information.json` | [원문](../evidence/0008-0009/originals/SRC-0023580.json) | manifest에 명시한 JSON 필드/NPZ 배열 |
| SRC-0023589 | `tmp/redesign_20260925/results/observed_risk_tables.npz` | [원문](../evidence/0008-0009/../0003-0007/originals/SRC-0023589.npz) | manifest에 명시한 JSON 필드/NPZ 배열 |

JSON의 합성 MC 평균/표준오차는 보고값을 읽었으며 원표본으로 재생성하지 않았다. 실제자료의120쌍×4 상관, 앞뒤 순위, coverage, occupancy는 저장 배열에서 다시 계산했다. `dates` object 배열은 읽지 않았고 pickle을 허용하지 않았다. 과거 코드는 `.py.txt`인 보존 자료로만 읽었다.

05 문헌 감사는 이6개 출처에 포함하지 않는다. 가까운 다섯 방법은 [history-003](history-003.md)으로 이어지며 나머지 문헌 근거의 확인·통합은 미완료다. 09의 세 외부 일차문헌은 조사 시점 목록 밖의 지정 절 검토이며 [별도 판본·범위](../verification/history-002-primary-review.json)에 기록한다. 파일 다운로드 성공만으로 전체 논문 읽기 완료를 표시하지 않는다.

원본 경로는 루트 별칭 `Tab-ICL` 기준이다. 같은 SHA의 원본·스냅샷 사본 연결은 manifest의 `exact_alias_source_ids`를 사용한다. 다른 해시 개정본을 같은 내용이라고 합치지 않는다. 보존 원문 안의 개인 경로·과거 명령·예산은 역사적 내용이며 실행하지 않는다.
