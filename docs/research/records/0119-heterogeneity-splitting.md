# 원89: cell 이질성과 RCTL 분할 효과의 구분

[출처](../sources/history-119.md) · [검수](../verification/history-119.md) · [근거](../evidence/0119-heterogeneity-splitting/README.md) · [이전 원88](0118-conditional-reference-audit.md)

특징의 차이, 그룹 정보의 가치, 별도 모델 학습의 효과를 혼동해 같은 실험을 다시 시작하지 않도록 원89의 판단과 근거를 연결한다. 논문에서 확인한 긍정 결과, 적용 한계, 표·본문의 미해결 차이를 함께 보존한다.

**상태:** 30개 주장·8개 묶음의 작성 후 원문 대조 완료. 새 모델 실행 0.

## 과거 실험과 판단의 연결

<a id="c01"></a>**C01. 원89가 구분한 네 비교.** 원89는 2026-09-26의 문헌·기호 검토이며 새 Tab/RCTL 실행이나 수치 pilot을 보고하지 않는다. global 입력에 cell/group 정보를 주는 비교, 같은 정보로 모델을 분할하는 비교, Tab context를 다른 cell로 바꾸는 비교, 특징 거리를 측정하는 비교를 구별했다. 각각 정보·학습·참고 표본·특징 표현을 바꾸므로 같은 효과로 취급하지 않는다. 당시 계획·Goal·예산 문구는 기록의 내용이다.

<a id="c02"></a>**C02. 원35의 훈련·validation 반대 방향.** 원35의 저장 checkpoint 진단에서는 7개 K4 조건 모두 global보다 훈련 MAE가 낮고 validation MAE가 높았다. global은 0.079981/0.075371, 주 seed TabICL K4는 0.078401/0.081656이었다. dropout을 끈 같은 가중치의 비교다. global의 두 번째 seed가 없고 자료량·optimizer step·early stopping 등이 달라 과적합 하나의 인과 증명이나 모든 분할의 실패로 확대하지 않는다. H119에서는 원35 보존 근거를 재연결했으며 checkpoint를 실행하지 않았다.

<a id="c03"></a>**C03. 원15의 ID 이득은 상한이 아님.** 원15의 동일 context 2,688행/query 1,024행 비교에서 cell ID를 추가한 TabICL 평균 MAE 이득은 약 0.78%, ID 열 순서를 바꾸면 약 1.01%였다. 7일 중 5일에서 개선했지만 모든 날짜·cell의 이득은 아니다. 한 주·단일 ensemble의 유한 추정 결과이므로 가능한 모든 clustering 이득의 상한으로 사용할 수 없다. 단독 교차 예측의 외삽 손해도 두 cell 자료를 함께 학습하는 손해와 다르다.

<a id="c04"></a>**C04. 원80의 직접 예측과 소속 선택.** 원80의 16cell에서는 input-only/raw/Tab/Ridge/HGB의 K4 소속이 완전히 같았다. 저장된 Tab 129개 중간 분위수 평균의 query MSE 0.0130434764는 Ridge 0.0158390254, HGB 0.0158616659보다 낮았다. 긍정적인 직접 예측 결과를 보존하되 동일 소속·고정 gradient 진단을 최종 RCTL 성능이나 독립 test의 개선으로 바꾸지 않는다. 좋은 예측값이 실제 설계 결정을 바꾸었는지가 별도 질문이다.

## 정보 손실과 유한 학습의 구분

<a id="c05"></a>**C05. 자체 MSE 분해의 조건.** 원89의 식은 외부 논문의 정리가 아니라 자체 기호 검토다. 고정 훈련 결과와 partition G=π(C), Y와 f̂의 유한 제곱적률, 독립 미래 모집단에서 μC=E[Y|X,C], μG=E[Y|X,G]라 두면 R(f̂)=E[(Y−μC)²]+E[(μC−μG)²]+E[(μG−f̂(X,G))²]다. (X,G)의 정보가 (X,C)에 포함되고 f̂가 (X,G)의 함수이므로 조건부 평균의 직교성이 교차항을 없앤다. 참 평균을 Tab 출력으로 바꾸거나 미래 분포가 달라지면 같은 항을 그대로 관측했다고 할 수 없다.

