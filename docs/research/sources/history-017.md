# 고정 RCTL recursive 진단의 출처와 읽은 범위

[24·25 §2 기록](../records/0024-0025-recursive-horizon.md)은 보존 참조32개를 연결한다. 새 원본7개(1,129,372bytes), 기존 보존25개 재사용이다. 원본 바이트를 바꾸지 않았고 코드·Markdown의 `.txt` 확장자는 자료임을 표시한다. [manifest](../evidence/0024-0025-horizon/manifest.json)와 [목록54행](../catalog/history-017-sources.jsonl)은 이32개, 원 H5 metadata1개, 미게시 체크포인트 metadata21개를 구분한다. 아래 원경로는 `Tab-ICL` 루트 기준이다.

| 출처 | 원본 경로 | 이번에 읽고 대조한 범위 |
|---|---|---|
| [SRC-0021163](../evidence/0024-0025-horizon/originals/SRC-0021163.md.txt) | `tmp/redesign_20260925/24_frozen_recursive_horizon_plan.md` | 계획 전체. 역사적 계획으로 읽고 현재 실행 지시로 사용하지 않음 |
| [SRC-0022867](../evidence/0024-0025-horizon/originals/SRC-0022867.py.txt) | `tmp/redesign_20260925/frozen_recursive_horizon_diagnostic.py` | 원 코드 전체 정적 열람;실행/import없음 |
| [SRC-0027709](../evidence/0024-0025-horizon/originals/SRC-0027709.npz) | `tmp/redesign_20260925/results/frozen_recursive_horizon/predictions.npz` | 전체 저장 배열의 형태·값 검산;모델 실행 없음 |
| [SRC-0027710](../evidence/0024-0025-horizon/originals/SRC-0027710.json) | `tmp/redesign_20260925/results/frozen_recursive_horizon/run_finished.json` | 완료 JSON 전문 |
| [SRC-0027711](../evidence/0024-0025-horizon/originals/SRC-0027711.json) | `tmp/redesign_20260925/results/frozen_recursive_horizon/run_started.json` | 시작 JSON 전문;과거 pid를 현재 실행으로 취급하지 않음 |
| [SRC-0027712](../evidence/0024-0025-horizon/originals/SRC-0027712.json) | `tmp/redesign_20260925/results/frozen_recursive_horizon/settings.json` | 전문 실제 출력·열람 |
| [SRC-0027713](../evidence/0024-0025-horizon/originals/SRC-0027713.json) | `tmp/redesign_20260925/results/frozen_recursive_horizon/summary.json` | 지정 필드 실제 열람;나머지 수치 행렬은 형태/집계 의미와 모든 값의 산술 대조. 모든 숫자의 수동 열람으로 세지 않음 |
| [SRC-0021188](../evidence/0024-0025-horizon/../0023-0025-pooling/originals/SRC-0021188.md.txt) | `tmp/redesign_20260925/25_pooling_and_horizon_findings.md` | H016 전체 열람 재사용;이번 주장은 §2 19–39행;§3문헌과후속전체연결대기 |
| [SRC-0030212](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030212.npz) | `tmp/redesign_20260925/results/rctl_pilot/empirical_risk_20260925_cluster0.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030215](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030215.npz) | `tmp/redesign_20260925/results/rctl_pilot/empirical_risk_20260925_cluster1.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030218](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030218.npz) | `tmp/redesign_20260925/results/rctl_pilot/empirical_risk_20260925_cluster2.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030221](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030221.npz) | `tmp/redesign_20260925/results/rctl_pilot/empirical_risk_20260925_cluster3.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030236](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030236.npz) | `tmp/redesign_20260925/results/rctl_pilot/evaluation_data.npz` | 기존 평가자료와 target/척도/시점 연결;peak_threshold재검수아님 |
| [SRC-0030238](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030238.json) | `tmp/redesign_20260925/results/rctl_pilot/frozen_settings.json` | 이전 전체 JSON 검수 재사용;이번 고정 소속과 기간 연결 |
| [SRC-0030239](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030239.npz) | `tmp/redesign_20260925/results/rctl_pilot/global_20260925_cluster0.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030242](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030242.npz) | `tmp/redesign_20260925/results/rctl_pilot/knn_risk_20260925_cluster0.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030245](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030245.npz) | `tmp/redesign_20260925/results/rctl_pilot/knn_risk_20260925_cluster1.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030248](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030248.npz) | `tmp/redesign_20260925/results/rctl_pilot/knn_risk_20260925_cluster2.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030251](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030251.npz) | `tmp/redesign_20260925/results/rctl_pilot/knn_risk_20260925_cluster3.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030254](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030254.npz) | `tmp/redesign_20260925/results/rctl_pilot/pcc_balanced_20260925_cluster0.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030257](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030257.npz) | `tmp/redesign_20260925/results/rctl_pilot/pcc_balanced_20260925_cluster1.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030260](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030260.npz) | `tmp/redesign_20260925/results/rctl_pilot/pcc_balanced_20260925_cluster2.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030263](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030263.npz) | `tmp/redesign_20260925/results/rctl_pilot/pcc_balanced_20260925_cluster3.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030266](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030266.npz) | `tmp/redesign_20260925/results/rctl_pilot/random_balanced_20260925_cluster0.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030269](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030269.npz) | `tmp/redesign_20260925/results/rctl_pilot/random_balanced_20260925_cluster1.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030272](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030272.npz) | `tmp/redesign_20260925/results/rctl_pilot/random_balanced_20260925_cluster2.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030275](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030275.npz) | `tmp/redesign_20260925/results/rctl_pilot/random_balanced_20260925_cluster3.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030281](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030281.npz) | `tmp/redesign_20260925/results/rctl_pilot/tabicl_risk_20260925_cluster0.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030284](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030284.npz) | `tmp/redesign_20260925/results/rctl_pilot/tabicl_risk_20260925_cluster1.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030287](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030287.npz) | `tmp/redesign_20260925/results/rctl_pilot/tabicl_risk_20260925_cluster2.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0030290](../evidence/0024-0025-horizon/../0003-0007/originals/SRC-0030290.npz) | `tmp/redesign_20260925/results/rctl_pilot/tabicl_risk_20260925_cluster3.npz` | 21개 기존 group 예측의 지정 배열;현재48origin의첫시점대조;다른배열은기존H001검수재사용 |
| [SRC-0023577](../evidence/0024-0025-horizon/../0001-0002/originals/SRC-0023577.npz) | `tmp/redesign_20260925/results/design_data.npz` | 초기 관측 이력과 고정 scale 연결;나머지 입력은 기존 H016 검수 재사용 |

