# `backend/app/channels/runtime_config_store.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/runtime_config_store.py`  ·  行数: 158

**模块文档首行**（仅供参考）: Local persistence for runtime IM channel configuration.

## 模块概览
- 函数 4 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: json, logging, tempfile, threading
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> Any

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `RUNTIME_CHANNEL_DISABLED_FLAG` = '_runtime_disabled'

## 函数
#### `ƒ` `_provider_enabled(channel_connections_config: Any, provider: str) -> bool`  L101
  - 分支数 0，函数体节点数 32；return: bool(getattr(provider_config, 'enabled', False))
  - 调用: getattr, bool
  - 反射: getattr (L102), getattr (L103)

#### `ƒ` `_runtime_channel_disconnected(runtime_config: dict[str, Any]) -> bool`  L106
  - 分支数 0，函数体节点数 37；return: runtime_config.get(RUNTIME_CHANNEL_DISABLED_FLAG) is True and runtime_config.get('enabled') is False
  - 调用: get

#### `ƒ` `merge_runtime_channel_configs(channels_config: dict[str, Any], channel_connections_config: Any, *, store: ChannelRuntimeConfigStore | None) -> None`  L110
  - _文档首行_（仅供参考）: Merge persisted runtime provider config into ``channels_config`` in-place.
  - 分支数 4，函数体节点数 140；return: None
  - 调用: getattr, ChannelRuntimeConfigStore, items, load_all, _provider_enabled, _runtime_channel_disconnected, pop, get, isinstance, dict, update
  - 反射: getattr (L117)

#### `ƒ` `apply_runtime_connection_config(channel_connections_config: Any, *, store: ChannelRuntimeConfigStore | None) -> Any`  L133
  - _文档首行_（仅供参考）: Apply persisted connection metadata that lives outside ``channels``.
  - 分支数 3，函数体节点数 125；return: channel_connections_config, config
  - 调用: getattr, ChannelRuntimeConfigStore, get_provider_config, isinstance, strip, str, get, _provider_enabled, model_copy
  - 反射: getattr (L144)

## 类
### 类 `ChannelRuntimeConfigStore`  L17
- _文档首行_: JSON-backed store for channel credentials entered from the UI.
- 方法:
  #### `m` `__init__(self, path: str | Path | None) -> None`  L25
    - 分支数 1，函数体节点数 102
    - 调用: Path, get_paths, mkdir, _load, Lock
  - 文件IO: mkdir (L31)
  #### `m` `_load(self) -> dict[str, dict[str, Any]]`  L35
    - 分支数 3，函数体节点数 110；return: {}, {str(name): dict(value) for name, value in raw.items() if isinstance(value, dict)}
    - 调用: exists, loads, read_text, warning, isinstance, str, dict, items
  - 文件IO: exists (L36), read_text (L38)
  #### `m` `_save(self) -> None`  L46
    - 分支数 3，函数体节点数 141；raise: bare raise
    - 调用: NamedTemporaryFile, chmod, Path, debug, dump, close, replace, unlink
  - 文件IO: chmod (L55), replace (L60), chmod (L62), unlink (L67)
  #### `m` `load_all(self) -> dict[str, dict[str, Any]]`  L70
    - 分支数 1，函数体节点数 50；return: {name: dict(config) for name, config in self._data.items()}
    - 调用: dict, items
  #### `m` `get_provider_config(self, provider: str) -> dict[str, Any] | None`  L74
    - 分支数 1，函数体节点数 52；return: dict(config) if isinstance(config, dict) else None
    - 调用: get, isinstance, dict
  #### `m` `set_provider_config(self, provider: str, config: dict[str, Any]) -> None`  L79
    - 分支数 1，函数体节点数 44
    - 调用: dict, _save
  #### `m` `set_provider_disconnected(self, provider: str) -> None`  L84
    - 分支数 1，函数体节点数 34
    - 调用: _save
  #### `m` `remove_provider_config(self, provider: str) -> bool`  L92
    - 分支数 2，函数体节点数 42；return: False, True
    - 调用: _save

## 文件内调用关系
- `merge_runtime_channel_configs` -> load_all, _provider_enabled, _runtime_channel_disconnected
- `apply_runtime_connection_config` -> get_provider_config, _provider_enabled
- `ChannelRuntimeConfigStore.__init__` -> _load
- `ChannelRuntimeConfigStore.set_provider_config` -> _save
- `ChannelRuntimeConfigStore.set_provider_disconnected` -> _save
- `ChannelRuntimeConfigStore.remove_provider_config` -> _save
