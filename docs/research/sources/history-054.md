# H054 출처와 실제 열람 범위

[팀 기록](../records/0059-optimal-lookback.md) · [원문 명세](../evidence/0059-optimal-lookback/manifest.json) · [출처 목록](../catalog/history-054-sources.jsonl)

원본16고유 바이트 묶음·32경로를 연결한다. 기존 정확 사본6개를 재사용하고 외부 원본10개는 메타데이터와 공식 링크를 둔다. 새 보존 사본은0개다. 추가 외부자료3개는 로컬 원본의 독해 수로 가산하지 않는다.

| source_id | 자료 | 실제 확인 범위 |
|---|---|---|
| SRC-0021920 | [59_history_grouping_review_plan.md](../evidence/0059-optimal-lookback/../0059-0062-history-grouping/originals/SRC-0021920.md.txt) | H051에서 전체 읽은 59 계획·62 판단을 재사용하고 이번에 62 전체를 다시 대조 |
| SRC-0021984 | [62_history_grouping_findings.md](../evidence/0059-optimal-lookback/../0059-0062-history-grouping/originals/SRC-0021984.md.txt) | H051에서 전체 읽은 59 계획·62 판단을 재사용하고 이번에 62 전체를 다시 대조 |
| SRC-0062781 | [fetch_log.json](../evidence/0059-optimal-lookback/../0059-alw/originals/SRC-0062781.json) | H053에서 전체 읽은 수집·개정·검토범위·렌더 JSON을 재사용; 문헌 열람과 취득 기록을 구별 |
| SRC-0062782 | [latest_and_code_log.json](../evidence/0059-optimal-lookback/../0059-alw/originals/SRC-0062782.json) | H053에서 전체 읽은 수집·개정·검토범위·렌더 JSON을 재사용; 문헌 열람과 취득 기록을 구별 |
| SRC-0062790 | [review_scope.json](../evidence/0059-optimal-lookback/../0059-alw/originals/SRC-0062790.json) | H053에서 전체 읽은 수집·개정·검토범위·렌더 JSON을 재사용; 문헌 열람과 취득 기록을 구별 |
| SRC-0062806 | [render_log.json](../evidence/0059-optimal-lookback/../0059-alw/originals/SRC-0062806.json) | H053에서 전체 읽은 수집·개정·검토범위·렌더 JSON을 재사용; 문헌 열람과 취득 기록을 구별 |
| SRC-0062783 | [optimal_lookback_2511_12791v1.html](https://arxiv.org/html/2511.12791v1) | 표시본문과전체MathML대조;v3 688줄본문, v1 전체canonicaldiff/수식split6묶음 비교;외부SVG는별도미보유이며해당PDF그림시각검토로내용확인 |
| SRC-0062784 | [optimal_lookback_2511_12791v1.pdf](https://arxiv.org/pdf/2511.12791v1) | 13쪽 본문/부록/참고문헌/그림/수식;v1은v3와동일본문재사용+전체고유diff/시각검토,2/8쪽pixel동일재사용 |
| SRC-0062785 | [optimal_lookback_2511_12791v1.txt](https://arxiv.org/pdf/2511.12791v1) | 원PAGE wrapper제외13쪽freshPDF본문과완전일치;독립연구내용재가산없음 |
| SRC-0062786 | [optimal_lookback_2511_12791v3.html](https://arxiv.org/html/2511.12791v3) | 표시본문과전체MathML대조;v3 688줄본문, v1 전체canonicaldiff/수식split6묶음 비교;외부SVG는별도미보유이며해당PDF그림시각검토로내용확인 |
| SRC-0062787 | [optimal_lookback_2511_12791v3.pdf](https://arxiv.org/pdf/2511.12791v3) | 13쪽 본문/부록/참고문헌/그림/수식;v1은v3와동일본문재사용+전체고유diff/시각검토,2/8쪽pixel동일재사용 |
| SRC-0062788 | [optimal_lookback_2511_12791v3.txt](https://arxiv.org/pdf/2511.12791v3) | 원PAGE wrapper제외13쪽freshPDF본문과완전일치;독립연구내용재가산없음 |
| SRC-0062789 | [optimal_lookback_history.html](https://arxiv.org/abs/2511.12791v3) | 과거arxiv메타HTML 표시본문전체독해,원시stylesheet/script은표현요소 |
| SRC-0062803 | [optimal_lookback_2511_12791v3_p6.png](https://arxiv.org/pdf/2511.12791v3) | 원미리보기6/7/9쪽 각각시각독해;새120dpi렌더와별도원본 |
| SRC-0062804 | [optimal_lookback_2511_12791v3_p7.png](https://arxiv.org/pdf/2511.12791v3) | 원미리보기6/7/9쪽 각각시각독해;새120dpi렌더와별도원본 |
| SRC-0062805 | [optimal_lookback_2511_12791v3_p9.png](https://arxiv.org/pdf/2511.12791v3) | 원미리보기6/7/9쪽 각각시각독해;새120dpi렌더와별도원본 |

두 PDF의13쪽 전체 내용·부록·참고문헌·그림을 확인했다. v3 시각13쪽, v1 시각11쪽을 직접 읽고2·8쪽은 pixel동일성에 따라 재사용했다. v3 HTML 표시본문688줄·article MathML487개와 밖의H1개, v1의 전체 canonical 차이·480+1개를 대조했다. 원 TXT26쪽은 PAGE wrapper를 제외하고 새 추출과 같다. 원 PNG3개는 새 렌더와 구분해 각각 읽었다. 파생 TXT/PNG/수식 수를 새 독립 연구기록으로 가산하지 않는다.

수식76→83개는6분리묶음에서7개가 늘어난 것이다. 그림의 제목·축·범례·크기는 바뀌었고, 외부 SVG 원바이트의 동일성은 미확인이다. 원시 HTML의 stylesheet/script은 연구 본문과 구분한다. 제출 이력 HTML의 표시본문 전체를 읽었다.

| 추가 참조 | 자료 | 실제 범위 |
|---|---|---|
| HL-SUP-01 | [공식 자료](https://ojs.aaai.org/index.php/AAAI/article/view/39781) | 공식 서지·DOI·권호·쪽·발행일; 저장 gzip을 별도 사본에서 해제 |
| HL-SUP-02 | [공식 자료](https://ojs.aaai.org/index.php/AAAI/article/download/39781/43742) | 8쪽 중 PDF 6/7쪽(인쇄 25828/25829)의 정리4 문장·증명만 본문과 시각 대조. 나머지6쪽 미독해 |
| HL-SUP-03 | [공식 자료](https://math.ucla.edu/~njhu/notes/nla/lsq/leastsquares/#projections) | 웹 본문을 읽고 볼록집합 투영의 부등식 및 닫힌 선형 부분공간의 직교 조건만 검수 근거로 사용 |

원본에 없는 v2와 정식 출판본의 나머지6쪽은 읽지 않았다. [저장 폴더32묶음·64경로](../verification/history-054-packet-scope.json)는 이전 ALW 검수와 이번 horizon 검토에 전수 연결된다. 외부SVG·원실행자료·원격tree의 다른코드까지 완료한 것이 아니다.

새 로컬 전체본문·전체JSON·선택필드 독해 집계는 각각0이다. 문헌 두판본의 새 검토는 별도 범위로 기록하며, 이전59/62 및 네JSON을 중복 가산하지 않는다. 원 연구 스크립트 실행·모델 호출·무작위 생성은0이다.
