# 문제별 과거 시도 색인

현재까지 검수한 기록의 색인이다. 여기에 없다는 이유로 과거 시도가 없다고 판단하면 안 된다. 전체 고유 기록 검토를 계속하고 있다.

| 찾으려는 문제·별칭 | 확인한 기록과 조건 | 결과·주의할 해석 | 재사용·새 실험의 차이 |
|---|---|---|---|
| Milan 가공 자료, 첫 CPU 실행, smoke, 날짜·시간 분할, Ridge 잔차 상관 | [01–02](records/0001-0002-initial-design.md), 32cell 진단·4cell smoke·256context행/64query행·seed20260925 | 저장 Tab 예측·오차 검산. 작은 직접 예측은 clustering 효용이 아님. H5 마지막 날짜2014-01-01, 정규화와 미래 target 범위 구분 | 13개 작은 원본/배열과 H5·checkpoint 해시/주소. 같은 동작 확인을 새 방법 실험으로 반복하지 않음 |
| conditional MAE curve, risk table, Bayes loss, 129quantiles, balanced merging, residual correlation | [02 설계](records/0001-0002-initial-design.md) → [03 B1](records/0003-b1-anchor-projection.md) → [04·06·07 B2](records/0004-0007-b2-observed-risk.md), 16cell·K4·504context·64상태·257action | 이상적 공통 예측 비용이며 pooled Tab/RCTL 보장 아님. B1 입력 축약 실패와 B2 RCTL 기각을 연결. [05의 가까운 방법](records/0005-closest-methods-audit.md)과 [08·09](records/0008-0009-finite-sample-pooling.md)의 후속 진단을 연결 | 처음 정한 비교군·기각 조건·예산과 가중합 척도, 실제 정답 접근 범위를 확인 |
| HCP, population pooling gain, RMB-CLE cross-error, ETAP gradient affinity, posterior projection | [05 부분 정리](records/0005-closest-methods-audit.md), [다섯 방법 비교](references/closest-pooling-methods.md), 20260925 후보 판단 | 실제 공동 적합·교차 예측·gradient·posterior 요약은 서로 다른 정보. 인용 위치3곳 정정, 후속 논문의 원문 설명/표 불일치 보존. 관련 여섯 연구는 아래 비교로 연결 | 묶는 단위·X/Y·K·learner 정보부터 비교. 같은 원리를 재명명하거나 risk table을 pooled gain의 정확한 대체로 보지 않음 |
| Localized TabICLv2, kNN context, CRUMB, MMD, query batch, TL-ANDI, anchor distillation | [05 관련 문헌](records/0005-related-foundations-audit.md), [여섯 방법 비교](references/related-tabular-clustering.md) | Localized의 같은 context/분류 미세조정, CRUMB의 X-only 선택, TL-ANDI의 의사 라벨·잔차·validation은 다름. 국소화 속도 악화와 validation 오차항 유지 | 제공 X/Y·test 시점·cache 단계·가중치 학습·검색/준비 비용부터 비교. cell 고정소속이나 RCTL 효용의 직접 증거가 아님 |
| environment-stratified, S-swap, spurious routing, CSR, TabClustPFN, amortized TS, ACF/QAF affinity | [05의 정보·학습 범위](records/0005-related-foundations-audit.md), PDF 지정 내용17쪽 | Entangled의 CSR 감소와 RMSE 악화 반례 보존. TabClust는 전체 가중치 추가 학습/K1 제외, Amortized는 합성 학습·pairwise affinity·graph 후처리 | 환경/S 추정과 최종오차, 합성 prior와 K·label 정보, checkpoint 재사용 조건을 명시. 논문 보고값을 우리 실행으로 세지 않음 |
| TabICL2.2.0, frozen fit, native999/API9/129midpoint, median/mean, KV cache, target-aware embedding, forecast wrapper | [05 공식 구현](records/0005-official-tabicl-audit.md), [고정 코드 비교](references/official-tabicl.md), 초기 B1/B2·504context·ensemble1 | 지정6코드 바이트·checkpoint config 확인. B1 median=129격자 중앙 열. 초기 cache 기본False, fit 준비 비용·다른 context 표현의 범위 구분 | 고정 버전·alpha·정보·호출량·cache·비용의 차이를 명시. 이미 저장된 예측을 새 모델 실행으로 세지 않음. 회귀 TabPFN은05 당시 미실행 제안 |
| UPC와 PCC 차이, TabPFN-ST-AR, TabPFN-TS, ISP TTM, MobiGPT, CoT throughput, multivariate channel context | [05 네트워크·시계열](records/0005-network-timeseries-audit.md), [아홉 문헌](references/network-timeseries.md), 초기16특징 | target·시간·공변량이 다름. 일/주 lag는 우리 선택, PCC balanced는 UPC가 아님. CoT 분할 서술·ISP minmax fit 기간·MobiGPT 자산 접근의 미확인 범위 보존 | 실제 제공 정보부터 비교. 문헌 지정 구간 검토와 전체 재현·우리 성능 근거를 구분 |
| random balanced, global/local, Traffic Matrix, 같은 K, 분할 자체의 효과 | [05 구현 연결](records/0005-network-timeseries-audit.md), B1→B2 동일 label·16cell/4×4·29RCTLfit | 첫 seed에서 global K1의 MAE0.07106777이 다섯 K4군보다 낮음. 논문 성능표는 방법별 K가 다르고 global 함수 존재는 유한 RCTL 보장이 아님 | 저장 소속·task·예측 재사용. 같은 초기 조건을 반복하기 전에 K·정보·평가 기간·계산 예산의 새 차이를 명시 |
| anchor quantization, 대표 입력, 최근값 수준 복원, W1 분위수 근사 | [03 B1](records/0003-b1-anchor-projection.md), 16×1088query·직접64시점·129분위수 | 직접 MAE0.072614에 비해 anchor0.140444, 수준 복원0.125104. RCTL 연결 전 기각이며 모든 Tab 방법의 실패 아님 | 원분위수·anchor·소속 재사용. 다른 상태 표현과 실제 query 보존 조건을 명시 |
| observed-query risk, empirical-target baseline, residualization, 공통 action grid, 손해 순위 | [04·06·07 B2](records/0004-0007-b2-observed-risk.md), 16×168query·5손실표·600쌍 진단·29RCTLfit | RCTL은 empirical 대비 두 seed에서+7.02%/+5.08%. 공통 action 범위에 query 정답이 참여. surrogate 이득·PCC 대비 이득만으로 채택하지 않음 | 저장 예측·손실·소속·학습 이력·기간/cell 반례 재사용. 함수군·label 가용성·독립 평가 기간의 차이를 명시 |
| finite-sample pooling, effective sample size, residual covariance, calibration, prediction-powered correction | [08·09](records/0008-0009-finite-sample-pooling.md), Gaussian3cell×31표본·20,000반복 보고와 B2설계주간16×168진단 | 같은 주변분포라도 표본 의존성에 따라 pooling 효과가 다름. Tab잔차 쌍 순위 안정성0.1332, 새 covariance/보정 후보는 미채택. MC평균/SE 독립 재현은 아님 | 기존 배열·집계·[세 선행의 적용 한계](references/finite-sample-pooling.md) 확인. 실제 추가 정보·learner·안정성 조건을 명시 |
| 전체 Milan 대표성, 중앙부 pilot, mean-scaled MAE, peak mode, 평균 profile 안정성 | [10–12](records/0010-0012-population-upc-stability.md), 10,000cell·첫28일과 다음7일·고정16pilot | pilot15/16이 전체 활동량 중앙값보다 높음. profile PCC 중앙값.98408과 mode 일치38.23%는 다른 통계. 동점45.99%는 저장 보고값 | 12개 저장 수치 배열·분포 재사용. 전체 도시 기각이나 활동량의 인과 효과로 확대하지 않고 기간·집합·척도 차이를 명시 |
| UPC core, 작은 peak group, θ=10, greedy 순서, 소속 안정성, ARI, label matching | [10–12의 제한 구현](records/0010-0012-population-upc-stability.md), 14일×2·크기>10·K3/4/5·2파형·2순서 | 주 조건 기간 일치56.64%; 공통9,986cell. weekday 연속/첫 기간 K3·4는 순서 일치100% 반례. 최종 예측 손해는 미검증 | 24개 소속 벡터·24비교·portable 검산 재사용. 원 UPC 전 재현·새 모델12회로 세지 않으며 예측 관계/learner의 새 질문을 명시 |
| same-data joint MAE, 전체 context, 직접 정확도와 clustering 효용, HGB_refreshed | [633](records/0633-joint-selection-negative.md), 두16cell·K4·세 고정 소속·cell당504행·64query·seed20260925 | Tab native MAE는 여섯 경우 모두 낮지만 선택 소속의 RCTL은 HGB 선택 대비 A+2.12%·B+19.20%. 개발 자료이며 모든 cell/Tab 방법의 기각은 아님 | 22group 출력·정확한 singleton cache2개·RCTL 원예측 보존. 같은 고정 메뉴 비교를 반복하기 전에 검산; 추가 정보·소속 연산·평가 조건의 차이를 명시 |
| bounded relation graph, UPC 소속 수정, `save()`의 `p` 충돌, `meter.json` PermissionError | [635–637](records/0635-0637-execution-recovery.md), cohort A 16cell·K4·504행 context·64 query·seed 20260925 | 구현 오류와 부분 복구다. 방법의 실증 기각으로 쓰지 않음 | 완료 14cell 분위수와 79쌍 분류 출력 보존. 같은 조건은 cache부터 확인 |
| float32/float64, 2→22 edge, 혼합 중앙값 root 잔차, Tab이 UPC를 유지함 | [638](records/0638-numeric-precision.md), 같은 예측·같은 지원/이동 규칙 | 정밀도 정정 후 Tab 3cell/HGB 1cell 이동. graph 목적 감소이며 RCTL 성능 판단은 별도 | 저장 결과만으로 수치 대조 가능. threshold·기간·모델 변경은 별도 실험 |
| relation 소속의 실제 RCTL 효용, HGB_free, 정규화·raw MAE, 평균과 전반 손해 | [639](records/0639-rctl-bridge.md), A 16cell·K4·개발 480시점·seed 20260925 | UPC 대비 정규화 −3.97%. HGB_free 대비 전체 −1.93%지만 전반 +2.71%, 원척도 전체 +6.58% | 13평가 자리 재사용·고유 원예측 10개·새 학습 3group. 같은 저장값 검산 가능 |
| Tab_path와 HGB_relation이 다른 실험인가, cell index 재사용 | [639의 출처 경로](records/0639-rctl-bridge.md), 306/325/367/388/563/581 → 639 | 367 Tab_path와 639 HGB_relation 소속 동일. 이름·인덱스만으로 새 결과나 같은 cell로 판단하지 않음 | 실제 ID·정답·시간·protocol·파일 hash를 함께 확인. 상위 기록 전체 검토는 진행 중 |
| 조건부 분위수 clustering, 함수 거리, no-refit, post-grouping의 신규성 | [640](records/0640-contribution-boundary.md), [가까운 선행 비교](references/conditional-clustering.md) | 이 요소들은 비교한 기존 방법에도 있음. 지정 절 검토이며 전수 신규성 조사나 전체 재현은 아님 | 공식 논문 링크·판본·수식·읽은 쪽수부터 확인. 논문 확보를 전체 검토로 세지 않음 |
| bounded score와 CQTE, 잡음/입력 빈도 제거, 실제 Y의 추가 판단 | [640](records/0640-contribution-boundary.md), 512/634식·635구현 | 정확한 재가중 관계와 조건부 기대값은 확인. 유한 traffic에서 p 일치·잡음 제거·MAE 보장은 미확정 | 같은 출력에서의 대조는 [641](records/0641-cached-score-controls.md)로 연결. 선행 전체 재현은 아님 |
| 같은 예측인데 다른 소속, 중앙값 거리, plug-in conflict, RCTL 재학습 필요 여부 | [641](records/0641-cached-score-controls.md), A16cell·14cache·64query·22edge·K4·같은 이동 규칙 | 네 대조 모두 UPC 유지. 기존 관측 Y 점수는 Tab3/HGB1cell 이동. 한 개발 조건의 사후 비교이며 HGB_free 반례 유지 | 16평가 자리는 기존 UPC4파일 재사용. 새 모델·MAE 계산0. 보존 산술 검산부터 확인하고 새 조건을 명시 |
| 연구 완료 선언, 연구 방향 추천, 원 UPC θ=10, 최소44cell, 아직 안 한 본실험 | [642](records/0642-research-direction.md), 20261004 최종 보고서·7쪽 Word | 완료는 착수 근거와 문서 범위. 독립 기간/도시·같은 wall-time·TabPFN·graph 크기 통제는 미실행. 44cell은 네 유효 seed 그룹의 필요조건 | 기존635–641을 다시 실행하기 전에 저장 근거를 확인. 정규화 이득과 원척도 HGB_free 손해를 함께 기록하고 새 조건을 고정 |

