# H072 출처 — ForeCA·mbrdr·GNN

[팀 기록](../records/0073-forecastable-output-audit.md) · [출처 명세](../evidence/0073-forecastable-output/manifest.json) · [주장별 검수](../verification/history-072-claims.json)

원73 당시 findings와 수집 이력을 보존하고, 이번에 실제 읽은 원문·정적 코드를 별도로 연결한다. 아래 파일은 원본14그룹·물리28경로이며 새 원문 복사는0이다. 원문별 해시·별칭은 명세와 [무결성 확인](../evidence/0073-forecastable-output/provenance-check.json)에 있다. 작성 후 36개 주장과 관련 원문을 다시 대조했다. 같은 에이전트의 재검토이며 독립 재현은 아니다.

| source_id | 자료 | 실제 독해/접근 |
|---|---|---|
| SRC-0022023 | [72_73_source_findings.md](../evidence/0073-forecastable-output/../0072-0075-output-compression/originals/SRC-0022023.md.txt) | 원72–73 findings 전체52행 또는 원73 수집 manifest 전체 재독해. H070에서 이미 보존·계수한 자료. |
| SRC-0063350 | [manifest.json](../evidence/0073-forecastable-output/../0072-0075-output-compression/originals/SRC-0063350.json) | 원72–73 findings 전체52행 또는 원73 수집 manifest 전체 재독해. H070에서 이미 보존·계수한 자료. |
| SRC-0063340 | [ForeCA_ICML2013.pdf](https://proceedings.mlr.press/v28/goerg13.pdf) | PDF9쪽 본문/수식/그림/서지27항목 전체 첫 독해. Fig2 밀집 관측 인덱스1413개와 Fig4 모든 좌표는 개별 전사하지 않음. |
| SRC-0063341 | [ForeCA_ICML2013.txt](https://proceedings.mlr.press/v28/goerg13.pdf) | TXT9본문의 strip 후 문자열이 실제 읽은 PDF추출문과 모두 정확일치. TXT raw 전체를 독립 재독해한 것으로 중복 집계하지 않음. |
| SRC-0063342 | [GNN_clustering_README.md](https://github.com/NGMLGroup/Time-Series-Clustering-with-GNNs/blob/303c8cc6c5142aa1a4eab06677ce44104bd95355/README.md) | README 전체 텍스트 첫 독해. 고정 commit 원본과 바이트 일치. 연결 그림은 추가 공식 자료로 별도 확인. |
| SRC-0063343 | [GNN_commit.json](https://github.com/NGMLGroup/Time-Series-Clustering-with-GNNs/commit/303c8cc6c5142aa1a4eab06677ce44104bd95355) | commit JSON 전체 및 README patch 독해. 실행 기록이 아님. |
| SRC-0063344 | [GNN_model.py](https://github.com/NGMLGroup/Time-Series-Clustering-with-GNNs/blob/303c8cc6c5142aa1a4eab06677ce44104bd95355/source/modules/model.py) | model.py 전체 정적 독해. import/실행 없음. |
| SRC-0063345 | [GNN_pooling_functions.py](https://github.com/NGMLGroup/Time-Series-Clustering-with-GNNs/blob/303c8cc6c5142aa1a4eab06677ce44104bd95355/source/modules/pooling_functions.py) | pooling_functions.py 전체 정적 독해. import/실행 없음. |
| SRC-0063346 | [GNN_predictor.py](https://github.com/NGMLGroup/Time-Series-Clustering-with-GNNs/blob/303c8cc6c5142aa1a4eab06677ce44104bd95355/source/modules/predictor.py) | predictor.py 전체 정적 독해. import/실행 없음. |
| SRC-0063347 | [MBRDR_CRAN_manual.pdf](https://cran.r-project.org/web/packages/mbrdr/mbrdr.pdf) | manual10쪽 전체 본문/식/예제/색인 첫 독해. 공식 현재 PDF와 바이트 일치. |
| SRC-0063348 | [MBRDR_CRAN_manual.txt](https://cran.r-project.org/web/packages/mbrdr/mbrdr.pdf) | TXT10본문 strip 후 문자열이 읽은 PDF추출문과 모두 정확일치. |
| SRC-0063352 | [ForeCA_ICML2013_p5.png](https://proceedings.mlr.press/v28/goerg13.pdf) | 원PNG ForeCA PDF5쪽 전체 시각 확인. |
| SRC-0063353 | [ForeCA_ICML2013_p8.png](https://proceedings.mlr.press/v28/goerg13.pdf) | 원PNG ForeCA PDF8쪽 전체 시각 확인. |
| SRC-0063354 | [MBRDR_CRAN_manual_p2.png](https://cran.r-project.org/web/packages/mbrdr/mbrdr.pdf) | 원PNG manual PDF2쪽 전체 시각 확인. |

## 추가 공식 자료

[외부 요청26개의 URL·해시·읽은 범위](../evidence/0073-forecastable-output/external-sources.json)를 따로 남겼다. 원본 연구 폴더에 없던 이번 추가 자료를 원본 목록의 고유 연구기록으로 가산하지 않는다. 다운로드한 논문/코드 전체를 게시하지 않고 공식 링크를 사용한다.

- ForeCA: 공식 본판은 보관본과 동일하다. 보충1쪽의 두 증명도 확인했다.
- mbrdr: 공식 manual은 보관본과 동일하다. CRAN1.1.1 소스의 R 파일·DESCRIPTION·NAMESPACE를 정적으로 읽고, 자료파일과 R 예제는 실행하지 않았다.
- MBRDR2024: Crossref가 제공한 출판사 PDF 링크로 본문을 확보했다. PDF12쪽 중 마지막1쪽은 백지이며 전체 텍스트/시각을 확인했다. 원2008 논문은 현재도 서지 메타데이터만 확보했다.
- GNN: 고정 commit의 보관3코드·README가 동일하다. 추가7 Python파일·환경·라이선스·구조 그림을 읽었다. 공식 tree는 경로/종류/크기/blob SHA 선택 필드만 읽었고 전체 JSON 독해로 세지 않는다. 논문 전체는403/브라우저 확인 화면으로 미확보다.

모든 코드는 실행하지 않은 참고 구현이다. 다운로드 성공, 전체 독해, 의미 검수, 설치/실험 재현을 서로 다른 상태로 기록한다. [형식 대조](../evidence/0073-forecastable-output/format-audit.json)와 [팀 검수 안내](../verification/history-072.md)를 함께 확인한다.
