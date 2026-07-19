# `backend/packages/harness/deerflow/config/stream_bridge_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/stream_bridge_config.py`  ·  行数: 74

**模块文档首行**（仅供参考）: Configuration for stream bridge.

## 模块概览
- 函数 3 个，类 1 个，模块级常量 2 个

## 依赖（import）
- `typing` -> Literal
- `pydantic` -> BaseModel, Field

## 模块级常量
- `StreamBridgeType` = Literal['memory', 'redis']
- `_stream_bridge_config` = None

## 函数
#### `ƒ` `get_stream_bridge_config() -> StreamBridgeConfig | None`  L56
  - _文档首行_（仅供参考）: Get the current stream bridge configuration, or None if not configured.
  - 分支数 0，函数体节点数 12；return: _stream_bridge_config

#### `ƒ` `set_stream_bridge_config(config: StreamBridgeConfig | None) -> None`  L61
  - _文档首行_（仅供参考）: Set the stream bridge configuration.
  - 分支数 0，函数体节点数 17

#### `ƒ` `load_stream_bridge_config_from_dict(config_dict: dict | None) -> None`  L67
  - _文档首行_（仅供参考）: Load stream bridge configuration from a dictionary.
  - 分支数 1，函数体节点数 32；return: None
  - 调用: StreamBridgeConfig

## 类
### 类 `StreamBridgeConfig`  L10
- 继承: BaseModel
- _文档首行_: Configuration for the stream bridge that connects agent workers to SSE endpoints.
- 类/实例变量:
  - `type` = Field(default='memory', description="Stream bridge backen...
  - `redis_url` = Field(default=None, description='Redis URL for the redis ...
  - `queue_maxsize` = Field(default=256, description='Maximum number of events ...
  - `max_connections` = Field(default=None, description="Max Redis connections in...
  - `stream_ttl_seconds` = Field(default=86400, ge=0, description='Rolling Redis str...
  - `recovered_stream_cleanup_delay_seconds` = Field(default=60.0, ge=0, description='Seconds to wait af...

## 文件内调用关系
_无文件内调用_
