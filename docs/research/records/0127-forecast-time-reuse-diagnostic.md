# 원97 — 저장 RCTL 예측의 시간 재사용과 정확도·비용 기준

> 과거 연구의 조건·결과를 보존한 문서입니다. 새 실험은 [공통 실험 규약](../../research-protocol.md)을 적용하며, 아래 수치는 새 기준의 재평가 결과가 아닙니다.

Global RCTL의 이전 증가량을 현재 관측에 더하면, 2시간 주기의 전체 정규화 MAE는 0.077725였다. 매시간 fresh 0.071068보다 9.3673% 나쁘며, 예측 행과 batch 호출을 절반으로 줄이는 구성의 산술값이다. 허용 가능한 손해나 실제 latency 개선을 확정하지 않았다. 두 K4 fresh보다 작은 전체 평균은 앞·뒤 기간에서 뒤집혔고, 뒤기간 persistence는 global fresh와 재사용보다 더 좋았다.

이 기록은 2026-09-26의 **저장 결과 재분석·개발 진단**이다. 새 Tab/RCTL 학습·추론, 소속 선택, 독립 미래 test는 없었다. 당시 단순 재사용/Tab 부가 방향은 추천하지 않았다. 지금 정리한 검산 역시 모델 재현이 아니다.

[출처21그룹](../sources/history-127.md) · [32개 주장과 위치](../verification/history-127-claims.json) · [작성 후 대조](../verification/history-127-second-pass.json) · [실제 판독/미독](../evidence/0127-forecast-time-reuse-diagnostic/read-scopes.json) · [저장값 검산](../evidence/0127-forecast-time-reuse-diagnostic/numeric-check.json)

## 질문과 실제 수행 범위

같은 cell의 고정 RCTL 예측을 다음 시점에 재사용하면 어느 정도의 정확도 손해로 계산 횟수를 줄일 수 있는가? 원83의 재학습 주기, 원49의 다른 cell 대표 출력, [원95의 동시 batch](0125-frozen-rctl-serving-cost-baseline.md), [원96의 가중치 병합](0126-rctl-parameter-merging-scope.md)과 구별한다. 가중치와 cell 소속을 그대로 유지했다.

16개 cell, target 시간1008–1487의480시간과 앞/뒤240시간을 비교했다. 이미 확인한20일 자료를 다시 썼으므로 독립 test가 아니다. 지표는 원문이 기존28일 평균으로 정규화했다고 기록한 cell별 MAE의 동등 가중 평균이며, raw byte·MAPE·Tab 직접 예측 점수와 혼합하지 않는다. 원시 traffic 정규화를 다시 실행하지 않고 기존 scale·cell·시간 연결을 검산했다. [기존4입력의 hash/팀 위치](../evidence/0127-forecast-time-reuse-diagnostic/input-reuse.json)를 연결했다.

8조건은 primary seed20260925의 global·empirical risk·knn risk·PCC balanced·random balanced·Tab risk와, secondary seed20260926의 empirical/Tab 두 조건이다. 새로운 알고리즘8개나 secondary global 비교로 세지 않는다. 8조건×2mode×4주기×3기간=192결과 행,64출력+4metadata=68배열이다. [선택 결과](../evidence/0127-forecast-time-reuse-diagnostic/selected-metrics.json)에 전체 scalar와 직접 읽은 global6행/persistence3객체를 보존했다.

## 두 재사용 규칙과 시간 연결

배열 위치t에서 마지막 재계산 위치는 `s(t)=d*floor(t/d)`이며, 주기d=1·2·3·6과 위상0을 결과 전에 고정했다. `o_t`는 현재까지 관측한 실제값, `p_s`는 마지막 저장 fresh 예측이다.

- 출력 유지: `p_s`를 다음 재계산 전까지 그대로 쓴다.
- 증가량 유지: `o_t+(p_s-o_s)`를 쓴다. 현재 관측은 매시간 계속 필요하다.

target1008의 최근 실제값은 design.Y의 마지막1007 열이고, 이후는 저장 target의 직전 열이다. 미래 target은 오차 평가에 쓰되 재계산 시점 선택에 쓰지 않았다. 모든 출력 시점을 평가했으며 줄이는 것은 일부 시점의 모델 계산이다. 오래된 한 시간 예측/증가량의 출력 근사이고 현재 신경망 내부의 정확한 cache 갱신이 아니다. 설명용100→110/108은 실제 결과가 아니다.

