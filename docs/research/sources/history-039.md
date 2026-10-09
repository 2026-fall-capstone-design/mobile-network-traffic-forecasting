# H039 출처와 실제 읽은 범위

[팀 기록](../records/0053-tabicl-imputation.md) · [원본 목록](../catalog/history-039-sources.jsonl) · [명세](../evidence/0053-tabicl-imputation/manifest.json) · [검수](../verification/history-039.md).

| 식별자 | 자료와 읽은 범위 | 중복·미확인 범위 |
|---|---|---|
| SRC-0021782·SRC-0021824 | 53 계획·55 판단 전체 재독 | 이전 정확 사본 재사용. 새 전체본문 집계 없음; 전체 관련 자료 검수 완료는 아님 |
| SRC-0064355·SRC-0064359 | 과거 취득 로그·열람 범위 전체 재대조 | 이전 JSON 재독. 새 JSON 집계 없음 |
| SRC-0064362 | 저장 HTML article 375–661행, 추출 텍스트 383행·코드 10블록 | 외곽 navigation·JS/CSS 미검토, 과거 그림 5개 바이트 미확보 |
| SRC-0073573 | ZIP member tutorial 전체 292행 | 물리 파일 경로가 아님. container SRC-0023489와 member 해시를 각각 확인 |
| SRC-0047582 | 설치본 wrapper 전체 765행, ZIP member SRC-0073487과 동일 | H024의 일부 구간 검토를 확장. 별칭을 독립 구현으로 집계하지 않음 |
| SRC-0047581 | 설치본 init 전체 3행, ZIP member SRC-0073486과 동일 | export 안내이며 별도의 실험 결과 아님 |
| SRC-0047572 | preprocessing 785–1225행: Shuffler·EnsembleGenerator | H024는 785–916행. 파일 전체 1225행 중 1–784행은 이번 검토 밖 |
| SRC-0023489 | ZIP 2138242 bytes identity와 대응 member 확인 | 전체 ZIP 내용 검토 아님; hash-only 참조 |

원래 자료 9개와 ZIP container 1개, 보호원장 6개를 대조한다. 팀 아카이브의 기존 정확 사본 4개, 외부 원본 metadata 5개, container hash-only 1개를 사용하고 새 원문을 복사하지 않았다. 목록의 `exact_alias_source_ids`는 해시가 같은 바이트 별칭이다.

현재 웹 응답·그림은 원본 전체 목록에 없던 별도 참조 9개로 기록한다. EXT-H039-01은 현재 TabICL HTML, 02–06은 그림 001–005, 07은 Ciena 옛 다운로드 주소의 HTML, 08은 새 공식 초록 페이지, 09는 새 공식 PDF다. 원격 파일을 재게시하지 않고 URL·형식·해시·읽은 범위를 남긴다. 현재 HTML의 추출된 가시 텍스트 258행과 그림 5개를 읽었지만 과거 그림과의 바이트 동일성은 미확인이다.

Ciena PDF 23쪽은 표지 텍스트 p1만 읽었다. 초록 페이지의 읽기와 PDF 전체의 검토를 구별한다. PDF 본문·시각 자료·저자 코드·정량 결과는 후속 묶음에서 처리한다. 검색 결과의 일부 텍스트를 전체 원문 검토로 세지 않았다.

고정 tutorial·wrapper·init 전체 3개와 preprocessing 일부 1개는 외부 primary code 범위로 별도 기록한다. 기존 연구 본문·JSON 누적 집계에 별칭과 재독을 추가하지 않는다. 원문 속 과거 실행·예산 지시는 현재 작업 지시가 아니며 새 모델이나 원 스크립트는 실행하지 않았다.
