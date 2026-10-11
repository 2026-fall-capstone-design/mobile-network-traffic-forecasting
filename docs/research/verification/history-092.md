# CCM v2 원문·표시값 검수

[기록](../records/0092-ccm-source-review.md) · [34개 주장](history-092-claims.json) · [작성 후 대조](history-092-second-pass.json) · [저장 문서 검사](history-092-document-check.json) · [출처](../sources/history-092.md)

34개 주장을 10묶음으로 원문과 다시 대조했다. 논문 TXT 2,929행·서지 TXT 114행의 첫 전체 독해, 대응 HTML의 본문·398 수식 alttext·19표·추가 속성, 같은 v2 PDF 23쪽의 첫 시각 독해가 근거다. 작성 후에는 기록된 TXT 구간과 19표 전체 compact 행·강조·caption, PDF 2·5·7·8·9·10·18·22·23쪽을 다시 읽었다. 모든 파일 전체의 두 번째 독해나 독립 심사를 수행한 것은 아니다.

표의 표시값은 Decimal/grid 계산과 별도의 Fraction/flat 행 계산으로 대조했다. 장기예측의 개선·동률·악화, M4 Avg. 중복 집계와 IMP 차이, zero-shot, PRReg 반례, ratio·lookback 민감도를 구분한다. [공개 산술 보고서](../evidence/0092-ccm/table-audit.json)는 반올림 전 값이나 실험 재현·유의성 검정을 대신하지 않는다.

`python scripts/research_archive/check_ccm_display.py --check`로 공개 전사의 산술 일치를 다시 확인할 수 있다. Eq.4의 trace 정리는 이번 수학적 대조이며 실제 코드의 오류나 군집 붕괴를 검증한 결과가 아니다. 연구 코드 import/실행과 새 모델 학습·추론은 0이다.

논문·서지 4그룹과 원81/collector 재참조 2그룹의 12사본 및 보호 원본 6개를 해시 대조했다. 새 가산 대상은 HTML 본문2개와 정리 기록1개·주장34개다. TXT2개·재참조 자료·보충 PDF는 추가 가산0이다. 원81의 나머지21그룹과 snapshot 변경분·이후 기록·전체 통합·장기 팀 접근·최종 검수는 남아 있다.
