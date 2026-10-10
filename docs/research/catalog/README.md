# 자료 목록과 출처 매핑

[history-024 목록](history-024-sources.jsonl)은 39–40의 새 원문 5개(19,293 bytes), 일차자료 metadata 8개, 해시 전용 4개를 연결한다. [읽은 범위](../sources/history-024.md)는 메모·코드 3개와 작은 JSON 2개 전체, 세 논문 지정 텍스트 22쪽/시각 9쪽, 설치 코드 선택 구간이다. 원문의 68G 비용과 pinned 구현의 최대 289G 정정을 구별한다.

[history-023 목록](history-023-sources.jsonl)은36–38의 새 원문10개·기존 원장1개·지정 일차자료 metadata11개·해시 전용4개를 연결한다. [실제 열람 범위](../sources/history-023.md)는 메모/코드5개·작은 JSON5개 전체와 세 논문의 지정45쪽/시각16쪽이다. 전체 논문 완료로 세지 않으며 원문의 fixed-k 표현을 일차문헌 범위로 좁힌 정정을 보존한다.

[inventory.jsonl.gz](inventory.jsonl.gz)는 2026년 10월 8일 조사한 48,149개 메타데이터 항목의 UTF-8 JSONL을 gzip으로 압축한 파일이다. 원문 내용은 포함하지 않는다. [집계와 파일 해시](scope-summary.json), [조사 방법과 한계](../verification/inventory-2026-10-08.md)를 함께 읽는다.

각 줄은 `source_id`, `kind`, 원본 루트 기준 `path`, 확장자·크기·수정 시각, `sha256`, 포함·제외 상태와 이유를 담는다. 압축 내부 항목에는 `container_id`, `container_path`, `member_index`가 있다. `mtime_ns`는 물리 파일 수정 시각이며 압축 멤버의 시각 필드는 형식에 따라 다르다. 경로는 원본 루트 별칭 `Tab-ICL`을 기준으로 한다. 외부 공용 런타임의 개인 경로는 별칭으로 표시하고 로컬 매핑에만 보존한다.

`representative_source_id`는 같은 SHA-256을 갖는 포함 대상의 대표다. 대표를 읽지 않은 상태는 `exact_duplicate_pending_representative_review`이며 내용 검토 완료를 뜻하지 않는다. 라이브러리 제외·캐시 제외·동일 사본 연결은 서로 다른 처리 상태다. 제외 파일도 목록에서 지우지 않는다. 포함된 고유 파일 16,326개에는 배열·환경 자료도 있으므로 연구 기록 수로 세지 않는다.

목록 상태와 본문 검토는 따로 관리한다. [첫 시범 출처 목록](pilot-001-sources.jsonl)은 635–638을, [RCTL 출처 목록](pilot-002-sources.jsonl)은 639에 사용한 source_id·해시·보존 사본·실제 검토 범위와 기록 번호를 연결한다. [첫 출처 안내](../sources/pilot-001.md)와 [RCTL 출처 안내](../sources/pilot-002.md)에서 원문과 정리본을 오갈 수 있다.

후속 묶음은 [640 출처](pilot-003-sources.jsonl), [641 출처](pilot-004-sources.jsonl), [642 출처](pilot-005-sources.jsonl)로 이어진다. [642 판본 안내](../sources/pilot-005.md)는 Word·렌더 이미지·생성 코드의 실제 읽기 범위와 목록 밖에서 확인한 외부 원문을 구분한다. 파일 보존, 해시 확인, 본문 열람, 주장 검증은 서로 다른 상태다.

[초기 01–02 출처](pilot-006-sources.jsonl)는 자료 진단·CPU 동작·후보 설계를 연결한다. [초기 출처 안내](../sources/pilot-006.md)는 원문13개, 외부 자료와 대용량 자산9건, 파생 날짜 발췌를 구분한다. 작은 배열 검산과 별도 로컬 H5 확인을 같은 CI 실행으로 표현하지 않는다.

[633 출처](pilot-007-sources.jsonl)는 직접 예측 정확도와 후속 소속 효용이 달랐던 부정 결과를 연결한다. [출처 안내](../sources/pilot-007.md)는173개 경로의 본문/필드/해시 확인을 구분하며, 정확한 이전 사본을 재사용한다. 선행 기록에서 필요한 근거를 읽은 것과 그 연구 전체 정리 완료를 구분한다.

Python으로 목록을 읽는 예:

```python
import gzip
import json

with gzip.open("docs/research/catalog/inventory.jsonl.gz", "rt", encoding="utf-8") as stream:
    for line in stream:
        item = json.loads(line)
        if item["source_id"] == "SRC-0021997":
            print(item)
```

초기 B1·B2는 [history-001 목록](history-001-sources.jsonl)과 [열람 범위](../sources/history-001.md)에서 98개 경로를 추적한다. 본문 전체18개, 지정 필드79개, 해시만1개이며, 별도 H5 지정 열 검사도 연결했다. 기록03·04·06·07을 통합했다. 후속08·09는 [history-002 목록](history-002-sources.jsonl)과 [열람 범위](../sources/history-002.md)에 원문6경로(전구간3·지정필드3), 새 보존4개와 기존 배열2개 재사용을 연결했다. 05는 다음 네 묶음으로 부분 통합했다.

