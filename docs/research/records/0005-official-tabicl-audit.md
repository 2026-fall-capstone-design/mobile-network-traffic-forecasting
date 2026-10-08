# 05 — 공식 TabICL과 초기 실행 설정의 연결

05는 TabICLv2의 고정 가중치를 cell별 context에 적용하되, **모델이 제공하는 기능과 실제 clustering 실험에서 사용한 기능을 구분**했다. 공식 시계열 pipeline의 존재, 회귀용 분위수 출력, context에 의존하는 표현은 확인할 수 있다. 이것만으로 clustering의 신규성이나 RCTL 성능 개선이 성립하지는 않는다.

이 페이지는 05의 공식 코드·자산·초기 호출 부분을 정리한다. [가까운 다섯 방법](0005-closest-methods-audit.md), [네트워크·시계열 아홉 문헌](0005-network-timeseries-audit.md)에 이은 부분 기록이다. 관련 여섯 연구와 이후 대체 모델 비교의 통합은 남아 있으며 **05 전체 완료로 집계하지 않는다.** [보존 원문](../evidence/0005/originals/SRC-0020826.md.txt), [지정 근거와 검수](../verification/history-005.md).

| 항목 | 확인한 범위 |
|---|---|
| 당시 시점·질문 | 2026-09-25. 고정 회귀 모델의 분포를 자료 공유 결정에 쓰는 후보가 기존 기능과 어떻게 다른가 |
| 수행 종류 | 05는 문헌·설계 감사. 실제 예측은 기존 B1·B2 실행으로 연결하며 새 실험으로 중복 집계하지 않음 |
| 공식 코드 | commit `0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3`. 지정한 6개 파일의 보관 runtime·소스 ZIP·공식 raw가 바이트 단위로 일치 |
| 설치·가중치 | 보관 METADATA는 TabICL 2.2.0. `tabicl-regressor-v2-20260212.ckpt`의 크기·SHA-256이 고정 Hugging Face revision의 LFS metadata와 일치 |
| 당시 자료·입력 | Milan 16cell, context target168–671의 504행, 최근 이력·일/주 lag·통계·달력 총16특징. 구체적인 정규화·분할은 [B1](0003-b1-anchor-projection.md)과 [B2](0004-0007-b2-observed-risk.md) 참조 |
| Tab 호출 | 두 코드 모두 ensemble1·batch_size1·CPU·seed20260925·n_jobs1. AMP/FA3/offload/자동 다운로드False |
| 이번 검수 | 코드 읽기·자산 해시·checkpoint의 단순 설정값·저장 출력 대조. 모델 로드·추론·훈련·과거 연구 코드 실행0 |

현재 남은 파일과 공식 파일의 일치는 출처 연결을 강화한다. B1의 봉인 자료가 전체 설치환경과 checkpoint를 모두 기록한 것은 아니므로 당시 프로세스의 환경을 독립적으로 재현했다는 뜻은 아니다. [자산·구현 비교](../references/official-tabicl.md), [공식 대조 결과](../verification/history-005-official-check.json).

## 999·9·129는 서로 다른 수다

| 수 | 의미 | 이번 확인 |
|---|---|---|
| 999 | 보관 checkpoint config의 `num_quantiles`, 회귀 `max_classes=0` | 설정의 직렬화된 단순 값과 모델 constructor의 출력 연결 확인 |
| 9 | `quantiles` 출력에 alpha를 주지 않을 때 기본0.1–0.9 | 공식 모델·forecast engine의 기본 반환 수준 |
| 129 | B1·B2가 명시한 `(j+0.5)/129`, j=0…128 | 코드와 저장 배열 대조. 가운데 index64는0.5 |

129개를 요청한 것은 모델의 사전학습 출력 head를129개로 교체한 일이 아니다. 공식 코드는 native 분위수에 단조 보정을 적용한 뒤 요청한 alpha에서 ICDF를 반환한다. `raw_quantiles`도 이 경로에서는 단조 보정 후 값이므로 가공 전 head 출력과 같은 뜻으로 쓰지 않는다. [출력 경로와 읽은 구간](../references/official-tabicl.md).

B1은 같은 호출의 median·mean·129quantiles를 모두 저장했고, **저장 median은129분위수의 index64와 배열 전체에서 정확히 일치**했다. B2는129분위수를 저장하고 그 중앙값에서 공통 Ridge를 뺀 값을 median 대안에 사용한다. 공식 API의 기본 점예측은 mean이므로 MAE용 median을 선택한 당시 코드를 생략하면 비교 조건이 바뀐다. 값의 척도는 모델에 넣은 cell별 정규화 target이며 원단위 Milan activity로 자동 복원되는 것이 아니다. [저장 출력 검수](../verification/history-005-saved-output-check.json).

