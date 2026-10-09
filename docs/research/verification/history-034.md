# H034 검수 — Frontiers 공동 학습과 비교 경계

[팀 기록](../records/0051-frontiers-beam-audit.md)의27개 핵심 주장을 [주장 명세](history-034-claims.json)에 연결한다. [출처 검사](history-034-primary-check.json)는 원본6개·원 제어파일6개·추출/수식/현재PDF의 identity와 범위를 확인하며, [수치 검사](history-034-numeric-check.json)는 인쇄값의 비교다. [문서 검사](history-034-document-check.json)는 공개 문서와 그 출처·수치의 재대조 및 저장 해시를 기록한다.

텍스트17쪽·시각10쪽, 저장 HTML805줄과 정적으로 복구한 MathML118항목을 읽었다. 12개 display 수식을 PDF와 비교했으며 전체 증명 인증이나 저자 구현 재현을 뜻하지 않는다. 원본 사본4개 재사용, 원본metadata2개, 원 inventory 밖의 현재PDF metadata1개다. 과거 원격 그림과 현재PDF의 바이트 동일성은 미확인이다.

Table2·3·4·5의88개 지표값과 Table1의6설정 행을 확인했다. MTL의8→168 MAE감소24.27%/역방향증가32.05%, ensemble의Table2 MTL대비1.45625%/Table5기준3.65%, LSTM/ESN대비40.85%/20.30%를 원 인쇄값에서 계산했다. 같은 Table2에서 짧은 입력이 더 좋은 모델도 확인했다. 계산 수와 모델 실행 횟수를 구분한다.

원문에서 해결하지 못한 차이를 수정해 숨기지 않는다. 특히56%·LSTM0.3223·Table5 기준 행·short ensemble60%·공통45%·variance 문구, 정규화/사용 head/ESN구조/실제 입력 채널을 함께 보존했다. 초록의1.45%는 네 자리 MAE로 설명 가능하므로 큰 수치 불일치와 구분했다. Table4의0.213을 Table2의0.213631과 같은 실행이라고 가정하지 않았다.

51 source packet에 있는 Frontiers 자료를55의 당시 결론 근거로 소급하지 않았다. 같은 주최측 baseline10값이 재인용되어도 실제 test week5와week6/11이 다르므로 직접 순위를 만들지 않았다. event 원문은 접근 실패 상태이며 metadata만 확인했다.

이 검수는 원본 보존·저장 산술·출처 대조다. 새 모델 실행·원 연구 스크립트 실행·무작위 표본 생성은0회다. 51/53/55 전체·남은 고유 기록·최종 원본 변경 확인·팀 접근·검색 검수의 완료를 뜻하지 않는다.
