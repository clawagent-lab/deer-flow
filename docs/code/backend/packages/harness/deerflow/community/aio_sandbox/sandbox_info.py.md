# `backend/packages/harness/deerflow/community/aio_sandbox/sandbox_info.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/aio_sandbox/sandbox_info.py`  ·  行数: 42

**模块文档首行**（仅供参考）: Sandbox metadata for cross-process discovery and state persistence.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: time
- `__future__` -> annotations
- `dataclasses` -> dataclass, field

## 类
### 类 `SandboxInfo`  L10  @dataclass
- _文档首行_: Persisted sandbox metadata that enables cross-process discovery.
- 类/实例变量:
  - `sandbox_id` = <annotated>
  - `sandbox_url` = <annotated>
  - `container_name` = None
  - `container_id` = None
  - `created_at` = field(default_factory=time.time)
- 方法:
  #### `cls` `from_dict(cls, data: dict) -> SandboxInfo`    @classmethod  L34
    - 分支数 0，函数体节点数 60；return: cls(sandbox_id=data['sandbox_id'], sandbox_url=data.get('sandbox_url', data.get('base_url', '')), container_name=data.get('container_name'), container_id=data.get('container_id'), created_at=data.get('created_at', time.time()))
    - 调用: cls, get, time
  #### `m` `to_dict(self) -> dict`  L24
    - 分支数 0，函数体节点数 32；return: {'sandbox_id': self.sandbox_id, 'sandbox_url': self.sandbox_url, 'container_name': self.container_name, 'container_id': self.container_id, 'created_at': self.created_at}

## 文件内调用关系
_无文件内调用_
