"""
批量处理9张新立绘：备份原图 → 用u2net抠图 → 输出到characters_alpha
"""
import os, shutil
import onnxruntime as ort
import numpy as np
from PIL import Image, ImageFilter

SRC_DIR = r"D:\shanchengxiaying\shanchengxiaying\game\images\characters"
DST_DIR = r"D:\shanchengxiaying\shanchengxiaying\game\images\characters_alpha"
BACKUP_DIR = r"D:\shanchengxiaying\shanchengxiaying\game\images\characters_backup"
MODEL_PATH = os.path.join(os.path.expanduser('~'), '.u2net', 'u2net.onnx')
INPUT_SIZE = 320

NEW_FILES = [
    "anya_look_at_me.png",
    "anya_run_to_me.png",
    "anya_take_my_hand.png",
    "anya_walk_runway.png",
    "anya_wear_starry_night_dress.png",
    "anya_blush_post.png",
    "me_hug_anya.png",
    "me_put_hand_on_anya_shoulder.png",
    "me_walk_to_anya.png",
]

# Load model once
print("Loading u2net model...")
session = ort.InferenceSession(MODEL_PATH)
print("Model loaded.")

def preprocess(img):
    img_resized = img.resize((INPUT_SIZE, INPUT_SIZE), Image.LANCZOS)
    arr = np.array(img_resized).astype(np.float32) / 255.0
    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
    arr = (arr - mean) / std
    arr = np.transpose(arr, (2, 0, 1))
    return np.expand_dims(arr, 0).astype(np.float32)

def remove_bg(img_path, out_path):
    img = Image.open(img_path).convert('RGB')
    input_data = preprocess(img)
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    result = session.run([output_name], {input_name: input_data})
    mask = result[0][0, 0]
    mask = (mask - mask.min()) / (mask.max() - mask.min() + 1e-8)
    mask = (mask * 255).astype(np.uint8)
    mask_img = Image.fromarray(mask, 'L').resize(img.size, Image.LANCZOS)
    mask_arr = np.array(mask_img)
    mask_pil = Image.fromarray(mask_arr, 'L').filter(ImageFilter.GaussianBlur(radius=1))
    mask_arr = np.array(mask_pil)
    rgba = np.dstack([np.array(img), mask_arr])
    fully_trans = mask_arr == 0
    rgba[fully_trans, :3] = 0
    out = Image.fromarray(rgba, 'RGBA')
    out.save(out_path, 'PNG')
    return out.size

os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(DST_DIR, exist_ok=True)

for fname in NEW_FILES:
    src = os.path.join(SRC_DIR, fname)
    dst = os.path.join(DST_DIR, fname)
    bak = os.path.join(BACKUP_DIR, fname)

    if not os.path.exists(src):
        print(f"  SKIP {fname} (not found in {SRC_DIR})")
        continue

    # Backup
    shutil.copy2(src, bak)
    print(f"  BACKUP {fname}")

    # Remove background
    try:
        size = remove_bg(src, dst)
        print(f"  OK  {fname} -> {dst} ({size[0]}x{size[1]})")
    except Exception as e:
        print(f"  FAIL {fname}: {e}")
