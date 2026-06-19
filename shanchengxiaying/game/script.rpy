# 游戏基础配置（可直接运行）
init python:
    config.window_title = "MT.CITY-SUMMERSHADOW | 山城夏影"
    config.screen_width = 1280
    config.screen_height = 720
    config.default_text_cps = 20  # 每秒20字，符合中文阅读习惯
    config.allow_skipping = True
    config.skip_indicator = True
    config.skip_delay = 0.15        # 快进速度（秒/句），越大越慢
    config.image_cache_size = 200   # 增大图片缓存，避免纹理重载导致渲染异常
    config.imagemap_cache = False   # 关闭图片缓存过滤，减少白边

# 角色定义
define 我 = Character(None)
define anya = Character("安雅", color="#ff6b9d")
define 老板娘 = Character("老板娘", color="#8b4513")
define 厂长 = Character("厂长", color="#4a90d9")
define 王老板 = Character("王老板", color="#d4a017")
define 服务员 = Character("服务员", color="#888888")
define 快递员 = Character("快递员", color="#666666")
define 站长 = Character("站长", color="#5a7a5a")
define 收件人 = Character("收件人", color="#999999")
define 主持人 = Character("主持人", color="#888888")
define 王总 = Character("王总", color="#d4a017")

# ========== 全局变换 ==========

# 背景：强制 1280x720 填满画布
transform bg_cover:
    xysize (1280, 720)
    xalign 0.5
    yalign 0.5

# 安雅站位（偏左）：yalign 1.05 让底部沉入对话框，视觉更稳
transform anya_std:
    zoom 0.49
    yalign 1.05
    xalign 0.25

# 安雅半身特写：zoom 0.8，显示头部和上半身
transform anya_close:
    zoom 0.8
    yalign 0.0
    xalign 0.25

# 男主站位（偏右）：避免和安雅重叠
transform me_std:
    zoom 0.49
    yalign 1.05
    xalign 0.75

# 老板娘站位（偏左，和安雅同位置，不会同时出现）
transform npc_std:
    zoom 0.49
    yalign 1.05
    xalign 0.25

# NPC站位（偏右，与安雅同屏时使用，避免立绘重叠）
transform npc_right:
    zoom 0.49
    yalign 1.05
    xalign 0.75


# 全局变量（记录分支与好感度，可用于后续章节）
default branch_type = 0
# 0=主线正常沟通  1=搭讪加好友分支  2=下头男负面分支
default anya_affection = 0
default trust_level = 0  # 安雅对男主的信任度（第二章新增）

# 角色立绘定义（Ren'Py 原生 image 语句，tag 自动识别，show 时自动替换同 tag 旧图）
image anya alert = "characters_alpha/anya_alert.png"
image anya angry = "characters_alpha/anya_angry.png"
image anya annoyed = "characters_alpha/anya_annoyed.png"
image anya arrive = "characters_alpha/anya_arrive.png"
image anya blush = "characters_alpha/anya_blush.png"
image anya blush look away = "characters_alpha/anya_blush_look_away.png"
image anya disgust = "characters_alpha/anya_disgust.png"
image anya eat bingfen = "characters_alpha/anya_eat_bingfen.png"
image anya excited = "characters_alpha/anya_excited.png"
image anya look around = "characters_alpha/anya_look_around.png"
image anya look down = "characters_alpha/anya_look_down.png"
image anya look out window = "characters_alpha/anya_look_out_window.png"
image anya look up determined = "characters_alpha/anya_look_up_determined.png"
image anya look up surprised = "characters_alpha/anya_look_up_surprised.png"
image anya looking camera = "characters_alpha/anya_looking_camera.png"
image anya looking equipment = "characters_alpha/anya_looking_equipment.png"
image anya looking umbrella = "characters_alpha/anya_looking_umbrella.png"
image anya nod = "characters_alpha/anya_nod.png"
image anya pout = "characters_alpha/anya_pout.png"
image anya run into dormitory = "characters_alpha/anya_run_into_dormitory.png"
image anya run to gate = "characters_alpha/anya_run_to_gate.png"
image anya sit down = "characters_alpha/anya_sit_down.png"
image anya sitting on steps = "characters_alpha/anya_sitting_on_steps.png"
image anya skeptical = "characters_alpha/anya_skeptical.png"
image anya smile happy quickly = "characters_alpha/anya_smile_happy_quickly.png"
image anya smile smug = "characters_alpha/anya_smile_smug.png"
image anya smile soft = "characters_alpha/anya_smile_soft.png"
image anya stand up = "characters_alpha/anya_stand_up.png"
image anya stand up quickly = "characters_alpha/anya_stand_up_quickly.png"
image anya stop = "characters_alpha/anya_stop.png"
image anya surprised silent = "characters_alpha/anya_surprised_silent.png"
image anya sweating but pout = "characters_alpha/anya_sweating_but_pout.png"
image anya take out bag = "characters_alpha/anya_take_out_bag.png"
image anya touch dress gently = "characters_alpha/anya_touch_dress_gently.png"
image anya turn around smile = "characters_alpha/anya_turn_around_smile.png"
image anya turn away = "characters_alpha/anya_turn_away.png"
image anya turn back = "characters_alpha/anya_turn_back.png"
image anya turn to leave = "characters_alpha/anya_turn_to_leave.png"
image anya turn to me = "characters_alpha/anya_turn_to_me.png"
image anya walk away = "characters_alpha/anya_walk_away.png"
image anya walk beside me = "characters_alpha/anya_walk_beside_me.png"
image anya walking ahead = "characters_alpha/anya_walking_ahead.png"
image anya wave goodbye = "characters_alpha/anya_wave_goodbye.png"
image anya wipe rain = "characters_alpha/anya_wipe_rain.png"
image me confused = "characters_alpha/me_confused.png"
image me follow anya = "characters_alpha/me_follow_anya.png"
image me look up = "characters_alpha/me_look_up.png"
image me looking anya = "characters_alpha/me_looking_anya.png"
image me pay = "characters_alpha/me_pay.png"
image me raise camera = "characters_alpha/me_raise_camera.png"
image me sigh = "characters_alpha/me_sigh.png"
image me smile = "characters_alpha/me_smile.png"
image me smile sincere = "characters_alpha/me_smile_sincere.png"
image me smile slight = "characters_alpha/me_smile_slight.png"
image me stand alone = "characters_alpha/me_stand_alone.png"
image me take out umbrella = "characters_alpha/me_take_out_umbrella.png"
image me take photo = "characters_alpha/me_take_photo.png"
image me wipe sweat = "characters_alpha/me_wipe_sweat.png"
image me weak = "characters_alpha/me_weak.png"
image me lie_in_bed = "characters_alpha/me_lie_in_bed.png"
image me lean on door = "characters_alpha/me_lean_on_door.png"
image anya limp = "characters_alpha/anya_casual_limp.png"
image anya cooking = "characters_alpha/anya_cooking.png"
image anya cry = "characters_alpha/anya_cry.png"
image anya stand_at_door = "characters_alpha/anya_stand_at_door.png"
image anya urgent = "characters_alpha/anya_urgent.png"
# ---- 以下为临时占位映射（原图待重新生成后替换） ----
image anya work = "characters_alpha/anya_looking_equipment.png"          # -> anya_work (待生成)
image anya open box happy = "characters_alpha/anya_smile_happy_quickly.png"  # -> anya_open_box_happy (待生成)
image anya cry happy = "characters_alpha/anya_smile_happy_quickly.png"       # -> anya_cry_happy (待生成)
image anya clean dress = "characters_alpha/anya_touch_dress_gently.png"      # -> anya_clean_dress (待生成)
image anya sit on steps = "characters_alpha/anya_sitting_on_steps.png"       # -> anya_sit_on_steps (待生成)
image anya stretch = "characters_alpha/anya_stand_up.png"               # -> anya_stretch (待生成)
image anya look_at_clock = "characters_alpha/anya_look_out_window.png"  # -> anya_look_at_clock (待生成)
image anya look_at_me = "characters_alpha/anya_looking_camera.png"      # -> anya_look_at_me (待生成)
image me confident = "characters_alpha/me_smile_sincere.png"            # -> me_confident (待生成)
image me tired = "characters_alpha/me_weak.png"                        # -> me_tired (待生成)
image me sit beside = "characters_alpha/me_stand_alone.png"            # -> me_sit_beside (待生成)
image me look_at_anya = "characters_alpha/me_looking_anya.png"         # -> me_look_at_anya (待生成)
image me put arm = "characters_alpha/me_smile_slight.png"              # -> me_put_arm (待生成)
image me take beads = "characters_alpha/me_take_photo.png"             # -> me_take_beads (待生成)

# ---- 以下为已用ch5专用图替换的占位 ----
image anya call = "characters_alpha/anya_ch5_call.png"
image anya shocked = "characters_alpha/anya_ch5_shocked.png"
image anya panic = "characters_alpha/anya_ch5_panic.png"
image anya open box = "characters_alpha/anya_ch5_open_box.png"
image anya teach me = "characters_alpha/anya_ch5_teach_sew.png"
image anya lean on me = "characters_alpha/anya_ch5_lean_shoulder.png"
image anya lean on railing = "characters_alpha/anya_ch5_dawn_railing.png"
image anya take dress = "characters_alpha/anya_ch5_find_dress.png"
image me hug = "characters_alpha/me_ch5_embrace.png"
image me squat = "characters_alpha/me_ch5_comfort_squat.png"
image 快递员 = "characters_alpha/courier.png"
image 站长 = "characters_alpha/station_master.png"
image 收件人 = "characters_alpha/courier.png"
image 厂长 = "characters_alpha/factory_manager.png"
image 王老板 = "characters_alpha/boss_wang.png"
image 服务员 = "characters_alpha/waiter.png"
image 老板娘 bring drinks = "characters_alpha/boss_lady_bring_drinks.png"
image 老板娘 leave = "characters_alpha/boss_lady_leave.png"
image 老板娘 smile = "characters_alpha/boss_lady_smile.png"

# ---- 第3章后半~第5章常服立绘 ----
image anya casual angry = "characters_alpha/anya_casual_angry.png"
image anya casual arrive = "characters_alpha/anya_casual_arrive.png"
image anya casual blush = "characters_alpha/anya_casual_blush.png"
image anya casual blush look away = "characters_alpha/anya_casual_blush.png"
image anya casual call = "characters_alpha/anya_casual_call.png"
image anya casual clean_dress = "characters_alpha/anya_casual_clean_dress.png"
image anya casual cooking = "characters_alpha/anya_casual_clean_dress.png"
image anya casual cry = "characters_alpha/anya_casual_cry.png"
image anya casual cry_happy = "characters_alpha/anya_casual_cry_happy.png"
image anya casual excited = "characters_alpha/anya_casual_excited.png"
image anya casual lean_on_me = "characters_alpha/anya_casual_lean_on_me.png"
image anya casual lean_on_railing = "characters_alpha/anya_casual_lean_on_railing.png"
image anya casual look_around = "characters_alpha/anya_casual_look_around.png"
image anya casual look_at_clock = "characters_alpha/anya_casual_look_at_clock.png"
image anya casual look_at_me = "characters_alpha/anya_casual_look_at_me.png"
image anya casual look_down = "characters_alpha/anya_casual_look_down.png"
image anya casual look_out_window = "characters_alpha/anya_casual_look_down.png"
image anya casual look up surprised = "characters_alpha/anya_casual_surprised_silent.png"
image anya casual nod = "characters_alpha/anya_casual_nod.png"
image anya casual open_box = "characters_alpha/anya_casual_open_box.png"
image anya casual open_box_happy = "characters_alpha/anya_casual_open_box_happy.png"
image anya casual panic = "characters_alpha/anya_casual_panic.png"
image anya casual pout = "characters_alpha/anya_casual_pout.png"
image anya casual run_into_dormitory = "characters_alpha/anya_casual_stop.png"
image anya casual shocked = "characters_alpha/anya_casual_shocked.png"
image anya casual sit_down = "characters_alpha/anya_casual_stop.png"
image anya casual sit_on_steps = "characters_alpha/anya_casual_sit_on_steps.png"
image anya casual smile happy quickly = "characters_alpha/anya_casual_excited.png"
image anya casual smile_smug = "characters_alpha/anya_casual_smile_smug.png"
image anya casual smile_soft = "characters_alpha/anya_casual_smile_soft.png"
image anya casual stand_at_door = "characters_alpha/anya_casual_arrive.png"
image anya casual stand_up = "characters_alpha/anya_casual_stand_up.png"
image anya casual stop = "characters_alpha/anya_casual_stop.png"
image anya casual stretch = "characters_alpha/anya_casual_stretch.png"
image anya casual surprised_silent = "characters_alpha/anya_casual_surprised_silent.png"
image anya casual take_dress = "characters_alpha/anya_casual_take_dress.png"
image anya casual teach_me = "characters_alpha/anya_casual_teach_me.png"
image anya casual turn_away = "characters_alpha/anya_casual_take_dress.png"
image anya casual turn_back = "characters_alpha/anya_casual_take_dress.png"
image anya casual turn_to_leave = "characters_alpha/anya_casual_take_dress.png"
image anya casual urgent = "characters_alpha/anya_casual_urgent.png"
image anya casual walk_beside_me = "characters_alpha/anya_casual_arrive.png"
image anya casual wave_goodbye = "characters_alpha/anya_casual_stop.png"
image anya casual work = "characters_alpha/anya_casual_work.png"
image me casual hug = "characters_alpha/me_casual_hug.png"
image me casual squat = "characters_alpha/me_casual_squat.png"

# ---- me casual 补全定义（映射到已有常服表情） ----
image me casual lie_in_bed = "characters_alpha/me_lie_in_bed.png"
image me casual weak = "characters_alpha/me_weak.png"
image me casual confused = "characters_alpha/me_confused.png"
image me casual lean on door = "characters_alpha/me_lean_on_door.png"
image me casual smile slight = "characters_alpha/me_smile_slight.png"
image me casual smile = "characters_alpha/me_smile.png"
image me casual smile sincere = "characters_alpha/me_smile_sincere.png"
image me casual confident = "characters_alpha/me_smile_sincere.png"
image me casual sit beside = "characters_alpha/me_smile_slight.png"
image me casual put arm = "characters_alpha/me_smile_slight.png"
image me casual take beads = "characters_alpha/me_take_photo.png"
image me casual look up = "characters_alpha/me_look_up.png"
image me casual tired = "characters_alpha/me_weak.png"
image me casual look_at_anya = "characters_alpha/me_looking_anya.png"
image anya casual turn to me = "characters_alpha/anya_casual_look_at_me.png"

# ---- 第六章 立绘定义（发布会Lolita版，映射到现有图） ----
image anya wear_starry_night_dress = "characters_alpha/anya_wear_starry_night_dress.png"
image anya walk_runway = "characters_alpha/anya_walk_runway.png"
image anya run_to_me = "characters_alpha/anya_run_to_me.png"
image anya smile_confident = "characters_alpha/anya_look_up_determined.png"
image anya take_my_hand = "characters_alpha/anya_take_my_hand.png"
image anya wear_starry_night_dress blush = "characters_alpha/anya_blush_post.png"
image anya wear_starry_night_dress look_at_me = "characters_alpha/anya_look_at_me.png"
image anya look_up = "characters_alpha/anya_look_up_surprised.png"
image anya look_at_river = "characters_alpha/anya_look_out_window.png"
image anya wave_to_me = "characters_alpha/anya_wave_goodbye.png"
image anya take_out_ticket = "characters_alpha/anya_excited.png"
image anya smile_happy = "characters_alpha/anya_smile_happy_quickly.png"
image anya shake_head = "characters_alpha/anya_nod.png"
image anya look_at_contract = "characters_alpha/anya_look_down.png"
image anya smile_weak = "characters_alpha/anya_smile_soft.png"
image anya teary = "characters_alpha/anya_cry.png"
image anya take_out_gift = "characters_alpha/anya_smile_soft.png"
image anya hug_me = "characters_alpha/anya_excited.png"
image anya walk_away = "characters_alpha/anya_turn_to_leave.png"
image anya wave = "characters_alpha/anya_wave_goodbye.png"
image me walk_to_anya = "characters_alpha/me_walk_to_anya.png"
image me put_hand_on_anya_shoulder = "characters_alpha/me_put_hand_on_anya_shoulder.png"
image me put_arm_around_anya = "characters_alpha/me_smile_sincere.png"
image me hug_anya = "characters_alpha/me_hug_anya.png"
image me take_out_photo = "characters_alpha/me_raise_camera.png"
image me smile_happy = "characters_alpha/me_smile_sincere.png"
image me surprised = "characters_alpha/me_confused.png"
image me put_hand_on_anya_hand = "characters_alpha/me_smile_sincere.png"
image me look_at_photo = "characters_alpha/me_look_up.png"
image me silent = "characters_alpha/me_stand_alone.png"
image me shake_head = "characters_alpha/me_smile_slight.png"
image me smile_weak = "characters_alpha/me_smile_slight.png"
image me smile_sad = "characters_alpha/me_stand_alone.png"
image me take_gift = "characters_alpha/me_pay.png"
image me wave = "characters_alpha/me_stand_alone.png"

image 主持人_enter = "characters_alpha/host.png"

image 王总_enter = "characters_alpha/boss_wang.png"
image 王总_nod = "characters_alpha/boss_wang.png"
image 王总_surprised = "characters_alpha/boss_wang.png"
image 王总_disappointed = "characters_alpha/boss_wang.png"
image 王总_leave = "characters_alpha/boss_wang.png"

# ---- 补全缺失的定义 ----
image anya smile = "characters_alpha/anya_smile_soft.png"
image anya take = "characters_alpha/anya_take_out_bag.png"
image me stand = "characters_alpha/me_stand_alone.png"
image me smile happy = "characters_alpha/me_smile_sincere.png"


init python:
    # CG图注册
    _cg_images = [
        "cg_first_meeting", "cg_share_umbrella", "cg_rooftop_sunset",
        "cg_treat_injury", "cg_fireflies", "cg_rooftop_stars",
        "cg_all_night_work", "cg_birthday_gift",
        "cg_printing_crisis", "cg_take_care",
        "cg_ch5_lost_dress", "cg_ch5_confession",
        "cg_kiss", "cg_final_photo",
    ]
    for _cg in _cg_images:
        renpy.image(tuple(_cg.split()), "cg/" + _cg + ".png")

    # 背景图注册
    _bg_images = [
        "bg_mountain_city_convention_outside_corner",
        "bg_old_town_street_sunset", "bg_old_mountain_city_alley",
        "bg_abandoned_factory_gate_mountain_city", "bg_bingfen_shop_entrance",
        "bg_bingfen_shop_interior", "bg_bingfen_shop_interior_rain_stop",
        "bg_street_after_rain_mountain_city", "bg_university_dormitory_gate",
        "bg_abandoned_factory_afternoon_mountain_city",
        "bg_abandoned_factory_interior", "bg_factory_hill",
        "bg_university_gate_morning", "bg_my_dormitory",
        "bg_my_dormitory_kitchen", "bg_print_shop_24h",
        "bg_print_shop_24h_night", "bg_printing_shop",
        "bg_printing_shop_corner",
        "bg_old_hotpot_shop",
        "bg_river_viewing_platform",
        "bg_river_walk",
        "bg_suburb_factory",
        "bg_anya_studio", "bg_studio_door",
        "bg_courier_station", "bg_west_community",
        "bg_west_community_night", "bg_anya_studio_night",
        "bg_anya_studio_dawn", "bg_studio_rooftop",
        "bg_conference_hall", "bg_conference_hall_backstage",
        "bg_nanshan_mountain", "bg_rooftop_one_year_later",
        "bg_airport", "bg_train_station",
    ]
    for _bg in _bg_images:
        renpy.image(tuple(_bg.split()), Transform("images/backgrounds/" + _bg + ".png", xysize=(1280, 720)))

    # 天气叠加层注册
    _weather_images = [
        "weather_clear", "weather_clear_evening", "weather_heavy_rain",
        "weather_hot_summer_mountain_city", "weather_rain_start", "weather_sunny",
    ]
    for _w in _weather_images:
        renpy.image(tuple(_w.split()), Transform("images/backgrounds/" + _w + ".png", xysize=(1280, 720)))


