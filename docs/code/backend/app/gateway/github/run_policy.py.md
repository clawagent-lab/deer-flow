# `backend/app/gateway/github/run_policy.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/github/run_policy.py`  ·  行数: 140

**模块文档首行**（仅供参考）: Per-run policy hooks for the GitHub channel.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `typing` -> TYPE_CHECKING, Any

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `⏵ƒ` `async inject_github_credentials(msg: InboundMessage, run_context: dict[str, Any]) -> None`  L25
  - _文档首行_（仅供参考）: Install a GitHub App installation token in ``run_context``.
  - 分支数 3，函数体节点数 121；return: None
  - 调用: isinstance, get, mint_installation_token, info

#### `ƒ` `register_policy() -> None`  L91
  - _文档首行_（仅供参考）: Register the GitHub channel's :class:`ChannelRunPolicy` entry.
  - 分支数 0，函数体节点数 28
  - 调用: ChannelRunPolicy

## 文件内调用关系
_无文件内调用_
