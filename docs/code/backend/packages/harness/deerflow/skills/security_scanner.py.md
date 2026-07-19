# `backend/packages/harness/deerflow/skills/security_scanner.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/security_scanner.py`  ·  行数: 130

**模块文档首行**（仅供参考）: Security screening for agent-managed skill writes.

## 模块概览
- 函数 3 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: json, logging, re
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> Any
- `deerflow.config` -> get_app_config
- `deerflow.config.app_config` -> AppConfig
- `deerflow.models` -> create_chat_model
- `deerflow.skills.types` -> SKILL_MD_FILE

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_extract_json_object(raw: str) -> dict | None`  L25
  - 分支数 12，函数体节点数 209；return: json.loads(raw), None, json.loads(raw[start:i + 1])
  - 调用: strip, match, group, loads, find, range, len

#### `ƒ` `_format_static_findings_context(static_findings: list[dict[str, Any]]) -> str`  L71
  - 分支数 3，函数体节点数 133；return: 'None.', '\n'.join(lines)
  - 调用: get, append, join

#### `⏵ƒ` `async scan_skill_content(content: str, *, executable: bool, location: str, app_config: AppConfig | None, static_findings: list[dict[str, Any]] | None) -> ScanResult`  L83
  - _文档首行_（仅供参考）: Screen skill content before it is written to disk.
  - 分支数 5，函数体节点数 281；return: ScanResult(decision, str(parsed.get('reason') or 'No reason provided.')), ScanResult('block', 'Security scan produced unparseable output; manual review required.'), ScanResult('block', 'Security scan unavailable for executable content; manual review required.'), ScanResult('block', 'Security scan unavailable for skill content; manual review required.')
  - 调用: lower, str, _format_static_findings_context, get_app_config, create_chat_model, ainvoke, getattr, _extract_json_object, get, ScanResult, warning
  - 反射: getattr (L115)

## 类
### 类 `ScanResult`  L20  @dataclass(...)
- 类/实例变量:
  - `decision` = <annotated>
  - `reason` = <annotated>

## 文件内调用关系
- `scan_skill_content` -> _format_static_findings_context, _extract_json_object
