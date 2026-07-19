# `backend/packages/harness/deerflow/authz/principal.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/authz/principal.py`  ·  行数: 63

**模块文档首行**（仅供参考）: Principal builder — the single sanctioned way to construct a Principal.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `typing` -> Any
- `deerflow.authz.provider` -> Principal

## 函数
#### `ƒ` `normalize_authz_attributes(raw: Any) -> dict[str, Any]`  L16
  - _文档首行_（仅供参考）: Validate and copy ``authz_attributes`` into a fresh dict.
  - 分支数 2，函数体节点数 53；raise: TypeError(f'authz_attributes must be a Mapping, got {type(raw).__name__}')；return: {}, dict(raw)
  - 调用: isinstance, dict, TypeError, type

#### `ƒ` `build_principal_from_context(context: Mapping[str, Any], *, default_role: str) -> Principal`  L34
  - _文档首行_（仅供参考）: Build a :class:`Principal` from a runtime context mapping.
  - 分支数 1，函数体节点数 102；return: Principal(user_id=context.get('user_id'), role=resolved_role, oauth_provider=context.get('oauth_provider'), oauth_id=context.get('oauth_id'), channel_user_id=context.get('channel_user_id'), is_internal=context.get('is_internal') is True, attributes=normalize_authz_attributes(context.get('authz_attributes')))
  - 调用: get, Principal, normalize_authz_attributes

## 文件内调用关系
- `build_principal_from_context` -> normalize_authz_attributes
