# TabICLv2 Traffic Forecasting

모바일 트래픽 예측 모델을 비교하고, 실험 결과를 웹에서 확인하는 4인 캡스톤 프로젝트입니다.

Python으로 데이터를 처리하고 예측·평가한 결과를 JSON으로 저장합니다.
정적 웹은 이 결과를 읽어 시계열 차트와 모델별 지표를 보여 줍니다.

[데모 보기](https://2026-fall-capstone-design.github.io/tabicl-traffic-forecasting/) ·
[팀 작업 보드](https://github.com/orgs/2026-fall-capstone-design/projects/1) ·
[협업 안내](CONTRIBUTING.md)

## 현재 구현

| 구성 | 내용 |
|---|---|
| 데이터 | 3개 셀의 96시간 합성 시계열 |
| 기준 모델 | 직전 값 예측, 24시간 전 값 예측 |
| 평가 | 마지막 24시간의 72개 표본으로 MAE, RMSE, Macro RMSE 계산 |
| 웹 | 실험·모델·셀 선택, 표시 구간 변경, 차트·수치 표·평가 결과 조회 |
| 자동화 | PR 검사, 예제 결과 재현성 확인, GitHub Pages 배포 |

현재 데모는 데이터부터 웹까지 연결한 합성 예제입니다.
연구 모델은 **TabICLv2 직접 예측**과 **TabICLv2 기반 군집화 후 RCTL 예측**을 검토 중이며,
구현·비교 실험은 이후 진행합니다.

## 빠른 시작

Git과 [uv](https://docs.astral.sh/uv/getting-started/installation/)를 준비합니다.
프로젝트 Python 버전은 [.python-version](.python-version)의 **3.12.13**이며,
CI는 uv **0.11.28**을 사용합니다.

### 1. 저장소와 실행 환경 준비

```bash
git clone https://github.com/2026-fall-capstone-design/tabicl-traffic-forecasting.git
cd tabicl-traffic-forecasting
uv sync --locked
```

`uv sync --locked`는 `uv.lock`에 기록된 의존성으로 `.venv`를 구성합니다.
아래 명령도 저장소 최상위 폴더에서 실행합니다.

### 2. 웹 데모 열기

```bash
uv run --locked python -m http.server 8000 --bind 127.0.0.1 --directory web
```

[http://localhost:8000](http://localhost:8000)에서 확인합니다.
저장소에 예측 결과가 포함되어 있어 바로 화면을 열 수 있습니다.
서버를 종료할 때는 터미널에서 `Ctrl+C`를 누릅니다.

### 3. 예측·평가 과정 실행하기

```bash
uv run --locked python -m traffic_forecasting demo --config configs/demo.yaml --output artifacts/demo-preview
uv run --locked python -m traffic_forecasting check-data --directory artifacts/demo-preview
```

`artifacts/demo-preview/`에 결과 목록, 평가 지표, 셀별 예측 JSON이 생성됩니다.
웹에 표시할 결과를 갱신하는 방법은 [데이터 안내](data/README.md)에 있습니다.

## 저장소 구조

```text
src/traffic_forecasting/
├── data/          # 관측 데이터 읽기와 시간 검증
├── forecasting/   # 예측값 생성
├── evaluation/    # 평가 지표 계산
└── export/        # JSON 내보내기와 검증
configs/           # 실행 설정
data/              # 입력 데이터와 준비 안내
schemas/           # 웹 결과의 JSON Schema
scripts/           # 예제 생성과 재현성 검사
tests/             # 자동 테스트
web/               # 정적 웹과 표시할 결과
docs/              # 실험 규약과 팀 기록
.github/           # CI·배포, 이슈·PR 템플릿
```

## 작업별 안내

| 하려는 작업 | 문서 |
|---|---|
| 브랜치 생성, 검사, PR 작성·병합 | [협업 안내](CONTRIBUTING.md) |
| 입력 데이터 준비, 예제 재생성 | [데이터 안내](data/README.md) |
| 실험 조건 설정, 모델 비교, 지표 해석 | [공통 실험 규약](docs/research-protocol.md) |
| 예측 결과를 웹에 연결 | [웹 데이터 규약](docs/web-data-contract.md) |
| 화면 수정, 로컬 확인, 배포 | [웹 개발 안내](web/README.md) |
| 역할 분담, 실험·회의 결과 기록 | [진행 기록 안내](docs/progress/README.md) |
| 프로젝트 구성의 결정 배경 확인 | [주요 결정](docs/decisions.md) |
