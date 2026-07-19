# `backend/packages/harness/deerflow/tools/builtins/review_skill_package_tool.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/builtins/review_skill_package_tool.py`  ·  行数: 188

**模块文档首行**（仅供参考）: Built-in non-activating skill package review tool.

## 模块概览
- 函数 8 个，类 0 个，模块级常量 3 个

## 依赖（import）
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> Literal
- `langchain_core.messages` -> ToolMessage
- `langchain_core.tools` -> tool
- `langgraph.types` -> Command
- `deerflow.runtime.user_context` -> resolve_runtime_user_id
- `deerflow.skills.review.analyzer` -> analyze_skill_package
- `deerflow.skills.review.models` -> stable_json_dumps
- `deerflow.skills.review.readers` -> ArchivePackageReader, InstalledSkillReader, LocalDirectoryReader, build_inline_snapshot
- `deerflow.skills.review.renderer` -> build_static_report, render_report_markdown
- `deerflow.skills.storage` -> get_or_new_skill_storage, get_or_new_user_skill_storage
- `deerflow.tools.types` -> Runtime

## 模块级常量
- `Profile` = Literal['deerflow', 'agentskills']
- `IncludeContent` = Literal['none', 'facts-only', 'semantic-review']
- `_MAX_SEMANTIC_ARTIFACT_CHARS` = 80000

## 函数
#### `ƒ` `review_skill_package(target: str, runtime: Runtime, profile: Profile, include_content: IncludeContent, scope: list[str] | None, inline_content: str | None) -> Command`    @tool(...)  L27
  - _文档首行_（仅供参考）: Inspect a skill package without activating, installing, executing, or editing it.
  - 分支数 1，函数体节点数 252；return: Command(update={'messages': [ToolMessage(content=_neutralize_review_content(stable_json_dumps(content_payload)), tool_call_id=tool_call_id, name='review_skill_package', additional_kwargs={'review_subject_entry': review_subject_entry}, artifact=payload)]}), Command(update={'messages': [ToolMessage(content=f'Error: failed to review skill package: {type(exc).__name__}: {exc}', tool_call_id=tool_call_id, name='review_skill_package', status='error')]})
  - 调用: _snapshot_for_target, analyze_skill_package, _semantic_artifacts, build_static_report, render_report_markdown, _tool_message_content_payload, Command, ToolMessage, _neutralize_review_content, stable_json_dumps, type, tool

#### `ƒ` `_snapshot_for_target(target: str, *, runtime: Runtime, inline_content: str | None) -> dict`  L100
  - 分支数 4，函数体节点数 123；raise: ValueError('inline_content is required for inline:// targets')；return: build_inline_snapshot(inline_content, name_hint=target), InstalledSkillReader.from_target(target, storage=storage).read(), ArchivePackageReader(path).read(), LocalDirectoryReader(path).read()
  - 调用: startswith, ValueError, build_inline_snapshot, resolve_runtime_user_id, get_or_new_user_skill_storage, read, from_target, expanduser, Path, _ensure_local_target_allowed, ArchivePackageReader, LocalDirectoryReader
  - 文件IO: read (L109), read (L114), read (L115)

#### `ƒ` `_ensure_local_target_allowed(path: Path) -> None`  L118
  - 分支数 3，函数体节点数 95；raise: ValueError('Local review targets must be under the current workspace, /tmp, or the configured skills root')；return: None
  - 调用: resolve, cwd, Path, get_or_new_skill_storage, append, get_skills_root_path, relative_to, _ensure_local_target_is_package_or_archive, ValueError

#### `ƒ` `_ensure_local_target_is_package_or_archive(path: Path) -> None`  L137
  - 分支数 2，函数体节点数 37；raise: ValueError('Local review targets must be .skill archives or directories containing a root SKILL.md')；return: None
  - 调用: is_dir, is_file, ValueError

#### `ƒ` `_tool_message_content_payload(payload: dict) -> dict`  L145
  - _文档首行_（仅供参考）: Keep model-visible review data compact; full raw renders stay in artifact.
  - 分支数 0，函数体节点数 35；return: {'untrusted_review_data': payload['untrusted_review_data'], 'facts': payload['facts'], 'artifacts': payload['artifacts'], 'static_report': payload['static_report']}

#### `ƒ` `_neutralize_review_content(content: str) -> str`  L155
  - 分支数 0，函数体节点数 15；return: neutralize_untrusted_tags(content)
  - 调用: neutralize_untrusted_tags

#### `ƒ` `_semantic_artifacts(snapshot: dict, *, include_content: IncludeContent) -> list[dict]`  L161
  - 分支数 6，函数体节点数 164；return: [], artifacts
  - 调用: get, str, _is_semantic_artifact, len, append

#### `ƒ` `_is_semantic_artifact(path: str) -> bool`  L184
  - 分支数 1，函数体节点数 40；return: True, path.startswith(('references/', 'templates/', 'evals/')) and path.endswith(('.md', '.json', '.txt', '.yaml', '.yml'))
  - 调用: startswith, endswith

## 文件内调用关系
- `review_skill_package` -> _snapshot_for_target, _semantic_artifacts, _tool_message_content_payload, _neutralize_review_content
- `_snapshot_for_target` -> _ensure_local_target_allowed
- `_ensure_local_target_allowed` -> _ensure_local_target_is_package_or_archive
- `_semantic_artifacts` -> _is_semantic_artifact
