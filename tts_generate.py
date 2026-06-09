"""
山城夏影 - 豆包 TTS 批量生成脚本 (HTTP Chunked 版本)
"""
import os, re, json, asyncio, sys
from collections import defaultdict

import httpx

# ── 配置 ──
API_URL = "https://openspeech.bytedance.com/api/v3/tts/unidirectional"
APP_ID = "1444978255"
ACCESS_KEY = "KZUtzY_6hwW3CyaKTbg_Dwg8R5kur8VP"
RESOURCE_ID = "seed-tts-2.0"

GAME = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(GAME, "game", "script.rpy")
VOICE_DIR = os.path.join(GAME, "game", "audio", "voice")

# 音色映射 - 使用已在控制台添加的音色
VOICE_TYPE_MAP = {
    "anya": "saturn_zh_female_keainvsheng_tob",          # 可爱女生2.0
    "我": "zh_male_taocheng_uranus_bigtts",          # 小天2.0
    "老板娘": "zh_female_vv_uranus_bigtts",           # Vivi 2.0
    "厂长": "zh_male_m191_uranus_bigtts",             # 云舟2.0
    "王老板": "zh_male_m191_uranus_bigtts",            # 云舟2.0
    "服务员": "zh_female_xiaohe_uranus_bigtts",        # 小何2.0
    "快递员": "zh_male_m191_uranus_bigtts",            # 云舟2.0
    "站长": "zh_male_m191_uranus_bigtts",              # 云舟2.0
    "主持人": "zh_female_xiaohe_uranus_bigtts",        # 小何2.0
    "王总": "zh_male_taocheng_uranus_bigtts",          # 小天2.0
}

DIALECT_MAP = {
    "老板娘": "sichuan",
}


async def generate_one(text: str, speaker: str, dialect: str = None) -> tuple:
    """调用豆包 HTTP API 生成单句音频"""
    additions = {}
    if dialect:
        additions["explicit_dialect"] = dialect

    req_body = {
        "user": {"uid": "galgame"},
        "req_params": {
            "text": text,
            "speaker": speaker,
            "audio_params": {
                "format": "mp3",
                "sample_rate": 24000,
            },
        }
    }
    if additions:
        req_body["req_params"]["additions"] = json.dumps(additions, ensure_ascii=False)

    headers = {
        "X-Api-App-Id": APP_ID,
        "X-Api-Access-Key": ACCESS_KEY,
        "X-Api-Resource-Id": RESOURCE_ID,
        "Content-Type": "application/json",
    }

    audio_chunks = []
    error_msg = None

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            async with client.stream("POST", API_URL, json=req_body, headers=headers) as resp:
                if resp.status_code != 200:
                    body = await resp.aread()
                    error_msg = f"HTTP {resp.status_code}: {body.decode('utf-8', errors='replace')[:200]}"
                else:
                    # 响应是 chunked JSON：{"code":0,"data":"base64..."}{"code":20000000,"message":"OK","data":null}
                    body = await resp.aread()
                    text = body.decode('utf-8')
                    import base64
                    # 拆出所有 {} 级别的 JSON 对象
                    depth = 0
                    start = 0
                    for i, ch in enumerate(text):
                        if ch == '{':
                            if depth == 0:
                                start = i
                            depth += 1
                        elif ch == '}':
                            depth -= 1
                            if depth == 0:
                                chunk = text[start:i+1]
                                try:
                                    obj = json.loads(chunk)
                                    if obj.get("code") == 0 and obj.get("data"):
                                        audio_chunks.append(base64.b64decode(obj["data"]))
                                except:
                                    pass
                    if not audio_chunks:
                        error_msg = f"No audio in response: {text[:200]}"
    except Exception as e:
        error_msg = str(e)

    if error_msg:
        return None, error_msg
    if not audio_chunks:
        return None, "No audio received"
    return b"".join(audio_chunks), None


