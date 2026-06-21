import os
import json
import re

manifest_path = 'images/manifest.json'
images_dir = 'images'

# Known name mappings
name_map = {
    'roy': ('רועי', 'ROY'),
    'aba': ('אבא', 'ABA'),
    'savta': ('סבתא', 'SAVTA'),
    'saba': ('סבא', 'SABA'),
    'arya': ('אריאה', 'ARYA'),
    'yahli': ('יהלי', 'YAHLI'),
    'alin': ('אלין', 'ALIN'),
    'yahel': ('יהל', 'YAHEL'),
    'ohad': ('אוהד', 'OHAD'),
    'emily': ('אמילי', 'EMILY'),
    'yona': ('יונה', 'YONA'),
    'yair': ('יאיר', 'YAIR'),
    'adi': ('עדי', 'ADI')
}

# Excluded files/folders
excluded_dirs = {'chrono', 'emotions', 'firstletter', 'habitat', 'mg', 'sharing', 'sharing_organized', 'מר גמיש'}
excluded_files = {'FUNNY GEKO.webp', 'fly-geko.webp', 'fly-target.jpg', 'child_photo.jpg'}

# Load existing manifest if exists
existing = []
if os.path.exists(manifest_path):
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    except Exception as e:
        print(f"Error reading existing manifest: {e}")

existing_by_file = {item['file']: item for item in existing}

# Scan images folder
found_files = []
for entry in os.scandir(images_dir):
    if entry.is_file():
        name = entry.name
        if name in excluded_files:
            continue
        ext = os.path.splitext(name)[1].lower()
        if ext in {'.jpg', '.jpeg', '.png', '.webp'}:
            found_files.append(name)

new_manifest = []
for filename in found_files:
    if filename in existing_by_file:
        new_manifest.append(existing_by_file[filename])
    else:
        # Generate names based on filename
        base = os.path.splitext(filename)[0]
        # Split by non-alphanumeric
        tokens = re.split(r'[-_&]+', base.lower())
        
        he_parts = []
        en_parts = []
        
        for tok in tokens:
            tok = tok.strip()
            if not tok:
                continue
            if tok in name_map:
                he_parts.append(name_map[tok][0])
                en_parts.append(name_map[tok][1])
            else:
                he_parts.append(tok.capitalize())
                en_parts.append(tok.upper())
        
        # Build English name
        if len(en_parts) == 1:
            name_en = en_parts[0]
        elif len(en_parts) == 2:
            name_en = f"{en_parts[0]} & {en_parts[1]}"
        else:
            name_en = ", ".join(en_parts[:-1]) + f" & {en_parts[-1]}"
            
        # Build Hebrew name
        name_he = ""
        for i, hp in enumerate(he_parts):
            if i == 0:
                name_he = hp
            else:
                if hp == 'אבא' or (i < len(he_parts) - 1 and hp == 'אבא'):
                    name_he += " ואבא"
                else:
                    name_he += " ו" + hp
        
        name_he = name_he.replace("ואבא ואבא", "ואבא")
        
        new_item = {
            "nameHe": name_he,
            "nameEn": name_en,
            "file": filename
        }
        print(f"Generated new entry: {new_item}")
        new_manifest.append(new_item)

# Save manifest
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(new_manifest, f, ensure_ascii=False, indent=2)

print(f"Manifest updated with {len(new_manifest)} entries.")
