# `src/config/report_style.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/config/report_style.py`
- **模块导入名**：`src.config.report_style`
- **代码行数**：14
- **架构归属**：src/config —— 配置加载（`conf.yaml` / `.env`）、模型与工具开关、报告样式、智能体映射

## 模块概述

```text
报告样式枚举：定义最终报告支持的几种写作风格（学术、科普、新闻、社交媒体、战略投资）。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `import enum`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `ReportStyle` | 9 | `` |

## 符号详解

### `ReportStyle`

- **类型**：类  |  **行号**：9–14  |  **完整限定名**：`src.config.report_style.ReportStyle`
- **基类**：`enum.Enum`
- **定义**：

```python
class ReportStyle(enum.Enum):
```
- **成员概览**：

  - `attr ACADEMIC`
  - `attr POPULAR_SCIENCE`
  - `attr NEWS`
  - `attr SOCIAL_MEDIA`
  - `attr STRATEGIC_INVESTMENT`

**说明**（自动推断）：

枚举类型 `ReportStyle`，定义该维度可选的取值集合。

## 调用关系（下游）

**被以下模块导入**：

- `src.config.configuration`
- `src.prompt_enhancer.graph.state`
- `src.server.app`
- `src.server.chat_request`
- `tests.unit.prompt_enhancer.graph.test_enhancer_node`
- `tests.unit.prompt_enhancer.graph.test_state`
- `tests.unit.server.test_app`
- `tests.unit.server.test_chat_request`

## 示例用法

```python
from src.config.report_style import ReportStyle
#
# TODO: 结合业务场景补充 ReportStyle 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
