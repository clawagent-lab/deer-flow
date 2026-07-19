# `backend/packages/harness/deerflow/runtime/secret_context.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/secret_context.py`  ·  行数: 147

**模块文档首行**（仅供参考）: Request-scoped secret carrier in the run context (issue #3861).

## 模块概览
- 函数 7 个，类 0 个，模块级常量 7 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any

## 模块级常量
- `SECRETS_CONTEXT_KEY` = 'secrets'
- `ACTIVE_SECRETS_CONTEXT_KEY` = '__active_skill_secrets'
- `SKILL_TOOL_POLICY_DECISION_CONTEXT_KEY` = '__skill_tool_policy_decision'
- `_SLASH_SECRET_SOURCE_KEY` = '__slash_skill_secret_source'
- `_SECRETS_BINDING_AUDIT_KEY` = '__skill_secrets_binding_audit'
- `_SLASH_SKILL_ACTIVATION_RUN_KEY` = '__slash_skill_activation_run'
- `REDACTED_CONTEXT_KEYS` = frozenset({SECRETS_CONTEXT_KEY, ACTIVE_SECRETS_CONTEXT_KE...

## 函数
#### `ƒ` `_string_pairs(raw: Any) -> dict[str, str]`  L35
  - 分支数 1，函数体节点数 61；return: {}, {key: value for key, value in raw.items() if isinstance(key, str) and isinstance(value, str)}
  - 调用: isinstance, items

#### `ƒ` `extract_request_secrets(context: Any) -> dict[str, str]`  L41
  - _文档首行_（仅供参考）: Return the caller-supplied request-scoped secrets mapping, or ``{}``.
  - 分支数 1，函数体节点数 40；return: {}, _string_pairs(context.get(SECRETS_CONTEXT_KEY))
  - 调用: isinstance, _string_pairs, get

#### `ƒ` `read_active_secrets(context: Any) -> dict[str, str]`  L52
  - _文档首行_（仅供参考）: Return the secrets resolved for the active skill (the per-run injection
  - 分支数 1，函数体节点数 40；return: {}, _string_pairs(context.get(ACTIVE_SECRETS_CONTEXT_KEY))
  - 调用: isinstance, _string_pairs, get

#### `ƒ` `write_slash_skill_source_path(context: Any, path: str, *, owner_token: str) -> None`  L60
  - _文档首行_（仅供参考）: Persist an authenticated slash-activated skill path in a run context.
  - 分支数 1，函数体节点数 56
  - 调用: isinstance

#### `ƒ` `read_slash_skill_source_path(context: Any, *, owner_token: str) -> str | None`  L71
  - _文档首行_（仅供参考）: Return the authenticated slash-activated skill path, if well formed.
  - 分支数 3，函数体节点数 107；return: None, path if isinstance(path, str) and path else None
  - 调用: isinstance, get

#### `ƒ` `redact_secret_context_keys(context: Any) -> Any`  L117
  - _文档首行_（仅供参考）: Return a shallow copy of ``context`` with secret-bearing keys removed.
  - 分支数 1，函数体节点数 46；return: context, {key: value for key, value in context.items() if key not in REDACTED_CONTEXT_KEYS}
  - 调用: isinstance, items

#### `ƒ` `redact_config_secrets(config: Any) -> Any`  L130
  - _文档首行_（仅供参考）: Return a copy of a run config safe to persist or echo back to clients.
  - 分支数 2，函数体节点数 66；return: config, redacted
  - 调用: isinstance, get, dict, redact_secret_context_keys

## 文件内调用关系
- `extract_request_secrets` -> _string_pairs
- `read_active_secrets` -> _string_pairs
- `redact_config_secrets` -> redact_secret_context_keys
