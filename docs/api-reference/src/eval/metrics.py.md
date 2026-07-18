# `src/eval/metrics.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/eval/metrics.py`
- **模块导入名**：`src.eval.metrics`
- **代码行数**：229
- **架构归属**：src/eval —— 报告评估：自动化指标（字数/引用/章节覆盖）+ LLM-as-Judge 综合评分

## 模块概述

```text
Automated metrics for report quality evaluation.

These metrics can be computed without LLM calls, providing fast and
deterministic quality assessment.
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from dataclasses import dataclass, field`
- `from typing import Dict, List, Optional`
- `from urllib.parse import urlparse`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `ReportMetrics` | 18 | `` |
| 常量 | `REPORT_STYLE_SECTIONS` | 53 | `{'default': ['title', 'key_points', 'overview', 'detailed_analysis', 'key_citations'], 'academic'...` |
| 常量 | `SECTION_PATTERNS` | 104 | `{'title': '^#\\s+.+', 'key_points': '(?:key\\s*points\|要点\|关键发现\|核心观点)', 'overview': '(?:overview...` |
| 函数 | `count_words` | 119 | `(text: str) -> int` |
| 函数 | `count_citations` | 126 | `(text: str) -> int` |
| 函数 | `extract_domains` | 132 | `(text: str) -> List[str]` |
| 函数 | `count_images` | 149 | `(text: str) -> int` |
| 函数 | `detect_sections` | 155 | `(text: str, report_style: str='default') -> Dict[str, bool]` |
| 函数 | `compute_metrics` | 176 | `(report: str, report_style: str='default', target_word_count: Optional[int]=None) -> ReportMetrics` |
| 函数 | `get_word_count_target` | 219 | `(report_style: str) -> Dict[str, int]` |

## 符号详解

### `ReportMetrics`

- **类型**：类  |  **行号**：18–49  |  **完整限定名**：`src.eval.metrics.ReportMetrics`
- **装饰器**：`@dataclass`
- **定义**：

```python
class ReportMetrics:
```
- **成员概览**：

  - `attr word_count`
  - `attr citation_count`
  - `attr unique_sources`
  - `attr image_count`
  - `attr section_count`
  - `attr sections_found`
  - `attr sections_missing`
  - `attr section_coverage_score`
  - `attr has_title`
  - `attr has_key_points`
  - `attr has_overview`
  - `attr has_citations_section`
  - `def to_dict`

**摘要**：

Container for computed report metrics.

### `REPORT_STYLE_SECTIONS`

- **类型**：模块常量  |  **行号**：53–101  |  **完整限定名**：`src.eval.metrics.REPORT_STYLE_SECTIONS`
- **值**：

```python
REPORT_STYLE_SECTIONS = {'default': ['title', 'key_points', 'overview', 'detailed_analysis', 'key_citations'], 'academic': ['title', 'key_poi...
```

**说明**（自动推断）：

章节定义常量 `REPORT_STYLE_SECTIONS`，列出报告应包含的章节顺序与名称。

### `SECTION_PATTERNS`

- **类型**：模块常量  |  **行号**：104–116  |  **完整限定名**：`src.eval.metrics.SECTION_PATTERNS`
- **值**：

```python
SECTION_PATTERNS = {'title': '^#\\s+.+', 'key_points': '(?:key\\s*points|要点|关键发现|核心观点)', 'overview': '(?:overview|概述|简介|背景)', 'detailed_...
```

**说明**（自动推断）：

正则模式常量 `SECTION_PATTERNS`，用于文本匹配或抽取。

### `count_words`

- **类型**：函数  |  **行号**：119–123  |  **完整限定名**：`src.eval.metrics.count_words`
- **签名**：

```python
def count_words(text: str) -> int:
```

**摘要**：

Count words in text, handling both English and Chinese.

### `count_citations`

- **类型**：函数  |  **行号**：126–129  |  **完整限定名**：`src.eval.metrics.count_citations`
- **签名**：

```python
def count_citations(text: str) -> int:
```

**摘要**：

Count markdown-style citations [text](url).

### `extract_domains`

- **类型**：函数  |  **行号**：132–146  |  **完整限定名**：`src.eval.metrics.extract_domains`
- **签名**：

```python
def extract_domains(text: str) -> List[str]:
```

**摘要**：

Extract unique domains from URLs in the text.

### `count_images`

- **类型**：函数  |  **行号**：149–152  |  **完整限定名**：`src.eval.metrics.count_images`
- **签名**：

```python
def count_images(text: str) -> int:
```

**摘要**：

Count markdown images ![alt](url).

### `detect_sections`

- **类型**：函数  |  **行号**：155–173  |  **完整限定名**：`src.eval.metrics.detect_sections`
- **签名**：

```python
def detect_sections(text: str, report_style: str='default') -> Dict[str, bool]:
```

**摘要**：

Detect which sections are present in the report.

### `compute_metrics`

- **类型**：函数  |  **行号**：176–216  |  **完整限定名**：`src.eval.metrics.compute_metrics`
- **签名**：

```python
def compute_metrics(report: str, report_style: str='default', target_word_count: Optional[int]=None) -> ReportMetrics:
```

**摘要**：

Compute automated metrics for a report.

**参数**：

```text
report: The report text in markdown format
    report_style: The style of report (academic, news, etc.)
    target_word_count: Optional target word count for compliance check
```

**返回值**：

```text
ReportMetrics object with computed values
```

### `get_word_count_target`

- **类型**：函数  |  **行号**：219–229  |  **完整限定名**：`src.eval.metrics.get_word_count_target`
- **签名**：

```python
def get_word_count_target(report_style: str) -> Dict[str, int]:
```

**摘要**：

Get target word count range for a report style.

## 调用关系（下游）

**被以下模块导入**：

- `src.eval`
- `src.eval.evaluator`
- `tests.unit.eval.test_evaluator`
- `tests.unit.eval.test_metrics`

## 示例用法

```python
from src.eval.metrics import count_words
#
# TODO: 结合业务场景补充 count_words 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
