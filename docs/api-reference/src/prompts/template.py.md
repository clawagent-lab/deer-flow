# `src/prompts/template.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/prompts/template.py`
- **模块导入名**：`src.prompts.template`
- **代码行数**：117
- **架构归属**：src/prompts —— Jinja2 提示词模板与 Plan/Step 数据模型

## 模块概述

```text
提示词模板加载与渲染工具。

基于 Jinja2 构建模板环境（``env``），支持按 locale（如 zh-CN/en-US）加载
对应的 ``*.md`` 模板并回退到默认英文版本。对外提供 ``get_prompt_template``
读取原始模板字符串，以及 ``apply_prompt_template`` 将 AgentState / Configuration
中的变量注入模板并返回 LangChain 消息列表。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.configuration import Configuration`

**外部依赖**（第三方库 / 标准库）：

- `from datetime import datetime`
- `from jinja2 import Environment, FileSystemLoader, TemplateNotFound, select_autoescape`
- `from langchain.agents import AgentState`
- `import dataclasses`
- `import os`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `env` | 21 | `Environment(loader=FileSystemLoader(os.path.dirname(__file__)), autoescape=select_autoescape(), t...` |
| 函数 | `get_prompt_template` | 29 | `(prompt_name: str, locale: str='en-US') -> str` |
| 函数 | `apply_prompt_template` | 56 | `(prompt_name: str, state: AgentState, configurable: Configuration=None, locale: str='en-US') -> list` |
| 函数 | `get_system_prompt_template` | 77 | `(prompt_name: str, state: AgentState, configurable: Configuration=None, locale: str='en-US') -> str` |

## 符号详解

### `env`

- **类型**：模块常量  |  **行号**：21–26  |  **完整限定名**：`src.prompts.template.env`
- **值**：

```python
env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)), autoescape=select_autoescape(), trim_blocks=True, lst...
```

**说明**（自动推断）：

Jinja2 模板环境实例，配置了模板加载路径与自动转义，用于渲染提示词模板。

### `get_prompt_template`

- **类型**：函数  |  **行号**：29–53  |  **完整限定名**：`src.prompts.template.get_prompt_template`
- **签名**：

```python
def get_prompt_template(prompt_name: str, locale: str='en-US') -> str:
```

**摘要**：

Load and return a prompt template using Jinja2 with locale support.

**参数**：

```text
prompt_name: Name of the prompt template file (without .md extension)
    locale: Language locale (e.g., en-US, zh-CN). Defaults to en-US
```

**返回值**：

```text
The template string with proper variable substitution syntax
```

### `apply_prompt_template`

- **类型**：函数  |  **行号**：56–75  |  **完整限定名**：`src.prompts.template.apply_prompt_template`
- **签名**：

```python
def apply_prompt_template(prompt_name: str, state: AgentState, configurable: Configuration=None, locale: str='en-US') -> list:
```

**摘要**：

Apply template variables to a prompt template and return formatted messages.

**参数**：

```text
prompt_name: Name of the prompt template to use
    state: Current agent state containing variables to substitute
    configurable: Configuration object with additional variables
    locale: Language locale for template selection (e.g., en-US, zh-CN)
```

**返回值**：

```text
List of messages with the system prompt as the first message
```

### `get_system_prompt_template`

- **类型**：函数  |  **行号**：77–117  |  **完整限定名**：`src.prompts.template.get_system_prompt_template`
- **签名**：

```python
def get_system_prompt_template(prompt_name: str, state: AgentState, configurable: Configuration=None, locale: str='en-US') -> str:
```

**摘要**：

Render and return the system prompt template with state and configuration variables.
This function loads a Jinja2-based prompt template (with optional locale-specific
variants), applies variables from the agent state and Configuration object, and
returns the fully rendered system prompt string.

**参数**：

```text
prompt_name: Name of the prompt template to load (without .md extension).
    state: Current agent state containing variables available to the template.
    configurable: Optional Configuration object providing additional template variables.
    locale: Language locale for template selection (e.g., en-US, zh-CN).
```

**返回值**：

```text
The rendered system prompt string after applying all template variables.
```

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.nodes`
- `src.podcast.graph.script_writer_node`
- `src.ppt.graph.ppt_composer_node`
- `src.prompt_enhancer.graph.enhancer_node`
- `src.prompts`
- `src.prose.graph.prose_continue_node`
- `src.prose.graph.prose_fix_node`
- `src.prose.graph.prose_improve_node`
- `src.prose.graph.prose_longer_node`
- `src.prose.graph.prose_shorter_node`
- `src.prose.graph.prose_zap_node`
- `tests.integration.test_template`

## 示例用法

```python
from src.prompts.template import get_prompt_template
#
# TODO: 结合业务场景补充 get_prompt_template 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
