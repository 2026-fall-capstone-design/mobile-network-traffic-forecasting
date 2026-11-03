# 원102 — 구조 기반 kernel과 공동 target 위험의 적용 범위

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

**원102는 현재 추천안에 RNN kernel 점수를 더하지 않기로 한 근거 검토다.** 구조 기반 계산의 가능성은 남겼지만, 초기화의 무한폭 이론·참고 구현을 실제 유한 RCTL의 Adam·MAE 학습 결과에 연결할 근거가 부족했다. 새 kernel 성능을 측정해 실패한 기록은 아니다.

[35출처/81사본](../sources/history-132.md) · [36주장](../verification/history-132-claims.json) · [작성 후 대조](../verification/history-132-second-pass.json) · [수식 검수](../evidence/0132-architecture-kernel-and-joint-risk/fixed-affine-identity-check.json) · [비용 산술](../evidence/0132-architecture-kernel-and-joint-risk/cost-arithmetic-check.json) · [문헌·재사용 조건](../references/architecture-kernel-and-joint-risk.md)

## 질문과 실제 수행

2026-09-26 [원101](0131-actual-pooled-context-and-rctl-ranking.md)의 실제 pooled Tab context는 직접 예측이 좋았지만 두 K4 소속의 평균 순위가 저장 RCTL과 달랐다. 원102는 학습 없이 구조를 반영한 점수가 그 연결을 보완할 수 있는지 논문·정적 코드·기호 전개로 살폈다. 좋은 직접 예측 근거와 소속 대리점수의 한계를 함께 남긴다.

당시 확보 PDF2편86쪽과 실제 관련 본문·렌더6쪽을 구별했고 공식 코드4파일은 실행하지 않았다. 새 Tab/RCTL/단순 predictor/traffic 실험은0, 잔여 Tab2context/4512query·추가 RCTLfit0과 Word는 그대로였다. 최종 추천안·최종 Word는 미완료였다. 현재 아카이브도 원코드 import/실행·모델 생성·학습·추론·gradient0이다.

## 이론과 실제 학습기의 연결

| 확인한 자료 | 조건과 확인된 역할 | 현재 RCTL에 남는 연결 |
|---|---|---|
| RNTK v4 | simple RNN·Gaussian NTK 초기화·infinite width·linear last readout; PD/학습 regime 조건 | TCN/LSTM/BN·잔차·Xavier/orthogonal·작은 폭의 Adam/MAE와 같지 않음 |
| TP II v4 | formal BP-like/GIA/regularity 조건의 NTK INIT; LSTM/GRU/conv/BN 등 표현 가능 | 일반 NTK TRAIN은 후속 문제; 초기 kernel 존재가 유한 학습 위험을 정하지 않음 |
| 공식 RNN 예제 | finite model gradient simulation과 input Gram 기반 analytic recursion 구분 | LastState/AvgPool 경계·합이 RCTL flatten8×16→scalar와 다름 |
| 공식 BN 예제 | ε0 ReLU MLP·두 batch7/5·CIFAR12·width/seed별 NTK 오차 | 현재 BN ε.001·momentum.01·잔차/LSTM과 다름; analytic covariance 미분에도 autograd 사용 |
| 실제 RCTL pilot | 폭16/32/64/64/32/16·8×9 입력·MAE/Adam·validation best | 이미 보관된 구현을 읽었으며 새 kernel·RCTL 비교는 실행하지 않음 |

TP II는 다른 폭의 유한 양의 비율도 다룬다. 폭이 서로 다르거나 LSTM/BN이 있다는 사실만으로 모든 구조 기반 접근을 기각하지 않는다. BN의 ε>0 Master 조건과 ε0 특수 공식 예제도 구별한다. 논문의 feature/gradient covariance는 아래 target 공동 covariance와 역할이 다르다.

## 개별 예측 분위수만으로 정해지지 않는 위험

입력·설정과 `A,b,W`를 고정하고 `W`가 대칭 PSD이며 target 공동분포에 유한2차적률이 있을 때, `e=A Y_T+b−Y_Q`, `d=A μ_T+b−μ_Q`의 조건부 제곱위험은 다음 기본 항등식이다.

`E[eᵀWe] = dᵀWd + tr{W[AΣ_TT Aᵀ + Σ_QQ − AΣ_TQ − Σ_QT Aᵀ]}`

