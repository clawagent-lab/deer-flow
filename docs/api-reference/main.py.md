# `main.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`main.py`
- **模块导入名**：`main`
- **代码行数**：191
- **架构归属**：main.py

## 模块概述

```text
Entry point script for the DeerFlow project.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.questions import BUILT_IN_QUESTIONS, BUILT_IN_QUESTIONS_ZH_CN`
- `from src.workflow import run_agent_workflow_async`

**外部依赖**（第三方库 / 标准库）：

- `from InquirerPy import inquirer`
- `import argparse`
- `import asyncio`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `ask` | 17 | `(question, debug=False, max_plan_iterations=1, max_step_num=3, enable_background_investigation=Tr...` |
| 函数 | `main` | 53 | `(debug=False, max_plan_iterations=1, max_step_num=3, enable_background_investigation=True, enable...` |

## 符号详解

### `ask`

- **类型**：函数  |  **行号**：17–50  |  **完整限定名**：`main.ask`
- **签名**：

```python
def ask(question, debug=False, max_plan_iterations=1, max_step_num=3, enable_background_investigation=True, enable_clarification=False, max_clarification_rounds=None, locale=None):
```

**摘要**：

Run the agent workflow with the given question.

**参数**：

```text
question: The user's query or request
    debug: If True, enables debug level logging
    max_plan_iterations: Maximum number of plan iterations
    max_step_num: Maximum number of steps in a plan
    enable_background_investigation: If True, performs web search before planning to enhance context
    enable_clarification: If False (default), skip clarification; if True, enable multi-turn clarification
    max_clarification_rounds: Maximum number of clarification rounds (default: None, uses State default=3)
    locale: The locale setting (e.g., 'en-US', 'zh-CN')
```

### `main`

- **类型**：函数  |  **行号**：53–115  |  **完整限定名**：`main.main`
- **签名**：

```python
def main(debug=False, max_plan_iterations=1, max_step_num=3, enable_background_investigation=True, enable_clarification=False, max_clarification_rounds=None):
```

**摘要**：

Interactive mode with built-in questions.

**参数**：

```text
enable_background_investigation: If True, performs web search before planning to enhance context
    debug: If True, enables debug level logging
    max_plan_iterations: Maximum number of plan iterations
    max_step_num: Maximum number of steps in a plan
    enable_clarification: If False (default), skip clarification; if True, enable multi-turn clarification
    max_clarification_rounds: Maximum number of clarification rounds (default: None, uses State default=3)
```

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
# main.py 示例用法
#
# 1) 交互模式（内置问题选择 + 自定义输入）
#    首先选择语言，然后从内置问题列表选择或输入自定义问题。
python main.py --interactive

# 2) 直接传入查询（非交互）
python main.py "分析 2025 年大语言模型在代码生成领域的趋势"

# 3) 启用调试日志 + 多轮澄清 + 关闭背景调查
python main.py "研究 RAG 架构优化" \
    --debug \
    --enable-clarification \
    --max-clarification-rounds 2 \
    --no-background-investigation

# 4) 在 Python 代码中调用 ask() 函数
from main import ask

# 单次提问，自动接受计划，启用背景调查
ask(
    question="对比 Milvus 与 Qdrant 在千万级向量检索下的性能差异",
    debug=False,
    max_plan_iterations=2,
    max_step_num=5,
    enable_background_investigation=True,
    enable_clarification=False,
    locale="zh-CN",
)

# 5) 在 Python 代码中调用交互式 main()
from main import main

# 进入语言选择 -> 问题选择 -> 执行工作流的完整交互流程
main(
    debug=True,
    max_plan_iterations=1,
    max_step_num=3,
    enable_background_investigation=True,
)
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
