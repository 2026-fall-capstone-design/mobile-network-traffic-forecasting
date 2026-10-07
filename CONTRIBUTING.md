# 협업 안내

기본 환경 설치와 웹 실행은 [README](README.md)의 빠른 시작을 따릅니다.
이 문서는 작업 브랜치에서 PR 병합까지의 흐름을 설명합니다.

## 협업 규칙

| 항목 | 운영 방식 |
|---|---|
| 이슈 | 자유롭게 작성합니다. 빈 이슈와 작업·버그·실험 템플릿을 사용할 수 있습니다. |
| 변경 반영 | 작업 브랜치에서 PR을 만들고 `main`에 Squash 병합합니다. |
| 필수 검사 | `python-check`, `web-check` |
| 승인·리뷰 | 승인 인원은 0명이며, 리뷰 대화 해결과 CodeRabbit 완료는 병합 필수 조건이 아닙니다. |
| 브랜치 정리 | 병합한 원격 작업 브랜치는 자동으로 삭제됩니다. |

## 1. 작업 시작

최신 `main`에서 작업 브랜치를 만듭니다.

```bash
git switch main
git pull --ff-only
git switch -c feat/result-filter
```

브랜치 이름은 작업 내용을 알아볼 수 있게 정합니다.
예를 들어 `feat/data-loader`, `fix/time-alignment`, `docs/experiment-guide`를 사용합니다.
위 예제의 `feat/result-filter`는 실제 작업에 맞게 바꿉니다.

한 PR에는 함께 설명하고 검토할 수 있는 변경을 담습니다.
실행 방법이나 결과 형식을 바꾸면 관련 문서도 같은 PR에서 수정합니다.

## 2. 변경 확인

저장소 최상위 폴더에서 다음 검사를 실행할 수 있습니다.

```bash
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv run --locked python -m traffic_forecasting check-data --site web
uv run --locked python scripts/check_reproducibility.py
```

| CI 작업 | 검사 내용 |
|---|---|
| `python-check` | Python 정적 검사, 코드 포맷, 자동 테스트 |
| `web-check` | JSON 형식과 파일 간 일관성, HTML의 로컬 CSS·스크립트 경로, 예제 결과 재현성 |

포맷 검사만 실패했다면 `uv run --locked ruff format .`으로 정리하고 변경 내용을 확인합니다.
웹 화면을 수정했다면 [웹 개발 안내](web/README.md)의 화면 확인 항목도 점검합니다.

의존성을 추가·변경할 때는 `pyproject.toml`과 `uv.lock`을 함께 반영합니다.
Python 버전은 `.python-version`, CI의 uv 버전은
[워크플로](.github/workflows/ci.yml)에서 관리합니다.

## 3. PR 작성

수정한 파일을 커밋한 뒤 작업 브랜치를 푸시하고, GitHub에서 `main`을 대상으로 PR을 엽니다.

```bash
git push -u origin feat/result-filter
```

PR 본문은 다음 세 가지를 중심으로 작성합니다.

| 항목 | 작성할 내용 |
|---|---|
| 변경 내용 | 해결하려는 문제와 변경 후 동작 |
| 확인한 내용 | 직접 실행한 명령과 결과, 화면 확인 내용 |
| 참고 사항 | 관련 자료, 스크린샷, 후속 작업 등 필요한 설명 |

관련 이슈가 있다면 링크를 넣습니다. 이슈 없이도 PR을 만들 수 있습니다.

### CodeRabbit 사용

| 목적 | 사용 방법 |
|---|---|
| 제목 자동 생성 | PR 제목에 `@coderabbitai` 입력 |
| 본문 요약 자동 생성 | 템플릿의 `@coderabbitai summary` 유지 |
| 리뷰 요청 | PR 댓글에 `@coderabbitai review` 작성 |
| PR 전체 다시 검토 | PR 댓글에 `@coderabbitai full review` 작성 |

자동 생성된 제목과 요약을 읽고 실제 변경과 맞는지 확인합니다.
`확인한 내용`에는 작성자가 수행한 검증을 기록합니다.

현재 설정은 `main` 대상의 Draft가 아닌 PR에 자동 리뷰를 요청하며,
리뷰와 대화 답변은 한국어로 작성하도록 되어 있습니다.
리뷰 결과를 반영할 계획이라면 `Review completed`와 실제 검토 내용을 확인한 뒤 병합합니다.
`Review in progress`는 진행 중, `Review skipped`는 검토를 건너뛴 상태입니다.

설정은 [.coderabbit.yaml](.coderabbit.yaml), 추가 명령은
[CodeRabbit 공식 안내](https://docs.coderabbit.ai/reference/review-commands)에서 확인합니다.

## 4. 최신 main 반영과 병합

다른 PR이 먼저 병합되었다면 현재 작업 브랜치에서 최신 `main`을 반영합니다.

```bash
git fetch origin
git merge origin/main
```

충돌이 있다면 해당 파일을 수정하고 해결한 변경을 커밋합니다.
이후 `git push`로 PR을 갱신합니다.

PR의 변경 파일과 확인 결과를 검토하고, `python-check`와 `web-check`가 통과하면
**Squash and merge**로 병합합니다. 다음 작업은 최신 `main`에서 시작합니다.

```bash
git switch main
git pull --ff-only
```

병합 후에는 `main`의 검사와 Pages 배포가 실행됩니다.
진행 상태는 저장소의 **Actions → Checks and Pages**에서 확인합니다.

## 작업 보드와 라벨

[팀 작업 보드](https://github.com/orgs/2026-fall-capstone-design/projects/1)에는
공유할 작업이나 PR을 추가합니다. 상태는 다음 기준으로 사용합니다.

| 상태 | 의미 |
|---|---|
| Backlog | 아직 범위나 우선순위를 정하지 않은 작업 |
| Ready | 착수할 수 있도록 목표와 범위를 정한 작업 |
| In Progress | 구현·분석 중인 작업 |
| In Review | PR 검토나 결과 확인 중인 작업 |
| Done | 병합하거나 결과 정리를 마친 작업 |

라벨은 작업 종류와 영역을 조합합니다.
데이터 오류 수정에는 `bug`와 `data`, 모델 비교에는 `experiment`와 `model`을 붙일 수 있습니다.

| 라벨 | 용도 |
|---|---|
| `task` | 기능 구현과 일반 작업 |
| `bug` | 오류 재현과 수정 |
| `docs` | 문서 작성과 수정 |
| `experiment` | 실험 수행과 결과 비교 |
| `data` | 데이터 수집과 전처리 |
| `model` | 예측·군집화 모델 |
| `evaluation` | 평가 지표와 재현성 |
| `web` | 정적 웹과 시각화 |
| `infra` | 개발 환경과 CI·배포 |
| `blocked` | 선행 작업이나 결정 대기 |

진행 단계와 기록 양식은 [진행 기록 안내](docs/progress/README.md)를 참고합니다.
