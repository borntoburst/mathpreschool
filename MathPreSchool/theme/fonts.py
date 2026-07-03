import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
FONT_NAME = "MathFont"
_registered = False
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
        pdfmetrics.registerFont(TTFont(FONT_NAME, font_path))
        _registered = True
        print("Font loaded:", font_path)
    else:
        print("Font NOT found:", font_path)
def get_font():
    if _registered:
        return FONT_NAME
    return "Helvetica"
