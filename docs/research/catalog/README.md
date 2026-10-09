# 자료 목록과 출처 매핑

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

[history-009 목록](history-009-sources.jsonl)은15 원문 재사용1개·새 입수 기록1개·문헌 텍스트6개/PDF6개의 메타데이터를 연결한다. [읽은 범위](../sources/history-009.md)는 지정 줄과 PDF29쪽의 지정 내용이며 전논문 완료0편이다. 당시 문헌 판단을 대조했고 원문 표현·비율 공백4건을 보존했다. 15의 후속 연결과 누적 실행 비용 재감사는 남아 있다.

[history-010 목록](history-010-sources.jsonl)은16–17의 원문8개 새 보존과 기존2개 재사용, H5 metadata1건을 연결한다. [읽은 범위](../sources/history-010.md)는 텍스트 전체3개·JSON 전체키3개·새 배열2개 및 재사용 자료의 지정 범위다. 저장 성능과 H5 지정 구간의 입력·정답을 대조했으며,H010 시점에서 세 문헌 방법과 후속 공간 정보 기록은 미완료였다. 지정 방법은 아래 H011에 연결했다.

[history-011 목록](history-011-sources.jsonl)은17 원문1개를 재사용한다. [별도 웹 metadata](../evidence/0017-literature/manifest.json)는MGSTC·PID·Joint QoS의 공식v1 세 편과 [지정 열람 범위](../sources/history-011.md)를 연결한다. 새 원본 보존0개이며 원 inventory에 웹 문헌을 추가하지 않았다. 전체 논문 검토는 미완료이며, 공간 진단은 아래 H012에 연결했다.

[history-012 목록](history-012-sources.jsonl)은 18계획·21종합·공간 코드·시작/완료/summary·NPZ의 원본 7개 새 보존과 기존 2개 재사용, H5 metadata 1건을 연결한다. [읽은 범위](../sources/history-012.md)는 텍스트 전체 3개·JSON 전체 키 3개·새 배열 1개이며, 기록21의 이번 주장 검수는 공간 부분 20–29행이다. 실제 확장 X 저장물은 없고, 19/20/22와 21의 나머지 부분은 후속 작업이다.

[history-013 목록](history-013-sources.jsonl)은19/20계획·코드·저장결과·집중도의새원본18개495,076bytes와기존2개재사용,H5/설치metadata/checkpoint3건을연결한다. [열람범위](../sources/history-013.md)는새텍스트전체5개·JSON전체9개·수치배열파일4개다.21은ID/잔차/집중도및추가6호출만더검수했으며문헌과전체누적원장은남았다. 위H012의19/20대기상태는이후이묶음으로진행됐다.

목록과 근거 사본은 정리 시점의 스냅샷이다. 원본 변경 시 관련 주장과 검토 상태를 재확인한다. GitHub에는 검수된 묶음부터 반영하며, 전체 기록의 본문 정리는 진행 중이다.
