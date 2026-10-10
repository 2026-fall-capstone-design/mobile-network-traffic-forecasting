# 72 — Globalization 논문의 학습 기반 군집화와 성능 주장 대조

이 논문은 모형에 따라 공유할 자료의 단위가 달라질 수 있다는 선행 근거다. 그러나 학습한 계수·중요도로 소속을 정하므로, 이를 그대로 적용해 **RCTL과 독립적인 cell 소속을 발견했다**고 말할 수는 없다. 평균 개선도 모든 지역·월·지표의 개선을 뜻하지 않는다.

[72–75의 당시 판단과 실제 실행](0072-0075-output-compression.md) · [출처·판본](../sources/history-071.md) · [표와 소속 전사](../evidence/0072-globalization/tables-membership.json) · [피크 그림 전사](../evidence/0072-globalization/figures.json) · [검수](../verification/history-071.md)

## 질문과 당시 판단

<a id="c01"></a>**C01.** 원72는 예측기의 학습 구조를 이용한 군집화가 현재의 독립 소속 조건에 맞는지 확인하려 했다. 당시 판단은 Algorithm 1의 학습 계수 의존, Algorithm 2의 sample 단위, 거리행렬 비용, 예보 입력 가정, 서로 다른 tree 수를 검토한 뒤 곧바로 채택하지 않는 것이었다. 이번 검토도 새로운 소속이나 성능 실험을 실행하지 않았다. [당시 findings 전체](../evidence/0072-0075-output-compression/originals/SRC-0022023.md.txt)

<a id="c02"></a>**C02.** 당시 문서의 부분 독해 범위와 이번 아카이브의 추가 독해를 구분한다. 원72는 HTML §3–4·5.2–5.5, 방법·표와 PDF 16·18·35·42쪽 렌더를 기록했다. H071은 정상 PDF 65쪽의 본문·시각 자료를 읽고 표·수식·부록·서지·세부 그림을 대조했다. 이를 2026-09-26 당시 이미 전부 읽었다는 뜻으로 소급하지 않는다.

