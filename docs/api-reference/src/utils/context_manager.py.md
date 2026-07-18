# `src/utils/context_manager.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/utils/context_manager.py`
- **模块导入名**：`src.utils.context_manager`
- **代码行数**：350
- **架构归属**：src/utils —— 通用工具（JSON 修复、日志脱敏、上下文管理）

## 模块概述

```text
对话上下文管理器。

定义 ``ContextManager``，依据 ``MODEL_TOKEN_LIMITS`` 配置估算消息列表的
token 数（英文 4 字符≈1 token、非英文 1 字符≈1 token，并按消息类型加权），
在超出 token 上限时对历史消息进行压缩/裁剪，保持前缀消息不变，
确保上下文长度符合底层模型的限制要求。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config import load_yaml_config`

**外部依赖**（第三方库 / 标准库）：

- `from typing import List`
- `from langgraph.runtime import Runtime`
- `from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage, ToolMessage`
- `import copy`
- `import json`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 27 | `logging.getLogger(__name__)` |
| 函数 | `get_search_config` | 30 | `()` |
| 类 | `ContextManager` | 36 | `` |
| 函数 | `validate_message_content` | 294 | `(messages: List[BaseMessage], max_content_length: int=100000) -> List[BaseMessage]` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：27–27  |  **完整限定名**：`src.utils.context_manager.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `get_search_config`

- **类型**：函数  |  **行号**：30–33  |  **完整限定名**：`src.utils.context_manager.get_search_config`
- **签名**：

```python
def get_search_config():
```

**说明**（自动推断）：

从 `conf.yaml` 读取搜索引擎配置段并返回字典，供搜索工具初始化时使用。

### `ContextManager`

- **类型**：类  |  **行号**：36–291  |  **完整限定名**：`src.utils.context_manager.ContextManager`
- **定义**：

```python
class ContextManager:
```
- **成员概览**：

  - `def __init__`
  - `def count_tokens`
  - `def _count_message_tokens`
  - `def _count_text_tokens`
  - `def is_over_limit`
  - `def compress_messages`
  - `def _compress_messages`
  - `def _create_summary_message`

**摘要**：

Context manager and compression class

### `validate_message_content`

- **类型**：函数  |  **行号**：294–349  |  **完整限定名**：`src.utils.context_manager.validate_message_content`
- **签名**：

```python
def validate_message_content(messages: List[BaseMessage], max_content_length: int=100000) -> List[BaseMessage]:
```

**摘要**：

Validate and fix all messages to ensure they have valid content before sending to LLM.

**参数**：

```text
messages: List of messages to validate
    max_content_length: Maximum allowed content length per message (default 100000)
```

**返回值**：

```text
List of validated messages with fixed content
```

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.nodes`
- `tests.unit.utils.test_context_manager`

## 示例用法

```python
from src.utils.context_manager import get_search_config
#
# TODO: 结合业务场景补充 get_search_config 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
