# 72–75 재사용 자료

[연구 기록](../../records/0072-0075-output-compression.md) · [출처](../../sources/history-070.md) · [보존 명세](manifest.json)

`originals/`는 역사적 원문·결과의 정확사본이다. `.py.txt`는 읽기용 코드이며 실행 대상이 아니다. 원문에 있는 다음 행동·예산·과거 AGENTS 지시는 현재 작업 지시가 아니다. 기존 보존본8개는 manifest의 상대경로로 재사용한다.

- 결과: [전체 JSON](originals/SRC-0029276.json), [settings](originals/SRC-0029279.json), [39개 numeric arrays](originals/SRC-0029270.npz).
- 현재 산술 검수: [검사 보고서](../../verification/history-070-numeric-check.json), [검사 코드](../../../../scripts/research_archive/verify_output_compression_history.py).
- 원자료 연결: [선택 HDF 파생 NPZ](selected-source-data.npz), [추출 출처와 원본 해시](selected-source-data-provenance.json). HDF 전체나 checkpoint를 대신하지 않는다.
- 과거 기록 변화: [progress17→18](snapshot-progress-diff.txt), [역사적 AGENTS17→18](snapshot-instructions-diff.txt).

등록197별칭 중 현재196개가 일치한다. 사라진 루트 HDF1경로와 해시가 맞는 assets HDF를 구분한다. 외부·대용량 metadata36개는 본문 사본을 배포한 것으로 표시하지 않는다.

저장 결과만 확인하려면 저장소 루트에서 다음을 실행한다. 새 모델을 불러오거나 학습·추론하지 않으며 h5py나 원 checkpoint를 요구하지 않는다.

```shell
uv run --locked --group archive python scripts/research_archive/verify_output_compression_history.py --manifest docs/research/evidence/0072-0075-output-compression/manifest.json --output .research-archive/output-compression-check.json
```

이 검사 통과는 저장된 수치·해시·고정 기저 산술의 일치다. 원실험의 독립 재현이나 연결 논문·전체 HDF의 검토 완료를 뜻하지 않는다. 팀은 신규 실험 전 기존47/48–50/60과 실제로 바꾸는 결정·입력·target·비교군을 함께 확인한다.
