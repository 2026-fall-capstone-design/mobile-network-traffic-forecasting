# 공식 TabICL — 고정 구현과 초기 연구의 연결

기준은 최신 배포판 일반론이 아니라 05가 지정한 [공식 commit](https://github.com/soda-inria/tabicl/tree/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3)이다. 아래 여섯 파일은 보관 runtime·소스 ZIP·공식 raw의 바이트가 일치했다. 코드 두 개는 전체, 네 개는 지정 구간을 읽었다. 설치 METADATA와 checkpoint 설정은 따로 확인했다. [ID·해시·구간](../sources/history-005.md), [대조 결과](../verification/history-005-official-check.json).

| 구현 | 확인한 기능 | 연구에 적용할 때 구분할 점 |
|---|---|---|
| [regressor.py](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/_sklearn/regressor.py#L245) | constructor·checkpoint 로드·fit·cache·predict | fit이라는 이름을 가중치 재훈련으로 세지 않음. 출력은 입력 target 척도로 inverse transform |
| [tabicl.py](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/_model/tabicl.py#L524) | 회귀 head와 예측 통계 | checkpoint 설정999와 반환9/129를 구분. 평균·중앙값·raw 반환의 처리 경로 확인 |
| [quantile_dist.py](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/_model/quantile_dist.py#L1478) | 기본 확률격자·단조 보정·ICDF 입출력 | 999의 기본 수준은0.001–0.999. 반환 alpha 수가 새 사전학습 head 크기는 아님 |
| [embedding.py](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/_model/embedding.py#L340) | feature grouping과 context target의 embedding 참여 | 고정 가중치가 context와 무관한 표현·cache를 보장하지 않음 |
| [_forecaster.py](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/forecast/_forecaster.py) | 시계열 context 준비·시간 특징·forecast engine 연결 | 기본4096은 wrapper 설정. 하위 transformer·dispatcher 전체 검토는 아님 |
| [_engine.py](https://github.com/soda-inria/tabicl/blob/0dbff3ec8fc68c123c87af77b0ea8b25cd2d23f3/src/tabicl/forecast/_engine.py) | regressor 호출과 mean/median·분위수 반환 | docstring의 Train만 읽고 새 가중치 학습으로 해석하지 않음 |

## 코드·설치·checkpoint의 연결

보관 설치 METADATA의 첫35행에서 Name `tabicl`, Version `2.2.0`을 확인했다. [자산 manifest](../evidence/0001-0002/originals/SRC-0022507.json)의 코드 ZIP SHA-256은 `810631974c22f2133e4890ca9953f475d13150835837f400b9fa5418970646ed`다. 지정 여섯 파일만 공식 코드와 대조했으며 전체 설치환경·모든 의존성·모든 압축 내용을 검토했다고 세지 않는다.

checkpoint의 SHA-256은 `0db9cb538f114e79026bf08f45f41ad8dd7ad2de2aaca9a5ca8cd3bd9748ae7a`, 크기는114,324,594바이트다. 고정 revision `4dcd344ece2c00be9e831fdd35bed57b5ad83e19`의 [공식 Hugging Face metadata](https://huggingface.co/api/models/jingang/TabICL/tree/4dcd344ece2c00be9e831fdd35bed57b5ad83e19?recursive=false&expand=false)와 일치했다. 이번에는 모델을 다운로드·로드하지 않았다.

보관 checkpoint의 `refactored_model/data.pkl`에서 byte offset73791–74475의 config 항목을 단순 문자열·수치·불리언과 그 내부 참조로 읽었다. `max_classes=0`, `num_quantiles=999`, `col_feature_group="same"`, `col_feature_group_size=3`, `col_target_aware=True`를 확인했다. 이는 constructor 기본값만 보고 추정한 설정이 아니다. 역직렬화 실행, torch import, tensor 로드, 사전학습 자료 검토는 하지 않았다.

## 출력과 비용의 의미

모델의 `predict_stats`는 native 분위수에 단조 보정을 적용한다. 기본 방식은 정렬이다. median은alpha0.5의 ICDF이고, mean은 보정된 native 분위수 값의 산술평균이다. 따라서 이 API의 mean을 별도 꼬리 모델까지 적분한 정확한 분포 평균이라고 바꾸어 부르지 않는다. 기본 `quantiles` 요청은0.1–0.9이고, 사용자가 지정한 alpha는 ICDF로 반환된다. cache 사용 경로에도 같은 통계 분기가 있다.

regressor는 결과를 target scaler로 역변환한 뒤 ensemble 축을 평균한다. B1·B2는 ensemble1이므로 여러 구성원의 median을 평균하는 문제는 해당 실행에 없다. B1은 mean도 보관했지만 직접 MAE 비교에는 median을 썼다. 저장 median과129격자의 중앙 열이 일치한 확인은 두 저장 필드의 일관성 검수이며 조건부 calibration의 증명이 아니다.

`fit`은 checkpoint·입력/target 변환·ensemble 준비를 포함하고, `kv_cache`가 활성화된 경우 추가로 cache를 만든다. 지정 `fit`·예측 경로에는 현재 자료로 가중치를 최적화하는 단계가 없으며 예측은 `torch.no_grad` 아래 수행된다. 초기 B1·B2가 생략한 `kv_cache` 인자는 이 버전에서False다. 후속 cache 실험의 비용을 초기 호출에 소급하거나 준비 시간을 제외한 추론 시간만으로 모델 비용을 대표하지 않는다. [당시 로그·배열 연결](../records/0005-official-tabicl-audit.md).

## 표현·시계열 wrapper에서 넘지 않을 경계

feature grouping의 `same` 경로는 지정 크기만큼 열을 순환해 묶는다. target-aware 경로는 train 부분에 Y embedding을 더하고 context 경계를 transformer에 전달한다. query의 정답을 받아 embedding에 더하는 경로로 읽지 않는다. 서로 다른 context의 표현이 동일 좌표계의 비교 가능한 거리라는 보장이나 attention의 인과적 의미는 이 구현 확인에서 나오지 않는다.

forecast wrapper는 index/datetime/periodic을 기본 시간 특징으로 등록하고 context 준비→특징 변환→engine을 연결한다. 기본 점예측은mean이며 median을 선택할 수 있다. B1·B2는 이 wrapper를 실행한 성능 결과가 아니라 직접 regressor를 사용한 결과다.

`_align_covariates`의 docstring에는 공통 공변량 사용을 적지만, 함수 자체는 공통 열을 확인한 뒤 원래 frame을 반환한다. 이 문구만으로 실제 열 삭제까지 검증했다고 표시하지 않는다. 하위 변환·dispatcher 전체 동작, 전체 사전학습·fine-tuning, 다른 context 간 안전한 cache 공유, 최신판 변화는 이번 범위 밖이다.

회귀 TabPFN의 동일 정보/실제 비용 비교는 [05 원문](../evidence/0005/originals/SRC-0020826.md.txt)의 제안·당시 미실행 범위로 남긴다. Localized TabICLv2·TL-ANDI·CRUMB·Entangled by Design·TabClustPFN·Amortized TS clustering은 이후 문헌 묶음에서 실제 판본과 주장에 대조한다.
