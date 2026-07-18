# `src/tools/python_repl.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/python_repl.py`
- **模块导入名**：`src.tools.python_repl`
- **代码行数**：70
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
Python 代码执行工具。

提供 ``python_repl_tool`` LangChain 工具，供智能体在研究流程中执行
Python 代码以进行数据分析或计算。工具默认通过环境变量
``ENABLE_PYTHON_REPL`` 控制开关，未启用时返回禁用提示，避免误用。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .decorators import log_io`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Annotated, Optional`
- `from langchain_core.tools import tool`
- `from langchain_experimental.utilities import PythonREPL`
- `import logging`
- `import os`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `_is_python_repl_enabled` | 21 | `() -> bool` |
| 常量 | `logger` | 32 | `logging.getLogger(__name__)` |
| 函数 | `python_repl_tool` | 37 | `(code: Annotated[str, 'The python code to execute to do further analysis or calculation.'])` |

## 符号详解

### `_is_python_repl_enabled`

- **类型**：函数  |  **行号**：21–27  |  **完整限定名**：`src.tools.python_repl._is_python_repl_enabled`
- **签名**：

```python
def _is_python_repl_enabled() -> bool:
```

**摘要**：

Check if Python REPL tool is enabled from configuration.

### `logger`

- **类型**：模块常量  |  **行号**：32–32  |  **完整限定名**：`src.tools.python_repl.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `python_repl_tool`

- **类型**：函数  |  **行号**：37–70  |  **完整限定名**：`src.tools.python_repl.python_repl_tool`
- **装饰器**：`@tool`, `@log_io`
- **签名**：

```python
def python_repl_tool(code: Annotated[str, 'The python code to execute to do further analysis or calculation.']):
```

**摘要**：

Use this to execute python code and do data analysis or calculation. If you want to see the output of a value,
you should print it out with `print(...)`. This is visible to the user.

## 调用关系（下游）

**被以下模块导入**：

- `src.tools`
- `tests.unit.tools.test_python_repl`

## 示例用法

```python
from src.tools.python_repl import python_repl_tool
#
# TODO: 结合业务场景补充 python_repl_tool 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
