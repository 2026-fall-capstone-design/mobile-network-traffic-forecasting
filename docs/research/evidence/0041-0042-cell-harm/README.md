# 41–42 cell 손해 진단의 저장 근거

[연구 기록](../../records/0041-0042-cell-harm.md) · [출처](../../sources/history-025.md) · [manifest](manifest.json) · [검수](../../verification/history-025.md)

새 원본 7개 59,195 bytes는 바이트 그대로 보존했다. 44 원문 전체 보존은 문헌 부분 검수 완료를 뜻하지 않는다. 기존 예측·validation·design·원장 등 9개는 기존 보존본을 참조한다. 원 코드는 `.py.txt`로 보존하며 실행 대상이 아니다.

저장된 결과와 입력을 바꾸지 않고 다음 검산을 실행할 수 있다. 작업 디렉터리는 저장소 루트다. NumPy를 사용하며 원 연구 코드·model package·checkpoint를 import하거나 실행하지 않는다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_cell_harm_history.py \
  --manifest docs/research/evidence/0041-0042-cell-harm/manifest.json \
  --output .research-archive/cell-harm-check.json
```

294개 검사는 원본 identity, 13조건의 모든 cell·half 오차, 21개 저장 validation checkpoint의 membership 연결, 두 oracle·validation 선택과 비용 prefix를 확인한다. [원 결과](originals/SRC-0024832.json)에는 전체 per-cell/half 값이, [문서 표](document-tables.json)에는 본문 표시값이 있다. 읽기 쉬운 정리와 원본은 구분한다.

이 검산은 저장 숫자의 일치다. 과거 fit/forward의 독립 재현이나 새 clustering 실험이 아니다. 43/44 문헌·종합과 기존 fit 입력 객체·가중치 팀 접근 공백은 별도 미완료 범위다.
