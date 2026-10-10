# H068 출처·판본 — DeepCog의 비용과 공개 코드

작성 후 44개 주장을 원문과 별도로 대조했다. 아래 범위는 실제 확인한 자료이며 관련 패킷 전체나 원실험 재현을 뜻하지 않는다.

[팀 기록](../records/0069-0071-deepcog.md) · [명세](../evidence/0069-0071-deepcog/manifest.json) · [목록](../catalog/history-068-sources.jsonl) · [검수](../verification/history-068.md)

기존69·71과 보고서·읽기 범위의 정확사본4개, DeepCog의 표현6개를 연결한다. 총10원본그룹·20물리경로이며 새 원본 복사는0이다. H066에 남긴 당시 미독해 명세는 보존한다.

| source_id | 팀 접근 | 실제 확인 범위 |
|---|---|---|
| SRC-0022020 | [69 계획](../evidence/0069-0071-peak-objective/originals/SRC-0022020.md.txt) | 전체26행 재대조 |
| SRC-0022022 | [71 판단](../evidence/0069-0071-peak-objective/originals/SRC-0022022.md.txt) | 전체43행 재대조 |
| SRC-0000152 | [당시 공개 보고서](../evidence/0069-0071-peak-objective/originals/SRC-0000152.md.txt) | 전체100행 재대조 |
| SRC-0063462 | [당시 읽은 범위](../evidence/0069-0071-peak-objective/originals/SRC-0063462.json) | 전체93행 재대조. 당시의 선택독해와 이번 전체 저자본 독해를 구분 |
| SRC-0063442 | [IMDEA 저자본 PDF](https://dspace.networks.imdea.org/bitstream/handle/20.500.12761/770/bega_jsac19.pdf?isAllowed=y&sequence=1) | 표지1+본문15쪽 전체 텍스트·시각, 그림11·각주7·감사·서지43항목·약력5 |
| SRC-0063443 | [대응 PDF](https://dspace.networks.imdea.org/bitstream/handle/20.500.12761/770/bega_jsac19.pdf?isAllowed=y&sequence=1) | 원TXT1969행의16본문을 읽은 PDF 추출문과 페이지별 `strip` 후 정확동일 확인 |
| SRC-0063444 | [기관 서지](https://dspace.networks.imdea.org/handle/20.500.12761/770) | HTML458행의 전체 가시 내용·메타44개·주석·inline script·관련 링크 정적 확인, 현재판 diff2곳 |
| SRC-0063464 | [PDF11쪽](https://dspace.networks.imdea.org/bitstream/handle/20.500.12761/770/bega_jsac19.pdf?isAllowed=y&sequence=1#page=11) | 원PNG 전체 시각: Fig6·비교군·offset과 MAE-pre 인쇄식 |
| SRC-0063465 | [PDF12쪽](https://dspace.networks.imdea.org/bitstream/handle/20.500.12761/770/bega_jsac19.pdf?isAllowed=y&sequence=1#page=12) | 원PNG 전체 시각: Fig7의24값·oracle 예외 |
| SRC-0063466 | [PDF8쪽](https://dspace.networks.imdea.org/bitstream/handle/20.500.12761/770/bega_jsac19.pdf?isAllowed=y&sequence=1#page=8) | 원PNG 전체 시각: 이상 비용·식1–2·α 단위 |

TXT·PNG 링크는 대응 논문 접근용이며 해당 파생파일 자체의 바이트 다운로드 주소가 아니다. 정확한 원경로·크기·해시·동일사본은 명세에 있다. TXT raw행과 HTML raw태그 모든행의 독립 수동독해로 세지 않는다. 연결된 JavaScript도 실행하지 않았다.

## 판본과 정적 코드

2026-10-10 받은 기관 PDF는9,797,527바이트, SHA-256 `e9aa96c24631f7532e3b5b5a6824f1a2c706c1f19ae897f4c00d3139169ef8e9`로 보존 원본과 같다. 서지의2020-02와 본문의2019 수락 정보는 구분한다. HTML의 `dateAccepted`는2021로 표시되지만, 이 저장소 값을 논문 본문에 적힌2019 수락일 대신 사용하지 않는다. 원HTML과 현재HTML의 메타44개·가시 내용은 같고 인물 browse 식별자·Eduroam footer 링크만 바뀌었다.

외부 [공개 저장소의 고정 커밋](https://github.com/wnlUc3m/deepcog/tree/b607e2c370ad222046dfe92ef4f5a7f7f94284e5)의 전체 tree는 README·DeepCog.ipynb 두 파일이다. [README](https://github.com/wnlUc3m/deepcog/blob/b607e2c370ad222046dfe92ef4f5a7f7f94284e5/README.md)는 INFOCOM2019 논문을 인용한다. [notebook](https://github.com/wnlUc3m/deepcog/blob/b607e2c370ad222046dfe92ef4f5a7f7f94284e5/DeepCog.ipynb)의10셀 중 code5셀, source51행과 나머지 Markdown·메타·저장 출력 모두를 정적으로 읽었다. AST는 구조 확인에만 썼다.

저자본 그림2의 decoder128→64→32→출력과 notebook64→32→출력, 식1의 양초과 기울기와 notebook의 `α/(1−εα)`, 본문 미확인 ε 수치와 notebook의 .1을 구분한다. 전역 factory 이름과 compile 호출 이름도 다르며 데이터·generator·실험별 비교 코드가 없다. 이것은 확인한 commit의 범위이고 다른 판본이나 비공개 구현 전체의 부재를 주장하지 않는다.

notebook 안의 Python3.5.6 메타데이터·execution_count·TensorFlow 안내 출력은 당시 저장 내용이다. 현재 실행 성공이나 완전한 환경 명세가 아니다. 새 모델 fit·forward, 역사 코드 import·실행, pickle 로딩·난수 생성은 하지 않았다. 원코드 파일은 재배포하지 않고 commit 링크·해시·읽은 범위·차이만 남겼다.

## 아직 확보하지 못한 근거

[DOI](https://doi.org/10.1109/JSAC.2019.2959245)는 IEEE 문서8932440로 이동했다. 일반 요청은 HTTP202의 빈 본문, 웹 열람은 로봇 확인 화면이었다. 검색에서 찾은 [UC3M postprint](https://e-archivo.uc3m.es/bitstreams/82d88c55-94ee-4ee8-8878-d70951f51494/download)는 일반 요청500·웹403으로 본문을 얻지 못했다. 검색 snippet을 최종 PDF 독해로 세지 않는다.

원데이터·모든 전처리 구간·패키지 버전·seed·그림 원배열·JSAC 비교군 전체 구현·실제 시간/메모리는 미확인이다. 다른 논문이나 INFOCOM 예시를 같은 실험으로 합치지 않는다. SIU2026과 보존 검색 원문도 후속 범위다.

[판본 감사](../evidence/0069-0071-deepcog/external-version-check.json)에 요청 결과·고정 commit·해시·차이를, [형식 감사](../evidence/0069-0071-deepcog/format-audit.json)에 실제 읽은 범위를 남겼다. 목록의 파생표현 수와 외부 원논문·코드의 독해 범위를 별도로 센다.

후속 [H069의 출처와 읽은 범위](../sources/history-069.md)에서 SIU 기관 HTML·저장 검색8내용을 검수했다. 이 문서의 앞선 대기 표시는 당시 범위로 보존한다. SIU 논문 본문·실행 자료, 첫 검색 묶음 원문과 검색전용 후보의 본문은 계속 미확인이다.
