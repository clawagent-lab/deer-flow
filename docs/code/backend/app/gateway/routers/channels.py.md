# `backend/app/gateway/routers/channels.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/channels.py`  ·  行数: 59

**模块文档首行**（仅供参考）: Gateway router for IM channel management.

## 模块概览
- 函数 2 个，类 2 个，模块级常量 3 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `fastapi` -> APIRouter, HTTPException, Request
- `pydantic` -> BaseModel
- `app.gateway.deps` -> require_admin_user

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api/channels', tags=['channels'])
- `_ADMIN_REQUIRED_DETAIL` = 'Admin privileges required to manage channel runtime work...

## 函数
#### `⏵ƒ` `async get_channels_status() -> ChannelStatusResponse`    @router.get(...)  L30
  - _文档首行_（仅供参考）: Get the status of all IM channels.
  - 分支数 1，函数体节点数 52；return: ChannelStatusResponse(service_running=False, channels={}), ChannelStatusResponse(**status)
  - 调用: get_channel_service, ChannelStatusResponse, get_status, get

#### `⏵ƒ` `async restart_channel(name: str, request: Request) -> ChannelRestartResponse`    @router.post(...)  L42
  - _文档首行_（仅供参考）: Restart a specific IM channel.
  - 分支数 2，函数体节点数 110；raise: HTTPException(status_code=503, detail='Channel service is not running')；return: ChannelRestartResponse(success=True, message=f'Channel {name} restarted successfully'), ChannelRestartResponse(success=False, message=f'Failed to restart channel {name}')
  - 调用: require_admin_user, get_channel_service, HTTPException, restart_channel, info, ChannelRestartResponse, warning, post

## 类
### 类 `ChannelStatusResponse`  L19
- 继承: BaseModel
- 类/实例变量:
  - `service_running` = <annotated>
  - `channels` = <annotated>

### 类 `ChannelRestartResponse`  L24
- 继承: BaseModel
- 类/实例变量:
  - `success` = <annotated>
  - `message` = <annotated>

## 文件内调用关系
- `restart_channel` -> restart_channel
