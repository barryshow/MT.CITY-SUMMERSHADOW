#!/c/Python314/python
"""TTS generation via WebSocket - 豆包语音合成 (新版控制台认证)"""
import asyncio, json, uuid, os, re, time
from collections import defaultdict

API_URL = "wss://openspeech.bytedance.com/api/v3/tts/unidirectional/stream"
API_KEY = "ark-2c4e8dcd-2967-4018-822a-6ba7d06a177a-0d471"
RESOURCE_ID = "seed-tts-2.0"
VOICE_DIR = "game/audio/voice"
LIST_FILE = "tts_generate_list.txt"
RATE_LIMIT = 0.3

# 新版控制台只需 X-Api-Key + X-Api-Resource-Id
HEADERS = {
    "X-Api-Key": API_KEY,
    "X-Api-Resource-Id": RESOURCE_ID,
}

VOICE_TYPES = {
    "anya": "saturn_zh_female_keainvsheng_tob",
    "me": "zh_male_taocheng_uranus_bigtts",
    "boss_lady": "zh_female_vv_uranus_bigtts",
    "boss_wang": "zh_male_m191_uranus_bigtts",
    "courier": "zh_male_m191_uranus_bigtts",
    "station_mgr": "zh_male_m191_uranus_bigtts",
    "factory_mgr": "zh_male_m191_uranus_bigtts",
    "host": "zh_female_xiaohe_uranus_bigtts",
    "waiter": "zh_female_xiaohe_uranus_bigtts",
    "president_wang": "zh_male_taocheng_uranus_bigtts",
}

def build_frame(req):
    """Build WebSocket binary frame for TTS request"""
    payload = json.dumps(req, ensure_ascii=False).encode('utf-8')
    header = bytearray()
    header.append(0x81)  # text frame + FIN
    if len(payload) < 126:
        header.append(len(payload))
    elif len(payload) < 65536:
        header.append(126)
        header.extend(len(payload).to_bytes(2, 'big'))
    else:
        header.append(127)
        header.extend(len(payload).to_bytes(8, 'big'))
    return bytes(header) + payload

async def generate_one(ws, char_name, text):
    """Generate a single TTS audio via WebSocket"""
    voice_type = VOICE_TYPES.get(char_name, "saturn_zh_female_keainvsheng_tob")
    reqid = str(uuid.uuid4())

    req = {
        "app": {
            "appid": "1444978255",
            "token": "access_token",
            "cluster": "volcano_tts"
        },
        "user": {
            "uid": "1"
        },
        "audio": {
            "voice_type": voice_type,
            "encoding": "mp3",
            "speed_ratio": 1.0,
            "volume_ratio": 1.0,
            "pitch_ratio": 1.0,
        },
        "request": {
            "reqid": reqid,
            "text": text,
            "text_type": "plain",
            "operation": "query",
        }
    }

    frame = build_frame(req)
    await ws.send(frame)

    audio = bytearray()
    while True:
        msg = await asyncio.wait_for(ws.recv(), timeout=30)
        if isinstance(msg, bytes):
            # Check for header frame
            if len(msg) >= 2 and msg[0] & 0x80:
                payload_data = await ws.recv()
                if isinstance(payload_data, bytes):
                    audio.extend(payload_data)
                elif isinstance(payload_data, str):
                    resp = json.loads(payload_data)
                    if resp.get('code') == 0:
                        pass
            else:
                audio.extend(msg)
        else:
            try:
                resp = json.loads(msg)
                if resp.get('code') != 0:
                    return None, f"API error: {resp.get('code')} {resp.get('message', '')}"
                if resp.get('done') or resp.get('type') == 'done' or resp.get('duration'):
                    break
            except:
                pass

    if audio:
        return bytes(audio), None
    return None, "No audio data"

async def generate_silent_placeholder(output_path):
    """Create a minimal silent MP3 for symbol-only lines"""
    silent = bytes([0xFF, 0xFB, 0x90, 0x00] + [0x00] * 413) * 15
    with open(output_path, 'wb') as f:
        f.write(silent)

def needs_tts(text):
    """Check if text needs real TTS (not just symbols)"""
    clean = re.sub(r'[（()）—…，。！？、；："\"''\s]', '', text)
    return len(clean) > 0

async def main():
    import websockets

    # Read list
    items = []
    with open(LIST_FILE, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(' | ')
            if len(parts) >= 3:
                items.append((parts[0].strip(), parts[1].strip(), ' | '.join(parts[2:]).strip()))

    # Filter existing - force regenerate ALL anya files
    pending = [(fid, char, text) for fid, char, text in items
               if char == 'anya' or not os.path.exists(os.path.join(VOICE_DIR, f"{fid}.mp3"))]
    print(f"Total: {len(items)}, Pending: {len(pending)}")

    if not pending:
        print("Nothing to generate!")
        return

    success = 0
    failed = 0
    silent_count = 0

    import ssl as ssl_mod
    ssl_ctx = ssl_mod.create_default_context()
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = ssl_mod.CERT_NONE
    async with websockets.connect(API_URL, additional_headers=HEADERS, max_size=10*1024*1024, ssl=ssl_ctx) as ws:
        print("WebSocket connected")

        for i, (fid, char, text) in enumerate(pending):
            out_path = os.path.join(VOICE_DIR, f"{fid}.mp3")
            print(f"[{i+1}/{len(pending)}] {fid}: \"{text[:40]}\"...", end=" ", flush=True)

            if not needs_tts(text):
                await generate_silent_placeholder(out_path)
                silent_count += 1
                print("silent")
                continue

            try:
                audio, err = await generate_one(ws, char, text)
                if err:
                    failed += 1
                    print(f"FAILED: {err}")
                    await asyncio.sleep(2)
                else:
                    with open(out_path, 'wb') as f:
                        f.write(audio)
                    success += 1
                    print(f"OK ({len(audio)} bytes)")
            except Exception as e:
                failed += 1
                print(f"ERROR: {e}")
                await asyncio.sleep(2)

            await asyncio.sleep(RATE_LIMIT)

    print(f"\nDone: {success} OK, {silent_count} silent, {failed} failed")

    still_missing = sum(1 for fid, _, _ in pending if not os.path.exists(os.path.join(VOICE_DIR, f"{fid}.mp3")))
    print(f"Still missing: {still_missing}")

if __name__ == '__main__':
    asyncio.run(main())