13–15의 추가 진단과 여섯 문헌의 지정 방법은 다음 조건으로 찾을 수 있다. 15의 후속 이력은 남아 있으며, 초기 누적 호출 비용은 [15·21 원장](records/0015-0021-cumulative-costs.md)에서 대조했다.

| 찾으려는 문제·별칭 | 확인한 기록과 조건 | 결과·주의할 해석 | 재사용·새 실험의 차이 |
|---|---|---|---|
| cross-context transfer, input support, 외삽, PCC와 교차 손해 | [13·15 일부](records/0013-0015-transfer-cell-identity.md), 16cell·504행 단독 context·고정 64query | 자기/타 context MAE0.07261397/0.17606688, 입력 거리 초과 비율과 pair 손해의 rank 상관0.74753123. 지원 matrix 요약만 검산, 인과·pooled 손해 아님 | B1 원예측·교차 MAE·PCC·지원 matrix 재사용. context 자료량·관측 범위·최종 learner의 차이를 명시 |
| UPC 소속 변화의 예측 의미, 부분집합 K, size-preserving random | [13·15의 UPC 비교](records/0013-0015-transfer-cell-identity.md), 도시 24소속을 16cell에 제한 | 실제 고유 소속10개. 주 조건 크기8/1/7→11/5이며 내부 손해는 저장 무작위 중앙범위 안. 민감도 하한 미만4행은2소속, 유의성 판정 아님 | 소속·120pair·내/외 손해 재사용. 원 1,000순열 개별값 미보존이며 새로 뽑아 독립 재현으로 세지 않음 |
| cell one-hot, full-ID, ID permutation, same-data pooled, clustering gain upper bound | [14·15 일부](records/0013-0015-transfer-cell-identity.md), 같은 2,688context행/1,024query·Tab3/Ridge2/HGB2조건 | Tab ID 평균0.775335%/열순서변경1.013756% 개선, 각각5/7cell과두날 손해. Ridge/HGB 평균 악화. 관측 ID 이득은 모든 clustering 이득의 상한 아님 | 7예측·부분3예측·168선택시간·ID순열·날짜/cell별 차이 재사용. 13의cell당504행과14의168행 차이를 pooled 효과로 해석하지 않음 |
| Effect fusion, Tree-Structured, category pooling, cell ID 병합 | [15 문헌](records/0015-category-cost-time-literature.md), 회귀 효과의 mixture/MCMC와 전체 자료 GLM split | 같은 자료에서 범주를 묶는 원리 존재. Effect의 두 partition/K1 한계, Tree의 deviance 선택과 CV/p-value 중단 구분 | 추정 대상·공변량·결정 차이를 명시. 모든 비선형 cell 병합의 기각으로 확대하지 않음 |
| BanditPAM++, virtual arms, permutation cache, Active Clustering, tight clustering | [계산 비용 선행](references/category-cost-time-methods.md), 지정 방법·정리 조건 | 고정 거리 재사용과 gap 조건, TC/오염/균형/최소 크기 필요. 같은 PAM 해는 전역 최적 보장 아님 | TFM context 준비·query 비용과 재사용 값의 동일성 확인. 식/알고리즘·보고비율 공백을 그대로 구현하지 않음 |
| CURE, entropy admission, short FIFO, long bank, NOMADD, prediction-field drift | [15 시간 context](records/0015-category-cost-time-literature.md), 분류 stream/고정 query의 class log-probability | 정보량 하한의 가정·centroid fallback·earlier-only forward validation 유지. α0 후보는 미래 무손해 보장 아님 | 시간 유효성·label 시점·단순 시간 특징 대비 결정 차이를 명시. traffic 회귀/RCTL 이득으로 간주하지 않음 |

16–17의 시간 유효성 진단은 다음 조건으로 찾을 수 있다.

| 찾으려는 문제·별칭 | 확인한 기록과 조건 | 결과·주의할 해석 | 재사용·새 실험의 차이 |
|---|---|---|---|
| old/recent/expanding, 오래된 context, 시간 유효성 | [16–17](records/0016-0017-temporal-validity.md), 32cell·4주·Ridge/HGB·고정 첫672시간 정규화·관측 lag 입력 | expanding의 전체 평균 우위에도 날짜별 손해. recent는 첫 주에 old보다 악화. 참 drift·RCTL·다중 시점 예측의 증거 아님 | 9개 저장 배열과 cell/day/week 차이 재사용. 자료 수·정보 시점·고정 origin 예측 여부를 명시 |
| 첫 주 정책 선택, 시간 구간 선택, 단순 adaptive 대조 | [고정 선택](records/0016-0017-temporal-validity.md), 첫 주 recent/expanding 선택 후 나머지3주에 고정 | always expanding 대비 후속 평균 MAE가 Ridge +0.002308935, HGB +0.002265186 악화. 모든 미래 선택 실패의 증명 아님 | 이후 정답으로 선택을 수정하지 않음. 독립 기간·선택 규칙·최종 learner가 달라지는지 확인. 17의 세 문헌은 [사용 정보·갱신 대상](records/0017-adaptation-literature.md)을 대조함 |

시간 적응과 cell 재배정 문헌은 다음처럼 찾을 수 있다.

| 찾으려는 문제·별칭 | 확인한 기록 | 적용 조건·공백 | 재검토 시 바꿔야 할 조건 |
|---|---|---|---|
| loss buffer, replay, fine/aggressive, MGSTC | [17](records/0017-adaptation-literature.md)·[방법 비교](references/temporal-adaptation-methods.md) | joint drift·예측 손실 의존 갱신. 감시 통계량 표기 미해결 | 같은 전체 입력의 조건부 변화와 정답 이용 시점을 별도로 확인 |
| PID, frozen backbone, cell별 Optuna, 출력 보정 | [PID 비교](references/temporal-adaptation-methods.md) | 이전 관측 오차 필요.200trials와200표본 한도 구분, 부호·튜닝/평가 경계 미해결 | 독립 소속 조건을 유지할지, offline 탐색과 online 비용을 어떻게 분리할지 명시 |
| Joint QoS, BCD, 재배정, nuclear norm, cluster수 축소 | [QoS 비교](references/temporal-adaptation-methods.md) | 모델 손실과 소속 공동 갱신. simulation분포 예측·가정 아래 criticalpoint | activity회귀·최종learner와 다른 점, penalty/threshold·분할을 확인 |

주변 관측 입력의 추가 가치는 다음 조건으로 찾을 수 있다.

| 찾으려는 문제·별칭 | 확인한 기록과 조건 | 결과·주의할 해석 | 재사용·새 실험의 차이 |
|---|---|---|---|
| spatial information, 이웃 평균, PCC 이웃, 8방향 | [18·21 공간 진단](records/0018-0021-spatial-information.md), 고정 32cell·Ridge/HGB·504행 학습·336시간 query | Ridge 세 추가 입력 모두 전체 평균 악화. HGB 이웃 평균의 −0.000030870 이득에도 20cell·두 번째 주 손해 | 5개 저장 배열과 전체 cell·날짜 차이를 재사용. 실제 확장 X는 미보존. 입력 추가와 grouping 효과를 분리 |
| 격자 경계, self padding, PCC 동점, 방향 정렬 | [이웃 처리](records/0018-0021-spatial-information.md), NW/N/NE/W/E/SW/S/SE 고정 순서 | Cell79의 세 자기 padding은 평균/8방향에 포함, PCC에서는 제외. 정확한 동점은 첫 방향 선택. 물리 방위 미확인 | 이웃 ID·PCC·padding을 먼저 대조. 방향 순서·동점 규칙 변경은 조건 변경으로 기록 |
| 공간·시간 진단 비교, 두 주 고정 모델 | [18·21 학습 조건](records/0018-0021-spatial-information.md), 첫 주 자기 예측은 16–17 expanding과 일치 | 공간 진단은 두 주 모델 고정, 시간 진단은 매주 적합. 매 query 실제 직전 관측 사용 | 전체 두 주를 같은 학습 조건으로 간주하지 않음. 고정 origin 다중 시점 예측과 구분 |

셀 식별 정보와 target 표현은 다음 조건으로 찾는다.

