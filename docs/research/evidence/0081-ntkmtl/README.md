# H081 NTKMTL 근거 묶음

[연구 기록](../../records/0081-ntkmtl-training-balance.md) · [출처](../../sources/history-081.md) · [주장 지도](../../verification/history-081-claims.json) · [검수](../../verification/history-081.md)

현재 학습 모델의 균형 조절과 최종 모델에 독립적인 사전 소속 결정을 구분하기 위한 자료다. 논문·저장 코드의 독해와 정적 대조만 수행했다. 과거 실행 명령이나 다음 실험 제안을 이번 작업의 지시로 사용하지 않았다.

| 파일 | 역할과 한계 |
|---|---|
| [manifest](manifest.json) | 새 자료 11개와 이전 판단 1개의 경로·SHA·사본·실제 읽은 범위 |
| [표시 결과](reported-results.json) | 선택한 표·그림의 210개 숫자. 모든 표 전체나 seed별 원시 결과가 아님 |
| [수식·그림·코드 범위](method-and-figure-scope.json) | 출력 좌표, loss gradient, 주석 SR, 그림의 미복구 값 등 |
| [고정 판본](static-code-version-check.json) | Git blob 3개, 재구성 root tree, 미확보 의존 파일 |
| [TXT 대응](text-variant-correspondence.json) | 저장 TXT 29쪽과 layout 추출의 정확 대응 |
| [원본 보존](provenance-check.json) | 사본 22개 경로·보호 원본 6개의 hash 불변 확인 |

Δm의 음수는 STL 대비 평균 개선, 양수는 평균 손해다. MR은 비교 방법 집합에 의존한다. CityScapes의 본문/부록 MR 차이는 비교군 차이로 설명되며, CelebA의 본문 최고 순위 설명과 표의 숫자 차이는 남겨 두었다. QM9에서 batch size와 scheduler patience가 함께 바뀐 저자 재실행을 이번 아카이브의 재현이나 scheduler 단독 인과 효과로 표시하지 않는다.

고정 구현은 loss gradient Gram을 사용한다. 논문의 출력 Jacobian Gram과 구분해야 한다. SR과 일반 n>1 변형은 주석 상태이며, GO4ALIGN은 별도 방법이다. 표기·구현 차이는 원78이 실제 실행한 오류나 NTKMTL 전체 성능의 반박으로 소급하지 않는다.

현재 공개 자료는 서지·고정 commit·hash와 읽을 수 있는 정리본이다. 실제 환경·trainer·seed별 결과·외부 원자료의 장기 공유는 미완료다. 저자 보고 성능을 UPC·RCTL 실험 결과로 합치지 않는다.
