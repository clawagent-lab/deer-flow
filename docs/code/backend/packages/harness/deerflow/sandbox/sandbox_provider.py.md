# `backend/packages/harness/deerflow/sandbox/sandbox_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/sandbox_provider.py`  ·  行数: 171

## 模块概览
- 函数 4 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, threading
- `abc` -> ABC, abstractmethod
- `deerflow.config` -> get_app_config
- `deerflow.reflection` -> resolve_class
- `deerflow.sandbox.sandbox` -> Sandbox

## 模块级常量
- `_default_sandbox_provider` = None
- `_provider_lock` = threading.Lock()

## 函数
#### `ƒ` `get_sandbox_provider(**kwargs) -> SandboxProvider`  L76
  - _文档首行_（仅供参考）: Get the sandbox provider singleton.
  - 分支数 5，函数体节点数 89；可变参数（*args/**kwargs）；return: _default_sandbox_provider, provider, winner
  - 调用: get_app_config, resolve_class, cls, hasattr, shutdown
  - 反射: hasattr (L110)

#### `ƒ` `reset_sandbox_provider() -> None`  L115
  - _文档首行_（仅供参考）: Reset the sandbox provider singleton.
  - 分支数 2，函数体节点数 31
  - 调用: reset

#### `ƒ` `shutdown_sandbox_provider() -> None`  L140
  - _文档首行_（仅供参考）: Shutdown and reset the sandbox provider.
  - 分支数 2，函数体节点数 39
  - 调用: hasattr, shutdown
  - 反射: hasattr (L153)

#### `ƒ` `set_sandbox_provider(provider: SandboxProvider) -> None`  L157
  - _文档首行_（仅供参考）: Set a custom sandbox provider instance.
  - 分支数 1，函数体节点数 18

## 类
### 类 `SandboxProvider`  L10
- 继承: ABC
- 含 abstractmethod（抽象基类）
- _文档首行_: Abstract base class for sandbox providers
- 类/实例变量:
  - `uses_thread_data_mounts` = False
  - `needs_upload_permission_adjustment` = True
- 方法:
  #### `m` `acquire(self, thread_id: str | None, *, user_id: str | None) -> str`    @abstractmethod  L17
    - _文档首行_（仅供参考）: Acquire a sandbox environment and return its ID.
    - 分支数 0，函数体节点数 24
  #### `m` `get(self, sandbox_id: str) -> Sandbox | None`    @abstractmethod  L36
    - _文档首行_（仅供参考）: Get a sandbox environment by ID.
    - 分支数 0，函数体节点数 16
  #### `m` `release(self, sandbox_id: str) -> None`    @abstractmethod  L45
    - _文档首行_（仅供参考）: Release a sandbox environment.
    - 分支数 0，函数体节点数 12
  #### `m` `reset(self) -> None`  L53
    - _文档首行_（仅供参考）: Clear cached state that survives provider instance replacement.
    - 分支数 0，函数体节点数 7
  #### `⏵m` `async acquire_async(self, thread_id: str | None, *, user_id: str | None) -> str`  L25
    - _文档首行_（仅供参考）: Acquire a sandbox without blocking the event loop.
    - 分支数 0，函数体节点数 37；return: await asyncio.to_thread(self.acquire, thread_id, user_id=user_id)
    - 调用: to_thread

## 文件内调用关系
- `reset_sandbox_provider` -> reset