| 문제·별칭 | 확인한 기록·조건 | 결과·한계 | 재사용·다음 질문 |
|---|---|---|---|
| broad cell ID, one-hot, ID permutation, static summary | [19](records/0019-broad-cell-identity.md),32cell·각64context/query·동일pooled정보 | Tab세추가조건모두전체악화,단순모델의작은이득에도cell/day손해. 모든partition의상한아님 | 10조건예측과고정행/순열/과거통계재사용;정보추가와grouping분리 |
| residual target, delta, 차분, 최근값baseline | [20·21](records/0020-0021-target-parameterization.md),같은행·Y−최근관측·복원 | Tab평균44.93%감소와28cell악화,7524에집중. 개발후속·RCTL변경아님 | raw19재실행없이6잔차예측재사용;독립기간과최종소속효용은별도 |
| extrapolation, saturation, loss concentration, cell7524 | [집중도](records/0020-0021-target-parameterization.md),32cell모두유지 | 60.449%raw손실,26/64query가context최대초과. 수학적출력상한/물리원인미확인 | 6큰target예시와전체cell/day손해;실제병합오류의근거와구분 |


문헌의 이름과 구현 버전은 다음 조건으로 구분한다.

| 문제·별칭 | 먼저 볼 기록 | 재사용 범위와 확인할 차이 |
|---|---|---|
| FSA, Feature to Dynamics, ARMA, AR rollout, pseudo-observation | [21·22](records/0021-0022-literature-scope.md)·[방법 비교](references/forecasting-version-boundaries.md) | 계수 생성·결정적 재귀·생성값 갱신을 분리. 대형 checkpoint 우위나 실제 미래 관측 갱신 근거 아님 |
| detrend, seasonality, delta target, 차분 | [고정 TabICL 코드](references/forecasting-version-boundaries.md) | FFT 전 신호 처리와20의 잔차 target 회귀 구분. Encoder/직접 함수의 기본값 확인 |
| TabPFN-TS-3, TabPFN-3.5, known-future, static, v1.3.0 | [세 commit 비교](references/forecasting-version-boundaries.md) | 날짜·의존성·모델·입력 설명을 고정. 원22의 실제 접근 commit과3.5 checkpoint는 미확인 |
| CDE, calibration, TabularMath, computational extrapolation | [발견 범위](records/0021-0022-literature-scope.md) | 초록/지정 절 열람을 전체 방법 검토로 세지 않음. 트래픽/RCTL 직접 성능과 구분 |
| 반복 Goal 안내, AGENTS, 자동 재개 | [운영 기록](records/0021-0022-literature-scope.md) | 초기/후속 판본과 실제 앱 동작을 구분. 과거 명령을 현재 실행 지시로 사용하지 않음 |

초기 계산 비용은 다음 조건으로 찾는다.

| 문제·별칭 | 확인한 기록 | 재사용 범위·주의 |
|---|---|---|
| 45contexts,35712query,223.887초,중복 호출 집계 | [15·21 비용](records/0015-0021-cumulative-costs.md) | 여섯 완료 호출군의 합계. 고유 관측 수·전체 연구시간과 구분 |
| fit_seconds,stage_seconds,순수 학습시간,29RCTL | [타이머 경계](records/0015-0021-cumulative-costs.md) | RCTL fit에validation/test추론/일부저장 포함. stage+fit 합산 금지 |
| 캐시 재분석 비용,상한과 소비량,실패 비용 | [재사용·남은 공백](records/0015-0021-cumulative-costs.md) | 모델0회도 재분석 시간이 있음. 미확인 비용은0으로 채우지 않음 |

조건부 공유 비용과 분할 선택은 다음 조건으로 찾는다.

| 문제·별칭 | 확인한 기록 | 재사용 범위·주의 |
|---|---|---|
| conditional pooling cost, mixture median, input overlap, p_i(x) | [23·25](records/0023-0025-conditional-pooling.md) | 16cell·기존B1·고정6소속. 관계 충돌 비용과 유한표본 학습 이득 구분 |
| Tab MAE는 우수하지만 소속 선택은 미확정, density k32 | [주 결과·반례](records/0023-0025-conditional-pooling.md) | K4다섯의 cost–RCTLρ.8/KNN.9. query는RCTLtrain내부;cell3737손해도 유지 |
| float32 nonnegative assertion, float64 resume, zero group mass | [실패·비용 경계](records/0023-0025-conditional-pooling.md) | 실패보고3.8575초를포함한6.4339초;원콘솔미확인. 모델0회와계산비용구분 |

고정 모델의 여러 시점 예측은 다음 조건으로 찾는다.

| 문제·별칭 | 확인한 기록 | 재사용 범위·주의 |
|---|---|---|
| frozen recursive, rollout, horizon6, multi-step, 21checkpoint | [24·25 §2](records/0024-0025-recursive-horizon.md) | 같은16cell·48origin·1시간학습모델.6시간 global .118290980 < Tab .136188413;직접다중시점학습아님 |
| 24시간 empirical 이득, 시간 절반·cell 손해 | [보조 결과](records/0024-0025-recursive-horizon.md) | 평균−.003772982지만뒤절반+.000100154;8cell악화.유리한horizon으로주지표변경금지 |
| raw/scaled rank reversal, persistence=daily at24h | [척도·단순 기준](records/0024-0025-recursive-horizon.md) | 12/24h Tab은raw에서global보다좋고scaled에서나쁨.겹친origin독립표본아님 |
| checkpoint hash, first-step reproduction, forward504 | [검산·공백](verification/history-017.md) | 이전21예측첫시점차0;저장산술·H5확인.새모델0,중간X미보존·가중치팀접근미확인 |

새 실험은 관련 과거 기록, 같게 유지할 조건, 달라지는 질문·조건, 재사용할 파일을 먼저 적는다. 기존 부정 결과를 회피하기 위한 조건 변경과 새로운 가설 검증을 구분한다. [첫 묶음 검수](verification/pilot-001.md), [RCTL 검수](verification/pilot-002.md), [문헌 검수](verification/pilot-003.md), [캐시 대조 검수](verification/pilot-004.md), [전체 조사 현황](verification/inventory-2026-10-08.md).

## 인접 구조를 새 소속 원리로 제안하기 전

[25 인접 문헌·판단 경계](records/0025-adjacent-structures.md)는 Ma의 VAL routing, NeST의 지역 미래 guidance, Graph Coloring의 gradient update 스케줄을 구별한다. [지정 원문 비교](references/adjacent-structures.md)에 fallback·SNR 보장의 한계와 문서 불일치를 연결했다. NTK는 상세 검토 완료 문헌이 아니다. 실제 peak 표는16cell중4개에 표본이 없고 나머지도1–28개여서, 이 결과만으로 peak 연구 방향을 확정하지 않았다.

## 관측 상태의 손해와 단순 예측기

[26·27](records/0026-0027-observable-states.md)은 최근 수준·변화·하루 편차의 TRAIN 분위수 상태를 고정하고 기존 RCTL 8개 조건·계절 기준 3개·Ridge/HGB 2개를 대조했다. empirical의 급증 이득은 두 seed/기간에 남지만 전체 손해를 상쇄하지 못했다. Tab의 희소 high_high 이득과 HGB 전체 이득에도 seed·기간·cell 반례가 있다. actual target peak·입력 상태·micro/macro·빈도 기여를 바꾸어 결론을 선택하지 않는다.

## 관계 차이·불확실성·residual 분할

[28](records/0028-mechanism-uncertainty.md)은 TabMGP posterior clustering, predictive CLT/UD 병합 확신도, Vario의 mechanism partition/MDL/top-down, two-stage global residual clustering을 비교한 문헌 검토다. 새 모델 실행 결과가 아니다. 예측 폭이 넓다는 사실이나 residual 자기상관만으로 cell별 다른 예측기가 필요하다고 결론 내리지 않는다. 재검토 시 기존 방법이 남긴 손해, TabICL의 추가 정보, 바뀔 소속, 고정 RCTL의 효용과 비용을 연결한다. 이미 존재하는 TabICL adapter·prefix 비용·겹치는 lag의 정리 조건을 먼저 확인한다. [문헌 비교와 공식 근거](references/mechanism-uncertainty.md)를 재사용하고 새로운 실행 조건의 차이를 남긴다.

## 시간 해상도만 바꾸면 공유 손해가 나타나는가

[29–32](records/0029-0032-resolution-diagnostic.md)는 동일 세cell의10분값/시간합, S8/S+L16, Ridge/HGB global/local32fit을 비교했다. 최근lag는 두해상도 모두 이득이지만 공유효과는조건별로달랐다. S+L10분Ridge4556·시간HGB4159 손해와 시간Ridge전체손해를 보존한다. 같은cell·평균정규화·학습분할·global3배행 조건의 반복인지 먼저 확인한다. [저장근거](evidence/0029-0032-resolution/README.md)와 [출처](sources/history-021.md)를 재사용하고 새 설계의 cell선정/자료량/용량/정보 차이를 명시한다. 원 UPC Fig. 7은1·2·4·6·8·12축과single global을 포함한다.

## process 식별과 분리 학습의 일반화 손해

[33–35](records/0033-0035-process-fit-gap.md): frozen fit gap, GPI/CF, G/F embedding cache, 유한 학습 손해. 고정16cell·기존29checkpoint의 일곱K=4 조건은 global보다 train평균이 좋고 validation평균은 나빴다. 주Tab의 validation은16cell모두 악화했다. 앞/뒤84시간에서도 평균손해가 남지만 과적합만을 원인으로 확정하지는 못한다. 같은 가중치·소속·자료의 질문은 보존 예측으로 확인할 수 있다. 새로운 데이터 크기·seed·시간 구간·소속을 묻는 경우 그 차이를 먼저 적는다.

Butera의 W>P는 가정 아래 MSE 필요조건이며 유한 RCTL의 MAE 보장이 아니다. G/F 분리와 embedding cache는 선행 구조다. 모델 수4배와 epoch/batch로 계산한 step4배를 혼동하지 않는다. [근거](evidence/0033-0035-frozen-fit/README.md)와 [읽기 범위](sources/history-022.md)를 함께 확인한다. UPC Fig7의10표기는 정리 오기였고1·2·4·6·8·12로 정정했다.

## 정보이론 보장·유한 학습·sample 공유

