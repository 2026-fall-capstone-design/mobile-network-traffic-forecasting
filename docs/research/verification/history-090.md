# H090 검수: 원81 공동 입력 검토

[기록](../records/0090-input-partition-decision.md) · [28개 주장](history-090-claims.json) · [작성 후 대조](history-090-second-pass.json) · [문서 검사](history-090-document-check.json) · [출처](../sources/history-090.md)

중심11그룹과 원74 코드·원80 판단을 작성 후 다시 읽고28개 주요 주장을6개 묶음으로 대조했다. 원74 결과와 원장은 필요한 필드를 재참조했다. 원소스는 정적으로 읽었으며 원래collector/archiver/model은 실행하지 않았다. 모델 학습·추론·forward·gradient 실행0이다.

현재 확인한 것은 저장자료의해시·범위, scalar코드를 다중출력으로 가정한 선형MAC 산술, 대칭독립±1 예시와 기존teacher 수치의 재인용이다. 원81 보고서의 문헌해석은 당시 보고로 귀속하며29개 연결자료의본문은 후속검수로 남긴다. 자동파일검사와 같은에이전트의대조는 독립 연구심사가 아니다.

## 문서 링크 집계 재확인

문서 검사 JSON의 `local_links_checked`는 이번 정리 작업에서 검사한 **로컬 링크의 출현 횟수**다. 보존한 과거 collector/archiver가 생성한 수치가 아니며, 고유 파일 수나 외부 URL 접속 성공 수를 뜻하지 않는다. 아래 코드를 저장소 루트에서 Python 3.10 이상으로 실행하면 공개된 검사 대상과 동일한 범위의 파일 존재·명시적 anchor를 검사하고 집계값을 재확인할 수 있다. 연구 코드 실행이나 네트워크 요청은 없다.

범위는 `document_sha256`의 28개 파일 중 `originals/`를 제외한 18개 작성 파일이다. Markdown 링크와 JSON의 `archive_path`, `record_path`, `verification_path` 문자열을 검사한다. JSONL의 문자열, 보존 원문 속 개인 경로, 외부 URL, 검사 결과 JSON 자체는 이 집계에 포함하지 않는다. 본문 전체의 해시·주장·출처 검수는 별도 절차다.

```python
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path.cwd().resolve()
report_path = root / "docs/research/verification/history-090-document-check.json"
report = json.loads(report_path.read_text(encoding="utf-8"))
counts = {}

def check_target(url, source):
    part = urlsplit(url.strip("<>"))
    if part.scheme or part.netloc:
        return
    target = (source.parent / unquote(part.path)).resolve() if part.path else source
    assert target.is_relative_to(root) and target.is_file(), (source, url)
    if part.fragment:
        anchor = '<a id="' + unquote(part.fragment) + '"></a>'
        assert anchor in target.read_text(encoding="utf-8"), (source, url)
    key = source.relative_to(root).as_posix()
    counts[key] = counts.get(key, 0) + 1

def scan(value, source, key=""):
    if isinstance(value, dict):
        for name, item in value.items():
            scan(item, source, name)
    elif isinstance(value, list):
        for item in value:
            scan(item, source, key)
    elif isinstance(value, str):
        for url in re.findall(r"\[[^\]]+\]\(([^)]+)\)", value):
            check_target(url, source)
        if key in {"archive_path", "record_path", "verification_path"}:
            check_target(value, source)

for item in report["document_sha256"]:
    if "/originals/" in item["path"]:
        continue
    source = root / item["path"]
    text = source.read_text(encoding="utf-8")
    if source.suffix == ".md":
        scan(text, source)
    elif source.suffix == ".json":
        scan(json.loads(text), source)

total = sum(counts.values())
assert total == report["local_links_checked"], (total, report["local_links_checked"])
print(json.dumps({"local_links_checked": total, "by_file": counts}, indent=2))
```
