# TabICL 연구기록

과거 연구에서 무엇을 시도했고 어떤 조건에서 어떤 판단을 내렸는지 찾아볼 수 있도록 정리하고 있습니다. 전체 목록·해시·동일 사본 조사를 마쳤고, 초기 01–04·06–14·16–17의 진단·후보 설계·B1/B2 기각·공유 효과·모집단 범위·UPC 소속 안정성·교차 예측·cell 식별 정보와 15의 수치 판단을 정리했습니다. 633의 부정 결과와 635–642의 실패·복구·수치 정정·RCTL 평가·기여 범위·저장 출력 대조·연구 방향 제안도 근거와 연결했습니다. 전체 기록의 본문 검토는 계속 진행 중입니다.

| 안내 | 내용 |
|---|---|
| [전체 정리 계획](../research-archive-plan.md) | 범위, 연구 기록 양식, 재개 절차와 완료 기준 |
| [과거 시도 색인](prior-attempts.md) | 같은 연구를 설계하기 전에 확인할 조건·결과·재사용 자료 |
| [01–02 초기 진단과 설계](records/0001-0002-initial-design.md) | 32cell 자료·4cell CPU 동작, 조건부 MAE 후보와 후속 RCTL 사전 계획 |
| [03 B1 대표 입력 축약](records/0003-b1-anchor-projection.md) | 대표 상태의 예측을 옮긴 오차와 수준 복원 진단, RCTL 연결 전 기각 |
| [04·06·07 B2 손실표와 RCTL](records/0004-0007-b2-observed-risk.md) | 실제 query의 위험함수, 600쌍 진단, 29fit 결과와 empirical 대비 악화 |
| [05 가까운 다섯 방법 비교](records/0005-closest-methods-audit.md) | HCP·Population-HCP·RMB-CLE·ETAP·posterior projection의 정보·결정 차이와 인용 정정 |
| [05 네트워크·시계열 비교](records/0005-network-timeseries-audit.md) | UPC·ST-AR·TabPFN-TS·ISP TTM·MobiGPT·CoT·다변량 TabPFN·Traffic Matrix·global/local과 실제 초기 입력·random/global 대조 연결 |
| [05 공식 TabICL·초기 호출](records/0005-official-tabicl-audit.md) | 고정 코드·checkpoint,999/9/129분위수,fit·cache·mean/median과 기존 B1/B2 출력 대조 |
| [05 관련 여섯 연구](records/0005-related-foundations-audit.md) | Localized·TL-ANDI·CRUMB·Entangled·TabClustPFN·Amortized TS의 정보·학습·소속 결정과 적용 한계 |
| [08·09 유한표본 공유 효과](records/0008-0009-finite-sample-pooling.md) | 합성 반례·같은 주간의 잔차 안정성·공분산 및 예측 보정 경로의 기각 |
| [10–12 모집단·UPC 진단](records/0010-0012-population-upc-stability.md) | 전체10,000cell과 pilot 범위, 기간·순서에 따른 소속 차이와 예외, 예측 손해와의 구분 |
| [13–15 교차 예측·cell ID](records/0013-0015-transfer-cell-identity.md) | B1 예측 재사용, UPC 24조건의 제한된 관계, 동일 자료의 ID 이득과 cell·날짜별 손해 |
| [15 범주·비용·시간 문헌](records/0015-category-cost-time-literature.md) | 여섯 선행의 지정 방법·가정, 당시 미채택 판단과 원문 표현·비율의 미해결 항목 |
| [16–17 시간 유효성 진단](records/0016-0017-temporal-validity.md) | old/recent/expanding의 저장 예측, 첫 주 정책 선택과 후속 손해, 관측 이력 기반 1시간 예측 |
| [17 적응 문헌의 판단](records/0017-adaptation-literature.md) | MGSTC·PID·Joint QoS의 사용 정보·갱신 대상, 독립 소속 조건과 표기 공백 |
| [18·21 공간 정보 진단](records/0018-0021-spatial-information.md) | 자기 입력·이웃 평균·PCC 이웃·8방향의 저장 비교, 작은 평균 이득과 cell·주·날짜별 손해 |
| [19 넓힌 cell ID 진단](records/0019-broad-cell-identity.md) | 고정32cell의ID/순열/과거통계,같은pooled자료의평균과cell/day손해 |
| [20·21 잔차 target 진단](records/0020-0021-target-parameterization.md) | 평균44.93%감소와28cell악화,최근값baseline·집중도·추가6호출의근거 |
| [21·22 문헌·최신 구현 범위](records/0021-0022-literature-scope.md) | FSA·주기 탐색·TabPFN-TS 고정 버전, 발견 단계 문헌과 운영 보고의 한계 |
| [15·21 누적 호출·비용](records/0015-0021-cumulative-costs.md) | 여섯 호출군·RCTL29fit의 합계와 타이머 경계, 상한·재사용·미확인 비용 구분 |
| [23·25 조건부 공유 비용](records/0023-0025-conditional-pooling.md) | 혼합 중앙값·고정5소속의사후순위·직접예측이득과cell손해·float32실패/재개 |
| [24·25 고정 RCTL recursive 진단](records/0024-0025-recursive-horizon.md) | 6시간 주 지표의 global 우위·24시간 일부 이득과 손해·척도별 순위·21checkpoint 재사용 |
| [25 인접 문헌과 판단 경계](records/0025-adjacent-structures.md) | 소속·지역 guidance·학습 스케줄의 차이, peak 표본 부족과 당시 미추천 이유 |
| [633 공동 MAE 선택의 부정 결과](records/0633-joint-selection-negative.md) | 같은 전체 자료에서 Tab 직접 정확도의 우위와 선택 소속의 RCTL 악화가 함께 관측됨 |
| [635–637 실행·복구](records/0635-0637-execution-recovery.md) | 저장 오류와 부분 예측 복구를 방법의 실패와 구분 |
| [638 수치 정정](records/0638-numeric-precision.md) | 같은 예측에서 유효 관계가 2→22개로 바뀐 근거 |
| [639 RCTL 평가](records/0639-rctl-bridge.md) | 기존 결과 재사용·새 3group 학습, 기간별 손해와 MAE 척도별 순위 차이 |
| [640 기여 범위](records/0640-contribution-boundary.md) | 기존 방법과 겹치는 부분, 실제 Y 점수의 추가 판단을 묻는 후속 계획 |
| [641 저장 점수 대조](records/0641-cached-score-controls.md) | 네 대조가 UPC 유지, 16평가 자리의 기존4파일 재사용, 새 학습0 |
| [642 연구 방향 제안](records/0642-research-direction.md) | 최종 보고서·7쪽 Word, 완료한 문서와 미실행 본실험의 구분 |
| [조건부 clustering 선행](references/conditional-clustering.md) | 가까운 네 방법의 결정식과 CQTE 점수의 재가중 관계 |
| [전체 목록·중복 조사](verification/inventory-2026-10-08.md) | 자료 수, 라이브러리 제외 근거와 포함 대기 범위 |
| [첫 사례 검수](verification/pilot-001.md) | 원문·저장 배열 대조와 미검토 범위 |
| [RCTL 사례 검수](verification/pilot-002.md) | 실제 cell·시각·정답·MAE·재사용 출처 대조 |
| [문헌 사례 검수](verification/pilot-003.md) | 논문 지정 구간·수식·구현 대조와 미검토 범위 |
| [캐시 대조 검수](verification/pilot-004.md) | 저장 비용·배정·RCTL 지표 연결과 실제 비용 확인 |
| [연구 방향 문서 검수](verification/pilot-005.md) | 두 문서의 MAE 인용·누적 원장·완료 범위와 원 UPC 조건 |
| [초기 자료·동작 검수](verification/pilot-006.md) | 저장 특징·정답·오차·시점 대조, H5와 고정 자산의 출처 확인 |
| [부정 결과 검수](verification/pilot-007.md) | 두 집단의 입력·정확한 cache·고정 소속·원예측에서 MAE와 반례 확인 |
| [B1·B2 검수](verification/history-001.md) | 손실표·병합·예측·학습 이력·재표집과 원 H5의 지정 열 대조 |
| [08·09 검수](verification/history-002.md) | MC 보고값과 독립 산술을 구분하고 상관·coverage·상태 점유 및 세 일차문헌 대조 |
| [05 부분 문헌 검수](verification/history-003.md) | 지정 일차문헌·실제 fitting·보고값·세 인용 위치와 원문 불일치 대조 |
| [05 네트워크 문헌 검수](verification/history-004.md) | 아홉 문헌의 지정 구간·논문 보고표·초기 소속 재사용과 서지·분할 설명의 공백 |
| [05 공식 구현 검수](verification/history-005.md) | 코드6개 바이트·checkpoint 설정·저장129분위수/median·호출 로그 연결 |
| [05 관련 문헌 검수](verification/history-006.md) | 여섯 논문의 지정 구간·PDF17쪽의 지정 내용·보고표21행과 진단/최종 성능 차이 |
| [10–12 저장 진단 검수](verification/history-007.md) | population 집계·24소속 벡터·24비교와 H5 날짜, 동점·비용 보고값의 한계 |
| [13/14·15 일부 검수](verification/history-008.md) | 7개 저장 예측과 전체/cell/day MAE, 24소속의 10개 고유 관계, 원 무작위 표본·문헌 미검수 범위 |
| [15 문헌 검수](verification/history-009.md) | 여섯 논문 지정 내용29쪽·보고표6행·11개 주장; 전체논문·후속 이력 완료와 구분 |
| [16–17 저장 진단 검수](verification/history-010.md) | 32cell·4주·768fit 보고와 저장 수치, H5 입력·정답, 평균 및 cell/day 반례. 문헌 검수는 다음 H011에 연결 |
| [17 문헌 검수](verification/history-011.md) | 세 공식 v1의 지정 방법·20쪽 시각 대조·11개 주장. 공간 진단은 다음 H012에 연결하며 전체 논문·성능 재현은 미완료 |
| [18·21 공간 진단 검수](verification/history-012.md) | 444개 저장값 검사·367개 H5 대조·14개 오류 자료 검사. 실제 확장 X 저장 공백과 기록21의 남은 범위 명시 |
| [19·20·21 검수](verification/history-013.md) | 1,033개저장값·44개H5·22개오류자료검사,15개주장과미완료범위 |
| [21·22 문헌·버전 검수](verification/history-014.md) | 12개 주장·FSA 선택5쪽·코드/버전/초기 지침 대조, 전논문과 재현 미완료 범위 |
| [24·25 저장 예측 검수](verification/history-017.md) | 972개 저장 검사·20개 오류 사본·30개 H5 확인과 중간 입력·가중치 접근 공백 |
| [앞으로의 팀 진행 기록](../progress/README.md) | 실험·회의 기록 양식 |

