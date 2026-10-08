# 639의 보존 근거

[연구 기록](../../records/0639-rctl-bridge.md) · [검수 범위](../../verification/pilot-002.md) · [출처 안내](../../sources/pilot-002.md)

76개 원본 경로를 SHA-256 기준 56개 고유 내용에 연결했다. 그중 638 결과 한 개는 [앞선 묶음](../0635-0638/README.md)의 사본을 참조한다. 이 폴더에 새로 저장한 파일은 55개, 1,808,047바이트다. 연구 시도나 새 학습 횟수가 아니다.

[manifest.json](manifest.json)은 원본 상대경로·source_id·SHA-256·보존 사본·정확히 같은 사본의 ID·검토 범위를 연결한다. `originals/`의 원문은 바이트를 수정하지 않았다. Markdown과 Python은 `.md.txt`, `.py.txt` 확장자로 보존한다. 원문 속 실행 지시·개인 경로·예산 변경은 과거 자료다.

| 필요한 자료 | 보존 사본 |
|---|---|
| 639 계획 / 결과 문서 | [계획](originals/SRC-0022006.md.txt), [결과](originals/SRC-0022005.md.txt) |
| 고정 설정 / 실행 계약 | [설정](originals/SRC-0023939.json), [계약](originals/SRC-0022007.json) |
| 결과 지표 / fit 기록 | [결과 JSON](originals/SRC-0023944.json), [fit 목록](originals/SRC-0023938.json) |
| 입력 / 평가 정답 | [prepared arrays](originals/SRC-0031696.npz), [evaluation](originals/SRC-0023937.npz) |
| 실행 완료 / 정산 | [완료](originals/SRC-0023946.json), [정산](originals/SRC-0023948.json) |
| 당시 검수 | [verification](originals/SRC-0023952.json) |
| 후속 검산 | [현재 검산 결과](../../verification/pilot-002-arithmetic.json) |

각 예측과 history의 사본은 manifest의 `archive_path`로 찾는다. `.pt` 모델은 역직렬화하거나 이 묶음에 복사하지 않았다. 고정 설정의 69개 의존 해시는 원본에서 모두 일치했다. 저장소 묶음에서는 포함된 44개만 다시 대조한다. 제외된 25개 의존 경로는 manifest의 `external_dependencies`와 검산 결과의 `external_dependencies_not_rechecked`에 남겼다. 이 25개 없이도 여기서 다루는 저장 예측·정답·MAE 대조를 실행할 수 있다.

저장소 최상위 폴더에서:

```bash
uv run --locked --group archive python scripts/research_archive/verify_rctl_pilot.py \
  --source docs/research/evidence/0639/manifest.json \
  --output .research-archive/recheck-0639.json
```

이 명령은 과거 학습 코드를 import하거나 실행하지 않는다. 저장된 배열, 메타데이터, 학습 history의 지정 필드와 학습 함수의 정적 텍스트를 비교한다. 원자료에서 입력을 다시 만들거나 모델을 재학습하는 명령은 아니다. 본문 전체를 읽은 자료와 지정 필드만 검사한 자료를 구분한 [출처 목록](../../catalog/pilot-002-sources.jsonl)을 참고한다.
