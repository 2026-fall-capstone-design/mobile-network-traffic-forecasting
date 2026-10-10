# H076 출처: 원76 TabDistill 상호작용 비교표

[연구 기록](../records/0076-tabdistill-interaction-audit.md) · [H075의 선행 범위](history-075.md) · [수치 자료](../evidence/0076-tabdistill-interactions/README.md)

20개 핵심 주장의 작성 후 원문 대조를 완료했다. 새 원본을 발명하거나 미검토 자료를 중복으로 제외하지 않고, H075에서 남긴 같은 커밋 JSON의 미독해 부분을 이어 읽었다.

| 구분 | 값 |
|---|---|
| 대표 ID | `SRC-0063879` |
| 바이트가 같은 사본 | `SRC-0001227` |
| 원본 상대 위치 | `tmp/redesign_20260925/sources/response_transfer_76/TabDistill_commit.json` |
| 원본 크기 | 540,666 bytes |
| SHA-256 | `ae7124a690fdcae8b69d30ab41cbd811a44c34b549531d728933a9f2964837c4` |
| 고정 커밋 | [64214da](https://github.com/Clouddelta/tab-distill/commit/64214da0edf7eef6e8bf645332471d78b30345e8) |
| 삭제 전 부모 | [58bd710](https://github.com/Clouddelta/tab-distill/tree/58bd71068a879c8ee90e62f405d8fb8f6db5e81e) |
| 이번 첫 독해 | `/files/1/patch`–`/files/27/patch` 전체 2,307 patch 행. 헤더를 제외한 데이터 2,253행 |
| 앞선 첫 독해 | H075의 patch 0 및 28–87, 총 61개 |
| 메타데이터 | 최상위 값과 파일 88개의 모든 필드. 공통식으로 복원되는 URL 264개도 원 문자열과 대조 |
| 내용 범위 | 저장된 커밋 응답 전체의 첫 독해가 연결됨. 저장소 전체 검토·새 모델 재현을 뜻하지 않음 |

복원한 CSV 27개는 원 응답의 Git blob SHA-1과 일치한다. 각 파일의 SHA-256·행 수·원 링크는 [개별 명세](../evidence/0076-tabdistill-interactions/source-manifest.json)에 있다. H075의 원시 결과·순위·요약·4개 Python patch는 이번에 새로 읽은 27개 CSV로 중복 집계하지 않는다.

후속 소비 코드의 정적 대조는 같은 JSON의 patch 29·86, 모델 결과 연결은 patch 31–57에 근거한다. 별도 저장 `compare_index_performance.py`는 H075에서 검토한 `SRC-0063884`의 189–261행을 다시 참조한다. 4월 논문의 선별 조건은 `SRC-0063877`의 4쪽과 [H075의 검수 범위](../verification/history-075.md)에 연결한다. 이 참조 자료들은 새로 전부 읽은 파일로 추가하지 않는다.

원 생성기가 이 CSV들을 저장한 실행 연결, 정확한 teacher 판본, 데이터 분할 식별자·정규화·하드웨어·전체 비용은 아직 연결되지 않았다. CSV에 없는 조건을 인접 코드의 기본값으로 보충하지 않는다. 고정 GitHub 링크는 원 자료의 출처이며 우리 팀 저장소에 모든 외부 파일의 동일 바이트를 보관했다는 뜻은 아니다.
