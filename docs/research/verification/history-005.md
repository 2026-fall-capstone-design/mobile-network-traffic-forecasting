# history-005 검수 — 공식 코드·자산·초기 출력

검수 대상은 [05 공식 구현 기록](../records/0005-official-tabicl-audit.md)과 [구현 비교](../references/official-tabicl.md)다. 05 전체 문헌·전체 공식 구현·전체 연구환경의 검증은 아니다. 같은 에이전트의 원문 대조이며 독립 연구자의 과학적 검증으로 표현하지 않는다.

| 검수 | 결과·범위 |
|---|---|
| 공식 구현 연결 | 6개 코드의 runtime·고정commit raw·보관ZIP member가 바이트 단위로 일치. 2파일 전체·4파일 지정 구간 읽기 |
| 설치·가중치 | 설치metadata Name/Version 확인. checkpoint 해시·크기와 공식HF LFS 대조. config의25개 단순 값 확인 |
| checkpoint 검사 방식 | 직렬화 member의 opcode·단순 설정만 읽음. 역직렬화 실행·tensor 로드·torch import 없음 |
| 자산 대조 | [119개 검사](history-005-official-check.json). 이 수에는 해시·크기·config token 형식 등이 포함되며 독립 연구 주장119개라는 뜻이 아님 |
| 저장 출력 대조 | [18개 검사](history-005-saved-output-check.json). 로그각16행, B1 16×1088×129 및 B2 16×168×129, B1 중앙 열=저장median |
| 주장 대조 | [H005-C01–C09](history-005-primary-review.json): 고정 버전·fit·분위수/통계·호출·cache·표현·forecast·대체 비교 범위 |
| 원문 보존 | 기존 보존8개 재사용·새 원문0. 공식코드·설치metadata·checkpoint·ZIP은 identity/공식주소만 추가 |
| 새 모델 실행 | 0. 과거 연구 코드 import·실행, 새로운 난수 실험 없음 |

문서·출처·표와 최종 저장 해시는 [문서 검사](history-005-document-check.json)에 기록한다. 자동 검사가 의미 검토를 대신하지 않는다. GitHub 아카이브 검사는 보존 근거의 바이트와 로컬 링크를 확인하며 외부 코드를 다시 다운로드하거나 모델을 실행하지 않는다.

이번에 분명히 한 구분은 다음과 같다.

- 보관 checkpoint config의999개, 기본 API 반환9개, 초기 실험의129개는 다른 계층의 수다.
- API mean은 보정된 native 분위수의 평균이고 median은alpha0.5 ICDF다. 저장129분위수 중앙 열의 일치는 calibration 보장이 아니다.
- 초기 B1·B2의 cache 인자 생략은 이 공식 버전에서False다. 후속 KV cache 설정이나 저장 배열 재사용과 섞지 않는다.
- fit 로그는 변환·예측 준비 비용이다. foundation 가중치 훈련 시간이나 전체 연구시간으로 재명명하지 않는다.
- 공식 forecast wrapper의 존재와 현재 후보의 clustering/RCTL 효용은 별개다. context에 의존하는 표현을 조건 없이 공유하는 근거로 쓰지 않는다.

공식 코드 여섯 파일과 metadata의 현재 보관 상태를 확인했지만 당시 전체 프로세스의 설치환경·가중치 로드를 독립 재현하지 않았다. 사전학습 자료·모든 tensor·의존성·하위 dispatcher/transformer·지정 범위 밖 코드도 미검토다. `_align_covariates`의 설명을 실제 열 삭제까지 검증한 것으로 옮기지 않았다.

회귀 TabPFN의 당시 미실행은05의 서술과 초기 구현에 한정했다. 이후 기록 전체에서의 미실행을 전수 증명하지 않았다. Localized TabICLv2·TL-ANDI·CRUMB·Entangled by Design·TabClustPFN·Amortized TS clustering은 다음 묶음으로 남겨 **05 전체 미완료**를 유지한다.
