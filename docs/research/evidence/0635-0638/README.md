# 635–638 근거 묶음

연구 기록 [635–637](../../records/0635-0637-execution-recovery.md)과 [638](../../records/0638-numeric-precision.md)의 계획·코드·로그·저장 배열을 보존한다. 304개 원본 경로가 가리키는 220개 고유 파일, 총 1,872,029바이트다. 동일한 SHA-256 사본은 하나의 보존 파일에 연결했다.

[manifest.json](manifest.json)은 source_id, 원래 상대경로, SHA-256, 보존 파일 경로, 같은 내용의 원본 ID, 검토 방식을 담는다. 원본 바이트는 바꾸지 않았다. 원래 Markdown과 Python은 각각 `.md.txt`, `.py.txt`로 보존해 과거 링크·실행 지시를 원문 텍스트로 구분한다. 이 파일들 안의 Goal·예약·다음 행동은 당시 연구기록이다.

독자가 따라갈 링크는 [출처 안내](../../sources/pilot-001.md)와 정리된 기록에 있다. 원문 안의 개인 경로나 과거 상대링크는 보존 자료의 일부이며 팀용 탐색 링크로 보정한 것이 아니다. 저장 배열의 616 원문에는 이번 검수와 무관한 예측 오차 필드도 있으며, 파일을 복사했다고 그 필드의 해석까지 검토 완료로 세지 않는다.

저장소 루트에서 잠금 파일의 `archive` 의존성 그룹으로 아래 대조를 수행할 수 있다. 원본 연구 스크립트나 모델을 호출하지 않는다.

```sh
uv run --locked --group archive python scripts/research_archive/verify_relation_pilot.py \
  --source docs/research/evidence/0635-0638/manifest.json \
  --output .research-archive/pilot-001-recheck.json
```

[실제로 실행한 검수 결과](../../verification/pilot-001-arithmetic.json)와 [검수 설명](../../verification/pilot-001.md)을 함께 확인한다. 이는 기존 저장값의 대조이며 학습 재현 성공을 뜻하지 않는다. 전체 checkpoint·runtime·원시 데이터는 이 작은 묶음에 포함하지 않았다.
