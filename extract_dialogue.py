"""提取 script.rpy 中所有对话台词"""
import re, os

GAME = r'D:\shanchengxiaying\shanchengxiaying\game'
SCRIPT = os.path.join(GAME, 'script.rpy')

with open(SCRIPT, encoding='utf-8') as f:
    lines = f.readlines()

# 角色定义映射：对话角色标识 -> 显示名称
CHARACTERS = {
    'anya': '安雅',
    '我': '林辰',
    '老板娘': '老板娘',
    '厂长': '厂长',
    '王老板': '王老板',
    '服务员': '服务员',
    '快递员': '快递员',
    '站长': '站长',
    '主持人': '主持人',
    '王总': '王总',
}

# 提取对话行：\t角色 "台词"
dialogues = []
for i, line in enumerate(lines, 1):
    # 匹配缩进 + 角色名 + 英文引号台词
    m = re.match(r'^(\s+)(\S+)\s+"(.+)"', line)
    if m:
        char_key = m.group(2)
        if char_key in CHARACTERS:
            text = m.group(3)
            # 跳过纯括号心理描写（以（开头或以）结尾的心理活动）
            # 但保留既有括号又有台词的混合句（极少）
            is_inner_thought = text.startswith('（') and text.endswith('）')
            dialogues.append({
                'line': i,
                'char_key': char_key,
                'char_name': CHARACTERS[char_key],
                'text': text,
                'is_thought': is_inner_thought,
            })

# 输出统计
total = len(dialogues)
voiced = [d for d in dialogues if not d['is_thought']]
thoughts = [d for d in dialogues if d['is_thought']]

# 按角色统计
from collections import Counter
role_counts = Counter(d['char_name'] for d in voiced)

print(f"=== 台词提取报告 ===")
print(f"总对话行（含心理描写）：{total}")
print(f"需要配音的台词：{len(voiced)}")
print(f"心理描写（不配音）：{len(thoughts)}")
print()
print("--- 各角色配音台词数 ---")
for name, count in sorted(role_counts.items(), key=lambda x: -x[1]):
    print(f"  {name}: {count} 句")
print()

# 输出前 20 行作为样例
print("--- 样例（前10句需要配音的） ---")
for d in voiced[:10]:
    print(f"  L{d['line']:4d}  {d['char_name']}: {d['text'][:60]}{'...' if len(d['text'])>60 else ''}")

print()
print(f"--- 心理描写样例（不配音，前5句） ---")
for d in thoughts[:5]:
    print(f"  L{d['line']:4d}  {d['char_name']}:（心理活动）{d['text'][:60]}{'...' if len(d['text'])>60 else ''}")

# 估算字符数
total_chars = sum(len(d['text']) for d in voiced)
print(f"\n--- 字符估算 ---")
print(f"需要配音的总字符数（含标点）：{total_chars}")
print(f"约需 Token：~{total_chars} 字符（豆包按字符计费）")
print()
print(f"建议文件名命名方案：")
print(f"  audio/voice/anya_001.wav, anya_002.wav, ...")
print(f"  audio/voice/me_001.wav, me_002.wav, ...")
