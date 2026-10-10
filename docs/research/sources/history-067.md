# H067 출처·판본 — Forecaster’s Dilemma

작성 후 44개 주장을 원문과 별도로 대조했다. 아래 범위는 실제 읽은 자료이며 보관 목록 전체·인용논문 전체의 검수 완료를 뜻하지 않는다.

[팀 기록](../records/0069-0071-forecaster-dilemma.md) · [명세](../evidence/0069-0071-forecaster-dilemma/manifest.json) · [목록](../catalog/history-067-sources.jsonl) · [검수](../verification/history-067.md)

원69·71과 당시 보고서·읽기 범위의 기존 정확사본4개, 문헌의 표현7개를 연결한다. 총11원본그룹·22물리경로다. 새 원본 복사는0이다. H066의 당시 미독해 명세는 보존하며 현재 확인 범위는 H067에 기록한다.

| source_id | 팀 접근 | 실제 확인 범위 |
|---|---|---|
| SRC-0022020 | [69 계획](../evidence/0069-0071-peak-objective/originals/SRC-0022020.md.txt) | 전체26행 재대조 |
| SRC-0022022 | [71 판단](../evidence/0069-0071-peak-objective/originals/SRC-0022022.md.txt) | 전체43행 재대조 |
| SRC-0000152 | [당시 공개 보고서](../evidence/0069-0071-peak-objective/originals/SRC-0000152.md.txt) | 전체100행 재대조 |
| SRC-0063462 | [당시 읽은 범위](../evidence/0069-0071-peak-objective/originals/SRC-0063462.json) | 전체93행 재대조. 당시 일부 독해와 이번 전체 저널본문 독해를 구분 |
| SRC-0063445 | [공식 기관 저널 PDF](https://bia.unibz.it/view/pdfCoverPage?download=true&filePid=13235236700001241&instCode=39UBZ_INST) | 저널22쪽 텍스트·시각, 표7·그림9·각주7·부록·감사·서지70항목 |
| SRC-0063446 | [대응 저널 PDF](https://bia.unibz.it/view/pdfCoverPage?download=true&filePid=13235236700001241&instCode=39UBZ_INST) | TXT2115행의22본문을 읽은 PDF 추출문과 페이지별 `strip` 후 정확동일 확인. raw행 별도 독립독해 아님 |
| SRC-0063447 | [arXiv v1 서지](https://arxiv.org/abs/1512.09244v1) | HTML621행의 전체 가시 내용·메타·주석·inline script 정적 확인. 현재 파일과 바이트동일 |
| SRC-0063448 | [기관 서지 URL](https://bia.unibz.it/esploro/outputs/journalArticle/Forecasters-Dilemma-Extreme-Events-and-Forecast/991005773027901241) | HTML43행 전체와 현재판 diff. 저장 파일은 논문 서지가 없는 로딩 shell |
| SRC-0063467 | [저널 PDF3쪽](https://bia.unibz.it/view/pdfCoverPage?download=true&filePid=13235236700001241&instCode=39UBZ_INST#page=3) | 원PNG 전체 시각, Table2·본문·각주 |
| SRC-0063468 | [저널 PDF6쪽](https://bia.unibz.it/view/pdfCoverPage?download=true&filePid=13235236700001241&instCode=39UBZ_INST#page=6) | 원PNG 전체 시각, 가중 결과점수·tilted density·CL |
| SRC-0063469 | [저널 PDF7쪽](https://bia.unibz.it/view/pdfCoverPage?download=true&filePid=13235236700001241&instCode=39UBZ_INST#page=7) | 원PNG 전체 시각, CSL/twCRPS/twCRLS·DM |

TXT와PNG의 링크는 대응 논문으로 접근하기 위한 것이며 그 파일들의 바이트 다운로드 주소는 아니다. 정확한 원경로·크기·해시·동일사본은 명세에 있다. 원 연구 코드·모델을 실행하거나 import하지 않았다.

## 저널본과2015 원고

2026-10-10 공동저자 기관에서 받은 저널 PDF는565,061바이트, SHA-256 `7ca1c43720f1408ed4c4b8e8ec7f9d76466fe2c05b40ec74615b72f8b9287164`로 원본과 같다. 제목·저자4명·2017년32권1호106–127쪽·DOI는 실제 PDF에서 확인한다.

[공식 arXiv 원고](https://arxiv.org/abs/1512.09244v1)의 제출일은2015-12-31이며 이력에 v1만 있다. 저장 abs와 현재 받은 abs40,553바이트는 SHA-256 `494c105ce08b6b9501945ae2d0166e53327723fbbd29d0dc9482382b1dbf4e44`로 같다. arXiv의 일반 code finder 메뉴는 실험 구현 연결의 증거가 아니다.

[공식 TeX 묶음](https://arxiv.org/src/1512.09244)은144,160바이트, SHA-256 `b0427f034877b86cf41070ae1021305f90e28f542aaa484b500acad6f4a117b2`다. 파일15개의 목록·크기·해시를 확인했다. `paper_FD_arXiv.tex`1828행 중270–315, 785–855, 891–917, 1110–1178, 1328–1374, 1385–1467, 1490–1565, 1689–1828, 총559행을 읽었다. 나머지 TeX·BBL·그림PDF·스타일의 본문 전수독해나 컴파일은 하지 않았다.

Table2–6의 결과는 대조한 값에서 같지만 Table7의32항목 중17개는 다르다. 두 변수의 Gaussian 열16개와 물가 VAR의 indicator k1이다. 표기 오류 가능성과 판본 변경 이유를 혼동하지 않는다. [수치 JSON](../verification/history-067-numeric-check.json)에 양판본의 값과 위치를 모두 보존했다. 이 검수는2015 원고 전체 내용을 읽었다는 뜻이 아니다.

## HTML과 별도 부록의 제한

기관 메타데이터라고 저장한 원HTML2328바이트의 SHA는 `31bccb50357843e33e44444c6dadcbe9f040e23cbbfc62a3e28d07eeea45a435`, 현재 파일의 SHA는 `af1743206dc653d1e48304d896aa243be2755efd6ca1937752ee5f90cf72a52f`다. 두 파일 모두 Research Portal 로딩 화면이며 논문 서지 본문이 없다. 전체 diff는 main JS 파일명 한 곳이다. 논문 자체가 바뀌었다는 근거로 쓰지 않는다.

[2017 별도 부록 DOI](https://doi.org/10.1214/16-STS588SUPP)는 추가 그림·표와 미디어 링크를 가리킨다고 저널에 적혀 있다. 웹 열람은 실패했고 일반 공개 요청도 HTTP200의 보안 중간화면으로 끝났다. 해당 PDF를 확보하거나 접근 제한을 우회하지 않았다. 저널 PDF 안의 부록 수식과 이 별도 온라인 부록은 다른 범위다.

2015 TeX의 Appendix B 뉴스16행·링크16개는 정적으로 읽었지만2017 부록의 대체본으로 취급하지 않는다. 저널 Table1은15행이다. 연결 기사 본문·현재 사건 상태·현재 법률을 확인하지 않았다. 관련 검색에서 다른 논문·발표자료가 나타난 것을 이번 논문의 부록 독해로 세지 않는다.

[판본 감사](../evidence/0069-0071-forecaster-dilemma/external-version-check.json)는 요청 결과·파일 해시·차이·실제 읽은 구간을, [형식 감사](../evidence/0069-0071-forecaster-dilemma/format-audit.json)는 PDF·TXT·HTML·원PNG의 범위를 구분한다. source 묶음에는 실험 실행 코드가 없지만, 전 세계에 코드가 공개되지 않았다는 주장은 아니다. 원표본·MCMC·DM검정 구현과 전체 비용은 미확인이다.
