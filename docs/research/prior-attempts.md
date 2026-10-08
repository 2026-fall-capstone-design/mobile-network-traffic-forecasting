# 문제별 과거 시도 색인

현재는 첫 시범 묶음의 색인이다. 여기에 없다는 이유로 과거 시도가 없다고 판단하면 안 된다. 전체 고유 기록 검토를 계속하고 있다.

| 찾으려는 문제·별칭 | 확인한 기록과 조건 | 결과·주의할 해석 | 재사용·새 실험의 차이 |
|---|---|---|---|
| bounded relation graph, UPC 소속 수정, `save()`의 `p` 충돌, `meter.json` PermissionError | [635–637](records/0635-0637-execution-recovery.md), cohort A 16cell·K4·504행 context·64 query·seed 20260925 | 구현 오류와 부분 복구다. 방법의 실증 기각으로 쓰지 않음 | 완료 14cell 분위수와 79쌍 분류 출력 보존. 같은 조건은 cache부터 확인 |
| float32/float64, 2→22 edge, 혼합 중앙값 root 잔차, Tab이 UPC를 유지함 | [638](records/0638-numeric-precision.md), 같은 예측·같은 지원/이동 규칙 | 정밀도 정정 후 Tab 3cell/HGB 1cell 이동. graph 목적 감소이며 RCTL 성능 판단은 별도 | 저장 결과만으로 수치 대조 가능. threshold·기간·모델 변경은 별도 실험 |
| relation 소속의 실제 RCTL 효용, HGB_free, 정규화·raw MAE, 평균과 전반 손해 | [639](records/0639-rctl-bridge.md), A 16cell·K4·개발 480시점·seed 20260925 | UPC 대비 정규화 −3.97%. HGB_free 대비 전체 −1.93%지만 전반 +2.71%, 원척도 전체 +6.58% | 13평가 자리 재사용·고유 원예측 10개·새 학습 3group. 같은 저장값 검산 가능 |
| Tab_path와 HGB_relation이 다른 실험인가, cell index 재사용 | [639의 출처 경로](records/0639-rctl-bridge.md), 306/325/367/388/563/581 → 639 | 367 Tab_path와 639 HGB_relation 소속 동일. 이름·인덱스만으로 새 결과나 같은 cell로 판단하지 않음 | 실제 ID·정답·시간·protocol·파일 hash를 함께 확인. 상위 기록 전체 검토는 진행 중 |

새 실험은 관련 과거 기록, 같게 유지할 조건, 달라지는 질문·조건, 재사용할 파일을 먼저 적는다. 기존 부정 결과를 회피하기 위한 조건 변경과 새로운 가설 검증을 구분한다. [첫 묶음 검수](verification/pilot-001.md), [RCTL 검수](verification/pilot-002.md), [전체 조사 현황](verification/inventory-2026-10-08.md).
