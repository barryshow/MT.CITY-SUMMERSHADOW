"""
山城夏影 - 新增分支 TTS 批量生成脚本
为所有 _new 后缀的 voice 文件生成配音
"""
import os, re, json, asyncio, base64
import httpx

API_URL = "https://openspeech.bytedance.com/api/v3/tts/unidirectional"
APP_ID = "1444978255"
ACCESS_KEY = "KZUtzY_6hwW3CyaKTbg_Dwg8R5kur8VP"
RESOURCE_ID = "seed-tts-2.0"

GAME = os.path.dirname(os.path.abspath(__file__))
VOICE_DIR = os.path.join(GAME, "game", "audio", "voice")

VOICE_TYPE_MAP = {
    "anya": "saturn_zh_female_keainvsheng_tob",
    "我": "zh_male_taocheng_uranus_bigtts",
    "王总": "zh_male_taocheng_uranus_bigtts",
}

def strip_stage_dir(text):
    """Remove leading （...） stage direction from spoken text"""
    text = text.strip()
    m = re.match(r'^（[^）]*）\s*(.*)', text)
    if m:
        return m.group(1).strip()
    return text

async def generate_one(text, speaker, retry=3):
    for attempt in range(retry):
        req_body = {
            "user": {"uid": "galgame"},
            "req_params": {
                "text": text, "speaker": speaker,
                "audio_params": {"format": "mp3", "sample_rate": 24000},
            }
        }
        headers = {
            "X-Api-App-Id": APP_ID,
            "X-Api-Access-Key": ACCESS_KEY,
            "X-Api-Resource-Id": RESOURCE_ID,
            "Content-Type": "application/json",
        }
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                async with client.stream("POST", API_URL, json=req_body, headers=headers) as resp:
                    if resp.status_code != 200:
                        body = await resp.aread()
                        if attempt < retry - 1:
                            await asyncio.sleep(2)
                            continue
                        return None, f"HTTP {resp.status_code}: {body.decode()[:200]}"
                    body = await resp.aread()
                    text_resp = body.decode('utf-8')
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
                                except: pass
                    if audio_data:
                        return audio_data, None
                    return None, f"Bad response: {text_resp[:100]}"
        except Exception as e:
            if attempt < retry - 1:
                await asyncio.sleep(3)
                continue
            return None, str(e)

