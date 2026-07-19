# `backend/packages/harness/deerflow/runtime/__init__.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/__init__.py`  ·  行数: 54

**模块文档首行**（仅供参考）: LangGraph-compatible runtime — runs, streaming, and lifecycle management.

## 模块概览
- 函数 0 个，类 0 个，模块级常量 1 个
- `__all__`: checkpointer_context, get_checkpointer, make_checkpointer, reset_checkpointer, CancelOutcome, ConflictError, DisconnectMode, RunContext, RunManager, RunRecord, RunStatus, UnsupportedStrategyError, run_agent, serialize, serialize_channel_values, serialize_channel_values_for_api, serialize_lc_object, serialize_messages_tuple, strip_data_url_image_blocks, get_store, make_store, reset_store, store_context, END_SENTINEL, HEARTBEAT_SENTINEL, MemoryStreamBridge, StreamBridge, StreamEvent, make_stream_bridge

## 依赖（import）
- `.checkpointer` -> checkpointer_context, get_checkpointer, make_checkpointer, reset_checkpointer
- `.runs` -> CancelOutcome, ConflictError, DisconnectMode, RunContext, RunManager, RunRecord, RunStatus, UnsupportedStrategyError, run_agent
- `.serialization` -> serialize, serialize_channel_values, serialize_channel_values_for_api, serialize_lc_object, serialize_messages_tuple, strip_data_url_image_blocks
- `.store` -> get_store, make_store, reset_store, store_context
- `.stream_bridge` -> END_SENTINEL, HEARTBEAT_SENTINEL, MemoryStreamBridge, StreamBridge, StreamEvent, make_stream_bridge

## 模块级常量
- `__all__` = ['checkpointer_context', 'get_checkpointer', 'make_checkp...
