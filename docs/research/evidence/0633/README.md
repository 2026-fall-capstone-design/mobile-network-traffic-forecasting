# 633의 작은 원본과 저장 예측

[연구 기록](../../records/0633-joint-selection-negative.md), [원문별 범위](../../sources/pilot-007.md), [검수](../../verification/pilot-007.md)를 함께 읽는다.

[manifest](manifest.json)는 173개 원본 경로와 실제 읽기·보존 위치를 연결한다. 새 보존 사본은117개·3,040,697bytes다. 기존 동일 바이트는 다른 묶음 사본을 가리킨다. 원문 `.py.txt`·`.md.txt`는 역사 자료다. 읽기용 정리문과 달리 원본의 개인 경로나 옛 지시 문구도 바이트 그대로 남아 있다.

주요 근거는633 계획·결과·세 코드, 고정 group/설정, native22group 예측과 오류/봉인/정산, 616의 입력과 HGB22group 출력, 562/567의 자료 출처·singleton cache, 581/632의 고정 RCTL24group 평가 자리와 재사용 출처·학습 이력이다. 평가 자리24개가 독립 모델24개 또는633의 신규 학습24개라는 뜻은 아니다. 633의 RCTL 신규 학습은0이다.

팀은 저장소만으로 다음 검산을 수행할 수 있다. 원본 연구 코드나 모델은 실행하지 않는다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_joint_selection_pilot.py \
  --source docs/research/evidence/0633/manifest.json \
  --output .research-archive/local-0633-check.json
```

원래 환경 전체·H5 원자료·checkpoint는 이 근거 묶음에 복사하지 않았다. 이번 검산은 보존 배열과 설정의 대응이며 원자료 처리나 모델 추론 재현이 아니다. checkpoint·구현 파일의 별도 로컬 해시 확인은 manifest에 범위를 명시했다.
