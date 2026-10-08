# 05 네트워크·시계열 비교의 출처와 검토 범위

이 묶음은05의 네트워크·시계열9항목만 통합한다. 새로 대조한8편의 로컬 자료11개는 지정 구간만 읽었고 UPC는 기존 검토를 재사용했다. 전체 논문 검토 완료는0편이다. 파일 확보·서지 확인·지정 구간 검토·원실험 재현을 구분한다.

[기록](../records/0005-network-timeseries-audit.md), [문헌 비교](../references/network-timeseries.md), [manifest](../evidence/0005-network/manifest.json), [기계 판독 목록](../catalog/history-004-sources.jsonl), [일차문헌 검토 장부](../verification/history-004-primary-review.json)

## 이미 보존한 원문9개

원본 루트의 경로·SHA-256·크기·동일 해시 사본 ID는 manifest에 있다. 아래 파일은 원바이트 그대로 재사용했으며 신규 사본 수·고유 검토량에 더하지 않았다. 05만 전체69행이고 코드와 JSON은 이번에 다시 확인한 구간을 적었다. 초기 코드·결과의 이전 전체 검토는 [초기 출처](pilot-006.md)와 [B1/B2 출처](history-001.md)에 있다.

| source_id | 보존 파일 | 이번 확인 범위 |
|---|---|---|
| SRC-0020826 | [05_literature_decision_audit.md](../evidence/0005/originals/SRC-0020826.md.txt) | 행 1–69 |
| SRC-0022703 | [data_and_smoke.py](../evidence/0001-0002/originals/SRC-0022703.py.txt) | 행 1–37 |
| SRC-0023116 | [risk_table_pilot.py](../evidence/0003-0007/originals/SRC-0023116.py.txt) | 행 1–24, 86–110 |
| SRC-0022942 | [observed_risk_pilot.py](../evidence/0003-0007/originals/SRC-0022942.py.txt) | 행 1–20, 61–90 |
| SRC-0023202 | [train_rctl_pilot.py](../evidence/0003-0007/originals/SRC-0023202.py.txt) | 행 14–70 |
| SRC-0023604 | [risk_table_pilot.json](../evidence/0003-0007/originals/SRC-0023604.json) | `partitions.pcc_balanced`; `partitions.random_balanced`; `partitions.cross_error_profile` |
| SRC-0023588 | [observed_risk_pilot.json](../evidence/0003-0007/originals/SRC-0023588.json) | `partitions` |
| SRC-0030238 | [frozen_settings.json](../evidence/0003-0007/originals/SRC-0030238.json) | `tasks` |
| SRC-0030280 | [summary.json](../evidence/0003-0007/originals/SRC-0030280.json) | `metrics.method`; `metrics.seed`; `metrics.models`; `metrics.mean_scaled_mae` |

JSON의 partitions/task/metrics 일부를 확인한 것을 파일 전체의 새 검토로 세지 않는다. 저장 label B1→B2 일치·다섯4×4 소속·29task·8개 MAE 연결은 [110항목 체크포인트](../verification/history-004-implementation-check.json)에 있다. 원예측 배열 계산은 [history-001 검산](../verification/history-001-risk-check.json)을 재사용했다. 새 모델과 새 난수는 실행하지 않았다.

## 일차자료11개: 판본·파일·읽은 구간

줄 번호는 보관 UTF-8 txt를 Python `splitlines()`로 나눈1기준이다. 제어문자 때문에 다른 줄 세기와 다를 수 있다. PDF 번호는 인쇄면 번호와 별개의 물리 페이지1기준이다. 제목·공식 서지 확인은 각 논문의 본문 전체 검토를 뜻하지 않는다. 파일명만 찾은 다른 사본은 읽음으로 표시하지 않았다.

