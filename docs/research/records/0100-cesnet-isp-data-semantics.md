# CESNET과 ISP TTM 원문에서 확인한 결측 분모와 결과의 한계

[출처](../sources/history-100.md) · [검수](../verification/history-100.md) · [표 전사](../evidence/0100-cesnet-isp/reported-tables.json) · [그림 확인](../evidence/0100-cesnet-isp/figure-review.json)

**핵심:** 99.94%는 “gap이 있는 IP 시계열의 비율”이다. 관측 시점의 결측률·실제0 비율과 다르다. ISP의 zero fill, 집계 설명, 이상치 제거와 비용 측정 범위를 함께 확인해야 결과를 재사용할 수 있다.

[원82의 보류 판단](0099-intermittence-decision.md)에 이어 두 일차 문헌을 검수했다. 아래 성능 값은 저자 보고이며 이번 작업의 재실행 결과가 아니다.

**상태:** 28개 주장·7개 묶음의 작성 후 원문·그림 대조 완료. 새 모델·원 연구 코드 실행0.

## 데이터와 관측 공백

<a id="c01"></a>**C01.** 원82에서 보류했던 간헐 트래픽 후보의 근거 중 CESNET-TimeSeries24 데이터 논문(2025, DOI 10.1038/s41597-025-04603-x)과 ISP TTM 논문의 arXiv 2511.17529v2(2026-02-17)를 대조했다. 데이터의 공백을 무엇으로 해석했는지, 어떤 분모와 전처리를 사용했는지, 보고 결과가 어느 범위까지 적용되는지가 질문이다. 현재 학습·추론·성능 실험은 수행하지 않았다.

<a id="c02"></a>**C02.** CESNET은 2023-10-09부터 2024-07-14까지 40주 동안 수집한 IP·기관·기관 subnet 자료다. 기관 283개, subnet 548개이며 필터 후 IP는 275,124개다. n_bytes는 구간별 전송 바이트 수다. Milan Internet activity나 무선 cell·beam의 값으로 바꿔 부를 수 없다. ISP의 약27만 IP 설명과 실제 평가 표의 IP Sample은 구별하며, 평가된 IP 개수는 본문만으로 확정하지 않는다.

<a id="c03"></a>**C03.** CESNET은 경계망의 IP flow 관측을 사용한다. 연결 분할의 active timeout은 5분, inactive timeout은 65초이고, 양 끝점이 외부인 transit traffic과 단일 TCP-SYN 스캔을 필터링했다. 이 과정과 IP flow에서 10분 datapoint를 만드는 과정이 Fig.2–3에 나온다. 따라서 공개 시계열은 모든 패킷·모든 활동을 그대로 보존한 원시 로그가 아니다.

<a id="c04"></a>**C04.** 데이터 논문은 원래 약40만 IP 중 10분 구간의 99.75% 초과가 비어 있는 시계열, 괄호 설명으로 non-empty datapoint가 100개 이하인 시계열을 제외했다고 적었다. 이는 ISP 논문의 결측률 설명보다 앞선 데이터 구성 단계다. 이 필터를 통과한 모집단의 결과를 필터 전 모든 endpoint에 일반화하지 않는다.

<a id="c05"></a>**C05.** CESNET Table1은 flows·packets·bytes를 합계로 집계하고, 고유 목적지 개수에는 합계·평균·표준편차를, 비율·평균 지표에는 평균을 제공한다. 반면 ISP §III-A는 hourly/daily 집계를 temporal averaging으로 설명한다. n_bytes를 포함한 모든 지표가 평균 집계라는 서술은 원 데이터 명세와 맞지 않는다. 실제 ISP 실행에서 어떤 파일·집계를 사용했는지는 코드와 결과를 추가 확인해야 하며, 이 문장 차이만으로 실행 오류를 확정하지 않는다.