label start:

    # 第一幕：非典型初遇（约5分钟）
    scene bg_mountain_city_convention_outside_corner at bg_cover  with fade
    play music "audio/bgm/bgm_encounter.mp3"

    我 "（七月的山城，空气粘稠得像融化的糖浆。）"
    我 "（会展中心里的空调形同虚设，三万多人挤在一个巨大的铁皮盒子里，汗味、爆米花味和廉价香水味混合成一种令人窒息的味道。）"
    我 "（作为山城大学设计系大二学生，本来是抱着找灵感的心态来的，结果只收获了一身黏糊糊的汗水和快要爆炸的太阳穴。）"

    show me sigh at me_std zorder 10
    我 "（绕到场馆后面这个连保安都懒得来的死角，终于能喘口气了。这里连棵黄桷树都没有，但至少没人。）"

    我 "（从背包里掏出我的老单反，漫无目的地对着远处的跨江大桥按了几下快门。）"
    我 "（这种鬼天气，连阳光都显得油腻腻的，拍出来的照片都带着一股挥之不去的闷热感。）"

    hide me
    show anya sitting on steps at anya_std  zorder 10 with dissolve
    我 "（嗯？）"

    我 "（台阶上坐着一个女孩。）"
    我 "（她穿着一身极其繁复的黑色哥特Lolita裙，层层叠叠的蕾丝和荷叶边在阳光下泛着哑光的光泽。巨大的裙撑把裙摆撑得像一朵盛开的黑玫瑰，在这个满是灰尘和垃圾的角落里显得格格不入。）"
    我 "（金色的长发被汗水打湿了几缕，贴在白皙得近乎透明的脖颈上。她正低着头，用一只手揉着脚踝，另一只手拿着一瓶喝了一半的冰可乐。）"

    我 "（太违和了。）"
    我 "（这种精致到不真实的打扮，和周围斑驳的墙壁、生锈的铁栏杆、地上的烟头和塑料袋放在一起，产生了一种奇异的化学反应。）"
    我 "（就像是从另一个世界掉落到这里的公主，狼狈却依然保持着最后的骄傲。）"

    scene cg_first_meeting with fade
    play music "audio/bgm/bgm_encounter.mp3"
    我 "（我屏住了呼吸。阳光落在她身上，把那一身黑色蕾丝照得像暗夜里的星河。那一刻，我忘记了闷热，忘记了嘈杂，眼前只剩下这个画面。）"
    scene bg_mountain_city_convention_outside_corner at bg_cover  with fade
    play music "audio/bgm/bgm_encounter.mp3"
    show anya sitting on steps at anya_std zorder 10

    hide anya
    show me raise camera at me_std zorder 10
    我 "（几乎是下意识地，我举起了相机。）"

    play sound "audio/sfx/camera_shutter.mp3"
    我 "（咔嚓。）"

    # 核心分支选项节点（冲突最强，互动性最好）
    hide me
    show anya look up surprised at anya_std zorder 10
    voice "audio/voice/anya_0001.mp3"
    anya "！"

    show anya stand up quickly at anya_std zorder 10
    voice "audio/voice/anya_0002.mp3"
    anya "你在干什么？！"

    我 "（心脏猛地一沉，被当场抓包了。）"

    menu:
        "诚恳道歉，主动递上相机":
            $ branch_type = 0
            $ anya_affection += 5
            jump main_story

        "顺势搭话，想要加个好友":
            $ branch_type = 1
            $ anya_affection += 4
            jump chat_up_branch

        "慌乱辩解，说\"不就是拍张照吗\"":
            $ branch_type = 2
            $ anya_affection -= 50
            jump cringe_branch

# ===================== 主线分支：正常沟通（约20分钟，完整剧情）=====================
label main_story:
    show anya angry at anya_close zorder 10
    voice "audio/voice/anya_0003.mp3"
    anya "你偷拍我？"

    voice "audio/voice/me_0001.mp3"
    我 "抱歉，我不是故意的。只是觉得这个画面很有故事感，作为设计生一时没忍住。"
    voice "audio/voice/me_0002.mp3"
    我 "你要看照片的话，我现在就给你看，不满意我立刻删掉。"

    voice "audio/voice/anya_0004.mp3"
    anya "少废话，拿过来。"

    我 "（她语气强硬，我只好把相机递过去。心里做好了被要求删图、被数落一顿的准备。）"

    show anya looking camera at anya_std zorder 10
    show anya surprised silent at anya_std zorder 10
    voice "audio/voice/anya_0005.mp3"
    anya "……这张照片，是你拍的？"

    voice "audio/voice/me_0003.mp3"
    我 "嗯。我是设计专业，摄影是必修课程。"

    voice "audio/voice/anya_0006.mp3"
    anya "你叫什么名字？哪个学校的？"

    voice "audio/voice/me_0004.mp3"
    我 "林辰，山城大学的。"

    voice "audio/voice/anya_0007.mp3"
    anya "山城大学设计系……大二？"
    voice "audio/voice/me_0005.mp3"
    我 "你怎么知道？"

    voice "audio/voice/anya_0008.mp3"
    anya "我也是这所学校的，大一服装设计方向。"

    我 "（有些意外，穿着这么显眼的她，我居然在学校里从没见过。）"

    show anya smile smug at anya_close zorder 10
    voice "audio/voice/anya_0009.mp3"
    anya "做我的品牌视觉设计师兼摄影师吧。"

    voice "audio/voice/me_0006.mp3"
    我 "哈？"

    # 第三幕：男主的犹豫（核心心理描写）
    hide anya
    show me confused at me_std zorder 10
    voice "audio/voice/me_0007.mp3"
    我 "你说什么？"

    voice "audio/voice/anya_0010.mp3"
    anya "我有一个独立Lolita品牌「暗夜蔷薇」，缺专属摄影师和视觉设计。"

    voice "audio/voice/anya_0011.mp3"
    anya "工资按项目结算，一张精修图50，一套海报300，拍摄一天800。比你去街头画头像或者做家教强多了。"

    我 "（脑子一片混乱，前一秒还在对峙，下一秒就收到了工作邀请。）"
    我 "（我看着她，心里开始快速地盘算。这个学期有三个大作业，还有一个课程设计要做，我每天都忙得脚不沾地。）"
    我 "（而且看她这个样子，绝对是那种难伺候的大小姐类型。要求多，脾气差，还喜欢挑三拣四。给她打工，绝对是给自己找罪受。）"
    我 "（理智告诉我，应该立刻拒绝她。）"

    voice "audio/voice/me_0008.mp3"
    我 "我们专业课业繁重，我恐怕没有太多空余时间。"

    voice "audio/voice/anya_0012.mp3"
    anya "我看得出来，你是有真本事的人。之前找的三个摄影师，拍出来的东西要么像淘宝爆款，要么像影楼婚纱照。"
    voice "audio/voice/anya_0013.mp3"
    anya "但你这张照片，抓住了我想要的那种「破碎感」和「倔强感」。"


    hide me
    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0014.mp3"
    anya "怎么，怕麻烦不敢接？也是，很多人看着有点天赋，真要落地做事就退缩了。"

    我 "（被激将法戳中，心里有些不服。）"
    我 "（而且……说实话，她的品牌理念和设计风格，其实有点吸引我。哥特Lolita这种小众文化，本身就充满了视觉张力。）"
    我 "（还有，刚才那张照片里的她，那种疲惫又倔强的眼神，确实让我有点在意。）"

    voice "audio/voice/me_0009.mp3"
    我 "算了，我答应你。"
    voice "audio/voice/me_0010.mp3"
    我 "不过丑话说在前头，我只能利用课余时间，学业优先，还请你理解。"

    show anya smile happy quickly at anya_std zorder 10
    $ anya_affection += 6
    voice "audio/voice/anya_0015.mp3"
    anya "成交！这点我没问题。表现好的话，还有奖金。"

    voice "audio/voice/anya_0016.mp3"
    anya "加个好友吧，我晚上把品牌资料、设计稿发给你，明天下午我们约个时间在老城区的老茶馆讨论一下具体的工作内容。"

    我 "（拿出手机，和她互加好友。她的微信头像是一只黑色的猫。）"

    show anya wave goodbye at anya_std zorder 10
    voice "audio/voice/anya_0017.mp3"
    anya "明天见，林辰。别迟到，我最讨厌等人了。"

    scene black with fade

    # 第四幕：是工作还是约会？（寻找拍摄地+冰粉互动）
    scene bg_old_town_street_sunset at bg_cover  with dissolve
    play music "audio/bgm/bgm_daily.mp3"

    我 "（三天后。）"
    我 "（我和安雅约好了在老城区见面，为她的新款裙子寻找外景拍摄地。）"
    我 "（昨天晚上她给我发了十几张设计稿，还有一堆参考图。不得不说，她的设计确实很有才华。）"

    show anya walking ahead at anya_std zorder 10
    我 "（她今天穿了一身酒红色的Lolita裙，比那天的黑色款稍微轻便一点，但依然是层层叠叠的蕾丝和厚重的裙撑。）"
    我 "（夕阳把她的金发染成了温暖的橘色，她走在前面，裙摆随着脚步轻轻摆动。周围的路人都在偷偷看她，还有人拿出手机拍照。）"

    hide anya
    show me wipe sweat at me_std zorder 10
    我 "（我跟在她后面，已经汗流浃背了。今天虽然是傍晚，但气温依然有三十五度。）"

    voice "audio/voice/me_0011.mp3"
    我 "我说……"
    voice "audio/voice/me_0012.mp3"
    我 "你夏天穿这么厚不热吗？"

    hide me
    show anya sweating but pout at anya_std zorder 10
    voice "audio/voice/anya_0018.mp3"
    anya "要你管啊，我体寒。"

    我 "（我看着她额头上明显的汗珠，还有被汗水浸湿的后背，忍不住翻了个白眼。）"
    我 "（体寒？体寒会流这么多汗吗？死鸭子嘴硬。）"

    voice "audio/voice/anya_0019.mp3"
    anya "你走快点行不行？磨磨蹭蹭的。前面那个巷子看起来不错，我们去看看。"

    hide anya
    show me follow anya at me_std zorder 10
    voice "audio/voice/me_0013.mp3"
    我 "来了来了。"

    scene bg_old_mountain_city_alley at bg_cover  with dissolve
    play music "audio/bgm/bgm_daily.mp3"
    show anya look around at anya_std zorder 10
    voice "audio/voice/anya_0020.mp3"
    anya "嗯……这里的墙壁太新了，没有那种年代感。而且光线太散了，拍出来会显得脸很平。"

    我 "（她一边走一边点评，专业得不像一个大一新生。我本来以为她只是个喜欢穿Lolita的大小姐，没想到她对摄影和视觉也这么了解。）"

    voice "audio/voice/anya_0021.mp3"
    anya "那边那个门怎么样？就是那个绿色的木门，上面有铜环的那个。"

    hide anya
    show me take photo at me_std zorder 10
    我 "（我举起相机拍了一张。）"
    voice "audio/voice/me_0014.mp3"
    我 "不行，门的颜色和你这条裙子的颜色太接近了，会融在一起。而且上面的电线太多了，背景太乱。"

    hide me
    show anya nod at anya_std zorder 10
    voice "audio/voice/anya_0022.mp3"
    anya "嗯，有道理。那我们再往前走走。"

    scene bg_abandoned_factory_gate_mountain_city at bg_cover  with dissolve
    play music "audio/bgm/bgm_encounter.mp3"
    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0023.mp3"
    anya "哇！这里太棒了！"

    我 "（我们走到了一个废弃的老工厂门口。生锈的大铁门，斑驳的红砖墙，爬满了爬山虎，还有几棵歪歪扭扭的黄桷树。）"
    我 "（夕阳从铁门的缝隙里照进来，在地上投下斑驳的光影。）"

    voice "audio/voice/anya_0024.mp3"
    anya "你看这个光影！太完美了！还有这个铁门的质感，和我的新款裙子简直是绝配！"

    show anya run to gate at anya_std zorder 10
    我 "（她兴奋地跑了过去，提着裙子在铁门前来回走动。）"

    voice "audio/voice/anya_0025.mp3"
    anya "林辰，你快过来看看！站在这里拍怎么样？还有这里！"

    hide anya
    show me smile slight at me_std zorder 10
    $ anya_affection += 3
    我 "（我看着她兴奋的样子，忍不住笑了。原来她也有这么孩子气的一面。）"

    voice "audio/voice/me_0015.mp3"
    我 "嗯，这里确实不错。不过最好是下午三点左右来拍，那时候的光线最柔和，阴影也最好看。"

    voice "audio/voice/anya_0026.mp3"
    anya "好！那我们就定在后天下午三点在这里拍摄！"

    hide me
    show anya turn around smile at anya_std zorder 10
    voice "audio/voice/anya_0027.mp3"
    anya "太好了！终于找到合适的地方了！我之前找了好几个地方，从文创园到江边步道，都不满意。"

    我 "（她站在夕阳里，笑得像个孩子。金色的头发在阳光下闪闪发光，碧绿色的眼睛里闪烁着兴奋的光芒。）"
    我 "（心跳，好像漏了一拍。）"

    scene cg_rooftop_sunset with fade
    play music "audio/bgm/bgm_sunset.mp3"
    我 "（我们沿着生锈的铁楼梯爬上了工厂的天台。脚下是斑驳的水泥地，四周没有围墙，只有生锈的栏杆。夕阳就悬在江面上方，把整片天空烧成了橙红色。安雅走到栏杆边，风把她的裙摆和金发一起吹起来。远处的跨江大桥亮起了灯，像一条金色的项链横卧在江面上。）"
    scene bg_abandoned_factory_gate_mountain_city at bg_cover  with dissolve
    play music "audio/bgm/bgm_sunset.mp3"
    show anya turn around smile at anya_std zorder 10

    voice "audio/voice/me_0016.mp3"
    我 "好看。"
    voice "audio/voice/me_0017.mp3"
    我 "非常好看。"

    show anya blush look away at anya_std zorder 10
    $ anya_affection += 4
    voice "audio/voice/anya_0028.mp3"
    anya "哼，算你有眼光。"

    play sound "audio/sfx/thunder.mp3"
    voice "audio/voice/anya_0029.mp3"
    anya "啊？怎么突然下雨了？"

    hide anya
    show me look up at me_std zorder 10
    我 "（我抬头一看，不知道什么时候，天空已经乌云密布了。山城的夏天就是这样，说下雨就下雨，比变脸还快。）"

    voice "audio/voice/anya_0030.mp3"
    anya "糟了！我没带伞！"

    show me take out umbrella at me_std zorder 10
    voice "audio/voice/me_0018.mp3"
    我 "我带了。不过只有一把。"

    hide me
    show anya looking umbrella at anya_std zorder 10
    voice "audio/voice/anya_0031.mp3"
    anya "……"
    voice "audio/voice/anya_0032.mp3"
    anya "那……那我们一起撑吧。"

    scene cg_share_umbrella with fade
    play music "audio/bgm/bgm_warm.mp3"
    我 "（伞不大，我们靠得很近。她的肩膀偶尔碰到我的手臂，冰凉冰凉的。雨声很大，大到好像整个世界只剩下我们两个人和这一把伞。）"
    scene bg_bingfen_shop_entrance at bg_cover  with dissolve
    play music "audio/bgm/bgm_warm.mp3"
    我 "（我们快步跑到了附近一家冰粉店的屋檐下躲雨。雨越下越大，豆大的雨点砸在青石板路上，溅起一朵朵水花。）"

    show anya wipe rain at anya_std zorder 10
    voice "audio/voice/anya_0033.mp3"
    anya "呼……差点就被淋湿了。这雨怎么说下就下啊。"

    voice "audio/voice/me_0019.mp3"
    我 "山城的夏天就是这样，天气预报根本不准。看样子一时半会儿停不了。"

    hide anya
    show 老板娘 smile at npc_std zorder 10
    voice "audio/voice/boss_lady_0001.mp3"
    老板娘 "两位，进来躲躲雨嘛。外面雨大得很，进来吃碗冰粉凉快凉快。"

    hide 老板娘
    show anya turn to me at anya_std zorder 10
    voice "audio/voice/anya_0034.mp3"
    anya "……"
    voice "audio/voice/anya_0035.mp3"
    anya "那……我们进去坐一会儿吧。"

    scene bg_bingfen_shop_interior at bg_cover  with dissolve
    play music "audio/bgm/bgm_daily.mp3"
    show anya sit down at anya_std zorder 10
    voice "audio/voice/boss_lady_0002.mp3"
    老板娘 "两位想吃点啥子？我们这里有红糖冰粉、糍粑冰粉、玫瑰冰粉，还有凉虾凉糕。"

    voice "audio/voice/anya_0036.mp3"
    anya "我要一碗红糖冰粉，多加点山楂碎和花生碎。"

    voice "audio/voice/me_0020.mp3"
    我 "我也要一碗红糖冰粉。"

    hide anya
    show 老板娘 leave at npc_std zorder 10
    voice "audio/voice/boss_lady_0003.mp3"
    老板娘 "要得，稍等哈。"

    hide 老板娘
    show anya look out window at anya_std zorder 10
    voice "audio/voice/anya_0037.mp3"
    anya "（望着窗外的雨）不知道这雨什么时候才能停。"

    voice "audio/voice/me_0021.mp3"
    我 "应该还要下一会儿。正好，我们可以趁这个时间讨论一下拍摄的细节。"

    show anya turn to me at anya_std zorder 10
    voice "audio/voice/anya_0038.mp3"
    anya "对了，我把新款裙子的样衣带来了，你看看。"

    show anya take out bag at anya_std zorder 10
    我 "（她从一个巨大的黑色手提袋里拿出了一条裙子。）"
    我 "（那是一条黑色的哥特Lolita裙，上面有银色的十字架刺绣和黑色的蕾丝花边。裙摆是多层的，最下面一层是透明的纱，上面有银色的星星图案。）"

    voice "audio/voice/me_0022.mp3"
    我 "哇……好漂亮。"

    voice "audio/voice/anya_0039.mp3"
    anya "这是我这个季度的主打款，名字叫「星夜」。我花了三个月才设计好，光是刺绣就改了五次。"


    show anya touch dress gently at anya_std zorder 10
    voice "audio/voice/anya_0040.mp3"
    anya "我跑了十几家工厂，从山城跑到隔壁省城，才找到一家愿意做这种复杂刺绣的。很多工厂都嫌麻烦，不愿意接小单子。"

    我 "（我看着她小心翼翼地抚摸着裙子的样子，心里有点触动。）"
    我 "（原来她不是什么都不用做的大小姐。她为了自己的品牌，付出了这么多努力。）"

    voice "audio/voice/me_0023.mp3"
    我 "你为什么要自己做品牌啊？以你的能力，毕业之后去大公司做设计师应该很容易吧。"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0041.mp3"
    anya "……"
    voice "audio/voice/anya_0042.mp3"
    anya "因为我想做自己真正喜欢的东西。"

    voice "audio/voice/anya_0043.mp3"
    anya "大公司的设计师，都要按照市场的需求来设计。什么好卖就设计什么，根本没有自己的想法。我不想那样。我想设计出能真正表达我自己的衣服。"

    voice "audio/voice/anya_0044.mp3"
    anya "虽然现在很难，品牌也没什么名气，赚的钱也只够勉强维持。但我相信，只要我坚持下去，总会有人喜欢我的设计的。"

    show anya look up determined at anya_close zorder 10
    voice "audio/voice/anya_0045.mp3"
    anya "我一定要让「暗夜蔷薇」成为全国最有名的Lolita品牌！"


    我 "（她的眼睛里闪烁着坚定的光芒。那一刻，我突然觉得，她不仅仅是一个漂亮的女孩。她是一个有梦想，并且愿意为之努力奋斗的人。）"

    hide anya
    show me smile sincere at me_std zorder 10
    $ anya_affection += 8
    voice "audio/voice/me_0024.mp3"
    我 "我相信你一定可以的。"

    hide me
    show anya blush at anya_close zorder 10
    voice "audio/voice/anya_0046.mp3"
    anya "哼……那是当然。也不看看我是谁。"

    hide anya
    show 老板娘 bring drinks at npc_std zorder 10
    voice "audio/voice/boss_lady_0004.mp3"
    老板娘 "两位的冰粉来了！"

    我 "（老板娘端着两碗冰粉走了过来。晶莹剔透的冰粉上面浇着浓稠的红糖汁，撒满了山楂碎、花生碎、葡萄干和白芝麻。）"

    voice "audio/voice/anya_0047.mp3"
    anya "谢谢老板娘。"

    hide 老板娘
    show anya eat bingfen at anya_std zorder 10
    voice "audio/voice/anya_0048.mp3"
    anya "哇，好好吃！比我之前在市中心吃的那家还要好吃。"

    我 "（我舀了一勺放进嘴里，冰凉的触感瞬间驱散了夏日的燥热。红糖的甜和山楂的酸完美地融合在一起，还有花生碎的香脆。）"

    voice "audio/voice/me_0025.mp3"
    我 "嗯，确实不错。"

    scene bg_bingfen_shop_interior_rain_stop at bg_cover  with dissolve
    play music "audio/bgm/bgm_soft.mp3"
    我 "（不知不觉，雨已经停了。天空被雨水洗过，变得格外蓝。空气也变得清新了很多，带着一股泥土和黄桷兰的香味。）"

    voice "audio/voice/me_0026.mp3"
    我 "雨停了。"

    show anya look out window at anya_std zorder 10
    voice "audio/voice/anya_0049.mp3"
    anya "真的哎！太好了，终于可以回去了。"

    show anya stand up at anya_std zorder 10
    voice "audio/voice/anya_0050.mp3"
    anya "老板娘，结账。"

    voice "audio/voice/boss_lady_0005.mp3"
    老板娘 "一共十六块。"

    hide anya
    show me pay at me_std zorder 10
    voice "audio/voice/me_0027.mp3"
    我 "我来吧。就当是我请你的，谢谢你给我这个工作机会。"

    hide me
    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0051.mp3"
    anya "哼……那好吧。下次我请你吃火锅。"

    scene bg_street_after_rain_mountain_city at bg_cover  with dissolve
    play music "audio/bgm/bgm_soft.mp3"
    show anya walk beside me at anya_std zorder 10
    我 "（我们并肩走在雨后的青石板路上。路面湿漉漉的，倒映着红灯笼的光芒。空气清新，微风拂面，让人感觉很舒服。）"

    voice "audio/voice/anya_0052.mp3"
    anya "对了，林辰。后天拍摄的时候，你记得带反光板和补光灯。还有，你最好穿黑色的衣服，这样不会在裙子上反光。"

    voice "audio/voice/me_0028.mp3"
    我 "知道了。你放心，我专业的。"

    voice "audio/voice/anya_0053.mp3"
    anya "哼，最好是这样。要是拍不好，我可是会扣你工资的。"

    我 "（我笑着摇了摇头。她还是这么嘴硬。）"

    scene bg_university_dormitory_gate at bg_cover  with dissolve
    play music "audio/bgm/bgm_sunset.mp3"
    show anya stop at anya_std zorder 10
    voice "audio/voice/anya_0054.mp3"
    anya "我到了。我住女生宿舍，你就不用送进去了。"

    voice "audio/voice/me_0029.mp3"
    我 "好。那后天下午三点，废弃工厂门口见。"

    show anya nod at anya_std zorder 10
    voice "audio/voice/anya_0055.mp3"
    anya "嗯。记得别迟到。还有，别忘了带反光板和补光灯。"

    voice "audio/voice/me_0030.mp3"
    我 "知道了，忘不了。"

    show anya turn to leave at anya_std zorder 10
    voice "audio/voice/anya_0056.mp3"
    anya "那我进去了。拜拜。"

    show anya turn back at anya_std zorder 10
    voice "audio/voice/anya_0057.mp3"
    anya "哦，对了！林辰。"

    hide anya
    show me looking anya at me_std zorder 10
    voice "audio/voice/me_0031.mp3"
    我 "嗯？怎么了？"

    hide me
    show anya smile soft at anya_close zorder 10
    $ anya_affection += 6
    voice "audio/voice/anya_0058.mp3"
    anya "今天……谢谢你。陪我找了一下午的拍摄地，还请我吃了冰粉。"

    show anya blush look away at anya_std zorder 10
    voice "audio/voice/anya_0059.mp3"
    anya "还有……你拍的照片，真的很好看。"

    show anya run into dormitory at anya_std zorder 10
    我 "（说完，她就红着脸跑进了宿舍大楼。）"

    hide anya
    show me stand alone at me_std zorder 10
    我 "（我站在原地，看着她消失的背影，心里有一种奇怪的感觉。暖暖的，甜甜的，还有一点小小的悸动。）"

    我 "（我拿出手机，打开了那张在漫展场外拍的照片。照片里的她，坐在台阶上，低着头喝可乐。金色的头发在阳光下闪闪发光，脸上带着一丝疲惫和倔强。）"

    show me smile at me_std zorder 10
    我 "（安雅……真是个有趣的女孩。）"

    scene black with fade

    # 第五幕：第一次拍摄（Demo结尾，留下悬念）
    scene bg_abandoned_factory_afternoon_mountain_city at bg_cover  with dissolve
    play music "audio/bgm/bgm_daily.mp3"

    我 "（后天下午三点。）"
    我 "（我准时来到了废弃工厂门口。我带了两个相机，三个镜头，还有反光板、补光灯、三脚架，几乎把我所有的家当都带来了。）"

    show anya arrive at anya_std zorder 10
    我 "（没过多久，安雅就来了。她今天没有穿Lolita裙，而是穿了一件简单的白色T恤和牛仔裤。头发也扎成了一个马尾，脸上没有化妆。）"
    我 "（即使是这样朴素的打扮，也依然掩盖不住她的美貌。）"

    voice "audio/voice/anya_0060.mp3"
    anya "你来得挺早的嘛。我还以为你会迟到呢。"

    voice "audio/voice/me_0032.mp3"
    我 "我从来不迟到。东西都带来了，你看看还缺什么。"

    show anya looking equipment at anya_std zorder 10
    voice "audio/voice/anya_0061.mp3"
    anya "哇，你装备挺齐全的啊。比我之前找的那个摄影师专业多了。"

    voice "audio/voice/me_0033.mp3"
    我 "那是当然。我们先去换衣服吧，那边有个废弃的值班室，可以当化妆间。"

    scene black with fade

    show text "第一章：漫展角落的黑玫瑰 完" with fade
    pause
    show text "即将进入第二章：星夜下的拍摄" with fade
    pause

    scene black with fade
    jump chapter_2

