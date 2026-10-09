# 04·06·07 — 실제 query 손실표 B2와 RCTL 사후 기각

2026-09-25의 연결된 설계·진단·판단 기록이다. B2는 [B1의 대표 입력 축약](0003-b1-anchor-projection.md)을 제거하고 실제 query의 분포로 group 손실을 합산했다. **후속 RCTL에서 관측 정답의 손실표보다 MAE가 두 seed 모두 컸고, 07은 이 후보를 추천 방향에서 제외했다.** 모든 Tab clustering 실패나 원인 하나의 확정을 뜻하지 않는다. [04 사전 계획](../evidence/0003-0007/originals/SRC-0020825.md.txt), [06 진단 계획](../evidence/0003-0007/originals/SRC-0020827.md.txt), [07 사후 판단](../evidence/0003-0007/originals/SRC-0020828.md.txt)

## 계획에서 실행으로 바뀐 내용

04는 각 cell의 실제 query168개를 그대로 Tab에 넣었다. 공통 기준 예측 `f0(x)`는 모든 context를 합친 StandardScaler+Ridge(alpha1)이고 cell ID는 특징에 넣지 않는다. 상태64개도 context만으로 정한 KMeans다. 비교하는 함수군은 `f_C(x)=f0(x)+a_C,state(x)`로, group별·상태별 하나의 보정값을 공유한다. 이 함수군은 실제 RCTL과 다르며 f0 예측은 RCTL의 입력·정답·최종 예측에 넘기지 않았다. [실제 구현](../evidence/0003-0007/originals/SRC-0022942.py.txt)

cell의 상태 b 손실표는 그 상태에 속한 query의 `|Q_i(u|x)-f0(x)-a|`를 분위수와 query에 대해 합해 `168×129`로 나눈 값이다. 전체168로 나누므로 상태 빈도가 반영되고 비어 있는 상태는0이다. group의 표는 덧셈으로 갱신하고 상태별 action 최소값의 합을 group 비용으로 쓴다. 병합은 disjoint pairs를 낮은 증가 비용부터 선택하는16→8→4이며, 실제 pooled 모델을 반복 학습하지 않는다.

**정리 과정에서 확인한 계획·구현 차이:** 04의 action 범위 문구는 해당 상태의 query residual-quantile 범위지만, 실제 코드는 Tab·관측 query 정답·KNN·median·median/IQR 다섯 대안의 최소/최대를 함께 사용해 공통257격자를 만든다. Tab 추론에는 query 정답을 전달하지 않았으나 **정답은 공통 action 범위의 후처리에 참여한다.** Tab 경로 전체가 query 정답을 전혀 사용하지 않았다고 요약하면 안 된다. 이는 개발 query672–839의 정답이며 마지막480개 평가 target을 격자에 넣었다는 뜻은 아니다. 실제 격자와 다섯 손실표를 이 구현 조건으로 검산했다.

empirical 대안은 같은 query의 실제 정답을 직접 손실에 사용한다. 각 대안의 정답 접근 범위가 다르며, 이미 query labels가 있는 clustering 상황에서 복잡한 분포 추정이 더 나은지 묻는 비교다. KNN32·median·median/IQR, 기존 PCC/random/교차오차 profile도 보존했다. 두 번째 RCTL seed는 02의 full risk/PCC 계획에서 04의 full risk/empirical 비교로 변경됐다. 04는 RCTL 실행 전 변경이라고 명시하고 봉인 해시가 대응 결과·계획·코드와 일치한다. 해시 일치는 내용 연결 증거이며 독립적인 실행 시각 증명과 구분한다. [소속 전 단계 해시](../evidence/0003-0007/originals/SRC-0023585.json), [실행 시 고정 설정](../evidence/0003-0007/originals/SRC-0030238.json)

## 자료·시점·모델과 비교 단위

