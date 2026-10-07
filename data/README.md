# 데이터 준비와 예제 실행

데이터를 읽는 코드는 [data 모듈](../src/traffic_forecasting/data/__init__.py),
예제 실행 설정은 [configs/demo.yaml](../configs/demo.yaml)에 있습니다.
아래 명령은 저장소 최상위 폴더에서 실행합니다.

## 저장 위치

| 경로 | 용도 | Git 관리 |
|---|---|---|
| `data/sample/` | 팀원이 바로 실행할 수 있는 작은 예제 입력 | 포함 |
| `data/raw/` | 내려받은 원본 데이터 | 제외 |
| `data/processed/` | 시간 정렬·집계·전처리를 마친 데이터 | 제외 |
| `artifacts/<run_id>/` | 실험별 예측, 지표, 로그 등 실행 결과 | 제외 |
| `web/data/` | 웹에 표시할 결과 JSON | 포함 |

Git에서 제외되는 데이터는 팀 저장 공간에 보관하고,
실험 기록에 파일 위치와 다운로드·생성 방법을 남깁니다.

## 현재 예제

| 항목 | 값 |
|---|---|
| 입력 파일 | `data/sample/traffic.csv` |
| 생성 방법 | `scripts/make_sample.py`, 난수 시드 17 |
| 셀 | `1001`, `1002`, `1003` |
| 전체 구간 | 2026-01-01 00:00부터 2026-01-04 23:00까지, UTC |
| 관측 간격·개수 | 1시간, 셀당 96개·전체 288개 |
| 평가 구간 | 2026-01-04 00:00부터 23:00까지, 셀당 24개 |
| 단위 | 합성 활동량 |

입력은 일별 주기·추세·작은 난수를 조합한 합성 데이터입니다.
두 기준 모델의 동작과 평가·웹 연결을 확인하는 데 사용합니다.

## 입력 CSV 형식

현재 로더는 다음 헤더를 **같은 순서**로 읽습니다.

```csv
cell_id,timestamp,value
1001,2026-01-01T00:00:00Z,42.5
1001,2026-01-01T01:00:00Z,45.0
```

| 열 | 형식과 조건 |
|---|---|
| `cell_id` | 셀 식별자. 웹 결과로 내보낼 때는 영문·숫자·`_`·`-` 사용 |
| `timestamp` | 시간대가 포함된 ISO 8601 시각. UTC로 변환했을 때 정시여야 함 |
| `value` | 0 이상의 유한한 숫자. 결측값과 실제 0을 구분 |

로더는 셀·시각 순서로 정렬한 뒤, 셀별 중복 시각과 1시간 간격 누락을 검사합니다.
결측 대체나 시간 집계가 필요하면 전처리 단계에서 처리하고 방법을 기록합니다.
모든 모델의 평가 데이터는 동일한 셀과 테스트 구간을 포함해야 합니다.

## 실행 설정

| 설정 | 현재 값 | 의미 |
|---|---|---|
| `run_id` | `synthetic-demo-v1` | 결과 파일과 실험을 연결하는 식별자 |
| `label` | 합성 데이터 기본 비교 | 웹의 실험 선택 목록에 표시할 이름 |
| `dataset_id` | `synthetic-hourly-v1` | 입력 데이터의 식별자 |
| `input` | `data/sample/traffic.csv` | 저장소 기준 입력 경로 |
| `output` | `web/data` | 저장소 기준 기본 결과 경로 |
| `test_start` | `2026-01-04T00:00:00Z` | 평가 시작 시각. 입력의 마지막 시각까지 평가 |
| `unit` | 합성 활동량 | 웹의 차트·결과 설명에 사용할 단위 |
| `timezone` | `UTC` | 웹 데이터의 시간 기준 |

`configs/` 아래의 설정 파일을 사용합니다.
현재 `demo` 명령은 직전 값·24시간 전 값 모델을 실행하고,
데이터 종류를 `synthetic`으로 기록하는 예제 전용 명령입니다.
연구 모델의 입력·출력 연결은 [공통 실험 규약](../docs/research-protocol.md)을 따릅니다.

## 결과 생성과 검증

### 별도 폴더에서 실행 확인

```bash
uv run --locked python -m traffic_forecasting demo --config configs/demo.yaml --output artifacts/demo-preview
uv run --locked python -m traffic_forecasting check-data --directory artifacts/demo-preview
```

`--output`은 설정의 출력 경로를 덮어씁니다.
생성된 `manifest.json`에서 지표와 셀별 예측 파일의 경로를 확인할 수 있습니다.

### 웹에 표시할 예제 갱신

```bash
uv run --locked python -m traffic_forecasting demo --config configs/demo.yaml
uv run --locked python -m traffic_forecasting check-data --site web
uv run --locked python scripts/check_reproducibility.py
```

기본 출력 위치인 `web/data/`를 갱신합니다.
현재 생성기는 실행할 때마다 해당 예제 하나를 담은 `manifest.json`을 작성합니다.
여러 실험을 등록한 경우에는 기존 목록을 합치는 처리가 필요합니다.

원본 합성 CSV 자체를 다시 만들 때만 다음 명령을 먼저 실행합니다.

```bash
uv run --locked python scripts/make_sample.py
```

예제 입력이나 설정을 변경했다면 결과 JSON도 함께 갱신합니다.
생성 시각과 실행 당시 Git 상태는 달라질 수 있으며, 재현성 검사는 입력·설정 해시와
예측값·지표 등 비교 가능한 내용을 확인합니다.

## 실제 데이터 도입 시 남길 정보

| 항목 | 기록할 내용 |
|---|---|
| 출처와 버전 | 데이터 이름, 다운로드 주소, 배포 버전 또는 수집 날짜, 파일 해시 |
| 범위 | 지역, 셀 목록, 시작·종료 시각 |
| 시간 기준 | 원본 시간대, 집계 간격, 시각이 구간의 시작인지 끝인지 |
| 관측값 | 원본 단위와 변환 방법 |
| 전처리 | 결측·중복·이상값 처리, 집계 및 제외 기준 |
| 재실행 방법 | 입력 위치, 전처리 명령, 설정 파일, 처리 결과 위치 |

실험 기록 예시는 [진행 기록 안내](../docs/progress/README.md),
웹 출력 필드는 [웹 데이터 규약](../docs/web-data-contract.md)에 정리되어 있습니다.
