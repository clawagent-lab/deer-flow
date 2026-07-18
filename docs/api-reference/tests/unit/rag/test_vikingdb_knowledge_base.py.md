# `tests/unit/rag/test_vikingdb_knowledge_base.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/rag/test_vikingdb_knowledge_base.py`
- **模块导入名**：`tests.unit.rag.test_vikingdb_knowledge_base`
- **代码行数**：540
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.rag.vikingdb_knowledge_base import VikingDBKnowledgeBaseProvider, parse_uri`

**外部依赖**（第三方库 / 标准库）：

- `from datetime import datetime`
- `from unittest.mock import MagicMock, patch`
- `import hashlib`
- `import hmac`
- `import json`
- `import os`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `MockResource` | 17 | `` |
| 类 | `MockChunk` | 24 | `` |
| 类 | `MockDocument` | 30 | `` |
| 函数 | `patch_imports` | 39 | `()` |
| 函数 | `env_vars` | 49 | `()` |
| 类 | `TestParseUri` | 64 | `` |
| 类 | `TestVikingDBKnowledgeBaseProviderInit` | 90 | `` |
| 类 | `TestVikingDBKnowledgeBaseProviderSignature` | 189 | `` |
| 类 | `TestVikingDBKnowledgeBaseProviderQueryRelevantDocuments` | 292 | `` |
| 类 | `TestVikingDBKnowledgeBaseProviderListResources` | 445 | `` |

## 符号详解

### `MockResource`

- **类型**：类  |  **行号**：17–21  |  **完整限定名**：`tests.unit.rag.test_vikingdb_knowledge_base.MockResource`
- **定义**：

```python
class MockResource:
```
- **成员概览**：

  - `def __init__`

**说明**（自动推断）：

测试用 mock 对象 `MockResource`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `MockChunk`

- **类型**：类  |  **行号**：24–27  |  **完整限定名**：`tests.unit.rag.test_vikingdb_knowledge_base.MockChunk`
- **定义**：

```python
class MockChunk:
```
- **成员概览**：

  - `def __init__`

**说明**（自动推断）：

测试用 mock 对象 `MockChunk`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `MockDocument`

- **类型**：类  |  **行号**：30–34  |  **完整限定名**：`tests.unit.rag.test_vikingdb_knowledge_base.MockDocument`
- **定义**：

```python
class MockDocument:
```
- **成员概览**：

  - `def __init__`

**说明**（自动推断）：

测试用 mock 对象 `MockDocument`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `patch_imports`

- **类型**：函数  |  **行号**：39–45  |  **完整限定名**：`tests.unit.rag.test_vikingdb_knowledge_base.patch_imports`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_imports():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_imports`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `env_vars`

- **类型**：函数  |  **行号**：49–61  |  **完整限定名**：`tests.unit.rag.test_vikingdb_knowledge_base.env_vars`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def env_vars():
```

**摘要**：

Fixture to set up environment variables

### `TestParseUri`

- **类型**：类  |  **行号**：64–87  |  **完整限定名**：`tests.unit.rag.test_vikingdb_knowledge_base.TestParseUri`
- **定义**：

```python
class TestParseUri:
```
- **成员概览**：

  - `def test_parse_uri_valid_with_fragment`
  - `def test_parse_uri_valid_without_fragment`
  - `def test_parse_uri_invalid_scheme`
  - `def test_parse_uri_malformed`

**说明**（自动推断）：

pytest 测试类 `TestParseUri`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestVikingDBKnowledgeBaseProviderInit`

- **类型**：类  |  **行号**：90–186  |  **完整限定名**：`tests.unit.rag.test_vikingdb_knowledge_base.TestVikingDBKnowledgeBaseProviderInit`
- **定义**：

```python
class TestVikingDBKnowledgeBaseProviderInit:
```
- **成员概览**：

  - `def test_init_success_with_all_env_vars`
  - `def test_init_success_without_retrieval_size`
  - `def test_init_custom_retrieval_size`
  - `def test_init_custom_region`
  - `def test_init_missing_api_url`
  - `def test_init_missing_api_ak`
  - `def test_init_missing_api_sk`

**说明**（自动推断）：

pytest 测试类 `TestVikingDBKnowledgeBaseProviderInit`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestVikingDBKnowledgeBaseProviderSignature`

- **类型**：类  |  **行号**：189–289  |  **完整限定名**：`tests.unit.rag.test_vikingdb_knowledge_base.TestVikingDBKnowledgeBaseProviderSignature`
- **定义**：

```python
class TestVikingDBKnowledgeBaseProviderSignature:
```
- **成员概览**：

  - `def provider`
  - `def test_hmac_sha256`
  - `def test_hash_sha256`
  - `def test_get_signed_key`
  - `def test_create_canonical_request`
  - `def test_create_signature`
  - `def test_make_signed_request_success`
  - `def test_make_signed_request_with_exception`

**说明**（自动推断）：

pytest 测试类 `TestVikingDBKnowledgeBaseProviderSignature`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestVikingDBKnowledgeBaseProviderQueryRelevantDocuments`

- **类型**：类  |  **行号**：292–442  |  **完整限定名**：`tests.unit.rag.test_vikingdb_knowledge_base.TestVikingDBKnowledgeBaseProviderQueryRelevantDocuments`
- **定义**：

```python
class TestVikingDBKnowledgeBaseProviderQueryRelevantDocuments:
```
- **成员概览**：

  - `def provider`
  - `def test_query_relevant_documents_empty_resources`
  - `def test_query_relevant_documents_success`
  - `def test_query_relevant_documents_with_document_filter`
  - `def test_query_relevant_documents_api_error`
  - `def test_query_relevant_documents_json_decode_error`
  - `def test_query_relevant_documents_multiple_resources`

**说明**（自动推断）：

pytest 测试类 `TestVikingDBKnowledgeBaseProviderQueryRelevantDocuments`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestVikingDBKnowledgeBaseProviderListResources`

- **类型**：类  |  **行号**：445–540  |  **完整限定名**：`tests.unit.rag.test_vikingdb_knowledge_base.TestVikingDBKnowledgeBaseProviderListResources`
- **定义**：

```python
class TestVikingDBKnowledgeBaseProviderListResources:
```
- **成员概览**：

  - `def provider`
  - `def test_list_resources_success`
  - `def test_list_resources_with_query_filter`
  - `def test_list_resources_api_error`
  - `def test_list_resources_json_decode_error`
  - `def test_list_resources_empty_response`

**说明**（自动推断）：

pytest 测试类 `TestVikingDBKnowledgeBaseProviderListResources`，聚合一组相关的测试用例方法（以 `test_` 开头）。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.rag.test_vikingdb_knowledge_base import patch_imports
#
# TODO: 结合业务场景补充 patch_imports 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