| 구간/항목 | 실제 조건 |
|---|---|
| 자료와 cell | [B1의 동일16cell](0003-b1-anchor-projection.md), 시간별 internet activity, 원시점0–671의 cell별 평균으로 정규화 |
| Tab context | target168–671, 각504행×16특징 |
| 소속 추정 query | target672–839, 각168개. 129 midpoint 분위수, 64상태, 공통257action |
| surrogate 진단 | target840–1007, 각168개. 이미 본 개발 구간이며 독립 최종 검증 아님 |
| RCTL train | target168–839, 각672개. 첫168시간 lag 준비를 뺀 유효28일 target |
| RCTL validation | 840–1007, 각168개, checkpoint 선택과 patience 판단 |
| RCTL 평가 | 1008–1487, 각480개. 07에서 결과를 참조한 이후 후속 연구의 개발 자료 |
| Tab 설정 | B1과 같은 경로상 v2-20260212/ensemble1/CPU/seed20260925/n_jobs1, AMP·FA3·offload·자동다운로드False |
| RCTL 입력 | 최근8시간 sequence×9채널. 최근값 외 lag24/168·24시간 평균/표준편차·달력 특징을 각 step에 반복 |
| RCTL 설정 | Torch port, MAE, Adam lr0.001/eps1e−7, batch256, 최대80epoch, validation patience10, 초기 torch threads4/inter-op2 |
| 소속 비교 | Tab/empirical/KNN/PCC/random: K4, 각4cell씩4group. global K1은 보조 |
| seed·학습 자리 | 20260925에5×4+global1=21fit. 20260926에Tab/empirical만8fit. 합29fit |

Tab의 공통 Ridge/KMeans 구성은 context만 사용하고, RCTL은 모든 조건에 같은 train/validation/test 입력과 학습 절차를 쓴다. KNN/median/IQR 등의 surrogate와 RCTL은 모델·시점이 다르므로 숫자를 같은 성능표에 섞지 않는다. 교차오차 profile과 두 median 대안의 RCTL은 이 제한 실행에서 미실행이다. 원 UPC의 원래 규모 비교도 수행하지 않았다. [학습 코드](../evidence/0003-0007/originals/SRC-0023202.py.txt), [보존 Torch 구현](../evidence/0003-0007/../0639/originals/SRC-0023048.py.txt)

원 H5의 고정16cell 열을 읽어 정규화·저장 정답·시간 범위와 peak 임계값을 확인했다. peak는 RCTL train target168–839의95% 분위수를 초과하는 평가 시점이다. H5→저장 target 일치는 원 CDR 전처리 재현과 다르다. Torch 포트의 보존 코드와 해시는 확인했으나 원 논문의10분 자료·학습 조건·UPC 전체 또는 Keras/Torch 수치 동등성을 재현하지 않았다. [H5 지정 열 검사](../verification/history-001-H5-check.json)

## 실제 결과: surrogate와 RCTL을 분리한다

개발 following-week에서 각 대안이 자기 손실표로 고른 보정값의 정규화 MAE는 다음과 같다. 이 비교에서는 Tab이 empirical보다 조금 낮아도 median/IQR보다 높다. 그 순서가 RCTL 결과를 보장하지 않는다. [surrogate·고정 partition 결과](../evidence/0003-0007/originals/SRC-0023588.json)

| 자체 손실표 | following-week MAE |
|---|---:|
| tabicl_risk | 0.085256860 |
| empirical_risk | 0.086252123 |
| knn_risk | 0.090493438 |
| median_only | 0.084888323 |
| median_iqr | 0.084712164 |

