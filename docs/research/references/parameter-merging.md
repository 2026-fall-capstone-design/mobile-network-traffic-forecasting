# 출력 혼합·파라미터 병합·학습 공유를 구분하는 문헌 비교

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

[원96 기록](../records/0126-rctl-parameter-merging-scope.md)과 [실제 판독 범위](../sources/history-126.md)를 함께 사용한다. 아래는 당시 보존된 판본의 방법·조건이다. 현재 RCTL에서 재현한 성능표가 아니다.

| 자료와 확인 위치 | 실제 연산·정보 | 현재 연구에 남기는 조건 |
|---|---|---|
| [Model soups, ICML2022](https://proceedings.mlr.press/v162/wortsman22a.html), §2/Table2/Recipe1·§3.1·§5, PDF2–4/8–9 | 공통 pretrained에서 fine-tuning한 가중치 평균; greedy는 validation 성능으로 재료를 선택 | 같은 random seed로 처음부터 학습하는 RCTL과 구별. inference 비용 감소와 이미 수행한 여러 학습의 비용도 별개. 분류 성과가 RCTL 회귀의 보장은 아님. |
| [Git Re-Basin v4](https://arxiv.org/html/2209.04836v4), §3–5.4/Algorithm1·A.3–A.4, PDF3–8/21 | 학습된 hidden 좌표를 activation/weight/STE 방식으로 정렬한 뒤 interpolation | data-free weight matching도 학습된 모델은 읽음. CIFAR LayerNorm과 ImageNet BN 재계산을 구별. split-data 병합의 combined-data 비교를 유지하며 RCTL의 BN/LSTM·잔차 정렬은 미검증. |
| [TIMEFUSE, ICML2025](https://proceedings.mlr.press/v267/liu25cm.html), §3.1–3.2/Eq1–2/Algorithm1, PDF3–5 | 24개 입력 특징→단층 softmax fusor; validation 예측·정답/Huber로 학습; 여러 출력의 가중합 | 하나의 RCTL로 가중치를 압축한 방법이 아님. 기존 cell당 지정 모델 하나의 실행보다 싼지 별도 확인 필요. benchmark 수치 재현·Table2 모든 수치의 시각 검수는 없음. |
| [Probabilistic merging, UAI2026](https://proceedings.mlr.press/v337/bui26a.html), §2–5/Eq18–26/Algorithm1·A/B/C, PDF2–6/13–15 | 공통 pretrained task vector의 directional-residual energy와 반복 MAP mapping | 인쇄된 분모와 ηI/pseudoinverse 차이를 확인한 뒤 조건부 인용. 국소 가정·논문 실험의 bound를 RCTL global 보장으로 옮기지 않음. 공식 구현·정오표 감사는 남음. |

같은 함수라도 좌표별 파라미터 평균은 달라질 수 있다는 ReLU 예는 기호 설명이다. 실제 RCTL/SGD나 공통 초기화의 실패 실험이 아니다. BN folding은 고정된 함수 표현을 바꾸는 대안이며 비선형 병합 전체의 보장과 구별한다.

소속을 먼저 고정한 뒤 병합을 비교하는 학습은 검토할 수 있다. 자료가 함께 사용 가능하다면 union-data RCTL과 비교하고, Tab이 바꿀 새로운 결정 또는 같은 유용한 결정의 비용·추정 변동 개선을 명시한다. 모델 저장량·예측 입력 수·batch 호출·학습 처리량·정렬/BN 준비를 각각 기록한다. [원86](../records/0114-shared-training-scope.md), [원93](../records/0123-candidate-gates-comparison-scope.md), [원95](serving-cost-baseline.md)를 연결한다.

PDF104페이지 중 텍스트23페이지·관련 원 이미지6개를 실제 읽었다. 나머지81페이지 텍스트와 다른 시각 내용·literal TXT 전문은 미완료다. 이 범위 검토를 모든 병합 방법의 기각이나 현재 모델의 재현 성공으로 집계하지 않는다.