<a id="c06"></a>**C06.** CESNET Table6의 분모는 시계열 개수다. 행 순서 IP/subnet/기관, 열 순서 10분/1시간/1일의 값은 각각 99.94/99.21/89.81%, 86.31/31.75/6.75%, 77.81/21.83/3.16%다. 뜻은 “결측 구간을 포함하는 시계열의 비율”이다. ISP §III-A는 같은 수치를 IP-level intervals 및 기관·subnet의 missing intervals 비율로 서술한다. 원82의 분모 정정은 원본 표와 일치한다. 99.94%를 전체 시점의 결측률이나 실제0 비율로 사용하지 않는다.

<a id="c07"></a>**C07.** CESNET Fig.6의 축은 집계 간격과 datapoint 비율(0–1)이고, Fig.7은 관측 비율에 대한 KDE다. 두 그림에는 기관·subnet·IP를 따로 식별하는 범례가 없다. 본문의 10분 평균 관측률20% 미만 설명과 Table6의 “gap이 있는 시계열 비율”은 서로 다른 통계다. 그림의 중앙선을 평균으로 읽거나, 이 설명을 모든 기관·subnet의 개별 관측률 또는 모든 timestamp를 합친 결측률로 확장하지 않는다.

<a id="c08"></a>**C08.** CESNET은 장치가 전송하지 않아 생기는 공백도 설명하지만, 약2024-05-21 16:30부터 06-04 20:00까지 한 monitoring probe가 고장 나 collector에 IP flow를 보내지 않았다고 별도로 기록했다. Fig.5에도 probe outage 구간이 표시된다. 이는 전체 네트워크가 멈췄다는 뜻이 아니며, 모든 공백이 장애 때문이거나 실제 무트래픽이라는 뜻도 아니다. 논문은 전체 공백의 원인별 비율을 제공하지 않는다.

<a id="c09"></a>**C09.** ISP §III-C는 결측을0으로 채우고 이를 전송량0으로 해석하며 추가 보간·평활화를 하지 않는다고 설명한다. 이는 해당 연구의 전처리 가정이다. CESNET의 수집 장애 기록과 함께 볼 때, 채운0이 모두 관측된 실제 무트래픽이라고 입증되지는 않는다. 이 차이를 보존한 채 결과를 인용해야 하며, 현재 자료의 occurrence label을 설계할 때도 관측 마스크와 실제0을 먼저 구별해야 한다.

## 예측·평가 프로토콜

<a id="c10"></a>**C10.** ISP는 시계열별 시간순 45/25/30% train/validation/test 분할, shuffle·rolling origin 없음, 각 split에서 L+H window를 만들 수 없는 시계열 제외를 명시한다. min–max는 시계열별 적용이다. 다만 scaler를 학습 구간에만 fit했는지, zero fill과 scaling의 정확한 순서, 제외 후 평가 표본 수는 본문만으로 검증되지 않는다. 따라서 RMSE를 원래 byte 척도나 현재 RCTL의 오차와 직접 비교하지 않는다.

<a id="c11"></a>**C11.** TTM-R2의 R2는 모델 release이고 평가 지표 R²와 다르다. 기본 입력은 scaled n_bytes 한 채널, stride1의 중첩 window이며 [L,1]→[H,1], batch에서는 [B,L,1]→[B,H,1]이다. timestamp는 window 구성에만 사용한다. TableI의 지원 조합은 L512에서 H48/96/192/336/720, L1024·1536에서 H96/192/336/720이다. 본 실험의 hourly H96과 10분 H96은 각각96시간과16시간으로 기간이 다르다.

<a id="c12"></a>**C12.** ISP는 약100만 parameter TTM의 zero-shot과 backbone을 고정하고 prefix/head를 수정하는 few-shot을 비교했다고 보고한다. 학습 window의10/30/50%, AdamW, LR finder, OneCycle, 최대10epoch, early stopping patience3, batch64, seed42가 기재돼 있다. 선택된 window 목록·실제 LR·정확한 checkpoint 식별은 이 본문에서 확보하지 못했다. 이 설정 설명을 현재 환경의 실행·재현 성공으로 표시하지 않는다.

