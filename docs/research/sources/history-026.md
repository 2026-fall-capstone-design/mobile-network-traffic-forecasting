# 43–44 출처와 실제 열람 범위

[연구 기록](../records/0043-0044-predictor-roles.md) · [25개 식별 목록](../catalog/history-026-sources.jsonl) · [manifest](../evidence/0043-0044-predictor-roles/manifest.json)

작은 원문 5개 17,623 bytes를 원 바이트·CRLF 그대로 추가 보존하고 44 원문 1개는 앞 묶음에서 재사용한다. 파일 수는 실험 수가 아니다. 외부 문헌·코드는 전체 파일을 게시하지 않고 정식 접근 링크·판본·해시·읽은 구간을 연결했다.

| 보존 링크 | 원 파일명 | bytes |
| --- | --- | ---: |
| [SRC-0021568](../evidence/0043-0044-predictor-roles/originals/SRC-0021568.md.txt) | 43_predictor_role_source_plan.md | 2145 |
| [SRC-0021588](../evidence/0043-0044-predictor-roles/../0041-0042-cell-harm/originals/SRC-0021588.md.txt) | 44_cell_harm_and_predictor_role_findings.md | 10924 |
| [SRC-0022770](../evidence/0043-0044-predictor-roles/originals/SRC-0022770.py.txt) | fetch_predictor_role_sources_43.py | 3011 |
| [SRC-0063559](../evidence/0043-0044-predictor-roles/originals/SRC-0063559.json) | local_distillation_repository.json | 9929 |
| [SRC-0063560](../evidence/0043-0044-predictor-roles/originals/SRC-0063560.json) | manifest.json | 2477 |
| [SRC-0063561](../evidence/0043-0044-predictor-roles/originals/SRC-0063561.json) | run_started.json | 61 |

43는 1–12행, 44는 1–84행, 다운로드 코드는 1–61행을 모두 읽었다. 44의 수치 §1–2/§6은 history-025, 문헌·판단 §3–5는 history-026에서 대조했다. manifest 여섯 항목과 run_started의 전체 키, repository JSON의 root 필드와 tree 전체 항목을 읽었다. tree를 읽었다는 사실이 그 안의 모든 코드 본문을 읽었다는 뜻은 아니다. 원 코드의 명령을 실행하지 않았다.

## 일차자료와 코드

