# 원81 공동 입력·다중 출력의 진입 보류와 계산 조건

[출처](../sources/history-090.md) · [검수](../verification/history-090.md) · [근거](../evidence/0090-input-partition/README.md) · [원80](0088-conditional-graph-diagnostic.md)

원래 번호는 **81**이다. H090은 당시 판단과 저장 소스의 기호 비용을 검토한다. 문헌 보고서가 주장한 독해 범위와 이번에 직접 검수한 범위를 구분한다.

## 무엇을 바꾸려 했는가

<a id="c01"></a>**C01.** 원81은2026-09-26의 입력 분할 진입 검토다. cell별 sample을 같은 scalar RCTL에 모으는 방식에서, 같은 시각의 여러 cell 이력을 공동 입력으로 쓰고 cell별 미래값을 별도 출력하는 방식으로 바꾸면 유효한 결정이 생기는지를 물었다. H090은 이 판단·기호 계산·자료 보존을 정리하는 묶음이다.

<a id="c02"></a>**C02.** 계획은 원문·정적 코드·기호식 검토였고 판단문은 새 TabICLv2 추론, 단순 회귀 적합, RCTL 학습·forward·gradient 계산을 모두0회로 기록한다. 새 다중 출력 모델의 성능표·학습 seed·실행 환경은 이 기록의 결과로 제시되지 않았다. 문서 보존 검사를 모델 실행 검증으로 바꾸지 않는다.

<a id="c03"></a>**C03.** scalar 공유에서는 각 sample이 한 cell의 이력을 받아 그 cell의 다음 값 하나를 예측한다. 공동 입력·다중 출력에서는 cell별 이력이 서로 다른 열이고 정답도 고정된 cell별 출력 좌표다. context 행에 여러 cell의 sample을 섞는 것만으로 후자의 구현이 되지 않는다.

<a id="c04"></a>**C04.** 원81은 출력 좌표가 구별되면 서로 반대 부호의 함수를 따로 출력할 수 있다고 판단했다. 따라서 원47의 식별되지 않는 scalar 함수 공유 반례를 다중 출력 후보 기각에 그대로 쓰지 않았다. TCN·LSTM·이중 잔차 core를 유지해도 입력·출력 폭과 학습 단위는 바뀐다.

<a id="c05"></a>**C05.** 당시 결론은 입력 공유로 바꾸는 것만으로 추천안을 확보하지 못했다는 진입 보류다. 이미 있는 방법보다 다른 유용한 선택을 한다는 근거와 단일 global 다중 출력 대비 이점이 부족하다고 보았다. 모든 다변량 clustering의 무용성이나 TabICLv2 직접 예측의 실패를 선언한 것은 아니다.

## 당시 문헌 검토가 남긴 비교 대상

<a id="c06"></a>**C06.** 원81은 DGCformer2405.08440v1·DUET2412.10859v3·CCM2404.01340v2·Fuchs–Wang2312.16544v1의 지정 절과 두 저장소의 선택 코드를 읽었다고 보고했다. 아래 C07–C10은 그 보고서의 검토 경로와 당시 반영 사항이다. 이번 H090에서 네 논문의 모든 방법·증명·그림 또는 외부코드를 검수한 것으로 세지 않는다.

<a id="c07"></a>**C07.** 원81은 DGCformer를 복원·상관 graph·잠재 clustering 뒤 같은 cluster의 channel attention을 허용하는 분리형 비교 대상으로 정리했다. cluster 수의 grid search가 예측 성능과 완전히 독립적인지는 미확인으로 남겼고 공식 실행 코드를 찾지 못했다고 적었다. 이 기록의 검색 실패를 현재 코드가 존재하지 않는다는 주장으로 확대하지 않는다.

