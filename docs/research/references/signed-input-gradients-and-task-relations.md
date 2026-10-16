# 입력 미분·task 관계·사전 소속 결정

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

[원114 기록](../records/0143-signed-input-gradients-and-task-relations.md) · [출처](../sources/history-143.md) · [원76 반응 전달](../records/0076-response-transfer-audit.md) · [원78 Task2Vec](../records/0080-task2vec-task-and-output-sharing.md)

[Bai·Zhao, KDD2022](https://arxiv.org/abs/2207.01117)의 SRDML은 공유 표현과 task별head·관계 가중치를 함께 학습한다. [고정 합성 코드](https://github.com/BaiTheBest/SRDML/blob/b65d6da39a2f92491f0982790a9bd3a3e2d5b9bf/synthetic_train.py#L114-L143)는 부호와 크기를 유지한 출력 gradient 차이의 L1 norm을 사용한다. [CIFAR 코드](https://github.com/BaiTheBest/SRDML/blob/b65d6da39a2f92491f0982790a9bd3a3e2d5b9bf/train.py#L76-L123)는 feature map gradient의 공간 합을 비교한다. 일반적인 raw 입력 미분, loss의 parameter gradient, sign만의 비교와 구별한다.

정리1의 전역 등식·함수 기준값·정의역 조건과 일부 query의 근접성을 합치지 않는다. 저자본 A.2의 정리2 증명 링크는 미완성 표기가 남아 있어 소장 판본의 완전한 증명 확인을 주장하지 않는다. 논문과 demo의 합성 sample/base설정도 다르다.

고정 TabICLv2 probe의 반응이 같은 RCTL 함수로 함께 학습하기 좋은 소속을 나타내는지는 별도 질문이다. 점 예측 정확도에서 미분 정확도·좌표 비교 가능성·공유 학습 이득을 도출하지 않는다. 원114는 이 원리를 새 추천안으로 채택하지 않았으며 원115의 task grouping 상세 검토는 후속 범위다.
