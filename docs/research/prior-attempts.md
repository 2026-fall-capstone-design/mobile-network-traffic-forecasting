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
