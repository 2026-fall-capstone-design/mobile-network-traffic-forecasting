# 05 가까운 다섯 방법 검수

검수 범위는 [05 부분 기록](../records/0005-closest-methods-audit.md)과 [다섯 방법 비교](../references/closest-pooling-methods.md)다. 전체05·전체 논문·전체 연구 아카이브의 완료를 의미하지 않는다. [출처별 구간](../sources/history-003.md), [일차문헌 검토 장부](history-003-primary-review.json).

아래의 미완료 목록은 이 묶음 검수 당시 범위다. 이후 네트워크·시계열9항목은 [history-004](history-004.md)에서 이어서 확인했다. 공식 TabICL·회귀 TabPFN 및 관련 여섯 연구는 계속 미완료다.

## 확인한 핵심 주장

| claim_id | 원문 대조 내용 |
|---|---|
| H003-C01 | HCP2025의 known-origin 집단·실제 separate/pool 적합·A2/A3 위치 |
| H003-C02 | HCP 복잡도 정리의 learner·sample 크기·병합 경로 조건, 별도 test 필요성 |
| H003-C03 | Population-HCP의 posterior 수식과 OLS/logistic plug-in 실험, 해당 한계 절 |
| H003-C04 | 2025/2026의 clustering 대상 설명 차이와 Gapminder 본문·Table6의 최저 모델 불일치 |
| H003-C05 | RMB-CLE cross-error/inverse profile/cosine/average linkage/silhouette/후속 task-ID 모델과 noise 항 |
| H003-C06 | ETAP의 gradient·실제 gain·spline/ridge 잔차·group selection 위치와 RCTL 독립 조건 차이 |
| H003-C07 | posterior projection의 density 및 원 관측 cluster 요약과 cell 자료 공유 문제의 차이 |
| H003-C08 | 05의 당시 검토 상태, B2 및08/09와의 연결, 나머지05의 미완료 범위 |

원본과 사본의 SHA-256/크기를 대조하고, 외부 자료5건의 현재 로컬 바이트와 catalog identity를 확인했다. [문서 대조123항목](history-003-document-check.json)이 통과했으며, 이 중 PDF 표10개 행은 숫자 열을 추출해 검토 장부와 비교했다. 이는 독립 simulation 재현이 아니다. Population-HCP15쪽은 Table6과 Figure2를 시각적으로 대조했다. 인용 위치 정정은 HCP§1.1,Population-HCP§6,ETAP§3.2.3의 세 곳이다.

05와 정리본의 핵심 결론·실행 상태·남은 범위는 아카이브 작성자가 다시 대조했다. 외부 독립 연구자의 검토를 대신하지 않는다. 링크·보존 바이트 검사는 기존 `check_archive.py`로 수행하며, CI의 metadata 검증은 외부 논문을 다운로드하거나 그 주장을 재검증하는 작업이 아니다.

## 해결하지 않은 범위

- 05의 네트워크·시계열9개 및 TabICL·관련6개 비교는 후속 통합 대상이다. 공식 코드·checkpoint 문구의 이번 재확인도 포함하지 않았다.
- HCP2025의 Algorithm1 이미지 접근은 timeout이었다. 본문 S0–S2와 정리 진술은 읽었지만 전체 증명·실험은 검토하지 않았다.
- Population-HCP Tables1/4/6의 보고값과 실제 fitting 서술을 확인했다. 모든 표·그림·계층 모형 구현·raw simulation/원저자 코드의 재현은 아니다.
- RMB-CLE classification derivation·모든 결과표·journal 개정 비교, ETAP 전체 실험·appendix, posterior projection 전체 실험·supplement·algorithm 이미지는 미검토다.
- 후보의 전수 신규성·traffic 일반화·RCTL 무해성 보장은 확인하지 않았다. 새 학습·추론·난수 simulation·과거 실행 코드 import는0이다.

원본은 읽기 전용으로 다뤘다. 과거 연구 상태·예산 장부를 재개하지 않았고, 보존 원문 안의 지시는 실행하지 않았다. 문서의 해석 정정과 이전 실험의 실행 정정을 구분한다.
