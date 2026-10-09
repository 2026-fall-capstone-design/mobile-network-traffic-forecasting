# 50번 문헌·판단의 재사용 근거

[팀 기록](../../records/0050-aggregation-literature.md), [출처](../../sources/history-030.md), [검수](../../verification/history-030.md)를 함께 사용한다. [manifest](manifest.json)에 원본 21경로의 source_id·크기·SHA-256·읽은 범위가 있다.

새 원본 사본은 fetch/render 코드·세 JSON의 5개(8,808 bytes)다. `.py.txt`는 실행 파일이 아니라 보존 자료이며 원 바이트를 유지했다. 48·50 원문은 H029 사본으로 연결했다. PDF 3개·TXT 3개·PNG 7개·HTML 1개는 외부 참조 metadata로 남겼다. 새로 렌더한 시각 검수 이미지는 로컬 정리 작업물이며 원 inventory의 파일이나 팀 보존 원문 수에 더하지 않았다.

재사용 순서는 50 기록에서 연구 질문과 출력 구조를 확인하고, H029의 미래 정답 진단·고정 비중 한계를 읽은 뒤, 필요한 논문의 해당 식/표와 버전을 확인하는 것이다. 값은 문헌에 인쇄된 값이며 본 연구의 재현 결과가 아니다. 논문 열람에 관한 주장과 원본 다운로드 로그를 구분한다.

공식 문헌 링크는 [HiGP](https://proceedings.mlr.press/v235/cini24a.html), [ONDM](https://dl.ifip.org/db/conf/ondm/ondm2023/1570874472.pdf), [HTS-Cluster v1](https://arxiv.org/abs/2205.14104v1)이다. IFIP 현재 웹 요청 timeout이 있어 저장 PDF를 사용했다. 팀원이 같은 저장 바이트가 필요한 경우 manifest의 원본 위치와 해시를 확인해야 하며, metadata 등록만으로 바이너리의 지속적인 팀 접근이 보장되는 것은 아니다.