def extract_dialogues():
    """提取所有需要配音的台词"""
    dialogues = []
    with open(SCRIPT, encoding="utf-8") as f:
        lines = f.readlines()

    char_keys = {'anya', '我', '老板娘', '厂长', '王老板', '服务员',
                 '快递员', '站长', '主持人', '王总'}

    for i, line in enumerate(lines, 1):
        m = re.match(r'^(\s+)(\S+)\s+"(.+)"', line)
        if m:
            key = m.group(2)
            if key in char_keys:
                text = m.group(3)
                if text.startswith('（') and text.endswith('）'):
                    continue
                dialogues.append({'line': i, 'char_key': key, 'text': text})
    return dialogues


def rename_npc(char_key):
    m = {
        '老板娘': 'boss_lady', '厂长': 'factory_mgr', '王老板': 'boss_wang',
        '服务员': 'waiter', '快递员': 'courier', '站长': 'station_mgr',
        '主持人': 'host', '王总': 'president_wang',
    }
    return m.get(char_key, char_key)


async def main():
    os.makedirs(VOICE_DIR, exist_ok=True)
    dialogues = extract_dialogues()

    if "--test" in sys.argv:
        # 用第2句安雅有意义的台词测试
        for d in dialogues:
            if d['char_key'] == 'anya' and len(d['text']) > 5:
                speaker = VOICE_TYPE_MAP.get(d['char_key'])
                print(f"Testing: {d['char_key']} voice={speaker}")
                print(f"  text='{d['text']}'")
                dialect = DIALECT_MAP.get(d['char_key'])
                audio, err = await generate_one(d['text'], speaker, dialect)
                if err:
                    print(f"[FAIL] {err}")
                else:
                    out = os.path.join(VOICE_DIR, "test_output.mp3")
                    with open(out, "wb") as f:
                        f.write(audio)
                    print(f"[OK] {len(audio)} bytes -> {out}")
                return
        print("[SKIP] No long enough Anya dialogue found")

    elif "--batch" in sys.argv:
        total = len(dialogues)
        print(f"Batch: {total} dialogues to generate")
        counter = defaultdict(int)
        success = 0
        fail = 0

        for idx, d in enumerate(dialogues, 1):
            speaker = VOICE_TYPE_MAP.get(d['char_key'])
            if not speaker:
                print(f"  [{idx}/{total}] SKIP {d['char_key']}: no voice")
                fail += 1
                continue

            counter[d['char_key']] += 1
            key = rename_npc(d['char_key']) if d['char_key'] not in ('anya', '我') else d['char_key']
            fname = f"{key}_{counter[d['char_key']]:04d}.mp3"
            out_path = os.path.join(VOICE_DIR, fname)

            if os.path.exists(out_path):
                print(f"  [{idx}/{total}] SKIP {fname} (exists)")
                success += 1
                continue

            dialect = DIALECT_MAP.get(d['char_key'])
            audio, err = await generate_one(d['text'], speaker, dialect)
            if err:
                print(f"  [{idx}/{total}] FAIL {fname}: {err}")
                fail += 1
            else:
                with open(out_path, "wb") as f:
                    f.write(audio)
                print(f"  [{idx}/{total}] OK {fname} ({len(audio)} bytes)")
                success += 1

            if idx % 10 == 0:
                await asyncio.sleep(0.3)

        print(f"\nDone! Success: {success}, Fail: {fail}")

        # 生成 voice 语句插入提示
        print("\n=== 接下来操作 ===")
        print("运行下面的命令在 script.rpy 中插入 voice 语句：")
        print("  python tts_insert_voice.py")

    else:
        print("Usage:")
        print("  python tts_generate.py --test")
        print("  python tts_generate.py --batch")
        role_count = defaultdict(int)
        for d in dialogues:
            role_count[d['char_key']] += 1
        print(f"\n{dialogues} dialogues total")
        for k, v in sorted(role_count.items(), key=lambda x: -x[1]):
            print(f"  {k}: {v} -> {VOICE_TYPE_MAP.get(k, '?')}")


if __name__ == "__main__":
    asyncio.run(main())