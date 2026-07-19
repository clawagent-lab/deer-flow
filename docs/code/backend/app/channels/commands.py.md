# `backend/app/channels/commands.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/commands.py`  ·  行数: 90

**模块文档首行**（仅供参考）: Shared command definitions used by all channel implementations.

## 模块概览
- 函数 4 个，类 0 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations

## 模块级常量
- `KNOWN_CHANNEL_COMMANDS` = frozenset({'/bootstrap', '/goal', '/new', '/status', '/mo...

## 函数
#### `ƒ` `_is_leading_mention_token(token: str) -> bool`  L24
  - _文档首行_（仅供参考）: Return whether *token* looks like a platform bot/user mention.
  - 分支数 3，函数体节点数 54；return: False, True
  - 调用: startswith, endswith, len

#### `ƒ` `strip_leading_mentions(text: str) -> str`  L44
  - _文档首行_（仅供参考）: Drop leading platform mention tokens (``@bot``, ``<@id>``) so a group-chat
  - 分支数 2，函数体节点数 73；return: remainder
  - 调用: split, isspace, _is_leading_mention_token, len

#### `ƒ` `extract_connect_code(text: str) -> str | None`  L66
  - _文档首行_（仅供参考）: Extract the one-time channel binding code from a connect command.
  - 分支数 3，函数体节点数 98；return: None, parts[index + 1]
  - 调用: split, strip, len, _is_leading_mention_token, lower

#### `ƒ` `is_known_channel_command(text: str) -> bool`  L85
  - _文档首行_（仅供参考）: Return whether text starts with a registered channel control command.
  - 分支数 1，函数体节点数 38；return: False, text.split(maxsplit=1)[0].lower() in KNOWN_CHANNEL_COMMANDS
  - 调用: startswith, lower, split

## 文件内调用关系
- `strip_leading_mentions` -> _is_leading_mention_token
- `extract_connect_code` -> _is_leading_mention_token
