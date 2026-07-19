# `backend/app/gateway/routers/github_webhooks.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/github_webhooks.py`  ·  行数: 358

**模块文档首行**（仅供参考）: Gateway router for inbound GitHub webhook deliveries.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: hashlib, hmac, json, logging, os
- `__future__` -> annotations
- `typing` -> Any
- `fastapi` -> APIRouter, Header, HTTPException, Request
- `app.gateway.github.dispatcher` -> fanout_event

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api/webhooks', tags=['webhooks'])
- `_SECRET_ENV_VAR` = 'GITHUB_WEBHOOK_SECRET'
- `_ALLOW_UNVERIFIED_ENV_VAR` = 'DEER_FLOW_ALLOW_UNVERIFIED_GITHUB_WEBHOOKS'
- `_KNOWN_EVENTS` = frozenset({'ping', 'issues', 'issue_comment', 'pull_reque...

## 函数
#### `ƒ` `_get_webhook_secret() -> str | None`  L60
  - _文档首行_（仅供参考）: Return the configured webhook secret, or None if unset.
  - 分支数 1，函数体节点数 43；return: None, stripped or None
  - 调用: get, strip

#### `ƒ` `_unverified_webhooks_allowed() -> bool`  L75
  - _文档首行_（仅供参考）: Return True iff the explicit dev opt-in for unverified deliveries is set.
  - 分支数 0，函数体节点数 35；return: raw in {'1', 'true', 'yes', 'on'}
  - 调用: lower, strip, get

#### `ƒ` `is_route_enabled() -> bool`  L85
  - _文档首行_（仅供参考）: Return True iff the GitHub webhook route should be mounted.
  - 分支数 0，函数体节点数 18；return: _get_webhook_secret() is not None or _unverified_webhooks_allowed()
  - 调用: _get_webhook_secret, _unverified_webhooks_allowed

#### `ƒ` `_verify_signature(secret: str, body: bytes, signature_header: str | None) -> bool`  L101
  - _文档首行_（仅供参考）: Verify the GitHub ``X-Hub-Signature-256`` HMAC.
  - 分支数 2，函数体节点数 81；return: False, hmac.compare_digest(provided, expected)
  - 调用: startswith, strip, removeprefix, hexdigest, new, encode, compare_digest

#### `ƒ` `_summarise_event(event: str, payload: dict[str, Any]) -> str`  L116
  - _文档首行_（仅供参考）: Build a short, human-readable summary for the log line.
  - 分支数 7，函数体节点数 509；return: f'ping zen={zen!r} hook_id={hook_id} repo={repo}', f'pull_request action={action} repo={repo} #{number} title={title!r} url={url}', f'pull_request_review action={action} repo={repo} #{number} state={state} author={author}', f'issues action={action} repo={repo} #{number} title={title!r} url={url}', f'issue_comment action={action} repo={repo} #{number} is_pr={is_pr} author={author}', f'pull_request_review_comment action={action} repo={repo} #{number} path={path} author={author}', f'{event} action={action} repo={repo}', f'{event} (summary failed: {exc!r})'
  - 调用: get

#### `⏵ƒ` `async receive_github_webhook(request: Request, x_github_event: str | None, x_github_delivery: str | None, x_hub_signature_256: str | None) -> dict[str, Any]`    @router.post(...)  L173
  - _文档首行_（仅供参考）: Receive a GitHub webhook delivery.
  - 分支数 9，函数体节点数 475；raise: HTTPException(status_code=503, detail=f'Webhook signature verification not configured. Set {_SECRET_ENV_VAR} or {_ALLOW_UNVERIFIED_ENV_VAR}=1 for unverified dev mode.'), HTTPException(status_code=401, detail='Invalid or missing X-Hub-Signature-256'), HTTPException(status_code=400, detail='Missing X-GitHub-Event header'), HTTPException(status_code=400, detail='Invalid JSON body'), HTTPException(status_code=503, detail=f'fan-out failed for delivery {x_github_delivery!r}: {exc!r}')；return: {'ok': True, 'event': x_github_event, 'delivery': x_github_delivery, 'handled': handled, 'dispatch': dispatch_result}
  - 调用: Header, body, _get_webhook_secret, _unverified_webhooks_allowed, error, HTTPException, warning, _verify_signature, loads, info, _summarise_event, get_channel_service, is_channel_enabled, get_channel_config, get, isinstance, strip, fanout_event, exception, post

## 文件内调用关系
- `is_route_enabled` -> _get_webhook_secret, _unverified_webhooks_allowed
- `receive_github_webhook` -> _get_webhook_secret, _unverified_webhooks_allowed, _verify_signature, _summarise_event
