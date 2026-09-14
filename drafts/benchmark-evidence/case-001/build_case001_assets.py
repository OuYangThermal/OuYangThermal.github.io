from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT.parents[1] / "private-evidence" / "case-001" / "source-originals"
OUT = ROOT / "assets" / "images" / "benchmark-evidence" / "case-001"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1440, 900
INK = "#10202b"
MUTED = "#52636f"
BRAND = "#087f8c"
BRAND2 = "#07545c"
ACCENT = "#f0a202"
LINE = "#d9e1e6"
WASH = "#f4f7f8"
WHITE = "#ffffff"


def font(size, bold=False):
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


F_TITLE = font(48, True)
F_SUB = font(25)
F_H = font(30, True)
F_BODY = font(24)
F_SMALL = font(19)
F_BIG = font(58, True)


def canvas(title, subtitle):
    image = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, W, 12), fill=BRAND)
    draw.text((72, 56), title, font=F_TITLE, fill=INK)
    draw.text((72, 126), subtitle, font=F_SUB, fill=MUTED)
    draw.line((72, 174, W - 72, 174), fill=LINE, width=2)
    return image, draw


def footer(draw):
    draw.line((72, H - 78, W - 72, H - 78), fill=LINE, width=2)
    draw.text((72, H - 58), "OUYANG THERMAL | Internal test data; results depend on sample and test conditions.", font=F_SMALL, fill=MUTED)


def save(image, name):
    image.save(OUT / name, "WEBP", quality=84, method=6)


def chart():
    image, draw = canvas("Thermal Resistance vs Thickness", "FT-BN035 thickness series with one 0.25 mm SP2000 reference point | ASTM D5470 | stated 50 psi")
    left, top, right, bottom = 160, 240, 1310, 720
    draw.line((left, bottom, right, bottom), fill=INK, width=3)
    draw.line((left, top, left, bottom), fill=INK, width=3)
    xmin, xmax, ymin, ymax = 0.18, 0.50, 0.16, 0.33
    def xy(x, y):
        return (left + (x - xmin) / (xmax - xmin) * (right - left), bottom - (y - ymin) / (ymax - ymin) * (bottom - top))
    for y in [0.16, 0.20, 0.24, 0.28, 0.32]:
        py = xy(xmin, y)[1]
        draw.line((left, py, right, py), fill=LINE, width=1)
        draw.text((78, py - 13), f"{y:.2f}", font=F_SMALL, fill=MUTED)
    for x in [0.20, 0.25, 0.31, 0.38, 0.47]:
        px = xy(x, ymin)[0]
        draw.text((px - 24, bottom + 18), f"{x:.2f}", font=F_SMALL, fill=MUTED)
    draw.text((555, bottom + 58), "Nominal thickness (mm)", font=F_BODY, fill=INK)
    draw.text((24, 435), "Thermal resistance", font=F_SMALL, fill=INK)
    draw.text((42, 463), "(°C·in²/W)", font=F_SMALL, fill=INK)
    series = [(0.20, 0.185), (0.25, 0.211), (0.31, 0.245), (0.38, 0.265), (0.47, 0.311)]
    points = [xy(x, y) for x, y in series]
    draw.line(points, fill=BRAND, width=5)
    for (x, y), (px, py) in zip(series, points):
        draw.ellipse((px - 8, py - 8, px + 8, py + 8), fill=BRAND)
        draw.text((px - 24, py - 37), f"{y:.3f}", font=F_SMALL, fill=BRAND2)
    sx, sy = xy(0.25, 0.267)
    draw.rectangle((sx - 10, sy - 10, sx + 10, sy + 10), fill=ACCENT)
    draw.text((sx + 20, sy - 17), "SP2000 reference: 0.267", font=F_SMALL, fill=INK)
    footer(draw)
    save(image, "case-001-thermal-resistance-vs-thickness.webp")


def comparison():
    image, draw = canvas("0.25 mm Same-Thickness Comparison", "Measured thermal resistance under the stated internal ASTM D5470 conditions | stated 50 psi")
    cards = [(90, 250, 675, 670, "FT-BN035", "0.211", BRAND), (765, 250, 1350, 670, "SP2000 reference sample", "0.267", ACCENT)]
    for x1, y1, x2, y2, label, value, color in cards:
        draw.rounded_rectangle((x1, y1, x2, y2), radius=20, fill=WASH, outline=LINE, width=2)
        draw.rectangle((x1, y1, x2, y1 + 12), fill=color)
        draw.text((x1 + 40, y1 + 55), label, font=F_H, fill=INK)
        draw.text((x1 + 40, y1 + 155), value, font=F_BIG, fill=color)
        draw.text((x1 + 40, y1 + 230), "°C·in²/W", font=F_BODY, fill=MUTED)
        draw.text((x1 + 40, y1 + 300), "Nominal thickness: 0.25 mm", font=F_BODY, fill=INK)
    draw.text((425, 710), "Approximately 21% lower measured thermal resistance", font=F_H, fill=BRAND2)
    draw.text((394, 755), "This is a sample-and-condition-specific comparison, not a universal replacement claim.", font=F_SMALL, fill=MUTED)
    footer(draw)
    save(image, "case-001-0-25mm-thermal-resistance-comparison.webp")


