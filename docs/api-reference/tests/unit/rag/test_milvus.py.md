# `tests/unit/rag/test_milvus.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/rag/test_milvus.py`
- **模块导入名**：`tests.unit.rag.test_milvus`
- **代码行数**：930
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Tests for Milvus RAG provider.

IMPORTANT NOTE: This test file creates temporary directories for testing examples
functionality. All temporary directories are automatically cleaned up using pytest
fixtures. When adding new tests that create temporary directories:

1. Use the provided fixtures (temp_examples_dir, temp_error_examples_dir, etc.)
2. Never create temporary directories without automatic cleanup
3. Follow the pattern: fixture -> use -> automatic cleanup
4. If you need a new directory pattern, create a corresponding fixture

This ensures tests don't leave behind temporary files that clutter the workspace.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.rag.milvus import MilvusProvider`
- `from src.rag.retriever import Resource`
- `import src.rag.milvus`

**外部依赖**（第三方库 / 标准库）：

- `from __future__ import annotations`
- `from pathlib import Path`
- `from types import SimpleNamespace`
- `from uuid import uuid4`
- `import shutil`
- `import tempfile`
- `import pytest`
- `import atexit`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `DummyEmbedding` | 34 | `` |
| 函数 | `patch_embeddings` | 46 | `(monkeypatch)` |
| 函数 | `project_root` | 58 | `()` |
| 函数 | `temp_examples_dir` | 64 | `(project_root)` |
| 函数 | `temp_error_examples_dir` | 81 | `(project_root)` |
| 函数 | `temp_load_skip_examples_dir` | 98 | `(project_root)` |
| 函数 | `temp_single_chunk_examples_dir` | 115 | `(project_root)` |
| 函数 | `_patch_init` | 131 | `(monkeypatch)` |
| 函数 | `test_list_local_markdown_resources_missing_dir` | 140 | `(project_root)` |
| 函数 | `test_list_local_markdown_resources_populated` | 148 | `(temp_examples_dir)` |
| 函数 | `test_list_local_markdown_resources_read_error` | 188 | `(monkeypatch, temp_error_examples_dir)` |
| 函数 | `test_create_collection_schema_fields` | 216 | `(monkeypatch)` |
| 函数 | `test_generate_doc_id_stable` | 231 | `(monkeypatch, tmp_path)` |
| 函数 | `test_extract_title_from_markdown` | 241 | `(monkeypatch)` |
| 函数 | `test_split_content_chunking` | 250 | `(monkeypatch)` |
| 函数 | `test_get_embedding_invalid_inputs` | 262 | `(monkeypatch)` |
| 函数 | `test_list_resources_remote_success_and_dedup` | 273 | `(monkeypatch)` |
| 函数 | `test_list_resources_lite_success` | 308 | `(monkeypatch)` |
| 函数 | `test_query_relevant_documents_lite_success` | 332 | `(monkeypatch)` |
| 函数 | `test_query_relevant_documents_remote_success` | 375 | `(monkeypatch)` |
| 函数 | `test_get_embedding_dimension_explicit` | 421 | `(monkeypatch)` |
| 函数 | `test_get_embedding_dimension_unknown_model` | 428 | `(monkeypatch)` |
| 函数 | `test_is_milvus_lite_variants` | 437 | `(monkeypatch)` |
| 函数 | `test_create_collection_lite` | 447 | `(monkeypatch)` |
| 函数 | `test_ensure_collection_exists_remote` | 466 | `(monkeypatch)` |
| 函数 | `test_get_existing_document_ids_lite` | 475 | `(monkeypatch)` |
| 函数 | `test_get_existing_document_ids_remote` | 491 | `(monkeypatch)` |
| 函数 | `test_insert_document_chunk_lite_and_error` | 499 | `(monkeypatch)` |
| 函数 | `test_insert_document_chunk_remote` | 526 | `(monkeypatch)` |
| 函数 | `test_connect_lite_and_error` | 544 | `(monkeypatch)` |
| 函数 | `test_connect_remote` | 573 | `(monkeypatch)` |
| 函数 | `test_list_resources_remote_failure` | 588 | `(monkeypatch)` |
| 函数 | `test_list_local_markdown_resources_empty` | 606 | `(monkeypatch)` |
| 函数 | `test_query_relevant_documents_error` | 614 | `(monkeypatch)` |
| 函数 | `test_create_collection_when_client_exists` | 624 | `(monkeypatch)` |
| 函数 | `test_load_examples_force_reload` | 632 | `(monkeypatch)` |
| 函数 | `test_clear_example_documents_remote` | 647 | `(monkeypatch)` |
| 函数 | `test_clear_example_documents_lite` | 656 | `(monkeypatch)` |
| 函数 | `test_get_loaded_examples_lite_and_error` | 676 | `(monkeypatch)` |
| 函数 | `test_get_loaded_examples_remote` | 704 | `(monkeypatch)` |
| 函数 | `test_close_lite_and_remote` | 712 | `(monkeypatch)` |
| 函数 | `test_get_embedding_invalid_output` | 738 | `(monkeypatch)` |
| 函数 | `test_dashscope_embeddings_empty_inputs_short_circuit` | 747 | `(monkeypatch)` |
| 函数 | `test_init_embedding_model_openai` | 763 | `(monkeypatch)` |
| 函数 | `test_init_embedding_model_dashscope` | 781 | `(monkeypatch)` |
| 函数 | `test_init_embedding_model_invalid_provider` | 798 | `(monkeypatch)` |
| 函数 | `test_load_example_files_directory_missing` | 804 | `(monkeypatch)` |
| 函数 | `test_load_example_files_loads_and_skips_existing` | 820 | `(monkeypatch, temp_load_skip_examples_dir)` |
| 函数 | `test_load_example_files_single_chunk_no_suffix` | 870 | `(monkeypatch, temp_single_chunk_examples_dir)` |
| 函数 | `cleanup_test_database` | 911 | `()` |

