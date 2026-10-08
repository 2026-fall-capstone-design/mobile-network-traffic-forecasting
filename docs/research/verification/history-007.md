# 10–12 모집단·UPC 진단 검수

[연구 기록](../records/0010-0012-population-upc-stability.md), [원문 안내](../sources/history-007.md), [보존 근거](../evidence/0010-0012/README.md)를 대조했다. 같은 정리 에이전트의 두 번째 대조이며 독립 연구자의 과학적 검증은 아니다.

## 저장 결과와 문헌을 구분한 확인

- 계획·판단3개와 코드2개를 전부 읽었다. 두 JSON은 전체 키를 확인했다. 결과의 계획 SHA는 일치하지만 실행 전 봉인의 독립 증거는 아니다.
- [공유 가능한 검산 도구](../../../scripts/research_archive/verify_population_upc_history.py)의 [562개 검사](history-007-arithmetic.json)가 통과했다. population12배열의 지정 집계, pilot16ID, UPC24개 소속 벡터와12개 기간/12개 순서 비교를 검산하고, 필수 신규 보존 원문9개의 ID 목록을 확인한다. ARI는 분할표의 조합식, label 일치는 K≤5의 모든 순열로 확인했다. 원 코드의 sklearn/scipy 함수나 clustering을 실행하지 않았다.
- 별도 로컬572개 확인에는 H5의 SHA·크기·shape·날짜와 원본 상태·예산6개 불변이 포함된다. 두 검사 수를 독립 연구 검증 횟수로 더하지 않는다. [로컬 자료 확인 범위](history-007-local-data-check.json).
- 잘못된 입력을 거부하는지도 확인했다. 평균 오차·ARI를 바꾸고 해시를 갱신한2개 사본과, 필수 보존 원문을 하나씩 목록에서 뺀9개 사본 모두 검산기가 거부했다. 원본이나 게시 근거는 변경하지 않았다.
- [주장·일차자료 대조](history-007-primary-review.json)는10개 핵심 주장과 적용 한계를 연결한다. 원 UPC PDF4·5쪽과 고정 GECOS 코드를 다시 확인했다. 공개 코드는 `idx % n_groups`로 초기화하며, 이 진단의 제한된 Algorithm1 해석과 동일하지 않다.
- K3·K4/weekday_sequence/첫 기간의 순서 일치100% 반례를 보존했다. 항상 순서에 민감하다고 쓰지 않는다. 기간 차이와 최종 예측 손해도 구분했다.
- 12의0.249초는 앞선08 진단이고,10/11은0.289·0.301초다. 모델/새 RCTL 세 번으로 중복 집계하지 않는다.

## 검수의 한계

저장 집계와 저장 배열이 맞는지 확인한 것이다. 원신호에서 weekday peak·동점·PCC·seed·greedy 배정을 다시 만든 독립 재현은 아니다. 동점45.99%, raw nonfinite/음수/zero 비율, 경과시간과 RSS는 저장 보고값이다. H5 날짜 검토를 전체 원자료나 upstream CDR 처리의 검증으로 확대하지 않는다.

원 UPC의 전체 재현·원 논문 예측 성능·TabICL 필요성·전체 도시 clustering의 기각은 검증하지 않았다. 이후13–15와 후속 수정 연결, 회귀 TabPFN 후속은 미완료다. 모델·새 clustering·새 난수 실행은0이다.

[본문·수치·출처 대조 결과](history-007-document-check.json)와 저장소 링크/해시 검사도 게시 전에 확인한다. CI의 archive-check는 portable 검산과 보존 링크/해시를 확인하며, 원 H5·외부 논문을 받아 원 연구를 실행하는 절차가 아니다.
