# `backend/packages/harness/deerflow/tracing/metadata.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tracing/metadata.py`  ·  行数: 115

**模块文档首行**（仅供参考）: Langfuse trace-attribute metadata builders.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any
- `deerflow.config` -> get_enabled_tracing_providers
- `deerflow.trace_context` -> DEERFLOW_TRACE_METADATA_KEY, get_current_trace_id, normalize_trace_id

## 模块级常量
- `_DEFAULT_TRACE_NAME` = 'lead-agent'

## 函数
#### `ƒ` `build_langfuse_trace_metadata(*, thread_id: str | None, user_id: str | None, assistant_id: str | None, model_name: str | None, environment: str | None, deerflow_trace_id: str | None) -> dict[str, Any]`  L29
  - _文档首行_（仅供参考）: Return Langfuse trace-attribute metadata for ``RunnableConfig.metadata``.
  - 分支数 5，函数体节点数 175；return: {}, metadata
  - 调用: get_enabled_tracing_providers, normalize_trace_id, get_current_trace_id, append

#### `ƒ` `inject_langfuse_metadata(config: dict, *, thread_id: str | None, user_id: str | None, assistant_id: str | None, model_name: str | None, environment: str | None, deerflow_trace_id: str | None) -> None`  L80
  - _文档首行_（仅供参考）: Merge Langfuse trace-attribute metadata into ``config["metadata"]``.
  - 分支数 2，函数体节点数 124；return: None
  - 调用: build_langfuse_trace_metadata, dict, get, items, setdefault

## 文件内调用关系
- `inject_langfuse_metadata` -> build_langfuse_trace_metadata
