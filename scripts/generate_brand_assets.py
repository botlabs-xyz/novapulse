"""Generate optimized documentation assets from the official NovaPulse image."""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "NovaPulse.png"
OUTPUT = ROOT / "assets" / "images"


def windows_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    fonts_dir = Path(os.environ.get("WINDIR", "")) / "Fonts"
    return ImageFont.truetype(fonts_dir / name, size)


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    image = Image.open(SOURCE).convert("RGB")

    for size, filename in (
        (32, "favicon-32.png"),
        (64, "novapulse-logo-64.png"),
        (180, "apple-touch-icon.png"),
        (256, "novapulse-logo-256.png"),
        (512, "novapulse-logo.png"),
    ):
        derivative = image.copy()
        derivative.thumbnail((size, size), Image.Resampling.LANCZOS)
        derivative.save(OUTPUT / filename, optimize=True)

    webp = image.copy()
    webp.thumbnail((512, 512), Image.Resampling.LANCZOS)
    webp.save(OUTPUT / "novapulse-logo.webp", quality=88, method=6)

    card = Image.new("RGB", (1200, 630), "#06070c")
    for center_x, center_y, color, radius in (
        (185, 40, (153, 51, 255), 430),
        (1120, 620, (0, 209, 255), 480),
    ):
        glow = Image.new("RGBA", card.size, (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow)
        glow_draw.ellipse(
            (
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
            ),
            fill=color + (105,),
        )
        glow = glow.filter(ImageFilter.GaussianBlur(120))
        card = Image.alpha_composite(card.convert("RGBA"), glow)

    logo = image.copy()
    logo.thumbnail((410, 410), Image.Resampling.LANCZOS)
    card.alpha_composite(logo.convert("RGBA"), (710, 110))

    draw = ImageDraw.Draw(card)
    draw.text((78, 88), "AFTERPARTY BOT LABS", font=windows_font("segoeuib.ttf", 20), fill="#c7a7ff")
    draw.text((72, 145), "NovaPulse", font=windows_font("segoeuib.ttf", 78), fill="white")
    draw.text((78, 250), "Official Documentation", font=windows_font("segoeui.ttf", 32), fill="#d5d9e8")
    draw.rounded_rectangle((78, 335, 600, 465), 24, fill="#10131f", outline="#9933ff", width=3)
    draw.text((108, 365), "Moderation  •  Verification", font=windows_font("segoeui.ttf", 32), fill="#ffffff")
    draw.text((108, 410), "Automation  •  Server Security", font=windows_font("segoeui.ttf", 32), fill="#ffffff")
    draw.text((78, 535), "botlabs-xyz.github.io/novapulse", font=windows_font("segoeuib.ttf", 20), fill="#aeb4c8")
    card.convert("RGB").save(OUTPUT / "novapulse-social-preview.png", optimize=True)


if __name__ == "__main__":
    main()
