"""Accurate check of image definitions and references in script.rpy"""
import os, re, sys

GAME = r"D:\shanchengxiaying\shanchengxiaying\game"
SCRIPT = os.path.join(GAME, "script.rpy")

# Use utf-8 for output
sys.stdout.reconfigure(encoding='utf-8')

with open(SCRIPT, encoding="utf-8") as f:
    lines = f.readlines()

# 1. Parse all `image NAME = "PATH"` definitions
image_defs = {}
image_def_paths = {}
for i, line in enumerate(lines, 1):
    m = re.match(r'^\s*image\s+(.+?)\s*=\s*"([^"]+)"', line)
    if m:
        name = m.group(1).strip()
        path = m.group(2).strip()
        image_defs[name] = path
        image_def_paths[name] = (i, path)

# 2. Check missing image definition files
missing_img_defs = []
for name, (lno, path) in sorted(image_def_paths.items(), key=lambda x: x[1][0]):
    full = os.path.join(GAME, "images", path)
    if not os.path.isfile(full):
        missing_img_defs.append((lno, name, path))

print(f"[OK] Image definitions: {len(image_defs)}")
print(f"[MISS] Missing referenced files: {len(missing_img_defs)}")
for lno, name, path in missing_img_defs:
    print(f"  Line {lno}: image {name} = \"{path}\"  -- FILE NOT FOUND")

# 3. Parse all show/hide commands
show_names = {}
for i, line in enumerate(lines, 1):
    m = re.match(r'^\s*show\s+(\S+)', line)
    if m:
        show_names[m.group(1)] = show_names.get(m.group(1), []) + [i]

# 4. Parse all scene commands
scene_names = set()
for i, line in enumerate(lines, 1):
    m = re.match(r'^\s*scene\s+(\S+)', line)
    if m:
        scene_names.add(m.group(1))

# 5. Check show commands against image definitions
show_undef = {}
for sn, linenos in sorted(show_names.items()):
    if sn in image_defs:
        pass
    elif sn in scene_names:
        continue
    elif sn in ("black",):
        continue
    elif sn.startswith("text"):
        continue
    elif sn.startswith("("):
        continue
    else:
        show_undef[sn] = linenos

if show_undef:
    print(f"\n[WARN] Show commands without matching image def: {len(show_undef)}")
    for sn, linenos in sorted(show_undef.items()):
        lines_str = ", ".join(str(x) for x in linenos[:10])
        if len(linenos) > 10:
            lines_str += ", ..."
        print(f"  show {sn}  (lines: {lines_str})")
else:
    print("\n[OK] All show commands have matching image definitions")

# 6. Check scene backgrounds vs files
print(f"\n=== Background image checks ===")
# Get all bg, cg, weather scene commands
all_scene_bg = {sn for sn in scene_names if sn.startswith(("bg_", "cg_", "weather_"))}
missing_bg = []
for sn in sorted(all_scene_bg):
    if sn.startswith("bg_"):
        subdir = "backgrounds"
    elif sn.startswith("cg_"):
        subdir = "cg"
    elif sn.startswith("weather_"):
        subdir = "backgrounds"
    else:
        continue
    fpath = os.path.join(GAME, "images", subdir, f"{sn}.png")
    if os.path.isfile(fpath):
        continue
    # Check for any extension
    dirpath = os.path.join(GAME, "images", subdir)
    found = False
    if os.path.isdir(dirpath):
        for f in os.listdir(dirpath):
            base = f.rsplit(".", 1)[0] if "." in f else f
            if base == sn:
                found = True
                break
    if not found:
        missing_bg.append(sn)

if missing_bg:
    print(f"[MISS] Scene backgrounds/CGs without matching image file: {len(missing_bg)}")
    for sn in missing_bg:
        print(f"  scene {sn}")
else:
    print("[OK] All scene bg/cg commands have matching image files")

# 7. Files with garbled names
print(f"\n=== Special file checks ===")
garbled = []
tinybak = []
extra_in_characters = []
for root, dirs, files in os.walk(os.path.join(GAME, "images")):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), os.path.join(GAME, "images"))
        rel = rel.replace("\\", "/")
        if ".tiny_bak" in f:
            tinybak.append(rel)
        try:
            f.encode('ascii')
        except:
            garbled.append(rel)

if tinybak:
    print(f"[WARN] Backup files (.tiny_bak):")
    for f in tinybak:
        print(f"  {f}  (can be safely deleted)")
else:
    print("[OK] No .tiny_bak files")

if garbled:
    print(f"\n[CRITICAL] Files with garbled/non-ASCII names ({len(garbled)}):")
    for f in sorted(garbled):
        full = os.path.join(GAME, "images", f)
        size = os.path.getsize(full)
        print(f"  {repr(f)}  ({size} bytes)")
    print("\n  These likely have corrupted Chinese character names. Check if they")
    print("  correspond to expected files (like NPC images).")
else:
    print("\n[OK] No garbled filenames")

# 8. Check characters_alpha/ files against image defs
print(f"\n=== characters_alpha directory check ===")
cap_dir = os.path.join(GAME, "images", "characters_alpha")
cap_files = set()
if os.path.isdir(cap_dir):
    for f in os.listdir(cap_dir):
        if f.endswith((".png", ".jpg", ".jpeg", ".webp")):
            cap_files.add(f)

# Check which cap files are referenced by image definitions
unused_cap = []
for cf in sorted(cap_files):
    refd = False
    for name, path in image_defs.items():
        if path.endswith(cf):
            refd = True
            break
    if not refd:
        unused_cap.append(cf)

if unused_cap:
    print(f"[WARN] Files in characters_alpha/ not referenced by any image definition: {len(unused_cap)}")
    for f in unused_cap:
        print(f"  {f}")
else:
    print("[OK] All characters_alpha/ files are referenced")

# 9. Check characters/ dir files for extra
char_dir = os.path.join(GAME, "images", "characters")
char_files = set()
if os.path.isdir(char_dir):
    for f in os.listdir(char_dir):
        if f.endswith((".png", ".jpg", ".jpeg", ".webp")):
            char_files.add(f)

unused_char = []
for cf in sorted(char_files):
    refd = False
    # Check against all image def paths (they should point to characters_alpha/ now)
    # but check if it's referenced by name
    basename = cf.rsplit(".", 1)[0]
    for name, path in image_defs.items():
        if path.endswith(cf) or path.endswith(basename):
            refd = True
            break
    if not refd:
        unused_char.append(cf)

if unused_char:
    print(f"\n[WARN] Files in characters/ (old dir) not referenced: {len(unused_char)}")
    for f in unused_char:
        print(f"  {f}")
else:
    print("\n[OK] All characters/ files are referenced")

# 10. Compare unused files from characters/ vs characters_alpha/ for same name
print(f"\n=== Summary ===")
print(f"Total image definitions: {len(image_defs)}")
print(f"Missing def files: {len(missing_img_defs)}")
print(f"Scene cmds with no image: {len(missing_bg)}")
print(f"Garbled filenames: {len(garbled)}")
print(f"Characters_alpha unused: {len(unused_cap)}")
print(f"Characters (old) unused: {len(unused_char)}")

print("\n=== CHECK COMPLETE ===")