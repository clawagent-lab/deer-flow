# `backend/packages/harness/deerflow/community/jina_ai/jina_client.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/jina_ai/jina_client.py`  ·  行数: 47

## 模块概览
- 函数 0 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: logging, os, httpx

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_api_key_warned` = False

## 类
### 类 `JinaClient`  L11
- 方法:
  #### `⏵m` `async crawl(self, url: str, return_format: str, timeout: int, proxy: str | None, trust_env: bool) -> str`  L12
    - 分支数 7，函数体节点数 261；return: f'Error: {error_message}', response.text
    - 调用: str, getenv, warning, AsyncClient, post, error, strip, type
  - 网络调用: post (L30)
  - 环境变量: getenv (L19), getenv (L20)

## 文件内调用关系
_无文件内调用_
