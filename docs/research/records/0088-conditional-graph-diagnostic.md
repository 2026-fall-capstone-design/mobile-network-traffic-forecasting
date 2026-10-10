# 원80: 조건부 평균 graph와 고정 RCTL gradient 진단

[출처](../sources/history-088.md) · [검수](../verification/history-088.md) · [저장 근거](../evidence/0088-conditional-graph/README.md) · [원79 후보 논리](0076-0079-learning-decisions.md)

**결론:** 원80은 Tab 예측의 평균 오차 이득을 확인했지만, 고정한 다섯 transport 방법의 소속이 같고 PCC 대비 gradient 이득도 일관되지 않아 후보를 추천하지 않았다. 아래는2026-09-26의 저장 기록을 정리한 것이며 새 실험 결과가 아니다.

## 검토 범위와 관측

<a id="c01"></a>**C01.** 원래 기록 번호 80의 계획·결과·기호 설명 3개, 진단·원장기록 코드 2개, JSON9개, NPZ2개를 연결했다. 16그룹의 동일 SHA 사본 55경로를 확인했다. budget_before는 H070의 budget_after와 같은 내용이므로 새 전체 JSON으로 중복 가산하지 않는다. 본문 5·새 전체JSON8·선택NPZ2가 이번 신규 검토 단위이며 새 모델 실행은 0이다.

<a id="c02"></a>**C02.** 원 80은 관측 입력과 추정 조건부 평균의 쌍 분포로 cluster를 정하면 분산 학습의 local MSE gradient 불일치를 줄일 수 있는지 검토했다. 실제 저장 결과에서 input-only, raw(x,y), TabICL, Ridge, HGB의 소속은 모두 같았고 후보를 추천하지 않았다. 분산 FedAvg 학습은 가정한 적용 방향이며 당시 실행한 학습 결과가 아니다.

<a id="c03"></a>**C03.** 다섯 transport 방법의 K4 소속은 아래 표와 같고 ARI는 1이다. 거리 행렬 자체가 같다는 뜻은 아니다. 각 방법의 저장 거리는 다르지만 동일한 두 차례 병합을 거쳐 같은 소속이 됐다. raw/PCC/probe/random/global은 역할이 다른 비교군으로 남긴다.

| cluster | 공통 cell 소속 |
|---|---|
| 1 | 3737, 4565, 5345, 6153 |
| 2 | 3745, 4537, 5353, 5365 |
| 3 | 3753, 3765, 4545, 4553 |
| 4 | 5337, 6137, 6145, 6165 |

<a id="c04"></a>**C04.** query672–839의 16cell×168행에서 TabICL의 MSE/MAE는 0.013043476419677038/0.07744037281233995, Ridge는 0.015839025414009555/0.09001100792846682, HGB는 0.015861665916631507/0.0877404633878408이다. 기존 평균정규화 단위의 pooled 오차이며, 참 조건부 평균의 오차·최종 RCTL 성능·독립 test 성능과 구분한다.

<a id="c05"></a>**C05.** TabICL의 cell MSE는 HGB보다 16cell 모두 작고 Ridge보다 15cell에서 작다. 예외인 6153에서는 Tab0.030753034736637846, Ridge0.02469025153199379로 Tab이 더 크다. 전체 평균 우위를 모든 cell의 개선으로 바꾸지 않는다. cell MAE는 별도 저장 요약에 없으며 여기서 동일한 우위를 추정하지 않는다.

## 자료·방법·정보 접근

<a id="c06"></a>**C06.** context는 target index168–671의 504개, 소속 계산 query는 672–839의 168개, gradient 사후 확인은 840–1007의 168개다. 세 구간은 이전에 사용한 개발 구간이며 새 독립 test가 아니다. 16cell 전체를 사용했고 이 단계에서 cell을 추가하거나 성능에 따라 제외하지 않았다.