| 문제·별칭 | 확인한 기록 | 재사용 범위·재검토 조건 |
| --- | --- | --- |
| XOR, conditional TC, synergy, capacity/redundancy, joint-predictive gap | [36–38 네 유한 사례](records/0036-0038-finite-information.md) | 주변 정보 합0/joint1, TC0→1, 중복 label 실제0/축약−1. S4.38 포화 조건과 유효한 전체식을 먼저 확인 |
| pooling uncertainty, heterogeneity, half-jackknife, empirical Bayes | [선형 panel 비교](records/0036-0038-finite-information.md) | 관계 차이 Δ와 T⁻¹h를 함께 고려. 선형성·외생성·의존 조건·MSFE를 MAE/RCTL에 그대로 옮기지 않음 |
| spectrum/context value, fixed memory, oracle, analog gain, Δnl | [context 정보집합](records/0036-0038-finite-information.md) | 같은 정보의 최적 선형 기준과 실제 학습 오차 구별. 60/40 AR·k4 추정, population 한계와 finite 값 구별 |
| 담당 cell 소속과 학습 sample 범위 분리, pretraining/reweighting | [당시 다음 질문](records/0036-0038-finite-information.md) | 공유 자체의 신규성 주장 금지. Tab의 추가 정보·단순 기준 대비 차이·기존33–35와 바뀐 조건을 기록. 39–40은 아래 자료 공유 검토,41–42는 아래 cell 진단으로 연결;43–44 문헌·역할 검토는 아래에 연결; 45 이후 미완료 |

같은 네 수학 반례는 [모델 없는 검산](evidence/0036-0038-finite-information/README.md)으로 확인한다. 문헌 상세 방법과 성능 검증, 초록 발견과 전체 논문 검토를 구분한다.

## 담당 소속과 학습 sample 공유를 분리하려는가

| 문제·별칭 | 확인한 기록 | 재사용 범위·재검토 조건 |
| --- | --- | --- |
| importance-weighted multi-task learning, task-origin classifier, joint ratio | [39–40 문헌·항등식](records/0039-0040-sample-reuse.md) | 참 ratio는 모집단 loss를 복원하지만 유한표본 성능 보장은 아님. 단순 source 분류기 대비 Tab의 추가 정보가 필요 |
| conditional ratio, quantile log_prob, geometric outlier score | [정확한 예·설치 코드](records/0039-0040-sample-reuse.md) | MAE .145/.525와 joint weight1.8/.2 예를 재사용. density calibration·공통 기준 측도·정규화 상수를 확인 |
| relative DRE, support adaptation, meta-learning | [Kumagai 비교](records/0039-0040-sample-reuse.md) | alpha>0의 참 ratio 상한과 clipped 추정값 구별. support/query 역할과 실제 포함 설정, meta-training 비용 확인 |
| positive transfer, greedy source chunk, Cantelli, lower confidence bound | [Cherkaoui v2 비교](records/0039-0040-sample-reuse.md) | 선형·noise·bias/variance 조건, alpha.01≠1% 보장, Algorithm1 gate 공백과 저자 코드 미확인 상태 보존 |
| n_permutations, Latin square, 68G, 289G, sample-sharing cost | [정적 비용 정정](records/0039-0040-sample-reuse.md) | pinned2.2.0 D17/요청4→실제17순서·최대289열별처리. 실제 forward/time과 구분하고 donor 포함 RCTL 비용을 계산 |

당시 추천안 미채택은 문헌·정보·비용 근거가 부족하다는 판단이다. 같은 자료에서 새 모델을 학습해 성능 실패를 관측한 기록이 아니다. [보존 원문과 검산](evidence/0039-0040-sample-reuse/README.md)을 재사용하고, 후속 연구에서 바뀔 질문과 조건을 명시한다.

## 평균에 가려진 cell 이득이나 기존 예측 경로 선택을 검토하는가

| 문제·별칭 | 확인한 기록·조건 | 결과와 재사용·재검토 조건 |
| --- | --- | --- |
| cell harm, persistent cell gain, 앞뒤 기간, 평균에 가려진 이득 | [41–42 및 44 수치 절](records/0041-0042-cell-harm.md), 16cell·480시간·240+240 | 주 Tab 전체 2cell 개선/두 절반 0, empirical 3/1, HGB 13/3. [27의 관측 급증 상태](records/0026-0027-observable-states.md) 이득과 다른 질문. 같은 예측 재집계에 새 fit 불필요 |
| cell oracle, sample oracle, routing, best-of-six | [사후 선택 범위](records/0041-0042-cell-harm.md), 같은 primary 6경로 | cell 사후 MAE 0.070409939/이득 0.925635307%, sample 사후 0.036067265. 정답 사용·partition 불일치 가능. 임의 clustering의 상한이나 구현 가능한 성능으로 쓰지 않음 |
| validation selector, 선택 편향, 시간 이동 | [validation→개발 연결](records/0041-0042-cell-harm.md), 840–1007에서 선택/1008–1487 평가 | 0.077273462로 global보다 8.732081404% 악화. global 선택 6개/사후 선택과 일치 5개. 저장 checkpoint 21개로 선택 입력 확인. 이미 사용한 validation·개발 자료이며 RCTL 손실 독립 조건을 충족하지 않음 |
| numeric_wall_seconds, end RSS, 비용 재사용 | [실행·원장](records/0041-0042-cell-harm.md) | 0.031521초는 저장 산술, 35,389,440 bytes는 종료 관측 RSS. 42 추가 모델 0, 지정 누적 1947.6963812초. finish 시간 중복 합산·현재 원장 전체를 당시 값으로 사용 금지 |

43과 44 §3–5의 문헌·역할 종합 및 §6 문헌 입수는 아래 기록으로 연결한다. 새 실험은 어떤 새 정보로 어떤 학습 행동을 바꾸는지, 기존 경로 재선택과 무엇이 다른지, 독립 평가 자료를 먼저 명시한다.

## 학습 후 성능이나 국소 설명으로 공유 그룹을 정하려는가

| 문제·별칭 | 확인한 기록·근거 | 같은 연구의 반복을 피하려면 |
| --- | --- | --- |
| TimeTic, transferability, fine-tuned performance, meta-regression | [43–44의 label·비용 비교](records/0043-0044-predictor-roles.md), 실제 학습 후 MASE·activation entropy·cold-start fine-tuning | RCTL 정보를 허용하는지 먼저 명시. cheap learner label은 다른 목표이며 RCTL로 옮기는 근거가 필요 |
| rank correlation, 0.6, Kendall, Spearman | [원문의 두 지표 표](records/0043-0044-predictor-roles.md), weighted Kendall과 medium Spearman 0.600 | 세 예측 구간·두 지표를 구분. 모델 순위 상관을 RCTL pooling MAE 개선으로 사용하지 않음 |
| local distillation, coefficient clustering, pseudo-observation, teacher locality | [기존 계수 군집화](records/0043-0044-predictor-roles.md), 157×8 계수·k3·100×157 재적합 | 구조 자체의 재제안과 새로운 관측·학습 행동을 구분. scalar 예측 유사성은 입력 관계 동일성의 보장이 아님 |
| feature selection stability, frozen teacher, response derivative | [정리의 가정](records/0043-0044-predictor-roles.md), 고정 locality·lasso·design/teacher 조건 | parameter 고정과 context y 독립을 구분. 5% tuning 허용오차·선택 확률 정리를 미래 MAE·군집 소속 보장으로 쓰지 않음 |
| OOF, shuffled KFold, shared ablation runtime | [고정 저자 코드](evidence/0043-0044-predictor-roles/README.md), commit f8ea1e71… | 시간 분할을 별도로 설계. global CV 추가 호출과 ablation의 공유 시간을 구별하고 같은 시간을 두 번 합산하지 않음 |

두 경로는 당시 목표에서 문헌 검토 후 미채택됐다. 새 모델 실행으로 성능 실패를 확인한 기록이 아니다. [43–44 출처](sources/history-026.md)를 재사용하고 새 정보·실제 학습 행동·이전 시도와 다른 검증 조건을 설계에 적는다.

## 다른 cell의 과거를 입력 열로 추가하려는가

| 문제·별칭 | 기존 근거 | 같은 연구의 반복을 피하려면 |
|---|---|---|
| input sharing, spatial input, 이웃 평균, PCC 이웃, 8방향 | [45–46 저장 예측](records/0045-0046-input-stability.md): 32cell·336시간, Ridge/HGB, 두 모델/두 주 교집합2/2/1개 | sample 행 공유와 입력 열 추가를 구별. 전체 평균과 기존/추가16cell·주별 손해를 함께 확인 |
| 첫 주 입력 선택, next-week selection | 같은 기록에서 Ridge 다음 주 차이+0.000147, HGB−0.000509; 둘 다15cell 개선 | 같은 개발 기간에서 선택/평가한 결과를 독립 검증으로 재인용하지 않음. 새 기간·가용 입력·선택 단위의 차이를 적음 |
| future-label oracle, 성공 cell 목록 | 사후 oracle Ridge0.145866/HGB0.231390; 소수 cell 교집합 | 미래 정답과 결과를 본 cell 선정은 실행 가능한 정책의 증거가 아님 |
| 공간 입력으로 RCTL 소속을 정하는가 | 46은 저장 단순 예측 재분석이며 새 Tab/RCTL/simple 실행0, 소속 변경false | RCTL의 입력 구성과 공동 학습 단위의 연결이 새 질문. 기존16cell/480시간 RCTL과 직접 순위 비교하지 않음 |
| cheap 비용, peak_RSS | 당시46타이머0.030364초, RSS는 종료무렵 단일 관측 | 입력/계획hash와 결과 저장은 타이머 밖. 18의 기존 적합 비용을46새비용으로 중복 합산하지 않음 |

[설정·예측·결과·당시 원장](evidence/0045-0046-input-stability/README.md)을 재사용할 수 있다. 47의 문헌·논리·규모·전체 판단은 아래 후속 기록에 연결했다. 후속75와 전수 범위는 남아 있으며 검색 결과가 없다는 이유로 새 연구라고 판단하지 않는다.

## 예측 의존 graph를 RCTL 소속으로 바꾸려는가

| 검색어·질문 | 먼저 볼 기록 | 같은 연구와 구별할 조건 |
|---|---|---|
| input sharing / sample pooling / GECOS 입력 채널 | [47](records/0047-input-sharing-roles.md): 행 공유·열 추가 구분, Input(steps,1), UPC cell별 sequence | 실제 cell/시간/열 역할과 공동 학습 함수의 연결을 명시 |
| DIC-ST / IMF / TE / Granger / 예측 관계 graph | 같은 기록: IMF군집·성분별TE/GCN, Table2와 표기·시간 절단 공백 | cell partition과 구별하고 분해+graph 자체의 선행성을 인정 |
| Markov boundary / feature mask / TabPFN / TabICL | MSE Bayes가정·OLS조건·추정mask의회귀기별Win·후속boundaryhead제안 | 합성/실제, 참/추정boundary, frozenAPI/새학습, Tab/RCTL을 구분 |
| 양방향 의존이면 같은 모델인가 | 정상Gaussian 한시점 반례: 동일분포·반대조건부중앙값 | ID·역할·이력schema를 바꿀 때 전제와 유한표본비용을 함께 설명 |
| N(k+1) / context / query 비용 | k8/query64의 특정 비교 산술; runtime아님 | 개별후보와2N묶음비교의 질문 차이, 반복·후보검색·전처리 비용 |

