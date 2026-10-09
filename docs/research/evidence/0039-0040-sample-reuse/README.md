# 39–40 sample 공유 근거의 재사용

[연구 기록](../../records/0039-0040-sample-reuse.md) · [출처](../../sources/history-024.md) · [manifest](manifest.json)

원문5개 19,293 bytes를 그대로 보존했다. .py.txt는 과거 다운로드 코드다. [문서 표](document-tables.json)는 원문40의 적분 예와 비용을 검수하기 위해 정리 과정에서 만든 값이며 과거 실행의 별도 result.json이 아니다.

저장소 루트에서 표준 라이브러리만으로 검산할 수 있다.

~~~shell
python scripts/research_archive/verify_sample_reuse_history.py --manifest docs/research/evidence/0039-0040-sample-reuse/manifest.json --output .research-archive/sample-reuse-check.json
~~~

정확한 uniform 절대오차 적분, joint weight, Gaussian 기하평균의 질량, source40 보고68과 정적 코드에 근거한289 정정,입수manifest·사본해시를 확인한다. 원 연구 코드 실행·model import/fit/forward·난수 표본 생성은 없다.

CI가 Latin square 구현을 직접 실행하거나 논문 증명을 재검증하는 것은 아니다. 비용의 구현 의미는 [원본 정적 대조](../../verification/history-024-code-check.json)에 근거하며 고정 버전·선택행·해시를 연결한다. 논문 조건과 인쇄상 공백은 [문헌 대조](../../verification/history-024-primary-review.json)를 함께 읽는다.