<a id="c07"></a>**C07.** 입력 16열은 최근 8개 값,24h·168h lag,24h 평균·표준편차, 시간·요일 sin/cos다. 기존 cell별 scale을 유지하며 cell ID나 이웃 정보를 새 특성으로 넣지 않는다. RCTL에는 같은 정보를 8×9 배열로 넣어 최근 8개를 첫 채널로, 나머지 8개 특성을 각 step에 반복한다.

<a id="c08"></a>**C08.** Tab 값은 기존 predicted_quantiles(16,168,129)의 마지막 축 평균이다. 저장된 129개 중간분위수의 근삿값이며 정확한 999분위수 평균 API 호출이 아니다. 원 80의 새 Tab context/query는 0이고 당시 생성된 16context 결과를 재사용했다. 이 정리에서도 추론하지 않았다.

<a id="c09"></a>**C09.** Ridge는 StandardScaler와 alpha1, HGB는 squared_error·100회·15leaf·min_samples_leaf20·l2=1·early_stoppingFalse·seed20260925다. 각 cell의 동일 context504개로 각각 16개씩 총 32개를 적합한 기록이다. 이 fit은 당시 수행한 단순 회귀이며 새 RCTL fit이나 이번 아카이브 작업의 실행 수가 아니다.

<a id="c10"></a>**C10.** 공통 scaler는 16cell의 context 입력 전체에만 적합했다. query의 16표준화 입력을 4로 나누고 mean-normalized output 한 열을 가중치 1로 붙였다. 저장 scaler의 평균·표준편차를 입력 배열에 대조했다. output weight1은 사전 고정 pilot 값이며 최적값이나 이론의 Lipschitz 상수를 뜻하지 않는다.

<a id="c11"></a>**C11.** 각 cell 자신의 관측 query168개에 균등 질량을 주고, cell 쌍마다 제곱 Euclidean 비용의 최적 1대 1 매칭 평균 W2²를 계산했다.16cell의 120쌍×5방법으로 600개의 매칭 문제다. 동일 시각을 동일 입력으로 간주하지 않으며 전쌍 계산을 선형 확장성의 근거로 쓰지 않는다. 이번에는 저장 거리를 검사했고 매칭 최적화 자체를 다시 실행하지 않았다.

<a id="c12"></a>**C12.** 각 거리에서 16→8→4로 두 차례 병합하며 평균 cross-cell 거리가 작은 edge부터 겹치지 않게 선택한다. 동점은 작은 cell 인덱스 순으로 처리하며 저장 cell ID는 정렬돼 있다. 저장 거리에서 이 병합을 작은 수치 확인으로 다시 계산해 6방법의 소속과 일치함을 확인했다. PCC는 기존 balanced 소속, random은 seed20260925의 균형 소속, global은 K1이다.

<a id="c13"></a>**C13.** untrained probe는 128개 Gaussian 방향·bias와 1+ReLU(zW+b)/4 예측을 사용한다. 이 식의 z는 코드의 tx에 해당하는 공통 scaler로 표준화한 context 입력이다. 코드에서 별도로 z라 이름 붙인 transport query 입력/4와 구분한다. 각 cell의 128차원 context MSE 벡터를 cell 안에서 중심화해 공통 y² 항을 없앤다. actual input-target 관계를 쓰는 강한 비교군이며 CLoVE 재현으로 등록하지 않는다.

<a id="c14"></a>**C14.** raw-joint는 query의 실제 y를 사용하고 Tab/Ridge/HGB mean은 context y와 query x를 사용한다. 같은 query 수와 입력을 비교해도 target 정보를 얻는 방식까지 같지는 않다. probe 역시 context actual y를 쓰므로 무라벨 기준이라고 부르지 않는다.

## 소속 고정과 gradient 확인

<a id="c15"></a>**C15.** 소속·거리·scaler·output weight를 담은 freeze JSON의 SHA는 c58909a0591ffb5882ade1960e86ab7f7f457ab52d22c94f69aedc94ca1454fa다. 코드에서는 RCTL class import와 checkpoint 파일 해시 읽기가 freeze보다 먼저이고 모델 생성·gradient 계산은 이후다. 따라서 계획의 “저장한 후에만 RCTL을 읽는다”는 문구는 문자 그대로의 모든 파일 접근이 아니라 grouping에 RCTL 결과를 쓰지 않는다는 범위로 해석해야 한다.

