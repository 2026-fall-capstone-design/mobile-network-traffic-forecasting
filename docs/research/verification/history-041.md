# H041 검수: STK-Diff 생성·평가·재사용 조건

[팀 기록](../records/0051-stkdiff-audit.md) · [주장 34개](history-041-claims.json) · [정적 출처/산술 105개](history-041-primary-check.json) · [문서 대조](history-041-document-check.json) · [출처](../sources/history-041.md)

README 그림 4개와 고정 commit의 의존 텍스트 6개 647줄을 읽고, 기존 README·loader·entry·version/NPZ 검수와 연결했다. 새 로컬 전체본문은 fetch script 28줄 1개다. 정적 검사 105개 중 작은 산술 12개는 단일샘플 CRPS 분모, 명목상 대칭 분위수의 축약, station/batch·reverse-step 수를 확인한다. float64 격자 검사는 원 PyTorch float32 실행과 구별한다.

기본 생성에 과거 값 mask가 없는 점, valid_loader 미사용, batch induced graph, 그림/코드의 결합 차이, 상충 환경 pin과 비활성 분기 문제를 각각 해당 범위에만 기록했다. 정적 발견으로 논문 성능 실패·누수·최종 RCTL 이득을 단정하지 않는다. 원본 10개·NPZ 1개·보호 원장 6개와 새 공식 응답 10개의 identity를 확인하고 원문 bytes를 보존했다.

문서의 주장·출처·수치·한계를 같은 에이전트가 다시 대조했다. 저장소 검사는 링크·해시·형식·기존 Python/web 동작을 확인한다. 독립 연구자 검토, 모델 성능 재현, 원 논문/전체 repository 검증은 아니다. 새 모델·원 연구 script import/실행·pickle load·난수 생성은 0이며 전체 Goal은 미완료다.
