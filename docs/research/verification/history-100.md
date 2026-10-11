# H100 문헌 대조 검수

[기록](../records/0100-cesnet-isp-data-semantics.md) · [주장별 좌표](history-100-claims.json) · [실제 읽기](../evidence/0100-cesnet-isp/read-scopes.json)

상태: 28개 주장·7개 묶음의 작성 후 원문·그림 대조 완료. [재독 범위와 판정](history-100-second-pass.json), [문서 검사](history-100-document-check.json)를 연결한다.

본문의 인용 의미 구간을 두 HTML의 문단·표·MathML과 TXT 지정행으로 다시 읽었다. CESNET10그림과 ISP PDF6쪽도 작성 후 다시 확인했다. HTML markup 전체를 읽었다고 표시하지 않는다. C01의 발행정보 좌표를 TXT52–54로 보강했다.

첫 읽기는 두 논문의 저장 HTML/TXT4그룹과 HTML 표13개·ISP MathML96개다. CESNET 그림10개는 공식 링크의 현재 이미지, ISP의7그림 및 표 형식 Fig.2는 기존 PDF6쪽으로 확인했다. 보조 PDF의 나머지3쪽과 원82의11자료 그룹·snapshot24 연혁은 완료 처리하지 않는다.

표의 저자 보고값과 작성자의 해석, trimmed 평균과 그림의 이상치, 단순 전사와 모델 재현을 구별한다. 원 연구 코드·모델 실행0이며 독립 검토자의 검증으로 표시하지 않는다.

표 전사 JSON의 TableII 두 셀(IP Sample·10% few-shot R²)은 MathML alttext의 LaTeX 기호를 `±`로 정규화했다. 평균·표준편차·부호는 유지했다. 원래 셀 문자열과 행·열 위치를 [전사 자료](../evidence/0100-cesnet-isp/reported-tables.json)의 `cell_text_normalizations`에 보존했으며, 문서 검사는 이 두 변환을 적용한 뒤 저장 HTML의 모든 전사 셀과 대조한다.
