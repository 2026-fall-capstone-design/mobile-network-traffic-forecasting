# H051 출처와 실제 열람 범위

[팀 기록](../records/0059-0062-history-grouping.md) · [manifest](../evidence/0059-0062-history-grouping/manifest.json) · [출처 목록](../catalog/history-051-sources.jsonl)

보존/재사용 15묶음·31원본 경로와 대형 입력/가중치 metadata 2묶음·2경로를 구분한다. 새 정확 사본은 14개·167,102bytes, 기존 원장 사본 재사용은 1개다. 네 cell의 HDF5 발췌는 새 파생물이며 원본 사본 수에 넣지 않는다.

| source_id | 팀 접근 | 실제 읽은 범위 |
|---|---|---|
| SRC-0021920 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0021920.md.txt) | 전체 텍스트 정적 독해 |
| SRC-0021940 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0021940.md.txt) | 전체 텍스트 정적 독해 |
| SRC-0021961 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0021961.md.txt) | 전체 텍스트 정적 독해 |
| SRC-0021984 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0021984.md.txt) | 전체 텍스트 정적 독해 |
| SRC-0022879 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0022879.py.txt) | 전체 텍스트 정적 독해 |
| SRC-0023214 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0023214.py.txt) | 전체 텍스트 정적 독해 |
| SRC-0027861 | [보존 원문](../evidence/0059-0062-history-grouping/../0056-0058-mae-sampling/originals/SRC-0000838.json) | 전체 JSON 키·항목 독해 |
| SRC-0027862 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0027862.json) | 전체 JSON 키·항목 독해 |
| SRC-0027863 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0027863.npz) | 숫자 배열 전수 계산·날짜 문자열 정적 확인; 원소 수동 전수 독해 아님 |
| SRC-0027864 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0027864.npz) | 숫자 배열 27개 전수 대조; object 날짜 배열 없음; 원소 수동 전수 독해 아님 |
| SRC-0027865 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0027865.json) | 전체 JSON 키·항목 독해 |
| SRC-0027866 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0027866.json) | 전체 JSON 키·항목 독해 |
| SRC-0027867 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0027867.json) | 전체 JSON 키·항목 독해 |
| SRC-0027868 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0027868.json) | 전체 JSON 키·항목 독해 |
| SRC-0027869 | [보존 원문](../evidence/0059-0062-history-grouping/originals/SRC-0027869.json) | 전체 JSON 키·항목 독해 |

59/60/61/62 메모 전체 29/34/7/76줄, pilot와 회계 코드 전체 120/23줄을 읽었다. 59/61과 62의 문헌·산술 절은 역사적 계획/보고로 보존했으며, 해당 일차문헌과 산술 실행 검수를 완료한 것으로 표시하지 않는다.

settings 410줄, calls 226줄, 시작·종료, 전체 result와 두 전후 원장의 키·값·항목을 읽었다. 60 직전 원장은 H045의 SRC-0000838과 같은 바이트여서 중복 독해를 새 JSON으로 가산하지 않는다. 새 본문 6개, 새 전체 JSON 6개, 선택 수치 범위 NPZ 2개로 집계하며 후자의 개별 원소를 사람이 모두 읽었다는 뜻이 아니다.

SRC-0023485 HDF5(357,150,320bytes)의 전체 해시와 지정 4열·날짜 1,488개를 확인했다. SRC-0023488 checkpoint(114,324,594bytes)는 바이트 해시만 확인하고 모델 객체를 읽지 않았다. 두 자산의 기존 부분 상태를 유지한다. [입력 대조](../evidence/0059-0062-history-grouping/input-audit.json)에는 raw slice·scale·정답·날짜 확인과 실제 범위가 있다.

숫자 NPZ는 pickle 없이 읽었다. final의 object 날짜 배열은 NPY header와 직렬화의 64개 날짜 문자열을 정적으로 읽었으며 객체 실행/로딩은 하지 않았다. 현재 계산은 저장 출력 검산이다. 새 예측이나 독립 모델 재현이 아니다. 61 코드/결과는 [후속 H052](history-052.md)에 연결했다. ALW는 [후속 H053](history-053.md)에 연결했다. horizon 자료와 이후 기록은 미완료다.
