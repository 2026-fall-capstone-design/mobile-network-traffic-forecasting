# history-006 출처 — 관련 여섯 문헌의 지정 구간

[기록05 부분 정리](../records/0005-related-foundations-audit.md)와 [문헌 비교](../references/related-tabular-clustering.md)를 원문에 연결한다. 텍스트6개와 PDF6개는 **외부 문헌 identity와 공식 링크만** 등록했다. 논문 원문 파일을 GitHub에 새로 복사하지 않았다.

줄 번호는 보관 UTF-8 텍스트의 Python `splitlines()` 기준1부터, PDF는 물리 페이지1부터다. 아래 구간 밖을 읽었다고 집계하지 않는다. 해시는 [13항목 목록](../catalog/history-006-sources.jsonl)과 [manifest](../evidence/0005-related/manifest.json)에 있다.

| 문헌·판본 | 텍스트 source ID와 실제 읽은 줄 | PDF source ID와 시각적으로 읽은 내용 |
|---|---|---|
| [Localized v1](https://arxiv.org/abs/2608.16429v1) | SRC-0020608: 1–307,381–399,482–497 | SRC-0000074: p3 설정·Tables1/2; p6 AppendixA/A1 비용 |
| [TL-ANDI v1](https://arxiv.org/abs/2607.04809v1) | SRC-0064584: 1–115,171–603 | SRC-0002044: p6 식1–5; p7 식6–7·후보 선택; p8 Algorithm2·Assumption1; p10 정리3.1/3.2 |
| [CRUMB v1](https://arxiv.org/abs/2606.11473v1) | SRC-0064596: 1–374 | SRC-0064597: p4 식2–3·context 선택; p5 Algorithm1·배치 추론; p7 Tables1/2·평가 범위 |
| [Entangled v1](https://arxiv.org/abs/2607.25532v1) | SRC-0061688: 1–599,861–911 | SRC-0061687: p8 Tables4–6·개입 조건; p9 Table7·semi-synthetic 설정·한계 |
| [TabClustPFN v3](https://arxiv.org/abs/2601.21656v3) | SRC-0063591: 1–405 | SRC-0063590: p3 Figure2·prior; p4 PIN/CIN·loss; p5 학습 설정·평가 지표. Table1 개별 수치 검산 제외 |
| [Amortized TS v1](https://arxiv.org/abs/2605.13128v1) | SRC-0061680: 1–460,507–553,637–657,885–924 | SRC-0061679: p10 pairwise network; p11 Figure1·후처리·학습 규모; p12 평가 절차. Figure2 수치화 제외 |

여섯 논문의 지정 내용17쪽이다. PDF 전체 페이지 수나 완독한 논문 수가 아니다. 텍스트에 나타난 표·그림의 글자를 읽은 것과 실제 도표의 개별 수치를 대조한 것도 구분한다. 문서에서 인용한 주요 표의21행은 [논문 보고값](../evidence/0005-related/paper-reported-tables.json)으로 보존했다.

05 원문 `SRC-0020826`의 전체69행과 SHA-256이 같은 보존 사본을 [기존 위치](../evidence/0005/originals/SRC-0020826.md.txt)에서 재사용한다. 이번 새 원문 사본은0개다. 초기 B1/B2의 실행·분위수·cache·RCTL 검수는 [history-001](../verification/history-001.md)과 [history-005](../verification/history-005.md)의 기존 결과를 연결하며 독립 재현으로 추가하지 않는다.

정확한 해시 사본만 `exact_alias_source_ids`로 연결했다. TabClustPFN의 여러 경로 v3 PDF는 같은 바이트이지만 별도 v2 PDF와 해시가 다른 텍스트 추출본은 자동 완료 처리하지 않았다. Localized의 다른 HTML 추출은 제목·UI 부분만 확인한 자료이므로 이번 방법 근거에서 제외하고 미검토로 남겼다.

남은 범위는 지정 구간 밖의 본문·부록·증명·그림·개정본, 저자 코드와 원출력, 05의 회귀 TabPFN 후속 이력 및 다른 연구 기록이다. 파일 등록·해시 확인·부분 열람·주장 대조는 서로 다른 단계다. [검수 보고](../verification/history-006.md)
