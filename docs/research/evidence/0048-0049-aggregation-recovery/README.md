# 48–49 집계와 개별 복원 진단의 재사용 근거

[팀용 기록](../../records/0048-0049-aggregation-recovery.md), [출처](../../sources/history-029.md), [검수](../../verification/history-029.md)를 함께 읽는다. [manifest](manifest.json)에 새 사본11개·기존3개·HDF5 metadata1개의 버전과 해시가 있다.

- [NPZ](originals/SRC-0023807.npz): `actual`은336시간×32cell 원 활동량, `scale`은32개 앞구간 평균, `cell_ids`와 `query_times`는순서다. 나머지48개배열의 이름은 `partition__allocation__scalar`다. partition은all32/geography_k8/PCC_k8/random_k8, allocation은last/day_lag/hour_profile, scalar는true_total/best_scalar/last_total/day_total이다. 50개float64·2개int64 배열이다.
- [결과 JSON](originals/SRC-0023808.json): scale·전체group/cell목록·cell별/주별/원단위/정규화지표·그룹총량지표·toy·비용·한계. oracle 두 조건은 미래 정답을 사용한다.
- [설정](originals/SRC-0023811.json), [시작](originals/SRC-0023810.json), [완료](originals/SRC-0023809.json), [코드](originals/SRC-0022133.py.txt), [계획](originals/SRC-0021681.md.txt), [판단50](originals/SRC-0021725.md.txt): 원본 그대로다. 원 코드 재실행은 이 아카이브 작업에서 수행하지 않았다.
- [당시 원장](originals/SRC-0000695.json), [보존 manifest](originals/SRC-0000690.json), [원장 갱신 코드](originals/SRC-0023211.py.txt)는 측정·보존 경계를 연결한다. 당시 예산을 현재 실행 지시로 사용하지 않는다.

저장된32cell·336시간의 복원 값과 지표를 비교하는 데는 위 NPZ/JSON을 재사용할 수 있다. 원자료의 다른 구간·전처리·당시 환경 전체를 재현하려면 HDF5와 별도 환경이 필요하며 팀 접근은 아직 미완료다. [산술 검사](../../verification/history-029-saved-check.json)와 [cell별 손해/원장 검사](../../verification/history-029-lineage-check.json)는 검산 범위를 명시한다. 전논문·전체50·관련후속기록완료를 뜻하지 않는다.
