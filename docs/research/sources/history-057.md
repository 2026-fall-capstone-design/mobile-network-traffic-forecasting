# H057 출처와 판본 — KDD 잔차 보정

[팀 기록](../records/0063-0065-kdd-residual.md) · [명세](../evidence/0063-0065-kdd-residual/manifest.json) · [목록](../catalog/history-057-sources.jsonl) · [검수](../verification/history-057.md)

8개 고유 원본 그룹은 16개 물리 경로에 대응한다. 기존63·65 정확 사본2개를 재사용하고 외부 문헌/파생물6개는 metadata와 공식 링크로 연결했다. 새 원본 사본·로컬 본문·전체JSON·선택필드 증분은 없다. PDF20쪽·HTML과파생물은 같은 문헌의 서로 다른 표현이다.

| source_id | 팀 접근 경로 | 실제 확인 범위 |
|---|---|---|
| SRC-0022008 | [63_residual_interface_review_plan.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022008.md.txt) | H055 전체본문 검토 재사용. 잔차 target과 최종합성의 계획 범위를 재대조. 신규본문 가산0. |
| SRC-0022016 | [65_residual_and_transform_findings.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022016.md.txt) | H055 전체본문 검토 재사용, 전체원문 재대조. §3의증명/누수/비용 한계는당시이미지적; validation선택 표현은이번KDD원문에서명시확인못함. 다른4문헌/전체종합 미완료. |
| SRC-0063835 | [Multi_scale_residual_2606.10678_latest_v2.pdf](https://arxiv.org/pdf/2606.10678v2) | 20쪽 전체 본문·시각·47참고문헌을 읽음. 18표314행3191인쇄필드 대조. 공식v2PDF와 바이트 동일. 원 실험 재현 아님. |
| SRC-0063836 | [Multi_scale_residual_2606.10678_latest_v2.txt](https://arxiv.org/pdf/2606.10678v2) | 20쪽 wrapper/앞뒤공백 제거와 CRLF→LF 후 새PDF추출과 문자 동일. 전체PDF독해를 연결한 파생물이며 독립 논문 아님. |
| SRC-0063837 | [Multi_scale_residual_2606.10678v2.html](https://arxiv.org/html/2606.10678v2) | 과학본문287단위 중194정규화대응·93직접독해,401수식·18표·47서지 및 기타article text 확인. UI/JS/CSS실행 없음. 외부이미지2SVG/3PNG바이트 미확인. |
| SRC-0063838 | [Multi_scale_residual_2606.10678v2.html.text](https://arxiv.org/html/2606.10678v2) | HTMLParser data와 저장HTML.text는 개행/앞뒤공백 정규화 후 같다. 해당HTML 전체과학본문 독해를 연결한 파생물. |
| SRC-0063860 | [Multi_scale_residual_2606.10678_latest_v2_p11.png](https://arxiv.org/pdf/2606.10678v2#page=11) | 저장PDF11쪽 PNG 전체 시각 확인. A.1제곱노름과오차조건 재표현 확인. 별도논문/실험으로세지 않음. |
| SRC-0063861 | [Multi_scale_residual_2606.10678_latest_v2_p4.png](https://arxiv.org/pdf/2606.10678v2#page=4) | 저장PDF4쪽 PNG 전체 시각 확인. Fig2의잔차부호/겹침평균/표기 확인. 별도논문/실험으로세지 않음. |

TXT/PNG 링크는 내용 출처인 PDF/HTML이며 원 파생 파일 다운로드나 파생 해시 검증 경로가 아니다. 원 경로·크기·SHA-256은 명세에 보존했다. 공식 PDF v2는 이번에 HTTP200/6,615,803바이트/SHA-256 일치까지 확인했다. 65의 과거 versioned URL406은 당시 실패 기록으로 남긴다.

PDF20쪽의 본문·시각·47참고문헌을 모두 읽었다. 원TXT20쪽은 wrapper/앞뒤공백 제거와 CRLF→LF 후 이번 추출과 같다. HTML287단위 중194정규화 대응과93직접 독해,401수식 alttext·18표·47서지 및 기타article text를 확인했다. HTML.text는 같은 개행 정규화 후 저장HTML의data추출과 같다. 이 문자 대응을 수식 의미의 완전한 동일성으로 취급하지 않는다. C.3의½항은 PDF설명과HTML에차이가 있다.

## 보충한 외부 접근 확인

[외부 판본 검수](../evidence/0063-0065-kdd-residual/external-version-check.json)는 [공식 v2 초록](https://arxiv.org/abs/2606.10678v2), [공식 v2 PDF](https://arxiv.org/pdf/2606.10678v2), [Crossref DOI 서지](https://api.crossref.org/works/10.1145/3770855.3817960), 출판사PDF403을 구분한다. Crossref는 제목·저자·날짜·쪽수·서지 개수·라이선스 등 선택metadata를 읽었으며 전체reference JSON을 검토한 것은 아니다. 새 원본inventory번호를 만들지 않았다.

출판사 최종본의 서지는 162–173쪽·46참고문헌, 저장 arxiv는20쪽·47참고문헌이다. 출판사PDF본문 미독해 상태로 두 판본 내용이 같다고 하지 않는다. 검토한 원문·초록과 제목 검색에서 공식 구현 링크를 식별하지 못했지만 코드의 전역적 부재를 확인한 것은 아니다.

HTML의 외부2SVG/3PNG asset은바이트를확인하지않았다. 그림은PDF및원PNG로읽었다. 외부 논문·코드 전체를 재게시하거나 실행하지 않았다. 다른4문헌·65전체종합은남아있다.