[history-003 목록](history-003-sources.jsonl)은05 원문1개와 외부 문헌 자료5개를 구분한다. [읽은 범위](../sources/history-003.md)의 네 논문·다섯 자료와 별도 웹 논문1편을 대조했다. [history-004 목록](history-004-sources.jsonl)은 기존 보존 원문9개 재사용과 새 일차자료11개(8편)를 연결하고, UPC의 기존 외부 검토를 [별도로 표시](../sources/history-004.md)한다. 새 원문 사본은0개다.

[history-005 목록](history-005-sources.jsonl)은 기존 보존8개를 재사용하고 공식 코드6개·설치metadata·checkpoint config의 지정 검토와 ZIP 해시/선택 member를 연결한다. [읽은 범위](../sources/history-005.md)는 코드전체2·부분4·metadata부분1·checkpoint설정1을 구분한다. 새 원문 사본0이며 외부 identity 등록을 팀 저장소의 원문 보존 완료로 세지 않는다.

[history-006 목록](history-006-sources.jsonl)은05 원문1개 재사용과 관련 여섯 논문의 텍스트6개·PDF6개를 연결한다. [읽은 범위](../sources/history-006.md)는 지정 줄과 PDF의 지정 내용17쪽이다. 전논문·다른 개정본 완료로 집계하지 않았다. 회귀 TabPFN 후속과05의 남은 판단 연결을 이어가며, 원문69행 열람을 전체 주장 검수 완료로 표시하지 않는다.

[history-007 목록](history-007-sources.jsonl)은10–12의 원문9개 새 보존과 기존2개 재사용을 연결한다. [읽은 범위](../sources/history-007.md)는 본문전체5개·JSON전체키2개·배열2개 및 이전 자료의 지정 필드를 구분한다. 고정 GECOS 코드와 대용량 H5 metadata는 기존 자료를 재검토한2건이며 새 논문이나 팀 원자료 보존 완료로 세지 않는다. 원 UPC의 지정 두 쪽은 별도 외부 검토에 연결했다.

[history-008 목록](history-008-sources.jsonl)은 13/14와 15 수치·방법 부분의 16출처를 연결한다. 새 원문 13개와 기존 배열 3개 재사용이며, [읽은 범위](../sources/history-008.md)는 본문 전체 5개·JSON 전체 키 5개·신규 배열 3개의 지정 필드다. 15의 전체 62행을 읽은 것과 §3 여섯 문헌의 주장 검수는 별도 작업이다.

[history-009 목록](history-009-sources.jsonl)은15 원문 재사용1개·새 입수 기록1개·문헌 텍스트6개/PDF6개의 메타데이터를 연결한다. [읽은 범위](../sources/history-009.md)는 지정 줄과 PDF29쪽의 지정 내용이며 전논문 완료0편이다. 당시 문헌 판단을 대조했고 원문 표현·비율 공백4건을 보존했다. 15의 완료 호출 누적은 [H015 비용 원장](../records/0015-0021-cumulative-costs.md)에서 대조했으며, 나머지 후속 연결과 전체 실패 비용은 남아 있다.

[history-010 목록](history-010-sources.jsonl)은16–17의 원문8개 새 보존과 기존2개 재사용, H5 metadata1건을 연결한다. [읽은 범위](../sources/history-010.md)는 텍스트 전체3개·JSON 전체키3개·새 배열2개 및 재사용 자료의 지정 범위다. 저장 성능과 H5 지정 구간의 입력·정답을 대조했으며,H010 시점에서 세 문헌 방법과 후속 공간 정보 기록은 미완료였다. 지정 방법은 아래 H011에 연결했다.

[history-011 목록](history-011-sources.jsonl)은17 원문1개를 재사용한다. [별도 웹 metadata](../evidence/0017-literature/manifest.json)는MGSTC·PID·Joint QoS의 공식v1 세 편과 [지정 열람 범위](../sources/history-011.md)를 연결한다. 새 원본 보존0개이며 원 inventory에 웹 문헌을 추가하지 않았다. 전체 논문 검토는 미완료이며, 공간 진단은 아래 H012에 연결했다.

[history-012 목록](history-012-sources.jsonl)은 18계획·21종합·공간 코드·시작/완료/summary·NPZ의 원본 7개 새 보존과 기존 2개 재사용, H5 metadata 1건을 연결한다. [읽은 범위](../sources/history-012.md)는 텍스트 전체 3개·JSON 전체 키 3개·새 배열 1개이며, 기록21의 이번 주장 검수는 공간 부분 20–29행이다. 실제 확장 X 저장물은 없고, 19/20/22와 21의 나머지 부분은 후속 작업이다.

[history-013 목록](history-013-sources.jsonl)은19/20계획·코드·저장결과·집중도의새원본18개495,076bytes와기존2개재사용,H5/설치metadata/checkpoint3건을연결한다. [열람범위](../sources/history-013.md)는새텍스트전체5개·JSON전체9개·수치배열파일4개다.21은ID/잔차/집중도및추가6호출만더검수했으며문헌과전체누적원장은남았다. 위H012의19/20대기상태는이후이묶음으로진행됐다.

