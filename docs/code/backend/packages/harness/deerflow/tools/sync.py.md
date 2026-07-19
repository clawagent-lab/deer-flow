# `backend/packages/harness/deerflow/tools/sync.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/sync.py`  ·  行数: 93

**模块文档首行**（仅供参考）: Utilities for invoking async tools from synchronous agent paths.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, atexit, concurrent.futures, contextvars, functools, logging
- `collections.abc` -> Callable
- `typing` -> Any, get_type_hints
- `langchain_core.runnables` -> RunnableConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SYNC_TOOL_EXECUTOR` = concurrent.futures.ThreadPoolExecutor(max_workers=10, thr...

## 函数
#### `ƒ` `_get_runnable_config_param(func: Callable[..., Any]) -> str | None`  L22
  - _文档首行_（仅供参考）: Return the coroutine parameter that expects LangChain RunnableConfig.
  - 分支数 4，函数体节点数 74；return: None, name
  - 调用: isinstance, get_type_hints, items

#### `ƒ` `make_sync_tool_wrapper(coro: Callable[..., Any], tool_name: str) -> Callable[..., Any]`  L38
  - _文档首行_（仅供参考）: Build a synchronous wrapper for an asynchronous tool coroutine.
  - 分支数 5，函数体节点数 228；raise: bare raise；return: future.result(), asyncio.run(coro(*args, **kwargs)), run_coroutine(*args, **kwargs), sync_wrapper
  - 调用: _get_runnable_config_param, get_running_loop, is_running, copy_context, submit, run, coro, result, error, run_coroutine
  - 子进程: run (L73), run (L75)

## 文件内调用关系
- `make_sync_tool_wrapper` -> _get_runnable_config_param
