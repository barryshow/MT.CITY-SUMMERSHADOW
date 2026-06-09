# 第五章图片重命名计划

## Context
第五章的图片虽已注册在 script.rpy 中，但实际文件都是空白占位图，需重新生成。当前命名（如 `anya_stretch`、`me_tired`）过于通用，可能与后续章节冲突。需改为特质命名。

## 重命名映射表

### 安雅（17张）

| # | 旧文件名 | 新文件名 | 说明 |
|---|---------|---------|------|
| 1 | `anya_work` | `anya_ch5_work` | 整理衣服 |
| 2 | `anya_shocked` | `anya_ch5_shocked` | 发现空箱震惊 |
| 3 | `anya_panic` | `anya_ch5_panic` | 翻找空箱惊慌 |
| 4 | `anya_call` | `anya_ch5_call` | 打电话质问快递 |
| 5 | `anya_open_box` | `anya_ch5_open_box` | 掀开空箱盖 |
| 6 | `anya_open_box_happy` | `anya_ch5_find_dress` | 找到裙子喜极而泣 |
| 7 | `anya_cry_happy` | `anya_ch5_cry_joy` | 找回样衣感动落泪 |
| 8 | `anya_clean_dress` | `anya_ch5_clean_dress` | 擦拭裙子灰尘 |
| 9 | `anya_teach_me` | `anya_ch5_teach_sew` | 教缝珠子 |
| 10 | `anya_sit_on_steps` | `anya_ch5_wait_steps` | 小区台阶等候 |
| 11 | `anya_stretch` | `anya_ch5_dawn_relief` | 通宵后伸懒腰 |
| 12 | `anya_look_at_clock` | `anya_ch5_see_clock` | 发现八点了 |
| 13 | `anya_take_dress` | `anya_ch5_hold_dress` | 抱起星夜裙赴发布会 |
| 14 | `anya_look_at_me` | `anya_ch5_love_gaze` | 天台温柔对视 |
| 15 | `anya_lean_on_me` | `anya_ch5_lean_shoulder` | 靠在肩上等候 |
| 16 | `anya_lean_on_railing` | `anya_ch5_dawn_railing` | 天台靠栏杆看日出 |
| 17 | `anya_turn_to_me` | **不改** | 已有文件复用 |

### 主角（8张）

| # | 旧文件名 | 新文件名 | 说明 |
|---|---------|---------|------|
| 1 | `me_confident` | `me_ch5_reassure` | 安慰时自信表情 |
| 2 | `me_tired` | `me_ch5_exhausted` | 通宵后疲惫 |
| 3 | `me_squat` | `me_ch5_comfort_squat` | 蹲下安慰 |
| 4 | `me_hug` | `me_ch5_embrace` | 告白后拥抱 |
| 5 | `me_sit_beside` | `me_ch5_wait_together` | 并排坐台阶等候 |
| 6 | `me_look_at_anya` | `me_ch5_love_look` | 深情注视 |
| 7 | `me_put_arm` | `me_ch5_protect_arm` | 搭肩保护 |
| 8 | `me_take_beads` | `me_ch5_sew_beads` | 笨拙缝珠子 |

### CG 插画（2张）

| # | 旧文件名 | 新文件名 |
|---|---------|---------|
| 1 | `cg_lost_dress` | `cg_ch5_lost_dress` |
| 2 | `cg_confession` | `cg_ch5_confession` |

### 背景图（8张，不改名）

`bg_anya_studio`, `bg_studio_door`, `bg_courier_station`, `bg_west_community`, `bg_west_community_night`, `bg_anya_studio_night`, `bg_anya_studio_dawn`, `bg_studio_rooftop`

---

## 修改步骤

1. **修复 bug**：删除 L146 重复的 `image anya turn to me` 声明
2. **修改 image 声明行**（L64-161）：旧文件名 → 新文件名
3. **修改 CG 注册列表**（L165-173）：`cg_lost_dress` → `cg_ch5_lost_dress`，`cg_confession` → `cg_ch5_confession`
4. **修改 show 语句**（chapter_3 ~ chapter_5）：所有 `show xxx` 引用更新
5. **输出新提示词**：用新文件名的中文生成提示词
6. **Grep 验证**：确认无旧名残留

## 验证

```bash
grep -n "anya_stretch\|me_tired\|me_hug\b\|me_squat\|me_sit_beside\|me_put_arm\|me_look_at_anya\|me_take_beads\|me_confident\|anya_cry_happy\|anya_lean_on_railing\|anya_shocked\|anya_panic\|anya_call\|anya_open_box\|anya_teach_me\|anya_take_dress\|anya_look_at_me\|anya_look_at_clock\|anya_clean_dress\|cg_lost_dress\|cg_confession" game/script.rpy
```