[history-014 목록](history-014-sources.jsonl)은21/22와 초기/현재 지침4건(새2·재사용2),외부 설치 코드·metadata4건을 연결한다. [열람 범위](../sources/history-014.md)와 별도 웹 metadata는FSA/CDE/TabularMath 세 논문,TabPFN-TS 세 commit,현재 공식 지침의 지정 구간을 구분한다.21의 문헌57–62행을 더 연결했고22의 미완료 문헌·운영 증거 공백을 남겼다. 21의 완료 호출 누적은 [H015](../records/0015-0021-cumulative-costs.md)에서 이어서 대조했다. 논문 전체와 실패·후속 비용의 전수 감사는 미완료다.

목록과 근거 사본은 정리 시점의 스냅샷이다. 원본 변경 시 관련 주장과 검토 상태를 재확인한다. GitHub에는 검수된 묶음부터 반영하며, 전체 기록의 본문 정리는 진행 중이다.

[15·21 초기 누적 비용 출처](history-015-sources.jsonl)는 기존28개 원본을 재사용하고 이번 타이머·비용 필드 대조 범위를 구분한다. 전체 실패·후속 비용 원장의 완료를 뜻하지 않는다.


[23·25 조건부 공유 비용 목록](history-016-sources.jsonl)은 새 원본9개·기존6개를 연결한다. [읽은 범위](../sources/history-016.md)는 텍스트3개·JSON전체5개·신규 배열1개와 재사용 구간을 구분한다.25의 전체 열람을 §2/§3 검수 완료로 세지 않는다.

[24·25 recursive 진단 목록](history-017-sources.jsonl)은 보존 참조32개(새7·기존25),H5 metadata1개,미게시체크포인트 metadata21개를 구분한다. [읽은 범위](../sources/history-017.md)는 새 텍스트2개·전체JSON3개·지정수치자료2개이며summary의큰행렬은모든값산술대조와수동열람을구분했다.25 §2를추가검수했고§3와전체후속연결은남았다. 체크포인트해시확인을팀가중치접근완료로세지않는다.

[25 인접 문헌 목록](history-018-sources.jsonl)은 기존 보존3개 재사용과 Ma PDF metadata1건을 연결한다. [읽은 범위](../sources/history-018.md)는 세 논문의 지정 방법·PDF에서 고른 총15개 페이지의 시각 대조이며, NeST·Graph Coloring·NTK의 별도 웹 metadata3건은 inventory 파일 수에 넣지 않았다. NTK는 검색/기관 초록 단계다.25 §3–4를 추가 연결했고 전체 후속 이력·25 전체 통합은 미완료다.

[26·27 출처 목록](history-019-sources.jsonl)은 새 원본 8개 1,350,811 bytes와 기존 2개, H5 metadata 1건을 연결한다. [열람 범위](../sources/history-019.md)는 텍스트/정적 코드 3개·작은 JSON 전체 3개·신규 수치 자료 2개의 선언한 검수 범위를 구별한다. 저장된 13개 예측·19개 상태를 검산했으며 실제 단순 모델 적합은 재현하지 않았다.

[28 출처 목록](history-020-sources.jsonl)은 원문·manifest 사본 3개(12,092 bytes), 외부 문헌 4개·정적 코드 3개의 metadata, 미검토 추출 txt 3개를 구분합니다. [열람 범위](../sources/history-020.md)의 선택 페이지·절을 논문 전체 읽기로 집계하지 않습니다.

[history-021 출처 행](history-021-sources.jsonl):29–32의24새사본·기존비용원장·외부출처6개를 연결한다. metadata목록·지정코드독해·전체원notebook검토를 구분한다. [사람이 읽은 범위](../sources/history-021.md)를 참조한다.

[history-022 목록](history-022-sources.jsonl)은33–35의13새사본(578,461 bytes)·기존7참조·일차문헌metadata5·해시만확인31개를 구분한다. [읽은 범위](../sources/history-022.md)의56참조를56개전체본문완료로세지 않는다.29가중치팀접근과논문전체는미완료다.

[H025 목록](history-025-sources.jsonl)은 41/42 및 44 수치 절의 새 원본 7개(59,195 bytes)와 기존 참조 9개를 연결한다. [열람 범위](../sources/history-025.md)는 계획·정적 코드 전체 2개, 44의 부분 검수 1개, 작은 JSON 전체 3개, 결과 JSON 선택 수치 1개를 구분한다. 44 전체 보존과 문헌 전체 검수는 같지 않다.

[H026 목록](history-026-sources.jsonl)은 43–44의 새 원문 5개(17,623 bytes)·44 재사용 1개·일차자료 metadata 10개·identity만 확인한 9개를 연결한다. [열람 범위](../sources/history-026.md)는 논문 선택 텍스트 34쪽·시각 9쪽, 저자 코드 3개·README 1개 전체와 미열람 변환본을 구분한다. 44의 수치 검수(H025)와 문헌·역할 검수(H026)를 함께 찾을 수 있다.

[H027 목록](history-027-sources.jsonl)은 새 원문10개(90,808 bytes), 기존 사본6개, HDF5 metadata1개를 연결한다. [열람 범위](../sources/history-027.md)는 텍스트3개·작은JSON5개·선택수치1개와 47의 부분 주장 검수를 구분한다. 스냅샷metadata32행을 연결파일32개 본문 완료로 세지 않는다.

[H028 목록](history-028-sources.jsonl)은 새 원문7개(9,102 bytes)·기존사본3개·외부metadata13개와 별도 UPC 참조를 구분한다. [열람 범위](../sources/history-028.md)는 새 텍스트4개·JSON4개·선택논문20쪽/UPC재독2쪽/시각6쪽, 전논문완료0개를 명시한다. H027에서 대기였던47의 주요 주장을 연결했으며 전체 관련 패킷은 미완료다.

