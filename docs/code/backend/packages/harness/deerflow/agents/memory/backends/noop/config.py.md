# `backend/packages/harness/deerflow/agents/memory/backends/noop/config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/backends/noop/config.py`  ·  行数: 92

**模块文档首行**（仅供参考）: Noop backend config -- TEMPLATE for parsing ``backend_config``.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Callable
- `dataclasses` -> dataclass
- `typing` -> Any

## 类
### 类 `NoopConfig`  L46  @dataclass
- _文档首行_: Parsed config for the noop backend (template -- noop ignores all fields).
- 类/实例变量:
  - `storage_path` = ''
  - `example_option` = 'default'
  - `tracing_callback` = None
  - `should_keep_hidden_message` = None
- 方法:
  #### `cls` `from_backend_config(cls, backend_config: dict[str, Any] | None) -> NoopConfig`    @classmethod  L72
    - _文档首行_（仅供参考）: Build a config from the ``backend_config`` dict.
    - 分支数 0，函数体节点数 76；return: cls(storage_path=str(cfg.get('storage_path') or ''), example_option=str(cfg.get('example_option', 'default')), tracing_callback=cfg.get('tracing_callback'), should_keep_hidden_message=cfg.get('should_keep_hidden_message'))
    - 调用: dict, cls, str, get

## 文件内调用关系
_无文件内调用_
