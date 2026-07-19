# `backend/debug.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/debug.py`  ·  行数: 169

**模块文档首行**（仅供参考）: Debug script for lead_agent.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, logging
- `dotenv` -> load_dotenv

## 模块级常量
- `_LOG_FMT` = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
- `_LOG_DATEFMT` = '%Y-%m-%d %H:%M:%S'

## 函数
#### `ƒ` `_setup_logging(log_level: int) -> None`  L37
  - _文档首行_（仅供参考）: Route logs to ``debug.log`` using *log_level* for the initial root/file setup.
  - 分支数 1，函数体节点数 96
  - 调用: list, removeHandler, close, setLevel, FileHandler, setFormatter, Formatter, addHandler

#### `⏵ƒ` `async main()`  L63
  - 分支数 11，函数体节点数 442
  - 调用: _setup_logging, get_app_config, apply_logging_level, initialize_mcp_tools, print, Runtime, make_lead_agent, PromptSession, InMemoryHistory, set, strip, prompt_async, input, lower, HumanMessage, ainvoke, get, get_effective_user_id, get_paths, resolve_virtual_path（+2）

## 文件内调用关系
- `main` -> _setup_logging
