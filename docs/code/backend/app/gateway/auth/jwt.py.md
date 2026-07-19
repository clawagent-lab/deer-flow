# `backend/app/gateway/auth/jwt.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/jwt.py`  ·  行数: 56

**模块文档首行**（仅供参考）: JWT token creation and verification.

## 模块概览
- 函数 2 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: jwt
- `datetime` -> UTC, datetime, timedelta
- `pydantic` -> BaseModel
- `app.gateway.auth.config` -> get_auth_config
- `app.gateway.auth.errors` -> TokenError

## 函数
#### `ƒ` `create_access_token(user_id: str, expires_delta: timedelta | None, token_version: int) -> str`  L21
  - _文档首行_（仅供参考）: Create a JWT access token.
  - 分支数 0，函数体节点数 85；return: jwt.encode(payload, config.jwt_secret, algorithm='HS256')
  - 调用: get_auth_config, timedelta, now, encode

#### `ƒ` `decode_token(token: str) -> TokenPayload | TokenError`  L40
  - _文档首行_（仅供参考）: Decode and validate a JWT token.
  - 分支数 1，函数体节点数 75；return: TokenPayload(**payload), TokenError.EXPIRED, TokenError.INVALID_SIGNATURE, TokenError.MALFORMED
  - 调用: get_auth_config, decode, TokenPayload

## 类
### 类 `TokenPayload`  L12
- 继承: BaseModel
- _文档首行_: JWT token payload.
- 类/实例变量:
  - `sub` = <annotated>
  - `exp` = <annotated>
  - `iat` = None
  - `ver` = 0

## 文件内调用关系
_无文件内调用_
