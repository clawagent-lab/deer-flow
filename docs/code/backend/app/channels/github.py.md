# `backend/app/channels/github.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/github.py`  ·  行数: 116

**模块文档首行**（仅供参考）: GitHub channel — webhook-driven IM channel for PR/issue comments.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `typing` -> Any
- `app.channels.base` -> Channel
- `app.channels.message_bus` -> MessageBus, OutboundMessage

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `GitHubChannel`  L42
- 继承: Channel
- _文档首行_: Webhook-driven GitHub channel.
- 方法:
  #### `m` `__init__(self, bus: MessageBus, config: dict[str, Any]) -> None`  L57
    - 分支数 0，函数体节点数 33
    - 调用: __init__, super
  #### `⏵m` `async start(self) -> None`  L62
    - _文档首行_（仅供参考）: Register the outbound callback.
    - 分支数 1，函数体节点数 37；return: None
    - 调用: subscribe_outbound, info
  #### `⏵m` `async stop(self) -> None`  L75
    - _文档首行_（仅供参考）: Unregister the outbound callback.
    - 分支数 1，函数体节点数 39；return: None
    - 调用: unsubscribe_outbound, info
  #### `⏵m` `async send(self, msg: OutboundMessage) -> None`  L85
    - _文档首行_（仅供参考）: Log the agent's final message — do NOT post it to GitHub.
    - 分支数 2，函数体节点数 112
    - 调用: isinstance, get, info, len, debug

## 文件内调用关系
- `GitHubChannel.__init__` -> __init__
