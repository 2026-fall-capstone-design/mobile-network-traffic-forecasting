# 원79 Toso 회귀 이론: 가정·gradient 수렴·함수 복원의 구분

[출처](../sources/history-086.md) · [검수](../verification/history-086.md) · [근거](../evidence/0086-toso-gradient-heterogeneity/README.md) · [원76–79](0076-0079-learning-decisions.md)

검수 완료: 저장v1 전문·부록의 첫 독해와 핵심34주장의 작성 후 대조를 마쳤다. 이 논문은 새 iid 표본과 공통 입력·Jacobian·PL 등의 조건을 둔 회귀 이론이며, TabICL 예측 유사성이나 RCTL 최종 성능의 직접 보장은 아니다. 논문 전체의 형식 증명 검증·독립 연구자 심사·모델 재현은 수행하지 않았다.


## 검토 자료와 실행 범위

<a id="c01"></a>**C01.** H086은 원79가 저장한 Toso·Anderson·Gupta·Pinot의 On the Gradient Heterogeneity Dynamics of Adversarially Robust Federated Regression, arXiv2609.25705v1(2026-09-22)을 다룬다. HTML의 초록·§1–7·참고문헌32항목·부록A/B.1–8/C.1–6을 읽었다. 원79 당시의 선택 독해를 이번 전문 독해로 소급하지 않는다.

