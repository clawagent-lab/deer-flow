# `backend/packages/harness/deerflow/community/searxng/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/searxng/tools.py`  ·  行数: 59

## 模块概览
- 函数 3 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: json, logging
- `langchain.tools` -> tool
- `deerflow.config` -> get_app_config
- `.searxng_client` -> SearxngClient

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_get_tool_config(tool_name: str) -> dict | None`  L13
  - _文档首行_（仅供参考）: Get tool config extras safely, returning None if not configured.
  - 分支数 1，函数体节点数 48；return: None, extras if extras is not None else {}
  - 调用: get_tool_config, get_app_config

#### `ƒ` `_get_searxng_client() -> SearxngClient`  L22
  - 分支数 1，函数体节点数 39；return: SearxngClient(base_url=base_url)
  - 调用: _get_tool_config, get, SearxngClient

#### `⏵ƒ` `async web_search_tool(query: str) -> str`    @tool(...)  L31
  - _文档首行_（仅供参考）: Search the web using SearXNG.
  - 分支数 2，函数体节点数 162；return: json.dumps(normalized, indent=2, ensure_ascii=False), json.dumps({'error': str(e), 'query': query}, ensure_ascii=False)
  - 调用: _get_tool_config, get, isinstance, int, _get_searxng_client, search, dumps, error, str, tool

## 文件内调用关系
- `_get_searxng_client` -> _get_tool_config
- `web_search_tool` -> _get_tool_config, _get_searxng_client
