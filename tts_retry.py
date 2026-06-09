"""重试失败的TTS生成"""
import os, re, json, asyncio, sys
from collections import defaultdict
import httpx, base64

API_URL = "https://openspeech.bytedance.com/api/v3/tts/unidirectional"
APP_ID = "1444978255"
ACCESS_KEY = "KZUtzY_6hwW3CyaKTbg_Dwg8R5kur8VP"
RESOURCE_ID = "seed-tts-2.0"

GAME = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(GAME, "game", "script.rpy")
VOICE_DIR = os.path.join(GAME, "game", "audio", "voice")

VOICE_TYPE_MAP = {
    "anya": "saturn_zh_female_keainvsheng_tob",
    "我": "zh_male_taocheng_uranus_bigtts",
    "老板娘": "zh_female_vv_uranus_bigtts",
    "厂长": "zh_male_m191_uranus_bigtts",
    "王老板": "zh_male_m191_uranus_bigtts",
    "服务员": "zh_female_xiaohe_uranus_bigtts",
    "快递员": "zh_male_m191_uranus_bigtts",
    "站长": "zh_male_m191_uranus_bigtts",
    "主持人": "zh_female_xiaohe_uranus_bigtts",
    "王总": "zh_male_taocheng_uranus_bigtts",
    "收件人": "zh_male_m191_uranus_bigtts",
}

DIALECT_MAP = {"老板娘": "sichuan"}

def rename_npc(char_key):
    m = {
        '老板娘': 'boss_lady', '厂长': 'factory_mgr', '王老板': 'boss_wang',
        '服务员': 'waiter', '快递员': 'courier', '站长': 'station_mgr',
        '主持人': 'host', '王总': 'president_wang',
    }
    return m.get(char_key, char_key)


async def generate_one(text, speaker, dialect=None, retry=3):
    for attempt in range(retry):
        additions = {}
        if dialect:
            additions["explicit_dialect"] = dialect
        req_body = {
            "user": {"uid": "galgame"},
            "req_params": {
                "text": text, "speaker": speaker,
                "audio_params": {"format": "mp3", "sample_rate": 24000},
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

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                resp = await client.post(API_URL, json=req_body, headers=headers)
                if resp.status_code != 200:
                    if attempt < retry - 1:
                        await asyncio.sleep(2)
                        continue
                    return None, f"HTTP {resp.status_code}"
                body = resp.read()
                text_resp = body.decode('utf-8')
                # parse JSON chunks
                depth, start = 0, 0
                audio_data = None
                for i, ch in enumerate(text_resp):
                    if ch == '{':
                        if depth == 0: start = i
                        depth += 1
                    elif ch == '}':
                        depth -= 1
                        if depth == 0:
                            try:
                                obj = json.loads(text_resp[start:i+1])
                                if obj.get("code") == 0 and obj.get("data"):
                                    audio_data = base64.b64decode(obj["data"])
                            except:
                                pass
                if audio_data:
                    return audio_data, None
                # "No readable text" -> use a hack: add a space
                if "No readable text" in text_resp:
                    if attempt < retry - 1:
                        text = f"​{text}"  # zero-width space prefix
                        await asyncio.sleep(1)
                        continue
                    return None, "No readable text"
                return None, f"Bad response: {text_resp[:100]}"
        except Exception as e:
            if attempt < retry - 1:
                await asyncio.sleep(3)
                continue
            return None, str(e)


def find_missing():
    """Find which files should exist but don't"""
    missing = []
    counter = defaultdict(int)
    char_keys = {'anya', '我', '老板娘', '厂长', '王老板', '服务员',
                 '快递员', '站长', '主持人', '王总'}

    with open(SCRIPT, encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        m = re.match(r'^(\s+)(\S+)\s+"(.+)"', line)
        if m:
            key = m.group(2)
            if key in char_keys:
                text = m.group(3)
                if text.startswith('（') and text.endswith('）'):
                    continue
                counter[key] += 1
                fn_key = rename_npc(key) if key not in ('anya', '我') else key
                fname = f"{fn_key}_{counter[key]:04d}.mp3"
                fpath = os.path.join(VOICE_DIR, fname)
                if not os.path.exists(fpath):
                    missing.append((fname, key, text))
    return missing


async def main():
    os.makedirs(VOICE_DIR, exist_ok=True)
    missing = find_missing()
    print(f"Missing files: {len(missing)}")

    success, fail = 0, 0
    for fname, key, text in missing:
        speaker = VOICE_TYPE_MAP.get(key)
        if not speaker:
            print(f"  SKIP {fname}: no voice for {key}")
            fail += 1
            continue

        dialect = DIALECT_MAP.get(key)
        print(f"  {fname}: text='{text[:30]}'... voice={speaker}")
        audio, err = await generate_one(text, speaker, dialect)
        if err:
            print(f"    -> FAIL: {err}")
            fail += 1
        else:
            out = os.path.join(VOICE_DIR, fname)
            with open(out, "wb") as f:
                f.write(audio)
            print(f"    -> OK ({len(audio)} bytes)")
            success += 1

    print(f"\nDone: {success} success, {fail} failed")

    # Final count
    total = len([f for f in os.listdir(VOICE_DIR) if f.endswith('.mp3')])
    print(f"Total mp3 files: {total}")


if __name__ == "__main__":
    asyncio.run(main())