<a id="c03"></a>**C03.** 대상은 Ahmadi·Zareipour·Leung의 *Globalization for Scalable Short-term Load Forecasting*, [arXiv:2507.11729v1](https://arxiv.org/abs/2507.11729v1)이다. v1 제출일은 2025-07-15, 저장 PDF 첫 본문 하단에는 2025-07-17이 인쇄돼 있다. arXiv의 “63 pages” 표기와 실제 파일 65쪽은 별도로 기록한다. 이 문서의 페이지는 표지류를 포함한 **PDF 파일 페이지**다. 정식 저널 출판일로 추정하지 않는다.

## 데이터·예측 시점·입력

<a id="c04"></a>**C04.** 주 자료는 AESO의 Alberta 전력 부하이며 42개 area, 6개 planning region, 시간별 MW다. 본문은 2011년 1월–2023년 10월이라고 적는다(PDF18). 지역·전체 합계 AIL은 송전 손실을 제외한다(PDF21). 통신 cell·Milan 자료의 결과가 아니다.

<a id="c05"></a>**C05.** 결정적 1시간 후 예측에서 train 2011–2021, validation 2022, test 2023으로 나눈 뒤 정규화·sample 구성을 했다고 설명한다. Optuna 수백 회 탐색 후 2011–2022를 합쳐 다시 학습한다(PDF19–20). 정확한 trial 목록, seed, 모든 scaler 설정·적합 표본, 원예측·실행 로그는 이 저장 논문만으로 확보되지 않는다. 이는 저자의 실행 보고이며 이번 작업의 재현 결과가 아니다.

<a id="c06"></a>**C06.** 168시간 창, lag 1·24·48·…·168 및 제곱·세제곱, 이동평균 3·12·24·72·168, EMA168, 날씨, 달력·주기 인코딩·공휴일·상호작용을 사용한다. COVID flag는 2020-05-01–2022-12-31, 외생 변수에는 pool price·일별 WTI의 forward fill·시간별 BTC·발전원별 outage·LSSI 등이 들어간다(PDF32–33). 정확한 feature 전체 배열은 미확보다.

<a id="c07"></a>**C07.** 목표 시각 t+1의 날씨·시장 입력에는 예측 시점에 hour-ahead forecast를 구할 수 있다고 **가정**한다. 실제 발행 시각·forecast vintage를 확인한 결과는 제시되지 않는다. `입력 시각 ≤ 목표 시각`과 `입수 가능 시각 ≤ 예측 시작 시각`은 다르다. 따라서 이 서술만으로 운영 환경의 정보 누출 방지나 Milan에서의 동일 입력 가용성을 확정하지 않는다. [§5.2](https://arxiv.org/html/2507.11729v1#S5.SS2)

## 무엇을 공유하고 무엇을 군집화하는가

<a id="c08"></a>**C08.** local은 series별 학습, global은 여러 series에서 만든 학습 행을 모아 하나의 함수를 학습하는 구조다. pooled global이라는 이유로 모든 area를 동시에 입력하는 다변량 모델이나 인과적 상호작용 모델이 되지는 않는다(PDF5·11–13). 전역 중요도 그림도 local 계수의 산술 평균으로 전역 모델을 만든다는 구현 증거가 아니다.

<a id="c09"></a>**C09.** Algorithm 1은 각 series의 local model을 먼저 적합하고 계수 벡터를 구한 뒤 K-means로 series를 묶고, 군집마다 pooled global model을 다시 적합한다(PDF16, 식7–8). 소속 계산에 학습된 예측기의 정보가 들어간다. 최종 RCTL의 계수로 이를 수행하면 연구에서 요구한 RCTL 독립 소속과 충돌한다. [Algorithm 1](https://arxiv.org/html/2507.11729v1#alg1)

<a id="c10"></a>**C10.** Fig11의 표시 소속은 세 모델 모두 K=5지만 같지 않다. 군집0–4의 크기는 Ridge `17/9/2/12/2`, LightGBM `10/3/6/7/16`, XGBoost `5/10/10/16/1`이다. 총126개 area 라벨을 전사하고 각 모델에서 동일한42지역이 한 번씩 등장함을 확인했다. 이 소속은 전력 지역의 저자 결과이며 연구실의 UPC cell 소속이 아니다. K 선정 기준·seed는 확인되지 않는다.

<a id="c11"></a>**C11.** Algorithm 2는 먼저 pooled global model을 학습하고 feature 중요도 θ로 sample 간 거리를 가중해 군집화한 다음 군집별 모델을 적합한다. 식10은 `sqrt(sum_r θ_r (x_i,r − x_j,r)^2)`, 거리행렬은 **M×M**, M은 pooled sample 수다(PDF17–18). 시간축이 포함된 sample 군집을 cell 군집으로 옮기려면 별도의 정의가 필요하다. 셀 수가 작아도 이 행렬의 계산·메모리가 작다는 보장은 없다. [Algorithm 2](https://arxiv.org/html/2507.11729v1#alg2)

<a id="c12"></a>**C12.** 식10의 가중치 부호·정규화, Ridge의 signed 계수를 어떤 비음수 중요도로 바꾸는지, 새 query의 군집 배정 절차, instance clustering의 세부 알고리즘·K 선택은 저장 본문·의사코드에서 충분히 특정되지 않는다. PDF43의 instance 중요도라는 설명을 학습 loss의 sample weight 구현으로 확장하지 않는다. 실제 코드·거리행렬·시간·메모리 측정값은 미확보다.

<a id="c13"></a>**C13.** tree 계열의 local은 200 estimators, global은1000이며 최대 깊이4·leaves32, 기본 learning rate·booster가 좋은 설정이었다고 적는다. Ridge α=1도 보고한다(PDF20). 자료 공유와 모형 용량이 함께 달라지므로 pooling의 효과만 분리한 동일 계산량 비교로 읽지 않는다. Fig1의 Ridge 계수·XGBoost 중요도·LightGBM 중요도는 척도도 다르다.

<a id="c14"></a>**C14.** feature-transformer와 target-transformer는 저자의 해석 틀이다. 선형·신경망과 tree·최근접 이웃을 묶는 설명을 모든 알고리즘의 외삽 가능성에 관한 증명으로 취급하지 않는다. 특히 boosting ensemble과 단일 tree의 출력 범위를 동일한 보편 성질로 확대하거나 TabICLv2의 공유 효과를 이 분류만으로 결론내리지 않는다(PDF4–10·15·27·36).

## 평균 오차와 반례

<a id="c15"></a>**C15.** 표의 nMAE(%)는 area별 MAE를 정규화된 ground truth의 최댓값으로 나눈 비율이다. MSE·MAPE·FB를 별도로 보고한다. 표의 min/mean/max는 area별 지표를 요약한 값이지 시간별 오차 분포의 분위수가 아니다. FB의 부호·절댓값, nMAE의 비율과 %를 섞지 않는다. 원시 MW 오차나 통신 자료의 정규화 MAE와 직접 비교할 수 없다(PDF21, Table1·3·4·A5 캡션).

<a id="c16"></a>**C16.** Table1·3의 평균 nMAE(%)는 다음과 같다. model cluster는 series 단위, instance 두 열은 sample 단위다.

| 예측기 | local | global | model cluster | instance | weighted instance |
|---|---:|---:|---:|---:|---:|
| Ridge | 2.1417 | 2.1925 | 2.1509 | 2.1856 | 2.1925 |
| XGBoost | 2.3524 | 2.2837 | 2.2605 | 2.2659 | 2.2305 |
| LightGBM | 2.3538 | 2.2764 | 2.2685 | 2.2427 | 2.2243 |

Ridge model cluster는 global보다 낮지만 local보다 높다. 두 tree의 가중 instance는 각각의 global보다 낮지만 Ridge global보다 낮지는 않다. [Table1](https://arxiv.org/html/2507.11729v1#S5.T1) · [Table3](https://arxiv.org/html/2507.11729v1#S5.T3)

<a id="c17"></a>**C17.** Table1에서 XGBoost의 local→global 평균 MAPE는 `12.8588→13.1145`, 최대는 `149.9138→253.532`로 악화된다. LightGBM은 평균 `12.7966→11.5732`가 좋아져도 최대 `148.0044→196.498`은 나빠진다. 평균 nMAE 감소를 모든 지표·모든 지역의 개선으로 옮기지 않는다. Fig9에서도 area17의 tree global nMAE는 local보다 높다.

<a id="c18"></a>**C18.** 본문·표의 불일치를 보존한다. Ridge local 평균 FB는 PDF34 본문 `0.0004`, Table1 `0.0005`다. local 최소 MSE는 XGBoost `1.074e-05`가 LightGBM `1.133e-05`보다 작지만 표에서는 후자가 강조된다. PDF39의 LightGBM model cluster 평균 nMAE 악화 설명과 달리 Table1은 `2.2764→2.2685`다. 다만 그 평균 MSE는 `0.0009→0.0010`으로 실제 악화하므로 지표별로 읽어야 한다.

<a id="c19"></a>**C19.** Table2는 안정 지역/드리프트 지역의 local→global nMAE 변화율을 Ridge `−2.5917/−2.1540`, XGBoost `4.7362/0.4432`, LightGBM `4.8692/2.0948`%로 보고한다. 표의 원평균은 소수2자리, 변화율은4자리다. 반올림된 평균만으로 마지막 자리까지 재현할 수 없다는 점을 산술 오류로 처리하지 않는다. 지역 집합의 정확한 분류·원지표·반복 실행 분산은 미확보다(PDF41).

<a id="c20"></a>**C20.** Table3에서 Ridge weighted instance의 nMAE min/mean/max는 global과 동일하지만 평균 MSE는 `0.0008→0.0009`다. LightGBM global/instance/weighted의 평균 MSE는 `0.0009/0.0010/0.0010`, 최대는 `0.0066/0.0066/0.0073`이다. 가중화가 두 tree의 MSE를 전반적으로 개선한다는 본문 설명을 모든 요약값에 적용할 수 없다(PDF42–43).

<a id="c21"></a>**C21.** 같은 global 비교의 표시값도 완전히 통일돼 있지 않다. XGBoost 최대 MAPE는 Table1 `253.532`, Table3 `253.528`이다. Fig9의 LightGBM global 최대 막대는 area26 `6.38%`지만 Table1·3 최대는 `6.3967%`다. Fig9 평균 legend는 `2.27%`, 표 평균은 `2.2764%`다. 원표·그림 값을 각각 보존하며 한쪽에 맞춰 수정하지 않는다. FB는 표마다 표시 정밀도도 다르다.

## 집계 수준과 피크 예측

<a id="c22"></a>**C22.** zero-shot 실험은 area 수준에서 학습한 모델을 region·system 수준에 적용한 평가다. 계층 예측의 합계 일치를 강제하거나 reconciliation을 수행한 결과와는 구분한다. 저자는 coherence를 향후 과제로 남긴다(PDF44–45·52). 미래 시점 전체를 관측 없이 예측하는 의미의 zero-shot으로도 확대하지 않는다.

<a id="c23"></a>**C23.** Table4에서 Calgary·Edmonton·Northwest의 nMAE는 XGBoost가 Ridge보다 낮다. 반대로 Northeast nMAE는 Ridge `2.0342`가 XGBoost `2.1725`보다 낮지만 XGBoost 값이 강조된다. system MAPE도 Ridge `3.3711`보다 높은 XGBoost `3.5236`이 강조된다. 모델의 우위를 굵은 글씨만 보고 정하지 않는다(PDF45).

<a id="c24"></a>**C24.** Figs12–17의 월별5방법 평균120개를 전사했다. Ridge global의 표시 평균 오차는 local보다 **2·4·5·6·7·8·9·10·11월에 높다**. model cluster도 8·9월에는 local보다 높다. LightGBM global은12개월 모두 local보다 낮지만, weighted instance가5방법 중 단독 최소인 달은1·3·4·12월이다. PDF45의 모든 달에서 global이 우월하다는 서술을 Ridge에도 일괄 적용하지 않는다.

<a id="c25"></a>**C25.** Figs18–19의 연간 평균은 아래와 같다. 42지역×5방법×2모델의 signed 막대420개를 따로 전사해, 부호 있는 평균과 절댓값 평균을 구분했다. 캡션의10개 평균은 인쇄값의 **단순 절댓값 평균과 소수2자리 반올림 오차 범위에서 양립**하며 signed 평균과는 맞지 않는다. 막대와 캡션이 각각 반올림되었다고 보면 두 값 차이의 허용 폭은0.01이다. 예를 들어 LightGBM global의 인쇄 막대 절댓값 평균은 약2.85429, 캡션은2.86이므로 단순히 인쇄 막대를 평균해 반올림한 값이 모두 정확히 일치한다는 뜻은 아니다. 저자의 원예측·집계 코드를 재현한 것은 아니다.

| 예측기 | local | global | model cluster | instance | weighted instance |
|---|---:|---:|---:|---:|---:|
| Ridge | 2.47 | 2.12 | 1.75 | 1.99 | 2.26 |
| LightGBM | 4.88 | 2.86 | 2.98 | 2.87 | 2.78 |

LightGBM weighted의 `2.78`은 Ridge model cluster의 `1.75`보다 높다. PDF52의 다른 Ridge 군집 방법보다도 낫다는 문장은 이 수치로 지지되지 않는다.

<a id="c26"></a>**C26.** 연간 평균 개선에도 지역별 예외가 있다. Ridge area6은 local `0.03`에서 global `4.02`, area4는 `5.39`에서 `−9.07`로 절댓값 오차가 커진다. LightGBM area24도 local `8.15`에서 global `10.09`로 커진다. 음수는 개선을 뜻하지 않으며 피크 오차의 방향과 크기를 나누어 읽는다. 이 값은 그림에 인쇄된 %다.

<a id="c27"></a>**C27.** 피크 그림은 실제 피크 대비 %라고 정의하지만, 예측 곡선 최댓값과 실제 최댓값의 차이인지 실제 피크 시각의 예측 오차인지 계산식이 충분히 특정되지 않는다. 월·연간 집계 결과를 월·연 단위 선행 예측, 피크 발생 시각 탐지, 임계값 이벤트 성능으로 바꾸지 않는다. 11·12월 그림 및8000시간 이상 예측 축과 본문의 데이터 종료2023-10 사이에도 기간 확인이 필요하다. 일부 월별 막대 라벨은 그림 경계에서 잘리거나 겹치며, 그 값을 높이로 추정해 복원하지 않았다.

<a id="c28"></a>**C28.** Fig8·10은 area17·19·24·29·30·57의 actual/forecast 오버레이다. 저자는 1-step 예측이 최근값을 따라가는 경향을 해석하지만, 이것을 naive baseline과의 별도 손실 검정이나 장기 horizon 실험으로 취급하지 않는다. 장기·확률 예측, 적대적 잡음·결측 강건성은 후속 과제다(PDF36–40·43·52–54).

## 데이터 분석·부록을 해석할 때 남는 경계

<a id="c29"></a>**C29.** Fig4(a)의 보라색 월별 중심선은5월, (f)의 mean 곡선은spring에서 가장 낮게 보이지만 본문은 July/August와summer를 최저로 설명한다. 일자13·14의 봉우리는 특히max 곡선에서 보이며 median·mean과 구분해야 한다. 연도mean의2021 추가 하락도 일괄 회복 설명과 다르다. PDF28은 area33을 Northeast와Central 양쪽에 쓰고 South 문단의 겨울 피크 설명에Calgary 소속57을 포함한다. 이 서술 차이를 임의로 저자 정정처럼 고치지 않는다.

<a id="c30"></a>**C30.** Fig7의 price95분위 초과 event, lag±12시간 분석은 가격·수요의 연관을 보여준다. 본문의 peak 직전29/30% 감소, lag0의6.15/5.28%, 그림 lag0의0.0% 주석은 분모·기준이 충분히 연결되지 않는다. 과거 자료의 사건 전후 비교만으로 가격 신호의 인과 효과를 확인했다고 표시하지 않는다(PDF30–31).

<a id="c31"></a>**C31.** Appendix A는 GEFCom2017의 ISO New England 자료(2003-03–2017-04,10zones:8개하위+2개집계)를 사용한다. TableA5의 local/global 평균 nMAE는 Ridge `.82/.77`, XGBoost `1.19/1.08`, LightGBM `1.19/1.08`%; 평균 MAPE는 `2.59/2.38`, `3.97/3.53`, `3.96/3.50`이다. 정확한 추가 실험 split·모든 모델 설정은 주 AESO 실험과 같다고 추정하지 않는다(PDF55–58).

<a id="c32"></a>**C32.** 부록의 비슷한 histogram·계절성·부하 ratio는 조건부 반응 함수의 동질성 증명이 아니다. TableA5는 local/global만 비교하며 cluster 열이 없다. 따라서 군집화 불필요의 직접 ablation으로 옮기지 않는다. Ridge FB 범위는 local `.0001… .0004`에서 global `−.0007… .0007`로 넓어져 모든 지표·요약값의 우월 주장도 제한해야 한다.

<a id="c33"></a>**C33.** 추가 표기 문제도 남긴다. PDF11은 actual/prediction의 Y·Y-hat 설명이 앞뒤 정의와 뒤집히고, sample 수m이 series마다 다를 수 있다는 문장 뒤에 M=n×m을 사용한다. PDF33의 계수/중요도 Fig2 참조는 실제 Fig1에 해당한다. 서지60항목 중19/27·37/39·5/40·17/45는 반복 서지이고34에는 venue/year가 없다. 표기 문제만으로 저장 결과 전체를 무효라고 결론내리지는 않는다.

## KBS 판본 확인과 재사용 조건

<a id="c34"></a>**C34.** 원72가 함께 확인한 KBS 문헌은 López-Oriona·Montero-Manso·Vilar의 *Time series clustering based on prediction accuracy of global forecasting models*, Knowledge-Based Systems323(2025),113649다. [출판본 DOI](https://doi.org/10.1016/j.knosys.2025.113649)와 [arXiv 서지](https://arxiv.org/abs/2305.00473)는 현재3저자를 표시한다. 원72의 저자·판본 차이 메모는 당시 주장으로 보존한다. 이번에는 저장 Crossref JSON 전체와61개 서지 항목, arXiv 가시 내용·메타를 확인했고 현재 Crossref 응답도 저장본과 바이트가 같다. 출판사 검색 미리보기는 있었으나 직접 본문은403, 공개 API는429로 접근하지 못했다. 출판본 전체 방법·수치의 판본 대조를 완료한 것은 아니다.

<a id="c35"></a>**C35.** 표5개390숫자, 소속126라벨, 월평균120개·연평균10개·연간 막대420개·Fig9 선택24값을 서로 다른 검수 단위로 보존한다. TXT65쪽은 PDF 추출문과 페이지별 일치하고, 불완전 PDF는 정상 PDF의 정확한 앞6,291,456바이트다. HTML의 본문·수식11개·의사코드2개·표·캡션·서지와 원PNG4개도 대조했다. 참고문헌60편 본문, 원예측, 실험 코드 전체를 확인한 것으로 확대하지 않는다. 전사 초안에서 발견한32개 연간 막대 오독은 확대 대조 후 수정 이력을 보존했다.

<a id="c36"></a>**C36.** 팀이 재사용할 것은 두 군집화의 정보 의존·단위 차이, 같은 비교군을 가진 지표별 결과, 개선되지 않은 월·지역, 입력 입수 시점과 비용의 확인 조건이다. 새 제안에서는 소속을 결정하는 정보, cell과sample 중 군집 단위, 고정 예측기와 계산량, 학습/선택/평가 분리, θ처리·query배정·seed를 명시해야 한다. 동일 논문을 다시 요약하는 대신 이 전사와 출처를 사용하고, 새 코드·판본·원예측이 확보되거나 적용 조건이 달라질 때 해당 주장만 재검토한다. Tab 직접 예측의 이득, Tab 소속 점수의 효용, 최종 RCTL 효용은 각각 검증해야 한다.