## 전체와 기간별 결과

아래 값은 primary seed20260925의 cell 평균 정규화 MAE다. 작을수록 좋다. 행/호출은 신경망을 이 방식으로 실행한다면 필요한 횟수의 산술이며 저장 재생의 실제 모델 호출 수가 아니다.

| 모델·재사용 주기 | 출력 유지 | 증가량 유지 | 새 예측 행 | batch 호출 |
|---|---:|---:|---:|---:|
| Global K1,1시간(fresh) |0.071068|0.071068|7,680|480|
| Global K1,2시간 |0.087171|0.077725|3,840|240|
| Global K1,3시간 |0.108567|0.086607|2,560|160|
| Global K1,6시간 |0.194346|0.094615|1,280|80|
| Empirical risk K4,1시간(fresh) |0.081600|0.081600|7,680|1,920|
| Empirical risk K4,2시간 |0.097274|0.089143|3,840|960|
| Tab risk K4,1시간(fresh) |0.087328|0.087328|7,680|1,920|
| Tab risk K4,2시간 |0.101214|0.094313|3,840|960|

Global의 증가량 유지 주기2·3·6은 자체 fresh보다9.3673%·21.8660%·33.1333% 악화했다. 주기3은 전체 persistence0.085135보다도 나쁘다. 주기2가 두 K4 fresh보다 작은 전체 평균은 모델수/호출수가 다른 비교이며 Tab의 기여나 새 partition 성공으로 확대하지 않는다.

| 비교 | 전체480시간 | 앞240시간 | 뒤240시간 |
|---|---:|---:|---:|
| Global fresh |0.071068|0.068523|0.073613|
| Global2시간 증가량 |0.077725|0.078791|0.076659|
| Empirical risk K4 fresh |0.081600|0.071408|0.091793|
| Tab risk K4 fresh |0.087328|0.074603|0.100053|
| Persistence(현재 실제값) |0.085135|0.103898|0.066372|

Global2시간은 앞기간에서 두 K4 fresh보다 나쁘고 뒤기간에서는 좋다. 자체 fresh 대비 악화도 앞14.9846%·뒤4.1384%다. 전체·앞기간의16cell 모두 자체 fresh보다 나빴으며, 뒤기간은2cell 개선/14cell 악화다. 전체의 가장 큰 정규화 MAE 증분은cell5337의0.0145020이다. 뒤기간 persistence0.066372는 global fresh/재사용보다 더 작다.

모든8조건에서 양 mode의 주기2 전체 평균은 해당 fresh보다 나빴지만, secondary empirical의 전체1cell·secondary Tab 주기6의 전체2cell 등 부분 이득은 보존한다. PCC primary의 주기2 뒤기간은 증가량0.111976가 출력 유지0.111818보다 크다. 증가량 유지의 global 전체 이득을 모든 방법·기간으로 일반화하지 않는다.

## 비용·오류·보존 범위

전체 새 예측 행은 `16*ceil(480/d)`, 담당 모델별 동시 batch 호출은 `K*ceil(480/d)`다. 주기2에서도 실제 관측7,680행을 계속 읽는다. 자료 수집·준비·cache 산술·모델 준비를0으로 두거나 예측 행 절반을 latency 절반으로 환산하지 않는다.

`summary.seconds=0.025216200010618195`는 시작 marker 뒤의 입력NPZ/기존 summary 읽기부터 수치 loop 종료까지다. `run_finished.wall_seconds=0.21576900000218302`는 그 구간에 hash/RSS 검사·결과 저장·출력까지 포함한 중첩 구간이다. 둘을 더하지 않으며 짧은 값을 순수 산술 시간으로 부르지 않는다. import·초기 input hash·settings/marker 쓰기는 타이머 밖이다. RSS38,850,560bytes는 종료 부근 한 표본이고 peak가 아니다.

원장은 forecast_reuse_97 한 stage와 detail 한 항목만 추가됐다. cheap69.40678320000966초/recorded modeling1,998.2764094000067초, 모델 사용량·잔여 count 불변을 확인했다. 이번 정리는 원장을 바꾸지 않았다. object 날짜 metadata/pickle 문제와 psutil import 실패는 원문이 성공 실행 전 오류로 보고한 내용이며 이번에 재현하지 않았다. 과거 budget/명령은 연구 자료다.

