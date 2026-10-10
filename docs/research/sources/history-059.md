# H059 출처와 판본 — GP-Copula

[팀 기록](../records/0064-0065-gp-copula.md) · [명세](../evidence/0064-0065-gp-copula/manifest.json) · [목록](../catalog/history-059-sources.jsonl) · [검수](../verification/history-059.md)

5개 원본 그룹·10개 물리 경로다. 기존64·65의 정확 사본2개를 재사용하며 PDF·TXT·PNG는 같은 논문의 표현인 외부 참조3개다. 새 정확 사본, 로컬 본문/전체JSON 독해 증분은0이다. 이번에 읽은 공식 보충자료·외부 코드의 범위는 아래에서 따로 기록한다.

| source_id | 팀 접근 경로 | 실제 확인 범위 |
|---|---|---|
| SRC-0022015 | [64_conditional_transform_review_plan.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022015.md.txt) | 64 전체를 다시 읽고 empirical marginal transform/shared forecasting 질문을 연결. 기존 H055 전체독해/정확 사본 재사용, 새 본문 가산 없음. |
| SRC-0022016 | [65_residual_and_transform_findings.md](../evidence/0063-0065-ecai-interface/originals/SRC-0022016.md.txt) | 65 전체와 §5/조건부PIT/손실/실행경계를 다시 대조. GP-Copula 구현 미검토였던 당시 범위를 보존. 다른 두 문헌 및 전체 후속 통합은 미완료. |
| SRC-0062145 | [Gaussian_copula_NeurIPS2019.pdf](https://papers.neurips.cc/paper_files/paper/2019/file/0b105cf1504c4e241fcc6d519ea962fb-Paper.pdf) | 본문11쪽 텍스트·시각 전체,3그림/3표/37참고문헌 서지. 공식PDF와 바이트동일. 보충12쪽/선택구현은 별도 외부근거. 원실험 재현 없음. |
| SRC-0062146 | [Gaussian_copula_NeurIPS2019.txt](https://papers.neurips.cc/paper_files/paper/2019/file/0b105cf1504c4e241fcc6d519ea962fb-Paper.pdf) | 11쪽 wrapper/외곽공백/개행 정규화 후 이번PDF 추출과 문자동일. 독립 문헌이나 실험으로 세지 않음. |
| SRC-0063858 | [Gaussian_copula_NeurIPS2019_p5.png](https://papers.neurips.cc/paper_files/paper/2019/file/0b105cf1504c4e241fcc6d519ea962fb-Paper.pdf#page=5) | 저장 원PNG5쪽 전체 시각독해. 경험CDF/선형보간/정상 주변분포 가정/원척도 Jacobian을 대조. PDF 파생물. |

## 논문과 보충자료

[공식 본문](https://papers.neurips.cc/paper_files/paper/2019/file/0b105cf1504c4e241fcc6d519ea962fb-Paper.pdf)은2026-10-10 HTTP200,5,238,951바이트이며 저장본과 SHA-256 `f535ca231118d3b6a2c3d632ff109afee1fe7a5be2eaa0db59809655f212d306`이 같다. 11쪽 텍스트·시각,3그림·3표·37참고문헌 서지를 읽었다. 시각5쪽은 원PNG로도 확인했다. 원TXT는 page wrapper·개행·외곽공백 정규화 뒤11쪽 모두 새PDF 추출과 같다. TXT/PNG 링크는 내용 출처PDF이며 파생 파일의 다운로드/해시 검증 URL은 아니다.

[공식 보충ZIP](https://papers.neurips.cc/paper_files/paper/2019/file/0b105cf1504c4e241fcc6d519ea962fb-Supplemental.zip)은3,065,767바이트/SHA-256 `dce7d0cd721e276995a8b31012233a251fc06e7a644b58c1550d494ba0e5dd76`이다. 단일 `multivariate_neurips_supplementary_material.pdf`는3,117,566바이트/SHA-256 `93416dcdc3839480bf5a8b50548b4e436abd37b525f86b9e6d0ef4985008cb9b`,12쪽이다. 텍스트·시각 전체와3그림·10표·24참고문헌 서지를 읽었다. 표지의 Preprint/Under review도 보존했다. 본문37/보충24는 인용 논문 본문61편 검수가 아니며 서로 중복된 서지도 있을 수 있다.

[공식 초록 페이지](https://papers.neurips.cc/paper_files/paper/2019/hash/0b105cf1504c4e241fcc6d519ea962fb-Abstract.html)는 서지·링크만 확인했다. 전체HTML 독해로 세지 않았다. 각 취득시각·바이트·해시는 [판본 확인](../evidence/0064-0065-gp-copula/external-version-check.json)에 있다. 보충 ZIP의 추출 전 상태와 이후 독해 상태를 구분했다.

## 고정 공개 코드와 읽지 않은 범위

[공개 재구현](https://github.com/mbohlkeschneider/gluon-ts/tree/442bd4ffffa4a0fcf9ae7aa25db9632fbe58a7ea)은 `mv_release` 확인 시 커밋 `442bd4ffffa4a0fcf9ae7aa25db9632fbe58a7ea`다. [코드 검수](../evidence/0064-0065-gp-copula/code-audit.json)에16파일 각각의 고정URL·Git blob SHA·SHA-256·바이트·총줄수·읽은줄범위를 저장했다.

전체로 읽은12파일은 README,requirements,GPVAR estimator/network,hyperparams,model factory,dataset/grouper,lowrank Gaussian/GP,benchmark test,demo다. 나머지는 transform448–491/980–1136/1280–1622,DeepVAR network1–109/244–450/456–596,evaluation67–148/207–330/383–575,DeepVAR estimator1–110만 읽었다. 그 밖의 내용은 검수 완료로 올리지 않는다.

고정 tree432항목은 경로·크기를 검색한 메타데이터이며432개 본문 독해가 아니다. 원논문 실행판·전체benchmark 호출·외부 데이터 tar를 읽거나 실행하지 않았다. 실제 데이터 전처리·구간·자료 권한과 팀 구성원별 접근, seed·완전한 환경·원결과 집계도 미검증이다. 공개 링크를 재현 성공으로 대신하지 않는다.

다음 문헌은 TACTiS-2·conditional normalization이며65전체 판단·후속 통합은 남아 있다.
