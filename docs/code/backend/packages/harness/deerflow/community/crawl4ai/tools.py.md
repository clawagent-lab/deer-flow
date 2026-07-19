# `backend/packages/harness/deerflow/community/crawl4ai/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/crawl4ai/tools.py`  ·  行数: 118

## 模块概览
- 函数 6 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: logging
- `langchain.tools` -> tool
- `deerflow.community.url_safety` -> validate_public_http_url
- `deerflow.config` -> get_app_config
- `.crawl4ai_client` -> Crawl4AiClient

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `DEFAULT_BASE_URL` = 'http://localhost:11235'
- `DEFAULT_TIMEOUT_S` = 30
- `DEFAULT_FILTER` = 'fit'
- `VALID_FILTERS` = ('fit', 'raw', 'bm25', 'llm')

## 函数
#### `ƒ` `_get_tool_config(tool_name: str) -> dict | None`  L18
  - _文档首行_（仅供参考）: Return the tool's config extras (model_extra) dict, or None if unconfigured.
  - 分支数 1，函数体节点数 48；return: None, extras if extras is not None else {}
  - 调用: get_tool_config, get_app_config

#### `ƒ` `_coerce_timeout(value: object, default: int) -> float`  L27
  - _文档首行_（仅供参考）: Coerce a config timeout into seconds, falling back to ``default`` on bad input.
  - 分支数 4，函数体节点数 79；return: float(default), float(value)
  - 调用: isinstance, float, warning

#### `ƒ` `_coerce_bool(value: object, default: bool) -> bool`  L46
  - 分支数 4，函数体节点数 67；return: value, True, False, default
  - 调用: isinstance, lower, strip

#### `ƒ` `_coerce_filter(value: object) -> str`  L58
  - _文档首行_（仅供参考）: Normalize and validate the markdown filter, falling back to the default.
  - 分支数 2，函数体节点数 58；return: normalized, DEFAULT_FILTER
  - 调用: isinstance, lower, strip, warning, join

#### `ƒ` `_build_client(cfg: dict | None) -> Crawl4AiClient`  L72
  - _文档首行_（仅供参考）: Build a ``Crawl4AiClient`` from an already-read ``web_fetch`` config dict.
  - 分支数 1，函数体节点数 86；return: Crawl4AiClient(base_url=base_url, token=token, timeout_s=timeout_s)
  - 调用: float, get, _coerce_timeout, Crawl4AiClient

#### `⏵ƒ` `async web_fetch_tool(url: str) -> str`    @tool(...)  L90
  - _文档首行_（仅供参考）: Fetch the contents of a web page at a given URL.
  - 分支数 3，函数体节点数 141；return: url_error, markdown, markdown[:4096], f'Error: {str(e)}'
  - 调用: _get_tool_config, _coerce_bool, get, validate_public_http_url, _coerce_filter, _build_client, fetch_markdown, startswith, error, str, tool

## 文件内调用关系
- `_build_client` -> _coerce_timeout
- `web_fetch_tool` -> _get_tool_config, _coerce_bool, _coerce_filter, _build_client
