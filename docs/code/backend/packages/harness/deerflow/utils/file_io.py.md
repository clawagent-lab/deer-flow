# `backend/packages/harness/deerflow/utils/file_io.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/utils/file_io.py`  ·  行数: 52

**模块文档首行**（仅供参考）: Dedicated async offload helper for filesystem work.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, atexit, contextvars, functools, logging, os
- `__future__` -> annotations
- `collections.abc` -> Callable
- `concurrent.futures` -> ThreadPoolExecutor

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_FILE_IO_EXECUTOR` = ThreadPoolExecutor(max_workers=_default_file_io_workers()...

## 函数
#### `ƒ` `_default_file_io_workers() -> int`  L17
  - 分支数 3，函数体节点数 61；return: workers, min(32, (os.cpu_count() or 1) + 4)
  - 调用: getenv, int, warning, min, cpu_count
  - 环境变量: getenv (L18)

#### `ƒ` `_shutdown_file_io_executor() -> None`  L33
  - 分支数 0，函数体节点数 13
  - 调用: shutdown

#### `⏵ƒ` `async run_file_io(func: Callable[P, T], *args, **kwargs) -> T`  L40
  - _文档首行_（仅供参考）: Run blocking filesystem-oriented work on the dedicated file IO pool.
  - 分支数 0，函数体节点数 77；可变参数（*args/**kwargs）；return: await loop.run_in_executor(_FILE_IO_EXECUTOR, ctx.run, call)
  - 调用: get_running_loop, copy_context, partial, run_in_executor

## 文件内调用关系
_无文件内调用_
