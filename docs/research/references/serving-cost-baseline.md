# RCTL 비용 비교에서 먼저 고정할 기본 구현

[원95](../records/0125-frozen-rctl-serving-cost-baseline.md)가 2026-09-26에 보존된 checkpoint로 측정한16개 cell의 CPU 결과다. 같은 가중치를 사용하는 cell을 같은 시각에 batch로 처리하는 조건을 기본 비교에 포함한다. 이 구현의 이득을 Tab의 연구 기여로 세지 않는다.

| 보존 모델 | cell별 median(ms) | 묶음 median(ms) | 묶음 P10–P90(ms) | 시점당 예측 행 / 묶음 호출 |
|---|---:|---:|---:|---:|
| global K1 | 33.186 | 3.493 | 3.337–5.506 | 16 / 1 |
| Tab risk K4 | 33.865 | 14.005 | 12.236–15.399 | 16 / 4 |
| empirical K4 | 34.038 | 14.152 | 12.614–14.757 | 16 / 4 |

각 경로는12시점×3반복의36개 timing이다. 표는 시점당16개 cell을 모두 처리한 시간이지만 준비·로딩·온라인 전체 지연을 포함하지 않는다. P10–P90은 관측 분위수이며 독립 신뢰구간이 아니다. [저장 수치](../records/0125-frozen-rctl-serving-cost-baseline.md#claim-08), [메모리 범위](../records/0125-frozen-rctl-serving-cost-baseline.md#claim-13), [총횟수와 warm-up](../records/0125-frozen-rctl-serving-cost-baseline.md#claim-17), [비용의 포함 관계](../records/0125-frozen-rctl-serving-cost-baseline.md#claim-18)를 함께 확인한다.

비교 설계에는 저장 모델 수·상태 tensor/파일 bytes, 시점당 입력 행·호출/batch, 실제 타이머 범위·warm-up, Tab context/query·준비 비용, 기기·threads/dtype, 개발자료·새자료를 적는다. 입력 행을 그대로 두고 호출만 합쳤다면 생략한 예측 문제 수로 표시하지 않는다. 같은K4의 약0.147ms 차이는 Tab 우위의 근거가 아니며 다른 기기나10000개 cell에 선형 확대하지 않는다. 새로운 비용 기여는 이 기본 구현에서도 제거되는 실제 일과 조건을 명시한다. [재검토 기준](../records/0125-frozen-rctl-serving-cost-baseline.md#claim-27).

[원96의 병합 문헌 검토](../records/0126-rctl-parameter-merging-scope.md)는 원95 batch 기준을 이어받았다. 모델 저장량 감소, 입력 N행의 연산, 정렬/BN 준비와 과거 학습 비용을 분리한다. 여러 모델 출력을 섞는 방식은 cell당 지정 모델 하나를 실행하던 조건과 비교해야 한다.
