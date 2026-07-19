# `backend/app/gateway/github/identity.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/github/identity.py`  ·  行数: 92

**模块文档首行**（仅供参考）: Identity helpers for GitHub webhook dispatch.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: uuid
- `__future__` -> annotations
- `typing` -> Any

## 模块级常量
- `GITHUB_THREAD_NAMESPACE` = uuid.UUID('a3f4b2c1-7e8d-4f6a-b9c0-1234567890ab')

## 函数
#### `ƒ` `resolve_thread_id(repo: str, issue_or_pr_number: int, agent_name: str) -> str`  L29
  - _文档首行_（仅供参考）: Build a deterministic langgraph thread id from a GitHub target + agent.
  - 分支数 3，函数体节点数 116；raise: ValueError(f"Expected repo as 'owner/name', got {repo!r}"), ValueError(f'Expected issue_or_pr_number as int, got {type(issue_or_pr_number).__name__}'), ValueError(f'Expected agent_name as non-empty str, got {agent_name!r}')；return: str(uuid.uuid5(GITHUB_THREAD_NAMESPACE, f'{repo}#{issue_or_pr_number}:{agent_name}'))
  - 调用: isinstance, ValueError, type, strip, str, uuid5

#### `ƒ` `extract_target(event: str, payload: dict[str, Any]) -> tuple[str, int] | None`  L62
  - _文档首行_（仅供参考）: Best-effort extraction of (repo, number) from a webhook payload.
  - 分支数 7，函数体节点数 222；return: None, (repo, number)
  - 调用: get, isinstance

## 文件内调用关系
_无文件内调用_
