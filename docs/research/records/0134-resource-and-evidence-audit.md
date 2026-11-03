# 원104 자원과 근거의 두 번째 감사

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

**원104는 실험 상한과 후속 근거를 다시 확인한 운영 기록이다.** 새 성능 실험이나 모든 대안의 기각으로 분류하지 않는다. 2026-09-26 당시 연구 Goal은 미완료·활성 상태로 남았다. 현재 아카이브 작업은 이 상태와 구별한다.

[4출처/10사본](../sources/history-134.md) · [13주장](../verification/history-134-claims.json) · [작성 후 대조](../verification/history-134-second-pass.json) · [범위](../evidence/0134-resource-and-evidence-audit/packet-coverage.json) · [재검토 안내](../references/resource-and-evidence-audit.md)

## 기록의 질문과 실제 수행

앞선 [원103](0133-current-evidence-and-unapproved-extension.md)은 미승인 추가 학습 제안과 최종 추천의 공백을 남겼다. 원104는 같은 제약이 계속되는지, 새 실험 없이 가능한 확인 경로가 직접 RCTL 후속 검사를 대신하는지 감사했다. JSON은 새 모델 호출0·새 수치 실험0·연구 진척 주장false를 기록했다.

원104에는 새 데이터·시간 분할·전처리·seed·실행 명령·성능표가 없다. 이 기록의 새 예측 지표는 해당 없음이며, 연결된 원101/95/102의 실험 조건을 새 실험 설정으로 복사하지 않는다. 원104가 언급한 후보 색인의 정확한 판본은 파일에 명시되지 않았다. 이후 root 색인을 당시 전수 검토의 근거로 간주하지 않는다.

## 당시 상태와 숫자

| 항목 | 원103 | 원104 | 읽을 때의 한계 |
|---|---:|---:|---|
| 첫 명시적 자원 감사 회차 | 103 | 103 | 원래 연구 Goal의 회차 |
| 연속 자원 감사 횟수 | 1 | 2 | 현재 정리 Goal의 횟수가 아님 |
| RCTL fit 사용 / 잔여 | 29 / 0 | 29 / 0 | 당시 같은 pinned 원장 |
| Tab context / query행 잔여 | 2 / 4512 | 2 / 4512 | 추가 학습 제안과 구별 |
| 제안 승인 / 응답 기록 | false / false | false / false | 기록 밖의 모든 대화 부재를 입증하지 않음 |
| Goal 완료 / 활성 유지 | false / true | false / true | 원104의 blocked threshold는false |

fit은 한 모델의 학습 실행을 뜻한다. 원장SHA60b589…의4필드를 선택 대조해29/0·2/4512·reset0·goalfalse를 확인했다. 이후root 원장SHA17a549…는 보호 대상의 해시만 확인했고 본문을 새로 읽지 않았다. [원본 보존 검사](../evidence/0134-resource-and-evidence-audit/preservation-check.json)와 [저장값 대조](../evidence/0134-resource-and-evidence-audit/saved-evidence-check.json)를 구별한다.

## 당시 다시 검토했다고 적은 다섯 경로

| 경로 | 원104의 판단 | 팀이 먼저 확인할 근거 |
|---|---|---|
| 후보 색인 | 당시 기록에서 새로운 별도 경로가 구체화되지 않음 | 색인의 판본·실제 검토 범위는 별도 확인 |
| 실제 pooled context | 직접Tab 예측은 좋았지만 두K4의 RCTL 순위와 다름 | [원101](0131-actual-pooled-context-and-rctl-ranking.md)의 조건·주간/cell 반례 |
| 기본 batching | 구현의 기본 이득을 재명명해도 Tab 기여가 생기지 않음 | [원95](0125-frozen-rctl-serving-cost-baseline.md)의 CPU/호출/비용 범위 |
| source/algebra 검토 | 유한 RCTL Adam·MAE 학습을 대신할 직접 연결이 부족 | [원102](0132-architecture-kernel-and-joint-risk.md)의 이론·실제 학습 경계 |
| 남은Tab2context | 판별 계획 없이 사용해도 RCTL 후속 근거 공백이 남음 | 구체적인 결정·후속 확인·자원 범위를 먼저 설명 |

