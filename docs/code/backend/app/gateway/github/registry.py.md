# `backend/app/gateway/github/registry.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/github/registry.py`  ·  行数: 248

**模块文档首行**（仅供参考）: Build the GitHub webhook → agent registry.

## 模块概览
- 函数 6 个，类 1 个，模块级常量 5 个

## 依赖（import）
- 模块: logging, threading
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `pathlib` -> Path
- `app.gateway.github.triggers` -> _resolved_trigger
- `deerflow.config.agents_config` -> AgentConfig, GitHubTriggerConfig, load_agent_config
- `deerflow.config.paths` -> get_paths
- `deerflow.runtime.user_context` -> DEFAULT_USER_ID

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_Signature` = tuple[tuple[str, str, float], ...]
- `_Registry` = dict[tuple[str, str], list[GitHubAgentMatch]]
- `_cache` = None
- `_cache_lock` = threading.Lock()

## 函数
#### `ƒ` `_discover_user_ids() -> list[str]`  L82
  - _文档首行_（仅供参考）: Return all user-id directories under ``base_dir/users/``.
  - 分支数 4，函数体节点数 107；return: [DEFAULT_USER_ID], found
  - 调用: get_paths, exists, sorted, iterdir, is_dir, append
  - 文件IO: exists (L91), iterdir (L95), exists (L96)

#### `ƒ` `_gather_agent_signature() -> tuple[_Signature, list[tuple[str, str]]]`  L103
  - _文档首行_（仅供参考）: Return (signature, [(user_id, agent_name)]) for every agent on disk.
  - 分支数 10，函数体节点数 346；return: (tuple(sig), discovered)
  - 调用: get_paths, set, _discover_user_ids, user_agents_dir, exists, sorted, iterdir, is_dir, stat, append, add, tuple
  - 文件IO: exists (L124), iterdir (L126), exists (L128), stat (L131), exists (L148), iterdir (L149), exists (L151), stat (L159)

#### `ƒ` `_rebuild(discovered: list[tuple[str, str]]) -> _Registry`  L168
  - _文档首行_（仅供参考）: Parse every agent's config.yaml and build the (repo, event) index.
  - 分支数 6，函数体节点数 158；return: index
  - 调用: load_agent_config, warning, items, _resolved_trigger, append, setdefault, GitHubAgentMatch

#### `ƒ` `build_github_agent_registry() -> _Registry`  L202
  - _文档首行_（仅供参考）: Return ``{(repo, event): [GitHubAgentMatch, ...]}`` across all users.
  - 分支数 2，函数体节点数 64；return: _cache[1], registry
  - 调用: _gather_agent_signature, _rebuild

#### `ƒ` `_invalidate_cache() -> None`  L229
  - _文档首行_（仅供参考）: Drop the cached registry. Test-only helper.
  - 分支数 1，函数体节点数 14

#### `ƒ` `lookup_agents(registry: _Registry, repo: str, event: str) -> list[GitHubAgentMatch]`  L236
  - _文档首行_（仅供参考）: Convenience: return the list of agent matches for ``(repo, event)``.
  - 分支数 0，函数体节点数 33；return: registry.get((repo, event), [])
  - 调用: get

## 类
### 类 `GitHubAgentMatch`  L46  @dataclass(...)
- _文档首行_: One ``(user, agent, _resolved_trigger)`` row in the ``(repo, event)`` index.
- 类/实例变量:
  - `user_id` = <annotated>
  - `agent` = <annotated>
  - `trigger` = <annotated>

## 文件内调用关系
- `_gather_agent_signature` -> _discover_user_ids
- `build_github_agent_registry` -> _gather_agent_signature, _rebuild
