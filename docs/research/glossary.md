# 연구 용어

[연구 안내](README.md) · [원86 학습 공유](records/0114-shared-training-scope.md) · [원96 파라미터 병합](records/0126-rctl-parameter-merging-scope.md)

아래는 원86·96에서 구별한 용어다. 전체 과거 자료의 용어 정리는 계속 진행한다.

| 용어 | 이 기록에서의 뜻 |
|---|---|
| 출력 혼합 | 여러 모델이 낸 예측값을 가중합하는 연산. 각각의 출력 계산이 필요하다. |
| 파라미터 병합 | 학습된 모델의 계수를 합쳐 하나의 모델로 만드는 작업. 내부 좌표·상태 처리와 성능 확인이 별도다. |
| 공통 무작위 초기화 | 같은 seed·구조로 학습을 시작하는 조건. 공통 사전학습 가중치나 최종 가중치의 동일함을 뜻하지 않는다. |
| 공통 사전학습 checkpoint | 이미 학습된 같은 모델 상태를 복사해 후속 학습의 출발점으로 쓰는 조건. |
| 지속 파라미터 공유 | 여러 자료의 gradient가 같은 파라미터 객체를 학습 중 함께 갱신하는 방식. 초기값만 복사하는 것과 다르다. |

같은 함수의 출력, 내부 파라미터의 좌표, 저장량과 실제 예측 입력 수를 구분한다. 자세한 근거와 적용 범위는 위 개별 기록과 [네 문헌 비교](references/parameter-merging.md)에 연결했다.

[원97](records/0127-forecast-time-reuse-diagnostic.md)의 **출력 유지(hold_output)**는 마지막 예측 자체를, **증가량 유지(hold_increment)**는 현재 관측+마지막 예측 증가량을 사용한다. 후자는 매시간 관측을 계속 요구한다. 신경망 내부의 정확한 delta 갱신, 같은 cell의 출력 근사, 다른 cell의 대표 예측, 재학습 주기는 별도로 구분한다.

[원98](records/0128-quantile-information-and-pooling-objective.md)의 **이상적 공유 비용**은 참 중앙값을 아는 경우의 손실 차이, **추정 초과 MAE**는 유한 자료에서 중앙값을 추정하면서 더해지는 주항이다. **불가피한 MAE**와 분리한다. **목표 분위수 밀도**는 한 점/구간·단위·조건을 명시하고, 입력 회귀의 정보 행렬이나 비선형 RCTL의 학습 정보와 같다고 두지 않는다.

[원99](records/0129-learning-units-and-clustering-cost.md)에서 **학습 단위**는 cell sample/ODflow벡터/하루MTS를 구별한다. **운영K**와**matched-K 구조분석**, **등록parameter/학습가능parameter/state tensorbytes**, **optimizer update/forward row/호출 횟수**는 별개다. **MLU bias**는1에 가까운 비율이며 topology없는 활동량의MAE가 아니다.

[원100](records/0130-pretraining-objective-and-time-conditioning.md)에서 **잠재 cardinality K**, **실제 점유 label 수**, **필요한 RCTL 수**, **APT prototype 수/top-k**는 서로 다르다. **single-forward API와 내부 K별 계산**, **달력 조건 변환과 cell 학습 소속**, **인쇄 동률과 저자 first-count**도 구별한다.

[원101](records/0131-actual-pooled-context-and-rctl-ranking.md)의 **actual pooled context**는 소속내 실제sample을 context로 주는 것이다. **rolling one-step 구간336시간**은 실측lag를 쓰며 **open-loop horizon336**과 다르다. **같은16기초값**과 **16열/8×9입력표현**, **초기intra-op4**와 **predict중n_jobs1**, **partial NaN placeholder**와 **최종실패**도 구별한다.

