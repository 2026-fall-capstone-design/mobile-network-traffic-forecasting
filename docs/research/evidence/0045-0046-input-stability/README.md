# 45–46 저장 공간 입력 재분석 근거

[팀용 기록](../../records/0045-0046-input-stability.md), [출처 범위](../../sources/history-027.md), [검수](../../verification/history-027.md)를 함께 읽는다. 이 폴더의 원문은 보존 사본이다. 원문 속 과거 명령·예산·Goal은 현재 실행 지시가 아니다.

- [45 계획](originals/SRC-0021616.md.txt), [46 정적 코드](originals/SRC-0022883.py.txt), [원장 갱신 코드](originals/SRC-0023219.py.txt), [47 원 메모](originals/SRC-0021660.md.txt)
- [46 설정](originals/SRC-0027919.json), [시작 표시](originals/SRC-0027918.json), [완료 표시](originals/SRC-0027917.json), [cell별 결과](originals/SRC-0027916.json)
- [당시 원장](originals/SRC-0000661.json), [스냅샷 manifest](originals/SRC-0000657.json), [이번 manifest](manifest.json)
- [재사용한 18 NPZ](../0018-0021/originals/SRC-0031959.npz), [18 summary](../0018-0021/originals/SRC-0031962.json), [18 코드](../0018-0021/originals/SRC-0023177.py.txt)

NPZ의 `pred`는 모델 Ridge/HGB, 입력 자기/평균/PCC/8방향, 32개 cell, 336시간 순서다. `y`·`cell_ids`·`query_times`로 정답·순서를 확인할 수 있다. 46의 `models.*.variants`에는 전체/부분집합/주별 MAE와 cell별 차이가 있고, `first_week_selection`과 `second_week_label_oracle`는 실행 가능한 시간 순서의 선택과 사후 정답 선택을 구분한다. oracle은 미래 정답을 쓰므로 실제 예측 성능으로 인용하지 않는다.

확장 X·적합 객체는 저장되지 않았다. 저장 예측의 산술 대조와 모델 재현 성공은 다르다. HDF5는 이번에 복제하지 않았으며 접근 경로·해시는 manifest에만 있다. 47의 문헌/논리/규모 판단은 보존돼 있으나 이번 묶음의 검수 완료 범위가 아니다.
