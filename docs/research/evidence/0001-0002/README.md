# 초기 01–02의 저장 근거와 데이터 출처

[연구 기록](../../records/0001-0002-initial-design.md), [13개 보존 원문·배열](manifest.json), [실제 읽은 범위](../../sources/pilot-006.md), [검수](../../verification/pilot-006.md)를 함께 읽는다. 새로 보존한 13파일은 합계 830,786 byte다. 원문 Markdown/Python은 `.txt`를 덧붙여 바이트 그대로 보존했으며 당시 실행 지시나 모델 코드를 현재 실행하지 않는다.

`design_data.npz`의 `X/Y/raw/scales/cell_indices/times`, `diagnostic_correlations.npz`의 저장 오차·상관행렬, 네 `smoke_cell_*.npz`의 예측·정답·시점을 보존했다. `design_data`의 object형 `dates`는 역직렬화하지 않았다. 별도 [H5 날짜 발췌](derived/h5-timestamps.json)는 정리 과정에 만든 UTF-8 JSON으로 **원본 파일과 구분**한다.

## 대용량 자산과 입수 경로

| 자산 | 고정된 입수 경로 | 크기 / SHA-256 |
|---|---|---|
| STCNet 7z | [commit dc3ff65의 실제 LFS 내용](https://media.githubusercontent.com/media/chuanting/STCNet/dc3ff65eb42b099ef8ec281c10282d6c47b533cb/Github_Version/data/data_git_version.7z) | 105,531,494 byte / `c2ee5848be863086c5addc1de33bace990bf8cd357e87fd8dafbf1f23bb7ae27` |
| 압축 안 H5 | 위 7z의 `data_git_version.h5` | 357,150,320 byte / `4371f984d6ff235ce1760869eb8fe44e10b5b0214196158f8fb8dea8b324e65e` |
| TabICLv2 regressor | [HF revision 4dcd344](https://huggingface.co/jingang/TabICL/resolve/4dcd344ece2c00be9e831fdd35bed57b5ad83e19/tabicl-regressor-v2-20260212.ckpt) | 114,324,594 byte / `0db9cb538f114e79026bf08f45f41ad8dd7ad2de2aaca9a5ca8cd3bd9748ae7a` |
| TabICL 소스 ZIP | [commit 0dbff3e](https://codeload.github.com/soda-inria/tabicl/zip/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3) | 2,138,242 byte / `810631974c22f2133e4890ca9953f475d13150835837f400b9fa5418970646ed` |

이 네 큰 파일은 저장소에 복제하지 않았다. 로컬 7z/checkpoint/ZIP의 바이트 해시를 목록과 당시 asset manifest에 대조했다. 공식 commit의 Git LFS pointer도 일치했다. 7z 내부 H5는 파일을 실행하거나 원본 폴더에 풀지 않고 스트림 해시를 계산해, 실제 읽은 H5와 동일함을 확인했다. checkpoint를 로드하거나 소스 ZIP의 모든 코드를 검토한 것은 아니다. [자산 동일성 증거](../../verification/pilot-006-assets-check.json)

공식 [STCNet README](https://github.com/chuanting/STCNet/blob/dc3ff65eb42b099ef8ec281c10282d6c47b533cb/readme.md)와 [전처리 예시](https://github.com/chuanting/STCNet/blob/dc3ff65eb42b099ef8ec281c10282d6c47b533cb/Github_Version/data/hour_level_demo.py)는 저장된 사본을 전체 읽고 해당 commit의 바이트와 비교했다. README는 채널 통합·반올림을 설명하지만, 전처리 예시 자체의 출력은 다섯 채널이며 월별 입력 경로 설정 등 추가 확인이 필요하다. 배포 H5를 원 CDR부터 재생성한 것은 아니다. README의 연말 특이 시점 처리 설명을 이번 01의 전처리로 사용했다고 단정하지 않는다.

당시 STCNet 논문 PDF 링크는 404, 일부 다른 문헌 링크는 403으로 기록돼 있다. 다운로드 목록의 실패 항목을 확보·본문 검토 완료로 세지 않았다. [당시 자산 기록](originals/SRC-0022507.json), [당시 문헌 다운로드 기록](originals/SRC-0022761.json)

## 원자료 표시와 데이터 이용 조건

원자료: Telecom Italia, **Telecommunications - SMS, Call, Internet - MI**, [Harvard Dataverse DOI 10.7910/DVN/EGZHFV](https://doi.org/10.7910/DVN/EGZHFV), **[from BigDataChallenge contest](http://www.telecomitalia.com/tit/en/bigdatachallenge.html)**. 자료 안내는 [ODI node Trento](http://theodi.fbk.eu/)에도 연결된다. STCNet 저자의 가공 배포본을 통해 연구 입력으로 사용했다.

연구 폴더에 보존된 Dataverse v1.3 메타데이터의 `termsOfUse`는 **ODbL 1.0**과 출처 표시·동일 조건 공유를 명시한다. 이 묶음에 포함된 해당 데이터 및 가공 데이터 부분에도 [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/)과 원자료 출처를 함께 표시한다. 저장소의 코드 라이선스를 원자료의 조건으로 바꿔 읽지 않는다. [검토한 메타데이터 항목](../../verification/pilot-006-dataset-metadata.json)

현재 Dataverse 웹 조회는 접근 확인 화면으로 본문을 읽지 못했다. 위 조건은 해시가 확인된 당시 메타데이터에서 읽었으며, 최신 약관을 새로 조회했다고 주장하지 않는다. 원자료 개별 파일 전체와 모든 전처리 단계는 별도 미검토 범위다.

## 저장 결과만 검사하기

저장소 루트에서 다음 명령은 작은 보존 배열과 날짜 발췌만 읽는다. H5 다운로드, checkpoint 로드, 모델 학습·추론은 하지 않는다.

```sh
uv run --locked --group archive python scripts/research_archive/verify_initial_pilot.py \
  --source docs/research/evidence/0001-0002/manifest.json \
  --output .research-archive/initial-check.json
```

CI에서는 보존 배열·원문 해시·명시된 필드·날짜 발췌를 확인한다. 로컬에서 별도로 수행한 H5 지정 구간 확인과 대용량 자산 해시 확인을 CI가 매번 반복하는 것은 아니다. 계산된 값의 일치가 모델 재현이나 최종 방법의 효용 검증을 뜻하지 않는다.
