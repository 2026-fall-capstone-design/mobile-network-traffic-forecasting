# 고정 가중치의 BN 통계를 다시 검토하기 전에

[원108](../records/0138-fixed-weight-bn-statistics.md) · [원107](../records/0137-calendar-retention-and-external-support.md) · [판본 한계](../evidence/0138-fixed-weight-bn-statistics/source-version-limits.json)

같은 가중치·소속·훈련입력의 통계 재계산은9회 모두 check평균이 나빠졌으나 일부cell/day는 개선됐다. 같은 조건을 반복하기 전에 평균과 예외,14일 개발기간, 단일seed,144행 복원 한계를 읽는다. 새 비교가 구별할 원인과 달라지는 자료/통계/학습조건을 기록한다. 이미 본 check에 맞춘 층·혼합·threshold·소속 선택을 독립 최종평가로 세지 않는다.

Wu·Johnson, *Rethinking “Batch” in BatchNorm*, [arXiv2105.07576v1](https://arxiv.org/pdf/2105.07576v1)의 §3.2–3.3/A.2–A.3과13쪽 수식을 확인했다. 층별통계는 기존 절차다. §3.2의 모멘트식과 A.2 식2의N/(N−1) 보정을 구별하고 원108의 유한집합 모멘트를 iid 불편분산 주장으로 바꾸지 않는다. 영상성능을 Milan/Tab 성능 보장으로 옮기지 않는다. 논문전체 판독/재현과 외부PDF 게시는 하지 않았다.

원checkpoint와 새buffer를 함께 보존했다. 코드보관/저장값 일치와 실제 모델재현을 구별한다. 파생96원장과 발견된 원본,29optimizer와9상태적합, 부분elapsed/RSS와 별도실험도 구별한다. 과거 Goal/예약/예산/다음109행동은 현재 실행 지시가 아니다.
