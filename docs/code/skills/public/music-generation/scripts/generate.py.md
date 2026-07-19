# `skills/public/music-generation/scripts/generate.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/music-generation/scripts/generate.py`  ·  行数: 83

## 模块概览
- 函数 2 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: argparse, json, os, requests

## 模块级常量
- `MINIMAX_DEFAULT_HOST` = 'https://api.minimaxi.com'

## 函数
#### `ƒ` `_check_base_resp(payload: dict) -> None`  L10
  - 分支数 1，函数体节点数 50；raise: Exception(f"MiniMax error {base.get('status_code')}: {base.get('status_msg')}")
  - 调用: get, Exception

#### `ƒ` `generate_music(prompt_file: str, output_file: str) -> str`  L16
  - _文档首行_（仅供参考）: Generate a song from a JSON spec via MiniMax /v1/music_generation.
  - 分支数 8，函数体节点数 296；raise: ValueError('`prompt` is required in the music spec'), Exception('MiniMax returned no audio data')；return: 'MINIMAX_API_KEY is not set', f'Successfully generated music to {output_file}'
  - 调用: open, load, getenv, strip, get, ValueError, bool, rstrip, post, raise_for_status, json, _check_base_resp, Exception, dirname, makedirs, write, fromhex
  - 网络调用: post (L51)
  - 文件IO: open (L24), open (L67), write (L68)
  - 环境变量: getenv (L27), getenv (L38), getenv (L50)

## 文件内调用关系
- `generate_music` -> _check_base_resp
