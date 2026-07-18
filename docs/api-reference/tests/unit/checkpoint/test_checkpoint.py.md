# `tests/unit/checkpoint/test_checkpoint.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/checkpoint/test_checkpoint.py`
- **模块导入名**：`tests.unit.checkpoint.test_checkpoint`
- **代码行数**：685
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `import src.graph.checkpoint`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import MagicMock, patch`
- `from postgres_mock_utils import PostgreSQLMockInstance`
- `import os`
- `import mongomock`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `POSTGRES_URL` | 13 | `'postgresql://postgres:postgres@localhost:5432/checkpointing_db'` |
| 常量 | `MONGO_URL` | 14 | `'mongodb://admin:admin@localhost:27017/checkpointing_db?authSource=admin'` |
| 函数 | `has_real_db_connection` | 17 | `()` |
| 函数 | `test_with_local_postgres_db` | 25 | `()` |
| 函数 | `test_with_local_mongo_db` | 39 | `()` |
| 函数 | `test_init_without_checkpoint_saver` | 54 | `()` |
| 函数 | `test_process_stream_partial_buffer_postgres` | 63 | `(monkeypatch)` |
| 函数 | `test_process_stream_partial_buffer_mongo` | 85 | `()` |
| 函数 | `test_persist_postgresql_local_db` | 107 | `()` |
| 函数 | `test_persist_postgresql_called_with_aggregated_chunks` | 138 | `()` |
| 函数 | `test_persist_not_attempted_when_saver_disabled` | 163 | `()` |
| 函数 | `test_persist_mongodb_local_db` | 170 | `()` |
| 函数 | `test_persist_mongodb_called_with_aggregated_chunks` | 208 | `()` |
| 函数 | `test_invalid_inputs_return_false` | 230 | `(monkeypatch)` |
| 函数 | `test_unsupported_db_uri_scheme` | 249 | `()` |
| 函数 | `test_process_stream_with_interrupt_finish_reason` | 260 | `()` |
| 函数 | `test_postgresql_connection_failure` | 294 | `(monkeypatch)` |
| 函数 | `test_mongodb_ping_failure` | 310 | `(monkeypatch)` |
| 函数 | `test_store_namespace_consistency` | 331 | `()` |
| 函数 | `test_cursor_initialization_edge_cases` | 357 | `()` |
| 函数 | `test_multiple_threads_isolation` | 376 | `()` |
| 函数 | `test_mongodb_insert_and_update_paths` | 416 | `()` |
| 函数 | `test_postgresql_insert_update_and_error_paths` | 451 | `()` |
| 函数 | `test_create_chat_streams_table_success_and_error` | 515 | `()` |
| 函数 | `test_close_closes_resources_and_handles_errors` | 560 | `()` |
| 函数 | `test_context_manager_calls_close` | 589 | `(monkeypatch)` |
| 函数 | `test_init_mongodb_success_and_failure` | 612 | `(monkeypatch)` |
| 函数 | `test_init_postgresql_calls_connect_and_create_table` | 632 | `(monkeypatch)` |
| 函数 | `test_chat_stream_message_wrapper` | 657 | `(monkeypatch)` |

## 符号详解

### `POSTGRES_URL`

- **类型**：模块常量  |  **行号**：13–13  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.POSTGRES_URL`
- **值**：

```python
POSTGRES_URL = 'postgresql://postgres:postgres@localhost:5432/checkpointing_db'
```

**说明**（自动推断）：

外部服务 API 地址常量 `POSTGRES_URL`，在模块导入时从配置或环境变量读取。

### `MONGO_URL`

- **类型**：模块常量  |  **行号**：14–14  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.MONGO_URL`
- **值**：

```python
MONGO_URL = 'mongodb://admin:admin@localhost:27017/checkpointing_db?authSource=admin'
```

**说明**（自动推断）：

外部服务 API 地址常量 `MONGO_URL`，在模块导入时从配置或环境变量读取。

### `has_real_db_connection`

- **类型**：函数  |  **行号**：17–22  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.has_real_db_connection`
- **签名**：

```python
def has_real_db_connection():
```

**说明**（自动推断）：

