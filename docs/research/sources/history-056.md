# H056 출처와 실제 읽은 범위

[팀 기록](../records/0063-0065-heatload-residual.md) · [명세](../evidence/0063-0065-heatload-residual/manifest.json) · [기계 판독 목록](../catalog/history-056-sources.jsonl) · [검수](../verification/history-056.md)

63·65의 H055 전체 독해와 보존본을 재사용하고 Heatload 부분을 확장했다. 아래 15개 원본 그룹은 30개 물리 경로에 대응한다. 기존 사본 2개, 외부 metadata 13개이며 새 원본 사본은 없다. 전체 JSON 3개만 새 읽기 증분이고, 외부 논문·코드·파생물은 별도 범위로 집계한다.

| source_id | 팀 접근 경로 | 실제 읽은 범위 |
|---|---|---|
| SRC-0022008 | [63_residual_interface_review_plan.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022008.md.txt) | H055 전체 독해를 재사용. 7–18/25–27행의 입력·잔차 목표·다중 해상도 계획과 손실 동치를 다시 대조. 새 본문 가산 0. |
| SRC-0022016 | [65_residual_and_transform_findings.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022016.md.txt) | H055 전체 독해를 재사용. 7–15/27–33/67/74–78행의 Heatload 판단·비용·신규 실행 0을 다시 대조. 다른 5문헌과 전체 종합 미완료. |
| SRC-0063830 | [Heatload_2608.20024v1.html](https://arxiv.org/html/2608.20024v1) | 과학 본문 245단위·수식 alttext 147개·표 12부분·참고문헌 52개 전체 확인. PDF 정규화 대응 149단위와 나머지 96단위 직접 독해. UI/JS/CSS 비실행. 외부 그림 asset 바이트 미검증. |
| SRC-0063831 | [HTML — 원 HTML.text의 내용 출처](https://arxiv.org/html/2608.20024v1) | 저장 HTML의 전체 data 텍스트 추출과 문자 동일 확인. 과학 내용 범위는 HTML/PDF와 같으며 파생 텍스트를 독립 논문으로 세지 않음. |
| SRC-0063832 | [Heatload_2608.20024v1.pdf](https://arxiv.org/pdf/2608.20024v1) | 전체 33쪽 본문·참고문헌·보충자료 독해, 그림/표 있는 19쪽 시각 확인. 표 11개 79행과 그림 S1/S2의 총 933개 인쇄 데이터 수치 검수. 원 실험 재현 아님. |
| SRC-0063833 | [PDF — 원 TXT의 내용 출처](https://arxiv.org/pdf/2608.20024v1) | page wrapper를 제외한 33쪽 본문이 PDF의 새 추출과 문자 동일. 전체 PDF 독해를 연결한 파생물. |
| SRC-0063834 | [Heatload_abs.html](https://arxiv.org/abs/2608.20024v1) | 저장 초록 페이지의 visible text 5,543자·서지 메타데이터 전체 확인. 원문 라이선스 링크와 PDF/HTML의 인용번호 차이 확인. |
| SRC-0063841 | [heatload_README.md](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/README.md) | README 전체 125줄. 공개 범위·실행 예제·자료 제한·환경 보고를 확인. 고정 raw 바이트 동일, 명령 실행 없음. |
| SRC-0063842 | [heatload_commit.json](https://api.github.com/repos/benspoek/tsfm-heatload/commits/b86ec88019f850eadb544c95ed257cce486be111) | 저장 commit JSON 전체. 고정 commit 날짜와 commit.tree.sha, 파일 변경 metadata 확인. 실행 결과 증거와 구분. |
| SRC-0063843 | [heatload_repo.json](https://api.github.com/repos/benspoek/tsfm-heatload) | 저장 repo JSON 전체. 과거 metadata snapshot이며 현재 API 응답의 바이트 동일성 보장 아님. |
| SRC-0063844 | [heatload_scripts__full_year_forecasting_utils.py](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/scripts/full_year_forecasting_utils.py) | 전체 722줄 정적 독해·AST 파싱. 시각 검증·집계·synthetic clock·미래 target 제외·q50·지표 확인. import/실행 없음. |
| SRC-0063845 | [heatload_scripts__stacked_residual_full_year_2024.py](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/scripts/stacked_residual_full_year_2024.py) | 전체 640줄 정적 독해·AST 파싱. 실제 잔차 target과 합산·발행시각 제한·보간·두 타이머·dry-run 경로 확인. import/실행 없음. |
| SRC-0063846 | [heatload_scripts__tabpfn_ts_heat_forecast.py](https://github.com/benspoek/tsfm-heatload/blob/b86ec88019f850eadb544c95ed257cce486be111/scripts/tabpfn_ts_heat_forecast.py) | 전체 506줄 정적 독해·AST 파싱. 단일 예제 설정·미래 target 제외·target/q50 처리·초기화 포함 타이머 확인. import/실행 없음. |
| SRC-0063847 | [heatload_tree.json](https://api.github.com/repos/benspoek/tsfm-heatload/git/trees/b86ec88019f850eadb544c95ed257cce486be111?recursive=1) | 저장 tree JSON 전체. 파일 목록과 12개 고정 파일의 blob SHA-1/크기 대조. 목록의 다른 코드·데이터 본문을 읽었다는 뜻 아님. |
| SRC-0063859 | [PDF 21쪽 — 원 PNG의 내용 출처](https://arxiv.org/pdf/2608.20024v1#page=21) | 저장 PDF 21쪽 PNG 전체 시각 확인. Table 5–7의 본문 수치와 연결. 독립 논문·실험으로 세지 않음. |

파생 TXT/PNG의 링크는 내용 출처인 PDF/HTML이다. 그 링크가 원 파생 파일을 다운로드하거나 원 파생 해시를 검증하는 경로는 아니다. 원 경로·크기·SHA-256은 명세에 보존했다. 현재 repo API 응답은 과거 저장 JSON snapshot과 다를 수 있다.

PDF 33쪽의 본문·참고문헌·보충자료를 읽었고 시각 19쪽은 1/3/6/7/10/12/13/14/15/16/17/18/19/20/21/30/31/32/33쪽이다. 그림 7과 S2는 확대해서 확인했다. 원 TXT 33쪽의 추출 동등성, HTML의 과학 본문 245단위·수식 alttext 147개·참고문헌 52개와 12표 부분을 대조했다. HTML 외부 SVG/PNG의 원격 바이트는 검증하지 않았다.

## 이번에 읽은 고정 외부 보충 자료

[외부 참조 명세](../evidence/0063-0065-heatload-residual/external-fixed-references.json)는 commit `b86ec88019f850eadb544c95ed257cce486be111`의 raw 12개 파일을 연결한다. 처음 4개는 위 README/저장 코드와 바이트가 같고, 나머지 8개는 다음 보충 자료다. 원본 inventory의 source_id나 과거 읽기 횟수를 새로 만들지 않았다.

| 외부 ref | 파일 | 전체 읽은 줄 |
|---|---|---:|
| EXT-H056-05 | [scripts/utils.py](https://raw.githubusercontent.com/benspoek/tsfm-heatload/b86ec88019f850eadb544c95ed257cce486be111/scripts/utils.py) | 89 |
| EXT-H056-06 | [requirements.txt](https://raw.githubusercontent.com/benspoek/tsfm-heatload/b86ec88019f850eadb544c95ed257cce486be111/requirements.txt) | 13 |
| EXT-H056-07 | [.python-version](https://raw.githubusercontent.com/benspoek/tsfm-heatload/b86ec88019f850eadb544c95ed257cce486be111/.python-version) | 1 |
| EXT-H056-08 | [LICENSE](https://raw.githubusercontent.com/benspoek/tsfm-heatload/b86ec88019f850eadb544c95ed257cce486be111/LICENSE) | 21 |
| EXT-H056-09 | [THIRD_PARTY_NOTICES.md](https://raw.githubusercontent.com/benspoek/tsfm-heatload/b86ec88019f850eadb544c95ed257cce486be111/THIRD_PARTY_NOTICES.md) | 84 |
| EXT-H056-10 | [flensburg/demand/heat/heat_dh_metadata.json](https://raw.githubusercontent.com/benspoek/tsfm-heatload/b86ec88019f850eadb544c95ed257cce486be111/flensburg/demand/heat/heat_dh_metadata.json) | 20 |
| EXT-H056-11 | [flensburg/weather/flensburg_weather_temperature_metadata.json](https://raw.githubusercontent.com/benspoek/tsfm-heatload/b86ec88019f850eadb544c95ed257cce486be111/flensburg/weather/flensburg_weather_temperature_metadata.json) | 36 |
| EXT-H056-12 | [flensburg/weather/representative_weeks_2024.csv](https://raw.githubusercontent.com/benspoek/tsfm-heatload/b86ec88019f850eadb544c95ed257cce486be111/flensburg/weather/representative_weeks_2024.csv) | 4 |

고정 12파일의 HTTP 200·크기·Git blob SHA-1을 확인했다. commit.tree.sha와 저장 tree.root.sha는 서로 다른 필드를 그대로 보존한다. 코드 AST 파싱은 했지만 import/실행하지 않았다. 다른 tree 항목의 목록을 읽은 것을 해당 코드·CSV 본문 검수로 세지 않는다.

[H057 후속 범위](history-057.md)는KDD전체본문·표·수식·판본검수를추가합니다. 현재남은다른문헌은PLOS·GP-Copula·TACTiS-2·conditional normalization의네가지이며65전체종합은미완료입니다. 기존범위와해시는당시snapshot으로보존합니다.

[H058 후속 범위](history-058.md)는PLOS copula의전체PDF·원파생물검수를추가합니다. 현재다른세문헌·65전체종합은남아있으며기존범위·해시는당시snapshot으로보존합니다.
