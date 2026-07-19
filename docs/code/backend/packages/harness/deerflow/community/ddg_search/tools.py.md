# `backend/packages/harness/deerflow/community/ddg_search/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/ddg_search/tools.py`  ·  行数: 183

**模块文档首行**（仅供参考）: Web Search Tool - Search the web using DuckDuckGo (no API key required).

## 模块概览
- 函数 8 个，类 0 个，模块级常量 7 个

## 依赖（import）
- 模块: json, logging
- `langchain.tools` -> tool
- `deerflow.config` -> get_app_config

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `DEFAULT_BACKEND` = 'auto'
- `DEFAULT_REGION` = 'wt-wt'
- `DEFAULT_SAFESEARCH` = 'moderate'
- `DEFAULT_WIKIPEDIA_REGION` = 'us-en'
- `WIKIPEDIA_BACKENDS` = {'auto', 'all', 'wikipedia'}
- `WIKIPEDIA_LANGUAGE_ALIASES` = {'jp': 'ja', 'kr': 'ko', 'tzh': 'zh', 'wt': 'en'}

## 函数
#### `ƒ` `_normalize_backend(backend: str | list[str] | tuple[str, ...] | None) -> str`  L28
  - 分支数 2，函数体节点数 94；return: DEFAULT_BACKEND, ','.join((str(part).strip() for part in backend if str(part).strip())) or DEFAULT_BACKEND, str(backend).strip() or DEFAULT_BACKEND
  - 调用: isinstance, join, strip, str

#### `ƒ` `_normalize_setting(value: str | None, default: str) -> str`  L36
  - 分支数 0，函数体节点数 27；return: str(value).strip() if value else default
  - 调用: strip, str

#### `ƒ` `_backend_includes_wikipedia(backend: str | list[str] | tuple[str, ...] | None) -> bool`  L40
  - 分支数 0，函数体节点数 63；return: any((part.strip().lower() in WIKIPEDIA_BACKENDS for part in backend.split(',')))
  - 调用: _normalize_backend, any, lower, strip, split

#### `ƒ` `_contains_codepoint(query: str, ranges: tuple[tuple[int, int], ...]) -> bool`  L45
  - 分支数 0，函数体节点数 56；return: any((start <= ord(char) <= end for char in query for start, end in ranges))
  - 调用: any, ord

#### `ƒ` `_infer_wikipedia_region(query: str) -> str`  L49
  - _文档首行_（仅供参考）: Pick a valid Wikipedia language region when DDGS' worldwide region is used.
  - 分支数 7，函数体节点数 122；return: 'jp-ja', 'kr-ko', 'cn-zh', 'ru-ru', 'gr-el', 'il-he', 'xa-ar', DEFAULT_WIKIPEDIA_REGION
  - 调用: _contains_codepoint

#### `ƒ` `_resolve_ddgs_region(query: str, region: str | None, backend: str | list[str] | tuple[str, ...] | None) -> str`  L68
  - _文档首行_（仅供参考）: DDGS' wikipedia engine treats the second part of region as a Wikipedia
  - 分支数 3，函数体节点数 116；return: normalized_region, _infer_wikipedia_region(query), DEFAULT_WIKIPEDIA_REGION, f'{country}-{WIKIPEDIA_LANGUAGE_ALIASES.get(language, language)}'
  - 调用: lower, _normalize_setting, _backend_includes_wikipedia, _infer_wikipedia_region, split, get

#### `ƒ` `_search_text(query: str, max_results: int, region: str | None, safesearch: str | None, backend: str | list[str] | tuple[str, ...] | None) -> list[dict]`  L87
  - _文档首行_（仅供参考）: Execute text search using DuckDuckGo.
  - 分支数 2，函数体节点数 165；return: [], list(results) if results else []
  - 调用: error, DDGS, _normalize_backend, _normalize_setting, _resolve_ddgs_region, text, list

#### `ƒ` `web_search_tool(query: str, max_results: int) -> str`    @tool(...)  L134
  - _文档首行_（仅供参考）: Search the web for information. Use this tool to find current information, news, articles, and facts from the internet.
  - 分支数 2，函数体节点数 216；return: json.dumps({'error': 'No results found', 'query': query}, ensure_ascii=False), json.dumps(output, indent=2, ensure_ascii=False)
  - 调用: get_tool_config, get_app_config, get, _search_text, dumps, len, tool

## 文件内调用关系
- `_backend_includes_wikipedia` -> _normalize_backend
- `_infer_wikipedia_region` -> _contains_codepoint
- `_resolve_ddgs_region` -> _normalize_setting, _backend_includes_wikipedia, _infer_wikipedia_region
- `_search_text` -> _normalize_backend, _normalize_setting, _resolve_ddgs_region
- `web_search_tool` -> _search_text
