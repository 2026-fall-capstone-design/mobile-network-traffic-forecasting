# H075: 원76의 문헌·구현·저장 결과 출처

[기록](../records/0076-response-transfer-audit.md) · [출처 목록](../catalog/history-075-sources.jsonl) · [보존 검사](../evidence/0076-response-transfer/provenance-check.json) · [검수](../verification/history-075.md)

원76 findings의 기존 정확사본 1개를 재사용하고, 외부 자료 24개 byte 그룹을 구분한다. 총 25그룹의 등록 경로 76개 중 74개가 현재 해시와 일치한다. 없어진 라이브러리 경로 2개는 H074에서 확인한 항목이며, 같은 내용의 보관본은 남아 있다. 원본을 수정하거나 옮기지 않았다.

첫 검토 범위는 PDF 3개·39쪽의 텍스트와 시각 내용, 코드·README 6개, 검색 응답 4개, 원 PNG 6개, tree JSON 1개, 별도 TXT 직접 독해 2개다. TabDistill TXT는 이미 읽은 PDF 20쪽의 추출문에서 줄바꿈을 LF→CRLF로 바꾸고 명시된 page header와 구분 개행을 더하면 62,388바이트 전체가 정확히 재구성된다. [구간 증명](../evidence/0076-response-transfer/TXT-format-map.json)은 의미 정규화나 유사도 중복 판정이 아니며, 이를 새 독립 TXT 독해로 가산하지 않는다.

커밋 JSON은 전체 읽기로 표시하지 않는다. 파일 88개의 선택 목록 필드, 커밋 header, 61개 patch는 실제 읽었다. 나머지 interaction CSV 27개 patch는 [별도 목록](../evidence/0076-response-transfer/commit-read-scope.json)에 미독해로 남겼다. 86개 삭제 파일의 Git blob 복원 검사가 통과해도 미독해 내용을 읽은 것으로 세지 않는다.

## 파일별 범위

