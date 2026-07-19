# `backend/scripts/migrate_user_isolation.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/scripts/migrate_user_isolation.py`  ·  行数: 340

**模块文档首行**（仅供参考）: One-time migration: move legacy thread dirs, memory, agents, and skills into per-user layout.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: argparse, logging, shutil
- `deerflow.config.paths` -> Paths, get_paths

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `migrate_thread_dirs(paths: Paths, thread_owner_map: dict[str, str], *, dry_run: bool) -> list[dict]`  L18
  - _文档首行_（仅供参考）: Move legacy thread directories into per-user layout.
  - 分支数 7，函数体节点数 307；return: report
  - 调用: exists, info, sorted, iterdir, is_dir, get, mkdir, move, str, warning, append, any, rmdir
  - 文件IO: exists (L36), iterdir (L40), exists (L49), mkdir (L53), mkdir (L59), exists (L66), iterdir (L66), rmdir (L67)

#### `ƒ` `migrate_agents(paths: Paths, user_id: str, *, dry_run: bool) -> list[dict]`  L72
  - _文档首行_（仅供参考）: Move legacy custom-agent directories into per-user layout.
  - 分支数 7，函数体节点数 280；return: report
  - 调用: exists, info, sorted, iterdir, is_dir, user_agent_dir, mkdir, move, str, warning, append, any, rmdir
  - 文件IO: exists (L98), iterdir (L102), exists (L110), mkdir (L114), mkdir (L120), exists (L127), iterdir (L127), rmdir (L128)

#### `ƒ` `migrate_skills(paths: Paths, user_id: str, *, dry_run: bool) -> list[dict]`  L133
  - _文档首行_（仅供参考）: Move legacy global custom skills into per-user layout.
  - 分支数 12，函数体节点数 434；return: report
  - 调用: exists, info, user_custom_skills_dir, is_dir, warning, mkdir, move, str, sorted, iterdir, startswith, append, any, rmdir
  - 文件IO: exists (L159), exists (L167), exists (L169), mkdir (L173), mkdir (L178), iterdir (L181), exists (L192), mkdir (L196), mkdir (L202), exists (L209), iterdir (L209), rmdir (L210)

#### `ƒ` `migrate_memory(paths: Paths, user_id: str, *, dry_run: bool) -> None`  L215
  - _文档首行_（仅供参考）: Move legacy global memory.json into per-user layout.
  - 分支数 4，函数体节点数 135；return: None
  - 调用: exists, info, user_memory_file, warning, rename, mkdir, move, str
  - 文件IO: exists (L229), exists (L234), rename (L238), mkdir (L243)

#### `ƒ` `_build_owner_map_from_db(paths: Paths) -> dict[str, str]`  L247
  - _文档首行_（仅供参考）: Query threads_meta table for thread_id -> user_id mapping.
  - 分支数 2，函数体节点数 113；return: {}, {row[0]: row[1] for row in cursor.fetchall()}
  - 调用: exists, info, connect, str, execute, fetchall, warning, close
  - 文件IO: exists (L255)

#### `ƒ` `main() -> None`  L270
  - 分支数 10，函数体节点数 405
  - 调用: ArgumentParser, add_argument, parse_args, basicConfig, get_paths, info, _build_owner_map_from_db, len, migrate_thread_dirs, migrate_memory, migrate_agents, migrate_skills, warning

## 文件内调用关系
- `main` -> _build_owner_map_from_db, migrate_thread_dirs, migrate_memory, migrate_agents, migrate_skills
