# `backend/packages/harness/deerflow/community/warm_pool_lifecycle.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/warm_pool_lifecycle.py`  ·  行数: 128

**模块文档首行**（仅供参考）: Shared warm-pool lifecycle helpers for community sandbox providers.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 5 个
- `__all__`: DEFAULT_IDLE_TIMEOUT, DEFAULT_REPLICAS, IDLE_CHECK_INTERVAL, WarmPoolLifecycleMixin

## 依赖（import）
- 模块: logging, threading, time
- `__future__` -> annotations
- `typing` -> Any

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `DEFAULT_IDLE_TIMEOUT` = 600
- `DEFAULT_REPLICAS` = 3
- `IDLE_CHECK_INTERVAL` = 60
- `__all__` = ['DEFAULT_IDLE_TIMEOUT', 'DEFAULT_REPLICAS', 'IDLE_CHECK_...

## 类
### 类 `WarmPoolLifecycleMixin`  L17
- _文档首行_: Mixin for provider warm-pool expiry and replica lifecycle mechanics.
- 类/实例变量:
  - `DEFAULT_IDLE_TIMEOUT` = DEFAULT_IDLE_TIMEOUT
  - `DEFAULT_REPLICAS` = DEFAULT_REPLICAS
  - `IDLE_CHECK_INTERVAL` = IDLE_CHECK_INTERVAL
  - `_idle_checker_thread_name` = 'warm-pool-idle-checker'
  - `_lock` = <annotated>
  - `_warm_pool` = <annotated>
  - `_config` = <annotated>
  - `_idle_checker_stop` = <annotated>
  - `_idle_checker_thread` = <annotated>
- 方法:
  #### `m` `_active_count_locked(self) -> int`  L31
    - _文档首行_（仅供参考）: Return active entry count while ``_lock`` is held.
    - 分支数 0，函数体节点数 10；raise: NotImplementedError
  #### `m` `_destroy_warm_entry(self, sandbox_id: str, entry: WarmEntryT, *, reason: str) -> None`  L35
    - _文档首行_（仅供参考）: Destroy a warm-pool entry after it has been removed from the pool.
    - 分支数 0，函数体节点数 18；raise: NotImplementedError
  #### `m` `_replica_count(self) -> tuple[int, int]`  L39
    - _文档首行_（仅供参考）: Return configured replicas and current active + warm entry count.
    - 分支数 1，函数体节点数 61；return: (replicas, total)
    - 调用: int, get, _active_count_locked, len
  #### `m` `_log_replicas_soft_cap(self, replicas: int, sandbox_id: str, evicted: str | None) -> None`  L46
    - _文档首行_（仅供参考）: Log the result of enforcing the warm-pool replica soft cap.
    - 分支数 1，函数体节点数 47；return: None
    - 调用: info, warning
  #### `m` `_evict_oldest_warm(self) -> str | None`  L58
    - _文档首行_（仅供参考）: Remove and destroy the oldest warm entry by timestamp.
    - 分支数 2，函数体节点数 83；return: None, sandbox_id
    - 调用: min, items, pop, _destroy_warm_entry
  #### `m` `_reap_expired_warm(self, idle_timeout: float | None) -> None`  L69
    - _文档首行_（仅供参考）: Remove and destroy warm entries older than ``idle_timeout`` seconds.
    - 分支数 6，函数体节点数 159；return: None
    - 调用: float, get, time, items, append, pop, _destroy_warm_entry
  #### `m` `_start_idle_checker(self) -> None`  L87
    - _文档首行_（仅供参考）: Start the daemon thread that periodically cleans idle warm entries.
    - 分支数 1，函数体节点数 79；return: None
    - 调用: is_alive, clear, Thread, start, info, get
  #### `m` `_stop_idle_checker(self) -> None`  L101
    - _文档首行_（仅供参考）: Stop the idle checker thread and wait for it to exit when running.
    - 分支数 1，函数体节点数 51
    - 调用: set, is_alive, current_thread, join
  #### `m` `_idle_checker_loop(self) -> None`  L108
    - _文档首行_（仅供参考）: Run periodic idle cleanup until the stop event is set.
    - 分支数 2，函数体节点数 55
    - 调用: float, get, wait, _cleanup_idle_resources, exception
  #### `m` `_cleanup_idle_resources(self, idle_timeout: float) -> None`  L117
    - _文档首行_（仅供参考）: Clean resources idle longer than ``idle_timeout`` seconds.
    - 分支数 0，函数体节点数 17
    - 调用: _reap_expired_warm

## 文件内调用关系
- `WarmPoolLifecycleMixin._replica_count` -> _active_count_locked
- `WarmPoolLifecycleMixin._evict_oldest_warm` -> _destroy_warm_entry
- `WarmPoolLifecycleMixin._reap_expired_warm` -> _destroy_warm_entry
- `WarmPoolLifecycleMixin._idle_checker_loop` -> _cleanup_idle_resources
- `WarmPoolLifecycleMixin._cleanup_idle_resources` -> _reap_expired_warm