# ===================== 分支2：搭讪加好友（约18分钟，暧昧拌嘴线）=====================
label chat_up_branch:
    show anya alert at anya_std zorder 10
    voice "audio/voice/anya_0062.mp3"
    anya "你偷拍我？"

    voice "audio/voice/me_0034.mp3"
    我 "那个……实在是你太亮眼了，和这个环境形成的反差感太绝了，我作为设计生一时没忍住。"
    voice "audio/voice/me_0035.mp3"
    我 "抱歉啊，我是山城大学设计系的林辰。其实我一直很喜欢Lolita风格的设计，冒昧问一句，可以加个好友认识一下吗？"

    show anya skeptical at anya_std zorder 10
    voice "audio/voice/anya_0063.mp3"
    anya "上来就要好友？你这人还真是直接。"
    voice "audio/voice/anya_0064.mp3"
    anya "先把照片给我看看，拍得不好，不光删图，别想再搭话。"

    我 "（连忙递过相机，心里有些忐忑。）"
    show anya looking camera at anya_std zorder 10
    show anya surprised silent at anya_std zorder 10
    voice "audio/voice/anya_0065.mp3"
    anya "……没想到构图和光影居然这么到位。"

    voice "audio/voice/anya_0066.mp3"
    anya "巧了，我也是山城大学的，大一服装设计。这身裙子就是我自己设计的。"

    我 "（大吃一惊）原来你就是设计师！难怪气质这么特别，和那些只会穿衣服的完全不一样。"

    show anya smile smug at anya_std zorder 10
    voice "audio/voice/anya_0067.mp3"
    anya "看你也算有点审美。正好，我缺摄影师和视觉设计，要不要来帮我做事？顺便……好友也可以加。"

    我 "（没想到搭讪居然歪打正着收到工作邀请，有点哭笑不得。）"
    voice "audio/voice/me_0036.mp3"
    我 "课业挺多的，但我可以抽空帮忙。加好友没问题。"

    我 "（两人互加微信，气氛不再尴尬，反而多了几分轻松。）"

    voice "audio/voice/anya_0068.mp3"
    anya "算你运气好。后续工作细节我微信发你，明天老城区碰面选拍摄地，别迟到。"

    scene black with fade

    # 后续剧情与主线基本一致，仅对话增加暧昧拌嘴
    scene bg_old_town_street_sunset at bg_cover  with dissolve
    play music "audio/bgm/bgm_daily.mp3"
    我 "（隔天和安雅一同寻找外景。）"

    show anya walking ahead at anya_std zorder 10
    hide anya
    show me wipe sweat at me_std zorder 10
    voice "audio/voice/me_0037.mp3"
    我 "我说，你夏天穿这么厚不热吗？我看着都替你热。"

    hide me
    show anya sweating but pout at anya_std zorder 10
    voice "audio/voice/anya_0069.mp3"
    anya "要你管啊，我体寒。"

    voice "audio/voice/me_0038.mp3"
    我 "体寒还流这么多汗？我看你就是爱美不要命。小心中暑了没人管你。"

    voice "audio/voice/anya_0070.mp3"
    anya "你少贫嘴！专心找场地。再废话我扣你工资。"

    scene bg_old_mountain_city_alley at bg_cover  with dissolve
    play music "audio/bgm/bgm_daily.mp3"
    show anya look around at anya_std zorder 10
    voice "audio/voice/anya_0071.mp3"
    anya "这里不行，太普通了。"

    voice "audio/voice/anya_0072.mp3"
    anya "前面看看。"

    scene bg_abandoned_factory_gate_mountain_city at bg_cover  with dissolve
    play music "audio/bgm/bgm_encounter.mp3"
    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0073.mp3"
    anya "这里完美！林辰你眼光可以啊。"

    voice "audio/voice/me_0039.mp3"
    我 "那当然，也不看是谁。"

    voice "audio/voice/anya_0074.mp3"
    anya "臭美。"

    scene cg_rooftop_sunset with fade
    play music "audio/bgm/bgm_sunset.mp3"
    我 "（我们爬上了工厂的天台。夕阳正好挂在江面上方，把整片天空染成了橙红色。安雅的酒红色裙摆被风吹起来，和天边的晚霞融为一体。）"
    scene bg_abandoned_factory_gate_mountain_city at bg_cover  with dissolve
    play music "audio/bgm/bgm_sunset.mp3"
    show anya turn around smile at anya_std zorder 10

    # 下雨躲雨、吃冰粉、送回宿舍流程与主线一致
    play sound "audio/sfx/thunder.mp3"
    voice "audio/voice/anya_0075.mp3"
    anya "糟糕，下雨了！"

    hide anya
    show me take out umbrella at me_std zorder 10
    voice "audio/voice/me_0040.mp3"
    我 "幸好我带了伞，一起走吧。"

    scene cg_share_umbrella with fade
    play music "audio/bgm/bgm_warm.mp3"
    我 "（伞不大，她靠得很近。我能闻到她身上淡淡的香水味，被雨水冲得若有若无。）"
    scene bg_bingfen_shop_entrance at bg_cover  with dissolve
    play music "audio/bgm/bgm_warm.mp3"
    show 老板娘 smile at npc_std zorder 10
    voice "audio/voice/boss_lady_0006.mp3"
    老板娘 "进来躲雨吃碗冰粉吧。"

    scene bg_bingfen_shop_interior at bg_cover  with dissolve
    play music "audio/bgm/bgm_daily.mp3"
    # 冰粉、聊梦想、下雨停后离场流程一致
    show anya eat bingfen at anya_std zorder 10
    voice "audio/voice/anya_0076.mp3"
    anya "这家冰粉真的好好吃。下次我们还来这里吃好不好？"

    voice "audio/voice/me_0041.mp3"
    我 "好啊，下次我请你。"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0077.mp3"
    anya "谁要你请……我自己有钱。"

    scene bg_university_dormitory_gate at bg_cover  with dissolve
    play music "audio/bgm/bgm_sunset.mp3"
    voice "audio/voice/anya_0078.mp3"
    anya "今天辛苦啦，下次拍摄再联系。"
    voice "audio/voice/anya_0079.mp3"
    anya "对了，以后不许随便搭讪陌生人，也就我好心理你。"

    voice "audio/voice/me_0042.mp3"
    我 "知道啦，我的大设计师。以后只搭讪你一个人。"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0080.mp3"
    anya "哼，油嘴滑舌。"

    show anya run into dormitory at anya_std zorder 10

    hide anya
    show me smile at me_std zorder 10
    我 "（看着她跑开的背影，我忍不住笑了。）"
    我 "（这个夏天，好像变得有趣起来了。）"

    scene black with fade

    show text "第一章：意外的相识 完" with fade
    pause
    show text "即将进入第二章：星夜下的拍摄" with fade
    pause

    scene black with fade
    jump chapter_2

# ===================== 分支3：下头男坏结局（约5分钟，短BE）=====================
label cringe_branch:
    show anya angry at anya_std zorder 10
    voice "audio/voice/anya_0081.mp3"
    anya "你居然偷拍我？"

    我 "（瞬间慌乱，手脚无措，说话语无伦次）啊、啊我不是故意的！主要是你长得太好看了，我一时看呆了才拍照的……"
    voice "audio/voice/me_0043.mp3"
    我 "别生气嘛，就一张照片而已，多大点事。要不……我请你喝东西，交个朋友？"

    show anya disgust at anya_std zorder 10
    voice "audio/voice/anya_0082.mp3"
    anya "够了。"

    voice "audio/voice/anya_0083.mp3"
    anya "先是偷拍别人，现在又说这种轻浮的话，真让人不舒服。"

    voice "audio/voice/me_0044.mp3"
    我 "不是，我真没有别的意思，你别多想啊！不就是拍张照吗，至于这么生气吗？"

    show anya annoyed at anya_std zorder 10
    voice "audio/voice/anya_0084.mp3"
    anya "不用解释了。随手偷拍别人，还一副理所当然的样子，**真是个下头男**。"

    voice "audio/voice/anya_0085.mp3"
    anya "把照片立刻删掉，以后离我远一点。"

    我 "（脸色一阵尴尬，自知言行失当，只好当着她的面删除照片。）"
    voice "audio/voice/me_0045.mp3"
    我 "对不起……是我失态了。"

    show anya turn away at anya_std zorder 10
    voice "audio/voice/anya_0086.mp3"
    anya "没必要再说了。"

    show anya walk away at anya_std  zorder 10 with dissolve
    我 "（安雅提着裙摆，头也不回地离开。原本短暂的相遇，彻底闹僵。）"

    我 "（独自站在空荡的角落，满心懊悔。一时慌乱说错话，好好的相遇就这样搞砸了。）"
    我 "（这场夏日里的意外邂逅，到此戛然而止。）"

    show text "【坏结局】尴尬收场" with fade
    pause
    show text "你失去了与她相识的机会" with fade
    pause

    scene black with fade
    return