06은 각120쌍×5대안의 공유 보정에 따른 손해를 저장값으로 확인했다. Tab의 추정 손해와 다음 주 실제 손해의 Spearman은−0.0969571, 실제 손해 양수는53/120, 평균 실제 합산 MAE 증가량은+0.000431453이었다. 경험적 정답−0.1698269, KNN−0.5045315, median−0.1935069, median/IQR−0.0314839도 함께 남긴다. 각 쌍은 cell을 공유하므로 독립 표본의 유의성으로 해석하지 않는다. 순위가 좋지 않았다는 관측만으로 특정 원인을 확정하지 않는다. [600쌍 진단 요약](../evidence/0003-0007/originals/SRC-0023583.json), [모든 쌍의 저장 값](../evidence/0003-0007/originals/SRC-0023584.json)

다음 표는 고정 소속에서 학습한 RCTL의 전체480시점 mean-scaled MAE다. 동일 cell·시점 수이므로 전체 평균과 cell별 MAE의 균등 평균이 같다. [RCTL 원 결과](../evidence/0003-0007/originals/SRC-0030280.json)

| 소속 기준 | seed20260925 | seed20260926 |
|---|---:|---:|
| Tab 전체 분위수 risk | 0.08732813 | 0.08776006 |
| 관측 query target risk | 0.08160040 | 0.08351629 |
| KNN 조건부 분포 risk | 0.08407308 | 미실행 |
| PCC balanced | 0.08987710 | 미실행 |
| random balanced | 0.08559771 | 미실행 |
| global (K1, 보조) | 0.07106777 | 미실행 |

Tab의 오차는 empirical보다 각각 **7.02%, 5.08% 컸다.** 첫 seed의 PCC 대비−2.84%만 취하면 더 강한 단순 대안과의 비교를 누락한다. 두 seed는 같은 도시·cell·기간의 반복으로서 독립 데이터셋 두 개가 아니다. global은 K가 다르지만 이 자료에서 분할이 반드시 필요하다는 전제도 지지하지 않는다. 이를 사후에 비용·모델 수 목표의 성공으로 바꾸지 않는다.

Tab−empirical의48시간 paired block 재표집95% percentile 범위는 두 seed에서 각각[0.001864,0.009725], [0.000188,0.008806]이다. 96시간도 양수 방향이며 PCC와의 차이는 두 길이 모두0을 포함한다. 10개48시간 블록 또는5개96시간 블록을 모든16cell 함께10,000번 재표집한 기술적 변동 확인이다. 보편적인 유의성·독립 미래 성능 보장이 아니다. 검산은 저장 예측으로 같은 순서와 seed20260925의 재표집을 확인했으며 모델을 다시 학습하지 않았다.

## 평균 밖의 반례와 평가 척도

아래는 **정리 과정의 추가 산술**이다. 같은 저장 예측을 float64로 집계해 empirical 대비 Tab 오차의 전후240시점과 cell별 방향을 확인했다. 양수는 Tab 악화다. 이는 새 실험·새 독립 기간이 아니다. [계산 결과](../verification/history-001-risk-check.json)

| seed | 구간 | 정규화 상대 변화 | 악화/개선 cell 수 |
|---|---|---:|---:|
| 20260925 | first240 | +4.4750% | 10/6 |
| 20260925 | last240 | +8.9985% | 10/6 |
| 20260925 | all480 | +7.0193% | 10/6 |
| 20260926 | first240 | +0.3921% | 7/9 |
| 20260926 | last240 | +8.7699% | 9/7 |
| 20260926 | all480 | +5.0814% | 9/7 |

전체 기간에서 seed20260925는6cell(3753,4537,4553,4565,5345,6137), seed20260926은7cell(3737,3745,4537,4553,4565,5337,6137)에서 Tab이 개선됐다. 평균 악화가 모든 cell의 악화는 아니다. 전후반의 cell 방향이 바뀌기도 하므로 전체 평균을 cell 보장으로 읽지 않는다.

원척도 전체 MAE도 추가 집계했다. Tab/empirical은 첫 seed100.612456/98.104617, 두 번째104.010291/97.264866이다. 이 값은 각 cell의 원래 활동 규모를 반영하므로 주 지표인 mean-scaled MAE와 다른 척도다. 원 결과에는 peak 및 전체 cell별 값도 보존돼 있고 검산했으며, 여기서 그 모두의 개선을 주장하지 않는다.