[H029 목록](history-029-sources.jsonl)은 새 원문11개(3,725,352 bytes)·기존사본3개·HDF5 metadata1개를 연결한다. [실제 열람](../sources/history-029.md)은 새 전체텍스트3개·작은JSON5개·선택수치1개와50부분검수를구분한다. snapshot11의33metadata행을연결파일33개본문완료로세지않는다.

[H030 목록](history-030-sources.jsonl)은 50 원문 판단·HiGP/ONDM/HTS-Cluster를 [열람 범위](../sources/history-030.md)에 연결한다. 새 사본 5개 8,808 bytes·재사용 2개·외부 metadata 14개다. 세 PDF의 내용 35쪽과 시각 21쪽을 읽고 선택 19행 128수치를 대조했다. 파생 TXT는 page header·CR/LF 차이까지 확인했지만 별도 새 논문·전체 텍스트 집계에 중복 가산하지 않았다. 50의 통합이 전체 관련 보고서·후속 판본 완료를 뜻하지 않는다.

[H031 목록](history-031-sources.jsonl)은 52·54와 55의 수치·실패·비용을 [열람 범위](../sources/history-031.md)에 연결한다. 새 정확 사본30개158,421bytes·기존3개·바이너리metadata3개다. 저장 배열·H5고정16열·타임스탬프·원장과 수정 전후 코드를 대조했다. snapshot12의108개 항목은 metadata이며 전체 본문 읽기 수가 아니다. 51·53/55 문헌·팀 바이너리 접근·관련 전체 보고서는 미완료다.

## H032: 51·55 GOTSF의 제한된 통합

[원본 목록](history-032-sources.jsonl)은 34경로(새 정확 사본 23개·236,888 bytes, 재사용 1개, metadata 10개)를 연결합니다. [manifest](../evidence/0051-0055-gotsf-audit/manifest.json)의 별도 추가 참조 4개 중 3개·15,273 bytes를 보존했습니다. 추가 취득은 원래 원본 목록의 증가나 당시 입수 실적을 뜻하지 않습니다. [읽기 범위](../sources/history-032.md)의 텍스트 23쪽·시각 확인 14쪽·코드/노트북 검토와 696개 인쇄값 대조는 저자 성능 재현 및 51·55 전체 완료와 구분합니다.

H033은 [15개 출처 행](history-033-sources.jsonl)과 [명세](../evidence/0051-0055-network-forecasting/manifest.json)에51·55의ITU/Cellular범위를 연결합니다.6기존사본 재사용·9외부metadata·5현재연결그림을 구분하고,28본문쪽/22시각쪽·인쇄표산술 검수는 원모델 재현과 별개로 기록합니다. 새원본복사0개이며전체51/55완료가아닙니다.

H034는 [6개 원본 행](history-034-sources.jsonl)과 [명세](../evidence/0051-frontiers-beam-audit/manifest.json)에 Frontiers 범위를 연결합니다. 기존사본4개·원본외부metadata2개·원inventory밖의현재PDFmetadata1개, 새원문복사0개입니다. [읽은 범위](../sources/history-034.md)의805줄/MathML118항목·PDF17본문쪽/10시각쪽은독립재현과구분하며,51/53/55전체는미완료입니다.

H035는 [12개 원본 행](history-035-sources.jsonl)과 [명세](../evidence/0053-moghadas-thesis/manifest.json)에 학위논문 범위를 연결합니다. 새 원문 사본5개·기존 사본1개·외부metadata6개입니다. [읽은 범위](../sources/history-035.md)는PDF131본문쪽/62시각쪽·과거미리보기3장과TXT131쪽계보 대조입니다. 파생본의 독립 내용 집계와 전체53/55 완료를 주장하지 않습니다.

H036은 [9개 원본 행](history-036-sources.jsonl)과 [명세](../evidence/0053-srsss/manifest.json)에 SRSSS를 연결합니다. 기존 사본5개 재사용·외부metadata4개·새 복사0개이며 [실제 읽기](../sources/history-036.md)는PDF9본문쪽/7시각쪽·과거미리보기2장과TXT9쪽 계보입니다. 반복 열람을 새 전체본문/JSON 집계에 가산하지 않고, 다른 telemetry 문헌과53/55 전체 종합은 계속 진행합니다.

H037은 [10개 원본 행](history-037-sources.jsonl)과 [명세](../evidence/0053-zoom2net/manifest.json)에 Zoom2Net을 연결합니다. 기존 사본5개 재사용·외부metadata5개·새 복사0개이며 [읽은 범위](../sources/history-037.md)는PDF14본문쪽/10시각쪽·과거미리보기3장과TXT14쪽 계보입니다. 파생본 재독을 새 전체본문/JSON 집계에 가산하지 않으며 전체53/55·다른 문헌은 미완료입니다.

H038은 [8개 원본 행](history-038-sources.jsonl)과 [명세](../evidence/0053-netnomos/manifest.json)에 NETNOMOS를 연결합니다. 기존 사본5개 재사용·외부metadata3개·새 복사0개이며 [읽은 범위](../sources/history-038.md)는PDF24본문쪽/18시각쪽·과거미리보기1장과TXT24쪽입니다. 파생본·기존 근거 재독을 새 전체본문/JSON 집계에 가산하지 않으며 전체53/55와 나머지 기록은 미완료입니다.

