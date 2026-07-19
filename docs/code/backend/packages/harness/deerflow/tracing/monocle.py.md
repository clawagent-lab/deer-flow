# `backend/packages/harness/deerflow/tracing/monocle.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tracing/monocle.py`  ·  行数: 70

**模块文档首行**（仅供参考）: Monocle telemetry: initialized once from the Gateway lifespan when ``MONOCLE_TRACING`` is set.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `deerflow.config` -> get_enabled_tracing_providers, get_tracing_config, is_monocle_tracing_enabled

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_setup_completed` = False

## 函数
#### `ƒ` `is_monocle_setup_completed() -> bool`  L20
  - _文档首行_（仅供参考）: Whether :func:`setup_monocle_tracing_if_enabled` ran in this process.
  - 分支数 0，函数体节点数 9；return: _setup_completed

#### `ƒ` `setup_monocle_tracing_if_enabled() -> bool`  L25
  - _文档首行_（仅供参考）: Initialize Monocle telemetry when ``MONOCLE_TRACING`` is enabled; a no-op otherwise.
  - 分支数 3，函数体节点数 124；raise: RuntimeError("MONOCLE_TRACING is enabled but monocle_apptrace is not installed. Install the 'monocle' extra: `uv sync --extra monocle` in backend/, or `pip install 'deerflow-harness[monocle]'`.")；return: False, True
  - 调用: is_monocle_tracing_enabled, get_tracing_config, validate, get_enabled_tracing_providers, warning, join, RuntimeError, setup_monocle_telemetry, info

## 文件内调用关系
_无文件内调用_
