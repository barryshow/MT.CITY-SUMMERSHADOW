#!/c/Python314/python
"""批量生成 TTS 配音 - SSE API 方式"""
import os, json, uuid, base64, re, time
import requests

API_URL = "https://openspeech.bytedance.com/api/v3/tts/unidirectional/sse"
VOICE_DIR = "game/audio/voice"
LIST_FILE = "tts_generate_list.txt"
RATE_LIMIT = 0.3

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer;KZUtzY_6hwW3CyaKTbg_Dwg8R5kur8VP",
    "X-Api-App-Id": "1444978255",
    "X-Api-Access-Key": "KZUtzY_6hwW3CyaKTbg_Dwg8R5kur8VP",
    "X-Api-Resource-Id": "seed-tts-2.0",
}

VOICE_MAP = {
    "anya":  "saturn_zh_female_keainvsheng_tob",
    "me":    "zh_male_taocheng_uranus_bigtts",
    "boss_lady":  "zh_female_vv_uranus_bigtts",
    "boss_wang":  "zh_male_m191_uranus_bigtts",
    "courier":    "zh_male_m191_uranus_bigtts",
    "station_mgr":"zh_male_m191_uranus_bigtts",
    "factory_mgr":"zh_male_m191_uranus_bigtts",
    "host":   "zh_female_xiaohe_uranus_bigtts",
    "waiter": "zh_female_xiaohe_uranus_bigtts",
    "president_wang": "zh_male_taocheng_uranus_bigtts",
}

def needs_tts(text):
    clean = re.sub(r'[（()）—…，。！？、；："\'\s]', '', text)
    return len(clean) > 0

def generate_silent_mp3(path):
    """纯标点符号的台词生成空白 MP3"""
    mp3 = bytes([0xFF, 0xFB, 0x90, 0x00] + [0x00] * 413) * 15
    with open(path, 'wb') as f:
        f.write(mp3)

def generate_one(char_name, text):
    """调用 SSE API 生成一条配音，返回 (mp3_bytes, error)"""
    speaker = VOICE_MAP.get(char_name, "saturn_zh_female_keainvsheng_tob")
    reqid = str(uuid.uuid4())

    payload = {
        "user": {"uid": "tts-batch"},
        "req_params": {
            "text": text,
            "speaker": speaker,
            "audio_params": {
                "format": "mp3",
                "sample_rate": 24000,
            }
        }
    }

    resp = requests.post(API_URL, headers={
        **HEADERS,
        "X-Api-Request-Id": reqid,
    }, json=payload, stream=True, timeout=120)

    if resp.status_code != 200:
        return None, f"HTTP {resp.status_code}: {resp.text[:200]}"

    chunks = []
    errors = []

    for line in resp.iter_lines(decode_unicode=True):
        if not line or not line.startswith("data:"):
            continue
        data_text = line[5:].strip()
        if not data_text:
            continue
        try:
            obj = json.loads(data_text)
        except Exception:
            continue

        code = obj.get("code")
        if code not in (0, 20000000, None):
            errors.append(f"code={code}: {obj.get('message','')}")

        raw = obj.get("data")
        if isinstance(raw, str) and raw:
            try:
                chunks.append(base64.b64decode(raw))
            except Exception as e:
                errors.append(f"base64 err: {e}")

    if chunks:
        return b"".join(chunks), None
    if errors:
        return None, "; ".join(errors)
    return None, "no audio data"

def main():
    # 读取待生成列表
    items = []
    with open(LIST_FILE, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(' | ')
            if len(parts) >= 3:
                items.append((parts[0].strip(), parts[1].strip(), ' | '.join(parts[2:]).strip()))

    # 过滤已存在的
    pending = [(fid, char, text) for fid, char, text in items
               if not os.path.exists(os.path.join(VOICE_DIR, f"{fid}.mp3"))]
    print(f"总数: {len(items)}, 待生成: {len(pending)}")

    if not pending:
        print("全部已生成完毕！")
        return

    success = 0
    failed = 0
    silent = 0

    for i, (fid, char, text) in enumerate(pending):
        out_path = os.path.join(VOICE_DIR, f"{fid}.mp3")
        short = text[:50].replace('\n', ' ')
        print(f"[{i+1}/{len(pending)}] {fid} ({char}): \"{short}\"...", end=" ", flush=True)

        if not needs_tts(text):
            generate_silent_mp3(out_path)
            silent += 1
            print("(silent)")
            continue

        audio, err = generate_one(char, text)
        if err:
            failed += 1
            print(f"FAILED: {err}")
        else:
            with open(out_path, 'wb') as f:
                f.write(audio)
            success += 1
            print(f"OK ({len(audio)} bytes)")

        time.sleep(RATE_LIMIT)

    print(f"\n{'='*40}")
    print(f"完成! {success} OK | {silent} silent | {failed} failed")
    still = sum(1 for fid,_,_ in pending if not os.path.exists(os.path.join(VOICE_DIR, f"{fid}.mp3")))
    print(f"仍缺失: {still}")

if __name__ == '__main__':
    main()