# ===================== 第二章：星夜下的拍摄（约1.5小时）=====================
label chapter_2:
    scene bg_abandoned_factory_afternoon_mountain_city at bg_cover with fade
    play music "audio/bgm/bgm_daily.mp3" fadein 1.0

    我 "（废弃工厂比想象中还要大，空气中弥漫着灰尘和铁锈的味道。）"
    我 "（阳光透过破碎的窗户洒进来，在地上投下斑驳的光影，确实是绝佳的拍摄场地。）"

    show anya turn to me at anya_std zorder 10
    voice "audio/voice/anya_0087.mp3"
    anya "那边的值班室还能用，我去换衣服。你先把设备架好，试一下光。"

    show anya turn to leave at anya_std zorder 10
    voice "audio/voice/anya_0088.mp3"
    anya "不许偷看！"

    hide anya
    show me smile slight at me_std zorder 10
    voice "audio/voice/me_0046.mp3"
    我 "知道了，我又不是变态。"

    scene black with dissolve
    我 "（大约二十分钟后，值班室的门开了。）"

    scene bg_abandoned_factory_afternoon_mountain_city at bg_cover with fade
    show anya arrive at anya_std zorder 10
    $ anya_affection += 3

    我 "（呼吸猛地一滞。）"
    我 "（黑色的裙摆层层叠叠，像盛开的暗夜玫瑰，银色的星星刺绣在阳光下闪闪发光。）"
    我 "（她化了精致的哥特妆，深红色的口红衬得皮肤更加白皙，整个人散发着一种神秘又冷艳的气质。）"

    voice "audio/voice/anya_0089.mp3"
    anya "看什么看？没见过啊？"

    show anya pout at anya_std zorder 10
    hide me
    我 "（连忙收回目光，假装调整相机。）"
    voice "audio/voice/me_0047.mp3"
    我 "没什么，就是觉得……比我想象中还要好看。"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0090.mp3"
    anya "哼，算你有眼光。赶紧开始拍吧，早点拍完早点收工。"

    # ---- 下午拍摄 ----
    show anya look around at anya_std zorder 10
    play sound "audio/sfx/camera_shutter.mp3"

    voice "audio/voice/me_0048.mp3"
    我 "头稍微低一点，眼神再冷一点……对，就是这样。"
    voice "audio/voice/me_0049.mp3"
    我 "手放在腰上，身体微微侧转……完美。"

    我 "（安雅的镜头感好得惊人，几乎不用我怎么指导，就能摆出最有感觉的姿势。）"
    我 "（她顶着三十多度的高温，穿着厚重的裙子，在太阳底下站了整整两个小时，连一句抱怨都没有。）"

    show anya sit down at anya_std zorder 10
    play sound "audio/sfx/camera_shutter.mp3"
    voice "audio/voice/me_0050.mp3"
    我 "保持住，眼神看远方……很好。"

    我 "（按下快门的瞬间，我注意到她的眉头微微皱了一下，脚不自觉地动了动。）"

    hide anya
    show me looking anya at me_std zorder 10
    我 "（她的脚踝……好像受伤了。）"

    hide me
    show anya limp at anya_std zorder 10
    voice "audio/voice/anya_0091.mp3"
    anya "好了，这组拍完了。我们休息一下吧。"

    我 "（她站起来的时候踉跄了一下，下意识地扶住了旁边的铁门。）"

    hide anya
    show me confused at me_std zorder 10
    voice "audio/voice/me_0051.mp3"
    我 "你脚踝受伤了？"

    hide me
    show anya alert at anya_std zorder 10
    voice "audio/voice/anya_0092.mp3"
    anya "没有啊，我好好的。"

    show anya turn away at anya_std zorder 10
    voice "audio/voice/anya_0093.mp3"
    anya "就是站久了有点麻而已。"

    voice "audio/voice/me_0052.mp3"
    我 "别装了，我都看到了。是不是早上来的时候扭到的？"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0094.mp3"
    anya "……"

    voice "audio/voice/anya_0095.mp3"
    anya "就……一点点而已，不碍事。"

    voice "audio/voice/me_0053.mp3"
    我 "都一瘸一拐了还说不碍事？过来坐下，我帮你看看。"

    menu:
        "强硬一点，拉她过来坐下":
            $ anya_affection += 4
            $ trust_level += 2

            hide me
            show me smile sincere at me_std zorder 10
            我 "少废话，过来。"

            show anya blush at anya_std zorder 10
            voice "audio/voice/anya_0397.mp3"
            anya "喂！你干什么啊！放开我！"

            show anya sit down at anya_std zorder 10
            voice "audio/voice/anya_0398.mp3"
            anya "（小声嘟囔）真是的，一点都不温柔。"

        "温柔劝说，耐心等她过来":
            $ anya_affection += 5
            $ trust_level += 12

            hide me
            show me smile sincere at me_std zorder 10
            我 "听话，要是伤势加重了，后面的拍摄就没法进行了。"
            我 "我学过一点急救，不会弄疼你的。"

            show anya look down at anya_std zorder 10
            voice "audio/voice/anya_0399.mp3"
            anya "……那好吧。"

    # ---- 处理伤口 ----
    play music "audio/bgm/bgm_soft.mp3" fadein 1.0

    我 "（我蹲下身，轻轻卷起她的裤脚。）"
    我 "（脚踝已经肿得很高了，青紫色的瘀血清晰可见。）"

    voice "audio/voice/me_0054.mp3"
    我 "都肿成这样了，你还硬撑着拍了两个小时？你是傻子吗？"

    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0096.mp3"
    anya "要你管啊……本来以为忍忍就过去了。"

    voice "audio/voice/anya_0097.mp3"
    anya "而且……这是新款裙子的第一次拍摄，我不想搞砸。"

    我 "（心里一阵心疼。）"
    我 "（她总是这样，把所有的压力都自己扛着，明明已经很辛苦了，却还要装作一副无所谓的样子。）"

    hide me
    show me smile sincere at me_std zorder 10
    voice "audio/voice/me_0055.mp3"
    我 "幸好我包里带了云南白药。先给你喷点药，然后用冰袋敷一下。"

    voice "audio/voice/anya_0098.mp3"
    anya "嘶……轻点。"

    show anya look down at anya_std zorder 10
    voice "audio/voice/me_0056.mp3"
    我 "忍一下，很快就好。"

    我 "（我小心翼翼地给她喷药，然后用冰袋轻轻敷在她的脚踝上。）"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0099.mp3"
    anya "……谢谢你。"

    voice "audio/voice/me_0057.mp3"
    我 "不用谢。谁让我是你的专属摄影师呢。"

    voice "audio/voice/anya_0100.mp3"
    anya "谁……谁要你专属了。"

    # ---- 突发停电 ----
    play sound "audio/sfx/sfx_power_out.mp3"
    scene black with dissolve

    voice "audio/voice/anya_0101.mp3"
    anya "啊！怎么回事？！"

    show anya alert at anya_std zorder 10
    voice "audio/voice/anya_0102.mp3"
    anya "停电了吗？"

    hide anya
    show me confused at me_std zorder 10
    voice "audio/voice/me_0058.mp3"
    我 "别慌，应该是工厂的老线路出问题了。"

    voice "audio/voice/me_0059.mp3"
    我 "我手机有手电筒。"

    我 "（手机的微弱光芒照亮了周围的环境，值班室里一片漆黑，只有窗外透进来一点点月光。）"

    voice "audio/voice/anya_0103.mp3"
    anya "（声音有点发抖）那……那我们现在怎么办？"

    # 初始分支对话差异
    if branch_type == 1:
        hide me
        show me smile slight at me_std zorder 10
        我 "怎么，害怕了？"

        show anya pout at anya_std zorder 10
        voice "audio/voice/anya_0400.mp3"
        anya "谁……谁害怕了！我只是……只是有点意外而已。"

        hide me
        show me smile sincere at me_std zorder 10
        我 "别怕，有我在呢。"

        voice "audio/voice/anya_0401.mp3"
        anya "……"
        voice "audio/voice/anya_0402.mp3"
        anya "谁要你保护啊。"

        我 "（她嘴上说着不要，身体却不自觉地向我靠近了一点。）"

    else:
        hide me
        show me smile sincere at me_std zorder 10
        我 "别担心，我在这里。"

        我 "我们就在这里等一会儿，应该很快就会来电的。"

        show anya look down at anya_std zorder 10
        voice "audio/voice/anya_0403.mp3"
        anya "……嗯。"

    # ---- 分享糗事 ----
    show anya sit down at anya_std zorder 10
    voice "audio/voice/anya_0104.mp3"
    anya "好无聊啊……我们说点什么吧。"

    voice "audio/voice/me_0060.mp3"
    我 "好啊。那你先说，你学生时代有没有什么特别糗的事？"

    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0105.mp3"
    anya "我才没有什么糗事呢。我一直都是完美的。"

    voice "audio/voice/me_0061.mp3"
    我 "是吗？我才不信。每个人都有糗事的。"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0106.mp3"
    anya "……好吧，就告诉你一件。"

    voice "audio/voice/anya_0107.mp3"
    anya "高一的时候，有一次我穿Lolita裙去上学，结果裙摆被自行车链条勾住了，摔了个狗吃屎。"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0108.mp3"
    anya "当时全校的人都看着我，我恨不得找个地缝钻进去。"

    hide me
    show me smile at me_std zorder 10
    voice "audio/voice/me_0062.mp3"
    我 "哈哈哈哈！没想到你还有这种时候！"

    show anya angry at anya_std zorder 10
    voice "audio/voice/anya_0109.mp3"
    anya "不许笑！再笑我就扣你工资！"

    voice "audio/voice/me_0063.mp3"
    我 "好好好，我不笑了。"

    voice "audio/voice/me_0064.mp3"
    我 "那我也告诉你一件我的糗事吧。大一军训的时候，我顺拐了整整一个星期，被教官单独拉出来训练。"

    show anya smile happy quickly at anya_std zorder 10
    voice "audio/voice/anya_0110.mp3"
    anya "哈哈哈哈！顺拐！太好笑了！"

    我 "（看着她笑得前仰后合的样子，我也忍不住笑了。）"
    我 "（这是我第一次看到她这么开心的样子，没有高冷，没有傲娇，就像一个普通的小女孩。）"

    play sound "audio/sfx/sfx_power_on.mp3"
    scene bg_abandoned_factory_afternoon_mountain_city at bg_cover with dissolve

    voice "audio/voice/anya_0111.mp3"
    anya "啊！来电了！"

    show anya stand up at anya_std zorder 10
    voice "audio/voice/anya_0112.mp3"
    anya "太好了！终于可以回去了！"

    hide anya
    show me looking anya at me_std zorder 10
    voice "audio/voice/me_0065.mp3"
    我 "等等，你看外面。"

    hide me
    show anya look out window at anya_std zorder 10
    voice "audio/voice/anya_0113.mp3"
    anya "怎么了？"

    voice "audio/voice/me_0066.mp3"
    我 "天已经黑了，月亮出来了。现在的光线……拍夜景应该会很好看。"

    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0114.mp3"
    anya "对哦！我怎么没想到！"

    voice "audio/voice/anya_0115.mp3"
    anya "我们拍一组夜景吧！就当是加更！"

    voice "audio/voice/me_0067.mp3"
    我 "可是你的脚……"

    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0116.mp3"
    anya "我的脚没事！已经不疼了！真的！"

    voice "audio/voice/anya_0117.mp3"
    anya "求求你了，就拍一组好不好？这个机会太难得了。"

    hide me
    show me sigh at me_std zorder 10
    voice "audio/voice/me_0068.mp3"
    我 "好吧好吧，真是怕了你了。"

    # ---- 萤火虫剧情 ----
    scene cg_fireflies at bg_cover with dissolve
    play music "audio/bgm/bgm_encounter.mp3" fadein 1.0

    我 "（我们走到了工厂后面的小山坡上。）"
    我 "（这里长满了野草和灌木，月光洒在草地上，像铺了一层银霜。）"

    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0118.mp3"
    anya "哇……这里好美啊。"

    show anya look around at anya_std zorder 10
    voice "audio/voice/anya_0119.mp3"
    anya "我从来不知道，废弃工厂后面还有这么漂亮的地方。"

    play sound "audio/sfx/sfx_fireflies.mp3"

    我 "（突然，一点微弱的绿光在草丛中闪烁。）"
    voice "audio/voice/me_0069.mp3"
    我 "嗯？那是什么？"

    voice "audio/voice/anya_0120.mp3"
    anya "萤火虫！"

    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0121.mp3"
    anya "是萤火虫！好多萤火虫！"

    我 "（越来越多的萤火虫从草丛中飞了出来，像无数颗坠落的星星，在夜空中飞舞。）"
    我 "（绿色的光点忽明忽暗，把整个山坡都照亮了，美得像一场梦。）"

    voice "audio/voice/anya_0122.mp3"
    anya "哇！太漂亮了！"

    voice "audio/voice/anya_0123.mp3"
    anya "我长这么大，还是第一次看到这么多萤火虫！"

    # 分支差异：肢体接触
    if branch_type == 1 and anya_affection >= 60:
        show anya turn to me at anya_std zorder 10
        voice "audio/voice/anya_0404.mp3"
        anya "林辰，你看！那只萤火虫飞到我手上了！"

        hide me
        show me looking anya at me_std zorder 10
        我 "（我走到她身边，低头看着她手上的萤火虫。）"

        voice "audio/voice/anya_0405.mp3"
        anya "你看你看！它在发光！"

        $ anya_affection += 6
        $ trust_level += 4
        我 "（她的手软软的，小小的，带着一丝凉意。）"
        我 "（心跳突然漏了一拍。）"

    else:
        hide me
        show me looking anya at me_std zorder 10
        我 "是啊，真的很漂亮。"

        show anya turn to me at anya_std zorder 10
        voice "audio/voice/anya_0406.mp3"
        anya "林辰，快帮我拍几张照片！我要和萤火虫合影！"

        $ anya_affection += 4
        $ trust_level += 2

    hide me
    show me raise camera at me_std zorder 10
    play sound "audio/sfx/camera_shutter.mp3"
    我 "（我举起相机，按下了快门。）"
    我 "（照片里，她站在萤火虫的光海中，笑得像个孩子，金色的头发在月光下闪闪发光。）"
    我 "（这张照片，后来成为了「暗夜蔷薇」最经典的宣传图。）"

    # ---- 屋顶看星星 ----
    scene cg_rooftop_stars at bg_cover with dissolve
    play music "audio/bgm/bgm_sunset.mp3" fadein 1.0

    我 "（我们爬上了工厂的屋顶。）"
    我 "（从这里可以看到整个山城的夜景，万家灯火像星星一样散落在大地上，远处的跨江大桥亮着暖黄色的灯光。）"

    show anya look out window at anya_std zorder 10
    voice "audio/voice/anya_0124.mp3"
    anya "哇……这里的夜景好美啊。"

    voice "audio/voice/anya_0125.mp3"
    anya "我以前怎么没发现，山城的夜晚这么漂亮。"

    hide me
    show me looking anya at me_std zorder 10
    voice "audio/voice/me_0070.mp3"
    我 "因为你以前总是一个人忙着工作，从来没有停下来好好看过这个城市。"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0126.mp3"
    anya "……也许吧。"

    show anya look up determined at anya_std zorder 10
    voice "audio/voice/anya_0127.mp3"
    anya "你看，好多星星啊。"

    voice "audio/voice/me_0071.mp3"
    我 "嗯。今天天气好，能看到很多平时看不到的星星。"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0128.mp3"
    anya "我小时候，在英国的时候，也经常和妈妈一起看星星。"

    voice "audio/voice/anya_0129.mp3"
    anya "那时候，妈妈会告诉我每一颗星星的名字，还给我讲关于星星的故事。"

    voice "audio/voice/anya_0130.mp3"
    anya "后来回到中国，就再也没有人陪我看星星了。"

    我 "（我静静地听着她说。）"

    voice "audio/voice/anya_0131.mp3"
    anya "刚回来的时候，我一句中文都不会说，长得也和别人不一样。"
    voice "audio/voice/anya_0132.mp3"
    anya "同学们都欺负我，叫我「洋鬼子」，不愿意和我玩。"
    voice "audio/voice/anya_0133.mp3"
    anya "我每天都一个人吃饭，一个人放学，一个人待在教室里。"

    show anya blush look away at anya_std zorder 10
    voice "audio/voice/anya_0134.mp3"
    anya "那时候我就在想，是不是我真的很讨厌，所以大家都不喜欢我。"

    $ trust_level += 2
    我 "（心里一阵刺痛。）"
    我 "（原来她高冷的外表下，藏着这么多不为人知的委屈和孤独。）"

    hide me
    show me smile sincere at me_std zorder 10
    voice "audio/voice/me_0072.mp3"
    我 "不是的。你一点都不讨厌。"

    voice "audio/voice/me_0073.mp3"
    我 "你很坚强，很勇敢，为了自己的梦想一直在努力。"
    voice "audio/voice/me_0074.mp3"
    我 "你设计的裙子很漂亮，你拍的照片也很好看。"
    voice "audio/voice/me_0075.mp3"
    我 "很多人都喜欢你，只是你不知道而已。"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0135.mp3"
    anya "……真的吗？"

    voice "audio/voice/me_0076.mp3"
    我 "真的。"

    voice "audio/voice/me_0077.mp3"
    我 "而且……以后我陪你看星星。"
    voice "audio/voice/me_0078.mp3"
    我 "以后你再也不是一个人了。"

    voice "audio/voice/anya_0136.mp3"
    anya "……"
    voice "audio/voice/anya_0137.mp3"
    anya "谁……谁要你陪啊。"

    show anya turn away at anya_std zorder 10
    voice "audio/voice/anya_0138.mp3"
    anya "不过……如果你非要陪的话，我也不是不可以勉强接受。"

    hide me
    show me smile at me_std zorder 10
    我 "（我看着她泛红的耳尖，忍不住笑了。）"
    我 "（真是个死鸭子嘴硬的家伙。）"

    # ---- 送回宿舍 ----
    scene bg_university_dormitory_gate at bg_cover with dissolve

    show anya stop at anya_std zorder 10
    voice "audio/voice/anya_0139.mp3"
    anya "好了，我到了。"

    hide me
    show me looking anya at me_std zorder 10
    voice "audio/voice/me_0079.mp3"
    我 "我送你上去吧。你的脚还没好。"

    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0140.mp3"
    anya "不用了，我自己可以的。"

    voice "audio/voice/anya_0141.mp3"
    anya "再说了，男生不能进女生宿舍。"

    voice "audio/voice/me_0080.mp3"
    我 "那好吧。你自己小心点。"

    show anya turn to leave at anya_std zorder 10
    voice "audio/voice/anya_0142.mp3"
    anya "今天……谢谢你。"

    show anya turn back at anya_std zorder 10
    voice "audio/voice/anya_0143.mp3"
    anya "不仅帮我拍了这么多好看的照片，还……陪我看了星星。"

    show anya smile soft at anya_close zorder 10
    voice "audio/voice/anya_0144.mp3"
    anya "这是我过得最开心的一天。"

    $ anya_affection += 8
    voice "audio/voice/me_0081.mp3"
    我 "我也是。"

    voice "audio/voice/anya_0145.mp3"
    anya "对了，明天早上八点，我们在学校门口见。"
    voice "audio/voice/anya_0146.mp3"
    anya "一起去印刷厂看宣传册的样稿。"

    voice "audio/voice/me_0082.mp3"
    我 "好。我准时到。"

    show anya wave goodbye at anya_std zorder 10
    voice "audio/voice/anya_0147.mp3"
    anya "拜拜。"

    show anya run into dormitory at anya_std zorder 10
    我 "（看着她跑开的背影，我站在原地，久久没有离开。）"

    scene black with fade

    show text "第二章：星夜下的拍摄 完" with fade
    pause
    show text "敬请期待第三章：印刷厂的危机" with fade
    pause

    scene black with fade
    jump chapter_3
