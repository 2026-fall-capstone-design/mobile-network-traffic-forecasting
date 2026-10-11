# H093 CCM 구현 근거

[기록](../../records/0093-ccm-code-review.md) · [출처](../../sources/history-093.md) · [검수](../../verification/history-093.md)

- [명세](manifest.json): 원소장6그룹과 기존2그룹, 새 보충 patch_layer를 구분한다.
- [보존 확인](provenance-check.json): 같은 바이트의 원본/스냅샷12경로.
- [Git 대조](git-content-correspondence.json): 저장코드4와 보충1의 blob, commit root 재구성.
- [함수 지도](function-map.json): 정적 AST 정의87개. 원코드 import/실행은 없다.
- [정적 관찰](static-observations.json): 활성 이름·입력 차원·trace 관계 및 작은 유리수 예시.
- [원81 연결 범위](packet-coverage.json): H090 이후29그룹 중14그룹 연결, 잔여15그룹.

본문 검토와 실행 검증을 구분한다. 고정 판본의 잠재 문제는 실제 실험에서 관측한 실패나 논문 수치의 원인으로 확정하지 않는다.
