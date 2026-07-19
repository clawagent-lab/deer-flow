# `backend/packages/harness/deerflow/community/brave/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/brave/tools.py`  ·  行数: 383

**模块文档首行**（仅供参考）: Web and image search tools powered by the Brave Search API.

## 模块概览
- 函数 12 个，类 0 个，模块级常量 8 个

## 依赖（import）
- 模块: json, logging, os, httpx
- `ipaddress` -> IPv4Address, IPv6Address, ip_address, ip_network
- `urllib.parse` -> urlparse
- `langchain.tools` -> tool
- `deerflow.config` -> get_app_config

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_BRAVE_WEB_ENDPOINT` = 'https://api.search.brave.com/res/v1/web/search'
- `_BRAVE_IMAGES_ENDPOINT` = 'https://api.search.brave.com/res/v1/images/search'
- `_DEFAULT_MAX_RESULTS` = 5
- `_BRAVE_WEB_MAX_COUNT` = 20
- `_BRAVE_IMAGE_MAX_COUNT` = 200
- `_NAT64_PREFIX` = ip_network('64:ff9b::/96')
- `_api_key_warned` = set()

## 函数
#### `ƒ` `_get_api_key(tool_name: str) -> str | None`  L38
  - 分支数 3，函数体节点数 95；return: api_key.strip(), env_key.strip(), None
  - 调用: get_tool_config, get_app_config, get, isinstance, strip, getenv
  - 环境变量: getenv (L44)

#### `ƒ` `_coerce_max_results(value: object, *, default: int, max_allowed: int) -> int`  L50
  - 分支数 1，函数体节点数 61；return: max(1, min(coerced, max_allowed))
  - 调用: int, warning, max, min

#### `ƒ` `_clean_query(query: str, *, max_length: int) -> str`  L69
  - 分支数 1，函数体节点数 42；return: query
  - 调用: strip, len

#### `ƒ` `_missing_key_error(query: str, tool_name: str) -> str`  L76
  - 分支数 1，函数体节点数 48；return: json.dumps({'error': 'BRAVE_SEARCH_API_KEY is not configured', 'query': query}, ensure_ascii=False)
  - 调用: add, warning, dumps

#### `ƒ` `_unexpected_format_error(query: str, *, service_name: str) -> str`  L89
  - 分支数 0，函数体节点数 29；return: json.dumps({'error': f'{service_name} returned an unexpected response format', 'query': query}, ensure_ascii=False)
  - 调用: dumps

#### `ƒ` `_decode_ipv4(host: str) -> IPv4Address | None`  L96
  - _文档首行_（仅供参考）: Decode obfuscated IPv4 literals that ``ip_address`` rejects.
  - 分支数 10，函数体节点数 238；return: None, IPv4Address(result)
  - 调用: split, len, startswith, append, int, IPv4Address

#### `ƒ` `_is_url_present(value: object) -> bool`  L136
  - 分支数 0，函数体节点数 25；return: isinstance(value, str) and bool(value.strip())
  - 调用: isinstance, bool, strip

#### `ƒ` `_embedded_ipv4(ip: IPv6Address) -> IPv4Address | None`  L140
  - _文档首行_（仅供参考）: Extract an IPv4 address embedded in an IPv6 literal, if any.
  - 分支数 4，函数体节点数 92；return: ip.ipv4_mapped, ip.sixtofour, IPv4Address(int(ip) & 4294967295), IPv4Address(packed & 4294967295), None
  - 调用: IPv4Address, int

#### `ƒ` `_safe_public_url(value: object) -> str`  L161
  - _文档首行_（仅供参考）: Return ``value`` only if it is a safe, public http(s) URL, else "".
  - 分支数 9，函数体节点数 176；return: '', url, url if ip.is_global else ''
  - 调用: isinstance, strip, urlparse, rstrip, lower, endswith, ip_address, _decode_ipv4, _embedded_ipv4

#### `ƒ` `_brave_get(endpoint: str, api_key: str, query: str, params: dict[str, object], *, service_name: str) -> tuple[dict | None, str | None]`  L200
  - 分支数 3，函数体节点数 232；return: (None, _unexpected_format_error(query, service_name=service_name)), (data, None), (None, json.dumps({'error': f'{service_name} API error: HTTP {e.response.status_code}', 'query': query}, ensure_ascii=False)), (None, json.dumps({'error': str(e), 'query': query}, ensure_ascii=False))
  - 调用: Client, get, raise_for_status, json, isinstance, error, type, _unexpected_format_error, dumps, str
  - 网络调用: get (L214)

#### `ƒ` `web_search_tool(query: str, max_results: int) -> str`    @tool(...)  L233
  - _文档首行_（仅供参考）: Search the web for information using Brave Search.
  - 分支数 4，函数体节点数 235；return: _missing_key_error(query, 'web_search'), error_json, json.dumps({'error': 'No results found', 'query': query}, ensure_ascii=False), json.dumps(output, indent=2, ensure_ascii=False)
  - 调用: get_tool_config, get_app_config, _coerce_max_results, _clean_query, _get_api_key, _missing_key_error, _brave_get, get, dumps, len, tool

#### `ƒ` `image_search_tool(query: str, max_results: int) -> str`    @tool(...)  L279
  - _文档首行_（仅供参考）: Search for images online using Brave Image Search. Use this tool BEFORE image generation to find reference images for ch
  - 分支数 17，函数体节点数 587；return: _missing_key_error(query, 'image_search'), error_json, _unexpected_format_error(query, service_name='Brave Image Search'), json.dumps({'error': 'No images found', 'query': query}, ensure_ascii=False), json.dumps({'error': 'No safe image URLs found', 'query': query}, ensure_ascii=False), json.dumps(output, indent=2, ensure_ascii=False)
  - 调用: get_tool_config, get_app_config, _coerce_max_results, _clean_query, _get_api_key, _missing_key_error, _brave_get, get, isinstance, error, type, _unexpected_format_error, dumps, _safe_public_url, _is_url_present, append, len, tool

## 文件内调用关系
- `_safe_public_url` -> _decode_ipv4, _embedded_ipv4
- `_brave_get` -> _unexpected_format_error
- `web_search_tool` -> _coerce_max_results, _clean_query, _get_api_key, _missing_key_error, _brave_get
- `image_search_tool` -> _coerce_max_results, _clean_query, _get_api_key, _missing_key_error, _brave_get, _unexpected_format_error, _safe_public_url, _is_url_present
