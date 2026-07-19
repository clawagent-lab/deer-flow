# `backend/packages/harness/deerflow/skills/catalog.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/catalog.py`  ·  行数: 103

**模块文档首行**（仅供参考）: Skill catalog — deferred skill discovery at runtime.

## 模块概览
- 函数 2 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: logging, re
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `functools` -> cached_property
- `deerflow.skills.types` -> Skill

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `MAX_RESULTS` = 5

## 函数
#### `ƒ` `_compile_catalog_regex(pattern: str) -> re.Pattern[str]`  L26
  - _文档首行_（仅供参考）: Compile ``pattern`` case-insensitively, falling back to literal match.
  - 分支数 1，函数体节点数 50；return: re.compile(pattern, re.IGNORECASE), re.compile(re.escape(pattern), re.IGNORECASE)
  - 调用: compile, escape
  - 危险执行: compile (L33), compile (L35)

#### `ƒ` `_catalog_regex_score(pattern: re.Pattern[str], s: Skill) -> int`  L100
  - _文档首行_（仅供参考）: Count regex hits across name + description for ranking.
  - 分支数 0，函数体节点数 42；return: len(pattern.findall(f"{s.name} {s.description or ''}"))
  - 调用: len, findall

## 类
### 类 `SkillCatalog`  L42  @dataclass(...)
- _文档首行_: Immutable catalog of skills.  Pure search, no mutation.
- 类/实例变量:
  - `skills` = <annotated>
- 方法:
  #### `m` `names(self) -> frozenset[str]`    @cached_property  L55
    - _文档首行_（仅供参考）: All skill names in insertion order.
    - 分支数 0，函数体节点数 29；return: frozenset((s.name for s in self.skills))
    - 调用: frozenset
  #### `m` `search(self, query: str) -> list[Skill]`  L59
    - _文档首行_（仅供参考）: Match *query* against skill names and descriptions.
    - 分支数 7，函数体节点数 306；return: [], [s for s in self.skills if s.name in wanted], candidates[:MAX_RESULTS], [s for _, s in scored][:MAX_RESULTS]
    - 调用: strip, startswith, split, lower, len, _compile_catalog_regex, sort, _catalog_regex_score, search, append

## 文件内调用关系
- `SkillCatalog.search` -> _compile_catalog_regex, _catalog_regex_score, search
