#!/usr/bin/env python3
"""
批量处理立绘背景：检测黑白方块背景，用rembg移除
"""
import os
from pathlib import Path
from PIL import Image
import numpy as np
from rembg import remove
from datetime import datetime

# 配置路径
CHARS_DIR = Path(r"D:\shanchengxiaying\shanchengxiaying\game\images\characters")
BACKUP_DIR = Path(r"D:\shanchengxiaying\shanchengxiaying\game\images\characters_backup")
PROCESSED_DIR = Path(r"D:\shanchengxiaying\shanchengxiaying\game\images\characters_processed")

# 创建备份和处理目录
BACKUP_DIR.mkdir(exist_ok=True)
PROCESSED_DIR.mkdir(exist_ok=True)

def has_checkered_bg(image_path):
    """检测图片是否有黑白方块背景（透明度通道）"""
    try:
        img = Image.open(image_path).convert('RGBA')
        # 检查是否已有透明通道
        alpha = np.array(img)[:,:,3]

        # 如果透明度通道几乎全是255（不透明），说明没有处理过
        transparent_ratio = np.sum(alpha < 255) / alpha.size

        # 如果透明度少于5%，可能就是黑白方块背景
        if transparent_ratio < 0.05:
            return True, "no_alpha"

        return False, "has_alpha"
    except Exception as e:
        return None, str(e)

def process_image(input_path, output_path):
    """用rembg移除背景"""
    try:
        with open(input_path, 'rb') as i:
            input_data = i.read()
        output_data = remove(input_data)
        with open(output_path, 'wb') as o:
            o.write(output_data)
        return True, "success"
    except Exception as e:
        return False, str(e)

def backup_image(src, dst):
    """备份原始文件"""
    try:
        import shutil
        shutil.copy2(src, dst)
        return True
    except Exception as e:
        return False, str(e)

# 扫描所有立绘
print(f"开始扫描立绘文件...")
print(f"目录: {CHARS_DIR}\n")

all_files = sorted(CHARS_DIR.glob("*.png"))
print(f"找到 {len(all_files)} 个PNG文件\n")

needs_processing = []
already_processed = []
errors = []

for img_file in all_files:
    has_bg, reason = has_checkered_bg(img_file)

    if has_bg is None:
        errors.append((img_file.name, reason))
    elif has_bg:
        needs_processing.append(img_file.name)
    else:
        already_processed.append(img_file.name)

print(f"✓ 已处理（有透明通道）: {len(already_processed)} 个")
if already_processed[:5]:
    print(f"  示例: {', '.join(already_processed[:5])}\n")

print(f"✗ 需要处理（黑白方块背景）: {len(needs_processing)} 个")
if needs_processing:
    print(f"  {', '.join(needs_processing[:10])}")
    if len(needs_processing) > 10:
        print(f"  ... 还有 {len(needs_processing)-10} 个\n")

if errors:
    print(f"⚠ 读取错误: {len(errors)} 个")
    for fname, err in errors[:3]:
        print(f"  {fname}: {err}\n")

# 如果有需要处理的文件
if needs_processing:
    print(f"\n开始处理 {len(needs_processing)} 个文件...\n")

    processed_count = 0
    for i, filename in enumerate(needs_processing, 1):
        src_path = CHARS_DIR / filename
        backup_path = BACKUP_DIR / filename
        output_path = PROCESSED_DIR / filename

        print(f"[{i}/{len(needs_processing)}] {filename}...", end=" ", flush=True)

        # 备份原文件
        if not backup_path.exists():
            backup_image(src_path, backup_path)
            print("备份✓", end=" ", flush=True)
        else:
            print("已备份", end=" ", flush=True)

        # 处理背景
        success, msg = process_image(src_path, output_path)
        if success:
            print("处理✓")
            processed_count += 1
        else:
            print(f"失败: {msg}")

    print(f"\n完成! 处理了 {processed_count}/{len(needs_processing)} 个文件")
    print(f"输出目录: {PROCESSED_DIR}")
    print(f"备份目录: {BACKUP_DIR}")
else:
    print("\n所有立绘都已处理完毕!")
