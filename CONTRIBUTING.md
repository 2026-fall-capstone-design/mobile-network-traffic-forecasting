# 함께 작업하는 방법

## 기본 규칙

- 이슈는 필요할 때 자유롭게 작성합니다. 빈 이슈와 기존 템플릿을 모두 사용할 수 있습니다.
- 이슈 연결, 브랜치 이름의 이슈 번호, 이슈 미작성 사유는 필수가 아닙니다.
- `main`에는 PR로 병합합니다. 필요한 승인 수는 **0명**입니다.
- 리뷰와 리뷰 대화 해결은 선택입니다. CodeRabbit 결과도 참고용입니다.
- CI의 `python-check`, `web-check`를 통과한 PR을 작성자가 직접 Squash 병합할 수 있습니다.
- 병합 전에 최신 `main`을 반영합니다. 작업 브랜치는 병합 후 자동 삭제됩니다.
- `main` 강제 푸시와 삭제를 차단합니다. 관리자도 평소에는 같은 PR 흐름을 사용합니다.

브랜치 예: `feat/data-loader`, `fix/time-alignment`, `docs/experiment-guide`.
Codex가 만드는 작업 브랜치는 `codex/` 접두사를 사용합니다.

## 로컬 개발

Python 3.12.13과 uv를 사용합니다. Windows에서는 연구 실행에 WSL2를 권장합니다.
저장소마다 가상환경을 만들며 `.venv`는 커밋하지 않습니다.

```bash
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv run --locked python -m traffic_forecasting check-data --site web
uv run --locked python scripts/check_reproducibility.py
```

의존성을 바꿀 때는 `pyproject.toml`과 `uv.lock`을 함께 커밋합니다.
CI에서 사용하는 uv 버전은 0.11.28입니다. Python이나 uv를 바꿀 때도 PR로 검증합니다.
GPU·모델 가중치가 필요한 실험 환경은 기본 개발 환경과 구분하여 기록합니다.

## PR 작성과 CodeRabbit

1. 작업 브랜치를 푸시하고 `main` 대상으로 PR을 엽니다.
2. 제목 자동 작성을 원하면 PR 제목을 `@coderabbitai`로 지정합니다.
3. 템플릿의 `@coderabbitai summary` 위치에 CodeRabbit이 변경 요약을 작성합니다.
4. 리뷰가 자동으로 시작되지 않으면 `Trigger review`를 누르거나 PR 댓글에
   `@coderabbitai review`를 작성합니다. 무료 공개 레포 정책에서는 별 10개 미만인 경우
   수동 요청이 필요하며, 체험 요금제에서는 자동으로 시작될 수 있습니다.
5. 생성된 제목·요약을 확인하고, 직접 확인한 내용이 있으면 보완합니다.
6. 필수 CI가 통과하면 별도 승인 없이 병합할 수 있습니다.

CodeRabbit은 필수 검사나 필수 승인자로 지정하지 않습니다. 유료 Coding Agent,
자동 수정, 자동 병합, 푸시만으로 PR을 생성하는 자동화는 기본 구성에 포함하지 않습니다.
정책이 바뀌면 [공식 요금제 문서](https://docs.coderabbit.ai/management/plans)를 확인합니다.

## 연구 변경

데이터·모델·평가가 바뀌면 실행 설정과 결과 위치를 기록합니다. 이슈, PR 설명,
`docs/progress/` 중 편한 곳을 사용합니다. 평가 기준은
[공통 실험 규약](docs/research-protocol.md)을 따릅니다.

성능이 개선되지 않아도 비교 조건과 해석을 남기면 유효한 연구 결과입니다.
전체 원본 데이터·가중치·캐시·비밀키는 커밋하지 않습니다.

## 작업 보드와 마일스톤

[팀 보드](https://github.com/orgs/2026-fall-capstone-design/projects/1)는 선택적으로 사용합니다.
Backlog → Ready → In Progress → In Review → Done 순서입니다.
필요한 작업이나 PR만 추가하며 모든 작업을 이슈로 만들 필요는 없습니다.
프로젝트는 조직 내부용이며, 접근 권한은 조직의 프로젝트 권한 설정을 따릅니다.

마일스톤은 환경과 합성 예제 → 데이터와 기준 모델 → 연구 비교 실험 → 최종 데모와 보고서로
준비했습니다. 일정과 담당자는 팀에서 정합니다. `area:*` 라벨로 작업 영역을 표시할 수 있습니다.
