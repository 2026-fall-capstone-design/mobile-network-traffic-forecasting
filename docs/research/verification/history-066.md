# H066 검수 — 피크 평가·보정·보관 복구와 목적 비교

[69–71 기록](../records/0069-0071-peak-objective.md) · [66–68 통합](../records/0066-0068-objectives.md) · [출처](../sources/history-066.md) · [주장 대조](history-066-claims.json)

초안 작성 후 50개 주장의 근거와 제한을 원문에 다시 대조했다. 같은 에이전트의 별도 의미 검수이며 독립 심사나 원실험 재현이 아니다. 계획의 cell별 피크 U/O 미저장과 Tab 정보를 사용하는 평균 높이 맞춤을 명시했다. [문서 검사](history-066-document-check.json)는 출처·수치·문서 파일을 연결하며 PR 검토·병합은 별도 확인한다.

| 검사 | 범위와 결과 |
|---|---|
| 보존 | 55그룹·124경로, snapshot17 56사본, 수집6·렌더6 해시, 검색 로그 복구2, 보호 원본6. 323개 검사 통과 |
| 저장 수치 | 보정98개, 원결과24행·보정114행·Tab 비교6행·보정 비교48행, toy·원장·입력 연결. 7,611개 검사, 5,827개 수치 leaf 대조 통과 |
| 코드 | 과거 코드6개 전체 정적 독해·AST parse. 원코드 실행·import 0 |
| 입력 배열 | NPZ3, 총77배열의 shape·dtype·finite. 검증29블록을 조건별로 복원하고 cell당 한 번만 포함되는지 확인 |
| 독립 재현 | 수행하지 않음. 저장된 예측과 기록을 대조하는 아카이브 검수 |

[수치 결과](history-066-saved-check.json)의 보정값 98개는 정확 일치한다. 원70 진단 필드의 허용오차는 1e−12, 이전 float32 summary와 저장 학습 임계값은 1e−6다. 전체 최대 차이는 약 9.537e−8이며 float32 참조값을 포함한 수치다. 피크 조건·null cell·분모·기간·seed·같은 τ 비교를 명시한다. 원문 스크립트를 다시 실행해서 같은 출력을 얻은 검사가 아니다.

저장 사본만으로 같은 대조를 수행하려면 저장소 루트에서 다음 명령을 사용한다. 모델 checkpoint나 외부 연구 원본 폴더는 필요하지 않다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_peak_objective_history.py \
  --manifest docs/research/evidence/0069-0071-peak-objective/manifest.json \
  --output .research-archive/peak-objective-check.json
```

검사기는 보존 경로·해시를 먼저 확인하고 NPZ는 allow_pickle=False로 읽는다. scalar 분위수는 정렬과 ceil(nτ) 순위, train 임계값은 두 순서통계량의 선형 보간, toy는 정확한 유리수 산술로 계산한다. 해시 대조와 수치 대조가 의미 검수를 대신하지는 않는다.

정리 범위는 로컬 본문10·전체 JSON14의 신규 독해와 기존 자료 재사용이다. 원69·71의 기초논문 내용, 검색 원문, snapshot17의 과거 제어 문서 전체, 그 뒤 기록들은 대기 상태로 남긴다. 66–68 세 문헌의 목표 비교는 기존 검수에 기반한 통합이며 각 문헌의 실행 근거 공백을 해결한 것은 아니다. 전체 Goal은 미완료다.

새 검사기 자체도 [8개 경계 검사](history-066-verifier-check.json)로 확인했다. 손으로 계산한 불균등 피크 개수의 macro/micro·전체 분모와 경험 분위수를 대조하고, private 사본의 수치 변조·비교행 누락·NPZ 변경을 거절하는지 확인했다. 원자료는 변경하지 않았다.

후속 [H067 검수](history-067.md)는 Forecaster’s Dilemma의 저널 본문과 표현·판본을 추가 대조했다. 위 H066의 당시 범위 수치는 그대로 유지한다. 이 문헌 대조는 H066의 저장 예측 계산을 독립 재현으로 다시 세는 작업이 아니다.

[H068 검수](history-068.md)에서 DeepCog 저자본과 별도 공개 코드의 판본·비용·비교군을 추가 대조했습니다. H066의 저장 예측을 새 실험이나 독립 재현으로 다시 가산하지 않습니다.
