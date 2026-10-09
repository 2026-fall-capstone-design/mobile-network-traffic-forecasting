# 고정 RCTL recursive 진단의 보존 근거

[정리 기록](../../records/0024-0025-recursive-horizon.md), [출처와 읽은 범위](../../sources/history-017.md), [검수 안내](../../verification/history-017.md)를 연결한다. [manifest](manifest.json)의32개 보존 참조는 새 원본7개·1,129,372bytes와 기존25개 재사용이다. 기존21개 group 예측을 첫 시점에 대조하며 원문25는 앞 묶음의 사본을 재사용한다.

`prediction`은9×16×48×24, `y`는16×48×24다. methods/cell_ids/scales/origins를 함께 보존했다. 기존6모델군과 단순 기준3개를 구분하고, 전체24시점의 정규화·원단위·cell·origin 지표를 포함한다. 코드·계획·시작·완료·설정·summary의 바이트는 원본과 같다. 과거 코드는 실행 지시가 아니다.

원 H51개와 체크포인트21개는 별도 metadata다. H5 선택 데이터 및21개 `.pt` 바이트 해시를 로컬에서 확인했지만, `.pt`를 역직렬화하거나 이 저장소에 게시하지 않았다. 팀 공유 위치 미확인과 중간 X 미보존을 그대로 남긴다. CI는 보존 예측의 산술을 검사하며 과거 모델을 재실행하지 않는다.
