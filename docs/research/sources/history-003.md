# 05 가까운 다섯 방법의 출처와 읽기 범위

[정리 기록](../records/0005-closest-methods-audit.md), [문헌 비교](../references/closest-pooling-methods.md), [manifest](../evidence/0005/manifest.json), [JSONL 매핑](../catalog/history-003-sources.jsonl).

05 원문1개15,708bytes는 전체69행을 읽고 원바이트로 보존했다. 논문 자료5개는 지정 구간을 확인해 metadata와 공식 링크만 게시한다. 이5개는 서로 다른 논문4편에 대응하며, Population-HCP의 txt와 PDF는 같은 논문의 서로 다른 자료다. 별도 웹 원문1편을 더해 가까운 다섯 방법을 비교했다. 보존 파일 수와 논문 수, 읽은 구간과 전체 검토 완료를 구분한다.

| source_id | 원본 루트 기준 경로 | 이번 읽기·팀 접근 |
|---|---|---|
| SRC-0020826 | `tmp/redesign_20260925/05_literature_decision_audit.md` | 전체1–69행. [원문 사본](../evidence/0005/originals/SRC-0020826.md.txt). network/Tab 관련 주장은 후속 근거 통합 대기 |
| SRC-0020785 | `tmp/preflight_20260925/sources/HCP_2025.txt` | 1–42,63–168,639–803행. known-origin/A2·A3/식7·8/S0–S2/Theorems1·2/별도 test. [공식 원문](https://link.springer.com/article/10.1007/s11222-025-10683-x) |
| SRC-0020787 | `tmp/preflight_20260925/sources/HCP_population_2026.txt` | 386–1382행. posterior 손실·§3 알고리즘·§4/5실제 fitting과 결과 서술·§6 한계. 표 본문은 txt에 없음. [공식 원문](https://link.springer.com/article/10.1007/s41060-026-01197-4) |
| SRC-0063481 | `tmp/redesign_20260925/sources/population_prediction_guided_267/paper.pdf` | 물리10·13·15쪽 텍스트,15쪽 Table6/Figure2 시각 대조. [640 때의7–8쪽 검토](pilot-003.md)와 같은 PDF. 이번에는 Tables1·4·6의 보고값을 추가 확인 |
| SRC-0061704 | `tmp/redesign_20260925/sources/RMB_CLE.txt` | 1–30,277–593,1502–1529행. §3.1/3.2/3.3.1/Algorithm1/A.1. [공식 v1](https://arxiv.org/html/2602.14231v1)과 수식·판본 대조 |
| SRC-0061684 | `tmp/redesign_20260925/sources/ETAP_2026.txt` | 1–35,96–120,163–433행. §2·3.1·3.2.1–3.2.3. 추출 수식의 제어문자/줄 분리를 [공식 v1](https://arxiv.org/html/2602.18591v1)과 대조 |

목록 밖에서 확인한 Bolfarine·Lopes·Carvalho의 [공식 원문](https://link.springer.com/article/10.1007/s11222-026-10859-z)은 title/abstract,§2.1–2.2,§3 식13–15,§4.1–4.2 식16–28을 읽었다. 로컬 판본을 이번 경로명 탐색에서 특정하지 않았으며, 폴더 전체에 해당 문헌이 없다고 판정한 것은 아니다. [판본·범위·공백 기록](../verification/history-003-primary-review.json).

HCP2025 Algorithm1의 공식 이미지는 수신 timeout으로 읽지 못했다. 본문의 S0–S2와 정리 진술을 확인했고 전체 증명을 읽었다고 표시하지 않는다. Population-HCP의 웹 table 경로는 접근 실패하여 기존 PDF를 사용했다. PDF15쪽의 Table6/Figure2를 읽은 것과 Figure3의 개별 국가 소속을 분석한 것은 다르다. Tables3·5·7 전체도 이번 검수 범위 밖이다.

원문 안의 개인 경로·이전 명령·예산은 역사적 자료다. 인용 위치 세 곳과 원문 사이의 불일치는 정리본에 표시하고 보존 사본은 바꾸지 않았다. 같은 SHA 사본 연결은 manifest의 `exact_alias_source_ids`에 따른다. 서로 다른 SHA의 추출문·HTML·PDF를 바이트 중복으로 처리하지 않는다.
