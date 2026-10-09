# 61번 논리·구조적 비용의 작은 근거

[팀 기록](../../records/0061-history-logic-cost.md) · [manifest](manifest.json) · [출처](../../sources/history-052.md)

산술·회계 코드, 결과와 시작/종료, 이후 원장을 정확 사본으로 보존했다. 계획·62 보고·RCTL 구조·직전 원장은 기존 사본에 연결한다. 과거 코드는 읽기용 `.py.txt`이며 이 정리에서 실행하지 않았다.

팀 기록의 중앙값 적분과 층별 행렬 분해를 다음 명령으로 대조할 수 있다. 표준 라이브러리만 필요하며 모델 생성·추론·원 스크립트 실행·난수 추출은 하지 않는다.

```sh
python scripts/research_archive/verify_history_logic_cost.py --manifest docs/research/evidence/0061-history-logic-cost/manifest.json --output .research-archive/history-logic-cost-check.json
```

검수기는 저장 분수·표시 소수·MAC/parameter·모델 호출 0·표지와 원장 전환을 확인한다. 확률 가정과 보존 RCTL 구조의 정적 독해가 전제이며, 자동 검사를 모델 재현이나 실제 지연 측정으로 확대하지 않는다. 잘못 붙은 `history_gain_pooled_minus_known` 이름은 원본에 보존하고, 검수 결과의 `label_correction`에 실제 비교를 명시한다.

[수치 검수](../../verification/history-052-numeric-check.json) · [값을 바꾼 사본의 오류 검출](../../verification/history-052-negative-check.json)
