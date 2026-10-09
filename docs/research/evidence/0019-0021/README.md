# 19·20·21 저장 진단의 보존 근거

[manifest](manifest.json)는 새 원본 18개 495,076bytes와 기존 2개 재사용, 대용량/외부 자산 metadata 3개를 연결한다. Markdown와 코드는 바이트 그대로 `.md.txt`/`.py.txt`에 보존했다. [ID 기록](../../records/0019-broad-cell-identity.md)·[잔차 기록](../../records/0020-0021-target-parameterization.md)·[출처 범위](../../sources/history-013.md)를 함께 읽는다.

19/20 계획과 코드 2개, 집중도 코드 1개, 두 진단의 시작/호출/완료/summary 8JSON과 집중도 1JSON, 최종/partial 4NPZ가 새 보존 자료다. 기존 [21 종합](../0018-0021/originals/SRC-0021095.md.txt)·[시간 진단 NPZ](../0016-0017/originals/SRC-0032487.npz)·[날짜 발췌](../0001-0002/derived/h5-timestamps.json)는 중복 복사하지 않았다.

[모든 cell/day 차이](../../verification/history-013-risk-check.json)와 [수치표 전사](document-tables.json)를 재사용할 수 있다. 저장소 루트에서 `uv sync --locked --group archive` 후 다음 명령을 실행하면 H5나 원 모델 없이 저장 결과를 검산한다. 새 학습·추론·무작위 추출은 없다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_identity_target_history.py \
  --manifest docs/research/evidence/0019-0021/manifest.json \
  --output .research-archive/identity-target-verification.json
```

[H5 대조](../../verification/history-013-local-data-check.json)·[자산 출처 한계](../../verification/history-013-provenance-check.json)는 별도 검수다. portable 검사의 통과는 실제 확장 X 보존이나 원 모델의 독립 성능 재현을 뜻하지 않는다. 과거 실행 상한·재시작 지시는 현재 실험 지시가 아니다.
