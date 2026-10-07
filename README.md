# TabICLv2 Traffic Forecasting

4인 캡스톤 팀의 모바일 트래픽 예측 연구와 정적 웹 시각화 프로젝트입니다.

Python에서 데이터를 처리하고 예측·평가한 뒤 JSON으로 내보냅니다.
웹은 HTML·CSS·JavaScript로 결과를 표시하며 GitHub Pages에 배포합니다.

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
uv run --locked python -m traffic_forecasting check-data
```

웹 개발에 Node.js·npm·React는 필요하지 않습니다.
TabICLv2·RCTL의 실행 의존성은 선택한 구현의 호환성을 검증한 뒤 별도로 추가합니다.

## 협업

이슈는 자유롭게 작성하고 PR로 병합합니다. 승인과 리뷰 대화 해결은 필수가 아닙니다.
자세한 절차는 [기여 안내](CONTRIBUTING.md)에 있습니다.

## 문서

- [데이터 준비](data/README.md)
- [공통 실험 규약](docs/research-protocol.md)
- [웹 데이터 규약](docs/web-data-contract.md)
- [주요 결정](docs/decisions.md)
- [역할과 진행 기록](docs/progress/README.md)

## 공개 자료와 라이선스

프로젝트 자체의 재사용 라이선스는 팀 합의 후 결정합니다.
외부 코드·데이터·모델은 각 출처의 라이선스와 인용 조건을 확인하고 기록합니다.
개인정보가 포함된 제출 서류와 공개 권한이 없는 자료는 이 저장소에 올리지 않습니다.