H039은 [원본 9개와 ZIP hash-only 1개](history-039-sources.jsonl)를 [명세](../evidence/0053-tabicl-imputation/manifest.json)에 연결합니다. 기존 정확 사본 4개·외부 원본 metadata 5개·container 1개·추가 웹 참조 9개이며 새 원문 복사는 없습니다. [읽은 범위](../sources/history-039.md)는 저장 HTML article, 코드 전체 3개/일부 1개, 현재 그림 5개와 Ciena PDF 표지입니다. 과거 그림 동일성·Ciena 전체 본문·전체 53/55는 미완료입니다.

H040은 [기존 원본4개](history-040-sources.jsonl)와 [명세](../evidence/0053-ciena-telemetry/manifest.json)에 Ciena 후속 독해를 연결합니다. 정확 사본4개와 기존 외부참조3개를 재사용했고 새 복사·고유 다운로드 집계는 없습니다. [읽은 범위](../sources/history-040.md)는PDF23본문쪽/14시각쪽·그림11개·표4개이며 외부 논문 독해를 localfulltext나 새 독립 실험으로 가산하지 않습니다.

H041은 [로컬 원본10행](history-041-sources.jsonl)과 [명세](../evidence/0051-stkdiff-audit/manifest.json)에 STK-Diff 후속 검수를 연결합니다. 새사본/전체본문1개(28줄)·기존사본9개·기존NPZ metadata1개·추가공식metadata10개이며, [읽은 범위](../sources/history-041.md)는그림4개/의존텍스트6개647줄입니다. 외부의존텍스트를localfulltext로중복가산하지않고51/55전체는미완료로유지합니다.

H042는 [기존 원본3행](history-042-sources.jsonl)과 [명세](../evidence/0051-event-context/manifest.json)에 event 후속을 연결합니다. 정확사본3재사용·새복사0·공식추가metadata2개이며 [범위](../sources/history-042.md)는AAM44본문쪽/26시각쪽입니다. 표5/6의72개 값을 검수했으며 외부PDF를 새 로컬fulltext/wholeJSON으로 가산하지 않습니다. 전체51/55는 미완료입니다.

H043은 [기존 원본 7행](history-043-sources.jsonl)을 [명세](../evidence/0051-0055-gotsf-media/manifest.json)로 재사용하고 공식 미디어 7개를 고정 URL·해시로 연결합니다. [실제 범위](../sources/history-043.md)는 PNG 4개·GIF 3개 전 144프레임입니다. SRC-0063280 tree는 whole JSON +1/selected-only −1로 승격하며 신규 사본·로컬 본문은 0개입니다. 전체 51/55는 미완료입니다.

H044는 [103개 대표 행](history-044-sources.jsonl)과 [207경로·판독 수준](../evidence/0051-0055-synthesis/scope-matrix.json)을 [51–55 종합](../records/0051-0055-synthesis.md)에 연결합니다. 신규수집/렌더code5개209줄·기존사본58개·metadata40개이며, 새localfulltext5/wholeJSON0/selected0입니다. PDF추출문·PNG·재독을독립내용으로중복가산하지않고,103자료를전체corpus나전자료검증완료의분모로쓰지않습니다.

[history-045 목록](history-045-sources.jsonl)은 56–58 MAE 반례의 새 사본16개·재사용5개·읽은외부metadata3개·해시전용15개를 연결합니다. [출처 범위](../sources/history-045.md)는 본문 독해와 사본/receipt 해시 대조를 구분합니다. 56/58의 다른 네 문헌과 전체 연관자료 정리는 미완료입니다.

[H046 출처 목록](history-046-sources.jsonl)은 TimeDC16묶음32원본경로와58메모재사용을연결합니다. [출처 안내](../sources/history-046.md)의원본/보충자료·전체/선택독해범위를함께보세요. 논문·저자코드는공식URL/고정commit·hash로접근하며원본사본새복제는0개입니다.

[H047 출처 목록](history-047-sources.jsonl)은TabPFN IML11묶음22원본경로와58메모재사용을연결합니다. [실제열람범위](../sources/history-047.md)에서전체텍스트·선택CSV·자동산술을구분하고공식URL/고정commit·해시를확인할수있습니다.

[H048 출처 목록](history-048-sources.jsonl)은 SCott 3묶음·6원본 경로와 58 메모 재사용 2경로를 연결합니다. [열람 범위](../sources/history-048.md)에 본문/부록·파생물·시각 자료와 공식 URL·해시를 구분했습니다.

[H049 출처 목록](history-049-sources.jsonl)은 SGD-as 4묶음·8원본 경로와 58 메모 재사용 2경로를 연결합니다. [열람 범위](../sources/history-049.md)에 PDF7쪽·TXT/preview 파생물·HTML visible text와 공식 URL·해시를 구분했습니다.

[H050 출처 목록](history-050-sources.jsonl)은 수집 script/receipt와 전체 필드로 검토를 확장한 tree 2개, 기존 계획/결과와 다섯 주논문을 연결합니다. [42개 파일 범위표](../evidence/0056-0058-compression-synthesis/packet-scope.json)에 전체 메타데이터·HTML의 보이는 본문·파생물·연결 본문의 구분을 보존했습니다.