새 텍스트 전문은24 계획33행과 코드142행의2개다. 시작·완료·settings JSON3개를 전문으로 읽었다. settings의20필드에는48origin과21checkpoint 해시가 포함된다. summary는9방법의24시점 scaled/raw 곡선·음수 개수·20comparisons 전체·21first-step 전체·나머지 상위 필드를 실제 출력해 읽었다. 큰 per-cell16×24 및 origin48×24 행렬은 구조·의미와 **모든 값의 저장 예측 산술 대조**를 수행했으며, 모든 숫자를 눈으로 열람한 JSON 전문으로 집계하지 않는다. 신규 NPZ1개와 이summary1개는 지정 필드 검수로 센다.

기존25의61행 전문 열람은 H016에서 재사용한다. 이번 주장은 §2의19–39행이며 §3 문헌은 후속 검수다. 기존21개 group NPZ에서는 `cell_ids`와`prediction`의 지정48origin 첫 시점만 이번에 대조했다. 나머지 배열의 기존 H001 검수를 새 검토량으로 더하지 않는다. 과거 코드 실행/import, 모델 추론·학습, 가중치 역직렬화는0회다.

## 대용량 H5와 미게시 체크포인트

원 H5 `SRC-0023485`는357,150,320bytes이며 SHA-256은 `4371f984d6ff235ce1760869eb8fe44e10b5b0214196158f8fb8dea8b324e65e`다. 전체 바이트 해시와 shape1488×10000×3, `idx[:]`, `data[:,16fixedcellIDs−1,2]`를 읽었다. [30개 확인과 날짜](../verification/history-017-H5-check.json), [앞 묶음의 입수·생성 안내](../evidence/0018-0021/README.md), manifest의 공식 위치·압축 member identity를 재사용한다. 전체 도시 모든 수치·다른 채널을 열람했다고 집계하지 않는다.

아래 `.pt`21개는 각각745,123bytes다. 로컬 원본의 바이트 SHA를 실제 읽어 settings와 대조했지만 Git에 파일을 게시하지 않았다. 팀 접근은 미확인이다. [과거 생성 코드](../evidence/0003-0007/originals/SRC-0023202.py.txt), [RCTL 구조](../evidence/0639/originals/SRC-0023048.py.txt), [고정 설정](../evidence/0003-0007/originals/SRC-0030238.json)은 앞 묶음에서 보존·검토한 자료를 연결한다. 지금 다시 학습하거나 같은 가중치의 재생성을 보장하는 지시가 아니다.