색인은 현재 정리한 범위만 담습니다. 검색 결과가 없다고 과거 시도가 없다고 판단하면 안 됩니다. 파일·기록 번호·실험·재분석을 구분하며, 초기·부정·문헌·캐시 재분석·미실행 사례를 이어서 확인합니다. 이 아카이브는 팀의 최종 모델 선정 결과가 아닙니다.

전체 목록은 48,149항목이고 포함된 고유 파일 내용은16,326개입니다. 이는 연구 시도 수가 아닙니다. 현재 45개 기록 페이지는 초기 진단·문헌·19/20의 cell ID와 잔차 target·21의 지정 종합·22의 접근 범위 및 후기633·635–642의 지정 기록을 담습니다. 기록21까지의 완료 호출 비용과23·25 §1의 조건부 공유 비용을 저장값과 대조했습니다.24·25 §2의 고정 recursive 진단도 연결했습니다.25 §3–4의 지정 문헌과 판단 경계를 연결했으며, 전체 후속 이력 통합은 미완료입니다. 05·15·17·21의 전체 통합, 실패·후속 연구를 포함한 전체 비용, 회귀 TabPFN 후속과 나머지 고유 자료는 미완료입니다. 전체 고유 연구 내용의 수와 본문 검토율도 미확정입니다. 검수된 묶음부터 PR로 반영하고 일부 병합을 전체 완료로 집계하지 않습니다.

