# `scripts/license_header.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`scripts/license_header.py`
- **模块导入名**：`scripts.license_header`
- **代码行数**：227
- **架构归属**：scripts —— 仓库脚本（API 文档生成器、license 头检查等）

## 模块概述

```text
Script to add or check license headers in Python and TypeScript files.
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from pathlib import Path`
- `from typing import Dict, List`
- `import argparse`
- `import sys`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `FILE_TYPE_MAP` | 22 | `{'.py': 'python', '.ts': 'typescript', '.tsx': 'typescript'}` |
| 常量 | `SKIP_PATTERNS` | 29 | `['__pycache__', '.pytest_cache', '.ruff_cache', 'node_modules', '.next', '.venv', 'venv', '.tox',...` |
| 函数 | `should_skip` | 45 | `(path: Path) -> bool` |
| 函数 | `get_file_type` | 50 | `(file_path: Path) -> str \| None` |
| 函数 | `has_license_header` | 55 | `(content: str, file_type: str) -> bool` |
| 函数 | `add_license_header` | 80 | `(file_path: Path, dry_run: bool=False) -> bool` |
| 函数 | `find_source_files` | 137 | `(root: Path) -> List[Path]` |
| 函数 | `main` | 150 | `()` |

## 符号详解

### `FILE_TYPE_MAP`

- **类型**：模块常量  |  **行号**：22–26  |  **完整限定名**：`scripts.license_header.FILE_TYPE_MAP`
- **值**：

```python
FILE_TYPE_MAP = {'.py': 'python', '.ts': 'typescript', '.tsx': 'typescript'}
```

**说明**（自动推断）：

模块级常量 `FILE_TYPE_MAP`，在导入时初始化，供本模块及相关流程引用。

### `SKIP_PATTERNS`

- **类型**：模块常量  |  **行号**：29–42  |  **完整限定名**：`scripts.license_header.SKIP_PATTERNS`
- **值**：

```python
SKIP_PATTERNS = ['__pycache__', '.pytest_cache', '.ruff_cache', 'node_modules', '.next', '.venv', 'venv', '.tox', 'build', 'dist', '....
```

**说明**（自动推断）：

黑名单/跳过规则常量 `SKIP_PATTERNS`，列出需拒绝或排除的取值。

### `should_skip`

- **类型**：函数  |  **行号**：45–47  |  **完整限定名**：`scripts.license_header.should_skip`
- **签名**：

```python
def should_skip(path: Path) -> bool:
```

**摘要**：

Check if a path should be skipped.

### `get_file_type`

- **类型**：函数  |  **行号**：50–52  |  **完整限定名**：`scripts.license_header.get_file_type`
- **签名**：

```python
def get_file_type(file_path: Path) -> str | None:
```

**摘要**：

Get the file type based on extension.

### `has_license_header`

- **类型**：函数  |  **行号**：55–77  |  **完整限定名**：`scripts.license_header.has_license_header`
- **签名**：

```python
def has_license_header(content: str, file_type: str) -> bool:
```

**摘要**：

Check if content already has the license header.

### `add_license_header`

- **类型**：函数  |  **行号**：80–134  |  **完整限定名**：`scripts.license_header.add_license_header`
- **签名**：

```python
def add_license_header(file_path: Path, dry_run: bool=False) -> bool:
```

**摘要**：

Add license header to a file if not present.

**参数**：

```text
file_path: Path to the file
    dry_run: If True, only check without modifying
```

**返回值**：

```text
True if header was added (or would be added in dry-run), False if already present
```

### `find_source_files`

- **类型**：函数  |  **行号**：137–147  |  **完整限定名**：`scripts.license_header.find_source_files`
- **签名**：

```python
def find_source_files(root: Path) -> List[Path]:
```

**摘要**：

Find all Python and TypeScript files in the given directory tree.

### `main`

- **类型**：函数  |  **行号**：150–222  |  **完整限定名**：`scripts.license_header.main`
- **签名**：

```python
def main():
```

**说明**（自动推断）：

脚本主入口函数，解析命令行参数并执行对应操作。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from scripts.license_header import main
#
# TODO: 结合业务场景补充 main 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
