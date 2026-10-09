# 조건부 공유 비용 검수

[정리 기록](../records/0023-0025-conditional-pooling.md)의 [출처15개](../sources/history-016.md)를 대조했다. [778개 기계 검사](history-016-pooling-check.json)는 원본 식별·설정·114개 배열·54개 결과행·9개 순위행·정규화·입력을 확인한다. Tab 분포와 중앙값의36조건은 저장 atom의 CDF 적분으로 비용을 검산하고 저장 예측의 가중 중앙값 최적성을 확인했다. 이 산술과 새 예측 모델 실행을 구분한다.

[18개 오류 자료 검사](history-016-negative-check.json)는 격리 사본의 행 누락·중복, 주 설정 치환, bool/int 혼동, 시간·순위·원본 해시 불일치, density 질량, 비유한 예측, 정규화·lag 오류를 거부했다. 특히 잘못된 예측이나 비용을 넣고 관련 JSON 집계와 해시까지 함께 고친 사본도 최적성·CDF 검사에서 거부했다. 원자료는 수정하지 않았다.

[12개 주장·원문 위치·한계](history-016-primary-review.json)와 [문서·원문 상태 확인](history-016-document-check.json)은 정의와 실행 상태, 개발 자료 범위, 표의 수치, 실패·비용의 근거 경계를 연결한다. 같은 정리 에이전트의 두 번째 대조이며 독립 연구자 검증이 아니다. 모델0회·원 연구 스크립트 실행/import0회다.

팀은 보존 자료로 다음 검산을 할 수 있다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_conditional_pooling_history.py --manifest docs/research/evidence/0023-0025-pooling/manifest.json --output .research-archive/checked-conditional-pooling.json
```

NPZ는 객체 역직렬화를 금지했다. `dates.npy`는 pickletools로 문자열 리터럴만 읽어 시간 간격을 검사했으며 pickle을 실행하지 않는다. 선택16cell의 저장 입력을 raw/scales와 대조한 최대 차이0과 Tab 비용의 최대 차이 약1.16×10⁻¹³은 해당 저장 자료에 대한 결과다.

원 H5 신규 대조, KNN atom·density 최근접 이웃 재구성, 과거 runtime·실패 콘솔의 독립 확인, 전체25·24·문헌·후속 기록은 미완료다. 처음부터 정한 경계와 검산 한계를 유지하며 이를 모델 성능 재현이나 새로운 소속의 독립 검증으로 표시하지 않는다.
