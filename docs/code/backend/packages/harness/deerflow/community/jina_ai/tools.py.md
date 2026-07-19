# `backend/packages/harness/deerflow/community/jina_ai/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/jina_ai/tools.py`  ·  行数: 69

## 模块概览
- 函数 4 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio
- `langchain.tools` -> tool
- `deerflow.community.jina_ai.jina_client` -> JinaClient
- `deerflow.config` -> get_app_config
- `deerflow.utils.readability` -> ReadabilityExtractor

## 模块级常量
- `readability_extractor` = ReadabilityExtractor()

## 函数
#### `ƒ` `_coerce_bool(value: object, default: bool) -> bool`  L12
  - 分支数 4，函数体节点数 67；return: value, True, False, default
  - 调用: isinstance, lower, strip

#### `ƒ` `_coerce_timeout(value: object, default: int) -> int`  L24
  - 分支数 4，函数体节点数 56；return: default, value, int(value)
  - 调用: isinstance, int

#### `ƒ` `_coerce_proxy(value: object) -> str | None`  L37
  - 分支数 1，函数体节点数 36；return: None, proxy or None
  - 调用: isinstance, strip

#### `⏵ƒ` `async web_fetch_tool(url: str) -> str`    @tool(...)  L45
  - _文档首行_（仅供参考）: Fetch the contents of a web page at a given URL.
  - 分支数 2，函数体节点数 161；return: html_content, article.to_markdown()[:4096]
  - 调用: JinaClient, get_tool_config, get_app_config, _coerce_timeout, get, _coerce_proxy, _coerce_bool, crawl, isinstance, startswith, to_thread, to_markdown, tool

## 文件内调用关系
- `web_fetch_tool` -> _coerce_timeout, _coerce_proxy, _coerce_bool
