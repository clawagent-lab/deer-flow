# `src/llms/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/llms/__init__.py`
- **模块导入名**：`src.llms`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：7
- **架构归属**：src/llms —— LLM 适配层（统一封装 dashscope 等提供商，按类型路由）

## 模块概述

```text
LLM 模块包。

聚合项目内大语言模型相关的子模块，对外暴露 ``llm.py`` 中的 LLM 实例工厂
（``get_llm_by_type``）等能力，便于上层智能体按类型复用 ChatModel。
```

## 依赖关系（上游）

_无导入。_

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

**被以下模块导入**：

- `tests.unit.llms.test_dashscope`
- `tests.unit.llms.test_llm`

## 示例用法

```python
# import src.llms
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
