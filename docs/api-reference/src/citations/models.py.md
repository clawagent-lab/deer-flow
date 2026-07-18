# `src/citations/models.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/citations/models.py`
- **模块导入名**：`src.citations.models`
- **代码行数**：185
- **架构归属**：src/citations —— 引用元数据采集、抽取与格式化，支撑报告中的来源标注

## 模块概述

```text
Citation data models for structured source metadata.
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from datetime import datetime`
- `from typing import Any, Dict, List, Optional`
- `from urllib.parse import urlparse`
- `from pydantic import BaseModel, ConfigDict, Field`
- `import hashlib`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `CitationMetadata` | 16 | `` |
| 类 | `Citation` | 114 | `` |

## 符号详解

### `CitationMetadata`

- **类型**：类  |  **行号**：16–110  |  **完整限定名**：`src.citations.models.CitationMetadata`
- **基类**：`BaseModel`
- **定义**：

```python
class CitationMetadata(BaseModel):
```
- **成员概览**：

  - `attr url`
  - `attr title`
  - `attr description`
  - `attr content_snippet`
  - `attr raw_content`
  - `attr domain`
  - `attr author`
  - `attr published_date`
  - `attr language`
  - `attr images`
  - `attr favicon`
  - `attr relevance_score`
  - `attr credibility_score`
  - `attr accessed_at`
  - `attr extra`
  - `attr model_config`
  - `def __init__`
  - `def id`
  - `def to_dict`
  - `def from_dict`
  - `def from_search_result`

**摘要**：

Metadata extracted from a source.

### `Citation`

- **类型**：类  |  **行号**：114–185  |  **完整限定名**：`src.citations.models.Citation`
- **基类**：`BaseModel`
- **定义**：

```python
class Citation(BaseModel):
```
- **成员概览**：

  - `attr number`
  - `attr metadata`
  - `attr context`
  - `attr cited_text`
  - `attr model_config`
  - `def id`
  - `def url`
  - `def title`
  - `def to_dict`
  - `def from_dict`
  - `def to_markdown_reference`
  - `def to_numbered_reference`
  - `def to_inline_marker`
  - `def to_footnote`

**摘要**：

A citation reference that can be used in reports.

## 调用关系（下游）

**被以下模块导入**：

- `src.citations`
- `src.citations.collector`
- `src.citations.extractor`
- `src.citations.formatter`
- `tests.unit.citations.test_citations`
- `tests.unit.citations.test_models`

## 示例用法

```python
from src.citations.models import CitationMetadata
#
# TODO: 结合业务场景补充 CitationMetadata 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
