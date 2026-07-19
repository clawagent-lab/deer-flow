# `backend/packages/harness/deerflow/skills/review/models.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/review/models.py`  ·  行数: 127

**模块文档首行**（仅供参考）: Shared contracts and deterministic helpers for skill review.

## 模块概览
- 函数 5 个，类 1 个，模块级常量 8 个

## 依赖（import）
- 模块: json, posixpath
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `pathlib` -> PurePosixPath
- `typing` -> Any, Literal

## 模块级常量
- `PACKAGE_SNAPSHOT_SCHEMA_VERSION` = 'deerflow.skill-package-snapshot.v1'
- `FACTS_SCHEMA_VERSION` = 'deerflow.skill-review.facts.v1'
- `REPORT_SCHEMA_VERSION` = 'deerflow.skill-review.report.v1'
- `Severity` = Literal['blocker', 'error', 'warning', 'info']
- `ProfileName` = Literal['deerflow', 'agentskills']
- `SEVERITY_RANK` = {'blocker': 0, 'error': 1, 'warning': 2, 'info': 3}
- `SKILLSCAN_SEVERITY_MAP` = {'CRITICAL': 'blocker', 'HIGH': 'error', 'MEDIUM': 'warni...
- `DEFAULT_PACKAGE_LIMITS` = PackageLimits()

## 函数
#### `ƒ` `stable_json_dumps(data: Any) -> str`  L50
  - _文档首行_（仅供参考）: Serialize review data in a byte-stable, path-independent form.
  - 分支数 0，函数体节点数 26；return: json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
  - 调用: dumps

#### `ƒ` `normalize_relative_path(path: str) -> str`  L55
  - _文档首行_（仅供参考）: Normalize a package-relative path and reject escape attempts.
  - 分支数 4，函数体节点数 109；raise: ValueError('path must not be empty'), ValueError('absolute paths are not allowed'), ValueError('path must not resolve to package root'), ValueError('path must not contain parent-directory traversal')；return: normalized
  - 调用: strip, replace, ValueError, PurePosixPath, is_absolute, normpath, any
  - 文件IO: replace (L57)

#### `ƒ` `make_finding(rule_id: str, *, severity: Severity, message: str, remediation: str, source: str, profile: str, path: str | None, line: int | None, evidence: Any | None, extra: dict[str, Any] | None) -> dict[str, Any]`  L72
  - 分支数 1，函数体节点数 113；return: finding
  - 调用: update

#### `ƒ` `sort_findings(findings: list[dict[str, Any]]) -> list[dict[str, Any]]`  L101
  - 分支数 0，函数体节点数 114；return: sorted(findings, key=lambda item: (SEVERITY_RANK.get(str(item.get('severity')), 99), str(item.get('path') or ''), item.get('line') if item.get('line') is not None else 10 ** 9, str(item.get('rule_id') or ''), str(item.get('message') or '')))
  - 调用: sorted, get, str

#### `ƒ` `summarize_findings(findings: list[dict[str, Any]]) -> dict[str, int]`  L114
  - 分支数 4，函数体节点数 106；return: summary
  - 调用: get

## 类
### 类 `PackageLimits`  L34  @dataclass(...)
- 类/实例变量:
  - `max_files` = 4096
  - `max_file_bytes` = 64 * 1024 * 1024
  - `max_total_bytes` = 512 * 1024 * 1024
- 方法:
  #### `m` `to_dict(self) -> dict[str, int]`  L39
    - 分支数 0，函数体节点数 30；return: {'max_files': self.max_files, 'max_file_bytes': self.max_file_bytes, 'max_total_bytes': self.max_total_bytes}

## 文件内调用关系
_无文件内调用_