| 출처 | 체크포인트 파일 | SHA-256 |
|---|---|---|
| SRC-0030213 | `empirical_risk_20260925_cluster0.pt` | `95a274b8e4b7825756b5d9bb79ed6ed7d780db57d4a4993d4d3e54fe46b155b8` |
| SRC-0030216 | `empirical_risk_20260925_cluster1.pt` | `aec1ff6c877631699da297e766b46057322e98e32c9663f4a6c1918d4817a38a` |
| SRC-0030219 | `empirical_risk_20260925_cluster2.pt` | `a6f4418c7cf5ce97f4a6a9f1abfb9686d3134aa1f4785b1af7748fde006ac6da` |
| SRC-0030222 | `empirical_risk_20260925_cluster3.pt` | `d2b926912cfc95129d4c6d646fcaf581a07b47939d63136c6bc3d753e0caad28` |
| SRC-0030240 | `global_20260925_cluster0.pt` | `822808952e35b22921569f915db4b693f0929362e564ff4deae7cafbd6bc8476` |
| SRC-0030243 | `knn_risk_20260925_cluster0.pt` | `b587f2dc11da117bd07988dae0a164803433d3bc8a2935eebc86c2c2d01b8d8b` |
| SRC-0030246 | `knn_risk_20260925_cluster1.pt` | `5a8f5721e8554601b61c06be2cce043b702ac62bb6e89ca4244bf01abb7f0a6a` |
| SRC-0030249 | `knn_risk_20260925_cluster2.pt` | `8cc1bfa889056faaf2eafb45bab08ccc9cd8811bb4c6618984587bf2ce29457f` |
| SRC-0030252 | `knn_risk_20260925_cluster3.pt` | `a1b5269a0deb639279c2fb61fb0489582bec01c293c8a7443bc2172844143553` |
| SRC-0030255 | `pcc_balanced_20260925_cluster0.pt` | `1a4fde1b22a667f042d65d84fdab5831faf9545675b846fe579fa35951170b25` |
| SRC-0030258 | `pcc_balanced_20260925_cluster1.pt` | `f1a3e436ef959c3e241efe2af78d911eef8f2f4d926f2ee458932fd4a464f7de` |
| SRC-0030261 | `pcc_balanced_20260925_cluster2.pt` | `7f6ac992db0e4822147ff6696c6d155696c6ef01ecea13a5617f2f7b9d54ecd7` |
| SRC-0030264 | `pcc_balanced_20260925_cluster3.pt` | `978b17168e9bbf8a4855b04d93bd631ca29995f6d29618c47b39f408ab6439ec` |
| SRC-0030267 | `random_balanced_20260925_cluster0.pt` | `8c6ac3f12b1281d631002285b5ebdb0684e373b00b09c3629f77e31073980d8e` |
| SRC-0030270 | `random_balanced_20260925_cluster1.pt` | `29bca0346f52ddc064d10c5eb3b9b21646a8b801023f63c91a9ab3354700a70b` |
| SRC-0030273 | `random_balanced_20260925_cluster2.pt` | `734e7e3b6188e565b972e602faa6d41645b38bc4d774fac3a484c48e0808e1b6` |
| SRC-0030276 | `random_balanced_20260925_cluster3.pt` | `c5068eb7d7c86565b75a7be1311d80e22ba32542194a5a96c83e9d5cd622812d` |
| SRC-0030282 | `tabicl_risk_20260925_cluster0.pt` | `081bcc8b369f3f3cb275cfb839677c004be3e2b55837b2fddb921aecbba82e69` |
| SRC-0030285 | `tabicl_risk_20260925_cluster1.pt` | `ae92219d6aff933933f726d783275f136dd6e05eb0aaa329d1ccedc3426424c2` |
| SRC-0030288 | `tabicl_risk_20260925_cluster2.pt` | `c165bbe9b891a9b2ad9f77058f387b72d9cfd1bb11d35254a45ef05fe3023ff9` |
| SRC-0030291 | `tabicl_risk_20260925_cluster3.pt` | `29381448c41cb1f0ec0b111215817875b8586fba74ea2df365974ddc4cf5f7d7` |

체크포인트 파일의 미게시 상태를 저장 예측의 팀 접근성과 혼동하지 않는다. 팀은 Git에 보존한 예측·정답·설정으로 현재의 지표 검산을 실행할 수 있다. 원 모델 실행과 실제 recursive 중간 입력 재현에는 별도 자료가 필요하며 완료했다고 표시하지 않는다. [주장별 위치](../verification/history-017-primary-review.json)와 [검수 안내](../verification/history-017.md)에 한계를 연결했다.