[26·27 관측 상태별 손해](records/0026-0027-observable-states.md)는 실제 peak와 예측 당시 상태를 구별하고, 19개 상태·13개 방법에서 empirical 급증 이득과 Tab/HGB의 기간·cell 손해를 함께 정리합니다. [검수](verification/history-019.md)는 저장 결과를 대조했으며 새 학습은 없습니다.

[28 관계 차이·추정 불확실성](records/0028-mechanism-uncertainty.md)은 네 문헌의 정보·조건·비용과 당시 미채택 이유를 연결합니다. 예측 폭과 추정 불확실성, CLT 정리별 조건, residual 자기상관의 해석을 구별하며 [검수](verification/history-020.md)에 실제 읽은 범위를 남겼습니다.

[29–32 10분 자료·해상도 진단](records/0029-0032-resolution-diagnostic.md)은 0.6초 표시 정정, 같은3cell의 공유·분리 손해, 원 UPC Fig. 7의 cluster 축 정정을 보존합니다. [검수](verification/history-021.md)와 원자료를 함께 재사용할 수 있습니다.

[33–35 process 식별·고정 fit gap](records/0033-0035-process-fit-gap.md)은 일곱 K=4의 train 개선/validation 손해, 모델 크기와 계산 step, MSE 필요조건의 적용 범위와 UPC 그림 정정을 연결합니다. [검수](verification/history-022.md)와 저장 예측으로 같은 질문을 재확인할 수 있습니다.

