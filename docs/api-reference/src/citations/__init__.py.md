# `src/citations/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/citations/__init__.py`
- **模块导入名**：`src.citations`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：28
- **架构归属**：src/citations —— 引用元数据采集、抽取与格式化，支撑报告中的来源标注

## 模块概述

```text
Citation management module for DeerFlow.

This module provides structured citation/source metadata handling
for research reports, enabling proper attribution and inline citations.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .collector import CitationCollector`
- `from .extractor import citations_to_markdown_references, extract_citations_from_messages, merge_citations`
- `from .formatter import CitationFormatter`
- `from .models import Citation, CitationMetadata`

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.nodes`
- `src.server.app`

## 示例用法

```python
# import src.citations
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
