# 05 공식 구현·초기 호출 근거

[연구 기록](../../records/0005-official-tabicl-audit.md)과 [공식 코드 비교](../../references/official-tabicl.md)의 근거다. [manifest](manifest.json)은 기존 보존 파일8개, 일차자료 metadata8개, ZIP 해시·지정 member 대조1개를 구분한다. 새 원문 사본은0개이며 코드·checkpoint·논문 전문을 추가 게시하지 않았다.

| 자료 | 재사용 위치·역할 |
|---|---|
| 05 원문 | [SRC-0020826](../0005/originals/SRC-0020826.md.txt): 공식 기능·제안·당시 미실행 서술 |
| 자산 manifest | [SRC-0022507](../0001-0002/originals/SRC-0022507.json): 코드 ZIP·checkpoint의 고정 주소·크기·해시 |
| B1·B2 호출 코드 | [B1](../0003-0007/originals/SRC-0023116.py.txt), [B2](../0003-0007/originals/SRC-0022942.py.txt): 직접 regressor·129alpha·median·cache 설정 |
| 호출 로그 | [B1](../0003-0007/originals/SRC-0023601.json), [B2](../0003-0007/originals/SRC-0023586.json): 각각16개 context의 행 수와 fit/predict 시간 |
| 저장 배열 | [B1](../0003-0007/originals/SRC-0023605.npz), [B2](../0003-0007/originals/SRC-0023589.npz): 지정 출력 필드의 shape·median 일치 확인 |

공식 코드 여섯 파일은 manifest의 고정 commit URL로 접근한다. 설치 METADATA는 로컬 보관 identity와 읽은 필드만 연결하고 공개된 공식 파일과 바이트가 같다고 표시하지 않았다. checkpoint의 고정 공식 주소와 SHA-256은 [자산 대조](../../verification/history-005-official-check.json)에 있다. config는 모델을 실행하지 않고 직렬화 데이터의 단순 값으로 읽었다.

[출처와 실제 열람 범위](../../sources/history-005.md), [검수 범위](../../verification/history-005.md). 과거 코드는 읽기용 `.py.txt`이며 실행 지시가 아니다. 보존 배열을 다시 읽은 작업은 새 모델 실험이나 독립 예측 재현으로 세지 않는다.
