"""Build the Tangram horizontal logo (icon + 'Tangram' text).

Run::

    pip install pillow
    python build_tangram_logo.py

Tune the constants below to adjust sizing, color, weight, and the relative
position of the icon vs. the text.
"""
from PIL import Image, ImageDraw, ImageFont

# ---- paths -----------------------------------------------------------------
LOGO_PATH = "/workspace/TANGRAM/static/images/tangram_icon_v3_removed.png"
OUT_PATH = "/workspace/vllm/docs/assets/logos/tangram-logo-text.png"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Regular

# ---- tunables --------------------------------------------------------------
TEXT = "Tangram"
TARGET_LOGO_H = 200            # icon height in px
FONT_SIZE = 180
STROKE_W = 0                   # thickens Regular slightly; 0 for pure Regular
COLOR = (58, 58, 58, 255)      # vLLM charcoal
GAP = 60                       # horizontal space between icon and text
MARGIN = 30                    # outer padding
EXTRA_TEXT_DROP = 110          # how far the text sits below the canvas top
EXTRA_LOGO_DROP = 45           # how far the icon sits below the canvas top


def build_logo() -> None:
    logo = Image.open(LOGO_PATH).convert("RGBA")
    logo = logo.crop(logo.getbbox())  # strip transparent padding
    ratio = TARGET_LOGO_H / logo.height
    logo = logo.resize(
        (int(logo.width * ratio), TARGET_LOGO_H), Image.LANCZOS
    )

    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    measure = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    tbbox = measure.textbbox((0, 0), TEXT, font=font, stroke_width=STROKE_W)
    text_w = tbbox[2] - tbbox[0]
    text_h = tbbox[3] - tbbox[1]
    text_top = tbbox[1]

    content_h = max(logo.height + EXTRA_LOGO_DROP, text_h + EXTRA_TEXT_DROP)
    canvas_w = logo.width + GAP + text_w + MARGIN * 2
    canvas_h = content_h + MARGIN * 2

    canvas = Image.new("RGBA", (canvas_w, canvas_h), (255, 255, 255, 0))
    canvas.paste(logo, (MARGIN, MARGIN + EXTRA_LOGO_DROP), logo)

    draw = ImageDraw.Draw(canvas)
    text_x = MARGIN + logo.width + GAP - tbbox[0]
    text_y = MARGIN + EXTRA_TEXT_DROP - text_top
    draw.text(
        (text_x, text_y), TEXT, font=font, fill=COLOR,
        stroke_width=STROKE_W, stroke_fill=COLOR,
    )

    canvas.save(OUT_PATH, "PNG")
    print(f"Saved: {OUT_PATH} ({canvas_w}x{canvas_h})")


if __name__ == "__main__":
    build_logo()
