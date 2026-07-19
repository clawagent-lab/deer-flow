# `backend/packages/harness/deerflow/community/tavily/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/tavily/tools.py`  ·  行数: 63

## 模块概览
- 函数 3 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: json
- `langchain.tools` -> tool
- `tavily` -> TavilyClient
- `deerflow.config` -> get_app_config

## 函数
#### `ƒ` `_get_tavily_client() -> TavilyClient`  L9
  - 分支数 1，函数体节点数 51；return: TavilyClient(api_key=api_key)
  - 调用: get_tool_config, get_app_config, get, TavilyClient

#### `ƒ` `web_search_tool(query: str) -> str`    @tool(...)  L18
  - _文档首行_（仅供参考）: Search the web.
  - 分支数 1，函数体节点数 122；return: json_results
  - 调用: get_tool_config, get_app_config, get, _get_tavily_client, search, dumps, tool

#### `ƒ` `web_fetch_tool(url: str) -> str`    @tool(...)  L44
  - _文档首行_（仅供参考）: Fetch the contents of a web page at a given URL.
  - 分支数 2，函数体节点数 119；return: f"Error: {res['failed_results'][0]['error']}", f"# {result['title']}\n\n{result['raw_content'][:4096]}", 'Error: No results found'
  - 调用: _get_tavily_client, extract, len, tool

## 文件内调用关系
- `web_search_tool` -> _get_tavily_client
- `web_fetch_tool` -> _get_tavily_client
