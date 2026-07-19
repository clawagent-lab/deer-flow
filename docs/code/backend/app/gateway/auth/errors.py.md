# `backend/app/gateway/auth/errors.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/errors.py`  ·  行数: 46

**模块文档首行**（仅供参考）: Typed error definitions for auth module.

## 模块概览
- 函数 1 个，类 3 个，模块级常量 0 个

## 依赖（import）
- `enum` -> StrEnum
- `pydantic` -> BaseModel

## 函数
#### `ƒ` `token_error_to_code(err: TokenError) -> AuthErrorCode`  L41
  - _文档首行_（仅供参考）: Map TokenError to AuthErrorCode — single source of truth.
  - 分支数 1，函数体节点数 28；return: AuthErrorCode.TOKEN_EXPIRED, AuthErrorCode.TOKEN_INVALID

## 类
### 类 `AuthErrorCode`  L13
- 继承: StrEnum
- _文档首行_: Exhaustive list of auth error conditions.
- 类/实例变量:
  - `INVALID_CREDENTIALS` = 'invalid_credentials'
  - `TOKEN_EXPIRED` = 'token_expired'
  - `TOKEN_INVALID` = 'token_invalid'
  - `USER_NOT_FOUND` = 'user_not_found'
  - `EMAIL_ALREADY_EXISTS` = 'email_already_exists'
  - `PROVIDER_NOT_FOUND` = 'provider_not_found'
  - `NOT_AUTHENTICATED` = 'not_authenticated'
  - `SYSTEM_ALREADY_INITIALIZED` = 'system_already_initialized'

### 类 `TokenError`  L26
- 继承: StrEnum
- _文档首行_: Exhaustive list of JWT decode failure reasons.
- 类/实例变量:
  - `EXPIRED` = 'expired'
  - `INVALID_SIGNATURE` = 'invalid_signature'
  - `MALFORMED` = 'malformed'

### 类 `AuthErrorResponse`  L34
- 继承: BaseModel
- _文档首行_: Structured error response — replaces bare `detail` strings.
- 类/实例变量:
  - `code` = <annotated>
  - `message` = <annotated>

## 文件内调用关系
_无文件内调用_
