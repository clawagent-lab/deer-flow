# `backend/packages/harness/deerflow/authz/__init__.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/authz/__init__.py`  ·  行数: 17

**模块文档首行**（仅供参考）: Pluggable fine-grained authorization (resource-level RBAC and beyond).

## 模块概览
- 函数 0 个，类 0 个，模块级常量 1 个
- `__all__`: AuthzDecision, AuthzReason, AuthzRequest, AuthorizationProvider, GuardrailAuthorizationAdapter, Principal, build_principal_from_context, normalize_authz_attributes

## 依赖（import）
- `deerflow.authz.adapter` -> GuardrailAuthorizationAdapter
- `deerflow.authz.principal` -> build_principal_from_context, normalize_authz_attributes
- `deerflow.authz.provider` -> AuthorizationProvider, AuthzDecision, AuthzReason, AuthzRequest, Principal

## 模块级常量
- `__all__` = ['AuthzDecision', 'AuthzReason', 'AuthzRequest', 'Authori...
