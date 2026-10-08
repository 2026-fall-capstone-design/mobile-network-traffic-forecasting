# 05 네트워크·시계열 비교 검수

검수 대상은 [05 부분 기록](../records/0005-network-timeseries-audit.md), [문헌9편 비교](../references/network-timeseries.md), 초기 입력·대조군의 저장 근거다. 각 논문의 지정 절을 읽은 것이며 전논문·원저자 코드·전체 아카이브의 완료가 아니다. [출처 구간](../sources/history-004.md), [주장 장부](history-004-primary-review.json)

## 대조한 핵심 주장

| claim_id | 근거와 확인 내용 |
|---|---|
| H004-C01 | 기존 UPC 지정 쪽/초기 코드: peak group PCC와 raw cell PCC balanced 구분 |
| H004-C02 | ST-AR§3/Table1/PDF3–4/초기 특징:34특징과 우리16특징, lag24/168 설계의 출처 |
| H004-C03 | TabPFN-TS§3/§5.1/§6: 비자기회귀·lag 부재·추세·비용의 적용 범위 |
| H004-C04 | ISP§III/§IV.D/§IV.G/§V: 단변량 target·시점 수·분할·전처리 미기록·tuning 한계 |
| H004-C05 | MobiGPT§3.2/§4/§5.1/§5.3: diffusion 구조·환경 정보·새 지역 전이·실행 자산 미확인 |
| H004-C06 | CoT§II–IV/PDF7: offline 정답·online 검색·5G target·분할 서술 공백 |
| H004-C07 | Multivariate TabPFN§2.2/§4/AppendixB: 채널 행 구성·정보·순서 및 비용 한계 |
| H004-C08 | Traffic Matrix TablesI/II/V/PDF6·8·9: K·RMSE·naive 크기와 구조 비교 구분 |
| H004-C09 | Global/local 표지·Proposition1·§2.2/§3.2–3.3/§3.6: 제목·전체 이력·유한 기억·가정 |
| H004-C10 | B1/B2 partitions·RCTL tasks/metrics: 소속 재사용·4×4·29fit·8개 지표 |
| H004-C11 | 05의 당시 판단·B2 후속 기각·남은 공식 TabICL/관련문헌 범위 |

## 바이트·저장값 확인과 문서 대조의 구분

[110항목 체크포인트](history-004-implementation-check.json)는 외부 일차자료11개의 로컬 바이트·읽기 범위, 기존 원문9개의 identity, 세 소속의 B1→B2 일치, 다섯4×4 소속,29task와 저장 summary8행, 원본 상태·예산6개의 불변을 확인했다. 해당 JSON의 `whole_batch_document_verified=false`는 **초안 작성 전 체크포인트**의 범위를 뜻한다. 논문 해석과 완성 문서 검수를 자동으로 완료했다는 뜻이 아니다.

완성 문서의 [256항목 대조](history-004-document-check.json)가 통과했다. 논문 보고표6행(K·RMSE·naive 크기)과 우리 RCTL 저장 지표8행을 별도 대조했고, 핵심 주장11개의 의미·적용 범위를 원문에 다시 확인했다. 자동 항목 수는 독립적인 과학 검증이나 새로운 자료 수가 아니다. [기존 원예측 검산](history-001-risk-check.json)은 이번의 독립 재현 횟수에 더하지 않는다. 같은 아카이브 작성자의 재검토이며 외부 독립 연구자의 검증으로 표현하지 않는다.

기존 `check_archive.py`는 보존 파일과 catalog identity, 로컬 파일 링크를 검사한다. 외부 primary metadata 검사는 논문을 다운로드하거나 본문 주장을 재검증하는 CI가 아니다. 논문 원문은 새로 게시하지 않고 지정 판본의 링크와 읽은 구간을 남긴다.

## 남은 범위와 해결하지 않은 공백

- 05의 공식 TabICL commit/checkpoint/forecast pipeline 및 분위수·표현 해석, 회귀 TabPFN과 여섯 관련 연구는 후속 묶음이다. 05 전체를 완료로 세지 않는다.
- CoT의 ‘동일 분할’과 ‘첫200초 평가/나머지 훈련’ 문장을 보존했다. 정확한 split 코드 미복원 상태에서 forward split 또는 정보 유출을 단정하지 않는다.
- ISP의 minmax fit 기간, Traffic Matrix의 자세한 random/선택 K 절차, MobiGPT의 checkpoint·자료 접근은 미확인이다. 문헌의 모든 그래프·표·증명·원저자 코드 재현도 포함하지 않는다.
- UPC는 기존 지정 구간 검토 재사용이다. 초기16cell의 PCC를 원 UPC로 세지 않으며,44cell의 필요조건을 충분조건으로 바꾸지 않는다.
- 초기 RCTL의 global은 K1, 다른 비교군은 K4다. 전체 평균과 모든 cell·기간의 우위를 구분하고 B2의 반례·원척도 결과를 함께 연결한다.
- 새 모델 학습·추론·난수 생성·과거 연구 코드 실행은0이다. 원본 내용과 과거 Goal·예산 장부를 갱신하지 않았다.
