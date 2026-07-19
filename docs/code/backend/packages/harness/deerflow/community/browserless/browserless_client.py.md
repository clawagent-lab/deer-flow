# `backend/packages/harness/deerflow/community/browserless/browserless_client.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/browserless/browserless_client.py`  ·  行数: 212

## 模块概览
- 函数 1 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: logging, httpx
- `dataclasses` -> dataclass
- `typing` -> Any

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_get_header(headers: Any, name: str) -> str`  L19
  - 分支数 1，函数体节点数 44；return: str(value), str(headers.get(name.lower(), ''))
  - 调用: get, str, lower

## 类
### 类 `BrowserlessScreenshotResult`  L11  @dataclass(...)
- 类/实例变量:
  - `content` = <annotated>
  - `content_type` = <annotated>
  - `target_status_code` = <annotated>
  - `target_status` = <annotated>
  - `final_url` = <annotated>

### 类 `BrowserlessClient`  L26
- _文档首行_: Client for Browserless headless Chrome API.
- 方法:
  #### `m` `__init__(self, base_url: str, token: str, timeout_s: float) -> None`  L29
    - 分支数 0，函数体节点数 40
    - 调用: rstrip
  #### `⏵m` `async fetch_html(self, url: str, wait_for_event: str, wait_for_timeout_ms: int, wait_for_selector: str, wait_for_selector_timeout_ms: int, reject_resource_types: list[str] | None, reject_request_pattern: list[str] | None) -> str`  L34
    - _文档首行_（仅供参考）: Fetch the rendered HTML of a page using Browserless.
    - 分支数 10，函数体节点数 348；return: f'Error: Browserless HTTP {code}: {resp.text[:200]}', 'Error: Browserless returned empty response', html, f'Error: Browserless request timed out after {self.timeout_s}s', f'Error: Browserless request failed: {e!s}', f'Error: Browserless fetch failed: {e!s}'
    - 调用: debug, AsyncClient, post, get, strip, error
  - 网络调用: post (L84)
  #### `⏵m` `async capture_screenshot(self, url: str, full_page: bool, output_format: str, quality: int | None, viewport: dict[str, int] | None, wait_for_selector: str, wait_for_selector_timeout_ms: int, wait_for_timeout_ms: int, best_attempt: bool) -> BrowserlessScreenshotResult | str`  L117
    - _文档首行_（仅供参考）: Capture a rendered screenshot of a URL using Browserless.
    - 分支数 9，函数体节点数 391；return: f'Error: Browserless HTTP {code}: {resp.text[:200]}', 'Error: Browserless returned empty screenshot response', BrowserlessScreenshotResult(content=content, content_type=_get_header(resp.headers, 'Content-Type'), target_status_code=_get_header(resp.headers, 'X-Response-Code'), target_status=_get_header(resp.headers, 'X-Response-Status'), final_url=_get_header(resp.headers, 'X-Response-URL')), f'Error: Browserless screenshot request timed out after {self.timeout_s}s', f'Error: Browserless screenshot request failed: {e!s}', f'Error: Browserless screenshot failed: {e!s}'
    - 调用: debug, AsyncClient, post, get, BrowserlessScreenshotResult, _get_header, error
  - 网络调用: post (L171)

## 文件内调用关系
- `BrowserlessClient.capture_screenshot` -> _get_header
