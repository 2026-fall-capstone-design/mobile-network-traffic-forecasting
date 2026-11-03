# 원87: 공동 출력의 표현 용량과 조건부 비교의 기준 분포

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

[출처](../sources/history-116.md) · [검수](../verification/history-116.md) · [근거](../evidence/0116-causal-capacity/README.md) · [원81 입력·출력 변경](0090-input-partition-decision.md) · [원86 학습 공유](0114-shared-training-scope.md)

구조의 기호적 제약을 실제 예측 손해로 바꾸어 읽거나, 조건 열을 남겼다는 설명만으로 조건부 표본 생성이 성립한다고 판단하지 않도록 당시 질문과 근거를 연결했다. 원래 연구 번호는 **87**이다.

**상태:** 26개 주장·7개 묶음의 작성 후 원문 대조 완료. 미독 범위는 후속 목록에 명시했다. 새 모델 실행 0.

## 질문·실행 상태·모델 구조

<a id="c01"></a>**C01.** 원87은 2026-09-26에 원81의 공동 입력·다중 출력 제안과 원86의 학습 공유 검토를 이어받았다. 같은 causal core를 여러 cell의 공동 출력에 쓸 때 전체 flatten 크기와 최신 입력의 영향이 통과하는 폭을 구분하고, 조건부 관계를 추정하는 비교 표본의 생성 과정을 확인했다. 기존 cell별 scalar UPC·RCTL의 결함을 발견한 기록으로 바꾸지 않는다.

<a id="c02"></a>**C02.** 당시 기록은 새 Tab 추론, RCTL 학습·forward·gradient, 데이터 수치 진단을 모두 0회로 명시한다. 같은 해시의 당시 원장에는 RCTL 29fit, Tab 69context·39,360query행, 잔량 11context·20,640행·추가 RCTL fit 0이 있다. 원87의 기호 검토를 새 성능 실험으로 세지 않는다. 이 원장은 과거 상태이며 현재 작업의 실행 허가가 아니다.

<a id="c03"></a>**C03.** 저장 RCTL은 왼쪽 padding convolution, 정방향 LSTM, 시간별 1×1 shortcut을 사용하며 block 폭은 16·32·64·64·32·16이다. 마지막 root shortcut도 폭 16이고 실제 dense는 `steps*16→1`이다. 따라서 원87의 다중 출력 head는 이 core에 대한 기호적 변경 가정이며, 저장 코드가 이미 다중 출력 모델을 학습했다는 증거가 아니다.

## 표현 용량과 위험 하한의 조건

<a id="c04"></a>**C04.** 과거 입력 O를 고정하고 최신 cell 벡터 Z만 바꾸며, 선형 다중 출력 head의 고정 가중치를 B∈R^(d×16)라 두면 `f(O,Z)=a(O)+B h(O,Z)`로 쓸 수 있다. 미분 가능한 곳에서는 `J_Z f=B J_Z h`여서 rank≤min(d,16)이다. flatten 크기 16L이 최신 입력의 독립적인 영향 차원 16을 늘려주지는 않는다. ReLU 경계에서도 고정 O의 출력 차이가 B의 열공간에 속한다는 진술은 유지된다.

<a id="c05"></a>**C05.** 이 주장은 평가 모드의 고정 BatchNorm 통계·dropout off, 과거 hidden으로 최신값을 보내지 않는 인과 경로, 고정 선형 출력층을 전제로 한다. training BatchNorm, 최신값을 이용해 이전 위치도 바꾸는 전처리·RevIN, 최신값 복제는 별도로 다뤄야 한다. scalar RCTL을 cell마다 호출하면 각 호출의 hidden이 달라 전체 cell에 같은 공동 rank-16 상한을 붙일 수 없다.

<a id="c06"></a>**C06.** 동일 모집단에서 제곱적분 가능한 Y와 예측 f를 두고 `m=E[Y|O,Z]`, `m_O=E[Y|O]`, `U=m−m_O`라 하자. 고정된 B의 열공간에 대한 직교 투영을 사용하면 초과 합 MSE는 `E||m−f||² ≥ E||(I−P_B)U||² ≥ Σ(j>16) λ_j(E[UUᵀ])`이다. 고유값은 큰 순서다. 이 하한은 국소 rank만이 아니라 고정 선형 부분공간을 사용한다. 출력 평균 MSE에는 d로 나누며 MAE에 같은 식을 적용하지 않는다.

