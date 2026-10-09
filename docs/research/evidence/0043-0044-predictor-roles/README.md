# 43–44 문헌·역할 검토의 근거와 재사용

[연구 기록](../../records/0043-0044-predictor-roles.md) · [출처](../../sources/history-026.md) · [검수](../../verification/history-026.md)

`originals/`에는 계획·다운로드 코드·입수 manifest·시작 표시·repository metadata 5개를 원 바이트 그대로 보존했다. 44는 [앞 묶음의 원본](../0041-0042-cell-harm/originals/SRC-0021588.md.txt)을 재사용한다. 원 코드의 실행 지시는 역사자료다.

[manifest](manifest.json)의 25개 항목은 보존 6·선택 문헌/코드 metadata 10·identity만 확인한 사본 9개다. 문헌과 저자 코드는 정식 판본·고정 커밋 링크로 열 수 있다. 네 코드 파일은 당시 보존본과 공개 GitHub의 고정 blob이 같음을 확인했다. 나머지 저자 저장소 전체와 의존성까지 재현한 것은 아니다.

[document-tables.json](document-tables.json)은 논문 mean 행 6개, 모의 결과 Table 2의 선택 행 7개, 100×157 재적합 규모, 입수 수량과 정확한 두 점 반례를 담는다. 표는 논문 보고의 전사이고 우리 트래픽 예측 결과가 아니다. 반례는 조건화 대상의 차이에 관한 유리수 계산이며 새 성능 실험이 아니다.

재사용할 때는 TimeTic의 실제 fine-tuned label·activation 비용, local distillation의 OOF·teacher anchor·μ gate·고정 locality와 lasso 안정성 조건을 함께 가져와야 한다. zero-shot/TabPFN만 바꾸거나 계수에 clustering이라는 이름을 붙여 기존 시도와 다른 연구로 세지 않는다. 실제로 달라지는 관측·학습 행동·평가 조건은 [과거 시도 색인](../../prior-attempts.md)에 연결한다.
