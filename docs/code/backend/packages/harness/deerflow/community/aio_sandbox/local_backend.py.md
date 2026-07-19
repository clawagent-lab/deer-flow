# `backend/packages/harness/deerflow/community/aio_sandbox/local_backend.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/aio_sandbox/local_backend.py`  ·  行数: 670

**模块文档首行**（仅供参考）: Local container backend for sandbox provisioning.

## 模块概览
- 函数 10 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: json, logging, os, shlex, subprocess
- `__future__` -> annotations
- `datetime` -> datetime
- `deerflow.utils.network` -> get_free_port, release_port
- `.backend` -> SandboxBackend, wait_for_sandbox_ready
- `.sandbox_info` -> SandboxInfo

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_parse_docker_timestamp(raw: str) -> float`  L24
  - _文档首行_（仅供参考）: Parse Docker's ISO 8601 timestamp into a Unix epoch float.
  - 分支数 5，函数体节点数 180；return: 0.0, datetime.fromisoformat(s).timestamp()
  - 调用: strip, index, len, isdigit, endswith, timestamp, fromisoformat, debug

#### `ƒ` `_extract_host_port(inspect_entry: dict, container_port: int) -> int | None`  L53
  - _文档首行_（仅供参考）: Extract the host port mapped to ``container_port/tcp`` from a docker inspect entry.
  - 分支数 3，函数体节点数 88；return: int(host_port), None
  - 调用: get, int

#### `ƒ` `_format_container_mount(runtime: str, host_path: str, container_path: str, read_only: bool) -> list[str]`  L70
  - _文档首行_（仅供参考）: Format a bind-mount argument for the selected runtime.
  - 分支数 3，函数体节点数 79；return: ['--mount', mount_spec], ['-v', mount_spec]

#### `ƒ` `_redact_container_command_for_log(cmd: list[str]) -> list[str]`  L90
  - _文档首行_（仅供参考）: Return a Docker/Container command with environment values redacted.
  - 分支数 6，函数体节点数 179；return: redacted
  - 调用: split, append, startswith, removeprefix

#### `ƒ` `_format_container_command_for_log(cmd: list[str]) -> str`  L124
  - 分支数 1，函数体节点数 35；return: subprocess.list2cmdline(cmd), shlex.join(cmd)
  - 调用: list2cmdline, join

#### `ƒ` `_normalize_sandbox_host(host: str) -> str`  L130
  - 分支数 0，函数体节点数 16；return: host.strip().lower()
  - 调用: lower, strip

#### `ƒ` `_is_ipv6_loopback_sandbox_host(host: str) -> bool`  L134
  - 分支数 0，函数体节点数 18；return: _normalize_sandbox_host(host) in {'::1', '[::1]'}
  - 调用: _normalize_sandbox_host

#### `ƒ` `_is_loopback_sandbox_host(host: str) -> bool`  L138
  - 分支数 0，函数体节点数 21；return: _normalize_sandbox_host(host) in {'', 'localhost', '127.0.0.1', '::1', '[::1]'}
  - 调用: _normalize_sandbox_host

#### `ƒ` `_resolve_docker_bind_host(sandbox_host: str | None, bind_host: str | None) -> str`  L142
  - _文档首行_（仅供参考）: Choose the host interface for legacy Docker ``-p`` sandbox publishing.
  - 分支数 4，函数体节点数 127；return: explicit_bind, '[::1]', '127.0.0.1', '0.0.0.0'
  - 调用: get, strip, debug, _is_ipv6_loopback_sandbox_host, _is_loopback_sandbox_host

#### `ƒ` `_is_no_such_container_error(stderr: str, container_name: str) -> bool`  L172
  - _文档首行_（仅供参考）: Return True only when stderr definitively says the container does not exist.
  - 分支数 2，函数体节点数 65；return: True, False, container_name.lower() in message or 'container' in message or 'object' in message
  - 调用: lower

## 类
### 类 `LocalContainerBackend`  L190
- 继承: SandboxBackend
- _文档首行_: Backend that manages sandbox containers locally using Docker or Apple Container.
- 方法:
  #### `prop` `runtime(self) -> str`    @property  L229
    - _文档首行_（仅供参考）: The detected container runtime ("docker" or "container").
    - 分支数 0，函数体节点数 14；return: self._runtime
  #### `m` `__init__(self, *, image: str, base_port: int, container_prefix: str, config_mounts: list, environment: dict[str, str])`  L203
    - _文档首行_（仅供参考）: Initialize the local container backend.
    - 分支数 0，函数体节点数 73
    - 调用: _detect_runtime
  #### `m` `_detect_runtime(self) -> str`  L233
    - _文档首行_（仅供参考）: Detect which container runtime to use.
    - 分支数 2，函数体节点数 79；return: 'container', 'docker'
    - 调用: system, run, info, strip
  - 子进程: run (L246)
  #### `m` `create(self, thread_id: str | None, sandbox_id: str, extra_mounts: list[tuple[str, str, bool]] | None, *, user_id: str | None) -> SandboxInfo`  L262
    - _文档首行_（仅供参考）: Start a new container and return its connection info.
    - 分支数 5，函数体节点数 258；raise: bare raise, RuntimeError('Could not start sandbox container: all candidate ports are already allocated by Docker')；return: existing, SandboxInfo(sandbox_id=sandbox_id, sandbox_url=f'http://{sandbox_host}:{port}', container_name=container_name, container_id=container_id)
    - 调用: range, get_free_port, _start_container, release_port, str, lower, warning, discover, RuntimeError, get, SandboxInfo
  #### `m` `destroy(self, info: SandboxInfo) -> None`  L332
    - _文档首行_（仅供参考）: Stop the container and release its port.
    - 分支数 3，函数体节点数 61
    - 调用: _stop_container, urlparse, release_port
  #### `m` `is_alive(self, info: SandboxInfo) -> bool`  L350
    - _文档首行_（仅供参考）: Check if the container is still running (lightweight, no HTTP).
    - 分支数 1，函数体节点数 27；return: self._is_container_running(info.container_name), False
    - 调用: _is_container_running
  #### `m` `discover(self, sandbox_id: str) -> SandboxInfo | None`  L356
    - _文档首行_（仅供参考）: Discover an existing container by its deterministic name.
    - 分支数 4，函数体节点数 131；return: None, SandboxInfo(sandbox_id=sandbox_id, sandbox_url=sandbox_url, container_name=container_name)
    - 调用: _is_container_running, warning, _get_container_port, get, wait_for_sandbox_ready, SandboxInfo
  #### `m` `list_running(self) -> list[SandboxInfo]`  L398
    - _文档首行_（仅供参考）: Enumerate all running containers matching the configured prefix.
    - 分支数 6，函数体节点数 312；return: [], infos
    - 调用: run, strip, warning, splitlines, startswith, _batch_inspect, get, len, append, SandboxInfo, info
  - 子进程: run (L416)
  #### `m` `_batch_inspect(self, container_names: list[str]) -> dict[str, tuple[float, int | None]]`  L475
    - _文档首行_（仅供参考）: Batch-inspect containers in a single subprocess call.
    - 分支数 6，函数体节点数 261；return: {}, out
    - 调用: run, warning, strip, loads, lstrip, get, _parse_docker_timestamp, _extract_host_port
  - 子进程: run (L484)
  #### `m` `_start_container(self, container_name: str, port: int, extra_mounts: list[tuple[str, str, bool]] | None) -> str`  L523
    - _文档首行_（仅供参考）: Start a new container.
    - 分支数 7，函数体节点数 327；raise: RuntimeError(f'Failed to start sandbox container: {e.stderr}')；return: container_id
    - 调用: extend, _resolve_docker_bind_host, items, _format_container_mount, append, _format_container_command_for_log, _redact_container_command_for_log, info, run, strip, error, RuntimeError
  - 子进程: run (L597)
  #### `m` `_stop_container(self, container_id: str) -> None`  L605
    - _文档首行_（仅供参考）: Stop a container (--rm ensures automatic removal).
    - 分支数 1，函数体节点数 70
    - 调用: run, info, warning
  - 子进程: run (L608)
  #### `m` `_is_container_running(self, container_name: str) -> bool`  L618
    - _文档首行_（仅供参考）: Check if a named container is currently running.
    - 分支数 3，函数体节点数 104；raise: RuntimeError(f'Timed out checking container {container_name}'), RuntimeError(f'Failed to inspect container {container_name}: {result.stderr.strip()}')；return: result.stdout.strip().lower() == 'true', False
    - 调用: run, RuntimeError, lower, strip, _is_no_such_container_error
  - 子进程: run (L632)
  #### `m` `_get_container_port(self, container_name: str) -> int | None`  L647
    - _文档首行_（仅供参考）: Get the host port of a running container.
    - 分支数 2，函数体节点数 96；return: int(port_str), None
    - 调用: run, strip, split, int
  - 子进程: run (L657)

## 文件内调用关系
- `_is_ipv6_loopback_sandbox_host` -> _normalize_sandbox_host
- `_is_loopback_sandbox_host` -> _normalize_sandbox_host
- `_resolve_docker_bind_host` -> _is_ipv6_loopback_sandbox_host, _is_loopback_sandbox_host
- `LocalContainerBackend.__init__` -> _detect_runtime
- `LocalContainerBackend.create` -> _start_container, discover
- `LocalContainerBackend.destroy` -> _stop_container
- `LocalContainerBackend.is_alive` -> _is_container_running
- `LocalContainerBackend.discover` -> _is_container_running, _get_container_port
- `LocalContainerBackend.list_running` -> _batch_inspect
- `LocalContainerBackend._batch_inspect` -> _parse_docker_timestamp, _extract_host_port
- `LocalContainerBackend._start_container` -> _resolve_docker_bind_host, _format_container_mount, _format_container_command_for_log, _redact_container_command_for_log
- `LocalContainerBackend._is_container_running` -> _is_no_such_container_error
