# `backend/packages/harness/deerflow/workspace_changes/__init__.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/workspace_changes/__init__.py`  ·  行数: 34

## 模块概览
- 函数 0 个，类 0 个，模块级常量 1 个
- `__all__`: WORKSPACE_CHANGES_EVENT_TYPE, WORKSPACE_CHANGES_METADATA_KEY, FileSnapshot, WorkspaceChangeLimits, WorkspaceChangeResult, WorkspaceChangeSummary, WorkspaceFileChange, WorkspaceRoot, WorkspaceSnapshot, capture_workspace_snapshot, compare_snapshots, get_changed_paths, get_workspace_changes_response, record_workspace_changes, scan_workspace_roots

## 依赖（import）
- `.api` -> get_workspace_changes_response
- `.diff` -> compare_snapshots, get_changed_paths
- `.recorder` -> capture_workspace_snapshot, record_workspace_changes
- `.scanner` -> scan_workspace_roots
- `.types` -> WORKSPACE_CHANGES_EVENT_TYPE, WORKSPACE_CHANGES_METADATA_KEY, FileSnapshot, WorkspaceChangeLimits, WorkspaceChangeResult, WorkspaceChangeSummary, WorkspaceFileChange, WorkspaceRoot, WorkspaceSnapshot

## 模块级常量
- `__all__` = ['WORKSPACE_CHANGES_EVENT_TYPE', 'WORKSPACE_CHANGES_METAD...
