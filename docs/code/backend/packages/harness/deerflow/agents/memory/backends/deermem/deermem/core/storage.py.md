# `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/storage.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/storage.py`  ·  行数: 202

**模块文档首行**（仅供参考）: Memory storage providers.

## 模块概览
- 函数 3 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: abc, json, logging, threading, uuid
- `datetime` -> UTC, datetime
- `pathlib` -> Path
- `typing` -> Any
- `..config` -> DeerMemConfig
- `.paths` -> memory_file_path

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `utc_now_iso_z() -> str`  L18
  - _文档首行_（仅供参考）: Current UTC time as ISO-8601 with ``Z`` suffix (matches prior naive-UTC output).
  - 分支数 0，函数体节点数 24；return: datetime.now(UTC).isoformat().removesuffix('+00:00') + 'Z'
  - 调用: removesuffix, isoformat, now

#### `ƒ` `create_empty_memory() -> dict[str, Any]`  L23
  - _文档首行_（仅供参考）: Create an empty memory structure.
  - 分支数 0，函数体节点数 65；return: {'version': '1.0', 'lastUpdated': utc_now_iso_z(), 'user': {'workContext': {'summary': '', 'updatedAt': ''}, 'personalContext': {'summary': '', 'updatedAt': ''}, 'topOfMind': {'summary': '', 'updatedAt': ''}}, 'history': {'recentMonths': {'summary': '', 'updatedAt': ''}, 'earlierContext': {'summary': '', 'updatedAt': ''}, 'longTermBackground': {'summary': '', 'updatedAt': ''}}, 'facts': []}
  - 调用: utc_now_iso_z

#### `ƒ` `create_storage(config: DeerMemConfig) -> MemoryStorage`  L165
  - _文档首行_（仅供参考）: Build the configured memory storage instance for ``config``.
  - 分支数 4，函数体节点数 132；raise: TypeError(f"Configured memory storage '{storage_class_path}' is not a class: {storage_class!r}"), TypeError(f"Configured memory storage '{storage_class_path}' is not a subclass of MemoryStorage"), ValueError(f'backend_config.storage_class={storage_class_path!r} failed to load: {e}. Refusing to silently fall back to FileMemoryStorage - memory is persistent state, so a wrong store is a silent data-integrity footgun (a misspelled class path would otherwise write every fact to local JSON instead of the intended backend).')；return: FileMemoryStorage(config), storage_class(config)
  - 调用: FileMemoryStorage, rsplit, import_module, getattr, isinstance, TypeError, issubclass, storage_class, ValueError
  - 反射: import_module (L184), getattr (L185)

## 类
### 类 `MemoryStorage`  L42
- 继承: abc.ABC
- 含 abstractmethod（抽象基类）
- _文档首行_: Abstract base class for memory storage providers.
- 方法:
  #### `m` `load(self, agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`    @abc.abstractmethod  L46
    - _文档首行_（仅供参考）: Load memory data for the given agent.
    - 分支数 0，函数体节点数 34
  #### `m` `reload(self, agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`    @abc.abstractmethod  L51
    - _文档首行_（仅供参考）: Force reload memory data for the given agent.
    - 分支数 0，函数体节点数 34
  #### `m` `save(self, memory_data: dict[str, Any], agent_name: str | None, *, user_id: str | None) -> bool`    @abc.abstractmethod  L56
    - _文档首行_（仅供参考）: Save memory data for the given agent.
    - 分支数 0，函数体节点数 37

### 类 `FileMemoryStorage`  L61
- 继承: MemoryStorage
- _文档首行_: File-based memory storage provider.
- 方法:
  #### `st` `_cache_key(agent_name: str | None, *, user_id: str | None) -> tuple[str | None, str | None]`    @staticmethod  L93
    - 分支数 0，函数体节点数 41；return: (user_id, agent_name)
  #### `m` `__init__(self, config: DeerMemConfig)`  L64
    - _文档首行_（仅供参考）: Initialize the file memory storage with an injected DeerMemConfig.
    - 分支数 0，函数体节点数 74
    - 调用: Lock
  #### `m` `_get_memory_file_path(self, agent_name: str | None, *, user_id: str | None) -> Path`  L73
    - _文档首行_（仅供参考）: Get the path to the memory file (DeerMem's own path resolution).
    - 分支数 0，函数体节点数 34；return: memory_file_path(self._config, agent_name, user_id=user_id)
    - 调用: memory_file_path
  #### `m` `_load_memory_from_file(self, agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`  L77
    - _文档首行_（仅供参考）: Load memory data from file.
    - 分支数 3，函数体节点数 101；return: create_empty_memory(), data
    - 调用: _get_memory_file_path, exists, create_empty_memory, open, load, warning
  - 文件IO: exists (L81), open (L85)
  #### `m` `load(self, agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`  L96
    - _文档首行_（仅供参考）: Load memory data (cached with file modification time check).
    - 分支数 4，函数体节点数 158；return: cached[0], memory_data
    - 调用: _get_memory_file_path, _cache_key, exists, stat, get, _load_memory_from_file
  - 文件IO: exists (L102), stat (L102)
  #### `m` `reload(self, agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`  L118
    - _文档首行_（仅供参考）: Reload memory data from file, forcing cache invalidation.
    - 分支数 2，函数体节点数 117；return: memory_data
    - 调用: _get_memory_file_path, _load_memory_from_file, _cache_key, exists, stat
  - 文件IO: exists (L125), stat (L125)
  #### `m` `save(self, memory_data: dict[str, Any], agent_name: str | None, *, user_id: str | None) -> bool`  L133
    - _文档首行_（仅供参考）: Save memory data to file and update cache.
    - 分支数 4，函数体节点数 198；return: True, False
    - 调用: _get_memory_file_path, _cache_key, mkdir, utc_now_iso_z, with_suffix, uuid4, open, dump, replace, stat, info, error
  - 文件IO: mkdir (L139), open (L146), replace (L149), stat (L152)

## 文件内调用关系
- `create_empty_memory` -> utc_now_iso_z
- `FileMemoryStorage._load_memory_from_file` -> _get_memory_file_path, create_empty_memory, load
- `FileMemoryStorage.load` -> _get_memory_file_path, _cache_key, _load_memory_from_file
- `FileMemoryStorage.reload` -> _get_memory_file_path, _load_memory_from_file, _cache_key
- `FileMemoryStorage.save` -> _get_memory_file_path, _cache_key, utc_now_iso_z
