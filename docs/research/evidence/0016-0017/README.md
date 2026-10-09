# 16–17 시간 유효성 진단의 보존 근거

[기록](../../records/0016-0017-temporal-validity.md)·[열람 범위](../../sources/history-010.md)·[검수](../../verification/history-010.md)·[manifest](manifest.json)를 연결한다. 새 원문8개4,821,210바이트를 그대로 보존했고 기존 원문2개는 사본을 늘리지 않고 재사용한다. 대용량 H5는 고정 공식 주소·해시·로컬 지정 구간 검수로 연결한다.

| 자료 | 팀에서 열 수 있는 근거 | 역할 |
|---|---|---|
| 계획16·판단17 | [16](originals/SRC-0020991.md.txt), [17](originals/SRC-0021004.md.txt) | 당시 질문·개발 범위·정책·판단. 17의 세 문헌 일차 방법은 별도 미검수 |
| 원 구현 | [temporal_validity_diagnostic.py](originals/SRC-0023201.py.txt) | 학습 구간·입력·고정 선택·측정 범위. 읽기 자료로 보존했으며 실행하지 않음 |
| 시작·완료 | [started](originals/SRC-0032490.json), [finished](originals/SRC-0032489.json) | 계획 해시·cell·seed·설정,768fit 및 보고 시간 |
| 저장 요약 | [summary](originals/SRC-0032491.json) | 전체·cell·주·고정 선택·기존/추가cell·단순 예측 비교 |
| 최종 배열 | [predictions](originals/SRC-0032487.npz) | pred/y/naive/cell_ids/origins/scales/X/Y/times의9개 수치 배열 |
| 주별 checkpoint | [predictions_partial](originals/SRC-0032488.npz) | pred/y/naive가 최종 배열과 모두 같음. 파일 이름만으로 미완료 판정하지 않음 |
| 앞선 판단·기존16cell | [15 원문](../0013-0015/originals/SRC-0020972.md.txt), [observed-risk 배열](../0003-0007/originals/SRC-0023589.npz) | 기존 보존2개 재사용. 뒤 배열에서는cell_ids만 읽음 |
| 시간축 | [기존 H5 날짜 발췌](../0001-0002/derived/h5-timestamps.json) | 첫1,344시간을 원 H5 idx에 다시 대조한 파생 자료 |

`.md.txt`와 `.py.txt`는 바이트 보존 사본이다. 그 안의 과거 실행 지시·개인 경로를 이번 작업 명령이나 팀 사용 경로로 삼지 않는다. NPZ는 `allow_pickle=False`로 열었다. 날짜별 집계·반례는 원 summary의 필드가 아니라 시간별 저장 예측에서 정리 중 계산한 산술이며, [검산 JSON](../../verification/history-010-risk-check.json)에 전체 cell/day/week 값이 있다. [문서 표](document-tables.json)는 기록에 표시한25개 수치 행을 연결한다.

동일 원 H5의357,150,320바이트·SHA-256·고정7z입수 URL·압축 member 동일성은 manifest에 있다. [초기 데이터 출처](../../sources/pilot-006.md)와 [이번 로컬 검수](../../verification/history-010-local-data-check.json)를 함께 확인한다. H5 전체나 모델을 저장소에 다시 올리지 않았으며 CI는 저장 배열·기존 날짜 발췌만 검사한다. 이번 정리에서 모델 학습·추론·무작위 선택·원 연구 코드 실행은0이다.
