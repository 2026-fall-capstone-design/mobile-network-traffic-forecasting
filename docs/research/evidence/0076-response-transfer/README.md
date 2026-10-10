# 76의 문헌·코드·저장 수치 재사용

[전체 기록](../../records/0076-response-transfer-audit.md) · [출처](../../sources/history-075.md) · [명세](manifest.json) · [보존 검사](provenance-check.json)

44개 주장의 원문 대조와 아래 인쇄 표의 시각 재대조를 마쳤다. 아래 자료의 인쇄 수치 전사와 과거 외부 결과를 새 실험이나 독립 재현으로 세지 않는다.

- [Sobolev Table1](sobolev-table1.json), [Jacobian Tables1–5](jacobian-tables.json), [TabDistill의 main/appendix 표](tabdistill-tables.json): 그림에서 읽은 인쇄값과 조건. 인쇄된 불일치도 유지한다.
- [TabDistill 인쇄값 산술](tabdistill-printed-value-arithmetic.json): MSE 제곱근과 appendix의 단순 budget 평균. 서로 다른 집계가 같은 것인지 확인되지 않은 차이는 오류 원인을 확정하지 않는다.
- [PMLB 저장 결과·순위·요약](pmlb-saved-results.json): 커밋 JSON의 위치와 함께 원래 문자열을 보존한 파생 데이터. 27개 task, 162결과행/161유효 순위행, PyGAM SVD 실패를 포함한다.
- [PMLB 산술 대조](pmlb-arithmetic-check.json): 원 코드를 실행하지 않고 161제곱근·805순위셀·60평균/표준오차셀을 계산해 저장값과 대조했다. 논문 Table1과는 18개 반올림 순위를 연결한다.
- [커밋 읽은 범위](commit-read-scope.json): 읽은 patch61개와 남은 interaction CSV27개. 삭제 blob의 복원/해시 검사와 본문 독해를 구분한다.
- [검색 응답 분류](search-response-ledger.json), [TXT 표현 대응](TXT-format-map.json): 원문·검색 요약·동일 내용의 다른 저장 형식을 구분한다.

학습 시간 열은 저장 수치다. 삭제 코드에서 일반 모델은 fit 구간, TabPFN은 객체 생성과 fit을 잰다. 설명 질의·예측·전체 pipeline 시간과 같은 비용으로 비교할 수 없고, 실제 저장 실행이 해당 코드 판본과 같다는 확인도 남아 있다. 이 파일들의 존재는 새 모델을 실행할 지시가 아니다.
