# `backend/packages/harness/deerflow/sandbox/security.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/security.py`  ·  行数: 46

**模块文档首行**（仅供参考）: Security helpers for sandbox capability gating.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 3 个

## 依赖（import）
- `deerflow.config` -> get_app_config

## 模块级常量
- `_LOCAL_SANDBOX_PROVIDER_MARKERS` = ('deerflow.sandbox.local:LocalSandboxProvider', 'deerflow...
- `LOCAL_HOST_BASH_DISABLED_MESSAGE` = 'Host bash execution is disabled for LocalSandboxProvider...
- `LOCAL_BASH_SUBAGENT_DISABLED_MESSAGE` = 'Bash subagent is disabled for LocalSandboxProvider becau...

## 函数
#### `ƒ` `uses_local_sandbox_provider(config) -> bool`  L23
  - _文档首行_（仅供参考）: Return True when the active sandbox provider is the host-local provider.
  - 分支数 2，函数体节点数 63；return: True, sandbox_use.endswith(':LocalSandboxProvider') and 'deerflow.sandbox.local' in sandbox_use
  - 调用: get_app_config, getattr, endswith
  - 反射: getattr (L28), getattr (L29)

#### `ƒ` `is_host_bash_allowed(config) -> bool`  L35
  - _文档首行_（仅供参考）: Return whether host bash execution is explicitly allowed.
  - 分支数 3，函数体节点数 59；return: False, True, bool(getattr(sandbox_cfg, 'allow_host_bash', False))
  - 调用: get_app_config, getattr, uses_local_sandbox_provider, bool
  - 反射: getattr (L40), getattr (L45)

## 文件内调用关系
- `is_host_bash_allowed` -> uses_local_sandbox_provider
