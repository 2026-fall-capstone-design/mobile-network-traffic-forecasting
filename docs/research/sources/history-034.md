# H034 출처와 실제 읽은 범위

[팀 기록](../records/0051-frontiers-beam-audit.md) · [6개 원본 행](../catalog/history-034-sources.jsonl) · [명세](../evidence/0051-frontiers-beam-audit/manifest.json) · [검수](../verification/history-034.md).

## 원본과 추가 취득의 구분

| 식별자 | 자료 | 이번 처리 |
|---|---|---|
| SRC-0021746 | 51 검토 계획 | H032 정확 사본 재사용·계획 전체 재독. 새 전체 본문 집계 없음 |
| SRC-0021824 | 55 당시 판단 | H031 정확 사본 재사용·§1–2 재독. Frontiers를 직접 언급하지 않으며55 전체 검수 아님 |
| SRC-0063272 | network fetch log | 기존 사본 재사용·event TLS 실패와 관련 entry 재대조 |
| SRC-0063292 | methods fetch log | 기존 사본 재사용·Frontiers 취득 시각/크기/해시 확인 |
| SRC-0063263 | 저장 Frontiers HTML | 보이는 텍스트805줄 전체, embedded MathML118항목. 원 raw HTML/실행 스크립트 전체 검토 아님 |
| SRC-0063304 | 저장 Zindi challenge HTML | H033에서 읽은 평가 주·baseline 범위 재사용. 새 전체 열람 가산 없음 |
| EXT-H034-01 | 현재 공식 Frontiers PDF | 원 inventory 밖의 추가 참조. 텍스트17쪽·시각10쪽 읽음, metadata/공식 링크만 게시 |

기존 보존 사본4개를 연결하고 원본 외부 참조2개·추가 PDF1개는 metadata로 둔다. 새 보존 원문 파일은0개다. 바이트 동일한 별칭은 각 원본 행의 `exact_alias_source_ids`에 연결하며 다른 개정본을 동일본으로 간주하지 않는다.

원 HTML은2026-09-25T16:06:59.582262Z 취득,1,011,037bytes, SHA-256 `de5b21ed932d6056ad4509cef1ad14fe7b1841ca52dd828edcf3d6f61865298b`다. PDF는2026-10-09T13:20:37.193344Z 취득,3,388,230bytes, SHA-256 `3cef9d625608c90a3cb4d7e402148a12068bb1619c2578825d4eccc32cd454a4`다. 같은 DOI의 내용 대조 자료이며 과거 그림과 현재 PDF의 바이트 동일성을 뜻하지 않는다.

## 텍스트·수식·그림

저장 HTML은 script/style/noscript를 제외한 보이는 텍스트1–180·181–320·321–395·396–490·491–805줄을 읽었다. 빈 수식 span은 `__NUXT_DATA__`의 JSON을 정적으로 역참조해 복구했다. 18,972개 payload 항목을 모두 연구 본문으로 읽었다는 뜻은 아니다. 수식 추출물은118항목·142출현·116element ID이며 글머리표·inline 숫자와 중복 표시가 있다. 괄호와 합 범위를 누락한 첫 평문 변환은 판단에 쓰지 않았고, grouping·첨자·합 범위를 보존한118행을 읽었다. 두 unnumbered loss 식과 식1–10의 총12개 display 식을 PDF p11–12와 대조했다. JavaScript 실행은 없었다.

PDF p1–17의 추출 텍스트를 모두 읽고 p2·3·4·5·6·7·8·9·11·12를 렌더링해 시각 확인했다. 선택 시계열, 희소성 그림, Fig6 공유 head, Fig7–10 분할/recursive, Fig11–13 공간 차원, Table1–5, Algorithm1, 식1–10이 포함된다. 현재 PDF 그림을 원 HTML의 당시 원격 그림 사본으로 집계하지 않는다. Alt text는 자동 생성될 수 있다는 p16 설명이 있어 실제 그림과 별도로 취급한다. linked tutorial·참고문헌의 각 원논문·추적 코드까지 검토한 것으로 확대하지 않는다.

## 재대조와 남은 범위

Table2의54·Table4의18·Table5의6개 지표를 시각 자료/텍스트/저장 HTML과 대조하고 Table3의10값을 이전 주최측 표와 비교했다. 총88지표값이며 Table1의6설정 행은 별도다. 인쇄 수치로 개선율·입력 길이별 반례·반올림 허용 범위를 계산했다. 모델 성능 재현이나 유의성 검증이 아니다.

원본6개와 기존 제어 원장6개의 해시를 검수했다. 원55의 event 접근 실패와 현재403은 서로 다른 시점의 기록이다. event 본문·원 데이터·저자 구현·51/53/55의 나머지 종합·전체 기록 접근/검색 검수는 미완료다. 이 범위를 중복·제외·전체 완료로 바꾸지 않는다.
