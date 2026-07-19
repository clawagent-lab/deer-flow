# `backend/packages/harness/deerflow/mcp/cache.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/mcp/cache.py`  ·  行数: 227

**模块文档首行**（仅供参考）: Cache for MCP tools to avoid repeated loading.

## 模块概览
- 函数 7 个，类 0 个，模块级常量 7 个

## 依赖（import）
- 模块: asyncio, hashlib, logging
- `pathlib` -> Path
- `langchain_core.tools` -> BaseTool

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_mcp_tools_cache` = None
- `_cache_initialized` = False
- `_initialization_lock` = asyncio.Lock()
- `_ConfigSignature` = tuple[float | None, int | None, str | None]
- `_config_path` = None
- `_config_signature` = None

## 函数
#### `ƒ` `_resolve_config_path() -> Path | None`  L29
  - _文档首行_（仅供参考）: Resolve the extensions config file path, or ``None`` when unconfigured.
  - 分支数 0，函数体节点数 17；return: ExtensionsConfig.resolve_config_path()
  - 调用: resolve_config_path

#### `ƒ` `_get_config_signature(config_path: Path) -> _ConfigSignature | None`  L36
  - _文档首行_（仅供参考）: Get cache metadata for the extensions config file, including a content digest.
  - 分支数 4，函数体节点数 102；return: None, (stat_result.st_mtime, stat_result.st_size, None), (stat_result.st_mtime, stat_result.st_size, digest.hexdigest())
  - 调用: stat, sha256, open, iter, read, update, hexdigest
  - 文件IO: stat (L45), open (L57), read (L58)

#### `ƒ` `_current_config_state() -> tuple[Path | None, _ConfigSignature | None]`  L66
  - _文档首行_（仅供参考）: Return the currently resolved extensions config path and its signature.
  - 分支数 1，函数体节点数 47；return: (None, None), (config_path, _get_config_signature(config_path))
  - 调用: _resolve_config_path, _get_config_signature

#### `ƒ` `_is_cache_stale() -> bool`  L74
  - _文档首行_（仅供参考）: Check if the cache is stale due to config file changes.
  - 分支数 4，函数体节点数 80；return: False, True
  - 调用: _current_config_state, info

#### `⏵ƒ` `async initialize_mcp_tools() -> list[BaseTool]`  L115
  - _文档首行_（仅供参考）: Initialize and cache MCP tools.
  - 分支数 2，函数体节点数 79；return: _mcp_tools_cache or [], _mcp_tools_cache
  - 调用: info, get_mcp_tools, _current_config_state, len

#### `ƒ` `get_cached_mcp_tools() -> list[BaseTool]`  L141
  - _文档首行_（仅供参考）: Get cached MCP tools with lazy initialization.
  - 分支数 6，函数体节点数 142；return: [], _mcp_tools_cache or []
  - 调用: _is_cache_stale, info, reset_mcp_tools_cache, get_event_loop, is_running, ThreadPoolExecutor, submit, initialize_mcp_tools, result, run_until_complete, run, exception
  - 子进程: run (L180)

#### `ƒ` `reset_mcp_tools_cache() -> None`  L191
  - _文档首行_（仅供参考）: Reset the MCP tools cache.
  - 分支数 1，函数体节点数 57
  - 调用: close_all_sync, get_session_pool, debug, reset_session_pool, info

## 文件内调用关系
- `_current_config_state` -> _resolve_config_path, _get_config_signature
- `_is_cache_stale` -> _current_config_state
- `initialize_mcp_tools` -> _current_config_state
- `get_cached_mcp_tools` -> _is_cache_stale, reset_mcp_tools_cache, initialize_mcp_tools
