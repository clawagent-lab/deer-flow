# `backend/packages/harness/deerflow/community/crawl4ai/crawl4ai_client.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/crawl4ai/crawl4ai_client.py`  ·  行数: 64

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: json, logging, httpx
- `typing` -> Any

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `Crawl4AiClient`  L10
- _文档首行_: Client for a self-hosted Crawl4AI Docker server (POST /md).
- 方法:
  #### `m` `__init__(self, base_url: str, token: str, timeout_s: float) -> None`  L13
    - 分支数 0，函数体节点数 40
    - 调用: rstrip
  #### `⏵m` `async fetch_markdown(self, url: str, filter_mode: str) -> str`  L18
    - _文档首行_（仅供参考）: Fetch a page's clean markdown via Crawl4AI's POST /md endpoint.
    - 分支数 7，函数体节点数 275；return: f'Error: Crawl4AI HTTP {resp.status_code}: {resp.text[:200]}', f'Error: Crawl4AI returned a non-JSON 200 response (content-type: {content_type}): {resp.text[:200]}', f'Error: Crawl4AI reported failure for {url}', 'Error: Crawl4AI returned empty markdown', markdown, f'Error: Crawl4AI request timed out after {self.timeout_s}s', f'Error: Crawl4AI request failed: {e!s}', f'Error: Crawl4AI fetch failed: {e!s}'
    - 调用: debug, AsyncClient, post, json, get, strip, error
  - 网络调用: post (L36)

## 文件内调用关系
_无文件内调用_