[H051 목록](history-051-sources.jsonl)은 보존/재사용15묶음31경로와 대형 자산2개를 연결합니다. [실제 열람 범위](../sources/history-051.md)에 전체 텍스트/JSON, 숫자 배열 검산, object 날짜의 정적 읽기와 미검토 문헌을 구분했습니다.

[H052 출처 목록](history-052-sources.jsonl)은 61번 산술의 10묶음·31경로와 6개 새 정확 사본·4개 재사용을 연결합니다. [실제 독해 범위](../sources/history-052.md)에 기존 자료 재독과 다음 묶음의 대기 독해를 구별했습니다.

[H053 출처 목록](history-053-sources.jsonl)은 59 ALW의25묶음·50원본 경로를 연결합니다. [실제 읽은 범위](../sources/history-053.md)에서 논문·고정 코드·추가 의존 자료와 아직 읽지 않은 horizon을 구별합니다.

[H054 출처 목록](history-054-sources.jsonl)은 horizon 두판본의16묶음·32원경로를 연결합니다. [32묶음·64경로의 문헌 폴더 대조](../verification/history-054-packet-scope.json)에서 ALW와horizon의 완료범위 및 미보유 외부자료를 구분합니다.

[H055 출처 목록](history-055-sources.jsonl)은 ECAI와63–65 관련23그룹47경로를 연결합니다. [실제 열람 범위](../sources/history-055.md)에13새사본·1재사용·9외부metadata,9쪽논문·2공식코드·다른6문헌의미완료를구분했습니다.

[H056 출처 목록](history-056-sources.jsonl)은 Heatload와 63·65의 15그룹 30원본 경로를 연결합니다. [실제 읽은 범위](../sources/history-056.md)에 기존 사본 2개·외부 metadata 13개와 새 보충 텍스트 8개를 구분했습니다.

[H057 출처 목록](history-057-sources.jsonl)은 KDD 문헌과63·65의8그룹16경로를연결합니다. [실제 읽은 범위](../sources/history-057.md)에서 기존2사본과외부6참조,공식v2와미독해출판본을구분했습니다.

[H058 출처 목록](history-058-sources.jsonl)은 PLOS 문헌과64·65의7그룹14경로를연결합니다. [읽은 범위](../sources/history-058.md)에서 새사본2·재사용2·외부3참조와공식판본대조를구분합니다.

[H059 출처 목록](history-059-sources.jsonl)은5그룹10경로의GP-Copula와64·65를연결합니다. [읽은 범위](../sources/history-059.md)는기존사본2재사용/외부참조3,공식보충과고정코드의전체·부분독해를구분합니다.

[H060 출처 목록](history-060-sources.jsonl)은7그룹14경로의TACTiS-2와64·65를연결합니다. [실제 범위](../sources/history-060.md)는 논문28쪽/15그림12표·공식코드16전체·기존사본2재사용/외부참조5입니다.

[H061 출처 목록](history-061-sources.jsonl)은11그룹22경로의 조건부 정규화 문헌·수집 이력과64·65를 연결합니다. [실제 범위](../sources/history-061.md)는 논문35쪽/26그림·코드18파일 전체, 새사본3/기존3재사용/외부참조5입니다.

[H062 출처 목록](history-062-sources.jsonl)은47그룹100경로를연결합니다. [실제 읽은 범위](../sources/history-062.md)는 새본문9/전체결과·관리JSON12와 외부검색문자열4를 구분합니다. 새사본21개125,075bytes·기존6재사용·외부20참조이며,3논문74쪽·PNG7개는 해시/판본표기만 확인해 본문·시각독해로 가산하지 않습니다.

[H063 출처 목록](history-063-sources.jsonl)은 MMR과 원66·68의7그룹14경로를 연결합니다. [실제 독해 범위](../sources/history-063.md)는35쪽 본문·시각과 파생TXT/HTML/preview이며 새복사·로컬본문/JSON 신규가산은0입니다.

[H064 출처 목록](history-064-sources.jsonl)은 MRI와 원66·68의6그룹12경로를 연결합니다. [실제 범위](../sources/history-064.md)는32쪽 본문·시각, TXT32본문 대응검사, HTML 의미·메타 정적 독해, preview1개와 공식 TeX 지정 범위입니다. 새복사·로컬본문/JSON 신규가산은0이며 표현 네 개를 네 연구로 세지 않습니다.

[H065 출처 목록](history-065-sources.jsonl)은 q-FFL과 원66·68의9그룹18경로를 연결합니다. [실제 범위](../sources/history-065.md)는 PDF7쪽·TXT7본문 대응·HTML 의미 독해·원preview4개·TeX 지정범위와 외부 원알고리즘8파일입니다. 새복사·로컬본문/JSON 신규가산은0이며 파생표현을 독립 연구로 세지 않습니다.

[H066 출처 목록](history-066-sources.jsonl)은 55그룹·124경로를 연결합니다. 새 정확사본 24개, 기존 사본 재사용 7개, 본문 대기 메타데이터 24개를 구분합니다. 로컬 본문 10개·전체 JSON 14개를 신규 검수했으며 논문 PDF·검색 출력·PNG를 읽은 것으로 합산하지 않습니다. [실제 범위](../sources/history-066.md)를 함께 확인하세요.

