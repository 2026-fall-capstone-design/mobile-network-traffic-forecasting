# H020 출처와 실제 읽은 범위

[기록 28](../records/0028-mechanism-uncertainty.md), [문헌 비교](../references/mechanism-uncertainty.md), [목록 13건](../catalog/history-020-sources.jsonl), [manifest](../evidence/0028-mechanism-uncertainty/manifest.json)를 연결한다. 원본 경로의 기준은 catalog의 `Tab-ICL` root다. 같은 SHA256의 alias는 manifest에 보존했다. 다른 바이트의 추출 txt는 동일 사본으로 처리하지 않았다.

| source_id | 사용한 원문 | 읽은 범위·상태 |
|---|---|---|
| SRC-0021257 | `28_mechanism_and_uncertainty_audit.md` | 1–66행 전체. 원본 바이트 보존 |
| SRC-0063064 / SRC-0063067 | 두 원 manifest | 모든 항목·키. 원본 바이트 보존 |
| SRC-0063058 | TabMGP v3 PDF, 36쪽 | 텍스트 1·2·3·4·5·6·8·9·15쪽; 시각 4·8·9·15쪽. 전체 논문 아님 |
| SRC-0063066 | CLT v2 HTML | S4, S5, A1, A2, A10.SS1, A10.SS6, A6.SS2, A6.SS3. MathML alttext의 LaTeX를 포함해 열람. 전체 HTML 아님 |
| SRC-0063062 | Vario PDF, 11쪽 | 텍스트 3·4·5·6·10·11쪽; 시각 3·4·5·10·11쪽. 별도로 1쪽 추출문 1–65행의 서지·도입 확인 |
| SRC-0063060 | Two-stage PDF, 표지 포함 9쪽 | 텍스트 1·3·4·5·6·7쪽; 시각 4·5·6·7쪽. 인쇄 쪽수 2969–2976과 PDF 페이지를 구별 |
| SRC-0063065 | `tabmgp_minimal_bf44db1.py` | 1–221행 전체 정적 열람, import·실행 없음 |
| SRC-0063068 | `posterior.py` | 1–151행 전체 정적 열람, import·실행 없음 |
| SRC-0063069 | `tabicl_adapter.py` | 1–184행 전체 정적 열람, import·실행 없음 |
| SRC-0063059 / SRC-0063061 / SRC-0063063 | 기존 PDF별 txt | identity만 확인. 전체 본문·주석·PDF와의 완전 동등성 미확인 |

PDF 페이지는 1부터 센다. 선택 텍스트 21쪽·시각 13쪽은 서로 겹치며 합쳐서 34개 고유 페이지라고 세지 않는다. Vario 첫 페이지 서지 구간은 이 21쪽에 추가하지 않은 별도 제한 열람이다. 자동 추출한 나머지 페이지를 읽기 완료로 처리하지 않았다. 표의 시각 열람은 실험값의 독립 재계산이 아니다.

세 코드의 공식 commit URL에서 받은 바이트는 로컬 원본과 정확히 일치했다. [원격 identity 확인](../verification/history-020-remote-code-check.json)에 URL·SHA256·크기·시각을 남겼다. 논문 네 건은 로컬 원본의 해시·기록된 공식 URL을 연결했으며 이번에 원격 PDF/HTML 바이트까지 동일하다고 검증한 것은 아니다. CLT의 제목·v2 날짜는 별도로 공식 버전 정보에서 확인했다.

외부 논문·코드는 공식 링크와 metadata로 제공한다. 본문 전체의 재게시, 저자 전체 코드 검토, 현재 runtime 호환성, 학습·추론·성능 재현을 완료했다고 표현하지 않는다. CIRM/CRT/NTK/PreqTorch는 원문에 남은 발견 단계이며 H020의 상세 방법 검토에 포함하지 않았다.

[H055 후속 범위](history-055.md)에서 ECAI PDF 전체9쪽·원TXT동등성·공식코드2개·Fig3/Table1–6를추가로검수했습니다. 위H020범위는당시기록이고다른문헌/파생TXT까지확대되지않습니다.