학습/확인 target 사이 공동 공분산까지 필요하다. 같은 ±1 주변분포라도 동일·반대·독립 결합의 제곱위험은0/4/2일 수 있다. 같은 평균0·분산1의 오차도 MAE1과1/2가 가능하다. 이 작은 유리수 예제와 식의 직접합/전개 차이0은 아카이브 수학 검수이며 실제 traffic 성능이나 새로운 이론이 아니다.

target을 보고 소속/규제값/A를 고른 선택을 생략하지 않는다. 적절히 조건화하면 원 항등식은 유효하다. lag 행렬을 고정한 독립 target 재추출은 원 시계열의 공동 관계를 바꿀 수 있지만, 무조건 긴 context/query 공백을 새로 요구한다는 뜻도 아니다. 실제 traffic의 공동 Gaussian 가정은 확인하지 않았다.

## 비용 산술의 한계

| 가정한 저장 대상 | global N=10752 | 균등 K4, 각 N=2688 |
|---|---:|---:|
| float64 dense kernel 한 행렬씩 | 924,844,032bytes /882MiB | 합231,211,008bytes /220.5MiB |
| RNN routine의 N×N×T×T 한 버퍼씩, T8·float64 가정 | 59,190,018,048bytes /55.125GiB | 합14,797,504,512bytes /13.78125GiB |

첫 행은 원문 두 정수값의 검산이고 둘째 행은 보관 code shape에 조건을 명시한 추가 산술이다. 어느 버퍼도 할당하지 않았고 kernel entry·peak memory·factorization·runtime을 측정하지 않았다. naive dense 저장 O(n²)/직접 solve O(n³)를 특수·근사·반복 solver를 포함한 모든 구현의 하한으로 쓰지 않는다.

## 문헌·판독·미완료 범위

현재 보관 RNTK26쪽/TP II60쪽은 전체 텍스트8069행·전체 이미지86개를 읽었다. 논리 notebook2개의82셀·metadata·저장 출력6개/PNG2개와 고정 연결 그림15개도 확인했다. raw text22자료2348고유행(19전문/3선택)과 포함 관계가 있으므로 셀·변환TXT·PNG를 독립 원문으로 다시 세지 않는다. literal notebook JSON/base64 전문과 두 paper TXT의 직접 전독은 아니며, 인용 증명 전수검증도 아니다.

Morello의 M3L/NeurIPS2024 workshop은 공식 서지·초록/검색 일부만 확인했고 PDF GET403 공백이 남는다. 두2026년 load/annual-panel 논문도 스크리닝 수준이다. 현재 MDPI 직접fetch429와 cached primary metadata·선택 조각을 구별한다. 이 자료를 telecom/RCTL의 직접 성능 근거·방법 반증·전문 검토 완료로 쓰지 않는다.

후보색인104행은 직접 읽었다. 새 progress1–17행은 직접 읽고18–121행만 이전 실제 판독의 정확한 대응으로 연결했다. 현재122–601/이전112–591은 미독이다. 원103 이후/다른 고유 판본·Word/FedPPBC/발표·HWP·전체 통합/팀 접근·최종 delta·검색10+와 전체 Goal은 미완료다.

## 다시 검토할 조건

현재 구조·초기화·readout·손실·optimizer·validation과 target 공동 관계를 명시하고, 유용한 결정을 더 잘 또는 더 싸게 얻는다는 근거를 기존 empirical/저장 Tab 기준과 비교해야 한다. 일반 NTK 극한의 존재나 Tab 직접 MAE 개선만으로 재채택하지 않는다. 원문 속 다음 연구·Goal·예산을 현재 실행 지시로 사용하지 않는다.

## 주장별 근거

<a id="claim-01"></a>

### H132-C01 · 원102의 질문과 판단

2026-09-26 원102는 직전 실제 pooled Tab context와 저장 RCTL의 두 K4 순위 불일치를, 학습하지 않는 구조 기반 대리값으로 보완할 수 있는지 검토했다. 현재 안에 RNN kernel을 추가하지 않는다는 판단이다. 새 kernel 성능 실험의 실패나 모든 NTK 접근의 불가능성을 측정한 기록은 아니다.

