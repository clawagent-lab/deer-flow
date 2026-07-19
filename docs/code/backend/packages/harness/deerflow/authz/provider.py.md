# `backend/packages/harness/deerflow/authz/provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/authz/provider.py`  ·  行数: 124

**模块文档首行**（仅供参考）: AuthorizationProvider protocol and data structures for fine-grained resource authorization.

## 模块概览
- 函数 0 个，类 5 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `dataclasses` -> dataclass, field
- `typing` -> Any, Protocol, runtime_checkable

## 类
### 类 `Principal`  L30  @dataclass
- _文档首行_: The actor resolved from trusted runtime identity context.
- 类/实例变量:
  - `user_id` = None
  - `role` = None
  - `oauth_provider` = None
  - `oauth_id` = None
  - `channel_user_id` = None
  - `is_internal` = False
  - `attributes` = field(default_factory=dict)

### 类 `AuthzRequest`  L50  @dataclass
- _文档首行_: Context passed to the provider for each authorization check.
- 类/实例变量:
  - `principal` = <annotated>
  - `resource` = <annotated>
  - `action` = <annotated>
  - `target` = <annotated>
  - `context` = field(default_factory=dict)

### 类 `AuthzReason`  L68  @dataclass
- _文档首行_: Structured reason for an allow/deny decision.
- 类/实例变量:
  - `code` = <annotated>
  - `message` = ''

### 类 `AuthzDecision`  L76  @dataclass
- _文档首行_: Provider's allow/deny verdict.
- 类/实例变量:
  - `allow` = <annotated>
  - `reasons` = field(default_factory=list)
  - `policy_id` = None
  - `metadata` = field(default_factory=dict)

### 类 `AuthorizationProvider`  L86  @runtime_checkable
- 继承: Protocol
- _文档首行_: Contract for pluggable fine-grained authorization.
- 类/实例变量:
  - `name` = <annotated>
- 方法:
  #### `m` `authorize(self, request: AuthzRequest) -> AuthzDecision`  L101
    - _文档首行_（仅供参考）: Per-call decision. Feeds Layer 2 (execution) and route checks.
    - 分支数 0，函数体节点数 12
  #### `m` `filter_resources(self, principal: Principal, resource_type: str, candidates: list[str]) -> list[str]`  L109
    - _文档首行_（仅供参考）: Layer 1: batch visibility filter at assembly time.
    - 分支数 0，函数体节点数 26
  #### `⏵m` `async aauthorize(self, request: AuthzRequest) -> AuthzDecision`  L105
    - _文档首行_（仅供参考）: Async variant.
    - 分支数 0，函数体节点数 12

## 文件内调用关系
_无文件内调用_
