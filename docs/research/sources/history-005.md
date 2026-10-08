# history-005 — 공식 구현·초기 호출의 실제 열람 범위

05 중 공식 TabICL·자산·초기 출력 부분의 출처다. [manifest](../evidence/0005-official/manifest.json), [기계 판독 목록](../catalog/history-005-sources.jsonl), [주장별 대조](../verification/history-005-primary-review.json)를 함께 사용한다. 줄 번호는 보관 UTF-8 텍스트를 `splitlines`로 나눈1-based 위치다.

| source_id | 자료 | 실제 읽은 범위 |
|---|---|---|
| SRC-0047585 | 공식 forecast `_engine.py`,114행 | 1–114 전체 |
| SRC-0047586 | 공식 forecast `_forecaster.py`,346행 | 1–346 전체. 하위 의존 파일 전체를 읽었다는 뜻은 아님 |
| SRC-0047573 | 공식 `_sklearn/regressor.py`,765행 | 230–765: constructor·load·fit·cache·predict |
| SRC-0047553 | 공식 `_model/tabicl.py`,913행 | 1–83,149–227,524–614,873–913: 구조·constructor·출력 통계 |
| SRC-0047542 | 공식 `_model/embedding.py`,892행 | 208–245,340–400,580–666: feature grouping·Y embedding·inference 연결 |
| SRC-0047550 | 공식 `_model/quantile_dist.py`,1543행 | 248–282,544–593,649–722,1478–1543: 단조 보정·기본 격자·ICDF·wrapper |
| SRC-0047644 | 설치 `tabicl-2.2.0.dist-info/METADATA` | 1–35의 Name·Version. 전체 metadata/라이선스 검토 아님 |
| SRC-0023488 | 회귀 checkpoint | 전체 파일 해시, `refactored_model/data.pkl`의 config byte73791–74475와25개 단순 설정값. tensor 내용 미검토 |
| SRC-0023489 | 공식 소스 ZIP | 전체 파일 해시와 위 여섯 코드 member의 바이트. 압축 전체 본문 미검토 |

공식 raw·runtime·ZIP의6파일 바이트 일치와 checkpoint의 공식 LFS 해시·크기 일치를 [별도 저장](../verification/history-005-official-check.json)했다. `pickletools`로 config의 문자열·수치·불리언과 내부 참조를 읽었고 pickle 실행·torch import·모델 로드·추론은 하지 않았다. opcode73791–74475는 압축 member를 푼 데이터의 위치이며 checkpoint 파일 자체의 물리 offset이 아니다.

기존 보존 근거8개는 새 사본을 만들지 않고 재사용했다.

| source_id | 이번 대조 범위 | 팀 경로 |
|---|---|---|
| SRC-0020826 | 05 전체1–69 재확인. 이번 통합은 공식 기능·초기 호출 부분 | [원문](../evidence/0005/originals/SRC-0020826.md.txt) |
| SRC-0022507 | 자산 manifest 전체1–41 | [manifest](../evidence/0001-0002/originals/SRC-0022507.json) |
| SRC-0023116 | B1 코드63–92 | [코드](../evidence/0003-0007/originals/SRC-0023116.py.txt) |
| SRC-0022942 | B2 코드1–30 | [코드](../evidence/0003-0007/originals/SRC-0022942.py.txt) |
| SRC-0023601 | B1 호출16행의cell·context/query·ensemble·fit/predict 시간·quantiles_returned | [로그](../evidence/0003-0007/originals/SRC-0023601.json) |
| SRC-0023586 | B2 호출16행의cell·context/query·ensemble·fit/predict 시간 | [로그](../evidence/0003-0007/originals/SRC-0023586.json) |
| SRC-0023605 | quantiles·median·mean의shape·유한값·중앙 열 일치 | [배열](../evidence/0003-0007/originals/SRC-0023605.npz) |
| SRC-0023589 | predicted_quantiles의shape·유한값 | [배열](../evidence/0003-0007/originals/SRC-0023589.npz) |

B1·B2의 다른 손실표·RCTL·지표 검수는 [history-001](../verification/history-001.md)을 재사용한다. 이번 배열 확인을 전체 원예측 재현·새 성능 실험으로 추가하지 않았다.

같은 SHA-256 사본만 `exact_alias_source_ids`로 연결했다. 전체 파일을 해시한 일, 지정 구간을 읽은 일, 해당 주장을 원문과 대조한 일을 구분한다. 이 묶음에서 발견만 했던 관련 여섯 논문의 실제 지정 구간 검토는 후속 [history-006](history-006.md)에 기록했다. 이를 history-005의 당시 본문 검토로 소급하지 않는다.
