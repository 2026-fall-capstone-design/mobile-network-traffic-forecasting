# 실제 pooled context 결과를 다른 learner에 옮길 때

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

[원101](../records/0131-actual-pooled-context-and-rctl-ranking.md) · [설정 원문](../evidence/0131-actual-pooled-context-and-rctl-ranking/originals/SRC-0001982.json) · [결과 원문](../evidence/0131-actual-pooled-context-and-rctl-ranking/originals/SRC-0001984.json) · [저장 배열 검산](../evidence/0131-actual-pooled-context-and-rctl-ranking/numeric-check.json)

TabICL은 이 개발 구간에서 같은16열을 받은 Ridge/HGB보다 직접 예측 MAE가 낮았다. 같은K4 소속 둘의 전체 평균 순위는 저장 RCTL과 반대였다. 직접 예측 성능, 같은 learner에서 소속의 효과, 다른 learner의 소속 선택을 대신하는 점수는 구별한다.

| 재사용 질문 | 먼저 확인할 자료와 조건 |
|---|---|
| 실제 sample을 pooling했는가 | context168–839; K1 10,752행, K4각2,688행; 세소속의 반복 사용 |
| 같은 자료·지표인가 | 같은16cell·336query·고정scales·normalized MAE; 기존480시점의 첫336slice |
| 입력까지 같은가 | Tab/Ridge/HGB16열; RCTL은 같은기초값을8×9로 변환하고validation을early-stop에 사용 |
| 미래 정보는 어떤가 | 각query직전실측 lag를 쓰는 rolling one-step; 아직 관측되지 않은336시간 재귀 예측과 다름 |
| 전체 평균은 모든cell에 적용되는가 | 두주·cell16·day14의 paired차이와 첫주K4/global 예외 |
| 새 독립 실험인가 | 이미본개발자료·소속/RCTL결과기지·새RCTL0; frozen파일은 저장순서/무결성 증거 |
| K4가 싸다는 뜻은 무엇인가 | 이번Tabcontext평가 시간; RCTL운영비용과 전체준비·검색비용은 별도 |

공식 보관 구현4개는 [고정commit](https://github.com/soda-inria/tabicl/tree/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3)의 바이트와 일치한다. 초기4thread와 predict중n_jobs1 범위를 구별한다. context target/일부K-V 제한을 확인했지만 선정 밖 callee 전체는 미검증이다. checkpoint를 다시 실행한 성능 재현도 아니다.

앞선 [원98 pooling 목적](../records/0128-quantile-information-and-pooling-objective.md), [원99 학습 단위](../records/0129-learning-units-and-clustering-cost.md), [원100 사전학습·시간조건](pretraining-objective-and-time-conditioning.md)을 함께 읽는다. 실제 소속 결정 또는 같은 유용한 결정의 추정 비용에서 Tab이 추가하는 차이를 특정해야 같은 실험을 반복하는 일을 줄일 수 있다.

후속 [원102](../records/0132-architecture-kernel-and-joint-risk.md)은 실제context의 순위 불일치를 보완할 analytic kernel을 검토했지만 현재 RCTL 구조/초기화·Adam/MAE·target 공동분포와 비용의 연결 근거가 부족했다. [조건 안내](architecture-kernel-and-joint-risk.md)에 직접 예측의 긍정 근거, 전체 NTK 가능성과 이번 후보 보류를 함께 남겼다.

후속 [원103](../records/0133-current-evidence-and-unapproved-extension.md)은 이직접예측/소속선호차이를4쪽중간Word와완료조건감사에반영했다. [재사용조건](current-evidence-and-unapproved-extension.md)에강한기준뒤의손해·Tab결정·최종RCTL/비용연결·미승인확장을함께남겼다.
