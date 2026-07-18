# `src/config/questions.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/config/questions.py`
- **模块导入名**：`src.config.questions`
- **代码行数**：34
- **架构归属**：src/config —— 配置加载（`conf.yaml` / `.env`）、模型与工具开关、报告样式、智能体映射

## 模块概述

```text
Built-in questions for Deer.
```

## 依赖关系（上游）

_无导入。_

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `BUILT_IN_QUESTIONS` | 9 | `['What factors are influencing AI adoption in healthcare?', 'How does quantum computing impact cr...` |
| 常量 | `BUILT_IN_QUESTIONS_ZH_CN` | 23 | `['人工智能在医疗保健领域的应用有哪些因素影响?', '量子计算如何影响密码学?', '可再生能源技术的最新发展是什么?', '气候变化如何影响全球农业?', '人工智能的伦理影响是什么?', ...` |

## 符号详解

### `BUILT_IN_QUESTIONS`

- **类型**：模块常量  |  **行号**：9–20  |  **完整限定名**：`src.config.questions.BUILT_IN_QUESTIONS`
- **值**：

```python
BUILT_IN_QUESTIONS = ['What factors are influencing AI adoption in healthcare?', 'How does quantum computing impact cryptography?', 'What ...
```

**说明**（自动推断）：

模块级常量 `BUILT_IN_QUESTIONS`，在导入时初始化，供本模块及相关流程引用。

### `BUILT_IN_QUESTIONS_ZH_CN`

- **类型**：模块常量  |  **行号**：23–34  |  **完整限定名**：`src.config.questions.BUILT_IN_QUESTIONS_ZH_CN`
- **值**：

```python
BUILT_IN_QUESTIONS_ZH_CN = ['人工智能在医疗保健领域的应用有哪些因素影响?', '量子计算如何影响密码学?', '可再生能源技术的最新发展是什么?', '气候变化如何影响全球农业?', '人工智能的伦理影响是什么?', '网络安全的当前趋势是什么?', '区块...
```

**说明**（自动推断）：

模块级常量 `BUILT_IN_QUESTIONS_ZH_CN`，在导入时初始化，供本模块及相关流程引用。

## 调用关系（下游）

**被以下模块导入**：

- `main`
- `src.config`

## 示例用法

```python
from src.config.questions import BUILT_IN_QUESTIONS
#
# TODO: 结合业务场景补充 BUILT_IN_QUESTIONS 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
