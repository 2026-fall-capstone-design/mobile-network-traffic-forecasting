# H066 출처와 실제 읽은 범위

[69–71 기록](../records/0069-0071-peak-objective.md) · [66–68 통합](../records/0066-0068-objectives.md) · [보존 명세](../evidence/0069-0071-peak-objective/manifest.json) · [기계 판독 목록](../catalog/history-066-sources.jsonl)

55개 출처 그룹·124개 물리 경로를 원목록과 해시로 연결했다. 작은 정확사본 24개·317,042 bytes를 새로 보존하고 기존 사본 7개를 재사용했다. 외부 문헌·파생 표현·검색 출력 24개는 해시와 접근 경로만 연결했으며 이번 본문 독해 가산 대상이 아니다.

| 자료 | 실제 읽고 확인한 범위 | 신규 독해 |
|---|---|---|
| 원69·70·71 / 공개 피크 보고서 | 26·48·43·100행 전체 텍스트 | 로컬 본문 4 |
| diagnostic70 / record71 / archive71 / collect69 / fixlogs71 / render69 | 160·80·82·41·14·15행 전체 정적 독해와 AST parse. 실행·import 없음 | 로컬 본문 6 |
| 설정·result·offsets·start/finish·after·budget receipt | result의 root와 originals24/calibrated114/Tab 비교6/보정 비교48/toy2 전체 필드. 나머지도 모든 항목 | 전체 JSON 7 |
| acquisition / review_scope / search_scope / log repairs / render manifest / snapshot manifest·verification | 모든 필드·항목. 연결 본문을 읽었다는 의미는 아님 | 전체 JSON 7 |
| budget_before70 | after67과 동일한 기존 사본. 전체 재독해 | 재가산 0 |
| 입력6 중 fit_results | 기존29개 항목의 모든 필드 재독해 | 재가산 0 |
| 입력6 중 frozen-fit summary | aggregates8의 모든 필드와 root schema. 이번 전체 JSON 독해 아님 | 재가산 0 |
| 입력6 중 RCTL summary | root schema 및 기존 metrics의 산술 대조. 이번 전체 JSON 독해 아님 | 재가산 0 |
| 입력6 중 NPZ3 | allow_pickle=False로 77배열 shape·dtype·finite 검사. 29개 검증 블록과 지정 target·예측 배열 재집계 | 재가산 0 |
| 문헌 PDF2·TXT2·HTML4·PNG6·검색 출력10 | 크기·해시·사본·수집/렌더 메타데이터 대조. 본문·픽셀 독해는 대기 | 0 |

신규 로컬 본문은 SRC-0000152, SRC-0022020–0022022, SRC-0022366, SRC-0022630, SRC-0022803, SRC-0022971, SRC-0023067, SRC-0023097이다. 전체 JSON은 SRC-0001075/0001076, SRC-0029493/0029495–0029500, SRC-0063450/0063451/0063462/0063463/0063470이다. before70 SRC-0029494는 H062의 SRC-0027838과 동일하므로 새 사본·새 전체 JSON으로 세지 않는다.

숫자 배열의 finite 검사나 일부 지표 재계산은 모든 배열의 모든 값을 수동 독해했다는 뜻이 아니다. frozen-fit의 29개 train prediction은 shape·dtype·finite를 확인했지만 이번 진단의 98개 보정 계산에는 사용하지 않는다. result JSON은 필드를 나눠 모두 읽었으며 들여쓰기 원시 행을 별도로 또 읽은 것은 아니다.

snapshot17의 56파일·14,152,614 bytes는 [보존 검사](../evidence/0069-0071-peak-objective/provenance-check.json)에서 확인했다. 그 안의 과거 AGENTS·progress 전체 독해는 이번 신규 범위에 포함하지 않는다. 당시 verification의 PDF 38쪽·선택 렌더 6쪽은 당시 다운로드·선택 확인 기록이다. 이번 일차논문 본문·시각 독해 수는 모두 0이다.

복구된 두 검색 로그는 원 .txt 바이트의 SHA-256와 JSON raw_text의 UTF-8 문자열 일치를 확인했다. 이는 검색 내용의 주장 검증이나 검색 결과가 가리킨 논문 독해가 아니다. 저장 검색 본문과 Forecaster’s Dilemma·DeepCog, SIU2026 메타데이터는 후속 문헌 묶음에서 다룬다. 새 웹 조회는 이번 묶음에서 하지 않았다.

66–68 통합은 기존 [H063](history-063.md)·[H064](history-064.md)·[H065](history-065.md)의 본문 검수와 출처를 재사용한다. 그 내용을 다시 연결했다고 논문 읽기 수를 중복 가산하지 않는다. 실제 실행 config·원배열·비용 및 별도 보충자료/최종 판본의 공백도 각 기록에 유지한다.
