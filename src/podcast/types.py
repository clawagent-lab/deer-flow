# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""播客（Podcast）模块的类型定义。

使用 Pydantic 定义脚本相关的数据结构：ScriptLine 表示单行对白
（含男/女声标识与段落文本），Script 表示完整脚本（含语言 locale
与对白行列表），供脚本撰写节点的结构化输出使用。
"""

from typing import Literal

from pydantic import BaseModel, Field


class ScriptLine(BaseModel):
    speaker: Literal["male", "female"] = Field(default="male")
    paragraph: str = Field(default="")


class Script(BaseModel):
    locale: Literal["en", "zh"] = Field(default="en")
    lines: list[ScriptLine] = Field(default=[])
