# 05 — 네트워크·시계열 선행과 실제 초기 입력·대조군

05의 네트워크·시계열 문헌9개는 **무슨 정보를 입력하고 어떤 비교를 해야 하는가**를 정하는 근거였다. 문헌의 방법·target·분할·K를 확인한 뒤, 초기 B1/B2의 코드와 저장 소속·RCTL 결과에 연결했다. 같은 이름의 실험을 반복하기 전에 이 차이와 기존 결과를 확인할 수 있도록 정리한다.

[05 보존 원문](../evidence/0005/originals/SRC-0020826.md.txt), [아홉 문헌 비교](../references/network-timeseries.md), [출처와 읽은 구간](../sources/history-004.md), [검수](../verification/history-004.md). 05의 [가까운 다섯 방법](0005-closest-methods-audit.md)은 앞 묶음, [공식 코드·초기 호출](0005-official-tabicl-audit.md)은 다음 부분 기록에 정리했다. 관련 여섯 연구와 회귀 TabPFN의 후속 비교가 남아 있으므로 **05 전체 완료가 아니다.**

| 항목 | 기록한 범위 |
|---|---|
| 역사적 시점 | 05의 검색·확인일2026-09-25. 추천안 확정 전 근거 기록 |
| 연구 질문 | 다른 network/time-series 연구에서 쓰는 정보와 비교 원칙을 현재 cell 소속 문제에 어떻게 적용할 것인가 |
| 당시 결정 | 실제 관측 lag·달력을 비교군에 동일 제공, 없는 공변량을 만들지 않음, balanced random/global 포함, 원 UPC와 작은 PCC 대조 구분 |
| 수행 상태 | 문헌·설계 기록. 후속 실행 여부는 B1/B2 결과에서 따로 확인. 이번 정리의 새 학습·추론·난수 실험0 |
| 주요 확인 | 로컬 일차자료11개에서8편의 지정 구간 확인, UPC는 기존 검토 재사용. 원문9개는 기존 보존본 재사용 |
| 비용 | 05 문헌 검토의 당시 시간·메모리는 미기록. 실제 초기 모델 비용은 B1/B2 기록에 별도 보존 |
| 남은 범위 | 관련 여섯 연구·회귀 TabPFN의 후속 비교, 각 논문의 미열람 구간·저자 코드·전체 재현 |

## 논문에서 가져온 원칙과 구현된 입력

TabPFN-ST-AR는 도로 속도와 시간·공간34특징을 사용한다. 초기 실험의 일·주간 lag를 직접 추천한 논문으로 요약하면 안 된다. TabPFN-TS는 미래 lag 없이 여러 horizon을 한 번에 예측한다. 현재의 다음1시간에는 관측된 과거값을 사용할 수 있다는 점이 다르다. CoT mobile의 throughput·RSRP·handover나 MobiGPT의 환경 정보를 Milan에 이미 보유한 것으로 가정하지 않았다. [판본·절별 차이](../references/network-timeseries.md)

| 실제 초기 조건 | 확인한 구현과 기존 결과 |
|---|---|
| target | Milan의 시간별 internet activity. 5G throughput/도로 속도/OD flow와 다름 |
| 정규화 | cell별 원시점0–671의 평균으로 나눔 |
| 표 입력16개 | 자기 최근8시간 + lag24/168 + 직전24시간 평균·표준편차 + 시간/요일 sin/cos4 |
| 포함하지 않은 입력 | 도로 이웃 평균·in/out degree·RSRP·handover·cell ID |
| Tab context/query |16cell 각각 target168–671의504행, 소속 결정 query672–839의168행 |
| RCTL 입력 | 최근8시간×9채널. 최근값 이외의8개 보조 특징을 매 step에 반복 |
| RCTL 기간 | train168–839, validation840–1007, 평가1008–1487의480시점 |

이 표는 당시 저장 구현·자료 연결이다. 논문이 모두 이16특징을 권고했다는 뜻은 아니다. [특징 생성1–37행](../evidence/0001-0002/originals/SRC-0022703.py.txt), [RCTL 설정·입력14–70행](../evidence/0003-0007/originals/SRC-0023202.py.txt), [기존 입력·H5 검수와 B2 조건](0004-0007-b2-observed-risk.md)

## 무작위 분할과 global은 실제로 비교했다

B1의 `risk_table_pilot.py`는 seed20260925의 permutation에 각4개씩 반복한 label을 배정한다. 저장된 `random_balanced`는16cell을4개씩 나눈 네 그룹이다. `pcc_balanced`는 원시점0–671의 **개별 cell 파형**으로 상관을 구해 균형 병합했다. weekday peak group의 평균 파형으로 seed를 고르는 UPC와 다르다. [B1 코드86–110행](../evidence/0003-0007/originals/SRC-0023116.py.txt), [저장 소속](../evidence/0003-0007/originals/SRC-0023604.json)

