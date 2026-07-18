# `src/server/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/server/__init__.py`
- **模块导入名**：`src.server`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：11
- **架构归属**：src/server —— FastAPI 服务层（chat / config / eval / mcp / rag 路由 + 校验工具）

## 模块概述

```text
FastAPI 服务端包入口。

导出核心 FastAPI 应用实例 ``app``，供 uvicorn 等 ASGI 服务器启动使用。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .app import app`

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
# import src.server
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
