# `backend/packages/harness/deerflow/logging_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/logging_config.py`  ·  行数: 110

**模块文档首行**（仅供参考）: Logging setup helpers for DeerFlow.

## 模块概览
- 函数 7 个，类 3 个，模块级常量 4 个

## 依赖（import）
- 模块: json, logging
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `typing` -> Any
- `deerflow.config.app_config` -> apply_logging_level
- `deerflow.trace_context` -> get_current_trace_id

## 模块级常量
- `DEFAULT_LOG_DATE_FORMAT` = '%Y-%m-%d %H:%M:%S'
- `DEFAULT_LOG_FORMAT` = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
- `TRACE_TEXT_LOG_FORMAT` = '%(asctime)s - %(name)s - %(levelname)s - [trace_id=%(tra...
- `_TRACE_FILTER_NAME` = 'deerflow_trace_context_filter'

## 函数
#### `ƒ` `_ensure_root_handler() -> None`  L57
  - 分支数 1，函数体节点数 28；return: None
  - 调用: basicConfig

#### `ƒ` `_has_trace_filter(handler: logging.Handler) -> bool`  L63
  - 分支数 0，函数体节点数 41；return: any((getattr(f, 'name', None) == _TRACE_FILTER_NAME or isinstance(f, TraceContextFilter) for f in handler.filters))
  - 调用: any, getattr, isinstance
  - 反射: getattr (L64)

#### `ƒ` `_install_trace_filter(handler: logging.Handler) -> None`  L67
  - 分支数 1，函数体节点数 25
  - 调用: _has_trace_filter, addFilter, TraceContextFilter

#### `ƒ` `_remove_trace_filter(handler: logging.Handler) -> None`  L72
  - 分支数 0，函数体节点数 45
  - 调用: getattr, isinstance
  - 反射: getattr (L73)

#### `ƒ` `_default_formatter() -> logging.Formatter`  L76
  - 分支数 0，函数体节点数 17；return: logging.Formatter(DEFAULT_LOG_FORMAT, datefmt=DEFAULT_LOG_DATE_FORMAT)
  - 调用: Formatter

#### `ƒ` `_trace_formatter(format_name: str | None) -> logging.Formatter`  L80
  - 分支数 1，函数体节点数 40；return: JsonTraceFormatter(), TraceTextFormatter(TRACE_TEXT_LOG_FORMAT, datefmt=DEFAULT_LOG_DATE_FORMAT)
  - 调用: lower, strip, JsonTraceFormatter, TraceTextFormatter

#### `ƒ` `configure_logging(config: object) -> None`  L86
  - _文档首行_（仅供参考）: Configure DeerFlow logging from an AppConfig-like object.
  - 分支数 3，函数体节点数 115
  - 调用: _ensure_root_handler, getattr, bool, _install_trace_filter, setFormatter, _trace_formatter, _remove_trace_filter, _default_formatter, apply_logging_level
  - 反射: getattr (L96), getattr (L97), getattr (L98), getattr (L103), getattr (L106), getattr (L109)

## 类
### 类 `TraceContextFilter`  L19
- 继承: logging.Filter
- _文档首行_: Inject the current request trace id into every log record.
- 类/实例变量:
  - `name` = _TRACE_FILTER_NAME
- 方法:
  #### `m` `filter(self, record: logging.LogRecord) -> bool`  L24
    - 分支数 0，函数体节点数 23；return: True
    - 调用: get_current_trace_id

### 类 `JsonTraceFormatter`  L29
- 继承: logging.Formatter
- _文档首行_: Small JSON formatter used when ``logging.enhance.format=json``.
- 类/实例变量:
  - `_deerflow_trace_formatter` = True
- 方法:
  #### `m` `format(self, record: logging.LogRecord) -> str`  L34
    - 分支数 3，函数体节点数 130；return: json.dumps(payload, ensure_ascii=False)
    - 调用: hasattr, get_current_trace_id, isoformat, fromtimestamp, getMessage, formatException, formatStack, dumps
  - 反射: hasattr (L35)

### 类 `TraceTextFormatter`  L51
- 继承: logging.Formatter
- _文档首行_: Marker subclass so trace formatting can be reverted cleanly in tests.
- 类/实例变量:
  - `_deerflow_trace_formatter` = True

## 文件内调用关系
- `_install_trace_filter` -> _has_trace_filter
- `configure_logging` -> _ensure_root_handler, _install_trace_filter, _trace_formatter, _remove_trace_filter, _default_formatter