# ===================== 第三章：印刷厂的危机 =====================
label chapter_3:
    scene bg_university_gate_morning at bg_cover with fade
    play music "audio/bgm/bgm_daily.mp3" fadein 1.0

    我 "（第二天早上七点五十，我准时出现在学校门口。）"
    我 "（手里提着刚买的豆浆和包子，还有一瓶云南白药——昨天她的脚踝虽然敷了药，但肯定还没好利索。）"

    show anya arrive at anya_std zorder 10
    voice "audio/voice/anya_0148.mp3"
    anya "早啊。"

    hide anya
    show me smile slight at me_std zorder 10
    voice "audio/voice/me_0083.mp3"
    我 "早。你的脚怎么样了？"

    hide me
    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0149.mp3"
    anya "没事了，已经不疼了。"

    我 "（我指了指她明显不敢用力的右脚）"
    voice "audio/voice/me_0084.mp3"
    我 "是吗？那你走两步给我看看。"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0150.mp3"
    anya "切，不看就不看。"

    hide anya
    show me smile sincere at me_std zorder 10
    voice "audio/voice/me_0085.mp3"
    我 "给你买的早餐，豆浆是热的。还有这个，记得按时喷药。"

    hide me
    show anya blush at anya_std zorder 10
    $ anya_affection += 3
    $ trust_level += 2
    voice "audio/voice/anya_0151.mp3"
    anya "……谢谢。"

    voice "audio/voice/anya_0152.mp3"
    anya "你怎么知道我没吃早饭？"

    hide anya
    show me smile slight at me_std zorder 10
    voice "audio/voice/me_0086.mp3"
    我 "猜的。毕竟某人昨天为了拍夜景，连晚饭都没吃。"

    hide me
    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0153.mp3"
    anya "谁让你拍那么慢的。"

    voice "audio/voice/me_0087.mp3"
    我 "好好好，我的错。快吃吧，不然凉了。"

    scene bg_printing_shop at bg_cover with fade

    我 "（半小时后，我们来到了位于老城区的印刷厂。）"
    我 "（空气中弥漫着油墨和纸张的味道，机器轰隆隆地响着。）"

    show 厂长 at npc_std zorder 10
    voice "audio/voice/factory_mgr_0001.mp3"
    厂长 "安小姐来了啊，样稿已经印出来了，您看看。"

    hide 厂长
    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0154.mp3"
    anya "太好了！终于出来了！"

    我 "（安雅迫不及待地接过样稿，脸上满是期待的笑容。）"

    show anya surprised silent at anya_std zorder 10
    voice "audio/voice/anya_0155.mp3"
    anya "……"

    show anya angry at anya_std zorder 10
    voice "audio/voice/anya_0156.mp3"
    anya "这……这不对啊。"

    scene cg_printing_crisis with dissolve
    我 "（我凑过去一看，心里咯噔一下。）"
    我 "（样稿上的裙子颜色完全不对，原本深邃的黑色变成了发灰的紫色。）"
    scene bg_printing_shop at bg_cover with dissolve

    hide me
    show anya angry at anya_std zorder 10
    voice "audio/voice/anya_0157.mp3"
    anya "这是怎么回事？！我给你们的色值明明是正确的！"

    show 厂长 at npc_right zorder 5
    voice "audio/voice/factory_mgr_0002.mp3"
    厂长 "实在抱歉安小姐，昨天晚上我们的印刷机出了点故障，颜色校准出了问题。"
    voice "audio/voice/factory_mgr_0003.mp3"
    厂长 "您放心，我们马上重新印，一定给您印好。"

    hide 厂长
    show anya angry at anya_std zorder 10
    voice "audio/voice/anya_0158.mp3"
    anya "重新印？什么时候能印好？"

    show 厂长 at npc_right zorder 5
    voice "audio/voice/factory_mgr_0004.mp3"
    厂长 "最快也要三天。"

    hide 厂长
    show anya surprised silent at anya_std zorder 10
    voice "audio/voice/anya_0159.mp3"
    anya "三天？！不行！绝对不行！"

    voice "audio/voice/anya_0160.mp3"
    anya "我的新品发布会就在三天后！宣传册必须今天印好，明天就要发出去！"

    show 厂长 at npc_right zorder 5
    voice "audio/voice/factory_mgr_0005.mp3"
    厂长 "这……这实在是没办法啊。机器已经排满了，最快也要后天才能给您开机。"
    hide 厂长

    show anya turn away at anya_std zorder 10
    voice "audio/voice/anya_0161.mp3"
    anya "怎么会这样……"

    scene bg_printing_shop_corner with dissolve

    show anya sit down at anya_std zorder 10
    show anya look down at anya_std zorder 10
    anya "（蹲在墙角，双手抱着膝盖，肩膀微微颤抖）"

    hide anya
    show me looking anya at me_std zorder 10
    我 "（我站在她身边，看着她难过的样子，心里也跟着揪了起来。）"

    hide me
    show anya blush look away at anya_std zorder 10
    $ trust_level += 4
    voice "audio/voice/anya_0163.mp3"
    anya "（声音带着哭腔）怎么办……一切都搞砸了……"

    voice "audio/voice/anya_0164.mp3"
    anya "我跑了十几家工厂才做出满意的样衣，熬了无数个通宵才设计好宣传册……"
    voice "audio/voice/anya_0165.mp3"
    anya "我以为一切都会很顺利的……"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0166.mp3"
    anya "是不是我真的不行？是不是我根本就不适合做品牌？"

    menu:
        "坚定地告诉她她可以的":
            $ anya_affection += 10
            $ trust_level += 12
            hide me
            show me smile sincere at me_std zorder 10
            我 "不是的。你很优秀，真的。"
            我 "你的设计很有才华，你的努力我都看在眼里。"
            我 "这点小挫折算不了什么，我们一起想办法解决。"

        "冷静地分析解决方案":
            $ anya_affection += 2
            $ trust_level += 5
            hide me
            show me confused at me_std zorder 10
            我 "别慌，现在哭解决不了问题。"
            我 "我们还有时间，一定能想到办法的。"
            我 "先告诉我，宣传册的源文件在你那里吗？"

        "实话实说，这确实很棘手":
            $ anya_affection -= 10
            $ trust_level -= 5
            hide me
            show me sigh at me_std zorder 10
            我 "这确实很麻烦。印刷厂的机器坏了，我们时间又不多了。"
            我 "如果今天印不出来，发布会就赶不上了。"
            我 "（安雅听我这么说，脸色更加难看了。）"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0167.mp3"
    anya "……在我电脑里。"

    hide me
    show me smile at me_std zorder 10
    voice "audio/voice/me_0088.mp3"
    我 "那就好办了。"
    voice "audio/voice/me_0089.mp3"
    我 "印刷厂的机器不行，我们可以找数码快印店。虽然成本高一点，但今天就能印好。"
    voice "audio/voice/me_0090.mp3"
    我 "不过我们需要重新调整颜色参数，把偏差修正过来。"

    show anya surprised silent at anya_std zorder 10
    voice "audio/voice/anya_0168.mp3"
    anya "真的吗？可是……重新调整颜色要花很长时间的。"

    voice "audio/voice/me_0091.mp3"
    我 "没关系，我陪你一起改。"

    hide me
    show me smile slight at me_std zorder 10
    voice "audio/voice/me_0092.mp3"
    我 "大不了通宵一晚上，肯定能赶在明天早上印好。"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0169.mp3"
    anya "……可是你的作业怎么办？你不是说这周要交课程设计吗？"

    hide me
    show me smile sincere at me_std zorder 10
    voice "audio/voice/me_0093.mp3"
    我 "作业可以晚点交，但你的发布会不能推迟。"
    voice "audio/voice/me_0094.mp3"
    我 "我说过，我是你的专属设计师兼摄影师。你的事，就是我的事。"

    show anya blush at anya_std zorder 10
    $ anya_affection += 8
    $ trust_level += 6
    voice "audio/voice/anya_0170.mp3"
    anya "……谢谢你。"
    voice "audio/voice/anya_0171.mp3"
    anya "（小声）林辰……"

    scene bg_print_shop_24h at bg_cover with fade

    我 "（下午两点，我们找到了一家数码快印店，开始重新调整宣传册的颜色。）"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0172.mp3"
    anya "这里的红色再加深一点……还有这个银色，要更亮一点。"

    hide anya
    show me looking anya at me_std zorder 10
    voice "audio/voice/me_0095.mp3"
    我 "不行，再亮就会显得廉价了。稍微降低一点饱和度，增加一点灰度。"

    hide me
    show anya nod at anya_std zorder 10
    voice "audio/voice/anya_0173.mp3"
    anya "嗯，有道理。"

    我 "（时间一分一秒地过去，窗外的天渐渐黑了。）"

    scene bg_print_shop_24h_night at bg_cover with dissolve

    hide anya
    show me sigh at me_std zorder 10
    我 "（已经晚上十一点了。眼睛已经开始发酸，脖子也僵硬得不行。）"

    hide me
    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0174.mp3"
    anya "（打了个哈欠）好累啊……"

    hide anya
    show me smile sincere at me_std zorder 10
    voice "audio/voice/me_0096.mp3"
    我 "给你买的咖啡，提提神。"

    hide me
    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0175.mp3"
    anya "谢谢。"

    if branch_type == 1:
        show anya smile smug at anya_std zorder 10
        voice "audio/voice/anya_0407.mp3"
        anya "喂，林辰。你说你这么帮我，是不是喜欢我啊？"

        hide anya
        show me confused at me_std zorder 10
        我 "（差点把咖啡喷出来）你胡说什么呢。"

        hide me
        show anya pout at anya_std zorder 10
        voice "audio/voice/anya_0408.mp3"
        anya "切，不说就算了。"
        voice "audio/voice/anya_0409.mp3"
        anya "（小声嘟囔）明明就是……"

    else:
        show anya look down at anya_std zorder 10
        voice "audio/voice/anya_0410.mp3"
        anya "林辰。对不起啊，耽误你这么多时间。"

        hide anya
        show me smile slight at me_std zorder 10
        我 "没事。能帮到你就好。"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0176.mp3"
    anya "其实……我以前从来没有和别人一起工作过。"
    voice "audio/voice/anya_0177.mp3"
    anya "我总是觉得，别人做的东西都达不到我的要求，所以什么事都自己扛着。"
    voice "audio/voice/anya_0178.mp3"
    anya "但是和你一起工作，我觉得很安心。"

    $ trust_level += 4
    我 "（心里一阵温暖。）以后有什么事，都可以告诉我。不用一个人硬撑着。"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0179.mp3"
    anya "……嗯。"

    scene cg_all_night_work with dissolve
    我 "（凌晨四点，我们终于完成了所有的调整工作。）"
    scene bg_print_shop_24h_night at bg_cover with dissolve

    hide anya
    show me smile at me_std zorder 10

    hide me
    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0180.mp3"
    anya "太好了！终于改完了！"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0097.mp3"
    我 "是啊。现在发给店家，早上八点就能印好。"

    hide me
    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0181.mp3"
    anya "发送成功！终于可以回家睡觉了！"

    scene bg_street_after_rain_mountain_city at bg_cover with dissolve

    show anya look out window at anya_std zorder 10
    voice "audio/voice/anya_0182.mp3"
    anya "哇，雨下得好大啊。"

    hide anya
    show me take out umbrella at me_std zorder 10
    voice "audio/voice/me_0098.mp3"
    我 "我带了伞。走吧，我送你回宿舍。"

    scene bg_university_dormitory_gate at bg_cover with dissolve

    show anya walk beside me at anya_std zorder 10
    我 "（我们并肩走在雨夜里。伞很小，我尽量把伞往她那边倾斜。）"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0183.mp3"
    anya "喂，伞歪了。"

    hide anya
    show me smile slight at me_std zorder 10
    voice "audio/voice/me_0099.mp3"
    我 "没有啊，正好。"

    hide me
    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0184.mp3"
    anya "明明就歪了！你都淋湿了！笨蛋……"

    show anya stop at anya_std zorder 10
    voice "audio/voice/anya_0185.mp3"
    anya "我到了。你的肩膀都湿透了……回去赶紧洗个热水澡，别感冒了。"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0100.mp3"
    我 "知道了。你也赶紧上去休息吧。"

    hide me
    show anya turn to leave at anya_std zorder 10
    voice "audio/voice/anya_0186.mp3"
    anya "今天……真的谢谢你。如果没有你，我真的不知道该怎么办。"

    show anya smile soft at anya_close zorder 10
    voice "audio/voice/anya_0187.mp3"
    anya "晚安，林辰。"

    show anya run into dormitory at anya_std zorder 10
    voice "audio/voice/me_0101.mp3"
    我 "晚安。"

    scene black with fade

    我 "（回到宿舍的时候，已经凌晨五点了。浑身都湿透了，头也开始晕晕的。）"
    我 "（随便冲了个热水澡，就倒在床上睡着了。）"

    scene bg_my_dormitory at bg_cover with fade

    hide anya
    show me casual lie_in_bed at me_std zorder 10
    我 "（醒来的时候，已经是中午了。头痛欲裂，浑身发烫。）"
    我 "（糟了，好像发烧了。）"

    voice "audio/voice/anya_0188.mp3"
    anya "宣传册印好了！效果特别好！你醒了吗？我请你吃饭！"

    hide me
    show me casual weak at me_std zorder 10
    我 "（回复：我有点不舒服，不去了）"

    voice "audio/voice/anya_0189.mp3"
    anya "你怎么了？哪里不舒服？"

    voice "audio/voice/me_0102.mp3"
    我 "没事，就是有点发烧，睡一觉就好了。"

    voice "audio/voice/anya_0190.mp3"
    anya "发烧？多少度？"

    voice "audio/voice/me_0103.mp3"
    我 "不知道……没量。"

    voice "audio/voice/anya_0191.mp3"
    anya "你等着！我马上过来！"

    hide me
    show me casual confused at me_std zorder 10
    voice "audio/voice/me_0104.mp3"
    我 "哎？不用了，我真的没事……"
    我 "（电话已经挂了。）"

    scene bg_my_dormitory at bg_cover with fade

    我 "（大约二十分钟后，敲门声响起。）"

    show me casual lean on door at me_std zorder 10
    我 "（拖着沉重的身体去开门。）"

    hide me
    show anya casual urgent at anya_std zorder 10
    voice "audio/voice/anya_0192.mp3"
    anya "（气喘吁吁）你怎么样了？"

    hide anya
    show me casual weak at me_std zorder 10
    voice "audio/voice/me_0105.mp3"
    我 "没事……就是有点晕。"

    hide me
    show anya casual angry at anya_std zorder 10
    voice "audio/voice/anya_0193.mp3"
    anya "快回床上躺着去！来，量一下体温。"
    voice "audio/voice/anya_0194.mp3"
    anya "都烧成这样了还说没事！你是不是傻啊！"

    hide anya
    show me casual smile slight at me_std zorder 10
    voice "audio/voice/me_0106.mp3"
    我 "哪有那么严重……"

    hide me
    show anya casual angry at anya_std zorder 10
    voice "audio/voice/anya_0195.mp3"
    anya "39度2！还说不严重！你等着，我去给你买药！"

    scene bg_my_dormitory with dissolve

    show anya casual stand_at_door at anya_std zorder 10
    我 "（没过多久，安雅就拿着药回来了。头发和衣服都被雨水打湿了。）"

    show anya casual pout at anya_std zorder 10
    voice "audio/voice/anya_0196.mp3"
    anya "来，吃药。"

    hide anya
    show me casual smile at me_std zorder 10
    voice "audio/voice/me_0107.mp3"
    我 "谢谢。"

    hide me
    show anya casual look_around at anya_std zorder 10
    voice "audio/voice/anya_0197.mp3"
    anya "你饿不饿？我给你煮点粥吧。"

    hide anya
    show me casual confused at me_std zorder 10
    voice "audio/voice/me_0108.mp3"
    我 "你会煮粥？"

    hide me
    show anya casual pout at anya_std zorder 10
    voice "audio/voice/anya_0198.mp3"
    anya "当然会！你别小看人！"

    scene cg_take_care with dissolve
    我 "（我躺在床上，听着厨房里传来的叮叮当当的声音，心里暖暖的。）"
    我 "（她笨手笨脚地在厨房里忙碌着，时不时传来锅碗瓢盆的碰撞声。虽然看起来很不熟练，但那份心意却让我鼻子发酸。）"
    scene bg_my_dormitory_kitchen with dissolve

    show anya casual cooking at anya_std zorder 10
    voice "audio/voice/anya_0199.mp3"
    anya "粥来了！"

    hide anya
    show me casual confused at me_std zorder 10
    我 "（看着碗里黑乎乎的东西）这……这是粥？"

    hide me
    show anya casual blush at anya_std zorder 10
    voice "audio/voice/anya_0200.mp3"
    anya "呃……可能火有点大了……不过应该能吃！"

    hide anya
    show me casual smile at me_std zorder 10
    我 "（味道一言难尽，但看着她期待的眼神，我还是全部吃完了。）好吃。"

    hide me
    show anya casual smile happy quickly at anya_std zorder 10
    voice "audio/voice/anya_0201.mp3"
    anya "真的吗？那我以后经常做给你吃！"

    hide anya
    show me casual confused at me_std zorder 10
    我 "（连忙摆手）不用不用！太麻烦你了！"

    hide me
    show anya casual pout at anya_std zorder 10
    voice "audio/voice/anya_0202.mp3"
    anya "切，好心没好报。"

    scene bg_my_dormitory at bg_cover with dissolve

    hide anya
    show me casual smile at me_std zorder 10
    我 "（吃了药睡了一觉，感觉好多了。）"

    hide me
    show anya casual look_down at anya_std zorder 10
    voice "audio/voice/anya_0203.mp3"
    anya "感觉怎么样了？"

    voice "audio/voice/me_0109.mp3"
    我 "好多了，谢谢你。"

    voice "audio/voice/anya_0204.mp3"
    anya "对不起……都是因为我，你才会生病的。"

    hide anya
    show me casual smile sincere at me_std zorder 10
    voice "audio/voice/me_0110.mp3"
    我 "不关你的事。是我自己不小心。而且，能帮到你，我很高兴。"

    show anya casual blush at anya_std zorder 10
    $ anya_affection += 8
    $ trust_level += 8
    voice "audio/voice/anya_0205.mp3"
    anya "林辰。"
    voice "audio/voice/anya_0206.mp3"
    anya "以前我总是觉得，什么事都要靠自己，别人都靠不住。"
    voice "audio/voice/anya_0207.mp3"
    anya "但是遇到你之后，我才发现，原来有人可以依靠的感觉，这么好。"
    voice "audio/voice/anya_0208.mp3"
    anya "原来……我不是一个人在战斗。"

    hide me
    show me casual smile sincere at me_std zorder 10
    voice "audio/voice/me_0111.mp3"
    我 "你从来都不是一个人。以后，我会一直陪着你。"

    show anya casual blush at anya_std zorder 10
    voice "audio/voice/anya_0209.mp3"
    anya "……嗯。"

    show anya casual turn_to_leave at anya_std zorder 10
    voice "audio/voice/anya_0210.mp3"
    anya "时间不早了，我该回去了。你好好休息。"
    voice "audio/voice/anya_0211.mp3"
    anya "对了，下周三我们要去郊区的工厂选布料。等你病好了，我们一起去。"

    hide me
    show me casual smile at me_std zorder 10
    voice "audio/voice/me_0112.mp3"
    我 "好。"

    show anya casual wave_goodbye at anya_std zorder 10
    voice "audio/voice/anya_0212.mp3"
    anya "拜拜。"

    show anya casual run_into_dormitory at anya_std zorder 10
    我 "（我站在窗边，看着安雅离开的背影。夕阳洒在她的身上，镀上了一层金色的光芒。）"
    我 "（原来，照顾一个人的感觉，这么好。）"

    scene black with fade

    show text "第三章：印刷厂的危机 完" with fade
    pause
    show text "敬请期待第四章：山城的火锅" with fade
    pause

    scene black with fade
    jump chapter_4

