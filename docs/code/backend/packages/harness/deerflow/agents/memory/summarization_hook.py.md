# `backend/packages/harness/deerflow/agents/memory/summarization_hook.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/summarization_hook.py`  ·  行数: 29

**模块文档首行**（仅供参考）: Hooks fired before summarization removes messages from state.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `deerflow.agents.memory` -> get_memory_manager
- `deerflow.agents.middlewares.summarization_middleware` -> SummarizationEvent
- `deerflow.config.memory_config` -> get_memory_config
- `deerflow.runtime.user_context` -> resolve_runtime_user_id

## 函数
#### `ƒ` `memory_flush_hook(event: SummarizationEvent) -> None`  L11
  - _文档首行_（仅供参考）: Flush messages about to be summarized into the memory queue.
  - 分支数 1，函数体节点数 61；return: None
  - 调用: get_memory_config, resolve_runtime_user_id, add_nowait, get_memory_manager, list

## 文件内调用关系
_无文件内调用_
