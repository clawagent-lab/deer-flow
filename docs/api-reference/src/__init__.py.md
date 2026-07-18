# `src/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/__init__.py`
- **模块导入名**：`src`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：18
- **架构归属**：src —— DeerFlow 后端核心包，包含工作流、智能体、工具、配置等所有业务模块

## 模块概述

```text
DeerFlow 项目根包初始化模块。

主要负责在导入早期设置 Windows 平台的事件循环策略，
以确保 psycopg（PostgreSQL 驱动）在 Windows 下使用 selector 事件循环而非默认的 ProactorEventLoop，
从而避免异步数据库连接出现兼容性问题。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `import asyncio`
- `import os`

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
# import src
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
