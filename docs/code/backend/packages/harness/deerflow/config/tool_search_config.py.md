# `backend/packages/harness/deerflow/config/tool_search_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/tool_search_config.py`  ·  行数: 53

**模块文档首行**（仅供参考）: Configuration for deferred tool loading via tool_search.

## 模块概览
- 函数 3 个，类 1 个，模块级常量 3 个

## 依赖（import）
- `pydantic` -> BaseModel, Field, field_validator

## 模块级常量
- `AUTO_PROMOTE_TOP_K_MIN` = 1
- `AUTO_PROMOTE_TOP_K_MAX` = 5
- `_tool_search_config` = None

## 函数
#### `ƒ` `clamp_auto_promote_top_k(value: int) -> int`  L9
  - _文档首行_（仅供参考）: Clamp the global MCP routing auto-promote breadth to PR2's range.
  - 分支数 0，函数体节点数 25；return: max(AUTO_PROMOTE_TOP_K_MIN, min(AUTO_PROMOTE_TOP_K_MAX, int(value)))
  - 调用: max, min, int

#### `ƒ` `get_tool_search_config() -> ToolSearchConfig`  L40
  - _文档首行_（仅供参考）: Get the tool search config, loading from AppConfig if needed.
  - 分支数 1，函数体节点数 22；return: _tool_search_config
  - 调用: ToolSearchConfig

#### `ƒ` `load_tool_search_config_from_dict(data: dict) -> ToolSearchConfig`  L48
  - _文档首行_（仅供参考）: Load tool search config from a dict (called during AppConfig loading).
  - 分支数 0，函数体节点数 23；return: _tool_search_config
  - 调用: model_validate

## 类
### 类 `ToolSearchConfig`  L14
- 继承: BaseModel
- _文档首行_: Configuration for deferred tool loading via tool_search.
- 类/实例变量:
  - `enabled` = Field(default=False, description='Defer tools and enable ...
  - `auto_promote_top_k` = Field(default=3, description='Maximum number of deferred ...
- 方法:
  #### `cls` `_clamp_auto_promote_top_k(cls, value: int) -> int`    @field_validator(...), classmethod  L33
    - 分支数 0，函数体节点数 20；return: clamp_auto_promote_top_k(value)
    - 调用: clamp_auto_promote_top_k, field_validator

## 文件内调用关系
- `ToolSearchConfig._clamp_auto_promote_top_k` -> clamp_auto_promote_top_k
