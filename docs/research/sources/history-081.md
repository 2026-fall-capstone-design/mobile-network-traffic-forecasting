# H081 출처: 원78의 NTKMTL 검토

[기록](../records/0081-ntkmtl-training-balance.md) · [12개 출처 목록](../catalog/history-081-sources.jsonl) · [전체 SHA·사본·읽은 범위](../evidence/0081-ntkmtl/manifest.json) · [검수](../verification/history-081.md)

원78의 외부 자료 43개 그룹 중 NTKMTL 관련 11개를 이번에 검토했다. 기존 findings 1개는 H074 보존본을 재참조한다. 이번 밖의 32개에는 H074·H079·H080에서 검토한 자료가 포함되므로 모두 미독해라고 부르지 않는다. 기존 목록의 당시 상태는 유지하고 이번 범위를 덧붙인다.

| Source ID | 자료 | 실제 첫 독해 범위 | 새 집계 |
|---|---|---|---|
| SRC-0064468 | NTKMTL_NeurIPS2025.pdf | 29쪽 text·visual 전체, 표·부록 확대 포함 | 독립 본문 1 |
| SRC-0064469 | 같은 논문의 TXT | 29쪽 layout 추출과 정확 대응 | 독립 본문 추가 0 |
| SRC-0064483 | README.md | 1–74행 전체 | 독립 본문 1 |
| SRC-0064484 | cluster_methods.py | 1–424행 전체 정적 독해 | 독립 본문 1 |
| SRC-0064485 | weight_methods.py | 1–1823행 전체 정적 독해 | 독립 본문 1 |
| SRC-0064491 | commit JSON | 전필드·patch·commit/tree | 전체 JSON 1 |
| SRC-0064492 | repository JSON | 전필드·저장 metadata | 전체 JSON 1 |
| SRC-0064493 | tree JSON | 전필드·46 entry·root/blob 대조 | 전체 JSON 1 |
| SRC-0064503 | 원 PNG p25 | 전체 직접 열람 | 이미지 별도 1 |
| SRC-0064504 | 원 PNG p5 | 전체 직접 열람 | 이미지 별도 1 |
| SRC-0064505 | 원 PNG p6 | 전체 직접 열람 | 이미지 별도 1 |
| SRC-0022034 | 원78 findings | 1–80행 재참조 | 추가 0 |

논문은 Xiaohan Qin, Xiaoxing Wang, Ning Liao, Junchi Yan의 *NTKMTL: Mitigating Task Imbalance in Multi-Task Learning from Neural Tangent Kernel Perspective*, NeurIPS 2025다. 당시 확보된 [공식 PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/4522de4178bddb36b49aa26efad537cf-Paper-Conference.pdf)와 [고정 코드](https://github.com/jianke0604/NTKMTL/tree/abbf1f00c2b0bc207a950149cf4bf3a03cd69c8f)를 연결한다. README의 [arXiv 서지](https://arxiv.org/abs/2510.18258)는 별도 판본 전체를 이번에 확보·독해했다는 뜻이 아니다.

[TXT 대응](../evidence/0081-ntkmtl/text-variant-correspondence.json)은 PDF PAGE 표지와 경계 개행만 제거한 비교다. 추출문이 같아도 표 배치·수식·그림은 이미지로 확인했다. 쪽번호가 표 숫자에 붙은 경우는 인쇄값을 따른다. 29쪽 재렌더와 원 PNG 3개의 집계도 구분한다.

[고정 코드 대조](../evidence/0081-ntkmtl/static-code-version-check.json)는 3개 Git blob과 7개 root entry로 재구성한 tree를 확인한다. 전체 46 entry의 목록을 읽은 것과 그 파일 본문을 읽은 것은 다르다. 실제 trainer·requirements·helper·LICENSE 전문은 이 packet에 없으며 별도 미확보 범위로 남겼다. 외부 원문·코드 전체는 이 저장소에 복제하지 않는다.