<a id="c08"></a>**C08.** 원81은 DUET의 temporal expert와 FFT 진폭 기반 학습 거리·channel mask를 고정된 서로소 partition과 구별했다. 선택 코드에서 쌍별 차이와 전체 attention score를 먼저 계산한다고 보고했고 논문 Eq.18과 일부 확률 처리의 차이를 남겼다. 따라서 sparse mask만으로 전체 쌍 비용이 없거나 논문을 정확히 재현했다고 보지 않았다.

<a id="c09"></a>**C09.** 원81은 CCM의 cluster별 출력층과 소속 확률에 따른 결합, 예측·cluster 손실의 공동 학습을 고정 cluster별 독립 RCTL과 구별했다. shared channel-independent 모델과 cell별 개별 가중치 모델도 구별해야 한다고 적었다. cell별 출력 좌표나 cluster별 head의 추가만으로 기여가 성립한다는 판단은 하지 않았다.

<a id="c10"></a>**C10.** 원81은 Fuchs–Wang의 변수 집합별 예측 의존도와 Example2.11을 pairwise linkage만으로 놓치는 공동 효과의 선행 경로로 연결했다. i.i.d. 가정과 sample 수 n에 관한 O(n log n)의 범위를 남겼고 CRAN didec 문서는 확인했으나 설치·패키지 소스 검토는 하지 않았다고 보고했다. 이를 미래 트래픽 MSE나 RCTL 학습을 직접 최적화하는 동일 방법으로 쓰지 않는다.

## 정보 손실과 실제 성능

<a id="c11"></a>**C11.** 제곱 적분 가능한 Y, 동일한 평가 분포, 전체 관측 입력 X_U와 그 일부 X_S를 두고 m_U=E[Y|X_U], m_S=E[Y|X_S]라 하자. R*(A)=E[(Y−E[Y|X_A])²]로 두면 조건부 기대값의 직교성과 tower property로 R*(S)−R*(U)=E[(m_U−m_S)²]가 성립한다. 이는 nested 정보에 대한 최적 제곱오차 관계이며 원81도 새 정리라고 주장하지 않았다.

<a id="c12"></a>**C12.** 실제 TabICL 예측을 위 m에 대입하면 추정 오차가 섞이며 RCTL이 최적 조건부 평균에 도달한다고 보장되지 않는다. 유한 자료에서 열을 제거해 실제 성능이 좋아져도 위 최적 위험 차이가 음수가 된 것은 아니다. 평균을 쓰는 같은 항등식을 MAE에 그대로 적용하지 않는다.

<a id="c13"></a>**C13.** 원문의 Y=2+UV 예시를 확인할 때 U와 V가 독립이고 각각−1과+1을 동일 확률1/2로 갖는다고 명시한다. 그러면 하나만 알아도 조건부 평균은2, 둘을 알면Y를 정확히 알며 최적 MSE는1에서0으로 줄어든다. 원문의 독립·±1이라는 표현만으로 평균0까지 보장되지는 않아 이 대칭 조건을 보완했다. 이는 기호 확인이며 트래픽의 빈번한 현상이나 TabICL만의 이점이 아니다.

<a id="c14"></a>**C14.** 원81은 전체 입력으로 이미 추론한 query에서 열을 지우거나 값을 바꾸는 것이 m_S 계산과 같지 않다고 지적했다. 해당 열 집합으로 context와 query를 함께 구성해야 하며 캐시 재사용은 별도 확인이 필요하다. 모든 subset을 평가하는 설계는 후보 입력 수에 따라 지수적으로 커질 수 있다. 이 기록에서 subset 탐색을 실행하지 않았다.

## 저장 코드에서 확인한 비용식

<a id="c15"></a>**C15.** 저장 rctl_torch.py의 실제 dense는 nn.Linear(steps*16,1)이다. 원81의 C(F,s)는 이 scalar 출력층을 s개 출력으로 확장하되 같은 core 폭을 유지한다고 가정한 선형 MAC 식이다. 저장 코드가 이미 다중 출력 RCTL을 구현하거나 학습했다는 뜻이 아니다.

