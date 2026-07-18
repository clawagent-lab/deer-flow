# `server.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`server.py`
- **模块导入名**：`server`
- **代码行数**：108
- **架构归属**：server.py

## 模块概述

```text
Server script for running the DeerFlow API.
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `import argparse`
- `import asyncio`
- `import logging`
- `import os`
- `import signal`
- `import sys`
- `import uvicorn`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 23 | `logging.getLogger(__name__)` |
| 函数 | `handle_shutdown` | 37 | `(signum, frame)` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：23–23  |  **完整限定名**：`server.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `handle_shutdown`

- **类型**：函数  |  **行号**：37–40  |  **完整限定名**：`server.handle_shutdown`
- **签名**：

```python
def handle_shutdown(signum, frame):
```

**摘要**：

Handle graceful shutdown on SIGTERM/SIGINT

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
# server.py 示例用法
#
# 该脚本是 FastAPI 服务的启动入口，实际应用对象在 src/server/app.py 中定义。
#
# 1) 默认启动（localhost:8000，info 日志级别）
python server.py

# 2) 开启热重载 + 指定端口 + debug 日志
python server.py --reload --port 8000 --log-level debug

# 3) 通过环境变量 DEBUG 覆盖日志级别
DEBUG=true python server.py --host 0.0.0.0 --port 8080

# 4) 绑定到非 localhost（仅限已加固的部署环境）
python server.py --host 0.0.0.0 --port 8080 --log-level warning

# 5) 在代码中直接使用 uvicorn 运行（等价于命令行）
import uvicorn

# 注意：应用对象路径为 "src.server:app"
uvicorn.run(
    "src.server:app",
    host="localhost",
    port=8000,
    reload=True,
    log_level="info",
)

# 6) 在代码中直接导入 app 对象进行测试或挂载
from src.server.app import app

# 可用于 TestClient 测试
from starlette.testclient import TestClient

client = TestClient(app)
# 健康检查 / 状态接口（具体路由见 src/server/ 下各 *_request.py）
# response = client.get("/health")
# assert response.status_code == 200
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`
