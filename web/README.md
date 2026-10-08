# 웹 개발 안내

예측 결과 JSON을 읽어 차트와 평가 지표를 보여 주는 정적 웹입니다.

[배포된 데모](https://2026-fall-capstone-design.github.io/mobile-network-traffic-forecasting/) ·
[결과 JSON 규약](../docs/web-data-contract.md)

## 파일별 역할

| 파일 | 수정할 내용 |
|---|---|
| `index.html` | 화면 구조, 설명 문구, 선택 항목 |
| `assets/style.css` | 색상, 간격, 화면 크기에 따른 배치 |
| `assets/app.js` | 데이터 로딩, 필터, 차트·표 갱신, 오류 처리 |
| `assets/vendor/chart.umd.min.js` | 차트 라이브러리 |
| `data/manifest.json` | 데이터 설명, 실험·모델·셀 목록 |
| `data/metrics/`, `data/predictions/` | 모델별 지표와 셀별 시계열 |

## 로컬에서 실행

[개발 환경](../README.md)을 준비한 뒤 저장소 최상위 폴더에서 실행합니다.

```bash
uv run --locked python -m http.server 8000 --bind 127.0.0.1 --directory web
```

[http://localhost:8000](http://localhost:8000)을 열고,
파일을 수정한 뒤 브라우저를 새로고침합니다.
JSON을 HTTP로 읽기 때문에 `index.html` 파일을 직접 더블클릭해서 여는 방식은 사용하지 않습니다.

화면은 저장된 JSON을 읽습니다.
예측 결과를 바꾸려면 [데이터 안내](../data/README.md)에 따라 결과 파일을 갱신합니다.

## 화면에서 확인할 수 있는 내용

| 영역 | 동작 |
|---|---|
| 실험 선택 | 해당 실험의 모델 목록과 전체 평가 결과 로딩 |
| 모델·셀 선택 | 선택한 셀의 실제값·예측값 표시 |
| 차트 표시 구간 | 전체, 마지막 12개, 마지막 6개 시점 선택 |
| 수치 표 | 차트에 표시된 시점의 실제값·예측값 확인 |
| 전체 평가 결과 | 선택한 모델의 지표와 모든 모델의 비교 표 |
| 실험 정보 | 데이터 이름, 평가 구간, 단위, 생성 시각, 코드 버전 |

모든 시각은 UTC로 표시합니다.
셀·표시 구간을 바꾸어도 평가 지표는 전체 테스트 표본 기준으로 유지됩니다.

## 수정 후 확인

먼저 데이터와 파일 경로를 검사합니다.

```bash
uv run --locked python -m traffic_forecasting check-data --site web
```

이어서 브라우저에서 변경한 기능을 중심으로 확인합니다.

- 실험·모델·셀을 바꿀 때 차트와 수치 표가 함께 바뀌는지
- 차트 표시 구간이 선택한 범위와 맞는지
- 셀·표시 구간 변경 후에도 전체 평가 지표가 유지되는지
- 좁은 화면에서 필터·차트·표를 사용할 수 있는지
- 키보드로 선택 항목, 수치 표, 다시 불러오기 버튼을 사용할 수 있는지
- 데이터 로딩 실패 시 안내가 표시되고, 복구 후 다시 불러오기가 동작하는지

리소스 경로는 `./assets/...`처럼 현재 페이지 기준으로 작성합니다.
GitHub Pages의 프로젝트 주소는 `/mobile-network-traffic-forecasting/` 하위에 있으므로
`/assets/...`처럼 도메인 루트부터 시작하는 경로는 맞지 않습니다.

## GitHub Pages 배포

[Checks and Pages](../.github/workflows/ci.yml)가 다음 순서로 실행됩니다.

1. PR에서 `python-check`와 `web-check`를 실행합니다.
2. PR을 `main`에 병합하면 같은 검사를 다시 실행합니다.
3. 두 검사가 성공하면 `deploy-pages`가 `web/`를 배포합니다.

배포 상태는
[GitHub Actions](https://github.com/2026-fall-capstone-design/mobile-network-traffic-forecasting/actions)에서
병합 커밋에 해당하는 실행을 확인합니다.
`deploy-pages`가 성공한 뒤 배포된 데모에서 변경 결과를 확인합니다.

## 문제가 생겼을 때

| 증상 | 확인할 항목 |
|---|---|
| 로컬에서 데이터가 표시되지 않음 | HTTP 서버로 접속했는지, `web/data/manifest.json`이 있는지 |
| 일부 모델·셀만 로딩 실패 | manifest의 파일 경로와 JSON의 실험·모델·셀 ID |
| 차트가 나오지 않음 | 브라우저 콘솔 오류, Chart.js와 `app.js`의 로딩 상태 |
| 로컬은 정상인데 배포 화면에서 파일을 못 찾음 | 도메인 루트 경로 사용 여부, 경로의 대소문자 |
| 병합 후 화면에 변경이 보이지 않음 | 해당 커밋의 검사·배포 성공 여부, 브라우저 새로고침 |
