# `src/graph/utils.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/graph/utils.py`
- **模块导入名**：`src.graph.utils`
- **代码行数**：115
- **架构归属**：src/graph —— LangGraph 主工作流：节点、状态、边、checkpoint、工具函数

## 模块概述

```text
图运行时消息工具模块：提供消息内容抽取、用户/助手消息判定、发言者名称集合等辅助函数，供节点与前端流式展示统一使用。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `ASSISTANT_SPEAKER_NAMES` | 8 | `{'coordinator', 'planner', 'researcher', 'coder', 'reporter', 'background_investigator'}` |
| 函数 | `get_message_content` | 18 | `(message: Any) -> str` |
| 函数 | `is_user_message` | 25 | `(message: Any) -> bool` |
| 函数 | `get_latest_user_message` | 57 | `(messages: list[Any]) -> tuple[Any, str]` |
| 函数 | `build_clarified_topic_from_history` | 67 | `(clarification_history: list[str]) -> tuple[str, list[str]]` |
| 函数 | `reconstruct_clarification_history` | 81 | `(messages: list[Any], fallback_history: list[str] \| None=None, base_topic: str='') -> list[str]` |

## 符号详解

### `ASSISTANT_SPEAKER_NAMES`

- **类型**：模块常量  |  **行号**：8–15  |  **完整限定名**：`src.graph.utils.ASSISTANT_SPEAKER_NAMES`
- **值**：

```python
ASSISTANT_SPEAKER_NAMES = {'coordinator', 'planner', 'researcher', 'coder', 'reporter', 'background_investigator'}
```

**说明**（自动推断）：

模块级常量 `ASSISTANT_SPEAKER_NAMES`，在导入时初始化，供本模块及相关流程引用。

### `get_message_content`

- **类型**：函数  |  **行号**：18–22  |  **完整限定名**：`src.graph.utils.get_message_content`
- **签名**：

```python
def get_message_content(message: Any) -> str:
```

**摘要**：

Extract message content from dict or LangChain message.

### `is_user_message`

- **类型**：函数  |  **行号**：25–54  |  **完整限定名**：`src.graph.utils.is_user_message`
- **签名**：

```python
def is_user_message(message: Any) -> bool:
```

**摘要**：

Return True if the message originated from the end user.

### `get_latest_user_message`

- **类型**：函数  |  **行号**：57–64  |  **完整限定名**：`src.graph.utils.get_latest_user_message`
- **签名**：

```python
def get_latest_user_message(messages: list[Any]) -> tuple[Any, str]:
```

**摘要**：

Return the latest user-authored message and its content.

### `build_clarified_topic_from_history`

- **类型**：函数  |  **行号**：67–78  |  **完整限定名**：`src.graph.utils.build_clarified_topic_from_history`
- **签名**：

```python
def build_clarified_topic_from_history(clarification_history: list[str]) -> tuple[str, list[str]]:
```

**摘要**：

Construct clarified topic string from an ordered clarification history.

### `reconstruct_clarification_history`

- **类型**：函数  |  **行号**：81–115  |  **完整限定名**：`src.graph.utils.reconstruct_clarification_history`
- **签名**：

```python
def reconstruct_clarification_history(messages: list[Any], fallback_history: list[str] | None=None, base_topic: str='') -> list[str]:
```

**摘要**：

Rebuild clarification history from user-authored messages, with fallback.

**参数**：

```text
messages: Conversation messages in chronological order.
    fallback_history: Optional existing history to use if no user messages found.
    base_topic: Optional topic to use when no user messages are available.
```

**返回值**：

```text
A cleaned clarification history containing unique consecutive user contents.
```

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.nodes`
- `src.server.app`
- `src.workflow`

## 示例用法

```python
from src.graph.utils import get_message_content
#
# TODO: 结合业务场景补充 get_message_content 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
