# `backend/packages/harness/deerflow/community/fastcrw/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/fastcrw/tools.py`  ·  行数: 112

## 模块概览
- 函数 5 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: json, os
- `firecrawl` -> FirecrawlApp
- `langchain.tools` -> tool
- `deerflow.community.url_safety` -> validate_public_http_url
- `deerflow.config` -> get_app_config

## 模块级常量
- `DEFAULT_BASE_URL` = 'https://fastcrw.com/api'

## 函数
#### `ƒ` `_get_fastcrw_client(tool_name: str) -> FirecrawlApp`  L17
  - 分支数 5，函数体节点数 113；return: FirecrawlApp(api_key=api_key, api_url=base_url)
  - 调用: get_tool_config, get_app_config, get, getenv, FirecrawlApp
  - 环境变量: getenv (L27), getenv (L29)

#### `ƒ` `_get_tool_config_extra(tool_name: str) -> dict`  L33
  - 分支数 0，函数体节点数 36；return: dict(config.model_extra or {}) if config is not None else {}
  - 调用: get_tool_config, get_app_config, dict

#### `ƒ` `_coerce_bool(value: object, default: bool) -> bool`  L38
  - 分支数 4，函数体节点数 67；return: value, True, False, default
  - 调用: isinstance, lower, strip

#### `ƒ` `web_search_tool(query: str) -> str`    @tool(...)  L51
  - _文档首行_（仅供参考）: Search the web.
  - 分支数 2，函数体节点数 152；return: json_results, f'Error: {str(e)}'
  - 调用: get_tool_config, get_app_config, get, _get_fastcrw_client, search, getattr, dumps, str, tool
  - 反射: getattr (L70), getattr (L71), getattr (L72)

#### `ƒ` `web_fetch_tool(url: str) -> str`    @tool(...)  L83
  - _文档首行_（仅供参考）: Fetch the contents of a web page at a given URL.
  - 分支数 3，函数体节点数 141；return: url_error, 'Error: No content found', f'Error: {str(e)}', f'# {title}\n\n{markdown_content[:4096]}'
  - 调用: _get_tool_config_extra, _coerce_bool, get, validate_public_http_url, _get_fastcrw_client, scrape, str, tool

## 文件内调用关系
- `web_search_tool` -> _get_fastcrw_client
- `web_fetch_tool` -> _get_tool_config_extra, _coerce_bool, _get_fastcrw_client
