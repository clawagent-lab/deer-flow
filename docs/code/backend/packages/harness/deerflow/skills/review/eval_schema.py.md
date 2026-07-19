# `backend/packages/harness/deerflow/skills/review/eval_schema.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/review/eval_schema.py`  ·  行数: 106

**模块文档首行**（仅供参考）: Eval-manifest adapters for deterministic skill review facts.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: json
- `__future__` -> annotations
- `typing` -> Any
- `deerflow.skills.review.models` -> make_finding

## 函数
#### `ƒ` `analyze_eval_manifests(snapshot: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]`  L11
  - 分支数 5，函数体节点数 384；return: (aggregate, findings)
  - 调用: str, get, sorted, startswith, endswith, set, append, make_finding, loads, _classify_manifest, add, len, next, iter

#### `ƒ` `_classify_manifest(payload: Any) -> dict[str, Any]`  L72
  - 分支数 4，函数体节点数 130；return: _case_stats('versioned', cases), {'schema': 'versioned', 'valid': True, 'case_count': 0, 'positive_trigger_cases': 0, 'negative_trigger_cases': 0}, _case_stats('skill-creator-evals', payload['evals']), _case_stats('trigger-eval-list', payload), {'schema': 'unknown', 'valid': True, 'case_count': 0, 'positive_trigger_cases': 0, 'negative_trigger_cases': 0}
  - 调用: isinstance, get, _case_stats

#### `ƒ` `_case_stats(schema: str, cases: list[Any]) -> dict[str, Any]`  L88
  - 分支数 4，函数体节点数 96；return: {'schema': schema, 'valid': True, 'case_count': len(cases), 'positive_trigger_cases': positive, 'negative_trigger_cases': negative}
  - 调用: isinstance, get, len

## 文件内调用关系
- `analyze_eval_manifests` -> _classify_manifest
- `_classify_manifest` -> _case_stats