<a id="c06"></a>**C06. 함수의 존재·유한 학습·MAE.** 각 cluster 함수군이 같은 입력의 global 함수를 포함하면 cluster별 최선 위험을 모집단 비중으로 합한 값은 최선 global 위험보다 나쁠 수 없다. 이는 가능한 함수의 비교이며 학습된 여러 RCTL의 성능 보장이 아니다. 마지막 MSE 항의 표현·추정 손해를 Tab 분위수 폭으로 대입하지 않는다. MAE에서는 조건부 중앙값과 절대손실 위험 차이를 사용해야 하며 위 제곱 분해를 그대로 옮길 수 없다. 원38도 최종 담당 소속과 학습 표본 공유 범위를 구별했다.

## Global Models 저장판의 결과와 조건

<a id="c07"></a>**C07. Global Models의 통제축과 그룹 입력.** Global Models의 저장판은 arXiv:2012.12485v3, 35쪽이다. DGP 복잡도·단일/다중 시계열·이질성·자료량을 구별한다. 보통의 MS-Het는 시계열마다 다른 계수를 주지만 GroupFeature는 반복되는 알려진 생성 그룹 정보를 하나의 global 모델에 추가한다. 별도 그룹 모델을 학습하는 GFM.Cluster는 이 판본의 향후 과제다. 이 실험을 실제 통신 cell의 소속 추정 또는 여러 RCTL 학습 검증으로 인용하지 않는다.

<a id="c08"></a>**C08. Global Models의 학습·평가 조건.** RNN은 잔차 연결 peephole LSTM, FFNN은 feed-forward 구조이며 전처리에 정규화·log·window 변환과 역변환이 포함된다. 신경망은 최적 하이퍼파라미터로 10개 graph seed를 다시 학습한 예측의 중앙값을 사용한다. AR/SETAR/PR의 재귀 예측과 LGBM의 horizon별 모델도 구별한다. SMAPE/MASE를 보고하며 logistic의 zero 처리 SMAPE 변형, 상세 손실·튜닝·하드웨어 등은 별도 Online Appendix에 위임돼 이번 확인 밖이다.

<a id="c09"></a>**C09. 알려진 그룹의 긍정 결과.** Global Models Table8의 SMAPE/MASE는 RNN 38.27/0.87→36.68/0.84, FFNN 39.13/0.90→38.40/0.88, LGBM 37.39/0.86→37.05/0.85다. PR 38.89/0.87은 그대로다. logistic-map에서 알려진 그룹 정보를 넣은 개선을 보존한다. 그 효과를 분할 학습만의 이득이나 실제 데이터에서 추정한 그룹의 성공으로 넓히지 않는다.

<a id="c10"></a>**C10. GroupFeature 길이의 미해결 차이.** Global Models Table6은 GroupFeature의 4개 DGP·100개 시계열·길이600·horizon12를 적지만 §6.1.6은 100개 dataset의 시계열 길이를240으로 설명한다. 원89에서도 기록한 불일치다. 통상의 1000 datasets 설명에는 SETAR/Mackey-Glass/GroupFeature를100으로 줄인 예외가 있으므로 모든 결과를1000반복으로 표시하지 않는다. 원 코드·별도 부록을 확인하지 않은 상태에서 어느 길이가 실제 실행값인지 결정하지 않는다.

<a id="c11"></a>**C11. DGP·자료량별 결과의 한계.** Global Models의 자료량 변화 실험은 AR/SAR/logistic에만 있고 SETAR/Mackey-Glass는 선택한 길이·개수에서 비교한다. Table7은 각 조건의 최대 길이·개수 결과다. 본문의 비선형 모델 우위 설명도 모든 표 항목에 적용되지는 않는다. 예를 들어 logistic SS의 FFNN SMAPE53.27은 AR52.91보다 크고 MS-Het의 FFNN28.18도 AR27.56보다 크다. 특정 조건의 결과를 동질성 또는 다양성의 보편 법칙으로 바꾸지 않는다.

<a id="c12"></a>**C12. Global Models의 시간 측정 범위.** Table9는 SETAR MS-Hom-Long의 100개 dataset 중 하나에서 측정한 초 단위 시간이다. 전처리와 학습·테스트 합계는 RNN10793.98초, FFNN655.09초, LGBM9.94초, AR111.08초, SETAR3.03초, PR0.45초다. 100회 평균이나 우리 RCTL의 비용이 아니며 하드웨어는 별도 부록에 있다. 모델 수·저장량·전체 처리량·실측 시간을 서로 대체하지 않는다.

## Similarity/Diversity 저장판의 결과와 조건

