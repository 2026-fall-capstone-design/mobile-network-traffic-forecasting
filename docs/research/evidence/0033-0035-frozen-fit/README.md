# 33–35 고정 RCTL fit gap 근거

[팀 기록](../../records/0033-0035-process-fit-gap.md) · [출처](../../sources/history-022.md) · [manifest](manifest.json)

새 원문 사본 13개 578,461 bytes와 기존 사본 7개를 연결한다. original 사본의 바이트·줄바꿈은 원본과 같고, 설명과 문서 표는 별도다. Python 원문은 .py.txt로 보존하며 연구 실행을 위한 자동 진입점으로 제공하지 않는다.

저장 예측 NPZ의 61배열은 29 checkpoint의 train/validation 출력 58개와 cell_ids·train_y·validation_y다. 29개 .pt는 metadata만 있고 파일 게시·팀 접근 검증은 미완료다. 원문 PDF·그림은 정식 링크와 SHA로 식별한다.

## 모델 없이 저장 결과 확인

저장소 루트에서 다음을 실행할 수 있다.

~~~shell
uv sync --locked --group archive
uv run --locked --group archive python scripts/research_archive/verify_frozen_fit_history.py --manifest docs/research/evidence/0033-0035-frozen-fit/manifest.json --output .research-archive/frozen-fit-check.json
~~~

이 검산은 표준 라이브러리와 NumPy를 사용한다. 보존 자료 해시·입력/정답·29개 결과·8개 집계·계산 step·정적 parameter·지정 누적 비용을 확인한다. 원래 연구 코드를 import/실행하지 않고 torch/checkpoint/모델을 불러오지 않는다. CI의 가중치 확인은 metadata 대조이며 로컬 원본의 바이트 감사와 다르다.

문서 표의 값과 반올림은 [document-tables.json](document-tables.json)에 있다. 앞·뒤 validation 분해는 같은 예측을 사용한 추가 산술로, 새 독립 평가가 아니다. saved test 지표는 기존 fit 결과를 복사한 값이며 새 test inference가 없다. 수치 일치가 당시 실행 입력·모델 상태의 완전한 재현을 의미하지 않는다.
