# H095 DUET 코드 검수

[기록](../records/0095-duet-code-review.md) · [주장 34개](history-095-claims.json) · [작성 후 대조 10묶음](history-095-second-pass.json) · [출처](../sources/history-095.md) · [문서 검사](history-095-document-check.json)

원소장 코드 4개 전체 716행과 commit/tree JSON 2개를 읽고 주장 관련 원문을 다시 대조했다. tree는 첫 독해에서 1,085항목의 모든 필드를 손실 없는 표시로 확인했다. 작성 후에는 관련 항목과 구조·해시를 검수했으며 참조된 973개 blob 본문 전체나 전체 tree의 두 번째 독해를 뜻하지 않는다.

같은 commit에서 보충한 14파일 2,063행을 처음 읽고, PyTorch 2.4.1의 gumbel_softmax 60행을 별도로 확인했다. 작성 후 재대조는 명세에 적힌 구간에 한정한다. 원12사본·보호원본6·재참조3의 SHA와 원코드4/보충14의 Git blob, root 포함113tree를 다시 계산했다. [대수 예](../evidence/0095-duet-code/algebra-check.json)는 Fraction·scalar·정수 산술이며 모델 sampling이나 tensor 할당이 아니다.

ILI 표 근거를 실제 행으로 수정하고, RevIN의 평균/표준편차와 noisy load 조건을 정밀화했다. 확률 재매핑·유한 score 마스킹·eval sampling·설정/Drop Last의 차이는 고정 판본에 대한 정적 관찰이다. 논문 당시 실행 오류·성능 실패나 통신 트래픽 실증으로 확대하지 않았다.

같은 에이전트의 작성 후 검수이며 독립 연구자 리뷰가 아니다. 원코드 import/실행·모델 학습·추론은 0이다. 원목록 가산 대상은 코드본문4·전체JSON2이며 재참조3·보충15·파생 자료는 가산0이다. 원81의 잔여5그룹·snapshot 연혁, 다른 과거기록과 전체 통합·장기 팀 접근·최종 원본 변경/검색 검수는 남는다.
