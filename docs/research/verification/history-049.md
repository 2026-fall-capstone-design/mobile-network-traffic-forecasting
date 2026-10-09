# H049 검수 범위

[연구 기록](../records/0056-0058-sgd-as.md) · [25개 주장](history-049-claims.json) · [일차 대조](history-049-primary-check.json) · [설정·산술](../evidence/0056-0058-sgd-as/printed-settings-arithmetic.json)

SGD-as 7쪽 텍스트·시각 자료, 저장 p5 preview, TXT 992줄과 HTML의 보이는 본문/이력 137줄을 대조했다. TXT는 PAGE 표식과 공백을 제외하면 PDF 추출과 동일하다. 58 메모를 포함해 5묶음·10경로이며 새 보존 사본은 0개다. HTML 전체 소스나 인용/연결 자료 전체를 읽은 것은 아니다.

Table 1의 설정18개를 시각·추출 텍스트에 대조하고, 직접 후보 스캔을 가정한 n(n+1)/2를 정수로 검산했다. Figure 2–3의 7개 모델/자료 조합·14개 패널은 시각적으로 읽었지만 정밀 수치를 추출하지 않았다. 목적값은 학습 자료의 값이고 가로축은 Epoch다. 원 run·seed·통계 검정·test 품질·전처리 포함 wall time은 확인하지 못했다.

permutation의 불편성과 음의 공분산 조건, greedy 방향성과 자기 짝 경계, logistic/SVM의 부호·계수·활동 조건, 공통 정규화항, 고정 파라미터에서의 분산 비교를 대조했다. 내적 proxy는 일반 거리 함수가 아니며 실제 gradient 내적의 순위를 보장하지 않는다. 식5·8의 gradient 기호 누락과 식32의 log-likelihood 최소화 부호를 보완 사항으로 명시했다. 이 관찰을 저자 코드/실험 전체의 무효로 확대하지 않는다.

같은 에이전트의 원문·문서 2차 대조와 자동 byte/설정/링크 검사를 구분한다. 인용 정리 전체의 독립 검증·독립 과학적 재현·새 RCTL 실험이 아니다. 원 코드 import/실행·fit/inference/forward·난수 생성은 0이며 보호 원장6개를 보존했다. 저자 코드·원run·실제 설정·검색 비용·56/58 종합과 전체 Goal은 미완료다.
