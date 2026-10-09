# H025 검수 — cell별 손해와 사후 선택

[기록](../records/0041-0042-cell-harm.md) · [출처](../sources/history-025.md) · [주장 12개](history-025-primary-review.json)

[저장 산술 검사](history-025-portable-check.json) 294개는 13개 조건의 전체·cell·앞뒤 오차, 개선 개수·IDs, 여섯 primary 경로의 oracle·validation 선택, 21개 validation checkpoint의 membership 순서, scale·시간·비용 prefix를 확인한다. 모든 결과 수치를 배열에서 다시 계산했으며 모델은 실행하지 않았다.

[오류 사본 검사](history-025-negative-check.json) 15개는 평균·half 값·NaN·Boolean 개수·cell/동률 순서·방법 누락·선택 경로·validation 손실·원장·RSS·중복 JSON key·비율의 변경을 검출했다. validation summary의 hash를 입력 설정에 다시 맞춘 사본도 원 예측과의 불일치에서 실패했다. 결과 행 순서만 바꾼 사본은 같은 수치로 통과했다. 원본 파일은 수정하지 않았다.

[원본 확인](history-025-source-check.json)은 원문 16개·새 사본 7개와 통제 파일 6개의 보존을 확인한다. [문서 대조](history-025-document-check.json)는 초안 이후 원문 재독해, 12개 핵심 주장, 실제 본문 표 37행과 navigation·source 연결을 기록한다. 검사 개수를 독립 연구 검증 수로 세지 않는다.

확인 범위는 41/42 및 44 §1–2·§6 수치다. schema/전체 수치의 프로그램 대조와 모든 cell 수치의 개별 수동독해를 구분한다. 44 §3–5·§6 문헌은 미완료다. 같은 정리 agent의 원문 대조이며 독립 심사나 전체 기록 완료가 아니다. 당시 0.031521초와 종료 RSS는 보고 계측값으로 남기며, 이번 검산의 실행 시간을 과거 비용에 추가하지 않았다.