<a id="c16"></a>**C16.** 확인한 상태는 seed20260925의 초기 RCTL과 기존 global MAE checkpoint다. 기존 checkpoint는 MAE 학습·validation으로 선택된 상태이므로 MSE 최적점이라고 부르지 않는다. 두 상태 모두 같은 실제 y의 MSE gradient를 계산했으며 clustered RCTL을 새로 학습한 결과가 아니다.

<a id="c17"></a>**C17.** 진단 코드는 eval 모드에서 autograd.grad를 호출하고 optimizer를 만들지 않는다. state_dict의 이름과 tensor bytes 해시를 각 상태의 계산 전후에 비교하는 assert가 있으며 결과에 두 해시와 weights_or_buffers_updated=false가 남아 있다. 이는 정적 코드·저장 결과의 일치이고 이번 작업에서 parameter·BN buffer 불변을 독립 실행으로 재현한 것은 아니다.

<a id="c18"></a>**C18.** 당시 기록은 2상태×16cell×7일의 224 forward/backward batch, 하루 24개씩 총 5376행이다. 마지막 progress에는 stored_global_MAE·day6(0부터 센 마지막 날)·224batch·5376행이 남고 finished/result/cost와 맞는다. 코드와 완료 파일은 이 실행 주장을 뒷받침하지만 원 프로세스의 exit0 자체는 결과 메모의 진술로 남긴다.

<a id="c19"></a>**C19.** 앞 3일 72h·뒤 4일 96h·전체 7일·각 하루의 10기간을 두 상태에서 기록했다. 기간별로 cell의 gradient 벡터를 먼저 평균한 뒤 Gram을 만들며, 일별 분산의 단순 평균이 아니다.84h/84h 분할도 아니다. NPZ에는 20개 16×16 Gram과 두 7×16 MSE 배열이 있고 원 gradient 벡터 자체는 이 두 NPZ에 보존돼 있지 않다.

<a id="c20"></a>**C20.** 지표는 (1/16)Σcell ||g_i−cluster 평균g||²이고 각 상태·기간의 global K1 분산으로 나눈 비율을 비교한다. K를 늘리면 cluster내 분산이 global 분산 이하가 되는 것은 분산분해의 성질이다. 따라서 비율이 1보다 작다는 사실만으로 clustering의 학습 실익을 확정하지 않고 같은 K4·4cell 비교군을 기준으로 판단한다.

## 기간·상태별 결과

<a id="c21"></a>**C21.** 전체 7일의 동일 5방법/PCC/probe/random 비율은 초기 상태에서 0.457014/0.411922/0.490738/0.742499, 저장 MAE 상태에서 0.743252/0.701094/0.634318/0.749987이다. Tab 소속은 두 상태 모두 PCC보다 불일치가 크다. probe와의 비교 방향은 초기에서 Tab이 작고 저장 상태에서는 Tab이 큰 것으로 바뀐다.

<a id="c22"></a>**C22.** Tab−PCC 비율 차이는 초기 상태에서 앞 3일−0.2262343578/뒤 4일+0.1401928731, 저장 상태에서−0.0326553512/+0.0214778281이다. 두 상태 모두 앞 기간에서 좋고 뒤 기간에서 나빠진다. 유리한 앞 기간만 골라 성공으로 표시하거나 전체 7일 값을 일별 비율 평균으로 대체하지 않는다.

| 모델 상태·기간 | 동일5방법 | PCC | probe | random |
|---|---:|---:|---:|---:|
| initial · first3days | 0.292605 | 0.518839 | 0.261788 | 0.855718 |
| initial · last4days | 0.598255 | 0.458062 | 0.643794 | 0.659244 |
| initial · all7days | 0.457014 | 0.411922 | 0.490738 | 0.742499 |
| stored_global_MAE · first3days | 0.807160 | 0.839816 | 0.821688 | 0.798471 |
| stored_global_MAE · last4days | 0.637727 | 0.616249 | 0.546752 | 0.649057 |
| stored_global_MAE · all7days | 0.743252 | 0.701094 | 0.634318 | 0.749987 |

