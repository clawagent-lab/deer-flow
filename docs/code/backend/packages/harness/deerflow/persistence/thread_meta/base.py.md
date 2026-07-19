# `backend/packages/harness/deerflow/persistence/thread_meta/base.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/thread_meta/base.py`  ·  行数: 91

**模块文档首行**（仅供参考）: Abstract interface for thread metadata storage.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 0 个

## 依赖（import）
- 模块: abc
- `__future__` -> annotations
- `typing` -> Any
- `deerflow.runtime.user_context` -> AUTO, _AutoSentinel

## 类
### 类 `InvalidMetadataFilterError`  L23
- 继承: ValueError
- _文档首行_: Raised when all client-supplied metadata filter keys are rejected.

### 类 `ThreadMetaStore`  L27
- 继承: abc.ABC
- 方法:
  #### `⏵m` `async create(self, thread_id: str, *, assistant_id: str | None, user_id: str | None | _AutoSentinel, display_name: str | None, metadata: dict | None) -> dict`    @abc.abstractmethod  L29
    - 分支数 0，函数体节点数 46
  #### `⏵m` `async get(self, thread_id: str, *, user_id: str | None | _AutoSentinel) -> dict | None`    @abc.abstractmethod  L41
    - 分支数 0，函数体节点数 28
  #### `⏵m` `async search(self, *, metadata: dict[str, Any] | None, status: str | None, limit: int, offset: int, user_id: str | None | _AutoSentinel) -> list[dict[str, Any]]`    @abc.abstractmethod  L45
    - 分支数 0，函数体节点数 64
  #### `⏵m` `async update_display_name(self, thread_id: str, display_name: str, *, user_id: str | None | _AutoSentinel) -> None`    @abc.abstractmethod  L57
    - 分支数 0，函数体节点数 27
  #### `⏵m` `async update_status(self, thread_id: str, status: str, *, user_id: str | None | _AutoSentinel) -> None`    @abc.abstractmethod  L61
    - 分支数 0，函数体节点数 27
  #### `⏵m` `async update_metadata(self, thread_id: str, metadata: dict, *, user_id: str | None | _AutoSentinel) -> None`    @abc.abstractmethod  L65
    - _文档首行_（仅供参考）: Merge ``metadata`` into the thread's metadata field.
    - 分支数 0，函数体节点数 29
  #### `⏵m` `async update_owner(self, thread_id: str, owner_user_id: str, *, user_id: str | None | _AutoSentinel) -> None`    @abc.abstractmethod  L75
    - _文档首行_（仅供参考）: Move a thread metadata row to a new owner.
    - 分支数 0，函数体节点数 29
  #### `⏵m` `async check_access(self, thread_id: str, user_id: str, *, require_existing: bool) -> bool`    @abc.abstractmethod  L84
    - _文档首行_（仅供参考）: Check if ``user_id`` has access to ``thread_id``.
    - 分支数 0，函数体节点数 22
  #### `⏵m` `async delete(self, thread_id: str, *, user_id: str | None | _AutoSentinel) -> None`    @abc.abstractmethod  L89
    - 分支数 0，函数体节点数 24

## 文件内调用关系
_无文件内调用_
