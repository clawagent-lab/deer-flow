# `backend/packages/harness/deerflow/runtime/stream_bridge/async_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/stream_bridge/async_provider.py`  ·  行数: 92

**模块文档首行**（仅供参考）: Async stream bridge factory.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: contextlib, logging, os
- `__future__` -> annotations
- `collections.abc` -> AsyncIterator
- `deerflow.config.app_config` -> AppConfig
- `deerflow.config.stream_bridge_config` -> StreamBridgeConfig, get_stream_bridge_config
- `.base` -> StreamBridge

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_ENV_REDIS_URL` = 'DEER_FLOW_STREAM_BRIDGE_REDIS_URL'

## 函数
#### `ƒ` `_resolve_config(app_config: AppConfig | None) -> StreamBridgeConfig | None`  L31
  - 分支数 3，函数体节点数 63；return: StreamBridgeConfig(type='redis', redis_url=redis_url), config
  - 调用: get_stream_bridge_config, getenv, StreamBridgeConfig
  - 环境变量: getenv (L38)

#### `ƒ` `_resolve_redis_url(config: StreamBridgeConfig) -> str`  L44
  - 分支数 0，函数体节点数 28；return: config.redis_url or os.getenv(_ENV_REDIS_URL) or os.getenv('REDIS_URL') or 'redis://localhost:6379/0'
  - 调用: getenv
  - 环境变量: getenv (L45), getenv (L45)

#### `⏵ƒ` `async make_stream_bridge(app_config: AppConfig | None) -> AsyncIterator[StreamBridge]`    @contextlib.asynccontextmanager  L49
  - _文档首行_（仅供参考）: Async context manager that yields a :class:`StreamBridge`.
  - 分支数 4，函数体节点数 176；生成器（yield）；raise: ValueError(f'Unknown stream bridge type: {config.type!r}')；return: None
  - 调用: _resolve_config, MemoryStreamBridge, info, close, _resolve_redis_url, RedisStreamBridge, ValueError

## 文件内调用关系
- `make_stream_bridge` -> _resolve_config, _resolve_redis_url
