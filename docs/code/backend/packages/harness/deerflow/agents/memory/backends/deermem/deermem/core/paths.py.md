# `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/paths.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/paths.py`  ·  行数: 96

**模块文档首行**（仅供参考）: DeerMem's own storage path resolution (no deer-flow ``get_paths`` / ``AGENT_NAME_PATTERN``).

## 模块概览
- 函数 4 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: hashlib, os, re
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> TYPE_CHECKING

## 模块级常量
- `_SAFE_USER_ID_RE` = re.compile('^[A-Za-z0-9_\\-]+$')
- `_UNSAFE_USER_ID_CHAR_RE` = re.compile('[^A-Za-z0-9_\\-]')
- `_SAFE_USER_ID_DIGEST_HEX_LEN` = 16
- `AGENT_NAME_PATTERN` = re.compile('^[A-Za-z0-9-]+$')

## 函数
#### `ƒ` `safe_user_id(raw: str) -> str`  L36
  - _文档首行_（仅供参考）: Normalize an external identity into the user-id charset (``[A-Za-z0-9_-]``).
  - 分支数 2，函数体节点数 71；raise: ValueError('user_id must be a non-empty string.')；return: raw, f'{sanitized}-{digest}'
  - 调用: ValueError, sub, hexdigest, sha256, encode

#### `ƒ` `validate_agent_name(name: str) -> None`  L53
  - _文档首行_（仅供参考）: Validate that the agent name is safe to use in filesystem paths.
  - 分支数 2，函数体节点数 43；raise: ValueError('Agent name must be a non-empty string.'), ValueError(f'Invalid agent name {name!r}: names must match {AGENT_NAME_PATTERN.pattern}')
  - 调用: ValueError, match

#### `ƒ` `_default_root() -> Path`  L61
  - _文档首行_（仅供参考）: DeerMem's default data root: ``$DEERMEM_DATA_DIR`` or ``~/.deermem/``.
  - 分支数 1，函数体节点数 35；return: Path(env), Path.home() / '.deermem'
  - 调用: get, Path, home

#### `ƒ` `memory_file_path(config: DeerMemConfig, agent_name: str | None, *, user_id: str | None) -> Path`  L69
  - _文档首行_（仅供参考）: Resolve the memory file path under DeerMem's own data root.
  - 分支数 3，函数体节点数 137；return: root / 'users' / uid / 'agents' / agent_name.lower() / 'memory.json', root / 'users' / uid / 'memory.json', root / 'agents' / agent_name.lower() / 'memory.json', root / 'memory.json'
  - 调用: Path, _default_root, safe_user_id, validate_agent_name, lower

## 文件内调用关系
- `memory_file_path` -> _default_root, safe_user_id, validate_agent_name