B2는 PCC/random/cross-error profile의 세 소속을 이전 JSON에서 복사했다. 세 label 배열이 B1/B2에서 같은지 확인했고, RCTL에 사용한 Tab/empirical/KNN/PCC/random 다섯 소속은 모두4×4다. RCTL의 frozen task29개도 해당 소속과 맞는다. **코드의 random 생성문을 이번에 실행한 것이 아니라 저장 label을 대조했다.** [B2 코드61–90행](../evidence/0003-0007/originals/SRC-0022942.py.txt), [B2 소속](../evidence/0003-0007/originals/SRC-0023588.json), [frozen tasks](../evidence/0003-0007/originals/SRC-0030238.json)

첫 seed20260925에는5방법×4group+global1개로21fit, 둘째 seed20260926에는Tab/empirical만8fit이었다. 총29fit은 과거 실행 수다. 다음은 같은16cell·480시점의 mean-scaled MAE 저장값을 재사용한 표다. [원 summary](../evidence/0003-0007/originals/SRC-0030280.json), [기존 원예측 검산](../verification/history-001-risk-check.json)

| 소속 기준 | K | seed20260925 | seed20260926 |
|---|---:|---:|---:|
| global | 1 | 0.07106777 | 미실행 |
| empirical_risk | 4 | 0.08160040 | 0.08351629 |
| knn_risk | 4 | 0.08407308 | 미실행 |
| random_balanced | 4 | 0.08559771 | 미실행 |
| tabicl_risk | 4 | 0.08732813 | 0.08776006 |
| pcc_balanced | 4 | 0.08987710 | 미실행 |

첫 seed에서 global이 다섯 K4 조건보다 낮다. K와 모델 수가 다르다는 조건을 남기면서, **이 자료에서 분할 자체가 반드시 이득이라는 전제도 지지되지 않았다**고 해석한다. Tab 대 PCC만 보면 empirical·random·global보다 나쁜 결과를 누락한다. 표의 전체 평균은 모든 cell·기간에서 같은 순위를 보장하지 않는다. [B2의 기간·cell 반례와 원척도 결과](0004-0007-b2-observed-risk.md)

Traffic Matrix 논문의 random 비교를 근거로 같은 K의 대조를 넣었지만, 논문 TablesI/II는 방법별 K가 다르다. 그 논문의 naive 그룹 크기는 TableV에서 균형적이며 세부 random 절차는 미확인이다. 이를 우리 구현의 동일 재현이나 Milan의 직접 성능 근거로 쓰지 않는다. Global/local의 함수 존재 정리 역시 유한 기억·유한 RCTL의 우위를 보장하지 않는다. [두 선행의 조건](../references/network-timeseries.md)

## 이번 정리에서 바로잡거나 남긴 내용

| 항목 | 정리본의 처리 |
|---|---|
| Montero-Manso·Hyndman2021 제목 | *Principles and Algorithms for Forecasting Groups of Time Series: Locality and Globality*로 서지 정정. 05 원문은 보존 |
| lag24/168의 근거 | 우리 설계 선택으로 표시. 도로 논문이 동일 특징을 제시했다고 쓰지 않음 |
| CoT mobile 분할 | ‘동일 분할’과 ‘첫200초 평가/나머지 훈련’ 및 train664/1569/588초의 서술을 함께 보존. forward split·유출 어느 쪽도 확정하지 않음 |
| ISP 정규화 | 읽은 절에 minmax fit 기간이 명시되지 않음. train-only를 임의로 보충하지 않음 |
| MobiGPT 비교 | checkpoint·자료 접근성 미확인과 실제 실행 미확인을 구분. 미공개라고 단정하지 않음 |
| 원 UPC | 초기 PCC balanced를 원 UPC 실행으로 승격하지 않음. strict 그룹 크기 조건 유지 |

05는 당시 후보를 ‘검토 중’이라고 적었다. 이후07은 empirical 대비 RCTL 악화를 근거로 B2를 추천에서 제외했고,08·09는 유한표본 효과와 추가 정보의 공백을 더 검토했다. 문헌이 설계에 영향을 주었다는 사실로 후속 부정 결과를 덮지 않는다. [B2 판단](0004-0007-b2-observed-risk.md), [08·09](0008-0009-finite-sample-pooling.md)

## 재사용과 다음 실험의 차이

같은 초기16cell·같은 특징·같은 K4·같은 기간을 다시 제안한다면 먼저 보존 소속,29fit 설정, 예측과 MAE를 확인한다. 이 표를 얻기 위해29개 모델을 다시 학습할 필요는 없다. [재사용 근거 묶음](../evidence/0005-network/README.md)

새 질문은 입력 공변량·시간 단위·context 행 수·horizon·소속 제약·최종 learner·독립 평가 기간 중 무엇이 달라지는지 적어야 한다. 예를 들어 실제 제공되는 이웃 정보의 추가, 원 UPC가 가능한 규모, 같은 K와 같은 계산 예산의 분리 비교는 기존 조건과의 차이를 명시할 수 있다. 이들은 재검토 조건이며 이번에 새로 실행한 실험은 아니다. 새 조건의 우위·신규성도 이 문헌 비교만으로 확정하지 않는다.
