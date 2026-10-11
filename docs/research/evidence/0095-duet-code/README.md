# DUET 코드 검토 근거

[기록](../../records/0095-duet-code-review.md) · [출처](../../sources/history-095.md) · [주장](../../verification/history-095-claims.json) · [검수](../../verification/history-095.md)

- [원문·보충자료 명세](manifest.json)와 [12사본 보존 확인](provenance-check.json)
- [Git blob/tree 대응](git-content-correspondence.json)와 [함수 위치](function-map.json)
- [읽은 범위](read-scopes.json), [스크립트의 설정 선언](script-settings.json), [한정된 수식·크기 계산](algebra-check.json)
- [원81 잔여 자료](packet-coverage.json)

수식 예제는 모델 sampling·훈련·추론 결과가 아니다. 메모리 수치는 특정 모양의 float32 tensor 한 개 원소값 저장 공간만 센 것이며 실제 peak가 아니다. 고정 코드와 논문의 시점을 구분하고, 과학적 실패나 당시 실행을 추정하지 않는다. 외부 원문 전체 대신 공식 고정 링크와 해시를 제공한다.
