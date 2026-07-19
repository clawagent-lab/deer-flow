# `backend/packages/harness/deerflow/persistence/thread_meta/memory.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/thread_meta/memory.py`  ·  行数: 160

**模块文档首行**（仅供参考）: In-memory ThreadMetaStore backed by LangGraph BaseStore.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any
- `langgraph.store.base` -> BaseStore
- `deerflow.persistence.thread_meta.base` -> ThreadMetaStore
- `deerflow.runtime.user_context` -> AUTO, _AutoSentinel, resolve_user_id
- `deerflow.utils.time` -> coerce_iso, now_iso

## 模块级常量
- `THREADS_NS` = ('threads',)

## 类
### 类 `MemoryThreadMetaStore`  L21
- 继承: ThreadMetaStore
- 方法:
  #### `st` `_item_to_dict(item) -> dict[str, Any]`    @staticmethod  L145
    - _文档首行_（仅供参考）: Convert a Store SearchItem to the dict format expected by callers.
    - 分支数 0，函数体节点数 90；return: {'thread_id': item.key, 'assistant_id': val.get('assistant_id'), 'user_id': val.get('user_id'), 'display_name': val.get('display_name'), 'status': val.get('status', 'idle'), 'metadata': val.get('metadata', {}), 'created_at': coerce_iso(val.get('created_at', '')), 'updated_at': coerce_iso(val.get('updated_at', ''))}
    - 调用: get, coerce_iso
  #### `m` `__init__(self, store: BaseStore) -> None`  L22
    - 分支数 0，函数体节点数 14
  #### `⏵m` `async _get_owned_record(self, thread_id: str, user_id: str | None | _AutoSentinel, method_name: str) -> dict | None`  L25
    - _文档首行_（仅供参考）: Fetch a record and verify ownership. Returns a mutable copy, or None.
    - 分支数 2，函数体节点数 93；return: None, record
    - 调用: resolve_user_id, aget, dict, get
  #### `⏵m` `async create(self, thread_id: str, *, assistant_id: str | None, user_id: str | None | _AutoSentinel, display_name: str | None, metadata: dict | None) -> dict`  L41
    - 分支数 0，函数体节点数 117；return: record
    - 调用: resolve_user_id, now_iso, aput
  #### `⏵m` `async get(self, thread_id: str, *, user_id: str | None | _AutoSentinel) -> dict | None`  L66
    - 分支数 0，函数体节点数 35；return: await self._get_owned_record(thread_id, user_id, 'MemoryThreadMetaStore.get')
    - 调用: _get_owned_record
  #### `⏵m` `async search(self, *, metadata: dict[str, Any] | None, status: str | None, limit: int, offset: int, user_id: str | None | _AutoSentinel) -> list[dict[str, Any]]`  L69
    - 分支数 3，函数体节点数 158；return: [self._item_to_dict(item) for item in items]
    - 调用: resolve_user_id, update, asearch, _item_to_dict
  #### `⏵m` `async check_access(self, thread_id: str, user_id: str, *, require_existing: bool) -> bool`  L95
    - 分支数 2，函数体节点数 67；return: not require_existing, True, record_user_id == user_id
    - 调用: aget, get
  #### `⏵m` `async update_display_name(self, thread_id: str, display_name: str, *, user_id: str | None | _AutoSentinel) -> None`  L104
    - 分支数 1，函数体节点数 75；return: None
    - 调用: _get_owned_record, now_iso, aput
  #### `⏵m` `async update_status(self, thread_id: str, status: str, *, user_id: str | None | _AutoSentinel) -> None`  L112
    - 分支数 1，函数体节点数 75；return: None
    - 调用: _get_owned_record, now_iso, aput
  #### `⏵m` `async update_metadata(self, thread_id: str, metadata: dict, *, user_id: str | None | _AutoSentinel) -> None`  L120
    - 分支数 1，函数体节点数 98；return: None
    - 调用: _get_owned_record, dict, get, update, now_iso, aput
  #### `⏵m` `async update_owner(self, thread_id: str, owner_user_id: str, *, user_id: str | None | _AutoSentinel) -> None`  L130
    - 分支数 1，函数体节点数 75；return: None
    - 调用: _get_owned_record, now_iso, aput
  #### `⏵m` `async delete(self, thread_id: str, *, user_id: str | None | _AutoSentinel) -> None`  L138
    - 分支数 1，函数体节点数 53；return: None
    - 调用: _get_owned_record, adelete

## 文件内调用关系
- `MemoryThreadMetaStore._get_owned_record` -> get
- `MemoryThreadMetaStore.get` -> _get_owned_record
- `MemoryThreadMetaStore.search` -> _item_to_dict
- `MemoryThreadMetaStore.check_access` -> get
- `MemoryThreadMetaStore.update_display_name` -> _get_owned_record
- `MemoryThreadMetaStore.update_status` -> _get_owned_record
- `MemoryThreadMetaStore.update_metadata` -> _get_owned_record, get
- `MemoryThreadMetaStore.update_owner` -> _get_owned_record
- `MemoryThreadMetaStore.delete` -> _get_owned_record
- `MemoryThreadMetaStore._item_to_dict` -> get
