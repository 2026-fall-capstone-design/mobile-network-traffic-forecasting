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