<a id="c16"></a>**C16.** 입력 폭 a·출력 폭 b의 block은 길이 L에서 두 convolution과 두 shortcut이 L(5ab+3b²), LSTM 네 gate의 입력·순환 선형항이8Lb²다. 합계 L(5ab+11b²)이며 첫 block의 입력 계수는80F다. 마지막 root shortcut16F를 더해 전체 입력 계수는96F다. bias·활성화·BN 등은 이 선형 MAC에 포함하지 않는다.

<a id="c17"></a>**C17.** 폭16·32·64·64·32·16에서 block 상수항의 합과 중간 projection16²+32²+64²를 더하면169728이다. 마지막 선형층을 s개 출력으로 가정하면16Ls가 추가되어 C(F,s)=L(169728+96F+16s)가 된다. 소스를 정적으로 읽고 작은 정수 산술로 대조했으며 forward 실행은 없다.

<a id="c18"></a>**C18.** 서로소 cluster K개에 cell 수 s_g를 배정하고 합계N, cell별 특징 q개와 공통 특징 c개를 가정하면 F_g=q s_g+c다. 이때 전체 선형 MAC은 L[(96q+16)N+(169728+96c)K]이다. 각 cluster가 같은 core 폭·입력 길이와 해당 출력 수를 사용한다는 비교 조건이 필요하다.

<a id="c19"></a>**C19.** 같은 폭의 단일 global 다중 출력은 K=1이므로 K>1에서 추가 MAC은 L(K−1)(169728+96c)다. 반면 같은 scalar 모델을 cell별로 N번 처리하는 비교에서는 core 반복을 K번으로 줄일 수 있다. cluster 수만 세거나 한 비교 대상을 생략하면 비용 결론이 바뀐다.

<a id="c20"></a>**C20.** 같은 hidden 폭은 같은 총 parameter 수가 아니다. 여러 core의 용량·정확도, global 출력 병목, batch 구성, 병렬 latency와 메모리·통신은 이 MAC 식만으로 판정할 수 없다. bias 덧셈·활성화·BN·메모리 이동을 제외한 계산이며 실제 wall time이나 네트워크 성능 측정이 아니다.

## 이미 있던 수치와 반례

<a id="c21"></a>**C21.** 원81이 인용한 MSE는 원74의 네 cell 3737·3765·6137·6165, 공통28입력, context256, seed20260925의 직접 teacher 개발 assessment 결과다. context는168–671에서256시점을 뽑았고 query672–1007 중 뒤168시간인840–1007에서 평가했다. 각 cell의 raw0–671 평균으로 나눈 무차원 target의 제곱오차이며 관측 이력으로 다음1시간을 예측했다. Tab 출력은 ensemble1의 mean이다. H070에서 검수한 값은 Tab0.009579815874350413, HGB0.011924807253712862, Ridge0.014359847237104397이며 원81 반올림과 일치한다. 독립 test나168시간 재귀 예측 결과가 아니다. 같은 조건의 own-only Tab과 비교하지 않았으므로 공간 입력 효과·새 다중 출력 RCTL 이득으로 바꾸지 않는다.

<a id="c22"></a>**C22.** 원80에서는16cell의 input-only·raw target·Tab·Ridge·HGB 기반 소속이 같았고 고정 gradient 지표의 PCC 대비 이득도 기간별로 뒤집혔다. 원81은 이를 좋은 직접 예측이 유용한 다른 clustering 선택으로 이어졌다는 증거가 부족한 사례로 재사용했다. 새 독립 실행이나 모든 조건부 평균 방법의 실패로 세지 않는다.

## 원문과 코드가 보존된 과정

