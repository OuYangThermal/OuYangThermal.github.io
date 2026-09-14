from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "assets" / "images" / "benchmark-evidence" / "case-002"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1440, 900
INK, MUTED = "#10202b", "#52636f"
BRAND, BRAND2, ACCENT = "#087f8c", "#07545c", "#f0a202"
LINE, WASH, WHITE = "#d9e1e6", "#f4f7f8", "#ffffff"


def font(size, bold=False):
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


F_TITLE, F_SUB = font(48, True), font(25)
F_H, F_BODY, F_SMALL = font(30, True), font(24), font(19)
F_BIG = font(54, True)


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


def thermal_chart():
    image, draw = canvas("Thin Insulating TIM: Thermal Resistance vs Thickness", "FT-BN050 | ASTM D5470 | 50 psi | internal comparative test data")
    left, top, right, bottom = 160, 240, 1310, 720
    draw.line((left, bottom, right, bottom), fill=INK, width=3)
    draw.line((left, top, left, bottom), fill=INK, width=3)
    xmin, xmax, ymin, ymax = 0.18, 0.55, 0.16, 0.31

    def xy(x, y):
        return (left + (x - xmin) / (xmax - xmin) * (right - left), bottom - (y - ymin) / (ymax - ymin) * (bottom - top))

    for y in [0.16, 0.20, 0.24, 0.28, 0.30]:
        py = xy(xmin, y)[1]
        draw.line((left, py, right, py), fill=LINE, width=1)
        draw.text((78, py - 13), f"{y:.2f}", font=F_SMALL, fill=MUTED)
    series = [(0.21, 0.179), (0.27, 0.195), (0.32, 0.209), (0.40, 0.249), (0.52, 0.292)]
    points = [xy(x, y) for x, y in series]
    draw.line(points, fill=BRAND, width=5)
    for (x, y), (px, py) in zip(series, points):
        draw.ellipse((px - 8, py - 8, px + 8, py + 8), fill=BRAND)
        draw.text((px - 26, py - 39), f"{y:.3f}", font=F_SMALL, fill=BRAND2)
        draw.text((px - 22, bottom + 18), f"{x:.2f}", font=F_SMALL, fill=MUTED)
    draw.text((550, bottom + 58), "Nominal thickness (mm)", font=F_BODY, fill=INK)
    draw.text((160, 202), "Thermal resistance (°C·in²/W)", font=F_SMALL, fill=INK)
    footer(draw)
    save(image, "case-002-ft-bn050-thermal-resistance-vs-thickness.webp")


def selection_guide():
    image, draw = canvas("Thickness Is Part of the Thermal Decision", "Measured FT-BN050 results under the stated ASTM D5470 conditions")
    rows = [
        ("0.21 mm", "0.210 mm", "0.179"),
        ("0.27 mm", "0.270 mm", "0.195"),
        ("0.32 mm", "0.311 mm", "0.209"),
        ("0.40 mm", "0.402 mm", "0.249"),
        ("0.52 mm", "0.504 mm", "0.292"),
    ]
    draw.rounded_rectangle((70, 210, 1370, 690), radius=18, fill=WASH, outline=LINE, width=2)
    draw.text((110, 235), "Nominal thickness", font=F_H, fill=INK)
    draw.text((535, 235), "Compressed thickness", font=F_H, fill=INK)
    draw.text((1015, 235), "Thermal resistance", font=F_H, fill=INK)
    y = 300
    for nominal, compressed, resistance in rows:
        draw.line((95, y, 1345, y), fill=LINE, width=2)
        draw.text((110, y + 18), nominal, font=F_BODY, fill=INK)
        draw.text((590, y + 18), compressed, font=F_BODY, fill=MUTED)
        draw.text((1080, y + 12), resistance, font=F_H, fill=BRAND2)
        y += 72
    draw.text((115, 720), "Selection takeaway", font=F_H, fill=ACCENT)
    draw.text((420, 724), "Compare thermal resistance at the required thickness and assembly pressure.", font=F_BODY, fill=INK)
    draw.text((420, 765), "Do not infer thermal conductivity or device temperature from this series.", font=F_SMALL, fill=MUTED)
    footer(draw)
    save(image, "case-002-ft-bn050-thickness-selection-guide.webp")


def electrical_summary():
    image, draw = canvas("Electrical Insulation Evidence", "FT-BN050 | ASTM D149 | 200 × 200 mm test area | internal test data")
    entries = [("0.21 mm", ">5 kV"), ("0.27 mm", ">6 kV"), ("0.32 mm", ">6 kV"), ("0.40 mm", ">6 kV"), ("0.52 mm", ">6 kV")]
    x = 80
    for thickness, value in entries:
        draw.rounded_rectangle((x, 245, x + 240, 610), radius=18, fill=WASH, outline=LINE, width=2)
        draw.rectangle((x, 245, x + 240, 257), fill=BRAND)
        draw.text((x + 35, 305), thickness, font=F_H, fill=INK)
        draw.text((x + 42, 405), value, font=F_BIG, fill=BRAND2)
        draw.text((x + 35, 520), "Displayed limit", font=F_SMALL, fill=MUTED)
        x += 265
    draw.text((90, 675), "Interpretation boundary", font=F_H, fill=ACCENT)
    draw.text((90, 725), "Breakdown voltage is not a complete assembly insulation rating.", font=F_BODY, fill=INK)
    draw.text((90, 768), "Validate conditioning, electrodes, defects, creepage, clearance and aging for the application.", font=F_SMALL, fill=MUTED)
    footer(draw)
    save(image, "case-002-ft-bn050-electrical-insulation-summary.webp")


if __name__ == "__main__":
    thermal_chart()
    selection_guide()
    electrical_summary()
    for path in sorted(OUT.glob("*.webp")):
        with Image.open(path) as image:
            print(f"{path.name}\t{image.width}x{image.height}\t{path.stat().st_size} bytes")
