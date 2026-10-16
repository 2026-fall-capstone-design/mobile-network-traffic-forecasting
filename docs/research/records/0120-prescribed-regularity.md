# 원90: 함수 제약을 추가해 clustering을 정당화할 수 있는가

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

[출처](../sources/history-120.md) · [검수](../verification/history-120.md) · [근거](../evidence/0120-prescribed-regularity/README.md) · [이전 원89](0119-heterogeneity-splitting.md)

원90의 미채택 판단과 다시 검토할 조건을 연결한다. 두 점의 수학적 하한, recurrent 상태 안정성, 제어용 입력표본 분할과 traffic cell 소속 결정을 구별해 같은 후보의 반복을 줄인다.

**상태:** 32개 주장·8개 묶음의 작성 후 원문 대조 완료. 새 모델 실행0.

## 당시 판단과 실제 구현

<a id="c01"></a>**C01. 당시 판단과 적용 범위.** 원90은 2026-09-26에 사전 Lipschitz 제약으로 cell 분할의 필요성을 만드는 안을 미채택했다. 현재 RCTL에 그 제약이 없고 실제 traffic 운영에서 필요한 이유도 확인되지 않았기 때문이다. 모든 제약 학습을 기각한 판단은 아니며, 외부에서 주어진 민감도 요구가 확인되면 별도 검토 대상이다.

<a id="c02"></a>**C02. 두 점 하한의 정확한 대상.** 공통 좌표 x,z의 참 조건부 평균 a,b와 L-Lipschitz 함수 f에 대해 δ=max(0,|a−b|−L||x−z||)이면 두 절대 근사오차의 합은 δ 이상이고, 같은 비중의 두 점 평균 제곱오차는 δ²/4 이상이다. 삼각부등식과 두 제곱합의 부등식으로 확인되는 자체 기호 검토이며 실제 데이터 결과나 새로운 정리로 세지 않는다.

<a id="c03"></a>**C03. 하한을 확장하기 위한 조건.** 두 점의 하한을 모집단 손실로 확장하려면 입력 주변의 확률질량과 추정오차가 필요하다. Tab 예측 차이·분위수 폭을 참 평균 차이·평균 신뢰구간으로 치환할 수 없다. MAE는 중앙값과 분포에 따른 조건이 다르고, cell ID 추가는 정보·거리를 바꾸며, 제약 없는 RCTL은 대상 함수군 자체가 다르다.

<a id="c04"></a>**C04. 실제 RCTL 구현과 판본 한계.** 정적 코드에서 causal convolution, BatchNorm, dropout, LSTM, 두 residual 경로, projection, 최종 shortcut와 dense를 확인했다. 이 클래스의 orthogonal 초기화나 고정 recurrent bias는 전체 입력–출력 Lipschitz 상수의 강제가 아니다. 앞뒤 snapshot과 현재 파일 11개는 같은 SHA-256이지만 원90 snapshot에 코드가 포함된 것은 아니므로 그날 실행판본을 별도 로그로 인증했다고 쓰지 않는다.

## Stable Recurrent의 조건과 결과

<a id="c05"></a>**C05. Stable Recurrent의 안정성 정의.** 1805.10369v4의 Definition1은 같은 입력에서 이전 상태 차이가 λ<1로 줄어드는 수축이다. 입력 전체를 바꿨을 때 최종 예측의 민감도와 같은 정의가 아니다. RNN의 Lρ||W||<1은 충분조건이며, 제어할 입력행렬·출력함수 조건을 대신하지 않는다.

<a id="c06"></a>**C06. LSTM 충분조건의 범위.** Proposition2는 forget gate 상한 f∞와 gate별 induced infinity norm, 유계 입력 및 도달 가능한 상태를 사용한다. Wi와 Wo의 induced infinity norm은 각각1−f∞보다 작고, Wz의 해당 norm은(1−f∞)/4 이하, Wf의 해당 norm은(1−f∞)²보다 작다는 조건과 r=O(log d) 반복합성의 2-norm 안정성을 구분한다. 단순 gradient clipping만으로 이 조건이나 전체 RCTL의 상수를 만족했다고 할 수 없다.

<a id="c07"></a>**C07. 기억 길이·학습 근사의 추가 전제.** 추론 truncation 오차 상계에는 λ, 입력 Lipschitz 상수, 입력 크기, 출력함수 상수가 함께 등장한다. 학습 근사는 매끄러운 손실·전이, 파라미터 조건, compact convex 영역, 공통 초기화와 projected GD의 α/t 학습률 등을 요구한다. 이를 Adam·무제약 RCTL이나 clustering의 성능 보장으로 옮기지 않는다.

