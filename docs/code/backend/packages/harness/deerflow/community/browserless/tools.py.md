# `backend/packages/harness/deerflow/community/browserless/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/browserless/tools.py`  ·  行数: 325

## 模块概览
- 函数 16 个，类 0 个，模块级常量 6 个

## 依赖（import）
- 模块: asyncio, logging, os, re
- `datetime` -> UTC, datetime
- `pathlib` -> Path
- `typing` -> Annotated
- `urllib.parse` -> urlparse
- `langchain.tools` -> InjectedToolCallId, tool
- `langchain_core.messages` -> ToolMessage
- `langgraph.types` -> Command
- `deerflow.community.url_safety` -> _resolve_host_addresses
- `deerflow.community.url_safety` -> validate_public_http_url
- `deerflow.config` -> get_app_config
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX
- `deerflow.tools.types` -> Runtime
- `deerflow.utils.readability` -> ReadabilityExtractor
- `.browserless_client` -> BrowserlessClient, BrowserlessScreenshotResult

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_readability_extractor` = ReadabilityExtractor()
- `_OUTPUTS_VIRTUAL_PREFIX` = f'{VIRTUAL_PATH_PREFIX}/outputs'
- `_OUTPUT_FORMAT_TO_EXTENSION` = {'png': 'png', 'jpeg': 'jpeg', 'webp': 'webp'}
- `_SAFE_FILENAME_RE` = re.compile('[^A-Za-z0-9._-]+')
- `_MAX_FILENAME_COLLISION_PROBES` = 1000

## 函数
#### `ƒ` `_get_tool_config(tool_name: str) -> dict | None`  L38
  - _文档首行_（仅供参考）: Get tool config extras safely, returning None if not configured.
  - 分支数 1，函数体节点数 48；return: None, extras if extras is not None else {}
  - 调用: get_tool_config, get_app_config

#### `ƒ` `_get_browserless_client(tool_name: str) -> BrowserlessClient`  L47
  - 分支数 1，函数体节点数 106；return: BrowserlessClient(base_url=base_url, token=token, timeout_s=timeout_s)
  - 调用: _get_tool_config, getenv, get, isinstance, float, BrowserlessClient
  - 环境变量: getenv (L50)

#### `ƒ` `_as_bool(value: object, default: bool) -> bool`  L60
  - 分支数 4，函数体节点数 67；return: value, True, False, default
  - 调用: isinstance, lower, strip

#### `ƒ` `_as_int(value: object, default: int) -> int`  L72
  - 分支数 3，函数体节点数 59；return: value, int(value.strip()), default
  - 调用: isinstance, int, strip

#### `ƒ` `_as_optional_quality(value: object, output_format: str) -> int | None`  L83
  - 分支数 1，函数体节点数 46；return: None, quality if 0 <= quality <= 100 else None
  - 调用: _as_int

#### `ƒ` `_normalize_output_format(value: object) -> str`  L90
  - 分支数 0，函数体节点数 35；return: output_format if output_format in _OUTPUT_FORMAT_TO_EXTENSION else 'png'
  - 调用: lower, strip, str

#### `ƒ` `_validate_capture_url(url: str, allow_private_addresses: bool) -> str | None`  L95
  - _文档首行_（仅供参考）: Validate a capture URL for scheme and (unless opted out) SSRF safety.
  - 分支数 0，函数体节点数 30；return: validate_public_http_url(url, allow_private_addresses=allow_private_addresses, action='capture', resolver=_resolve_host_addresses)
  - 调用: validate_public_http_url

#### `ƒ` `_default_capture_stem(url: str) -> str`  L111
  - 分支数 0，函数体节点数 61；return: raw[:80]
  - 调用: urlparse, split, join

#### `ƒ` `_safe_capture_filename(filename: str | None, url: str, output_format: str) -> str`  L118
  - 分支数 1，函数体节点数 110；return: f'{safe_stem[:100]}.{extension}'
  - 调用: Path, strftime, now, _default_capture_stem, strip, sub

#### `ƒ` `_thread_outputs_path(runtime: Runtime) -> Path | str`  L131
  - 分支数 2，函数体节点数 57；return: 'Error: Thread runtime state is not available', 'Error: Thread outputs path is not available', Path(outputs_path)
  - 调用: get, Path

#### `ƒ` `_tool_message(content: str, tool_call_id: str) -> Command`  L141
  - 分支数 0，函数体节点数 27；return: Command(update={'messages': [ToolMessage(content, tool_call_id=tool_call_id)]})
  - 调用: Command, ToolMessage

#### `ƒ` `_dedupe_output_name(outputs_path: Path, output_name: str) -> str`  L145
  - _文档首行_（仅供参考）: Return a non-colliding filename under ``outputs_path``.
  - 分支数 3，函数体节点数 119；return: output_name, probe, f'{stem}-{timestamp}{suffix}'
  - 调用: exists, Path, range, strftime, now
  - 文件IO: exists (L154), exists (L161)

#### `ƒ` `_write_capture_output(outputs_path: Path, output_name: str, content: bytes) -> str`  L168
  - _文档首行_（仅供参考）: Write ``content`` into ``outputs_path`` and return the actual filename used.
  - 分支数 0，函数体节点数 50；return: final_name
  - 调用: mkdir, _dedupe_output_name, write_bytes
  - 文件IO: mkdir (L170), write_bytes (L172)

#### `ƒ` `_target_status_warning(result: BrowserlessScreenshotResult) -> str`  L176
  - _文档首行_（仅供参考）: Return a human-readable warning when the captured page itself errored.
  - 分支数 1，函数体节点数 68；return: '', f' (warning: target page responded {detail})'
  - 调用: strip, startswith

#### `⏵ƒ` `async web_fetch_tool(url: str) -> str`    @tool(...)  L193
  - _文档首行_（仅供参考）: Fetch the contents of a web page at a given URL using Browserless (headless Chrome).
  - 分支数 3，函数体节点数 249；return: url_error, html, article.to_markdown()[:4096], f'Error: {str(e)}'
  - 调用: _get_tool_config, _as_bool, get, validate_public_http_url, isinstance, int, _get_browserless_client, fetch_html, startswith, to_thread, to_markdown, error, str, tool

#### `⏵ƒ` `async web_capture_tool(runtime: Runtime, url: str, tool_call_id: Annotated[str, InjectedToolCallId], filename: str | None, full_page: bool | None, output_format: str | None, viewport_width: int | None, viewport_height: int | None) -> Command`    @tool(...)  L249
  - _文档首行_（仅供参考）: Capture a rendered webpage screenshot and present it as an artifact.
  - 分支数 4，函数体节点数 452；return: _tool_message(url_error, tool_call_id), _tool_message(outputs_path, tool_call_id), _tool_message(result, tool_call_id), Command(update={'artifacts': [virtual_path], 'messages': [ToolMessage(message, tool_call_id=tool_call_id)]}), _tool_message(f'Error: {str(e)}', tool_call_id)
  - 调用: _get_tool_config, _as_bool, get, _validate_capture_url, _tool_message, _thread_outputs_path, isinstance, _normalize_output_format, _as_int, _as_optional_quality, str, _safe_capture_filename, _get_browserless_client, capture_screenshot, to_thread, _target_status_warning, Command, ToolMessage, error, tool

## 文件内调用关系
- `_get_browserless_client` -> _get_tool_config
- `_as_optional_quality` -> _as_int
- `_safe_capture_filename` -> _default_capture_stem
- `_write_capture_output` -> _dedupe_output_name
- `web_fetch_tool` -> _get_tool_config, _as_bool, _get_browserless_client
- `web_capture_tool` -> _get_tool_config, _as_bool, _validate_capture_url, _tool_message, _thread_outputs_path, _normalize_output_format, _as_int, _as_optional_quality, _safe_capture_filename, _get_browserless_client, _target_status_warning