<a id="c13"></a>**C13.** ISP §III-G는 각 test window의 RMSE·MAE·MSE·R²를 계산한 뒤 시계열 안에서 평균한다고 설명한다. TableII는 시계열들에 대한 평균±표준편차이며 상·하위5% 이상치를 제거했다는 표제가 있다. 그림은 이상치 점을 보여 준다. 이 세 수준을 구별하고, window별 RMSE 평균을 전체 예측 오차 제곱의 pooled RMSE와 동일시하지 않는다. trim의 정확한 적용 단위·각 지표별 제외 방식과 overlap 가중치는 코드 검수가 남아 있다.

## 긍정 결과와 함께 보존할 반례

<a id="c14"></a>**C14.** 저자가 보고한 trimmed TableII에서 hourly 기관 H96의 RMSE는 L512/1024/1536에서0.0566/0.0551/0.0551이다. 10분 기관 L1024에서는 H96/336/720의 RMSE가0.0259/0.0268/0.0271, R²가0.0975/0.0654/0.0456이다. 긴 horizon에서 R²가 내려가는 값도 보존한다. 이 수치는 per-series min–max 평가의 저자 보고이며, 새 실행이나 서로 다른 시간 해상도의 동일 난이도 비교가 아니다.

<a id="c15"></a>**C15.** hourly L1024/H96에서 기관·subnet·IP의 RMSE는 각각0.0551±0.0263, 0.0541±0.0365, 0.0317±0.0262다. 대응 R²는0.2460±0.1571, 0.1685±0.1672, −1.3872±8.6764다. 따라서 IP의 scaled RMSE가 작다는 것만으로 모든 계층의 성능이 비슷하거나 안정적이라고 결론 내리지 않는다. 저자는 희소성을 원인으로 해석하지만, 이 논문 대조만으로 인과관계가 검증되지는 않는다.

<a id="c16"></a>**C16.** 실제 그림의 R² 축에는 Fig.3의10⁹, Fig.4의10¹⁸, Fig.5의10¹⁰, Fig.8의10¹⁹ 배율과 큰 음의 이상치가 보인다. Fig.5의 RMSE에도 수천 단위 점이 남아 있다. 원자료를 digitize하거나 재계산한 수치는 아니지만, trimmed TableII만으로 전체 분포가 안정적이라고 읽기 어렵다는 시각 근거다. 거의 일정한 target, 정규화, 평가 구현 중 무엇이 원인인지는 추가 검수 없이 단정하지 않는다.

<a id="c17"></a>**C17.** TableII의 hourly 기관 L1024/H96에서0/10/30/50% few-shot RMSE는0.0551/0.0718/0.0605/0.0622, R²는0.2460/−0.2170/0.1196/0.1936이다. 이 표에서는 모든 few-shot RMSE가 zero-shot보다 나쁘고30%→50%도 단조 개선이 아니다. Fig.6은 평균·중앙값과 음영을 따로 보여 주며0% 점도 있다. 본문의 약0.075→0.070은 그림 설명이므로 trimmed 표 값과 다르다는 이유만으로 오류라고 단정하지 않는다. 음영을 확인된 신뢰구간으로 부르지도 않는다.

<a id="c18"></a>**C18.** ISP가 비교한 외생 변수는 이진 주말·휴일 지표다. 저자는 성능 이득이 미미하다고 기술하지만 Fig.7의 On 조건에는 큰 RMSE 이상치가 있고 R²도10⁹ 배율로 표시된다. 그림과 요약문을 함께 보존하며 모든 개별 시계열에서 영향이 없었다고 하지 않는다. 이 결과는 모든 calendar·과거 활동 특징이 무용하다는 결론이나 다른 데이터의 외생 변수 효과를 대신하지 않는다.

<a id="c19"></a>**C19.** TableIII의 eval seconds/100 points는 hourly L1024/H96에서 기관0.044±0.003, subnet0.052±0.006, IP Sample0.096±0.028이다. 10분 기관 L1024/H96은0.376±0.042다. 따라서 초록의0.05초 미만을 모든 조건에 적용할 수 없다. 같은 표의 few-shot eval은 약0.44–0.45초, train은4.21/5.28/5.48초 per100 points다. 이 비용은 저자 보고이며 현재 TabICL/RCTL 또는1만 cell의 총 실행 시간으로 환산하지 않는다.