# ===================== 第四章：山城的火锅 =====================
label chapter_4:
    scene bg_university_gate_morning at bg_cover with fade
    play music "audio/bgm/bgm_daily.mp3" fadein 1.0

    我 "（周三早上八点，我准时在学校门口等安雅。）"
    我 "（经过几天的休息，我的烧已经退了，安雅的脚踝也基本好了。）"

    show anya arrive at anya_std zorder 10
    voice "audio/voice/anya_0213.mp3"
    anya "早啊！"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0113.mp3"
    我 "早。东西都带齐了吗？"

    hide me
    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0214.mp3"
    anya "带齐了！色卡、样布、笔记本，一样都没少。"

    voice "audio/voice/anya_0215.mp3"
    anya "今天我们要去郊区的那家布料厂，他们家的蕾丝质量是整个山城最好的。"

    hide me
    show me smile slight at me_std zorder 10
    voice "audio/voice/me_0114.mp3"
    我 "好，那我们走吧。"

    # ---- 第一幕：郊区布料工厂 ----
    scene bg_suburb_factory at bg_cover with fade

    我 "（一个小时后，我们来到了位于郊区的布料工厂。）"
    我 "（巨大的厂房里堆满了各种颜色和材质的布料，空气中弥漫着布料和染料的味道。）"

    show 王老板 at npc_std zorder 10
    voice "audio/voice/boss_wang_0001.mp3"
    王老板 "安小姐来了啊！这次要找什么布料？"

    hide 王老板
    show anya look around at anya_std zorder 10
    voice "audio/voice/anya_0216.mp3"
    anya "王老板好。我要找一款黑色的哑光蕾丝，还有银色的刺绣线。"

    voice "audio/voice/anya_0217.mp3"
    anya "就是上次我跟你说的那款，要最柔软的那种，不能扎皮肤。"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0218.mp3"
    anya "（拿起一卷蕾丝仔细地摸着，眉头微微皱起）这个不行，太硬了。穿在身上会不舒服。"

    voice "audio/voice/anya_0219.mp3"
    anya "还有别的吗？"

    hide anya
    show 王老板 at npc_std zorder 10
    voice "audio/voice/boss_wang_0002.mp3"
    王老板 "有有有，这边还有一批进口的，你看看。"

    hide 王老板
    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0220.mp3"
    anya "（拿起另一卷蕾丝，眼睛一下子亮了）就是这个！这个手感太好了！"

    voice "audio/voice/anya_0221.mp3"
    anya "王老板，就要这个，给我来五百米。还有银色的刺绣线，也要最好的那种。"

    hide anya
    show 王老板 at npc_std zorder 10
    voice "audio/voice/boss_wang_0003.mp3"
    王老板 "没问题！安小姐的眼光就是好，这批货刚到，你是第一个看上的。"

    voice "audio/voice/boss_wang_0004.mp3"
    王老板 "年纪轻轻就这么能干，自己做品牌，真了不起啊。"

    hide 王老板
    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0222.mp3"
    anya "（耳朵一下子红了）哪里哪里，都是王老板照顾。"

    hide anya
    show me smile slight at me_std zorder 10
    我 "（看着她强装镇定的样子，忍不住偷偷笑了。）"
    我 "（这还是我第一次看到她被别人夸得脸红的样子，有点可爱。）"

    scene bg_abandoned_factory_interior at bg_cover with fade

    hide me
    show anya nod at anya_std zorder 10
    anya "（认真地签着合同，一笔一划，非常仔细。）"

    我 "（我站在旁边看着她，心里有些感慨。）"
    我 "（平时她总是一副傲娇又任性的样子，但在工作的时候，却异常的认真和专业。）"

    voice "audio/voice/anya_0224.mp3"
    anya "好了，王老板，合同签好了。下周三之前能发货吗？"

    hide anya
    show 王老板 at npc_std zorder 10
    voice "audio/voice/boss_wang_0005.mp3"
    王老板 "没问题！一定准时送到。"

    hide 王老板

    scene bg_abandoned_factory_gate_mountain_city at bg_cover with fade

    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0225.mp3"
    anya "（伸了个懒腰）呼……终于搞定了！"

    voice "audio/voice/anya_0226.mp3"
    anya "没想到这么顺利，比我预想的早了好几个小时。"

    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0227.mp3"
    anya "那个……今天下午没事了。"

    $ anya_affection += 3

    menu:
        "那我们去吃火锅吧":
            $ anya_affection += 8
            $ trust_level += 8

            hide anya
            show me smile at me_std zorder 10
            我 "正好我也饿了。我知道老城区有一家特别地道的九宫格老火锅，要不要去试试？"

            hide me
            show anya excited at anya_std zorder 10
            voice "audio/voice/anya_0411.mp3"
            anya "好啊好啊！我早就想吃火锅了！"

            show anya blush at anya_std zorder 10
            voice "audio/voice/anya_0412.mp3"
            anya "（连忙清了清嗓子）咳……既然你这么诚心邀请，那我就勉强陪你去吧。"

            jump hot_pot_date

        "那我先回去了":
            hide anya
            show me smile at me_std zorder 10
            我 "那我先回学校了，还有点作业要写。"

            hide me
            show anya look down at anya_std zorder 10
            voice "audio/voice/anya_0413.mp3"
            anya "……哦，好吧。那……宣传册的事，我们微信联系。"

            show anya turn to leave at anya_std zorder 10
            voice "audio/voice/anya_0414.mp3"
            anya "拜拜。"

            我 "（看着她有点失落的背影，我心里有点后悔。）"

            scene black with fade
            show text "你选择了先回去，错过了和安雅一起吃饭的机会。" with dissolve
            pause
            show text "好感度提升的机会减少了……" with dissolve
            pause

            jump missed_hot_pot_date

# ---- 第二幕（精简版）：山城火锅·错过篇 ----
label missed_hot_pot_date:
    scene bg_old_hotpot_shop at bg_cover with fade
    play music "audio/bgm/bgm_warm.mp3" fadein 1.0

    我 "（一周后，我们约在一家火锅店碰面讨论宣传册的事。）"
    我 "（虽然上次没有一起吃饭，但安雅还是主动约了我。）"
    我 "（她看起来心情不错，没有因为上次的事生气。）"

    show anya smile soft at anya_std zorder 10
    voice "audio/voice/anya_0228.mp3"
    anya "你来啦。快坐吧，我已经点好菜了。"

    hide anya
    show me smile slight at me_std zorder 10
    voice "audio/voice/me_0115.mp3"
    我 "不好意思，让你久等了。"

    hide me
    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0229.mp3"
    anya "哼，知道就好。今天主要是讨论宣传册的事，你别想太多。"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0116.mp3"
    我 "好，听你的。"

    # 精简的火锅场面 - 好感小幅加成
    $ anya_affection += 3
    $ trust_level += 3

    scene black with fade
    我 "（我们简单吃了顿饭，聊了宣传册的细节。）"
    我 "（虽然氛围没有上次一起吃饭那么亲密，但也没有我想象中那么尴尬。）"
    pause

    jump birthday_surprise

# ---- 第二幕：山城九宫格火锅 ----
label hot_pot_date:
    scene bg_old_hotpot_shop at bg_cover with fade
    play music "audio/bgm/bgm_warm.mp3" fadein 1.0

    我 "（傍晚时分，我们来到了老城区的那家九宫格老火锅。）"
    我 "（店里人声鼎沸，热气腾腾，空气中弥漫着牛油火锅的香味。）"

    show anya look around at anya_std zorder 10
    voice "audio/voice/anya_0230.mp3"
    anya "哇……好多人啊。"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0117.mp3"
    我 "这家店开了二十多年了，味道特别正宗，所以每天都爆满。"

    scene bg_old_hotpot_shop at bg_cover with fade

    hide me
    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0231.mp3"
    anya "（看着桌上的九宫格锅底）这个……为什么要分成九个格子啊？"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0118.mp3"
    我 "不同的格子温度不一样，中间的火最大，适合涮毛肚鸭肠这种需要快煮的，边上的火小，适合煮土豆藕片这种需要慢炖的。"

    hide me
    show anya nod at anya_std zorder 10
    voice "audio/voice/anya_0232.mp3"
    anya "哦……原来是这样。"

    hide anya
    show 服务员 at npc_std zorder 10
    voice "audio/voice/waiter_0001.mp3"
    服务员 "两位要点什么锅底？我们这里有微辣、中辣、特辣。"

    hide 服务员
    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0233.mp3"
    anya "（偷偷看了我一眼）那就……特辣吧！我能吃辣！"

    hide anya
    show me smile slight at me_std zorder 10
    voice "audio/voice/me_0119.mp3"
    我 "是吗？我怎么记得上次有人吃小面都被辣得直吐舌头。"

    hide me
    show anya pout at anya_std zorder 10
    voice "audio/voice/anya_0234.mp3"
    anya "那是意外！我现在很能吃辣了！"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0120.mp3"
    我 "好好好，那就微辣吧。我不能吃太辣。"

    hide me
    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0235.mp3"
    anya "（偷偷松了一口气）好吧，那就听你的，微辣。"

    我 "（我看着她的样子，忍不住笑了。其实我早就看到她偷偷跟服务员比了个微辣的手势。）"

    scene bg_old_hotpot_shop at bg_cover with dissolve

    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0236.mp3"
    anya "哇……开了开了！"

    voice "audio/voice/anya_0237.mp3"
    anya "（拿起筷子就要往锅里放毛肚）这个要煮多久啊？"

    $ anya_affection += 3
    $ trust_level += 2
    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0121.mp3"
    我 "等等，我教你。毛肚要七上八下，就是在锅里涮八次，每次提起来一下，这样煮出来的毛肚才会脆。"

    hide me
    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0238.mp3"
    anya "（手被我抓住，脸一下子红了）哦……哦好。"

    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0239.mp3"
    anya "（小心翼翼地按照我说的方法涮着毛肚）这样……可以了吗？"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0122.mp3"
    我 "可以了，尝尝看。"

    hide me
    show anya smile happy quickly at anya_std zorder 10
    voice "audio/voice/anya_0240.mp3"
    anya "（咬了一口，眼睛一下子亮了）哇！好好吃！好脆啊！"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0123.mp3"
    我 "好吃就多吃点。"

    我 "（我看着她吃得津津有味的样子，心里暖暖的。）"
    我 "（火锅的热气模糊了她的脸，她的脸颊红红的，嘴唇也红红的，看起来特别可爱。）"

    hide me
    show anya blush at anya_std zorder 10
    anya "（用纸巾擦了擦嘴，偷偷看了我一眼，发现我在看她，连忙低下头）"

    $ anya_affection += 3
    voice "audio/voice/anya_0242.mp3"
    anya "那个……你喜欢吃什么？"

    hide anya
    show me smile slight at me_std zorder 10
    voice "audio/voice/me_0124.mp3"
    我 "我都可以，不挑食。"

    voice "audio/voice/anya_0243.mp3"
    anya "那你除了拍照和设计，还喜欢做什么？"

    voice "audio/voice/me_0125.mp3"
    我 "喜欢看电影，还有爬山。山城的山很多，周末没事的时候我就会去爬山。"

    voice "audio/voice/me_0126.mp3"
    我 "你呢？除了设计裙子，还喜欢做什么？"

    hide me
    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0244.mp3"
    anya "我喜欢看星星，还有听古典音乐。"

    voice "audio/voice/anya_0245.mp3"
    anya "小时候在英国的时候，我家后面有一片很大的草地，晚上我就会躺在草地上看星星。"

    show anya blush look away at anya_std zorder 10
    voice "audio/voice/anya_0246.mp3"
    anya "那时候的星星特别亮，比山城的亮多了。"

    hide anya
    show me smile sincere at me_std zorder 10
    voice "audio/voice/me_0127.mp3"
    我 "以后我带你去南山看星星。南山的海拔高，没有光污染，星星也很亮。"

    hide me
    show anya excited at anya_std zorder 10
    voice "audio/voice/anya_0247.mp3"
    anya "真的吗？"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0128.mp3"
    我 "真的。"

    hide me
    show anya smile happy quickly at anya_std zorder 10
    voice "audio/voice/anya_0248.mp3"
    anya "（喝了一口酸梅汤）其实……我挺喜欢山城的。"

    voice "audio/voice/anya_0249.mp3"
    anya "虽然夏天很热，冬天很冷，路也很难走，但这里的人很热情，东西也很好吃。"

    voice "audio/voice/anya_0250.mp3"
    anya "而且……在这里，我遇到了很多喜欢我设计的人。"

    hide anya
    show me smile sincere at me_std zorder 10
    voice "audio/voice/me_0129.mp3"
    我 "以后你会遇到更多的。来，再喝一杯酸梅汤。解解辣。"

    hide me
    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0251.mp3"
    anya "谢谢。"

    $ anya_affection += 4
    我 "（我们的手指不小心碰到了一起，两个人都愣了一下。）"
    anya "（连忙收回手，低下头，脸红得像熟透的苹果）"
    我 "（我的心跳也漏了一拍，连忙移开视线。）"
    我 "（火锅的热气模糊了我们的视线，但我却能清晰地听到自己的心跳声。）"

# ---- 第三幕：江边生日惊喜 ----
label birthday_surprise:
    scene bg_river_walk at bg_cover with fade
    play music "audio/bgm/bgm_sunset.mp3" fadein 1.0

    我 "（吃完火锅，我们沿着江边散步。）"
    我 "（夜晚的江边很凉快，微风吹拂着脸颊，非常舒服。）"
    我 "（对岸的灯光璀璨，倒映在江面上，波光粼粼。）"

    show anya walk beside me at anya_std zorder 10
    voice "audio/voice/anya_0253.mp3"
    anya "今天的火锅真好吃。谢谢你请我吃火锅。"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0130.mp3"
    我 "不用谢。我也吃得很开心。"

    hide me
    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0254.mp3"
    anya "（沉默了一会儿，轻声说）其实……今天是我生日。"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0131.mp3"
    我 "我知道。"

    hide me
    show anya surprised silent at anya_std zorder 10
    voice "audio/voice/anya_0255.mp3"
    anya "你……你怎么知道？"

    hide anya
    show me smile slight at me_std zorder 10
    voice "audio/voice/me_0132.mp3"
    我 "拍宣传册那天，看到你身份证了。"

    hide me
    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0256.mp3"
    anya "……你记性真好。"

    hide anya
    show me smile sincere at me_std zorder 10
    voice "audio/voice/me_0133.mp3"
    我 "关于你的事，我都记得。给，生日礼物。"

    hide me
    show anya surprised silent at anya_std zorder 10
    voice "audio/voice/anya_0257.mp3"
    anya "你……你还给我准备了礼物？"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0134.mp3"
    我 "打开看看吧。"

    scene cg_birthday_gift with dissolve

    $ anya_affection += 15
    $ trust_level += 8

    voice "audio/voice/anya_0258.mp3"
    anya "（看着照片，眼睛一下子红了）这是……那天晚上的萤火虫……"

    voice "audio/voice/me_0135.mp3"
    我 "嗯。我觉得这张照片拍得最好，所以打印出来送给你。"

    voice "audio/voice/me_0136.mp3"
    我 "希望你每次看到它，都能想起那个美好的夜晚。"

    if anya_affection >= 80:
        voice "audio/voice/anya_0415.mp3"
        anya "（眼泪一下子掉了下来）谢谢你……林辰。"
        voice "audio/voice/anya_0416.mp3"
        anya "这是我收到过最好的生日礼物。"
        voice "audio/voice/anya_0417.mp3"
        anya "以前从来没有人记得我的生日，也没有人给我送过礼物。"

        我 "以后每年的生日，我都陪你过。"

    elif anya_affection >= 50:
        voice "audio/voice/anya_0418.mp3"
        anya "（红着眼眶，吸了吸鼻子）哼……还行吧，勉强及格。"
        voice "audio/voice/anya_0419.mp3"
        anya "（小声）其实……挺好看的。"

        我 "喜欢就好。"

    else:
        voice "audio/voice/anya_0420.mp3"
        anya "……谢谢。"
        voice "audio/voice/anya_0421.mp3"
        anya "（紧紧地抱着相框，眼神复杂）"

# ---- 第四幕：江边告白伏笔 ----
label river_confession_foreshadow:
    scene bg_river_viewing_platform at bg_cover with fade
    play music "audio/bgm/bgm_dream.mp3" fadein 1.0

    我 "（我们走到了江边的观景台。）"
    我 "（从这里可以看到整个山城的夜景，万家灯火像星星一样散落在大地上。）"

    show anya look out window at anya_std zorder 10
    voice "audio/voice/anya_0259.mp3"
    anya "（靠在栏杆上，看着对岸的灯光）林辰，你知道我为什么要做Lolita品牌吗？"

    hide anya
    show me looking anya at me_std zorder 10
    voice "audio/voice/me_0137.mp3"
    我 "嗯？为什么？"

    hide me
    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0260.mp3"
    anya "小时候在英国，我喜欢穿Lolita裙，同学们都嘲笑我，说我穿得像个怪物。"

    voice "audio/voice/anya_0261.mp3"
    anya "后来回到中国，又有人说我崇洋媚外，说我穿奇装异服。"

    voice "audio/voice/anya_0262.mp3"
    anya "那时候我就想，Lolita是我的盔甲。穿上它，我就可以变得很强大，就不会再被别人欺负了。"

    hide anya
    show me smile sincere at me_std zorder 10
    voice "audio/voice/me_0138.mp3"
    我 "不是盔甲。"

    hide me
    show anya surprised silent at anya_std zorder 10
    voice "audio/voice/anya_0263.mp3"
    anya "嗯？"

    hide anya
    show me smile sincere at me_std zorder 10
    voice "audio/voice/me_0139.mp3"
    我 "是翅膀。穿上它的你，是最自由的。"

    hide me
    show anya cry at anya_std zorder 10
    voice "audio/voice/anya_0264.mp3"
    anya "（转过头看着我，眼睛里闪烁着泪光）翅膀……"

    voice "audio/voice/anya_0265.mp3"
    anya "林辰……谢谢你出现在我的生命里。"
    voice "audio/voice/anya_0266.mp3"
    anya "如果没有你，我可能早就放弃了。"

    menu:
        "其实我也想说一样的话":
            $ anya_affection += 12
            $ trust_level += 12

            hide anya
            show me smile sincere at me_std zorder 10
            我 "其实我也想说一样的话。遇到你之后，我的生活也变得不一样了。"

            hide me
            show anya blush at anya_std zorder 10
            voice "audio/voice/anya_0422.mp3"
            anya "……"
            voice "audio/voice/anya_0423.mp3"
            anya "（低下头，小声说）笨蛋。"

        "我们是搭档嘛":
            $ anya_affection += 5
            $ trust_level += 6

            hide anya
            show me smile at me_std zorder 10
            我 "我们是搭档嘛。你的事，就是我的事。"

        "（沉默，不知道说什么）":
            $ anya_affection -= 5
            $ trust_level -= 5

            hide anya
            show me stand alone at me_std zorder 10
            我 "（我不知道该说什么，只是沉默地站在那里。）"

            hide me
            show anya look down at anya_std zorder 10
            voice "audio/voice/anya_0424.mp3"
            anya "（她看出我的尴尬，也沉默了。）"

            hide me
            show anya look down at anya_std zorder 10
            voice "audio/voice/anya_0425.mp3"
            anya "……哦，对。搭档。"
            voice "audio/voice/anya_0426.mp3"
            anya "（转过头，继续看着江面，眼神有点失落）"

# ---- 第五幕：送回宿舍 ----
label send_back_dorm:
    scene bg_university_dormitory_gate at bg_cover with fade

    show anya stop at anya_std zorder 10
    voice "audio/voice/anya_0267.mp3"
    anya "我到了。"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0140.mp3"
    我 "嗯。上去吧，早点休息。"

    hide me
    show anya turn to leave at anya_std zorder 10
    anya "（走了几步，又转回身）"

    $ anya_affection += 4
    $ trust_level += 4
    voice "audio/voice/anya_0269.mp3"
    anya "林辰。"
    voice "audio/voice/anya_0270.mp3"
    anya "今天……是我过得最开心的一个生日。"
    voice "audio/voice/anya_0271.mp3"
    anya "明年生日，你也来。"

    show anya run into dormitory at anya_std zorder 10
    我 "（还没等我回应，她就红着脸跑进了宿舍大楼。）"

    我 "（我站在原地，看着她消失的背影，忍不住笑了。）"
    我 "（心里暖暖的，像被什么东西填满了。）"

    scene black with fade

    show text "第四章：山城的火锅 完" with fade
    pause
    show text "好感度和信任度将在第五章决定结局走向" with fade
    pause

    scene black with fade
    jump chapter_5

