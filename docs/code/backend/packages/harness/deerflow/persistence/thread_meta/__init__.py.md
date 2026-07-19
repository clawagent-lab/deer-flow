# `backend/packages/harness/deerflow/persistence/thread_meta/__init__.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/thread_meta/__init__.py`  ·  行数: 40

**模块文档首行**（仅供参考）: Thread metadata persistence — ORM, abstract store, and concrete implementations.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 1 个
- `__all__`: InvalidMetadataFilterError, MemoryThreadMetaStore, ThreadMetaRepository, ThreadMetaRow, ThreadMetaStore, make_thread_store

## 依赖（import）
- `__future__` -> annotations
- `typing` -> TYPE_CHECKING
- `deerflow.persistence.thread_meta.base` -> InvalidMetadataFilterError, ThreadMetaStore
- `deerflow.persistence.thread_meta.memory` -> MemoryThreadMetaStore
- `deerflow.persistence.thread_meta.model` -> ThreadMetaRow
- `deerflow.persistence.thread_meta.sql` -> ThreadMetaRepository

## 模块级常量
- `__all__` = ['InvalidMetadataFilterError', 'MemoryThreadMetaStore', '...

## 函数
#### `ƒ` `make_thread_store(session_factory: async_sessionmaker[AsyncSession] | None, store: BaseStore | None) -> ThreadMetaStore`  L26
  - _文档首行_（仅供参考）: Create the appropriate ThreadMetaStore based on available backends.
  - 分支数 2，函数体节点数 52；raise: ValueError('make_thread_store requires either a session_factory (SQL) or a store (memory)')；return: ThreadMetaRepository(session_factory), MemoryThreadMetaStore(store)
  - 调用: ThreadMetaRepository, ValueError, MemoryThreadMetaStore

## 文件内调用关系
_无文件内调用_
