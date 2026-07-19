# `backend/packages/harness/deerflow/sandbox/sandbox.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/sandbox.py`  ·  行数: 176

## 模块概览
- 函数 1 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: re
- `abc` -> ABC, abstractmethod
- `deerflow.sandbox.search` -> GrepMatch

## 模块级常量
- `_ENV_NAME_PATTERN` = re.compile('^[A-Za-z_][A-Za-z0-9_]*$')

## 函数
#### `ƒ` `_validate_extra_env(extra_env: dict[str, str] | None) -> None`  L17
  - _文档首行_（仅供参考）: Reject ``env`` keys that are not valid POSIX env-var names.
  - 分支数 3，函数体节点数 61；raise: ValueError(f'extra_env key {key!r} is not a valid POSIX environment variable name (must match ^[A-Za-z_][A-Za-z0-9_]*$). This protects shell-using sandbox implementations from command injection via the key.')；return: None
  - 调用: isinstance, fullmatch, ValueError

## 类
### 类 `Sandbox`  L44
- 继承: ABC
- 含 abstractmethod（抽象基类）
- _文档首行_: Abstract base class for sandbox environments
- 类/实例变量:
  - `_id` = <annotated>
- 方法:
  #### `prop` `id(self) -> str`    @property  L53
    - 分支数 0，函数体节点数 12；return: self._id
  #### `m` `__init__(self, id: str)`  L49
    - 分支数 0，函数体节点数 13
  #### `m` `execute_command(self, command: str, env: dict[str, str] | None, timeout: float | None) -> str`    @abstractmethod  L57
    - _文档首行_（仅供参考）: Execute bash command in sandbox.
    - 分支数 0，函数体节点数 35
  #### `m` `read_file(self, path: str) -> str`    @abstractmethod  L94
    - _文档首行_（仅供参考）: Read the content of a file.
    - 分支数 0，函数体节点数 13
  #### `m` `download_file(self, path: str) -> bytes`    @abstractmethod  L106
    - _文档首行_（仅供参考）: Download the binary content of a file.
    - 分支数 0，函数体节点数 13
  #### `m` `list_dir(self, path: str, max_depth) -> list[str]`    @abstractmethod  L125
    - _文档首行_（仅供参考）: List the contents of a directory.
    - 分支数 0，函数体节点数 19
  #### `m` `write_file(self, path: str, content: str, append: bool) -> None`    @abstractmethod  L138
    - _文档首行_（仅供参考）: Write content to a file.
    - 分支数 0，函数体节点数 19
  #### `m` `glob(self, path: str, pattern: str, *, include_dirs: bool, max_results: int) -> tuple[list[str], bool]`    @abstractmethod  L149
    - _文档首行_（仅供参考）: Find paths that match a glob pattern under a root directory.
    - 分支数 0，函数体节点数 36
  #### `m` `grep(self, path: str, pattern: str, *, glob: str | None, literal: bool, case_sensitive: bool, max_results: int) -> tuple[list[GrepMatch], bool]`    @abstractmethod  L154
    - _文档首行_（仅供参考）: Search for matches inside text files under a directory.
    - 分支数 0，函数体节点数 47
  #### `m` `update_file(self, path: str, content: bytes) -> None`    @abstractmethod  L168
    - _文档首行_（仅供参考）: Update a file with binary content.
    - 分支数 0，函数体节点数 15

## 文件内调用关系
_无文件内调用_
