# `tests/unit/checkpoint/test_memory_leak.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/checkpoint/test_memory_leak.py`
- **模块导入名**：`tests.unit.checkpoint.test_memory_leak`
- **代码行数**：46
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `import src.graph.checkpoint`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import patch`
- `import mongomock`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `MONGO_URL` | 6 | `'mongodb://admin:admin@localhost:27017/checkpointing_db?authSource=admin'` |
| 函数 | `test_memory_leak_check_memory_cleared_after_persistence` | 8 | `()` |

## 符号详解

### `MONGO_URL`

- **类型**：模块常量  |  **行号**：6–6  |  **完整限定名**：`tests.unit.checkpoint.test_memory_leak.MONGO_URL`
- **值**：

```python
MONGO_URL = 'mongodb://admin:admin@localhost:27017/checkpointing_db?authSource=admin'
```

**说明**（自动推断）：

外部服务 API 地址常量 `MONGO_URL`，在模块导入时从配置或环境变量读取。

### `test_memory_leak_check_memory_cleared_after_persistence`

- **类型**：函数  |  **行号**：8–46  |  **完整限定名**：`tests.unit.checkpoint.test_memory_leak.test_memory_leak_check_memory_cleared_after_persistence`
- **签名**：

```python
def test_memory_leak_check_memory_cleared_after_persistence():
```

**摘要**：

Test that InMemoryStore is cleared for a thread after successful persistence.
This prevents memory leaks for long-running processes.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.checkpoint.test_memory_leak import test_memory_leak_check_memory_cleared_after_persistence
#
# TODO: 结合业务场景补充 test_memory_leak_check_memory_cleared_after_persistence 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