47의 방향 미추천은 모든 공간 입력 기각이 아니다. [45–46의 일부 긍정·부정 결과](records/0045-0046-input-stability.md)와 함께 읽고, 새 연구는 정보 손실·입력 구성·RCTL 학습 단위·독립 기간 중 무엇을 새로 검증하는지 적는다.

## 군집 합계 하나로 예측량을 줄이려는가

| 검색어·질문 | 먼저 볼 기록 | 같은 연구와 구별할 조건 |
|---|---|---|
| aggregation / top-down / scalar / 비중 배분 / 복원 | [48–49](records/0048-0049-aggregation-recovery.md):32cell·336시간·4partition·3비중 | 합계 예측과 개별 복원, 출력 수와 모델 수·호출 수를 분리 |
| 완벽한 합계 / oracle total / 최저 오차 / weighted median | 고정비중의 미래합계와사후최적scalar는다름. weightedmedian가중치p/scale | 어떤 비중·척도·비음수scalar 제약의 하한인지 명시. 미래oracle을성능으로보고하지않음 |
| PCC clustering / 평균 이득 / cell 손해 | 실제미래합계·직전비중에서PCC평균은낮지만16cell악화 | 저장cell별차이·두주·원단위손해를함께확인. 새Tab/RCTL기여와구별 |
| 직전 비중 / 전날 비중 / hour profile | 같은시점비중×합계는기존직전값/전날값과동일 | 계산경로를바꾼것과새예측구조를구별 |
| N/4 / 압축 / 추론 비용 | 4개당scalar1개출력수;실제지연시간절감미측정 | 자료읽기·비중·복원·후보PCC 비용, 실제cell정확도와절충을기록 |

[저장 NPZ/JSON](evidence/0048-0049-aggregation-recovery/README.md)으로 같은 조건의 진단을 재사용할 수 있다. 50의 상세 선행연구·신규성 종합과 후속 기록은 남아 있으므로 이 색인만으로 새 기여라고 결론내리지 않는다.

## 합계 예측·다중 출력·대표 예측을 혼동하지 않기 — 50

[50 문헌과 판단](records/0050-aggregation-literature.md)을 먼저 확인한다. ONDM은 2k 입력/k 출력의 다중 출력, HiGP는 하위·상위 출력과 정합, HTS-Cluster는 거리 기반 대표 예측 조합이다. 모델 수가 줄었다고 출력·호출·지연이 같은 비율로 줄지 않는다. HTS의 상대 시간 0.16과 네 계층 MASE 악화, ONDM MLP 동률, HiGP의 horizon별 손해를 함께 본다. [48–49 진단](records/0048-0049-aggregation-recovery.md)의 고정 비중 복원 오차를 이 세 방법 전체의 불가능성으로 확대하지 않는다. 기존 대표 예측과 다른 결정·TabICLv2의 추가 정보·개별 오차와 실측 비용이 재검토 조건이며 새 실험은 수행하지 않았다.

## 부분 관측 복원·probe 선택을 다시 설계하기 전에 — 52·54

[52·54 기록](records/0052-0054-partial-observation.md)을 확인한다. Beijing 부분집합은 두 배열의 identity와 스키마가 확인됐지만 시각·단위·물리 cell mapping이 부족하다. Milan에서는 probe4/target4·16시간 생략·cell당 context256/query64·ensemble1을 검사했다. TabICL 전체 정규화 MAE0.108537은 Ridge0.092963/HGB0.098836보다 컸고, 앞쪽 이득과 뒤쪽 손해가 공존했다. 세 확대 조건은 false/false/0이었다. 최초 context공동결측 assert 오류와 query만 검사한 수정, 실패4.1631648초도 남겼다. 현재값 복원과 미래 RCTL 성능·소속 판단은 별도 과제이며 51·53/55의 문헌 종합은 계속 검토한다.

## 목적 구간의 예측·sleep 정책을 다시 설계하기 전에 — 51·55

[GOTSF 기록](records/0051-0055-gotsf-audit.md)을 먼저 봅니다. interval은 target 값 범위이며 zero-mask MAE는 구간 빈도를 포함합니다. BLW PatchTST I1의 D1_2L은 B보다 27.48% 악화하며, 표의 평균 55.8%는 다른 최선 정책의 이득입니다. 2,880 beam을 cell로 부르거나 week 6·11을 연속 기간으로 연결하지 않습니다. 논문·코드 설정, 1025·1026행의 차이, 정수 date의 시간축, notebook 출처 공백을 확인하고 새 정보·학습 행동·구간 빈도·기간/cell 손해·실측 비용을 명시해야 합니다. 운영 simulation을 RCTL 소속 개선이나 실측 전력 절감으로 옮기지 않습니다.

## Beam 특징과 도로 정보로 예측 개선 — 51·55 후속

검색어: ITU, LightGBM, CatBoost, beam forecasting, stratified CV, target encoding, Cellular Predictions, PeMS, flow, speed, 모의 통화, 입력 가용성. [기록](records/0051-0055-network-forecasting.md)에서 10-fold BS층화와 시간순검증, 실측도로입력과모의target, 24주개선과7주금요일손해를 구분합니다. 재검토하려면 같은target/척도와미래입력가용성·분할·정규화를고정하고 셀/기간별반례까지 비교해야 합니다. 소속수정효용은 최종RCTL에서 별도확인해야하며55전체신규성검토는남아있습니다.

## Zero 판별과 공동 학습을 새 역할로 제안하기 전에 — 51 Frontiers

검색어: sparse beam, zero inflation, GRU-MTL, multi-task learning, ensemble, 입력 길이, week5, 56%, regression head. [기록](records/0051-frontiers-beam-audit.md)에서0/nonzero분류+회귀의 기존 구조와 조건별 반례를 확인합니다. 긴 입력의 보편적 우위·MAE에서분산개선·주최측week6/11직접순위는 지지되지 않습니다. 새 제안에는 실제 추가정보·학습행동·입력가용성·같은test·계산비용·기간/beam별손해를 명시하고 최종RCTL효용을 별도로 확인해야 합니다.55의event문헌은 본문미검토 상태로 남깁니다.

## 관측 입력을 줄이는 clustering을 제안하기 전에 — 53·55 Moghadas

검색어: 부분 관측, probe selection, sensor selection, LRP, DTW, softDTW, centroid, input redundancy,17%,81%,10415.90,DeExp,SEA. [학위논문 기록](records/0053-moghadas-thesis.md)은 시간 군집→일부 입력 선택→전체 미래 출력의 기존 구조와 작은M의 손해·perBS 정확도·최초 비용을 보존합니다. 단변량 RCTL 표본 공유나 현재 이력 복원과 목적을 구분하고, 새 제안에는 관측/선택/출력의 차이·시간 분리·초기/반복 비용·최종 RCTL 효용을 적습니다. [54의 제한된 복원 진단](records/0052-0054-partial-observation.md)도 함께 확인해야 합니다.

## 센서 선택과 복원을 함께 제안하기 전에 — 53·55 SRSSS

검색어: SRSSS, streaming sensor selection, 공간 정보, 관측 비용, 주기적 전체 관측, C_xx, ADMM, 선형 복원. [SRSSS 기록](records/0053-srsss.md)에서 현재값 복원과 미래 예측을 구분하고 초기100개 관측·전체 갱신·합성 비용 c의 조건을 확인합니다. 같은 관측을 줄이는 제안에는 단순 선형 복원과 다른 추가 정보, 실제 예산·초기/반복 비용, 최종 RCTL 효용을 명시해야 합니다. 표의 비교 분모와 작은 차이, 식9 부호·λ=0·주기 표기의 미해결 조건도 보존했습니다.

## 거친 관측에서 세밀한 이력을 복원하기 전에 — 53·55 Zoom2Net

검색어: Zoom2Net, telemetry imputation, super-resolution, collision, KAL, CEM, ILP, target refinement, EMD. [Zoom2Net 기록](records/0053-zoom2net.md)에서 이미 있는 측정/운영 제약·모호한 정답 집합·출력 보정을 확인합니다. 정밀 학습 정답과 실제 가용 관측, 모델 단독/CEM 포함 비용, 최종 미래 예측에 필요한 정보가 새 제안의 차이여야 합니다. MSE·Meta position 반례와 zoom factor 문구 차이, 100회 uncertainty forward의 비용 공백도 보존했습니다.

## 규칙으로 예측·복원 출력을 제한하기 전에 — 53·55 NETNOMOS

검색어: NETNOMOS, neurosymbolic, logic enforcement, SMT, constrained generation, hitting set, rule mining, semantic filtering. [NETNOMOS 기록](records/0053-netnomos.md)에서 이미 있는 규칙 학습·선택·생성 제어와 초기 GPT-2 학습, 약5배 추론 비용을 확인합니다. 새 제안은 예측 시 가용 입력·학습 구간·잘못된 규칙 처리·단순 비교군·최종 미래 예측 지표의 차이를 설명해야 합니다. sMAPE와 Burst Position의 손해, MAWI 위반0.3%, 필터 recall·비용 공백은 같은 조건의 반복을 판단할 근거입니다.

## 조건부 대체 API를 새 관측 정책으로 제안하기 전에 — 53·55

검색어: TabICLUnsupervised, impute, MICE, missingness, temperature, Shuffler, n_permutations, Ciena. [imputation 기록](records/0053-tabicl-imputation.md)은 이미 있는 대체 기능, 먼저 완전한 X로 fit한 공식 예제, [54의 직접 회귀 실험](records/0052-0054-partial-observation.md)을 구분합니다. 새 실험에는 가용 입력·시간 분리·강한 단순 대안·관측 선택 규칙·최종 RCTL 효용·반복 복원 비용의 차이가 필요합니다. 저장 코드의 범주 fallback과 요청 순열 수/실제 순서 수 차이도 재사용 조건입니다.

## 관측·전송·저장 감소를 같은 비용으로 계산하기 전에 — 53·55 Ciena

검색어: Ciena, IPFIX, OD traffic matrix, link counts, telemetry pruning, denoising autoencoder, DNN compression, index memorization. [Ciena 기록](records/0053-ciena-telemetry.md)은 링크로 흐름을 추정하는 방법, 표본 전송을 줄이는 방법, 과거 이력을 가중치로 압축하는 방법을 구분합니다. 새 제안에는 가용 참값·관측 정책·시점 분리·강한 단순 비교군·최종 예측 효용·총비용의 차이가 필요합니다. 75/78%의 분모, 시뮬레이션 압축표, 2021년 비용 기간의 공백도 함께 확인합니다.

