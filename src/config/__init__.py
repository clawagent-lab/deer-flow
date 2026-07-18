# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""配置子包入口，集中加载并暴露 DeerFlow 运行所需的各项配置。

启动时通过 dotenv 加载环境变量，并从 loader、questions、tools 子模块汇总导出：
yaml 配置加载器、内置示例问题、所选搜索引擎以及团队成员（researcher、coder）的角色描述配置，
供工作流构建与智能体创建使用。
"""

from dotenv import load_dotenv

from .loader import load_yaml_config
from .questions import BUILT_IN_QUESTIONS, BUILT_IN_QUESTIONS_ZH_CN
from .tools import SELECTED_SEARCH_ENGINE, SearchEngine

# Load environment variables
load_dotenv()

# Team configuration
TEAM_MEMBER_CONFIGURATIONS = {
    "researcher": {
        "name": "researcher",
        "desc": (
            "Responsible for searching and collecting relevant information, understanding user needs and conducting research analysis"
        ),
        "desc_for_llm": (
            "Uses search engines and web crawlers to gather information from the internet. "
            "Outputs a Markdown report summarizing findings. Researcher can not do math or programming."
        ),
        "is_optional": False,
    },
    "coder": {
        "name": "coder",
        "desc": (
            "Responsible for code implementation, debugging and optimization, handling technical programming tasks"
        ),
        "desc_for_llm": (
            "Executes Python or Bash commands, performs mathematical calculations, and outputs a Markdown report. "
            "Must be used for all mathematical computations."
        ),
        "is_optional": True,
    },
}

TEAM_MEMBERS = list(TEAM_MEMBER_CONFIGURATIONS.keys())

__all__ = [
    # Other configurations
    "TEAM_MEMBERS",
    "TEAM_MEMBER_CONFIGURATIONS",
    "SELECTED_SEARCH_ENGINE",
    "SearchEngine",
    "BUILT_IN_QUESTIONS",
    "BUILT_IN_QUESTIONS_ZH_CN",
    load_yaml_config,
]
