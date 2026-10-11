# 원95 실행 비용의 근거

[기록](../../records/0125-frozen-rctl-serving-cost-baseline.md) · [명세](manifest.json) · [해시·사본](provenance-check.json) · [판독 범위](read-scopes.json) · [판본 차이](version-comparison.json) · [저장 수치 검산](saved-measurement-check.json) · [기존 입력·checkpoint 참조](input-references.json) · [남은 범위](packet-coverage.json)

새 보존 사본20개230,062bytes와 이전5개 사본을25출처로 연결했다. [5,813bytes의 원 measurements.npz](originals/SRC-0001814.npz)에는6경로의 timing·예측·origins·cell IDs가 들어 있다. numpy의 allow_pickle=False로 저장값을 읽어 수치를 대조했으며 연구 코드·모델을 실행하지 않았다. 원 연구 `.py`는 보존 텍스트로 제공한다.

가중치9개와 design_data는 원 snapshot에 복사하지 않았고 이 묶음에서도 기존 metadata만 연결한다. 장기 공유는 미완료다. 첫 raw2,002행과 작성 후1,645행을 대조한 같은 에이전트의 검수이며 독립 연구 심사·새 timing 측정이 아니다.