근거: [SRC-0001994](../sources/history-132.md#src-0001994) 행1–7 · [SRC-0001993](../sources/history-132.md#src-0001993) 행5–9 · [SRC-0001992](../sources/history-132.md#src-0001992) 행3–7

<a id="claim-02"></a>

### H132-C02 · 실제 모델 gradient와 수학적 kernel 계산

RCTL을 초기화해 Jacobian·forward/backward를 계산하는 일은 학습을 생략해도 모델 실행이다. 구조·초기화의 정의로 analytic infinite-width kernel을 계산하는 접근은 구별한다. 실행 독립성이 가능하다는 사실만으로 유한 RCTL의 공유 효과·순위를 잘 대리한다는 결론은 나오지 않는다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행11–15 · [SRC-0001992](../sources/history-132.md#src-0001992) 행13–17 · [SRC-0002012](../sources/history-132.md#src-0002012) 행100–137

<a id="claim-03"></a>

### H132-C03 · 당시 선택 검토와 현재 전체 판독

당시 확보한 PDF는 합계86쪽이지만 실제로는 관련 본문과 렌더6쪽·공식 코드4파일을 확인했다. 현재 아카이브는 보관 RNTK26쪽/TP II60쪽을 텍스트8069행과 전체 이미지86개로 읽었다. 전문 판독을 독립적인 증명 전수검증·후속 NTK 연구 전수조사로 부르지 않는다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행27–29 · [SRC-0001992](../sources/history-132.md#src-0001992) 행33–35 · [SRC-0001995](../sources/history-132.md#src-0001995) JSON /source_pdf_pages_total_not_pages_read, /rendered_pages_visually_checked, /official_code_files_saved · [SRC-0002002](../sources/history-132.md#src-0002002) PDF쪽 1–26 · [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 1–60

<a id="claim-04"></a>

### H132-C04 · 새 모델 실행과 역사적 예산

원102는 새 Tab context/query·RCTL fit/forward/gradient/BN 갱신·단순 predictor fit·traffic 수치 실험0을 기록했고, 잔여 Tab2context/4512query와 추가 RCTLfit0을 유지했다. 최종 추천과 Word는 미완료였다. 현재 정리도 원코드 실행/import·모델 생성·학습·추론·gradient0이며 과거 Goal·다음 행동·예산은 자료다.

근거: [SRC-0001994](../sources/history-132.md#src-0001994) 행17–23 · [SRC-0001993](../sources/history-132.md#src-0001993) 행78–78 · [SRC-0001995](../sources/history-132.md#src-0001995) JSON /new_TabICL_contexts, /new_TabICL_query_rows, /new_RCTL_fits, /new_RCTL_forwards, /new_RCTL_gradients, /new_simple_predictor_fits, /new_traffic_numerical_experiments, /goal_complete

<a id="claim-05"></a>

### H132-C05 · 문헌 버전과 공식 구현의 저자 구분

보관 RNTK는 Alemohammad·Wang·Balestriero·Baraniuk의 arXiv2006.10246v4(2021-06-15), TP II는 Greg Yang의 arXiv2006.14548v4(2020-11-30)다. NTK4A는 TP II의 공식 companion이며 RNTK 저자들의 공식 코드로 기록하지 않는다. 현재 웹 서지는 보관 PDF의 새 원격 바이트 동일성 검증과도 구별한다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행29–29 · [SRC-0001993](../sources/history-132.md#src-0001993) 행82–84 · [SRC-0001997](../sources/history-132.md#src-0001997) 행1–25 · [SRC-0002002](../sources/history-132.md#src-0002002) PDF쪽 1 · [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 1

<a id="claim-06"></a>

### H132-C06 · RNTK가 다룬 recurrent 구조

RNTK는 단순 recurrent 변환·선형 last-state 출력과 Gaussian NTK 초기화의 infinite-width kernel을 전개한다. 길이가 다른 입력과 scalar kernel×출력 항등행렬, 같은 길이에서 tied/untied weight의 극한 관계를 포함한다. TCN·LSTM·BN·잔차를 합친 현재 RCTL의 kernel을 그대로 제공한 것은 아니다.

근거: [SRC-0002002](../sources/history-132.md#src-0002002) PDF쪽 3,4,6 · [SRC-0001993](../sources/history-132.md#src-0001993) 행21–25

<a id="claim-07"></a>

### H132-C07 · RNTK 초기화·학습 정리와 제곱오차의 조건

RNTK의 kernel 안정성·학습 연결에는 NTK 초기화, 충분한 폭, 초기 kernel의 양의 고유값과 학습 regime/step 조건 등이 붙는다. §2의 제곱오차 선형 ODE·kernel 회귀 연결을 유한 RCTL의 Adam·MAE 최종 예측과 동일시하지 않는다. 본문의 일반 loss 표기와 부록의 조건부 kernel 안정성 진술을 논문 전체가 오직 MSE만 다룬다는 뜻으로 축소하지 않으며, 독립적인 증명 검증도 주장하지 않는다.

근거: [SRC-0002002](../sources/history-132.md#src-0002002) PDF쪽 2,3,5,23,24,25,26 · [SRC-0001993](../sources/history-132.md#src-0001993) 행21–24

<a id="claim-08"></a>

### H132-C08 · RNTK의 실증 범위와 예외

RNTK의 UCR 분류·synthetic/stock next-step 비교는 telecom의 pooling 소속·336시간 평가와 다르다. stock에서는 PTS가 kernel들보다 좋았고 분류도 모든 dataset 승리는 아니다. 부록 P90/P95는 각 dataset의 비교 classifier 최고 관측 정확도의90/95% 이상을 달성하는 dataset의 비율로, Tab 예측 분위수나 신뢰구간이 아니다. 저장 연구를 현재 새 실험으로 세지 않는다.

근거: [SRC-0002002](../sources/history-132.md#src-0002002) PDF쪽 7,8,12,13,14 · [SRC-0001993](../sources/history-132.md#src-0001993) 행82–82

<a id="claim-09"></a>

### H132-C09 · TP II의 일반 구조와 INIT/TRAIN 구분

TP II는 formal tensor program 조건에서 LSTM/GRU·합성곱·skip/residual·BN·pooling 등의 초기 NTK 극한을 다루므로 LSTM이나 BN을 이론상 못 다룬다는 기각은 부정확하다. 본문은 NTK INIT을 일반화하고 일반 구조의 NTK TRAIN은 후속 문제로 구별한다. 표현 가능성과 실제 유한 Adam·MAE 학습 위험의 정확한 대리는 별개다.

근거: [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 1,2,3,10,11,25,26,27,28 · [SRC-0001993](../sources/history-132.md#src-0001993) 행23–25

<a id="claim-10"></a>

### H132-C10 · TP II 가정·폭 비율·증명 검증의 한계

TP II의 BP-like 프로그램, mean-zero independent readout/GIA 조건과 rank 안정성·약미분/성장 조건을 유지한다. deterministic readout averaging 반례는 shortcut의 조건 위반이며 kernel 자체의 부재가 아니다. 변수별 폭의 유한 양의 비율을 허용하므로 RCTL 채널 수가 서로 다르다는 사실만으로 적용 불가를 증명하지 않는다. 60쪽 전문을 읽었지만 인용 증명과 인쇄 기호의 불일치를 모두 독립 해결한 것은 아니다.

근거: [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 6,9,10,11,16,17,18,19,20,21,22,23,24,41,52,60

<a id="claim-11"></a>

### H132-C11 · 현재 RCTL의 구조·초기화·readout

재사용 RCTL은6개 causal Conv/LSTM/residual block, 폭16/32/64/64/32/16, BN eps.001·momentum.01, dropout.05와 flatten8×16→scalar readout을 쓴다. Conv/Linear Xavier uniform, LSTM input Xavier·recurrent orthogonal·forget bias1이다. Gaussian·infinite-width simple RNN의 LastState/AvgPool과 같지 않지만 이 차이 자체가 성능 실패의 증명은 아니다.

근거: [SRC-0023048](../sources/history-132.md#src-0023048) 행11–60 · [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 32,33 · [SRC-0002012](../sources/history-132.md#src-0002012) 행36–98 · [SRC-0001993](../sources/history-132.md#src-0001993) 행24–25

<a id="claim-12"></a>

### H132-C12 · 현재 RCTL 학습 조건과 자료 표현

보관 pilot는 같은16기초값을8lag step마다 나머지8값을 반복하는8×9 입력으로 바꾼다. cell당672학습행(index168–839), validation840–1007, 기존 test1008–1487, 최대80epoch/batch256/patience10/Adam lr.001·eps1e-7·MAE와 validation best를 사용한다. 원101은 test 첫336시점의 rolling 실측 lag 비교였다. 새 kernel/RCTL 비교를 실행하지 않았고 이 기존 코드 재독의 신규 집계는0이다.

근거: [SRC-0023202](../sources/history-132.md#src-0023202) 행17–50 · [SRC-0023202](../sources/history-132.md#src-0023202) 행51–126 · [SRC-0001993](../sources/history-132.md#src-0001993) 행9–9 · [SRC-0001993](../sources/history-132.md#src-0001993) 행22–24 · [SRC-0001996](../sources/history-132.md#src-0001996) 행40–40 · [SRC-0001969](../sources/history-132.md#src-0001969) 행9–12

<a id="claim-13"></a>

### H132-C13 · NTK4A pin과 source-only 변환

NTK4A commit db79a5bd9e75e5a15548306d4770951f94883fb7의 README·utils·RNN/BN notebook4개는 Git blob/크기/SHA와 보관 바이트가 일치한다. README는 선택한 advanced architecture의 구현이며 모든 구조를 구현하지 않는다. 당시 notebook TXT는 모든 cell의 source만 이어 붙여 저장 출력·metadata를 생략했다. 현재 논리 내용 판독은 그 누락을 따로 확인했다.

근거: [SRC-0002013](../sources/history-132.md#src-0002013) 행1–30 · [SRC-0002010](../sources/history-132.md#src-0002010) 행1–30 · [SRC-0002000](../sources/history-132.md#src-0002000) 행1–42

<a id="claim-14"></a>

### H132-C14 · RNN simulation·analytic·출력 방식

SimpleRNNClassifier/simrnn_ntk는 finite Gaussian model을 만들고 forward/backward 후 parameter gradient 내적을 계산한다. rnnntk_batch는 input Gram에서 activation·backward covariance를 전개하는 analytic 경로다. LastState와 AvgPool의 NTK 합·경계조건이 달라 현재 RCTL flatten readout에 그대로 대입할 수 없다. 함수 읽기만 했고 어떤 경로도 실행하지 않았다.

근거: [SRC-0002012](../sources/history-132.md#src-0002012) 행36–137 · [SRC-0002012](../sources/history-132.md#src-0002012) 행169–252 · [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 32,33

<a id="claim-15"></a>

### H132-C15 · RNN 예제의 입력·seed·측정량

RNN 저장 예제는 CIFAR10 첫2이미지의 첫5pixel×3channel을 sequence로 사용하고 erf·varw1/varu2/varb.2/varv1·avgpool True·width64–8192·100seed를 비교한다. 다른 길이용 rnnntk helper도 있지만 해당 예제의 호출은 rnnntk_batch다. 상대 Frobenius NTK 오차는 원101의 traffic MAE·소속 위험이 아니다.

근거: [SRC-0002012](../sources/history-132.md#src-0002012) 행259–333 · [SRC-0002012](../sources/history-132.md#src-0002012) 행337–421 · [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 2

<a id="claim-16"></a>

### H132-C16 · BN 예제의 epsilon·batch·analytic 미분

BN 예제는 Gaussian ReLU MLP/depth1·CIFAR12·projection13차원·두 batch7/5·width64–8192·100seed다. eps0·momentumNone·affineFalse·running stats 없음은 현재 RCTL BN과 다르며, 두 batch를 cell cluster K2로 부르지 않는다. analytic backward는 covariance 변환에 Torch autograd를 사용하고 simNTK의 model gradient와 역할이 다르다. TP II Master의 epsilon>0 조건/epsilon0 각주와 공식 예제 범위를 구별한다.

근거: [SRC-0002009](../sources/history-132.md#src-0002009) 행42–80 · [SRC-0002009](../sources/history-132.md#src-0002009) 행157–237 · [SRC-0002009](../sources/history-132.md#src-0002009) 행393–561 · [SRC-0002009](../sources/history-132.md#src-0002009) 행640–798 · [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 26,36,37,38 · [SRC-0023048](../sources/history-132.md#src-0023048) 행19–25

<a id="claim-17"></a>

### H132-C17 · notebook 저장 출력·시각 자료의 출처

현재 BN48/RNN34셀의 source·metadata·저장 출력6개/PNG2개를 모두 읽었고 고정 공식 연결 그림15개도 전체 확인했다. 이는 literal notebook JSON/base64 전문 읽기나 새2026실행이 아니다. ExecuteTime은2020-06-17, kernelspec Python3.6.6/language_info3.6.10을 함께 보존한다. 저장 진행률·시간·width 오차곡선을 현재 RCTL 비용/MAE로 옮기지 않는다. TP II 2쪽 plot의 band는100seed 평균의95%CI로 명시되어 있다.

근거: [SRC-0002008](../sources/history-132.md#src-0002008) notebook zero-based cell 36,44,46 · [SRC-0002011](../sources/history-132.md#src-0002011) notebook zero-based cell 23,31,32 · [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 2

<a id="claim-18"></a>

### H132-C18 · 공식 Transformer와 전체 RCTL 구현 확보 여부

TP II는 저자가 정의한 Transformer의 projection/attention/LN/readout 조건으로 초기 kernel을 전개한다. 이것을 pretrained TabICLv2 또는 현재 RCTL의 kernel·학습 위험이라고 부르지 않는다. Transformer/GP4A/별도 plot notebook은 이번4파일 수집에 포함되지 않아 전체 코드 판독/실행을 주장하지 않는다. RCTL 전체 analytic kernel 구현은 미확보다.

근거: [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 38,39,40,41 · [SRC-0002010](../sources/history-132.md#src-0002010) 행1–30 · [SRC-0002013](../sources/history-132.md#src-0002013) 행1–30 · [SRC-0001993](../sources/history-132.md#src-0001993) 행25–29

<a id="claim-19"></a>

### H132-C19 · 고정 affine smoother의 조건부 위험 항등식

입력·설정과 A,b,대칭 PSD W를 고정하고 target 공동분포의 유한2차적률이 존재하면 d=AμT+b−μQ에 대해 E[eᵀWe]=dᵀWd+tr W[AΣTTAᵀ+ΣQQ−AΣTQ−ΣQTAᵀ]다. 이는 기본 조건부 제곱오차 항등식이며 새로운 RCTL 성능 보장이 아니다. 아카이브의 작은 유리수 예제에서 직접 합과 식은775997/11025로 같고 차이는0이다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행31–43

<a id="claim-20"></a>

### H132-C20 · target 공동 공분산과 activation covariance

위 식에는 학습/확인 target의 ΣTT·ΣTQ·ΣQQ가 필요하다. input Gram, Gaussian activation moment 또는 gradient covariance를 계산하는 NTK/GP recursion이 그 target 공동 공분산을 자동 제공하지 않는다. 다른 kernel로 A를 바꾸면 다른 learner의 위험이며 RCTL의 소속 순위와 동일하다고 할 수 없다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행35–51 · [SRC-0002014](../sources/history-132.md#src-0002014) 행24–29 · [SRC-0002014](../sources/history-132.md#src-0002014) 행35–64 · [SRC-0002012](../sources/history-132.md#src-0002012) 행169–252 · [SRC-0002004](../sources/history-132.md#src-0002004) PDF쪽 29,30,31,32

<a id="claim-21"></a>

### H132-C21 · 같은 주변 분위수와 다른 공동 위험

개별 sample의 완전한 주변분포/분위수도 다른 시간·cell 사이의 coupling을 정하지 않는다. 검수용 ±1 두 target의 같은 주변분포를 동일·반대·독립으로 결합하면 A=1,b=0,W=1의 제곱위험이 각각0/4/2다. 실제 traffic 결과가 아니라 원문 정보 요구를 확인한 유한 지지집합 예제다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행47–49

<a id="claim-22"></a>

### H132-C22 · 평균·공분산만으로 일반 MAE는 결정되지 않음

제곱위험 식을 일반 MAE 식으로 바꾸지 않는다. 검수용 오차 ±1(각1/2)과0(3/4)·±2(각1/8)는 모두 평균0/분산1이지만 MAE는1과1/2다. 공동 Gaussian처럼 오차분포를 정하는 추가 가정이 있으면 별도 계산은 가능하나 현재 traffic에서 그 가정을 확인한 기록은 아니다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행51–51 · [SRC-0001992](../sources/history-132.md#src-0001992) 행21–23

<a id="claim-23"></a>

### H132-C23 · target 적응 선택과 고정 조건

target을 보고 partition·regularization·A를 고른 과정을 고정 A의 무조건 식에 생략하지 않는다. 검수 예제 A=YT, YT=±1, YQ=0은 실제 제곱위험1이지만 평균 A=0을 대입하면0이다. 선택을 적절히 조건화한 target 적률에는 원 항등식이 여전히 유효하며 선택 적응 자체의 불가능성 정리는 아니다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행35–43

<a id="claim-24"></a>

### H132-C24 · lag 행렬 조건화와 독립 target 생성

X(t+1)에 Y(t)가 lag로 들어 있으면 모든 입력을 고정한 뒤 target을 독립 재추출하는 절차가 원래 공동 시계열을 보존하지 않는다. 검수 예제 Xnext=1을 조건화하면 Yprev=1/조건부분산0인데 무조건 ±1을 추출하면 lag 관계를 지킬 확률은1/2다. 이는 무조건 긴 context/query 공백을 새로 요구하는 주장도 아니다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행53–57

<a id="claim-25"></a>

### H132-C25 · dense kernel 계산량과 대안의 범위

naive dense kernel ridge는 n학습행에 저장 O(n²)·직접 선형계 풀이 O(n³)가 필요하다. 특수·근사·반복 solver나 구조 활용이 존재하므로 이를 모든 kernel 방법의 비용 하한으로 쓰지 않는다. RCTL 학습을 생략한 것과 kernel 점수의 실제 비용·유용성 개선은 별도다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행59–65

<a id="claim-26"></a>

### H132-C26 · 원102의 두 저장량 검산

원101과 같은16×672=10752학습행에서 float64 dense kernel 한 행렬은924844032bytes(882MiB), 균등 네 group(각2688행)의 행렬 합은231211008bytes(220.5MiB)다. 원문의 두 정수값을 검산했으며 allocation·factorization·시점별 중간값·peak memory·실행 시간은 측정하지 않았다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행63–65 · [SRC-0001992](../sources/history-132.md#src-0001992) 행25–25

<a id="claim-27"></a>

### H132-C27 · 공식 RNN 4차원 버퍼의 조건부 산술

rnnntk_batch의 N×N×T×T hcov/hhcov shape에 원101의 N과8step·float64를 가정하면 한 global 버퍼59190018048bytes(55.125GiB), 균등 네 group의 한 버퍼씩 합14797504512bytes(13.78125GiB)다. 아카이브의 추가 shape 산술이며 원102의 kernel 실행 결과·전체 peak·모든 구현의 하한이 아니다. 버퍼를 할당하거나 kernel entry를 계산하지 않았다.

근거: [SRC-0002012](../sources/history-132.md#src-0002012) 행169–192 · [SRC-0001993](../sources/history-132.md#src-0001993) 행63–65 · [SRC-0023202](../sources/history-132.md#src-0023202) 행60–69

<a id="claim-28"></a>

### H132-C28 · 값이 싸다는 주장에 필요한 비교

kernel을 더해 모델 학습을 피했다는 설명만으로 기존 empirical 기준/저장 Tab 결과보다 싸거나 좋은 결정을 얻는다고 하지 않는다. 실제 구조·손실·최적화의 연결과 후보 재계산/중간 배열을 포함한 비용 근거가 필요하다. 원102는 이 근거 없이 새 kernel 실행을 시작하지 않았다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행61–65 · [SRC-0001993](../sources/history-132.md#src-0001993) 행72–76 · [SRC-0001994](../sources/history-132.md#src-0001994) 행19–23

<a id="claim-29"></a>

### H132-C29 · Morello 워크숍의 접근 공백

Morello·Grégoire·Verboven의2024 M3L/NeurIPS workshop task-affinity 연구는 대학 공식 서지·초록/검색 일부만 확인했다. 보관 접근과 현재 일반 PDF GET은403으로 원문 확보에 실패했다. early-training gradient similarity/synthetic task 검토를 현재 RCTL pooling 성능 증거·세부식 전수검증·정확한 방법 반증이나 main-track NeurIPS로 표기하지 않는다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행69–70 · [SRC-0001993](../sources/history-132.md#src-0001993) 행85–85 · [SRC-0001994](../sources/history-132.md#src-0001994) 행11–11

<a id="claim-30"></a>

### H132-C30 · 2026년 두 논문의 스크리닝 수준

2026-08-10 Sustainability18(16)8165 load-heterogeneity 연구와2026-09-18 Forecasting8(5)89(Aras Yolusever) annual compositional pooling 연구는 서지·검색 공개 내용 수준이다. 후자는 Eurostat 연간 composition panel의 parameter sharing 비교로 hourly telecom/RCTL과 다르다. 현재 MDPI 직접 fetch429와 cached primary metadata/선택 조각을 구별하고 두 논문 전문·정리의 직접 성능 검증 완료로 세지 않는다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행70–70 · [SRC-0001993](../sources/history-132.md#src-0001993) 행86–87 · [SRC-0001994](../sources/history-132.md#src-0001994) 행15–15

<a id="claim-31"></a>

### H132-C31 · 직접 예측의 긍정 근거와 소속 대리점수

원101에서 실제 Tab pooled context의 직접 예측 우위는 원102에서도 긍정 근거로 보존했다. 두 K4 순위 불일치 때문에 이를 RCTL clustering 개선으로 승격하지 않았으며 모든 cell/기간·소속의 실패로 일반화하지 않는다. 같은 저장 결과를 색인·보고서가 다시 인용한 것을 독립 재현/새 실험 여러 번으로 세지 않는다.

근거: [SRC-0001992](../sources/history-132.md#src-0001992) 행7–7 · [SRC-0001992](../sources/history-132.md#src-0001992) 행29–35 · [SRC-0001993](../sources/history-132.md#src-0001993) 행9–9 · [SRC-0001993](../sources/history-132.md#src-0001993) 행74–78 · [SRC-0001996](../sources/history-132.md#src-0001996) 행40–40

<a id="claim-32"></a>

### H132-C32 · 색인·progress 개정의 정확한 연결

Snapshot43 후보103행→44 후보104행은 새7행 삽입 외 전행이 정확히 대응한다. progress는 old7행을 new7–17로 대체하고 old8–591=new18–601이다. 현재 candidate104행과 progress1–17은 직접 읽었고 new18–121만 prior old8–111의 실제 판독과 hash-bound 행 동일성으로 연결한다. new122–601/old112–591은 미독이다. 개정 비교만으로 전체 progress 판독을 완료하지 않는다.

근거: [SRC-0001996](../sources/history-132.md#src-0001996) 행1–8 · [SRC-0001999](../sources/history-132.md#src-0001999) 행1–17 · [SRC-0001966](../sources/history-132.md#src-0001966) 행5–8 · [SRC-0001969](../sources/history-132.md#src-0001969) 행1–12 · [SRC-0002001](../sources/history-132.md#src-0002001) 행1–103

<a id="claim-33"></a>

### H132-C33 · 원장·Word 버전 보존

원102 verification의 원장SHA60b589e806c4d1bc8b37d9130e1215d5e15de1d186980ca7de5d2bf4d0a1a43a와 WordSHA4f1112dc09f995b3438a0fccc7801bffdad9220f887251cb9aff710c9571b686는 당시 불변 증거다. 현재 루트 원장 후속 버전과 구별한다. Word는 hash 보존을 확인한 것이며 본문 완료가 아니다. 현재 아카이브의 보호 원본·별칭 해시 검수는 연구 예산·최종 추천을 갱신하지 않는다.

근거: [SRC-0001995](../sources/history-132.md#src-0001995) JSON /ledger_unchanged_sha256, /prior_Word_unchanged_sha256, /goal_complete · [SRC-0001993](../sources/history-132.md#src-0001993) 행78–78 · [SRC-0002001](../sources/history-132.md#src-0002001) 행17–23

<a id="claim-34"></a>

### H132-C34 · 출처·사본·배포와 집계 단위

최초 선택33출처/65물리경로에 기존 RCTL2출처/16경로를 연결해 최종35출처/81경로다. 같은SHA 사본·이전자료 재독·변환TXT·PDF파생PNG·공식 연결 그림은 독립 새 원문으로 중복 집계하지 않는다. 연구자 소형 원본과 기존 정확사본을 팀 경로로 연결하고 논문/공식 코드 원문은 버전·hash·정식 링크·검토 범위로 제공한다.

근거: [SRC-0001991](../sources/history-132.md#src-0001991) 행1–151 · [SRC-0020840](../sources/history-132.md#src-0020840) 행1–8 · [SRC-0002013](../sources/history-132.md#src-0002013) 행1–30

<a id="claim-35"></a>

### H132-C35 · 전체 판독과 아직 읽지 않은 구간

현재 raw text22자료2348고유행(19전문/3선택)·두 PDF86쪽8069행·notebook82셀과 저장 출력6개를 확인했다. literal paper TXT 두 개는 직접 전독하지 않았고 PDF 추출의 정확 대응만 검수했다. notebook raw JSON 전문도 아니다. progress 긴 tail, Word/FedPPBC/발표자료와 다른 고유 판본·후속 원103 이후·전체 통합/팀 접근/최종 delta/검색10+는 남는다.

근거: [SRC-0001999](../sources/history-132.md#src-0001999) 행1–17 · [SRC-0001969](../sources/history-132.md#src-0001969) 행1–12 · [SRC-0001993](../sources/history-132.md#src-0001993) 행27–29 · [SRC-0001993](../sources/history-132.md#src-0001993) 행78–83

<a id="claim-36"></a>

### H132-C36 · 재검토 조건과 현재 Goal의 완료 범위

Tab 추정값+RNN kernel을 다시 검토하려면 현재 구조·학습 조건에서 유용한 결정의 대리 정확도 또는 같은 결정을 더 싸게 얻는 근거와 기존 empirical/저장 Tab 기준 대비 차이를 특정해야 한다. 일반 NTK 극한의 존재나 Tab 직접 MAE 개선만으로 재채택하지 않는다. 현재는 원102 정리이며 새 설계·모델 실험·최종 Word를 완료한 것이 아니다. 검수본의 PR/병합 뒤에도 전체 연구기록 정리 Goal은 계속된다.

근거: [SRC-0001993](../sources/history-132.md#src-0001993) 행72–78 · [SRC-0001992](../sources/history-132.md#src-0001992) 행27–35 · [SRC-0001994](../sources/history-132.md#src-0001994) 행19–23