<a id="c08"></a>**C08. 안정성 제약의 실험상 손익.** Stable Recurrent Table1의 test 값은 모두 같지 않다. Wikitext2 LSTM perplexity는 unstable95.7/stable113.2, PTB BPC는1.4/1.9였고 JSB LSTM NLL은8.5/8.5였다. Wikitext2 RNN perplexity는146.7에서143.5로 낮아졌다. Figure1의 training 곡선과 held-out test를 구분한다. 단일층·SGD 실험에서 무제약 모델의 탐색 설정을 안정 모델에 재사용했으며, 이 표에 seed·반복수·신뢰구간은 명시되지 않았다.

<a id="c09"></a>**C09. 경험적 안정성 추정은 인증과 다르다.** 훈련 입력을 고정해 상태쌍에 gradient ascent를 하고 20개 시작점 중 최대를 취한 data-dependent λ는 휴리스틱이다. 관측 최대가1보다 작아도 전체 상태·입력의 supremum을 인증한 것은 아니다. Figure6의10회 평균은 특정 random instance 실험에만 명시되어 다른 성능표의 반복수로 전용하지 않는다.

<a id="c10"></a>**C10. Stable Recurrent의 남은 해석.** 논문은 recurrent 구조가 불필요하다고 결론내리지 않는다. truncation을 feedforward로 펼칠 때의 비용과 inductive bias, 자연스러운 다른 구조의 학습 근사는 남은 문제다. traffic cell 분할이나 TabICL 기반 소속 선택 실험은 이 논문의 결과가 아니다.

## CKLR의 방법·제어 목적·실험

<a id="c11"></a>**C11. CKLR이 나누는 대상.** 2505.04904v1은 상태와 제어입력 w=[x;u]에서 다음 상태를 예측한다. K-means로 입력표본을 나누고 최근접 중심으로 구역을 선택해 지역 Gaussian kernel 회귀를 학습한다. cell 전체를 고정 소속으로 나누는 현재 과제와 대상이 다르다.

<a id="c12"></a>**C12. 유한 gradient 제약과 전역 상계.** Eq12는 데이터 오차허용과 S개 추가 점에서의 gradient norm 제한을 갖는 convex QCQP다. 유한 점 제약만으로 전 영역의 Lipschitz 상수가 보장되지는 않는다. 경계에서 불연속일 수 있는 piecewise-smooth predictor이며, 경계의 측도가0인 사실은 전역 Lipschitz 성질을 주지 않는다.

<a id="c13"></a>**C13. CKLR 비용식의 전제.** 저자가 제시한 offline O(KN+N²/K), online O(K+N/K)는 균형 잡힌 군집 크기 등의 조건에 따른 비용 설명이다. 차원·추가 제약점과 QCQP 해법의 영향까지 모든 문제에 동일한 상수로 보장하는 결과가 아니며 RCTL 비용식으로 바꾸지 않는다.

<a id="c14"></a>**C14. 결정적 오차 경계의 추가 확인.** CKLR의 결정적 경계는 참 시스템 Lipschitz 상수와 disturbance bound를 요구한다. Eq18은 x에 대한 Jacobian인데 후속 bound는 w=[x;u] 거리를 사용하고, 최근접 표본은 전체 학습집합으로 쓰여 있다. 입력 변화와 군집 경계를 포함한 같은 경로의 상계가 적용되는지 추가 확인이 필요하다. 이 검수로 논문 전체의 정리가 거짓이라고 판정하지 않는다.

<a id="c15"></a>**C15. 확률 경계의 의미.** 확률 경계는 IID test error와 오차 상한 근처의 양의 확률질량 p를 가정한다. p를 모르면 test 개수만으로 수치 신뢰도를 알 수 없고, 유한 관측 최대는 결정적 전역 상계가 아니다. 시간에 의존하는 traffic 관측이 자동으로 이 IID 가정을 충족하는 것도 아니다.

<a id="c16"></a>**C16. 제어 보장의 적용 범위.** CKLR의 recursive feasibility와 안정성은 terminal feedback·비용·영역, 초기 feasibility와 허용 예측오차 같은 제어 조건 아래의 결과다. kernel을 TabICL이나 RCTL로 교체하거나 cell partition에 적용해도 보장이 그대로 전이되지는 않는다.

