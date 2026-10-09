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
| [16–17 저장 진단 검수](verification/history-010.md) | 32cell·4주·768fit 보고와 저장 수치, H5 입력·정답, 평균 및 cell/day 반례. 세 문헌 검수는 미완료 |
| [앞으로의 팀 진행 기록](../progress/README.md) | 실험·회의 기록 양식 |

색인은 현재 정리한 범위만 담습니다. 검색 결과가 없다고 과거 시도가 없다고 판단하면 안 됩니다. 파일·기록 번호·실험·재분석을 구분하며, 초기·부정·문헌·캐시 재분석·미실행 사례를 이어서 확인합니다. 이 아카이브는 팀의 최종 모델 선정 결과가 아닙니다.

전체 목록은 48,149항목이고 포함된 고유 파일 내용은 16,326개입니다. 이는 연구 시도 수가 아닙니다. 현재 열아홉 기록 페이지에는 05의 부분 정리 네 페이지와 15의 일부를 담은 두 페이지, 17의 수치 부분이 포함됩니다. 13/14와 16/17의 저장 진단 및 15의 여섯 문헌 지정 방법을 대조했습니다. 17의 세 문헌·공간 정보 후속 이력·회귀 TabPFN·15의 누적 비용·05의 남은 판단과 이후 기록을 계속 확인합니다. 05·15·17 전체 완료와 전논문 검토 완료는 집계하지 않았습니다. 전체 고유 연구 내용의 수와 본문 검토율도 미확정입니다. 검수가 끝난 묶음부터 PR로 반영하고, 원격 반영과 전체 정리 완료를 구분합니다.
