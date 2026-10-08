# 초기 B1·B2 근거

[B1](../../records/0003-b1-anchor-projection.md), [B2](../../records/0004-0007-b2-observed-risk.md), [원문별 범위](../../sources/history-001.md), [검수](../../verification/history-001.md).

[manifest](manifest.json)는98원본 경로의 SHA-256·크기·원래 ID·정확사본·읽은 범위·팀 보존 경로를 연결한다. 새95파일(26,356,643bytes), 기존 바이트 동일3파일을 재사용한다. 원문은 수정하지 않았고 코드·Markdown은 `.txt`로 보존했다.

주요 근거는 B1의 분위수·anchor·가중치·소속, B2의 다섯 손실표·상태 배정·기준 예측·소속, 다음 주 surrogate, RCTL 29group 예측과 학습 이력, 8조건 평가, 설정과 해시다. B1의 partial이라는 이름의 파일도 최종 예측과 같은 배열을 끝까지 포함해 수치 동일성을 확인했다. 파일 이름만으로 중단 실행으로 분류하지 않는다.

원본과 같은 값의 산술 검산은 저장소 루트에서 다음으로 수행한다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_early_risk_history.py \
  --source docs/research/evidence/0003-0007/manifest.json \
  --output .research-archive/check-early-risk.json
```

이 명령은 옛 연구 코드를 import하지 않고 NumPy로 저장값만 대조한다. Tab/RCTL 등 학습·추론이나 KMeans/Ridge/KNN을 실행하지 않는다. `allow_pickle=False`이며 NPZ의 object dates는 읽지 않는다. 모델 `.pt`는 이 묶음에 복사하지 않았다.

H5와 checkpoint·라이브러리는 [초기 자산 안내](../0001-0002/README.md)를 따른다. [H5 결과](../../verification/history-001-H5-check.json)는 원파일 해시와 16cell 지정 열의 로컬 대조이고, 위 portable 명령이나 CI에서 대형 H5를 다시 읽었다는 뜻은 아니다. 알려진 상류 처리·실행 환경 공백은 기록에 남겨두었다.
