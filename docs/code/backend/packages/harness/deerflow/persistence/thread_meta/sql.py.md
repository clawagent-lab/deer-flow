# `backend/packages/harness/deerflow/persistence/thread_meta/sql.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/thread_meta/sql.py`  ·  行数: 244

**模块文档首行**（仅供参考）: SQLAlchemy-backed thread metadata repository.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `typing` -> Any
- `sqlalchemy` -> select, update
- `sqlalchemy.ext.asyncio` -> AsyncSession, async_sessionmaker
- `deerflow.persistence.json_compat` -> json_match
- `deerflow.persistence.thread_meta.base` -> InvalidMetadataFilterError, ThreadMetaStore
- `deerflow.persistence.thread_meta.model` -> ThreadMetaRow
- `deerflow.runtime.user_context` -> AUTO, _AutoSentinel, resolve_user_id
- `deerflow.utils.time` -> coerce_iso

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `ThreadMetaRepository`  L21
- 继承: ThreadMetaStore
- 方法:
  #### `st` `_row_to_dict(row: ThreadMetaRow) -> dict[str, Any]`    @staticmethod  L26
    - 分支数 2，函数体节点数 81；return: d
    - 调用: to_dict, pop, get, isinstance, coerce_iso
  #### `m` `__init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None`  L22
    - 分支数 0，函数体节点数 18
  #### `⏵m` `async create(self, thread_id: str, *, assistant_id: str | None, user_id: str | None | _AutoSentinel, display_name: str | None, metadata: dict | None) -> dict`  L37
    - 分支数 1，函数体节点数 132；return: self._row_to_dict(row)
    - 调用: resolve_user_id, now, ThreadMetaRow, _sf, add, commit, refresh, _row_to_dict
  #### `⏵m` `async get(self, thread_id: str, *, user_id: str | None | _AutoSentinel) -> dict | None`  L65
    - 分支数 3，函数体节点数 89；return: None, self._row_to_dict(row)
    - 调用: resolve_user_id, _sf, get, _row_to_dict
  - 网络调用: get (L73)
  #### `⏵m` `async check_access(self, thread_id: str, user_id: str, *, require_existing: bool) -> bool`  L81
    - _文档首行_（仅供参考）: Check if ``user_id`` has access to ``thread_id``.
    - 分支数 3，函数体节点数 69；return: not require_existing, True, row.user_id == user_id
    - 调用: _sf, get
  - 网络调用: get (L104)
  #### `⏵m` `async search(self, *, metadata: dict[str, Any] | None, status: str | None, limit: int, offset: int, user_id: str | None | _AutoSentinel) -> list[dict[str, Any]]`  L111
    - _文档首行_（仅供参考）: Search threads with optional metadata and status filters.
    - 分支数 7，函数体节点数 290；raise: InvalidMetadataFilterError(f'All metadata filter keys were rejected as unsafe: {rejected_keys}')；return: [self._row_to_dict(r) for r in result.scalars()]
    - 调用: resolve_user_id, order_by, select, desc, where, items, json_match, warning, ascii, join, sorted, str, InvalidMetadataFilterError, offset, limit, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async _check_ownership(self, session: AsyncSession, thread_id: str, resolved_user_id: str | None) -> bool`  L152
    - _文档首行_（仅供参考）: Return True if the row exists and is owned (or filter bypassed).
    - 分支数 1，函数体节点数 56；return: True, row is not None and row.user_id == resolved_user_id
    - 调用: get
  - 网络调用: get (L156)
  #### `⏵m` `async update_display_name(self, thread_id: str, display_name: str, *, user_id: str | None | _AutoSentinel) -> None`  L159
    - _文档首行_（仅供参考）: Update the display_name (title) for a thread.
    - 分支数 2，函数体节点数 103；return: None
    - 调用: resolve_user_id, _sf, _check_ownership, execute, values, where, update, now, commit
  #### `⏵m` `async update_status(self, thread_id: str, status: str, *, user_id: str | None | _AutoSentinel) -> None`  L174
    - 分支数 2，函数体节点数 101；return: None
    - 调用: resolve_user_id, _sf, _check_ownership, execute, values, where, update, now, commit
  #### `⏵m` `async update_metadata(self, thread_id: str, metadata: dict, *, user_id: str | None | _AutoSentinel) -> None`  L188
    - _文档首行_（仅供参考）: Merge ``metadata`` into ``metadata_json``.
    - 分支数 3，函数体节点数 127；return: None
    - 调用: resolve_user_id, _sf, get, dict, update, now, commit
  - 网络调用: get (L203)
  #### `⏵m` `async update_owner(self, thread_id: str, owner_user_id: str, *, user_id: str | None | _AutoSentinel) -> None`  L214
    - _文档首行_（仅供参考）: Move a thread metadata row to ``owner_user_id``.
    - 分支数 2，函数体节点数 103；return: None
    - 调用: resolve_user_id, _sf, _check_ownership, execute, values, where, update, now, commit
  #### `⏵m` `async delete(self, thread_id: str, *, user_id: str | None | _AutoSentinel) -> None`  L229
    - 分支数 3，函数体节点数 91；return: None
    - 调用: resolve_user_id, _sf, get, delete, commit
  - 网络调用: get (L237), delete (L242)

## 文件内调用关系
- `ThreadMetaRepository._row_to_dict` -> get
- `ThreadMetaRepository.create` -> _row_to_dict
- `ThreadMetaRepository.get` -> get, _row_to_dict
- `ThreadMetaRepository.check_access` -> get
- `ThreadMetaRepository.search` -> _row_to_dict
- `ThreadMetaRepository._check_ownership` -> get
- `ThreadMetaRepository.update_display_name` -> _check_ownership
- `ThreadMetaRepository.update_status` -> _check_ownership
- `ThreadMetaRepository.update_metadata` -> get
- `ThreadMetaRepository.update_owner` -> _check_ownership
- `ThreadMetaRepository.delete` -> get, delete
