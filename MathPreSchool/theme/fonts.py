import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

_registered = False
FONT_NAME = "MathFont"


def register_fonts():
    global _registered

    if _registered:
        return

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    font_path = os.path.join(
        base_dir,
        "assets",
        "fonts",
        "NotoSans-Regular.ttf"
    )

    if os.path.exists(font_path):
        pdfmetrics.registerFont(
            TTFont(FONT_NAME, font_path)
        )
        _registered = True
    else:
        print(f"[WARNING] Font not found: {font_path}")


def get_font():
    if _registered:
        return FONT_NAME

    return "Helvetica"
