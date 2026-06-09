import json

with open('translations_en.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

BS = chr(92)
DQ = chr(34)

lines = ['init python:', '    _en = {']
for item in data:
    zh = item['zh'].replace(BS, BS*2).replace(DQ, BS+DQ)
    en = item['en'].replace(BS, BS*2).replace(DQ, BS+DQ)
    lines.append(DQ*3 + zh + DQ*3 + ': ' + DQ*3 + en + DQ*3 + ',')

lines.append('    }')
text = '\n'.join(lines)

with open('game/translations.rpy', 'w', encoding='utf-8') as f:
    f.write(text)
print(f'Written: {len(lines)} lines, {len(data)} entries')