<a id="c07"></a>**C07.** 하한의 U는 알려지지 않은 참 조건부 평균의 추가 성분이다. noisy target이나 Tab 예측의 공분산을 바로 대입해 RCTL의 실제 손해를 입증할 수 없다. 원74의 4-cell 직접 teacher 결과도 d>16의 공동 출력 제약을 시험한 결과가 아니다. 원87에는 이 하한을 실제 트래픽에서 추정한 결과나 해당 다중 출력 모델의 seed·성능표가 없다.

<a id="c08"></a>**C08.** `f=Z+core` 같은 최신값 출력 skip이나 cell별 선형 AR 항을 허용하면 전체 Jacobian에 보편적인 rank-16 상한을 적용할 수 없다. 예를 들어 core가 0이면 identity 전달이 가능하다. 이것이 항상 full rank이거나 실제 오차가 줄어든다는 뜻은 아니다. 출력 차분 뒤 최신값을 복원하는 구성도 구별해 먼저 비교해야 한다.

<a id="c09"></a>**C09.** cluster 크기를 줄여 용량 제약을 완화할 수 있다는 사실만으로 어떤 cell을 묶어야 하는지, Tab이 균등 분할보다 나은 소속을 고르는지가 정해지지는 않는다. 원81의 같은 폭에서 계산한 선형 MAC 비교는 유지하면서 용량·정확도·실측 시간의 해석 범위를 보완한다. 원86의 학습 공유 가능성도 신규성이나 성공으로 자동 전환하지 않는다.

## CIB 문헌과 저장 구현의 대조

<a id="c10"></a>**C10.** CIB는 Xinhui Li·Liang Duan·Lixing Yu·Kun Yue·Yuehua Li의 IJCAI 2025 논문이다. 저장 PDF는 9쪽·297,818바이트이며 이번에는 파일 1–6쪽의 본문과 전체 페이지 이미지를 읽었다. 기존 4·5·6쪽 PNG도 대조했다. 논문의 inter-series CIB와 intra-series CMI 손실은 서로 다른 부분이며, clustering이나 사전학습 Tab 소속 수정의 성능 증거가 아니다. 7–9쪽·실험표의 후속 검수는 남아 있다.

<a id="c11"></a>**C11.** 저장 metadata의 공식 커밋은 `ac09a66245f9eaa7371065ec3f7d3673df125c94`다. 네 코드 저장본은 공식 Git blob과 바이트 그대로 같지는 않았다. 마지막 LF 하나를 제외하면 backbone·exp_main은 공식 blob에 일치하고, CMI·Conditional_MI는 추가로 LF를 CRLF로 바꾸면 일치한다. 원저장본을 수정하지 않고 양쪽 SHA·바이트 수와 변환 관계를 보존했다. 현재 main의 최신 코드나 재현 성공을 확인한 결과는 아니다.

<a id="c12"></a>**C12.** 논문 §4.3 식24–25가 정의하는 기준 분포는 `P(C)P(A|C)P(B|C)`다. 다만 5쪽 본문도 과거 C를 고정한 채 인접 두 patch를 shuffle한다고 설명하며, 조건부 분포를 맞추는 구체적 절차까지 제시하지는 않는다. 따라서 ‘논문은 완전한 조건부 sampler를 구현했고 코드만 이를 어겼다’고 요약하지 않는다. 정의한 분포, 본문의 구현 설명, 실제 저장 코드를 각각 대조한다.

<a id="c13"></a>**C13.** CMI.generate_samples는 앞 patch들을 평균한 벡터를 condition으로 두고 patch1·condition을 유지한 채 patch2를 batch축에서 무조건 randperm한다. backbone의 실제 loop는 i=1부터 M−2까지 i와 i+1을 비교하므로 함수의 patch_idx1=0 영조건 분기는 이 경로에서 쓰지 않는다. 과거 전체를 조건으로 둔 논문과 과거 평균을 둔 코드도 구별한다.

<a id="c14"></a>**C14.** 고정된 표현의 독립 모집단 표본에서 무조건 B를 섞는 이상화의 기준은 `P(A,C)P(B)`다. 필요한 KL이 존재할 때 이에 대한 KL은 `I(B;A,C)=I(B;C)+I(B;A|C)`다. condition을 입력에 남겨두는 것만으로 같은 C에서 B를 다시 뽑는 연산이 되지는 않는다. 이는 해당 생성 방식의 일반적 분포 차이에 관한 기호 관계다.

