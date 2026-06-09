"""
制作标题画面背景图：从 cg_fireflies.png 生成，叠加暗色渐变确保文字可读
"""
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os, math

SRC = r"D:\shanchengxiaying\shanchengxiaying\game\images\cg\cg_fireflies.png"
DST = r"D:\shanchengxiaying\shanchengxiaying\game\gui\main_menu.png"
DST_OVERLAY = r"D:\shanchengxiaying\shanchengxiaying\game\gui\overlay\main_menu.png"

# 打开原图
img = Image.open(SRC).convert('RGBA')
w, h = img.size
print(f"Source: {w}x{h}")

# 调整为 1280x720 (如果不等比例则裁剪中心)
target_w, target_h = 1280, 720

# 先裁剪为 16:9
src_ratio = w / h
target_ratio = target_w / target_h

if src_ratio > target_ratio:
    # 原图更宽，裁剪左右
    new_w = int(h * target_ratio)
    offset = (w - new_w) // 2
    img = img.crop((offset, 0, offset + new_w, h))
else:
    # 原图更高，裁剪上下
    new_h = int(w / target_ratio)
    offset = (h - new_h) // 2
    img = img.crop((0, offset, w, offset + new_h))

img = img.resize((target_w, target_h), Image.LANCZOS)
print(f"Resized to: {img.size}")

# 覆盖一层半透明暗色渐变（底部深色区域供文字阅读）
overlay = Image.new('RGBA', (target_w, target_h), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# 从 y=400 到 y=720 渐变加深
for y in range(400, target_h):
    alpha = int(50 + 155 * (y - 400) / (target_h - 400))
    draw.line([(0, y), (target_w, y)], fill=(0, 0, 0, alpha))

# 顶部也加一点暗色（让标题更明显）
for y in range(0, 160):
    alpha = int(120 * (1 - y / 160))
    draw.line([(0, y), (target_w, y)], fill=(0, 0, 0, alpha))

img = Image.alpha_composite(img, overlay)

# 保存主背景
img.save(DST, 'PNG')
print(f"Saved: {DST}")

# 生成 overlay（左侧菜单框用半透明底）
overlay2 = Image.new('RGBA', (420, target_h), (0, 0, 0, 140))
overlay2.save(DST_OVERLAY, 'PNG')
print(f"Saved: {DST_OVERLAY}")