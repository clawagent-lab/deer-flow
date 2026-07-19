# `backend/packages/harness/deerflow/tui/input_history.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/input_history.py`  ·  行数: 59

**模块文档首行**（仅供参考）: Bounded composer input history with up/down navigation (pure).

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations

## 模块级常量
- `DEFAULT_LIMIT` = 200

## 类
### 类 `InputHistory`  L13
- 方法:
  #### `m` `__init__(self, entries: list[str] | None, limit: int) -> None`  L14
    - 分支数 0，函数体节点数 79
    - 调用: max, list
  #### `m` `entries(self) -> list[str]`  L20
    - 分支数 0，函数体节点数 17；return: list(self._entries)
    - 调用: list
  #### `m` `add(self, text: str) -> None`  L23
    - _文档首行_（仅供参考）: Record a submitted entry. Ignores blank and consecutive-duplicate lines.
    - 分支数 3，函数体节点数 93；return: None
    - 调用: strip, append, len
  #### `m` `up(self, draft: str) -> str`  L35
    - _文档首行_（仅供参考）: Move one entry older. Returns the entry (or ``draft`` if empty).
    - 分支数 3，函数体节点数 77；return: draft, self._entries[self._cursor]
    - 调用: len
  #### `m` `down(self) -> str`  L46
    - _文档首行_（仅供参考）: Move one entry newer. Past the newest entry, restores the draft.
    - 分支数 2，函数体节点数 66；return: self._draft, self._entries[self._cursor]
    - 调用: len
  #### `m` `reset(self) -> None`  L56
    - 分支数 0，函数体节点数 16

## 文件内调用关系
_无文件内调用_