| reference / source_id | 판본과 공식 접근 | 실제 읽은 구간 |
|---|---|---|
| H004-P02 / SRC-0064566 | [Architectural Bias vs. Feature Engineering: Deconstructing the Limits of Tabular Foundation Models in Traffic Forecasting](https://doi.org/10.1145/3768740.3768798); SMBD 2025, 2025-08-28–30, 12쪽 | txt 행 1–150, 195–388, 416–447, 524–554 |
| H004-P02 / SRC-0000081 | [Architectural Bias vs. Feature Engineering: Deconstructing the Limits of Tabular Foundation Models in Traffic Forecasting](https://doi.org/10.1145/3768740.3768798); SMBD 2025, 2025-08-28–30, 12쪽 | PDF 시각 3, 4쪽 |
| H004-P03 / SRC-0020699 | [From Tables to Time: Extending TabPFN-v2 to Time Series Forecasting](https://arxiv.org/html/2501.02945v4); arXiv 2501.02945v4, 2026-01-26 | txt 행 1–58, 120–258, 590–609, 797–855 |
| H004-P09 / SRC-0020783 | [Principles and Algorithms for Forecasting Groups of Time Series: Locality and Globality](https://doi.org/10.1016/j.ijforecast.2021.03.004); 보관 arXiv 2008.00444v3, 표지2021-03-30; 출판 서지 IJF37(4),1632–1653 | txt 행 1–56, 156–237, 306–434, 500–532 |
| H004-P04 / SRC-0020687 | [Time-Series Foundation Models for ISP Traffic Forecasting](https://arxiv.org/html/2511.17529v2); arXiv 2511.17529v2, 2026-02-17 | txt 행 1–32, 271–473, 613–738 |
| H004-P05 / SRC-0020690 | [MobiGPT: A Foundation Model for Mobile Wireless Networks](https://arxiv.org/html/2509.18166v1); arXiv 2509.18166v1, 2025-09-17 | txt 행 1–44, 363–631, 648–714, 772–814, 970–1025 |
| H004-P06 / SRC-0020693 | [Chain-of-Thought Reasoning Enhances In-Context Learning for LLM-Based Mobile Traffic Prediction](https://arxiv.org/html/2605.09260v1); arXiv 2605.09260v1, 2026-05-10 | txt 행 1–42, 280–370, 614–1083, 1082–1110 |
| H004-P06 / SRC-0020692 | [Chain-of-Thought Reasoning Enhances In-Context Learning for LLM-Based Mobile Traffic Prediction](https://arxiv.org/pdf/2605.09260v1); arXiv 2605.09260v1, 2026-05-10 | PDF 7쪽: §IV 분할·설정 문단. Figure3 수치 미검산 |
| H004-P07 / SRC-0020696 | [Zero-shot Multivariate Time Series Forecasting Using Tabular Prior Fitted Networks](https://arxiv.org/html/2604.08400v1); arXiv 2604.08400v1, 2026-04-09 | txt 행 1–190, 258–278 |
| H004-P08 / SRC-0062987 | [On the Role of Time Series Clustering in Traffic Matrix Prediction](https://arxiv.org/html/2604.26081v1); arXiv 2604.26081v1, 2026-04-28 | txt 행 1–36, 224–355, 391–751, 890–950, 1120–1270 |
| H004-P08 / SRC-0062986 | [On the Role of Time Series Clustering in Traffic Matrix Prediction](https://arxiv.org/pdf/2604.26081v1); arXiv 2604.26081v1, 2026-04-28 | PDF 6쪽: TableI·GRU/ACF/PSD 설정; PDF 8쪽: TablesII/III 및 고정 K 구조 비교. Figure4 수치화 제외; PDF 9쪽: TablesIV/V와 해석 |

H004-P01 UPC는 `EXT-P005-UPC`이며 Tab-ICL 조사 루트 밖의 기존 논문이다. [DOI](https://doi.org/10.1109/TNSM.2025.3599168), SHA-256 `d8b720fe96f4d2da8ebcbe9dc779c0b4512dec0b2f4823295f908fcd639ae622`,7,721,301bytes. 앞서 읽은 PDF1·4·5쪽 텍스트와4·5쪽 시각 검토를 [pilot-005의 UPC_paper 항목](../verification/pilot-005-document-review.json)에 연결했다. 이번의 새 전논문 검토나166 전체 통합으로 집계하지 않는다.

## 추가 접근과 남긴 공백

- TabPFN-ST-AR의 공식 ACM 페이지는403이어서 보관 txt/PDF를 이용했다. PDF3·4쪽의 Figure1/Table1/§3.2–3.5를 확인했으며 성능 Table3 전체 검증은 아니다.
- arXiv의 지정 판본 서지는 공식 페이지와 대조했다. CoT mobile의 제어문자·수식·분할 문장은 공식 HTML§III.B 식16–20/§IV 및 보관 PDF7쪽으로 보완했다. Figure3의 수치를 추출하지 않았다.
- Traffic Matrix PDF6·8·9쪽의 TablesI/II/V를 시각적으로 대조했다. TablesIII/IV와 주변 문맥도 읽었지만 raw 재현은 아니고 Figure4의 곡선은 수치화하지 않았다.
- Global/local의 제목·DOI·권호는 [저자 공식 페이지](https://robjhyndman.com/publications/global-forecasting/)와 대조했다. 보관 arXiv v3와 출판 PDF 전체의 동일성을 검증하지 않았다.
- 논문 전문·원저자 코드·checkpoint·모든 실험·증명을 이 묶음에서 확보하거나 재현했다고 표시하지 않는다. 각 파일의 남은 절·그림·부록은 검토 장부 `read_scope.unreviewed`에 있다.
- 05의 공식 TabICL/분위수/forecast pipeline, 회귀 TabPFN과 관련 여섯 연구의 근거 연결은 후속 묶음이다. 파일의 발견·이름 일치만으로 이 범위를 완료 처리하지 않는다.

외부 자료는 metadata와 공식 링크로 접근하게 하고 논문 전문을 이 저장소에 새로 복사하지 않았다. 원문9개는 기존 보존본과 현재 원본 바이트를 대조했다. 역사적 실행 지시는 자료로만 읽었다.
