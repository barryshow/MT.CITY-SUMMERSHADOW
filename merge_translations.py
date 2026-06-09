"""
合并所有翻译chunk，生成 _en 字典，注入到 script.rpy 开头的 init python 块
"""

import json, os, re

BASE = r"D:\shanchengxiaying\shanchengxiaying"
CHUNK_DIR = os.path.join(BASE, "dialogue_all")
SCRIPT = os.path.join(BASE, "game", "script.rpy")

# 1. 合并所有 translated_X.json
all_translations = []
for i in range(10):
    path = os.path.join(CHUNK_DIR, f"translated_{i}.json")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            chunk = json.load(f)
        all_translations.extend(chunk)
        print(f"Loaded chunk {i}: {len(chunk)} lines")
    else:
        print(f"WARNING: chunk {i} not found yet")

print(f"\nTotal translations: {len(all_translations)}")

# 2. Check for duplicates
seen = {}
for item in all_translations:
    zh = item['zh']
    if zh in seen:
        print(f"DUPLICATE: {zh[:40]}...")
    seen[zh] = item

# 3. Write combined translation JSON
trans_path = os.path.join(BASE, "translations_en.json")
with open(trans_path, 'w', encoding='utf-8') as f:
    json.dump(all_translations, f, ensure_ascii=False, indent=2)
print(f"\nSaved: {trans_path}")

# 4. Generate _en dictionary injection code
dict_entries = []
for item in all_translations:
    zh = item['zh'].replace('\\', '\\\\').replace('"', '\\"')
    en = item['en'].replace('\\', '\\\\').replace('"', '\\"')
    dict_entries.append(f'    "{zh}": "{en}"')

dict_code = "init python:\n    _en = {\n" + ",\n".join(dict_entries) + "\n    }"

# 5. Inject into script.rpy
with open(SCRIPT, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the _en definition or add it after the first init python block
_en_exists = 'en_text = _t' in content or '_en = {' in content
if _en_exists:
    print("Translation dict already exists in script.rpy (update in place)")
else:
    print("\nReady to inject. Run merge step 2 when all chunks are complete.")
    print(f"Dictionary size: {len(dict_entries)} entries")
    print(f"Estimated file size: ~{len(dict_code.encode('utf-8')) / 1024:.0f} KB")