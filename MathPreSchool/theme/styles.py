from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from theme.fonts import get_font

FONT = get_font()

TITLE_STYLE = ParagraphStyle(
    "TITLE",
    fontName=FONT,
    fontSize=24,
    leading=30,
    alignment=TA_CENTER,
)

HEADER_STYLE = ParagraphStyle(
    "HEADER",
    fontName=FONT,
    fontSize=13,
    leading=18,
)

SECTION_STYLE = ParagraphStyle(
    "SECTION",
    fontName=FONT,
    fontSize=15,
    leading=20,
)

QUESTION_STYLE = ParagraphStyle(
    "QUESTION",
    fontName=FONT,
    fontSize=16,
    leading=24,
)
