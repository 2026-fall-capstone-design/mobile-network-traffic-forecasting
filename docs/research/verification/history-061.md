# H061 검수 — Conditional normalization

[팀 기록](../records/0064-0065-conditional-normalization.md) · [40개 주장](history-061-claims.json) · [문서 검사](history-061-document-check.json) · [출처](../sources/history-061.md)

논문35쪽 전체 텍스트·시각,26그림,공식 패키지18파일·2,423줄 전체를 읽었다. 공식 v1 PDF 바이트동일과 TXT35쪽 대응, 원PNG5쪽 전체를 확인했다. HTML은 선택 서지·초록/본문·이력·링크 독해다. 원64·65 전체와 기존 정확사본도 재대조했다.

수치 검수는 인쇄 설정36필드와 Fig20 Pearson15값, 명시한 결정적 산술을 포함한다. 81개는 형식·표기·계산 검사 수이며 논문의 모든 숫자 개수나 독립 실험 횟수가 아니다. Fig20은 시각 전사이며 원자료 재계산이 아니다. 실제 holdout 개수를 임의 반올림하지 않고, HMC 잔여 표본 수도 문구에 따른 조건부 계산으로 둔다.

핵심 경계는 모멘트 정규화 대 PIT, 보간 대 미래예측, .946 mean-HPD 관측 포함과 약96% estimated-CCF 비교의 의미, 음수 탁도 역변환 뒤 제거다. Fourier5/3쌍과 그림 캡션 차이를 임의 교정하지 않는다.

공개 패키지의 ACF min–max 재조정, 선택 lognormal 경로, 기존 모멘트 재사용·행lag, response 척도 p값, 원ARfitted+innovation bootstrap, basepipe 점 바인딩, broom SE, 전처리 차이는 정적 코드 검수다. 논문 실제 실행판이나 런타임 장애·결과 영향의 재현이 아니다. 직접 만든 작은 산술 예도 원R코드 실행과 구분한다.

작성 후 40주장과 팀 문서를 원논문·고정 코드에 다시 대조했다. 쪽·절번호와 원PNG5쪽 내용, 수집 코드 동작, EOS/TSW 제품 구분을 수정했다. Fig20의15값도 다시 시각 대조했다. 완료 범위와 수정 사항은 주장JSON/문서 검사JSON에 저장한다. 같은 에이전트의 두 번째 검수를 독립 연구자 검증으로 세지 않는다. 원본11그룹22경로와 보호6해시, 새사본3/재사용3/외부5를 확인한다.

새 모델·원연구코드 실행/import·난수 생성0. 전체 분석 저장소404, 원실행판/Stan·config·seed·raw/posterior/split·전체 비용,65 종합·후속 통합과 전체Goal은 미완료다.