<a id="c13"></a>**C13. Similarity/Diversity의 대상과 모델.** Similarity/Diversity 저장판 arXiv:2404.06198v2는34쪽이며 주 단위 단변량 전이를 비교한다. 5개 source, 합친 Multisource, source별 모델 Ensemble을 5개 target에 적용한다. DeepAR는 5개 멤버, context25/horizon15, 2층, negative-binomial 출력, 최대800epoch/early stopping이며 별도 하이퍼파라미터 탐색을 하지 않았다. 모든 층을 fine-tune하고 item-wise mean scaling을 사용한다. Traffic은 도로 차선 점유율이며 통신 트래픽이 아니다.

<a id="c14"></a>**C14. 평가 지표와 편향 부호의 충돌.** AvgRMSSE는 rolling origin과 시계열별 median forecast RMSE를 과거 lag1 naive RMSE로 나눈 뒤 평균한다. MSIS는95% 예측구간과 같은 RMSE 분모를 사용해 통상 MAE 분모를 바꾼 지표다. Eq5는 ME=y−ŷ인데 Table5 설명은 음수를 과소예측, 양수를 과대예측이라고 적어 부호가 반대다. Table5는 target별로 양 모드 결과의 표준편차로 나눈 값이다. 실제 구현 부호를 확인하지 않았으므로 과대·과소 방향을 확정해 옮기지 않는다.

<a id="c15"></a>**C15. 전이의 개선·악화와 비율 불일치.** Table4에는 M5→Traffic의 AvgRMSSE 4.46→1.60 개선과 M4→Traffic 1.97→2.52 악화가 함께 있다. ETS는 Traffic1.08과 Wholesaler1 0.60으로 두 모드 모두 최상이다. 인쇄값 35쌍을 엄격한 부등호로 세면 zero-shot이 Scratch보다 낮은 경우14, fine-tuning이 zero-shot보다 낮은 경우26으로 본문의40%/74%에 대응한다. 반면 fine-tuned<Scratch는29/35(약82.9%), 같은 값1개이며 본문의89%와 맞지 않는다. 반올림 전 값·집계 코드를 확인하지 않아 이를 임의로 고치지 않는다. 이 산술은 논문 인쇄값 검수이고 모델 재현이 아니다.

<a id="c16"></a>**C16. 유사도는 두 단계 중앙값.** §5.2는 feature를 모든 source dataset을 합쳐 표준화하고 모든 target dataset을 합쳐 별도로 표준화한다. 각 feature의 source–target 시계열 쌍별 1차원 Euclidean 거리에서 중앙값을 구하고 다시 feature별 거리의 중앙값을 취한다. 다차원 feature vector의 Euclidean norm을 한 번 계산하는 방법과 다르다. tsfresh로 부르는10개는 자체 feature2개를 포함하며 catch22는 mean·sd를 더한24개다. 표본은 dataset별 최대1000개 무작위 ID이고 평가와 같은 ID·seed·시점 구간인지는 명확하지 않다.

<a id="c17"></a>**C17. 상대 다양성과 PCA.** 다양성은 dataset별 feature 분산을 feature마다 source 집합 사이에서 min–max 변환한 뒤 더한다. tsfresh 최대는 Electricity5.51, catch22 최대는 M4 12.86으로 정의에 따라 순위도 다르다. PCA는 source와 target을 함께 표준화하므로 §5.2의 표준화와 구별한다. 두 축 설명분산은 tsfresh79%, catch22 49%다. 낮은 차원의 겹침이나 상대 다양성 값을 절대 병합 임계값·성공 보장으로 사용하지 않는다.

<a id="c18"></a>**C18. 회귀 기울기와 유의성.** §6은 대략 선형 관계를 보이는 조합을 선택해 zero-shot 결과를 target별로 비교한다. 각 관계의 source 점은 5개 source+Multisource의6개다. Table11의 catch22 다양성–정확도 기울기는 모두 음수지만 p<0.05는 Wholesaler2 한 곳뿐이며 불확실성 지표의 기울기는 모두 비유의다. Table12의 tsfresh 거리–bias 기울기는 모두 양수지만 p값0.14/0.11/1.00/0.06/0.84로 모두 비유의다. 관측된 방향을 인과 효과나 분할 기준으로 승격하지 않는다.

