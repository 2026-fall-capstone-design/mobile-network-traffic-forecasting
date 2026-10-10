# H060 출처·판본 — TACTiS-2

[팀 기록](../records/0064-0065-tactis2.md) · [명세](../evidence/0064-0065-tactis2/manifest.json) · [목록](../catalog/history-060-sources.jsonl) · [검수](../verification/history-060.md)

7원본 그룹·14물리 경로다. 64·65 정확사본2개를 재사용하고 논문 PDF/TXT/HTML/PNG2개는 외부 참조5개다. TXT·PNG는 동일논문의 표현이며 서로 다른 연구실험이 아니다. 새 사본·로컬 전체본문/전체JSON/선택필드 독해 증분은0이다.

| source_id | 팀 접근 경로 | 실제 확인 범위 |
|---|---|---|
| SRC-0022015 | [64_conditional_transform_review_plan.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022015.md.txt) | 64 전체 재대조. 분포변환 후 clustering/RCTL 질문과 full-history/달력조건 PIT 구분을 연결. H055 전체독해/기존 정확사본 재사용. |
| SRC-0022016 | [65_residual_and_transform_findings.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022016.md.txt) | 65 전체 재대조, 특히 §6/연결논리. 당시 논문선택독해와 구현미검토 상태를 보존하고 이번 전체논문/고정코드 검수와 구분. |
| SRC-0062147 | [TACTiS2_2310.01327v2.pdf](https://arxiv.org/pdf/2310.01327v2) | 28쪽 전체 텍스트·시각,15그림/12표/10–14쪽 참고문헌 서지. 공식v2 PDF 바이트동일. 실행재현 없음. |
| SRC-0062148 | [TACTiS2_2310.01327v2.txt](https://arxiv.org/pdf/2310.01327v2) | 28쪽 page wrapper/외곽공백/LF 정규화 뒤 새PDF 추출과 문자동일. 독립 논문/실험 아님. |
| SRC-0062149 | [TACTiS2_abs.html](https://arxiv.org/abs/2310.01327v2) | 저장 abstract HTML의 서지·초록·판본이력·공식논문/구현링크만 독해. 2026-10-10 latest URL 응답과 바이트동일. 전체HTML 독해 아님. |
| SRC-0063862 | [TACTiS2_2310.01327v2_p4.png](https://arxiv.org/pdf/2310.01327v2#page=4) | 저장 원PNG4쪽 전체 시각대조. 목적식/두단계 학습·encoder 구조. PDF의 파생물. |
| SRC-0063863 | [TACTiS2_2310.01327v2_p5.png](https://arxiv.org/pdf/2310.01327v2#page=5) | 저장 원PNG5쪽 전체 시각대조. 학습·추론 모듈과 mask/decoder/DSF. PDF의 파생물. |

## 논문과 형식

Arjun Ashok, Étienne Marcotte, Valentina Zantedeschi, Nicolas Chapados, Alexandre Drouin의 *TACTiS-2: Better, Faster, Simpler Attentional Copulas for Multivariate Time Series*, ICLR2024다. [공식 history](https://arxiv.org/abs/2310.01327v2)는 v1 2023-10-02, v2 2024-03-25를 표시하며2026-10-10 확인 시 최신은v2다.

[공식 v2 PDF](https://arxiv.org/pdf/2310.01327v2)는 HTTP200,3,214,923바이트/SHA-256 `53eb86fed82fe520e55ea1587eed75abfe1dcc3d098e3f8403dc9e4cc9e6e37f`로 저장본과 같다. 28쪽 전체 텍스트·시각,15그림·12표·10–14쪽 서지목록을 읽었다. 인용논문들의 본문까지 읽었다는 뜻은 아니다. 원PNG4·5쪽은 전체시각으로 대조했다. TXT는 page wrapper·개행·외곽공백 정규화 뒤28쪽 모두 새 추출과 같다. TXT/PNG의 연결URL은 논문내용 접근용이며 파생파일의 바이트를 제공하는 URL은 아니다.

저장 abstract HTML은 latest 주소의 응답과42,334바이트/SHA가 같고, versioned v2 응답42,346바이트와는 별도다. 서지·초록·history·논문/공식코드링크만 읽었으며 전체 사이트 HTML 독해가 아니다. UTF-8을 명시하여 추출기에서 생긴 저자명 디코딩 문제를 바로잡았고 원본 바이트는 보존했다. [판본 검사](../evidence/0064-0065-tactis2/external-version-check.json)에 응답시각과 해시를 저장했다. 원65의 OpenReview403은 당시 접근실패로 유지하며 우회하지 않았다.

## 공식 코드

논문이 연결한 [ServiceNow/TACTiS](https://github.com/ServiceNow/TACTiS/tree/19df68b20b574f662fb1b2e1bf022f4116027f90)의 `tactis-2` branch를 commit `19df68b20b574f662fb1b2e1bf022f4116027f90`로 고정했다. [코드 검수](../evidence/0064-0065-tactis2/code-audit.json)에 파일별 URL·Git blob SHA·SHA-256·바이트·줄수·전체읽기범위가 있다.

전체로 읽은16파일: README.md,requirements.txt,requirements_research.txt,train.py,model의tactis/encoder/decoder/flow/marginal.py,gluon의trainer/network/estimator/metrics/backtest/dataset/utils.py다. Python3.10.8은README의 시험환경이고 GluonTS0.9.6/PyTorchTS0.6.0과torch>=1.13.1 등은 의존성 범위다. 완전히 고정한 재현 환경은 아니다.

Tree35항목/31blobs는 메타데이터 목록이다. 전체repo·노트북·원데이터를 읽거나 환경을 설치·실행하지 않았다. 이커밋이2024논문 실제실행판인지, 어떤config/seed/원배열로표와Newey-West/순위를만들었는지는미확인이다. 현재CLI기본값·코드경로의차이를논문결과의확정원인으로바꾸지않는다.

Conditional normalization 문헌 전체와65종합·후속 이력,기존부분기록과최종검색검수는남아있다.