이는 원104의 `independent_routes_rechecked`에 적힌 요약이다. 연결 자료의 새 전문 검증이나 모델 재현으로 집계하지 않는다. 유용한 직접 예측을 부정하지 않으며 모든 연구 방향이 불가능하다는 주장도 아니다.

## 재검토와 다음 실행을 구별하는 기준

상한 증액은 후보 선정이나 개선의 근거가 아니다. [원103의 조건부 확장](0133-current-evidence-and-unapproved-extension.md#claim-26)은 후보1개를 먼저 고정하는 미승인 제안이었다. seed당최대9fit, 선택적두seed18fit/누적최대47fit·추가1440epoch·1800초CPU는 계획 상한이며 실제 사용량이 아니다. 과거 감사의 note에 있는 blocked 처리·대기 지침을 현재 작업의 명령으로 실행하지 않는다.

새 연구안에는 실제 손해, 가까운 선행과의 차이, Tab이 바꾸는 결정, 같은 정보·비용의 비교군, 후속 RCTL 근거와 중단 조건을 명시해야 한다. 실패한 조건과 달라지는 점은 [재검토 안내](../references/resource-and-evidence-audit.md)에 연결했다. 이 아카이브는 새 학습이나 과거 범위 질문을 실행하지 않았다.

## 판독 범위와 남은 기록

원104 JSON37행·원103 pending32행·extension25행을 실제 읽고, 작성 후 같은94행과 원장4필드를 다시 대조했다.4출처/10경로 중 새 정확사본은 원104 JSON1개2796bytes이며 기존3사본을 재사용한다. 독립 전문JSON 신규 집계는1, 다른 전문/선택/이미지 신규 집계는0이다. 같은 자료를 다시 읽거나 해시가 같은 사본을 연결한 것을 새 실험으로 세지 않는다.

현재progress132–611/이전122–601와RCTLsummary literal전문, 이후·옛고유판본/다른형식·전체통합/장기접근/최종delta/검색10+는 남아 있다. root progress4335행·candidate2537행도 다른SHA이며 동등 구간을 아직 증명하지 않았다. 원본·상태·예산 원장은 보존했고 원code 실행/import·모델 생성·새 학습·추론0이다. 전체Goal은 미완료다.

## 주장별 근거

<a id="claim-01"></a>

### H134-C01 · 원104는 새 실험이 아닌 자원과 근거 감사

2026-09-26 원104는 원103 pending scope를 앞선 감사로 연결한 자원·근거 감사다. new_model_calls=0, new_numeric_experiments=0, research_progress_claimed=false라고 기록했다. 새 성능 결과나 모든 연구 방향의 불가능성을 입증한 기록으로 세지 않는다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행1–4 · [SRC-0020849](../sources/history-134.md#src-0020849) 행10–11 · [SRC-0020849](../sources/history-134.md#src-0020849) 행26–31

<a id="claim-02"></a>

### H134-C02 · 과거 감사 횟수는1에서2로 늘고 Goal은 미완료

원103의 첫 명시적 자원 감사는103/연속1회였고 원104에는 시작103/연속2회로 적었다. 원104의 blocked_threshold_reached=false, goal_status_left_active=true, goal_complete=false를 함께 보존한다. 이 과거 횟수와 상태를 현재 아카이브 Goal의 차단 감사나 완료 판정에 적용하지 않는다.

근거: [SRC-0020848](../sources/history-134.md#src-0020848) 행18–22 · [SRC-0020849](../sources/history-134.md#src-0020849) 행4–6 · [SRC-0020849](../sources/history-134.md#src-0020849) 행26–29

<a id="claim-03"></a>

### H134-C03 · 응답과 제안 승인 미기록 및 질문 반복 없음

원104는 user_response_recorded=false, proposal_is_authorized=false, scope_question_repeated=false, budget_changed=false로 기록했다. 이 파일의 미기록 상태와 모든 외부 대화의 부재를 동일시하지 않는다. 당시 기다림·자동 회차의 경과를 학습 승인으로 읽거나 정리 작업에서 같은 질문을 다시 보내지 않는다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행7–12 · [SRC-0020849](../sources/history-134.md#src-0020849) 행32–35 · [SRC-0020848](../sources/history-134.md#src-0020848) 행7–11

<a id="claim-04"></a>

### H134-C04 · 29fit 소진과 남은Tab 범위는 pinned 원장과 일치

원104의 pinned 원장SHA60b589…는 RCTL29fit 사용/잔여0, Tab2context/4512query행 잔여를 기록했다. 같은 원장의 /used·/remaining_count_budgets·/budget_resets·/research_goal_complete를 선택 대조해 원104·원103의 값과 일치하고 reset0·goalfalse임을 확인했다. 새 모델을 실행해 다시 측정한 것은 아니다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행12–17 · [SRC-0020848](../sources/history-134.md#src-0020848) 행12–17 · [SRC-0002031](../sources/history-134.md#src-0002031) JSON /used, /remaining_count_budgets, /budget_resets, /research_goal_complete

<a id="claim-05"></a>

### H134-C05 · 당시 상한과 이후root 원장의 판본을 구별

감사에 인용된60b589…는 당시 저장 판본이며 이후 root 원장의17a549…와 구별한다. 상한 소진만으로 방법 오류나 성능 기각을 증명하지 않고, 다른partition·단순예측기의 결과를 새partition의 직접 RCTL 확인으로 대신하지 않는다. 정리 작업은 기존 연구 원장이나 학습 범위를 변경하지 않는다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행13–18 · [SRC-0020849](../sources/history-134.md#src-0020849) 행31–32 · [SRC-0020843](../sources/history-134.md#src-0020843) 행5–9 · [SRC-0020843](../sources/history-134.md#src-0020843) 행25–25

<a id="claim-06"></a>

### H134-C06 · 다섯 독립 경로의 재확인은 당시 요약 진술

independent_routes_rechecked의5항목은 후보 색인, 원101 pooled context, 원95 batching, 원102 source/algebra, 남은Tab2context에 관한 당시 요약이다. 이를 원104에서 각 연결 원문·모델·저장 결과의 전문을 새로 재검증하거나 독립 재현했다는 증거로 세지 않는다. 가능한 모든 대안을 전수 기각한 주장도 아니다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행19–25 · [SRC-0020849](../sources/history-134.md#src-0020849) 행31–31

<a id="claim-07"></a>

### H134-C07 · 직접Tab 예측의 긍정 근거와 소속 판단은 별개

원104는 원101의 실제 pooled context가 직접Tab 예측의 이점을 보존하면서 두K4의 선호 순위가 저장 RCTL과 다름을 다시 인용했다. 이 재인용으로 새로운 clustering 규칙이 검증됐다고 하지 않는다. 원101의 실제 기간·입력·평균과 cell별 반례는 이전 검수 기록으로 연결하고 원104의 새 수치 실험으로 집계하지 않는다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행21–21 · [SRC-0020849](../sources/history-134.md#src-0020849) 행10–11

<a id="claim-08"></a>

### H134-C08 · 기본 batching 비용의 재명명은Tab 기여의 새 증거가 아니다

원104는 원95가 이미 확인한 기본 batching 비용을 다른 이름으로 설명해도 Tab 기여의 근거가 추가되지는 않는다고 판단했다. 원95의 실제 CPU/호출/상태·파일 비용과 허용오차는 이전 기록에 연결한다. 원104가 다시 latency를 측정했거나 모든 clustering 비용 개선을 부정했다고 확대하지 않는다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행22–22 · [SRC-0020849](../sources/history-134.md#src-0020849) 행10–11

<a id="claim-09"></a>

### H134-C09 · 원102의 기호 검토와 현재유한RCTL 학습의 연결 공백

원104는 원102의 source/algebra 검토가 현재 유한 RCTL의 Adam·MAE 학습에 대한 동등한 직접 근거를 제공하지 못했다고 썼다. 초기화·극한 이론과 실제 학습 결과의 연결 범위를 보존하며 모든 analytic/RNN kernel 접근의 불가능성이나 새 kernel 실행 실패로 바꾸지 않는다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행23–23 · [SRC-0020849](../sources/history-134.md#src-0020849) 행18–18 · [SRC-0020849](../sources/history-134.md#src-0020849) 행31–31

<a id="claim-10"></a>

### H134-C10 · 남은 두context 소진보다 구별 가능한 계획이 먼저

원104는 남은Tab2context만으로 새partition의 RCTL 후속 확인 공백을 채울 수 없고, 구체적인 판별 계획 없이 이를 쓰는 것은 당시 자원 장애를 해결하지 못한다고 판단했다. 모든 가능한 분석이 무의미하다는 결론은 아니다. 현재 아카이브는 잔여context를 사용하지 않는다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행16–17 · [SRC-0020849](../sources/history-134.md#src-0020849) 행24–24 · [SRC-0020849](../sources/history-134.md#src-0020849) 행31–32

<a id="claim-11"></a>

### H134-C11 · 미승인18fit은후보를 대신하지 않는 조건부상한

앞선 원103 확장문은 새 후보1개와 문헌·실제손해·Tab결정·비교군·seed·중단 조건을 먼저 고정하는 제안이었다. K4후보4+단순비교4+Global1=seed당최대9fit, 선택적두seed18fit/누적최대47fit·추가1440epoch·1800초CPU는 상한 산술이며 승인·실제사용·후보의 확보와 다르다. 원104도 증액만으로 후보가 선정·검증되지 않는다고 남겼다.

근거: [SRC-0020843](../sources/history-134.md#src-0020843) 행1–3 · [SRC-0020843](../sources/history-134.md#src-0020843) 행11–23 · [SRC-0020849](../sources/history-134.md#src-0020849) 행7–8 · [SRC-0020849](../sources/history-134.md#src-0020849) 행32–32

<a id="claim-12"></a>

### H134-C12 · 과거blocked 지침의 조건과 현재정리 작업의 경계

원104 note는 같은 제약의 세 번째 연속 회차에도 의미 있는 독립 경로가 없다면 과거 연구 Goal을 blocked로 처리하라고 적었으며 새 응답이나 구체적인 경로가 생기면 재평가하도록 했다. 이는 원문 속 과거 운영 지침이다. 아카이브의 GitHub 반영 권한·현재 Goal 상태·새 학습 실행 권한을 이 note에서 가져오지 않는다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행29–35 · [SRC-0020848](../sources/history-134.md#src-0020848) 행27–31

<a id="claim-13"></a>

### H134-C13 · 이번확인 범위와 전체기록 정리의 미완료

원104의37행 JSON과 원103의32행 pending/25행 extension을 실제 읽고 당시 원장의4개 JSON필드를 선택 대조했다. 초기3출처/4사본에 원장1출처/6정확사본을 연결한4출처/10경로이며 새 독립 내용은 원104 JSON1개다. 파생 번호·재사용·재독은 새실험이나 새전문으로 세지 않는다. progress132–611/이전122–601, RCTLsummary literal전문, 이후·옛 고유판본/다른형식·통합/팀접근/최종delta/검색10+와 전체Goal은 미완료다.

근거: [SRC-0020849](../sources/history-134.md#src-0020849) 행1–37 · [SRC-0020848](../sources/history-134.md#src-0020848) 행1–32 · [SRC-0020843](../sources/history-134.md#src-0020843) 행1–25 · [SRC-0002031](../sources/history-134.md#src-0002031) JSON /used, /remaining_count_budgets, /budget_resets, /research_goal_complete
