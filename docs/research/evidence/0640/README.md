# 640의 보존 근거

[연구 기록](../../records/0640-contribution-boundary.md) · [문헌 비교](../../references/conditional-clustering.md) · [검수 범위](../../verification/pilot-003.md) · [출처](../../sources/pilot-003.md)

13개 원본 경로를 연결했다. 12개는 이 폴더에 바이트 그대로 새로 보존했으며 합계 75,976바이트다. 635 코드 한 개는 앞선 묶음의 사본을 재사용한다. 기록 수나 새 실험 수가 아니다.

| 자료 | 보존 사본 |
|---|---|
| 640 계획·결과 | [계획](originals/SRC-0022010.md.txt), [결과](originals/SRC-0022009.md.txt) |
| 당시 검토·완료 상태 | [review manifest](originals/SRC-0030714.json), [archive complete](originals/SRC-0030713.json) |
| 당시 보존 코드 | [archiver](originals/SRC-0022414.py.txt) |
| Yang HTML 확보 내역 | [source manifest](originals/SRC-0063796.json) |
| 관련 상세 기록 | [116](originals/SRC-0020879.md.txt), [267](originals/SRC-0021203.md.txt), [473](originals/SRC-0021646.md.txt), [512](originals/SRC-0021730.md.txt), [634](originals/SRC-0021996.md.txt) |
| 641 당시 후속 계획 | [계획](originals/SRC-0022012.md.txt) |
| 점수·배정 구현 | [635 코드](../0635-0638/originals/SRC-0022528.py.txt), 65–120·205–235행 |

[manifest.json](manifest.json)은 원본 ID·경로·SHA-256·사본·읽은 구간을 연결한다. `.md.txt`와 `.py.txt`의 옛 링크·실행 지시는 역사적 자료다. 이 코드들을 실행해 현재 연구 상태나 예산을 갱신하면 안 된다.

외부 논문은 전체 PDF/HTML을 이 폴더에 게시하지 않고 공식 링크·판본·로컬 원본 해시·검토 구간을 `primary_sources`에 기록했다. 5개 PDF와 3개 기존 페이지 이미지의 지정 구간을 읽었다. 별도 `hash_only_sources`의 Yang HTML은 확보된 원본의 해시만 대조했다. 현재 공식 HTML의 지정 절을 읽은 사실과 저장된 HTML 전체를 읽은 사실을 구분한다.

저장소 최상위에서 다음 명령으로 보존 바이트·목록 연결·읽기용 파일 링크를 확인할 수 있다.

```bash
uv run --locked python scripts/research_archive/check_archive.py
```

이 검사는 논문을 다운로드하거나 과거 연구 코드를 실행하지 않는다. 외부 논문의 목록 메타데이터 대조와 원문 내용 검증의 차이는 [검수 범위](../../verification/pilot-003.md)에 설명했다.