<a id="c19"></a>**C19. Table11과 bias 설명의 미해결 차이.** Table11의 Kaggle/Traffic/Solar bias slope·p-value는 uncertainty 열과 각각 −1.66/0.24, −5.95/0.71, −0.34/0.70으로 완전히 같다. 반면 본문은 bias 기울기가 거의 항상 양수라고 설명한다. Wholesaler1의0.31/0.01, Wholesaler2의0.41/0.00은 인쇄값 그대로 보존하며0.00을 정확한 p=0으로 읽지 않는다. Fig4/5의 bias 점들은 음수 없이 표시되므로 Table5의 signed ME를 그대로 그린 값으로 간주할 수 없다. 절댓값·스케일 변환의 정확한 구현은 미확인이다. 원 코드 없이 올바른 회귀값을 추정해 대체하지 않는다.

<a id="c20"></a>**C20. 적용 범위와 접근하지 않은 코드.** 저자도 상대적인 관계만 제공하며 절대적 성공 threshold는 없고 많은 회귀가 유의하지 않다고 명시한다. weekly·univariate·외생 입력 없음·horizon15의 제한이 있으며 다른 horizon 결과는 미확인이다. 같은 이름의 zero-shot이라도 학습된 DeepAR 전이는 Tab의 context 교체와 동일 연산이 아니다. 저장 v2의 코드 공개 예정 문구를 현재 코드 공개·재현 가능성 확인으로 바꾸지 않는다.

<a id="c21"></a>**C21. fine-tuning 시간의 분모.** Table13은 Linux VM 32CPU/77GB RAM에서 target별 fine-tuning 시간을 Scratch 학습시간으로 나눈 비율이다.35개 중25개가1보다 작아 약71.4%이며 Multisource→Traffic은2.17로 더 오래 걸렸다. 사전학습 비용을 합친 총비용이나 초 단위 값이 아니다. Sum은 서로 다른 target 분모의 비율을 더한 값이므로 전체 실행시간 비율로 읽지 않는다. 이 비용을 통신 cell의 여러 RCTL 학습 비용으로 전환하지 않는다.

<a id="c22"></a>**C22. 자료 규모 표의 산술 불일치.** Table1 source 합계는31,289개 시계열·7,446,010개 training points다. Table2의 Wholesaler2는55,000개×124기간이면6,820,000인데 training size는7,820,000으로 인쇄돼1,000,000 차이가 있다. 표의 총계35,768,411은 인쇄된7,820,000을 포함한다. 표의 어느 열이 실제 자료와 다른지는 확인하지 않았으므로 데이터 규모를 임의 확정하거나 모델 결과를 재계산하지 않는다.

## 수집·보존·판본·남은 확인

<a id="c23"></a>**C23. 초록만 확보한 연구의 범위.** 원89의 Sonnleitner 연구 DOI10.1016/j.eswa.2024.125666/SSRN4897928은 초록·검색 metadata 수준이다. 기록된 publisher/SSRN403·Fraunhofer 읽기 실패는 당시 접근 결과이며 현재 접근 상태가 아니다. LightGBM·13개 특징이라는 전제만으로 표본추출·통제·튜닝·특징별 부호를 확인했다고 쓰지 않는다. 검색 요약의8–13%를 연구 근거로 추가하지 않으며 원38의 미확인 표시를 유지한다.

<a id="c24"></a>**C24. 논문 수집 실패와 판본 식별.** 첫 PDF는 v3 고정 URL로 수집됐다. 두 번째 v2 URL 요청은2026-09-26T03:05:40 UTC에406을 남겼고 공개 latest URL 수집은03:06:49 UTC에 성공해 저장 문서의v2 표기를 확인했다. 현재 latest가 같은 판본이라고 가정하지 않으며 논문2개2,168,823bytes를 각각 SHA-256과 고정 판본 URL로 연결한다. 수집·검증 스크립트는 정적으로 읽었고 실행하지 않았다.

<a id="c25"></a>**C25. 최초·수정 렌더 manifest.** 최초 manifest는 각 논문의3개 페이지를 같은 잘못된 PNG 경로로 적었고 수정 manifest는6개 실제 파일·해시를 구별한다. 원89는 with_suffix 문제라고 설명하지만 보존된 render 소스20행은 이미 Path(str(output)+".png") 형태다. 보존 소스에 그 버그가 그대로 있다고 쓰거나 실제 실행 당시 수정 순서를 입증했다고 쓰지 않는다. 기존6개 PNG를 직접 열어 대응 PDF 페이지와 대조했으며 독립 이미지 완료 수에는 더하지 않는다.

<a id="c26"></a>**C26. snapshot과 원본 보존.** snapshot31 manifest에 나열된27개 파일은3,782,139bytes이며 manifest 자신의5,881bytes를 포함하면 폴더28개·3,788,020bytes다. 루트의 별도89_archive_verification.json 213bytes는 이 수에 포함되지 않는다. 새28표현물의52개 별칭 경로와 기존 비교 자료·보호 원본6개를 해시로 확인했다. 바이트 보존은 모든 연구 주장이나 실행 결과 검증과 다르다.