## 실제 비용과 당시 판단

B2는 새 Tab context16개/query2688행, 호출 로그 fit4.877237초+predict26.6554663초다. stage timer 34.125933500초는 선행 공통 scaler/KMeans/Ridge 구성 전부터 잰 시간이 아니다. smoke와 B1까지 당시 누적36context/20,352query이며 상한80/60,000을 실제 소비량으로 쓰지 않는다. [호출 로그](../evidence/0003-0007/originals/SRC-0023586.json)

RCTL은29/29fit,1565epoch, wall1658.1391634초, 개별 fit 시간 합1652.1772001초다. 모든 fit은validation patience로 끝나80epoch 상한에 닿지 않았다. 모든 최적화 경로의 수렴을 증명한 것은 아니다. fit 종료 시 측정한 RSS의 최대467,939,328bytes는 연속 peak나 process-tree 전체 메모리가 아니다. 과거 상한29fit/2320epoch/3000초/20GiB와 실제 소비를 구분한다. [종료 기록](../evidence/0003-0007/originals/SRC-0030278.json), [29fit 기록](../evidence/0003-0007/originals/SRC-0030237.json)

06의 누적합 손실표는 저장 직접 계산과 최대9.44e−16 차이였다. 속도0.0295732초/진단 전체0.1837626초는 RCTL 동시 실행의 CPU 경합 가능성이 기록된 값이다. 10,000cell에서 약328.47분이라는 추론 시간은 기존 호출 시간을 선형 확대한 추정이며 특징·graph·병합·RCTL을 제외한다. 구현하지 않은 대규모 시스템의 측정 성능으로 쓰지 않는다. 06 자체의 새 모델 호출은0이다.

07은 B2 추천을 기각하고, 제한된 함수군·조건부 분포 추정 오차·유한 자료 pooling 효과·기간 변화 중 어느 원인인지 미확정으로 남겼다. 이후 [08·09의 유한표본·문헌 경로](0008-0009-finite-sample-pooling.md)는 별도 묶음에서 근거를 대조했다. B2 결과만으로 해당 후속 주장이나 전체 연구의 완료를 확정하지 않는다.

## 재사용과 재검토 기준

고정 소속,5손실표,원분위수,전체29group 예측·학습 이력,평가 target·scale,paired 결과를 재사용할 수 있다. 당장 같은29학습을 반복해야 숫자를 확인할 구조가 아니다. 모델 `.pt`와 전체 라이브러리는 게시·로드하지 않았고, Tab/KNN/Ridge/KMeans/RCTL 재실행은 미확인이다. 저장 bin·기준 예측·예측 분포 자체의 모델 재현을 손실표 산술 검수와 구분한다.

재검토하려면 이미 labels가 있는 상황에서 empirical보다 분포 추정이 유용할 새 조건, 더 적합한 공유 함수군, 유한 표본 효과나 다른 도시·독립 기간 등을 명시해야 한다. 단순 PCC 대비 한 번의 이득, surrogate 순위, 이미 본20일을 다시 독립 검증으로 부르는 방식은 새 근거가 아니다. action의 정답 접근 범위와 두 번째 seed 대상 변경도 조건표에 남겨야 한다.

[원문·실제 열람 범위](../sources/history-001.md), [검수](../verification/history-001.md), [근거와 실행 방법](../evidence/0003-0007/README.md). [과거 시도 색인](../prior-attempts.md).


후속 [23·25 조건부 공유 비용](0023-0025-conditional-pooling.md)은 기존B1 분포와 고정 소속을 재사용했다. 직접 혼합 예측의 이득과 RCTL 소속 선택의 근거를 구분하고, 유한표본 반례·수치 실패·비용 한계를 연결했다. 새 Tab 추론이나 RCTL fit은0회다.
