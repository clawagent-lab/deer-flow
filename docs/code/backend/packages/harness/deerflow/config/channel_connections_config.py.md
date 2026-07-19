# `backend/packages/harness/deerflow/config/channel_connections_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/channel_connections_config.py`  ·  行数: 63

**模块文档首行**（仅供参考）: Configuration for user-owned IM channel connections.

## 模块概览
- 函数 0 个，类 5 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `pydantic` -> BaseModel, Field

## 类
### 类 `SlackChannelConnectionConfig`  L8
- 继承: BaseModel
- 类/实例变量:
  - `enabled` = False
- 方法:
  #### `prop` `configured(self) -> bool`    @property  L12
    - 分支数 0，函数体节点数 9；return: True

### 类 `TelegramChannelConnectionConfig`  L16
- 继承: BaseModel
- 类/实例变量:
  - `enabled` = False
  - `bot_username` = ''
- 方法:
  #### `prop` `configured(self) -> bool`    @property  L21
    - 分支数 0，函数体节点数 15；return: bool(self.bot_username)
    - 调用: bool

### 类 `DiscordChannelConnectionConfig`  L25
- 继承: BaseModel
- 类/实例变量:
  - `enabled` = False
- 方法:
  #### `prop` `configured(self) -> bool`    @property  L29
    - 分支数 0，函数体节点数 9；return: True

### 类 `BindingCodeChannelConnectionConfig`  L33
- 继承: BaseModel
- 类/实例变量:
  - `enabled` = False
- 方法:
  #### `prop` `configured(self) -> bool`    @property  L37
    - 分支数 0，函数体节点数 9；return: True

### 类 `ChannelConnectionsConfig`  L41
- 继承: BaseModel
- _文档首行_: Top-level config for browser-connectable IM channels.
- 类/实例变量:
  - `enabled` = False
  - `require_bound_identity` = True
  - `slack` = Field(default_factory=SlackChannelConnectionConfig)
  - `telegram` = Field(default_factory=TelegramChannelConnectionConfig)
  - `discord` = Field(default_factory=DiscordChannelConnectionConfig)
  - `feishu` = Field(default_factory=BindingCodeChannelConnectionConfig)
  - `dingtalk` = Field(default_factory=BindingCodeChannelConnectionConfig)
  - `wechat` = Field(default_factory=BindingCodeChannelConnectionConfig)
  - `wecom` = Field(default_factory=BindingCodeChannelConnectionConfig)
- 方法:
  #### `m` `provider_status(self, provider: str) -> dict[str, bool]`  L54
    - 分支数 1，函数体节点数 66；return: {'enabled': False, 'configured': False}, {'enabled': enabled, 'configured': enabled and bool(config.configured)}
    - 调用: getattr, bool
  - 反射: getattr (L55)

## 文件内调用关系
_无文件内调用_
