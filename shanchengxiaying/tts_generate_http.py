#!/c/Python314/python
"""TTS generation via HTTP - 豆包语音合成 (新版控制台认证, HTTP streaming)"""
import json, os, re, base64, time, ssl, urllib.request
from collections import defaultdict

API_URL = "https://openspeech.bytedance.com/api/v3/tts/unidirectional"
API_KEY = "ark-2c4e8dcd-2967-4018-822a-6ba7d06a177a-0d471"
RESOURCE_ID = "seed-tts-2.0"
VOICE_DIR = "game/audio/voice"
LIST_FILE = "tts_generate_list.txt"
RATE_LIMIT = 0.3

HEADERS = {
    "X-Api-Key": API_KEY,
    "X-Api-Resource-Id": RESOURCE_ID,
    "Content-Type": "application/json; charset=utf-8",
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

def needs_tts(text):
    """Check if text needs real TTS (not just symbols)"""
    clean = re.sub(r'[（()）—…，。！？、；：""''\s]', '', text)
    clean = clean.replace('"', '').replace("'", '')
    return len(clean.strip()) > 0

def generate_one_sync(char_name, text, timeout=60):
    """Generate a single TTS audio via HTTP"""
    voice_type = VOICE_TYPES.get(char_name, "saturn_zh_female_keainvsheng_tob")

    payload = {
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
            "reqid": f"{char_name}_{int(time.time()*1000)}",
            "text": text,
            "text_type": "plain",
            "operation": "query",
        }
    }

    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(API_URL, data=data, headers=HEADERS, method='POST')
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        resp = urllib.request.urlopen(req, context=ctx, timeout=timeout)
        resp_data = json.loads(resp.read().decode('utf-8'))

        if resp_data.get('code') != 0:
            return None, f"API error: {resp_data.get('code')} - {resp_data.get('message', '')}"

        audio_b64 = resp_data.get('data')
        if not audio_b64:
            return None, "No audio data in response"

        audio = base64.b64decode(audio_b64)
        return audio, None
    except Exception as e:
        return None, str(e)

def generate_silent_placeholder(output_path):
    """Create a minimal silent MP3 for symbol-only lines"""
    silent = bytes([0xFF, 0xFB, 0x90, 0x00] + [0x00] * 413) * 15
    with open(output_path, 'wb') as f:
        f.write(silent)

def main():
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

    # Force regenerate ALL anya files
    pending = [(fid, char, text) for fid, char, text in items
               if char == 'anya' or not os.path.exists(os.path.join(VOICE_DIR, f"{fid}.mp3"))]
    print(f"Total: {len(items)}, Pending (only anya): {len([p for p in pending if p[1]=='anya'])}")

    if not pending:
        print("Nothing to generate!")
        return

    success = 0
    failed = 0
    silent_count = 0

    # Use urllib with SSL verification disabled
    print("HTTP client ready")

    for i, (fid, char, text) in enumerate(pending):
        out_path = os.path.join(VOICE_DIR, f"{fid}.mp3")
        print(f"[{i+1}/{len(pending)}] {fid}: \"{text[:40]}\"...", end=" ", flush=True)

        if not needs_tts(text):
            generate_silent_placeholder(out_path)
            silent_count += 1
            print("silent")
            continue

        try:
            audio, err = generate_one_sync(char, text)
            if err:
                failed += 1
                print(f"FAILED: {err}")
                time.sleep(2)
            else:
                with open(out_path, 'wb') as f:
                    f.write(audio)
                success += 1
                print(f"OK ({len(audio)} bytes)")
        except Exception as e:
            failed += 1
            print(f"ERROR: {e}")
            time.sleep(2)

        time.sleep(RATE_LIMIT)

    print(f"\nDone: {success} OK, {silent_count} silent, {failed} failed")

if __name__ == '__main__':
    main()
