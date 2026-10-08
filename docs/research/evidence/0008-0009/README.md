# 08·09 보존 근거

[정리 기록](../../records/0008-0009-finite-sample-pooling.md)과 [검수](../../verification/history-002.md)를 함께 읽는다. [manifest](manifest.json)는 원문6경로의 해시·정확한 사본·읽기 범위를 연결한다. 계획·판단·과거 코드·결과 JSON4개는 여기 보존하고, B2의 큰 배열2개는 기존 보존 사본을 상대경로로 재사용한다. 새 모델 weight나 논문 전체를 포함하지 않는다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_finite_sample_history.py \
  --source docs/research/evidence/0008-0009/manifest.json \
  --output .research-archive/finite-sample-check.json
```

이 명령은 현재 작성한 검산기를 실행한다. 원 실험 코드를 실행하거나 MC 난수·모델 출력을 새로 만들지 않는다. 저장된 합성 집계의 내부 관계와 실제자료 상관·분위수 포괄률·상태 점유를 검산한다. MC 평균·표준오차의 독립 재현은 아니다. 새 Python/NumPy 환경의 작은 반올림 차이는1e−10 허용오차로 확인한다.

과거 코드와 Markdown은 `.txt`로 원바이트를 보존했다. 해시는 보존 내용의 일치 여부이며 독립 시각 인증이나 과학적 참임의 증명이 아니다. [외부 문헌 비교](../../references/finite-sample-pooling.md)는 공식 링크·판본·확인 위치만 연결한다.
