# TabICLv2 Traffic Forecasting

4인 캡스톤 팀의 모바일 트래픽 예측 연구와 정적 웹 시각화 프로젝트입니다.

Python에서 데이터를 처리하고 예측·평가한 뒤 JSON으로 내보냅니다.
웹은 HTML·CSS·JavaScript로 결과를 표시하며 GitHub Pages에 배포합니다.

- [정적 데모](https://2026-fall-capstone-design.github.io/tabicl-traffic-forecasting/)
- [팀 작업 보드](https://github.com/orgs/2026-fall-capstone-design/projects/1)

## 현재 범위

연구 방향은 아직 결정되지 않았습니다. TabICLv2 직접 예측과 TabICLv2 기반 군집화 후
RCTL 예측을 검토하며, 데이터·평가·웹 출력 형식을 공통으로 준비합니다.
기본 환경과 예제는 실제 연구 모델의 정확도를 입증하는 결과가 아닙니다.

## 개발 환경

Python **3.12.13**, uv **0.11.28**을 기준으로 합니다.
uv 설치는 [공식 안내](https://docs.astral.sh/uv/getting-started/installation/)를 따릅니다.

```bash
git clone https://github.com/2026-fall-capstone-design/tabicl-traffic-forecasting.git
cd tabicl-traffic-forecasting
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv run --locked python -m traffic_forecasting demo --config configs/demo.yaml
uv run --locked python -m traffic_forecasting check-data --site web
uv run --locked python scripts/check_reproducibility.py
uv run --locked python -m http.server 8000 --directory web
```

마지막 명령을 실행한 뒤 <http://localhost:8000>에서 웹을 확인합니다.
JSON을 읽으므로 HTML 파일을 직접 더블클릭하는 대신 HTTP 서버를 사용합니다.
기본 데모는 합성 데이터 3개 셀과 두 기준 모델을 비교합니다.
셀·표시 구간 필터는 차트만 바꾸며, 평가 지표는 전체 테스트 표본 기준입니다.

웹 개발에 Node.js·npm·React는 필요하지 않습니다.
TabICLv2·RCTL의 실행 의존성은 선택한 구현의 호환성을 검증한 뒤 별도로 추가합니다.

## 협업

`main`의 필수 검사가 통과하면 GitHub Actions가 `web/`를 Pages에 배포합니다.
PR에서는 검사만 실행합니다. 별도 서버·API 키·웹 빌드 과정은 없습니다.

이슈는 자유롭게 작성하고 PR로 병합합니다. 승인과 리뷰 대화 해결은 필수가 아닙니다.
자세한 절차는 [기여 안내](CONTRIBUTING.md)에 있습니다.

## 문서

코드는 `src/traffic_forecasting/`, 실행 설정은 `configs/`, 검증은 `tests/`와
`schemas/`에 있습니다. `data/sample/`만 예제 데이터로 커밋하며,
`data/raw/`, `data/processed/`, `artifacts/`, `models/`는 Git에서 제외합니다.
웹에 공개할 검증된 JSON은 `web/data/`에 둡니다.

- [데이터 준비](data/README.md)
- [공통 실험 규약](docs/research-protocol.md)
- [웹 데이터 규약](docs/web-data-contract.md)
- [주요 결정](docs/decisions.md)
- [역할과 진행 기록](docs/progress/README.md)

## 공개 자료와 라이선스

프로젝트 자체의 재사용 라이선스는 팀 합의 후 결정합니다.
외부 코드·데이터·모델은 각 출처의 라이선스와 인용 조건을 확인하고 기록합니다.
개인정보가 포함된 제출 서류와 공개 권한이 없는 자료는 이 저장소에 올리지 않습니다.
