# 51–55 종합의 보존 자료와 재사용 근거

[기록](../../records/0051-0055-synthesis.md) · [명세](manifest.json) · [103자료 범위표](scope-matrix.json) · [읽은 범위](../../sources/history-044.md) · [검수](../../verification/history-044.md).

새 파일은 아래 수집·렌더링 코드 5개뿐이다. 원 바이트를 `.py.txt`로 보존했고 실행하지 않았다. 과거 코드 안의 개인 실행 경로와 웹 주소는 역사적 내용이며 현재 실행 지시가 아니다. 기존 사본 58개는 상대경로로 재사용하고, 외부 논문·HTML·미리보기 등의 metadata 40개는 기존 명세와 공식 출처를 연결한다. 207개 원본 경로의 hash·크기를 확인했다.

| source | 원 코드 | 줄 수 | 보존 사본 |
|---|---|---:|---|
| SRC-0022754 | fetch_gotsf_code_51.py | 46 | [원본](originals/SRC-0022754.py.txt) |
| SRC-0022764 | fetch_network_methods_51.py | 50 | [원본](originals/SRC-0022764.py.txt) |
| SRC-0022782 | fetch_telemetry_sources_53.py | 44 | [원본](originals/SRC-0022782.py.txt) |
| SRC-0022797 | finish_network_sources_51.py | 56 | [원본](originals/SRC-0022797.py.txt) |
| SRC-0023101 | render_telemetry_sources_53.py | 13 | [원본](originals/SRC-0023101.py.txt) |

26개 취득 항목 중25개 성공 출력의 bytes/SHA256과1개 Ciena `Not PDF`를 대조했다. source 추출33cell과16개 PDF 미리보기의 hash/페이지도 연결했다. 산출물과 코드 경로가 맞는다는 확인이며 이 코드 버전의 유일한 과거 실행을 증명하는 process trace는 아니다. source code를 다시 실행해 자료를 내려받거나 모델을 실행하지 않았다.

54의 정량 비교는 기존 저장 JSON·NPZ와 H031 검수를 재사용한다. 새 학습 없이 결과 JSON의 평균·앞뒤 구간·셀별 순위·stage 비용 합계를 대조했다. 원 예측·수정 전후 코드·입력 가용성·원장 계보는 [52·54 자료 묶음](../0052-0054-partial-observation/README.md)에 있다. 당시 제공된 문헌의 모든 의존성·대용량 원자료·가중치가 팀 환경에서 재현됐다는 뜻은 아니다.
