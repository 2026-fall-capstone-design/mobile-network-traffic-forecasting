# 사전학습 목적·시간 조건·cell 공유 — 원100 문헌 비교

[기록](../records/0130-pretraining-objective-and-time-conditioning.md) · [40출처](../sources/history-130.md) · [실제 판독](../evidence/0130-pretraining-objective-and-time-conditioning/literature-scope.json) · [공식코드 scope](../evidence/0130-pretraining-objective-and-time-conditioning/official-code-scope.json)

| 문헌·판본 | 대상·학습·현재 확인 | 현재 RCTL 공유에 적용할 때의 경계 |
|---|---|---|
| TabClustPFN2601.21656v3 | 합성latent row소속/K·PIN SoftARI/CIN CE·TabICL2025 초기화;35쪽text/image | 자동K2–10·같은표현/K별decoder9회·cell 표현설계와유한공유효용은별도 |
| APT AAAI2026 | known history-start/horizon-end timestamp→prototype top-k→W/B;9쪽text/image·출판표2 | 초기동결후공동학습·시간정보와cell소속분리·Traffic도로자료·일부metric악화 |

Tianqi Zhao, Guanyang Wang, Yan Shuo Tan, Qiong Zhang, **TabClustPFN**. [공식v3](https://arxiv.org/abs/2601.21656v3) · [PDF](https://arxiv.org/pdf/2601.21656v3). v3는 2026-05-14에 공개됐다. 로컬 표지의 Prior-data Fitted와 공식 abs의 Prior-Fitted 제목 표기를 구별한다. 이전 [H006 검토](../sources/history-006.md)의 같은 SHA PDF/TXT를 재사용했다. N10000평가·D/PCA한계,44개curatedbenchmark의subsampling/ARI제외,3200GMM K집합coverage와최종trafficMAE는서로다르다. 본문two-layer/lower-triangle과부록3-layer/upper-triangle 표현도 임의통일하지않는다.

[공식보관commit](https://github.com/Tianqi-Zhao/TabClustPFN/tree/5673beaab72d69bb9db30da2740aef90975a3e0c)은 2026-05-01로 v3 공개일보다 앞선다. 선정 README/cluster.py/train_config.py/run_Softari.py/tabcluster.py를 전부 읽고 현재 pinned Git blob 바이트를 대조했다. inference는공유encoder표현을재사용한다. 자동K와점유label수·manualK1허용/실제작동을구별한다. model/learning.py/decision.py/embedding.py/interaction.py와preprocessor/base trainer/prior generator는선택밖이며checkpoint링크를실제다운로드/실행한것은아니다.

Yujie Li, Zezhi Shao, Chengqing Yu, Yisong Fu, Tao Sun, Yongjun Xu, Fei Wang, **APT: Affine Prototype-Timestamp For Time Series Forecasting Under Distribution Shift**. [출판본](https://ojs.aaai.org/index.php/AAAI/article/view/38542) · [공식PDF](https://ojs.aaai.org/index.php/AAAI/article/download/38542/42504) · [v1부록](https://arxiv.org/html/2511.12945v1). 공식page공개일2026-03-14/40(18)/15180–15188/DOI10.1609/aaai.v40i18.38542. PDF물리3–4쪽은방법/학습,5쪽은Table2다. 출판본과v1HTML의편집·부록·바이트동일성을가정하지않는다. 현재HTML의Table5/C1–2선택범위만확인했고전체HTML/부록전독은아니다.

[공식보관commit](https://github.com/blisky-li/APT/tree/98a4c9c017666207b02029f842eff92818f0eab8)은 2026-01-26이다. 선정 README/trainnormal.py/ETTh1 config/L2affine/APT.py/runner를 전부 읽고 두 저장소의 선정 파일 11개 모두 pinned Git blob을 대조했다. currentcapturedETTh1은None/H96/maskedMAE이며Table2TrafficRevIN/네horizon평균재현이아니다. loss/__init__.py의l2binding·model wrapper/normalizer 전체경로는미확인이다. unusedfused코드관찰을논문gate/전체결함으로옮기지않는다.

원100의같은함수/다른입력예시와상수공통affine의기울기보존은제한된직접추론이다. 실제finiteRCTL우위나전체APT불가의증명은아니다. 비교문헌과현재cell의묶는객체·학습정답·K1·최종learner사용·전체비용을명시한다. 좋은clusteringrank/시간보정효과만으로유용한공유결정이확보되었다고쓰지않는다.

외부 본문·PDF/TXT/PNG는 통째 게시하지 않고 정식 URL, SHA, 실제 읽기 범위를 제공한다. 원문을읽은것과원실험재현·모든곡선/증명독립검수는구별한다. 다른선행연구의부재/전체분야불가능성을판정한기록이아니다.
