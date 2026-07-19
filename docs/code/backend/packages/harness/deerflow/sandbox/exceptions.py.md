# `backend/packages/harness/deerflow/sandbox/exceptions.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/exceptions.py`  ·  行数: 72

**模块文档首行**（仅供参考）: Sandbox-related exceptions with structured error information.

## 模块概览
- 函数 0 个，类 7 个，模块级常量 0 个

## 类
### 类 `SandboxError`  L4
- 继承: Exception
- _文档首行_: Base exception for all sandbox-related errors.
- 方法:
  #### `m` `__init__(self, message: str, details: dict | None)`  L7
    - 分支数 0，函数体节点数 39
    - 调用: __init__, super
  #### `m` `__str__(self) -> str`  L12
    - 分支数 1，函数体节点数 57；return: f'{self.message} ({detail_str})', self.message
    - 调用: join, items

### 类 `SandboxNotFoundError`  L19
- 继承: SandboxError
- _文档首行_: Raised when a sandbox cannot be found or is not available.
- 方法:
  #### `m` `__init__(self, message: str, sandbox_id: str | None)`  L22
    - 分支数 0，函数体节点数 43
    - 调用: __init__, super

### 类 `SandboxRuntimeError`  L28
- 继承: SandboxError
- _文档首行_: Raised when sandbox runtime is not available or misconfigured.

### 类 `SandboxCommandError`  L34
- 继承: SandboxError
- _文档首行_: Raised when a command execution fails in the sandbox.
- 方法:
  #### `m` `__init__(self, message: str, command: str | None, exit_code: int | None)`  L37
    - 分支数 2，函数体节点数 92
    - 调用: len, __init__, super

### 类 `SandboxFileError`  L48
- 继承: SandboxError
- _文档首行_: Raised when a file operation fails in the sandbox.
- 方法:
  #### `m` `__init__(self, message: str, path: str | None, operation: str | None)`  L51
    - 分支数 2，函数体节点数 71
    - 调用: __init__, super

### 类 `SandboxPermissionError`  L62
- 继承: SandboxFileError
- _文档首行_: Raised when a permission error occurs during file operations.

### 类 `SandboxFileNotFoundError`  L68
- 继承: SandboxFileError
- _文档首行_: Raised when a file or directory is not found.

## 文件内调用关系
- `SandboxError.__init__` -> __init__
- `SandboxNotFoundError.__init__` -> __init__
- `SandboxCommandError.__init__` -> __init__
- `SandboxFileError.__init__` -> __init__
