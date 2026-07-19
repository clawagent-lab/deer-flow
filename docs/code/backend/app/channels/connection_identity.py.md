# `backend/app/channels/connection_identity.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/connection_identity.py`  ·  行数: 45

**模块文档首行**（仅供参考）: Helpers for attaching persisted channel connection ownership to inbound messages.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any
- `app.channels.message_bus` -> InboundMessage

## 函数
#### `⏵ƒ` `async attach_connection_identity(inbound: InboundMessage, *, repo: Any, provider: str, workspace_id: str | None, fallback_without_workspace: bool) -> InboundMessage`  L10
  - _文档首行_（仅供参考）: Attach connection metadata to an inbound message when a persisted binding exists.
  - 分支数 6，函数体节点数 146；return: inbound
  - 调用: append, find_connection_by_external_identity, get
  - 网络调用: get (L41)

## 文件内调用关系
_无文件内调用_
