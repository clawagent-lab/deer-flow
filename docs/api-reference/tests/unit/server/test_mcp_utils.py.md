# `tests/unit/server/test_mcp_utils.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/server/test_mcp_utils.py`
- **模块导入名**：`tests.unit.server.test_mcp_utils`
- **代码行数**：185
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `import src.server.mcp_utils`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import AsyncMock, MagicMock, patch`
- `from fastapi import HTTPException`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 异步函数 | `test__get_tools_from_client_session_success` | 14 | `(mock_ClientSession)` |
| 异步函数 | `test_load_mcp_tools_stdio_success` | 47 | `(mock_stdio_client, mock_StdioServerParameters, mock_get_tools)` |
| 异步函数 | `test_load_mcp_tools_stdio_missing_command` | 72 | `()` |
| 异步函数 | `test_load_mcp_tools_sse_success` | 82 | `(mock_sse_client, mock_get_tools)` |
| 异步函数 | `test_load_mcp_tools_sse_with_sse_read_timeout` | 106 | `(mock_sse_client, mock_get_tools)` |
| 异步函数 | `test_load_mcp_tools_sse_without_sse_read_timeout` | 134 | `(mock_sse_client, mock_get_tools)` |
| 异步函数 | `test_load_mcp_tools_sse_missing_url` | 156 | `()` |
| 异步函数 | `test_load_mcp_tools_unsupported_type` | 164 | `()` |
| 异步函数 | `test_load_mcp_tools_exception_handling` | 175 | `(mock_stdio_client, mock_StdioServerParameters, mock_get_tools)` |

## 符号详解

### `test__get_tools_from_client_session_success`

- **类型**：异步函数  |  **行号**：14–40  |  **完整限定名**：`tests.unit.server.test_mcp_utils.test__get_tools_from_client_session_success`
- **装饰器**：`@pytest.mark.asyncio`, `@patch`
- **签名**：

```python
async def test__get_tools_from_client_session_success(mock_ClientSession):
```

**说明**（自动推断）：

测试用例函数 `test__get_tools_from_client_session_success`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_mcp_tools_stdio_success`

- **类型**：异步函数  |  **行号**：47–68  |  **完整限定名**：`tests.unit.server.test_mcp_utils.test_load_mcp_tools_stdio_success`
- **装饰器**：`@pytest.mark.asyncio`, `@patch`, `@patch`, `@patch`
- **签名**：

```python
async def test_load_mcp_tools_stdio_success(mock_stdio_client, mock_StdioServerParameters, mock_get_tools):
```

**说明**（自动推断）：

测试用例函数 `test_load_mcp_tools_stdio_success`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_mcp_tools_stdio_missing_command`

- **类型**：异步函数  |  **行号**：72–76  |  **完整限定名**：`tests.unit.server.test_mcp_utils.test_load_mcp_tools_stdio_missing_command`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_load_mcp_tools_stdio_missing_command():
```

**说明**（自动推断）：

测试用例函数 `test_load_mcp_tools_stdio_missing_command`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_mcp_tools_sse_success`

- **类型**：异步函数  |  **行号**：82–100  |  **完整限定名**：`tests.unit.server.test_mcp_utils.test_load_mcp_tools_sse_success`
- **装饰器**：`@pytest.mark.asyncio`, `@patch`, `@patch`
- **签名**：

```python
async def test_load_mcp_tools_sse_success(mock_sse_client, mock_get_tools):
```

**说明**（自动推断）：

测试用例函数 `test_load_mcp_tools_sse_success`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_mcp_tools_sse_with_sse_read_timeout`

- **类型**：异步函数  |  **行号**：106–128  |  **完整限定名**：`tests.unit.server.test_mcp_utils.test_load_mcp_tools_sse_with_sse_read_timeout`
- **装饰器**：`@pytest.mark.asyncio`, `@patch`, `@patch`
- **签名**：

```python
async def test_load_mcp_tools_sse_with_sse_read_timeout(mock_sse_client, mock_get_tools):
```

**摘要**：

Test that sse_read_timeout parameter is used when provided.

### `test_load_mcp_tools_sse_without_sse_read_timeout`

- **类型**：异步函数  |  **行号**：134–152  |  **完整限定名**：`tests.unit.server.test_mcp_utils.test_load_mcp_tools_sse_without_sse_read_timeout`
- **装饰器**：`@pytest.mark.asyncio`, `@patch`, `@patch`
- **签名**：

```python
async def test_load_mcp_tools_sse_without_sse_read_timeout(mock_sse_client, mock_get_tools):
```

**摘要**：

Test that timeout_seconds is used when sse_read_timeout is not provided.

### `test_load_mcp_tools_sse_missing_url`

- **类型**：异步函数  |  **行号**：156–160  |  **完整限定名**：`tests.unit.server.test_mcp_utils.test_load_mcp_tools_sse_missing_url`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_load_mcp_tools_sse_missing_url():
```

**说明**（自动推断）：

测试用例函数 `test_load_mcp_tools_sse_missing_url`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_mcp_tools_unsupported_type`

- **类型**：异步函数  |  **行号**：164–168  |  **完整限定名**：`tests.unit.server.test_mcp_utils.test_load_mcp_tools_unsupported_type`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_load_mcp_tools_unsupported_type():
```

**说明**（自动推断）：

测试用例函数 `test_load_mcp_tools_unsupported_type`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_mcp_tools_exception_handling`

- **类型**：异步函数  |  **行号**：175–185  |  **完整限定名**：`tests.unit.server.test_mcp_utils.test_load_mcp_tools_exception_handling`
- **装饰器**：`@pytest.mark.asyncio`, `@patch`, `@patch`, `@patch`
- **签名**：

```python
async def test_load_mcp_tools_exception_handling(mock_stdio_client, mock_StdioServerParameters, mock_get_tools):
```

**说明**（自动推断）：

测试用例函数 `test_load_mcp_tools_exception_handling`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.server.test_mcp_utils import test__get_tools_from_client_session_success
#
# TODO: 结合业务场景补充 test__get_tools_from_client_session_success 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
