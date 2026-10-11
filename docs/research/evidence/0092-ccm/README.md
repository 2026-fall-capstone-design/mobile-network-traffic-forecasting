# CCM v2의 검수 근거

[기록](../../records/0092-ccm-source-review.md) · [출처](../../sources/history-092.md) · [명세](manifest.json) · [보존 확인](provenance-check.json)

[19개 표의 표시값·강조](displayed-tables.json), [산술 대조](table-audit.json), [그림 대조](figure-review.json), [읽은 범위](read-scopes.json)를 제공한다. 평균·표준편차·동률·악화를 구분하며 M4 Avg.를 독립적인 추가 실험으로 세지 않는다. 원문의 표시값과 이번 계산 결과를 모두 남긴다.

저장소 루트에서 `python scripts/research_archive/check_ccm_display.py --check`로 표시값의 비교·집계·강조 대조를 다시 계산할 수 있다. 입력은 `displayed-tables.json`, 기대 보고서는 `table-audit.json`이다. 연구 코드, 학습 자료, 모델 실행, 네트워크 접속을 사용하지 않는다. 이 검사는 논문 실험의 재현이나 의미 검수를 대신하지 않는다.
