# `backend/packages/harness/deerflow/community/url_safety.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/url_safety.py`  ·  行数: 79

**模块文档首行**（仅供参考）: Shared URL safety checks for server-side web tools.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: ipaddress, socket
- `__future__` -> annotations
- `collections.abc` -> Callable
- `urllib.parse` -> urlparse

## 模块级常量
- `_BLOCKED_HOSTNAMES` = {'localhost', 'metadata.google.internal'}

## 函数
#### `ƒ` `resolve_host_addresses(hostname: str) -> list[ipaddress._BaseAddress]`  L13
  - _文档首行_（仅供参考）: Resolve a hostname to all IP addresses for SSRF screening.
  - 分支数 3，函数体节点数 89；return: addresses
  - 调用: getaddrinfo, append, ip_address

#### `ƒ` `is_blocked_address(address: ipaddress._BaseAddress) -> bool`  L29
  - _文档首行_（仅供参考）: Return True for addresses web tools should not reach by default.
  - 分支数 0，函数体节点数 38；return: address.is_private or address.is_loopback or address.is_link_local or address.is_reserved or address.is_multicast or address.is_unspecified

#### `ƒ` `validate_public_http_url(url: str, *, allow_private_addresses: bool, action: str, resolver: Callable[[str], list[ipaddress._BaseAddress]] | None) -> str | None`  L34
  - _文档首行_（仅供参考）: Validate an http(s) URL before a server-side web tool fetches it.
  - 分支数 8，函数体节点数 198；return: 'Error: Only http:// and https:// URLs are supported', None, 'Error: URL host could not be parsed', f'Error: Refusing to {action} a private or loopback address', 'Error: URL host could not be resolved', f'Error: Refusing to {action} a private, loopback, or metadata address'
  - 调用: urlparse, lower, rstrip, strip, ip_address, resolve, any, is_blocked_address

## 文件内调用关系
- `validate_public_http_url` -> is_blocked_address
