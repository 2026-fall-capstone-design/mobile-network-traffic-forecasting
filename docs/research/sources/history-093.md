# CCM 코드 저장본과 읽은 범위

[기록](../records/0093-ccm-code-review.md) · [목록](../catalog/history-093-sources.jsonl) · [명세](../evidence/0093-ccm-code/manifest.json) · [검수](../verification/history-093.md)

원소장 코드4개 전체1,021행과 commit/tree JSON2개 전체 키를 처음 읽었다. 작성 후에는 [8묶음 대조](../verification/history-093-second-pass.json)의 실제 구간을 다시 읽었다. 전체 모든 원문2회독, 독립 연구자 검토, 환경 구축이나 실행 재현으로 세지 않는다.

| source_id | 원소장 파일명 | 행수 | 팀 접근 | SHA-256 |
|---|---|---:|---|---|
| `SRC-0062856` | `ccm__exp__exp_ccm.py` | 379 | [고정 판본](https://github.com/Graph-and-Geometric-Learning/TimeSeriesCCM/blob/e4769baa7f8457358eb9b4614af2de1fbfba2257/exp/exp_ccm.py) | `f6b4f9c50302f57250a95922549b4cf12c33512d0271dda035e656b3281335c6` |
| `SRC-0062857` | `ccm__models__Dlinear.py` | 100 | [고정 판본](https://github.com/Graph-and-Geometric-Learning/TimeSeriesCCM/blob/e4769baa7f8457358eb9b4614af2de1fbfba2257/models/Dlinear.py) | `a7ba728c836256da9566e42d5dfe770c99c06f67fe4ea60af432f5b1543b1cb4` |
| `SRC-0062858` | `ccm__models__attention.py` | 149 | [고정 판본](https://github.com/Graph-and-Geometric-Learning/TimeSeriesCCM/blob/e4769baa7f8457358eb9b4614af2de1fbfba2257/models/attention.py) | `5273bb3e96a8e96fde364e75343bf342f5ead4ecd01deb9a0031471da3f2fbc5` |
| `SRC-0062859` | `ccm__models__layers.py` | 393 | [고정 판본](https://github.com/Graph-and-Geometric-Learning/TimeSeriesCCM/blob/e4769baa7f8457358eb9b4614af2de1fbfba2257/models/layers.py) | `db59d0ef411c5145afb131cc4f23ab36a037743bc47376dd344eadc78384585e` |
| `SRC-0062860` | `ccm_commit.json` | 1 | [고정 판본](https://github.com/Graph-and-Geometric-Learning/TimeSeriesCCM/commit/e4769baa7f8457358eb9b4614af2de1fbfba2257) | `8fe88d4023a0a3760149234cf937b6ca7a49fe8e13dcf4650638442fabbfdb74` |
| `SRC-0062861` | `ccm_tree.json` | 1 | [고정 판본](https://github.com/Graph-and-Geometric-Learning/TimeSeriesCCM/tree/e4769baa7f8457358eb9b4614af2de1fbfba2257) | `8fb6eabbfcb45f3ddfe7db9b2f0dae91a0417c0449603b0403cb5572b1f25808` |

원본 루트 별칭은 `Tab-ICL`이며 정확 상대경로와12사본은 명세/보존 확인에 있다. 외부 코드 전체를 재게시하지 않고 고정 commit의 공식 링크·해시와 검토 결과를 제공한다. Git tree의 나머지 항목은 본문 독해 완료가 아니다.

보충 [models/patch_layer.py](https://github.com/Graph-and-Geometric-Learning/TimeSeriesCCM/blob/e4769baa7f8457358eb9b4614af2de1fbfba2257/models/patch_layer.py)는 동일 commit에서 새로 확인한376행이다. SHA-256 `0f6b9a1cb557675f56712f7fa7d29240d5985f8a9b86f97d47fc06e3cd4d2288`, Git blob `0d2c00a4a6afb52b054954f359a8304668ed6c07`이며, 원목록 독해 수에는0을 추가한다. 공개이름과 Cluster_wise_linear 경로를 확인하기 위한 범위다. 첫독해 전체와 작성후1–84/193–267/271–368행 재대조를 구분한다.

기존 [원81 보존본](../evidence/0090-input-partition/originals/SRC-0022042.md.txt)의15–103행과 [CCM 논문](../records/0092-ccm-source-review.md)의 방법·부록 구간을 재참조했다. 새 본문 가산은4개, 전체JSON 가산은2개다. 새 모델 실행은0이다.

실제 entrypoint·자료 loader·utils·다른 모델과 설정/환경/seed별 결과·M4/Stock 실행 경로, 원81 잔여15그룹 및 snapshot23 연혁 고유 변경분은 별도 검토 대상이다.