[36–38 유한 학습·정보 반례](records/0036-0038-finite-information.md)는 정보량 예산과 예측 정보 포화, panel의 이질성·추정 오차, context의 oracle 한계·유한 추정량을 구분합니다. 네 개의 정확한 사례와 세 문헌의 지정 구간을 [검수](verification/history-023.md)했으며, 새 모델 실행 없이 재사용할 수 있습니다. 소속과 학습 sample 공유 범위의 재검토는 당시 다음 질문이며 새 후보 확정이 아닙니다.

[39–40 담당 소속과 sample 공유](records/0039-0040-sample-reuse.md)는 참 joint ratio의 목적 보존, 세 선행연구와 당시 미채택 이유, 조건부 분포·outlier 점수의 한계를 연결합니다. [검수](verification/history-024.md)에서 적분 예를 확인하고 pinned 코드의 최대 열별 처리 수를 원문 68G에서 289G로 정정했습니다. 실제 모델 호출 수나 실행 시간의 측정치는 아닙니다.

[41–42 cell별 손해·사후 선택](records/0041-0042-cell-harm.md)은 저장된 13개 조건의 cell·기간별 손해와 기존 여섯 경로의 oracle·validation 선택을 구분합니다. [검수](verification/history-025.md)는 21개 저장 validation checkpoint의 순서·손실과 비용을 연결했으며 새 모델 실행은 없습니다. 44의 수치 부분을 연결했으며 문헌·역할 종합은 아래 43–44 기록에서 이어집니다.

