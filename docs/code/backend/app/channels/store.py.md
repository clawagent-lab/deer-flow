# `backend/app/channels/store.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/store.py`  ·  行数: 154

**模块文档首行**（仅供参考）: ChannelStore — persists IM chat-to-DeerFlow thread mappings.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: json, logging, tempfile, threading, time
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> Any

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `ChannelStore`  L16
- _文档首行_: JSON-file-backed store that maps IM conversations to DeerFlow threads.
- 方法:
  #### `st` `_key(channel_name: str, chat_id: str, topic_id: str | None) -> str`    @staticmethod  L75
    - 分支数 1，函数体节点数 44；return: f'{channel_name}:{chat_id}:{topic_id}', f'{channel_name}:{chat_id}'
  #### `m` `__init__(self, path: str | Path | None) -> None`  L36
    - 分支数 1，函数体节点数 102
    - 调用: Path, get_paths, mkdir, _load, Lock
  - 文件IO: mkdir (L42)
  #### `m` `_load(self) -> dict[str, dict[str, Any]]`  L48
    - 分支数 2，函数体节点数 67；return: json.loads(self._path.read_text(encoding='utf-8')), {}
    - 调用: exists, loads, read_text, warning
  - 文件IO: exists (L49), read_text (L51)
  #### `m` `_save(self) -> None`  L56
    - 分支数 1，函数体节点数 84；raise: bare raise
    - 调用: NamedTemporaryFile, dump, close, replace, Path, unlink
  - 文件IO: replace (L66), unlink (L69)
  #### `m` `get_thread_id(self, channel_name: str, chat_id: str, topic_id: str | None) -> str | None`  L82
    - _文档首行_（仅供参考）: Look up the DeerFlow thread_id for a given IM conversation/topic.
    - 分支数 0，函数体节点数 54；return: entry['thread_id'] if entry else None
    - 调用: get, _key
  #### `m` `set_thread_id(self, channel_name: str, chat_id: str, thread_id: str, *, topic_id: str | None, user_id: str) -> None`  L87
    - _文档首行_（仅供参考）: Create or update the mapping for an IM conversation/topic.
    - 分支数 1，函数体节点数 102
    - 调用: _key, time, get, _save
  #### `m` `remove(self, channel_name: str, chat_id: str, topic_id: str | None) -> bool`  L109
    - _文档首行_（仅供参考）: Remove a mapping.
    - 分支数 5，函数体节点数 146；return: True, False
    - 调用: _key, _save, startswith
  #### `m` `list_entries(self, channel_name: str | None) -> list[dict[str, Any]]`  L139
    - _文档首行_（仅供参考）: List all stored mappings, optionally filtered by channel.
    - 分支数 3，函数体节点数 158；return: results
    - 调用: items, split, len, append

## 文件内调用关系
- `ChannelStore.__init__` -> _load
- `ChannelStore.get_thread_id` -> _key
- `ChannelStore.set_thread_id` -> _key, _save
- `ChannelStore.remove` -> _key, _save
