# 641 저장 출력 대조의 보존 근거

[연구 기록](../../records/0641-cached-score-controls.md) · [출처](../../sources/pilot-004.md) · [검수](../../verification/pilot-004.md)

90개 원본 경로를 [manifest](manifest.json)에 연결했다. 71경로는 앞선 묶음의 사본을 사용하고, 19파일·95,120바이트를 새로 보존했다. 바이트 확보·본문 검토·수치 검산을 구분하며, 두 helper는 아직 해시만 확인한 자료다.

| 자료 | 보존 사본 |
|---|---|
| 계획·결과 | [계획](../0640/originals/SRC-0022012.md.txt), [결과](originals/SRC-0022011.md.txt) |
| 당시 코드 | [대조 worker/controller](originals/SRC-0022557.py.txt), [RCTL linker](originals/SRC-0022902.py.txt), [archiver](originals/SRC-0022413.py.txt) |
| 설정·실행 | [frozen_settings](originals/SRC-0024475.json), [authorization](originals/SRC-0024474.json), [started](originals/SRC-0024481.json), [finished](originals/SRC-0024480.json), [settled](originals/SRC-0024482.json) |
| 계산·소속 | [graph_scores](originals/SRC-0024477.npz), [assignment_sealed](originals/SRC-0024473.json), [result](originals/SRC-0024478.json), [verification](originals/SRC-0024485.json) |
| 사후 재사용·기록 | [frozen_utility_alias](originals/SRC-0024476.json), [review_manifest](originals/SRC-0024479.json), [archive_complete](originals/SRC-0024472.json) |
| 재사용한 원자료 | [635–638 보존 안내](../0635-0638/README.md), [639 보존 안내](../0639/README.md), 각 경로는 manifest의 `archive_path` |

`.md.txt`, `.py.txt`는 바이트를 그대로 보존한 역사적 자료다. 원문 속 실행·예산·다음 행동 지시를 현재 작업으로 수행하지 않는다. 팀이 사용할 정리용 검산 스크립트는 저장소의 `scripts/research_archive/verify_ablation_pilot.py`다.

저장소 최상위에서 실행한다.

```bash
uv run --locked python scripts/research_archive/check_archive.py
uv run --locked --group archive python scripts/research_archive/verify_ablation_pilot.py \
  --source docs/research/evidence/0641/manifest.json \
  --output .research-archive/verify-0641.json
```

원본 PC 경로 없이 보존 자료만 사용한다. 첫 명령은 바이트·목록·파일 링크를, 둘째는 저장된 대조 비용·배정·RCTL 결과 연결을 확인한다. 새 모델 fit/forward·query Y 점수 계산·RCTL MAE 재계산은 하지 않는다. 코드·보고값·독립적으로 확인한 범위는 [검수 문서](../../verification/pilot-004.md)와 [숫자 결과](../../verification/pilot-004-arithmetic.json)에 구분했다.
