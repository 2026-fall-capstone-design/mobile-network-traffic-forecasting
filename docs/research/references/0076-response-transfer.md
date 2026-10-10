# 반응 전달과 상호작용 전달의 선행 근거

[76의 당시 판단](../records/0076-0079-learning-decisions.md#c04) · [전체 대조 기록](../records/0076-response-transfer-audit.md) · [수치 증거](../evidence/0076-response-transfer/README.md)

| 문헌 | 확인한 판본·위치 | 전달 대상 | 보존할 조건과 예외 |
|---|---|---|---|
| [Sobolev Training for Neural Networks](https://papers.neurips.cc/paper_files/paper/2017/hash/758a06618c69880a6cee5314ee42d52f-Abstract.html), Czarnecki 외, NIPS 2017 | 공식 10쪽, Eq.1–2/Fig.1–4/Table1 | 함수값과 입력 미분, 무작위 투영 | teacher 미분 접근·신뢰성, 저자료 Ackley의 예외, Atari의 모방 지표, full backprop 기준과의 격차 |
| [Knowledge Transfer with Jacobian Matching](https://proceedings.mlr.press/v80/srinivas18a.html), Srinivas·Fleuret, ICML 2018, PMLR80:4723–4731 | 공식 9쪽, Eq.1–10/Tables1–5 | 출력·attention map과 입력 Jacobian | 국소 전개, target 최대 loss와 평균 loss 차이, 깊은 층의 최적화 실패, 자료량에 따른 이득 반전 |
| [Selecting Feature Interactions for Generalized Additive Models by Distilling Foundation Models](https://arxiv.org/abs/2604.13332v1), Jia·Singh·Caruana·Lengerich, 2026-04-14 v1 | 20쪽, Algorithm1, main Tables1–3 및 AppendixA | 마스킹 예측으로 고른 변수 상호작용 | 실제 target으로 GAM 적합, 순위와 오차 구분, 42분류 TabICL 범위, 일부 본문/표 차이와 코드 판본 차이 |

입력 반응을 최종 loss로 전달하는 방법과 변수 조합을 선택하는 방법 모두 선행 사례가 있다. 이것만으로 별도 clustering의 필요성이 생기는 것은 아니다. 새 연구는 같은 teacher 정보를 쓰는 global 증류와 비교하여 어떤 공유 결정이 달라지는지 설명해야 한다. 현 검토는 최종 모델 선정이나 모든 증류 방법의 기각이 아니다.

## 저장 코드와 논문 표를 연결할 때

[저장 커밋](https://github.com/Clouddelta/tab-distill/commit/64214da0edf7eef6e8bf645332471d78b30345e8)은 4월 논문 이후의 9월 판본이다. 삭제 이력에 PMLB 결과·순위·집계 코드가 남아 있으며 Table1의 18개 반올림 순위와 연결된다. PyGAM의 task 수 26과 나머지 방법의 27, SVD 실패 제외, 버전 없는 TabPFN 행명을 보존한다. 현재 코드의 v3 기본값을 과거 저장 결과의 실제 실행 버전으로 채우지 않는다.

Table2의 F1/variance 예외, Table3의 자기 기준 overlap, Fiat의 위치 변수·반복 조합·4변수 항·RMSE 차이는 [상세 기록 C25–C34](../records/0076-response-transfer-audit.md#c25)에 구분했다. 집계 방법 또는 실행 판본이 확인되지 않은 차이는 원인 미확인으로 남긴다.

## 검색 요약에서 생기는 차이

당시 DBLP 발췌의 Jacobian 페이지 4730–4738은 공식 PMLR 서지 4723–4731과 다르다. 위 서지는 공식 PMLR을 따른다. 일부 alphaXiv 요약의 포괄적인 우위 표현은 모든 표 조건과 일치하지 않으므로 공식 PDF 수치와 예외를 기준으로 읽는다. 검색 발췌에 있는 runtime density의 Jacobian 보정, 시간 미분, 파라미터 gradient를 입력 반응 증류와 같은 방법으로 묶지 않는다.