## Beijing 생성 자료를 미래 예측으로 재사용하기 전에 — 51·55 STK-Diff

검색어: STK-Diff, Beijing, 960×168, UrbanKG, diffusion, CRPS, nsample, seed, induced subgraph. [STK-Diff 기록](records/0051-stkdiff-audit.md)은 이미 검수한 스키마와 station 생성 분할, 과거값 mask 없는 생성, 단일샘플 지표의 정답절댓값합 분모를 연결합니다. 새 제안은 실제 시간·단위·예측 때의 가용입력·시간holdout·단순비교군·최종RCTL 효용·비용의 차이를 밝혀야 합니다. 같은 NPZ 스키마 확인은 H031 결과를 재사용하고, 배치 구성·seed 초기화·샘플 수·환경과 그림/코드 차이를 재현 조건으로 남깁니다.

## 미래 일정·합성 증강을 clustering의 새 기여로 제안하기 전에 — 51·55

검색어: football, event context, future covariates, MWS, Past Learner, Future Priors Learner, STL, Bezier, synthetic augmentation, BHE, E-MAPE. [event 기록](records/0051-event-context.md)은 사전에 알려진 일정과 학습 자료 기반 합성, 전체/이벤트/주거/업무 오차의 다른 순위와 큰K 손해를 연결합니다. 새 제안은 일정의 asof 버전·같은 입력의 단순 비교군·지표 구현·train 안의 K 선택·추가 훈련비·소속 변경 행동과 최종 RCTL 효용의 차이를 명시해야 합니다. 원자료/코드 접근과 날짜·수식 불일치가 해소되기 전에는 재현 완료로 세지 않습니다.

H043 — GOTSF 그림을 실험 결과로 재사용하기 전: [구간별 정책·patching·분할 그림 검토](records/0051-0055-gotsf-media.md). GIF 144프레임은 독립 실험 횟수가 아니며, 생략된 예측과 무표기 생성 조건을 보존합니다. target 값 범위의 목적 변경을 새 cell clustering/RCTL 개선으로 동일시하지 않습니다.

## 관측 절감을 TabICL clustering으로 다시 제안하기 전에 — 51–55 종합

검색어: partial observation, telemetry, sensor selection, reconstruction, imputation, 관측 비용, 신규성, 입력 선택, 직접 회귀, sample pooling. [51–55 종합](records/0051-0055-synthesis.md)은 문제 존재·기존 원리·Tab 추가 기여를 나눕니다. 같은 네 cell·네 블록·같은 입력의 재실험보다 [저장 예측·오류·비용](evidence/0052-0054-partial-observation/README.md)을 먼저 확인합니다. 새 제안은 관측/전송/저장 단위, 가용 추가 정보, 실제 선택 행동, 시간 분리, 강한 단순 비교군, 기간·cell별 손해, 최종 RCTL 효용과 전체 비용에서 달라지는 조건을 적어야 합니다. 앞 기간 이득을 지우거나 후반 손해를 숨기지 않으며, 54를 MICE/clustering/RCTL 실험으로 재명명하지 않습니다.

## 큰 loss를 중요한 학습 표본으로 바꾸기 전에 — MAE 표본추출 반례 — 56–58

검색어: importance sampling, loss-proportional, gradient variance, unbiased, inverse probability, coreset, sample compression, 큰 오차, strata, 학습량. [56–58 기록](records/0056-0058-mae-sampling.md)은 손실분산18→0이어도 기울기분산3.025배인 정확 반례와 당시 기각 범위를 연결합니다. [보존 결과·원장과 산술 검산](evidence/0056-0058-mae-sampling/README.md)을 먼저 재사용합니다. 표본 추출용 층화와 최종 cell cluster, 모델 수와 처리 행·계산 step·fit 시간을 분리하고, 새 제안은 학습기·모드·확률·가중·정보·전체 비용에서 달라지는 조건을 명시해야 합니다. 다른 네 압축/표본추출 문헌은 아직 현재 원문 대조가 남아 있습니다.

## 합성 자료의 epoch 절감을 전체 학습비 절감으로 제안하기 전에 — 56·58 TimeDC

검색어: TimeDC, dataset condensation, synthetic time series, trajectory matching, expert buffer, DDFM, CT2M, cross-architecture, coreset, 압축 비용. [TimeDC 기록](records/0056-0058-timedc.md)에서 합성자료 허용 여부, 원 X/y pairing, 원자료expert 비용, 예측기별 원자료 대조 유무를 확인합니다. 새 제안은 단순 표본선택·cell군집·lookback 축과 달라지는 행동, 시간분할·실제지표·반복학습횟수·최종 RCTL 효용을 밝혀야 합니다. [인쇄표와 정적 코드 검토](evidence/0056-0058-timedc/README.md)를 재사용하고 재현 완료로 표시된 baseline인지 먼저 확인합니다.

## TabPFN context Shapley를 RCTL 표본 중요도로 제안하기 전에 — 56·58

검색어: TabPFN IML, Data Shapley, Kernel SHAP, context optimization, validation risk, WLS, coreset, pp, 9216 forward, sample valuation. [문맥 선택 기록](records/0056-0058-tabpfn-iml.md)에서어떤예측기의손실을설명하는지,무엇을선택하는지,validation/test와사전비용을확인합니다. 논문의분류AUC우위를최종RCTL학습속도·회귀오차·cell소속근거로대체하지않습니다. 새제안은기존안과달라지는선택단위·목적·독립근거·전체비용을연결해야합니다.

## 시간대 층화로 학습을 줄이겠다는 제안 전에 — 56·58 SCott

검색어: SCott, stratified sampling, control variate, gradient variance, timestamp, strata, SCSG, SVRG, S-Adam, S-Adagrad. [SCott 기록](records/0056-0058-scott.md)에서 학습 창과 cell cluster, snapshot과 inner update, smooth 이론과 MAE/ReLU·BatchNorm/dropout 조건을 확인합니다. 같은 strata·시간 규칙에 Tab 이름만 붙이는 것은 새 clustering 결정이 아닙니다. 새 제안은 다른 선택 대상·목적·직접 근거와 준비/튜닝까지 포함한 총비용을 연결해야 합니다.

## 반대 방향 표본을 미리 짝지어 학습하겠다는 제안 전에 — 56·58 SGD-as

검색어: SGD-as, antithetic sampling, permutation, negative covariance, signed inner product, gradient variance, 사전 짝짓기. [SGD-as 기록](records/0056-0058-sgd-as.md)에서 균등 주변분포와 음의 공분산, greedy permutation과 대칭 쌍, 이진 label과 MAE residual을 구분합니다. Tab median의 부호로 바꿨다는 사실만으로 RCTL의 분산·시간 개선이 확인되지는 않습니다. 새 제안은 실제 학습기의 근거, 시간 분할, 대응표 준비비와 재사용 횟수를 연결해야 합니다.

## 학습자료를 줄여 RCTL을 빠르게 하겠다는 제안 전에 — 56–58 종합

검색어: training compression, sample importance, dataset condensation, context valuation, stratification, antithetic sampling, 학습량, 준비비, 재사용. [다섯 문헌 비교](records/0056-0058-compression-synthesis.md)에서 셀 소속·학습 창·PFN 문맥·합성 자료를 먼저 구분합니다. 원문별 유효 사례와 적용 한계, 비용의 분모, 당시 미채택 조건을 확인하고 새 제안에서 달라지는 학습기·목적·분할·직접 근거를 연결하세요.


## cell을 나누어 입력 길이를 줄이겠다는 제안 전에 — 59–62

검색어: grouping × history, lookback, 짧은 입력, process identification, global ID, context 공유량. [60번 pilot](records/0059-0062-history-grouping.md)은 4cell의 L2/L8와 일·주간 lag를 비교했습니다. Tab의 좋은 통합 예측을 clustering의 효과로 바꾸지 않고, 분할 뒤 손해와 기간별 상호작용 부호 변경을 보존했습니다. 새 기간·공유량·소속 기준·RCTL 평가에서 무엇이 달라지는지 먼저 연결하세요.

## 긴 이력의 식별 정보나 짧은 모델의 비용을 주장하기 전에 — 61

검색어: Bayes MAE, conditional median, Markov, process identification, history gain, MAC, trainable parameter, frozen bias. [61번 산술 기록](records/0061-history-logic-cost.md)에서 cell을 아는 조건과 찾는 절차, 관측 1개/2개, 전체/학습 가능한 parameter, 표준 연산 수/실제 시간을 구별합니다. 같은 식별 직관과 입력 후보만으로 신규성이나 실데이터 성능을 주장하지 말고, 달라진 가정·선택 규칙·평가·총비용 근거를 연결하세요.

## 입력 압축·wavelet·attention으로 비용 절감을 주장하기 전에 — 59 ALW

검색어: ALW, adaptive lookback, wavelet, soft truncation, 입력 길이, 공동 학습, PE, 정규화, 비용. [59번 ALW 검토](records/0059-alw.md)에서 L512→H256과 전체 Q/K·mask 연산, 고정 L512 기준의 iteration 증가, seed/환경/epoch 및 복원식 차이를 확인하세요. 기존보다 달라지는 소속 결정·독립성·실제 총비용을 설명해야 같은 시도를 반복하지 않을 수 있습니다.

## 최적 입력 길이·첫 평탄구간·cell 분할 — 59–62

검색어: Optimal Look-back, horizon, Bayes 위험, approximation loss, 이력 길이, 최초 포화, GPI, process identification, grouping, trimmed mean. [문헌과62 종합](records/0059-optimal-lookback.md)을 먼저 읽으세요. 기대 Bayes 위험 비증가, 실제 공유 예측기 오차, 최적성 증명 조건은 다릅니다. [60 파일럿](records/0059-0062-history-grouping.md)과 [61 산술·비용](records/0061-history-logic-cost.md)의 조건을 재사용하고, 새 정보집합·기간·공유량·지표·선택 비용이 무엇인지 적어야 합니다.

## 예측값 입력·잔차 target·잔차 군집 — 63–65 ECAI

검색어: forecast column, stacking, residual target, addback, ratio residual, heterogeneity, Ljung–Box, cumulative MAE, frozen layer. [63–65 ECAI 기록](records/0063-0065-ecai-interface.md)에서 세 연결 방식과 실제 학습 목표를 먼저 확인하세요. Fig.3(d)의 예측 입력 선행, 공개 TypeII의 실제값 target, 전후 잔차 정의 차이, 악화 조건·전체 비용 공백을 보존했습니다. 새 시도는 정보 가용 시점·최종 합성·비교군·지표·탐색 예산과 기존 방식에서 달라진 질문을 적어야 합니다.

