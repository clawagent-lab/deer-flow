# `backend/packages/harness/deerflow/utils/network.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/utils/network.py`  ·  行数: 140

**模块文档首行**（仅供参考）: Thread-safe network utilities.

## 模块概览
- 函数 2 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: socket, threading
- `contextlib` -> contextmanager

## 模块级常量
- `_global_port_allocator` = PortAllocator()

## 函数
#### `ƒ` `get_free_port(start_port: int, max_range: int) -> int`  L113
  - _文档首行_（仅供参考）: Get a free port in a thread-safe manner.
  - 分支数 0，函数体节点数 24；return: _global_port_allocator.allocate(start_port, max_range)
  - 调用: allocate

#### `ƒ` `release_port(port: int) -> None`  L133
  - _文档首行_（仅供参考）: Release a previously allocated port.
  - 分支数 0，函数体节点数 16
  - 调用: release

## 类
### 类 `PortAllocator`  L8
- _文档首行_: Thread-safe port allocator that prevents port conflicts in concurrent environments.
- 方法:
  #### `m` `__init__(self)`  L31
    - 分支数 0，函数体节点数 27
    - 调用: Lock, set
  #### `m` `_is_port_available(self, port: int) -> bool`  L35
    - _文档首行_（仅供参考）: Check if a port is available for binding.
    - 分支数 3，函数体节点数 57；return: False, True
    - 调用: socket, bind
  - 网络调用: socket (L51)
  #### `m` `allocate(self, start_port: int, max_range: int) -> int`  L58
    - _文档首行_（仅供参考）: Allocate an available port in a thread-safe manner.
    - 分支数 3，函数体节点数 73；raise: RuntimeError(f'No available port found in range {start_port}-{start_port + max_range}')；return: port
    - 调用: range, _is_port_available, add, RuntimeError
  #### `m` `release(self, port: int) -> None`  L82
    - _文档首行_（仅供参考）: Release a previously allocated port.
    - 分支数 1，函数体节点数 25
    - 调用: discard
  #### `m` `allocate_context(self, start_port: int, max_range: int)`    @contextmanager  L92
    - _文档首行_（仅供参考）: Context manager for port allocation with automatic release.
    - 分支数 1，函数体节点数 40；生成器（yield）
    - 调用: allocate, release

## 文件内调用关系
- `get_free_port` -> allocate
- `release_port` -> release
- `PortAllocator.allocate` -> _is_port_available
- `PortAllocator.allocate_context` -> allocate, release