<a id="c15"></a>**C15.** C가 0·1을 각각 확률 1/2로 갖고 A=B=C라면 조건부 MI는 0이지만 무조건 shuffle 기준의 KL은 log 2이다. 이번 정리에서는 8개 가능한 상태의 정확 유리확률을 열거해 원문의 반례를 다시 확인했다. log 2≈0.693147은 자연로그 단위의 기호 예시이며 실제 데이터 실험·논문 성능 재현·새 모델 pilot이 아니다.

<a id="c16"></a>**C16.** backbone은 CMI 값들을 평균하고 상한 clipping한 뒤 `klweight·KL + contraweight·contrast − cmiweight·CMI`를 vaeloss로 반환한다. Conditional_MI의 Gaussian KL 계산은 CMI critic과 별도다. 현재 고정 커밋의 model wrapper를 추가 조회해 `decomposition=False` 경로의 backbone 호출과 `(출력, vaeloss)` 반환을 확인했다. exp_main의 `use_amp=False` 경로는 예측 MSE에 vaeloss를 더해 backward·optimizer에 넘긴다. 정적 호출 연결 확인이며 원연구 당시 wrapper를 저장·독해했다는 주장이나 실행 재현이 아니다.

<a id="c17"></a>**C17.** 같은 exp_main의 AMP/CIBMTSF 분기는 모델의 두 반환값을 분리하지 않고 outputs로 받은 뒤 tensor처럼 슬라이싱한다. 확인한 wrapper의 tuple 반환과 맞지 않는 정적 코드 문제다. 따라서 앞의 정상적인 손실 연결 설명을 AMP를 포함한 모든 실행 경로의 검증으로 확대하지 않는다. 이 분기를 실행하거나 당시 논문의 실험 설정이 이 분기를 사용했다고 확인한 것은 아니다.

<a id="c18"></a>**C18.** 유한 batch 순열에는 제자리 항목이 남을 수 있고, 겹친 시간 window·변하는 표현·유한 critic·clipping도 영향을 준다. 실제 코드 출력이 앞의 모집단 KL과 같다고 주장할 수 없다. 확인한 범위는 무조건 shuffle이 조건부 독립 기준 분포를 일반적으로 보장하지 않는다는 점이다. 이 사실만으로 논문의 모든 이론이나 예측 결과를 부정하지 않는다.

## 문헌 해석과 후속 판단

<a id="c19"></a>**C19.** 논문 5쪽 식21 직전의 설명은 I(Zi;Yi)와 I(Zi;다른 변수)를 minimize한다고 쓰지만, 앞뒤 설명과 식21의 부호는 이 두 항을 키우는 목적을 나타낸다. 이 문장과 수식의 불일치를 보존한다. 6쪽 식27·Algorithm1은 MSE+α1·KL+α1·contrast−α2·CMI를 사용한다. 이번 대조를 논문의 모든 변분 경계·증명·시간복잡도 검증으로 확대하지 않는다.

<a id="c20"></a>**C20.** 읽은 §5.1에는 ETT 4종·Weather·Traffic·Electricity·ILI·Exchange Rate의 9자료, ETT의 6:2:2와 나머지의 7:1:2 분할, MSE·MAE 평가가 있다. 6쪽의 성능 우위·개선율은 저자의 보고이며 아직 Table1·2를 대조하지 않았다. 이를 원87의 모바일 통신 트래픽 성능표나 Tab/RCTL 개선율로 재사용하지 않는다.

<a id="c21"></a>**C21.** 원87은 시간·요일·계절 조건을 남겨두었다는 말 대신 실제로 생성되는 결합분포를 확인하자는 판단을 남겼다. TabPFN+CRT arXiv2603.06609v1은 당시 초록·버전까지 확인했다고 보고하고 원88에 본문 검토를 넘겼다. H116에서 그 논문 방법을 검증한 것으로 세지 않으며, scalar 회귀 분위수를 다변량 시계열 공동 생성기로 간주하거나 Tab으로 교체했다는 사실만으로 신규성을 주장하지 않는다.

## 수집 실패·보존 검수·남은 범위