<a id="c17"></a>**C17. CKLR 수치 예제의 정확도와 시간.** 200개 훈련·100개 test의 예제에서 CKLR의 군집별 최대 QCQP 시간은37.07초, 전체 데이터를 한 번에 맞춘 SLR의 해당 최적화시간은63.43초였다. Table1 R²는 CKLR .9880, SLR .9899, KI .9650, SPKI .9070, RBFNN .9950이다. 이 예제의 속도 이득과 예측 정확도 우월성은 같은 결론이 아니며, 최대 QCQP 시간과 전체 실행시간도 구분한다.

<a id="c18"></a>**C18. CSTR의 경험값과 보장값.** CSTR 예제는 K81, 추가 test300개, 최대 관측 오차 .0077을 보고하며 PKI·SPKI보다 정확했다고 설명한다. 저자는 어려운 Eq18을 직접 풀지 않고10000개 점의 Jacobian norm 최댓값1.1376을 추정 L로 썼다. 이는 전역 상계 인증과 다르다. 원 물리단위 상태 범위와 normalization 이후의 상태값도 구분해야 한다.

<a id="c19"></a>**C19. CSTR 비교에서 빠뜨리지 않을 한계.** CKLR은 이 예제에서 PKI/SPKI보다 느렸고, LEMPC는 같은 α의 EMPC보다 빠르게 수렴하지만 경제성능은 나쁘다고 보고한다. 40회 시뮬레이션의 최대 합산 최적화시간23.8887초가 sampling30초보다 작다는 관찰은 모든 운영환경의 보장이 아니다. 본문이 언급한 Table4 본체를 보존HTML과 확인PDF에서 찾지 못해 경제차이 수치는 미확인으로 남긴다.

## Mixture 이론의 적용 조건과 미해결 표기

<a id="c20"></a>**C20. Mixture 이론이 다루는 오차.** 2504.20651v1은 혼합분포에서 IID로 받은 표본과 정해진 함수군을 다룬다. §II의 bounded loss 일반화와 §III의 공통 f*·Gaussian noise 아래 경험 L2 추정오차를 구분한다. 혼합이라는 사실만으로 시간 상관을 처리하거나 MAE RCTL에 같은 결과를 주지는 않는다.

<a id="c21"></a>**C21. 한 표본 TV와 n표본 통계량.** Proposition II.1의 empirical Rademacher 통계량은 n개 표본에 의존하지만 Appendix A의 TV 단계에는 한 표본 분포의 γ가 등장한다. 읽은 증명에서 결합분포로 연결하는 추가 논증을 확인하지 못했으므로 같은 상수의 상계를 인증하지 않는다. 다른 증명 가능성이나 논문 전체를 부정하는 판단은 아니다.

<a id="c22"></a>**C22. γ 조건의 인쇄 지수 차이.** convex의 γ 조건은 Theorem III.7·Appendix에서 n^(−2/5)인데 요약·Remark III.9는 n^(−4/5)로 적는다. Hölder도 정리·Appendix의 n^(−α/(1+2α))와 요약·Remark의 n^(−2α/(1+2α))가 다르다. 위험률의 지수와 γ 조건을 혼용하지 않고 어느 표기가 맞는지 임의로 고치지 않는다.

<a id="c23"></a>**C23. 혼합 선형모형의 비교 대상.** §IV는 같은 isotropic Gaussian 입력과 잠재 선형계수·잡음 조건에서 혼합 최적계수 대비 초과위험을 분석한다. cell별 oracle 대비 통합의 정보 손실이나 RCTL 분리의 이득을 직접 계산한 값이 아니다. 상계의 추가 이질성 항만으로 모든 실제 오차가 더 커진다고 결론내리지 않는다.

<a id="c24"></a>**C24. Mixture 결과의 설계 사용 한계.** γ는 성분과 혼합분포 사이의 TV 반경이며 성분 쌍의 직경과 동일한 수치가 아니다. 함수군·표본 수·입력 분포·시간 의존성과 실제 추정 가능성을 확인하기 전에는 이론의 rate를 Tab 분위수와 결합해 병합 임계값으로 사용하지 않는다. PDF 전문 읽기는 모든 증명의 인증이나 실험 재현과 구분한다.

## 자료 보존·판본·검수 범위

<a id="c25"></a>**C25. 과거 독해와 이번 독해의 구분.** 당시 기록은 정상PDF2개40쪽 확보, 관련5쪽 시각 대조와 CKLR HTML의 지정 부분 독해였다. 이번 아카이브 작업에서는 보존PDF40쪽3574행과 HTML article1588행·TeX alttext457개를 읽고 PDF 새 렌더25쪽·기존 PNG5개를 확인했다. TXT3개는 원문과 기계적 대응을 확인한 파생본이므로 별도 전문 독해로 더하지 않는다.

