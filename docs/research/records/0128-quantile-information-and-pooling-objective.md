# 원98 — 중앙값 정보량과 공동 학습의 목적

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

같은 참 중앙값을 가진 cell도 유한한 자료로 학습하면 공유의 효과가 다를 수 있다. 독립 Uniform 기호 모형에서는 A의 추정 분산이 악화하면서 두 cell 평균의 **추정 초과 MAE**는 줄었다. 한 target을 보호하는 규칙과 모든 cell 평균 목적을 구분해야 한다. 이 결과는 실제 traffic 성능 개선이나 RCTL 보장이 아니다.

2026-09-26의 원98은 문헌·설치 TabICL2.2.0 코드·기호 계산을 확인한 기록이다. 밀도 기반 donor/병합안을 새 추천 방향으로 채택하지 않았고, 최종 방향/Word는 미완료였다. 좋은 Tab 직접 예측의 긍정 증거는 유지하지만 밀도 정확성이나 새 소속의 RCTL 성공으로 바꾸지 않는다.

[출처31그룹](../sources/history-128.md) · [32주장/위치](../verification/history-128-claims.json) · [작성 후 대조](../verification/history-128-second-pass.json) · [실제 판독](../evidence/0128-quantile-information-and-pooling-objective/read-scopes.json) · [분수·보존 감사](../evidence/0128-quantile-information-and-pooling-objective/numeric-check.json) · [문헌 비교](../references/quantile-information-and-grouping.md)

## 질문·방법·실제 수행 범위

원08의 독립/중복 sample, 원23–25의 이상적 MAE 공유 비용, 원28의 미래 잡음/함수 불확실성, 원38의 pooled OLS를 이어 중앙값 주변 밀도와 sample 수가 유한 추정에 미치는 역할을 검토했다. 원97은 저장 예측 재사용의 비용 진단이며 별도 실험 계보다. 실제 traffic 자료·시간 분할·context/query·feature/정규화·모델 가중치·K/소속·seed는 이번 기호 모형에 **해당 없음**이다. 논문의 이론 조건과 현재 RCTL의 실제 조건 연결은 **미확인**이다.

원PDF3편은178페이지4,270,133bytes지만 이번 실제 텍스트 판독은41페이지2351행과 관련6이미지다. 설치 코드477행은 이미 H122/H075에서 전부 읽었던 같은 SHA의 재독이다. 별도로 확보한 현재 Bai v1 비교는3페이지160행·2이미지이며 당시 다운로드가 아니다. 원 연구 script를 실행/import하지 않았고 새 모델 fit·forward·gradient0이다.

## 기호 계산의 결과와 반례

A~Uniform[9.5,10.5], B~Uniform[5,15], 중앙값10, 각 cell 독립 n개, 입력 없는 중앙값 추정, 동등 cell 비중이다. 아래 숫자는 분산/추정 초과 MAE에 n을 곱한 **점근적 주항**이다. 유한 n의 정확한 값·simulation·실측 지표가 아니다.

| 항 | 개별 추정 | 공동 추정 |
|---|---:|---:|
| A 중앙값 분산×n | 1/4 | 50/121 |
| B 중앙값 분산×n | 25 | 50/121 |
| 동등 cell 평균 추정 초과 MAE×n | 11/8 | 5/22 |

