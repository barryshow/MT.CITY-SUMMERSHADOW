"""Check image-file definitions vs actual files in script.rpy"""
import os, re

GAME = r"D:\shanchengxiaying\shanchengxiaying\game"
SCRIPT = os.path.join(GAME, "script.rpy")

with open(SCRIPT, encoding="utf-8") as f:
    lines = f.readlines()

# ── 1. Parse all `image NAME = "PATH"` definitions ──
image_defs = {}  # name -> (path, line_no, line_text)
for i, line in enumerate(lines, 1):
    m = re.match(r'^\s*image\s+(.+?)\s*=\s*"([^"]+)"', line)
    if m:
        name = m.group(1).strip()
        path = m.group(2).strip()
        image_defs[name] = (path, i, line.strip())

# ── 2. Check if each referenced file exists (resolution: characters_alpha/ → characters/, try both) ──
missing_files = []
for name, (path, lno, txt) in image_defs.items():
    full = os.path.join(GAME, "images", path)
    if os.path.isfile(full):
        continue
    # try with characters_ -> characters fallback already covered by path in script
    # check in both characters_alpha/ and characters/
    if "characters_alpha/" in path:
        alt = path.replace("characters_alpha/", "characters/")
        full_alt = os.path.join(GAME, "images", alt)
        if os.path.isfile(full_alt):
            continue
    missing_files.append((name, path, lno))

# ── 3. Collect all file names in images/ directory tree ──
existing_files = set()
for root, dirs, files in os.walk(os.path.join(GAME, "images")):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), os.path.join(GAME, "images"))
        existing_files.add(rel.replace("\\", "/"))

# ── 4. Find unused image files ──
referenced_files = set(path for path, _, _ in image_defs.values())
unused_files = existing_files - referenced_files

# ── 5. Parse all show commands ──
show_cmds = set()
for i, line in enumerate(lines, 1):
    m = re.match(r'^\s*show\s+(\S+)', line)
    if m:
        show_cmds.add(m.group(1))

# ── 6. Parse all scene commands ──
scene_cmds = set()
for i, line in enumerate(lines, 1):
    m = re.match(r'^\s*scene\s+(\S+)', line)
    if m:
        scene_cmds.add(m.group(1))

# ── 7. Check all cg_ / bg_ scene refs have actual image files ──
scene_images = set(name for name in scene_cmds if name.startswith(("bg_", "cg_")))
img_no_file_for_scene = []
for sn in sorted(scene_images):
    # scene may use bg_cover transform so name alone; check any png with that base
    found = any(f.startswith(sn) for f in existing_files)
    if not found:
        img_no_file_for_scene.append(sn)

# ── 8. CG images referenced in script ──
# also check if cg_ files exist
cg_img_files = sorted(f for f in existing_files if f.startswith("cg_"))
print("=== CG files on disk ===")
for f in cg_img_files:
    print(f"  {f}")

# ── Output ──
print(f"\n=== IMAGE DEFINITIONS: {len(image_defs)} total ===")
print(f"Missing referenced files: {len(missing_files)}")
if missing_files:
    for name, path, lno in sorted(missing_files, key=lambda x: x[2]):
        print(f"  Line {lno}: '{name}' -> '{path}' -- FILE NOT FOUND")

print(f"\n=== UNUSED IMAGE FILES: {len(unused_files)} ===")
for f in sorted(unused_files):
    print(f"  {f}")

print(f"\n=== SHOW COMMANDS WITHOUT IMAGE DEF: {len(show_cmds)} shown total ===")
# Check show names not in image_defs
show_no_def = show_cmds - set(image_defs.keys()) - scene_cmds
# Filter out known suffixes (like transforms, non-character shows)
show_no_def = {s for s in show_no_def
               if not s.startswith("text")
               and not s.startswith("bg_")
               and not s.startswith("(")}
if show_no_def:
    print(f"  Show commands with no matching image definition:")
    for s in sorted(show_no_def):
        print(f"    {s}")

print(f"\n=== SCENE BACKGROUNDS MISSING IMAGES: {len(img_no_file_for_scene)} ===")
for s in sorted(img_no_file_for_scene):
    print(f"  {s}")

print("\n=== DONE ===")