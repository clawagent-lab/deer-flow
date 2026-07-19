# `backend/packages/harness/deerflow/workspace_changes/api.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/workspace_changes/api.py`  ·  行数: 76

## 模块概览
- 函数 4 个，类 0 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any
- `.types` -> WORKSPACE_CHANGES_EVENT_TYPE, WORKSPACE_CHANGES_METADATA_KEY

## 模块级常量
- `EMPTY_SUMMARY` = {'created': 0, 'modified': 0, 'deleted': 0, 'additions': ...

## 函数
#### `⏵ƒ` `async get_workspace_changes_response(event_store: Any, thread_id: str, run_id: str, *, include_files: bool, include_diff: bool) -> dict[str, Any]`  L17
  - 分支数 4，函数体节点数 160；return: _empty_response(), response
  - 调用: list_events, _empty_response, _extract_workspace_changes_payload, isinstance, dict, setdefault, _without_diff

#### `ƒ` `_empty_response() -> dict[str, Any]`  L50
  - 分支数 0，函数体节点数 29；return: {'available': False, 'version': 1, 'summary': dict(EMPTY_SUMMARY), 'files': [], 'limits': {}}
  - 调用: dict

#### `ƒ` `_extract_workspace_changes_payload(event: dict[str, Any]) -> Any`  L60
  - 分支数 2，函数体节点数 72；return: metadata[WORKSPACE_CHANGES_METADATA_KEY], content, None
  - 调用: get, isinstance

#### `ƒ` `_without_diff(file: Any) -> Any`  L70
  - 分支数 1，函数体节点数 38；return: file, sanitized
  - 调用: isinstance, dict

## 文件内调用关系
- `get_workspace_changes_response` -> _empty_response, _extract_workspace_changes_payload, _without_diff
