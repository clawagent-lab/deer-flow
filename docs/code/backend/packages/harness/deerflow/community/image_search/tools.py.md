# `backend/packages/harness/deerflow/community/image_search/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/image_search/tools.py`  ·  行数: 136

**模块文档首行**（仅供参考）: Image Search Tool - Search images using DuckDuckGo for reference in image generation.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: json, logging
- `langchain.tools` -> tool
- `deerflow.config` -> get_app_config

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_search_images(query: str, max_results: int, region: str, safesearch: str, size: str | None, color: str | None, type_image: str | None, layout: str | None, license_image: str | None) -> list[dict]`  L15
  - _文档首行_（仅供参考）: Execute image search using DuckDuckGo.
  - 分支数 7，函数体节点数 194；return: [], list(results) if results else []
  - 调用: error, DDGS, images, list

#### `ƒ` `image_search_tool(query: str, max_results: int, size: str | None, type_image: str | None, layout: str | None) -> str`    @tool(...)  L78
  - _文档首行_（仅供参考）: Search for images online. Use this tool BEFORE image generation to find reference images for characters, portraits, obje
  - 分支数 2，函数体节点数 182；return: json.dumps({'error': 'No images found', 'query': query}, ensure_ascii=False), json.dumps(output, indent=2, ensure_ascii=False)
  - 调用: get_tool_config, get_app_config, get, _search_images, dumps, len, tool

## 文件内调用关系
- `image_search_tool` -> _search_images