def electrical():
    image, draw = canvas("Electrical Property Summary", "FT-BN035 internal test evidence and the tested 0.25 mm SP2000 reference sample")
    rows = [
        ("Breakdown voltage | ASTM D149", "FT-BN035 0.20 mm", "4.93 kV"),
        ("Breakdown voltage | ASTM D149", "FT-BN035 0.25 / 0.31 / 0.38 / 0.47 mm", ">6 kV"),
        ("Breakdown voltage | ASTM D149", "SP2000 reference 0.25 mm", "5.37 kV"),
        ("Surface resistance | ASTM D257 | 500 V", "FT-BN035", "approx. 1.62 × 10¹⁴ Ω"),
        ("Density | ASTM D792", "FT-BN035 | 1.833 / 1.875 / 1.900", "avg. approx. 1.87 g/cm³"),
    ]
    y = 225
    draw.rounded_rectangle((70, 205, W - 70, 735), radius=16, fill=WASH, outline=LINE, width=2)
    draw.text((95, y), "Property / method", font=F_H, fill=INK)
    draw.text((540, y), "Sample", font=F_H, fill=INK)
    draw.text((1080, y), "Displayed result", font=F_H, fill=INK)
    y += 58
    for prop, sample, result in rows:
        draw.line((90, y, W - 90, y), fill=LINE, width=2)
        draw.text((95, y + 18), prop, font=F_SMALL, fill=INK)
        draw.text((540, y + 18), sample, font=F_SMALL, fill=MUTED)
        draw.text((1080, y + 18), result, font=F_SMALL, fill=BRAND2)
        y += 86
    draw.text((88, 760), "Electrical suitability requires application-level creepage, clearance, aging and system validation.", font=F_SMALL, fill=MUTED)
    footer(draw)
    save(image, "case-001-electrical-properties-summary.webp")


def methods():
    image, draw = canvas("Case 001 Test-Method Evidence Map", "Use each result only with its stated method, specimen and condition context")
    items = [
        ("ASTM D5470", "Thermal resistance", "Thickness series; stated pressure 50 psi"),
        ("ASTM D149", "Breakdown voltage", "Five FT-BN035 thicknesses; one 0.25 mm reference"),
        ("ASTM D257", "Surface resistance", "Displayed measuring voltage 500 V"),
        ("ASTM D792", "Density", "Three displayed FT-BN035 measurements"),
    ]
    y = 220
    for method, prop, context in items:
        draw.rounded_rectangle((90, y, 1350, y + 118), radius=16, fill=WASH, outline=LINE, width=2)
        draw.text((125, y + 24), method, font=F_H, fill=BRAND2)
        draw.text((410, y + 24), prop, font=F_H, fill=INK)
        draw.text((410, y + 70), context, font=F_SMALL, fill=MUTED)
        y += 140
    draw.text((90, 790), "Raw run around 0.22 mm is retained separately and is not merged into the formal thickness series.", font=F_SMALL, fill=MUTED)
    footer(draw)
    save(image, "case-001-test-method-evidence-map.webp")


def raw_derivative():
    source = Image.open(SOURCE / "02_D5470_raw_screen_2.jpeg").convert("RGB")
    crop = source.crop((145, 20, 1430, 770))
    background = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(background)
    draw.rectangle((0, 0, W, 12), fill=BRAND)
    draw.text((60, 35), "Anonymized Raw ASTM D5470 Run Evidence", font=F_H, fill=INK)
    draw.text((60, 82), "Shown separately from the formal thickness-series report; not used in the 0.25 mm comparison.", font=F_SMALL, fill=MUTED)
    crop.thumbnail((1320, 680), Image.Resampling.LANCZOS)
    x = (W - crop.width) // 2
    background.paste(crop, (x, 135))
    draw.rectangle((x, 135, x + crop.width, 170), fill="#20262b")
    draw.text((x + 18, 142), "Software / device-identifying header redacted", font=F_SMALL, fill=WHITE)
    footer(draw)
    save(background, "case-001-anonymized-raw-d5470-run.webp")


if __name__ == "__main__":
    chart()
    comparison()
    electrical()
    methods()
    raw_derivative()
    for path in sorted(OUT.glob("*.webp")):
        with Image.open(path) as image:
            print(f"{path.name}\t{image.width}x{image.height}\t{path.stat().st_size} bytes")
