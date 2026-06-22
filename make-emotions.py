"""
Generates all 50 emotion images from 10 base faces:
  face-{emo}.jpg / .png
  eyes-{emo}.jpg / .png       (3:1 crop, eye region)
  mouth-{emo}.jpg / .png      (3:1 crop, mouth region)
  face-{emo}-noeyes.jpg       (face with eye patch + ?)
  face-{emo}-nomouth.jpg      (face with mouth patch + ?)
"""
from PIL import Image, ImageDraw, ImageFont
import os

EMOTIONS = ['happy', 'sad', 'angry', 'surprised', 'scared']
GENDERS  = ['boy', 'girl']

BASE    = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE, 'images', 'emotions-src')
OUT_DIR = os.path.join(BASE, 'images', 'emotions')

# Proportions (fraction of image size)
# Eyes: horizontal strip centered at ~42% from top
EYES_Y_CENTER = 0.42
EYES_X_FRAC   = 0.88   # width of crop relative to image width
# Mouth: centered at ~68% from top
MOUTH_Y_CENTER = 0.68
MOUTH_X_FRAC   = 0.72   # narrower than eyes

def load_font(size):
    for name in ['arial.ttf', 'Arial.ttf', 'DejaVuSans-Bold.ttf', 'NotoSans-Bold.ttf']:
        try:
            return ImageFont.truetype(name, size=size)
        except Exception:
            pass
    return ImageFont.load_default()

def strip_crop(img, x_frac, y_center_frac):
    """Return 3:1 horizontal strip crop."""
    w, h = img.size
    cw = int(w * x_frac)
    ch = cw // 3
    x1 = (w - cw) // 2
    x2 = x1 + cw
    yc = int(h * y_center_frac)
    y1 = yc - ch // 2
    y2 = y1 + ch
    # clamp
    y1 = max(0, y1); y2 = min(h, y2)
    return img.crop((x1, y1, x2, y2))

def patch_region(img, x1f, y1f, x2f, y2f, fill, outline):
    """Return copy of img with a soft rounded rectangle over the given region."""
    out = img.copy().convert('RGB')
    w, h = out.size
    x1, y1, x2, y2 = int(w*x1f), int(h*y1f), int(w*x2f), int(h*y2f)
    draw = ImageDraw.Draw(out)
    draw.rounded_rectangle([x1, y1, x2, y2], radius=22,
                           fill=fill, outline=outline, width=4)
    # question mark
    fsize = int((y2-y1) * 0.65)
    font  = load_font(fsize)
    cx, cy = (x1+x2)//2, (y1+y2)//2
    # shadow
    draw.text((cx+2, cy+2), '?', fill=(0,0,0,60), font=font, anchor='mm')
    draw.text((cx, cy),     '?', fill=outline,      font=font, anchor='mm')
    return out

def process(gender, emotion):
    src = os.path.join(SRC_DIR, f'{gender}-{emotion}.jpg')
    if not os.path.exists(src):
        print(f'  MISSING source: {src}')
        return False

    img   = Image.open(src).convert('RGB')
    outd  = os.path.join(OUT_DIR, gender)
    os.makedirs(outd, exist_ok=True)

    def save(im, name):
        path = os.path.join(outd, name)
        ext  = os.path.splitext(name)[1].lower()
        fmt  = 'PNG' if ext == '.png' else 'JPEG'
        kw   = {} if fmt == 'PNG' else {'quality': 95}
        im.save(path, fmt, **kw)

    # 1. Full face
    save(img, f'face-{emotion}.jpg')
    save(img, f'face-{emotion}.png')

    # 2. Eyes strip
    eyes = strip_crop(img, EYES_X_FRAC, EYES_Y_CENTER)
    save(eyes, f'eyes-{emotion}.jpg')
    save(eyes, f'eyes-{emotion}.png')

    # 3. Mouth strip
    mouth = strip_crop(img, MOUTH_X_FRAC, MOUTH_Y_CENTER)
    save(mouth, f'mouth-{emotion}.jpg')
    save(mouth, f'mouth-{emotion}.png')

    # 4. Face – eyes covered (light blue patch)
    noeyes = patch_region(img,
                          x1f=0.06, y1f=0.28, x2f=0.94, y2f=0.56,
                          fill=(200, 225, 255),
                          outline=(100, 155, 230))
    save(noeyes, f'face-{emotion}-noeyes.jpg')

    # 5. Face – mouth covered (light peach patch)
    nomouth = patch_region(img,
                           x1f=0.16, y1f=0.57, x2f=0.84, y2f=0.81,
                           fill=(255, 220, 190),
                           outline=(230, 140, 80))
    save(nomouth, f'face-{emotion}-nomouth.jpg')

    return True

print('=== Generating emotion images ===')
ok = err = 0
for g in GENDERS:
    for e in EMOTIONS:
        if process(g, e):
            print(f'  OK  {g}/{e}')
            ok += 1
        else:
            err += 1

print(f'\nDone: {ok} sets OK, {err} missing')
if err:
    print('Run copy-emotions-src.bat first to copy source images from Downloads.')
