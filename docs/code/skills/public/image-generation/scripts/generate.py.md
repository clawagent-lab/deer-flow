# `skills/public/image-generation/scripts/generate.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/image-generation/scripts/generate.py`  ·  行数: 229

## 模块概览
- 函数 11 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: base64, json, os, requests

## 模块级常量
- `MINIMAX_DEFAULT_HOST` = 'https://api.minimaxi.com'
- `MINIMAX_PROMPT_MAX_CHARS` = 1500

## 函数
#### `ƒ` `validate_image(image_path: str) -> bool`  L13
  - _文档首行_（仅供参考）: Validate if an image file can be opened and is not corrupted.
  - 分支数 3，函数体节点数 66；return: True, False
  - 调用: open, verify, load, print
  - 文件IO: open (L18), open (L20)

#### `ƒ` `_resolve_provider(override_env: str, existing_provider: str, has_existing_creds: bool) -> str`  L28
  - _文档首行_（仅供参考）: Pick the generation provider.
  - 分支数 3，函数体节点数 66；raise: ValueError(f'No credentials found. Set GEMINI_API_KEY for {existing_provider}, or MINIMAX_API_KEY for minimax (optionally force with {override_env}).')；return: override.strip().lower(), existing_provider, 'minimax'
  - 调用: getenv, lower, strip, ValueError
  - 环境变量: getenv (L35), getenv (L40)

#### `ƒ` `_minimax_host() -> str`  L48
  - 分支数 0，函数体节点数 17；return: os.getenv('MINIMAX_API_HOST', MINIMAX_DEFAULT_HOST).rstrip('/')
  - 调用: rstrip, getenv
  - 环境变量: getenv (L49)

#### `ƒ` `_check_base_resp(payload: dict) -> None`  L52
  - 分支数 1，函数体节点数 50；raise: Exception(f"MiniMax error {base.get('status_code')}: {base.get('status_msg')}")
  - 调用: get, Exception

#### `ƒ` `_guess_mime(image_path: str) -> str`  L60
  - 分支数 0，函数体节点数 43；return: {'.png': 'image/png', '.webp': 'image/webp', '.gif': 'image/gif', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg'}.get(ext, 'image/jpeg')
  - 调用: lower, splitext, get

#### `ƒ` `_to_data_url(image_path: str) -> str`  L71
  - 分支数 1，函数体节点数 47；return: f'data:{_guess_mime(image_path)};base64,{b64}'
  - 调用: open, decode, b64encode, read, _guess_mime
  - 文件IO: open (L72), read (L73)

#### `ƒ` `_ensure_output_dir(output_file: str) -> None`  L77
  - _文档首行_（仅供参考）: Create the output file's parent directory so nested paths don't fail.
  - 分支数 1，函数体节点数 33
  - 调用: dirname, makedirs

#### `ƒ` `_minimax_prompt(raw: str) -> str`  L84
  - _文档首行_（仅供参考）: Extract the single text prompt MiniMax image-01 expects.
  - 分支数 3，函数体节点数 81；return: text, core.strip()
  - 调用: strip, loads, isinstance, get

#### `ƒ` `_generate_image_minimax(prompt: str, reference_images: list[str], output_file: str, aspect_ratio: str) -> str`  L106
  - 分支数 5，函数体节点数 233；raise: Exception('MiniMax returned no image data')；return: 'MINIMAX_API_KEY is not set', f'Prompt is {len(prompt)} characters but MiniMax image-01 accepts at most {MINIMAX_PROMPT_MAX_CHARS}. Shorten the prompt to stay within the limit; reference images plus a tighter description usually recover the detail.', f'Successfully generated image to {output_file}'
  - 调用: getenv, _minimax_prompt, len, _to_data_url, post, _minimax_host, raise_for_status, json, _check_base_resp, get, Exception, _ensure_output_dir, open, write, b64decode
  - 网络调用: post (L133)
  - 文件IO: open (L146), write (L147)
  - 环境变量: getenv (L109), getenv (L120)

#### `ƒ` `_generate_image_gemini(prompt: str, reference_images: list[str], output_file: str, aspect_ratio: str) -> str`  L151
  - 分支数 8，函数体节点数 316；raise: Exception('Failed to generate image')；return: 'GEMINI_API_KEY is not set', f'Successfully generated image to {output_file}'
  - 调用: validate_image, append, print, len, open, decode, b64encode, read, getenv, post, raise_for_status, json, get, _ensure_output_dir, write, b64decode, Exception
  - 网络调用: post (L173)
  - 文件IO: open (L166), read (L167), open (L188), write (L189)
  - 环境变量: getenv (L170)

#### `ƒ` `generate_image(prompt_file: str, reference_images: list[str], output_file: str, aspect_ratio: str) -> str`  L194
  - 分支数 3，函数体节点数 107；raise: ValueError(f"Unknown image provider: {provider!r} (use 'gemini' or 'minimax')")；return: _generate_image_minimax(prompt, reference_images, output_file, aspect_ratio), _generate_image_gemini(prompt, reference_images, output_file, aspect_ratio)
  - 调用: open, read, _resolve_provider, bool, getenv, _generate_image_minimax, _generate_image_gemini, ValueError
  - 文件IO: open (L200), read (L201)
  - 环境变量: getenv (L203)

## 文件内调用关系
- `_to_data_url` -> _guess_mime
- `_generate_image_minimax` -> _minimax_prompt, _to_data_url, _minimax_host, _check_base_resp, _ensure_output_dir
- `_generate_image_gemini` -> validate_image, _ensure_output_dir
- `generate_image` -> _resolve_provider, _generate_image_minimax, _generate_image_gemini