测试守卫函数，检测是否具备真实数据库连接，用于跳过需 DB 的测试。

### `test_with_local_postgres_db`

- **类型**：函数  |  **行号**：25–36  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_with_local_postgres_db`
- **签名**：

```python
def test_with_local_postgres_db():
```

**摘要**：

Ensure the ChatStreamManager can be initialized with a local PostgreSQL DB.

### `test_with_local_mongo_db`

- **类型**：函数  |  **行号**：39–51  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_with_local_mongo_db`
- **签名**：

```python
def test_with_local_mongo_db():
```

**摘要**：

Ensure the ChatStreamManager can be initialized with a local MongoDB.

### `test_init_without_checkpoint_saver`

- **类型**：函数  |  **行号**：54–60  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_init_without_checkpoint_saver`
- **签名**：

```python
def test_init_without_checkpoint_saver():
```

**摘要**：

Manager should not create DB clients when checkpoint_saver is False.

### `test_process_stream_partial_buffer_postgres`

- **类型**：函数  |  **行号**：63–82  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_process_stream_partial_buffer_postgres`
- **签名**：

```python
def test_process_stream_partial_buffer_postgres(monkeypatch):
```

**摘要**：

Partial chunks should be buffered; Postgres init is stubbed to no-op.

### `test_process_stream_partial_buffer_mongo`

- **类型**：函数  |  **行号**：85–101  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_process_stream_partial_buffer_mongo`
- **签名**：

```python
def test_process_stream_partial_buffer_mongo():
```

**摘要**：

Partial chunks should be buffered; Use mongomock instead of real MongoDB.

### `test_persist_postgresql_local_db`

- **类型**：函数  |  **行号**：107–132  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_persist_postgresql_local_db`
- **装饰器**：`@pytest.mark.skipif`
- **签名**：

```python
def test_persist_postgresql_local_db():
```

**摘要**：

Ensure that the ChatStreamManager can persist to a local PostgreSQL DB.

### `test_persist_postgresql_called_with_aggregated_chunks`

- **类型**：函数  |  **行号**：138–160  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_persist_postgresql_called_with_aggregated_chunks`
- **装饰器**：`@pytest.mark.skipif`
- **签名**：

```python
def test_persist_postgresql_called_with_aggregated_chunks():
```

**摘要**：

On 'stop', aggregated chunks should be passed to PostgreSQL persist method.

### `test_persist_not_attempted_when_saver_disabled`

- **类型**：函数  |  **行号**：163–167  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_persist_not_attempted_when_saver_disabled`
- **签名**：

```python
def test_persist_not_attempted_when_saver_disabled():
```

**摘要**：

When saver disabled, stop should not persist and should return False.

### `test_persist_mongodb_local_db`

- **类型**：函数  |  **行号**：170–202  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_persist_mongodb_local_db`
- **签名**：

```python
def test_persist_mongodb_local_db():
```

**摘要**：

Ensure that the ChatStreamManager can persist to a mocked MongoDB.

### `test_persist_mongodb_called_with_aggregated_chunks`

- **类型**：函数  |  **行号**：208–227  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_persist_mongodb_called_with_aggregated_chunks`
- **装饰器**：`@pytest.mark.skipif`
- **签名**：

```python
def test_persist_mongodb_called_with_aggregated_chunks():
```

**摘要**：

On 'stop', aggregated chunks should be passed to MongoDB persist method.

### `test_invalid_inputs_return_false`

- **类型**：函数  |  **行号**：230–246  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_invalid_inputs_return_false`
- **签名**：

```python
def test_invalid_inputs_return_false(monkeypatch):
```

**摘要**：

Empty thread_id or message should be rejected and return False.

### `test_unsupported_db_uri_scheme`

- **类型**：函数  |  **行号**：249–257  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_unsupported_db_uri_scheme`
- **签名**：

```python
def test_unsupported_db_uri_scheme():
```

**摘要**：

Manager should log warning for unsupported database URI schemes.

### `test_process_stream_with_interrupt_finish_reason`

