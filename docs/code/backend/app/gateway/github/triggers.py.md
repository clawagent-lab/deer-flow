# `backend/app/gateway/github/triggers.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/github/triggers.py`  ·  行数: 209

**模块文档首行**（仅供参考）: Trigger filter logic for GitHub webhook dispatch.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: re
- `__future__` -> annotations
- `typing` -> Any
- `deerflow.config.agents_config` -> GitHubTriggerConfig

## 模块级常量
- `DEFAULT_TRIGGERS` = {'ping': None, 'issues': None, 'pull_request_review': Non...

## 函数
#### `ƒ` `_action(payload: dict[str, Any]) -> str | None`  L53
  - 分支数 0，函数体节点数 39；return: action if isinstance(action, str) else None
  - 调用: get, isinstance

#### `ƒ` `_comment_body(event: str, payload: dict[str, Any]) -> str`  L58
  - _文档首行_（仅供参考）: Extract the human-typed text to scan for an ``@mention``.
  - 分支数 4，函数体节点数 161；return: body if isinstance(body, str) else '', ''
  - 调用: get, isinstance

#### `ƒ` `_author_login(event: str, payload: dict[str, Any]) -> str | None`  L82
  - _文档首行_（仅供参考）: Login of the human who triggered the event, for ``allow_authors``.
  - 分支数 4，函数体节点数 162；return: login if isinstance(login, str) else None
  - 调用: get, isinstance

#### `ƒ` `_resolved_trigger(event: str, binding_triggers: dict[str, GitHubTriggerConfig]) -> GitHubTriggerConfig | None`  L97
  - _文档首行_（仅供参考）: Merge the binding's override with per-event field defaults.
  - 分支数 2，函数体节点数 84；return: None, override, merged
  - 调用: get, model_dump, model_copy

#### `ƒ` `_mentions(body: str, login: str) -> bool`  L131
  - _文档首行_（仅供参考）: Return True if ``body`` @-mentions ``login`` with proper boundaries.
  - 分支数 0，函数体节点数 44；return: re.search(pattern, body, flags=re.IGNORECASE) is not None
  - 调用: escape, search

#### `ƒ` `event_should_fire(event: str, payload: dict[str, Any], trigger: GitHubTriggerConfig, default_mention_login: str) -> tuple[bool, str]`  L150
  - _文档首行_（仅供参考）: Decide whether ``event`` fires the agent for this binding.
  - 分支数 6，函数体节点数 195；return: (False, f'action={action!r} not in {trigger.actions}'), (True, f'allow_authors:{author}'), (False, f'mention required for @{login}'), (True, f'action={action}' if action else 'ok')
  - 调用: _action, _author_login, lower, _comment_body, _mentions

## 文件内调用关系
- `event_should_fire` -> _action, _author_login, _comment_body, _mentions