| ID | 정식 접근 링크 | bytes | SHA-256 |
| --- | --- | ---: | --- |
| SRC-0063549 | [2509.23695_abs.html](https://arxiv.org/abs/2509.23695) | 43659 | e7b44ae94e0dced068e4fdf1271df4edc2e0a43c71aafe1d6f4cfb8a9e0dd771 |
| SRC-0063550 | [2509.23695v1.html](https://arxiv.org/html/2509.23695v1) | 705802 | 303c46632165f4325afb4d0555316ea8dc1017c48668dedf003ab2047eaefd3b |
| SRC-0063551 | [2509.23695v1.pdf](https://arxiv.org/pdf/2509.23695v1) | 3416814 | 49303220e5c52fe66f3d5b7a3e24f00d8ab7d658ae39fa6852da9a287d70c2ad |
| SRC-0063554 | [2608.23538_abs.html](https://arxiv.org/abs/2608.23538) | 43261 | 009ff729ec4792d5957d7aa13ea3bfb4bf4df5d36f7dcf34c2abaef6405d1528 |
| SRC-0063555 | [2608.23538v2.html](https://arxiv.org/html/2608.23538v2) | 663163 | 8858f2833714515cfa23312d3f6ae2cc800dd1484fdf12a382fed0be8a1c8adf |
| SRC-0063556 | [2608.23538v2.pdf](https://arxiv.org/pdf/2608.23538v2) | 1646969 | 9c30bf7f4ed4c5b260301cda9c91654f93605e38f50d3404a72cb8d0d31ce166 |
| SRC-0063562 | [README.md](https://github.com/erincr/local-distillation-benchmark/blob/f8ea1e71f19afd3167ba7ca0984ed34294d40823/README.md) | 4126 | aefe0d9cfd069a873ae886949fa9be3049e5e7626994c582897606bbee163df1 |
| SRC-0063563 | [benchmark_methods__common.py](https://github.com/erincr/local-distillation-benchmark/blob/f8ea1e71f19afd3167ba7ca0984ed34294d40823/benchmark_methods/common.py) | 27709 | 91d722134f4dc849580fd8c8c189907d4efe467302fd5dc7795efe5dceff0f15 |
| SRC-0063564 | [benchmark_methods__method_ld.py](https://github.com/erincr/local-distillation-benchmark/blob/f8ea1e71f19afd3167ba7ca0984ed34294d40823/benchmark_methods/method_ld.py) | 1934 | 7e7d680f32c2f94ab7924513a080b08fe553624cd2c8cf75c2c97446c2837c9a |
| SRC-0063565 | [benchmark_methods__method_ld_ablation.py](https://github.com/erincr/local-distillation-benchmark/blob/f8ea1e71f19afd3167ba7ca0984ed34294d40823/benchmark_methods/method_ld_ablation.py) | 2819 | 8bdd07b5e6ac12a8db043bc32f75842013aeee02af8bbc252d52f292591603a5 |

- TimeTic v1 PDF 22쪽 중 텍스트 1,3–9,14–15,17–19,21–22(15쪽), 시각 6,7,15,21,22(5쪽)를 확인했다. Table 1과 Tables F/G의 TimeTic·zero-shot mean 열, 특징 구성·의사코드·부록 D 식을 대조했다. PDF18 Table C의 300개 항목 전체를 시각 검산하지 않았다. PDF2,10–13,16,20은 미열람이다.
- Local distillation v2 PDF 42쪽 중 텍스트 1–7,10–18,36–38(19쪽), 시각 7,13,16,38(4쪽)를 확인했다. Algorithm 1·계수 군집화·안정성 정리의 가정과 결론·Appendix D 식18 및 Table 2의 선택 필드를 대조했다. PDF36–37 앞부분의 benchmark 그림 전체 수치, Appendix A 전체 증명, 나머지 페이지는 검토 완료가 아니다.

합계 텍스트 34쪽·시각 9쪽이며 전체 논문 검토 완료는 0편이다. PDF 64쪽 추출을 64쪽 독해로 집계하지 않는다. 논문 결과를 재현한 학습·추론도 없다.

abs HTML 2개는 citation tag·submission-history만 읽었다. 본문 HTML 2개는 GitHub href만 선택 확인했다. 문자 offset은 manifest에 있다. 원 HTML의 수식·그림·고유 내용 전체를 PDF와 대조했다고 표시하지 않는다. TimeTic history에는 v1(2025-09-28), local distillation에는 v1(2026-08-24)·v2(2026-09-22)가 있다. 2026-10-09 공식 arXiv 서지 조회도 이 판본을 확인했지만 저장 원본을 교체하지 않았다. Local PDF 표지의 2026-09-23은 별도 문서 날짜다.

외부 저장 README 1–88행, common.py 1–673행, method_ld.py 1–47행, method_ld_ablation.py 1–70행은 전체 정적으로 읽었다. 결론 대조의 중심은 common.py 269–363행의 similarity·gate·anchor와 508–515행의 split, method_ld.py 23–47행 및 ablation 38–70행의 비용 경계다. 원 코드 import·실행은 0회다. 저장 Git blob과 공개 API의 고정 commit `f8ea1e71f19afd3167ba7ca0984ed34294d40823`에 있는 네 파일의 바이트가 같음을 [검사](../verification/history-026-code-check.json)했다. 최신 main이나 전체 repository 검토와는 구별한다.

TimeTic 자체 구현은 확인하지 못했다. 저장 HTML의 TabPFN 링크와 arXiv 도구 링크는 TimeTic 구현의 근거가 아니다. 2026-10-09 두 검색어(`"TimeTic" "Qingren" "github"`, 논문 전체 제목+code)를 GitHub/arXiv로 제한해 추가 확인했으며 저자 scaling-laws 저장소의 논문 인용만 찾았다. 검색 범위를 넘어 코드 부재를 단정하지 않는다.

## 해시만 확인한 변환본·렌더 사본

| ID | 원 파일명 | bytes | SHA-256 |
| --- | --- | ---: | --- |
| SRC-0063552 | 2509.23695v1_html.txt | 84290 | 33936468059ffc5d5af648a835ad0e14f9814805d8055eb1f420c493849f1f55 |
| SRC-0063553 | 2509.23695v1_pdf.txt | 79244 | ce174affb1925705d5642e3262dc1c3cea5175c87c35fa37eabe707be7f2a0bb |
| SRC-0063557 | 2608.23538v2_html.txt | 110431 | 9710288a82fe8a1ada16145abdc88f3c9255fa29f67f9f004e956e7b0a70e2d7 |
| SRC-0063558 | 2608.23538v2_pdf.txt | 82946 | d75935dcc8edfc2b4347e04f6964e6f853e183bf199f0cecb260dee842d92bbc |
| SRC-0063566 | local_distillation_page13.png | 199484 | 6779a815f19305850b2b066cac1b79a34afccd0d9dcae37cadacfc1e07c6d85a |
| SRC-0063567 | local_distillation_page16.png | 206802 | 91d74e66349975d6f907f0a50f78a6ac6d7c0e9f4695ade013a43a9bfc07c430 |
| SRC-0063568 | local_distillation_page38.png | 216590 | 50622cbf12c62795598cb64b1d275d0d16ad0a6a969f3d03611d37ca4672a27f |
| SRC-0063569 | local_distillation_page7.png | 166289 | a0ef79cac539031901f604eb2121e8aed48a4ff65af9ce51dde4e96176400b42 |
| SRC-0063570 | timetic_page6.png | 298547 | eff2558dd20c1b5665cdbde0f323084bcb4db64036e9e1c18c190a6d3a176c71 |

텍스트 변환본 4개와 과거 렌더 5개는 identity만 확인했다. 시각 확인에 사용한 이미지는 이번 정리 작업공간에서 해당 PDF 페이지를 다시 렌더한 것이다. 과거 렌더에 고유한 편집·내용이 없는지까지 대조 완료한 것은 아니다.

[원본 검사](../verification/history-026-source-check.json)는 25개 identity·통제파일 6개 불변을 확인했다. CI는 저장소의 사본·metadata·작은 산술을 확인하며 외부 논문을 다시 내려받거나 저자 모델을 실행하지 않는다. [주장 지도](../verification/history-026-primary-review.json)에서 주요 판단의 위치와 한계를 확인한다.
