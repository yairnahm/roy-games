"""
Compress emotion PNGs to JPGs and create pre-masked face versions.
"""
from PIL import Image, ImageDraw, ImageFilter
import os, struct

BASE    = r"C:\Users\Yairn\Desktop\roy-games\images\emotions"
QUALITY = 72   # JPEG quality — ~150-200KB per image

# Approximate face-part regions as fraction of image size.
# Calibrated for Disney/Pixar-style square cartoon face images.
# Eyes:  ~y 38%-62%, full width
# Mouth: ~y 63%-80%, slightly inset
EYE_REGION   = (0.04, 0.36, 0.96, 0.62)   # left, top, right, bottom
MOUTH_REGION = (0.10, 0.62, 0.90, 0.82)

EMOTIONS = ['happy', 'sad', 'angry', 'surprised', 'scared']
GENDERS  = ['boy', 'girl']
PARTS    = ['face', 'eyes', 'mouth']

def compress(src, dst, quality=QUALITY):
    img = Image.open(src).convert('RGB')
    img.save(dst, 'JPEG', quality=quality, optimize=True)
    before = os.path.getsize(src)
    after  = os.path.getsize(dst)
    print(f"  {os.path.basename(src)} {before//1024}KB -> {after//1024}KB")

def make_masked(src, dst, region, quality=QUALITY):
    img = Image.open(src).convert('RGB')
    w, h = img.size
    l = int(region[0] * w)
    t = int(region[1] * h)
    r = int(region[2] * w)
    b = int(region[3] * h)

    # Blur the region
    blurred = img.filter(ImageFilter.GaussianBlur(radius=18))
    img.paste(blurred.crop((l, t, r, b)), (l, t))

    # White semi-transparent overlay
    overlay = Image.new('RGBA', img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    draw.rounded_rectangle([l, t, r, b], radius=20,
                            fill=(255,255,255,255), outline=(180,180,180,255), width=4)
    img = img.convert('RGBA')
    img = Image.alpha_composite(img, overlay).convert('RGB')

    # Draw ? in center
    draw2 = ImageDraw.Draw(img)
    cx = (l + r) // 2
    cy = (t + b) // 2
    fsize = (b - t) // 2
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("C:\\Windows\\Fonts\\arialbd.ttf", fsize)
    except Exception:
        font = ImageFont.load_default()
    draw2.text((cx, cy), "?", fill=(210, 50, 50), font=font, anchor="mm")

    img.save(dst, 'JPEG', quality=quality, optimize=True)
    before = os.path.getsize(src)
    after  = os.path.getsize(dst)
    print(f"  {os.path.basename(dst)} (masked) {before//1024}KB -> {after//1024}KB")

for gender in GENDERS:
    src_dir = os.path.join(BASE, gender)
    print(f"\n=== {gender} ===")

    # Compress all parts
    for emo in EMOTIONS:
        for part in PARTS:
            src = os.path.join(src_dir, f"{part}-{emo}.png")
            dst = os.path.join(src_dir, f"{part}-{emo}.jpg")
            if os.path.exists(src):
                compress(src, dst)

    # Create masked face versions
    for emo in EMOTIONS:
        src = os.path.join(src_dir, f"face-{emo}.png")
        if os.path.exists(src):
            make_masked(src, os.path.join(src_dir, f"face-{emo}-noeyes.jpg"),  EYE_REGION)
            make_masked(src, os.path.join(src_dir, f"face-{emo}-nomouth.jpg"), MOUTH_REGION)

print("\nDone!")
