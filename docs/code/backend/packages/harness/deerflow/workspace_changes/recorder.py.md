# `backend/packages/harness/deerflow/workspace_changes/recorder.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/workspace_changes/recorder.py`  ·  行数: 167

## 模块概览
- 函数 7 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, logging, shutil, tempfile
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> Any
- `deerflow.config` -> get_paths
- `.diff` -> compare_snapshots, get_changed_paths
- `.scanner` -> scan_workspace_roots
- `.types` -> WORKSPACE_CHANGES_EVENT_TYPE, WORKSPACE_CHANGES_METADATA_KEY, WorkspaceChangeLimits, WorkspaceRoot, WorkspaceSnapshot

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `build_thread_workspace_roots(thread_id: str, *, user_id: str | None) -> list[WorkspaceRoot]`  L25
  - 分支数 0，函数体节点数 63；return: [WorkspaceRoot(name='workspace', host_path=paths.sandbox_work_dir(thread_id, user_id=user_id), virtual_prefix='/mnt/user-data/workspace'), WorkspaceRoot(name='outputs', host_path=paths.sandbox_outputs_dir(thread_id, user_id=user_id), virtual_prefix='/mnt/user-data/outputs')]
  - 调用: get_paths, WorkspaceRoot, sandbox_work_dir, sandbox_outputs_dir

#### `ƒ` `_prepare_capture(thread_id: str, *, user_id: str | None, include_text: bool) -> tuple[list[WorkspaceRoot], Path | None]`  L41
  - 分支数 0，函数体节点数 66；return: (roots, text_cache_dir)
  - 调用: build_thread_workspace_roots, Path, mkdtemp

#### `⏵ƒ` `async _remove_text_cache_dir(text_cache_dir: str | Path) -> None`  L50
  - _文档首行_（仅供参考）: Remove a snapshot's text cache off the event loop.
  - 分支数 1，函数体节点数 42
  - 调用: to_thread, warning

#### `⏵ƒ` `async _reclaim_prepare_and_cleanup(prepare: asyncio.Future[tuple[list[WorkspaceRoot], Path | None]]) -> None`  L62
  - _文档首行_（仅供参考）: Await a cancelled prepare handoff and remove any dir it created.
  - 分支数 2，函数体节点数 57；return: None
  - 调用: _remove_text_cache_dir

#### `⏵ƒ` `async capture_workspace_snapshot(thread_id: str, *, user_id: str | None, limits: WorkspaceChangeLimits | None, include_text: bool) -> WorkspaceSnapshot`  L77
  - 分支数 5，函数体节点数 145；raise: bare raise；return: await asyncio.to_thread(scan_workspace_roots, roots, limits=limits, include_text=include_text, text_cache_dir=text_cache_dir)
  - 调用: ensure_future, to_thread, shield, _reclaim_prepare_and_cleanup, done, _remove_text_cache_dir

#### `⏵ƒ` `async record_workspace_changes(event_store: Any, thread_id: str, run_id: str, before: WorkspaceSnapshot, *, user_id: str | None, limits: WorkspaceChangeLimits | None) -> dict | None`  L119
  - 分支数 2，函数体节点数 219；return: None, await event_store.put(thread_id=thread_id, run_id=run_id, event_type=WORKSPACE_CHANGES_EVENT_TYPE, category='workspace', content=content, metadata={WORKSPACE_CHANGES_METADATA_KEY: payload})
  - 调用: to_thread, get_changed_paths, compare_snapshots, has_changes, to_dict, put, _cleanup_snapshot_text_cache

#### `⏵ƒ` `async _cleanup_snapshot_text_cache(snapshot: WorkspaceSnapshot) -> None`  L164
  - 分支数 1，函数体节点数 20
  - 调用: _remove_text_cache_dir

## 文件内调用关系
- `_prepare_capture` -> build_thread_workspace_roots
- `_reclaim_prepare_and_cleanup` -> _remove_text_cache_dir
- `capture_workspace_snapshot` -> _reclaim_prepare_and_cleanup, _remove_text_cache_dir
- `record_workspace_changes` -> _cleanup_snapshot_text_cache
- `_cleanup_snapshot_text_cache` -> _remove_text_cache_dir
