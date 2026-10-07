# 웹 데이터 규약 v1

Python의 예측 결과를 정적 웹에 연결하는 파일 구조입니다.
현재 규약의 `schema_version`은 `"1.0"`이며,
형식은 [schemas/](../schemas/)와 파일 간 일관성 검사로 검증합니다.

## 파일 구조와 읽는 순서

```text
web/data/
├── manifest.json
├── metrics/
│   └── <run_id>.json
└── predictions/
    └── <run_id>/
        └── <model_id>/
            └── <cell_id>.json
```

1. 웹이 `manifest.json`에서 데이터 설명과 실험 목록을 읽습니다.
2. 선택한 실험의 `metrics_path`에서 모델별 지표를 읽습니다.
3. 선택한 모델·셀의 `series[].path`에서 실제값과 예측값을 읽습니다.

경로는 모두 **manifest 파일이 있는 폴더 기준**입니다.
예를 들어 `metrics/synthetic-demo-v1.json`으로 기록합니다.
외부 URL, 절대 경로, 상위 폴더를 가리키는 `..`는 사용할 수 없습니다.

## 1. manifest.json

실제 예제는 [현재 manifest](../web/data/manifest.json)에서 확인할 수 있습니다.
최상위 필드는 `schema_version`, `dataset`, `runs`입니다.

### 데이터 정보: dataset

| 필드 | 내용 |
|---|---|
| `id` | 데이터 식별자 |
| `kind` | 합성 데이터는 `synthetic`, 실제 데이터는 `real` |
| `unit` | 관측값의 단위. 차트 축과 실험 정보에 표시 |
| `timezone` | `UTC` |
| `description` | 데이터와 결과를 이해하는 데 필요한 설명 |

하나의 manifest는 하나의 데이터 설명을 공유합니다.
서로 다른 데이터셋을 한 목록에서 선택하게 하려면 데이터 정보 구조와 웹 로직을 함께 확장합니다.

### 실험 정보: runs[]

| 필드 | 내용 |
|---|---|
| `id` | 실험 식별자. 지표·예측 파일의 `run_id`와 일치 |
| `label` | 웹에 표시할 실험 이름 |
| `test_start`, `test_end` | 평가 대상 시각의 시작·끝. 양 끝을 포함 |
| `generated_at` | 결과를 생성한 시각 |
| `provenance` | 실행 코드·입력·설정 정보 |
| `metrics_path` | 모델별 지표 파일 경로 |
| `models` | 비교 모델 목록 |

### 실행 정보: provenance

| 필드 | 내용 |
|---|---|
| `commit` | 생성 당시 Git 커밋 SHA. 확인할 수 없으면 `null` |
| `dirty` | 생성 당시 미커밋 변경 여부. 확인할 수 없으면 `null` |
| `python` | 실행한 Python 버전 |
| `data_sha256` | 입력 파일의 SHA-256 |
| `config_sha256` | 실행 설정 파일의 SHA-256 |

### 모델과 셀: models[]

| 필드 | 내용 |
|---|---|
| `id` | 모델 식별자. 지표·예측 파일의 `model_id`와 일치 |
| `label` | 웹에 표시할 모델 이름 |
| `series[].cell_id` | 셀 식별자 |
| `series[].path` | 해당 셀의 예측 JSON 경로 |

위 필드는 모두 필수입니다. 데이터·실험·모델·셀 식별자에는 영문, 숫자, `_`, `-`를 사용합니다.
v1 스키마는 정의되지 않은 추가 필드를 허용하지 않으므로,
새 메타데이터가 필요하면 스키마와 읽는 코드를 함께 수정합니다.

## 2. 셀별 예측 파일

다음은 형식을 설명하기 위한 2개 시점의 예시입니다.

```json
{
  "schema_version": "1.0",
  "run_id": "example-run",
  "model_id": "example-model",
  "cell_id": "1001",
  "points": [
    {
      "origin_time": "2026-01-03T23:00:00Z",
      "timestamp": "2026-01-04T00:00:00Z",
      "actual": 10,
      "predicted": 9
    },
    {
      "origin_time": "2026-01-04T00:00:00Z",
      "timestamp": "2026-01-04T01:00:00Z",
      "actual": 12,
      "predicted": 11
    }
  ]
}
```

| 필드 | 의미 |
|---|---|
| `origin_time` | 예측에 사용할 정보를 확정하는 기준 시점 |
| `timestamp` | 예측 대상 시점. 기준 시점보다 정확히 1시간 뒤 |
| `actual` | 실제 관측값. 0 이상 |
| `predicted` | 모델의 예측값 |

시각은 UTC의 ISO 8601로 기록합니다.
`points`는 테스트 시작부터 끝까지 오름차순으로, 중복이나 누락 없이 1시간 간격이어야 합니다.
수치는 유한한 JSON 숫자를 사용합니다.

## 3. 모델별 평가 파일

위 예시의 지표는 다음과 같습니다.
모델을 추가하면 같은 `rows` 배열에 해당 모델의 지표를 추가합니다.

```json
{
  "schema_version": "1.0",
  "run_id": "example-run",
  "rows": [
    {
      "model_id": "example-model",
      "n_points": 2,
      "n_cells": 1,
      "mae": 1.0,
      "rmse": 1.0,
      "macro_rmse": 1.0
    }
  ]
}
```

모델마다 전체 셀·전체 테스트 구간의 지표를 한 행으로 저장합니다.
각 지표의 계산 방법은 [공통 실험 규약](research-protocol.md)에 정의되어 있습니다.
웹은 이 값을 읽어 표시하며, 차트 필터를 바꿀 때 지표를 다시 계산하지 않습니다.

## 결과 추가와 검증

1. 고유한 `run_id`를 정하고 모델·셀별 예측 파일을 작성합니다.
2. 같은 예측값으로 지표 파일을 생성합니다.
3. manifest의 `runs`에 실험 정보와 모델·셀 경로를 등록합니다.
4. 다음 검사와 [웹 화면 확인](../web/README.md)을 수행합니다.

```bash
uv run --locked python -m traffic_forecasting check-data --site web
```

검사는 다음 항목을 확인합니다.

| 검사 | 확인하는 내용 |
|---|---|
| 구조 | 필수 필드, 자료형, 스키마 버전 |
| 참조 | 상대 경로의 실제 파일 존재 여부 |
| 식별자 | 실험·모델·셀 ID의 중복과 파일 간 불일치 |
| 시간 | 1시간 예측 간격, 시점 정렬, 선언한 테스트 구간 전체 포함 |
| 비교 조건 | 모든 모델의 셀·예측 시점·실제값 일치 |
| 지표 | 예측값으로 재계산한 값과 저장 지표 일치. 허용 오차 `1e-6` |
| 웹 리소스 | HTML에서 참조하는 로컬 CSS·스크립트 파일 존재 여부 |

화면 상호작용과 레이아웃은 브라우저에서 별도로 확인합니다.

## 예제 재현성 검사

```bash
uv run --locked python scripts/check_reproducibility.py
```

이 검사는 기본 데모를 임시 폴더에서 다시 만들고 커밋된 예제 결과와 비교합니다.
실행마다 달라질 수 있는 `generated_at`, `provenance.commit`,
`provenance.dirty`, `provenance.python`은 비교에서 제외합니다.

검사는 현재 기본 데모를 대상으로 합니다.
manifest에 연구 실험을 추가할 때는 예제 재현성 검사의 비교 범위도 함께 조정합니다.
