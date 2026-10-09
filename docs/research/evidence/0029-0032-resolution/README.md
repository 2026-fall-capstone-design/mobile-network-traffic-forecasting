# 29–32 재사용 근거

[연구 기록](../../records/0029-0032-resolution-diagnostic.md), [출처·읽기 범위](../../sources/history-021.md), [manifest](manifest.json), [검수](../../verification/history-021.md).

`originals/`의 24파일은 원 바이트를 보존했다. 3CSV는 Yunis-konda001의 고정 commit에서 배포한 처리된 활동량으로, 제공된 원 연구 기록의 입력이다. README·notebook 전체를 재게시하지 않고 출처에서 연결한다. 원본 경로·해시·동일 사본 source_id·접근 주소는 manifest에 있다. 기존 비용 원장은 다른 evidence의 사본을 재사용한다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_resolution_history.py   --manifest docs/research/evidence/0029-0032-resolution/manifest.json   --output .research-archive/resolution-check.json
```

검산은 표준 라이브러리와 NumPy로 파일 해시, 62일 시각 격자, 첫30일 척도·정답·naive, 16개 저장 모델 예측, 22개 방법/해상도의 MAE, cell·기간 손해, 상관·시간 내 변동, 정정 차이와 비용 entry를 확인한다. 모델 적합·추론·외부 코드 실행이나 데이터 다운로드는 포함하지 않는다. `.py.txt`는 역사적 코드의 읽기용 사본이다. 이 명령을 연구 모델 재현 성공으로 기록하지 않는다.

H5는 357,150,320 bytes라 이 묶음에 중복 복사하지 않는다. [기존 자산 접근](../../sources/pilot-006.md)의 고정 7z에서 얻을 수 있으며 SHA256은 `4371f984d6ff235ce1760869eb8fe44e10b5b0214196158f8fb8dea8b324e65e`다. [이번 H5 대조](../../verification/history-021-H5-check.json)는 로컬 자산의 지정 세cell/720시간 검수이며 CI의 자동 다운로드 검증이 아니다.

실제 fit X·모델 객체·당시 환경 전체·Telecom Italia 원시 각10분값과의 대조는 미확인이다. `summary_initial_timestamp_unit_bug.json`의 최초 값과 수정 summary를 함께 남겨 0.6초 표기의 원인과 정정 범위를 추적할 수 있게 했다.
