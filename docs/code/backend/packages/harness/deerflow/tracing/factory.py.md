# `backend/packages/harness/deerflow/tracing/factory.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tracing/factory.py`  ·  行数: 66

## 模块概览
- 函数 3 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `typing` -> Any
- `deerflow.config` -> get_enabled_tracing_providers, get_tracing_config, is_monocle_tracing_enabled, validate_enabled_tracing_providers
- `deerflow.tracing.monocle` -> is_monocle_setup_completed

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_create_langsmith_tracer(config) -> Any`  L17
  - 分支数 0，函数体节点数 16；return: LangChainTracer(project_name=config.project)
  - 调用: LangChainTracer

#### `ƒ` `_create_langfuse_handler(config) -> Any`  L23
  - 分支数 0，函数体节点数 37；return: LangfuseCallbackHandler(public_key=config.public_key)
  - 调用: Langfuse, LangfuseCallbackHandler

#### `ƒ` `build_tracing_callbacks() -> list[Any]`  L37
  - _文档首行_（仅供参考）: Build callbacks for all explicitly enabled tracing providers.
  - 分支数 7，函数体节点数 139；raise: RuntimeError(f'LangSmith tracing initialization failed: {exc}'), RuntimeError(f'Langfuse tracing initialization failed: {exc}')；return: [], callbacks
  - 调用: validate_enabled_tracing_providers, is_monocle_tracing_enabled, is_monocle_setup_completed, debug, get_enabled_tracing_providers, get_tracing_config, append, _create_langsmith_tracer, RuntimeError, _create_langfuse_handler

## 文件内调用关系
- `build_tracing_callbacks` -> _create_langsmith_tracer, _create_langfuse_handler
