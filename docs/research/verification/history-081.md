# H081 원문 대조와 검수

[기록](../records/0081-ntkmtl-training-balance.md) · [주장 지도](history-081-claims.json) · [작성 후 대조](history-081-second-pass.json) · [출처](../sources/history-081.md)

11개 자료의 첫 독해를 마친 뒤 42개 주장을 작성하고, 같은 에이전트가 관련 원문 위치를 별도로 대조했다. 전체 첫 독해는 PDF 29쪽 text·visual, README 74행·Python 424/1823행, JSON 3개 전체, TXT 29쪽 대응과 원 PNG 3개다. 두 번째 검토는 주장에 쓰인 구간·수식·표·코드·metadata를 대상으로 한다. 독립 연구자 검수나 모델 실행 재현은 아니다.

출력 Jacobian과 loss gradient, 원래 출력과 weighted 출력 좌표, 평균 고유값과 코드의 trace, 기본 구현과 주석 SR/n>1, 별도 GO4ALIGN을 대조했다. 추가 배율·clipping·미사용 임시 배열·영 gradient의 미보호 조건을 실행한 실패로 단정하지 않았다. 미확보 trainer와 실제 loss·설정에 관한 결론도 제한했다.

[표시 결과](../evidence/0081-ntkmtl/reported-results.json)의 210개 값은 p7–9·26–29 확대 이미지에서 작성 후 확인했다. 전체 표의 모든 값을 전사한 것은 아니며, 포함한 수치와 해석을 연결했다. STL 대비 평균 손해, SR의 일부 normal 지표 손해, CelebA의 본문/표 차이, QM9 설정 변경 후 FAMO HOMO의 악화, 바뀐 STL 기준을 보존했다. Figure 3의 정확한 비표시 값은 복원하지 않았으며 prose variance/caption stderr 차이를 남겼다.

CityScapes의 Table 2/7 평균 순위 차이는 부록 C.2가 비교군 차이로 설명함을 확인했다. 이를 미해결 모순으로 분류하지 않았다. NYUv2 SR의 n=2 예외, 3 seeds의 stderr와 MT10 10 seeds, 설정 두 개를 동시에 바꾼 QM9 저자 재실행, 상대 epoch 시간의 적용 범위도 확인했다. 원78에 이미 있던 지적을 신규 성과로 세지 않는다.

[사본·보존 확인](../evidence/0081-ntkmtl/provenance-check.json), [Git 판본 확인](../evidence/0081-ntkmtl/static-code-version-check.json), [TXT 대응](../evidence/0081-ntkmtl/text-variant-correspondence.json), [문서·링크 검사](history-081-document-check.json)를 의미 검수와 별도로 둔다. 독립 본문 4개·전체 JSON 3개·원 이미지 3개를 구분하며, 같은 PDF의 TXT·재렌더·정확 사본은 본문 중복 가산이 없다.

남은 범위는 실제 trainer·환경·원시 결과와 장기 팀 공유, 원78의 남은 검색·접근 자료, 원79 이후와 이전 partial 범위, 실패·비용 종합 및 최종 검수다. 원본 속 과거 지시·예산·완료 문구는 역사적 내용으로만 다뤘다.
