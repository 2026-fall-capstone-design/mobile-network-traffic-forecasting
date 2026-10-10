# 63·65 · Heatload의 다중 해상도 잔차 보정과 비용 경계

**느리게 갱신하는 기본 예측에 빠른 잔차 예측을 더하는 구조는 이미 직접적인 선행연구가 있다.** Heatload 논문의 MRRC는 시간 단위 기본 예측과 15분 단위 잔차를 결합한다. 에너지 오차와 계산 비용을 줄인 조건이 있지만, 비교 기준에 따라 단기 오차는 커지고 기본 예측 단독보다 비용도 늘어난다. 팀이 같은 구조를 다시 제안할 때는 무엇을 새로 검증하는지부터 구분해야 한다. [논문 v1](https://arxiv.org/abs/2608.20024v1) · [주장별 근거](../verification/history-056-claims.json)

2026-09-26의 [63번 계획](../evidence/0063-0065-ecai-interface/originals/SRC-0022008.md.txt)은 예측값 입력, 실제값에서 기준 예측을 뺀 잔차 목표, 다중 해상도 연결을 나눴다. [65번 검토](../evidence/0063-0065-ecai-interface/originals/SRC-0022016.md.txt)의 27–33행은 Heatload의 보정 구조와 비용 한계를 근거로 단순 치환안을 새 추천으로 채택하지 않았다. 당시에도 이번에도 새 TabICL·RCTL 성능 실험은 없었다. 아래는 당시 판단을 논문 전체·고정 코드·인쇄값으로 확장 검수한 기록이다. [C01–C03]

## 어떤 질문을 다뤘는가

| 항목 | 확인한 범위 |
|---|---|
| 연구 질문 | 강한 기준 예측의 오차를 별도 모델이 보정하면 최종 목표와 비용이 개선되는가 |
| 외부 연구 | Ben Spoek 등의 *Systematic Evaluation of TabPFN-TS for Zero-Shot Probabilistic Heat Load Forecasting in District Heating Networks*, arXiv 2608.20024v1, 2026-08-20 |
| 실제 대상 | 지역 난방 부하의 TabPFN-TS·Chronos-2·AutoGluon 비교. 통신 cell·TabICL·RCTL 군집 실험이 아님 |
| 이번 독해 | 논문 33쪽 전체, 시각 19쪽, 저장 Python 3개 1,868줄, 직접 의존 코드 89줄, 저장 JSON 3개, 보충 텍스트 8개 |
| 이번 수치 검수 | 표 11개 79자료행의 508개 수치, Figure S2의 420개 승률, Figure S1의 5개 연간 값. 합계 933개 |
| 실행 상태 | 정적 독해·추출·그림 확인·저장 숫자의 산술 대조. 원 코드 import/실행·모델 학습/추론·난수 생성 0 |
| 우리 실험의 데이터·split·seed | 새 실행이 없어 해당 없음. 아래 외부 논문 보고값과 구분 |
| 미완료 | 다른 5문헌과 65 전체 판단, 원 예측 배열·실행 로그·전체 비용·다른 코드 및 원자료의 재현 검증 |

논문의 PFN 설명은 합성 prior에 대한 사후 예측 근사를 다룬다. 실제 난방·통신 시스템의 정확한 사후분포를 알고 있다는 뜻으로 옮기지 않는다. 논문 서론에서 TabICL을 언급한 사실도 TabICL로 MRRC를 평가했다는 근거가 아니다. [PDF 3–4쪽](https://arxiv.org/pdf/2608.20024v1#page=3) · [C03–C04]

## 비교 조건과 자료의 한계

주 실험은 시간 단위의 24시간 예측이다. TabPFN-TS의 선택 context는 12주이고 point forecast는 0.5 quantile이다. Chronos-2는 최대 8,192 steps의 context를 사용한다. AutoGluon은 2023년 자료로 학습하고 2024년을 rolling 평가하며, 예측마다 2023년 시작부터의 이력을 전달하되 모델마다 내부 사용 방식이 다르다. 모든 비교군이 같은 12주 입력과 같은 학습 예산을 쓴 실험으로 읽으면 안 된다. [PDF 5–6쪽](https://arxiv.org/pdf/2608.20024v1#page=5) · [C05]

Munich 자료는 비공개 15분 부하이고 Flensburg 공개 자료는 시간 단위다. Munich의 설정 선택에는 2024-01-15–21, 04-22–28, 08-12–18의 clean 3주를 사용한다. 이 주들은 전체 평가년인 2024년 안에 있다. 설정 선택과 완전히 분리된 새 연도의 평가로 표현하지 않는다. 전체 연도 평가는 이상 신호도 포함한다. 공개 Flensburg 대표 주의 여름 날짜는 09-02로 Munich과 다르다. [PDF 9–10·30쪽](https://arxiv.org/pdf/2608.20024v1#page=9) · [C06–C07]

Flensburg 기간은 출처 사이에 차이가 있다. 본문 10쪽은 2014–2024년이라고 쓰지만 자료 제목·README·고정 저자 metadata는 **2020–2024년**이다. 해당 heat metadata는 원 43,843행에서 5행을 삽입·보간해 43,848행을 만들었다고 보고하고, weather metadata는 같은 기간 43,848행·결측 0을 보고한다. 실제 CSV 전체·원 XLSX·전처리 결과를 재계산한 검수는 아니다. [고정 heat metadata](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/flensburg/demand/heat/heat_dh_metadata.json) · [C08]

주 실험은 미래 기온의 **실제 관측값**을 제공하는 perfect-weather 조건이다. 별도 민감도 분석은 2024-01-20–12-30 공통 구간에서 불완전 horizon을 양쪽에서 제외하고, valid time마다 24시간 lead의 기온 예측을 연결한다. 하나의 예측 origin에서 받은 단일 weather run과 같지 않다는 점을 논문도 명시한다. 우리 운영 설계에서는 실제 도착 시각과 사용 가능한 날씨를 별도로 정해야 한다. [PDF 5–6·10–11쪽](https://arxiv.org/pdf/2608.20024v1#page=5) · [C09]

## 무엇을 예측하고 어떻게 합치는가

| 경로 | 해상도·context | horizon·갱신 | 역할 |
|---|---|---|---|
| Base | 시간 단위, 12주 | 24시간, 12시간마다 | 장기 구조를 예측하고 15분 축으로 보간 |
| HFHR | 15분 단위, 12주 | 13시간, 1시간마다 | 고해상도 부하를 직접 예측하는 비교군 |
| MRRC의 residual | 15분 단위, 7일 | 2시간, 1시간마다 | 실제 부하에서 Base를 뺀 잔차 예측 |
| MRRC 최종값 | 15분 단위 | target별 최신 사용 가능 예측 | 보간한 Base + 예측 residual |

위 context는 선택한 설정을 나타낸다. Chronos-2에는 논문의 최대 8,192 steps 제한이 적용되므로, 특히 15분 자료의 12주 설정과 실제 전달되는 context 길이를 구분해야 한다.

잔차 단계의 입력 공변량은 기온과 보간한 기본 예측이다. 즉 MRRC는 기준 예측을 입력에도 넣고 **실제값−기준 예측을 context의 target으로 제공해 잔차를 예측하는 보정**이다. 읽은 코드는 명시적 `fit` 대신 `pipeline.predict_df`를 호출하며 내부 패키지 동작까지 검수한 것은 아니다. [ECAI 공개 Type II](0063-0065-ecai-interface.md)의 잔차 군집 후 실제값 target 학습과 구분한다. 식의 잔차 부호와 최종 합산 부호를 함께 보존해야 한다. [PDF 11–12·21–24쪽](https://arxiv.org/pdf/2608.20024v1#page=11) · [C10–C11]

코드 검수의 고정 commit은 `b86ec88019f850eadb544c95ed257cce486be111`이다. README와 저장 코드 3개는 고정 raw 응답과 바이트가 같고, 직접 의존 파일 등을 포함한 12개 파일의 크기·Git blob SHA-1도 저장 tree와 맞는다. 이 확인은 실제 논문 실행이나 설치 성공을 뜻하지 않는다. [코드 검토](../evidence/0063-0065-heatload-residual/code-audit.json) · [고정 참조 명세](../evidence/0063-0065-heatload-residual/external-fixed-references.json) · [C12]

## 시점 가용성과 공개 코드에서 확인한 동작

아래 행 번호는 [stacked_residual_full_year_2024.py](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/scripts/stacked_residual_full_year_2024.py)의 고정 판본이다.

| 위치 | 확인 내용 | 해석의 한계 |
|---|---|---|
| 272–345행 | Base 전체를 먼저 생성해도 잔차 origin마다 `forecast_start <= origin`으로 제한한 뒤 target별 최신 예측을 선택 | origin 이후 발행 예측을 정적으로 제외함. 데이터 도착 지연·추론 완료 시각까지 보장한 운영 시뮬레이션은 아님 |
| 89–138·307–345행 | context는 origin 미만, future는 origin부터 horizon 미만. 평가용 `future_raw`에 실제 잔차가 있어도 모델용 frame에는 target 제외 | 평가 배열의 존재만으로 미래 정답이 모델에 들어갔다고 판정하지 않음 |
| 283–345행 | Base를 시간 보간하고 앞뒤 값을 채워 15분 축에 맞춤 | 현재 origin에서 쓸 수 있는 예측으로 과거 context도 구성. 각 과거 시점에 고정해 둔 잔차와 항상 같다고 할 수 없음 |
| 348–372행 | 보간한 Base와 예측 residual 합산 | 실제 잔차를 최종 정답 보정으로 넣는 코드가 아님 |
| 141–174·375–431행 | q50 우선, 없으면 `target` 열 사용. 최종 평가는 target별 최신 residual 하나 선택 | 블록별 지표는 겹치는 2시간 창을 각각 포함하므로 최종 중복 제거 지표와 집계 대상이 다름 |
| 494–522·576–582행 | dry-run 검사는 실제 heat로 만든 `fake_base`를 쓰지만 예측·결과 저장 전에 반환 | 정상 성능 생성 경로는 `run_base_forecasts` 출력 사용. dry-run을 실제 성능 입력과 혼동하지 않음 |

공통 유틸리티는 시각·중복·결측·규칙 간격을 확인하고, 완전한 하위 시간 묶음만 평균해 시간 단위로 집계한다. 공개 시간 단위 데이터를 15분 관측 target처럼 보간해 쓰지는 않는다. 또한 안내 문구는 15분보다 미세한 cadence도 허용하는 듯하지만, 읽은 `aggregate_to_step(15분)` 경로의 `expected_count == 1` 제한 때문에 실제로는 더 미세한 입력도 거절한다. 이 정적 조건이 논문 자료에서 실행 오류를 냈다는 뜻은 아니다. [공통 코드 152–236·308–327행](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/scripts/full_year_forecasting_utils.py#L152) · [C13–C17]

MRRC의 기본/잔차 모델에는 각각 2000-01-01에서 시작하는 연속 synthetic clock을 제공한다. 실제 Europe/Berlin 시각은 스케줄·보간·출력에 남는다. DST 처리와 실제 날짜의 calendar feature 의미는 구분해야 하며, 이 변환의 효과를 분리한 ablation은 확인하지 않았다. [공통 코드 350–360행](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/scripts/full_year_forecasting_utils.py#L350) · [C18]

단일 예제 `tabpfn_ts_heat_forecast.py`의 기본 context는 365일로 논문의 선택값 12주와 다르다. 이 예제는 `target` 열을 `predicted_heat`로 유지하고 q50은 따로 저장하지만, 공통 flatten 함수는 q50을 point forecast에 쓴다. 라이브러리 `target` 열의 실제 의미와 결과 영향은 내부 구현·실행 없이 확정하지 않았다. 읽은 코드에 명시적 seed 설정은 없고, 내부 seed·가중치 revision도 미확인이다. [단일 예제](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/scripts/tabpfn_ts_heat_forecast.py) · [C19–C20]

## 개선과 손해를 같은 비교군으로 읽는다

Table 7과 S4의 인쇄값이다. CVRMSE와 E-CVRMSE·E-bias는 %, MAE는 kW, RTF는 무차원이다. MAE 뒤의 ±는 **예측 블록 MAE의 표준편차**로 반복 학습·seed의 불확실성이 아니다. 에너지 지표는 시간 단위 anchor에서 향후 12시간을 집계한다. [PDF 7–8·21–22·33쪽](https://arxiv.org/pdf/2608.20024v1#page=7) · [C21–C23]

| 모델·경로 | 단기 CVRMSE | R² | 단기 MAE ± 표준편차 | E-CVRMSE | E-bias | RTF |
|---|---:|---:|---:|---:|---:|---:|
| TabPFN-TS Base | 18.64 | 0.919 | 124.9 ± 57.8 | 7.56 | −1.23 | 1.72e−5 |
| TabPFN-TS HFHR | 17.96 | 0.925 | 114.2 ± 54.4 | 7.41 | −1.23 | 4.21e−4 |
| TabPFN-TS MRRC | 17.95 | 0.925 | 114.0 ± 54.1 | 7.21 | −1.18 | 2.16e−4 |
| Chronos-2 Base | 18.21 | 0.923 | 121.2 ± 54.7 | 6.89 | −0.51 | 5.80e−7 |
| Chronos-2 HFHR | 17.72 | 0.927 | 107.7 ± 52.8 | 7.12 | +0.55 | 8.01e−6 |
| Chronos-2 MRRC | 18.18 | 0.923 | 109.0 ± 54.1 | 6.68 | −0.47 | 6.27e−6 |

TabPFN-TS의 HFHR→MRRC는 단기 MAE가 114.2→114.0으로 거의 같고, E-CVRMSE는 약 2.7%, RTF는 48.7% 감소한다. 하지만 MRRC의 RTF는 Base 단독의 **12.6배**다. Chronos-2에서는 E-CVRMSE가 약 6.2%, RTF가 21.7% 줄어도 단기 CVRMSE는 17.72→18.18로 약 **2.6% 악화**, MAE도 107.7→109.0으로 악화한다. Chronos MRRC 역시 Base의 **10.8배** RTF다. 빠른 직접 예측 대비 비용 감소와 기본 예측 대비 추가 비용을 서로 바꿔 쓰지 않는다. [인쇄값·산술](../verification/history-056-numeric-check.json) · [C22–C23]

Table 6의 날씨 민감도 변화율 중 세 값은 앞뒤 인쇄값으로 계산하면 논문 표기와 소수 첫째 자리에서 달라진다. Tab MAE는 표기 11.7% 대 재계산 11.8%, Chronos MAE는 12.6% 대 12.7%, Chronos CRPS는 12.1% 대 12.2%다. **반올림 전 값의 가능한 범위를 고려하면 세 표기 모두 양립하므로 오류로 확정하지 않는다.** 검수한 본문 변화율 18개도 모두 그 범위와 양립한다. [C24]

## 두 단계 전체 비용을 어디서 확인할 수 있는가

| 비용 항목 | 공개 코드의 계측 경계 | 확인하지 못한 것 |
|---|---|---|
| MRRC `prediction_seconds` | `pipeline.predict_df` 호출만 측정 | pipeline 초기화·window 구성·Base 보간·flatten/merge 비용 |
| summary의 `stacked` 시간 | `raw_residual`만 합산. Base는 별도 행 | stacked 행 하나를 두 단계 총비용으로 사용할 수 없음 |
| 별도 `total_seconds` | 데이터 로드·clock·start 구성 뒤 시작. pipeline 초기화·Base/잔차 예측·지표·CSV 저장까지 포함 | 앞단 준비와 이후 metadata 저장은 제외 |
| 단일 예제 `prediction_seconds` | pipeline 초기화도 포함 | 이름이 같아도 MRRC의 같은 필드와 동일 경계가 아님 |
| 논문의 RTF | forecast wall-clock 합을 경과 운영 기간으로 나눈다고 설명 | 저장 3코드만으로 논문 후처리·두 단계 합산·분모·warm-up 포함을 종단 대조하지 못함 |

Base는 평가 시작보다 192시간 앞서 warm-up 예측을 시작한다. 해당 시간의 처리, 캐시 생성·전처리·탐색·실패 재시도까지 포함한 전체 비용은 원 측정 배열과 후처리가 필요하다. **65번 원문도 이미 잔차 단계만 합산되는 문제를 지적했다.** 이번 전체 코드 독해가 그 지적을 보강했으며, 이를 당시에는 없던 새 정정으로 소급하지 않는다. [stacked 코드 165–174·396–416·525–627행](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/scripts/stacked_residual_full_year_2024.py#L165) · [C25–C27]

논문은 H100 95,830 MiB, 8 CPU cores, RAM 64 GB, Python 3.12.3와 CUDA 12.6.3 환경을 보고한다. 고정 requirements에는 TabPFN 8.0.3, tabpfn-time-series 1.1.0, torch 2.7.1 등 12개 패키지 버전이 있다. 환경 파일을 읽은 것과 실제 설치·실행 환경을 확인한 것은 다르다. 이 GPU 보고 비용을 우리 CPU 실험의 비용으로 환산하지 않는다. [고정 requirements](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/requirements.txt) · [C20·C27]

## 잔차 보정 외에 보존할 반례와 조건

| 문헌의 비교 | 팀이 함께 확인할 조건 |
|---|---|
| context·갱신 빈도 | 긴 context가 항상 낫지 않음. 24시간 예측을 4시간마다 갱신한 CVRMSE 14.17%와 최선 4시간 직접 예측 14.04%의 차이는 0.13pp. context도 각각 12주·4주여서 순수 빈도만의 비교는 아님 |
| 모든 날씨 변수 추가 | 본문은 모든 aggregate 지표의 최고/공동 최고를 서술하지만 Chronos MAE는 전체 변수 95.6보다 기온+강수+바람 94.2, 기온+일사 95.3이 작음 |
| 지난 해 이력 추가 | Table 2의 최근 12주 기본 MAE 102.6, 자동 특징 제외 106.9, 최근 6주+전년 6주·자동 특징 제외 113.0. 특징 처리도 같게 놓고 비교해야 함 |
| 전체 연도 집계·선택 주 | Table 4에서 두 지역 모두 Chronos가 TabPFN보다 좋음. 선택 주의 주간 예측 이점도 전체 연도 168시간 Table S2에서는 유지되지 않음: Chronos CVRMSE 15.64/MAE 109.7, Tab 17.06/120.2 |
| 일별 순위·CD 그림 | 같은 선두 연결 구간은 통계적 동등성 증명이 아님. 검정 이름·기준·의존성 전제와 raw daily 배열은 미검증 |
| 평균 calibration | Tab의 평균 오차가 작아도 Flensburg 95% 구간은 Chronos의 coverage 오차 0.16pp가 Tab 0.75pp보다 작음 |

Table S3의 6개 구간 coverage로 계산한 MACE는 Munich Tab/Chronos 각각 약 0.4067/1.6267pp, Flensburg 0.4350/1.3067pp다. 그림 8에는 정확한 값 라벨이 없어 이 계산을 그림의 원값 복원으로 표시하지 않는다. MACE는 coverage 오차, CRPS는 분포 점수다. Flensburg 구간 폭 표의 kW와 그림 8 CRPS의 MW도 구분한다. Table 5의 네 행은 S3의 재인용으로 독립 실험이 아니다. [PDF 13–21·31–32쪽](https://arxiv.org/pdf/2608.20024v1#page=13) · [C28–C33]

Figure S2는 두 지역의 모델 순서를 각각 보존했다. 대각선의 빈칸을 제외한 420개 승률에서 반대 방향 210쌍의 합은 100이다. 같은 날·같은 가중치·동률 절반 승리의 midrank를 가정해 30개 평균 순위를 복원하면 Table 4와 최대 0.03 차이로, 표시 정밀도에 따른 보수적 상계 0.075 안에 든다. 인쇄표에서 순위 불일치 오류가 확인된 것은 아니다. raw 일별 결과의 동일성이나 유의성 검정을 재현한 것도 아니다. [C34]

## 재사용과 재검토 조건

63번의 잔차 MAE 항등식 `|y−(b+r)| = |(y−b)−r|`는 고정한 기본값에 잔차를 더하는 손실 표현의 동치다. 유한한 RCTL 함수 집합에서 잔차가 더 쉽게 학습되거나 통신 cell의 최종 성능·비용이 개선된다는 보장은 아니다. 이미 좋은 [60번의 Tab 직접 예측](0059-0062-history-grouping.md)과 새 RCTL 보정 성능도 분리해서 기록한다. [C01–C03·C35]

새 실험 설계에는 기본 예측과 residual의 해상도·context·horizon·발행 간격, 실제 잔차의 생성 시점, 합성 방법, 단기/에너지 목표, 동일한 정보·갱신 조건의 비교군, 두 단계와 준비 과정을 포함한 비용을 적는다. 군집 변경을 제안한다면 예측기 변경의 효과와 군집의 효과를 나누어야 한다. 이는 같은 연구의 반복을 피하기 위한 재검토 조건이며 이번 정리에서 실행하거나 채택한 알고리즘은 없다. [과거 시도 색인](../prior-attempts.md)

고정 저장소의 MIT 표기는 코드·자체 문서·합성 fixture에 대한 것이다. 저자 고지는 Flensburg heat와 weather에 별도 출처·라이선스를 부여하고, Munich 자료는 제3자 제한으로 공개하지 않는다. 시간 단위 공개 자료는 15분 residual 관측을 제공하지 않는다. 전체 데이터·가중치의 재배포나 MRRC의 완전 재현이 확보됐다고 표시하지 않는다. [저자 고지](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/THIRD_PARTY_NOTICES.md) · [C36]

## 출처와 남은 범위

[출처 목록](../sources/history-056.md)은 15개 원본 그룹·30개 경로를 연결한다. 기존 63·65 사본 두 개를 재사용하고 Heatload 원본 13개는 크기·해시·공식 접근 경로를 보존한다. 새 외부 보충 텍스트 8개에는 과거 원본의 source_id를 부여하지 않는다. PDF·HTML·TXT·PNG와 같은 결과의 재인용을 별도 연구 횟수로 세지 않는다. [근거 묶음](../evidence/0063-0065-heatload-residual/README.md) · [검수 범위](../verification/history-056.md)

원 TXT의 33쪽은 새 PDF 추출과 문자 동일하고, 저장 HTML.text는 원 HTML의 data 텍스트 추출과 동일하다. HTML과 PDF의 인용 번호는 다르므로 문헌 제목·저자·DOI로 연결한다. 예를 들어 Flensburg 데이터는 PDF의 46번, HTML의 14번이다. HTML이 참조하는 외부 SVG 10개·PNG 1개의 바이트는 확보·비교하지 않았고, 그림의 내용은 저장 PDF에서 확인했다. 이 확인을 HTML 파일 안에 그림이 모두 보존됐다는 뜻으로 쓰지 않는다. [형식 검수](../evidence/0063-0065-heatload-residual/format-audit.json) · [C37–C39]

ECAI와 Heatload의 해당 검수는 끝났지만, KDD residual·PLOS copula·GP-Copula·TACTiS-2·conditional normalization과 65 전체 종합은 남아 있다. 읽은 3코드에서 에너지·CRPS·MACE·RTF 최종 표 생성까지 연결하지 못했으며, 다른 저자 코드·tests·외부 패키지 내부·원 데이터·실행 결과도 미검수다. 전체 고유 기록, 실패·비용 종합, 팀의 대용량 자료 접근, 최종 원본 변경분과 검색 검수 역시 계속 진행한다. [C40]

## 후속 범위: KDD 전체 검수

[H057 KDD 기록](0063-0065-kdd-residual.md)에서20쪽본문·시각/18표314행3191인쇄값과판본을추가검수했습니다. 위 미완료문헌수는각작성당시범위이며현재는PLOS·GP-Copula·TACTiS-2·conditional normalization의네문헌과65전체종합이남습니다. 기존검수JSON은당시snapshot으로보존합니다.