# ===================== 第五章：暗夜蔷薇的绽放 =====================
label chapter_5:
    scene bg_anya_studio at bg_cover with fade
    play music "audio/bgm/bgm_tense.mp3" fadein 1.0

    我 "（发布会前一天下午，我来到了安雅的工作室。）"
    我 "（工作室不大，但收拾得井井有条，墙上贴满了设计稿，桌子上放着各种布料和针线。）"
    我 "（明天就是「暗夜蔷薇」第一次新品发布会了，整个工作室都弥漫着紧张又期待的氛围。）"


    show anya casual work at anya_std zorder 10
    anya "（正蹲在地上整理衣服，头发有点乱，脸上沾了一点线头）"
    voice "audio/voice/anya_0273.mp3"
    anya "你来了啊！快过来帮我看看这个吊牌有没有问题。"

    hide anya
    show me casual smile at me_std zorder 10
    我 "（蹲下身，接过吊牌）"
    voice "audio/voice/me_0141.mp3"
    我 "没问题，设计得很好看。"

    hide me
    show anya casual stand_up at anya_std zorder 10
    anya "（拍了拍手上的灰）"
    voice "audio/voice/anya_0275.mp3"
    anya "那就好。所有的准备工作都差不多了，就等明天的样衣送到了。"

    voice "audio/voice/anya_0276.mp3"
    anya "这次的发布会我准备了很久，一定要成功。"

    hide anya
    show me casual confident at me_std zorder 10
    voice "audio/voice/me_0142.mp3"
    我 "一定会成功的。你的设计这么好，大家都会喜欢的。"

    hide me
    show anya casual smile_smug at anya_std zorder 10
    voice "audio/voice/anya_0277.mp3"
    anya "哼，那是当然。也不看看是谁设计的。"

    play sound "audio/sfx/sfx_phone_ring.mp3"
    show anya casual call at anya_std zorder 10
    voice "audio/voice/anya_0278.mp3"
    anya "喂？您好，是快递吗？"

    show anya casual smile happy quickly at anya_std zorder 10
    voice "audio/voice/anya_0279.mp3"
    anya "对，是我的快递。麻烦您送上来吧，谢谢。"

    voice "audio/voice/anya_0280.mp3"
    anya "太好了！样衣到了！"

    scene bg_studio_door at bg_cover with fade
    play sound "audio/sfx/sfx_knock.mp3"

    show anya casual excited at anya_std zorder 10
    voice "audio/voice/anya_0281.mp3"
    anya "来了来了！"

    show 快递员 at npc_right zorder 10
    voice "audio/voice/courier_0001.mp3"
    快递员 "您好，安小姐的快递。麻烦签收一下。"

    hide 快递员
    show anya casual nod at anya_std zorder 10
    voice "audio/voice/anya_0282.mp3"
    anya "谢谢！"

    show anya casual open_box at anya_std zorder 10
    anya "（迫不及待地打开箱子，然后愣住了）"
    voice "audio/voice/anya_0284.mp3"
    anya "……"

    show anya casual shocked at anya_std zorder 10
    voice "audio/voice/anya_0285.mp3"
    anya "空的？箱子是空的！"

    hide anya
    show me casual confused at me_std zorder 10
    我 "（凑过去一看，箱子里果然什么都没有，只有几张揉皱的报纸。）"
    voice "audio/voice/me_0143.mp3"
    我 "怎么会这样？"

    hide me
    show anya casual panic at anya_std zorder 10
    voice "audio/voice/anya_0286.mp3"
    anya "不可能！我明明看着快递员把样衣装进去的！"

    anya "（翻遍了整个箱子，急得快要哭了）"
    voice "audio/voice/anya_0288.mp3"
    anya "样衣呢？我的样衣去哪里了？"

    show anya casual call at anya_std zorder 10
    anya "（颤抖着拨通了快递员的电话）"
    voice "audio/voice/anya_0290.mp3"
    anya "喂！我的快递怎么是空的？！你把我的样衣弄到哪里去了？"

    show anya casual angry at anya_std zorder 10
    voice "audio/voice/anya_0291.mp3"
    anya "什么？中转站搞错了？送到别的地方去了？"

    voice "audio/voice/anya_0292.mp3"
    anya "那什么时候能找回来？明天早上？不行！明天早上我就要用！"

    show anya look down at anya_std zorder 10
    anya "（无力地挂了电话，瘫坐在地上）"

    scene cg_ch5_lost_dress with dissolve
    stop music fadeout 0.5

    voice "audio/voice/anya_0294.mp3"
    anya "完了……一切都完了。"

    voice "audio/voice/anya_0295.mp3"
    anya "明天就是发布会了，没有样衣，我怎么开发布会？"

    voice "audio/voice/anya_0296.mp3"
    anya "所有人都在等着看我的笑话……我就知道，我根本就做不好……"

    scene bg_studio_door at bg_cover with dissolve
    play music "audio/bgm/bgm_tense.mp3"
    show anya casual cry at anya_std zorder 10
    anya "（双手捂着脸，肩膀剧烈地颤抖着）"
    voice "audio/voice/anya_0298.mp3"
    anya "我真的好没用……"

    hide anya
    show me casual squat at me_std zorder 10
    voice "audio/voice/me_0144.mp3"
    我 "安雅，别这样。"

    show me casual smile sincere at me_std zorder 10
    voice "audio/voice/me_0145.mp3"
    我 "现在哭解决不了问题。我们还有时间，一定能把样衣找回来的。"

    hide me
    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0299.mp3"
    anya "怎么找？快递员说最快也要明天早上才能找回来！"

    voice "audio/voice/anya_0300.mp3"
    anya "明天早上九点发布会就开始了，根本来不及！"

    hide anya
    show me casual confident at me_std zorder 10
    voice "audio/voice/me_0146.mp3"
    我 "相信我。我们现在就去快递中转站，一定能在今天晚上把样衣找回来。"

    hide me
    show anya casual look up surprised at anya_std zorder 10
    voice "audio/voice/anya_0301.mp3"
    anya "可是……中转站那么大，那么多快递，我们怎么找？"

    hide anya
    show me casual confident at me_std zorder 10
    voice "audio/voice/me_0147.mp3"
    我 "只要有一丝希望，就不能放弃。"

    voice "audio/voice/me_0148.mp3"
    我 "你忘了吗？我们连印刷厂的危机都一起挺过来了。这次也一定可以的。"

    show me casual smile sincere at me_std zorder 10
    voice "audio/voice/me_0149.mp3"
    我 "走吧。我陪你一起去找。"

    hide me
    show anya casual look_at_me at anya_std zorder 10
    $ trust_level += 8
    voice "audio/voice/anya_0302.mp3"
    anya "……嗯。"

    # ---- 寻找样衣 ----
    scene bg_courier_station at bg_cover with fade
    play music "audio/bgm/bgm_tense.mp3" fadein 1.0

    我 "（一个小时后，我们来到了位于郊区的快递中转站。）"
    我 "（巨大的仓库里堆满了成千上万的快递，叉车来来往往，噪音震耳欲聋。）"

    show 站长 at npc_std zorder 10
    voice "audio/voice/station_mgr_0001.mp3"
    站长 "实在抱歉安小姐，是我们的工作人员失误，把您的快递和另一个同名的快递搞混了。"

    voice "audio/voice/station_mgr_0002.mp3"
    站长 "那个快递已经被送到城西的一个小区了。我们已经联系了收件人，但是她不在家，要晚上八点才能回来。"

    hide 站长
    show anya casual urgent at anya_std zorder 10
    voice "audio/voice/anya_0303.mp3"
    anya "晚上八点？那我们现在就过去等她！"

    # ---- 城西小区等待 ----
    scene bg_west_community at bg_cover with fade
    play sound "audio/sfx/env_rain.mp3" loop

    我 "（下午六点，我们来到了城西的那个小区。）"
    我 "（天空下起了小雨，气温也降了下来。）"

    show anya casual sit_on_steps at anya_std zorder 10
    anya "（坐在单元楼门口的台阶上，双手抱着膝盖，眼神空洞地看着前方）"

    hide anya
    show me casual sit beside at me_std zorder 10
    voice "audio/voice/me_0150.mp3"
    我 "别担心，很快就能等到了。"

    hide me
    show anya casual lean_on_me at anya_std zorder 10
    $ anya_affection += 6
    anya "（轻轻靠在我的肩膀上，声音沙哑）"
    voice "audio/voice/anya_0306.mp3"
    anya "林辰，如果这次找不回样衣，怎么办？"

    hide anya
    show me casual put arm at me_std zorder 10
    voice "audio/voice/me_0151.mp3"
    我 "不会的。一定能找回来的。"

    voice "audio/voice/me_0152.mp3"
    我 "就算真的找不回来，我们还有备用布料。大不了通宵一晚上，重新做一件。"

    hide me
    show anya look down at anya_std zorder 10
    voice "audio/voice/anya_0307.mp3"
    anya "可是……一晚上根本做不完。「星夜」的刺绣那么复杂。"


    hide anya
    show me casual smile sincere at me_std zorder 10
    voice "audio/voice/me_0153.mp3"
    我 "没关系。我陪你一起做。我虽然不会做衣服，但我可以帮你钉珠子，剪线头。"

    voice "audio/voice/me_0154.mp3"
    我 "只要我们一起努力，就没有做不到的事。"

    hide me
    show anya casual look_at_me at anya_std zorder 10
    voice "audio/voice/anya_0308.mp3"
    anya "……谢谢你。"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0309.mp3"
    anya "有你在，真好。"

    # ---- 夜晚拿到样衣 ----
    scene bg_west_community_night at bg_cover with fade
    play sound "audio/sfx/env_rain_heavy.mp3" loop

    我 "（晚上八点，那个收件人终于回来了。）"
    我 "（当我们从她手里接过那个熟悉的箱子时，我和安雅都松了一口气。）"

    show anya casual open_box_happy at anya_std zorder 10
    anya "（打开箱子，看到那件黑色的「星夜」裙子完好无损地躺在里面，眼泪一下子掉了下来。）"

    voice "audio/voice/anya_0311.mp3"
    anya "太好了……太好了……"

    hide anya
    show me smile at me_std zorder 10
    voice "audio/voice/me_0155.mp3"
    我 "我就说吧，一定能找回来的。"

    # ---- 通宵赶工 ----
    scene bg_anya_studio_night at bg_cover with fade
    play music "audio/bgm/bgm_warm.mp3" fadein 1.0

    我 "（晚上九点，我们回到了工作室。）"
    我 "（样衣虽然找回来了，但在运输过程中沾了一点灰尘，还有几颗珠子掉了。）"

    show anya casual clean_dress at anya_std zorder 10
    anya "（小心翼翼地清理着裙子上的灰尘）"
    voice "audio/voice/anya_0313.mp3"
    anya "幸好没有弄坏，不然我真的不知道该怎么办了。"

    hide anya
    show me casual take beads at me_std zorder 10
    voice "audio/voice/me_0156.mp3"
    我 "我来帮你钉珠子吧。你告诉我怎么弄。"

    hide me
    show anya casual teach_me at anya_std zorder 10
    voice "audio/voice/anya_0316.mp3"
    anya "好。你看，就是这样，把珠子穿在针上，然后缝在裙子上。"

    我 "（按照安雅教我的方法，认真地钉着珠子。）"
    我 "（时间一分一秒地过去，窗外的雨还在下着。）"
    我 "（工作室里很安静，只有针线穿过布料的声音和我们的呼吸声。）"

    show anya look_at_me at anya_std zorder 10
    anya "（停下手里的活，看着我认真的侧脸，眼神温柔）"
    voice "audio/voice/anya_0318.mp3"
    anya "林辰。"

    hide anya
    show me look up at me_std zorder 10
    voice "audio/voice/me_0157.mp3"
    我 "嗯？怎么了？"

    hide me
    show anya smile soft at anya_close zorder 10
    voice "audio/voice/anya_0319.mp3"
    anya "没什么。就是觉得……能遇到你，真好。"

    $ anya_affection += 8
    我 "（心里一阵温暖）"
    voice "audio/voice/me_0158.mp3"
    我 "我也是。"

    # ---- 黎明完成 ----
    scene bg_anya_studio_dawn at bg_cover with fade

    我 "（凌晨五点，我们终于完成了所有的工作。）"
    我 "（「星夜」裙子焕然一新，比之前更加漂亮了。）"


    show anya stretch at anya_std zorder 10
    anya "（伸了个懒腰）"
    voice "audio/voice/anya_0321.mp3"
    anya "终于搞定了！"

    voice "audio/voice/anya_0322.mp3"
    anya "现在才五点，还有四个小时发布会才开始。我们可以休息一下。"

    hide anya
    show me tired at me_std zorder 10
    voice "audio/voice/me_0159.mp3"
    我 "好啊。"

    # ---- 天台告白高潮 ----
    scene bg_studio_rooftop at bg_cover with fade
    play music "audio/bgm/bgm_confession.mp3" fadein 1.0

    我 "（我们爬上了工作室的屋顶。）"
    我 "（天已经蒙蒙亮了，东方的天空泛起了鱼肚白。）"
    我 "（远处的山城还在沉睡，只有零星的灯光亮着。）"

    show anya casual lean_on_railing at anya_std zorder 10
    anya "（靠在栏杆上，看着远方的日出）"
    voice "audio/voice/anya_0324.mp3"
    anya "好美啊。"

    voice "audio/voice/me_0160.mp3"
    我 "嗯。好久没有看过日出了。"

    show anya casual turn to me at anya_std zorder 10
    voice "audio/voice/anya_0325.mp3"
    anya "林辰。"

    voice "audio/voice/anya_0326.mp3"
    anya "其实……我有话想对你说。"

    hide anya casual
    show me casual look_at_anya at me_std zorder 10
    voice "audio/voice/me_0161.mp3"
    我 "我也有话想对你说。"

    scene cg_ch5_confession with dissolve

    # ---- 基于好感度和信任度的告白分支 ----
    if anya_affection >= 110 and trust_level >= 80:
        # 完美告白结局
        我 "安雅，我喜欢你。"
        我 "从第一次在漫展角落看到你的时候，我就注意到你了。"
        我 "后来和你一起工作，一起经历了那么多事，我越来越喜欢你。"
        我 "喜欢你的倔强，喜欢你的认真，喜欢你嘴硬心软的样子。"
        我 "我想做你的男朋友，想一直陪在你身边，和你一起把「暗夜蔷薇」做下去。"


        scene bg_studio_rooftop at bg_cover with dissolve
        show anya casual cry_happy at anya_close zorder 10
        voice "audio/voice/anya_0427.mp3"
        anya "（眼泪一下子掉了下来，笑着捶了我一下）"
        voice "audio/voice/anya_0428.mp3"
        anya "笨蛋！你怎么现在才说！"

        voice "audio/voice/anya_0429.mp3"
        anya "我早就喜欢你了！从你帮我处理伤口的时候，从你陪我通宵赶宣传册的时候，从你送我萤火虫照片的时候……"
        voice "audio/voice/anya_0430.mp3"
        anya "我一直在等你说这句话。"

        hide anya casual
        show me casual hug at me_std zorder 10
        我 "（紧紧地抱住她）"
        我 "对不起，让你等了这么久。"

        show anya casual blush at anya_close zorder 10
        voice "audio/voice/anya_0431.mp3"
        anya "（靠在我的怀里，声音哽咽）"
        voice "audio/voice/anya_0432.mp3"
        anya "林辰，我喜欢你。真的很喜欢你。"

        $ anya_affection += 15
        $ trust_level += 18

    elif anya_affection >= 80 and trust_level >= 60:
        # 犹豫告白结局
        我 "安雅，我喜欢你。"
        我 "我不知道从什么时候开始，我的眼里就只有你了。"
        我 "我想和你在一起，不只是工作伙伴。"

        scene bg_studio_rooftop at bg_cover with dissolve
        show anya casual blush at anya_std zorder 10
        voice "audio/voice/anya_0433.mp3"
        anya "（低下头，手指绞着衣角）"
        voice "audio/voice/anya_0434.mp3"
        anya "……我……"

        voice "audio/voice/anya_0435.mp3"
        anya "我也喜欢你。但是……我有点害怕。"

        voice "audio/voice/anya_0436.mp3"
        anya "我从来没有谈过恋爱，我不知道怎么和别人相处。"
        voice "audio/voice/anya_0437.mp3"
        anya "而且，我的品牌才刚刚起步，未来还有很多不确定的事情。"

        hide anya casual
        show me casual smile sincere at me_std zorder 10
        我 "没关系。我们可以慢慢来。"
        我 "不管未来有什么困难，我都会陪你一起面对。"

        hide me casual
        show anya casual look_at_me at anya_std zorder 10
        voice "audio/voice/anya_0438.mp3"
        anya "……嗯。"

        show anya casual blush look away at anya_std zorder 10
        voice "audio/voice/anya_0439.mp3"
        anya "那……我们就试试吧。"

        $ anya_affection += 5
        $ trust_level += 3

        scene black with fade
        show text "她虽然没有完全答应，但至少……没有拒绝。" with dissolve
        pause
        scene black with fade
        jump chapter_5_transition

    else:
        # 告白失败结局
        我 "安雅，我喜欢你。"

        scene bg_studio_rooftop at bg_cover with dissolve
        show anya casual surprised_silent at anya_std zorder 10
        voice "audio/voice/anya_0440.mp3"
        anya "……"

        show anya casual look_down at anya_std zorder 10
        voice "audio/voice/anya_0441.mp3"
        anya "对不起，林辰。"

        voice "audio/voice/anya_0442.mp3"
        anya "我……我一直把你当成最好的搭档和朋友。"
        voice "audio/voice/anya_0443.mp3"
        anya "我从来没有想过别的事情。"

        hide anya casual
        show me casual smile slight at me_std zorder 10
        我 "没关系。是我唐突了。"

        我 "那我们……还是做朋友吧。"

        hide me casual
        show anya casual nod at anya_std zorder 10
        voice "audio/voice/anya_0444.mp3"
        anya "……嗯。"

        $ anya_affection -= 5
        $ trust_level -= 5

        # 告白失败直接跳结局
        scene black with fade
        show text "告白被拒绝了……" with dissolve
        pause
        show text "虽然发布会还是顺利举行了，但我们之间的距离，似乎越来越远了。" with dissolve
        pause
        jump sad_ending_ch6

    # ---- 结尾过渡 ----
    scene bg_anya_studio at bg_cover with fade

    show anya casual look_at_clock at anya_std zorder 10
    voice "audio/voice/anya_0327.mp3"
    anya "啊！已经八点了！我们该去发布会现场了！"

    hide anya casual
    show me casual smile at me_std zorder 10
    voice "audio/voice/me_0162.mp3"
    我 "好。走吧。"

    hide me
    show anya take dress at anya_std zorder 10
    anya "（小心翼翼地抱起「星夜」裙子）"

    voice "audio/voice/anya_0329.mp3"
    anya "今天的发布会，一定会成功的。"

    hide anya
    show me confident at me_std zorder 10
    voice "audio/voice/me_0163.mp3"
    我 "一定会的。"

    scene black with fade

    show text "第五章：暗夜蔷薇的绽放 完" with fade
    pause
    show text "你的选择将决定最终的结局" with fade
    pause

    scene black with fade
    jump chapter_6


label chapter_5_transition:
    scene bg_anya_studio at bg_cover with fade

    show anya casual look_at_clock at anya_std zorder 10
    voice "audio/voice/anya_0327.mp3"
    anya "啊！已经八点了！我们该去发布会现场了！"

    hide anya casual
    show me casual smile at me_std zorder 10
    voice "audio/voice/me_0162.mp3"
    我 "好。走吧。"

    hide me
    show anya take dress at anya_std zorder 10
    anya "（小心翼翼地抱起「星夜」裙子）"

    voice "audio/voice/anya_0329.mp3"
    anya "今天的发布会，一定会成功的。"

    hide anya
    show me confident at me_std zorder 10
    voice "audio/voice/me_0163.mp3"
    我 "一定会的。"

    scene black with fade

    show text "第五章：暗夜蔷薇的绽放 完" with fade
    pause
    show text "你的选择将决定最终的结局" with fade
    pause

    scene black with fade
    jump chapter_6


