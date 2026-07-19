# `backend/packages/harness/deerflow/config/authorization_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/authorization_config.py`  ·  行数: 57

**模块文档首行**（仅供参考）: Configuration for fine-grained resource authorization.

## 模块概览
- 函数 3 个，类 2 个，模块级常量 1 个

## 依赖（import）
- `pydantic` -> BaseModel, Field

## 模块级常量
- `_authorization_config` = None

## 函数
#### `ƒ` `get_authorization_config() -> AuthorizationConfig`  L38
  - _文档首行_（仅供参考）: Get the authorization config, returning defaults if not loaded.
  - 分支数 1，函数体节点数 22；return: _authorization_config
  - 调用: AuthorizationConfig

#### `ƒ` `load_authorization_config_from_dict(data: dict) -> AuthorizationConfig`  L46
  - _文档首行_（仅供参考）: Load authorization config from a dict (called during AppConfig loading).
  - 分支数 0，函数体节点数 23；return: _authorization_config
  - 调用: model_validate

#### `ƒ` `reset_authorization_config() -> None`  L53
  - _文档首行_（仅供参考）: Reset the cached config instance. Used in tests to prevent singleton leaks.
  - 分支数 0，函数体节点数 10

## 类
### 类 `AuthorizationProviderConfig`  L14
- 继承: BaseModel
- _文档首行_: Configuration for an authorization provider.
- 类/实例变量:
  - `use` = Field(description="Class path (e.g. 'deerflow.authz.rbac:...
  - `config` = Field(default_factory=dict, description='Provider-specifi...

### 类 `AuthorizationConfig`  L21
- 继承: BaseModel
- _文档首行_: Configuration for fine-grained resource authorization.
- 类/实例变量:
  - `enabled` = Field(default=False, description='Enable fine-grained aut...
  - `fail_closed` = Field(default=True, description='Block access if the prov...
  - `default_role` = Field(default='user', description='Role applied when user...
  - `provider` = Field(default=None, description='Authorization provider c...

## 文件内调用关系
_无文件内调用_
