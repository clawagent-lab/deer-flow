# `backend/packages/harness/deerflow/config/memory_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/memory_config.py`  ·  行数: 200

**模块文档首行**（仅供参考）: Configuration for the memory mechanism (host-shared fields only).

## 模块概览
- 函数 4 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: logging
- `typing` -> Any, Literal
- `pydantic` -> BaseModel, Field

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SHARED_FIELDS` = frozenset({'enabled', 'mode', 'injection_enabled', 'shutd...
- `_LEGACY_DEERMEM_FIELDS` = frozenset({'storage_path', 'storage_class', 'debounce_sec...
- `_memory_config` = MemoryConfig()

## 函数
#### `ƒ` `should_use_memory_tools(config: MemoryConfig) -> bool`  L114
  - _文档首行_（仅供参考）: Return True when memory should use model-directed tools.
  - 分支数 0，函数体节点数 23；return: config.enabled and config.mode == 'tool'

#### `ƒ` `get_memory_config() -> MemoryConfig`  L123
  - _文档首行_（仅供参考）: Get the current memory configuration.
  - 分支数 0，函数体节点数 9；return: _memory_config

#### `ƒ` `set_memory_config(config: MemoryConfig) -> None`  L128
  - _文档首行_（仅供参考）: Set the memory configuration.
  - 分支数 0，函数体节点数 14

#### `ƒ` `load_memory_config_from_dict(config_dict: dict) -> None`  L134
  - _文档首行_（仅供参考）: Load memory configuration from a dictionary.
  - 分支数 9，函数体节点数 253
  - 调用: dict, get, list, keys, pop, append, endswith, str, warning, sorted, join, MemoryConfig

## 类
### 类 `MemoryConfig`  L55
- 继承: BaseModel
- _文档首行_: Host-shared memory configuration (backend-agnostic).
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether to enable the me...
  - `mode` = Field(default='middleware', description="Memory operation...
  - `injection_enabled` = Field(default=True, description='Whether to inject memory...
  - `shutdown_flush_timeout_seconds` = Field(default=30.0, ge=1.0, le=300.0, description="Hard t...
  - `manager_class` = Field(default='deermem', description='Memory backend sele...
  - `backend_config` = Field(default_factory=dict, description="Backend-private ...

## 文件内调用关系
_无文件内调用_