<a id="c23"></a>**C23.** 일별 결과도 전부 보존했다. 초기 상태는 day6·day7에서 Tab 소속이 random보다 나쁘고, 저장 상태는 day2·day3·day5·day7에서 나쁘다. 반대로 저장 상태 day6의 Tab−PCC는−0.4173372486으로 크게 작다. 이런 날짜별 변화가 있으므로 어느 비교군에도 모든 날짜의 일관된 우위를 주장하지 않는다.

<a id="c24"></a>**C24.** 전체 7일 global gradient 분산은 초기 148.128864700961, 저장 MAE 상태 0.06974793403595458로 척도가 다르다. raw 분산을 두 상태에 걸쳐 평균해 통합 성능으로 쓰지 않는다. 저장 MSE_initial/MSE_stored_global_MAE는 같은 고정 모델의 일별·cell별 loss이며 소속별로 새로 학습한 모델의 최종 예측 오차가 아니다.

## 논리와 적용 한계

<a id="c25"></a>**C25.** 고정 scalar fθ와 유한 2차 moment, 미분·기대값 교환 조건에서 제곱손실의 population gradient는 E[2(fθ(X)−m_i(X))∇fθ(X)]로 쓸 수 있다. 조건부 mean-zero 잡음은 이 기대식에서 없어져도 유한 표본 gradient의 분산에는 남는다. 학습 경로나 여러 local step의 동등성을 뜻하지 않는다.

<a id="c26"></a>**C26.** ν_i=(X,m_i(X))의 분포이고 Gθ(x,m)=2(fθ(x)−m)∇fθ(x)가 현재 좌표계에서 Lθ-Lipschitz이면 ||g_i−g_j||≤LθW1≤LθW2라는 coupling 상계를 사용한다. Lθ는 측정하지 않았고 새로운 정리·거리 순위 일치·양방향 보장이 아니다. 실제 계산한 W2²를 이 부등식의 W2와 혼동하지 않는다.

<a id="c27"></a>**C27.** ||∇fθ||≤Bθ일 때 추정 mean 사용의 gradient 차이는 2BθE|m̂−m|로 제한된다. 관측 y에 대한 예측 MSE에는 잡음도 포함되므로 원 80의 작은 예측 오차만으로 참 mean 오차나 이 상계 상수가 작다고 입증하지 않는다.

<a id="c28"></a>**C28.** x가 ±1에 같은 확률을 가질 때 y=3+x와 y=3+x+조건부 mean-zero 잡음은 fθ=3+θx의 기대 gradient가 모두 2(θ−1)이다. y=3−x는 입력분포와 평균 output 주변분포가 같아도 gradient가 2(θ+1)로 4 차이 난다. 입력분포가 다른 추가 예에서는 같은 m이라도 E[X²]가 다르면 2(θ−1)E[X²]가 달라질 수 있다. 이 예시들은 joint 정보의 논리적 필요성을 보여주지만 해당 상황이 실제 16cell clustering 손해를 만들었다는 증거는 확보하지 못했다.

<a id="c29"></a>**C29.** MAE gradient는 conditional CDF에 의존하므로 MSE의 mean 등식을 그대로 옮기지 않는다. frozen eval은 training-mode BN·dropout·Adam·여러 local epoch·FedAvg 수렴을 검증하지 않는다. 분산 환경은 후보의 적용 가정이며 사용자 데이터의 확인된 운영 요건이 아니었다.

## 비용·검수·재사용

<a id="c30"></a>**C30.** 당시 새 Tab context/query0, RCTL fit/optimizer step0, 단순 회귀 32fit·1.4865054000초다. 다섯 방법에 걸친 600개 매칭 약 0.884초를 포함한 cheap2.4464091000초와 frozen gradient4.5957178000초를 합해 측정 단계 7.0421269000초다. peak RSS 기록은 572198912바이트다. 단순 회귀 시간과 transport 시간을 cheap에 다시 더해 중복 합산하지 않는다.

