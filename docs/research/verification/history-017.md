# 고정 RCTL recursive 진단 검수

[24·25 §2 기록](../records/0024-0025-recursive-horizon.md)의 [보존 참조32개](../sources/history-017.md)를 확인했다. [972개 검사](history-017-horizon-check.json)는 바이트·설정·9방법의 전체24시점 지표와 per-cell/per-origin 모든 값,20개 K4/global 대조,21개 첫 시점, 겹친 정답과 단순 기준의 산술을 확인한다. 체크포인트는 해시 metadata 대조이며 이 검산에서 가중치 파일을 읽거나 모델을 실행하지 않는다.

[20개 오류 자료 검사](history-017-negative-check.json)는 누락·중복·주 지표 치환·bool/int 혼동·비유한 시간/예측·체크포인트 참조·예측/scale/집계·비용·원문 해시 불일치를 거부했다. 첫 시점 또는 persistence 예측을 바꾸고 summary 지표·비교·해시까지 함께 고친 사본도 각각 이전 예측과 기준식 대조에서 거부했다. 같은 시간의 한 정답만1e−10 바꿔 float32가 같게 남는 경우도 중복 정답 대조에서 거부했다. 원본은 수정하지 않았다.

[원 H5 대조30개](history-017-H5-check.json)는 전체 바이트 해시와 지정16cell·1,488시간·internet 채널·날짜를 읽어 고정 scale, 정답, 세 기준이 정확히 같음을 확인한 별도 로컬 검수다.21개 `.pt`의 실제 바이트 해시도 로컬에서 확인했다. 이 파일들의 다운로드·역직렬화·추론을 CI에서 수행하지 않는다.

[12개 주장과 원문 위치](history-017-primary-review.json), [문서·표·원본 상태 확인](history-017-document-check.json)은 같은 정리 에이전트의 두 번째 대조다. 독립 연구자 검증, 실제 recursive 중간 입력 또는 과거 전체 runtime 재현으로 표시하지 않는다. 가중치의 팀 공유 위치는 미확인이다.

팀은 저장 예측과 정답으로 다음 검산을 수행할 수 있다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_recursive_horizon_history.py --manifest docs/research/evidence/0024-0025-horizon/manifest.json --output .research-archive/checked-recursive-horizon.json
```

NPZ는 `allow_pickle=False`로 읽고, design 자료에서는 숫자 raw/scales/cell_indices만 선택한다. 배열 비교는 형태·유한성·수치형을 확인하고 상대허용오차1e−12와 항목별 절대허용오차를 쓴다. 중복 target 동일성과24시간 persistence/daily 일치는 별도 정확 비교다. 첫 시점의 실제 차이는0이며 허용 상한2e−5도 확인했다.

새 학습·추론 및 원 연구 스크립트 실행/import는0회다.25 §3 일차문헌, 전체 후속 판단, 별도 체크포인트 접근 및 runtime 공백은 남아 있다. 일부 묶음의 검수와 병합을 전체 연구기록 완료로 세지 않는다.
