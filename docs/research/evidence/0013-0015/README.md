# 13–15 저장 근거

[연구 기록](../../records/0013-0015-transfer-cell-identity.md)과 [원문 안내](../../sources/history-008.md)에 연결한 13/14 및 15 수치·방법 부분이다. 15의 여섯 문헌에 대한 방법 검수는 미완료다.

[manifest.json](manifest.json)에 16출처의 원경로·해시·크기·정확한 사본 ID·실제 검토 범위를 보존했다. 새 원문 13개 124,722bytes와 기존 사본 3개 재사용이며 원본을 수정하지 않았다. `.md.txt`와 `.py.txt`는 역사적 자료이며 현재 지시나 실행 모듈이 아니다.

| 자료 | 재사용 범위 |
|---|---|
| 13/14 계획·15 판단·코드 2개 | 계획과 실제 설정/집계식의 정적 검토 |
| transfer JSON/NPZ | 16×16 MAE/excess/PCC/지원 matrix, 24소속 비교, 4pair 변경 |
| identity 시작/호출/완료/summary | 168context 시각·64query·ID 열 순열·당시 호출·비용 |
| identity final/partial NPZ | 최종 7예측과 정답/ID/시간, 부분 3예측 일치 |
| 기존 design_data/risk_table_predictions/UPC labels | 정답·정규화·실제 query 매핑, 고정 B1 median, 도시 소속 24개 |

모델 학습·추론·새 난수 없이 저장값을 확인하는 명령은 다음과 같다. 저장소 환경 설치는 프로젝트 안내를 따른다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_transfer_identity_history.py \
  --source docs/research/evidence/0013-0015/manifest.json \
  --output .research-archive/verify-0013-0015.json
```

[공유 검산 결과](../../verification/history-008-arithmetic.json)는 520개 확인과 전체 표·반례를 담는다. 보존 원문 13개 목록과 모든 16출처의 바이트를 확인한다. NPZ는 pickle을 허용하지 않으며 `design_data.dates` 객체 본문은 읽지 않는다. 원 코드 실행·모델 재현 성공을 뜻하지 않는다.

원자료에서 8th-neighbor 거리/95%threshold를 재계산하지 않았다. 무작위 1,000순열의 개별 값은 저장 NPZ에 없고 세 분위수만 보고됐다. 이를 새 순열로 대체하지 않는다. 실행시간/RSS는 보고값이며 로그 시간 합과 중복 필드의 일치만 확인했다. 전체 논문·후속 기록의 검토 완료도 아니다.
