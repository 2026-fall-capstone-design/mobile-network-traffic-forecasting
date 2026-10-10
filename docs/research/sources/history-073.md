# H073 출처 — 72–75 저장 검색과 선택 열람 응답

[팀 기록](../records/0072-0075-saved-search-audit.md) · [보존 명세](../evidence/0072-0075-saved-search/manifest.json) · [응답별 역할·URL·위치](../evidence/0072-0075-saved-search/response-ledger.json) · [검수](../verification/history-073.md)

아래 저장 응답 11개를 전구간 읽었다. 실제 외부 페이지 전체를 읽었다는 뜻은 아니다. 긴 외부 발췌·사이트 UI·연락처·서명 URL을 새로 복사하지 않고, 원본 식별과 짧은 역할 분류를 게시한다. 원검색 파일의 팀 공유는 아직 미완료이며 공개 URL이 당시 응답과 같은 내용을 돌려준다고 보장하지 않는다.

| source_id | 원파일 이름 | 실제 첫 독해 범위 | 응답 블록 |
|---|---|---|---:|
| SRC-0063895 | 72_new_candidate_search.txt | 1–175,176–397행 |17|
| SRC-0063896 | 72_read_b1.json | status 전체; value UTF-16 문자1–17000,17001–끝 |4|
| SRC-0063897 | 72_read_c1.json | status 전체; value UTF-16 문자1–15000,15001–끝 |5|
| SRC-0063898 | 72_source_web.txt | 1–200,201–396행 |5|
| SRC-0063899 | 73_covariance_search.txt | 1–135,136–263행 |22|
| SRC-0063900 | 73_followup_1.json | status 전체; value UTF-16 문자1–16000,16001–32066 |18|
| SRC-0063901 | 73_mbrdr_access_search.txt | 1–289행 |13|
| SRC-0063902 | 73_predictable_subspace_search.txt | 1–190,191–386행 |16|
| SRC-0063903 | 73_review_leads.txt | 1–225,226–452행 |19|
| SRC-0063904 | 75_search_a.txt | 1–220,221–446행 |21|
| SRC-0063905 | 75_search_b.txt | 1–165,166–335행 |19|

JSON은 `status`와 `value` 두 필드이며 각각 원파일4행이다. PowerShell 첫 독해의 UTF-16 문자 위치와 공개 응답 목록의 Python Unicode 코드포인트 위치는 다른 좌표계다. 목록의 `location.field=value`는 디코딩한 값, `whole_text`는 TXT를 뜻한다. 목록의 행은1부터 양끝을 포함하고 문자 범위는0부터 끝을 포함하지 않는다. CRLF는 좌표 산출 때 LF로 정규화한다. 파일 SHA-256은 원바이트, 블록 SHA-256은 이 디코딩·정규화 뒤의 범위에 적용한다.

`response-ledger.json`의159개 항목은143개 검색 노출·13개 선택 open/find·2개 내부 오류·1개 브라우저 확인으로 나뉜다. URL 관계는 검색 노출의 연결이며 바이트 중복 판정이 아니다. 원본11그룹의 정확사본22경로는 [무결성 검수](../evidence/0072-0075-saved-search/provenance-check.json)에서 별도로 확인한다. 모든 외부 URL은 저장된 위치를 안내하는 것으로 이번 묶음에서 새 접속 검사를 하지 않았다.

기존 보존 findings도 이번 문서의 판단과 연결해 다시 읽었다. [SRC-0022023: 72–73 findings](../evidence/0072-0075-output-compression/originals/SRC-0022023.md.txt)는 전체52행, [SRC-0022029: 75 findings](../evidence/0072-0075-output-compression/originals/SRC-0022029.md.txt)는 전체18행이다. 두 자료는 새 본문 독해 수에 다시 가산하지 않는다. 이를 포함한 이번 출처 명세는13그룹·26경로이며, 새 원본 복사는0개다.

H070의 검색 미열람 표시는 당시 검토 범위로 보존한다. 이번에는 저장 TXT8개와 JSON3개를 실제 읽었지만 연결 논문·도표·코드를 전부 확보하거나 재현한 것은 아니다. H071·H072의 일차자료 검수와 접근 공백, 앞으로 읽을 후보의 원문을 구분한다. 같은 에이전트가 작성 후 관련 원문을 다시 대조하며 독립 심사로 표시하지 않는다.
