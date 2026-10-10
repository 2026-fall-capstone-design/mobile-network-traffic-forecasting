# H061 출처·판본 — Conditional normalization

[팀 기록](../records/0064-0065-conditional-normalization.md) · [명세](../evidence/0064-0065-conditional-normalization/manifest.json) · [목록](../catalog/history-061-sources.jsonl) · [검수](../verification/history-061.md)

11원본 그룹·22물리 경로를 연결했다. 새 정확사본은 수집 코드와 다운로드 JSON2개인 3파일·3,178바이트다. 64·65와 render log의 기존 정확사본3개를 재사용한다. PDF/TXT/HTML2개/PNG는 외부 참조5개다. 새 로컬 전체본문 독해1·전체JSON 독해2만 가산 대상으로 삼고, PDF의 여러 표현이나 재독해를 별도 연구로 세지 않는다.

| source_id | 팀 접근 경로 | 실제 확인 범위 |
|---|---|---|
| SRC-0022015 | [64_conditional_transform_review_plan.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022015.md.txt) | 64 전체 재대조. 달력 조건 변환·clustering·RCTL 질문을 연결한다. H055 전체 독해와 정확사본 재사용. |
| SRC-0022016 | [65_residual_and_transform_findings.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022016.md.txt) | 65 전체 재대조, 특히 §7. 당시 선택 논문 검토/코드 미검토와 이번 전체 논문·고정 코드 검수를 구분한다. |
| SRC-0062150 | [conditional_normalization_alternative_manifest.json](../evidence/0064-0065-conditional-normalization/originals/SRC-0062150.json) | 대체 다운로드 manifest 전체 1항목. 과거 arXiv 다운로드 성공 기록. 이번 공식 응답 검수와 구분. |
| SRC-0062151 | [conditional_normalization_manifest.json](../evidence/0064-0065-conditional-normalization/originals/SRC-0062151.json) | 다운로드 manifest 전체 3항목. 과거 Monash PDF403/abs·저자 페이지200 기록. 당시 접근 상태로 보존. |
| SRC-0063866 | [conditional_normalization_render_log.json](../evidence/0063-0065-ecai-interface/originals/SRC-0063866.json) | render log 전체 1항목 재대조. H055 정확사본·전체JSON 독해 재사용. 이번에는 해당 PNG도 실제 확인. |
| SRC-0022595 | [collect_conditional_normalization_65.py](../evidence/0064-0065-conditional-normalization/originals/SRC-0022595.py.txt) | 수집 스크립트 전체 텍스트 정적 독해. 다운로드·PDF 텍스트 추출 동작을 읽었으며 렌더링 코드는 없다. 실행/import하지 않음. |
| SRC-0062139 | [Conditional_normalization_2305.12651v1.pdf](https://arxiv.org/pdf/2305.12651v1) | 논문 35쪽 전체 텍스트·시각, 26그림/8번호식/알고리즘1/참고문헌30항목. 공식 v1 PDF와 바이트동일. 원실험 재현 없음. |
| SRC-0062140 | [Conditional_normalization_2305.12651v1.txt](https://arxiv.org/pdf/2305.12651v1) | 35쪽 전체 TXT를 PDF 추출과 대조. page wrapper·개행·외곽공백 정규화 뒤 일치. 독립 논문이나 실험이 아니다. |
| SRC-0062141 | [Conditional_normalization_abs.html](https://arxiv.org/abs/2305.12651v1) | HTML 서지·초록·판본이력·논문 링크 선택 독해. latest 응답과 바이트동일. 전체 HTML 독해 아님. |
| SRC-0062142 | [Conditional_normalization_author.html](https://robjhyndman.com/publications/condnormts.html) | 저자 HTML 서지·본문·공식 논문/패키지 링크 선택 독해. 현재 응답은 CSS·분류 링크만 다르고 보이는 본문/선택 메타데이터 동일. |
| SRC-0063856 | [Conditional_normalization_2305_12651v1_p5.png](https://arxiv.org/pdf/2305.12651v1#page=5) | 저장 PNG 5쪽 전체 시각 재대조. 조건부 평균·Gamma 분산·Kalman 보간과 역변환 식2–4. PDF의 파생물. |

## 논문 판본과 실제 읽은 범위

저자는 Puwasala Gamakumara, Edgar Santos-Fernandez, Priyanga Dilini Talagala, Rob J. Hyndman, Kerrie Mengersen, Catherine Leigh다. [arXiv history](https://arxiv.org/abs/2305.12651v1)는 2023-05-22 제출 v1만 표시한다. PDF표지는 2023-05-23, [저자 페이지](https://robjhyndman.com/publications/condnormts.html)는 2023-05-26과 Working paper, unpublished 서지를 표시한다. arXiv의 자유기입 comment에 Journal Article이 있다는 이유로 정식 학술지 게재를 확정하지 않는다.

2026-10-10 확인한 [v1 PDF](https://arxiv.org/pdf/2305.12651v1)는 HTTP200, 2,731,455바이트/SHA-256 `e0f7240180427365be983738b202a3b3ee5095c6c0c5eb471e2e8a1d68f92f7a`로 원본과 같다. 실제35쪽 전체 텍스트·시각,26그림·8번호식·알고리즘1·번호표0을 읽었다. arXiv comment의36쪽과 구분한다. 33–35쪽의 참고문헌30항목은 서지 독해이며 인용논문30편 전체 독해가 아니다. TXT35쪽은 page wrapper·개행·외곽공백 정규화 뒤 PDF 추출과 같다. 원PNG5쪽도 전체 시각으로 대조했다.

저장 arXiv HTML은 latest 응답41,554바이트와 같다. versioned v1 응답41,566바이트는 별도 해시다. 저장 저자 HTML35,765바이트와 현재35,808바이트는 다르지만 전체 diff에서 CSS3개와 분류 span→link 변경을 확인했으며 보이는 본문과 선택 메타데이터는 같다. HTML의 서지·초록/본문·이력·관련 링크만 읽었고 scripts·탐색·footer까지 읽었다는 뜻은 아니다. [판본 검사](../evidence/0064-0065-conditional-normalization/external-version-check.json)에 응답시각·바이트·해시를 저장했다.

2026-09-26의 수집 manifest는 Monash PDF403, arXiv PDF/abs 및 저자 페이지200을 기록한다. 이번에 Monash에 다시 접근한 것으로 쓰지 않는다. 원 render log의 visually_reviewed 표기와 이번 PNG 실제 시각 검수도 구분한다. 원 수집 코드는 실행하지 않았다.

## 공식 패키지와 접근 한계

논문이 연결한 [전체 분석 저장소](https://github.com/PuwasalaG/Conditional_normalisation_in_TSA)는 웹·GitHub API에서404였고, 저자의 공개 저장소12개 목록에서도 같은 이름을 찾지 못했다. 삭제·비공개 여부나 원인을 확정하지 않았으며 접근 제한을 우회하지 않았다.

공개 [conduits](https://github.com/PuwasalaG/conduits/tree/80a48697c05463afa641a318d8ab1f457bc79cc4)는 master의 commit `80a48697c05463afa641a318d8ab1f457bc79cc4`, 2023-04-18T09:13:28Z로 고정했다. 실제 tree는 `0f4b8dabad94b5a4fc3c0d407077f1d2350449da`다. 57항목·50blobs는 목록 메타데이터이며 전체 내용 독해가 아니다.

전체로 읽은18파일은 DESCRIPTION, NAMESPACE, LICENSE, LICENSE.md, README.md, README.Rmd, R/augment.R, conditional_acf.R, conditional_ccf.R, conditional_mean.R, conditional_var.R, conduits.R, data.R, estimate_dt.R, normalize.R, reexports.R, data-raw/NEON_PRIN.R, man/calc_dt_CI.Rd다. 합계2,423줄이며 [코드 검수](../evidence/0064-0065-conditional-normalization/code-audit.json)에 고정 URL·Git blob SHA·SHA-256·바이트·읽은 줄 범위가 있다. README의 링크된 그림과 다른32blobs, 의존 패키지 내부·데이터는 읽지 않았다.

DESCRIPTION의 MIT+LICENSE와 라이선스 파일을 확인했으며 API의 NOASSERTION 표기와 구분한다. R≥4.1, mgcv·forecast·broom 등은 완전 고정된 재현환경이 아니다. 실제 논문 실행판/Stan 코드·config·seed·원자료·posterior/split 배열·전체 비용은 확인하지 못했다. 설치·R/Stan 실행·난수 생성·NEON_TOKEN 조회·수집·.rda 다운로드/역직렬화는 수행하지 않았다.

65 전체 선행의 종합 판단과 후속 이력, 기존 부분 기록과 최종 검색 검수는 남아 있다.
