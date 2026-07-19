# `backend/packages/harness/deerflow/skills/review/analyzer.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/review/analyzer.py`  ·  行数: 360

**模块文档首行**（仅供参考）: Deterministic skill package analyzer.

## 模块概览
- 函数 7 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: re, tempfile
- `__future__` -> annotations
- `pathlib` -> Path, PurePosixPath
- `typing` -> Any
- `deerflow.skills.frontmatter` -> ALLOWED_FRONTMATTER_PROPERTIES, split_skill_markdown
- `deerflow.skills.package_paths` -> is_eval_fixture_path, is_eval_fixture_skill_md
- `deerflow.skills.parser` -> parse_allowed_tools, parse_required_secrets
- `deerflow.skills.review.digest` -> compute_package_digest
- `deerflow.skills.review.eval_schema` -> analyze_eval_manifests
- `deerflow.skills.review.models` -> FACTS_SCHEMA_VERSION, SKILLSCAN_SEVERITY_MAP, ProfileName, make_finding, sort_findings, summarize_findings
- `deerflow.skills.review.resource_graph` -> build_resource_graph
- `deerflow.skills.skillscan.orchestrator` -> scan_skill_dir

## 函数
#### `ƒ` `analyze_skill_package(snapshot: dict[str, Any], *, profile: ProfileName) -> dict[str, Any]`  L27
  - _文档首行_（仅供参考）: Produce review-facts.v1 from a PackageSnapshot.
  - 分支数 9，函数体节点数 612；return: {'schema_version': FACTS_SCHEMA_VERSION, 'subject': subject, 'profile': profile, 'completeness': {'package_enumerated': not any((error.get('code') == 'root_not_found' for error in snapshot.get('reader_errors', []))), 'text_content_complete': text_complete, 'truncated': bool(snapshot.get('truncated')), 'not_assessed': sorted(set(not_assessed))}, 'summary': summarize_findings(findings), 'findings': findings, 'resources': resource_graph, 'evals': evals, 'reader_errors': snapshot.get('reader_errors', []), 'analyzer_errors': analyzer_errors}
  - 调用: str, get, PurePosixPath, append, make_finding, _analyze_skill_md, sorted, is_eval_fixture_skill_md, items, _is_nested_archive, _is_hidden_sensitive_path, build_resource_graph, extend, analyze_eval_manifests, _scan_with_skillscan, type, sort_findings, compute_package_digest, any, bool（+2）

#### `ƒ` `_analyze_skill_md(content: str, *, profile: ProfileName, findings: list[dict[str, Any]]) -> str | None`  L148
  - 分支数 11，函数体节点数 453；return: None, declared_name
  - 调用: split_skill_markdown, append, make_finding, sorted, set, join, get, isinstance, strip, _valid_skill_name, len, parse_allowed_tools, Path, str, parse_required_secrets, _add_agentskills_findings

#### `ƒ` `_add_agentskills_findings(metadata: dict[str, Any], declared_name: str | None, findings: list[dict[str, Any]]) -> None`  L277
  - 分支数 2，函数体节点数 122
  - 调用: get, isinstance, len, strip, append, make_finding

#### `ƒ` `_scan_with_skillscan(snapshot: dict[str, Any]) -> list[dict[str, Any]]`  L305
  - 分支数 5，函数体节点数 325；return: [], findings
  - 调用: get, is_eval_fixture_path, str, TemporaryDirectory, Path, mkdir, write_text, scan_skill_dir, append, make_finding
  - 文件IO: mkdir (L314), write_text (L315)

#### `ƒ` `_valid_skill_name(name: str) -> bool`  L348
  - 分支数 0，函数体节点数 29；return: bool(re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', name)) and len(name) <= 64
  - 调用: bool, fullmatch, len

#### `ƒ` `_is_nested_archive(path: str) -> bool`  L352
  - 分支数 0，函数体节点数 34；return: lowered.endswith(('.zip', '.tar', '.tar.gz', '.tgz', '.tar.bz2', '.tbz2', '.tar.xz', '.txz', '.7z', '.rar', '.whl'))
  - 调用: lower, endswith

#### `ƒ` `_is_hidden_sensitive_path(path: str) -> bool`  L357
  - 分支数 0，函数体节点数 36；return: any((part in {'.env', '.npmrc', '.pypirc', '.netrc'} for part in parts))
  - 调用: PurePosixPath, any

## 文件内调用关系
- `analyze_skill_package` -> _analyze_skill_md, _is_nested_archive, _is_hidden_sensitive_path, _scan_with_skillscan
- `_analyze_skill_md` -> _valid_skill_name, _add_agentskills_findings