<a id="c27"></a>**C27. 당시 읽기와 이번 읽기의 차이.** 원89의 scope는 두 논문의 지정 절·표와6쪽 시각 확인을 보고했다. 이번 H119는 두 PDF 본문·참고문헌·파일 안 부록69쪽의2,299행을 끝까지 읽고 1차로 새 렌더33쪽과 기존 PNG6개를 직접 확인했다. 작성 후에는 PDF46쪽의 인용 내용을 다시 읽고 이미 확인한 렌더 중15쪽을 재대조했다. PDF 파생 TXT2개는 페이지별 추출 대응만 대조했다. 별도 부록·외부 코드·참고문헌에 나오는 모든 논문의 방법·원자료 재현까지 완료한 것은 아니다. TXT·PNG·별칭·페이지 수를 독립 연구 성과로 중복 집계하지 않는다.

<a id="c28"></a>**C28. 후보표·진행일지의 판본 차이.** snapshot30→31의47행 후보표는8행의 유한 학습 판단만 바뀌고 다른 행은 같다. 진행 기록은467→478행으로 늘었으며 원89 절이 추가됐다. 이전8–467행은 새19–478행과 같다. 현재 후보표47행과 진행 기록1–30행을 실제 읽었고 현재 진행판본31–478행은 직접 재독하지 않았다. 이전 판본과의 동일성 검사는 새 판본 전체의 의미 독해 완료로 세지 않는다.

<a id="c29"></a>**C29. 당시 예산과 자료 재사용.** 원89가 참조한 원장 SHA f3e370ba0bb39b220a3448daf00ab532729b91b93bce80b6d92a43a7ea71f2a9의 잔여값은 Tab11contexts/20,640query행, 추가 RCTL fit0이다. 이는 당시 기록이며 현재 정리 작업의 예산 또는 모델 실행 허가가 아니다. 원15·35·38·80 및 기존 후보표·진행 기록은 이전 보존 근거를 재사용하고 새 독립 완료로 가산하지 않는다. 원본을 변경하지 않았고 새 모델 실행은0이다.

<a id="c30"></a>**C30. 다시 설계할 때 필요한 결정과 남은 작업.** 원89는 특징 이질성 최소화나 다양성 최대화를 새 병합 규칙으로 채택하지 않았다. 새 후보는 어떤 소속·입력 정보·표현·표본 공유·학습 비용을 바꾸는지 명시하고 같은 소속을 group 입력으로 주는 global 대안과 비교해야 한다. 최종 추천안이 있었다고 꾸미지 않는다. 별도 부록·실행 근거, 현재 진행판본의 미독 구간, 원90 이후와 이전 고유 판본·기존 문서 공백, 전체 실패·비용 통합과 팀 접근·최종 검색 검수가 남아 전체 Goal은 진행 중이다.

## 같은 연구를 다시 제안할 때

| 제안 | 이미 확인한 범위 | 새 설계에 필요한 차이 |
|---|---|---|
| 비슷한 cell을 더 정확히 묶기 | 원80의 더 좋은 직접 예측에도 같은 소속 | 소속이 실제로 바뀌는 근거와 최종 학습 효과 |
| 이질성·다양성 점수를 병합 규칙에 추가 | source 집합에 상대적인 값·대부분 비유의 관계 | 정보 손실과 유한 학습 손해를 구분한 검증 |
| 그룹 정보를 주어 성능 개선 | 알려진 synthetic group의 단일 global 입력 실험 | 동일한 그룹 입력 global 대비 분리 학습의 추가 효과 |
| 모델 수를 줄여 비용 절감 | 모델 수·표본 처리량·학습시간은 서로 다름 | 동일 조건의 전체 비용 경계와 비교 |

이전 근거: [원15 ID 비교](0013-0015-transfer-cell-identity.md) · [원35 훈련·validation](0033-0035-process-fit-gap.md) · [원38 출처](../sources/history-023.md) · [원80 출처](../sources/history-088.md).

[인쇄표 산술](../evidence/0119-heterogeneity-splitting/printed-table-audit.json) · [판본 대응](../evidence/0119-heterogeneity-splitting/version-comparison.json) · [남은 확인](../evidence/0119-heterogeneity-splitting/packet-coverage.json)
