# 60번 grouping × 최근 입력 길이의 작은 근거

[팀 기록](../../records/0059-0062-history-grouping.md) · [출처](../../sources/history-051.md) · [manifest](manifest.json)

원 계획·코드·설정·결과·두 예측 NPZ·시작/종료·전후 원장을 바이트 그대로 보존하거나 기존 정확 사본으로 연결했다. `four-cell-input-slice.npz`는 HDF5 Internet 채널의 지정 4cell×1488시간과 날짜를 뽑은 숫자/문자열 파생물이다. 원본 해시와 대조 범위는 [input-audit](input-audit.json)에 있다. 데이터/가중치 전체 접근은 [기존 자산 안내](../0001-0002/README.md)를 따르며 현재 환경의 모델 재현 성공을 뜻하지 않는다.

최종 NPZ의 `query_timestamps`는 object dtype이다. 검수기는 숫자를 `allow_pickle=False`로 읽고 날짜는 직렬화 문자열만 정적으로 확인한다. 보존 코드는 읽기용 `.py.txt`이며 이 정리 과정에서 실행하지 않았다.

저장소 루트에서 다음 검사를 수행할 수 있다. 원 모델이나 연구 스크립트는 실행하지 않는다.

```sh
python scripts/research_archive/verify_history_grouping_pilot.py --manifest docs/research/evidence/0059-0062-history-grouping/manifest.json --output .research-archive/history-grouping-check.json
```

[숫자 검수](../../verification/history-051-numeric-check.json) · [주장과 한계](../../verification/history-051.md)
