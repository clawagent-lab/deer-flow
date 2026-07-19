# `backend/packages/harness/deerflow/community/aio_sandbox/backend.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/aio_sandbox/backend.py`  ·  行数: 153

**模块文档首行**（仅供参考）: Abstract base class for sandbox provisioning backends.

## 模块概览
- 函数 2 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, logging, time, httpx, requests
- `__future__` -> annotations
- `abc` -> ABC, abstractmethod
- `.sandbox_info` -> SandboxInfo

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `wait_for_sandbox_ready(sandbox_url: str, timeout: int) -> bool`  L18
  - _文档首行_（仅供参考）: Poll sandbox health endpoint until ready or timeout.
  - 分支数 3，函数体节点数 78；return: True, False
  - 调用: time, get, sleep
  - 网络调用: get (L31)

#### `⏵ƒ` `async wait_for_sandbox_ready_async(sandbox_url: str, timeout: int, poll_interval: float) -> bool`  L40
  - _文档首行_（仅供参考）: Async variant of sandbox readiness polling.
  - 分支数 6，函数体节点数 142；return: True, False
  - 调用: get_running_loop, time, AsyncClient, get, min, sleep
  - 网络调用: get (L56)

## 类
### 类 `SandboxBackend`  L68
- 继承: ABC
- 含 abstractmethod（抽象基类）
- _文档首行_: Abstract base for sandbox provisioning backends.
- 方法:
  #### `m` `create(self, thread_id: str | None, sandbox_id: str, extra_mounts: list[tuple[str, str, bool]] | None, *, user_id: str | None) -> SandboxInfo`    @abstractmethod  L77
    - _文档首行_（仅供参考）: Create/provision a new sandbox.
    - 分支数 0，函数体节点数 48
  #### `m` `destroy(self, info: SandboxInfo) -> None`    @abstractmethod  L100
    - _文档首行_（仅供参考）: Destroy/cleanup a sandbox and release its resources.
    - 分支数 0，函数体节点数 13
  #### `m` `is_alive(self, info: SandboxInfo) -> bool`    @abstractmethod  L109
    - _文档首行_（仅供参考）: Quick check whether a sandbox is still alive.
    - 分支数 0，函数体节点数 14
  #### `m` `discover(self, sandbox_id: str) -> SandboxInfo | None`    @abstractmethod  L124
    - _文档首行_（仅供参考）: Try to discover an existing sandbox by its deterministic ID.
    - 分支数 0，函数体节点数 17
  #### `m` `list_running(self) -> list[SandboxInfo]`  L138
    - _文档首行_（仅供参考）: Enumerate all running sandboxes managed by this backend.
    - 分支数 0，函数体节点数 14；return: []

## 文件内调用关系
_无文件内调用_
