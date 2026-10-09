# 기록25의 인접 구조: 소속·지역 guidance·학습 스케줄

[연구 기록25의 판단](../records/0025-adjacent-structures.md)을 이해하기 위한 제한적 비교다. 2026-10-09에 지정 버전을 확인했다. 논문이 보고한 성능을 재현하거나 최신 모든 개정본을 비교한 문서가 아니다. 버전·파일 해시·읽은 구간은 [출처](../sources/history-018.md)에 있다.

## Ma · VAL 손실로 선택하는 소속과 fallback

[2604.13748v1](https://arxiv.org/pdf/2604.13748v1)의 §2.1–2.5·§3.1, 식2–6·11–14, Algorithm1을 대조했다. TRAIN 통계로 전처리하고 global·prototype을 적합한다. 공유 encoder/decoder와 특화 parameter를 구분하며, global warm start와 L2-SP 정규화를 사용한다. one-step으로 적합하지만 재배정 비용은 지정 horizon 집합의 VAL 손실 평균이다. K/seed 선택식의 routed 1-step 손실과 `γK/N` 항을 이 비용과 혼동하지 않는다.

집단의 specialized 1-step VAL 평균 손실이 그 집단에 적용한 global보다 **엄격히 크면** fallback한다. 동점은 specialized에 남는다. 선택·routing을 동결한 다음 TRAIN+VAL에서 다시 적합하고 TEST를 한 번 평가한다. VAL 평균 fallback을 모든 series·미래 기간의 무손해 보장으로 옮기지 않는다. H017은 기존 checkpoint를 고정한 개발 진단이었다. **H018-C02·C03**

## NeST · 예측한 지역 미래로 개별 예측을 안내

[2605.16447v2](https://arxiv.org/pdf/2605.16447v2)의 §3–4.3은 이력 affinity→정규화 Laplacian→spectral embedding/K-means→지역 평균과 patch autoregressive 예측을 연결한다. node 이력과 지역 future guidance를 cross-attention으로 결합한다. 추론의 첫 지역 guidance는 zero-mask와 과거 node 입력에서 예측하고, 이후 예측한 지역값을 이어 쓴다. 미래 실제값을 사용할 수 있다는 뜻은 아니다. **H018-C04·C05**

다음 불일치는 원문을 임의로 고쳐 구현할 수 있는 근거가 아니다.

| 위치 | 확인한 내용 | 재사용 범위 |
|---|---|---|
| §4.1 식1 / A7 / Algorithm1, PDF3·16·17 | chunk 평균이라는 설명, vector subsequence 거리, 전체 이력 RBF의 관계가 충분히 명시되지 않음. A7은 주기 길이 약100을 근거로 chunk **개수**100을 정함 | 주기 길이와 chunk 수의 동치·동일 affinity 구현을 가정하지 않음 |
| Figure1 / Algorithm2 / limitations, PDF4·18·9 | 그림·알고리즘에는 teacher forcing과 예측 guidance를 섞는 scheduled sampling이 있으나 limitations는 이를 future work로도 제시 | 실제 실험의 스케줄은 코드로 확인하지 않음 |
| A4 식17–20, PDF14–15 | 식17의 부등호와 식19–20의 일반 하한에 아래 문제가 있음 | noise 독립성만으로 SNR 이득을 보장한다고 인용하지 않음 |

정적 grouping, affinity의 `O(N²)` 전처리, 노출 편향과 순차 rollout 지연도 limitations에 명시돼 있다. 위 열람을 전체 성능표 검증으로 세지 않는다. **H018-C05·C06·C07**

### SNR 식의 작은 대수 대조

원문 A4는 결정적 신호 `S_i`와 독립·동일 분산 Gaussian noise를 놓고, `n=|C_m|`일 때 다음 정의를 사용한다.

$$
\mathrm{SNR}(Z_m)=n\|\bar S\|^2/\sigma^2,\qquad
\overline{\mathrm{SNR}}_m=\frac{1}{n}\sum_i\|S_i\|^2/\sigma^2.
$$

식17은 `||Σ S_i||² ≥ (Σ ||S_i||)²`를 요구한다. 두 직교 단위 vector이면 왼쪽2, 오른쪽4라 성립하지 않는다. 이는 삼각부등식의 일반 방향과 반대다.

식19–20의 하한도 인쇄된 가정만으로 일반적으로 성립하지 않는다. 원문의 식18은 정규화 내적을 상관으로 정의한다. `n=2, S₁=1, S₂=2, σ²=1`이면 그 상관은1이고, 원문 정의에 따른 지역 SNR은 `2×1.5²=4.5`, 제시된 하한은 `(1+1)×(1²+2²)/2=5`이다. 따라서 `4.5 ≥ 5`는 거짓이다. PDF14–15를 시각적으로 대조해 추출 문자 오류와 구분했다. 이는 **인쇄된 식과 가정의 대수 확인**이며, 학습 실험·noise 표본 생성·실제 traffic 성능 반증이 아니다. **H018-C06**

부수 확인: A6 식22는 `e=예측−정답`으로 정의하면서 통상 `정답−예측`에 쓰는 pinball 식을 적는다. 이 표기만으로 분위수 label의 실제 구현·보정을 인증하지 않는다. 코드 검토와 실험 결과의 오류 여부는 미확인이다.

## Graph Coloring · 공유 parameter를 갱신하는 task 스케줄

[2509.16959v3](https://arxiv.org/pdf/2509.16959v3)의 §3.1–4.5·Algorithm1은 가중 task gradient EMA의 음의 cosine `ρ`가 `τ`보다 클 때 충돌 edge를 만든다. 큰 degree부터 처리하는 Welsh–Powell greedy coloring은 충돌 없는 색 집합을 만들지만 최소 색 수를 보장하지 않는다. 활성 집합만 공유 parameter와 task head를 갱신한다. 주기적으로 모든 task를 refresh하며 compatible slot 복제로 최소 빈도를 조절한다. cluster별 독립 모델을 배포하는 소속 결정과 다르다. **H018-C08·C09**

AppendixD, PDF26–28의 dense refresh는 `Θ(K²d)`이며 간격R로 상각하면 `Θ(K²d/R)`이다. 새로운 probe gradient 계산은 별도 `Θ(KG/R)` 비용이므로 scheduler 산술만으로 전체 학습 비용을 설명하지 않는다. 여기서 K는 task 수, d는 gradient 차원, G는 task gradient 계산 비용이다. **H018-C10**

Figure1(e)의 색 순서는 A·B·B·A로 보이며, 식11의 두 집합 단순 순환 A·B·A·B와 다르다. 도식과 수식의 차이를 남기고 실제 구현을 추정하지 않는다. 최신판 링크로 과거 v3의 근거를 교체하지 않았다. **H018-C09**

## NTK · 발견 단계였다는 경계

[Morello·Grégoire·Verboven의 기관 초록](https://researchportal.vub.be/en/publications/exploring-task-affinities-through-ntk-alignment-and-early-trainin/)은 초기 **학습 단계**에서 여러 run을 평균해 affinity를 추정했다고 설명한다. 기관 기록은 2024-12-02, M3L NeurIPS24 Workshop으로 표시한다. 원문25는 검색 발췌·기관 초록만 읽었다고 명시했다. 이번 직접 [OpenReview PDF](https://openreview.net/pdf?id=HxT9EuHdXW) 열기는 브라우저 확인 페이지였으며 검색 발췌와 기관 초록만 대조했다. 상세 알고리즘·초기화만 사용한 추정기·RCTL 대리성 검증으로 집계하지 않는다. **H018-C11**

위 방법이 존재한다는 사실은 새 제안의 성능이나 신규성을 자동으로 결정하지 않는다. 어느 입력·모델·평가 정보가 소속에 들어가며 최종 배포 단위가 무엇인지까지 비교해야 한다. 당시 결론과 실제 peak support는 [기록25](../records/0025-adjacent-structures.md)에 연결했다.
