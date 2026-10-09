# 기록17 문헌의 출처와 실제 읽은 범위

[정리 기록](../records/0017-adaptation-literature.md)·[방법 비교](../references/temporal-adaptation-methods.md)·[manifest](../evidence/0017-literature/manifest.json)·[원문 매핑](../catalog/history-011-sources.jsonl)을 연결한다. SRC-0021004 전체1–26행을 다시 읽고18–22행의 세 방법을 확인했다. 기존 바이트 사본을 재사용했고 새 원본 파일을 더 보존하지 않았다.

| 문헌·공식 metadata | 저자·v1 제출일 | 확보·대조한 판본 |
|---|---|---|
| [MGSTC](https://arxiv.org/abs/2508.08281v1) | Ningning Fu, Shengheng Liu, Weiliang Xie, Yongming Huang ·2025-08-01 | [HTML](https://arxiv.org/html/2508.08281v1)·[PDF](https://arxiv.org/pdf/2508.08281v1),26쪽. 관련 DOI10.1145/3758099 |
| [PID](https://arxiv.org/abs/2608.08332v1) | John Sengendo, Zineddine Bettouche, Khalid Ali, Andreas Kassler, Fabrizio Granelli ·2026-08-08 | [HTML](https://arxiv.org/html/2608.08332v1)·[PDF](https://arxiv.org/pdf/2608.08332v1),9쪽 |
| [Joint QoS](https://arxiv.org/abs/2604.12903v1) | Oscar Stenhammar, Gábor Fodor, Carlo Fischione ·2026-04-14 | [HTML](https://arxiv.org/html/2604.12903v1)·[PDF](https://arxiv.org/pdf/2604.12903v1),18쪽 |

이 세 편은 이번 공식 웹 자료로 확보했다. 원 목록48,149항목에서 해당 PDF의 정확한 SHA 일치가 없었고 경로명 탐색도 일치0이었다. 제한된 sources 디렉터리의 본문 탐색에서는 다른 논문의 참고문헌과 검색 로그에 인용이 있었다. 이 탐색으로 로컬 전체에 다른 판본이 없다고 단정하지 않는다. 원 목록에 가상 SRC 번호를 추가하거나 전체 논문을 GitHub에 복사하지 않았다.

| 문헌 | 추출문에서 읽은 줄 | PDF 시각 대조 | HTML 전체 지정 절 |
|---|---|---|---|
| MGSTC | 292–592,839–964 | 물리6–8·11–13쪽:정의·Fig2/3/5·§4.3·Algorithm1·식16–18·Table2·Milan 설명 | S3.SS2,S4.SS3 |
| PID | 165–622 | 물리2–6쪽:Fig1·방법·Algorithm1·튜닝·TableIV·평가 설정/지표 | S3.SS1,S3.SS3,S4.SS3 |
| QoS | 115–790 | 물리3–11쪽:Fig1·시스템·목적함수·교대 갱신·가정/명제·설정·Fig2 | S3,S4.SS1,S4.SS2,S4.SS3,S5.SS1 |

줄 번호는 manifest에 기록한 SHA의 pypdf 추출문에 Python `splitlines()`를 적용한1기준이다. HTML 수식은 원 MathML의 alttext를 대조했다. MGSTC 추출문의 NUL과 QoS Fig2의 깨진 글리프는 원본을 바꾸지 않고 PDF 시각 대조로 보완했다. 읽기 도구에 인접 구간이 보였다는 이유로 전체 절·전체 논문을 완료 처리하지 않았다.

시각 대조20쪽은 선택한 방법·표기 확인이다. PID2쪽의 관련연구,6쪽의 결과 전체,TableIII 모든 성능 수치와 Figure3그래프 검증을 포함하지 않는다. QoS11쪽의 결과 도입부를 읽은 것과 뒤의 전체 수렴·성능 그래프 및 부록 증명 검토는 다르다. MGSTC4.1/4.2의 전체 구조와 나머지 데이터·성능도 남아 있다. 전체 논문 검토 완료는0편이다.

MGSTC PDF의 템플릿 날짜와 공식 arXiv 제출일을 혼용하지 않았다. SHA·byte수·확보 시각·공식 metadata·정확한 미열람 범위는 manifest에 있다. 원본 속 당시 명령이나 다음 행동은 연구 이력이며 이번 작업의 실행 지시가 아니다.