<a id="c31"></a>**C31.** 타이머는 import와 초기 해시·settings 저장 뒤 시작하고 teacher 지표·ARI·최종 결과 저장 전에 total을 확정한다. gradient 구간에는 gradient 외 기간 요약·상태 검사·gc도 포함된다. 마지막 progress의 4.398327초와 최종 4.595718초는 측정 지점이 다르다. RSS는 check() 호출 시 관측한 최대치이며 연속 감시한 전 프로세스 최대나 완전한 end-to-end 시간으로 쓰지 않는다.

<a id="c32"></a>**C32.** 실행 전후 원장과 recorder 코드를 대조했다. caps·remaining·기존 used 항목은 같고 reset0이다. cheap는 66.7446051000→69.1910142000초, frozen gradient4.5957178000초가 새 항목으로 더해져 기록된 modeling 합계 1992.6150618000초다. Tab69/80context·39360/60000행과 RCTL29/29fit은 변하지 않았다. 초기 전처리 일부 미측정이 남아 있으며 이 과거 예산을 현재 Goal의 예산으로 적용하지 않는다.

<a id="c33"></a>**C33.** pre_RCTL_arrays의 22필드는 final arrays의동명 22필드와 모두 같다. final44필드와 pre22필드의 shape·dtype·유한성을 검사하고, teacher 오차·ARI·소속·20Gram의 180 within 분산·180비율·180차이를 저장 결과에 대조했다. 분산 최대 절대 차이는 3.87×10⁻¹²다. 저장 Gram의 대수 확인이며 원 backward와 gradient 생성·시간순서의 독립 실행 검증이 아니다.

<a id="c34"></a>**C34.** settings의 8개 source hash를 원본 또는 당시 budget_before에 대조했고 freeze/settings hash와 시작·진행·완료·결과 파일을 연결했다. 입력 data·Tab 출력·기존 PCC·RCTL 코드·checkpoint는 역할을 나눠 기록했다. checkpoint는 bytes 해시만 확인했으며 역직렬화하지 않았다. 원문 메모와 코드는 보존 사본이며 지금 수행할 지시가 아니다.

<a id="c35"></a>**C35.** 현재 weighting·K4·같은 개발 구간에서 Tab의 더 좋은 직접 예측이 새 소속이나 일관된 gradient 이득으로 이어지지 않았다는 부정 결과다. 모든 conditional-mean 방법의 실패를 뜻하지 않는다. 재진입하려면 단순 입력 clustering이 다른 예측 관계를 잘못 묶어 실제 손해를 만드는 사례와 이전 조건에서 무엇이 달라지는지를 먼저 제시해야 한다. 같은 자료를 보고 weight/K만 조정한 결과를 새 검증으로 제시하지 않는다.

<a id="c36"></a>**C36.** 원 80의 literature_search_leads.json과 파생 pyc는 이번 16그룹에 포함하지 않고 다음 검토에 남긴다. 원 81–642와 이전 부분 기록, 실패·비용의 전체 통합, 장기 팀 원자료 접근, 최종 원본 변경과 대표 질문 검색 검수도 미완료다. 이 한 후보의 보류와 아카이브 전수 완료를 구분한다.

## 재사용 전에

[원80 전체 결과](../evidence/0088-conditional-graph/originals/SRC-0025157.json)와 [수치 대조](../evidence/0088-conditional-graph/numeric-audit.json)에서 일별·cell별 반례를 함께 확인한다. [계획](../evidence/0088-conditional-graph/originals/SRC-0022038.md.txt)의 비교 조건을 새 실험 양식에 연결하고, 새로운 자료·분할·가설·평가 기준의 차이를 적는다. 소속 결정에 RCTL 결과를 되먹임했는지와 실제 분산 운영 필요가 있는지도 별도로 기록한다.
