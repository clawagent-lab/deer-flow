# `backend/packages/harness/deerflow/skills/review/renderer.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/review/renderer.py`  ·  行数: 203

**模块文档首行**（仅供参考）: Report finalization and localized Markdown rendering.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 5 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `typing` -> Any, Literal
- `deerflow.skills.review.models` -> REPORT_SCHEMA_VERSION

## 模块级常量
- `Readiness` = Literal['blocked', 'revise', 'publish_candidate']
- `Assurance` = Literal['static_only', 'trigger_checked', 'behavior_verif...
- `Locale` = Literal['en', 'zh']
- `_READINESS_LABELS` = {'en': {'blocked': 'Not ready', 'revise': 'Needs revision...
- `_ASSURANCE_LABELS` = {'en': {'static_only': 'Static review only', 'trigger_che...

## 函数
#### `ƒ` `readiness_from_facts(facts: dict[str, Any], *, scope: list[str] | None) -> Readiness`  L43
  - 分支数 3，函数体节点数 97；return: 'blocked', 'revise', 'publish_candidate'
  - 调用: get, int

#### `ƒ` `build_static_report(facts: dict[str, Any], *, scope: list[str] | None, reviewer_model: str, completed_at: str | None) -> dict[str, Any]`  L54
  - _文档首行_（仅供参考）: Create a valid review-report.v1 with deterministic facts only.
  - 分支数 3，函数体节点数 388；return: {'schema_version': REPORT_SCHEMA_VERSION, 'subject': {'display_ref': facts.get('subject', {}).get('display_ref'), 'package_digest': facts.get('subject', {}).get('package_digest')}, 'review': {'scope': scope, 'profile': facts.get('profile', 'deerflow'), 'facts_schema_version': facts.get('schema_version'), 'reviewer_model': reviewer_model, 'completed_at': completed_at or datetime.now(UTC).replace(microsecond=0).isoformat().replace('+00:00', 'Z')}, 'readiness': readiness, 'assurance': 'static_only', 'dimensions': dimensions, 'issues': issues, 'evidence': {'facts_complete': not facts.get('completeness', {}).get('truncated'), 'runtime_runs': [], 'baseline': None, 'retained_artifacts': [], 'limitations': limitations}, 'recommended_actions': _recommended_actions(facts, readiness)}
  - 调用: readiness_from_facts, _semantic_severity, get, enumerate, _dimensions_from_facts, append, replace, isoformat, now, _recommended_actions
  - 文件IO: replace (L99), replace (L99)

#### `ƒ` `render_report_markdown(report: dict[str, Any], facts: dict[str, Any] | None, *, locale: Locale) -> str`  L116
  - 分支数 9，函数体节点数 574；return: '\n'.join(lines).rstrip() + '\n'
  - 调用: get, join, extend, append, rstrip

#### `ƒ` `_semantic_severity(severity: Any) -> str`  L171
  - 分支数 2，函数体节点数 25；return: 'blocker', 'major', 'minor'

#### `ƒ` `_dimensions_from_facts(facts: dict[str, Any]) -> list[dict[str, Any]]`  L179
  - 分支数 0，函数体节点数 141；return: [{'id': 'structure', 'status': status, 'summary': f"{summary.get('blockers', 0)} blocker(s), {summary.get('errors', 0)} error(s), {summary.get('warnings', 0)} warning(s)"}, {'id': 'evidence_quality', 'status': 'concern' if facts.get('evals', {}).get('case_count', 0) == 0 else 'pass', 'summary': f"{facts.get('evals', {}).get('case_count', 0)} eval case(s) detected"}]
  - 调用: get

#### `ƒ` `_recommended_actions(facts: dict[str, Any], readiness: str) -> list[str]`  L196
  - 分支数 2，函数体节点数 82；return: [], actions
  - 调用: get, append

## 文件内调用关系
- `build_static_report` -> readiness_from_facts, _semantic_severity, _dimensions_from_facts, _recommended_actions
