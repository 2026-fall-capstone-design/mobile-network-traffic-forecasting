# H046 출처와 실제 열람 범위

[연구 기록](../records/0056-0058-timedc.md) · [manifest](../evidence/0056-0058-timedc/manifest.json) · [기계 판독 목록](../catalog/history-046-sources.jsonl)

원본 루트 별칭은 `Tab-ICL`이다. TimeDC 원본 16개 바이트 묶음·32개 동일 사본 경로와 기존 58번 메모를 연결한다. 58은 H045 보존 사본을 재사용한다. 32개 경로를 독립 연구 수로 세지 않는다. 원본을 바꾸지 않았고 새 모델 실행도 없다.

## 원본 기록과 외부 자료의 연결

[58 메모 전체](../evidence/0056-0058-mae-sampling/originals/SRC-0021898.md.txt)는 당시 판단을 보존한다. 아래 논문·저자 코드는 공식 주소·고정 commit과 보존 원본 해시를 제공한다. 저자 repo의 저장 license 필드가 null이므로 전체 코드를 새 라이선스로 재배포하지 않았다. 공개 여부를 사용 허가로 해석하지 않는다.

| source_id | 원본 파일 | 팀 접근·실제 읽은 범위 |
|---|---|---|
| SRC-0064438 | `TimeDC_PVLDB_2024.pdf` | [공식 자료](https://www.vldb.org/pvldb/vol18/p226-miao.pdf) — 13쪽 텍스트·11쪽 시각;식1–17/표1–7/그림1–9/알고리즘1–2;raw run 미재현 |
| SRC-0064439 | `TimeDC_PVLDB_2024.txt` | [공식 자료](https://www.vldb.org/pvldb/vol18/p226-miao.pdf) — 파생 TXT 1,575줄;PAGE header·공백 제거 후 현재 추출과 전체 내용 동일;독립 내용 가산 없음 |
| SRC-0064440 | `TimeDC__buffer_cls.py` | [공식 자료](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/buffer_cls.py) — 전체 181줄 정적 독해 |
| SRC-0064441 | `TimeDC__buffer_ts.py` | [공식 자료](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/buffer_ts.py) — 전체 171줄 정적 독해 |
| SRC-0064442 | `TimeDC__distill_cls.py` | [공식 자료](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/distill_cls.py) — 전체 389줄 정적 독해 |
| SRC-0064443 | `TimeDC__distill_ts.py` | [공식 자료](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/distill_ts.py) — 전체 373줄 정적 독해 |
| SRC-0064444 | `TimeDC__layers__stdistillation_backbone.py` | [공식 자료](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/layers/stdistillation_backbone.py) — 전체 376줄 정적 독해 |
| SRC-0064445 | `TimeDC__layers__stdistillation_layers.py` | [공식 자료](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/layers/stdistillation_layers.py) — 전체 121줄 정적 독해 |
| SRC-0064446 | `TimeDC__process__tools.py` | [공식 자료](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/process/tools.py) — 전체 150줄 정적 독해 |
| SRC-0064447 | `TimeDC__readme.md` | [공식 자료](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/readme.md) — 전체 68줄 정적 독해 |
| SRC-0064448 | `TimeDC_arxiv_history.html` | [공식 자료](https://arxiv.org/abs/2410.20905v1) — 저장 HTML의 보이는 설명·저자·버전 이력;확장 PDF/스크립트 실행 제외 |
| SRC-0064449 | `TimeDC_commit.json` | [공식 자료](https://api.github.com/repos/uestc-liuzq/STdistillation/commits/60169680447a12ad77b050831ee71da8be7f48f7) — commit/parent/tree/일시/README patch와 전체 JSON 필드 열람;PGP 서명을 독립 인증한 것은 아님 |
| SRC-0064450 | `TimeDC_repo.json` | [공식 자료](https://api.github.com/repos/uestc-liuzq/STdistillation) — 저장 시점 repo JSON 전체 필드;license null/공개 여부·기본 branch. 현재 통계의 재확인 아님 |
| SRC-0064451 | `TimeDC_tree.json` | [공식 자료](https://api.github.com/repos/uestc-liuzq/STdistillation/git/trees/60169680447a12ad77b050831ee71da8be7f48f7?recursive=1) — 114 항목의 path/mode/type/size/SHA와 root/truncated 읽음. 각 URL 필드/연결된 모든 파일 본문은 읽지 않음;현재 root tree와 항목 자동 동일성 대조 |
| SRC-0064464 | `TimeDC_PVLDB_2024_p10.png` | [공식 자료](https://www.vldb.org/pvldb/vol18/p226-miao.pdf#page=10) — 주논문 10쪽의 과거 preview 전체 시각 열람;독립 결과 아님 |
| SRC-0064465 | `TimeDC_PVLDB_2024_p6.png` | [공식 자료](https://www.vldb.org/pvldb/vol18/p226-miao.pdf#page=6) — 주논문 6쪽의 과거 preview 전체 시각 열람;독립 결과 아님 |

원본 상대경로·byte 크기·SHA-256·동일 사본 source_id는 manifest와 기계 판독 목록에 모두 남겼다. PDF의 현재 공식 응답은 원본과 동일하다. 코드 8개는 Git blob까지 검수했다. 저장 tree 응답의 최상위 SHA가 commit을 반복하므로, 실제 root tree `6043d4d6db3cf88c307e5b1d32c3296550af2397`를 재구성해 114개 항목을 대조했다. 첫 검수기의 root/commit 혼동을 수정한 것이며 원본 손상이 아니다.

commit/repo JSON은 전체 필드를 읽었다. tree는 114개 항목의 path·mode·type·size·SHA와 최상위 sha/url/truncated를 읽었고 각 URL 필드·연결 파일 전체 본문은 읽지 않았다. arXiv는 저장 HTML의 보이는 설명과 이력만 읽었으며 페이지 스크립트를 실행하지 않았다.

## 고정 commit에서 추가로 읽은 직접 의존 자료

아래 27개는 원본 corpus에 새 연구가 생긴 것이 아니라 검수 중 연결한 보충 자료다. 각 바이트를 고정 tree의 Git blob과 대조했다. 26개 전체 2,221줄과 utils의26줄 선택 범위를 구분한다. 학습·import·forward·pickle load는 하지 않았다.

| reference_id | 고정 파일 | 실제 독해 |
|---|---|---|
| EXT-H046-01 | [network_patch.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/network_patch.py) | 전체 정적 독해; 1–97줄 |
| EXT-H046-02 | [process/exp.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/process/exp.py) | 전체 정적 독해; 1–296줄 |
| EXT-H046-03 | [process/data_factory.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/process/data_factory.py) | 전체 정적 독해; 1–57줄 |
| EXT-H046-04 | [process/data_loader.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/process/data_loader.py) | 전체 정적 독해; 1–398줄 |
| EXT-H046-05 | [process/metrics.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/process/metrics.py) | 전체 정적 독해; 1–44줄 |
| EXT-H046-06 | [reparam_module.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/reparam_module.py) | 전체 정적 독해; 1–159줄 |
| EXT-H046-07 | [process/data_loader_cls.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/process/data_loader_cls.py) | 전체 정적 독해; 1–124줄 |
| EXT-H046-08 | [process/exp_cls.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/process/exp_cls.py) | 전체 정적 독해; 1–189줄 |
| EXT-H046-09 | [process/timefeatures.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/process/timefeatures.py) | 전체 정적 독해; 1–134줄 |
| EXT-H046-10 | [scripts_buffer/electricity.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_buffer/electricity.sh) | 전체 정적 독해; 1–46줄 |
| EXT-H046-11 | [scripts_buffer/etth1.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_buffer/etth1.sh) | 전체 정적 독해; 1–43줄 |
| EXT-H046-12 | [scripts_buffer/etth2.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_buffer/etth2.sh) | 전체 정적 독해; 1–43줄 |
| EXT-H046-13 | [scripts_buffer/ettm1.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_buffer/ettm1.sh) | 전체 정적 독해; 1–46줄 |
| EXT-H046-14 | [scripts_buffer/ettm2.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_buffer/ettm2.sh) | 전체 정적 독해; 1–46줄 |
| EXT-H046-15 | [scripts_buffer/illness.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_buffer/illness.sh) | 전체 정적 독해; 1–44줄 |
| EXT-H046-16 | [scripts_buffer/traffic.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_buffer/traffic.sh) | 전체 정적 독해; 1–46줄 |
| EXT-H046-17 | [scripts_buffer/weather.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_buffer/weather.sh) | 전체 정적 독해; 1–44줄 |
| EXT-H046-18 | [scripts_distill/electricity.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_distill/electricity.sh) | 전체 정적 독해; 1–39줄 |
| EXT-H046-19 | [scripts_distill/etth1.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_distill/etth1.sh) | 전체 정적 독해; 1–36줄 |
| EXT-H046-20 | [scripts_distill/etth2.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_distill/etth2.sh) | 전체 정적 독해; 1–36줄 |
| EXT-H046-21 | [scripts_distill/ettm1.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_distill/ettm1.sh) | 전체 정적 독해; 1–39줄 |
| EXT-H046-22 | [scripts_distill/ettm2.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_distill/ettm2.sh) | 전체 정적 독해; 1–39줄 |
| EXT-H046-23 | [scripts_distill/illness.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_distill/illness.sh) | 전체 정적 독해; 1–37줄 |
| EXT-H046-24 | [scripts_distill/traffic.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_distill/traffic.sh) | 전체 정적 독해; 1–39줄 |
| EXT-H046-25 | [scripts_distill/weather.sh](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/scripts_distill/weather.sh) | 전체 정적 독해; 1–37줄 |
| EXT-H046-26 | [layers/RevIN.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/layers/RevIN.py) | 전체 정적 독해; 1–63줄 |
| EXT-H046-27 | [utils.py](https://github.com/uestc-liuzq/STdistillation/blob/60169680447a12ad77b050831ee71da8be7f48f7/utils.py) | imports/get_time/add_noise26줄 선택;다른 함수 미독해; 1–17, 223–227, 605–608줄 |

EXT-H046-28–30은 공식 주논문 응답, 고정 commit 응답, 실제 root tree 응답이다. manifest에 응답 해시와 범위를 기록했다. 공식 코드의 raw URL도 연결하여 웹 화면에서 숨겨지는 README 주석을 확인할 수 있다.

## 현재 범위에 포함하지 않은 내용

arXiv 확장 PDF, Appendix.pdf·Additional_experiment.pdf, framework/precision 이미지와 별도 figures, 원 데이터·checkpoint·환경·저자 실행 로그는 미검수다. tree에 파일명이 있다는 사실은 본문 독해가 아니다. 다른 세 문헌과 전체56/58 종합도 남아 있다. 이 범위를 corpus의 중복·제외로 처리하지 않는다. 이후 원본에 실제 저장된 추가 자료가 발견되면 별도 source로 검토한다.