<a id="c26"></a>**C26. 불완전 PDF와 별도 보완자료.** 기존 CKLR latest 요청 파일은1048576바이트이며 마지막1024바이트의 끝표식 부재와 PdfStreamError를 확인했다. 이를 정상 논문 수에 넣지 않았다. 별도 공식 고정v1 PDF는2026-10-11 UTC에7374073바이트·18쪽으로 수집했으며 원본을 대체하지 않았다. 이 보완PDF는 전체 이미지9쪽과 텍스트14–16쪽149행만 직접 읽었고 전체18쪽 전문 검수로 세지 않는다.

<a id="c27"></a>**C27. 수집·변환 코드의 정적 확인.** fetch 코드는 5MB를 넘으면 거부하며 PDF bytes를 저장한 뒤 PdfReader를 호출하므로 parse 실패 뒤 파일이 남을 수 있다. 기존1MB 실패의 원인을5MB 제한이라고 단정하지 않는다. finish 코드는 script/style을 제외한 HTML text를 평탄화하고5개 PNG 경로를 기록한다. 원 수집·변환·verify 코드는 읽기만 했으며 실행/import하지 않았다.

<a id="c28"></a>**C28. HTML 그림과 보존 경로.** 보존HTML은 PNG5개와 SVG object3개의 외부 그림 참조를 갖는다. 자체 첫 추출기의 img 목록에서 SVG3개가 빠졌던 점을 보정했다. 그림 bytes가 HTML에 내장돼 있다는 뜻은 아니며 별도 고정PDF에서8그림·표1–3을 확인했다. 두 저장PDF의 TXT와 기존PNG 대응도 독립 연구 증거로 중복 가산하지 않는다.

<a id="c29"></a>**C29. 스냅샷 보존과 수량.** snapshot32 manifest는25개 파일4766081바이트를 나열한다. manifest5439바이트를 포함하면26개4771520바이트이며 루트 archive 검증213바이트는 별도다. 새 원문14개를 그대로 보존하고 기존6개 사본·외부12개 metadata를 연결했다. 48개 원본 별칭·RCTL11개 동일해시 사본·보호 원본6개의 해시를 확인했다.

<a id="c30"></a>**C30. 후보표·진행기록 판본.** 원89 후보표47행에 원90의 함수 제약 판단 한 행이 추가되어48행이 됐다. 진행기록은 원90 최신상태 삽입과 원89 제목 변경으로478행에서488행이 됐다. 현재 판본은1–45행을 실제 읽었고46–488행은 대응 관계만 확인했으므로 이번 전체 독해로 올리지 않는다.

<a id="c31"></a>**C31. 과거 예산과 현재 작업 권한.** 당시 원장은 Tab context69/80, query39360/60000으로 잔여11context·20640행, RCTL fit29/29로 잔여0이었다. 과거 Goal·지시·예산은 연구 경과를 설명하는 자료이며 이번 정리의 실행 명령이 아니다. 이번 작업에서도 새 모델 실행은0이고 원 연구코드 실행/import는0이다.

<a id="c32"></a>**C32. 재검토 조건과 남은 일.** Tab의 직접 예측 이득은 유지하지만 그것을 유용한 RCTL 소속 변경의 증거로 바꾸지 않는다. 재검토에는 실제 운영 요구·관측 제약, 달라지는 정보나 학습 결정, 같은 group 정보를 받는 global 대안 대비 이득을 연결해야 한다. 원91 이후와 기존 고유 판본·문서 공백·통합 검수는 남아 있어 전체 Goal은 미완료다.

## 같은 안을 다시 제안할 때

| 제안 | 이미 확인한 범위 | 새로 필요한 근거 |
|---|---|---|
| Lipschitz penalty로 cell 분리 | 제약 함수의 두 점 하한 | 실제 운영 요구와 그 제약을 강제한 전체 모델 |
| stable LSTM을 그대로 적용 | 상태 수축·학습 근사의 조건 | convolution·BN·잔차·출력을 포함한 전체 영향 |
| CKLR의 clustering을 가져오기 | 입력표본 구역·kernel·제어 목적 | cell 소속에 해당하는 다른 결정과 실제 예측 이득 |
| mixture rate로 병합 임계값 정하기 | 함수군·IID·TV 조건과 표기 차이 | 정당한 추정량·시간 의존성·비교 대상 |

[판본 차이](../evidence/0120-prescribed-regularity/version-comparison.json) · [실제 읽기](../evidence/0120-prescribed-regularity/read-scopes.json) · [남은 범위](../evidence/0120-prescribed-regularity/packet-coverage.json)
