import os, glob
from PIL import Image, ImageDraw, ImageFont
RES = "android/app/src/main/res"
D = {"mdpi": (48, 108), "hdpi": (72, 162), "xhdpi": (96, 216), "xxhdpi": (144, 324), "xxxhdpi": (192, 432)}
def font(px):
    for p in ("DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        try: return ImageFont.truetype(p, px)
        except Exception: pass
    return ImageFont.load_default()
def draw(size, bg, round_=False):
    S = size * 4
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if bg:
        m = d.rounded_rectangle if not round_ else None
        if round_: d.ellipse((0, 0, S - 1, S - 1), fill=(10, 11, 18, 255))
        else: d.rounded_rectangle((0, 0, S - 1, S - 1), radius=S // 5, fill=(10, 11, 18, 255))
    c = S // 2
    r = int(S * (0.27 if not bg else 0.36))
    d.ellipse((c - r, c - r, c + r, c + r), outline=(80, 110, 255, 255), width=max(4, S // 40))
    f = font(int(r * 1.0))
    d.text((c, c), "MV", font=f, fill=(255, 255, 255, 255), anchor="mm")
    return im.resize((size, size), Image.LANCZOS)
for dn, (leg, fg) in D.items():
    folder = os.path.join(RES, "mipmap-" + dn)
    if not os.path.isdir(folder): continue
    draw(leg, True).save(os.path.join(folder, "ic_launcher.png"))
    draw(leg, True, True).save(os.path.join(folder, "ic_launcher_round.png"))
    draw(fg, False).save(os.path.join(folder, "ic_launcher_foreground.png"))
vals = os.path.join(RES, "values")
os.makedirs(vals, exist_ok=True)
open(os.path.join(vals, "ic_launcher_background.xml"), "w").write(
    '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#0A0B12</color>\n</resources>\n')
print("icons done")
