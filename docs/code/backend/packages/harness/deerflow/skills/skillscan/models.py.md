# `backend/packages/harness/deerflow/skills/skillscan/models.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/skillscan/models.py`  ·  行数: 60

**模块文档首行**（仅供参考）: Data contracts for DeerFlow SkillScan.

## 模块概览
- 函数 0 个，类 5 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> Literal, TypedDict

## 模块级常量
- `FindingSeverity` = Literal['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']

## 类
### 类 `SecurityFinding`  L19
- 继承: TypedDict
- 类/实例变量:
  - `rule_id` = <annotated>
  - `severity` = <annotated>
  - `file` = <annotated>
  - `line` = <annotated>
  - `message` = <annotated>
  - `remediation` = <annotated>
  - `evidence` = <annotated>

### 类 `ScanResult`  L29
- 继承: TypedDict
- 类/实例变量:
  - `findings` = <annotated>
  - `blocked` = <annotated>
  - `scanner_errors` = <annotated>

### 类 `RuleSpec`  L36  @dataclass(...)
- _文档首行_: Static definition of one SkillScan rule; ``remediation`` is authored here once and copied into findings.
- 类/实例变量:
  - `rule_id` = <annotated>
  - `severity` = <annotated>
  - `message` = <annotated>
  - `remediation` = <annotated>

### 类 `StaticScannerError`  L45
- 继承: RuntimeError
- _文档首行_: Raised when SkillScan cannot evaluate its input at the package boundary.

### 类 `StaticScanBlockedError`  L49
- 继承: ValueError
- _文档首行_: Raised when deterministic findings block a skill write or install.
- 类/实例变量:
  - `findings` = <annotated>
  - `skill_name` = <annotated>
- 方法:
  #### `m` `__init__(self, findings: list[SecurityFinding], *, skill_name: str | None, message: str | None) -> None`  L55
    - 分支数 0，函数体节点数 77
    - 调用: dict, __init__, super

## 文件内调用关系
- `StaticScanBlockedError.__init__` -> __init__
