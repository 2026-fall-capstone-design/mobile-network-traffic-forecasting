# GOTSF 연결 그림의 고정 출처

[기록](../../records/0051-0055-gotsf-media.md) · [명세](manifest.json) · [출처 범위](../../sources/history-043.md) · [검수](../../verification/history-043.md).

기존 원문 7개는 다른 묶음의 정확 사본을 상대경로로 재사용한다. 새 외부 미디어 7개는 아래 공식 고정 URL과 해시로 연결하며 공개 저장소에 이미지 바이트를 복사하지 않는다. 개인 절대경로 없이 원본 사본과 공식 추가참조를 구분했다.

| 참조 | 고정 공식 원본 | 크기(bytes) | SHA256 |
|---|---|---:|---|
| EXT-H043-01 | [figures/all_intervals_16.gif](https://raw.githubusercontent.com/netop-team/gotsf/31b17e55a0cb6f41bfe25230db3f81567efd58f3/figures/all_intervals_16.gif) | 4694031 | `d73cf76004cd12e61472e76a15c9552616db83e7b56e7ecafe003855b7a80b76` |
| EXT-H043-02 | [figures/gotsf-logo.png](https://raw.githubusercontent.com/netop-team/gotsf/31b17e55a0cb6f41bfe25230db3f81567efd58f3/figures/gotsf-logo.png) | 305696 | `4f5f129f0dca3fe090034cd0213858635bad2b3a0bc1e350549a326bed31e367` |
| EXT-H043-03 | [figures/patching_inf_16.gif](https://raw.githubusercontent.com/netop-team/gotsf/31b17e55a0cb6f41bfe25230db3f81567efd58f3/figures/patching_inf_16.gif) | 2598463 | `b21dd178e73155537fb378ae0fb03ee1fa3fccc5d8f1d1f3aed661b7b8f15b54` |
| EXT-H043-04 | [figures/subset_intervals_wproba_16.gif](https://raw.githubusercontent.com/netop-team/gotsf/31b17e55a0cb6f41bfe25230db3f81567efd58f3/figures/subset_intervals_wproba_16.gif) | 3209796 | `7eb71619c9c5fe2ac5cf4f1ea904ace729d116585e46742989f11f82826f8d24` |
| EXT-H043-05 | [figures/system_model.png](https://raw.githubusercontent.com/netop-team/gotsf/31b17e55a0cb6f41bfe25230db3f81567efd58f3/figures/system_model.png) | 802960 | `b3c9947bcc3ec6d10a8f266192dbdf2dfe2b02a927929dd83a5aaab6f6e04b50` |
| EXT-H043-06 | [images/dataset_split.png](https://huggingface.co/datasets/netop/gotsf-ds/resolve/c9ecaf153354b2cc415c64750a966c47c7f3f6ac/images/dataset_split.png) | 91777 | `79f8080ac858e7dbb9637ddbe27736774f0cccaa838fba7b9bc9d4b74c280cab` |
| EXT-H043-07 | [images/network.png](https://huggingface.co/datasets/netop/gotsf-ds/resolve/c9ecaf153354b2cc415c64750a966c47c7f3f6ac/images/network.png) | 54645 | `93f84f6200a696c59a631b27f3217b87ce758921bbe7350246e9a8b7c2f92b6a` |

코드 그림 5개는 Git blob SHA1 = SHA1(`blob <바이트수>\0` + 내용), HF 그림 2개는 LFS 내용 SHA256으로 과거 저장 tree와 일치함을 확인했다. 명세의 read_scope와 관찰에는 실제 프레임 범위, 그림의 역할과 해석 한계를 함께 기록했다. 다운로드·해시 확인은 생성 모델의 실행이나 성능 재현이 아니다. 공식 호스팅의 장기 가용성과 모든 팀원의 로그인 환경까지 검증한 것은 아니다.
