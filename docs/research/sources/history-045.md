# H045 출처와 실제 열람 범위

[연구 기록](../records/0056-0058-mae-sampling.md) · [manifest](../evidence/0056-0058-mae-sampling/manifest.json) · [기계 판독 목록](../catalog/history-045-sources.jsonl)

원본 루트 별칭은 `Tab-ICL`이다. 전체 목록의 `source_id`·원본 상대경로·해시로 원문에 돌아갈 수 있다. 이번에는 39개 고유 바이트 그룹과 동일 사본 경로 94개를 확인했다. ZIP 내부 사본도 해당 container와 member index로 바이트를 대조했으며 압축을 원본 폴더에 풀지 않았다. 이는 56–58의 발견된 전체 자료를 읽었다는 뜻이 아니다.

## 팀이 열 수 있는 보존 근거

새 메모·코드 7개와 작은 JSON 9개는 전체를 읽었다. 기존 원장·RCTL 구조·34 코드·summary·fit 결과 5개는 기존 근거를 재사용했다. 새 원문 16개는 40,572bytes다. 보존 사본의 과거 실행 지시·개인 경로는 역사적 원문이며 현재 명령이나 팀 탐색 경로가 아니다.

| source_id | 원본 상대경로 | 팀용 사본 | 이번 범위 |
|---|---|---|---|
| SRC-0021848 | `tmp/redesign_20260925/56_training_compression_review_plan.md` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0021848.md.txt) | 전체 텍스트 35줄 |
| SRC-0021872 | `tmp/redesign_20260925/57_mae_sampling_plan.md` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0021872.md.txt) | 전체 텍스트 9줄 |
| SRC-0021898 | `tmp/redesign_20260925/58_training_compression_findings.md` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0021898.md.txt) | 전체 텍스트 68줄 |
| SRC-0022784 | `tmp/redesign_20260925/fetch_training_compression_56.py` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0022784.py.txt) | 전체 텍스트 47줄 |
| SRC-0022800 | `tmp/redesign_20260925/finish_training_compression_sources_56.py` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0022800.py.txt) | 전체 텍스트 41줄 |
| SRC-0022906 | `tmp/redesign_20260925/mae_sampling_audit_57.py` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0022906.py.txt) | 전체 텍스트 46줄 |
| SRC-0023220 | `tmp/redesign_20260925/update_budget_after_mae_sampling_57.py` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0023220.py.txt) | 전체 텍스트 18줄 |
| SRC-0000838 | `output/research/redesign_20260925_snapshot_13/tmp/redesign_20260925/cumulative_execution_budget.json` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0000838.json) | 전체 JSON |
| SRC-0028241 | `tmp/redesign_20260925/results/mae_sampling_57/result.json` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0028241.json) | 전체 JSON |
| SRC-0028242 | `tmp/redesign_20260925/results/mae_sampling_57/run_finished.json` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0028242.json) | 전체 JSON |
| SRC-0028243 | `tmp/redesign_20260925/results/mae_sampling_57/run_started.json` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0028243.json) | 전체 JSON |
| SRC-0028244 | `tmp/redesign_20260925/results/mae_sampling_57/settings.json` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0028244.json) | 전체 JSON |
| SRC-0064452 | `tmp/redesign_20260925/sources/training_compression_56/adjacent_fetch_log.json` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0064452.json) | 전체 JSON |
| SRC-0064457 | `tmp/redesign_20260925/sources/training_compression_56/fetch_log.json` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0064457.json) | 전체 JSON |
| SRC-0064460 | `tmp/redesign_20260925/sources/training_compression_56/render_log.json` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0064460.json) | 전체 JSON |
| SRC-0064461 | `tmp/redesign_20260925/sources/training_compression_56/review_scope.json` | [새 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0064461.json) | 전체 JSON |
| SRC-0028240 | `tmp/redesign_20260925/results/mae_sampling_57/budget_before_accounting.json` | [기존 사본 재사용](../evidence/0056-0058-mae-sampling/../0052-0054-partial-observation/originals/SRC-0000732.json) | 전체 JSON |
| SRC-0023048 | `tmp/redesign_20260925/rctl_torch.py` | [기존 사본 재사용](../evidence/0056-0058-mae-sampling/../0639/originals/SRC-0023048.py.txt) | Block의 BatchNorm1d eps=.001·momentum=.01, Dropout .05와 forward |
| SRC-0022860 | `tmp/redesign_20260925/frozen_fit_gap_34.py` | [기존 사본 재사용](../evidence/0056-0058-mae-sampling/../0033-0035-frozen-fit/originals/SRC-0022860.py.txt) | eval·state와 epoch 기반 original_optimizer_steps 식 |
| SRC-0027517 | `tmp/redesign_20260925/results/frozen_fit_gap_34/summary.json` | [기존 사본 재사용](../evidence/0056-0058-mae-sampling/../0033-0035-frozen-fit/originals/SRC-0027517.json) | 주 seed 20260925 global·tabicl_risk의 fit 5개와 비용 필드 |
| SRC-0030237 | `tmp/redesign_20260925/results/rctl_pilot/fit_results.json` | [기존 사본 재사용](../evidence/0056-0058-mae-sampling/../0003-0007/originals/SRC-0030237.json) | 주 seed 20260925 global·tabicl_risk의 fit 5개와 비용 필드 |