| source_id | 접근 관문 또는 기존 사본 | 실제 읽은 범위 |
|---|---|---|
| `SRC-0022031` | [76_response_transfer_findings.md](../evidence/0076-0079-learning-decisions/originals/SRC-0022031.md.txt) | 원76 findings 전체122행을 작성 후 다시 읽고 당시 무실행·판단·기호 해석을 검수. 재사용이며 새 독해 가산 없음. |
| `SRC-0063869` | [76_initial_0.txt](https://arxiv.org/abs/2604.13332v1) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063870` | [76_search_a.txt](https://arxiv.org/abs/2604.13332v1) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063871` | [76_search_b.txt](https://arxiv.org/abs/2604.13332v1) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063872` | [76_search_c.txt](https://arxiv.org/abs/2604.13332v1) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063873` | [Jacobian_ICML2018.pdf](https://proceedings.mlr.press/v80/srinivas18a/srinivas18a.pdf) | PDF 전체 텍스트·그림 첫 독해 완료. 작성 후 관련 주장·공개 표 전사 대조 완료. 별도 supplementary와 링크된 참고문헌 전문 검토는 아님. |
| `SRC-0063874` | [Jacobian_ICML2018.txt](https://proceedings.mlr.press/v80/srinivas18a/srinivas18a.pdf) | 전체 첫 독해 완료. 작성 후 관련 주장은 원 PDF 페이지와 대조했으며 이 파생 파일 자체를 다시 전부 읽은 것은 아님. |
| `SRC-0063875` | [Sobolev_NIPS2017.pdf](https://proceedings.neurips.cc/paper/2017/file/758a06618c69880a6cee5314ee42d52f-Paper.pdf) | PDF 전체 텍스트·그림 첫 독해 완료. 작성 후 관련 주장·공개 표 전사 대조 완료. 별도 supplementary와 링크된 참고문헌 전문 검토는 아님. |
| `SRC-0063876` | [Sobolev_NIPS2017.txt](https://proceedings.neurips.cc/paper/2017/file/758a06618c69880a6cee5314ee42d52f-Paper.pdf) | 전체 첫 독해 완료. 작성 후 관련 주장은 원 PDF 페이지와 대조했으며 이 파생 파일 자체를 다시 전부 읽은 것은 아님. |
| `SRC-0063877` | [TabDistill_2604.13332v1.pdf](https://arxiv.org/pdf/2604.13332v1) | PDF 전체 텍스트·그림 첫 독해 완료. 작성 후 관련 주장·공개 표 전사 대조 완료. 별도 supplementary와 링크된 참고문헌 전문 검토는 아님. |
| `SRC-0063878` | [TabDistill_2604.13332v1.txt](https://arxiv.org/pdf/2604.13332v1) | 이미 실제 읽은 PDF20쪽 텍스트와 가역적 바이트 대응 확인; 새 독립 TXT 독해 가산 없음. |
| `SRC-0063884` | [compare_index_performance.py](https://github.com/Clouddelta/tab-distill/blob/64214da0edf7eef6e8bf645332471d78b30345e8/experiments/TabDistill_downstream_comparison/compare_index_performance.py) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063885` | [tabarena_single_mulindex.py](https://github.com/Clouddelta/tab-distill/blob/64214da0edf7eef6e8bf645332471d78b30345e8/experiments/interaction_search/tabarena_single_mulindex.py) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063883` | [readme.md](https://github.com/Clouddelta/tab-distill/blob/64214da0edf7eef6e8bf645332471d78b30345e8/readme.md) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063886` | [interactions.py](https://github.com/Clouddelta/tab-distill/blob/64214da0edf7eef6e8bf645332471d78b30345e8/src/spectralexplain/interactions.py) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063879` | [TabDistill_commit.json](https://github.com/Clouddelta/tab-distill/commit/64214da0edf7eef6e8bf645332471d78b30345e8) | 파일 목록88개와61patch 전체 첫 독해; 작성 후 주장 관련 patch·수치 대조. interaction CSV27개와 나머지 JSON metadata 미독해. whole JSON 완료 아님. |
| `SRC-0063880` | [TabDistill_repository_tree.json](https://github.com/Clouddelta/tab-distill/tree/64214da0edf7eef6e8bf645332471d78b30345e8) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063887` | [inference.py](https://tabicl.readthedocs.io/en/latest/) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063888` | [regressor.py](https://tabicl.readthedocs.io/en/latest/) | 명세에 적은 전체 첫 독해 및 작성 후 관련 주장 대조 완료. 연결된 다른 자료 전체 검토나 코드 실행·재현 성공을 뜻하지 않음. |
| `SRC-0063889` | [Jacobian_ICML2018_p3.png](https://proceedings.mlr.press/v80/srinivas18a/srinivas18a.pdf) | 전체 첫 독해 완료. 작성 후 관련 주장은 원 PDF 페이지와 대조했으며 이 파생 파일 자체를 다시 전부 읽은 것은 아님. |
| `SRC-0063890` | [Jacobian_ICML2018_p8.png](https://proceedings.mlr.press/v80/srinivas18a/srinivas18a.pdf) | 전체 첫 독해 완료. 작성 후 관련 주장은 원 PDF 페이지와 대조했으며 이 파생 파일 자체를 다시 전부 읽은 것은 아님. |
| `SRC-0063891` | [Sobolev_NIPS2017_p4.png](https://proceedings.neurips.cc/paper/2017/file/758a06618c69880a6cee5314ee42d52f-Paper.pdf) | 전체 첫 독해 완료. 작성 후 관련 주장은 원 PDF 페이지와 대조했으며 이 파생 파일 자체를 다시 전부 읽은 것은 아님. |
| `SRC-0063892` | [Sobolev_NIPS2017_p6.png](https://proceedings.neurips.cc/paper/2017/file/758a06618c69880a6cee5314ee42d52f-Paper.pdf) | 전체 첫 독해 완료. 작성 후 관련 주장은 원 PDF 페이지와 대조했으며 이 파생 파일 자체를 다시 전부 읽은 것은 아님. |
| `SRC-0063893` | [TabDistill_2604.13332v1_p4.png](https://arxiv.org/pdf/2604.13332v1) | 전체 첫 독해 완료. 작성 후 관련 주장은 원 PDF 페이지와 대조했으며 이 파생 파일 자체를 다시 전부 읽은 것은 아님. |
| `SRC-0063894` | [TabDistill_2604.13332v1_p7.png](https://arxiv.org/pdf/2604.13332v1) | 전체 첫 독해 완료. 작성 후 관련 주장은 원 PDF 페이지와 대조했으며 이 파생 파일 자체를 다시 전부 읽은 것은 아님. |

## 접근 범위와 남은 내용

공식 링크는 당시 저장 판본의 출처 또는 프로젝트 문서 관문이다. 저장 TXT·PNG·검색 응답의 동일 byte를 모두 다운로드할 수 있다는 뜻이 아니다. 특히 TabICL의 latest 문서 링크는 보관된 2.2 파일의 고정 버전 링크가 아니다. 정확한 외부 저장 사본의 팀 공용 접근은 아직 미완료이며, 이 아카이브에는 해시·위치·작은 파생 증거를 제공한다.

Sobolev/Jacobian의 별도 supplementary는 해당 이름·논문 식별자로 원목록을 검색했을 때 식별되지 않았다. 다른 이름의 모든 파일에 존재하지 않는다고 단정하지는 않는다. 논문 본문은 보충자료를 별도로 안내하며 이번 검토에서 해당 증명·세부 설정 전체를 읽지는 않았다.

검색 응답 전체를 읽은 것과 검색 결과에 노출된 모든 논문을 읽은 것은 다르다. [검색 응답 분류](../evidence/0076-response-transfer/search-response-ledger.json)는 공식 서지·본문 발췌·2차 요약·다국어 반복·관련 없는 결과를 구분한다. 현재 최신 연구 검색으로 갱신한 목록도 아니다.

<a id="tabicl-runtime"></a>
## 저장 TabICL 2.2 코드의 접근 범위

`SRC-0063887`의 `_run_forward:1226–1232`와 호출 경로, `SRC-0063888`의 `fit:357–446`, `no_grad:467/529/598`, NumPy 반환 `539–541/608–610`을 저장 사본에서 정적으로 대조했다. 해시는 위 명세에 있다. 공식 문서의 latest 주소는 관문일 뿐 해당 저장 바이트의 증거가 아니다. 정확한 저장 코드 사본의 팀 공용 접근은 아직 미완료다.
