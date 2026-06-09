"""
在 script.rpy 中插入 voice 语句
每句对话前添加 voice "audio/voice/xxx_xxxx.mp3"
"""
import os, re
from collections import defaultdict

GAME = r'D:\shanchengxiaying\shanchengxiaying\game'
SCRIPT = os.path.join(GAME, 'script.rpy')
BACKUP = SCRIPT + '.bak'

VOICE_TYPE_MAP = {
    "anya": "anya",
    "我": "我",
    "老板娘": "boss_lady",
    "厂长": "factory_mgr",
    "王老板": "boss_wang",
    "服务员": "waiter",
    "快递员": "courier",
    "站长": "station_mgr",
    "主持人": "host",
    "王总": "president_wang",
}

with open(SCRIPT, encoding='utf-8') as f:
    lines = f.readlines()
    original = lines[:]

# 先备份
if not os.path.exists(BACKUP):
    with open(BACKUP, 'w', encoding='utf-8') as f:
        f.writelines(original)
    print(f"[OK] Backup saved: {BACKUP}")

# 统计已有 voice 语句
existing_voice_count = sum(1 for l in lines if l.strip().startswith('voice '))
print(f"Existing voice statements: {existing_voice_count}")

# 逐行处理：找到对话行时在其前面插入 voice 语句
counter = defaultdict(int)
new_lines = []
inserted = 0
char_keys = {'anya', '我', '老板娘', '厂长', '王老板', '服务员',
             '快递员', '站长', '主持人', '王总'}

for line in lines:
    m = re.match(r'^(\s+)(\S+)\s+"(.+)"', line)
    if m:
        key = m.group(2)
        if key in char_keys:
            text = m.group(3)
            # 跳过纯括号心理描写
            if text.startswith('（') and text.endswith('）'):
                new_lines.append(line)
                continue
            counter[key] += 1
            fn_key = VOICE_TYPE_MAP[key]
            fname = f"{fn_key}_{counter[key]:04d}.mp3"
            # 使用与对话行相同的缩进（保留原始缩进格式）
            orig_indent = re.match(r'^(\s+)', line)
            indent = orig_indent.group(1) if orig_indent else '\t'
            voice_line = f'{indent}voice "audio/voice/{fname}"\n'

            # 检查是否已有 voice 语句（避免重复插入）
            # 看上一行是不是 voice 语句
            if new_lines and new_lines[-1].strip().startswith('voice '):
                # 替换已有的 voice 语句路径
                new_lines[-1] = voice_line
                inserted += 1
            else:
                new_lines.append(voice_line)
                inserted += 1
            new_lines.append(line)
            continue
    new_lines.append(line)

# 写回
with open(SCRIPT, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"[OK] Inserted/updated {inserted} voice statements")
print(f"[OK] Written to {SCRIPT}")