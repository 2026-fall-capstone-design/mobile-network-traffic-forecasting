# 63·65 Heatload 잔차 보정 근거

[팀 기록](../../records/0063-0065-heatload-residual.md) · [출처 범위](../../sources/history-056.md) · [명세](manifest.json)

- [인쇄값과 수치 검수](../../verification/history-056-numeric-check.json): 표 11개 79행 508수치, S2 승률 420개, S1 연간 GWh 5개. 수치 필드 933개는 독립 실험 수가 아니다. S4의 short/long 분할로 PDF 행 대조는 82개다.
- [코드 검토](code-audit.json): 저장 3파일 1,868줄과 직접 의존 89줄. 실제 잔차 target·합산·발행시각·보간·두 타이머·예제 설정·미확인 범위를 기록한다.
- [고정 외부 참조](external-fixed-references.json): 원본 대응 4개와 보충 8개. 12파일의 SHA-256·Git blob SHA-1·크기·URL을 보존하며 원본 source_id를 임의 생성하지 않는다.
- [형식 검수](format-audit.json): PDF/TXT·HTML/text 동등성, 인용번호 재정렬, 수식·표·그림 접근 범위. HTML 원격 이미지 asset의 바이트 동일성은 미확인이다.
- [40개 주요 주장](../../verification/history-056-claims.json)과 [문서 검수](../../verification/history-056.md)는 당시 판단과 이번 확장 검수를 구분한다.

63·65 원문은 기존 정확 사본을 연결하고 새 원본 파일은 복사하지 않았다. 외부 논문·코드는 metadata와 고정 원문 링크로 제공한다. 본문·표의 읽기와 작은 산술 대조는 원 실험 재현이 아니다. 원 코드 import/실행·모델 학습/추론·난수 생성은 없다. 다른 5문헌·65 전체 종합과 원 실행/전체 비용 검증은 남아 있다.