출처: [SRC-0062499 · 메타데이터/전본문·부록](https://arxiv.org/html/2609.25705v1#abstract1) · [SRC-0022036 · 읽은 범위와 접근 기록](../evidence/0076-0079-learning-decisions/originals/SRC-0022036.md.txt)

<a id="c02"></a>**C02.** 저장 HTML820978B와 TXT96649B는 다른 파일이다. 수식을 alttext로 치환하고 script/style/nav와 공백을 제외하면 HTML86366문자, TXT86371문자이며 차이는 navigation의 G_{T}5문자뿐이다. 전체 HTML에는 수식734개가 있고 그중1개는 navigation 반복이다. TXT를 독립 논문 한 편으로 중복 가산하지 않는다.

출처: [SRC-0062499 · 전체 DOM·수식734 및 navigation](https://arxiv.org/html/2609.25705v1#infobox) · [SRC-0062500 · 95547문자 전체 대응/앞뒤 직접대조](https://arxiv.org/html/2609.25705v1#infobox)

보충 근거: [바이트·표현 대응 및 새PDF 취득 기록](../evidence/0086-toso-gradient-heterogeneity/representation-check.json)


<a id="c03"></a>**C03.** 표기의 변환 오류 여부를 확인하려고 같은 v1의 PDF를 이번 정리 때 새로 취득했다. 447570B·30쪽이며3·8·9·10·11·17·24·25·28쪽을 시각 대조했다. PDF30쪽 전체를 별도 독해했다고 세거나 원79 당시 확보한 자료라고 기록하지 않는다. PDF·렌더 원문은 재게시하지 않고 URL·해시·확인 위치를 연결한다.

출처: [SRC-0062499 · §1.2/§3–4/B.1/B.8/C.1/C.5](https://arxiv.org/html/2609.25705v1#S1.SS2) · [SRC-0022036 · 당시 Toso HTML 선택 독해 범위](../evidence/0076-0079-learning-decisions/originals/SRC-0022036.md.txt)

보충 근거: [바이트·표현 대응 및 새PDF 취득 기록](../evidence/0086-toso-gradient-heterogeneity/representation-check.json) · [공식v1 PDF](https://arxiv.org/pdf/2609.25705v1)


<a id="c04"></a>**C04.** 이 논문 본문은 회귀 이론과 증명으로 구성되며 경험 실험표·성능 그림·dataset별 seed 결과를 제공하지 않는다. DOM의 table148개는 수식 등의 배치 구조이며 실험표148개가 아니다. 실제 traffic 시간 분할·정규화·훈련 seed·GPU 시간·성능 비교값은 이 이론 기록에 해당 없음이다. 원79의 새 모델·수치 pilot과 누적 비용 원장 변경은0이다.

출처: [SRC-0062499 · 전본문/부록·DOM table/figure 범위](https://arxiv.org/html/2609.25705v1#S6) · [SRC-0022036 · 도입/79 새 수치 계산 없음](../evidence/0076-0079-learning-decisions/originals/SRC-0022036.md.txt)


## 공통 설정과 선형 회귀

<a id="c05"></a>**C05.** 논문은 서버가 하나의 공통 parameter를 갱신하는 동기식 federated regression을 다룬다. n명 중 알려지지 않은 honest 집합H와 f명의 임의 업데이트 공격자를 구분하고 f<n/2를 요구한다. cell 군집을 찾는 알고리즘이나 UPC 소속 수정 절차, 분산 RCTL 실험을 제안한 논문으로 분류하지 않는다.

출처: [SRC-0062499 · §2 Problem Formulation/§2.1](https://arxiv.org/html/2609.25705v1#S2)

<a id="c06"></a>**C06.** 각 honest client는 매 round τ개의 새 iid 표본을 뽑으며 client와 round 사이의 batch는 독립이다. 현재 iterate에 조건부로 다음 gradient 표본의 독립성을 이용한다. 같은 고정 시계열 창을 여러 epoch 재사용하는 경우와 같다고 쓰지 않는다. 고정 local dataset 재사용의 의존성 제어는 §6의 후속 과제다.

출처: [SRC-0062499 · §2 Data and samples/§6/C.3/B.6](https://arxiv.org/html/2609.25705v1#S2.p3)

<a id="c07"></a>**C07.** population loss L_i와 새 batch의 empirical loss Lhat_i를 구별한다. G^(t)는 honest empirical gradient가 그 평균에서 벗어나는 제곱 norm의 평균이고 G_T는 시간 평균이다. Q_T는 honest-average population gradient의 제곱 norm을 시간 평균한 수렴 지표다. client 간 경험 gradient 차이, population 평균 gradient가 작아짐, 최종 test MAE를 같은 지표로 취급하지 않는다.

출처: [SRC-0062499 · §2 losses/§2.2/G_T,Q_T 정의](https://arxiv.org/html/2609.25705v1#S2.SS2)

<a id="c08"></a>**C08.** (f,κ)-robustness는 임의 입력과 가능한 honest 집합에 대해 aggregate와 honest 평균의 제곱 거리가 κ배 honest 입력 분산으로 제어된다는 조건이다. κ=O(f/n)인 집계기가 주어졌을 때 충분한 표본으로 분석을 닫는다. κ를 자유로운 군집 임계값으로 쓰거나 표본만 늘리면 임의 공격 비율·임의 집계기가 허용된다고 결론내리지 않는다.

출처: [SRC-0062499 · §2.1 Definition2.1/§1/§3 discussion](https://arxiv.org/html/2609.25705v1#S2.Thmdefinition1)

<a id="c09"></a>**C09.** Assumption2.1은 모든 honest client에 E[XXᵀ]=I_d인 isotropy를 둔다. 알려진 비특이 population covariance로 whitening할 수 있다는 설명이 있으나 우리 데이터가 이미 이를 만족한다는 증거는 아니다. 비선형 분석은 추가로 모든 honest client의 입력 주변분포가 같다고 명시한다.

출처: [SRC-0062499 · §2 Assumption2.1/§4 common marginal](https://arxiv.org/html/2609.25705v1#S2.Thmassumption1)

<a id="c10"></a>**C10.** 선형 모델은 Y=θ_i⋆X+V, θ_i⋆∈R^(q×d), ||X||≤R를 가정한다. V는 X에 조건부 평균0이며 방향별 σ²-sub-Gaussian이다. Γ_lin은 honest 참 parameter들 사이의 제곱 거리 평균으로 정의된다. label 잡음의 분산, 현재 추정 parameter 오차, 참 client 차이를 구분한다.

출처: [SRC-0062499 · §3 Assumption3.1/Γ_lin/B.1](https://arxiv.org/html/2609.25705v1#S3.Thmassumption1)

<a id="c11"></a>**C11.** 새 batch 선형 gradient는 2(θ−θ_i⋆)Σhat_i−ξ_i이다. honest 평균과의 차이는 참 parameter 차이, covariance의 표본 오차, label-noise 차이와 현재 iterate가 곱해지는 항을 포함한다. 논문은 이 구조에서 경험 gradient heterogeneity의 iterate 의존 항을 도출한다. 참 함수가 비슷하다는 사실 하나로 유한 batch gradient가 동일하다고 보장하지 않는다.

출처: [SRC-0062499 · §3 decomposition/B.1 Eq8–10/B.5 Eq15–22](https://arxiv.org/html/2609.25705v1#S3.p6)

<a id="c12"></a>**C12.** 논문에서 iterate 의존 제곱-gradient 항의 계수는 ω²이고, (G,B)-dissimilarity에 대응하는 것은 B²이다. 선형의 ω²는 (R²+1)²·log(2|H|T(d+q)/δ)/τ에 비례한다. B 자체가 언제나1/τ라고 바꾸지 않으며, 유한 표본의 covariance 차이가 없는 population gradient와도 구분한다.

출처: [SRC-0062499 · §2.2/§3 Key Takeaway/B.5 Eq16](https://arxiv.org/html/2609.25705v1#S3.p14)

<a id="c13"></a>**C13.** 선형 burn-in은 round 수가 아니라 매 client·round의 새 표본 수 τ의 하한이다. 충분히 큰 상수 C0C1에 대해 (R²+1)²·max{1,κ+1/|H|}·log(2|H|T(d+q)/δ)에 비례하는 표본을 요구한다. 이 조건은 ω≤1 및 ω²(κ+1/|H|)의 충분한 작음을 확보한다. Lemma3.1은 η≤1/2, Theorem3.1은 η=1/2로 진술한다.

출처: [SRC-0062499 · §3 Lemma3.1/Theorem3.1/B.5 Eq16–17](https://arxiv.org/html/2609.25705v1#S3.Thmlemma1)

<a id="c14"></a>**C14.** Theorem3.1의 Q_T 상한은 초기 손실 차이/T, (κ+ω²/|H|)Γ_lin, 그리고 R²σ²(κ+1/|H|)(dq+log(2|H|T/δ))/τ의 합 형태다. 각 식은 확률1−δ의 상수 생략 상한이며 실측 향상률이나 모든 개별 round의 오차 보장이 아니다. κ>0일 때 참 client 차이의 항은 τ만 늘려 일반적으로 제거되지 않는다.

출처: [SRC-0062499 · §3 Theorem3.1/B.7 proof](https://arxiv.org/html/2609.25705v1#S3.Thmtheorem1)

<a id="c15"></a>**C15.** Corollary3.1은 client·round 평균 parameter 복원 오차를 Q_T/4+Γ_lin/2라고 진술한다. 따라서 평균 목적 gradient가 작아져도 서로 다른 모든 client의 참 parameter를 하나의 model로 동시에 복원한다는 뜻이 아니다. 본문의 상한에는 (1+κ+ω²/|H|)Γ_lin이 남는다. matrix norm 표기의 확인사항은 C25에 별도로 남긴다.

출처: [SRC-0062499 · §3 Corollary3.1/B.6 Eq21/B.8](https://arxiv.org/html/2609.25705v1#S3.Thmcorollary1)

<a id="c16"></a>**C16.** TheoremB.1과 CorollaryB.1은 일반 η≤1/2의 초기항1/(ηT)를 유지하고 Γ 계수를 κ+1/|H|, 1+κ+1/|H|로 느슨하게 진술한다. B.7 증명에는 ω²/|H|가 남은 식도 있다. ω≤1 조건에서의 느슨화와 η=1/2 대입을 표기 차이로 기록하며 서로 다른 경험 결과나 자동적인 모순으로 세지 않는다.

출처: [SRC-0062499 · B.7 TheoremB.1/Ex90/B.8 CorollaryB.1/§3](https://arxiv.org/html/2609.25705v1#A2.Thmtheorem1)


## 비선형 가정과 보장의 대상

<a id="c17"></a>**C17.** 비선형 Γ_nonlin은 같은 입력 주변분포의 X에서 참 함수 h_i⋆(X)와 h_j⋆(X)의 제곱 차이를 평균한다. 서로 다른 cell의 관측 x 분포 자체가 다른 상황은 이 정의와 가정에 추가 연결이 필요하다. 각자 관측한 x와 TabICL 추정 m(x)의 joint 분포 거리를 곧 Γ_nonlin이라고 부르지 않는다.

출처: [SRC-0062499 · §4 common marginal/Γ_nonlin/C.4](https://arxiv.org/html/2609.25705v1#S4.p3) · [SRC-0022036 · 다음 후보의 실제 차이](../evidence/0076-0079-learning-decisions/originals/SRC-0022036.md.txt)

<a id="c18"></a>**C18.** 비선형 h_θ:R^d→R^q의 parameter 차원은 p다. Assumption4.1은 모든 θ,X의 Jacobian norm을 Jbar로 제어한다. Assumption4.2는 현재 θ에 조건부인 참 함수 residual norm의 ψ2 크기를 sqrt(E_i^(t))로 제어한다. bounded 입력이나 사전학습 모델 사용만으로 이 두 조건이 검증됐다고 간주하지 않는다.

출처: [SRC-0062499 · §4 Assumption4.1–4.2/C.3 LemmaC.1](https://arxiv.org/html/2609.25705v1#S4.Thmassumption1)

<a id="c19"></a>**C19.** Assumption4.3은 honest-average population loss의 L′-Lipschitz gradient, Assumption4.4는 모든 θ의 global PL 조건 ||∇L_H||²≥2μ′(L_H−L_H⋆)를 요구한다. 논문의 신경망/NTK 설명은 조건이 만족되는 예시에 관한 설명이다. 우리 RCTL의 모든 초기값·훈련 구간·parameter에서 이 조건을 확인한 결과가 아니다.

출처: [SRC-0062499 · §4 Assumption4.3–4.4/Eq6](https://arxiv.org/html/2609.25705v1#S4.Thmassumption3)

<a id="c20"></a>**C20.** Γ_nonlin의 h_i⋆는 자료 생성의 참 함수다. 저장 TabICL 출력은 추정값이므로 estimation error·support·공통 입력 및 비교할 최종 함수의 Jacobian을 연결해야 한다. 참 함수 거리의 상한을 추정 출력 거리나 cluster score에 바로 대입하여 RCTL 수렴 보장으로 바꾸지 않는다.

출처: [SRC-0062499 · §4 model/Γ_nonlin/C.2–4](https://arxiv.org/html/2609.25705v1#S4.p8) · [SRC-0022036 · 다음 후보의 실제 차이](../evidence/0076-0079-learning-decisions/originals/SRC-0022036.md.txt)

<a id="c21"></a>**C21.** C.2–4는 empirical residual–Jacobian 평균 shat_i, population 평균 s_i, 잡음 ξ_i를 나누고, 공통 X에서 현재 h_θ 항이 소거되는 구조를 사용한다. G^(t)는 Jbar²Γ_nonlin, ωbar²Ebar^(t), 표본 잡음 항으로 제어된다. C.5의 PL을 통해 Ebar^(t)≤Γ_nonlin+||∇L_H||²/(2μ′)로 연결한다.

출처: [SRC-0062499 · C.2 Eq28/C.4 LemmaC.2/C.5 Eq34–35](https://arxiv.org/html/2609.25705v1#A3.SS4)

<a id="c22"></a>**C22.** 비선형 ωbar²는 Jbar²(p+log(2|H|T/δ))/τ에 비례하고 τ 하한은 Jbar²/μ′·(κ+1/|H|)·(p+log(2|H|T/δ))에 비례한다. C.5의 Q_T 상한은 초기 손실 차이/(ηT), [κJbar²+ωbar²(κ+1/|H|)]Γ_nonlin, Jbar²σ²(κ+1/|H|)(p+log(2|H|T/δ))/τ를 포함한다. κ만 작으면 되는 무조건 보장이 아니다.

출처: [SRC-0062499 · §4 Lemma4.1/Theorem4.1/C.4 Eq31/C.5 Eq36/TheoremC.1](https://arxiv.org/html/2609.25705v1#A3.Thmtheorem1)

<a id="c23"></a>**C23.** Corollary4.1과 CorollaryC.1의 heading은 Parameter Recovery이지만 좌변은 E||h_θ(X)−h_i⋆(X)||²의 client·round 평균이다. C.6 절 제목도 Function Recovery다. nonlinear parameter 자체의 거리나 식별성을 보장한다고 확대하지 않는다. 상한의 Γ 계수에는1이 남아 하나의 전역 함수와 여러 참 함수의 차이를 보존한다.

출처: [SRC-0062499 · §4 Corollary4.1/C.6 CorollaryC.1](https://arxiv.org/html/2609.25705v1#A3.SS6)


## 인용 전에 확인할 표기

<a id="c24"></a>**C24.** Lemma4.1은 η≤1/L′를 두지만 Theorem4.1의 초기항은 L′ΔL⁽⁰⁾/T, Corollary4.1은 L′ΔL⁽⁰⁾/(μ′T)를 쓴다. AppendixC는 각각 ΔL⁽⁰⁾/(ηT), ΔL⁽⁰⁾/(μ′ηT)를 유지한다. η=1/L′이면 이 두 표기를 연결할 수 있으나 더 작은 모든 η에 같은 L′/T 상한을 그대로 적용하지 않는다. Lemma4.1의 두 번째 G_T 식과 LemmaC.3의1/η 차이도 재확인 대상으로 남긴다.

출처: [SRC-0062499 · §4 Lemma4.1/Theorem4.1/Corollary4.1/C.5 TheoremC.1/LemmaC.3](https://arxiv.org/html/2609.25705v1#S4.Thmtheorem1)

<a id="c25"></a>**C25.** §1.2는 기본 matrix norm을 spectral/operator, Frobenius norm은 아래첨자F로 구분한다. B.8은 isotropy하의 E||(θ−θ_i⋆)X||²=Tr((θ−θ_i⋆)ᵀ(θ−θ_i⋆))를 아래첨자 없는 norm²와 동일시한다. 일반 matrix에서 trace는 Frobenius norm²에 해당하므로 표기 해석을 확인해야 한다. scalar-output 특수 경우와 일반 q×d matrix를 구분하며 이 관찰만으로 논문 전체 정리의 참·거짓을 판정하지 않는다.

출처: [SRC-0062499 · §1.2/B.6 Eq21/B.8 Ex91/CorollaryB.1](https://arxiv.org/html/2609.25705v1#A2.SS8)

<a id="c26"></a>**C26.** §3 Key Takeaway에는 client 차이가 있는 복원 오차 항이 없어지지 않는다는 설명과 τ→∞에서 사라진다는 괄호 문구가 함께 있다. Corollary3.1의 Q_T/4+Γ_lin/2 및1+κ+ω²/|H|를 함께 읽어야 한다. τ 증가로 줄어드는 표본 항, κ=0일 때의 Q_T 상한, 모든 client에 대한 복원 오차 바닥을 분리한다.

출처: [SRC-0062499 · §3 Key Takeaway/Corollary3.1/B.8](https://arxiv.org/html/2609.25705v1#S3.p13)

<a id="c27"></a>**C27.** RemarkB.1의 G^(t) 식은 hat 없는 L_i를 쓰면서 아래에서는 empirical covariance 편차를 설명한다. 공통 isotropy인 선형 population gradient는2(θ−평균 θ⋆)이고 개별 gradient와 평균의 차이에서 현재 θ가 소거된다. 따라서 유한 표본 경험 gradient의 비유계 가능성을 이 특수 population gradient에도 그대로 옮겨 쓰지 않는다.

출처: [SRC-0062499 · B.1 RemarkB.1/B.6 Eq20/§2 losses](https://arxiv.org/html/2609.25705v1#A2.Thmremark1)

<a id="c28"></a>**C28.** §4는 r_j^(t)를 함수 차이의 scalar norm으로 정의한 뒤 W=r_j^(t)Jᵀ라고 표기한다. C.1–3의 gradient와 W는 부호·방향이 남은 함수 차이 vector를 사용한다. norm의 tail 제어와 실제 gradient에 들어가는 residual vector 및 행·열 관례를 구분해야 한다. 변환 오류인지 확인한 PDF에서도 이 차이가 있어 임의로 원문을 고쳐 쓰지 않는다.

출처: [SRC-0062499 · §4 Assumption4.2 뒤 W 정의/C.1/C.3 Ex105](https://arxiv.org/html/2609.25705v1#S4.p5)

<a id="c29"></a>**C29.** 이번에는 부록의 부등식·concentration·gradient 분해·최적화 recursion·복원 연결까지 읽고 핵심 주장과 표기를 대조했다. 이는 완전한 형식 증명 검증이나 독립 연구자 심사, 실제 모델 재현이 아니다. 충분히 큰 미지 상수의 상한을 dataset별로 수치화하거나 임의의 sample 수를 이 논문의 권장값으로 제시하지 않는다.

출처: [SRC-0062499 · B.2–8/C.1–6/§1.2 asymptotic notation](https://arxiv.org/html/2609.25705v1#A1)


## 원79 판단과 다음 연구의 차이

<a id="c30"></a>**C30.** §5의 FedProx·SCAFFOLD·Krum·NNM·clipping 등 비교 설명과 참고문헌32개를 확인했지만 그 인용 논문32편의 전문을 읽은 것으로 세지 않는다. §6은 고정 dataset 재사용, local model updates, 부분 client 참여, 시간에 따라 바뀌는 공격자 집합을 미래 범위로 둔다. 이를 현재 정리의 검증 범위로 추가하지 않는다.

출처: [SRC-0062499 · §5/§6/References32](https://arxiv.org/html/2609.25705v1#S5)

<a id="c31"></a>**C31.** 원79는 Toso의 HTML§2–4와 B.1 모델·gradient 식을 선택적으로 읽었고 전체 proof 검증·구현 재현이 아니라고 명시했다. 당시 결론은 예측값 유사성을 최종 학습 효과와 동일시하지 않으며, 같은 입력 주변분포·bounded Jacobian·PL 및 새 iid 표본 등의 가정 때문에 시계열·RCTL에 보장을 그대로 가져오지 않는다는 것이었다.

출처: [SRC-0022036 · 선행연구 표/읽은 범위와 접근 기록](../evidence/0076-0079-learning-decisions/originals/SRC-0022036.md.txt) · [SRC-0062499 · §2–4/B.1](https://arxiv.org/html/2609.25705v1#S2)

<a id="c32"></a>**C32.** 원79가 별도로 설명한 제곱손실 기대 gradient E[2(f(x)−m(x))∇f(x)]는 고정된 함수와 미분·기대값 교환 조건하의 관계다. 동일 입력 분포와 조건부 평균이면 label 잡음 분산이 달라도 이 기대값이 같을 수 있다. 유한 batch SGD 분산, 학습 경로, 최종 test 오차가 같다는 뜻은 아니다. 이 관계를 논문이 TabICL이나 RCTL에 입증한 결과라고 인용하지 않는다.

출처: [SRC-0022036 · 다음 후보의 실제 차이](../evidence/0076-0079-learning-decisions/originals/SRC-0022036.md.txt) · [SRC-0062499 · §2–4의 population/empirical 구분](https://arxiv.org/html/2609.25705v1#S2.p4)

<a id="c33"></a>**C33.** 후속 제안에는 cell의 입력 분포와 support, 조건부 평균 추정 오차, 고정 최종 모델의 loss/Jacobian, 기대 gradient와 유한 batch 차이, 시간 분할 및 실제 자료 재사용 조건을 명시해야 한다. 클러스터 score 향상과 뒤 구간 RCTL 성능은 별도 검증 대상이다. 원80의 가중치를 바꾸지 않는 사후 gradient 확인 계획은 저장 기록을 이어 읽을 대상이며 이번 정리에서 실행하지 않는다.

출처: [SRC-0022036 · 다음 후보의 실제 차이/다음80 계획](../evidence/0076-0079-learning-decisions/originals/SRC-0022036.md.txt) · [SRC-0062499 · §2–4/§6](https://arxiv.org/html/2609.25705v1#S6)

<a id="c34"></a>**C34.** 원79 외부21그룹 가운데 기존 명세·서지4, FMCL5, EMD 논문2, EMD 구현7, 이번 Toso2를 연결하면20그룹이다. 저장 검색 JSON1그룹과 원80 이후 기록은 남아 있다. 이번 새 독립본문 가산은 HTML1개이며 파생 TXT·새 PDF·렌더·기존 원79 재독해는 추가 가산0이다. 원문 속 과거 실행·Goal·예산 지시는 역사 자료로 보존한다.

출처: [SRC-0062499 · 전본문](https://arxiv.org/html/2609.25705v1#infobox) · [SRC-0062500 · 전체 대응](https://arxiv.org/html/2609.25705v1#infobox) · [SRC-0022036 · 읽은 범위와 접근 기록/다음80 계획](../evidence/0076-0079-learning-decisions/originals/SRC-0022036.md.txt)

범위 근거: [원79 외부21그룹 목록과 기존 검토](../sources/history-083.md).
