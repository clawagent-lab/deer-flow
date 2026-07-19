# `skills/public/ppt-generation/scripts/generate.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/ppt-generation/scripts/generate.py`  ·  行数: 162

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: json, os
- `io` -> BytesIO
- `PIL` -> Image
- `pptx` -> Presentation
- `pptx.util` -> Inches

## 函数
#### `ƒ` `generate_ppt(plan_file: str, slide_images: list[str], output_file: str) -> str`  L10
  - _文档首行_（仅供参考）: Generate a PowerPoint presentation from slide images.
  - 分支数 15，函数体节点数 558；return: f'Error: Slide image not found: {image_path}', f'Successfully generated presentation with {len(slide_images)} slides to {output_file}'
  - 调用: open, load, get, Inches, Presentation, enumerate, exists, add_slide, convert, int, BytesIO, save, seek, add_picture, len, append, join
  - 文件IO: open (L27), exists (L55), open (L62)

## 文件内调用关系
_无文件内调用_
