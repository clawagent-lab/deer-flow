# `skills/public/video-generation/scripts/generate.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/video-generation/scripts/generate.py`  ·  行数: 223

## 模块概览
- 函数 13 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: base64, os, time, requests

## 模块级常量
- `MINIMAX_DEFAULT_HOST` = 'https://api.minimaxi.com'

## 函数
#### `ƒ` `_resolve_provider(override_env: str, existing_provider: str, has_existing_creds: bool) -> str`  L10
  - _文档首行_（仅供参考）: Pick the provider: <SKILL>_PROVIDER override > existing creds > MiniMax fallback.
  - 分支数 3，函数体节点数 66；raise: ValueError(f'No credentials found. Set GEMINI_API_KEY for {existing_provider}, or MINIMAX_API_KEY for minimax (optionally force with {override_env}).')；return: override.strip().lower(), existing_provider, 'minimax'
  - 调用: getenv, lower, strip, ValueError
  - 环境变量: getenv (L12), getenv (L17)

#### `ƒ` `_minimax_host() -> str`  L25
  - 分支数 0，函数体节点数 17；return: os.getenv('MINIMAX_API_HOST', MINIMAX_DEFAULT_HOST).rstrip('/')
  - 调用: rstrip, getenv
  - 环境变量: getenv (L26)

#### `ƒ` `_ensure_output_dir(output_file: str) -> None`  L29
  - _文档首行_（仅供参考）: Create the output file's parent directory so nested paths don't fail.
  - 分支数 1，函数体节点数 33
  - 调用: dirname, makedirs

#### `ƒ` `_check_base_resp(payload: dict) -> None`  L36
  - 分支数 1，函数体节点数 50；raise: Exception(f"MiniMax error {base.get('status_code')}: {base.get('status_msg')}")
  - 调用: get, Exception

#### `ƒ` `_guess_mime(image_path: str) -> str`  L42
  - 分支数 0，函数体节点数 43；return: {'.png': 'image/png', '.webp': 'image/webp', '.gif': 'image/gif', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg'}.get(ext, 'image/jpeg')
  - 调用: lower, splitext, get

#### `ƒ` `_to_data_url(image_path: str) -> str`  L53
  - 分支数 1，函数体节点数 47；return: f'data:{_guess_mime(image_path)};base64,{b64}'
  - 调用: open, decode, b64encode, read, _guess_mime
  - 文件IO: open (L54), read (L55)

#### `ƒ` `_poll_video_task(host: str, auth: str, task_id: str, max_attempts: int, interval: int) -> str`  L59
  - 分支数 3，函数体节点数 160；raise: Exception(f"MiniMax video task {task_id} failed: {base.get('status_code')} {base.get('status_msg')}"), Exception(f'MiniMax video task {task_id} timed out after {max_attempts} polls')；return: payload['file_id']
  - 调用: range, get, raise_for_status, json, Exception, _check_base_resp, sleep
  - 网络调用: get (L62)

#### `ƒ` `_retrieve_file_url(host: str, auth: str, file_id: str) -> str`  L86
  - 分支数 0，函数体节点数 67；return: payload['file']['download_url']
  - 调用: get, raise_for_status, json, _check_base_resp
  - 网络调用: get (L87)

#### `ƒ` `_download(url: str, output_file: str) -> None`  L99
  - 分支数 1，函数体节点数 53
  - 调用: get, raise_for_status, _ensure_output_dir, open, write
  - 网络调用: get (L100)
  - 文件IO: open (L103), write (L104)

#### `ƒ` `_generate_video_minimax(prompt: str, reference_images: list[str], output_file: str) -> str`  L107
  - 分支数 2，函数体节点数 170；return: 'MINIMAX_API_KEY is not set', f'The video has been generated successfully to {output_file}'
  - 调用: getenv, _minimax_host, _to_data_url, post, raise_for_status, json, _check_base_resp, _poll_video_task, _retrieve_file_url, _download
  - 网络调用: post (L118)
  - 环境变量: getenv (L110), getenv (L115)

#### `ƒ` `download(url: str, output_file: str) -> None`  L134
  - 分支数 2，函数体节点数 77；raise: ValueError('GEMINI_API_KEY is not set')
  - 调用: getenv, ValueError, get, raise_for_status, _ensure_output_dir, open, write
  - 网络调用: get (L138)
  - 文件IO: open (L141), write (L142)
  - 环境变量: getenv (L135)

#### `ƒ` `_generate_video_gemini(prompt: str, reference_images: list[str], output_file: str) -> str`  L145
  - 分支数 6，函数体节点数 246；return: 'GEMINI_API_KEY is not set', f'The video has been generated successfully to {output_file}'
  - 调用: open, decode, b64encode, read, append, getenv, post, raise_for_status, json, get, download, sleep
  - 网络调用: post (L162), get (L172)
  - 文件IO: open (L151), read (L152)
  - 环境变量: getenv (L159)

#### `ƒ` `generate_video(prompt_file: str, reference_images: list[str], output_file: str, aspect_ratio: str) -> str`  L187
  - 分支数 3，函数体节点数 103；raise: ValueError(f"Unknown video provider: {provider!r} (use 'gemini' or 'minimax')")；return: _generate_video_minimax(prompt, reference_images, output_file), _generate_video_gemini(prompt, reference_images, output_file)
  - 调用: open, read, _resolve_provider, bool, getenv, _generate_video_minimax, _generate_video_gemini, ValueError
  - 文件IO: open (L193), read (L194)
  - 环境变量: getenv (L196)

## 文件内调用关系
- `_to_data_url` -> _guess_mime
- `_poll_video_task` -> _check_base_resp
- `_retrieve_file_url` -> _check_base_resp
- `_download` -> _ensure_output_dir
- `_generate_video_minimax` -> _minimax_host, _to_data_url, _check_base_resp, _poll_video_task, _retrieve_file_url, _download
- `download` -> _ensure_output_dir
- `_generate_video_gemini` -> download
- `generate_video` -> _resolve_provider, _generate_video_minimax, _generate_video_gemini