Snapshot39는 manifest가18파일2,151,527bytes를 열거한다. manifest4,916bytes를 더하면 실제19파일2,156,443bytes다. 별도 receipt531bytes와 after 동일 SHA 사본을 구분했다. 중간 Word의 hash 확인은 본문/layout 판독이 아니다. 연구 코드·로그는 자료로 보존하고 실행하지 않았다.

## 문헌과 후속 설계

[Delta Networks와 Skip RNN의 확인 범위](../references/forecast-time-reuse.md)를 먼저 읽는다. Delta의 고정 행렬/GRU 내부 delta 갱신과 이번 최종 출력 근사, threshold 근사와 정확한 등식을 구별한다. 당시 문헌 다운로드0와 이번 공식PDF의 별도 확인을 섞지 않는다. Skip은 제목·초록·서지까지만 확인했으며 상세 gate/공식 코드/PDF 전체는 미확인이다.

새 후보에는 다음을 명시한다.

1. 단순 주기/현재값/persistence가 놓치는 실제 문제와, Tab이 바꾸는 유용한 실행 결정 또는 같은 유용한 결정의 비용 개선.
2. 하나의 global에서 필요한 cell만 batch로 계산하는 대안보다 clustering으로 모델을 나눌 이유.
3. 미래 target을 결정 시점에 넣지 않는 규칙, 독립 확인 구간, 전체/기간/cell별 손해와 결과 전에 정한 판단 기준.
4. 기본 동시 batch, 관측/준비/cache/Tab 추가 비용을 포함한 실측 latency와 정확도 비교.

이 기록의 미추천을 모든 재사용 연구의 실패로 확대하지 않는다. 같은 실패 조건에 이름만 바꿔 재진입하지 않으며, 달라진 조건과 재사용할 근거를 새 실험 이슈에 연결한다.

## 판독과 검수의 한계

최초 원문1,320행,192행의 선택 scalar 표시,global6개 완전 metric row와persistence3개 cell vector를 실제 읽었다. 작성 후 원문695행·선택 필드·Delta PDF2–4 전체 이미지를 별도로 대조했다. 자체 계산은192개 지표 행/68배열의 모든 수치 규칙을 확인했지만 JSON9,953행 전체·나머지 cell vectors·모든NPZ float를 사람이 읽은 것으로 처리하지 않는다. d=1은 float64로 변환한 fresh와 원소값이 동일한 확인이며 바이트 비교가 아니다. 새 모델·원코드 실행/import·독립 재현0이다.

현재 progress76–554행·이전67–545행, summary literal71–9909행/다른 cell vectors/NPZ 원소, 문헌 나머지 내용은 미독이다. [묶음 범위](../evidence/0127-forecast-time-reuse-diagnostic/packet-coverage.json)에 원98 이후·이전 고유 판본/FedPPBC/DOCX·전체 통합/장기 팀 접근/최종 변경분/대표 질문 검수까지 남겼다. 이 기록의 검수·병합은 전체 Goal 완료가 아니다.

## 검수된 주장과 원문 위치

<a id="claim-01"></a>

### H127-C01 저장 예측을 재분석한 개발 진단

원97(2026-09-26)은 기존 RCTL 예측을 재생해 예측 계산의 주기를 줄이는 단순 기준을 확인한 기록이다. 당시 소속과 모델을 바꾸거나 새 신경망을 호출하지 않았다. 이번 아카이브에서도 저장 배열·수치만 검산했으며 원 연구 코드 실행/import와 새 모델 실행은0이다.