[원102](records/0132-architecture-kernel-and-joint-risk.md)의 **NTK INIT/TRAIN**은 초기 kernel 극한과 학습 중의 연결을 구별한다. **target 공동 covariance**와 **activation/gradient covariance**, **고정 A**와 **target 적응 선택**, **주변 분위수**·**seed 평균95%CI**·**P90/P95 dataset 비율**, **한 버퍼 산술**과 **peak/runtime 실측**도 서로 다른 정보다.

[원103](records/0133-current-evidence-and-unapproved-extension.md)의 **조건부상한제안**은 승인/실제사용과다르다. **중간산출물완료**와 **최종연구완료**, **Global완비조건**과 **secondseed미실행**, **state tensor bytes**와 **checkpoint file bytes**, **허용오차내예측대응**과 **bit동일성**, **retainedPDF시각검토**와 **새Wordcompilation**도구별한다.

[원104](records/0134-resource-and-evidence-audit.md)의 **자원·근거 감사**는 새 성능 실험과 다르다. **조건부상한**과 **실제 승인·사용량**, **당시 파일의 응답 미기록**과 **모든 외부 대화 부재**, **과거Goal 감사 횟수**와 **현재 아카이브 상태**, **연결 기록의 재인용**과 **새 전문 검증·독립 재현**을 구별한다.

[원105](records/0135-blocked-audit-and-resume-conditions.md)에서 **감사JSON의 상태보고**와 **당시 도구응답의 별도복구**, **운영차단**과 **연구완료/모든가능성의 기각**, **문서바이트 동일성**과 **현재새판독/이전범위재사용**, **누적상한 증액**과 **실제후보 검증**을 구별한다.

[원106](records/0136-same-k-cellwise-error-transition.md)에서 **동일K/sample 수**와 **자료 구성/실제최적화 경로 통제**, **부호전이 항등식**과 **인과 기여율**, **저장배열 산술 대조**와 **독립 모델 재현**, **하나의 회계사건/두기록위치**, **잔여포함 계획상한**과 **실제사용**을 구별한다.

[원107](records/0137-calendar-retention-and-external-support.md)의 **k이웃 수/K소속 수**, **학습행 점유/density own비중**, **external/group 비중**, **훈련query절반 평균/개별cell·이후10일**, **sample개수/독립정보량**, **입력근접성/RCTL scaled MAE**를 구별한다.

[원108](records/0138-fixed-weight-bn-statistics.md)에서 **optimizer fit/모델상태 적합**, **EMA/유한집합 모멘트/불편분산 보정**, **평균 손해/cell·day 개선**, **복원144행/전체 예측 복원**, **파생원장/복구된 원본**, **저장값 검수/모델 재현**을 구별한다.

## online train / 공통 epoch / validation-selected checkpoint

[원109](records/0139-saved-training-path-and-stopping.md)의online train은학습중배치별가변가중치·train mode 손실의가중평균이다. validation은epoch종료뒤eval mode 값이다. 공통epoch는같은seed의여덟K4로그가모두남은구간으로42/43이다. validation-selected checkpoint 평균은서로다른best_epoch에서선택한4모델의최소validation 평균이며동시epoch나새test값이 아니다.

## profile 이동 / 원형 잔차 / 공통 mask / own query 합집합

[원110–111](records/0140-calendar-alignment-and-input-preflight.md)의 δij는 j[h+δ]를 i[h]에 맞춘다. 원형 잔차는 mod24의짧은 거리이고 pair별 최적을 하나의cell 좌표로 곧바로 쓸 수 없다. 공통 mask는세 이동의 지원교집합이며, own mask는같은target 시점의합집합이다.1222전체공통시점·807통과방향공통시점·2421세이동행·675own행·3096합계는다른집계다.

## 방향×query / target×query / 기간 기여

[원112](records/0141-calendar-predictive-selection-and-weighting.md)의402는방향×query이며 서로다른target×query는336이다. 동일target label을donor비교에서재사용한것을독립표본으로세지않는다. 이336은원101미래336행/cell과다른단위다. 각기간새평균과원래전체weight의기간기여도구별한다.