## 이번에 읽은 외부 자료

| source_id | 자료 | 식별·범위 |
|---|---|---|
| SRC-0064458 | [importance_sampling_ICML2018.pdf](https://proceedings.mlr.press/v80/katharopoulos18a/katharopoulos18a.pdf) | 547,433bytes; SHA256 `1d6726829dd83572323499d6dbe238b9251e529362bde12937d0969104487fd8`; 본문/참고문헌10쪽 텍스트,수식·Algorithm1·Fig1–5가 있는3–8쪽 시각 확인;부록/저자코드 미검수 |
| SRC-0064467 | [importance_sampling_ICML2018_p3.png](https://proceedings.mlr.press/v80/katharopoulos18a/katharopoulos18a.pdf#page=3) | 298,884bytes; SHA256 `bf6a13f05bf61ebaa61688f347bbe888bad1b943689a489e5882d81e9a855cfb`; 과거PDF3쪽렌더 전체시각열람;renderreceipt해시일치 |
| SRC-0064459 | [importance_sampling_ICML2018.txt](https://proceedings.mlr.press/v80/katharopoulos18a/katharopoulos18a.pdf) | 41,356bytes; SHA256 `13ccb3062aa218cc5f0d9e9025ff7b9965d0d2b4a338906eea857a54d0f1158b`; PDF10쪽과추출결과동일;파생TXT1047줄,독립내용가산없음 |

공식 PMLR PDF 응답은 저장본과 같은 바이트다. 논문 텍스트를 현재 PDF 추출과 대조했으며 수식·그림은 렌더를 직접 읽었다. 이 사실을 증명 전체 인증·실험 재현이나 인용 논문 전체 검토로 확대하지 않는다.

## 해시만 확인한 관련 자료 — 본문 미완료

아래 15개는 저장 receipt와 바이트를 대조했다. 일부 논문 PDF가 있다는 이유로 방법·수식·결과를 읽었다고 세지 않는다. 58에 적힌 당시 판단은 원문 사본에서 열 수 있으며 후속 검토에서 대조한다.

| source_id | 자료 | 확인 범위 |
|---|---|---|
| SRC-0064438 | [TimeDC_PVLDB_2024.pdf](https://www.vldb.org/pvldb/vol18/p226-miao.pdf) | 2,909,872bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064448 | [TimeDC_arxiv_history.html](https://arxiv.org/abs/2410.20905) | 42,605bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064434 | [TabPFN_IML_arxiv_history.html](https://arxiv.org/abs/2403.10923) | 45,164bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064428 | [TabPFN_IML_2403_10923v2.pdf](https://arxiv.org/pdf/2403.10923v2) | 948,512bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064450 | [TimeDC_repo.json](https://api.github.com/repos/uestc-liuzq/STdistillation) | 5,401bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064436 | [TabPFN_IML_repo.json](https://api.github.com/repos/david-rundel/tabpfn_iml) | 5,420bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064426 | [SCott_ICML2021.pdf](https://proceedings.mlr.press/v139/lu21d/lu21d.pdf) | 711,890bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064453 | [antithetic_1810_03124v1.pdf](https://arxiv.org/pdf/1810.03124v1) | 286,943bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064455 | [antithetic_history.html](https://arxiv.org/abs/1810.03124) | 41,251bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064446 | [TimeDC__process__tools.py](https://raw.githubusercontent.com/uestc-liuzq/STdistillation/60169680447a12ad77b050831ee71da8be7f48f7/process/tools.py) | 5,133bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064465 | [TimeDC_PVLDB_2024_p6.png](https://www.vldb.org/pvldb/vol18/p226-miao.pdf#page=6) | 392,702bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064464 | [TimeDC_PVLDB_2024_p10.png](https://www.vldb.org/pvldb/vol18/p226-miao.pdf#page=10) | 284,968bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064463 | [TabPFN_IML_2403_10923v2_p11.png](https://arxiv.org/pdf/2403.10923v2#page=11) | 243,156bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064462 | [SCott_ICML2021_p5.png](https://proceedings.mlr.press/v139/lu21d/lu21d.pdf#page=5) | 299,584bytes·해시/동일 사본 확인;본문 미독해 |
| SRC-0064466 | [antithetic_1810_03124v1_p5.png](https://arxiv.org/pdf/1810.03124v1#page=5) | 337,884bytes·해시/동일 사본 확인;본문 미독해 |

## 정리 중 연결한 공식 응답

| reference_id | 링크 | 확인 범위 |
|---|---|---|
| EXT-H045-01 | [공식 응답](https://proceedings.mlr.press/v80/katharopoulos18a/katharopoulos18a.pdf) | 저장 PDF와 동일 바이트,위10쪽 범위;547,433bytes·SHA는manifest |
| EXT-H045-02 | [공식 응답](https://proceedings.mlr.press/v80/katharopoulos18a.html) | 서지:제목/저자/PMLR80/2525–2534;15,058bytes·SHA는manifest |
| EXT-H045-03 | [공식 응답](https://docs.pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html?highlight=mean) | stable주소의redirect표식만 확인;1,781bytes·SHA는manifest |
| EXT-H045-04 | [공식 응답](https://docs.pytorch.org/docs/stable/generated/torch.nn.modules.dropout.Dropout.html) | stable주소의redirect표식만 확인;1,841bytes·SHA는manifest |
| EXT-H045-05 | [공식 응답](https://docs.pytorch.org/docs/2.14/generated/torch.nn.BatchNorm1d.html) | 2.14 BatchNorm 설명·default·train/eval 범위;203,395bytes·SHA는manifest |
| EXT-H045-06 | [공식 응답](https://docs.pytorch.org/docs/2.14/generated/torch.nn.modules.dropout.Dropout.html) | 2.14 Dropout 설명·train/eval 범위;175,929bytes·SHA는manifest |

2.14 문서는 모드 의미의 참고이며 당시 설치된 PyTorch 버전의 증거가 아니다. 첫 두 stable주소 응답은 redirect여서 내용 독해 완료로 세지 않고 실제 대상 URL을 추가 확인했다.

## 남은 범위

TimeDC·TabPFN IML·SCott·SGD-as의 본문·공식 코드·버전과 56/58 종합, 중요도 논문의 부록·저자 구현·raw run, 59 이후 전체 기록은 미완료다. 57은 정확 산술이며 실교통·RCTL 학습 성능 실험이 아니다. 원 연구의 시작/완료 표식과 독립 process console·전체 비용·실제 환경의 차이도 유지한다.
