# 검색 응답과 배포 metadata의 해석 범위

[범위 JSON](search-scope.json) · [출처](../../sources/history-078.md) · [C29–C34](../../records/0078-dynamic-graphs-load-balancing.md#c29)

저장 검색 응답11개를 전부 읽었다. 과거 검색 결과에는 본문이 부분적으로 들어 있어도 생략된 절·표·그림이 있다. 전체 응답 독해와 문헌 전체 검토를 구분한다.

| 저장 key | 남아 있는 내용과 처리 |
|---|---|
| 77_initial_0 | Cash 등의2025/2026 arXiv 초록·메타, DynaSTar공식메타. OD flow와cell자료를구별 |
| 77_initial_1 | 이전05기록/progress의문헌항목검색출력. 독립실험결과가아님 |
| 77_search_b | 2025DLM초록,DTGARCH학회초록,day-type/도로/소형셀/C-RAN등검색부분문. 관련성후보와직접증거구별 |
| 77_search_c | Liu그림설명,FedCAP초록·도입부,SIGMAformer,Fuzzy초록,C-RAN·일반forecast·FL등부분문 |
| 77_search_d | Fuzzy초록·도입부의CPAGM설명,MoE·관련연구snippet,arXiv메타,Wiley/ScienceDirect열기응답 |
| 77_dynamic_meta | 2020DLM arXiv메타와초록,Wileytimeout |
| 77_fuzzy_page | ScienceDirect403 |
| 77_search_e | Fuzzy서지/저자CV,2025DLM초록·일부참고문헌,FedCAP부분문,기타FL검색결과 |
| 77_collect_0 | DLM/DynaSTar2PDF수집의URL·크기·해시·쪽수,추출회전글자경고 |
| 77_collect_1 | 저자홈페이지와MDPI429. 연락처·개인이력은방법근거로재게시하지않음 |
| 77_code_lookup_final | dynmix commit/tree API의당시웹도구접근실패. H077에서확보한고정응답과구별 |

서로 다른 의미의 동적 군집을 검색 결과 순서대로 하나의 계보로 합치지 않는다. 예를 들어 C-RAN 용량·배치 목적의 보완성 군집, 도로의 day-type, 기후 GMM, 전문가 routing은 목적과 결정 단위부터 다르다. 무관한 LLM 목록·상용 문헌 판매 페이지·다른 분야의 연관 검색은 그 논문의 원문을 검수했다는 근거가 아니다.

## 판본과 부분 공개의 구별

| 문헌 | 이번에 확인한 범위 | 아직 하지 않은 것 |
|---|---|---|
| [2025 DLM 저널판](https://doi.org/10.1002/sam.70044) | 저장초록의78국/1960–2007/3변량; 2020v1과표본·기간·변량다름 | 저널전문·새방법차이·실행판본검수 |
| [Fuzzy CPAGM 확장](https://doi.org/10.1016/j.fss.2025.109748) | 저장초록·도입부:global모델별검증오차에의한소속,모델예측의가중결합. 직접열기403도기록됨 | 전체방법·결과표·코드검수,우리자료효용측정 |
| [FedCAP](https://www.mdpi.com/2673-4001/7/4/104) | 저장부분문:training-only profile의고정군집→군집별LSTM→동결backbone+clientadapter | 전문·원시seed결과·코드검수;동적UPC효과판정 |

Fuzzy 도입부에 있는 CPAGM의 train/validation 분리와 최종 refit 설명은 **인용된 선행 방법의 설명**이다. 그것만으로 해당 Fuzzy 알고리즘 전체의 정확한 훈련 순서를 확정하지 않는다. 초록의 최고 개선율이나 FedCAP의 seed별 통계도 본문 전체 및 원시 결과와 확인하기 전에는 우리 실험의 수치표에 섞지 않는다.

## dynmix 배포물

저장 PyPI JSON은1.1.2 sdist의2019-10-05T00:13:57.802786Z 업로드,16,651바이트, SHA-256 `3c0177ab69c05c0dfa7c449dfe72e5681d0c6a3344efc4bbb3511db22686d5bc`를 표시한다. 7개release파일과urls의중복항목을확인했다. sdist내용을다운로드·설치하지않았으므로 H077의2020고정commit과코드가같다고표현하지않는다.

PyPI classifier에는MIT/Planning,설명에는MPL2.0/개발중이있고,저장repository응답에는MPL2.0/archived=true가있다. 홈페이지의vsartor와repository의victhorio표기도구별한다. 이문서는metadata차이의보존이며사용권에대한판정이나현재상태확인이아니다.