근거: [SRC-0001853 행1–5](../sources/history-127.md#src-0001853) · [SRC-0001855 행1–9](../sources/history-127.md#src-0001855) · [SRC-0001859 행1–5](../sources/history-127.md#src-0001859) · [SRC-0001867 행1–6](../sources/history-127.md#src-0001867); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-02"></a>

### H127-C02 시간 재사용과 재학습·동시 batch의 구분

같은 cell의 이전 예측을 다음 시점에 재사용하는 것은 원83의 재학습 주기, 원49의 다른 cell 대표 출력, 원95의 같은 시각 cell 묶음 호출과 다른 결정이다. 이번 변경은 시간축에서 일부 RCTL 계산을 생략하는 구성이고, 기존 partition을 다시 선정한 작업이 아니다.

근거: [SRC-0001854 행5–9](../sources/history-127.md#src-0001854) · [SRC-0001855 행7–20](../sources/history-127.md#src-0001855) · [SRC-0001857 행72–78](../sources/history-127.md#src-0001857); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-03"></a>

### H127-C03 16cell·480시간·이미 사용한 확인 구간

기존16cell의 target시간1008–1487을 전체480시간과 앞/뒤240시간으로 비교했다. 이전에 확인한20일 자료를 다시 사용했으므로 독립적인 미래 test가 아니라 개발 진단이다. 저장 조건도 independent_test=False, changed_partitions=False로 남아 있다.

근거: [SRC-0001854 행11–16](../sources/history-127.md#src-0001854) · [SRC-0001855 행3–3](../sources/history-127.md#src-0001855) · [SRC-0001869 행33–53](../sources/history-127.md#src-0001869) · [SRC-0001870 JSON 위치2개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-04"></a>

### H127-C04 정규화 MAE와 cell별 동등 가중

지표는 원문이 기존28일 평균으로 정규화했다고 기록한 cell별 MAE의 동일 비중 평균이다. 저장 scale과 cell 순서를 기존 입력에 대조했고, 전체/기간별 mean·cell값을 검산했다. 원단위 byte·MAPE·Tab 직접 예측 점수와 혼합하지 않는다. 원시 traffic을 다시 정규화하거나 새 모델 예측을 만든 작업은 아니다.

근거: [SRC-0001855 행24–24](../sources/history-127.md#src-0001855) · [SRC-0001859 행38–51,79–91](../sources/history-127.md#src-0001859) · [SRC-0001870 JSON 위치1개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-05"></a>

### H127-C05 첫 현재값1007와 이후 관측의 연결

시간1008을 예측할 때의 최근 실제값은 design.Y의 시간1007 열에서 가져온다. 이후에는 저장 target의 직전 열을 현재 관측으로 사용한다. 실제 cell·scale·시간 연결을 검산했으며, 해당 시점의 미래 target을 재계산 시점 선택에 사용하지 않는 규칙이다.

근거: [SRC-0001854 행14–19](../sources/history-127.md#src-0001854) · [SRC-0001859 행38–56](../sources/history-127.md#src-0001859) · [SRC-0001866 NPZ 배열4개](../sources/history-127.md#src-0001866); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-06"></a>

### H127-C06 사전 고정한 주기와 시작 위상

재계산 주기는1·2·3·6시간, 시작 위상은0으로 고정했다. 배열 위치t에서 가져올 마지막 예측 위치는 s(t)=d·floor(t/d)다. 결과를 본 뒤 유리한 위상·threshold·partition을 고르지 않았으며, 모든 시점의 예측을 계속 평가한다.

근거: [SRC-0001854 행16–23](../sources/history-127.md#src-0001854) · [SRC-0001869 행22–46](../sources/history-127.md#src-0001869) · [SRC-0001859 행55–77](../sources/history-127.md#src-0001859); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-07"></a>

### H127-C07 출력 유지 규칙

hold_output은 마지막 재계산 시점s의 저장 예측 p_s를 다음 재계산 전까지 유지한다. 설명에 쓰인100→110 또는108의 숫자는 실제 결과가 아니라 동작 예시다. 오래된 한 시간 예측을 현재 시점에 재사용하는 근사이며 현재 RCTL의 동일 출력을 보장하지 않는다.

근거: [SRC-0001853 행7–11](../sources/history-127.md#src-0001853) · [SRC-0001855 행11–20](../sources/history-127.md#src-0001855) · [SRC-0001859 행69–78](../sources/history-127.md#src-0001859); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-08"></a>

### H127-C08 증가량 유지 규칙과 계속 필요한 관측

hold_increment는 현재 관측 o_t에 마지막 예측 증가량(p_s−o_s)을 더한다. 저장된 함수는 o_t+(p_s−o_s)이며, 모델 재학습이나 신경망 내부 cache 갱신은 아니다. 새로운 실제 관측값을 매시간 계속 사용하므로 관측·통신 비용까지 제거한 방식으로 해석하지 않는다.

근거: [SRC-0001854 행17–25](../sources/history-127.md#src-0001854) · [SRC-0001855 행13–20](../sources/history-127.md#src-0001855) · [SRC-0001859 행69–91](../sources/history-127.md#src-0001859); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-09"></a>

### H127-C09 8개 방법·seed 조건과192개 결과

8개 저장 조건은6개 primary 방법·추가2개 secondary seed 조건이다. 이8조건×2재사용 방식×4주기×3기간이192개 결과 행을 이룬다. NPZ에는64개 재사용 출력과 y/current_observation/cell_ids/target_times의4개 metadata 배열이 있다. seed 조건을 새로운 알고리즘8개로 세지 않는다.

근거: [SRC-0001859 행52–91](../sources/history-127.md#src-0001859) · [SRC-0001862 행47–75](../sources/history-127.md#src-0001862) · [SRC-0001870 JSON 위치3개](../sources/history-127.md#src-0001870) · [SRC-0001866 NPZ 배열4개](../sources/history-127.md#src-0001866); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-10"></a>

### H127-C10 주기1 및 재계산 시점의 불변 조건

원 구현은 d=1과 refresh 위치의 출력이 저장된 fresh 예측과 atol1e-15 이내로 같음을 검사했다. 이번 검산에서 d=1의16개 배열은 fresh 예측을 float64로 변환한 배열과 원소값이 완전히 같았고, 모든 refresh·재사용 규칙도 일치했다. np.array_equal로 확인한 수치적 동일성이며 바이트 비교·신경망 재실행·모든 원소의 사람 직접 판독을 뜻하지 않는다.

근거: [SRC-0001859 행73–77](../sources/history-127.md#src-0001859) · [SRC-0001862 행56–75](../sources/history-127.md#src-0001862) · [SRC-0001870 JSON 위치1개](../sources/history-127.md#src-0001870) · [SRC-0001866 NPZ 배열16개](../sources/history-127.md#src-0001866); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-11"></a>

### H127-C11 예측 행과 모델 호출의 산술

전체480시간에서 필요한 새 예측 행은16×ceil(480/d), 동일 시각 cell을 담당 모델별로 batch 처리하는 호출은K×ceil(480/d)다. 주기2에서 행7,680→3,840, global 호출480→240, K4 호출1,920→960이다. 이는 해당 방식을 실행할 때의 산술값이며 이번에 그 횟수만큼 모델을 실행한 측정치가 아니다.

근거: [SRC-0001854 행25–25](../sources/history-127.md#src-0001854) · [SRC-0001859 행83–91](../sources/history-127.md#src-0001859) · [SRC-0001870 JSON 위치4개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-12"></a>

### H127-C12 관측·준비 비용과 실측 latency의 미확인

주기2의 재사용에서도 전체 관측 행7,680은 유지한다. 자료 수집·입력 준비·cache 산술·모델 준비의 비용을0으로 두지 않으며, 예측 행 절반을 실제 latency 절반으로 환산하지 않는다. 저장 조건과 결과는 새 모델 실행·실측 speedup을 명시적으로 부정한다.

근거: [SRC-0001854 행25–25](../sources/history-127.md#src-0001854) · [SRC-0001855 행37–39](../sources/history-127.md#src-0001855) · [SRC-0001869 행48–53](../sources/history-127.md#src-0001869) · [SRC-0001870 JSON 위치3개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-13"></a>

### H127-C13 Global 주기2의 두 재사용 방식

primary global의 fresh 정규화 MAE는0.071068이다. 주기2에서는 출력 유지0.087171, 증가량 유지0.077725다. 증가량 유지의 fresh 대비 악화는9.3673%이며, 이를 허용 가능한 손해나 성공 기준으로 정하지 않았다. 이번 수치는 저장 결과를 다시 계산해 확인했다.

근거: [SRC-0001855 행26–39](../sources/history-127.md#src-0001855) · [SRC-0001870 JSON 위치4개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-14"></a>

### H127-C14 주기3·6과 persistence를 넘는 손해

global 증가량 유지의 전체 MAE는 주기3에서0.086607, 주기6에서0.094615로 fresh보다 각각21.8660%·33.1333% 크다. 주기3은 persistence 전체0.085135보다도 크다. 더 적은 예측 행만으로 모델 사용의 이득이나 허용 가능한 정확도를 확정하지 않는다.

근거: [SRC-0001855 행28–31,50–52](../sources/history-127.md#src-0001855) · [SRC-0001870 JSON 위치5개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-15"></a>

### H127-C15 K4 fresh보다 작은 전체 평균의 범위

global 주기2 증가량 유지0.077725는 같은 primary seed의 empirical K4 fresh0.081600와 Tab K4 fresh0.087328보다 전체 평균에서 작았다. 모델수K·호출 수가 다르며, 이 비교를 Tab 소속의 효용이나 새 partition의 성공으로 해석하지 않는다. 기존 같은K4에서의 Tab 판정도 이 비용 진단으로 바꾸지 않는다.

근거: [SRC-0001855 행28–39](../sources/history-127.md#src-0001855) · [SRC-0001870 JSON 위치3개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-16"></a>

### H127-C16 앞·뒤240시간에서 뒤집히는 비교

앞240시간에서는 global 주기2가0.078791로 empirical/Tab K4 fresh0.071408/0.074603보다 크지만, 뒤240시간에서는0.076659로0.091793/0.100053보다 작았다. global 자체 fresh 대비 악화도 앞14.9846%·뒤4.1384%로 다르다. 전체 평균의 비교 우위를 모든 기간의 우위로 확대하지 않는다.

근거: [SRC-0001855 행41–50](../sources/history-127.md#src-0001855) · [SRC-0001870 JSON 위치6개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-17"></a>

### H127-C17 Global 주기2의 cell별 손해

global 주기2 증가량 유지의 전체·앞기간에서는16cell 모두 fresh 대비 MAE가 컸다. 뒤기간에는2cell이 작고14cell이 컸다. 전체의 가장 큰 정규화 MAE 증분은cell5337의0.0145020이다. 평균 비교와 cell별 손해를 함께 보존하며 이 정규화 증분을 원단위 평균으로 바꾸어 쓰지 않는다.

근거: [SRC-0001870 JSON 위치5개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-18"></a>

### H127-C18 뒤기간의 단순 persistence 기준

persistence MAE는 전체0.085135·앞0.103898·뒤0.066372다. 뒤기간에서는 global fresh0.073613와 global 주기2 증가량 유지0.076659보다 작았다. 전체에서 global 재사용이 persistence보다 좋다는 관찰을 두 기간 모두의 우위로 읽지 않는다. 이 대조는 저장 근거 판독에서 함께 명시한 한계다.

근거: [SRC-0001870 JSON 위치3개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-19"></a>

### H127-C19 seed와 일부 cell의 이득을 보존한다

모든8개 방법·seed 조건에서 두 mode의 주기2 전체 평균은 해당 조건의 fresh보다 악화했지만, secondary empirical 조건의 전체1cell 등 부분 이득이 있다. secondary Tab의 주기6 전체에서도2cell이 이득이다. primary global 한 조건만 저장되어 secondary global 비교는 없다. seed·기간·cell 조건이 다른 결과를 하나의 보편적 판정으로 합치지 않는다.

근거: [SRC-0001855 행24–24](../sources/history-127.md#src-0001855) · [SRC-0001870 JSON 위치84개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-20"></a>

### H127-C20 증가량 유지가 모든 조건에서 더 좋지는 않다

PCC primary의 주기2 뒤기간에서는 증가량 유지0.111976가 출력 유지0.111818보다 크다. 따라서 global 전체 평균에서의 장점을 모든 모델·기간의 규칙으로 일반화하지 않는다. 두 mode와 네 주기를 함께 보존한192행의 범위 안에서 판단한다.

근거: [SRC-0001870 JSON 위치2개](../sources/history-127.md#src-0001870) · [SRC-0001855 행20–24](../sources/history-127.md#src-0001855); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-21"></a>

### H127-C21 Tab의 유용한 실행 결정과 clustering의 역할

이번 재사용 규칙에는 Tab이나 새 clustering이 필요하지 않았다. 후속에는 단순 주기·최근 실제값보다 유용한 실행 결정인지, 필요한 cell만 global에서 계산하는 대안보다 소속 분리가 필요한지와 전체 비용을 명시한다. 원93의 기준처럼 같은 유용한 결정을 더 효율적으로 얻는 방향도 구별하며, 이번 미추천을 모든 재사용 연구의 실패로 확대하지 않는다.

근거: [SRC-0001855 행62–71](../sources/history-127.md#src-0001855) · [SRC-0001857 행42–58,72–78](../sources/history-127.md#src-0001857); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-22"></a>

### H127-C22 새 모델 호출과 partition 선택은 없었다

계획·runner·완료 기록은 새 Tab context/query, RCTL fit/forward/gradient가 없고 저장 예측만 재생했다고 남긴다. 재계산 시점은 clock으로 정했고, RCTL의 새 오차·표현으로 소속을 바꾸지 않았다. 기록된 과거 fit0 상한은 현재 아카이브의 실행 지시가 아니며 미래 팀 연구 전체의 금지로도 옮기지 않는다.

근거: [SRC-0001854 행29–31](../sources/history-127.md#src-0001854) · [SRC-0001859 행1–5,69–103](../sources/history-127.md#src-0001859) · [SRC-0001867 행1–6](../sources/history-127.md#src-0001867) · [SRC-0001856 행62–70](../sources/history-127.md#src-0001856); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-23"></a>

### H127-C23 두 타이머의 실제 포함 범위

summary.seconds=0.0252162000초는 settings/시작 marker 저장 뒤부터 입력NPZ·이전 summary 읽기와 수치 loop 종료까지다. finally의0.2157690000초는 그 구간에 hash/RSS 검사·NPZ/JSON 쓰기·출력까지 포함한다. 짧은 값을 순수 산술 시간으로 부르거나 둘을 더하지 않는다. import·초기 input hash·settings/marker 쓰기는 이 타이머 밖이다.

근거: [SRC-0001859 행22–37,92–113](../sources/history-127.md#src-0001859) · [SRC-0001861 행19–27](../sources/history-127.md#src-0001861) · [SRC-0001865 행1–8](../sources/history-127.md#src-0001865) · [SRC-0001867 행1–6](../sources/history-127.md#src-0001867) · [SRC-0001870 JSON 위치1개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-24"></a>

### H127-C24 RSS는 끝 시점 표본이다

저장 RSS는38,850,560bytes이며 수치 loop 뒤의 한 번 측정이다. 원문 필드도 rss_bytes_end_not_peak라고 표시한다. 지속 peak나 전 구간의 메모리 상한 준수로 강화하지 않는다. 계획의20초/1GB와 코드의 끝점 검사 및 실제 저장 시간·RSS를 구분한다.

근거: [SRC-0001854 행31–31](../sources/history-127.md#src-0001854) · [SRC-0001859 행92–99](../sources/history-127.md#src-0001859) · [SRC-0001869 행48–53](../sources/history-127.md#src-0001869) · [SRC-0001870 JSON 위치1개](../sources/history-127.md#src-0001870); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-25"></a>

### H127-C25 원장 증분을 한 번만 반영했다

before ad8926…와 after807600…를 대조하면 forecast_reuse_97의0.2157690000초와 대응 detail 한 항목만 추가됐다. 내부0.0252162000초는 포함 항목이며 중복 비용이 아니다. 모델 사용량·잔여 count는 같고, cheap69.4067832초·recorded modeling1,998.2764094초를 검산했다. 현재 원장은 변경하지 않았다.

근거: [SRC-0001861 행17–39](../sources/history-127.md#src-0001861) · [SRC-0001865 행1–15](../sources/history-127.md#src-0001865) · [SRC-0001858 행93–126,246–260](../sources/history-127.md#src-0001858); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-26"></a>

### H127-C26 사전 메타데이터·import 오류의 범위

원문은 object 날짜 배열을 읽으려던 메타데이터 점검과 psutil import 실패를 run marker·수치 작업 전의 오류로 기록한다. 성공 실행의 marker·완료·결과는 보존돼 있다. 실패 로그를 이번에 독립 재현한 것은 아니며, 이를 재사용 방법의 성능 실패로 분류하거나 원 코드를 실행해 복구하지 않는다. 현재 검산은 numeric 배열만 allow_pickle=False로 읽었다.

근거: [SRC-0001855 행73–79](../sources/history-127.md#src-0001855) · [SRC-0001859 행1–31](../sources/history-127.md#src-0001859) · [SRC-0001858 행255–259](../sources/history-127.md#src-0001858) · [SRC-0001868 행1–4](../sources/history-127.md#src-0001868) · [SRC-0001867 행1–6](../sources/history-127.md#src-0001867); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-27"></a>

### H127-C27 Snapshot39와 입력·Word 보존

Snapshot39의 manifest는18파일2,151,527bytes를 열거하며 manifest4,916bytes를 더한 실제 파일은19개2,156,443bytes다. 별도 receipt는531bytes다. after 사본1863과1858은 같은 SHA 그룹이며 입력4개의 hash를 확인했다. 중간 Word의 hash4f1112… 확인은 본문·layout 독해가 아니다.

근거: [SRC-0001852 행1–118](../sources/history-127.md#src-0001852) · [SRC-0001862 행172–198](../sources/history-127.md#src-0001862) · [SRC-0022102 행1–13](../sources/history-127.md#src-0022102) · [SRC-0001869 행4–20](../sources/history-127.md#src-0001869); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-28"></a>

### H127-C28 Delta Networks의 내부 계산 재사용과 출력 근사

Delta Networks(ICML2017) §2 식2–5는 고정 행렬의 이전 결과와 입력 변화량으로 같은 선형 결과를 계산하는 등식이다. §3은 GRU 내부 preactivation에 적용하며, §4의 threshold 근사는 마지막으로 기억한 값·오차 누적을 별도로 다룬다. 출력 오차가 같은 threshold로 제한된다는 보장은 없다. 원97의 최종 출력/증가량 유지는 이 내부 알고리즘의 RCTL 구현이 아니며 논문 속도 수치를 가져오지 않는다.

근거: [SRC-0001855 행54–58](../sources/history-127.md#src-0001855) · [SRC-0001856 행18–32](../sources/history-127.md#src-0001856); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-29"></a>

### H127-C29 Skip RNN은 초록·서지까지만 확인했다

당시 기록은 Skip RNN의 학습 기반 state update 생략을 초록·서지에서 확인했고 OpenReview 전문의 확인 화면을 기록한다. 이번에는 arXiv1708.06834v3의 제목·초록·저자·2018-02-05 개정과 ICLR2018 서지를 대조했다. 전체 알고리즘·공식 코드·PDF는 검증하지 않았고, 당시 접근 실패를 현재의 접근 실패로 재사용하지 않는다.

근거: [SRC-0001855 행60–60](../sources/history-127.md#src-0001855) · [SRC-0001856 행33–47](../sources/history-127.md#src-0001856); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-30"></a>

### H127-C30 기계 검산·직접 판독·독립 재현의 구분

이번 자체 검사에서192행의 scalar/cell 지표와68개 배열의 시간·cell·재생 규칙은 모두 일치했다. 최초 직접 판독은 원문1,320행,192행의 선택 scalar projection,global6개 완전 metric row·persistence3개 cell vector와 문헌3페이지 이미지 범위다. summary9,953행의 전체 literalJSON·나머지 cell vectors·모든NPZ float의 직접 독해나 독립 모델 재현을 완료 처리하지 않는다.

근거: [SRC-0001862 행47–75](../sources/history-127.md#src-0001862) · [SRC-0022102 행5–12](../sources/history-127.md#src-0022102) · [SRC-0001870 JSON 위치2개](../sources/history-127.md#src-0001870) · [SRC-0001866 NPZ 배열4개](../sources/history-127.md#src-0001866); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-31"></a>

### H127-C31 후보·연혁의 다른 판본과 미독 구간

현재 candidate1857은78행 전체를 읽었고 이전1828의70행 판본과 비교했다. 현재 progress1860은1–75/554행만 읽어76–554행이 남는다. 이전1831의67–545행도 미독이다. 판본의 기계 대응과 같은 과거 결과의 재인용을 후반 기록 독해나 독립 연구 여러 회로 집계하지 않는다.

근거: [SRC-0001857 행72–78](../sources/history-127.md#src-0001857) · [SRC-0001860 행7–23](../sources/history-127.md#src-0001860); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

<a id="claim-32"></a>

### H127-C32 미추천과 전체 Goal의 미완료

당시 단순 시간 재사용 또는 Tab 부가 후보는 추천 방향으로 채택되지 않았고 최종 방향·Word도 미완료였다. 이번 진단은 후속 비용 후보가 비교할 단순 기준을 구체화한 것이다. 원98 이후·이전 고유 판본, 문헌·연혁·JSON 미독, FedPPBC/DOCX 공백, 통합·장기 팀 접근·최종 변경분·대표 질문 검수는 계속 남아 있다. 원97 기록의 검수·병합을 전체 Goal 완료로 표시하지 않는다.

근거: [SRC-0001853 행31–37](../sources/history-127.md#src-0001853) · [SRC-0001855 행62–81](../sources/history-127.md#src-0001855) · [SRC-0001860 행9–14](../sources/history-127.md#src-0001860); 상세 위치는 [주장 근거](../verification/history-127-claims.json) 참조.

후속 [원98](0128-quantile-information-and-pooling-objective.md)은 저장 예측 재사용 실험을 추가하지 않고, 중앙값 주변 정보량과 공유 목적의 차이를 문헌·기호 모형·설치 코드로 확인했다. 원97의 비용 기준과 원98의 유한 추정 논의를 같은 성능 실험으로 합치지 않는다.
