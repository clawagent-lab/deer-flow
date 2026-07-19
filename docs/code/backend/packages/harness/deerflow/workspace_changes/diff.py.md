# `backend/packages/harness/deerflow/workspace_changes/diff.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/workspace_changes/diff.py`  ·  行数: 197

## 模块概览
- 函数 8 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: difflib
- `__future__` -> annotations
- `.types` -> DiffUnavailableReason, FileSnapshot, WorkspaceChangeLimits, WorkspaceChangeResult, WorkspaceChangeStatus, WorkspaceChangeSummary, WorkspaceFileChange, WorkspaceSnapshot

## 函数
#### `ƒ` `compare_snapshots(before: WorkspaceSnapshot, after: WorkspaceSnapshot, *, limits: WorkspaceChangeLimits | None) -> WorkspaceChangeResult`  L17
  - 分支数 7，函数体节点数 423；return: WorkspaceChangeResult(summary=WorkspaceChangeSummary(created=created, modified=modified, deleted=deleted, additions=additions, deletions=deletions, truncated=truncated), files=changes, limits=resolved_limits)
  - 调用: WorkspaceChangeLimits, sorted, set, get, _same_file, _status, _build_diff, max, len, encode, append, WorkspaceFileChange, bool, WorkspaceChangeResult, WorkspaceChangeSummary

#### `ƒ` `get_changed_paths(before: WorkspaceSnapshot, after: WorkspaceSnapshot) -> set[str]`  L95
  - 分支数 2，函数体节点数 95；return: changed
  - 调用: set, get, _same_file, add

#### `ƒ` `_status(before_file: FileSnapshot | None, after_file: FileSnapshot | None) -> WorkspaceChangeStatus`  L106
  - 分支数 2，函数体节点数 34；return: 'created', 'deleted', 'modified'

#### `ƒ` `_same_file(before_file: FileSnapshot, after_file: FileSnapshot) -> bool`  L117
  - 分支数 1，函数体节点数 61；return: before_file.sha256 == after_file.sha256, before_file.size == after_file.size and before_file.mtime_ns == after_file.mtime_ns

#### `ƒ` `_build_diff(path: str, before_file: FileSnapshot | None, after_file: FileSnapshot | None, *, remaining_bytes: int) -> tuple[str, int, int, bool, DiffUnavailableReason | None]`  L123
  - 分支数 4，函数体节点数 221；return: ('', 0, 0, False, reason), ('', 0, 0, False, None), ('', additions, deletions, True, 'truncated'), (diff, additions, deletions, False, None)
  - 调用: _diff_unavailable_reason, _snapshot_text, list, unified_diff, splitlines, join, _count_diff_lines, len, encode

#### `ƒ` `_diff_unavailable_reason(before_file: FileSnapshot | None, after_file: FileSnapshot | None) -> DiffUnavailableReason | None`  L158
  - 分支数 2，函数体节点数 70；return: preferred, None
  - 调用: any

#### `ƒ` `_snapshot_text(file: FileSnapshot | None) -> str | None`  L169
  - 分支数 5，函数体节点数 66；return: '', file.text, cached.read(), None
  - 调用: open, read
  - 文件IO: open (L176), read (L177)

#### `ƒ` `_count_diff_lines(lines: list[str]) -> tuple[int, int]`  L183
  - 分支数 4，函数体节点数 79；return: (additions, deletions)
  - 调用: startswith

## 文件内调用关系
- `compare_snapshots` -> _same_file, _status, _build_diff
- `get_changed_paths` -> _same_file
- `_build_diff` -> _diff_unavailable_reason, _snapshot_text, _count_diff_lines
