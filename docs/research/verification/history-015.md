# 초기 누적 비용 검수

[정리 기록](../records/0015-0021-cumulative-costs.md)과 [출처28개](../sources/history-015.md)를 대조했다. [687개 기계 검사](history-015-cost-check.json)는 출처 바이트, 완료 호출 식별, context/query 행 수, 시간 합계, summary와 호출 로그,29fit의 method/seed/cluster·epoch·종료 상태를 검사한다. 숫자 합계는 확인하지만 전체 연구시간이나 실행 성능을 재현한 검사가 아니다.

[14개 오류 자료 검사](history-015-negative-check.json)는 격리 사본에서 누락·중복 호출, query 단위 치환, 비유한 시간, summary 불일치, 잘못된 RCTL seed·epoch·완료 상태·시간 포함관계와 보존 바이트 변경을 거부한다. 최선 epoch에 불리언이나 소수를 넣은 경우도 거부한다. 원본은 수정하지 않았다.

[주장11개와 한계](history-015-primary-review.json)의 별도 원문 대조는 타이머의 위치, 준비/저장/추론 포함 관계, 상한과 실제 소비량, 재사용을 검토한다. 같은 정리 에이전트의 두 번째 읽기이며 독립 연구자 검증이 아니다. [문서·원문 상태 확인](history-015-document-check.json)은 문서 저장과 링크 검사를 보완한다.

팀은 저장된 자료만으로 다음 검산을 수행할 수 있다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_initial_cost_ledger.py --manifest docs/research/evidence/0015-0021-costs/manifest.json --output .research-archive/checked-initial-costs.json
```

초기 실패·시작 시도 전수 비용, 타이머 밖 준비·대기·저장·문헌 비용, 이후 전체 누적 원장, 개별 과거 실행 환경의 완전한 동일성은 미확인이다.15·21의 후속 연결과 전체 고유 기록 정리도 남아 있다. 예산 상한이나 과거 명령을 새 실행 허가로 사용하지 않는다.