## 다중 해상도 잔차 보정과 총비용 — 63·65 Heatload

검색어: MRRC, HFHR, residual target, addback, multi-resolution, forecast origin, perfect weather, RTF, stacked timing. [Heatload 검토](records/0063-0065-heatload-residual.md)에서 Base+예측잔차의 직접 선행을 확인하세요. HFHR 대비 비용 이득과 Base 대비 추가 비용, Chronos 단기 악화·에너지 개선을 함께 보존했습니다. 새 설계에는 해상도·context·horizon·발행 간격·잔차 생성 시점·최종 합성·동일 정보 비교군·두 단계 전체 비용과 기존 질문에서 달라진 점을 적어야 합니다.

## 별도 잔차 학습과 보정 강도 — 63·65 KDD

검색어: residual pipeline, meta corrector, shrinkage, alpha, overlap averaging, recursive input, Huber, parallel inference, seed confidence. [KDD 검토](records/0063-0065-kdd-residual.md)는 prediction−actual 잔차를 별도 학습해 기준 예측에서 빼는 선행을 연결합니다. α 선택 분할·초기 잔차 부호·동일 target 지표·비교 모델 식별·두 단계 전체 비용이 미확인인 부분을 구분했습니다. 모델 치환을 반복하기 전에 새 질문과 실제 최종 학습기의 이득을 확인할 조건을 적으세요.

## 경험 순위와 lag copula로 군집화 — 64·65 PLOS

검색어: empirical CDF, rank, lag copula, serial dependence, Cramér–von Mises, Lance–Williams, Ward, silhouette, STMA, WA. [PLOS 검토](records/0064-0065-plos-copula.md)는 각시계열내lag의존을비교하는선행과정리의가정을연결합니다. 단순주변변환·전체쌍거리·계층병합을새방법으로반복하기전에,조건부변환이남길정보와최종RCTL성과를확인할차이를명시하세요.

## 경험 CDF와 공유 확률 예측 — 64·65 GP-Copula

검색어: Gaussian copula, empirical CDF, marginal transform, shared RNN, low-rank covariance, Jacobian, CRPS-sum, GluonTS. [GP-Copula 검수](records/0064-0065-gp-copula.md)는분포변환→공유신경망→역변환이기존연결임을확인합니다. 새실험은Tab이추가하는정보·비용과RCTL이배울남은정보를명시해야합니다. Electricity/Taxi의예외,원본/재구현설정·구간·지표차이를먼저확인하세요.

## 조건부 PIT와 공동 의존 — 64·65 TACTiS-2

검색어: TACTiS-2, conditional marginal, PIT, copula validity, DSF, two-stage curriculum, NLL, Newey-West, interpolation. [TACTiS-2 기록](records/0064-0065-tactis2.md)은 개별 미래값의 정확조건부PIT가균등해도 공동의존은남을수있음을구분합니다. Tab CDF로바꾸는것만으로새알고리즘이되지는않습니다. 새실험은제거할정보·남길정보,단일중앙값대공동분포,원척도목표와비용을명시하고공개코드의샘플범위·단계설정·보간시각경로부터확인하세요.

## 공변량 정규화 뒤 잔존 의존 — 64·65 Conditional normalization

검색어: conditional normalization, GAM, Gamma variance, ARIMA, Kalman smoother, sieve bootstrap, conduits, lag, PIT. [조건부 정규화 기록](records/0064-0065-conditional-normalization.md)은 공변량으로 평균·분산을 제거하고 남은 의존을 모델링하는 기존 방법을 정리합니다. 약96%를 지연 정답률로, .946을 미래예측 정확도로 인용하지 마세요. Tab 적용은 남길 정보·예측 시점의 가용 공변량·원척도 손실·기존 회귀 대비 추가 기여와 비용을 먼저 정의해야 합니다. 코드 재사용 때는 ACF 변환·행lag·bootstrap 구현과 논문 조건의 차이를 확인하세요.

## 예측값·변환·보호 목표를 최종 학습에 연결하려는 경우

| 다시 제안할 질문 | 확인할 과거 기록 | 재사용과 달라져야 할 조건 |
|---|---|---|
| Tab 예측을 입력에 넣거나 잔차를 학습하면 새로운가 | [63–65 종합](records/0063-0065-synthesis.md)·H055–57 | 입력/target/합성 부호·시점 가용성·추가 예측정보·전체 비용의 차이를 제시한다. 모델 이름 교체만을 신규성으로 세지 않는다. |
| CDF·달력 정규화로 군집과 RCTL을 연결할 수 있는가 | [63–65 종합](records/0063-0065-synthesis.md)·H058–61 | 주변/전체H/달력Z/모멘트 변환과 단일값/공동분포 목표를 구분한다. 목표 척도의 역변환 loss와 남는 정보를 확인한다. |
| 평균은 나빠도 최악cell 보호에는 유리한가 | [66–68 저장 위험](records/0066-0068-group-risk.md) | 기존24프로파일을 재사용한다. 전체/뒤 모든top-k손해와 앞기간·같은cell예외를 함께 남기며 새fairness학습 반박으로 확대하지 않는다. |
| Tab 오차를 빼면 RCTL 초과손해가 되는가 | [66–68 기준 risk 예](records/0066-0068-group-risk.md) | teacher 오차와 같은 함수집합의 최적risk를 구분한다. baseline·분모·운영손해와 허용행동을 먼저 정의한다. |

MMR·MRI·q-FFL의 후속 일차문헌 대조는 아래 기록에 연결한다. 세 목적의 본문 비교는 [H066](records/0066-0068-objectives.md)에 통합했으며 실행 근거 공백은 남아 있다. 검색결과52블록·논문74쪽 보관과 본문 검증 완료를 구분한다.

## 집단별 최적 위험을 뺀 보호 — MMR / minimax regret

검색어: MMR, minimax regret, WMR, GDRO, MMV, worst group, 집단별 기준, 단일 집단 지배. [66·68 MMR](records/0066-0068-mmr.md)은 절대 위험이 큰 cell과 최적 위험 대비 손해를 구분할 때 확인할 기록입니다. 같은Θ의집단최적값과 유한 RCTL baseline을 같다고 놓지 마세요. IID/support·집중·볼록성 조건, K개 기준적합 비용, 평균과 개별 집단 결과를 먼저 구분해야 합니다. 원67의 저장 위험을 MMR 학습 결과로 재사용할 수는 없습니다.

## 기준 대비 개선 비율의 보호 — MRI / relative improvement

검색어: MRI, MMRI, maximin relative improvement, Kalai–Smorodinsky, baseline, oracle gap, leximin, 손해 없음. [66·68 MRI](records/0066-0068-mri.md)에서 계절 MAE로 단순히 나누는 것과 같은 함수집합의 개선 가능 폭으로 정규화하는 것의 차이를 확인하세요. 작은 분모·기준 선택·집단 최적값 추정, 시간순 평가와 비용이 남습니다. ACS의 400조건 빈도와 선택6사례는 RCTL의 cell 보호율이 아닙니다.

## 편차 감소와 부족 할당의 구분 — 통신 q-FFL / q-FedAvg

검색어: q-FFL, q-FedAvg, Abilene, fairness, CV, under-provisioning, 과잉·부족, 식5, 80%. [66·68 q-FFL](records/0066-0068-qffl.md)에서 MSE 편차 감소와 개별 손실 증가, 부족/과잉 균형과 부족량 증가를 먼저 확인하세요. 원래 알고리즘의 공개 코드는 통신 실험 구현으로 확인되지 않았습니다. 지표 이름 변경이나 Tab loss 대입만으로 보호 효과와 신규성을 주장할 근거가 생기지 않습니다.

## 피크 보호·분위수 보정·부족 예측 비용

검색어: peak, extreme, macro, micro, pinball, quantile, inverted_cdf, 여유분, underprediction, Forecaster’s Dilemma, DeepCog. [69–71](records/0069-0071-peak-objective.md)에서 기존 8조건과 38보정 조건을 먼저 확인하세요. 실제 target으로 고른 피크의 이득과 전체 U/O·발생 빈도·기간별 예외를 구분합니다. 평균 높이 맞춤은 Tab 검증 정보를 사용하며 새 독립 경쟁 모델이 아닙니다. [세 보호 목적 비교](records/0066-0068-objectives.md)는 baseline·최적 위험·손실 척도의 차이를 정리합니다.

## 피크 subset 평가와 proper score — Forecaster’s Dilemma

검색어: outcome conditioning, observed extreme, twCRPS, CL, CSL, calibration, DM, Neyman–Pearson, 점예측, 꼬리 가중치. [69–71 문헌 검수](records/0069-0071-forecaster-dilemma.md)에서 결과 y에 가중치를 곱하는 평가와 임계값 z에 가중하는 twCRPS를 먼저 구분하세요. 전체 MAE·관측 피크 손해·실제 운영 결정은 서로 다른 질문입니다. 논문의 점예측 반례는 실제 Tab 이득 전체의 원인이 상수 편향이라는 증명이 아니며, 모든 비대칭 학습 목적을 기각하지 않습니다. 판본 없는 Table 7 인용은 2015/2017의 17개 차이를 먼저 확인해야 합니다.

## 용량 결정·SLA 사건 비용·DeepCog 구현을 검토할 때

검색어: DeepCog, α-OMC, capacity, SLA, 사건 비용, pinball, SBD, MDS, Hungarian, MAE-pre, MAE-post, oracle. [69–71 DeepCog](records/0069-0071-deepcog.md)에서 먼저 용량 유지 기간과 비용의 분모를 확인하세요. INFOCOM2019 notebook과 JSAC 저자본은 손실의 양초과 기울기와 Dense 구조가 다르고, 고정 상수+MAE 인쇄식만으로 학습이 바뀌지는 않습니다. 미래 oracle의 이득을 배치 가능한 보정으로 제시하거나 입력 격자 배치를 UPC 소속 수정의 기여로 재명명하지 않습니다.

## SIU2026·비대칭 예측·검색에만 등장한 후보

검색어: NeuralProphet, PELT, rolling Z-score, SIU2026, TSUL, SVAE, Digital Twin, quantile GRU, 검색 오류, 중복 초록. [69–71 검색 기록](records/0069-0071-siu-search.md)에서 먼저 본문 검수 여부와 실제 연구 대상을 확인하세요. SIU 손실 계수·단위·시간 분할은 미확인입니다. TSUL 주변 추천문의76.4%·10%, Digital Twin의 통신량5.41–7.01%를 UPC/RCTL 성능으로 옮기지 않습니다. 새 설계에는 실제 논문/실행 자료와 정보 시점·행동·비교군의 차이가 필요합니다.

