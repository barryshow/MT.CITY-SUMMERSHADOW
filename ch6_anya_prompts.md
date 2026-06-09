## 第六章发布会立绘生成任务

### 当前占位说明
第六章所有发布会相关立绘目前临时映射到已有旧图（如 `anya_smile_smug` → 发布会穿星夜裙），需要新生成发布会专用版替换。

### 需要生成的图片（共6张+2张CG背景皮肤版）

---

## 1. anya_wear_starry_night_dress（发布会后台——化妆镜前全身立绘）

**文件路径：** `game/images/characters_alpha/anya_wear_starry_night_dress.png`

**提示词：**
```
anime style, visual novel character sprite, galgame style, full body character, transparent background, clean lineart, high quality, detailed, young woman with long blonde hair and green eyes, wearing a magnificent gothic lolita dress in dark navy blue with silver star embroidery and sequins, the dress has a full petticoat skirt and lace details, she is sitting in front of a dressing table mirror, holding a small makeup brush, looking slightly to the side through the mirror, proud yet nervous expression, lips slightly parted, detailed dress texture, no background, transparent background, full body standing pose
```

**替代方案**（如果 DALL-E 对透明背景生成效果不好，先生成带背景的再抠图）：
```
anime style, visual novel character sprite, galgame style, full body character, clean lineart, high quality, detailed, young woman with long blonde hair and green eyes, wearing a magnificent gothic lolita dress in dark navy blue with silver star embroidery and sequins, full petticoat skirt, sitting at vanity mirror, conference backstage room, warm lighting, golden hour, soft shadows, front facing but eyes looking towards mirror reflection, mixed nervous and determined expression
```

**说明：** 星夜主题连衣裙——深蓝底色，银河般银色星形刺绣和亮片装饰，多层蕾丝裙摆。

---

## 2. anya_walk_runway（T台走秀全身立绘）

**文件路径：** `game/images/characters_alpha/anya_walk_runway.png`

**提示词：**
```
anime style, visual novel character sprite, galgame style, full body character, transparent background, clean lineart, high quality, detailed, young woman with long blonde hair and green eyes, wearing a magnificent navy blue gothic lolita dress with silver star embroidery, full petticoat skirt spreading wide, one hand slightly lifting the skirt hem, walking forward with confident and elegant posture, chin slightly raised, proud smile, dress details including lace and silver thread shining, spotlight effect from above, no background, full body
```

---

## 3. anya_run_to_me（发布会结束后跑向主角的喜悦立绘）

**文件路径：** `game/images/characters_alpha/anya_run_to_me.png`

**提示词：**
```
anime style, visual novel character sprite, galgame style, full body character, transparent background, clean lineart, high quality, detailed, young woman with long blonde hair and green eyes, still wearing the navy blue gothic lolita starry night dress, running forward with both arms slightly open, huge happy smile on face, tears of joy in eyes, skirt and hair flowing dynamically from movement, excited and emotional expression, front facing running pose, no background, full body
```

---

## 4. anya_look_at_me（发布会台上与台下主角对视——半身/特写）

**文件路径：** `game/images/characters_alpha/anya_look_at_me.png`

**提示词：**
```
anime style, visual novel character sprite, galgame style, bust up portrait, transparent background, clean lineart, high quality, detailed, young woman with long blonde hair and green eyes, wearing navy blue gothic lolita dress with silver stars, spotlight lighting from above, looking directly at viewer with tender and grateful expression, eyes slightly shimmering, soft smile, gentle blush on cheeks, emotional moment, no background
```

---

## 5. 主角 me_walk_to_anya（发布会后台走向安雅）

如果也想增强男主在发布会场景的表现，可以生成一张替换 `me_walk_to_anya` 的专用图：

**文件路径：** `game/images/characters_alpha/me_walk_to_anya.png`

**提示词：**
```
anime style, visual novel character sprite, galgame style, full body character, transparent background, clean lineart, high quality, detailed, young Chinese college-age man with short black hair, wearing a smart casual outfit -- white button-up shirt with rolled sleeves and dark chinos, a camera hanging from his shoulder, walking forward with a gentle smile, confident but warm expression, no background, full body
```

---

## 6. me_put_hand_on_anya_shoulder（安慰紧张安雅）

**文件路径：** `game/images/characters_alpha/me_put_hand_on_anya_shoulder.png`

**提示词：**
```
anime style, visual novel character sprite, galgame style, full body character, transparent background, clean lineart, high quality, detailed, young Chinese college-age man with short black hair, wearing casual smart outfit, one hand reaching forward as if placing on someone's shoulder, gentle and reassuring expression, slight smile, warm eyes, side view or slightly angled, no background, full body
```

---

## 立绘文件命名对照表

| 新文件名 | 替换旧图 | 对应剧情 |
|----------|----------|----------|
| `anya_wear_starry_night_dress.png` | `anya_smile_smug.png` | 发布会后台化妆镜前 |
| `anya_walk_runway.png` | `anya_smile_smug.png` | T台走秀鞠躬讲话 |
| `anya_run_to_me.png` | `anya_excited.png` | 结束后跑向主角 |
| `anya_look_at_me.png` | `anya_looking_camera.png` | 台上含情脉脉看向主角 |
| `me_walk_to_anya.png` | `me_smile_sincere.png` | 男主走入后台化妆间 |
| `me_put_hand_on_anya_shoulder.png` | `me_smile_sincere.png` | 男主安慰紧张安雅 |

## 生成注意事项

1. **立绘统一规则：** 透明背景 PNG，全身像（半身特写除外），≥1500px 高
2. **服装统一性：** 安雅发布会造型统一为「星夜」——深藏青色/深蓝底色哥特Lo裙，银色星形刺绣花纹，灯笼袖/公主袖设计，A字大裙摆
3. **发型一致：** 金色长发，发布会当天做精致编发/半扎发造型（但保留金发披肩特征）
4. **表情差异化：**
   - `wear_starry_night_dress` → 紧张中带着期待
   - `walk_runway` → 自信骄傲
   - `run_to_me` → 兴奋喜悦，眼中带泪
   - `look_at_me` → 温柔感激
5. **男主造型一致：** 白色衬衫配深色休闲裤，单反相机斜挎

## 生成完成后替换步骤

1. 将生成的 PNG 文件放入 `game/images/characters_alpha/`
2. 用 `rembg` 处理（如果未自动出透明背景）
3. 更新 `script.rpy` 中对应的 `image` 定义，把路径从临时映射改为新图（已注册的定义名不变，只改 = 后面的路径即可）
4. 运行 `renpy.sh` 验证无报错
