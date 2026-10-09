# 36–38 유한 정보 반례와 문헌 근거

[연구 기록](../../records/0036-0038-finite-information.md) · [출처](../../sources/history-023.md) · [manifest](manifest.json)

새 원문 사본10개 25,950 bytes, 기존 비용 원장1개를 연결한다. Python은 .py.txt로 보존한 과거 코드다. 일차논문·HTML·그림은 정식 접근 링크·SHA·실제 열람 범위로 식별하며 metadata 등록과 본문 검토를 구분한다.

저장소 루트에서 모델 없이 네 사례를 확인할 수 있다. 표준 라이브러리만 필요하다.

~~~shell
python scripts/research_archive/verify_information_claim_history.py --manifest docs/research/evidence/0036-0038-finite-information/manifest.json --output .research-archive/information-claim-check.json
~~~

이 검사는 네 개의 저장 상태를 직접 확률비 MI/조건부 MI로 계산해 모든 저장 숫자와8개 판정, 보존11사본의 해시, PDF metadata 연결, 입수 manifest와 비용 key를 대조한다. 난수 생성·원 연구 코드 실행·모델 import/fit/forward가 없다. 과거 코드의 entropy 차이 구현과 다른 산술식이지만 독립 연구 재현으로 부르지 않는다.

[문서 표 값](document-tables.json)은 네 사례와8개 다운로드 항목·계산 timer를 담는다. bit 단위 수학 반례이지 네트워크 성능 결과가 아니다. 문헌의 수식과 가정은 [지정 수동 대조](../../verification/history-023-primary-review.json)를 함께 확인해야 한다. 원 실행 코드 해시가 결과에 묶이지 않은 한계와 논문 전체 미검토 범위를 보존한다.
