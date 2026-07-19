# `backend/packages/harness/deerflow/community/firecrawl/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/firecrawl/tools.py`  ·  行数: 74

## 模块概览
- 函数 3 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: json
- `firecrawl` -> FirecrawlApp
- `langchain.tools` -> tool
- `deerflow.config` -> get_app_config

## 函数
#### `ƒ` `_get_firecrawl_client(tool_name: str) -> FirecrawlApp`  L9
  - 分支数 1，函数体节点数 56；return: FirecrawlApp(api_key=api_key)
  - 调用: get_tool_config, get_app_config, get, FirecrawlApp

#### `ƒ` `web_search_tool(query: str) -> str`    @tool(...)  L18
  - _文档首行_（仅供参考）: Search the web.
  - 分支数 2，函数体节点数 152；return: json_results, f'Error: {str(e)}'
  - 调用: get_tool_config, get_app_config, get, _get_firecrawl_client, search, getattr, dumps, str, tool
  - 反射: getattr (L37), getattr (L38), getattr (L39)

#### `ƒ` `web_fetch_tool(url: str) -> str`    @tool(...)  L50
  - _文档首行_（仅供参考）: Fetch the contents of a web page at a given URL.
  - 分支数 2，函数体节点数 104；return: 'Error: No content found', f'Error: {str(e)}', f'# {title}\n\n{markdown_content[:4096]}'
  - 调用: _get_firecrawl_client, scrape, str, tool

## 文件内调用关系
- `web_search_tool` -> _get_firecrawl_client
- `web_fetch_tool` -> _get_firecrawl_client
