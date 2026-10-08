# 초기 01–02 원문과 읽은 범위

[연구 기록](../records/0001-0002-initial-design.md), [근거 안내](../evidence/0001-0002/README.md), [검수](../verification/pilot-006.md). 원문 번호와 source_id를 함께 보존한다. 코드·옛 Goal·예산은 역사적 자료다.

## 저장소에서 열 수 있는 작은 원문

13파일을 바이트 그대로 보존했다. 본문 전체 읽기는 7개, 나머지 6개 배열은 아래 명시한 필드를 검산했다. 자동 SHA 확인과 본문 검토를 구분한다. 원본 전체의 별칭 관계는 [manifest](../evidence/0001-0002/manifest.json)에 있다.

| source_id | 원본 루트 기준 경로 / 보존 사본 | 실제 검토 |
|---|---|---|
| SRC-0020822 | [tmp/redesign_20260925/01_data_and_smoke_plan.md](../evidence/0001-0002/originals/SRC-0020822.md.txt) | 본문 전체 1–16행 |
| SRC-0020823 | [tmp/redesign_20260925/02_candidate_and_pilot_plan.md](../evidence/0001-0002/originals/SRC-0020823.md.txt) | 본문 전체 1–56행 |
| SRC-0022507 | [tmp/redesign_20260925/asset_manifest.json](../evidence/0001-0002/originals/SRC-0022507.json) | 본문 전체 1–41행 |
| SRC-0022703 | [tmp/redesign_20260925/data_and_smoke.py](../evidence/0001-0002/originals/SRC-0022703.py.txt) | 본문 전체 1–61행 |
| SRC-0022761 | [tmp/redesign_20260925/fetch_manifest.json](../evidence/0001-0002/originals/SRC-0022761.json) | 본문 전체 1–111행 |
| SRC-0023576 | [tmp/redesign_20260925/results/data_diagnostic.json](../evidence/0001-0002/originals/SRC-0023576.json) | 본문 전체 1–285행 |
| SRC-0023577 | [tmp/redesign_20260925/results/design_data.npz](../evidence/0001-0002/originals/SRC-0023577.npz) | X, Y, cell_indices, raw, scales, times |
| SRC-0023578 | [tmp/redesign_20260925/results/diagnostic_correlations.npz](../evidence/0001-0002/originals/SRC-0023578.npz) | raw_corr, residual_corr, ridge_errors |
| SRC-0023607 | [tmp/redesign_20260925/results/smoke.json](../evidence/0001-0002/originals/SRC-0023607.json) | 본문 전체 1–67행 |
| SRC-0023608 | [tmp/redesign_20260925/results/smoke_cell_3737.npz](../evidence/0001-0002/originals/SRC-0023608.npz) | context_indices, pred, query_indices, y |
| SRC-0023609 | [tmp/redesign_20260925/results/smoke_cell_3765.npz](../evidence/0001-0002/originals/SRC-0023609.npz) | context_indices, pred, query_indices, y |
| SRC-0023610 | [tmp/redesign_20260925/results/smoke_cell_6137.npz](../evidence/0001-0002/originals/SRC-0023610.npz) | context_indices, pred, query_indices, y |
| SRC-0023611 | [tmp/redesign_20260925/results/smoke_cell_6165.npz](../evidence/0001-0002/originals/SRC-0023611.npz) | context_indices, pred, query_indices, y |

`design_data.npz`의 object형 dates는 읽지 않았다. H5의 날짜를 별도로 추출해 calendar 특징을 확인했다. 32cell 진단 Ridge는 저장 오차를 검산했고, 네 smoke Ridge의 MAE는 저장 JSON의 보고값만 확인했다.

## 외부 원문과 대용량 자산

다음 원문은 다시 게시하지 않고 식별정보·공식 주소·지정 구간을 연결한다. 체크포인트/소스 ZIP의 해시 확인은 내부 내용 검토나 실행을 뜻하지 않는다.

| source_id | 공식 접근 | 읽기와 확인 범위 |
|---|---|---|
| SRC-0023484 | [STCNet_preprocessing.py](https://raw.githubusercontent.com/chuanting/STCNet/dc3ff65eb42b099ef8ec281c10282d6c47b533cb/Github_Version/data/hour_level_demo.py) | 본문 전체 [1, 100]; 고정commit 바이트 일치 |
| SRC-0023485 | [data_git_version.h5](https://media.githubusercontent.com/media/chuanting/STCNet/dc3ff65eb42b099ef8ec281c10282d6c47b533cb/Github_Version/data/data_git_version.7z) | H5 shape, idx 전체, 처음1008시간×고정32cell×채널2. 원 target 전체는 읽지 않음. 7z멤버 SRC-0073719와 바이트 동일 |
| SRC-0061698 | [Milan_official_metadata.json](https://doi.org/10.7910/DVN/EGZHFV) | 당시 v1.3: 상태·DOI·버전·이용조건·지정 citation 값만. 현재 웹 본문 접근 미확인 |
| SRC-0061707 | [STCNet_README.txt](https://raw.githubusercontent.com/chuanting/STCNet/dc3ff65eb42b099ef8ec281c10282d6c47b533cb/readme.md) | 본문 전체 [1, 59]; 고정commit 바이트 일치 |
| SRC-0061708 | [STCNet_data_pointer.txt](https://raw.githubusercontent.com/chuanting/STCNet/dc3ff65eb42b099ef8ec281c10282d6c47b533cb/Github_Version/data/data_git_version.7z) | 본문 전체 [1, 3]; 고정commit 바이트 일치 |
| SRC-0061714 | [TabICLv2_model_metadata.json](https://huggingface.co/jingang/TabICL/tree/4dcd344ece2c00be9e831fdd35bed57b5ad83e19) | 본문 전체 [1, 1]; 당시 모델 메타데이터, 현재 상태 검증 아님 |
| SRC-0023486 | [milan_stcnet.7z](https://media.githubusercontent.com/media/chuanting/STCNet/dc3ff65eb42b099ef8ec281c10282d6c47b533cb/Github_Version/data/data_git_version.7z) | 로컬 전체 바이트 SHA/크기와 당시 asset manifest 대조. 모델 로드·코드 실행 없음 |
| SRC-0023488 | [tabicl-regressor-v2-20260212.ckpt](https://huggingface.co/jingang/TabICL/resolve/4dcd344ece2c00be9e831fdd35bed57b5ad83e19/tabicl-regressor-v2-20260212.ckpt) | 로컬 전체 바이트 SHA/크기와 당시 asset manifest 대조. 모델 로드·코드 실행 없음 |
| SRC-0023489 | [tabicl_source.zip](https://codeload.github.com/soda-inria/tabicl/zip/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3) | 로컬 전체 바이트 SHA/크기와 당시 asset manifest 대조. 모델 로드·코드 실행 없음 |

STCNet 전처리 예시·README·LFS pointer는 공식 commit의 작은 원문 바이트와 일치했다. H5 지정 구간과 압축 내부 동일성은 별도 검수 증거에 남겼으며, CI가 대용량 파일을 내려받아 다시 확인한다고 표시하지 않는다.

## 아직 연결해야 하는 기록

목록상 후속 03(projection), 04(observed query risk), 05(literature audit), 06(loss table), 07(RCTL decision), 08(finite sample information), 09(additional path) 문서가 있다. 이 묶음에서는 제목·경로만 확인했으며 본문/실행 근거 검토는 대기 중이다. 02를 전체 미실행으로 분류하거나 후속 성패를 추정하지 않는다. 원 자료 전처리 전체와 초기 계획을 인용한 모든 개정본도 이 묶음 완료 범위에 포함하지 않는다.
