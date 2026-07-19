# `backend/packages/harness/deerflow/community/infoquest/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/infoquest/tools.py`  ·  行数: 94

## 模块概览
- 函数 4 个，类 0 个，模块级常量 1 个

## 依赖（import）
- `langchain.tools` -> tool
- `deerflow.config` -> get_app_config
- `deerflow.utils.readability` -> ReadabilityExtractor
- `.infoquest_client` -> InfoQuestClient

## 模块级常量
- `readability_extractor` = ReadabilityExtractor()

## 函数
#### `ƒ` `_get_infoquest_client() -> InfoQuestClient`  L11
  - 分支数 6，函数体节点数 246；return: InfoQuestClient(search_time_range=search_time_range, fetch_timeout=fetch_timeout, fetch_navigation_timeout=navigation_timeout, fetch_time=fetch_time, image_search_time_range=image_search_time_range, image_size=image_size)
  - 调用: get_tool_config, get_app_config, get, InfoQuestClient

#### `ƒ` `web_search_tool(query: str) -> str`    @tool(...)  L47
  - _文档首行_（仅供参考）: Search the web.
  - 分支数 0，函数体节点数 29；return: client.web_search(query)
  - 调用: _get_infoquest_client, web_search, tool

#### `ƒ` `web_fetch_tool(url: str) -> str`    @tool(...)  L59
  - _文档首行_（仅供参考）: Fetch the contents of a web page at a given URL.
  - 分支数 1，函数体节点数 61；return: result, article.to_markdown()[:4096]
  - 调用: _get_infoquest_client, fetch, startswith, extract_article, to_markdown, tool
  - 网络调用: fetch (L70)

#### `ƒ` `image_search_tool(query: str) -> str`    @tool(...)  L78
  - _文档首行_（仅供参考）: Search for images online. Use this tool BEFORE image generation to find reference images for characters, portraits, obje
  - 分支数 0，函数体节点数 29；return: client.image_search(query)
  - 调用: _get_infoquest_client, image_search, tool

## 文件内调用关系
- `web_search_tool` -> _get_infoquest_client
- `web_fetch_tool` -> _get_infoquest_client
- `image_search_tool` -> _get_infoquest_client
