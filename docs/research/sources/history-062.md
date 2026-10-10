# H062 출처와 실제 읽은 범위

[65 종합](../records/0063-0065-synthesis.md) · [66–68 진단](../records/0066-0068-group-risk.md) · [명세](../evidence/0063-0068-synthesis-risk/manifest.json) · [기계 판독 목록](../catalog/history-062-sources.jsonl)

원본 47그룹·100경로의 크기·SHA-256·같은 바이트의 사본 관계를 확인했다. 읽은 내용과 보존 상태는 별도다.

| 범위 | 실제 수행 | 신규 독해 가산 |
|---|---|---|
| 66/67/68 및 중간 보고서 | 4개 전체 텍스트 | 로컬 본문4 |
| collect66/render66/diagnostic67/record68/archive68 | 5개 코드 전체 정적 독해·AST parse, 실행/import 없음 | 로컬 본문5 |
| 결과·설정·marker·after·receipt | 6개 전체 JSON, 24프로파일의 모든 값 독해 및 산술 대조 | 전체 JSON6 |
| download/review/search scope/render log, snapshot manifest/verification | 6개 전체 JSON | 전체 JSON6 |
| 63/64/65·before·42·NPZ | 기존 사본6 재사용. 65 전체 판단 재독, before 전체·42 지정128값·NPZ 숫자 배열 대조 | 재가산0 |
| 검색/열람 결과4개 | JSON 문자열 전체52블록. 검색의 맥락·범위와 판본 차이 확인 | 외부 검색 문자열4로 별도 표시. 로컬 결과 JSON 가산0 |
| MMR/MRI/q-FFL PDF3 | 페이지 수35/32/7과 첫 페이지 판본 marker 확인 | 본문·시각 독해0 |
| TXT3/HTML3/PNG7 | manifest/해시·사본 대조 | 본문·시각 독해0, 후속 대기 |

신규 로컬 본문은 `SRC-0000116`, `SRC-0022017–0022019`, `SRC-0022281`, `SRC-0022606`, `SRC-0022876`, `SRC-0023065`, `SRC-0023089`다. 신규 전체 JSON은 `SRC-0001028/0001029`, `SRC-0027838/0027840–0027844`, `SRC-0062716/0062717/0062721/0062729`다. before `SRC-0027839`는 H052의 `SRC-0000901`과 바이트가 같아 이미 완료한 독해를 재사용한다.

외부 검색 출력의 표제·주소는 [search-audit](../evidence/0063-0068-synthesis-risk/search-audit.json)에 있다. 문자열 전체를 읽었다고 연결된 논문 전체를 읽은 것은 아니다. 특히 66b는 MRI v1과 다른 발표가 섞인 학회 프로그램 발췌를 포함하고, primary 검색의 MMR 요약과 저장 v2 초록은 응용 설명이 다르다. search_scope의 15검색어·9필터 선언만으로 전체 질의 실행·전세계 신규성 검토를 확정하지 않는다.

snapshot16의 45개 사본·8,626,942 bytes를 [보존 검수](../evidence/0063-0068-synthesis-risk/provenance-check.json)했다. 그 안의 progress·과거 AGENTS 전체를 이번에 새로 읽었다고 세지 않는다. 다운로드6개와 PNG7개의 바이트 일치, PDF 판본 marker 확인도 과거 논문 주장의 내용 검증을 대신하지 않는다.

일곱 선행의 내용은 [H055](history-055.md)·[H056](history-056.md)·[H057](history-057.md)·[H058](history-058.md)·[H059](history-059.md)·[H060](history-060.md)·[H061](history-061.md)의 기존 검수를 재사용한다. 이번에 새로운 일차문헌 웹 조회나 외부 코드 실행은 하지 않았다. MMR/MRI/q-FFL의 본문·표·그림·공식 판본·코드 검수는 다음 묶음에 남는다.

[H063 MMR 출처·판본](history-063.md)에서 MMR35쪽/파생TXT·HTML·preview2개 검수를 추가했습니다. H062 manifest의 당시 미독해 표시는 과거 snapshot이며 현재 범위는 H063을 확인하세요. [H064 MRI 출처·판본](history-064.md)에서 MRI32쪽과 파생 표현·출판본·TeX 지정 범위의 검수도 추가했습니다. [H065 q-FFL 출처·판본](history-065.md)에서7쪽·파생표현·TeX 지정범위와 원알고리즘 코드를 추가 확인했습니다. 최종 통합과 실행 근거의 공백은 남아 있습니다.
