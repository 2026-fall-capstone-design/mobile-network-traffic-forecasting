# history-006 검수 — 관련 여섯 연구

[기록05](../records/0005-related-foundations-audit.md)와 [방법 비교](../references/related-tabular-clustering.md)를 지정 일차자료에 대조했다. 같은 에이전트의 별도 원문 대조이며 독립 연구자의 과학적 검증을 뜻하지 않는다.

| 확인 | 범위 |
|---|---|
| 판본·identity | Localized/TL-ANDI/CRUMB/Entangled/Amortized의 v1, TabClustPFN의 v3. 텍스트6개·PDF6개를 목록과 현재 원본 해시로 연결 |
| 실제 열람 | [줄·페이지별 범위](../sources/history-006.md). PDF 지정 내용17쪽; 전논문 완독0편으로 유지 |
| 주장 | [H006-C01–C09](history-006-primary-review.json)의 방법·정보·가정·비용·역사적 적용 범위 |
| 논문 보고 수치 | PDF와 대조한5개 표21행. 원실험 출력 재현과 구분 |
| 프로젝트 실행 연결 | 05 원문69행 및 기존B1/B2 검수 재사용. 논문 존재를 프로젝트 실행 완료로 바꾸지 않음 |
| 원문 보존 | 기존 보존 사본1개 재사용, 새 사본0. 논문은 metadata/공식 링크만 게시 |
| 새 연구 실행 | 모델·시뮬레이션0. 과거 연구 코드 import/실행 없음 |

[문서 검사](history-006-document-check.json)는 identity·정확한 사본·범위 경계·표 전사·공개 파일 해시·기존 상태/예산 원장 보존을 확인한다. 자동 검사 수는 과학적 주장 수가 아니다. 저장소 아카이브 CI는 로컬 근거와 링크를 검사하며 외부 논문을 다시 내려받거나 모델을 실행하지 않는다.

원문 대조에서 다음 한계를 유지했다.

- Localized의 shared cache는 같은 context 조건이다. 분류 미세조정의 효과를 frozen 회귀로 옮기지 않으며 k128의 속도 악화도 남겼다.
- TL-ANDI는 source label 증류와 target 잔차 보정·validation 후보 선택을 포함한다. no-negative-transfer 정리의 양의 오차항과 명시 가정, 실험의 선택 후 refit을 구분했다.
- CRUMB는 X 기반 query clustering과 배치 context 선택이다. 모든 cell의 내부 cache 교환, 세 backbone 모두의 회귀 우위, kNN과의 통계적 동등성을 주장하지 않았다.
- Entangled는 ridge 가정의 이론, S 추정이 필요한 개입, semi-synthetic 결과다. CSR 감소와 RMSE 악화를 함께 보존하고 실제자료 부분의 cell-type 기준도 적었다.
- TabClustPFN은 encoder 초기화 뒤 전체 가중치를 학습하며 K1을 제외한다. Amortized TS는 별도 합성 학습·모든 쌍의 affinity·graph 후처리를 포함한다.

여섯 논문의 저자 코드·원출력·전체 증명·모든 그림·다른 개정본은 미검토다. 현재 checkpoint 배포 여부나 전체 연구의 특정 모델 미실행을 전수 판정하지 않았다. 05의 회귀 TabPFN 후속과 이후 연구 연결을 포함해 전체 Goal은 계속된다.
