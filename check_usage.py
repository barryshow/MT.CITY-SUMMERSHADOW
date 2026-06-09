"""Analyse CG and BG registration vs usage in script.rpy"""
import os, re

GAME = r'D:\shanchengxiaying\shanchengxiaying\game'
SCRIPT = os.path.join(GAME, 'script.rpy')

with open(SCRIPT, encoding='utf-8') as f:
    text = f.read()

# CG images registered in init python
cg_registered = set()
m = re.search(r'_cg_images\s*=\s*\[(.*?)\]', text, re.DOTALL)
if m:
    cg_registered = set(re.findall(r'"(cg_\w+)"', m.group(1)))
print('CG registered in init:', sorted(cg_registered))

cg_scened = set(re.findall(r'scene\s+(cg_\w+)', text))
print('CG used in scene:', sorted(cg_scened))

cg_disk = set()
for f in os.listdir(os.path.join(GAME, 'images', 'cg')):
    if f.endswith(('.png', '.jpg', '.jpeg')):
        cg_disk.add(f.rsplit('.', 1)[0])
print('CG on disk:', sorted(cg_disk))

issues = []
for sn in sorted(cg_scened):
    if sn not in cg_registered:
        issues.append(f'[WARN] scene {sn} used but NOT in init python registry')
    if sn not in cg_disk:
        issues.append(f'[MISS] scene {sn} used but no file on disk')

for fn in sorted(cg_disk):
    if fn not in cg_scened:
        issues.append(f'[EXTRA] {fn} on disk but never used in scene command')

print()
print('--- CG Issues ---')
for i in issues:
    print(i)

# BG
bg_registered = set()
m = re.search(r'_bg_images\s*=\s*\[(.*?)\]', text, re.DOTALL | re.MULTILINE)
if m:
    bg_registered = set(re.findall(r'"(bg_\w+)"', m.group(1)))

bg_scened = set(re.findall(r'scene\s+(bg_\w+)', text))

bg_disk = set()
bgdir = os.path.join(GAME, 'images', 'backgrounds')
for f in os.listdir(bgdir):
    if f.endswith(('.png', '.jpg', '.jpeg')):
        bg_disk.add(f.rsplit('.', 1)[0])

print()
print('--- BG Issues ---')
for sn in sorted(bg_scened):
    if sn not in bg_registered:
        print(f'[WARN] scene {sn} used but NOT in init python registry')
    if sn not in bg_disk:
        print(f'[MISS] scene {sn} used but NO file')

for fn in sorted(bg_disk):
    if fn.startswith('bg_') and fn not in bg_registered and fn not in bg_scened:
        print(f'[EXTRA] {fn} on disk but never used')

# Weather
print()
print('--- Weather Issues ---')
weather_registered = set()
m = re.search(r'_weather_images\s*=\s*\[(.*?)\]', text, re.DOTALL | re.MULTILINE)
if m:
    weather_registered = set(re.findall(r'"(weather_\w+)"', m.group(1)))
    print('Registered:', sorted(weather_registered))

weather_shown = set(re.findall(r'show\s+(weather_\w+)', text))
print('Used in show:', sorted(weather_shown))

weather_disk = set()
for f in os.listdir(os.path.join(GAME, 'images', 'backgrounds')):
    if f.startswith('weather_') and f.endswith(('.png', '.jpg', '.jpeg')):
        weather_disk.add(f.rsplit('.', 1)[0])
print('On disk:', sorted(weather_disk))

# Check for registered but missing files
for w in sorted(weather_registered):
    if w not in weather_disk:
        print(f'[MISS] {w} registered but no .png file')

# Check eg. show 老板娘 - show without at clause line 603
print()
print("--- Script count ---")
total_lines = 0
with open(SCRIPT, encoding='utf-8') as f:
    for _ in f:
        total_lines += 1
print(f'Total lines in script.rpy: {total_lines}')
