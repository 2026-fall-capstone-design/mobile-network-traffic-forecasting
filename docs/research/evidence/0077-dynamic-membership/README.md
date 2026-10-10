# 동적 소속 DLM 재사용 자료

[기록](../../records/0077-dynamic-membership-dlm.md) · [출처](../../sources/history-077.md) · [구현 대조](implementation-review.md) · [원문 식별](source-identity.json)

예측 origin에서 사용할 소속을 설계할 때 DLM·EDP의 선행 원리와 저장 구현을 구분하기 위한 자료다. 22개 핵심 주장의 작성 후 원문 대조를 마쳤다. 새 모델 실험은 수행하지 않았다.

| 조건 | 확인한 상태 |
|---|---|
| 논문 판본 | 2020 arXiv v1,27쪽. 2025 출판본과 동등성 미확인 |
| 코드 판본 | bf866cefcd1f2754ee4b2ede31ff14aed79d0a7e; 저장4본문과 보완2본문 blob 일치 |
| 입력/소속 | 시계열T×(n·m), 시간별 확률. 학습구간 전체의 smoothing과 origin 배정을 구별 |
| 논문 결과 | EU·Gapminder·인공예의 과거 소속, 보고된 시간. traffic/RCTL MAE는 해당 없음 |
| 실제 실행 연결 | 논문 각 그림의 생성 코드·환경·seed·원체인 미확인 |
| PyPI판본 | 저장1.1.2와 이 commit의 동일 배포물 여부 미확인 |
| 코드 차이의 영향 | 정적 대조 항목이며 실행 오류·성능 손해·논문 기각으로 확정하지 않음 |
| 팀 접근 | 공식 고정 링크와 해시 제공; 동일바이트 장기 공용 보존은 별도 미완료 |

소속 δ와 DLM 진화 discount를 분리하고, final forecast target을 보지 않는 배정 규칙을 먼저 정의한다. 구현을 재현하려면 [대조 항목](implementation-review.md)의 계산·주석 차이와 실제 실행 버전을 확인해야 한다. 이 안내는 추가 모델 실행을 수행했다는 기록이 아니다.
