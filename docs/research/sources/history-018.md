# H018 출처와 실제 읽은 범위

[기록25 §3–4](../records/0025-adjacent-structures.md)의 2026-10-09 검수다. [원 inventory 연결4건](../catalog/history-018-sources.jsonl)과 [manifest](../evidence/0025-adjacent/manifest.json)는 보존 참조3건과 외부 PDF metadata1건을 구분한다. 별도 웹 일차자료3건은 원 inventory의 파일 수에 추가하지 않았다.

| 출처 | 실제 사용·열람 | 완료로 세지 않은 범위 |
|---|---|---|
| SRC-0021188 기록25 | H016에서 전체61행 열람; 이번43–61행 §3–4 재대조 | 전체 후속 판단 통합 |
| SRC-0030236 평가 NPZ | `cell_ids/test_times/test_y/peak_threshold`의 저장 support 재계산 | 새 예측·학습, 전체 파일의 별도 재검수 |
| SRC-0030280 summary | 8개 metrics의 method/seed·peak count·peak cell MAE·peak 평균 | 나머지 지표의 신규 검수 |
| SRC-0062988 Ma PDF / H018-Ma | 공식v1과 로컬 PDF 바이트 동일. HTML0–200행, PDF8·14·37쪽 시각 대조,15쪽 텍스트 | 전체43쪽·전체 증명/성능표·코드. 발견한 로컬txt와 과거 PNG는 이번 본문 검토에 추가하지 않음 |
| H018-NeST | 공식v2 HTML 선택구간105–113/139–154/318; PDF3·4·5·9·14·15·16·17·18쪽 시각 대조,3·8·9·14–18쪽 텍스트 | 전체20쪽·전체 성능표·코드·실행 스케줄 |
| H018-GraphColoring | 공식v3 HTML147–356/374–383; PDF4·5·16쪽 시각 대조,3·26–28쪽 텍스트 | 전체39쪽·전체 증명/성능표·코드·최신 개정판 |
| H018-NTK | 원문25의 과거 읽기 범위; 현재 기관 제목·저자·초록·날짜·워크숍 필드와 검색 발췌 | 상세 알고리즘·PDF 전체. 직접 PDF 열기는 verification challenge |

PDF 페이지는1부터 센다. 시각 열람15쪽은 지정 내용의 확인이며 페이지에 실린 모든 성능표를 재계산했다는 뜻이 아니다. 자동 text 추출·렌더링만으로 읽기 완료를 부여하지 않았다. 이력·코드는 실행하지 않았다. [주장별 locator와 한계](../verification/history-018-primary-review.json)를 함께 보존했다.

논문은 원문 전체를 복사 게시하지 않고 지정 공식 링크·파일 identity·검토 범위를 제공한다. Ma PDF의 SHA256은 `4507a6f8b0110431ffc22ecd8c5ce2819d7bb54e5ef3a500cc48431cd97e28c8`, NeST는 `88468c57b6d42abb1659b21ecc57f3b52ade395a7d6e87e34acc51d095d34761`, Graph Coloring은 `f493b8ab47b0f1186654226f1b604701f3ea2ad91999d91dc4066a64cf41a03f`다. NTK PDF 바이트는 확보하지 않았으므로 해시를 만들지 않았다.

peak TRAIN threshold·H5는 [H001](../verification/history-001.md)을 재사용한다. 조건부 공유 비용과 recursive 숫자는 [H016](../verification/history-016.md)·[H017](../verification/history-017.md)의 범위에서 연결하며 이번에 새로 재현한 결과로 세지 않는다.
