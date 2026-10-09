# 29–32 검수 범위

[연구 기록](../records/0029-0032-resolution-diagnostic.md), [출처](../sources/history-021.md), [근거](../evidence/0029-0032-resolution/README.md).

- 원문4개·정적 코드3개를 전체 읽고, 실제 저장 CSV/예측과 계획·보고의 관계를 대조했다. 새 연구 모델 실행은 0회다.
- [저장값 검산](history-021-saved-check.json)은 번들 Python/pandas로 278개 검사, [팀용 검산](history-021-portable-check.json)은 표준 라이브러리/NumPy로 304개 검사를 수행했다. 같은 예측의 산술을 확인하며 독립 모델 재현은 아니다.
- [H5 대조](history-021-H5-check.json)는 21개 검사로 UTC+1·세cell·720시간의 집계 차이를 확인했다. 전체 원시 전처리를 검증하지 않는다.
- [오류 사본 12개](history-021-negative-check.json)는 누락 배열, 시각·정답·척도·예측·cell raw MAE·기간 순서·간격 단위·fit 수·중복 비용·CSV 행 순서의 변조를 거부했다. 변조 파일의 해시도 갱신해 단순 해시 실패만 검사하지 않았다. 원본과 보존 사본은 바꾸지 않았다.
- [고정 원격 바이트](history-021-remote-check.json)는 CSV3·README·notebook의 동일성을 확인했다. 외부 코드 실행과 성능 검증을 의미하지 않는다.
- UPC 지정 텍스트4쪽·시각3쪽, 재사용 STCNet 코드와 Dataverse API 객체 역할을 확인했다. Fig. 7 실제 축이 12까지라는 인용 정정을 남겼다.

주장별 위치와 한계는 [16개 주장 지도](history-021-primary-review.json), 최종 원문·문서 대조는 [문서 검사](history-021-document-check.json)에 있다. 같은 정리 에이전트가 수행한 검수이며 독립 과학적 심사가 아니다.

범위 밖: 외부 notebook 전체 코드/출력, 실제 fit X/객체, 원시CDR 전처리, 논문 전체와 학습 재현, 33 이후·전체 고유 내용. 29–32의 지정 기록 통합을 전체 연구 Goal 완료로 세지 않는다.