- **类型**：函数  |  **行号**：260–291  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_process_stream_with_interrupt_finish_reason`
- **签名**：

```python
def test_process_stream_with_interrupt_finish_reason():
```

**摘要**：

Test that 'interrupt' finish_reason triggers persistence like 'stop'.

### `test_postgresql_connection_failure`

- **类型**：函数  |  **行号**：294–307  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_postgresql_connection_failure`
- **签名**：

```python
def test_postgresql_connection_failure(monkeypatch):
```

**摘要**：

Test PostgreSQL connection failure handling.

### `test_mongodb_ping_failure`

- **类型**：函数  |  **行号**：310–328  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_mongodb_ping_failure`
- **签名**：

```python
def test_mongodb_ping_failure(monkeypatch):
```

**摘要**：

Test MongoDB ping failure during initialization.

### `test_store_namespace_consistency`

- **类型**：函数  |  **行号**：331–354  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_store_namespace_consistency`
- **签名**：

```python
def test_store_namespace_consistency():
```

**摘要**：

Test that store namespace is consistently used across methods.

### `test_cursor_initialization_edge_cases`

- **类型**：函数  |  **行号**：357–373  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_cursor_initialization_edge_cases`
- **签名**：

```python
def test_cursor_initialization_edge_cases():
```

**摘要**：

Test cursor handling edge cases.

### `test_multiple_threads_isolation`

- **类型**：函数  |  **行号**：376–413  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_multiple_threads_isolation`
- **签名**：

```python
def test_multiple_threads_isolation():
```

**摘要**：

Test that different thread_ids are properly isolated.

### `test_mongodb_insert_and_update_paths`

- **类型**：函数  |  **行号**：416–448  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_mongodb_insert_and_update_paths`
- **签名**：

```python
def test_mongodb_insert_and_update_paths():
```

**摘要**：

Exercise MongoDB insert, update, and exception branches using mongomock.

### `test_postgresql_insert_update_and_error_paths`

- **类型**：函数  |  **行号**：451–512  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_postgresql_insert_update_and_error_paths`
- **签名**：

```python
def test_postgresql_insert_update_and_error_paths():
```

**摘要**：

Exercise PostgreSQL update, insert, and error/rollback branches.

### `test_create_chat_streams_table_success_and_error`

- **类型**：函数  |  **行号**：515–557  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_create_chat_streams_table_success_and_error`
- **签名**：

```python
def test_create_chat_streams_table_success_and_error():
```

**摘要**：

Ensure table creation commits on success and rolls back on failure.

### `test_close_closes_resources_and_handles_errors`

- **类型**：函数  |  **行号**：560–586  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_close_closes_resources_and_handles_errors`
- **签名**：

```python
def test_close_closes_resources_and_handles_errors():
```

**摘要**：

Close should gracefully handle both success and exceptions.

### `test_context_manager_calls_close`

- **类型**：函数  |  **行号**：589–609  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_context_manager_calls_close`
- **签名**：

```python
def test_context_manager_calls_close(monkeypatch):
```

**摘要**：

The context manager protocol should call close() on exit.

### `test_init_mongodb_success_and_failure`

- **类型**：函数  |  **行号**：612–629  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_init_mongodb_success_and_failure`
- **签名**：

```python
def test_init_mongodb_success_and_failure(monkeypatch):
```

**摘要**：

MongoDB init should succeed with mongomock and fail gracefully with errors.

### `test_init_postgresql_calls_connect_and_create_table`

- **类型**：函数  |  **行号**：632–654  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_init_postgresql_calls_connect_and_create_table`
- **签名**：

```python
def test_init_postgresql_calls_connect_and_create_table(monkeypatch):
```

**摘要**：

PostgreSQL init should connect and create the required table.

### `test_chat_stream_message_wrapper`

- **类型**：函数  |  **行号**：657–685  |  **完整限定名**：`tests.unit.checkpoint.test_checkpoint.test_chat_stream_message_wrapper`
- **签名**：

```python
def test_chat_stream_message_wrapper(monkeypatch):
```

**摘要**：

Wrapper should delegate when enabled and return False when disabled.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.checkpoint.test_checkpoint import has_real_db_connection
#
# TODO: 结合业务场景补充 has_real_db_connection 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