## 符号详解

### `DummyEmbedding`

- **类型**：类  |  **行号**：34–42  |  **完整限定名**：`tests.unit.rag.test_milvus.DummyEmbedding`
- **定义**：

```python
class DummyEmbedding:
```
- **成员概览**：

  - `def __init__`
  - `def embed_query`
  - `def embed_documents`

**说明**（自动推断）：

测试用替身类 `DummyEmbedding`，模拟真实对象的接口行为以隔离外部依赖。

### `patch_embeddings`

- **类型**：函数  |  **行号**：46–54  |  **完整限定名**：`tests.unit.rag.test_milvus.patch_embeddings`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_embeddings(monkeypatch):
```

**说明**（自动推断）：

测试 fixture 函数 `patch_embeddings`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `project_root`

- **类型**：函数  |  **行号**：58–60  |  **完整限定名**：`tests.unit.rag.test_milvus.project_root`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def project_root():
```

**说明**（自动推断）：

pytest fixture，返回仓库根目录路径，用于定位测试资源文件。

### `temp_examples_dir`

- **类型**：函数  |  **行号**：64–77  |  **完整限定名**：`tests.unit.rag.test_milvus.temp_examples_dir`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def temp_examples_dir(project_root):
```

**摘要**：

Create a temporary examples directory with automatic cleanup.

### `temp_error_examples_dir`

- **类型**：函数  |  **行号**：81–94  |  **完整限定名**：`tests.unit.rag.test_milvus.temp_error_examples_dir`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def temp_error_examples_dir(project_root):
```

**摘要**：

Create a temporary error examples directory with automatic cleanup.

### `temp_load_skip_examples_dir`

- **类型**：函数  |  **行号**：98–111  |  **完整限定名**：`tests.unit.rag.test_milvus.temp_load_skip_examples_dir`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def temp_load_skip_examples_dir(project_root):
```

**摘要**：

Create a temporary examples directory for load_skip tests with automatic cleanup.

### `temp_single_chunk_examples_dir`

- **类型**：函数  |  **行号**：115–128  |  **完整限定名**：`tests.unit.rag.test_milvus.temp_single_chunk_examples_dir`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def temp_single_chunk_examples_dir(project_root):
```

**摘要**：

Create a temporary examples directory for single_chunk tests with automatic cleanup.

### `_patch_init`

- **类型**：函数  |  **行号**：131–137  |  **完整限定名**：`tests.unit.rag.test_milvus._patch_init`
- **签名**：

```python
def _patch_init(monkeypatch):
```

**摘要**：

Patch retriever initialization to use dummy embedding model.

### `test_list_local_markdown_resources_missing_dir`

