# 동적 그래프·부하 분산의 재사용 자료

[연구 기록](../../records/0078-dynamic-graphs-load-balancing.md) · [원문 목록](manifest.json) · [논문 대조](paper-review.md) · [검색 범위](search-review.md)

36개 핵심 주장의 작성 후 원문 대조를 마쳤다. 아래 자료는 논문 보고값과 저장 기록의 검토이며 새 모델 실험을 포함하지 않는다.

| 자료 | 용도 |
|---|---|
| [reported-tables.json](reported-tables.json) | DynaSTar Table1/2, Liu Table2/3·Fig12/13의 370개 표시 수치와 출처 |
| [text-variant-correspondence.json](text-variant-correspondence.json) | 저장 TXT3개의 총52쪽과 PDF layout text의 대응 |
| [search-scope.json](search-scope.json) | 검색 응답11항목의 독해 범위, 당시 접근 실패와 전문 검토의 구분 |
| [주장별 근거](../../verification/history-078-claims.json) | 36개 주장에서 원문 해시·쪽·식·표 또는 저장 응답 key로 돌아가기 |

수치의 데이터·단위·평가 목적을 함께 사용한다. 도로 예측 MAE, 통신 grid 예측 오차, RL 복합 보상, 전송량, 에너지 효율은 동일 지표가 아니다. 논문 표의 불일치가 있는 곳은 값을 그대로 보존하고 `paper-review.md`의 제한과 함께 읽는다.

모델 재현을 하려면 원시 데이터·전처리·코드 판본·입력 창·seed·학습 설정·run별 결과를 추가로 확인해야 한다. 이 묶음은 이를 이미 확보했다는 증명이 아니다.
