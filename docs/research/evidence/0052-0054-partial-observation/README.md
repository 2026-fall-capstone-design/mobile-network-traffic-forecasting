# 52·54 원본과 재사용 자료

[팀 기록](../../records/0052-0054-partial-observation.md), [출처](../../sources/history-031.md), [검수](../../verification/history-031.md)를 함께 읽는다. [manifest](manifest.json)는 36개 원본 경로를 연결한다. 새 30개 정확 사본은 158,421 bytes이며 기존 3개 사본을 재사용하고 외부 바이너리 3개는 metadata로 남겼다.

원본의 줄바꿈까지 보존했으며 `.md.txt`/`.py.txt` 확장자는 역사 자료임을 드러낸다. STK-Diff의 작은 소스·README를 함께 보존하며 [원 LICENSE](originals/SRC-0063295.txt)를 포함했다. 공식 고정 버전은 [e1faed12](https://github.com/tsinghua-fib-lab/STK-Diff/tree/e1faed12aa7abb33d801fe9483026769ffaeeed3)이다. 소스 보존은 전체 모델 또는 README의 모든 그림을 읽었다는 뜻이 아니다.

[52 결과](originals/SRC-0023905.json)에서 자료 적합성을 확인하고, [54 계획](originals/SRC-0021802.md.txt)·[수정 전 코드](originals/SRC-0022965.py.txt)·[수정 후 코드](originals/SRC-0022964.py.txt)·[보정 보고](originals/SRC-0029390.json)를 읽는다. [54 결과](originals/SRC-0029391.json), [최종 예측](originals/SRC-0029388.npz), [부분 저장](originals/SRC-0029389.npz), [54 이후 원장](originals/SRC-0000732.json)은 같은 실행 묶음의 근거다. 부분 저장을 독립 재현으로 세지 않는다.

H5·checkpoint·Beijing NPZ는 manifest의 위치/해시로 식별한다. Beijing은 [고정 원본 입수 링크](https://raw.githubusercontent.com/tsinghua-fib-lab/STK-Diff/e1faed12aa7abb33d801fe9483026769ffaeeed3/traffic_data/beijing.npz)를 연결했다. H5와 checkpoint의 기존 안내는 [자료 접근 현황](../../catalog/README.md)에서 관련 기록을 찾는다. metadata만으로 팀의 실제 파일 접근이나 재현 성공이 보장되지 않는다.
