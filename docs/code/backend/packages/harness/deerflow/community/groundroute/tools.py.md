# `backend/packages/harness/deerflow/community/groundroute/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/groundroute/tools.py`  ·  行数: 167

**模块文档首行**（仅供参考）: GroundRoute community web search + fetch tools.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 7 个

## 依赖（import）
- 模块: json, logging, os, httpx
- `langchain.tools` -> tool
- `deerflow.config` -> get_app_config

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_GROUNDROUTE_ENDPOINT` = 'https://api.groundroute.ai/v1/search'
- `_DEFAULT_MAX_RESULTS` = 5
- `_MAX_RESULTS_CAP` = 50
- `_TIMEOUT_S` = 30.0
- `_FETCH_SNIPPET_LIMIT` = 4096
- `_api_key_warned` = set()

## 函数
#### `ƒ` `_get_api_key(tool_name: str) -> str | None`  L40
  - _文档首行_（仅供参考）: Resolve the GroundRoute key from a given tool's config block, then the env var.
  - 分支数 2，函数体节点数 71；return: api_key.strip(), os.getenv('GROUNDROUTE_API_KEY')
  - 调用: get_tool_config, get_app_config, get, isinstance, strip, getenv
  - 环境变量: getenv (L52)

#### `ƒ` `_coerce_max_results(value: object, *, default: int) -> int`  L55
  - 分支数 1，函数体节点数 56；return: max(1, min(coerced, _MAX_RESULTS_CAP))
  - 调用: int, warning, max, min

#### `ƒ` `_missing_key_error(tool_name: str, **context) -> str`  L64
  - 分支数 1，函数体节点数 47；可变参数（*args/**kwargs）；return: json.dumps({'error': 'GROUNDROUTE_API_KEY is not configured', **context}, ensure_ascii=False)
  - 调用: add, warning, dumps

#### `ƒ` `_post_search(api_key: str, body: dict) -> dict`  L74
  - 分支数 1，函数体节点数 55；return: response.json()
  - 调用: Client, post, raise_for_status, json
  - 网络调用: post (L76)

#### `ƒ` `web_search_tool(query: str, max_results: int | None) -> str`    @tool(...)  L86
  - _文档首行_（仅供参考）: Search the web for information using GroundRoute.
  - 分支数 5，函数体节点数 279；return: _missing_key_error('web_search', query=query), json.dumps({'error': f'GroundRoute API error: HTTP {e.response.status_code}', 'query': query}, ensure_ascii=False), json.dumps({'error': str(e), 'query': query}, ensure_ascii=False), json.dumps({'error': 'No results found', 'query': query}, ensure_ascii=False), json.dumps(normalized_results, indent=2, ensure_ascii=False)
  - 调用: get_tool_config, get_app_config, get, _coerce_max_results, _get_api_key, _missing_key_error, _post_search, error, dumps, type, str, tool

#### `ƒ` `web_fetch_tool(url: str) -> str`    @tool(...)  L136
  - _文档首行_（仅供参考）: Fetch the contents of a web page at a given URL via GroundRoute.
  - 分支数 3，函数体节点数 182；return: _missing_key_error('web_fetch', url=url), f'Error: GroundRoute API error: HTTP {e.response.status_code}', f'Error: {e}', 'Error: No results found', f'# {title}\n\n{content[:_FETCH_SNIPPET_LIMIT]}'
  - 调用: _get_api_key, _missing_key_error, _post_search, error, type, get, tool

## 文件内调用关系
- `web_search_tool` -> _coerce_max_results, _get_api_key, _missing_key_error, _post_search
- `web_fetch_tool` -> _get_api_key, _missing_key_error, _post_search
