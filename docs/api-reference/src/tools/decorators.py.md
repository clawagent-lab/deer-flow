# `src/tools/decorators.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/decorators.py`
- **模块导入名**：`src.tools.decorators`
- **代码行数**：88
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
工具装饰器与日志增强辅助。

提供 ``log_io`` 装饰器用于记录工具函数的输入输出；``LoggedToolMixin``
与工厂函数 ``create_logged_tool`` 可为任意 ``BaseTool`` 子类动态生成
带日志的派生类，便于在研究流程中统一观测工具调用行为。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Callable, Type, TypeVar`
- `import functools`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 15 | `logging.getLogger(__name__)` |
| 常量 | `T` | 17 | `TypeVar('T')` |
| 函数 | `log_io` | 20 | `(func: Callable) -> Callable` |
| 类 | `LoggedToolMixin` | 51 | `` |
| 函数 | `create_logged_tool` | 72 | `(base_tool_class: Type[T]) -> Type[T]` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：15–15  |  **完整限定名**：`src.tools.decorators.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `T`

- **类型**：模块常量  |  **行号**：17–17  |  **完整限定名**：`src.tools.decorators.T`
- **值**：

```python
T = TypeVar('T')
```

**说明**（自动推断）：

模块级常量 `T`，在导入时初始化，供本模块及相关流程引用。

### `log_io`

- **类型**：函数  |  **行号**：20–48  |  **完整限定名**：`src.tools.decorators.log_io`
- **签名**：

```python
def log_io(func: Callable) -> Callable:
```

**摘要**：

A decorator that logs the input parameters and output of a tool function.

**参数**：

```text
func: The tool function to be decorated
```

**返回值**：

```text
The wrapped function with input/output logging
```

### `LoggedToolMixin`

- **类型**：类  |  **行号**：51–69  |  **完整限定名**：`src.tools.decorators.LoggedToolMixin`
- **定义**：

```python
class LoggedToolMixin:
```
- **成员概览**：

  - `def _log_operation`
  - `def _run`

**摘要**：

A mixin class that adds logging functionality to any tool.

### `create_logged_tool`

- **类型**：函数  |  **行号**：72–88  |  **完整限定名**：`src.tools.decorators.create_logged_tool`
- **签名**：

```python
def create_logged_tool(base_tool_class: Type[T]) -> Type[T]:
```

**摘要**：

Factory function to create a logged version of any tool class.

**参数**：

```text
base_tool_class: The original tool class to be enhanced with logging
```

**返回值**：

```text
A new class that inherits from both LoggedToolMixin and the base tool class
```

## 调用关系（下游）

**被以下模块导入**：

- `src.tools.crawl`
- `src.tools.python_repl`
- `src.tools.search`
- `tests.unit.tools.test_decorators`

## 示例用法

```python
from src.tools.decorators import log_io
#
# TODO: 结合业务场景补充 log_io 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