## fit 비용과 cache 설정을 구분한다

공식 `TabICLRegressor.fit`은 checkpoint를 읽고 target·입력 변환과 ensemble을 준비하며, 설정에 따라 context cache를 만든다. 해당 경로는 현재 cell 자료로 foundation-model 가중치를 최적화하는 훈련이 아니다. 그렇다고 준비 비용이0인 것도 아니다.

| 기존 실행 | context 수 × query 수 | fit 로그 합(초) | predict 로그 합(초) | 두 합(초) |
|---|---:|---:|---:|---:|
| B1 | 16 × 1088 = 17,408 | 7.4334117 | 92.8880715 | 100.3214832 |
| B2 | 16 × 168 = 2,688 | 4.8772370 | 26.6554663 | 31.5327033 |

이는 당시 저장된 호출 로그를 합산한 값이다. 앞뒤 자료 준비·clustering·문서화 또는 RCTL을 포함한 전체 작업시간이 아니다. B1 query는 공통 anchor64와16cell별64개를 합친 것이고, B2는 각 cell 자신의168개 query다. 서로 다른 호출량을 같은 성능·비용 실험으로 비교하지 않는다. [B1 로그](../evidence/0003-0007/originals/SRC-0023601.json), [B2 로그](../evidence/0003-0007/originals/SRC-0023586.json).

초기 두 실행 코드는 `kv_cache`를 지정하지 않았고, 대조한 공식 constructor의 기본값은False다. 따라서 후속 기록의 KV cache 활성 설정을 초기 B1·B2에 소급하지 않는다. 저장 예측 배열을 다시 쓰는 것과 모델 내부의 context cache를 사용하는 것도 구분한다. [B1 코드](../evidence/0003-0007/originals/SRC-0023116.py.txt), [B2 코드](../evidence/0003-0007/originals/SRC-0022942.py.txt).

## 재사용할 수 있는 기능과 아직 입증하지 않은 해석

고정 checkpoint의 target-aware embedding은 context의 Y를 포함한다. regressor의 변환 준비 역시 context 자료에 의존한다. 따라서 가중치가 같다는 사실만으로 서로 다른 context의 앞 단계 cache를 그대로 교체하거나 embedding 거리를 동일한 기준으로 해석할 수 있다고 결론 내리지 않는다. attention을 sample의 인과적 기여도 또는 RCTL 공유 이득으로 해석하는 근거도 이번 코드 확인에 없다.

같은 공식 commit에는 `TabICLForecaster`가 이미 있다. 기본 시간 특징은 index/datetime/periodic이고, `max_context_length=4096`은 이 wrapper의 설정이다. 이를 TabICL 모델 전체의 보편적 행 수 한계로 옮기지 않는다. B1·B2는 이 wrapper 대신 실제 lag 입력을 가진 `TabICLRegressor`를 직접 사용했다. 그러므로 ‘TabICL의 최초 시계열 적용’은 당시 후보의 기여로 삼을 수 없다.

05는 회귀 TabPFN도 같은 역할의 대안으로 검토하고 같은 정보·context/query·ensemble 조건 또는 실제 비용 조건에서 비교해야 한다고 적었다. 당시 누적 예산에서는 실행하지 않았다는 **05의 범위에 한정한 기록**이다. 이후 전체 연구에서 한 번도 사용하지 않았음을 전수 확인한 결과나, 두 API가 완전히 같다는 보장은 아니다.

팀원은 새 실험을 설계할 때 checkpoint·코드 revision, 출력 alpha·median/mean, 실제 context/query 수, cache와 준비 비용, 실제 label 접근 범위부터 기존 조건과 비교하면 된다. 같은 배열의 재분석은 재사용으로 기록한다. 달라진 정보·자료 기간·모델·비용 조건이 없으면 기존 호출을 새로운 방법 검증으로 세지 않는다. [관련 여섯 연구의 후속 대조](0005-related-foundations-audit.md)는 같은 context의 국소화·배치 공유와 별도 clustering 사전학습을 이 고정 회귀 경로와 구분한다.

[출처·실제 읽은 구간](../sources/history-005.md), [근거 목록](../evidence/0005-official/README.md), [과거 시도 색인](../prior-attempts.md).
