# 36–38 출처와 실제 열람 범위

[연구 기록](../records/0036-0038-finite-information.md) · [전체 식별 목록](../catalog/history-023-sources.jsonl) · [manifest](../evidence/0036-0038-finite-information/manifest.json)

Tab-ICL 루트 기준 26개 source 참조다. 새 작은 원문 10개 25,950 bytes와 기존 원장 1개를 연결하고, 지정 일차자료 11개와 해시만 확인한 4개를 별도로 기록한다. 파일 수는 독립 연구 시도 수가 아니다. 원문의 CRLF·바이트를 보존하고 설명문을 따로 작성했다.

## 보존 원문과 코드

| 링크 | 원 파일명 | 실제 범위 |
| --- | --- | --- |
| [SRC-0021428](../evidence/0036-0038-finite-information/originals/SRC-0021428.md.txt) | 36_finite_learning_source_plan.md | 36 전체 1–21행; 문헌 계획 |
| [SRC-0021450](../evidence/0036-0038-finite-information/originals/SRC-0021450.md.txt) | 37_information_claim_audit_plan.md | 37 전체 1–25행; 네 유한 사례 사전 계획 |
| [SRC-0021471](../evidence/0036-0038-finite-information/originals/SRC-0021471.md.txt) | 38_finite_learning_findings.md | 38 전체 1–68행; 문헌·반례·후속 판단 |
| [SRC-0022722](../evidence/0036-0038-finite-information/originals/SRC-0022722.py.txt) | extract_finite_learning_36.py | 전체 1–15행 정적 독해; HTML/PDF 추출 코드, 실행 없음 |
| [SRC-0022881](../evidence/0036-0038-finite-information/originals/SRC-0022881.py.txt) | information_claim_audit_37.py | 전체 1–111행 정적 독해; entropy 구현·marker·timer, 실행 없음 |
| [SRC-0027888](../evidence/0036-0038-finite-information/originals/SRC-0027888.json) | result.json | 작은 JSON 전체 키·4사례·8판정·시간·호출 수 |
| [SRC-0027889](../evidence/0036-0038-finite-information/originals/SRC-0027889.json) | run_started.json | 작은 JSON 전체; 시작 UTC·model_calls |
| [SRC-0062607](../evidence/0036-0038-finite-information/originals/SRC-0062607.json) | manifest.json | 작은 JSON 전체; 7입수 시도·404 포함 |
| [SRC-0062610](../evidence/0036-0038-finite-information/originals/SRC-0062610.json) | panel_published_manifest.json | 작은 JSON 전체; 출판본 PDF 별도 입수 |
| [SRC-0062612](../evidence/0036-0038-finite-information/originals/SRC-0062612.json) | run_started.json | 작은 JSON 전체; 다운로드 시작·크기 제한 |
| [SRC-0022700](../evidence/0036-0038-finite-information/../0642/originals/SRC-0022700.json) | cumulative_execution_budget.json | 기존 사본 재사용; information_claim_audit_37 비용 key만 연결, 중복 JSON key 검사 |

전체 텍스트 5개는 메모3개·정적 코드2개다. 작은 JSON5개는 전체 키를 읽었다. 재사용 원장은 신규 전체 읽기 수에 더하지 않는다. 코드와 원문에 남은 실행 명령은 과거 자료이며 이 정리에서 실행하지 않았다.

## 일차자료 식별