A의 분산 주항은65.289256% 증가한다. 평균 초과항의 비는20/121이지만 전체 MAE가 그 비율로 감소하는 것은 아니다. 현재 추가 산술에서 참 중앙값에 남는 동등 평균 MAE는 `(1/4+10/4)/2=11/8`이며, 같은 숫자의 개별 초과항 계수와 별개다. 원분수와 자체 Fraction 감사는 일치했다. [원JSON](../sources/history-128.md#src-0001876)·[확인 범위](../verification/history-128-second-pass.json)를 함께 본다.

독립 CDF의 분산을 쓰는 모형이므로 시간/cell 의존에서는 공분산을 고려해야 한다. 행 수 증가를 독립 정보 증가로 세지 않는다. 원척도 기호 값을 기존 정규화 Tab/RCTL 점수와 합치지 않는다.

## 문헌·구현과 적용 조건

[문헌 비교](../references/quantile-information-and-grouping.md)는 Bai target/source QR의 관계 대비·sample 수·잔차 밀도 선별, Gu 공통 slope 아래 절편 fusion/refit/IC, Yang slope 함수 grouping/원자료 refit를 구분한다. Bai의 이론식·one-shot·교대 추정과 v1/v2, Yang의 group 회복·group 수 선택·CLT 조건도 분리한다. 본문이나 일부 수식의 검토는 모든 증명/공식 구현 재현이 아니다.

설치 TabICL 코드는 spline의 `Δq/Δalpha`와 역도함수 관계로 밀도를 계산하며 tail·monotonicity 처리·수치 clamp를 포함한다. clamp가 작동하지 않는 양의 내부 구간에만 `f=Δalpha/Δq`를 바로 쓸 수 있다. 45%–55% 분위수 간격에서는 `0.1/간격`으로 구간 평균 농도를 계산한다. 한 점의 참 밀도/실제 calibration, RCTL 학습 분산 감소량으로 대입하지 않는다. raw_quantiles의 정적 반환 경로를 확인했으며 새로운 inference는 없다. [기존 코드 재사용 범위](../evidence/0128-quantile-information-and-pooling-objective/code-reuse.json).

## 당시 판단·재사용 자료·재검토 조건

밀도 추정기를 Tab으로 바꾸거나 donor 허용을 양방향 edge로 바꾸는 것만으로 공동 clustering의 실익·최적화·신규성을 확보하지 못했다는 당시 미추천 판단을 보존한다. 이론적 불가능성이나 실제 RCTL 성능 실패로 확대하지 않는다. 후속 검토는 실제 traffic의 pooling 문제, 유용한 다른 소속 또는 같은 유용한 결정의 효율, 강한 단순/global 대안, cell 목적/비중/손해, Tab 밀도 정확성과 learner 연결, 전체 비용에서 달라지는 근거를 먼저 적는다.

작은 내부 원문14개는 byte 그대로 보존하고 이전 원장·candidate·연혁3개는 같은 SHA의 팀 사본을 연결한다. 원 script는 `.py.txt`로 보존하며 실행하지 않는다. 외부 PDF/TXT/PNG와 코드2개는 metadata·정식 링크·판독 범위만 제공한다. 현재 환경에서의 재현 성공을 주장하지 않는다.

Snapshot40은 manifest에25파일6,248,743bytes를 열거한다. manifest6,259bytes를 포함한 실제 파일은26개6,255,002bytes이고 별도 root receipt440bytes는 분리한다. 과거 원장 SHA807600…와 Word SHA4f1112…는 불변이다. Word는 hash-only이며 본문/layout 확인 완료가 아니다. 당시 Tab 잔여11context/20,640행과 RCTL 추가fit0은 역사적 상태다.

## 판독·접근·전체 Goal의 한계

최초 원문은846행(core676+candidate86+progress84)이다. 작성 후 원문349행·기존 코드214행·원PDF19전체 텍스트 페이지와 Gu10페이지1–15행/총1248행, Bai16/Yang15 전체 이미지2개·현재 v1 비교9–10페이지135행을 별도로 대조했다. 수정한 주장의 저장본과8검수그룹도 실제 읽었다. 새로운 원문/이미지/실험 완료 수를 재독 때문에 늘리지 않는다.

현재 연혁85–563/이전76–554, 원PDF 나머지137페이지·전TXT 직접 판독/다른 시각 내용, 현재 v1 나머지50페이지는 미완료다. Xu Wiley는 당시 abstract-only 보고였고 현재 URL은 이 도구에서 접근되지 않았다. 과거 PMC 확인 화면과 현재 arXiv 원문 판독을 혼동하지 않으며 논문 전체가 불가능하다고 결론내리지 않는다.

원99 이후·이전 고유 판본/FedPPBC·DOCX 공백·전체 통합·장기 팀접근·최종 원본 변경분·대표 질문10개 이상 검색 검수도 남는다. 이 기록의 검수·GitHub 병합은 전체 Goal 완료가 아니다.

## 검수된 주장과 근거

<a id="claim-01"></a>

### H128-C01 문헌·정적 코드·기호 계산 기록

원98(2026-09-26)은 중앙값 주변 밀도와 sample 수가 공유 판단에 주는 영향을 문헌·설치 코드·기호 모형으로 검토했다. 실제 traffic 수치 실험이나 새 Tab/RCTL fit·forward·gradient는 없었다. 이번 아카이브도 기존 원문과 저장 분수의 확인이며 원 연구 코드 실행/import·새 모델 실행0이다.

근거: [SRC-0001872 행3–9](../sources/history-128.md#src-0001872) · [SRC-0001873 행1–11](../sources/history-128.md#src-0001873) · [SRC-0001874 행1–5](../sources/history-128.md#src-0001874) · [SRC-0001875 행90–102](../sources/history-128.md#src-0001875) · [SRC-0001880 행7–14](../sources/history-128.md#src-0001880); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-02"></a>

### H128-C02 이상적 MAE 공유 비용과 유한 자료 추정

참 조건부 중앙값이 같으면 이상적인 MAE 공유 비용이0일 수 있어도, 자료로 그 중앙값을 추정하는 어려움이0이라는 뜻은 아니다. 원08·23–25·28·38에서 논의한 자료 공유와 함수 추정의 차이를 중앙값 주변 밀도의 관점에서 구체화했다. 이상적 예측 관계의 일치와 유한 학습의 이득을 같은 판정으로 쓰지 않는다.

근거: [SRC-0001874 행7–9](../sources/history-128.md#src-0001874) · [SRC-0001873 행7–11](../sources/history-128.md#src-0001873) · [SRC-0001877 행7–9](../sources/history-128.md#src-0001877); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-03"></a>

### H128-C03 잡음 분포와 학습 불확실성의 역할

정답 분포의 폭을 함수 추정의 epistemic 불확실성과 동일시하지 않으면서, 그 분포가 유한 sample의 학습 효율에 영향을 줄 수 있다는 점도 보존한다. 미래 잡음이라는 이유만으로 밀도를 학습과 무관하다고 배제하거나, 좋은 Tab 직접 예측을 밀도 정확성·RCTL 학습 개선의 증거로 바꾸지 않는다.

근거: [SRC-0001873 행7–11](../sources/history-128.md#src-0001873) · [SRC-0001873 행54–60](../sources/history-128.md#src-0001873) · [SRC-0001877 행82–86](../sources/history-128.md#src-0001877) · [SRC-0001874 행22–25](../sources/history-128.md#src-0001874); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-04"></a>

### H128-C04 단일 target 보호와 전체 cell 평균

하나의 target에 손해인 donor가 모든 cell의 동등 가중 평균에는 이득일 수 있다. 한 target을 개선하는 transfer 규칙을 양방향으로 적용하거나 그래프 edge로 바꾸는 것만으로 공동 clustering 목적을 최적화했다고 할 수 없다. 개별 cell 보호가 필요한 경우 목적과 정규화·손실 비중을 별도로 명시한다.

근거: [SRC-0001872 행5–9](../sources/history-128.md#src-0001872) · [SRC-0001873 행21–23](../sources/history-128.md#src-0001873) · [SRC-0001873 행36–48](../sources/history-128.md#src-0001873) · [SRC-0001873 행56–60](../sources/history-128.md#src-0001873) · [SRC-0001883 PDF2,3쪽](../sources/history-128.md#src-0001883); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-05"></a>

### H128-C05 Bai v2의 선형 QR target와 source

Bai 등2411.19933v2는 고정 분위수τ에서 희소 target 계수β*를 추정하는 고차원 선형 QR이다. source 계수w^(k)와의 차이δ^(k)를 작은ℓ1 대비로 선별하고, 독립 source datasets를 둔다. 이 연구의 target 계수 목적과 전체 cell MAE·비선형 RCTL의 학습 목적은 구별한다.

근거: [SRC-0001883 PDF2,3,6쪽](../sources/history-128.md#src-0001883) · [SRC-0001873 행17–17](../sources/history-128.md#src-0001873); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-06"></a>

### H128-C06 v1과 v2 정보 조건의 실제 차이

현재 공식 v1 PDF10 식3은 E[f0]/E[fk]와 균형 sample 수의 단순화를 명시한다. 원문 v2 PDF8 식2는 n0·E[f0]/(nk·E[fk])를 사용한다. v1이 모든 손실·이론에서 sample 수를 무시했다고 확대하지 않는다. 이번 v1 PDF의 확보는 당시 로컬 다운로드 기록이 아니라 현재 판본 대조다.

근거: [SRC-0001874 행11–16](../sources/history-128.md#src-0001874) · [SRC-0001873 행21–21](../sources/history-128.md#src-0001873) · [SRC-0001883 PDF4,8,15,16쪽](../sources/history-128.md#src-0001883); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-07"></a>

### H128-C07 이론식·one-shot·교대 추정의 구별

v2 이론식3은 β와 source 대비δ를 함께 추정하는 희소 score 제약이다. 실용 Algorithm1은 초기 target/대비 추정과 두 선별집합의 교집합을 만든 뒤, 그 대비를 고정한 pooled QR을 푼다. Appendix Algorithm3은 알려진 source 집합에서 대비와β를 번갈아 갱신한다. 원문의 rate 연결 및 반복 설명을 보존하되 같은 최적화식으로 혼합하거나 공식 구현·모든 증명을 검증한 것으로 쓰지 않는다.

근거: [SRC-0001883 PDF8,9,15,16,17,39,40쪽](../sources/history-128.md#src-0001883) · [SRC-0001875 행27–39](../sources/history-128.md#src-0001875); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-08"></a>

### H128-C08 Bai의 밀도 추정은 잔차 주변 빈도다

v2 식7은 추정한 β+δ의 잔차가 bandwidth bk 안에 든 빈도를2bk·nk로 나누는 평균 잔차 밀도 추정이다. 전체 CDF를 직접 추정한 절차가 아니다. 선별에는 계수 차이와 sample 수를 함께 쓰며, 이 kernel 계산을 Tab의 미래값 분위수로 바꿀 때도 척도·조건·오차의 연결이 별도로 필요하다.

근거: [SRC-0001883 PDF14,15,16,40,41쪽](../sources/history-128.md#src-0001883) · [SRC-0001873 행17–23](../sources/history-128.md#src-0001873); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-09"></a>

### H128-C09 밀도 scalar와 회귀 정보 행렬의 범위

Bai의 조건은 밀도로 가중한 입력 행렬의 restricted eigenvalue, sub-Gaussian 설계, 밀도 정칙성과 source 분리 등을 포함한다. 단일 밀도 scalar만으로 회귀 방향의 정보나 임의 시계열의 유효 sample 수를 보장하지 않는다. theoretical error/detection 조건을 실제 RCTL 성능·clustering 이득으로 옮기지 않는다.

근거: [SRC-0001883 PDF10,11,13,16,17쪽](../sources/history-128.md#src-0001883) · [SRC-0001873 행17–19](../sources/history-128.md#src-0001873) · [SRC-0001873 행58–60](../sources/history-128.md#src-0001873); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-10"></a>

### H128-C10 Bai PDF7의 문장·식 방향과 경계

v2 PDF7의 target 밀도f0가 더 작다는 문장은 바로 뒤의 pooling 분산과 손해 부등식 방향에 맞지 않는다. 공통 Σx, 양의 밀도 아래 r=n1/n0,s=f1/f0이면 pooled/target 분산 주항 비는(1+r)/(1+rs)^2다. s<1/(sqrt(1+r)+1)에서 strict 손해이며 경계에서는 주항이 같다. 식과 직접 비교를 기준으로 해석하고 논문 전체의 무효나 RCTL 실패로 확대하지 않는다.

근거: [SRC-0001873 행72–73](../sources/history-128.md#src-0001873) · [SRC-0001875 행34–39](../sources/history-128.md#src-0001875) · [SRC-0001883 PDF6,7,8,12쪽](../sources/history-128.md#src-0001883); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-11"></a>

### H128-C11 Gu는 공통 기울기 아래 절편을 묶는다

Gu·Volgushev v2는 공통 β(τ)와 개별 절편α_i(τ)를 가진 panel QR에서 절편의 latent groups를 찾는다. group 수와 소속은 분위수τ에 따라 달라질 수 있다. 임의의 비선형 cell 함수 전체나 동일 미래 출력값을 묶는 모형과 같다고 쓰지 않는다.

근거: [SRC-0001887 PDF1,4,7쪽](../sources/history-128.md#src-0001887) · [SRC-0001873 행18–18](../sources/history-128.md#src-0001873); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-12"></a>

### H128-C12 Gu의 fusion·refit·정보기준

Gu는 초기 절편 차이의 역제곱을 가중한 fusion penalty로 후보 group을 만들고, 각 후보에서 실제 자료를 재추정한 pinball loss에 group 수 벌점을 더해 선택한다. 최종 추정을 초기 계수의 단순 평균이나 RCTL 모델 가중치 병합으로 해석하지 않는다.

근거: [SRC-0001887 PDF4,5,6,10쪽](../sources/history-128.md#src-0001887) · [SRC-0001873 행18–18](../sources/history-128.md#src-0001873); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-13"></a>

### H128-C13 Gu의 역밀도·독립성·pointwise 조건

Gu의 sparsity ŝ는 초기 fit의 pooled residual 경험 분위수 폭으로 계산하고, 공통 잔차 밀도 단순화 아래 역밀도에 대응한다. 일반적인 inverse-density 합과 이 단순화를 구분한다. 본문은 개체 내부 i.i.d./개체 간 독립, bounded design·양의 밀도·group separation을 두며 pointwise 결과의 범위도 밝힌다. 겹치는 traffic lag나 거의 붙은 모든 group에 보장을 자동 적용하지 않는다.

근거: [SRC-0001887 PDF4,5,6,7,8,9,10쪽](../sources/history-128.md#src-0001887) · [SRC-0001873 행18–18](../sources/history-128.md#src-0001873); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-14"></a>

### H128-C14 Yang은 slope 함수와 개별 효과를 구분한다

Yang 등 v1은 조건Z에 따른 slope 함수β_i(Z)를 묶으며 개별 효과α_i는 같은 group에서도 다를 수 있다. 관측한Z에서 계수 함수의 Euclidean 차이를 평균해 complete linkage로 묶는다. group 수 선택용 초기 함수 평균과 최종 실제 sample을 사용한 post-grouping QR을 구분한다.

근거: [SRC-0001891 PDF6,7,8,9,10,11쪽](../sources/history-128.md#src-0001891) · [SRC-0001873 행19–19](../sources/history-128.md#src-0001873); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-15"></a>

### H128-C15 Yang의 group 회복·group 수·CLT 조건

Yang의 known-R group 회복은 Assumptions1–4 아래이며 별도의 cross-sectional 독립 제약을 요구하지 않는다. unknown-R 선택에는5가 추가되고 post-grouping CLT에는1–7 및 joint mixing·covariance/group 크기 조건이 필요하다. 같은 조건 세트로 뭉뚱그리거나 모든 공통 충격을 배제하는 논문으로 읽지 않는다.

근거: [SRC-0001891 PDF12,13,14,15,16,17쪽](../sources/history-128.md#src-0001891) · [SRC-0001875 행60–69](../sources/history-128.md#src-0001875); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-16"></a>

### H128-C16 Yang의 시간 변형과 재학습 범위

Yang은 smooth한 scaled time t/T나 개별Z_it 모형 변형도 명시한다. 이는 임의 급변·비정상 traffic 전체의 보장이 아니다. clustering 후 원자료의 공동 추정으로 함수 수를 줄이는 구조와, N개의 서로 다른 입력·관측을 계산하지 않아도 된다는 비용 주장은 구분한다.

근거: [SRC-0001891 PDF6,7,8,11,12,14,17쪽](../sources/history-128.md#src-0001891) · [SRC-0001873 행19–19](../sources/history-128.md#src-0001873) · [SRC-0001873 행64–68](../sources/history-128.md#src-0001873); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-17"></a>

### H128-C17 직접 기호 모형의 가정과 단위

기호 모형은 입력 없이 중앙값10 하나를 추정하는 두 독립 Uniform[9.5,10.5]/Uniform[5,15] 집단과 cell당 n개 sample이다. 중앙값 밀도는1/0.1, cell loss는 동일 비중이다. 실제 traffic·특징·시간 분할·학습 가중치·seed의 실험이 아니다. 저장 계수는 n을 곱한 점근적 주항이며 유한 n의 정확한 값으로 쓰지 않는다.

근거: [SRC-0001873 행25–29](../sources/history-128.md#src-0001873) · [SRC-0001876 JSON선택5필드](../sources/history-128.md#src-0001876); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-18"></a>

### H128-C18 각자·공동 중앙값 분산의 계수

개별 중앙값 분산의 n 배 계수는 A=1/4, B=25이고, 공동 추정은 양쪽에50/121≈0.413223이다. 공통 중앙값에서 두 경험 CDF의 분산과 혼합 CDF 기울기를 사용한 결과다. 이번 자체 Fraction 계산에서 저장된 계수와 정확히 일치했지만 독립 simulation·model 재현으로 집계하지 않는다.

근거: [SRC-0001873 행29–44](../sources/history-128.md#src-0001873) · [SRC-0001882 행29–48](../sources/history-128.md#src-0001882) · [SRC-0001876 JSON선택3필드](../sources/history-128.md#src-0001876); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-19"></a>

### H128-C19 A의 손해와 B의 추정 안정화

공동 추정의 분산 주항은 A의1/4보다 커져65.289256% 증가하고 B의25보다 작다. 이 수치는 추정 분산에 관한 것이며 A의 전체 MAE가 같은 비율로 악화했다는 실제 성능 결과가 아니다. 한쪽의 손해만으로 전체 cell 공유의 손해를 확정하지 않는다.

근거: [SRC-0001873 행31–46](../sources/history-128.md#src-0001873) · [SRC-0001876 JSON선택4필드](../sources/history-128.md#src-0001876); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-20"></a>

### H128-C20 전체 평균 초과 MAE 주항의 비교

중앙값 주변에서 population MAE의 증가가 밀도×δ²라는 관계를 이용하면, 동등 cell 평균 추정 초과 MAE의 n 배 계수는 개별11/8에서 공동5/22로 줄고 비는20/121이다. 이 비교는 추정 오차의 주항이며 전체 MAE 감소율·현재 traffic의 clustering 개선률로 쓰지 않는다.

근거: [SRC-0001873 행36–44](../sources/history-128.md#src-0001873) · [SRC-0001876 JSON선택3필드](../sources/history-128.md#src-0001876); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-21"></a>

### H128-C21 불가피한 MAE와 목표·척도를 보존한다

이번 정리의 추가 산술 확인에서 Uniform 두 집단의 참 중앙값에 남는 동등 cell 평균 MAE는11/8이다. 원98의 추정 초과항과 별도이며 숫자가 같은 개별 초과항 계수11/8과 혼합하지 않는다. cell 보호·동등 평균·정규화/가중치를 먼저 구별하며 기호 모형의 원척도 결과를 기존 정규화 RCTL/Tab 점수와 합치지 않는다.

근거: [SRC-0001873 행38–48](../sources/history-128.md#src-0001873) · [SRC-0001873 행58–60](../sources/history-128.md#src-0001873) · [SRC-0001876 JSON선택2필드](../sources/history-128.md#src-0001876); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-22"></a>

### H128-C22 독립 sample 수와 공분산의 차이

기호 CDF 분산은 독립 sample을 가정한다. 시간·cell 의존이 있으면 경험 CDF의 분산에 공분산 항이 더해지므로 행 수 증가를 독립 정보 증가로 계산하지 않는다. 이 기록은 그 의존성을 보정하는 새 알고리즘이나 실제 유효 sample 수를 검증한 결과가 아니다.

근거: [SRC-0001873 행42–48](../sources/history-128.md#src-0001873) · [SRC-0001874 행23–25](../sources/history-128.md#src-0001874) · [SRC-0001887 PDF4쪽](../sources/history-128.md#src-0001887) · [SRC-0001891 PDF12,14,15쪽](../sources/history-128.md#src-0001891); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-23"></a>

### H128-C23 Tab 밀도 구현의 Δalpha와 수치 처리

설치된 TabICL2.2.0의 quantile distribution은 분위수 사이 선형 spline 기울기를 구하고 log_prob/pdf에서 그 역수 관계를 사용한다. 양의 비퇴화·clamp가 작동하지 않는 내부 구간의 밀도는 Δalpha/Δq이며 확률 차이를 생략하지 않는다. monotonicity 처리·tail·수치 clamp가 있는 구현을 모든 입력의 참 밀도나 실제 calibration 보장으로 강화하지 않는다.

근거: [SRC-0001873 행50–54](../sources/history-128.md#src-0001873) · [SRC-0047550 행544–601](../sources/history-128.md#src-0047550) · [SRC-0047550 행953–983](../sources/history-128.md#src-0047550) · [SRC-0047550 행1031–1102](../sources/history-128.md#src-0047550); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-24"></a>

### H128-C24 Raw quantiles와 구간 평균 농도

regressor.predict는 raw_quantiles 전달·반환 경로를 갖고 원척도로 inverse transform한 뒤 ensemble 평균을 반환한다. 45%–55% 분위수의0.1/간격은 해당 구간 평균 농도 계산이며 한 점의 참 밀도를 직접 관측한 값이 아니다. 이번 확인은 정적 코드 재독이고 새 inference를 호출하지 않았다.

근거: [SRC-0001873 행52–54](../sources/history-128.md#src-0001873) · [SRC-0047573 행621–668](../sources/history-128.md#src-0047573) · [SRC-0047573 행710–760](../sources/history-128.md#src-0047573) · [SRC-0047550 행579–601](../sources/history-128.md#src-0047550); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-25"></a>

### H128-C25 좋은 점 예측과 밀도 정확성

좋은 mean·median 예측은 중앙값 주변 기울기의 정확성을 보장하지 않는다. 좁은 분위수 간격의 작은 오차도 밀도 값을 크게 바꿀 수 있다. 기존 Tab 직접 예측의 긍정 결과를 유지하면서 밀도 검증이나 새로운 소속의 RCTL 개선으로 바꾸어 재인용하지 않는다.

근거: [SRC-0001872 행17–19](../sources/history-128.md#src-0001872) · [SRC-0001873 행54–60](../sources/history-128.md#src-0001873) · [SRC-0001877 행34–40](../sources/history-128.md#src-0001877) · [SRC-0001877 행82–86](../sources/history-128.md#src-0001877); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-26"></a>

### H128-C26 밀도만으로 RCTL의 학습 정보를 알 수 없다

입력 없는 중앙값 추정에서의 밀도 효과와, 회귀의 입력 방향·밀도 가중 정보 행렬, 비선형 RCTL의 표현/미분 방향·gradient 의존을 구분한다. Tab 밀도 scalar를 RCTL 분산 감소량이나 pooling 이득으로 바로 대입하지 않는다. 실제 learner의 정보와 목적을 연결한 직접 근거는 이 기록에서 미확인이다.

근거: [SRC-0001873 행56–60](../sources/history-128.md#src-0001873) · [SRC-0001883 PDF10쪽](../sources/history-128.md#src-0001883) · [SRC-0001891 PDF11,14,16쪽](../sources/history-128.md#src-0001891); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-27"></a>

### H128-C27 미추천과 다시 검토할 조건

당시 밀도 기반 donor/병합안은 새 추천 방향으로 채택하지 않았다. 이미 알려진 선별·group 복잡도 조절에 추정기만 바꾸는 것으로 실익을 확보하지 못했다는 판단이다. 같은 원리 전체의 불가능성이나 실제 RCTL 성능 실패로 확대하지 않는다. 실제 문제, 다른 유용한 소속 결정 또는 같은 유용한 결정의 효율, strong global 대안과 전체 비용의 차이를 새로 특정해야 한다.

근거: [SRC-0001873 행62–68](../sources/history-128.md#src-0001873) · [SRC-0001877 행44–58](../sources/history-128.md#src-0001877) · [SRC-0001877 행80–86](../sources/history-128.md#src-0001877) · [SRC-0001872 행19–19](../sources/history-128.md#src-0001872); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-28"></a>

### H128-C28 과거 예산과 현재 아카이브 실행 범위

원98의 누적 원장 SHA807600…는 원97 이후와 같은 바이트이며 추가 모델 사용·예산 reset을 기록하지 않았다. 원문이 적은 Tab 잔여11context/20,640행·RCTL 추가fit0은 당시 상태다. 이번 정리는 원장/중간 Word를 바꾸지 않았고 과거 fit 상한을 미래 팀 연구 전체의 실행 규칙으로 옮기지 않는다.

근거: [SRC-0001874 행3–5](../sources/history-128.md#src-0001874) · [SRC-0001873 행75–77](../sources/history-128.md#src-0001873) · [SRC-0001875 행93–102](../sources/history-128.md#src-0001875) · [SRC-0001880 행9–14](../sources/history-128.md#src-0001880) · [SRC-0001871 행141–145](../sources/history-128.md#src-0001871) · [SRC-0022106 행6–10](../sources/history-128.md#src-0022106); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-29"></a>

### H128-C29 문헌 확인·접근·판본의 범위

당시 PDF3편178페이지와 관련6이미지를 확보한 기록, 지금 원PDF41페이지/2351텍스트행을 읽은 범위, 별도로 확보한 v1 비교를 구분한다. Xu 논문은 당시 abstract-only로 보고됐고 현재 Wiley URL 요청은 이 도구에서 접근되지 않았다. 과거 PMC 확인 화면과 현재 arXiv 원문 읽기를 구분하며 모든 논문 증명·공식 코드의 검증/재현을 완료 처리하지 않는다.

근거: [SRC-0001873 행70–77](../sources/history-128.md#src-0001873) · [SRC-0001875 행22–79](../sources/history-128.md#src-0001875) · [SRC-0001895 행1–32](../sources/history-128.md#src-0001895) · [SRC-0001896 행1–32](../sources/history-128.md#src-0001896); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-30"></a>

### H128-C30 Snapshot40·receipt·Word hash-only

Snapshot40 manifest는25파일6,248,743bytes를 열거하고 manifest6,259bytes를 더한 실제 파일은26개6,255,002bytes다. 별도 root receipt440bytes와 원장/Word hash를 대조했다. Word SHA4f1112…의 불변은 문서 본문·layout 판독 완료가 아니다.

근거: [SRC-0001871 행1–145](../sources/history-128.md#src-0001871) · [SRC-0001882 행141–164](../sources/history-128.md#src-0001882) · [SRC-0022106 행1–10](../sources/history-128.md#src-0022106); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-31"></a>

### H128-C31 이전 코드·사본·TXT 대응의 집계

quantile_dist/regressor 두SHA는 이전 H122/H075 전체 판독과 동일하며 이번 관련477행 재독에 새 본문/선택 완료를 가산하지 않는다. 원TXT3은 CRLF 때문에 raw 바이트 재구성 비교가 달랐지만 개행 정규화 후 모든 PDF페이지 내용과 구간이 정확히 대응했다. 기계 대응·파생PNG/TXT·현재 v1·별칭을 독립 내용이나 전TXT 판독으로 세지 않는다.

근거: [SRC-0001871 행131–139](../sources/history-128.md#src-0001871) · [SRC-0001875 행80–92](../sources/history-128.md#src-0001875) · [SRC-0001879 행25–30](../sources/history-128.md#src-0001879) · [SRC-0001881 행12–20](../sources/history-128.md#src-0001881) · [SRC-0047550 행579–601](../sources/history-128.md#src-0047550) · [SRC-0047573 행737–765](../sources/history-128.md#src-0047573); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

<a id="claim-32"></a>

### H128-C32 실제 읽은 구간과 전체 Goal의 남은 범위

첫 판독은 새 원문846행(core676+candidate86+progress84), 원PDF41페이지/2351행·관련6이미지, 기존 코드477재독행과 현재 v1의3페이지/160행·2이미지다. current progress85–563/이전76–554, 원PDF 나머지137페이지·v1나머지50페이지·전TXT의 직접 판독·다른 시각 내용은 미완료다. 원99 이후·이전 고유 판본/FedPPBC·DOCX·전체 통합/장기 팀 접근/최종 변경분/대표 질문 검수까지 계속 남으며 원98의 검수·병합을 전체 Goal 완료로 표시하지 않는다.

근거: [SRC-0001877 행80–86](../sources/history-128.md#src-0001877) · [SRC-0001880 행7–14](../sources/history-128.md#src-0001880) · [SRC-0001873 행70–77](../sources/history-128.md#src-0001873); 추가 산술·현재 판본과 상세 위치는 [주장 목록](../verification/history-128-claims.json) 참조.

후속 [원99](0129-learning-units-and-clustering-cost.md)는 원98의 target/전체평균 구분을 다른 예측 단위와 비용 구조에 연결했다. 새로운 밀도/Tab/RCTL 실험 없이 문헌·정적코드·정수 계산을 대조했다.
