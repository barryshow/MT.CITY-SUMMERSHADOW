#!/usr/bin/env python3
"""
直接处理立绘背景：逐个用rembg移除，替换原文件
"""
import os
import shutil
from pathlib import Path
from PIL import Image
import numpy as np
from rembg import remove
import sys

# 配置路径
CHARS_DIR = Path(r"D:\shanchengxiaying\shanchengxiaying\game\images\characters")
BACKUP_DIR = Path(r"D:\shanchengxiaying\shanchengxiaying\game\images\characters_backup")

BACKUP_DIR.mkdir(exist_ok=True)

def has_transparent_channel(image_path):
    """检查图片是否已有透明通道"""
    try:
        img = Image.open(image_path).convert('RGBA')
        alpha = np.array(img)[:,:,3]
        transparent_ratio = np.sum(alpha < 255) / alpha.size
        return transparent_ratio > 0.05  # 超过5%透明像素视为已处理
    except:
        return False

def process_image(input_path):
    """用rembg移除背景，返回处理后的二进制数据"""
    try:
        with open(input_path, 'rb') as f:
            input_data = f.read()
        output_data = remove(input_data)
        return output_data
    except Exception as e:
        print(f"    错误: {e}")
        return None

# 扫描所有立绘
all_files = sorted(CHARS_DIR.glob("*.png"))
print(f"找到 {len(all_files)} 个PNG文件\n")

needs_processing = []
already_done = []

for img_file in all_files:
    if has_transparent_channel(img_file):
        already_done.append(img_file.name)
    else:
        needs_processing.append(img_file)

print(f"✓ 已处理: {len(already_done)} 个")
print(f"✗ 需要处理: {len(needs_processing)} 个\n")

if not needs_processing:
    print("所有立绘都已处理完毕!")
    sys.exit(0)

print(f"开始处理 {len(needs_processing)} 个文件...\n")

processed = 0
failed = []

for i, img_file in enumerate(needs_processing, 1):
    filename = img_file.name
    backup_path = BACKUP_DIR / filename

    print(f"[{i}/{len(needs_processing)}] {filename}...", end=" ", flush=True)

    # 备份原文件
    if not backup_path.exists():
        shutil.copy2(img_file, backup_path)
        print("备份✓", end=" ", flush=True)
    else:
        print("已备份", end=" ", flush=True)

    # 处理背景
    output_data = process_image(img_file)
    if output_data:
        # 直接覆盖原文件
        with open(img_file, 'wb') as f:
            f.write(output_data)
        print("处理✓")
        processed += 1
    else:
        print("失败✗")
        failed.append(filename)

print(f"\n完成! 处理了 {processed}/{len(needs_processing)} 个文件")
if failed:
    print(f"失败: {', '.join(failed)}")
print(f"\n备份位置: {BACKUP_DIR}")
