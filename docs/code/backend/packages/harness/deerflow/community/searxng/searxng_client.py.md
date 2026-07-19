# `backend/packages/harness/deerflow/community/searxng/searxng_client.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/searxng/searxng_client.py`  ·  行数: 66

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: logging, httpx
- `typing` -> Any

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `SearxngClient`  L9
- _文档首行_: Client for SearXNG meta search engine API.
- 方法:
  #### `m` `__init__(self, base_url: str) -> None`  L12
    - 分支数 0，函数体节点数 18
    - 调用: rstrip
  #### `⏵m` `async search(self, query: str, max_results: int, categories: list[str] | None) -> list[dict[str, Any]]`  L15
    - _文档首行_（仅供参考）: Search the web using SearXNG.
    - 分支数 4，函数体节点数 227；raise: bare raise；return: results[:max_results] if max_results else results
    - 调用: join, debug, AsyncClient, get, raise_for_status, json, error
  - 网络调用: get (L45)

## 文件内调用关系
_无文件内调用_
