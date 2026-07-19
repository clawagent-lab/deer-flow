# `backend/packages/harness/deerflow/community/aio_sandbox/remote_backend.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/aio_sandbox/remote_backend.py`  ·  行数: 233

**模块文档首行**（仅供参考）: Remote sandbox backend — delegates Pod lifecycle to the provisioner service.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: logging, requests
- `__future__` -> annotations
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.skills.storage` -> user_should_see_legacy_skills
- `.backend` -> SandboxBackend
- `.sandbox_info` -> SandboxInfo

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `RemoteSandboxBackend`  L33
- 继承: SandboxBackend
- _文档首行_: Backend that delegates sandbox lifecycle to the provisioner service.
- 方法:
  #### `prop` `provisioner_url(self) -> str`    @property  L60
    - 分支数 0，函数体节点数 12；return: self._provisioner_url
  #### `m` `__init__(self, provisioner_url: str, api_key: str)`  L47
    - _文档首行_（仅供参考）: Initialize with the provisioner service URL and optional API key.
    - 分支数 0，函数体节点数 30
    - 调用: rstrip
  #### `m` `_auth_headers(self) -> dict[str, str]`  L63
    - 分支数 0，函数体节点数 26；return: {'X-API-Key': self._api_key} if self._api_key else {}
  #### `m` `create(self, thread_id: str | None, sandbox_id: str, extra_mounts: list[tuple[str, str, bool]] | None, *, user_id: str | None) -> SandboxInfo`  L68
    - _文档首行_（仅供参考）: Create a sandbox Pod + Service via the provisioner.
    - 分支数 0，函数体节点数 59；return: self._provisioner_create(thread_id, sandbox_id, extra_mounts, user_id=user_id)
    - 调用: _provisioner_create
  #### `m` `destroy(self, info: SandboxInfo) -> None`  L83
    - _文档首行_（仅供参考）: Destroy a sandbox Pod + Service via the provisioner.
    - 分支数 0，函数体节点数 19
    - 调用: _provisioner_destroy
  #### `m` `is_alive(self, info: SandboxInfo) -> bool`  L87
    - _文档首行_（仅供参考）: Check whether the sandbox Pod is running.
    - 分支数 0，函数体节点数 20；return: self._provisioner_is_alive(info.sandbox_id)
    - 调用: _provisioner_is_alive
  #### `m` `discover(self, sandbox_id: str) -> SandboxInfo | None`  L91
    - _文档首行_（仅供参考）: Discover an existing sandbox via the provisioner.
    - 分支数 0，函数体节点数 21；return: self._provisioner_discover(sandbox_id)
    - 调用: _provisioner_discover
  #### `m` `list_running(self) -> list[SandboxInfo]`  L99
    - _文档首行_（仅供参考）: Return all sandboxes currently managed by the provisioner.
    - 分支数 0，函数体节点数 17；return: self._provisioner_list()
    - 调用: _provisioner_list
  #### `m` `_provisioner_list(self) -> list[SandboxInfo]`  L113
    - _文档首行_（仅供参考）: GET /api/sandboxes → list all running sandboxes.
    - 分支数 6，函数体节点数 235；return: [], infos
    - 调用: get, _auth_headers, raise_for_status, json, isinstance, warning, type, append, SandboxInfo, info, len
  - 网络调用: get (L116)
  #### `m` `_provisioner_create(self, thread_id: str | None, sandbox_id: str, extra_mounts: list[tuple[str, str, bool]] | None, *, user_id: str | None) -> SandboxInfo`  L145
    - _文档首行_（仅供参考）: POST /api/sandboxes → create Pod + Service.
    - 分支数 1，函数体节点数 179；raise: RuntimeError(f'Provisioner create failed: {exc}')；return: SandboxInfo(sandbox_id=sandbox_id, sandbox_url=data['sandbox_url'])
    - 调用: get_effective_user_id, user_should_see_legacy_skills, post, _auth_headers, raise_for_status, json, info, SandboxInfo, error, RuntimeError
  - 网络调用: post (L158)
  #### `m` `_provisioner_destroy(self, sandbox_id: str) -> None`  L180
    - _文档首行_（仅供参考）: DELETE /api/sandboxes/{sandbox_id} → destroy Pod + Service.
    - 分支数 2，函数体节点数 91
    - 调用: delete, _auth_headers, info, warning
  - 网络调用: delete (L183)
  #### `m` `_provisioner_is_alive(self, sandbox_id: str) -> bool`  L195
    - _文档首行_（仅供参考）: GET /api/sandboxes/{sandbox_id} → check Pod phase.
    - 分支数 3，函数体节点数 113；raise: RuntimeError(f'Provisioner health check failed for {sandbox_id}: {exc}'), RuntimeError(f'Provisioner health check failed for {sandbox_id}: HTTP {resp.status_code} {resp.text}')；return: False, data.get('status') == 'Running'
    - 调用: get, _auth_headers, RuntimeError, json
  - 网络调用: get (L198)
  #### `m` `_provisioner_discover(self, sandbox_id: str) -> SandboxInfo | None`  L214
    - _文档首行_（仅供参考）: GET /api/sandboxes/{sandbox_id} → discover existing sandbox.
    - 分支数 2，函数体节点数 99；return: None, SandboxInfo(sandbox_id=sandbox_id, sandbox_url=data['sandbox_url'])
    - 调用: get, _auth_headers, raise_for_status, json, SandboxInfo, debug
  - 网络调用: get (L217)

## 文件内调用关系
- `RemoteSandboxBackend.create` -> _provisioner_create
- `RemoteSandboxBackend.destroy` -> _provisioner_destroy
- `RemoteSandboxBackend.is_alive` -> _provisioner_is_alive
- `RemoteSandboxBackend.discover` -> _provisioner_discover
- `RemoteSandboxBackend.list_running` -> _provisioner_list
- `RemoteSandboxBackend._provisioner_list` -> _auth_headers
- `RemoteSandboxBackend._provisioner_create` -> _auth_headers
- `RemoteSandboxBackend._provisioner_destroy` -> _auth_headers
- `RemoteSandboxBackend._provisioner_is_alive` -> _auth_headers
- `RemoteSandboxBackend._provisioner_discover` -> _auth_headers
