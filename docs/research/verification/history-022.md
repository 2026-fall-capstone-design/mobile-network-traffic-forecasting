# 33–35 검수 범위

[연구 기록](../records/0033-0035-process-fit-gap.md) · [출처](../sources/history-022.md) · [근거](../evidence/0033-0035-frozen-fit/README.md)

- 메모 3개·정적 코드 3개 전체, 작은 JSON 4개 전체를 읽었다. summary/partial/NPZ의 선택 범위와 재사용 7개는 별도 집계한다.
- [원본 저장값 검사](history-022-saved-check.json) 794개와 [팀용 검사](history-022-portable-check.json) 811개가 저장 지표·입력·집계·비용을 확인했다. 같은 산술에서 발전한 코드이며 독립 알고리즘 검증이나 모델 재현으로 부르지 않는다.
- [정적 구조 산술](history-022-parameter-check.json)은 parameter·buffer 크기를 원 코드와 대조한다. 실제 checkpoint tensor를 읽거나 실행하지 않았다.
- [오류 사본 검사](history-022-negative-check.json)는 예측 누락/수정·정답·비유한값·cell순서·지표·step·parameter·불변flag·중복/중첩비용·checkpoint metadata의 12변조를 거부했다. 파일 해시를 함께 갱신하여 단순 해시 실패에만 기대지 않았다. 이후 ledger used 값을 바꿔도 초기 prefix 계산이 유지되는 정상 사례 1개도 확인했다.
- Butera v1은 지정 텍스트 14쪽·시각 4쪽, UPC는 PDF8/9와 Fig7 확대를 확인했다. 원 PNG 3개를 직접 비교했다. 전체 논문·저자 학습 코드는 미완료다.
- 원 UPC Fig7을 10 포함으로 읽었던 정리 오기를 본문·근거에 이어 과거 시도 색인에서도 정정했다. 35 원문 자체는 1·2·4·6·8·12로 정확했다.

주장 14개와 표 23행은 [주장 지도](history-022-primary-review.json)·[문서 대조](history-022-document-check.json)에 연결한다. 검수는 같은 정리 에이전트가 수행하며 자동 검사가 문장의 과학적 의미나 실제 과거 실행을 독립 입증하지 않는다. 새 모델 실행은 0회다.

가중치 29개 팀 접근, 실제 forward X/상태의 독립 재현, 전체 실패 비용·논문 고유 내용·36 이후/전체 기록 통합은 남아 있다. 이 묶음의 검수·PR 병합을 전체 연구 아카이브 완료로 집계하지 않는다.
