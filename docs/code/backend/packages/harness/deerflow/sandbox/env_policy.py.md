# `backend/packages/harness/deerflow/sandbox/env_policy.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/env_policy.py`  ·  行数: 113

**模块文档首行**（仅供参考）: Environment-variable policy for sandbox command execution (issue #3861).

## 模块概览
- 函数 2 个，类 0 个，模块级常量 2 个

## 功能语义解读

### 模块职责
本模块为 skill 沙盒子进程定义环境变量安全策略（对应 issue #3861）。skill 脚本以沙盒子进程形式执行，默认会继承 Gateway 父进程的整个 `os.environ`，本模块负责在将环境变量传递给子进程之前，擦洗其中"看起来像凭据"的条目，防止平台凭据泄漏。

### 核心问题：默认继承会泄漏平台凭据
Gateway 进程的 `os.environ` 携带平台级凭据（`OPENAI_API_KEY`、tracing keys、社区 provider keys 等）。若子进程原样继承，skill 脚本可直接读取这些平台密钥，使任何"按请求注入的 scoped secret"形同虚设——攻击面从"声明过的 secret"扩大到"父进程持有的全部凭据"。本模块的擦洗逻辑正是为了关闭这条泄漏通道。

### `_SECRET_NAME_PATTERNS`：通配符擦洗规则
模块级常量 `_SECRET_NAME_PATTERNS` 是一组大小写不敏感的通配符（匹配 upper 后的变量名），包含六类模式：

| 模式 | 覆盖示例 |
|------|---------|
| `*KEY*` | `OPENAI_API_KEY`、`API_KEY`、`SECRET_KEY` |
| `*SECRET*` | `CLIENT_SECRET`、`JWT_SECRET` |
| `*TOKEN*` | `ACCESS_TOKEN`、`CSRF_TOKEN` |
| `*PASS*` | `PASSWORD`、`PASSWD`、`DB_PASS`、`MYSQL_PASS`、`PGPASSFILE` |
| `*CREDENTIAL*` | `AWS_CREDENTIAL_FILE` 等 |
| `*DSN*` | 含密码的连接串（data source name） |

良性系统变量（`PATH`、`HOME`、`SHELL`、`LANG`、`PWD`、`TMPDIR`、`VIRTUAL_ENV`、`PYTHONPATH` 等）不含上述子串，因此被保留。

**`*PASS*` 覆盖 `*_ASKPASS` 的原因**：`GIT_ASKPASS`、`SSH_ASKPASS`、`SUDO_ASKPASS` 命名的不是密钥本身，而是一个"凭据助手程序"的路径。但该程序存在的目的正是向调用方返回凭据——把指针继承下去等同于把凭据继承下去，属于本模块要关闭的同一类泄漏。因此擦洗 `*_ASKPASS` 是有意为之，而非副作用。附带被误伤的 `COMPASS_*`、`BYPASS_*` 等也被擦洗，方向是 fail-safe：skill 若真的需要某个被擦洗的变量，应通过 `required-secrets` 显式声明。注意 `PWD`/`OLDPWD` 不含 `PASS` 子串，不受影响。

### `_BLOCKED_EXACT_NAMES`：精确名单及"不能用通配符"的原因
模块级常量 `_BLOCKED_EXACT_NAMES` 是一个 frozenset，精确匹配一批"承载连接串/凭据但名称不含 KEY/SECRET/TOKEN/DSN 子串"的变量：

- 连接串类：`DATABASE_URL`、`DATABASE_URI`、`REDIS_URL`、`MONGODB_URI`、`MONGO_URL`、`AMQP_URL`、`RABBITMQ_URL`、`POSTGRES_URL`、`POSTGRESQL_URL`、`MYSQL_URL`、`CLICKHOUSE_URL`、`CONNECTION_STRING`、`CONN_STR`
- 客户端无 flag 凭据源：`MYSQL_PWD`（mysql 文档化的无 flag 密码源）、`REDISCLI_AUTH`（redis-cli 文档化的无 flag 认证源）、`REDIS_AUTH`（非任何标准 Redis 客户端的规范名，但客户端库和部署模板常设，防御性拦截）、`PGSERVICEFILE`（libpq 读取其指向的 `pg_service.conf`，可能含密码字段）
- Token 类：`GH_PAT`、`GITHUB_PAT`（GitHub Personal Access Token 缩写，不含通配符子串）

**为什么不能用通配符**：
- 不能用 `*URL*`：会误伤 skill 合法需要读取的良性服务 URL。
- `PWD`/`AUTH`/`SERVICEFILE` 无法通配化：`*PWD*` 会连带擦掉 `PWD`/`OLDPWD`（shell 维护的当前目录变量），而这些是无害且必需的；`AUTH`/`SERVICEFILE` 又没有与其他变量共享的唯一子串。
- `PGPASSFILE` 已被 `*PASS*` 覆盖，故只在精确名单里放 `PGSERVICEFILE`（其兄弟项）。

`is_blocked_env_name` 的判定顺序：先查精确名单（`upper in _BLOCKED_EXACT_NAMES`），再用 `fnmatch.fnmatchcase` 对大写名逐一匹配通配符模式。精确名单优先使特殊变量免受通配符误伤/漏判。

### `build_sandbox_env` 的两步逻辑
```
env = {k: v for k, v in os.environ.items() if not is_blocked_env_name(k)}
if injected:
    env.update(injected)
return env
```
1. **擦洗继承环境**：复制 `os.environ`，但丢弃所有 `is_blocked_env_name` 为 True 的条目。此步只做"减法"，不引入任何新值。
2. **叠加注入密钥**：若调用方传入 `injected`（请求级 scoped secret），用 `env.update(injected)` 覆盖写入。

### 注入值优先于擦洗规则的安全意义
`env.update(injected)` 发生在擦洗之后，因此即使某个 `injected` 的键名匹配 `*KEY*`/`*PASS*` 等模式或命中精确名单，它仍会出现在最终环境里。这并非漏洞，而是设计：注入值来源于上游授权（skill 通过 `required-secrets` 声明，值来自请求上下文 `context.secrets`，而非宿主环境），是"被允许进入沙箱"的凭据。擦洗规则只针对"未经声明、被动继承"的宿主凭据。两者的信任级别不同，故注入胜出。

### 与 codex/hermes blocklist 的对比
- **codex**：有 `*KEY*/*SECRET*/*TOKEN*` 默认排除集，但默认**关闭**（opt-in）。
- **hermes**：采用固定的 provider blocklist。
- **DeerFlow**：模式集参考 codex 的通配符与 hermes 的固定名单，但策略相反——**默认擦洗**（opt-out），security first。这意味着 DeerFlow 沙箱在未显式声明 required-secrets 的情况下，不会向子进程泄漏任何看起来像凭据的继承变量；skill 若需要某凭据，必须走声明 + 注入路径。

## 依赖（import）
- 模块: fnmatch, os
- `__future__` -> annotations

## 模块级常量
- `_SECRET_NAME_PATTERNS` = ('*KEY*', '*SECRET*', '*TOKEN*', '*PASS*', '*CREDENTIAL*'...
- `_BLOCKED_EXACT_NAMES` = frozenset({'DATABASE_URL', 'DATABASE_URI', 'REDIS_URL', '...

## 函数
#### `ƒ` `is_blocked_env_name(name: str) -> bool`  L91
  - _文档首行_（仅供参考）: Return True if ``name`` looks like a credential that must not be inherited
  - 分支数 1，函数体节点数 45；return: True, any((fnmatch.fnmatchcase(upper, pattern) for pattern in _SECRET_NAME_PATTERNS))
  - 调用: upper, any, fnmatchcase

#### `ƒ` `build_sandbox_env(injected: dict[str, str] | None) -> dict[str, str]`  L100
  - _文档首行_（仅供参考）: Build the environment dict for a sandbox subprocess.
  - 分支数 1，函数体节点数 72；return: env
  - 调用: items, is_blocked_env_name, update

## 文件内调用关系
- `build_sandbox_env` -> is_blocked_env_name
