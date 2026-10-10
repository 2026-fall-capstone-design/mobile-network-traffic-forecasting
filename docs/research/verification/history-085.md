# H085 검수

[기록](../records/0085-emd-cfl-code.md) · [주장 목록](history-085-claims.json) · [작성 후 원문 대조](history-085-second-pass.json)

36개 주장을7묶음으로 작성 후 대조했다. README/Python4/JSON2 전체 첫독해와, 관련 코드·논문·원79 판단의 재독해를 구분한다. 같은 에이전트의 검수를 독립 연구자 검토나 논문 실행 재현으로 표시하지 않는다.

새 원자료7그룹·14개 사본/보호원본6 SHA, Gitblob5개 및 root/src tree 재구성,18개 fit 정의와 get_wd 호출4개·K참조·집계/누적문 포함관계를 정적으로 확인했다. [구조검사](../evidence/0085-emd-cfl-code/static-observations.json)는 원코드 실행 없이 만든 AST 검사다.

검수 중 helper의 max_sample 기본값None과 호출의512 제한, SVD 최대3성분, 이미지 분류에 시간분할 해당없음, 최종 RCTL encoder를 사용할 경우의 독립성 조건을 명확히 했다. 정적 위험은 당시 관찰된 실패나 논문 수치의 원인으로 바꾸지 않았다.

원79 잔여 Toso2/검색1,실제 model/data/config/test·seed/환경/결과와 이론 전용 조건,원80 이후/이전 부분기록·장기팀접근·최종 원본 변경/대표 질문 검수는 남아 있다. 원연구 코드 import/실행·학습·추론은0이다.
