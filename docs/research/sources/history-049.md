# H049 출처와 실제 열람 범위

[연구 기록](../records/0056-0058-sgd-as.md) · [manifest](../evidence/0056-0058-sgd-as/manifest.json) · [기계 판독 목록](../catalog/history-049-sources.jsonl)

SGD-as 4개 바이트 묶음·8개 원본/동일 사본 경로와 58 메모 재사용 2경로를 연결한다. 원본 루트 별칭은 `Tab-ICL`이다. 외부 원문은 공식 URL·SHA-256으로 접근하며 새 보존 사본은 0개다. PDF/TXT/preview와 snapshot 사본을 독립 연구로 중복 계산하지 않는다.

| source_id | 원 파일 | 실제 열람 |
|---|---|---|
| SRC-0064453 | [antithetic_1810_03124v1.pdf](https://arxiv.org/pdf/1810.03124v1) | 7쪽 텍스트/시각 전체;Algorithm1–2/식1–35/Table1/Fig1–3. 참고문헌은 서지만 읽음. 원run 재현·인용된 모든 논문 검수 아님. |
| SRC-0064454 | [antithetic_1810_03124v1.txt](https://arxiv.org/pdf/1810.03124v1) | 992줄은 PAGE header/공백 제외 PDF 추출과 동일. 독립 전체본문으로 중복 가산하지 않음. |
| SRC-0064455 | [antithetic_history.html](https://arxiv.org/abs/1810.03124v1) | 저장 HTML의 보이는 본문·서지·v1 이력 137줄. script/style·연결 논문/코드 본문 미독해. |
| SRC-0064466 | [antithetic_1810_03124v1_p5.png](https://arxiv.org/pdf/1810.03124v1#page=5) | 저장 p5 preview 전체 시각 열람. 링크 테두리 표시는 파생 렌더 차이;독립 연구로 가산하지 않음. |

58 메모 `SRC-0021898`은 [기존 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0021898.md.txt)을 재대조했다. 전체 68줄의 과거 독해를 재사용하며 새 전체본문으로 가산하지 않는다. 원문 속 과거 다음 행동·실험 지시는 역사적 자료다.

## 현재 공식 자료와 동일성

| reference_id | 공식 자료 | 대조 범위 |
|---|---|---|
| EXT-H049-01 | [공식 연결](https://arxiv.org/pdf/1810.03124v1) | 현재 공식 v1 PDF가 저장본과 바이트 동일;독립 자료로 가산하지 않음. |
| EXT-H049-02 | [공식 연결](https://arxiv.org/abs/1810.03124v1) | 제목·저자·2018-10-07T11:42:10Z·표시된 v1 이력·arXiv DOI와 PDF 링크. 별도 출판/코드가 없다는 전수 검색 결론 아님. |

현재 공식 v1 PDF와 저장 PDF의 SHA-256은 `c7faf85251bcfa5ce3eed28de4f176d39680437fc812b274ee42503bcb8b143f`다. 제목·저자·2018-10-07 11:42:10 UTC와 표시된 v1 이력을 확인했다. 다른 출판/코드가 없다는 전수 검색 결론은 아니다.

Table 1의 6개 자료에 대한 표본수·feature 수·λ 18개 설정값을 시각·추출 텍스트에 대조했다. [설정·산술 JSON](../evidence/0056-0058-sgd-as/printed-settings-arithmetic.json)은 이를 보존하고 직접 후보 스캔을 가정한 내적 수를 계산한다. 정확한 그래프 값·원 run·성능 차이를 복원한 자료가 아니다.

저장 HTML은 보이는 본문/서지 137줄만 읽었다. PDF 전체 7쪽과 TXT992줄·preview는 같은 본문의 독해 범위로 연결하며 서로 다른 전체본문으로 중복 가산하지 않는다. 인용 논문 전체·저자 코드·자료 파일/정규화/분할·seed·학습률 수치·검색 구현·실제 비용은 미확인이다. 원 코드 import/실행·모델 fit/inference/forward·난수 생성은 없고 보호 원장 6개를 보존했다. [검수 범위](../verification/history-049.md)
