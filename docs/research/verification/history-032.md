# H032 검수 — GOTSF의 지표·구현·재현 조건

[팀 기록](../records/0051-0055-gotsf-audit.md)과 [출처](../sources/history-032.md)의 24개 핵심 주장을 [원문 대조표](history-032-claims.json)에 연결했다. 새 모델 실행·원코드 실행·난수 생성은 0이다. 51·55의 GOTSF 부분만 통합한다.

두 PDF 23쪽의 텍스트와 모든 그림·표가 있는 14쪽을 읽고, 공식 코드 9개·README/card 텍스트·notebook 연구 source와 저장 출력을 정적으로 확인했다. 181개 tree 항목은 metadata 파싱이며 전체 구현 검토가 아니다. README/card 연결 그림, cell0의 생성 runtime JS, 전체 HF 공개 CSV는 해당 읽기 범위에 넣지 않았다.

[주요 검사](history-032-primary-check.json)는 원본 34경로·보존 23사본·기존 1사본·추가 참조4개와 원 연구 제어 파일6개를 대조했다. notebook source33개·PNG12개, code/card Git blob12개·추가 blob4개를 연결한다. 현재 pandas 날짜 변환은 고정 저장값 검사이며 원 loader 실행이나 원 환경 재현이 아니다.

[인쇄 표 검사](history-032-paper-table-check.json)는 양쪽 판본 Table 1의 696개 인쇄 숫자 순서, 100개 policy 평균의 산술·반올림 허용 범위, 선택한 18개 값과 9개 정책 비교를 다룬다. BLW DLinear DL의 인쇄 평균 54.0과 8행 평균 54.5의 차이는 양쪽 이미지에서도 확인돼 미해결로 보존했다. 55.8%의 최선 정책 이득을 다른 정책이나 단일 global 예측의 MAE 개선으로 옮기지 않는다.

회귀 손실의 MAE·제곱 분기, validation L1, 실제 helper와 미사용 helper, zero-mask 분모, stats의 명시적 bounds를 확인했다. 원논문과 shell의 설정 차이, notebook의 서로 맞지 않는 source·저장 출력과 IndexError, 에너지 simulation의 단위 공백을 보존했다. 없는 근거를 추정 결과로 채우지 않았다.

[문서 검사](history-032-document-check.json)는 작성된 숫자·주장·출처·범위와 문서 해시를 검증한다. 저장소 CI의 바이트·링크 검사는 의미 검수나 저자 성능 재현을 대체하지 않는다. 전체 원본, 다른 51·53 문헌, 55 전체 종합, 원 예측·환경·자료 대응과 최종 검색 검수는 계속 진행한다.
