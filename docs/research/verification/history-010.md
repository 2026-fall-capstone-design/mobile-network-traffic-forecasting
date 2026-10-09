# history-010: 16–17 시간 유효성 진단 검수

[기록](../records/0016-0017-temporal-validity.md)·[출처](../sources/history-010.md)·[manifest](../evidence/0016-0017/manifest.json)·[주장11개 대조](history-010-primary-review.json)를 연결한다. 원 계획·코드·저장 출력의 의미를 같은 아카이브 에이전트가 작성 후 다시 대조했다. 독립 연구자의 과학적 검증이나 원 모델 실행 재현을 뜻하지 않는다.

| 검사 | 확인한 범위 | 결과 파일 |
|---|---|---|
| 저장 수치 173검사 | 10출처 해시, 최종 배열9개, checkpoint 배열3개, 32cell·4주·3정책·2모델, 원 summary의 모든 성능 집계·고정 선택·단순 대조 | [portable 검산](history-010-risk-check.json) |
| 원 H5 로컬 32검사 | 전체 해시·지정 구간의 날짜/scale/Y/queryY/naive/X16열·추가16cell의 사분위 소속 | [로컬 자료 대조](history-010-local-data-check.json) |
| 오염 입력 11종 | 출처3종 누락·중복ID·summary 평균·첫 주 선택·fit수·shape·lag·origin·checkpoint 불일치가 거부되는지 확인 | [음성 검사](history-010-negative-check.json) |
| 문서·원본 대조 | 원본/목록/사본 해시·읽기 범위·11개 주장 출처·수치표25행·원본 상태 파일6개·정리 파일 해시 | [문서 검사](history-010-document-check.json) |

Portable 검사는 저장 Y에서 복원 가능한 뒤1,008행의 lag/24시간 통계와 전체 calendar를 확인한다. 첫168행까지 포함한 입력1,176행 전체는 별도 로컬 H5 검사에서 확인했다. H5 대조 시 시간 sine열의 최대 차이는1.1102230246251565e-16, 나머지15열은0이며 `rtol=atol=1e-12` 이내다. scale·정답·단순 예측은 정확히 같다. 원 무작위 순열을 새로 실행하지 않았으므로 seed로 같은 추가 cell이 선택되는 것까지 재현했다는 주장은 하지 않는다.

CI에 추가한 [검산 스크립트](../../../scripts/research_archive/verify_temporal_validity_history.py)는 보존 자료만 읽으며 원 연구코드 import·학습·추론·난수 생성을 하지 않는다. 대용량 원 H5가 없는 환경에서도 실행한다.

```bash
uv run --locked --group archive python scripts/research_archive/verify_temporal_validity_history.py \
  --manifest docs/research/evidence/0016-0017/manifest.json \
  --output .research-archive/ci-0016-0017.json
```

모든 cell·주 평균과 날짜별 손해를 보존했다. 날짜별 집계는 정리 중 추가한 산술이고 원 summary의 보고 필드가 아니다. 첫 주에 고른 정책은 이후3주에서 변경하지 않았으며 이후 정답으로 선택을 고친 절차는 없다. mean·cell·cell×week·day의 분모와 전체4주/후속3주의 기간을 구분한다. 평균이 좋아도 모든 날짜에서 우위는 아니다.

보고된768fit·30.648936100초·174,518,272bytes를 비용 재측정으로 표현하지 않는다. elapsed는 최종 출력 쓰기 전에 끝나고 RSS는 fit 뒤의 표본 관측이다. 모델 재실행·난수 simulation·원 연구 코드 실행은0이다. 이 검사는 참 conditional drift·독립 최종 기간·RCTL 성능·미래 무손해·신규성을 입증하지 않는다. 기록17의 세 문헌 방법과 후속 공간 정보 이력은 미검수로 남는다.

공통 archive integrity는 보존 바이트·목록·로컬 링크를 검사하며 외부 링크의 현재 접근이나 원문 해석을 자동으로 증명하지 않는다. 기계적 검사 통과와 실제 열람·의미 대조·전체 연구 완료를 구분한다.