[H067 목록](history-067-sources.jsonl)은 Forecaster’s Dilemma와 기존 69–71의 11그룹·22경로를 연결합니다. 새 원본 복사는 0개이며 기존 정확사본 4개·외부 메타데이터 참조 7개입니다. [출처별 읽은 범위](../sources/history-067.md)는 저널 22쪽·TXT 22본문 대응·HTML 정적 독해·원PNG 3개·공식 TeX 559행을 구분합니다. 인용논문 전체나 원실험 재현으로 세지 않습니다.

[H068 목록](history-068-sources.jsonl)은 DeepCog와 기존69–71의10그룹·20경로를 연결합니다. 새 원본 복사는0개, 기존 정확사본4개·외부 메타데이터 참조6개입니다. [읽은 범위](../sources/history-068.md)는 저자본16쪽·TXT 대응·HTML 정적 독해·원PNG3개와 외부 notebook10셀을 구분합니다. 파생표현과 재독해를 새 로컬 본문 수로 가산하지 않습니다.

[H069 목록](history-069-sources.jsonl)은 SIU·검색 기록과 기존69–71의20그룹·40경로를 연결합니다. 기존 정확사본9개·메타데이터11개이며 새 사본과 source 독해 수 가산은0입니다. [실제 범위](../sources/history-069.md)는 검색8내용/10표현/100결과와 기관 HTML을 구분합니다. 검색 원문은 새로 재게시하지 않고 해시·원경로·결과별 접근 색인을 제공합니다.

[H070 source별 범위](../sources/history-070.md)와 [81그룹 catalogue](history-070-sources.jsonl)는 원72–75에 대응한다. 등록197경로 중196현재일치·1누락, 정확사본45참조/metadata36을 분리한다. 원문19·전체JSON15·선택2의 새 검수 범위만 가산 대상으로 두며, 미열람 외부34자료는 후속 상태다.

[H071 목록](history-071-sources.jsonl)은72 Globalization/KBS의13그룹·27경로를 연결합니다. 기존 정확사본2개·외부 참조11개이며 새 원본 복사는0입니다. [출처별 범위](../sources/history-071.md)에서 PDF65쪽, TXT65본문 대응, HTML 정적내용, 원PNG4개, KBS서지와 접근 실패를 구분합니다.

[H072 목록](history-072-sources.jsonl)은 원73 관련 14그룹·28경로를 연결합니다. 기존 정확사본 2개·외부 자료 메타데이터 12개이며 새 원본 복사는 0개입니다. [출처](../sources/history-072.md)는 원PDF 19쪽·보충/추가PDF 13쪽(백지 1쪽 포함), TXT 대조·원PNG 3개, 고정 코드와 외부 요청 26개의 실제 열람 범위를 구분합니다.

[H073 목록](history-073-sources.jsonl)은 기존 findings2개와 저장 검색11개, 총13그룹·26경로를 연결합니다. [159개 응답 색인](../evidence/0072-0075-saved-search/response-ledger.json)은 원본 좌표·URL·해시·연구 역할을 제공합니다. TXT8개와 JSON3개를 전구간 읽었으며, 이를 외부 논문159편의 독해나 새 실험으로 가산하지 않습니다. 새 원본 복사는0개이고 원검색 전체의 팀 접근은 미완료입니다.

[H074 출처](../sources/history-074.md)와 [161그룹 catalogue](history-074-sources.jsonl)는 원76–79의 전체 텍스트27·JSON24·변경행8, 정확사본59참조와 metadata102를 구분한다. 등록338경로 중336개는 현재 일치하며 라이브러리2경로는 없다. snapshot19–22의178파일 해시 검사는178본문 독해가 아니다.

## H075: 원76 외부 자료와 저장 결과

[출처](../sources/history-075.md)와 [25그룹 목록](history-075-sources.jsonl)은 PDF 3개·39쪽, 코드·README 6개, 검색 4개, 별도 TXT 2개, 원 PNG 6개, tree JSON과 부분 commit JSON을 구분한다. TabDistill TXT의 가역적인 표현 대응은 새 독립 독해로 가산하지 않는다. 등록76경로 중74개 해시 일치, 기존 누락2경로는 보관사본과 분리해 기록했다. commit의61patch 독해와27patch 미독해도 명세에 남긴다.

## H076: 남은 상호작용 CSV와 커밋 전체 범위

[출처](../sources/history-076.md)와 [3그룹 목록](history-076-sources.jsonl)은 같은 커밋 JSON의 후속 검토와 재참조 논문·코드를 연결한다. CSV 27개·2,253행과 남은 메타데이터를 읽고 20개 주장을 대조했다. `SRC-0063879`는 H075의 부분 검토에서 저장 JSON 전체 검토로 전환한다. 부분 자료 1개를 빼고 전체 JSON 1개를 더하며, 27개 patch나 기존 논문·코드를 새 파일 독해로 중복 가산하지 않는다. H075 목록은 그 당시의 읽기 범위를 보존한다.


## 77의 동적 소속 근거

[H077 출처](../sources/history-077.md)와 [22그룹 목록](history-077-sources.jsonl)은 원77외부21그룹과 재참조findings1개를 구분한다. 새전체본문5개·전체JSON2개이며 다른14그룹은 미독해다. 같은commit의 보완외부2파일은 별도명세로 남기고 로컬목록의 완료 수에 더하지 않는다.

