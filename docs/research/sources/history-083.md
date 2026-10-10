# H083 출처와 읽은 범위

[연구 기록](../records/0083-fmcl-client-clustering.md) · [목록](../catalog/history-083-sources.jsonl) · [검수](../verification/history-083.md)

| 출처 ID | 실제 범위 | 집계 |
|---|---|---|
| SRC-0062493 | FMCL arXiv2604.27510v1, 전체16쪽 text·visual 및 Table1/Figure1·2/Algorithm1–5 | 독립 본문1 |
| SRC-0062494 | 보존 TXT16개 페이지 블록과 같은 PDF의 새 추출16쪽 정확 대응 | 파생 표현, 본문 추가0 |
| SRC-0062495 | 보존 PNG의 PDF12쪽 전체: 설정·평가·결과 설명 | 전체 이미지1 |
| SRC-0062496 | 보존 PNG의 PDF7쪽 전체: Algorithm2·overlap·군집화 | 전체 이미지1 |
| SRC-0062497 | 보존 PNG의 PDF8쪽 전체: Algorithm3 | 전체 이미지1 |
| SRC-0022036 | 원79 findings1–51행 재참조 | 기존 본문, 추가0 |
| SRC-0022037 | 원79 plan1–24행 재참조 | 기존 본문, 추가0 |

신규5그룹의 사본10경로는 SHA-256으로 확인했다. 원PDF에는 회전된 arXiv 판본표시가 있고 텍스트 추출은 단어 간격·수식이 깨져 있어 페이지 이미지를 함께 읽었다. TXT 대응 검사는 전체16쪽의 양끝 공백을 제거한 새 pypdf 일반 추출과 일치한다. 추출의 정확 대응은 독해나 실행 재현과 별개의 검사다.

외부 원문 PDF·TXT·PNG는 여기 재게시하지 않고 원경로·크기·해시와 검토 결과를 제공한다. 기존 [findings](../evidence/0076-0079-learning-decisions/originals/SRC-0022036.md.txt)·[plan](../evidence/0076-0079-learning-decisions/originals/SRC-0022037.md.txt)은 이미 보존한 사본으로 연결한다. 새 독립 본문1·이미지3이며 이번에 만든 표/절차 JSON을 기존 원자료 JSON 독해 수로 가산하지 않는다.

원79 외부21그룹 중 H074의명세·Crossref4그룹과 이번5그룹 외의12그룹은 후속 검수 범위다. FMCL 참고문헌16개가 목록에 있다는 이유로 그 논문 전문을 읽은 것으로 세지 않는다. 실행 코드·원시 결과·실제 환경과 장기 원자료 공유도 미완료다.
