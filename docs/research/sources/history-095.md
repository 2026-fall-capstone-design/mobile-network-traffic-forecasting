# DUET 코드 저장본과 확인 범위

[기록](../records/0095-duet-code-review.md) · [명세](../evidence/0095-duet-code/manifest.json) · [검수](../verification/history-095.md)

원소장 코드 4개 716행과 commit/tree JSON 2개 전체를 읽었다. tree의 1,085항목 독해와 참조된 파일 본문 독해는 구분한다. 보충 14파일 2,063행 및 PyTorch 2.4.1의 gumbel_softmax 60행을 읽었으며, 이 보충자료는 원목록 독해 수에 가산하지 않는다.

| source_id | 파일 | 행수 | 팀 접근 | SHA-256 |
|---|---|---:|---|---|
| `SRC-0062863` | `duet__ts_benchmark__baselines__duet__duet.py` | 68 | [고정 판본](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/duet.py) | `fc26a8d6d4b53d342219b33face13c551115aada57611fdbbfac7b582fc9b46b` |
| `SRC-0062864` | `duet__ts_benchmark__baselines__duet__layers__SelfAttention_Family.py` | 360 | [고정 판본](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/layers/SelfAttention_Family.py) | `cb1266e7aadee3da2040966029f08e5fe30d391d09f06600480e11e3938172db` |
| `SRC-0062865` | `duet__ts_benchmark__baselines__duet__models__duet_model.py` | 81 | [고정 판본](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/models/duet_model.py) | `840690b13fecdd08fdc4a602f3d700ede940731a29ad0fe1de7830b7bb9b22b7` |
| `SRC-0062866` | `duet__ts_benchmark__baselines__duet__utils__masked_attention.py` | 207 | [고정 판본](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/utils/masked_attention.py) | `edc17a01d813f6847d847b21ac53c9cb090af99e0b4d35c530d588f182bdb57c` |
| `SRC-0062867` | `duet_commit.json` | 1 | [고정 판본](https://github.com/decisionintelligence/DUET/commit/dcc6e6780a9138731b64b9b5398a94a1d97033f0) | `67eb7a31cb7ed0e95fb2ff8f7287d6052297166ad680bf7a31c402d5fdc33fb3` |
| `SRC-0062868` | `duet_tree.json` | 1 | [고정 판본](https://github.com/decisionintelligence/DUET/tree/dcc6e6780a9138731b64b9b5398a94a1d97033f0) | `bb295c6a168e515c30f21c9933a3a9ecee3c84e001ba2e4794307f563a075216` |

재참조 자료는 [원81 보존본](../evidence/0090-input-partition/originals/SRC-0022042.md.txt) 및 [DUET 논문·서지 출처](history-094.md)다. 원본 루트 별칭은 `Tab-ICL`; 정확한 상대경로·12사본과 새 보충자료의 위치·해시는 명세에 기록했다. 외부 코드 전체를 재게시하지 않고 고정 판본 링크와 검토 근거를 제공한다.

| 보충 ID | 같은 판본 파일 또는 API | 읽은 범위 |
|---|---|---|
| H095-S01 | [ts_benchmark/baselines/duet/layers/linear_extractor_cluster.py](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/layers/linear_extractor_cluster.py) | 전체 290행 |
| H095-S02 | [ts_benchmark/baselines/duet/layers/distributional_router_encoder.py](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/layers/distributional_router_encoder.py) | 전체 21행 |
| H095-S03 | [ts_benchmark/baselines/duet/layers/linear_pattern_extractor.py](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/layers/linear_pattern_extractor.py) | 전체 81행 |
| H095-S04 | [ts_benchmark/baselines/duet/layers/RevIN.py](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/layers/RevIN.py) | 전체 67행 |
| H095-S05 | [ts_benchmark/baselines/deep_forecasting_model_base.py](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/deep_forecasting_model_base.py) | 전체 752행 |
| H095-S06 | [config/rolling_forecast_config.json](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/config/rolling_forecast_config.json) | 전체 45행 |
| H095-S07 | [requirements.txt](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/requirements.txt) | 전체 15행 |
| H095-S08 | [README.md](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/README.md) | 전체 145행 |
| H095-S09 | [ts_benchmark/baselines/duet/__init__.py](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/__init__.py) | 전체 3행 |
| H095-S10 | [ts_benchmark/baselines/utils.py](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/utils.py) | 전체 388행 |
| H095-S11 | [ts_benchmark/baselines/duet/layers/Autoformer_EncDec.py](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/ts_benchmark/baselines/duet/layers/Autoformer_EncDec.py) | 전체 232행 |
| H095-S12 | [scripts/multivariate_forecast/ETTh1_script/DUET.sh](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/scripts/multivariate_forecast/ETTh1_script/DUET.sh) | 전체 8행 |
| H095-S13 | [scripts/multivariate_forecast/ILI_script/DUET.sh](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/scripts/multivariate_forecast/ILI_script/DUET.sh) | 전체 8행 |
| H095-S14 | [scripts/multivariate_forecast/Traffic_script/DUET.sh](https://github.com/decisionintelligence/DUET/blob/dcc6e6780a9138731b64b9b5398a94a1d97033f0/scripts/multivariate_forecast/Traffic_script/DUET.sh) | 전체 8행 |
| H095-S15 | [pytorch/v2.4.1/torch/nn/functional.py](https://github.com/pytorch/pytorch/blob/v2.4.1/torch/nn/functional.py) | gumbel_softmax 1894–1953행만 |

명령을 읽었다는 사실은 실행 결과를 뜻하지 않는다. entrypoint·CLI 최종 병합, 나머지 baseline·그림·자료·unified 결과, 이전 commit과 실제 재검사 이력은 이번 범위 밖이다. 작성후 대조 구간은 검수 문서에 별도로 기록한다.