- **类型**：函数  |  **行号**：140–145  |  **完整限定名**：`tests.unit.rag.test_milvus.test_list_local_markdown_resources_missing_dir`
- **签名**：

```python
def test_list_local_markdown_resources_missing_dir(project_root):
```

**说明**（自动推断）：

测试用例函数 `test_list_local_markdown_resources_missing_dir`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_list_local_markdown_resources_populated`

- **类型**：函数  |  **行号**：148–185  |  **完整限定名**：`tests.unit.rag.test_milvus.test_list_local_markdown_resources_populated`
- **签名**：

```python
def test_list_local_markdown_resources_populated(temp_examples_dir):
```

**说明**（自动推断）：

测试用例函数 `test_list_local_markdown_resources_populated`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_list_local_markdown_resources_read_error`

- **类型**：函数  |  **行号**：188–213  |  **完整限定名**：`tests.unit.rag.test_milvus.test_list_local_markdown_resources_read_error`
- **签名**：

```python
def test_list_local_markdown_resources_read_error(monkeypatch, temp_error_examples_dir):
```

**说明**（自动推断）：

测试用例函数 `test_list_local_markdown_resources_read_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_create_collection_schema_fields`

- **类型**：函数  |  **行号**：216–228  |  **完整限定名**：`tests.unit.rag.test_milvus.test_create_collection_schema_fields`
- **签名**：

```python
def test_create_collection_schema_fields(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_create_collection_schema_fields`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_generate_doc_id_stable`

- **类型**：函数  |  **行号**：231–238  |  **完整限定名**：`tests.unit.rag.test_milvus.test_generate_doc_id_stable`
- **签名**：

```python
def test_generate_doc_id_stable(monkeypatch, tmp_path):
```

**说明**（自动推断）：

测试用例函数 `test_generate_doc_id_stable`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_extract_title_from_markdown`

- **类型**：函数  |  **行号**：241–247  |  **完整限定名**：`tests.unit.rag.test_milvus.test_extract_title_from_markdown`
- **签名**：

