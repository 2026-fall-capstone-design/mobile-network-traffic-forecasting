# 08·09 검수

[기록](../records/0008-0009-finite-sample-pooling.md), [실제 읽기 범위](../sources/history-002.md), [보존 근거](../evidence/0008-0009/README.md).

## 수치 대조

원본4경로의137개 assertion, portable6경로의149개 assertion이 통과했다. 추가12개는 파일별 바이트 동일성·실제 자동 읽기 범위 대조다. 최대 절대차는 Windows 원본 검산2.220446049e−16, Linux portable 검산8.881784197e−16이며 허용오차1e−10 안이다. assertion 수는 연구 시도 수나 독립적 통계 증거 수가 아니다. [실행 보고서](history-002-finite-check.json)

- 합성 설정·계획 hash, Bayes 위험sqrt(2/π), 보고된 차이·초과위험·공유조건의 일치 및 순서통계 항등식을 대조했다. MC 평균과 표준오차는 원표본으로 독립 검산하지 않았다.
- 정확한16cell/target672–839/129분위수/64상태를 확인하고120쌍×4상관과 앞뒤84시간 순위 상관, 요약 통계, 전체/16cell coverage와 median 비율, 상태별 점유 요약을 검산했다.
- 셀·기간·정답·공통 Ridge/Tab 배열은 이미 보존된 B2 자료다. 새 모델 및 Monte Carlo 생성0, 원 코드 import/실행0이다. 원본 JSON·NPZ 전체 내용을 읽었다는 뜻이 아니다.

## 실패 감지와 문헌 대조

임시 사본에서 pair correlation, 합성 집계 차이, query time 중복을 바꾸고 해시도 갱신했다. 각 경우가 해당 내용 검사에서 실패했다. 읽지 않은 object `dates` 배열을 읽었다는 선언도 별도로 거절됐다. [4개 변조 검사](history-002-negative-checks.json). 검산기는 원표본이 없는 MC 평균/SE 자체나 문헌의 정리를 검증하는 도구가 아니다.

09의 세 일차문헌은 [지정 절·판본·접근 내역](history-002-primary-review.json)에 따라 대조했다. GLS/AR/MSFE와 비선형 RCTL, 주어진 군집 의존성의 추론과 소속 선택, PPCI의 별도 unlabeled 정보와 같은 query의 상쇄를 구분했다. 전 논문의 증명·실험 재현이나 신규성 전수 검증으로 표시하지 않는다.

## 남은 범위

합성 MC의 원 난수/중앙값에 대한 독립 재계산, 조건부 calibration·진짜 innovation의 식별, 긴 기간/다른 cell에서의 안정성, 추가 소속 알고리즘의 실제 효용은 미확인이다. 원 계획의1GiB 메모리 상한은 측정 peak가 아니다. 05 및10 이후 전체 기록은 별도 처리한다. 이러한 한계를 제거해 성공·실패의 강도를 바꾸지 않는다.