| ID | 정식 접근 링크 | bytes | SHA-256 |
| --- | --- | --- | --- |
| SRC-0062602 | [2607.13006v2.pdf](https://arxiv.org/abs/2607.13006v2) | 996326 | 2cc2d740733d2eede3b61354f97a4f0a227adce3af672ab64e4e9aa2fb76c5c7 |
| SRC-0062604 | [khan26a.html](https://proceedings.mlr.press/v337/khan26a.html) | 15146 | 8d868895d2d1a79d17e58a3713e68379668ca877a80ec35d6ed6975fc1626c22 |
| SRC-0062605 | [khan26a.pdf](https://proceedings.mlr.press/v337/khan26a.html) | 1672517 | c0d663923db74a90a9f4512e28b95f062e5c01a8b939212d2c2665346c08ff93 |
| SRC-0062608 | [panel_published_2026.pdf](https://doi.org/10.3982/QE2589) | 1594562 | 26d16b00273774fd48254e7d3502d6a09e508fc53c1cce1ff36f3afa1bcaba1c |
| SRC-0062611 | [panel_repository.html](https://www.repository.cam.ac.uk/handle/1810/404172) | 478950 | 639b8e501a5d5133a8d40ef9e0bc9d57322f950f802f68951d180ac0413884b8 |
| SRC-0062613 | [spectrum_abs.html](https://arxiv.org/abs/2607.13006v2) | 43564 | 86a0d938a93200af3f51613e71741a691bd18db2d209d8cb791d0ad4459f3b5a |
| SRC-0062614 | [khan_page_15.png](https://proceedings.mlr.press/v337/khan26a.html) | 249027 | 86bd0f9b3ac64ea9252a5964477a5559a02150531aaa190f561d2a08699b8a62 |
| SRC-0062615 | [khan_page_16.png](https://proceedings.mlr.press/v337/khan26a.html) | 257342 | f43ca2836a1bf5db1ea858a07b51c011a175af2e8837684f705502f51452db5d |
| SRC-0062616 | [khan_page_3.png](https://proceedings.mlr.press/v337/khan26a.html) | 478832 | f148e101308bf9f28c53a378f783f75449c4b6e34bc404ed292cb737969003ce |
| SRC-0062617 | [khan_page_5.png](https://proceedings.mlr.press/v337/khan26a.html) | 551036 | 1fdca1a9289d1c648887395402426be6d8ab0b20f725730c7065b1708368dc23 |
| SRC-0062618 | [khan_page_6.png](https://proceedings.mlr.press/v337/khan26a.html) | 540147 | b335b2b15b9d836c06003c0506255ca4a00b0ca5ae3d2c012571188272a9f757 |

- Khan: PDF24쪽 중 전체 텍스트 페이지 3–8,12,15–18(11쪽), PDF1은 추출 1–50행만 읽었다. PDF3·5·6·15·16의 원 PNG5개를 직접 확인했다. S4.33–38의 전체식/포화 조건, Gaussian gradient 조건, residual 추정·LoRA probe를 대조했다. 논문 전체·저자 코드 검토가 아니다.
- Panel: PDF52쪽 중 텍스트 1–2,4–19(18쪽), 시각 10·11·12·15·17·18(6쪽). 모형·Assumptions1–9·Propositions1–3·Eq23–24/32/40–45를 확인했다. PDF19의 Monte Carlo는 시작 부분이며 실험·부록 전체를 읽지 않았다.
- Spectrum v2: PDF21쪽 중 텍스트 1–9,12–13,17–21(16쪽), 시각 5·6·18·19·20(5쪽). §3–4, A.1–A.12와 지정 protocol/limitations를 읽되 PDF10–11/14–16과 저자 코드는 미검토다. Tables3/4/A1/A2는 보고 내용으로 읽었으며 수치를 재현하지 않았다.

총 지정 전체 텍스트 페이지45개·시각16개다. 추출 도구가 PDF97쪽을 변환한 것과 실제 읽은 범위는 다르며 전체 논문 완료0편이다. 과거38이 보고한 열람 범위를 현재 검수의 전수 완료로 대신 사용하지 않는다.

Khan HTML의 metadata는 저장13·14·18·117·121·141·142·171·176·195·233·236행만 읽었다. PMLR337, UAI42, 2026-08-06 metadata다. Cambridge HTML은7–8행 안의 citation tag12개를 선택해 제목·저자·2026-06-03·DOI·PDF bitstream을 확인했다. 긴 행 전체를 읽었다는 뜻이 아니다. Spectrum abs의41행 citation tag와119–120행 dateline,164–170행 submission-history 요소를 선택했다. v2는2026-07-15 15:43:13 UTC이고 현재 최신 버전을 조회한 것은 아니다. 정확한 선택 문자 offset은 manifest에 있다.

원 PNG5개는 Khan의 대응 페이지 시각 자료이며 PDF와 별개의 독립 연구결과가 아니다. Panel/Spectrum의 현재 렌더는 정리용 임시 산출물로 보관하고 PDF를 저장소에 일괄 게시하지 않았다.

## 해시만 확인한 자료

| ID | 파일명 | bytes | SHA-256 |
| --- | --- | --- | --- |
| SRC-0062601 | 2607.13006v2.html | 424207 | 3bb4148bc3af671d1a46195eb9251304eeba5bf132aebd007f20734907320b8e |
| SRC-0062603 | 2607.13006v2.txt | 70501 | ed99d296e6e26227744df1cf918c580d8b6380210b8175508a15ef7da01f2e1d |
| SRC-0062606 | khan26a.txt | 74682 | 039b428a6080e50f2acc09985a2345cdc99b26b776f05475ea571e00757cee65 |
| SRC-0062609 | panel_published_2026.txt | 136623 | ec62ab6e1353e798a0d0dd1dbdcca8ef720e01f1ba976b7ab96bbd0432e98eda |

Spectrum HTML과 과거 추출 txt3개의 고유 내용은 아직 읽지 않았다. PDF의 지정 구간을 읽었다고 별도 변환본 전체를 자동 완료하지 않는다.

## 검수 연결과 한계

[주장15개 지도](../verification/history-023-primary-review.json)는 원문 위치·계산·가정·남은 공백을 연결한다. [소스 검사](../verification/history-023-source-check.json)는26개 로컬 원본의 크기·해시와6개 연구 통제 파일의 불변을 확인했다. CI는 보존 사본과 metadata를 검사하며 원격 논문을 다시 내려받거나 과거 실행을 재현하지 않는다.

2025 author URL404, 출판본200, 이후 web parser timeout은 별개 사건이다. 보존 manifest로 접근 성공과 실패를 구분하며 timeout은38의 보고 수준이다. 나머지 문헌·다른 판본·39이후·전체 비용 통합은 계속 남는다.