```python
def test_extract_title_from_markdown(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_extract_title_from_markdown`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_split_content_chunking`

- **类型**：函数  |  **行号**：250–259  |  **完整限定名**：`tests.unit.rag.test_milvus.test_split_content_chunking`
- **签名**：

```python
def test_split_content_chunking(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_split_content_chunking`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_get_embedding_invalid_inputs`

- **类型**：函数  |  **行号**：262–270  |  **完整限定名**：`tests.unit.rag.test_milvus.test_get_embedding_invalid_inputs`
- **签名**：

```python
def test_get_embedding_invalid_inputs(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_get_embedding_invalid_inputs`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_list_resources_remote_success_and_dedup`

- **类型**：函数  |  **行号**：273–305  |  **完整限定名**：`tests.unit.rag.test_milvus.test_list_resources_remote_success_and_dedup`
- **签名**：

```python
def test_list_resources_remote_success_and_dedup(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_list_resources_remote_success_and_dedup`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_list_resources_lite_success`

- **类型**：函数  |  **行号**：308–329  |  **完整限定名**：`tests.unit.rag.test_milvus.test_list_resources_lite_success`
- **签名**：

```python
def test_list_resources_lite_success(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_list_resources_lite_success`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_query_relevant_documents_lite_success`

- **类型**：函数  |  **行号**：332–372  |  **完整限定名**：`tests.unit.rag.test_milvus.test_query_relevant_documents_lite_success`
- **签名**：

```python
def test_query_relevant_documents_lite_success(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_query_relevant_documents_lite_success`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_query_relevant_documents_remote_success`

- **类型**：函数  |  **行号**：375–418  |  **完整限定名**：`tests.unit.rag.test_milvus.test_query_relevant_documents_remote_success`
- **签名**：

```python
def test_query_relevant_documents_remote_success(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_query_relevant_documents_remote_success`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_get_embedding_dimension_explicit`

- **类型**：函数  |  **行号**：421–425  |  **完整限定名**：`tests.unit.rag.test_milvus.test_get_embedding_dimension_explicit`
- **签名**：

```python
def test_get_embedding_dimension_explicit(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_get_embedding_dimension_explicit`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_get_embedding_dimension_unknown_model`

- **类型**：函数  |  **行号**：428–434  |  **完整限定名**：`tests.unit.rag.test_milvus.test_get_embedding_dimension_unknown_model`
- **签名**：

```python
def test_get_embedding_dimension_unknown_model(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_get_embedding_dimension_unknown_model`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_is_milvus_lite_variants`

- **类型**：函数  |  **行号**：437–444  |  **完整限定名**：`tests.unit.rag.test_milvus.test_is_milvus_lite_variants`
- **签名**：

```python
def test_is_milvus_lite_variants(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_is_milvus_lite_variants`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_create_collection_lite`

- **类型**：函数  |  **行号**：447–463  |  **完整限定名**：`tests.unit.rag.test_milvus.test_create_collection_lite`
- **签名**：

```python
def test_create_collection_lite(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_create_collection_lite`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_ensure_collection_exists_remote`

- **类型**：函数  |  **行号**：466–472  |  **完整限定名**：`tests.unit.rag.test_milvus.test_ensure_collection_exists_remote`
- **签名**：

```python
def test_ensure_collection_exists_remote(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_ensure_collection_exists_remote`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_get_existing_document_ids_lite`

- **类型**：函数  |  **行号**：475–488  |  **完整限定名**：`tests.unit.rag.test_milvus.test_get_existing_document_ids_lite`
- **签名**：

```python
def test_get_existing_document_ids_lite(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_get_existing_document_ids_lite`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_get_existing_document_ids_remote`

- **类型**：函数  |  **行号**：491–496  |  **完整限定名**：`tests.unit.rag.test_milvus.test_get_existing_document_ids_remote`
- **签名**：

```python
def test_get_existing_document_ids_remote(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_get_existing_document_ids_remote`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_insert_document_chunk_lite_and_error`

- **类型**：函数  |  **行号**：499–523  |  **完整限定名**：`tests.unit.rag.test_milvus.test_insert_document_chunk_lite_and_error`
- **签名**：

```python
def test_insert_document_chunk_lite_and_error(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_insert_document_chunk_lite_and_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_insert_document_chunk_remote`

- **类型**：函数  |  **行号**：526–541  |  **完整限定名**：`tests.unit.rag.test_milvus.test_insert_document_chunk_remote`
- **签名**：

```python
def test_insert_document_chunk_remote(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_insert_document_chunk_remote`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_connect_lite_and_error`

- **类型**：函数  |  **行号**：544–570  |  **完整限定名**：`tests.unit.rag.test_milvus.test_connect_lite_and_error`
- **签名**：

```python
def test_connect_lite_and_error(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_connect_lite_and_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_connect_remote`

- **类型**：函数  |  **行号**：573–585  |  **完整限定名**：`tests.unit.rag.test_milvus.test_connect_remote`
- **签名**：

```python
def test_connect_remote(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_connect_remote`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_list_resources_remote_failure`

- **类型**：函数  |  **行号**：588–603  |  **完整限定名**：`tests.unit.rag.test_milvus.test_list_resources_remote_failure`
- **签名**：

```python
def test_list_resources_remote_failure(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_list_resources_remote_failure`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_list_local_markdown_resources_empty`

- **类型**：函数  |  **行号**：606–611  |  **完整限定名**：`tests.unit.rag.test_milvus.test_list_local_markdown_resources_empty`
- **签名**：

```python
def test_list_local_markdown_resources_empty(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_list_local_markdown_resources_empty`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_query_relevant_documents_error`

- **类型**：函数  |  **行号**：614–621  |  **完整限定名**：`tests.unit.rag.test_milvus.test_query_relevant_documents_error`
- **签名**：

```python
def test_query_relevant_documents_error(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_query_relevant_documents_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_create_collection_when_client_exists`

- **类型**：函数  |  **行号**：624–629  |  **完整限定名**：`tests.unit.rag.test_milvus.test_create_collection_when_client_exists`
- **签名**：

```python
def test_create_collection_when_client_exists(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_create_collection_when_client_exists`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_examples_force_reload`

- **类型**：函数  |  **行号**：632–644  |  **完整限定名**：`tests.unit.rag.test_milvus.test_load_examples_force_reload`
- **签名**：

```python
def test_load_examples_force_reload(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_load_examples_force_reload`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_clear_example_documents_remote`

- **类型**：函数  |  **行号**：647–653  |  **完整限定名**：`tests.unit.rag.test_milvus.test_clear_example_documents_remote`
- **签名**：

```python
def test_clear_example_documents_remote(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_clear_example_documents_remote`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_clear_example_documents_lite`

- **类型**：函数  |  **行号**：656–673  |  **完整限定名**：`tests.unit.rag.test_milvus.test_clear_example_documents_lite`
- **签名**：

```python
def test_clear_example_documents_lite(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_clear_example_documents_lite`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_get_loaded_examples_lite_and_error`

- **类型**：函数  |  **行号**：676–701  |  **完整限定名**：`tests.unit.rag.test_milvus.test_get_loaded_examples_lite_and_error`
- **签名**：

```python
def test_get_loaded_examples_lite_and_error(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_get_loaded_examples_lite_and_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_get_loaded_examples_remote`

- **类型**：函数  |  **行号**：704–709  |  **完整限定名**：`tests.unit.rag.test_milvus.test_get_loaded_examples_remote`
- **签名**：

```python
def test_get_loaded_examples_remote(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_get_loaded_examples_remote`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_close_lite_and_remote`

- **类型**：函数  |  **行号**：712–735  |  **完整限定名**：`tests.unit.rag.test_milvus.test_close_lite_and_remote`
- **签名**：

```python
def test_close_lite_and_remote(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_close_lite_and_remote`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_get_embedding_invalid_output`

- **类型**：函数  |  **行号**：738–744  |  **完整限定名**：`tests.unit.rag.test_milvus.test_get_embedding_invalid_output`
- **签名**：

```python
def test_get_embedding_invalid_output(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_get_embedding_invalid_output`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_dashscope_embeddings_empty_inputs_short_circuit`

- **类型**：函数  |  **行号**：747–759  |  **完整限定名**：`tests.unit.rag.test_milvus.test_dashscope_embeddings_empty_inputs_short_circuit`
- **签名**：

```python
def test_dashscope_embeddings_empty_inputs_short_circuit(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_dashscope_embeddings_empty_inputs_short_circuit`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_init_embedding_model_openai`

- **类型**：函数  |  **行号**：763–778  |  **完整限定名**：`tests.unit.rag.test_milvus.test_init_embedding_model_openai`
- **签名**：

```python
def test_init_embedding_model_openai(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_init_embedding_model_openai`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_init_embedding_model_dashscope`

- **类型**：函数  |  **行号**：781–795  |  **完整限定名**：`tests.unit.rag.test_milvus.test_init_embedding_model_dashscope`
- **签名**：

```python
def test_init_embedding_model_dashscope(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_init_embedding_model_dashscope`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_init_embedding_model_invalid_provider`

- **类型**：函数  |  **行号**：798–801  |  **完整限定名**：`tests.unit.rag.test_milvus.test_init_embedding_model_invalid_provider`
- **签名**：

```python
def test_init_embedding_model_invalid_provider(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_init_embedding_model_invalid_provider`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_example_files_directory_missing`

- **类型**：函数  |  **行号**：804–817  |  **完整限定名**：`tests.unit.rag.test_milvus.test_load_example_files_directory_missing`
- **签名**：

```python
def test_load_example_files_directory_missing(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_load_example_files_directory_missing`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_example_files_loads_and_skips_existing`

- **类型**：函数  |  **行号**：820–867  |  **完整限定名**：`tests.unit.rag.test_milvus.test_load_example_files_loads_and_skips_existing`
- **签名**：

```python
def test_load_example_files_loads_and_skips_existing(monkeypatch, temp_load_skip_examples_dir):
```

**说明**（自动推断）：

测试用例函数 `test_load_example_files_loads_and_skips_existing`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_example_files_single_chunk_no_suffix`

- **类型**：函数  |  **行号**：870–904  |  **完整限定名**：`tests.unit.rag.test_milvus.test_load_example_files_single_chunk_no_suffix`
- **签名**：

```python
def test_load_example_files_single_chunk_no_suffix(monkeypatch, temp_single_chunk_examples_dir):
```

**说明**（自动推断）：

测试用例函数 `test_load_example_files_single_chunk_no_suffix`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `cleanup_test_database`

- **类型**：函数  |  **行号**：911–926  |  **完整限定名**：`tests.unit.rag.test_milvus.cleanup_test_database`
- **签名**：

```python
def cleanup_test_database():
```

**摘要**：

Clean up milvus_demo.db file created during testing.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.rag.test_milvus import patch_embeddings
#
# TODO: 结合业务场景补充 patch_embeddings 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
