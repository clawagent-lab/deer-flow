# `backend/packages/harness/deerflow/workspace_changes/types.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/workspace_changes/types.py`  ·  行数: 108

## 模块概览
- 函数 0 个，类 7 个，模块级常量 4 个

## 依赖（import）
- `__future__` -> annotations
- `dataclasses` -> asdict, dataclass, field
- `pathlib` -> Path
- `typing` -> Literal

## 模块级常量
- `WORKSPACE_CHANGES_EVENT_TYPE` = 'workspace_changes'
- `WORKSPACE_CHANGES_METADATA_KEY` = 'workspace_changes'
- `WorkspaceChangeStatus` = Literal['created', 'modified', 'deleted']
- `DiffUnavailableReason` = Literal['binary', 'large', 'sensitive', 'truncated']

## 类
### 类 `WorkspaceChangeLimits`  L15  @dataclass(...)
- 类/实例变量:
  - `max_files` = 200
  - `max_scanned_files` = 2000
  - `max_file_bytes_for_diff` = 256 * 1024
  - `max_total_diff_bytes` = 1024 * 1024
- 方法:
  #### `m` `to_dict(self) -> dict`  L21
    - 分支数 0，函数体节点数 11；return: asdict(self)
    - 调用: asdict

### 类 `WorkspaceRoot`  L26  @dataclass(...)
- 类/实例变量:
  - `name` = <annotated>
  - `host_path` = <annotated>
  - `virtual_prefix` = <annotated>
- 方法:
  #### `m` `__post_init__(self) -> None`  L31
    - 分支数 0，函数体节点数 37
    - 调用: __setattr__, Path, rstrip

### 类 `FileSnapshot`  L37  @dataclass(...)
- 类/实例变量:
  - `path` = <annotated>
  - `root` = <annotated>
  - `size` = <annotated>
  - `mtime_ns` = <annotated>
  - `sha256` = <annotated>
  - `binary` = False
  - `sensitive` = False
  - `text` = None
  - `text_path` = None
  - `content_unavailable_reason` = None

### 类 `WorkspaceSnapshot`  L51  @dataclass(...)
- 类/实例变量:
  - `files` = field(default_factory=dict)
  - `truncated` = False
  - `text_cache_dir` = None

### 类 `WorkspaceFileChange`  L58  @dataclass(...)
- 类/实例变量:
  - `path` = <annotated>
  - `root` = <annotated>
  - `status` = <annotated>
  - `binary` = <annotated>
  - `sensitive` = <annotated>
  - `size_before` = <annotated>
  - `size_after` = <annotated>
  - `sha256_before` = <annotated>
  - `sha256_after` = <annotated>
  - `diff` = ''
  - `diff_truncated` = False
  - `diff_unavailable_reason` = None
  - `additions` = 0
  - `deletions` = 0
- 方法:
  #### `m` `to_dict(self) -> dict`  L74
    - 分支数 0，函数体节点数 11；return: asdict(self)
    - 调用: asdict

### 类 `WorkspaceChangeSummary`  L79  @dataclass(...)
- 类/实例变量:
  - `created` = 0
  - `modified` = 0
  - `deleted` = 0
  - `additions` = 0
  - `deletions` = 0
  - `truncated` = False
- 方法:
  #### `m` `to_dict(self) -> dict`  L87
    - 分支数 0，函数体节点数 11；return: asdict(self)
    - 调用: asdict

### 类 `WorkspaceChangeResult`  L92  @dataclass(...)
- 类/实例变量:
  - `summary` = <annotated>
  - `files` = <annotated>
  - `limits` = field(default_factory=WorkspaceChangeLimits)
  - `version` = 1
- 方法:
  #### `m` `has_changes(self) -> bool`  L98
    - 分支数 0，函数体节点数 41；return: bool(self.summary.created or self.summary.modified or self.summary.deleted or self.summary.additions or self.summary.deletions)
    - 调用: bool
  #### `m` `to_dict(self) -> dict`  L101
    - 分支数 0，函数体节点数 42；return: {'version': self.version, 'summary': self.summary.to_dict(), 'files': [change.to_dict() for change in self.files], 'limits': self.limits.to_dict()}
    - 调用: to_dict

## 文件内调用关系
- `WorkspaceChangeResult.to_dict` -> to_dict
