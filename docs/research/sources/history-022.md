# 33–35 출처와 실제 열람 범위

[기록](../records/0033-0035-process-fit-gap.md) · [전체 식별자 목록](../catalog/history-022-sources.jsonl) · [보존 manifest](../evidence/0033-0035-frozen-fit/manifest.json)

원본 경로는 기존 Tab-ICL 루트 기준이다. 새 사본 13개·기존 참조 7개, 일차문헌 관련 metadata 5개, 해시만 대조한 항목 31개로 총 56개 참조를 구분한다. 바이트 동일 사본의 별칭은 manifest에 보존한다. 파일 수는 연구 시도 수가 아니다.

## 보존 원문 20개

| 보존 링크 | 원 파일명 | 이번 읽기/대조 범위 |
| --- | --- | --- |
| [SRC-0021362](../evidence/0033-0035-frozen-fit/originals/SRC-0021362.md.txt) | 33_process_identification_source_plan.md | 33 전체 1–24행; 문헌 확인 계획 |
| [SRC-0021383](../evidence/0033-0035-frozen-fit/originals/SRC-0021383.md.txt) | 34_frozen_fit_gap_plan.md | 34 전체 1–32행; 고정 가중치 진단 계획 |
| [SRC-0021407](../evidence/0033-0035-frozen-fit/originals/SRC-0021407.md.txt) | 35_process_and_fit_gap_findings.md | 35 전체 1–83행; 결과·판단·보고한 실행 상태 |
| [SRC-0022700](../evidence/0033-0035-frozen-fit/../0642/originals/SRC-0022700.json) | cumulative_execution_budget.json | 기존 보존 재사용; 지정 초기 prefix 비용·중복 stage·이후 누적과 구분 |
| [SRC-0022772](../evidence/0033-0035-frozen-fit/originals/SRC-0022772.py.txt) | fetch_process_identification_33.py | 전체 1–35행 정적 독해; 실행·import 없음 |
| [SRC-0022860](../evidence/0033-0035-frozen-fit/originals/SRC-0022860.py.txt) | frozen_fit_gap_34.py | 전체 1–152행 정적 독해; 입력·지표·계산 step·저장 타이머 |
| [SRC-0023048](../evidence/0033-0035-frozen-fit/../0639/originals/SRC-0023048.py.txt) | rctl_torch.py | 기존 보존 재사용;56행 정적 재독·층별 크기 산술, import/실행 없음 |
| [SRC-0023577](../evidence/0033-0035-frozen-fit/../0001-0002/originals/SRC-0023577.npz) | design_data.npz | 기존 보존 재사용;16cell 선택·정답·시간·X shape 대조 |
| [SRC-0027513](../evidence/0033-0035-frozen-fit/originals/SRC-0027513.json) | partial.json | 선택 JSON; records와 summary 일치·RSS 차이 대조 |
| [SRC-0027514](../evidence/0033-0035-frozen-fit/originals/SRC-0027514.npz) | predictions.npz | 61배열의 shape/dtype/유한값과 저장 예측·정답 산술; 모델 재현 아님 |
| [SRC-0027515](../evidence/0033-0035-frozen-fit/originals/SRC-0027515.json) | run_started.json | 작은 JSON 전체; 시작 표식·settings hash |
| [SRC-0027516](../evidence/0033-0035-frozen-fit/originals/SRC-0027516.json) | settings.json | 작은 JSON 전체; 고정 설정·입력 해시 |
| [SRC-0027517](../evidence/0033-0035-frozen-fit/originals/SRC-0027517.json) | summary.json | 선택 JSON;29record/8집계·타이머/불변 플래그 독해, 모든 지표 산술; per-cell 숫자의 수동 전수 열람 아님 |
| [SRC-0023588](../evidence/0033-0035-frozen-fit/../0003-0007/originals/SRC-0023588.json) | observed_risk_pilot.json | 기존 보존 재사용;16cell 순서·소속 연결 |
| [SRC-0030237](../evidence/0033-0035-frozen-fit/../0003-0007/originals/SRC-0030237.json) | fit_results.json | 기존 보존 재사용;29fit 설정/epoch/MAE/시간/크기와 대조 |
| [SRC-0030238](../evidence/0033-0035-frozen-fit/../0003-0007/originals/SRC-0030238.json) | frozen_settings.json | 기존 보존 재사용;학습 설정과 model code hash |
| [SRC-0030280](../evidence/0033-0035-frozen-fit/../0003-0007/originals/SRC-0030280.json) | summary.json | 기존 보존 재사용;execution.wall과 fit 소타이머·누적 비용 |
| [SRC-0063641](../evidence/0033-0035-frozen-fit/originals/SRC-0063641.json) | manifest.json | 작은 JSON 전체; 다운로드 응답·시간·크기·해시 |
| [SRC-0063643](../evidence/0033-0035-frozen-fit/originals/SRC-0063643.json) | run_started.json | 작은 JSON 전체; 다운로드 시작 표식 |
| [SRC-0023213](../evidence/0033-0035-frozen-fit/originals/SRC-0023213.py.txt) | update_budget_after_frozen_gap_34.py | 전체 1–24행 정적 독해; 원장 갱신은 실행하지 않음 |