## 예측 가능한 출력 공간으로 압축하려는 경우

[72–75](records/0072-0075-output-compression.md)를 먼저 확인한다. 좋은 직접 Tab 예측은 압축 성공과 다르며, 실제 target의 rank2 압축7조건은 비압축 HGB보다 전체·양쪽 절반 MSE가 나빴다. 국소 이득은 남긴다. 같은 비용의 multioutput 대안·복원 손실·실제 RCTL 연결을 명시해야 한다. 75의 입력 공유 재진입은47중복으로 새 모델 실행 전에 중단됐다.

## 예측모형의 계수·중요도로 군집화 — Globalization

검색어: model-based whole TSC, weighted instance TSC, local/global, feature-transformer, target-transformer, M×M, AESO, peak load. [72 문헌 대조](records/0072-globalization-audit.md)를 먼저 확인하세요. Algorithm1은 local계수로 series를 묶고 Algorithm2는 global중요도로 sample거리를 가중합니다. 최종 RCTL계수에 의존하면 독립 소속 조건과 충돌하며, cell과sample의 군집 단위도 다릅니다. 평균nMAE만으로 채택하지 말고 최대MAPE·월별피크 반례, local200/global1000 trees, t+1입력 입수 가정, θ처리/query배정/seed 공백을 함께 확인해야 합니다.

## 예측 가능한 출력·response DR·GNN 공동학습

검색어: ForeCA, forecastability, spectral entropy, mbrdr, yc, prr, pfrr, upfrr, MinCutPool, static assignment, output compression. [73의 문헌·구현 대조](records/0073-forecastable-output-audit.md)를 먼저 확인하세요. 스펙트럼 집중도는 특정 horizon의 예측 손실이 아니며 mbrdr의 통계량은 자동 차원 선택이나 누적 설명분산과 다릅니다. GNN의 S는 예측 손실과 공동학습하므로 최종 RCTL 독립 소속 조건을 다시 확인해야 합니다. 같은 문헌 요약을 반복하기보다 바뀐 입력 정보·전처리·최종 예측기·비용 또는 확보한 원자료를 명시하세요.

## 검색에서 찾은 군집·입력 선택·설명을 다시 제안하려는 경우

검색어: GFSM, Granger, context resampling, ScaleMoR, TabClustPFN, geocif, SHAP, shapiq, fippy, causal discovery. [72–75 검색 검수](records/0072-0075-saved-search-audit.md)와 [47](records/0047-input-sharing-roles.md)을 먼저 확인하세요. 검색159응답은 독립 실험159개가 아닙니다. 학습 sample을 고르는 것, 입력 열을 추가하는 것, 같은 함수를 공유할 cell을 정하는 것은 다른 행동입니다. fippy의 TabPFN은 당시 계획이었고, geocif의 PCA→Ward 분석은 같은 페이지의 TabICL 모델 목록과 별도 기능입니다. 같은 후보를 다시 열려면 확보한 실제 구현·새 정보 조건·비교군·비용과 기존 중단 이유의 변화를 명시하세요.

## 반응 증류·동적 routing·task 표현·분산 학습을 제안하려는 경우

[76–79](records/0076-0079-learning-decisions.md)를 먼저 확인한다. 반응 loss는 global distillation과, 동적 소속은 calendar/global 대안 및 예측 시점 정보와 비교한다. task 전이는 허용 head와 동일 target을, 분산 학습은 실제 배치·통신 조건과 독립적인 소속 판단을 확인한다. 모델명·거리·embedding 교체만으로 과거 시도와 다른 연구가 되지는 않는다. 77 FedCAP의 IoT 표기는 79에서 Telecom으로 정정됐고, 80은 별도 원결과 검수가 남았다.

## 입력 반응·상호작용 증류를 다시 설계하기 전

[76의 문헌·구현 대조](records/0076-response-transfer-audit.md)에서 입력 미분, 파라미터 gradient, 시간 변화, 마스킹 예측 차이를 먼저 구분한다. Sobolev·Jacobian의 반응 loss와 TabDistill의 변수 조합 전달은 선행 사례이며, teacher의 좋은 점 예측만으로 미분 정확도나 별도 clustering 필요성이 보장되지 않는다. 같은 정보를 받는 global 대안, 실제로 가능한 입력 변화, teacher 버전과 질의 비용을 명시해야 한다.

[저장 결과](evidence/0076-response-transfer/README.md)는 PMLB 27개 task의 결과·순위·요약과 PyGAM 1개 실패를 제공한다. 논문의 평균 순위를 원단위 오차로 해석하거나 코드 기본 v3를 버전 없는 과거 결과에 소급하지 않는다.

[상호작용 목록·예산별 결과](records/0076-tabdistill-interaction-audit.md)는 SPEX의 FBII/BII/FOURIER/FSII/MOBIUS/SII/STII와 Baseline·RuleFit을 찾는 관문이다. 4항 FBII는 Baseline 대비 MAE가 작은 과제 12개·큰 과제 15개이며, RuleFit 대비는 16개·11개다. MAE와 MSE가 반대로 움직인 사례와 같은 항이 반복되는 12행도 함께 확인한다. 새 비교는 원 순서·고유 항 수·실제 행 존재 여부를 보존하고, 생성 코드·분할·판본·시간 범위의 공백을 채우는 조건으로 설계한다.


## 77의 동적 소속 근거

[동적 소속 DLM·EDP·soft membership](records/0077-dynamic-membership-dlm.md)을 먼저 확인한다. 별칭이나 시간별 배정만 바꾼 설계보다 origin에서 가능한 규칙, 상태별 공유 이득, 같은 정보의 global·달력 대안, RCTL bank/재학습의 연결을 제시해야 한다. 저장 구현에는 η 사용·역방향 mean·다변량 index 등 재사용 전 확인 항목이 있다.

[그래프 갱신·참여 셀 군집의 비교](records/0078-dynamic-graphs-load-balancing.md)를 함께 찾는다. DynaSTar의 momentum 제거 비교와 Liu의 최대 12% 복합 보상은 고정 UPC 대비 동적 소속의 독립 이득이 아니다. 새 설계에서는 입력 이웃, 참여 여부, 함께 학습할 자료 중 무엇을 바꾸는지 먼저 명시한다.

## 전이 점수를 cell 병합에 다시 쓰기 전

[원78 회귀 전이 검수](records/0079-regression-transferability.md)의 head·입력·출력 좌표 조건을 확인한다. 높은 상관과 최적 source 선택, Ridge 학습과 반환 점수, 같은 source의 전이와 실제 target pooling은 별개다. source별 정규화 손해와 global multi-head 비교 조건도 보존했다.

[Task2Vec·Fisher task embedding·MODEL2VEC](records/0080-task2vec-task-and-output-sharing.md)을 같은 문제의 관련 시도로 찾을 수 있다. 공통 probe에도 과제별 head 적합이 필요하고, MODEL2VEC은 다른 과제의 모델 성능을 사용한다. 거리 코드의 `asymmetric_kl`과 논문의 비대칭 선택 점수는 식이 다르다. 재검토할 때는 허용할 head·출력 변환, 같은 구조의 global 대안, 최종 RCTL과 독립적인 선정 정보를 먼저 명시한다.

[NTKMTL·NTKMTL-SR·gradient norm weighting·GO4ALIGN](records/0081-ntkmtl-training-balance.md)은 학습 중 균형 조절을 소속 결정에 옮기기 전에 확인한다. RCTL gradient를 직접 쓰는지, 별도 probe를 쓰는지, clustering 이후 loss만 조절하는지에 따라 질문이 달라진다. 재검토 시 공유할 출력·head, 최종 모델 독립성, 같은 global multi-head 대안과 실제 RCTL 공유 효과의 근거를 명시한다.

[M3L·early training affinity·NTK alignment와 원78 검색 이력](records/0082-search-and-access-provenance.md)을 추가 탐색의 출발점으로 쓸 수 있다. 저장 snippet만으로 전문 검토가 끝났다고 가정하지 말고, 전문·고정 판본·실험 조건을 확보한 뒤 최종 예측기 독립성과 실제 출력 공유 조건을 다시 확인한다.

## FMCL과 같은 사전 군집 구조의 재제안 방지

[H083](records/0083-fmcl-client-clustering.md): 고정 FM으로 client를 사전 군집화하고 별도 모델을 학습하는 구조는 이미 선행연구에 있다. 새 제안은 class 라벨 조건을 연속 target에서 어떻게 바꾸는지, 관측 가능한 정보와 총비용, 실제 출력 공유의 이득을 구체화해야 한다. 평균 성능과 편차·ablation 예외를 함께 보존한다.

## EMD-CFL과 embedding 분포 군집의 재제안 방지

[H084](records/0084-emd-cfl-embedding-distributions.md): encoder로 자료를 변환해 OT로 군집을 정하는 구조에는 선행연구가 있다. 고정 TabICL을 쓴다는 차이를 주장하려면 초기 local 학습·encoder 교환·관측 입력/target 정보·threshold/K 선택·총비용·최종 출력 공유 조건을 명시해야 한다. 군집ARI가 같아도 downstream accuracy가 다른 반례를 먼저 확인한다.

### EMD-CFL 코드를 그대로 UPC 소속 결정으로 옮기는 제안

[H085 구현](records/0085-emd-cfl-code.md)은 학습한 encoder·분류 loss·own train/other validation·겹칠 수 있는 이웃집계에 의존한다. K 입력은 군집 수 강제가 아니라 진단에 사용된다. 고정 TabICL의 관측 x/조건부 평균을 쓰려는 후보는 별도 정보와 비용 조건이 필요하다. 부분 참여의 거리 재계산도 one-shot 비용 설명과 구분한다.

### 예측값이 비슷하면 RCTL 학습도 같다는 제안

[H086 회귀 이론](records/0086-toso-gradient-heterogeneity.md)의 Γ는 참 함수의 공통 입력 분포상 차이이며, 새 iid 표본·Jacobian·PL 조건이 붙는다. TabICL 추정값의 유사성만으로 유한 batch 학습 경로나 최종 test 성능을 보장하지 않는다. 입력 support·추정 오차·고정 최종 함수·시간 분할·기대 gradient와 SGD 변동의 차이를 먼저 명시한다.

[원79 검색 후보와 판단](records/0087-distributed-search-provenance.md)을 확인해 FedCAP 약칭의 다른 논문, OCFL의 다른 arXiv ID, OTDD의 class 조건부 분포와 회귀 조건부 평균을 구분한다. 후보를 다시 제안하려면 미확인 전문·정보 조건·최종 모델 독립성과 총비용의 차이를 먼저 명시한다.
