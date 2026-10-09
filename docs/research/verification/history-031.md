# H031 검수 기록

[52·54 기록](../records/0052-0054-partial-observation.md)의 [22개 주장](history-031-claims.json)을 원문·코드·저장 결과에 대조했다. [저장 수치 검사](history-031-saved-check.json)는 152개 확인·70개 numeric field를 다룬다. 한 배열을 하나의 field로 세므로 70개를 scalar 개수와 동일시하지 않는다. 7개 방법의 전체/cell/block/cell×block/half/activity MAE와 paired 변화, screening, 두 NPZ, Beijing schema를 확인했다.

[H5 입력 검사](history-031-input-check.json)는 고정 16열과 1488개 timestamp로 36개 확인을 했다. 저장 정답·척도·네 무학습 기준은 대조했고 12입력의 정적 구성을 재구성했다. 실제 실행 X·fitted object는 없으며 같은 모델을 재실행하지 않았다.

[출처·비용 검사](history-031-lineage-check.json)는 132개 확인으로 36원본 identity, 새30사본·재사용3, STK fetch6개·고정blob5개, snapshot12 metadata와 전후원장·현재prefix, 통제파일6개를 대조했다. 실패 process 비용의 별도 반영과 simple시간 이중계상 방지를 확인했다. 외부 실패 transcript 미대조·55 인쇄값의 마지막 자리 차이를 남겼다.

[문서 대조](history-031-document-check.json)는 표·claim·출처 및 저장 문서 바이트를 확인한다. 같은 정리 에이전트의 두 번째 근거 검토이며 독립 연구자의 재현 검증이 아니다. CI의 해시·링크 검사는 의미 검토와 다르다. 정리 단계의 새 모델 실행·원 연구 코드 실행·난수 생성은 0이다.

52·54의 제한된 실행 기록을 통합했다. 51·53의 1차 문헌과 55 전체 종합, 관련 보고서, 전체 원본, 모든 실패/비용, 팀 데이터·모델 접근, 최종 원본 변경 및 검색 검수는 남아 있다. 기존 audit의 pending 문구는 그 감사 시점의 상태이고 후속 비용 검수는 별도 lineage 파일에 연결했다.
