# `backend/app/gateway/__init__.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/__init__.py`  ·  行数: 13

## 模块概览
- 函数 1 个，类 0 个，模块级常量 1 个
- `__all__`: app, create_app, GatewayConfig, get_gateway_config

## 依赖（import）
- `.config` -> GatewayConfig, get_gateway_config

## 模块级常量
- `__all__` = ['app', 'create_app', 'GatewayConfig', 'get_gateway_config']

## 函数
#### `ƒ` `__getattr__(name: str)`  L6
  - _文档首行_（仅供参考）: Lazily expose the FastAPI app without initializing it on package import.
  - 分支数 1，函数体节点数 42；raise: AttributeError(f'module {__name__!r} has no attribute {name!r}')；return: app if name == 'app' else create_app
  - 调用: AttributeError

## 文件内调用关系
_无文件内调用_