<a id="c23"></a>**C23.** source_manifest는 HTML8개와 commit/tree JSON4개의12항목이다. HTML은 네 논문의 versioned 본문4개와 arXiv 서지4개이고, 수집 코드는 별도로TXT8개를 만든다. math alttext를 넣고 script/style/nav를 제외하는 추출 방식이므로 TXT가 원 HTML의 그림·모든 표현을 보존한다고 가정하지 않는다. 이번에는 수집 코드를 재실행하지 않았다.

<a id="c24"></a>**C24.** code_manifest는 DUET의 dcc6e6780a9138731b64b9b5398a94a1d97033f0와 CCM의 e4769baa7f8457358eb9b4614af2de1fbfba2257에 고정된 선택8파일을 담았다. 최초 HEAD 조회와 이후 SHA별 tree/raw 파일 수집을 구별한다. 명세·파일 해시 일치는 전체 저장소 확보·의존성 완비·논문 재현 성공의 증거가 아니다.

<a id="c25"></a>**C25.** snapshot23 manifest의42파일·3,524,587바이트를 실제 보존 파일과 대조했고 원81 검증 요약은 items를 제외한 manifest와 일치했다. 그 안에는 당시 progress·candidate index·원장·AGENTS도 있다. 보존42파일의 해시 확인을42개 고유 내용 전수 독해로 세지 않으며, 과거 지시를 실행하지 않는다.

<a id="c26"></a>**C26.** 원81 snapshot의 예산 원장은 원80 종료원장과 SHA-256 f3e370ba0bb39b220a3448daf00ab532729b91b93bce80b6d92a43a7ea71f2a9로 같다. 당시 잔량은 Tab11context·20640query행·RCTL추가fit0이었다. 이는 역사적 상태이며 현재 모델 실행 허가나 새 예산이 아니다. 정리 과정은 원장을 변경하지 않았다.

## 재사용과 남은 검토

<a id="c27"></a>**C27.** H090의 중심11그룹 중 새 내용은 본문6개·전체JSON4개이고 RCTL1개는 재참조다. 원74 결과·코드와 원80 판단·원장4개도 중복 가산하지 않는다. 문헌 폴더의 HTML/TXT16·선택 외부코드8·commit/tree4·검색1, 합계29그룹의 본문과 snapshot 연혁 변경분은 후속 검수로 남긴다.

<a id="c28"></a>**C28.** 같은 입력 공유 후보를 다시 검토할 때는 관측 가능한 조건에서 강한 단순 대안이 잘못 고른 입력 집합 때문에 생기는 실제 손해와 TabICL이 바꾸는 선택을 먼저 특정한다. 원81은 그 근거 없이 subset·hypergraph나 architecture 이름만 추가하지 않기로 했다. 전체 연구 방향 확정·최종 문서·현재 Goal 완료는 별개의 작업이다.

## 근거를 찾는 순서

| 대상 | 위치 |
|---|---|
| 원81 판단·계획·공개 요약 | [보존 자료](../evidence/0090-input-partition/manifest.json) |
| 선형 MAC의 항별 수치와 보존42파일 검수 | [기호 계산](../evidence/0090-input-partition/archive-and-symbolic-audit.json) |
| 원74 수치와 조건 | [H070](0072-0075-output-compression.md), [재인용 값](../evidence/0090-input-partition/reused-teacher-values.json) |
| 원80 소속·gradient 반례 | [H088](0088-conditional-graph-diagnostic.md) |
| 네 문헌의 저장 당시 주소 | [DGCformer](https://arxiv.org/html/2405.08440v1), [DUET](https://arxiv.org/html/2412.10859v3), [CCM](https://arxiv.org/html/2404.01340v2), [Fuchs–Wang](https://arxiv.org/html/2312.16544v1) |
| 문헌·외부코드·검색의 남은 범위 | [29그룹 목록](../evidence/0090-input-partition/pending-source-index.json) |

외부 링크는 저장된 버전의 탐색 주소다. 이 묶음에서 현재 웹페이지를 재조회하거나 외부 코드를 실행하지 않았다.
