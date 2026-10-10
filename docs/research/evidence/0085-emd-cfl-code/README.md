# H085 EMD-CFL 구현 근거

[기록](../../records/0085-emd-cfl-code.md) · [출처](../../sources/history-085.md) · [검수](../../verification/history-085.md)

- [명세](manifest.json): 새7그룹과 기존2그룹의 출처·읽기 범위.
- [원사본 해시](provenance-check.json): 원본을 바꾸지 않은14개 경로 대응.
- [Git 내용 대조](git-content-correspondence.json):5개 저장 파일·root/src tree 바이트 대응.
- [함수 지도](function-map.json): 실행 없이 파싱한 정의 위치.
- [호출 경로](call-paths.json): 전체/부분 참여·표본·투영·최적화.
- [정적 관찰](static-observations.json): 논문과 코드의 차이 및 재사용 전 확인할 조건.

코드가 존재한다는 사실과 실제 수행·정확도·비용 재현을 구분한다. 잠재 오류 조건은 당시 발생한 실패로 바꾸지 않는다.