<a id="c20"></a>**C20.** ISP의 환경은 Apple M2 Pro·16GB RAM·macOS14.7.1 CPU이며 GPU/MPS를 쓰지 않았다고 보고한다. eval/train runtime은 HuggingFace Trainer 항목에서 가져오고 첫 시계열의 cold-start를 제외했다. TableIII의100 points와100 windows는 서로 다른 표제이므로 정확한 normalization 코드를 확인하기 전에는 같은 처리량으로 취급하지 않는다. 데이터 준비·모델 로딩을 포함한 end-to-end 비용으로 확대하지 않는다.

## 문헌의 미해결 설명과 적용 범위

<a id="c21"></a>**C21.** ISP §IV-B/C/E의 deep-learning benchmark·r=−0.69·GRU-FCN 대비 시간 비교는 여러 곳에서[11]을 가리킨다. 참고문헌[11]은 CESNET 데이터 논문이고, Comparative Analysis of Deep Learning Models for Real-World ISP Network Traffic Forecasting(arXiv2503.17410)은[12]다. 인용 번호 불일치를 기록한다. 해당 benchmark 원문·평가 코드·하드웨어를 이번 묶음에서 대조하지 않았으므로 직접 비교 가능성이나1.5배 속도 우위를 독립 검증한 결과로 쓰지 않는다.

<a id="c22"></a>**C22.** 데이터 논문의 SARIMA 시연은 IP103의 hourly n_flows, order(1,1,1), seasonal order(1,1,1,168), 2일·7일 예측과 재학습을 기술한다. 그런데 월간 학습을31 datapoints라고 표현하고, order의 세 성분을 같은 weight라고 설명하며, R²까지 낮을수록 좋다고 쓴 뒤0.77→0.79를 개선으로 해석한다. 원문의 기술상 불일치를 남기고 추정으로 고치지 않는다. Fig.10은 예측 곡선을 확인할 수 있을 뿐 이 문장들을 해결하지 않는다.

<a id="c23"></a>**C23.** CESNET Fig.8은 point·collective·trend 이상 예시이고 Fig.9는 IP1367을 여러 지표로 살펴 CESNET 전문가가 DoS로 해석한 사례다. 이는 전체 dataset에 대한 사건 정답 label이나 검출 성능 평가가 아니다. ISP도 labeled anomaly 부족 때문에 forecasting만 평가했다고 제한한다. 예측 모델의 작은 RMSE를 이상 탐지 정확도나 모든 장애 원인의 확인으로 바꾸어 적지 않는다.

<a id="c24"></a>**C24.** ISP §IV-G의 두 단계 occurrence/conditional magnitude 예측, 과거 활동 횟수·마지막 non-zero 이후 시간, 계층 간 정보 공유는 앞으로 검토할 방향이다. 이 논문에서 그런 모델을 학습해 성능 향상을 입증한 결과가 아니다. 데이터가 희소하다는 사실과 cell을 묶거나 나눌 선택이 유용하다는 주장은 별도 증거가 필요하다.

<a id="c25"></a>**C25.** 두 논문은 수집·집계·관측 상태를 확인하고 IP 계층의 어려움과 few-shot의 비용·부정 결과를 보존하는 근거로 사용할 수 있다. 그러나 ISP의 독립 univariate n_bytes 예측에는 TabICL의 UPC 소속 수정이나 최종 RCTL 비교가 없다. 이 결과를 소속 점수 개선·최종 예측 개선·cell clustering의 신규성 증거로 인용하지 않는다. 모델 선택과 시계열 공유 선택은 구별해 설계한다.

