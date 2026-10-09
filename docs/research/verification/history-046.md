# H046 검수 범위

[연구 기록](../records/0056-0058-timedc.md) · [28개 주장 지도](history-046-claims.json) · [일차 대조](history-046-primary-check.json) · [인쇄표](../evidence/0056-0058-timedc/printed-tables.json) · [산술](../evidence/0056-0058-timedc/printed-arithmetic.json)

TimeDC 주논문 13쪽 텍스트와 11쪽 시각 자료, 저장 코드·README 8개 1,829줄을 읽었다. 직접 연결된 보충 자료 26개 2,221줄과 utils 26줄은 별도 범위다. 원본 16묶음 32경로, Git blob 8개, tree 114항목, 보충 텍스트 27개와 보호 원장 6개를 대조했다. 초기 tree 응답의 commit SHA와 실제 root SHA를 혼동한 아카이브 검수기를 고쳤으며 원본 파일은 수정하지 않았다.

표 1–7의 인쇄 수치 494개를 전사하고 8·10·11쪽에서 다시 시각 대조했다. 최대 MAE 개선율에 관한 본문 13.49%와 표 17.1512%의 차이, Table 5 Weather I의 MAE .656/RMSE .512 정의 문제, 다른 구조가 더 작은 6조건과 원 자료 대비 41손해/1이득을 보존했다. epoch당 시간과 전체 비용, 동적 메모리와 오프라인 buffer, 전처리 저장과 통신량, 모델 파라미터 수를 구분했다.

정적 검토는 공개 entrypoint의 클래스 연결, synthetic detach, 초기 0분모 조건, 조기 종료의 테스트 사용, train/eval 복귀, 분류 전처리와 지표 범위를 포함한다. 이는 조건부 코드 관찰이다. 실제 최초 오류/NaN, 논문 실행의 누수, 출판 성능의 무효를 단정하지 않는다. 예측 evaluate_synset의 인자 수는 맞으며 shell --model은 --model_id 축약 가능성을 구분했다.

동일 에이전트의 주장·본문 2차 대조와 문서·링크 검수는 마지막 문서 체크에 기록한다. 자동 검사와 외부 코드 리뷰는 독립 연구자의 과학적 재현을 대신하지 않는다. 원본 코드 import/실행, model forward/fit/inference, pickle load, 난수 생성은 0이다. 확장판·부록·추가 그림·환경·저자 raw run, 나머지 56/58와 전체 과거 기록 검수는 미완료다.