<a id="c22"></a>**C22.** 수집기는 arXiv API query 두 건에 각각 최대 12결과·1MB cap을 설정했지만, 저장 search manifest에는 두 건 모두 HTTP406 오류만 남아 있다. 최대 24편을 찾거나 읽었다고 세지 않는다. 이후 공개 검색에서 공식 PDF를 찾았다는 경로는 당시 기록의 설명이며, API 오류 자체는 모델 실패나 연구 가설의 기각이 아니다.

<a id="c23"></a>**C23.** cib_source_manifest에는 HTTP200·297,818바이트·동일 PDF 해시·9쪽과 cp949 UnicodeEncodeError가 함께 있다. fetcher는 PDF 저장, TXT 추출 저장, 페이지 수 기록을 마친 뒤 첫 페이지를 console에 출력한다. 현재 PDF를 새로 추출한 결과도 9쪽이며 저장 TXT의 각 페이지가 머리글·양끝 공백을 제외하고 일치했다. 오류 기록을 지우거나 다운로드 전체 실패로 바꾸지 않는다. 이 자동 대응 확인은 TXT 1,128행 전체의 의미 독해를 대신하지 않는다.

<a id="c24"></a>**C24.** snapshot29 manifest의 24파일·1,790,337바이트를 저장 파일의 크기·해시와 대조했다. 원87 archive_verification의 수치도 일치한다. manifest 자체와 뒤에 쓴 archive_verification은 이 24파일 목록에 들어 있지 않다. 24는 보존 파일 수이며 독립 실험 수나 모든 내용의 검수 완료 수가 아니다.

<a id="c25"></a>**C25.** 원 verifier는 예산·PDF 해시, 페이지 수, PNG 존재, 일부 문자열, JSON parse, 복사 후 해시를 확인하고 scope·progress·snapshot을 작성한다. 이 절차가 기호 증명·CMI 추정의 정확성·성능 실행을 검증한 것은 아니다. 과거 Goal·예산·다음 행동 문구는 자료로 보존했으며 원본 연구 스크립트는 실행하거나 import하지 않았다.

<a id="c26"></a>**C26.** 핵심 11표현물 486행, code metadata 전체와 짧은 코드 2개, backbone 1–252행·exp_main 1–220행, 논문 1–6쪽을 읽었다. 기존 PNG 3개는 같은 논문의 파생 표현으로 독립 내용을 추가 집계하지 않는다. 결정표·연혁·원88 계획·TXT 전문, 논문 7–9쪽, 긴 코드의 나머지는 후속 검수로 남긴다. 재검토하려면 실제 용량 손해, 단순 skip/AR 대비 차이, Tab이 바꾸는 소속 또는 조건부 생성의 정확도·비용을 먼저 명시해야 한다. 이번 검수와 전체 연구 Goal 완료는 별개다.

## 같은 질문을 다시 검토하기 전에

| 확인할 질문 | 먼저 읽을 근거 |
|---|---|
| 원래 scalar RCTL과 공동 출력 제안이 같은가 | [원81 C15–C20](0090-input-partition-decision.md#c15), [기호 조건](../evidence/0116-causal-capacity/symbolic-audit.json) |
| 4-cell teacher 결과가 폭16 제약의 실측인가 | [원81 C21](0090-input-partition-decision.md#c21), [원74 상세](0072-0075-output-compression.md) |
| 소속을 미리 고정한 학습 공유가 금지되는가 | [원86의 네 공유 방식](0114-shared-training-scope.md) |
| 조건을 고정하고 섞으면 무엇이 달라지는가 | [분포·반례](../evidence/0116-causal-capacity/symbolic-audit.json), [CIB 원문](https://www.ijcai.org/proceedings/2025/0627.pdf) 5쪽 |
| 실제로 어떤 학습 경로를 확인했는가 | [코드 경로와 AMP 제한](../evidence/0116-causal-capacity/code-path-audit.json), [고정 커밋 model wrapper](https://raw.githubusercontent.com/Xinhui-Lee/CIB-MTSF/ac09a66245f9eaa7371065ec3f7d3673df125c94/CIB-MTSF/CIB-MTSF/models/CIBMTSF.py) |
| 무엇이 아직 검수되지 않았는가 | [남은 7그룹](../evidence/0116-causal-capacity/packet-coverage.json), [문헌 범위](../evidence/0116-causal-capacity/paper-scope.json) |

논문의 Table1·2, 코드의 나머지 구간과 후속 판본을 이어서 검토한다. 자료 확보·정적 호출 연결·기호 대조·실행 재현은 각각 다른 상태다.
