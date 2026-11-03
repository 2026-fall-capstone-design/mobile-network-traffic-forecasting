# 저장 학습 경로와 조기 종료를 해석하는 기준

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

[원109 기록](../records/0139-saved-training-path-and-stopping.md) · [정적 학습 정의](../sources/history-139.md#src-0023202) · [진단 코드](../sources/history-139.md#src-0023204) · [공통 경로 결과](../sources/history-139.md#src-0032508)

원109에서 재사용한 것은 기존29개 로그다. 코드의 strict improvement와 patience10, 선택 checkpoint, 공통42/43epoch를 원본에 대조했다. 상한 절단의 증거가 없다는 판단과 optimizer 수렴/추가학습 효과/공정한 최적 설정의 증명은 구별한다.

online train loss는 배치 사이 가중치가 변하는 train mode 값이다. epoch 뒤 eval validation과의 차이는 고정 checkpoint의 과적합 크기를 뜻하지 않는다. global42와 K4모델11은 명목 epoch당 update 수이며 실제 step trace를 복구한 수가 아니다.

마지막 공통 epoch·마지막5개 평균·서로 다른 best checkpoint의 평균은 다른 비교다. 유리한 epoch를 고르거나 종료 뒤 값을 채워 독립 성능을 만들지 않는다. 새 연구에는 바뀌는 소속/입력/학습·종료 조건과 독립평가를 먼저 적고, 기존 조건의 반복 여부를 확인한다.

before/after 원장과 실행 marker는 당시 판본의 증거다. 다음 기록 디렉터리의 원장 백업을 읽은 것이 그 다음 실험의 본문 검토나 실행 완료는 아니다. 새 모델 실행은 이 아카이브의 범위에 포함되지 않는다.
