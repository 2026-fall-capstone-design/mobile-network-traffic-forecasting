# H029 검수: 합계와 cell 복원

[팀용 기록](../records/0048-0049-aggregation-recovery.md)의 주요 주장16개를 원문과 저장 근거에 대조했다. 같은 에이전트의 두 번째 검수이며 독립 연구자의 재현은 아니다. [주장 목록](history-029-claims.json), [출처와 실제 독해](../sources/history-029.md)

- [저장 산술 검사](history-029-saved-check.json):1,025개 확인, 그중231수치필드 비교. 지정H5자료·scale·정답·52배열·48복원정의·median최적조건·지표·항등식·원단위범위·toy·기록된비용을 검산했다. 원소 수로 검사수를 부풀리지 않았다.
- [계보와cell손해 검사](history-029-lineage-check.json):64개 확인. source15·새사본11·재사용3·통제6, 원장prefix/스냅샷행/시간경계, PCC대무작위의cell별델타와원단위손해를 연결했다.
- [문서 검사](history-029-document-check.json): 본문 표를 저장값에서 다시 만들고 사본해시·핵심한계 문구를 확인한다. 문장 의미는 별도 원문 재독으로 검수했다.

| 주장 | 내용 | 근거 | 한계 |
|---|---|---|---|
| H029-C01 | 합계압축 질문과49의실제산술·모델0범위 | 48계획;49코드/설정/start/finish/result | 새RCTL/Tab실험·최종채택 아님 |
| H029-C02 | 같은32cell과원자료·정답·scale·query연결 | 49settings/NPZ;18NPZ;H5지정구간 | 초기design_data수정의전체이력은계획보고 |
| H029-C03 | 672시간척도/PCC와336시간개발구간·1시간가용성 | 48계획;49코드35–61;H027시간검수 | 독립시험/336시간재귀 아님 |
| H029-C04 | partition규칙과무작위seed의검수한계 | 49greedy/groupsets;result.cell_groups | seed난수재생0;1그룹/8그룹비용차이 |
| H029-C05 | 세비중·네scalar와가용과거/미래구별 | 49normalize_rows/loop;48계획 | zero참조합계분기는정적확인만 |
| H029-C06 | true_total과best_scalar의비동등성·toy | 49best_scalar/toy;50수치절 | 고정비중·비음수scalar의사후하한 |
| H029-C07 | normalized/raw·주별/cell별/그룹총량지표 | 49metrics/total_errors;result | 배열비교는필드1개;척도·분모혼동금지 |
| H029-C08 | 직전비중4partition결과와원단위손해 | result.groups.*.allocation.last | 정규화최적이원단위최적아님 |
| H029-C09 | PCC대무작위평균·주별이득과16cell손해 | 저장true_total last cell/week metrics | 사후개발진단·모든cell개선아님 |
| H029-C10 | 세비중복원결과와두과거기준값 | 12allocation의true_total;baselines | 모든도시·horizon으로확대안함 |
| H029-C11 | 직전/전날비중×동일합계의항등식 | 49loop assertions;저장NPZ | 다른새예측의독립성과로세지않음 |
| H029-C12 | 원단위삼각부등식과정규화계수·RCTL범위 | 49rawL1checks;50RCTL절 | RCTL학습가능성/이득보장아님 |
| H029-C13 | numeric타이머/RSS와UTC표시간격 | 49코드timer/serialization;start/finish/result | 전체wall/연속peak아님;시간중복합산금지 |
| H029-C14 | snapshot10→11한cheap항목과모델·잔여일관성 | snapshot10/11/currentprefix;manifestledger행 | 미기록실행부재·전체비용증명아님 |
| H029-C15 | N/4출력수와계산단위·미측정속도 | 50비용절;49PCC정적코드 | 모델수/출력수/호출수/지연시간구별 |
| H029-C16 | 당시미채택의수치적범위·재사용·50잔여 | 48판정;50수치/비용절;저장근거 | 문헌·신규성종합은후속;전체Goal미완료 |

평균 이득과불리한조건을함께남겼다. PCC대무작위의직전비중/실제미래합계조건은평균−0.016330이지만16개cell이악화된다. 정규화최적scalar가원단위MAE를늘리는사례도보존했다. 두oracle의미래정답, 개발구간재사용, 다른비중/출력구조에는적용되지않는하한을명시했다.

현재새학습/추론/forward/원코드실행/난수생성0. 저장무작위partition만확인했고seed재생은하지않았다. 0참조합계분기는관측되지않아정적독해범위로남겼다. 모델실험이나원자료전체전처리재현성공으로표시하지않는다. 기존archiveCI로바이트/목록/링크를검사하며새연구테스트를추가하지않았다.

50문헌HiGP/ONDM/HTS-Cluster·신규성종합·접근렌더·별도보고서·후속191/392는남아있다. 전체고유내용·실패비용·팀접근·최종원본변경·대표검색QA도미완료다. 이번PR이전체Goal완료는아니다.
