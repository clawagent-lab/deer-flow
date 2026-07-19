# `backend/packages/harness/deerflow/sandbox/file_operation_lock.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/file_operation_lock.py`  ·  行数: 28

## 模块概览
- 函数 2 个，类 0 个，模块级常量 3 个

## 依赖（import）
- 模块: threading, weakref
- `deerflow.sandbox.sandbox` -> Sandbox

## 模块级常量
- `_LockKey` = tuple[str, str]
- `_FILE_OPERATION_LOCKS` = weakref.WeakValueDictionary()
- `_FILE_OPERATION_LOCKS_GUARD` = threading.Lock()

## 函数
#### `ƒ` `get_file_operation_lock_key(sandbox: Sandbox, path: str) -> tuple[str, str]`  L13
  - 分支数 1，函数体节点数 51；return: (sandbox_id, path)
  - 调用: getattr, id
  - 反射: getattr (L14)

#### `ƒ` `get_file_operation_lock(sandbox: Sandbox, path: str) -> threading.Lock`  L20
  - 分支数 2，函数体节点数 62；return: lock
  - 调用: get_file_operation_lock_key, get, Lock

## 文件内调用关系
- `get_file_operation_lock` -> get_file_operation_lock_key