<a id="c26"></a>**C26.** 재사용 전 추가로 확인할 것은 Full IP/Sample IP 및 제외 후 표본 수, scaler fit 구간, 결측·실제0 마스크, zero fill 순서, checkpoint와 라이브러리 버전, few-shot window 선택, trim·R²·시간 normalization 구현이다. CESNET Usage Notes도 dataset part·집계·전처리·분할·horizon·지표·비용을 명시하도록 권고한다. 이는 앞으로의 확인 항목이며 본문만으로 확인했다고 세지 않는다.

## 검수 범위와 다음 자료

<a id="c27"></a>**C27.** 저장 HTML/TXT4개를 실제 읽고 HTML 표13개(중복 Table8 포함)와 ISP MathML96개를 확인했다. CESNET 그림10개는 저장 HTML의 공식 CDN 링크를 브라우저에서 열어 확인했으며, 과거 저장 시점의 이미지 바이트 동일성은 확인하지 않았다. ISP 그림7개와 표 형식 Fig.2는 기존 v2 PDF의3·4·5·6·7·9쪽으로 대조했다. PDF의 나머지3쪽을 포함한 별도 전체 PDF 검수나 외부 그림 파일의 새 원본 집계로 올리지 않는다.

<a id="c28"></a>**C28.** 이 기록은 원82의 CESNET/ISP 분모 정정과 문헌 적용 범위를 구체화한다. Citywide·Beam·Deep Renewal의 저장11자료 그룹, snapshot24의 후보표·연구일지 고유 변경, benchmark2503.17410 및 ISP 실행 코드 대조는 여전히 남아 있다. 원82 전체 자료나 전체 아카이브 Goal을 완료한 것으로 표시하지 않으며, 문헌 본문 속 향후 실행 제안을 현재 실험 명령으로 사용하지 않는다.

## 팀원이 같은 조사를 반복하기 전에

| 확인하려는 내용 | 재사용할 근거 |
|---|---|
| 99.94%를 어떻게 인용할까 | C06, CESNET Table6와 ISP §III-A |
| 모든 결측을 실제0으로 볼 수 있을까 | C08–C10, 수집기 장애·zero fill·scaler 미확인 항목 |
| IP에서도 TTM이 안정적인가 | C13–C16, trimmed 표와 이상치 그림을 함께 확인 |
| fine-tuning이나 달력 지표를 넣을까 | C17–C18, zero-shot 기준과 개별 손해·추가 비용 |
| 현재 cell 공유 설계에 직접 적용할까 | C24–C26, 예측 문제와 공유 결정·RCTL 비교의 차이 |

새 설계에는 기존 기록 링크, 데이터·시간 범위·단위, 관측 마스크, 손실과 비교군, 실제로 바꾸려는 공유 결정을 함께 적는다. [다음 자료와 남은 범위](../evidence/0100-cesnet-isp/packet-coverage.json)를 유지한다.

## 핵심 값 빠르게 찾기

CESNET Table6: **gap을 포함한 시계열의 비율**. 분모는 각 집단의 시계열 수다.

| 집단 | 10분 | 1시간 | 1일 |
|---|---:|---:|---:|
| IP | 99.94% | 99.21% | 89.81% |
| 기관 subnet | 86.31% | 31.75% | 6.75% |
| 기관 | 77.81% | 21.83% | 3.16% |

ISP TableII·III: hourly L1024/H96의 저자 보고. 아래 오차는 시계열별 min–max 척도이고 TableII는 상·하위5% 이상치 제거 후 요약이다. 비용은 CPU eval runtime 기준이며 cold-start를 제외했다. 평균만 빠르게 찾는 표로, 표준편차와 개별 이상치는 C15–C20 및 [원문 표 전사](../evidence/0100-cesnet-isp/reported-tables.json)를 함께 본다.

| 평가 집단 | 평균 RMSE | 평균 R² | eval 초/100 points |
|---|---:|---:|---:|
| 기관 | 0.0551 | 0.2460 | 0.044 |
| subnet | 0.0541 | 0.1685 | 0.052 |
| IP Sample | 0.0317 | −1.3872 | 0.096 |
