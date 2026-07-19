# `backend/app/gateway/github/prompts.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/github/prompts.py`  ·  行数: 223

**模块文档首行**（仅供参考）: Translate GitHub webhook payloads into prompts for the agent.

## 模块概览
- 函数 9 个，类 0 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any

## 模块级常量
- `_EVENT_BUILDERS` = {'ping': _ping_prompt, 'pull_request': _pull_request_prom...

## 函数
#### `ƒ` `_truncate(text: str | None, limit: int) -> str`  L29
  - _文档首行_（仅供参考）: Trim long fields so a single bad payload doesn't blow the context window.
  - 分支数 2，函数体节点数 50；return: '', text, text[:limit - 20] + '\n\n[…truncated…]'
  - 调用: len

#### `ƒ` `_pull_request_prompt(payload: dict[str, Any]) -> str`  L38
  - 分支数 0，函数体节点数 164；return: f"A pull request was {action} on {repo}:\n\n  #{number} {title}\n  Author: {author}\n  URL: {url}\n\nDescription:\n{body or '(no description)'}\n\nDecide what action (if any) to take for this pull request and carry it out. Your final assistant message is for the run log only — it will NOT be posted to GitHub. If you want to reply on the PR, call `gh pr comment` (or `gh pr review`) yourself during the run."
  - 调用: get, _truncate

#### `ƒ` `_render_parent_context(parent: dict[str, Any], kind: str) -> str`  L61
  - _文档首行_（仅供参考）: Render the issue/PR the event hangs off as a header block.
  - 分支数 0，函数体节点数 101；return: f"Parent {kind}:\n  Title: {title}\n  Author: {author}\n  URL: {url}\n\n  Description:\n{body or '(no description)'}\n"
  - 调用: get, _truncate

#### `ƒ` `_issue_comment_prompt(payload: dict[str, Any]) -> str`  L76
  - 分支数 0，函数体节点数 182；return: f"A new comment was posted on {target} #{number} in {repo}.\n\n{parent_block}\nNew comment:\n  Author: {author}\n  URL: {url}\n\n  Body:\n{body or '(empty comment)'}\n\nDecide what action (if any) to take in response to this comment, in the context of the parent {target} above. Your final assistant message is for the run log only — it will NOT be posted to GitHub. If you want to reply, call `gh issue comment {number} --repo {repo} --body-file -` yourself during the run."
  - 调用: get, _render_parent_context, _truncate

#### `ƒ` `_pr_review_comment_prompt(payload: dict[str, Any]) -> str`  L101
  - 分支数 0，函数体节点数 197；return: f"A new review comment was posted on pull request #{number} in {repo}.\n\n{parent_block}\nReview comment:\n  Author: {author}\n  File: {path}:{line}\n\n  Diff context:\n```\n{diff_hunk}\n```\n\n  Body:\n{body or '(empty comment)'}\n\nDecide what action (if any) to take in response to this review comment, in the context of the parent pull request above. Your final assistant message is for the run log only — it will NOT be posted to GitHub. If you want to reply, call `gh pr comment {number} --repo {repo} --body-file -` yourself during the run."
  - 调用: get, _render_parent_context, _truncate

#### `ƒ` `_pr_review_prompt(payload: dict[str, Any]) -> str`  L127
  - 分支数 1，函数体节点数 204；return: f"A pull request review was submitted on #{number} in {repo}.\n\n{parent_block}\nReview:\n  Reviewer: {author}\n  State: {state}\n\n  Body:\n{body or '(no review body)'}\n\n{fetch_hint}Decide what action (if any) to take in response to this review, in the context of the parent pull request above. Your final assistant message is for the run log only — it will NOT be posted to GitHub. If you want to reply (or push a fix), call `gh pr comment {number} --repo {repo} --body-file -` (and the usual `git clone` / `gh pr checkout` / `git push` flow for code changes) yourself during the run."
  - 调用: get, _render_parent_context, _truncate

#### `ƒ` `_issues_prompt(payload: dict[str, Any]) -> str`  L170
  - 分支数 0，函数体节点数 164；return: f"An issue was {action} on {repo}:\n\n  #{number} {title}\n  Author: {author}\n  URL: {url}\n\nDescription:\n{body or '(no description)'}\n\nDecide what action (if any) to take for this issue and carry it out. Your final assistant message is for the run log only — it will NOT be posted to GitHub. If you want to reply on the issue (or open a PR), call `gh issue comment {number} --repo {repo} --body-file -` / `gh pr create` yourself during the run."
  - 调用: get, _truncate

#### `ƒ` `_ping_prompt(payload: dict[str, Any]) -> str`  L193
  - 分支数 0，函数体节点数 54；return: f'GitHub sent a ping event. zen={zen!r} hook_id={hook_id}\n\nNo action required.'
  - 调用: get

#### `ƒ` `build_prompt(event: str, payload: dict[str, Any]) -> str`  L211
  - _文档首行_（仅供参考）: Return the prompt string for a webhook delivery.
  - 分支数 1，函数体节点数 79；return: f"GitHub event {event!r} fired on {repo}. action={payload.get('action')!r}", builder(payload)
  - 调用: get, builder

## 文件内调用关系
- `_pull_request_prompt` -> _truncate
- `_render_parent_context` -> _truncate
- `_issue_comment_prompt` -> _render_parent_context, _truncate
- `_pr_review_comment_prompt` -> _render_parent_context, _truncate
- `_pr_review_prompt` -> _render_parent_context, _truncate
- `_issues_prompt` -> _truncate
