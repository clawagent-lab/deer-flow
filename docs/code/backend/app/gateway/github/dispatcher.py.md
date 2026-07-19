# `backend/app/gateway/github/dispatcher.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/github/dispatcher.py`  ·  行数: 484

**模块文档首行**（仅供参考）: Fan out a verified GitHub webhook delivery onto the channel bus.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, logging
- `__future__` -> annotations
- `typing` -> Any
- `app.channels.message_bus` -> InboundMessage, InboundMessageType, MessageBus
- `app.gateway.github.identity` -> extract_target, resolve_thread_id
- `app.gateway.github.prompts` -> build_prompt
- `app.gateway.github.registry` -> build_github_agent_registry, lookup_agents
- `app.gateway.github.triggers` -> event_should_fire
- `deerflow.config.agents_config` -> GitHubAgentConfig, GitHubTriggerConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_is_self_event(event: str, payload: dict[str, Any], agent_name: str, github: GitHubAgentConfig) -> bool`  L41
  - _文档首行_（仅供参考）: Return True if this event was triggered by *this agent itself*.
  - 分支数 8，函数体节点数 216；return: False, sender_login.lower() in {s.lower() for s in self_logins}
  - 调用: get, isinstance, endswith, set, strip, add, values, lower

#### `ƒ` `_is_redundant_review_comment(payload: dict[str, Any]) -> bool`  L104
  - _文档首行_（仅供参考）: Return True if this ``pull_request_review_comment`` has the *shape*
  - 分支数 1，函数体节点数 59；return: False, comment.get('pull_request_review_id') is not None and comment.get('in_reply_to_id') is None
  - 调用: get, isinstance

#### `⏵ƒ` `async fanout_event(bus: MessageBus, event: str, delivery_id: str, payload: dict[str, Any], *, operator_default_mention_login: str | None) -> dict[str, Any]`  L188
  - _文档首行_（仅供参考）: Translate one webhook delivery into N inbound messages.
  - 分支数 6，函数体节点数 679；return: {'matched_agents': [], 'fired_agents': [], 'skipped': [{'reason': 'no_target'}]}, {'matched_agents': [], 'fired_agents': [], 'skipped': []}, {'matched_agents': matched_names, 'fired_agents': fired, 'skipped': skipped}
  - 调用: extract_target, info, to_thread, lookup_agents, get, _is_redundant_review_comment, _is_self_event, append, strip, event_should_fire, build_prompt, resolve_thread_id, InboundMessage, publish_inbound

## 文件内调用关系
- `fanout_event` -> _is_redundant_review_comment, _is_self_event
