# 56–58 MAE 표본추출의 보존 근거

[연구 기록](../../records/0056-0058-mae-sampling.md) · [출처·범위](../../sources/history-045.md) · [manifest](manifest.json) · [일차 대조](../../verification/history-045-primary-check.json) · [산술 결과](../../verification/history-045-portable-check.json)

새 사본 16개 40,572bytes와 기존 사본 참조 5개를 연결한다. 원 코드·문서·JSON은 바이트 그대로 보존했다. `.py.txt`는 열람 자료이며 원 스크립트 실행은 검수 절차가 아니다. 논문 PDF·그림은 정식 URL과 해시·읽은 범위만 게시한다. 해시 전용 15개 자료는 본문 독해 완료가 아니다.

저장소 루트에서 다음 명령은 보존 파일만 읽어 세 결과의 정확한 분수 평균·분산, 57 원장의 한 항목 차이, 과거 epoch 기반 step·처리 행과 fit 초 합을 계산한다. 원 연구 코드를 import하지 않으며 모델·checkpoint·난수·네트워크를 사용하지 않는다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_mae_sampling_history.py \
  --manifest docs/research/evidence/0056-0058-mae-sampling/manifest.json \
  --output .research-archive/mae-sampling-check.json
```

이 검산은 실제 RCTL 학습·수렴·성능 재현과 구분한다. 역사적 실행의 독립 console/exit code, 전체 process 시간, 논문 부록·저자 실행 결과, 당시 정확한 라이브러리 환경은 이 명령으로 확인되지 않는다. 56/58의 나머지 네 문헌은 후속 검토 대상이다.
