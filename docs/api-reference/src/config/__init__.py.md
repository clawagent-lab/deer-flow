# `src/config/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/config/__init__.py`
- **模块导入名**：`src.config`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：57
- **架构归属**：src/config —— 配置加载（`conf.yaml` / `.env`）、模型与工具开关、报告样式、智能体映射

## 模块概述

```text
配置子包入口，集中加载并暴露 DeerFlow 运行所需的各项配置。

启动时通过 dotenv 加载环境变量，并从 loader、questions、tools 子模块汇总导出：
yaml 配置加载器、内置示例问题、所选搜索引擎以及团队成员（researcher、coder）的角色描述配置，
供工作流构建与智能体创建使用。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .loader import load_yaml_config`
- `from .questions import BUILT_IN_QUESTIONS, BUILT_IN_QUESTIONS_ZH_CN`
- `from .tools import SELECTED_SEARCH_ENGINE, SearchEngine`

**外部依赖**（第三方库 / 标准库）：

- `from dotenv import load_dotenv`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `TEAM_MEMBER_CONFIGURATIONS` | 21 | `{'researcher': {'name': 'researcher', 'desc': 'Responsible for searching and collecting relevant ...` |
| 常量 | `TEAM_MEMBERS` | 46 | `list(TEAM_MEMBER_CONFIGURATIONS.keys())` |

## 符号详解

### `TEAM_MEMBER_CONFIGURATIONS`

- **类型**：模块常量  |  **行号**：21–44  |  **完整限定名**：`src.config.TEAM_MEMBER_CONFIGURATIONS`
- **值**：

```python
TEAM_MEMBER_CONFIGURATIONS = {'researcher': {'name': 'researcher', 'desc': 'Responsible for searching and collecting relevant information, underst...
```

**说明**（自动推断）：

模块级常量 `TEAM_MEMBER_CONFIGURATIONS`，在导入时初始化，供本模块及相关流程引用。

### `TEAM_MEMBERS`

- **类型**：模块常量  |  **行号**：46–46  |  **完整限定名**：`src.config.TEAM_MEMBERS`
- **值**：

```python
TEAM_MEMBERS = list(TEAM_MEMBER_CONFIGURATIONS.keys())
```

**说明**（自动推断）：

模块级常量 `TEAM_MEMBERS`，在导入时初始化，供本模块及相关流程引用。

## 调用关系（下游）

**被以下模块导入**：

- `src.crawler.crawler`
- `src.llms.llm`
- `src.tools.infoquest_search.infoquest_search_api`
- `src.tools.search`
- `src.tools.tavily_search.tavily_search_api_wrapper`
- `src.utils.context_manager`
- `tests.unit.tools.test_search`

## 示例用法

```python
from src.config import TEAM_MEMBER_CONFIGURATIONS
#
# TODO: 结合业务场景补充 TEAM_MEMBER_CONFIGURATIONS 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
