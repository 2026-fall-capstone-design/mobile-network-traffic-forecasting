# 문제별 과거 시도 색인

현재는 첫 시범 묶음의 색인이다. 여기에 없다는 이유로 과거 시도가 없다고 판단하면 안 된다. 전체 고유 기록 검토를 계속하고 있다.

| 찾으려는 문제·별칭 | 확인한 기록과 조건 | 결과·주의할 해석 | 재사용·새 실험의 차이 |
|---|---|---|---|
| Milan 가공 자료, 첫 CPU 실행, smoke, 날짜·시간 분할, Ridge 잔차 상관 | [01–02](records/0001-0002-initial-design.md), 32cell 진단·4cell smoke·256context행/64query행·seed20260925 | 저장 Tab 예측·오차 검산. 작은 직접 예측은 clustering 효용이 아님. H5 마지막 날짜2014-01-01, 정규화와 미래 target 범위 구분 | 13개 작은 원본/배열과 H5·checkpoint 해시/주소. 같은 동작 확인을 새 방법 실험으로 반복하지 않음 |
| conditional MAE curve, risk table, Bayes loss, 129quantiles, balanced merging, residual correlation | [02의 초기 후보 설계](records/0001-0002-initial-design.md), 16cell·K4·504context·64상태·257action 계획 | 이상적 공통 예측 비용이며 pooled Tab/RCTL 보장 아님. 원 UPC 조건을 임의 완화하지 않음. 후속03–09 실행 검토 대기 | 처음 정한 비교군·기각 조건·예산과 가중합 오차 척도를 먼저 확인. 새 기간·양자화·비용·모델의 차이 명시 |
| bounded relation graph, UPC 소속 수정, `save()`의 `p` 충돌, `meter.json` PermissionError | [635–637](records/0635-0637-execution-recovery.md), cohort A 16cell·K4·504행 context·64 query·seed 20260925 | 구현 오류와 부분 복구다. 방법의 실증 기각으로 쓰지 않음 | 완료 14cell 분위수와 79쌍 분류 출력 보존. 같은 조건은 cache부터 확인 |
| float32/float64, 2→22 edge, 혼합 중앙값 root 잔차, Tab이 UPC를 유지함 | [638](records/0638-numeric-precision.md), 같은 예측·같은 지원/이동 규칙 | 정밀도 정정 후 Tab 3cell/HGB 1cell 이동. graph 목적 감소이며 RCTL 성능 판단은 별도 | 저장 결과만으로 수치 대조 가능. threshold·기간·모델 변경은 별도 실험 |
| relation 소속의 실제 RCTL 효용, HGB_free, 정규화·raw MAE, 평균과 전반 손해 | [639](records/0639-rctl-bridge.md), A 16cell·K4·개발 480시점·seed 20260925 | UPC 대비 정규화 −3.97%. HGB_free 대비 전체 −1.93%지만 전반 +2.71%, 원척도 전체 +6.58% | 13평가 자리 재사용·고유 원예측 10개·새 학습 3group. 같은 저장값 검산 가능 |
| Tab_path와 HGB_relation이 다른 실험인가, cell index 재사용 | [639의 출처 경로](records/0639-rctl-bridge.md), 306/325/367/388/563/581 → 639 | 367 Tab_path와 639 HGB_relation 소속 동일. 이름·인덱스만으로 새 결과나 같은 cell로 판단하지 않음 | 실제 ID·정답·시간·protocol·파일 hash를 함께 확인. 상위 기록 전체 검토는 진행 중 |
| 조건부 분위수 clustering, 함수 거리, no-refit, post-grouping의 신규성 | [640](records/0640-contribution-boundary.md), [가까운 선행 비교](references/conditional-clustering.md) | 이 요소들은 비교한 기존 방법에도 있음. 지정 절 검토이며 전수 신규성 조사나 전체 재현은 아님 | 공식 논문 링크·판본·수식·읽은 쪽수부터 확인. 논문 확보를 전체 검토로 세지 않음 |
| bounded score와 CQTE, 잡음/입력 빈도 제거, 실제 Y의 추가 판단 | [640](records/0640-contribution-boundary.md), 512/634식·635구현 | 정확한 재가중 관계와 조건부 기대값은 확인. 유한 traffic에서 p 일치·잡음 제거·MAE 보장은 미확정 | 같은 출력에서의 대조는 [641](records/0641-cached-score-controls.md)로 연결. 선행 전체 재현은 아님 |
| 같은 예측인데 다른 소속, 중앙값 거리, plug-in conflict, RCTL 재학습 필요 여부 | [641](records/0641-cached-score-controls.md), A16cell·14cache·64query·22edge·K4·같은 이동 규칙 | 네 대조 모두 UPC 유지. 기존 관측 Y 점수는 Tab3/HGB1cell 이동. 한 개발 조건의 사후 비교이며 HGB_free 반례 유지 | 16평가 자리는 기존 UPC4파일 재사용. 새 모델·MAE 계산0. 보존 산술 검산부터 확인하고 새 조건을 명시 |
| 연구 완료 선언, 연구 방향 추천, 원 UPC θ=10, 최소44cell, 아직 안 한 본실험 | [642](records/0642-research-direction.md), 20261004 최종 보고서·7쪽 Word | 완료는 착수 근거와 문서 범위. 독립 기간/도시·같은 wall-time·TabPFN·graph 크기 통제는 미실행. 44cell은 네 유효 seed 그룹의 필요조건 | 기존635–641을 다시 실행하기 전에 저장 근거를 확인. 정규화 이득과 원척도 HGB_free 손해를 함께 기록하고 새 조건을 고정 |

새 실험은 관련 과거 기록, 같게 유지할 조건, 달라지는 질문·조건, 재사용할 파일을 먼저 적는다. 기존 부정 결과를 회피하기 위한 조건 변경과 새로운 가설 검증을 구분한다. [첫 묶음 검수](verification/pilot-001.md), [RCTL 검수](verification/pilot-002.md), [문헌 검수](verification/pilot-003.md), [캐시 대조 검수](verification/pilot-004.md), [전체 조사 현황](verification/inventory-2026-10-08.md).
