# H027 검수: 저장 공간 입력 선택과 당시 비용

45–46과 47 §2/§7 수치·보존 부분의 주요 주장 14개를 원문에 대조했다. [팀용 기록](../records/0045-0046-input-stability.md), [출처](../sources/history-027.md), [기계 판독 주장 목록](history-027-claims.json)을 연결한다. 같은 에이전트의 두 번째 원문 대조이며 독립 연구자의 재현으로 표시하지 않는다.

- [저장 산술 검사](history-027-saved-check.json): 146개 수치 필드. 전체·cell별·주별·부분집합·양/음 delta 합·선택 index/count·oracle·교집합과 18의 8개 평균을 확인했다. 한 배열 비교를 그 원소 수만큼 부풀려 세지 않았다.
- [계보/원장 검사](history-027-lineage-check.json): 46개 검사. 이전 H012의 원본과 감사 파일 해시, cell/시간/정답 순서, snapshot10의 46까지 비용, 현재 원장의 같은 prefix, 보존 시 코드 해시와 원 연구 통제파일 6개를 연결했다.
- [본문 표·파일 검사](history-027-document-check.json): 저장값을 다시 읽어 본문 숫자 행, 출처 사본, 주요 범위 문구를 확인했다. 자동 검사가 문장 의미 검수를 대신하지 않는다.

| 주장 | 확인한 내용 | 근거 위치 | 한계 |
|---|---|---|---|
| H027-C01 | 45의 입력 공유 질문과 46의 저장 재분석; 새 모델 0 | 45 전체;46 코드1–34/87–91;settings/start/finish | 과거 계획은 현재 실행 지시가 아님 |
| H027-C02 | 32개 cell·336시간·float64·앞뒤168시간 동일성 | 46 settings/result;18 NPZ;temporal NPZ의 cell_ids/times/Y | 개발 구간이며 새 독립 시험이 아님 |
| H027-C03 | 첫672시간 cell별 정규화와 학습/평가 시간 | 18 코드17–46;H012 local-data/risk check | 실제 과거 확장 X는 저장되지 않음 |
| H027-C04 | 16/24/24/80열·경계/PCC·Ridge/HGB 설정 | 18 코드24–65;18 run_started | 방향의 실제 지리 매핑·전체 환경 재현 아님 |
| H027-C05 | 8조건 전체/기존16/추가16/주별 MAE와 두 주 개선 수 | 46 result.models.*.variants;18 NPZ | 반올림 전 <0로 개선 판정 |
| H027-C06 | 교집합2/2/1개와 cell목록 | 46 result.cross_model_stability;18 NPZ | 사후 개발 집합을 성공 cell 선정 기준으로 사용하지 않음 |
| H027-C07 | 평균과 부분집합·기간별 손해가 함께 존재 | 46 variants MAE_original16/MAE_additional16/MAE_by_week | 모든 공간 신호의 무용성이나 일반 성능 우위로 확대하지 않음 |
| H027-C08 | 첫 주 cell·회귀기별 argmin과 동률 순서 | 45 계획;46 코드55–69;selected_variant_index_by_cell | 두 번째 주 labels는 첫 주 선택에 들어가지 않음 |
| H027-C09 | 선택 MAE·차이·선택 수·개선 수·oracle 일치 | 46 first_week_selection;18 NPZ | 모델 재적합 없이 저장 출력만 선택 |
| H027-C10 | oracle 미래 정답 사용과 직접 순위 비교 한계 | 46 second_week_label_oracle;47§2 | Tab 우위·RCTL grouping 개선이나 다른16cell/480h순위가 아님 |
| H027-C11 | 0.030364초와 RSS35,512,320의 측정 경계 | 46 코드25/76–87;result/finish;47§7 | 실제 연속 peak·전체 preprocessing wall 아님 |
| H027-C12 | 당시 cheap/modeling·호출·잔여와 단일 반영 | snapshot10 ledger;currentledger prefix;update_budget code | 저장 원장의 일관성; 미기록 실행 부재 증명 아님 |
| H027-C13 | 원본/계획/설정 identity와 보존 시 코드 해시 | settings/start;스냅샷manifest의 지정9행/코드hash | 코드 해시는 실행 전 필드가 아님;전32파일본문검수아님 |
| H027-C14 | 소속·추천 변경 없음과 재검토 범위 | 46 result의두false;45판단기준;47§2 | 47문헌·논리·규모·종합은후속검수;전체Goal미완료 |

첫 주 선택은 Ridge에서 다음 주 MAE가 +0.000147, HGB에서 −0.000509 변했다. 교집합은 입력별 2/2/1개이며 일부 긍정 결과를 버리지 않았다. HGB 전체의 작은 이웃 평균 이득과 다음 주 평균 손해도 함께 표시했다. oracle의 미래 label, 개발 구간 재사용, 지표 정규화, RCTL 평가와 다른 조건을 본문에 명시했다.

새 연구 모델 실행·원 코드 import/실행·난수 추출은 0이다. 검수 때문에 원장이나 원 연구 상태를 갱신하지 않았다. 문서/근거 묶음은 기존 archive CI의 해시·링크 검사를 사용하며 새 모델 실험이나 구현과 같은 내용을 반복하는 테스트를 추가하지 않았다.

47의 원논문·GECOS 입력 역할·AR 반례·Tab 작업량 산술·전체 미추천 종합과 후속75는 다음 범위다. 전논문/전코드/전체 실패 비용·전수 팀 접근·최종 원본 변경분·대표 검색 검수는 미완료다. 이 묶음 병합을 전체 연구기록 정리 완료로 세지 않는다.

후속 업데이트: 위 H027 수행 시점에 대기였던 47의 문헌·입력 역할·논리·작업량·종합은 [H028 기록](../records/0047-input-sharing-roles.md)으로 검수했다. H027의 원래 수치 검수 범위는 그대로이며, 후속75와 전수 범위는 남아 있다.
