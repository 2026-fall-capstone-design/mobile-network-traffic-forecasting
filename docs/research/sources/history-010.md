# 16–17 시간 유효성 진단의 출처와 열람 범위

[기록](../records/0016-0017-temporal-validity.md)·[보존 근거](../evidence/0016-0017/README.md)·[출처 JSONL](../catalog/history-010-sources.jsonl)·[검수](../verification/history-010.md)를 연결한다. 줄 번호는 해당 SHA-256의 UTF-8 텍스트에 Python `splitlines()`를 적용한1기준이다. 전체 원문을 읽은 것과 그 안의 모든 인용·후속 연구까지 검증한 것을 구분한다.

| Source ID | 원본 루트 아래 경로 | 실제 읽은 범위·역할 |
|---|---|---|
| SRC-0020991 | tmp/redesign_20260925/16_temporal_validity_diagnostic_plan.md | 전체1–32행. 질문·32cell선정·분할·보고·선택·상한 |
| SRC-0021004 | tmp/redesign_20260925/17_temporal_validity_findings.md | 전체1–26행. 수치·실행·방향 전환.18–22행의 세 문헌 주장은 미검수 |
| SRC-0023201 | tmp/redesign_20260925/temporal_validity_diagnostic.py | 전체1–123행 정적 열람. import/실행하지 않음 |
| SRC-0032490 | tmp/redesign_20260925/results/temporal_validity/run_started.json | 전체113행·모든JSON키. 계획 해시·32ID·설정 |
| SRC-0032489 | tmp/redesign_20260925/results/temporal_validity/run_finished.json | 전체5행·모든JSON키. fit수·시간 보고 |
| SRC-0032491 | tmp/redesign_20260925/results/temporal_validity/summary.json | Ridge/HGB/나머지 상위키로 나누어 모든 키·값 열람. 모든 저장 성능 집계를 배열과 대조 |
| SRC-0032487 | tmp/redesign_20260925/results/temporal_validity/predictions.npz | 모든9수치배열의 shape·유한값·매핑·지표. 원 추론 재현 아님 |
| SRC-0032488 | tmp/redesign_20260925/results/temporal_validity/predictions_partial.npz | 모든3수치배열. 최종pred/y/naive와 정확히 같음 |
| SRC-0020972 | tmp/redesign_20260925/15_transfer_identity_and_literature_findings.md | 이전 전체62행 열람 재사용. 후속 질문과 남은 범위는51–62행을 다시 대조 |
| SRC-0023589 | tmp/redesign_20260925/results/observed_risk_tables.npz | 기존cell_ids16개만 재사용. 다른 저장배열을 이번 범위로 합산하지 않음 |

앞8개는 새 바이트 보존, 뒤2개는 기존 보존 재사용이다. [manifest](../evidence/0016-0017/manifest.json)에 크기·SHA-256·동일 사본source_id와 저장소 경로가 있다. 파일 수·연구 기록 수·fit수는 다른 단위다.

대용량 **SRC-0023485**는 `tmp/redesign_20260925/assets/data_git_version.h5`다. 전체 파일 해시와 `data.shape`, `idx[:1344]`, `data[:672,:,2]`의전체10,000cell평균, `data[:1344,저장32cell,2]`를 읽었다. 이 범위로 정규화·활동량 사분위·정답·입력16열·단순 예측을 대조했다. 날짜 발췌는 이전 파생 파일을 그대로 재사용한다. 상류 CDR 처리 전체나 H5의 다른 열·기간을 이번 검수 완료로 세지 않는다. 이 외부 metadata1건은 새 논문이나 새 원자료의 팀 보존을 뜻하지 않는다.

원문16의 계획과17의 수치 판단을 정리했으며17 전체 통합은 미완료다. MGSTC·PID cellular forecasting·Joint clustering and QoS prediction의 지정 일차 방법과18이후 공간 정보 이력이 남는다. 15의 누적 비용 감사도 별개로 남겨 둔다. 당시 sklearn 등 패키지 버전과 실행 환경 lock은 이 묶음에서 확인하지 않았다. 과거 terminal handle의 exit0은 당시 문서 보고이며 새로 확인한 실행 로그가 아니다.
