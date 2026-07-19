# `backend/app/gateway/auth/password.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/password.py`  ·  行数: 82

**模块文档首行**（仅供参考）: Password hashing utilities with versioned hash format.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 3 个

## 依赖（import）
- 模块: asyncio, base64, hashlib, bcrypt

## 模块级常量
- `_CURRENT_VERSION` = 2
- `_PREFIX_V2` = '$dfv2$'
- `_PREFIX_V1` = '$dfv1$'

## 函数
#### `ƒ` `_pre_hash_v2(password: str) -> bytes`  L27
  - _文档首行_（仅供参考）: SHA-256 pre-hash to bypass bcrypt's 72-byte limit.
  - 分支数 0，函数体节点数 29；return: base64.b64encode(hashlib.sha256(password.encode('utf-8')).digest())
  - 调用: b64encode, digest, sha256, encode

#### `ƒ` `hash_password(password: str) -> str`  L32
  - _文档首行_（仅供参考）: Hash a password (current version: v2 — SHA-256 + bcrypt).
  - 分支数 0，函数体节点数 39；return: f'{_PREFIX_V2}{raw}'
  - 调用: decode, hashpw, _pre_hash_v2, gensalt

#### `ƒ` `verify_password(plain_password: str, hashed_password: str) -> bool`  L38
  - _文档首行_（仅供参考）: Verify a password, auto-detecting the hash version.
  - 分支数 3，函数体节点数 100；return: bcrypt.checkpw(_pre_hash_v2(plain_password), bcrypt_hash.encode('utf-8')), bcrypt.checkpw(plain_password.encode('utf-8'), bcrypt_hash.encode('utf-8')), False
  - 调用: startswith, len, checkpw, _pre_hash_v2, encode

#### `ƒ` `needs_rehash(hashed_password: str) -> bool`  L61
  - _文档首行_（仅供参考）: Return True if the hash uses an older version and should be rehashed.
  - 分支数 0，函数体节点数 19；return: not hashed_password.startswith(_PREFIX_V2)
  - 调用: startswith

#### `⏵ƒ` `async hash_password_async(password: str) -> str`  L66
  - _文档首行_（仅供参考）: Hash a password using bcrypt (non-blocking).
  - 分支数 0，函数体节点数 20；return: await asyncio.to_thread(hash_password, password)
  - 调用: to_thread

#### `⏵ƒ` `async verify_password_async(plain_password: str, hashed_password: str) -> bool`  L75
  - _文档首行_（仅供参考）: Verify a password against its hash (non-blocking).
  - 分支数 0，函数体节点数 25；return: await asyncio.to_thread(verify_password, plain_password, hashed_password)
  - 调用: to_thread

## 文件内调用关系
- `hash_password` -> _pre_hash_v2
- `verify_password` -> _pre_hash_v2
