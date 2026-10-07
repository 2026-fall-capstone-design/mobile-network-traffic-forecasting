# 웹 데이터 규약 v1

웹은 `web/data/manifest.json`을 시작점으로 삼습니다. 경로는 모두 이 파일이 있는
디렉터리 기준의 상대 경로입니다. URL, 절대 경로, 상위 디렉터리 참조는 허용하지 않습니다.
배포 파일의 구조는 `schemas/`의 JSON Schema로 검사합니다.

## 파일

| 파일 | 내용 |
|---|---|
| manifest.json | 데이터 종류·단위·UTC 시간 기준, 실험 목록, 결과 경로, 출처 |
| metrics/<run_id>.json | 모델별 MAE, pooled RMSE, macro cell RMSE, 표본·셀 수 |
| predictions/<run_id>/<model_id>/<cell_id>.json | 셀별 시간 순서의 실제값·예측값 |

예측의 `origin_time`은 정보를 사용할 수 있는 예측 기준 시점이고 `timestamp`는
예측 대상 시점입니다. v1은 정확히 1시간 뒤를 예측합니다. 모든 시각은 UTC를 사용합니다.
원본이 다른 시간대이면 변환 기준을 데이터 문서와 실험 설정에 기록합니다.

같은 실험의 모든 모델은 동일한 셀·시각·실제값을 사용해야 합니다. 각 셀은 선언된
테스트 시작부터 끝까지 빠짐없이 1시간 간격으로 있어야 합니다. 지표는 Python에서
전체 테스트 구간을 기준으로 계산합니다. 웹의 기간 필터는 그래프 표시 범위만 바꿉니다.

## 합성 예제

`scripts/make_sample.py`는 시드 17로 3개 셀의 96시간 데이터를 만듭니다.
마지막 24시간을 평가하며 직전 값과 24시간 전 값을 기준 모델로 사용합니다.
직전 시간의 관측값을 매 시간 사용할 수 있는 rolling one-step 평가입니다.
앞선 테스트 시점의 실제값을 다음 시점에 사용하는 조건을 모든 모델에 동일하게 적용합니다.

이 데이터는 실제 트래픽이 아니며 모델 학습이나 TabICLv2 추론을 수행하지 않습니다.
실제 연구용 데이터는 `kind: real`과 근거 있는 단위·출처를 갖춘 별도 실험으로 추가합니다.
연구 모델도 공통 Prediction 형식을 내보내고 같은 평가·검증을 통과해야 합니다.

## 재현

설정·입력 CSV의 SHA-256과 생성 시각, Python 버전, 코드 커밋, 작업 트리 변경 여부를 기록합니다.
생성 시각과 Git 상태는 실행마다 다를 수 있습니다. CI에서는 예측 수치·지표·데이터 규약을
다시 생성하여 커밋된 예제와 비교합니다.

```bash
uv run --locked python -m traffic_forecasting demo --config configs/demo.yaml
uv run --locked python -m traffic_forecasting check-data
uv run --locked python scripts/check_reproducibility.py
```

군집 결과나 다중 예측 구간은 연구 방향 확정 후 스키마 버전을 정해 확장합니다.