async def main():
    os.makedirs(VOICE_DIR, exist_ok=True)

    # All new voice lines: (filename, character_key, dialogue_text)
    new_lines = [
        # ---- remake_dress ----
        ("me_0175_remake1.mp3", "我", "备用布料不是还有吗？一晚上做不完，我们就做一晚上。"),
        ("me_0175_remake2.mp3", "我", "我陪你通宵。钉珠子、剪线头，我都能干。"),
        ("anya_0324_new.mp3", "anya", "可是……「星夜」上面的刺绣光是我一个人就要一个月。"),
        ("me_0186_new.mp3", "我", "那就一起做。你负责刺绣和版型，我负责钉珠子、剪线头、熨烫。我们两个人，一晚上顶半个月。"),
        ("anya_0325_new.mp3", "anya", "……你真的愿意陪我疯？"),
        ("me_0187_new.mp3", "我", "你说呢？从漫展那天开始，我不一直都在陪你疯吗？"),
        ("anya_0326_new.mp3", "anya", "……也是。那开工吧。"),
        ("anya_0327_new.mp3", "anya", "林辰。"),
        ("anya_0327_new2.mp3", "anya", "从今以后，不管你要拍什么，我都给你当模特。"),
        ("me_0189_new.mp3", "我", "一言为定。"),

        # ---- reject_acquisition ----
        ("anya_0365_new.mp3", "anya", "对不起，王总。我不能接受。"),
        ("anya_0367_new.mp3", "anya", "我确定。这条路再难，也是我自己选的。"),

        # ---- accept_acquisition ----
        ("me_0212_new.mp3", "我", "安雅，五百万不是小数目。有了这笔钱，你可以用更好的布料，请更多的设计师。"),
        ("me_0212_new2.mp3", "我", "「暗夜蔷薇」是你一手做起来的，被收购不代表放弃。等你有了资源，还能把它做得更大。"),
        ("anya_0364_new.mp3", "anya", "你说得对……可是如果卖了，它就不完全是我的了。"),

        # ---- reject_low_ending ----
        ("anya_0391_new.mp3", "anya", "谢谢你能支持我的决定。"),
        ("me_0229_new.mp3", "我", "当然支持你。这是你的品牌。"),
        ("anya_0392_new.mp3", "anya", "林辰，好久不见。"),
        ("me_0230_new.mp3", "我", "是啊，好久不见。你还好吗？"),
        ("anya_0393_new.mp3", "anya", "还好。品牌小，但能活下去。你呢？"),
        ("me_0231_new.mp3", "我", "老样子。上班，拍照，偶尔接点私单。"),
        ("anya_0394_new.mp3", "anya", "林辰，谢谢你。那个夏天，我会一直记得。"),
        ("me_0232_new.mp3", "我", "我也是。如果以后需要摄影师，随时找我。"),
        ("anya_0395_new.mp3", "anya", "好。一言为定。"),

        # ---- accept_perfect_ending ----
        ("anya_0365_accept.mp3", "anya", "好。我接受。"),
        ("anya_0366_new.mp3", "anya", "林辰，我把它卖了。"),
        ("me_0212_new3.mp3", "我", "卖了也好。你现在是星辰的设计总监了，不用再一个人扛所有事。"),
        ("me_0212_new4.mp3", "我", "而且——不管品牌叫什么名字，设计师还是你。"),
        ("anya_0367_accept.mp3", "anya", "那你呢？你愿意跟我一起去星辰吗？"),
        ("anya_0368_new.mp3", "anya", "我做设计总监，你做摄影总监。我们在一起工作。"),
        ("me_0213_new.mp3", "我", "从漫展那天开始，我就没想过去别的地方。"),
        ("anya_0378_new.mp3", "anya", "林辰，下季度的拍摄方案你看了没有？"),
        ("me_0217_new.mp3", "我", "看了。不过我觉得咱们还是得去重庆拍一次外景。"),
        ("anya_0379_new.mp3", "anya", "为什么？"),
        ("me_0218_new.mp3", "我", "因为那是我们故事开始的地方。"),
        ("anya_0380_new.mp3", "anya", "……你真是，什么时候都忘不了那个夏天。"),
        ("me_0219_new.mp3", "我", "当然忘不了。那个夏天我遇到了你，偷拍了一张照片，然后整个人生都变了。"),
        ("anya_0380_new2.mp3", "anya", "我的也是。"),

        # ---- accept_normal_ending ----
        ("anya_0381_new.mp3", "anya", "我接受。"),
        ("anya_0382_new.mp3", "anya", "林辰，我是不是做了一个很懦弱的选择？"),
        ("me_0221_new.mp3", "我", "不。你做了一个很现实的选择。这没有错。"),
        ("me_0222_new.mp3", "我", "而且——不管品牌卖不卖，你还是你。"),
        ("anya_0384_new.mp3", "anya", "好久不见。"),
        ("me_0224_new.mp3", "我", "大忙人，终于舍得约我出来了？"),
        ("anya_0385_new.mp3", "anya", "少来。我很想你。"),
        ("anya_0386_new.mp3", "anya", "林辰，虽然品牌卖了，但我们还在。"),
        ("anya_0387_new.mp3", "anya", "等这阵忙完，我们一起去南山看星星吧。就我们俩。"),
        ("me_0225_new.mp3", "我", "好。我等你说这句话很久了。"),
        ("anya_0388_new.mp3", "anya", "你说，如果当初我没有接受收购，我们会是什么样？"),
        ("me_0226_new.mp3", "我", "大概会穷一点、累一点。但该在一起的，还是会在一起。"),
        ("anya_0389_new.mp3", "anya", "嘴这么甜，是不是又偷拍我了？"),
        ("me_0227_new.mp3", "我", "我光明正大地拍。"),

        # ---- 修改的台词：me_0209（原文"别紧张..." → "这几个月你熬了多少个通宵..."） ----
        ("me_0209.mp3", "我", "这几个月你熬了多少个通宵，为的不就是今天吗？"),

        # ---- 补全缺失的配音 ----
        ("me_0175_alt.mp3", "我", "先去快递中转站，一定能在今天晚上把样衣找回来。"),
        ("me_0188_new.mp3", "我", "我就说吧。"),
    ]

    success, fail = 0, 0
    for fname, char_key, text in new_lines:
        fpath = os.path.join(VOICE_DIR, fname)
        if os.path.exists(fpath):
            print(f"  SKIP {fname} (exists)")
            success += 1
            continue

        speaker = VOICE_TYPE_MAP.get(char_key)
        if not speaker:
            print(f"  SKIP {fname}: no voice for {char_key}")
            fail += 1
            continue

        print(f"  {fname} ({char_key}): '{text[:40]}...'")
        audio, err = await generate_one(text, speaker)
        if err:
            print(f"    -> FAIL: {err}")
            fail += 1
        else:
            with open(fpath, "wb") as f:
                f.write(audio)
            print(f"    -> OK ({len(audio)} bytes)")
            success += 1

        if (success + fail) % 10 == 0:
            await asyncio.sleep(0.3)

    print(f"\nDone: {success} success, {fail} failed")

if __name__ == "__main__":
    asyncio.run(main())