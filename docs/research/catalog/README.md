# 자료 목록과 출처 매핑

[inventory.jsonl.gz](inventory.jsonl.gz)는 2026년 10월 8일 조사한 48,149개 메타데이터 항목의 UTF-8 JSONL을 gzip으로 압축한 파일이다. 원문 내용은 포함하지 않는다. [집계와 파일 해시](scope-summary.json), [조사 방법과 한계](../verification/inventory-2026-10-08.md)를 함께 읽는다.

각 줄은 `source_id`, `kind`, 원본 루트 기준 `path`, 확장자·크기·수정 시각, `sha256`, 포함·제외 상태와 이유를 담는다. 압축 내부 항목에는 `container_id`, `container_path`, `member_index`가 있다. `mtime_ns`는 물리 파일 수정 시각이며 압축 멤버의 시각 필드는 형식에 따라 다르다. 경로는 원본 루트 별칭 `Tab-ICL`을 기준으로 한다. 외부 공용 런타임의 개인 경로는 별칭으로 표시하고 로컬 매핑에만 보존한다.

`representative_source_id`는 같은 SHA-256을 갖는 포함 대상의 대표다. 대표를 읽지 않은 상태는 `exact_duplicate_pending_representative_review`이며 내용 검토 완료를 뜻하지 않는다. 라이브러리 제외·캐시 제외·동일 사본 연결은 서로 다른 처리 상태다. 제외 파일도 목록에서 지우지 않는다. 포함된 고유 파일 16,326개에는 배열·환경 자료도 있으므로 연구 기록 수로 세지 않는다.

목록 상태와 본문 검토는 따로 관리한다. [첫 시범 출처 목록](pilot-001-sources.jsonl)은 635–638을, [RCTL 출처 목록](pilot-002-sources.jsonl)은 639에 사용한 source_id·해시·보존 사본·실제 검토 범위와 기록 번호를 연결한다. [첫 출처 안내](../sources/pilot-001.md)와 [RCTL 출처 안내](../sources/pilot-002.md)에서 원문과 정리본을 오갈 수 있다.

후속 묶음은 [640 출처](pilot-003-sources.jsonl), [641 출처](pilot-004-sources.jsonl), [642 출처](pilot-005-sources.jsonl)로 이어진다. [642 판본 안내](../sources/pilot-005.md)는 Word·렌더 이미지·생성 코드의 실제 읽기 범위와 목록 밖에서 확인한 외부 원문을 구분한다. 파일 보존, 해시 확인, 본문 열람, 주장 검증은 서로 다른 상태다.

[초기 01–02 출처](pilot-006-sources.jsonl)는 자료 진단·CPU 동작·후보 설계를 연결한다. [초기 출처 안내](../sources/pilot-006.md)는 원문13개, 외부 자료와 대용량 자산9건, 파생 날짜 발췌를 구분한다. 작은 배열 검산과 별도 로컬 H5 확인을 같은 CI 실행으로 표현하지 않는다.

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

목록과 근거 사본은 정리 시점의 스냅샷이다. 원본 변경 시 관련 주장과 검토 상태를 재확인한다. GitHub에는 검수된 묶음부터 반영하며, 전체 기록의 본문 정리는 진행 중이다.
