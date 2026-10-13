# 현재 근거와 다음 연구안의 차이를 기록할 때

[원103](../records/0133-current-evidence-and-unapproved-extension.md) · [원101](../records/0131-actual-pooled-context-and-rctl-ranking.md) · [원95](../records/0125-frozen-rctl-serving-cost-baseline.md) · [원102](../records/0132-architecture-kernel-and-joint-risk.md)

| 확인할 연결 | 원103의 당시 판단 | 새안에서 달라져야 할 근거 |
|---|---|---|
| 직접 예측→소속 결정 | Tab 직접MAE는좋았지만두K4의RCTL평균선호와반대 | 실제유용한결정이바뀌는과정과기간/cell별손해 |
| 독립소속→학습효용 | RCTL을호출하지않는조건은유지됐으나효용보장은아님 | 최종learner에연결된직접근거·선택후대조 |
| model수→운영비용 | K1/K4 모두16행;batch기본비교·state/file/시간구분 | 같은정보·조건에서줄어드는연산/저장량과전체비용 |
| 추가상한→추천/완료 | 조건부18fit제안미승인·미실행/후보미확정 | 후보1먼저 고정·비교군·seed·중단조건·별도권한 |

HCP/RMB-CLE는 [가까운선행](closest-pooling-methods.md), 도로시간입력·network traffic-matrix는 [네트워크·시계열](network-timeseries.md), 공식회귀는 [TabICLv2](official-tabicl.md)에이전세부검토를연결했다. 원103의문헌요약을이논문들의새전문검토·독립재현·신규성전수감사로세지않는다. 구조이론의가능성과원102에서의점수보류도구별한다.

원103의한국어보고서·Word는중간산출물이다. 개인PC링크·PDFURI문자깨짐·새Word렌더부재·미독progress/RCTLsummary전문을보존하며, [읽기용보고서](../evidence/0133-current-evidence-and-unapproved-extension/readable-report.md)에서팀이근거로이동할수있게했다. 새학습이나기존연구Goal은재개하지않았다.
