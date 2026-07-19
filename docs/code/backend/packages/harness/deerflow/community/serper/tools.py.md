# `backend/packages/harness/deerflow/community/serper/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/serper/tools.py`  ·  行数: 324

**模块文档首行**（仅供参考）: Web and image search tools powered by Serper (Google Search API).

## 模块概览
- 函数 12 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: json, logging, os, httpx
- `ipaddress` -> IPv4Address, ip_address
- `urllib.parse` -> urlparse
- `langchain.tools` -> tool
- `deerflow.config` -> get_app_config

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SERPER_SEARCH_ENDPOINT` = 'https://google.serper.dev/search'
- `_SERPER_IMAGES_ENDPOINT` = 'https://google.serper.dev/images'
- `_SERPER_MAX_RESULTS` = 10
- `_api_key_warned` = set()

## 函数
#### `ƒ` `_get_api_key(tool_name: str) -> str | None`  L27
  - 分支数 3，函数体节点数 91；return: api_key.strip(), env_key.strip(), None
  - 调用: get_tool_config, get_app_config, get, isinstance, strip, getenv
  - 环境变量: getenv (L33)

#### `ƒ` `_coerce_max_results(value: object, default: int, max_allowed: int) -> int`  L39
  - _文档首行_（仅供参考）: Coerce config/parameter input into a bounded positive result count.
  - 分支数 2，函数体节点数 54；return: default, min(count, max_allowed)
  - 调用: int, min

#### `ƒ` `_missing_key_error(query: str, tool_name: str) -> str`  L50
  - 分支数 1，函数体节点数 48；return: json.dumps({'error': 'SERPER_API_KEY is not configured', 'query': query}, ensure_ascii=False)
  - 调用: add, warning, dumps

#### `ƒ` `_unexpected_format_error(query: str) -> str`  L60
  - 分支数 0，函数体节点数 21；return: json.dumps({'error': 'Serper returned an unexpected response format', 'query': query}, ensure_ascii=False)
  - 调用: dumps

#### `ƒ` `_response_items(data: dict, field: str, query: str) -> tuple[list[dict] | None, str | None]`  L67
  - 分支数 2，函数体节点数 107；return: ([], None), (None, _unexpected_format_error(query)), ([item for item in items if isinstance(item, dict)], None)
  - 调用: get, isinstance, error, type, _unexpected_format_error

#### `ƒ` `_clean_query(query: str) -> str`  L79
  - _文档首行_（仅供参考）: Normalize a raw query into the value actually sent to Serper.
  - 分支数 1，函数体节点数 38；return: query
  - 调用: strip, len

#### `ƒ` `_decode_ipv4(host: str) -> IPv4Address | None`  L87
  - _文档首行_（仅供参考）: Decode obfuscated IPv4 literals that ``ip_address`` rejects.
  - 分支数 10，函数体节点数 238；return: None, ip_address(result)
  - 调用: split, len, startswith, append, int, ip_address

#### `ƒ` `_is_url_present(value: object) -> bool`  L129
  - _文档首行_（仅供参考）: Return ``True`` when *value* is a non-empty URL string.
  - 分支数 0，函数体节点数 27；return: isinstance(value, str) and bool(value.strip())
  - 调用: isinstance, bool, strip

#### `ƒ` `_safe_public_url(value: object) -> str`  L139
  - _文档首行_（仅供参考）: Return ``value`` only if it is a safe, public http(s) URL, else "".
  - 分支数 6，函数体节点数 138；return: '', url, url if ip.is_global else ''
  - 调用: isinstance, strip, urlparse, rstrip, lower, endswith, ip_address, _decode_ipv4

#### `ƒ` `_serper_post(endpoint: str, api_key: str, query: str, max_results: int) -> tuple[dict | None, str | None]`  L174
  - _文档首行_（仅供参考）: Send a POST request to a Serper endpoint.
  - 分支数 3，函数体节点数 244；return: (None, _unexpected_format_error(query)), (data, None), (None, json.dumps({'error': f'Serper API error: HTTP {e.response.status_code}', 'query': query}, ensure_ascii=False)), (None, json.dumps({'error': str(e)[:500], 'query': query}, ensure_ascii=False))
  - 调用: Client, post, raise_for_status, json, isinstance, error, type, _unexpected_format_error, dumps, str
  - 网络调用: post (L191)

#### `ƒ` `web_search_tool(query: str, max_results: int) -> str`    @tool(...)  L211
  - _文档首行_（仅供参考）: Search the web for information using Google Search via Serper.
  - 分支数 5，函数体节点数 229；return: _missing_key_error(query, 'web_search'), error_json, json.dumps({'error': 'No results found', 'query': query}, ensure_ascii=False), json.dumps(output, indent=2, ensure_ascii=False)
  - 调用: get_tool_config, get_app_config, get, _coerce_max_results, _clean_query, _get_api_key, _missing_key_error, _serper_post, _response_items, dumps, len, tool

#### `ƒ` `image_search_tool(query: str, max_results: int) -> str`    @tool(...)  L259
  - _文档首行_（仅供参考）: Search for images online using Google Images via Serper. Use this tool BEFORE image generation to find reference images 
  - 分支数 9，函数体节点数 335；return: _missing_key_error(query, 'image_search'), error_json, json.dumps({'error': 'No images found', 'query': query}, ensure_ascii=False), json.dumps({'error': 'No safe image URLs found', 'query': query}, ensure_ascii=False), json.dumps(output, indent=2, ensure_ascii=False)
  - 调用: get_tool_config, get_app_config, get, _coerce_max_results, _clean_query, _get_api_key, _missing_key_error, _serper_post, _response_items, dumps, _safe_public_url, _is_url_present, append, len, tool

## 文件内调用关系
- `_response_items` -> _unexpected_format_error
- `_safe_public_url` -> _decode_ipv4
- `_serper_post` -> _unexpected_format_error
- `web_search_tool` -> _coerce_max_results, _clean_query, _get_api_key, _missing_key_error, _serper_post, _response_items
- `image_search_tool` -> _coerce_max_results, _clean_query, _get_api_key, _missing_key_error, _serper_post, _response_items, _safe_public_url, _is_url_present