# ===================== 第六章：夏天的约定 =====================
label chapter_6:
    scene bg_conference_hall_backstage at bg_cover with fade
    play music "audio/bgm/bgm_tense.mp3" fadein 1.0
    play sound "audio/sfx/env_crowd_far.mp3" fadein 0.3

    我 "（上午八点半，发布会后台化妆间。）"
    我 "（工作人员来来往往，紧张地做着最后的准备。）"
    我 "（安雅正在化妆镜前做最后的造型，穿着那件「星夜」裙子，美得像从画里走出来的一样。）"

    show anya wear_starry_night_dress at anya_std zorder 10
    anya "（通过镜子看着我）"
    voice "audio/voice/anya_0331.mp3"
    anya "你怎么才来？我还以为你要迟到了。"

    show me walk_to_anya at me_std zorder 10
    voice "audio/voice/me_0164.mp3"
    我 "怎么会迟到。你的专属摄影师，永远不会缺席。"

    show anya wear_starry_night_dress blush at anya_std zorder 10
    voice "audio/voice/anya_0332.mp3"
    anya "哼，算你识相。"

    hide anya
    hide me
    show 主持人_enter at npc_right zorder 10
    voice "audio/voice/host_0001.mp3"
    主持人 "安小姐，还有十分钟发布会就要开始了。"

    hide 主持人
    show anya wear_starry_night_dress at anya_std zorder 10
    voice "audio/voice/anya_0333.mp3"
    anya "好，我知道了。"

    # 安雅站起身
    anya "（深吸一口气，手微微发抖）"
    voice "audio/voice/anya_0335.mp3"
    anya "我……我有点紧张。"

    show me put_hand_on_anya_shoulder at me_std zorder 10
    我 "（走到她身后，双手轻轻搭在她肩上）这几个月你熬了多少个通宵，为的不就是今天吗？"
    voice "audio/voice/me_0165.mp3"
    我 "我会在台下，一直看着你。"

    show anya smile soft at anya_std zorder 10
    voice "audio/voice/anya_0336.mp3"
    anya "嗯。"

    scene bg_conference_hall at bg_cover with fade
    play music "audio/bgm/bgm_dramatic.mp3" fadein 1.0
    play sound "audio/sfx/env_crowd_applause.mp3"

    我 "（发布会准时开始。）"
    我 "（聚光灯打在T台上，安雅作为主理人第一个出场。）"
    我 "（她穿着「星夜」裙子，一步步走在T台上，自信又耀眼。）"
    我 "（台下的观众都看呆了，随即爆发出热烈的掌声。）"

    show anya walk_runway at anya_std zorder 10
    anya "（走到T台中央，停下脚步，对着台下深深鞠了一躬）"
    voice "audio/voice/anya_0338.mp3"
    anya "大家好，我是「暗夜蔷薇」的主理人安雅。"
    voice "audio/voice/anya_0339.mp3"
    anya "欢迎大家来到「星夜」系列新品发布会。"
    voice "audio/voice/anya_0340.mp3"
    anya "这个系列，我花了整整三个月的时间设计。"
    voice "audio/voice/anya_0341.mp3"
    anya "曾经有人说，Lolita是小众文化。也有人说，我一个女孩子，不可能把品牌做起来。"
    voice "audio/voice/anya_0342.mp3"
    anya "但我想说，只要有梦想，并且愿意为之努力，就没有什么是不可能的。"
    voice "audio/voice/anya_0343.mp3"
    anya "而且，我不是一个人在战斗。"

    show anya look_at_me at anya_std zorder 10
    anya "（目光穿过人群，落在我的身上）"
    voice "audio/voice/anya_0345.mp3"
    anya "谢谢你，林辰。"

    $ anya_affection += 4
    play sound "audio/sfx/env_crowd_applause.mp3"

    我 "（心脏猛地一跳，看着台上闪闪发光的她，心里充满了骄傲和感动。）"
    我 "（那个曾经在漫展角落独自舔舐伤口的女孩，现在已经站在了属于自己的舞台上。）"

    scene bg_conference_hall_backstage at bg_cover with fade
    play music "audio/bgm/bgm_happy.mp3" fadein 1.0
    play sound "audio/sfx/env_crowd_cheer.mp3" fadein 0.3

    show anya run_to_me at anya_std zorder 10
    anya "（发布会结束后，安雅兴奋地跑向我）"
    voice "audio/voice/anya_0347.mp3"
    anya "林辰！我们成功了！"

    show me hug_anya at me_std zorder 10
    voice "audio/voice/me_0166.mp3"
    我 "恭喜你，安雅。你做到了。"

    anya "（靠在我的怀里，声音哽咽）"
    voice "audio/voice/anya_0349.mp3"
    anya "我真的做到了……我以为我永远都做不到……"

    hide anya
    show 王总_enter at npc_std zorder 10
    voice "audio/voice/president_wang_0001.mp3"
    王总 "安小姐，恭喜恭喜！发布会非常成功！"
    voice "audio/voice/president_wang_0002.mp3"
    王总 "我是星辰服饰的总经理。我们非常看好「暗夜蔷薇」的发展前景，想以五百万的价格收购你的品牌。"
    voice "audio/voice/president_wang_0003.mp3"
    王总 "如果你同意的话，我们会给你提供最好的资源和平台，让你的品牌走向全国。"

    show anya surprised silent at anya_std zorder 10
    voice "audio/voice/anya_0350.mp3"
    anya "五百万？"

    我 "（五百万。对于一个连房租都经常拖欠的独立设计师来说，这是她这辈子听到的最大数字。）"
    我 "（我注意到她握着玻璃杯的手，指节泛白。）"

    show 王总_nod at npc_std zorder 10
    voice "audio/voice/president_wang_0004.mp3"
    王总 "是的。这是我们的合同，你可以先看看。"

    scene black with dissolve
    我 "（安雅拿着合同，陷入了沉默。）"
    我 "（五百万，对于一个刚起步的独立品牌来说，无疑是一个天文数字。）"

    if anya_affection >= 130 and trust_level >= 95:
        jump perfect_ending_ch6
    elif anya_affection >= 85 and trust_level >= 65:
        jump normal_ending_ch6
    else:
        jump sad_ending_ch6

# ===================== 完美结局：夏日永恒 =====================
label perfect_ending_ch6:
    scene bg_conference_hall_backstage at bg_cover with fade
    show anya wear_starry_night_dress look_at_me at anya_std zorder 10
    anya "（抬起头，看着我，眼神坚定）"
    voice "audio/voice/anya_0352.mp3"
    anya "对不起，王总。我不能接受你的收购。"

    show 王总_surprised at npc_std zorder 10
    voice "audio/voice/president_wang_0005.mp3"
    王总 "为什么？五百万已经是很高的价格了。"

    show anya smile at anya_std zorder 10
    voice "audio/voice/anya_0353.mp3"
    anya "因为「暗夜蔷薇」是我的孩子。我想亲手把它养大。"
    voice "audio/voice/anya_0354.mp3"
    anya "虽然现在很难，但我相信，只要我和林辰一起努力，总有一天会成功的。"

    show 王总_disappointed at npc_std zorder 10
    voice "audio/voice/president_wang_0006.mp3"
    王总 "好吧。既然你已经决定了，我也不勉强。如果以后改变主意了，随时可以联系我。"

    show 王总_leave at npc_std zorder 10
    hide 王总
    show me smile at me_std zorder 10
    voice "audio/voice/me_0167.mp3"
    我 "你真的想好了吗？五百万不是小数目。"

    show anya take_my_hand at anya_std zorder 10
    voice "audio/voice/anya_0355.mp3"
    anya "我想好了。"
    voice "audio/voice/anya_0356.mp3"
    anya "钱可以慢慢赚，但梦想不能卖。"
    voice "audio/voice/anya_0357.mp3"
    anya "而且，有你在我身边，我什么都不怕。"

    scene bg_nanshan_mountain at bg_cover with fade
    show weather_clear at bg_cover
    play sound "audio/sfx/env_crickets.mp3" fadein 0.3

    我 "（发布会结束后的第二天晚上，我带安雅去了南山。）"
    我 "（兑现第四章的承诺，带她来看星星。）"

    show anya look up surprised at anya_std zorder 10
    voice "audio/voice/anya_0358.mp3"
    anya "哇……好多星星啊。"
    voice "audio/voice/anya_0359.mp3"
    anya "比我小时候在英国看到的还要亮。"

    show me smile at me_std zorder 10
    voice "audio/voice/me_0168.mp3"
    我 "我说过，会带你来南山看星星的。"

    show anya lean on me at anya_std zorder 10
    voice "audio/voice/anya_0360.mp3"
    anya "嗯。你说过的话，都做到了。"
    voice "audio/voice/anya_0361.mp3"
    anya "林辰，你还记得我们第一次见面的地方吗？"

    voice "audio/voice/me_0169.mp3"
    我 "当然记得。漫展场外的那个偏僻角落。"

    voice "audio/voice/anya_0362.mp3"
    anya "那时候我真的好狼狈。脚扭了，又热又累，还被你偷拍了。"

    voice "audio/voice/me_0170.mp3"
    我 "那时候我就在想，这个女孩真好看，怎么会一个人坐在那种地方。"

    show anya look_at_me at anya_std zorder 10
    voice "audio/voice/anya_0363.mp3"
    anya "那时候我怎么也不会想到，那个偷拍我的男生，会成为我生命中最重要的人。"

    scene cg_kiss at bg_cover with dissolve
    $ renpy.pause(3.0, hard=True)

    voice "audio/voice/anya_0364.mp3"
    anya "林辰，我爱你。"
    voice "audio/voice/me_0171.mp3"
    我 "我也爱你，安雅。"

    scene bg_rooftop_one_year_later at bg_cover with fade
    show weather_sunny at bg_cover
    play music "audio/bgm/bgm_ending.mp3" fadein 1.0
    我 "（一年后。）"
    我 "（「暗夜蔷薇」已经成为了国内知名的Lolita品牌。）"
    我 "（我毕业之后，成为了品牌的全职设计总监。）"

    show anya lean on me at anya_std zorder 10
    anya "（靠在我的肩膀上，看着远处的夕阳）"
    voice "audio/voice/anya_0366.mp3"
    anya "时间过得真快啊。一转眼，一年就过去了。"

    voice "audio/voice/me_0172.mp3"
    我 "是啊。那个夏天，好像就在昨天。"

    show me take_out_photo at me_std zorder 10
    voice "audio/voice/me_0173.mp3"
    我 "你看。"

    show anya look_at_me at anya_std zorder 10
    anya "（接过照片，是我们初遇时我偷拍的那张）"
    voice "audio/voice/anya_0368.mp3"
    anya "你还留着这张照片啊。"

    voice "audio/voice/me_0174.mp3"
    我 "当然。这是我们故事的开始。"

    show anya smile soft at anya_std zorder 10
    voice "audio/voice/anya_0369.mp3"
    anya "这个夏天结束了。"

    voice "audio/voice/me_0175.mp3"
    我 "是啊。但我们的故事，才刚刚开始。"

    scene black with fade

    show text "完美结局：夏日永恒" with fade
    pause
    show text "你们一起把梦想变成了现实，也找到了属于彼此的永恒" with fade
    pause

    scene black with fade
    return

# ===================== 普通结局：未来可期 =====================
label normal_ending_ch6:
    scene bg_conference_hall_backstage at bg_cover with fade
    show anya look down at anya_std zorder 10
    anya "（拿着合同，犹豫了很久）"
    voice "audio/voice/anya_0371.mp3"
    anya "对不起，王总。我还是想再试试自己做。"

    show 王总_nod at npc_std zorder 10
    voice "audio/voice/president_wang_0007.mp3"
    王总 "好吧。我尊重你的决定。"

    show 王总_leave at npc_std zorder 10
    hide 王总
    show me smile at me_std zorder 10
    voice "audio/voice/me_0176.mp3"
    我 "我还以为你会接受。"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0372.mp3"
    anya "我也犹豫过。但是一想到要把「暗夜蔷薇」交给别人，我就舍不得。"
    voice "audio/voice/anya_0373.mp3"
    anya "不过……我现在还没有信心能把它做好。"

    show me smile at me_std zorder 10
    voice "audio/voice/me_0177.mp3"
    我 "没关系。我们可以慢慢来。"
    voice "audio/voice/me_0178.mp3"
    我 "等你毕业之后，我们一起努力。"

    scene bg_university_gate_morning at bg_cover with fade
    play music "audio/bgm/bgm_warm.mp3" fadein 1.0
    我 "（又过了一年，安雅毕业了。）"
    我 "（她没有接受任何公司的收购，继续经营着「暗夜蔷薇」。）"
    我 "（我也顺利毕业，找到了一份设计工作。）"

    show anya wave at anya_std zorder 10
    voice "audio/voice/anya_0374.mp3"
    anya "林辰！这里！"

    show me smile at me_std zorder 10
    voice "audio/voice/me_0179.mp3"
    我 "怎么了？这么急着找我。"

    show anya take at anya_std zorder 10
    voice "audio/voice/anya_0375.mp3"
    anya "你看！这是上海漫展的门票。我们的品牌被邀请去参展了！"

    voice "audio/voice/me_0180.mp3"
    我 "真的吗？太好了！"

    voice "audio/voice/anya_0376.mp3"
    anya "是啊！我们终于可以去上海参展了！"

    show anya look_at_me at anya_std zorder 10
    voice "audio/voice/anya_0377.mp3"
    anya "林辰，等这次上海漫展结束，我们就正式在一起吧。"

    show me confused at me_std zorder 10
    voice "audio/voice/me_0181.mp3"
    我 "真的吗？"

    show anya blush at anya_std zorder 10
    voice "audio/voice/anya_0378.mp3"
    anya "嗯。这一年来，你一直陪在我身边，帮我解决了那么多问题。"
    voice "audio/voice/anya_0379.mp3"
    anya "我现在有信心了。我可以做好品牌，也可以做好你的女朋友。"

    show me smile at me_std zorder 10
    voice "audio/voice/me_0182.mp3"
    我 "好。我等你。"

    scene bg_train_station at bg_cover with fade
    play music "audio/bgm/bgm_hopeful.mp3" fadein 1.0
    show anya wave at anya_std zorder 10
    voice "audio/voice/anya_0380.mp3"
    anya "我走了！等我回来！"

    show me stand at me_std zorder 10
    voice "audio/voice/me_0183.mp3"
    我 "一路顺风！我等你回来！"

    我 "（看着火车缓缓驶离，我心里充满了期待。）"
    我 "（虽然我们现在还不能天天在一起，但我们都在为了共同的未来努力着。）"
    我 "（等明年夏天，我们就可以永远在一起了。）"

    scene black with fade

    show text "普通结局：未来可期" with fade
    pause
    show text "你们约定好，等梦想实现的那一天，就正式在一起" with fade
    pause

    scene black with fade
    return

# ===================== 遗憾结局：夏日终曲 =====================
label sad_ending_ch6:
    scene bg_conference_hall_backstage at bg_cover with fade
    show anya look down at anya_std zorder 10
    anya "（沉默了很久，终于抬起头）"
    voice "audio/voice/anya_0382.mp3"
    anya "好，我同意收购。"

    show me confused at me_std zorder 10
    voice "audio/voice/me_0184.mp3"
    我 "安雅？"

    show anya look up surprised at anya_std zorder 10
    voice "audio/voice/anya_0383.mp3"
    anya "我累了，林辰。"
    voice "audio/voice/anya_0384.mp3"
    anya "这一年来，我每天都在熬夜，每天都在担心品牌会倒闭。我真的撑不下去了。"
    voice "audio/voice/anya_0385.mp3"
    anya "接受收购，我就不用再这么辛苦了。"

    show me stand at me_std zorder 10
    我 "（看着她疲惫的样子，我心里一阵刺痛。）"
    voice "audio/voice/me_0185.mp3"
    我 "如果你已经决定了，我支持你。"

    scene bg_river_walk at bg_cover with fade
    show weather_heavy_rain at bg_cover
    play music "audio/bgm/bgm_sad.mp3" fadein 1.0
    play sound "audio/sfx/env_rain_light.mp3"

    我 "（一周后，安雅签了收购合同。）"
    我 "（她要去上海总部工作了。）"
    我 "（我去送她。）"

    show anya look out window at anya_std zorder 10
    voice "audio/voice/anya_0386.mp3"
    anya "其实，我挺舍不得山城的。"
    voice "audio/voice/anya_0387.mp3"
    anya "舍不得这里的火锅，舍不得这里的冰粉，也舍不得……你。"

    show me smile at me_std zorder 10
    voice "audio/voice/me_0186.mp3"
    我 "到了上海，要好好照顾自己。"

    voice "audio/voice/anya_0388.mp3"
    anya "嗯。你也是。要好好吃饭，别总是熬夜。"

    show anya take at anya_std zorder 10
    voice "audio/voice/anya_0389.mp3"
    anya "这个给你。"

    我 "（接过盒子，打开一看，是一件黑色的Lolita衬衫，上面有银色的星星刺绣。）"
    voice "audio/voice/anya_0390.mp3"
    anya "这是我专门为你设计的。情侣款。"
    voice "audio/voice/anya_0391.mp3"
    anya "本来想等发布会结束后送给你的。现在……就当是离别礼物吧。"

    show anya cry at anya_std zorder 10
    voice "audio/voice/anya_0392.mp3"
    anya "林辰，对不起。"

    show me smile at me_std zorder 10
    voice "audio/voice/me_0187.mp3"
    我 "不用说对不起。我理解你。"

    show anya walk beside me at anya_std zorder 10
    anya "（紧紧地抱住我，哭了起来）"
    voice "audio/voice/anya_0394.mp3"
    anya "我会想你的。"
    voice "audio/voice/anya_0395.mp3"
    anya "如果……如果以后我回来了，你还会等我吗？"

    show me smile at me_std zorder 10
    voice "audio/voice/me_0188.mp3"
    我 "会的。我会一直等你。"

    scene bg_airport at bg_cover with fade
    show weather_heavy_rain at bg_cover
    play sound "audio/sfx/env_airport_announcement.mp3" fadein 0.3

    show anya turn to leave at anya_std zorder 10
    anya "（转身走向安检口，没有回头。）"
    我 "（看着她的背影消失在人群中，眼泪终于忍不住掉了下来。）"

    scene bg_studio_rooftop at bg_cover with fade
    show weather_sunny at bg_cover
    play music "audio/bgm/bgm_ending.mp3" fadein 1.0
    我 "（三个月后。）"
    我 "（安雅去了上海之后，我们渐渐失去了联系。）"
    我 "（我知道，我们已经是两个世界的人了。）"

    show me stand at me_std zorder 10
    我 "（手里拿着那张初遇时的照片，看着远处的江景。）"
    我 "（那个夏天，就像一场梦。）"
    我 "（梦里有漫展的闷热，有冰粉的清甜，有萤火虫的光芒，还有那个穿着黑色Lolita裙的女孩。）"
    我 "（梦醒了，只剩下照片里的黑玫瑰。）"

    show me smile at me_std zorder 10
    voice "audio/voice/me_0189.mp3"
    我 "再见了，安雅。"
    voice "audio/voice/me_0190.mp3"
    我 "再见了，那个属于我们的夏天。"

    scene black with fade

    show text "遗憾结局：夏日终曲" with fade
    pause
    show text "那个夏天就像一场短暂的梦，醒来后只剩下回忆" with fade
    pause

    scene black with fade
    return