[43–44 예측기의 역할 변경](records/0043-0044-predictor-roles.md)은 TimeTic의 실제 학습 후 성능 label과 local distillation의 국소 설명·계수 군집화를 비교합니다. 당시 미채택을 성능 실험의 실패와 구분하고, 논문 수치·안정성 조건·고정 저자 코드·비용 경계를 연결했습니다. [검수](verification/history-026.md)의 범위는 선택 문헌 구간이며 전체 논문은 미완료이며, 45 이후 기록은 아래에서 이어집니다.

[45–46 공간 입력의 시간·모델 간 유지](records/0045-0046-input-stability.md)는 같은 32개 cell·두 주의 저장 예측에서 일부 긍정 cell, 첫 주 선택의 다음 주 이득/손해와 사후 oracle을 구분합니다. [검수](verification/history-027.md)는 당시 비용 스냅샷까지 연결했습니다. 47의 수치 부분을 반영했으며 문헌·논리·규모·종합은 [47 후속 기록](records/0047-input-sharing-roles.md)에 연결했습니다.

[47 입력 정보와 공동 학습의 구분](records/0047-input-sharing-roles.md)은 GECOS 입력 역할, DIC-ST·Markov boundary의 실제 근거 범위, 양방향 의존성의 논리 반례와 Tab 비교 작업량을 정리합니다. [검수](verification/history-028.md)는 당시 미추천 판단과 재검토 조건을 연결하며 전논문 완료나 새 성능 실험을 뜻하지 않습니다.

[48–49 합계와 개별 cell 복원](records/0048-0049-aggregation-recovery.md)은 미래 실제 합계·사후 최적 scalar·실행 가능한 과거 기준을 구별합니다. 평균 이득과16개cell손해, 정규화와원단위의차이, 당시비용을 [검수](verification/history-029.md)와 연결했습니다. 50의 문헌·신규성 종합은 후속 검수 범위입니다.

[50 합계·다중 출력·대표 예측 문헌](records/0050-aggregation-literature.md)은 HiGP·ONDM·HTS-Cluster의 실제 출력을 구분하고, 선행 대표 예측과 정확도·시간 절충을 당시 미채택 판단에 연결합니다. [H030 검수](verification/history-030.md)는35쪽 본문·21쪽 시각 열람과 선택128개 표 수치를 기록합니다.

[52·54 자료 적합성과 부분 관측 복원](records/0052-0054-partial-observation.md)은 Beijing의 스키마 한계와 Milan 4-cell 복원의 확대 기준 미통과를 정리합니다. 앞 구간의 이득, 후반·셀별 손해, 최초 검사 오류와 실패 비용까지 [H031 검수](verification/history-031.md)에 연결했습니다.

## 51·55 GOTSF의 목적과 재현 조건

[GOTSF 검토 기록](records/0051-0055-gotsf-audit.md)은 값 구간별 예측·zero-mask MAE의 분모·논문/코드 설정 차이를 연결합니다. 두 판본의 인쇄표 비교, 정책별 반례, 미해결 평균값 차이, 공개 beam 자료의 시간 간격과 notebook 실행 증거의 한계를 함께 확인할 수 있습니다. 51·55 전체 검토는 계속 진행 중입니다.

## 51·55 ITU·Cellular 예측 조건

[네트워크 예측 문헌 기록](records/0051-0055-network-forecasting.md)은 beam 단위·시간 분할·입력 가용성과 모의 통화 target을 구분합니다. ITU의 기준별 이득, Cellular의 금요일 악화 사례, 표/그림·개선율 불일치를 [H033 검수](verification/history-033.md)에 연결했습니다. 두 연구를 cell clustering이나 RCTL 이득의 증거로 확대하지 않습니다.

[51 Frontiers 희소 beam 공동 학습](records/0051-frontiers-beam-audit.md)은 zero 분류·회귀의 역할, week5 평가, 긴 입력의 반례와 표/본문 불일치를 연결합니다. [검수](verification/history-034.md)는27개 주장과88개 인쇄 지표를 확인했습니다.55의 event 원문은 여전히 미접근이며 전체 문헌 종합은 계속 진행합니다.

