# 18·21 공간 진단의 보존 근거

[manifest](manifest.json)는 새 원본 7개807,071bytes와 재사용 2개의 SHA·원본 경로·동일 사본 관계·열람 범위를 연결한다. 새 원본은 18계획·21종합·공간 진단 코드·시작/완료/summary·5배열NPZ다. Markdown와 코드는 `.md.txt`/`.py.txt`로 바이트 보존했다. 당시 명령을 새 연구 실행 지시로 해석하지 않는다.

기존 [17 원문](../0016-0017/originals/SRC-0021004.md.txt)과 [시간 진단 예측](../0016-0017/originals/SRC-0032487.npz)은 중복 복사하지 않았다. H5는 metadata와 고정된 입수 근거,기존 [날짜 발췌](../0001-0002/derived/h5-timestamps.json)를 연결한다. 공간 NPZ에는 확장 X가 없으며 그 공백을 숨기지 않았다.

[정리](../../records/0018-0021-spatial-information.md)·[검산 결과](../../verification/history-012-risk-check.json)·[수치표 전사](document-tables.json)·[검수](../../verification/history-012.md)를 연결한다. 모든 cell/day 차이는 원 예측의 추가 산술이며 새로운 모델 실험이 아니다.

저장소 루트에서 `uv sync --locked --group archive` 후 다음 명령으로 저장값을 다시 검산할 수 있다. 명령은 새 학습·추론·무작위 추출을 하지 않으며 로컬 원본 H5도 요구하지 않는다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_spatial_history.py \
  --manifest docs/research/evidence/0018-0021/manifest.json \
  --output .research-archive/spatial-verification.json
```

H5대조 결과는 별도로 보존했다. Portable 검산의 통과가 원 학습 재현·실제 확장 X 복원 검증·물리적 공간 인과의 증명은 아니다.
