# `backend/scripts/benchmark/bench_sandbox_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/scripts/benchmark/bench_sandbox_provider.py`  ·  行数: 898

**模块文档首行**（仅供参考）: Provider-agnostic sandbox benchmark.

## 模块概览
- 函数 20 个，类 1 个，模块级常量 5 个

## 依赖（import）
- 模块: argparse, importlib, importlib.metadata, json, os, sys, threading, time, types
- `__future__` -> annotations
- `collections.abc` -> Callable
- `concurrent.futures` -> ThreadPoolExecutor, as_completed
- `contextlib` -> contextmanager
- `dataclasses` -> asdict, dataclass
- `pathlib` -> Path
- `typing` -> Any

## 模块级常量
- `WORKLOADS` = {'noop': 'true', 'python_small': 'python -c "print(sum(ra...
- `_STATE_WRITE` = 'python - <<\'PY\'\nfrom pathlib import Path\nPath("/tmp/...
- `_STATE_READ` = 'python - <<\'PY\'\nfrom pathlib import Path\nprint(Path(...
- `PROVIDER_FACTORIES` = {'boxlite': _make_boxlite_provider, 'aio-docker': _make_a...
- `_WARM_HIT_STATE` = threading.local()

## 函数
#### `ƒ` `_stub_config(sandbox_attrs: dict[str, Any] | None) -> types.SimpleNamespace`  L125
  - _文档首行_（仅供参考）: Build a stub config namespace mimicking ``get_app_config()``.
  - 分支数 0，函数体节点数 46；return: types.SimpleNamespace(sandbox=types.SimpleNamespace(**attrs))
  - 调用: SimpleNamespace

#### `ƒ` `_patched_module_attr(module_name: str, attr_name: str, value: Any)`    @contextmanager  L132
  - 分支数 1，函数体节点数 58；生成器（yield）
  - 调用: import_module, getattr, setattr
  - 反射: import_module (L133), getattr (L134), setattr (L135), setattr (L139)

#### `ƒ` `_boxlite_version() -> str | None`  L142
  - 分支数 1，函数体节点数 26；return: importlib.metadata.version('boxlite'), None
  - 调用: version

#### `ƒ` `_chmod_boxlite_shims(boxes_dir: str) -> int`  L149
  - 分支数 2，函数体节点数 61；return: fixed
  - 调用: glob, Path, stat, chmod
  - 文件IO: glob (L151), stat (L152), chmod (L155)

#### `ƒ` `_create_box_with_097_shim_workaround(create_box: Callable[[str], Any], sandbox_id: str, *, boxes_dir: str) -> Any`  L160
  - 分支数 3，函数体节点数 77；raise: RuntimeError(f'BoxLite benchmark shim workaround only supports boxlite 0.9.7; got {version!r}'), bare raise；return: create_box(sandbox_id)
  - 调用: create_box, _boxlite_version, RuntimeError, _chmod_boxlite_shims

#### `ƒ` `_make_boxlite_provider(config: dict[str, Any]) -> tuple[Any, dict[str, Any]]`  L178
  - _文档首行_（仅供参考）: Create a BoxliteProvider with stub config; returns (provider, config_used).
  - 分支数 4，函数体节点数 204；return: _create_box_with_097_shim_workaround(original_create_box, sandbox_id, boxes_dir=boxes_dir), (provider, sandbox_attrs)
  - 调用: get, _patched_module_attr, _stub_config, BoxliteProvider, expanduser, _create_box_with_097_shim_workaround, MethodType

#### `ƒ` `_make_aio_provider(config: dict[str, Any]) -> tuple[Any, dict[str, Any]]`  L220
  - _文档首行_（仅供参考）: Create an AioSandboxProvider with stub config.
  - 分支数 1，函数体节点数 128；return: (provider, sandbox_attrs)
  - 调用: get, _patched_module_attr, _stub_config, AioSandboxProvider

#### `ƒ` `_install_warm_hit_tracking(provider: Any) -> None`  L254
  - _文档首行_（仅供参考）: Record warm-pool reclaims from inside the provider acquire path.
  - 分支数 4，函数体节点数 110；return: None, result
  - 调用: getattr, _original, setattr
  - 反射: getattr (L256), getattr (L261), setattr (L271), setattr (L274)

#### `ƒ` `_reset_warm_hit_tracking() -> None`  L277
  - 分支数 0，函数体节点数 9

#### `ƒ` `_warm_hit_from_acquire() -> bool`  L281
  - 分支数 0，函数体节点数 15；return: bool(getattr(_WARM_HIT_STATE, 'value', False))
  - 调用: bool, getattr
  - 反射: getattr (L282)

#### `ƒ` `_compute_sandbox_id(provider: Any, thread_id: str, user_id: str) -> str`  L285
  - _文档首行_（仅供参考）: Compute the deterministic sandbox_id the provider would use.
  - 分支数 1，函数体节点数 58；return: provider._sandbox_id(thread_id, user_id), hashlib.sha256(f'{user_id}:{thread_id}'.encode()).hexdigest()[:8]
  - 调用: hasattr, _sandbox_id, hexdigest, sha256, encode
  - 反射: hasattr (L287)

#### `ƒ` `_was_warm_hit(provider: Any, sandbox_id: str) -> bool`  L295
  - _文档首行_（仅供参考）: Check if the sandbox_id is currently in the provider's warm pool.
  - 分支数 1，函数体节点数 27；return: sandbox_id in provider._warm_pool

#### `ƒ` `_evict_from_warm(provider: Any, sandbox_id: str) -> None`  L301
  - _文档首行_（仅供参考）: Forcibly remove and destroy a warm-pool entry (no-warmpool simulation).
  - 分支数 3，函数体节点数 56
  - 调用: pop, close

#### `ƒ` `_run_one_turn(provider: Any, provider_name: str, scenario: str, workload_name: str, command: str, iteration: int, concurrency: int, user_id: str, thread_id: str, no_warmpool: bool, state_write_turn: bool, expected_state: str | None) -> BenchResult`  L316
  - _文档首行_（仅供参考）: Execute one acquire→run→release cycle and return a BenchResult.
  - 分支数 14，函数体节点数 600；raise: RuntimeError(f'acquire returned {sid!r} but get() returned None'), RuntimeError(output), RuntimeError(f'State reuse failed: expected {expected_state!r} in output, got {output.strip()!r}')；return: BenchResult(provider=provider_name, scenario=scenario, workload=workload_name, iteration=iteration, concurrency=concurrency, thread_id=thread_id, user_id=user_id, acquire_ms=acquire_ms, run_ms=run_ms, release_ms=release_ms, total_ms=(t_f - t0) * 1000, warm_hit=warm_hit, success=True, no_warmpool=no_warmpool), BenchResult(provider=provider_name, scenario=scenario, workload=workload_name, iteration=iteration, concurrency=concurrency, thread_id=thread_id, user_id=user_id, acquire_ms=acquire_ms, run_ms=run_ms, release_ms=release_ms, total_ms=(time.perf_counter() - t0) * 1000, warm_hit=warm_hit, success=False, error=error, no_warmpool=no_warmpool)
  - 调用: perf_counter, _compute_sandbox_id, getattr, _reset_warm_hit_tracking, _was_warm_hit, acquire, _warm_hit_from_acquire, get, RuntimeError, execute_command, startswith, strip, release, _evict_from_warm, BenchResult, repr, str
  - 反射: getattr (L342)

#### `ƒ` `_run_scenario(provider: Any, provider_name: str, scenario: str, workload_name: str, iterations: int, concurrency: int, output_path: Path, no_warmpool: bool, config_used: dict[str, Any], fault_inject_after: int | None) -> list[BenchResult]`  L436
  - 分支数 20，函数体节点数 650；return: _run_one_turn(provider=provider, provider_name=provider_name, scenario=scenario, workload_name=workload_name, command=command, iteration=i, concurrency=concurrency, user_id='bench-user', thread_id=tid, no_warmpool=no_warmpool, state_write_turn=state_write, expected_state=expect_state), f'cold-{i}', 'warm-hit', f'thread-{i % max(concurrency, 4)}', f'warm-hit-{i % concurrency}', f'default-{i}', None, _run_one(i), results
  - 调用: get, max, _run_one_turn, _tid, _compute_sandbox_id, close, print, range, _run_one, append, _inject_fault, BoundedSemaphore, ThreadPoolExecutor, submit, as_completed, result, open, write, dumps, asdict
  - 文件IO: open (L548), write (L550)

#### `ƒ` `_parse_args(argv: list[str] | None) -> argparse.Namespace`  L558
  - 分支数 0，函数体节点数 234；return: p.parse_args(argv)
  - 调用: ArgumentParser, add_argument, list, parse_args

#### `ƒ` `main(argv: list[str] | None) -> int`  L652
  - 分支数 8，函数体节点数 416；raise: SystemExit('state_reuse requires --scenario warm_same_thread --concurrency 1')；return: _run_idle_timeout_scenario(provider, args, output_path, config_used), _run_replica_pressure_scenario(provider, args, output_path, config_used), 0
  - 调用: _parse_args, SystemExit, Path, factory, _install_warm_hit_tracking, exists, open, write, print, range, _run_one_turn, _run_idle_timeout_scenario, _run_replica_pressure_scenario, _run_scenario, _print_summary, shutdown
  - 文件IO: exists (L670), open (L672), write (L673)

#### `ƒ` `_run_idle_timeout_scenario(provider: Any, args: argparse.Namespace, output_path: Path, config_used: dict[str, Any]) -> int`  L731
  - _文档首行_（仅供参考）: Acquire, release, force-reap warm entries, verify re-acquire is cold.
  - 分支数 5，函数体节点数 349；return: 0
  - 调用: min, print, range, _run_one_turn, get, append, sleep, _reap_expired_warm, open, write, dumps, asdict, _print_summary
  - 文件IO: open (L795), write (L797)

#### `ƒ` `_run_replica_pressure_scenario(provider: Any, args: argparse.Namespace, output_path: Path, config_used: dict[str, Any]) -> int`  L803
  - _文档首行_（仅供参考）: Push past replicas limit to verify eviction behaviour.
  - 分支数 5，函数体节点数 289；return: 0
  - 调用: print, range, _run_one_turn, get, len, append, open, write, dumps, asdict, _print_summary
  - 文件IO: open (L850), write (L852)

#### `ƒ` `_print_summary(results: list[BenchResult], args: argparse.Namespace) -> None`  L858
  - _文档首行_（仅供参考）: Print a quick summary to stderr.
  - 分支数 3，函数体节点数 355；return: None, 0.0, sorted(arr)[idx]
  - 调用: print, max, min, len, int, sorted, _p

## 类
### 类 `BenchResult`  L68  @dataclass
- 类/实例变量:
  - `provider` = <annotated>
  - `scenario` = <annotated>
  - `workload` = <annotated>
  - `iteration` = <annotated>
  - `concurrency` = <annotated>
  - `thread_id` = <annotated>
  - `user_id` = <annotated>
  - `acquire_ms` = <annotated>
  - `run_ms` = <annotated>
  - `release_ms` = <annotated>
  - `total_ms` = <annotated>
  - `warm_hit` = None
  - `success` = True
  - `error` = None
  - `replicas` = None
  - `idle_timeout` = None
  - `health_check_skip_seconds` = None
  - `image` = None
  - `no_warmpool` = False

## 文件内调用关系
- `_create_box_with_097_shim_workaround` -> _boxlite_version, _chmod_boxlite_shims
- `_make_boxlite_provider` -> _patched_module_attr, _stub_config, _create_box_with_097_shim_workaround
- `_make_aio_provider` -> _patched_module_attr, _stub_config
- `_run_one_turn` -> _compute_sandbox_id, _reset_warm_hit_tracking, _was_warm_hit, _warm_hit_from_acquire, _evict_from_warm
- `_run_scenario` -> _run_one_turn, _compute_sandbox_id
- `main` -> _parse_args, _install_warm_hit_tracking, _run_one_turn, _run_idle_timeout_scenario, _run_replica_pressure_scenario, _run_scenario, _print_summary
- `_run_idle_timeout_scenario` -> _run_one_turn, _print_summary
- `_run_replica_pressure_scenario` -> _run_one_turn, _print_summary
