# H048 출처와 실제 열람 범위

[연구 기록](../records/0056-0058-scott.md) · [manifest](../evidence/0056-0058-scott/manifest.json) · [기계 판독 목록](../catalog/history-048-sources.jsonl)

SCott 3개 바이트 묶음·6개 원본/동일 사본 경로와 58 메모의 2경로를 연결한다. 원본 루트 별칭은 `Tab-ICL`이다. 외부 논문은 공식 URL·SHA-256으로 접근하며, 새 원본 복제는 0개다. TXT/preview·snapshot 사본을 독립 연구로 중복 계산하지 않는다.

| source_id | 원 파일 | 실제 열람 |
|---|---|---|
| SRC-0064426 | [SCott_ICML2021.pdf](https://proceedings.mlr.press/v139/lu21d/lu21d.pdf) | 11쪽 텍스트 전체,1–9쪽 시각·표1–3/식1–11/그림1–3. 참고문헌은 서지만 읽고 인용된 논문 전체로 확장하지 않음. |
| SRC-0064427 | [SCott_ICML2021.txt](https://proceedings.mlr.press/v139/lu21d/lu21d.pdf) | PAGE header/공백을 제외한 1292줄의 내용이 현재 PDF 추출과 동일. 새 독립 원문으로 가산하지 않음. |
| SRC-0064462 | [SCott_ICML2021_p5.png](https://proceedings.mlr.press/v139/lu21d/lu21d.pdf#page=5) | 저장 p5 preview 전체 시각 열람; 새 연구로 중복 가산하지 않음. |

58 메모 `SRC-0021898`은 [기존 보존 사본](../evidence/0056-0058-mae-sampling/originals/SRC-0021898.md.txt)의 전체 68줄을 다시 읽었다. 새 전체본문으로 가산하지 않는다. 원문에 적힌 과거 다음 행동은 역사적 자료이며 현재 실행 지시가 아니다.

## 직접 보충 자료

| reference_id | 공식 자료 | 열람 범위 |
|---|---|---|
| EXT-H048-01 | [공식 연결](https://proceedings.mlr.press/v139/lu21d/lu21d.pdf) | 현재 공식 main PDF는 저장본과 바이트 동일;독립 가산 없음. |
| EXT-H048-02 | [공식 연결](https://proceedings.mlr.press/v139/lu21d/lu21d-supp.pdf) | 공식 부록 10쪽 텍스트·시각 전체,Algorithm2/Table4/Fig4–5/식12–85 독해. 증명 전개의 완전한 독립 검증은 아님. 원 inventory 밖 직접 보충 자료. |
| EXT-H048-03 | [공식 연결](https://proceedings.mlr.press/v139/lu21d.html) | 제목·저자·PMLR139:7145–7155·ICML2021 서지와 main/supplement 공식 링크. |

현재 공식 main PDF SHA-256은 `7364e07d2e0ef3b78f91e065633ef3e3a2e1bfdd42da94c408592b77afe4ea00`, 부록은 `5484f082d2ed2c421b61770557c6ff6774cb64059517adc4fbecafef62ae5a92`다. 부록은 원 inventory 밖 자료로서 그 진행률에 새 파일을 가산하지 않는다.

표 3의 84개 평균·표준편차 쌍(168개 숫자), Table 4의 42개 lr와 18개 γ를 시각·텍스트 추출에 대조했다. 48개 평균차는 Decimal과 Fraction으로 검산했다. [수치 JSON](../evidence/0056-0058-scott/stored-results-arithmetic.json)은 인쇄된 자료의 산술이며 원 run·원예측을 복원한 것이 아니다.

부록 10쪽의 식과 증명 전개도 읽었으나 인용된 보조정리·상수·모든 변형의 수렴을 독립 인증하지 않는다. 저자 코드·실제 분할/seed/batch/K/정규화/구획과 원 run은 미확인이다. 원 패키지 import/실행·모델 학습/추론·난수 생성은 없으며 보호 원장 6개와 원본의 바이트를 보존했다. [검수 범위](../verification/history-048.md)
