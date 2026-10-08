# 네트워크·시계열 선행 9편과 초기 설계의 적용 범위

05는 선행의 결과를 그대로 재현했다고 보고하지 않고, 입력 정보와 비교군을 결정하는 근거로 사용했다. 아래는 그 아홉 항목을 **해당 판본의 지정 구간**에 대조한 결과다. 논문 전체·저자 코드·새 실험을 검증한 목록은 아니다. [05 기록](../records/0005-network-timeseries-audit.md), [읽은 구간과 미검토 범위](../sources/history-004.md), [주장별 검토 장부](../verification/history-004-primary-review.json)

| 문헌 | 예측 대상·방법 | 초기 실험으로 옮길 때 구분할 점 |
|---|---|---|
| [UPC / Urban Mobile Data Prediction](https://doi.org/10.1109/TNSM.2025.3599168) | 도시 mobile activity, weekday peak group와 파형 PCC, 후속 예측기 | raw cell PCC balanced와 원 UPC는 다름 |
| [TabPFN-ST-AR](https://doi.org/10.1145/3768740.3768798) | METR-LA 도로 속도, 시간·공간 34특징 | 우리 lag24/168은 자체 설계 선택; 이웃 정보 부재 |
| [TabPFN-TS, v4](https://arxiv.org/html/2501.02945v4) | 시간·달력·주기 특징의 비자기회귀 다단계 예측 | 미래 lag 부재와 관측된 one-step lag는 다름 |
| [ISP TTM, v2](https://arxiv.org/html/2511.17529v2) | CESNET 계층별 단변량 bytes, TTM-R2 | 연속 시간 표본 수와 Tab context 행 수는 다른 단위 |
| [MobiGPT, v1](https://arxiv.org/html/2509.18166v1) | 환경 조건을 이용하는 diffusion Transformer | 자연어 GPT나 TabICL 회귀와 다름; 실행 자산 미확인 |
| [CoT mobile traffic, v1](https://arxiv.org/html/2605.09260v1) | 5G 다음 초 downlink throughput, 자연어 LLM ICL | grid activity와 다름; 분할 설명의 모호함을 남김 |
| [Multivariate TabPFN, v1](https://arxiv.org/html/2604.08400v1) | 채널별 정규화 후 시간·채널 표시를 가진 행 결합 | 행을 합쳤다는 사실만으로 공간 관계를 제공하지 않음 |
| [Traffic Matrix clustering, v1](https://arxiv.org/html/2604.26081v1) | Abilene/GÉANT OD flow의 그룹별 GRU | random/global 비교 근거이지만 방법별 K와 과제가 다름 |
| [Locality and Globality](https://doi.org/10.1016/j.ijforecast.2021.03.004) | local/global 함수 관계와 일반화·분할 복잡도 | 전체 이력의 존재 결과는 고정 길이 RCTL의 성능 보장이 아님 |

## UPC: 비교군의 이름과 실제 구현

*Urban Mobile Data Prediction With Geospatial Clustering and Dual Residual Learning*의 UPC는 weekday별 peak hour의 최빈값으로 cell을 먼저 묶고, 그 peak group의 평균 트래픽 파형 간 PCC로 seed와 소속을 정한다. 피크 한 시점의 값만 비교하는 방법이 아니다. 여기서는 앞서 확인한 PDF1·4·5쪽 텍스트와4·5쪽 시각 검토를 재사용했다. [기존 UPC 검토](../verification/pilot-005-document-review.json)

원문의 θ=10 조건은 seed 후보에 대해 `|G| > 10`이다. K4의 서로 다른 유효 seed 그룹에는 최소44cell이 필요하지만, 그 수만으로 peak group과 PCC 조건이 충족되지는 않는다. **16cell 초기 pilot의 `pcc_balanced`를 원 UPC라고 부를 수 없다.** 그 코드는 첫672시간의 개별 cell 원파형 상관으로 균형 병합한다. 이후 연구의 UPC 조건·규모 문제는 [642](../records/0642-research-direction.md)와 연결하며, 이번 검토를 역사기록166 전체의 완료로 세지 않는다. [원 논문](https://doi.org/10.1109/TNSM.2025.3599168), [초기 코드86–110행](../evidence/0003-0007/originals/SRC-0023116.py.txt)

## TabPFN-ST-AR: 공간 특징과 일·주간 lag의 출처

Li 외의 *Architectural Bias vs. Feature Engineering: Deconstructing the Limits of Tabular Foundation Models in Traffic Forecasting*는 SMBD2025의 METR-LA 도로 속도 예측이다. 207개 sensor의5분 자료를 시간순70/10/20으로 나누고 train 통계로 z-score한다. 과거12step으로 이후12step을 예측하며3/6/12step, 즉15/30/60분을 평가한다. [논문§3](https://doi.org/10.1145/3768740.3768798)

Table1의34특징은 자기 lag12, 달력 sin/cos4, 1-hop 이웃 평균의 이력12, 공간 시퀀스의 평균·표준편차·최소·최대4, 정규화 in/out degree2다. §3.4의 예측별 무작위 train1024행 context는 해당 TabPFN 설정이며 현재 TabICLv2의 보편적 한계로 옮기지 않는다. §4.1은 A100과 test10,000개를 적는다. 전체 성능표·checkpoint·저자 코드는 이번에 검증하지 않았다.

초기 Milan 구현의16특징은 자기 최근8시간,24/168시간 lag, 직전24시간 평균·표준편차, 시간/요일 sin/cos4다. **일·주간 lag는 이 논문의 특징을 그대로 옮긴 것이 아니라05가 택한 설계다.** 현재 입력에는 도로 이웃 평균·degree·RSRP·handover가 없다. 공간 특징의 효과를 Milan의 실증 결과로 쓰지 않는다. ACM 페이지 접근은403이어서 보관 PDF의 물리3·4쪽과 지정 txt를 확인했다. [초기 특징 코드1–37행](../evidence/0001-0002/originals/SRC-0022703.py.txt)

## TabPFN-TS: 미래를 한 번에 예측하는 표 구성

Hoo 외의 *From Tables to Time: Extending TabPFN-v2 to Time Series Forecasting*는 arXiv2501.02945v4(2026-01-26)를 기준으로 읽었다. §3은 running index, 달력 주기, 연도, 자동 추출 주기와 알려진 미래 공변량으로 전체 horizon을 비자기회귀 예측한다. 미래 구간의 lag·이동평균을 만들려면 이전 예측이 필요하므로 이 설계에서는 사용하지 않는다. §3.2는 제곱손실에는 평균, 절대손실에는 중앙값을 구분한다. [해당 판본§3](https://arxiv.org/html/2501.02945v4)

따라서 이 논문을 ‘lag를 추천한 근거’로 쓰지 않으며, 실제 관측 lag를 사용할 수 있는 다음1시간 문제를 금지한 결과로도 읽지 않는다. §5.1/§6.1의 특정 선형·지수 추세 외삽 한계는 모든 TabICLv2 예측의 수학적 불가능성 증명이 아니다. §6.2의 하드웨어 보정 GPU 비용 비교도 초기 CPU 실행 측정과 구분한다. 전체 benchmark 표·추세 그림·appendix·코드 재현은 미검토다.

## ISP TTM: 관측 단위·시간 길이·전처리 범위

Liu·Farkiani·Crowley의 *Time-Series Foundation Models for ISP Traffic Forecasting*는 arXiv2511.17529v2(2026-02-17)다. §III는 CESNET-TimeSeries24의 약40주 조직·서브넷·IP 자료에서 각 entity를 단변량으로 다루며 대표 target을 `n_bytes`로 둔다. 10분 자료와 집계한 시간 단위를 구분하고, 시간순45/25/30 분할 내에 context+horizon 창을 만들 수 없는 series를 제외한다. stride1의 겹친 창에서 지표를 계산해 series 내 평균을 낸다. [논문§III](https://arxiv.org/html/2511.17529v2)

series별 minmax와 결측0 처리가 적혀 있으나, 읽은§III.C에는 **minmax 통계를 어느 구간에 맞췄는지 명시돼 있지 않다.** train-only라고 보충하지 않는다. TTM의 L=512/1024/1536은 연속 관측 수다. lag와 target을 가진 Tab context 표 행 수와 같은 단위가 아니다.

TTM-R2 zero-shot은 가중치를 고정하고, few-shot은 backbone을 고정한 prefix/head 조정과 train window10/30/50%를 사용한다. CPU M2 Pro16GB, seed42, 최대10epoch 등의 설정이 있다. §IV.D/§V의 작은 tuning 이득은 해당 자료·설정의 보고이며 모든 회귀 TFM의 우열이 아니다. §IV.G의 희소 IP·cross-metric 미검증·native ICL 부재와 함께 읽는다. 전체 결과표나 실행 비용을 독립 재현하지 않았다.

## MobiGPT: 환경 조건을 이용한 diffusion 모델

Qi·Chai·Li의 *MobiGPT: A Foundation Model for Mobile Wireless Networks*는 arXiv2509.18166v1(2025-09-17)이다. §3.2/§4의 모델은 temporal convolution으로 token을 만들고, task mask·학습된 soft prompt·VAE 환경 표현을 사용하는 **조건부 diffusion Transformer**다. 자연어 GPT에 숫자 prompt를 넣는 방식이나 TabICL 회귀와 같지 않다. [논문§3–4](https://arxiv.org/html/2509.18166v1)

환경 정보는 BS의 도시 knowledge graph, 앱의 사용자 profile, RSRP의 안테나·송신전력·거리·지형 등이다. §5.1은 네 도시의 BS traffic, 앱 사용량, RSRP를 길이64 sample로 구성한다. §5.3은 학습에 없던 Shandong cell 자료에 직접 적용하거나 새 자료2/5%로 조정한다. 이런 전이와 같은 Milan의 cell 소속 결정은 과제가 다르다.

05의 ‘가능하면 비교’는 실행 완료가 아니다. 공개 checkpoint·자료·코드의 현재 접근성과 정확한 train/test 구성은 이번 지정 절 검토만으로 확인하지 않았다. 첫 페이지의 Received2019/Revised2020 형식 문구도 arXiv 등록일이나 확정 학술지 발행일로 사용하지 않는다.

## CoT mobile: 관측 정보와 train/test 서술의 공백

Ghadaksaz 외의 *Chain-of-Thought Reasoning Enhances In-Context Learning for LLM-Based Mobile Traffic Prediction*는 arXiv2605.09260v1(2026-05-10)이다. 대상은 실제5G의 다음1초 downlink throughput이다. §IV는 static/driving의 다운로드·Amazon Prime 환경, uplink·serving/neighbor RSRP·network mode·handover의5개 공변량, W=5초/S=1, 주 모델 o4-mini와5회 평균을 적는다. [논문§II–IV](https://arxiv.org/html/2605.09260v1)

offline의 lecture→plan→rationale 생성은 훈련 example의 정답도 사용한다. online 검색 식17–20은 **throughput 원시 창과1차 차분의 Euclidean 거리 합**으로 M개 예시를 고른다. 공변량은 prompt에 있지만 그 검색 거리의 직접 항은 아니다. 자연어 rationale와 검색 정보 범위를 분리한다.

분할 설명에는 ‘동일하게 나눈다’는 문장과 ‘각 test trace의 첫200초를 평가하고 나머지를 훈련에 쓴다’는 문장이 함께 있고, train 길이는664/1569/588초로 적혀 있다. PDF 물리7쪽과 공식 HTML에서도 같은 서술을 확인했다. **정확한 trace 관계와 시간 방향을 코드로 복원하기 전에는 forward train→test라고 확정할 수 없다.** 이 공백만으로 정보 유출을 확정한 것도 아니다. 전체 성능표·그림·비율은 이번 검산 대상이 아니다.

05에는 없는 RSRP·handover를 만들어 넣지 않았다. 알려진 공변량의 역할을 비교할 수는 있지만, Milan grid activity와 throughput을 같은 target으로 보거나 숫자 TabICL에 CoT 모듈을 적용한 실험으로 집계하지 않는다.

## Multivariate TabPFN: 채널을 합치는 방식도 명시한다

Jayawardhana 외의 *Zero-shot Multivariate Time Series Forecasting Using Tabular Prior Fitted Networks*는 arXiv2604.08400v1(2026-04-09)이다. §2.2는 채널별 z-score 후 time feature와 categorical channel indicator를 가진 행으로 시계열을 결합하고 scalar target을 예측해 각 채널 척도로 복원한다. 같은 시간 길이에도 채널 d개를 넣으면 context 행이 d배가 된다. [논문§2.2](https://arxiv.org/html/2604.08400v1)

채널 공통 context와 분리 예측의 비교에서 일부 자료는 분리 쪽이 낫고, §4는 보정·계산량의 한계를 남긴다. AppendixB는 고정 열 순서와 별도 순서 ablation이 없음을 설명한다. backend ensemble 설명을 모든 열 순열의 불변성 실증으로 바꾸지 않는다.

cell을 한 context에 넣기만 하면 지리적 관계나 올바른 공동분포가 자동 제공된다고 주장할 근거는 아니다. 05가 확인하려는 것은 시간·채널·이웃 정보가 실제 행과 열에 어떻게 들어갔는가다. 저자 코드·joint sampling 구현·전체 appendix 결과 재현은 미확인이다.

## Traffic Matrix clustering: 같은 K 비교와 논문 표를 구분한다

Cash·Fowler·Wyglinski의 *On the Role of Time Series Clustering in Traffic Matrix Prediction*는 arXiv2604.26081v1(2026-04-28)이다. Abilene12node/144 OD flow의5분 자료와 GÉANT23node/529flow의15분 자료를 사용한다. 과거 행렬10개로 다음 행렬을 예측하고80/20 train/test와 train 내10% validation을 둔다. 그룹별 다변량 출력 GRU는 우리 cell 행 결합 RCTL과 동일한 학습 문제는 아니다. [논문§III–V](https://arxiv.org/html/2604.26081v1)

histogram50bin은 JSD/complete linkage, ACF와 Welch PSD는 Euclidean/average linkage를 쓴다. naive random도 비교한다. **TablesI/II의 성능 비교는 방법별 선택 K가 다르다.** NMI/ARI 소속 구조를 비교할 때의 K=21/40 고정과 혼동하지 않는다. 아래는 보관 PDF 물리6·8·9쪽에서 확인한 **논문 보고값**이며 원출력·저자 코드의 재현 결과가 아니다.

| 자료 | histogram K | ACF K | PSD K | naive K |
|---|---:|---:|---:|---:|
| Abilene | 21 | 21 | 41 | 21 |
| GÉANT | 40 | 100 | 100 | 50 |

| 자료 / TableII RMSE(Mbps) | histogram | ACF | PSD | naive | Prophet | ARCNN | EM | local |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Abilene | 0.640 | 0.755 | 0.597 | 0.688 | 3.350 | 2.500 | 1.280 | 0.189 |
| GÉANT | 0.014 | 0.027 | 0.014 | 0.014 | 0.067 | 0.041 | 0.040 | 0.003 |

| TableV naive 그룹 크기 | K | 최소 | 최대 | 평균 |
|---|---:|---:|---:|---:|
| Abilene | 21 | 6 | 7 | 6.86 |
| GÉANT | 50 | 10 | 11 | 10.58 |

읽은 본문에는 random seed와 균형 제약의 세부 절차가 충분히 적혀 있지 않지만, TableV의 실제 크기는 위처럼 균형적이다. ‘절차를 미확인했다’와 ‘논문의 random은 불균형했다’를 혼동하지 않는다. 05는 여기서 **같은 K의 balanced random과 global RCTL을 함께 보자**는 자체 비교 원칙을 택했다. 논문의 전체 성능표가 이미 같은 K·같은 정보 비교라는 뜻은 아니다.

§VII–VIII는 분할 자체의 효과를 해석하면서 작은 K에서는 표현 차이가 중요할 수 있음을 남긴다. TableII의 local이 더 낮다는 결과도 함께 보존한다. 이것으로 random이 Milan/RCTL에서 항상 충분하거나 clustering이 항상 필요하다고 결론내리지 않는다. 초기 실험에서는 오히려 global이 모든 K4 대조보다 낮았다. [우리 저장 결과와 조건](../records/0005-network-timeseries-audit.md)

## Locality and Globality: 함수의 존재와 실제 학습

Montero-Manso·Hyndman2021의 정확한 제목은 *Principles and Algorithms for Forecasting Groups of Time Series: Locality and Globality*다. 05의 *Global and local forecasting models: properties and comparative performance*는 보관 원문·저자 공식 서지와 다르므로 정리본에서 바로잡는다. IJF37(4),1632–1653의 DOI와 로컬 arXiv2008.00444v3를 연결하되 출판 PDF와 전체 바이트가 같다고 확인한 것은 아니다. [저자 서지](https://robjhyndman.com/publications/global-forecasting/), [DOI](https://doi.org/10.1016/j.ijforecast.2021.03.004)

Proposition1은 유한한 관측 series 집합의 **전체 이력**을 입력으로 local algorithm의 출력을 표현하는 global 함수의 존재 결과다. 같은 전체 입력이면 local algorithm도 같은 출력을 낸다는 설정이다. 임의 회귀 입력의 서로 다른 정답을 유한 모델이 모두 맞춘다는 보장이 아니다. §2.2는 최근 M개로 기억을 제한하면 같은 최근 이력·다른 과거를 가진 series를 구별하지 못해 같은 등가성을 보장하지 못한다고 명시한다.

§3.2는 좋은 generalization bound가 실제 오차 우위를 보장하지 않는다고 설명한다. §3.3의 유한 가설군·독립 series·같은 유효 표본 수·유계 손실 조건, §3.6의 자료를 보기 전 고정 분할과 자료로 고른 분할의 복잡도 차이도 구분한다. 동시 network cell이나8시간 입력의 RCTL에 자동 적용하지 않는다. 서로 다르다는 이유만으로 pooling 손해를 확정하지 않는 것과, global이 항상 낫다고 말하는 것은 별개다. 전체 증명·경험 표·저자 코드 재현은 미검토다.
