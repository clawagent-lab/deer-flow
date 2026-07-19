# `backend/packages/harness/deerflow/runtime/events/store/__init__.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/events/store/__init__.py`  ·  行数: 27

## 模块概览
- 函数 1 个，类 0 个，模块级常量 1 个
- `__all__`: MemoryRunEventStore, RunEventStore, make_run_event_store

## 依赖（import）
- `deerflow.runtime.events.store.base` -> RunEventStore
- `deerflow.runtime.events.store.memory` -> MemoryRunEventStore

## 模块级常量
- `__all__` = ['MemoryRunEventStore', 'RunEventStore', 'make_run_event_...

## 函数
#### `ƒ` `make_run_event_store(config) -> RunEventStore`  L5
  - _文档首行_（仅供参考）: Create a RunEventStore based on run_events.backend configuration.
  - 分支数 4，函数体节点数 91；raise: ValueError(f'Unknown run_events backend: {config.backend!r}')；return: MemoryRunEventStore(), DbRunEventStore(sf, max_trace_content=config.max_trace_content), JsonlRunEventStore()
  - 调用: MemoryRunEventStore, get_session_factory, DbRunEventStore, JsonlRunEventStore, ValueError

## 文件内调用关系
_无文件内调用_
