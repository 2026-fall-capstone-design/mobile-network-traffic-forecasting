# 39–40 출처와 실제 열람 범위

[연구 기록](../records/0039-0040-sample-reuse.md) · [17개 식별 목록](../catalog/history-024-sources.jsonl) · [manifest](../evidence/0039-0040-sample-reuse/manifest.json)

작은 원문 5개 19,293 bytes를 원 바이트·CRLF 그대로 보존했다. 메모 2개·다운로드 코드 1개 전체와 작은 JSON 2개 전체 키를 읽었다. 별도 일차자료 metadata 8개와 해시만 확인한 4개를 구분한다. 파일 수는 실험 수가 아니다.

| 보존 링크 | 원 파일명 | bytes |
| --- | --- | ---: |
| [SRC-0021492](../evidence/0039-0040-sample-reuse/originals/SRC-0021492.md.txt) | 39_sample_reuse_source_plan.md | 2935 |
| [SRC-0021511](../evidence/0039-0040-sample-reuse/originals/SRC-0021511.md.txt) | 40_sample_reuse_findings.md | 10739 |
| [SRC-0022776](../evidence/0039-0040-sample-reuse/originals/SRC-0022776.py.txt) | fetch_sample_reuse_sources_39.py | 2496 |
| [SRC-0063937](../evidence/0039-0040-sample-reuse/originals/SRC-0063937.json) | manifest.json | 3062 |
| [SRC-0063938](../evidence/0039-0040-sample-reuse/originals/SRC-0063938.json) | run_started.json | 61 |

39는 1–23행, 40은 1–80행, 다운로드 코드는 1–49행 전체다. 코드의 실행 명령은 역사자료이고 현재 실행하지 않았다. manifest는 5개 입수 항목 전체, run_started는 시작 UTC/model_calls 전체를 확인했다.

## 일차자료·설치 코드

| ID | 정식 접근 링크 | bytes | SHA-256 |
| --- | --- | ---: | --- |
| SRC-0063929 | [2510.16986_abs.html](https://arxiv.org/abs/2510.16986) | 41242 | a1587afb8b47e4b8c9d7bf85974b161e273390dda2d5527e49719febd8b86479 |
| SRC-0063931 | [2510.16986v2.pdf](https://arxiv.org/pdf/2510.16986v2) | 1019171 | 52f0d21ceeaf3534dc5c64948b7d00219ad2ec1d84e78f29cfd5ec605eebd44d |
| SRC-0063933 | [bickel2008.pdf](https://icml.cc/Conferences/2008/papers/520.pdf) | 226556 | 2f413065a2ac219ec197199b78e05634ba550303a509e1091d80c7235442b3f2 |
| SRC-0063935 | [kumagai2021.pdf](https://proceedings.neurips.cc/paper_files/paper/2021/file/ff49cc40a8890e6a60f40ff3026d2730-Paper.pdf) | 427948 | 711334768319768cf3ad6a7dddc44880d1dd5932fa350037f73bfd1d7528ad71 |
| SRC-0047550 | [quantile_dist.py](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/_model/quantile_dist.py) | 56335 | 7e09ac0c3ce0260dc07cef79b0a98ee63b0785efafbf415fd243fe2981499b99 |
| SRC-0047582 | [unsupervised.py](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/_unsupervised/unsupervised.py) | 27940 | a226992e3c959e5e665b5f79dfca0e74a76f927cb7a94a83c392a78939f8285c |
| SRC-0047572 | [preprocessing.py](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/_sklearn/preprocessing.py) | 43233 | 2163a3bf6754127365a7aedac854d99a6f565545cc1ea7e63c68a596081b2976 |
| SRC-0047644 | [METADATA](https://pypi.org/project/tabicl/2.2.0/) | 38256 | e429edbe64f243241e6425854643b0d4128de550121b9feb1598ef710b9941a2 |

- Bickel PDF 8쪽 중 전체 텍스트 페이지 1–5, 시각 3·4·5. §4 식1–11·최종 weighted 학습·응용 구분, Optimization Problem1 부호를 대조했다. 6–8쪽과 저자 구현은 미검토다.
- Kumagai PDF 13쪽 중 텍스트 1–6, 시각 4·5. 상대 ratio·집합 표현·비제약해/clipping·meta-training·support/query 포함 설정을 확인했다. 7–13쪽·별도 부록·저자 구현은 미검토다.
- Cherkaoui v2 PDF 23쪽 중 텍스트 1–6,16–20(11쪽), 시각 5·18·19·20. 선형 조건·bias/variance·Cantelli·Algorithm1/복잡도를 선택 확인했다. 7–15,21–23쪽 및 전체 증명·저자 구현 검토는 미완료다. 본문 proof를 읽은 것과 모든 대수 전개를 검증한 것은 다르다.

합계 텍스트 22쪽·시각 9쪽이다. PDF 44쪽 변환을 44쪽 독해로 세지 않으며 전체 논문 검토 완료 0편이다. 논문 결과표의 새 재현도 없다.

설치된 quantile_dist.py는 816–1130행, unsupervised.py는 1–267/377–626행, preprocessing.py는 785–916행을 정적으로 읽었다. METADATA는 1–25행의 Name/Version/License 부분을 확인했다. 셋의 코드 바이트는 기존 고정 commit 0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3의 보존 ZIP 대응 항목과도 같았다. 전체 라이브러리나 세 파일 전체 독해가 아니다. 원 파일 실행·import·난수 생성 없이 열 반복과 Latin square의 크기를 대조했다.

저장 abs HTML은 citation tag·제목·dateline·submission history의 선택 요소만 읽었다. metadata는 v2 2026-05-13을 가리킨다. [공식 v1 서지](https://arxiv.org/abs/2510.16986v1)는 2026-10-09 조회에서 옛 제목·2025-10-19 날짜를 확인했으며 원 inventory 파일로 추가하지 않았다. 논문 v1 전체 독해가 아니다. citation tag의 선택 문자 offset은 manifest에 남겼다.

## 해시만 확인한 항목

| ID | 원 파일명 | bytes | SHA-256 |
| --- | --- | ---: | --- |
| SRC-0063930 | 2510.16986v2.html | 823501 | 94bd70ae56ff01ff31607fb12362249812b869d1718dc2631a63eb6b785c0cd9 |
| SRC-0063932 | 2510.16986v2.txt | 75185 | 1a82f4769895807cfea3ded538b591c344faa3f998bdd2d776a4ef584ee07725 |
| SRC-0063934 | bickel2008.txt | 36090 | 9a89f73a96750da62d9158c925ecfda05606ff91e4e3e0d5c855812693aa93e5 |
| SRC-0063936 | kumagai2021.txt | 50381 | dbce967d0feffaf93b9973c56700184187aac1b69e9a770a55e5fc2457fb9543 |

v2 HTML과 과거 추출 txt 3개의 고유 내용은 미검토다. PDF 지정 구간을 읽었다고 별도 변환본 전체를 자동 완료하지 않는다. 문헌과 라이브러리는 원문을 일괄 게시하지 않고 정식 위치·고정 버전·해시·검토 구간을 연결했다.

[원본 검사](../verification/history-024-source-check.json)는 17개 identity와 연구 통제파일 6개 불변을 확인했다. CI는 보존 사본과 등록 metadata를 검사하며 원격 논문·라이브러리를 다시 내려받아 검증하지 않는다. [주장 지도](../verification/history-024-primary-review.json)에서 과거 판단·현재 정정·남은 공백을 함께 확인한다.
