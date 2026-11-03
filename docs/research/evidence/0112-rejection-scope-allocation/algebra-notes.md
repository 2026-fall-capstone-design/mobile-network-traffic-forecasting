# 원85의 고정 손실 배분식 대조

[원문35–47행](originals/SRC-0022056.md.txt) · [정리 기록 C08–C14](../../records/0112-rejection-scope-allocation.md#c08) · [7개 대수 전개](algebra-check.json)

아래는 원문의 기호식을 확인한 설명이다. 통신 데이터나 학습기를 새로 실행한 결과가 아니다. 모든 식은 한 group g의 기여에 관한 식이다.

$$Q=\sum_g\pi_gP_g,\quad \pi_g>0,\quad \sum_g\pi_g=1,\quad Z=(X,Y),\quad r_g(Z)=\pi_g\frac{dP_g}{dQ}(Z),\quad c_g=\frac{a_g}{\pi_g}.$$

함수·모수·손실과 a_g를 고정한다. 기대값에는 적분 가능성을, 분산에는 관련 제2모멘트의 존재를 가정한다. H_g와 U_g는 다음과 같다.

$$H_g=\mathbf1\{G=g\}c_g\ell_g(Z),\qquad U_g=c_gr_g(Z)\ell_g(Z).$$

조건부 출처 지시의 평균은 r_g이므로 E[H_g|Z]=U_g이고 E_Q[U_g]=a_g E_{P_g}[ℓ_g]다. 분산을 비교하는 변수의 제2모멘트가 존재하면,

$$\operatorname{Var}(H_g\mid Z)=c_g^2r_g(1-r_g)\ell_g^2,\qquad \operatorname{Var}(H_g)=\operatorname{Var}(U_g)+\mathbb E[\operatorname{Var}(H_g\mid Z)].$$

J를 p(·|Z)에 따라 하나 뽑을 때 r_g>0이면 p_g>0이어야 한다. r_g=p_g=0인 항은0이다.

$$S_g=\mathbf1\{J=g\}\frac{c_gr_g\ell_g}{p_g},\qquad \mathbb E_J[S_g\mid Z]=U_g.$$

$$\operatorname{Var}_J(S_g\mid Z)=c_g^2r_g^2\ell_g^2\left(\frac1{p_g}-1\right).$$

support 조건만으로 S_g의 적분 가능한 제2모멘트가 보장되지는 않는다. p_g가 너무 작으면 변동이 커질 수 있다. p=r인 특별한 경우에는 위 조건부 분산이 H_g의 값과 같고 Q(dz)r_g(z)=π_g P_g(dz)이므로 (Z,J)와 (Z,G)의 결합분포가 같다.

원문47행의 반복식을 사용할 때는 아래의 p=r 조건을 명시해야 한다. 같은 Z에 조건부로 독립인 J_1,…,J_E를 p=r로 뽑아 기여를 평균하자. E는 양의 정수다.

$$\operatorname{Var}\left(\frac1E\sum_{e=1}^{E}S_{g,e}\right)=\operatorname{Var}(U_g)+\frac1E\mathbb E[\operatorname{Var}(H_g\mid Z)].$$

이는 공통 Z의 변동을 줄이지 않으며, 조건부 배분 변동만1/E로 줄인다. 일반 p라면 뒤 항에는 H_g가 아니라 해당 S_g의 조건부 분산이 들어간다. 원래 G를 고정해 같은 기여를 반복하는 것과 조건부 독립 재배분을 구분한다.

새 관측 증가·실제 SGD의 모수 변화·BatchNorm의 batch 변화·시간/cell 의존·추정 posterior·고정 quota 전체에 자동 적용되는 식이 아니다. soft 기여를 모두 계산하는 비용도 여러 모델 평가와 연결한다. 기존 이론의 보편적 성능 보장이나 새로운 정리로 제시하지 않는다.
