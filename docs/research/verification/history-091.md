# DGCformer 원문과 표시값 검수

[기록](../records/0091-dgcformer-source-review.md) · [30개 주장](history-091-claims.json) · [작성 후 대조](history-091-second-pass.json) · [문서 검사](history-091-document-check.json) · [출처](../sources/history-091.md)

논문·서지 HTML/TXT의 같은 본문과 추가 metadata·수식·주석을 확인했다. 같은 v1 PDF 14쪽을 처음 읽은 뒤, 초안 작성 후 주요 주장에 해당하는 본문·표·그림을 다시 대조했다. 실제 재독해 범위는 위 대조 기록에 남겼다. 주요 수치 검수는 표의 소수·강조 형식에 대한 비교다. 원81 당시의 판단을 보존하면서 데이터셋 서술과 학습·K 선택의 해석을 후속 보완한다.

저장소 루트에서 `python scripts/research_archive/check_dgcformer_display.py --check`를 실행하면 공개한 표시값의 동률 포함 최저 수·단독 최저 수·굵은 수와 예외를 재계산한다. 입력은 [표시값](../evidence/0091-dgcformer/displayed-table-1.json), 비교 대상은 [저장된 재계산 보고서](../evidence/0091-dgcformer/table-1-audit.json)다. 두 파일은 `docs/research/evidence/0091-dgcformer/`에 있다.

원표 전사, 수식·그림 해석, 실험 조건은 주장별 대조에서 별도로 확인했다. 같은 에이전트가 작성 후 다시 검토한 결과이며, 독립 연구 심사나 모델 학습·추론의 재현은 아니다.