[H078 출처](../sources/history-078.md)와 [목록](history-078-sources.jsonl)이 그 후 남은 14개 그룹을 완료했다. 새 독립 PDF 2개·전체 JSON 3개, 기존 논문과 전쪽 대응하는 TXT 3개·직접 열람한 PNG 6개를 구분한다. H077의 목록은 당시 범위를 보존하며, 현재 원77 외부 21개 그룹의 저장 내용 검토는 완료됐다. 인용 문헌 전문과 실행 재현까지 완료한 것은 아니다.

## H079: 원78 회귀 전이 12개 그룹

[출처](../sources/history-079.md)와 [13개 목록](history-079-sources.jsonl)은 새 검토 12개와 재참조 findings 1개를 구분한다. 새 독립 본문 4개·전체 JSON 3개, TXT 2개의 23쪽 대응·PNG 3개의 직접 열람이다. 원78의 외부 43개 그룹 중 다른 31개는 이번 범위 밖이며, 그중 H074에서 읽은 manifest도 있어 모두 미독해로 세지 않는다.

## H080: 원78 Task2Vec 13개 그룹

[출처](../sources/history-080.md)와 [14개 목록](history-080-sources.jsonl)은 새 검토 13개와 원78 판단 재참조 1개를 연결한다. 독립 본문 5개·전체 JSON 3개, TXT 16쪽 대응·원 PNG 2개·공식 서지 HTML 전체를 구분한다. 표 20개 값과 보충 행렬 3,500개 정수는 표시 결과이며 새 실험 수가 아니다. 이번 밖의 30개에는 H079 등의 기존 완료 자료도 있다.

## H081: 원78 NTKMTL 11개 그룹

[출처](../sources/history-081.md)와 [12개 목록](history-081-sources.jsonl)은 새 자료 11개와 이전 판단 1개를 연결한다. PDF29쪽·README74행·Python424/1823행으로 독립 본문4개, 전체JSON3개, 원PNG3개를 구분한다. TXT29쪽 대응·사본22경로·재참조findings는 본문 중복 가산이 없다. 이번 밖의32개에는 기존 검수 범위도 포함된다.

## H082: 원78 검색·접근 3개 그룹

[출처](../sources/history-082.md)와 [4개 목록](history-082-sources.jsonl)은 새3개와 기존 판단1개를 연결한다. 전체JSON2·빈HEAD1을 구분하고 독립 본문·이미지 추가 가산은 없다. [43개 소장그룹 연결](../evidence/0082-transferability-access/packet-coverage.json)은 H0744·H07912·H08013·H08111·H0823으로 검수 책임을 나눈다. 검색에 나온 모든 논문/저장소 의존 파일을 확보한 목록은 아니다.

## H083: 원79 FMCL 5개 그룹

[출처](../sources/history-083.md)와 [7개 목록](history-083-sources.jsonl)은 새5개와 기존 findings·plan2개를 연결한다. 독립 PDF1개·16쪽, 파생TXT16쪽 대응·원PNG3개·사본10경로를 구분한다. 새 JSON 독해 가산은 없고 원79 외부21그룹 중 잔여12그룹은 후속 검수 대상이다.

## H084: 원79 EMD-CFL 논문2그룹

[출처](../sources/history-084.md) · [4개 목록](history-084-sources.jsonl). 새HTML/TXT2그룹과 기존findings/plan2그룹을 연결한다. 독립본문1,파생TXT추가0이며 공식v1보충PDF24쪽·그림17개는 현재검수의별도출처다. 원79 외부21중누적11그룹연결·10그룹후속,새JSON/이미지독해가산0.

### H085 구현7그룹

[출처](../sources/history-085.md) · [목록](history-085-sources.jsonl) · [기록](../records/0085-emd-cfl-code.md). 새텍스트5/전체JSON2와 기존2그룹 재참조를 구분한다. 코드/환경 실행은0이고 원79 외부21그룹 중 이번 범위까지18, Toso2/검색1은 후속 범위다.

### H086 Toso2그룹

[출처](../sources/history-086.md) · [목록](history-086-sources.jsonl) · [기록](../records/0086-toso-gradient-heterogeneity.md). 저장HTML 전체와 파생TXT를 대응했고 독립본문은1개다. 새PDF30쪽 중9쪽 보충시각대조는 원목록 가산0이며 원79 외부21그룹 중20개 연결/검색1개가 남는다.

## H087: 원79 검색1그룹

[출처](../sources/history-087.md) · [목록](history-087-sources.jsonl) · [21그룹 연결](../evidence/0087-distributed-search/packet-coverage.json). 9개 값 전체를 읽은 JSON1개를 추가하며 독립 논문·이미지 가산은0이다. H0744·H0835·H0842·H0857·H0862·H0871은 소장 파일의 검수 연결이며 모든 외부문헌 확보를 뜻하지 않는다.

## H088: 원80 진단과 실행 기록

[출처](../sources/history-088.md) · [목록](history-088-sources.jsonl) · [검수](../verification/history-088.md).16그룹55경로, 신규본문5·전체JSON8·선택NPZ2이며 budget_before는 H070과 같아 추가 가산0이다. 검색JSON과pyc는 다음 범위로 남긴다.

[H089 출처](history-089-sources.jsonl)는 새 검색·캐시2그룹과 H088 재참조4개를 연결한다. 검색은 전체JSON1개, 캐시는 검토된 소스의 파생 관계이며 새 독립 본문 가산0이다.