새 전체 텍스트 6개는 메모 3개와 정적 코드 3개다. 작은 JSON 전체 4개와 선택 수치 자료 3개를 구분한다. 재사용 7개는 신규 전체 읽기 수에 더하지 않는다. summary의 모든 numeric field 산술 확인을 JSON 모든 내용을 사람이 전수 읽은 것으로 집계하지 않는다. 원문 사본은 변경하지 않았다.

## 일차문헌과 그림

| ID | 정식 접근 링크 | bytes | SHA-256 |
| --- | --- | --- | --- |
| SRC-0063638 | [2606.01999v1.pdf](https://arxiv.org/pdf/2606.01999v1) | 2313347 | 9226e890eaf0c0306caec014475d6c123b4185d6727e08da42b26b453351a0c8 |
| SRC-0063640 | [abs.html](https://arxiv.org/abs/2606.01999v1) | 42481 | b244ecc20fd75254e71c0f5df6506bbb35f32ada4da6dac612646d1d7847d104 |
| SRC-0063642 | [page05.png](https://arxiv.org/pdf/2606.01999v1) | 476837 | 7276f6a5d92c84b131b3e99552a32810fcb313b20a8a50ba7bf286887f10620b |
| SRC-0063644 | [upc_page08.png](https://doi.org/10.1109/TNSM.2025.3599168) | 779310 | 9209161e5f8acfe8ad075ab838d59bb52626c6bd62a82a2fb30db242b02b7324 |
| SRC-0063645 | [upc_page09.png](https://doi.org/10.1109/TNSM.2025.3599168) | 757688 | 5a86ca6cbb9ae422ef7c5ec967cacba606a316ea0af5e890cad09248ea18761c |

Butera v1 텍스트는 PDF 1–8,13–14,19–22쪽(14쪽)을 읽었다. 시각 대조는 5·7·20·21쪽, 기존 page05.png도 직접 확인했다. §2 식1–2, §3 식3–7·Assumption3.1·Theorem3.2, §4 식8, Appendix B.1/E.2/F.1/F.2/G를 지정해 확인했다. 22쪽의 H는 시작 부분이며 H 전체 독해가 아니다. 저자 학습 코드와 나머지 페이지, HTML/txt 고유 내용 전체는 미검토다.

abs.html은 저장 120행과165–168행의 제출 이력만 읽었다. v1 2026-06-01 09:55:06 UTC이며 현재 최신 버전을 조회한 것은 아니다. 제출 이력의 1,367KB는 다운로드 PDF의 2,313,347 bytes와 같은 크기 항목으로 취급하지 않는다.

UPC의 별도 PDF 식별자는 EXT-P005-UPC, SHA-256 d8b720fe96f4d2da8ebcbe9dc779c0b4512dec0b2f4823295f908fcd639ae622, 7,721,301 bytes다. PDF8/9와 보존 PNG8/9를 시각 대조하고 Fig.7을 확대해 **1·2·4·6·8·12, 10 없음**을 확인했다. TableII의 ±0.348/±0.004는 99% CI이고 without UPC 대시는 결측 표기다. 그림의 모든 y값 추출이나 논문 전체 재현은 하지 않았다.

## 해시·크기만 확인한 31개

| ID | 원 파일명 | bytes | SHA-256 |
| --- | --- | --- | --- |
| SRC-0030213 | empirical_risk_20260925_cluster0.pt | 745123 | 95a274b8e4b7825756b5d9bb79ed6ed7d780db57d4a4993d4d3e54fe46b155b8 |
| SRC-0030216 | empirical_risk_20260925_cluster1.pt | 745123 | aec1ff6c877631699da297e766b46057322e98e32c9663f4a6c1918d4817a38a |
| SRC-0030219 | empirical_risk_20260925_cluster2.pt | 745123 | a6f4418c7cf5ce97f4a6a9f1abfb9686d3134aa1f4785b1af7748fde006ac6da |
| SRC-0030222 | empirical_risk_20260925_cluster3.pt | 745123 | d2b926912cfc95129d4c6d646fcaf581a07b47939d63136c6bc3d753e0caad28 |
| SRC-0030225 | empirical_risk_20260926_cluster0.pt | 745123 | 79e00ba093ec31f4d1bbe2916f4503409292a1d46428b2140ec787717f909d37 |
| SRC-0030228 | empirical_risk_20260926_cluster1.pt | 745123 | b4fbcfd4377394cad9f510750af89f609554c91ab39df823ca36e146f4dce986 |
| SRC-0030231 | empirical_risk_20260926_cluster2.pt | 745123 | 62116c4b607e2af512659338427461f39f09f2975c31c09323925f5ab0fac4d1 |
| SRC-0030234 | empirical_risk_20260926_cluster3.pt | 745123 | 130d1e5f32047c81dffc5e2c40ccd17e84b05b1ac21e436dbf665a1dd3a8b67b |
| SRC-0030240 | global_20260925_cluster0.pt | 745123 | 822808952e35b22921569f915db4b693f0929362e564ff4deae7cafbd6bc8476 |
| SRC-0030243 | knn_risk_20260925_cluster0.pt | 745123 | b587f2dc11da117bd07988dae0a164803433d3bc8a2935eebc86c2c2d01b8d8b |
| SRC-0030246 | knn_risk_20260925_cluster1.pt | 745123 | 5a8f5721e8554601b61c06be2cce043b702ac62bb6e89ca4244bf01abb7f0a6a |
| SRC-0030249 | knn_risk_20260925_cluster2.pt | 745123 | 8cc1bfa889056faaf2eafb45bab08ccc9cd8811bb4c6618984587bf2ce29457f |
| SRC-0030252 | knn_risk_20260925_cluster3.pt | 745123 | a1b5269a0deb639279c2fb61fb0489582bec01c293c8a7443bc2172844143553 |
| SRC-0030255 | pcc_balanced_20260925_cluster0.pt | 745123 | 1a4fde1b22a667f042d65d84fdab5831faf9545675b846fe579fa35951170b25 |
| SRC-0030258 | pcc_balanced_20260925_cluster1.pt | 745123 | f1a3e436ef959c3e241efe2af78d911eef8f2f4d926f2ee458932fd4a464f7de |
| SRC-0030261 | pcc_balanced_20260925_cluster2.pt | 745123 | 7f6ac992db0e4822147ff6696c6d155696c6ef01ecea13a5617f2f7b9d54ecd7 |
| SRC-0030264 | pcc_balanced_20260925_cluster3.pt | 745123 | 978b17168e9bbf8a4855b04d93bd631ca29995f6d29618c47b39f408ab6439ec |
| SRC-0030267 | random_balanced_20260925_cluster0.pt | 745123 | 8c6ac3f12b1281d631002285b5ebdb0684e373b00b09c3629f77e31073980d8e |
| SRC-0030270 | random_balanced_20260925_cluster1.pt | 745123 | 29bca0346f52ddc064d10c5eb3b9b21646a8b801023f63c91a9ab3354700a70b |
| SRC-0030273 | random_balanced_20260925_cluster2.pt | 745123 | 734e7e3b6188e565b972e602faa6d41645b38bc4d774fac3a484c48e0808e1b6 |
| SRC-0030276 | random_balanced_20260925_cluster3.pt | 745123 | c5068eb7d7c86565b75a7be1311d80e22ba32542194a5a96c83e9d5cd622812d |
| SRC-0030282 | tabicl_risk_20260925_cluster0.pt | 745123 | 081bcc8b369f3f3cb275cfb839677c004be3e2b55837b2fddb921aecbba82e69 |
| SRC-0030285 | tabicl_risk_20260925_cluster1.pt | 745123 | ae92219d6aff933933f726d783275f136dd6e05eb0aaa329d1ccedc3426424c2 |
| SRC-0030288 | tabicl_risk_20260925_cluster2.pt | 745123 | c165bbe9b891a9b2ad9f77058f387b72d9cfd1bb11d35254a45ef05fe3023ff9 |
| SRC-0030291 | tabicl_risk_20260925_cluster3.pt | 745123 | 29381448c41cb1f0ec0b111215817875b8586fba74ea2df365974ddc4cf5f7d7 |
| SRC-0030294 | tabicl_risk_20260926_cluster0.pt | 745123 | a24f2f383394d8c5fb32b9bd3e94165760b8d066bc5223d85bd37d40ca3abd92 |
| SRC-0030297 | tabicl_risk_20260926_cluster1.pt | 745123 | 540e5b5a4256e9fa1757b5f6724f35735e291ea4c945a586388ecc899db74571 |
| SRC-0030300 | tabicl_risk_20260926_cluster2.pt | 745123 | 583ffd07fc60aef204ff95c69401f224c120cec31736275fdb4ddc2e03b9aeba |
| SRC-0030303 | tabicl_risk_20260926_cluster3.pt | 745123 | 347b576cee4fc0f32ef801690a2811de9a6cce02711ab6e14a239032c7e0c3bf |
| SRC-0063637 | 2606.01999v1.html | 580955 | b012d55d1f9deb78c0419d06a22ee9aa8e184416a8c65fc33047ef7060183d6b |
| SRC-0063639 | 2606.01999v1.txt | 124333 | 0399d4b1dd33cb9e3435e90b3a83ec304a1aac58381e0bc61626b660148e6f73 |

29개의 .pt는 로컬 원본 바이트만 확인했으며 역직렬화·모델 초기화·forward는 하지 않았다. 가중치 팀 접근은 미완료다. 다른 두 파일 HTML/txt의 고유 본문은 이 표 등록만으로 읽기 완료 처리하지 않는다.

## 주장·검산·한계

[14개 주장 지도](../verification/history-022-primary-review.json)는 과거 보고와 현재 저장 산술·정적 계산·일차문헌 대조를 구분한다. [검수 설명](../verification/history-022.md)과 [자료 재사용](../evidence/0033-0035-frozen-fit/README.md)을 함께 읽는다. 33/34 계획을 현재 실행 명령으로 사용하지 않는다.
