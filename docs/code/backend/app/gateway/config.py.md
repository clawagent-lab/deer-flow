# `backend/app/gateway/config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/config.py`  ·  行数: 27

## 模块概览
- 函数 1 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: os
- `pydantic` -> BaseModel, Field

## 模块级常量
- `_gateway_config` = None

## 函数
#### `ƒ` `get_gateway_config() -> GatewayConfig`  L17
  - _文档首行_（仅供参考）: Get gateway config, loading from environment if available.
  - 分支数 1，函数体节点数 55；return: _gateway_config
  - 调用: GatewayConfig, getenv, int, lower
  - 环境变量: getenv (L22), getenv (L23), getenv (L24)

## 类
### 类 `GatewayConfig`  L6
- 继承: BaseModel
- _文档首行_: Configuration for the API Gateway.
- 类/实例变量:
  - `host` = Field(default='0.0.0.0', description='Host to bind the ga...
  - `port` = Field(default=8001, description='Port to bind the gateway...
  - `enable_docs` = Field(default=True, description='Enable Swagger/ReDoc/Ope...

## 文件内调用关系
_无文件内调用_
