# 논문과 고정 구현의 대조 항목

[22개 주장](../../records/0077-dynamic-membership-dlm.md) · [위치와 해시](../../verification/history-077-claims.json)

아래는 원문과 코드의 정적 관찰이다. 이번에 실행 오류나 성능 변화를 관측하지 않았다. 원래 논문이 이 commit으로 모든 그림을 만들었다고 확정하지도 않는다.

| 항목 | 실제 저장 코드 | 해석의 범위 |
|---|---|---|
| 점추정 소속 likelihood | common.py92–129: η 인자를 받지만 density 정규화에 사용하지 않음 | 논문 p11–12 및 sampler의 η×density와 대조. 전체 알고리즘에서 EDP가 사라진다는 뜻은 아님 |
| backward mode | dirichlet.py220–250: mean helper 호출;178–217의 S는 mode | 정확한 전체 posterior mean이라고 단정하지 않음 |
| 가중 DLM | dlm.py622–655: weight>1e-3,filter→smoother,잔차/T 뒤 전체 weight 합으로 나눔 | 작은 weight 처리와 분산 정규화의 통계식 검토 필요 |
| 다변량 관측 | dynamic.py215는 Y[t,i], common.py87는 m개열 index map | m>1수정 메시지만으로 모든 경로 정상 판정 불가 |
| 0 weight fallback | dynamic.py219–225: signed residual sum argmin | 절댓값·제곱 거리 아님. runtime 실패는 미관측 |
| δ 추정 분기 | dirichlet.py267의 c0=.01,273의 Z차가 nonzero일 때 가산 | dynamic의 c0=.1 및 같은 범주 갱신 재귀와 대조. model_delta=True에만 연결 |
| 상태 sampling | dynamic.py260–266: smoother 후 각 시점 주변분포에서 별도 sampling | joint FFBS 경로와 동일하다고 표시하지 않음 |
| burn-in/평균 | dynamic.py274–277 그대로 chain 반환,148–165 전체 mean | 주석의 burn-in 제거와 차이. 정수 label mean을 범주별 소속 확률로 읽지 않음 |
| precision shape | dynamic.py255의 시점별 n_j,271의 sum(n_j)*T+1 | 시간 합 뒤 추가T의 의미는 미검증, 적절한 posterior라고 확정하지 않음 |
| 초기화 | common.py267의 최대거리,276–278의 다른F/G TODO | 논문 p8–9 전체 절차 구현으로 간주하지 않음 |
| API 설명 | dynamic.py33–37은4반환 설명,93은δ까지5반환 | 호출 전에 실제 인터페이스 확인 필요 |

## 인쇄본의 미해결 표기

PDF를 렌더해 확인한 차이이며 추출 오류라는 이유로 조용히 고치지 않는다.

| 위치 | 남긴 차이 |
|---|---|
| p6 Eq6/7/8 | 관측 항에 시간 합이 명시되지 않은 표기, Eq6/7 상태 항 cluster 합의 상한 n |
| p10 첫 관측식 | Σ_j∏_t 형태로 인쇄된 합·곱 순서와 시간별 잠재 소속 설명의 대응 확인 필요 |
| p14 Figure4 | 캡션 시작1996과 축1990 차이 |
| p16 재생에너지 설명 | Estonia 국명 반복 |
| p20 Morocco | 2017로 인쇄된 연도와 자료 종료2007 차이 |
| p20 Figure13 | 캡션의 North Africa/Turkey와 본문의 Albania/Bosnia/Mauritius/Reunion 차이 |

이 표기·구현 관찰은 2020 저장본에 한정한다. 원77의 미채택 판단은 그 당시 원문에서 제시한 정보 범위·공유 이득·대안·비용 조건과 함께 보존한다.