[53·55 학위논문 검토](records/0053-moghadas-thesis.md)는 일부 입력으로 군집 전체를 예측하는 기존 방법, 정확도 반례와 최초 클러스터링 비용을 연결합니다. 입력 약17% 사례와 결론의81%를 전체 비용 절감으로 섞지 않으며, [39개 주장 검수](verification/history-035.md)에 원문 설정·구성 수의 불일치도 남겼습니다. 다른 telemetry 문헌과53/55 전체 종합은 계속 진행합니다.

[53·55 SRSSS 관측 선택·현재값 복원](records/0053-srsss.md)은 주기적 전체 관측과 초기화 비용, 합성 전력 예산, 비교 기준별 오차를 연결합니다. [30개 주장 검수](verification/history-036.md)는 표36값·9쪽 본문과 수식의 재사용 조건을 확인했으며, 현재값 복원을 미래 트래픽 예측·RCTL 이득으로 확대하지 않습니다.

[53·55 Zoom2Net 복원 조건](records/0053-zoom2net.md)은 정밀 학습 자료·측정 제약·모호한 이력과 추가 보정 비용을 연결합니다. [32개 주장 검수](verification/history-037.md)는14쪽 본문/10쪽 시각 자료·runtime 표와 지표별 반례를 확인했으며, 그럴듯한 복원을 실제 정답 이력·미래 예측 이득으로 확대하지 않습니다.

[53·55 NETNOMOS의 규칙·예측·복원](records/0053-netnomos.md)은 데이터에서 규칙을 찾고 생성에 적용하는 방법을 세 과제별로 구분합니다. [39개 주장 검수](verification/history-038.md)는 sMAPE 반례·MAWI 위반0.3%·약5배 추론 비용·인쇄 수치 차이를 보존하며, 규칙 준수를 RCTL의 예측 이득으로 바꾸지 않습니다.

[53·55 TabICL imputation](records/0053-tabicl-imputation.md)은 공식 기능 예제와 실제 54 실험을 구별합니다. 완전한 context를 먼저 넣은 예제, 반복 대체·순열의 실제 비용, 과거/현재 문서 차이와 Ciena 원문 접근을 [32개 주장](verification/history-039.md)에 연결했습니다.

[Ciena 관측·전송·저장 비용](records/0053-ciena-telemetry.md)은 이전에 확보하지 못했던23쪽 원문을 검토한 후속 기록입니다. [36개 주장](verification/history-040.md)에 세 비용 단위, 압축·MAPE 표, 감소율과 비용 기간의 미확인 분모를 연결하며 이를 cell 선택·RCTL 미래 예측 성능으로 환산하지 않습니다.

[51·55 STK-Diff 생성 코드](records/0051-stkdiff-audit.md)는 기존 Beijing 스키마 검토에 그림4개·의존텍스트647줄을 연결합니다. [34개 주장 검수](verification/history-041.md)에서 station 분할, 기본 단일샘플 지표의 분모, 그림/코드 차이와 재현 공백을 확인할 수 있습니다. 미래 예측·clustering 성능 검증으로 확대하지 않습니다.

[51·55 event context와 합성 증강](records/0051-event-context.md)은 이전 접근 공백을 공식AAM44쪽 검토로 보완합니다. [40개 주장](verification/history-042.md)에 사전 일정·train 합성·MAPE식/날짜 불일치와 큰K·주거/업무별 반례를 연결했습니다. 전체 오차와 이벤트 오차를 구분하며 51·55 전체 종합은 계속 진행합니다.

H043 후속: [51·55 GOTSF 그림·애니메이션](records/0051-0055-gotsf-media.md)은 고정 미디어 7개와 144프레임의 실제 독해, 값 구간·확률 음영·분할 그림의 해석 한계를 연결합니다. [범위와 검수](verification/history-043.md)를 함께 확인하세요. 전체 51/55는 미완료입니다.
