# `src/prompts/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/prompts/__init__.py`
- **模块导入名**：`src.prompts`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：14
- **架构归属**：src/prompts —— Jinja2 提示词模板与 Plan/Step 数据模型

## 模块概述

```text
Prompts 模块包。

统一对外暴露提示词模板的加载与应用能力，包括 ``get_prompt_template`` 与
``apply_prompt_template``，供各智能体按名称获取 Jinja2 渲染后的提示消息。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .template import apply_prompt_template, get_prompt_template`

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

**被以下模块导入**：

- `src.agents.agents`

## 示例用法

```python
# import src.prompts
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
