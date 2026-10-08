# 05 네트워크·시계열 비교의 재사용 근거

[manifest](manifest.json)는 기존 보존 원문9개와 외부 일차자료11개의 metadata를 연결한다. **새 원문 사본은0개**다. 같은 파일을 여러 문헌 비교에서 사용한 것을 독립 실험이나 새 고유 자료로 세지 않는다. 외부 논문은 전문을 재게시하지 않고 공식 링크·판본·해시·검토 구간을 등록했다. UPC는 조사 루트 밖의 기존 검토를 별도로 연결한다.

| 자료 | 재사용 목적 |
|---|---|
| [05 원문](../0005/originals/SRC-0020826.md.txt) | 당시 문헌·설계 판단과 정리본의 서지 정정 구분 |
| [특징 생성](../0001-0002/originals/SRC-0022703.py.txt) | 초기16특징과 정규화 |
| [B1 코드](../0003-0007/originals/SRC-0023116.py.txt) / [결과](../0003-0007/originals/SRC-0023604.json) | PCC/random/cross-error 소속의 출처 |
| [B2 코드](../0003-0007/originals/SRC-0022942.py.txt) / [결과](../0003-0007/originals/SRC-0023588.json) | 세 소속의 재사용과 다섯 RCTL 비교 소속 |
| [RCTL 코드](../0003-0007/originals/SRC-0023202.py.txt) / [고정 설정](../0003-0007/originals/SRC-0030238.json) / [결과](../0003-0007/originals/SRC-0030280.json) | 입력·29task·8개 MAE 집계 연결 |
| [기존 원예측 검산](../../verification/history-001-risk-check.json) | 이번 문헌 비교와 독립 재현으로 중복 집계하지 않는 배열 검수 |
| [이번 소속·설정 대조](../../verification/history-004-implementation-check.json) | 원본 identity와 저장 소속·task·summary의110개 검사. 완성 문서 검수와 별도 |
| [일차문헌 장부](../../verification/history-004-primary-review.json) | 지정 구간·시각 검토·논문 보고표·해석 한계 |

과거 `.py.txt`와 `.md.txt`는 읽기 위한 자료이며 실행하지 않았다. 모델·checkpoint·원자료 전체를 이 묶음에 새로 포함하거나 현재 환경에서의 재현 성공으로 표시하지 않는다. [05 기록](../../records/0005-network-timeseries-audit.md), [출처 안내](../../sources/history-004.md), [검수 범위](../../verification/history-004.md)
