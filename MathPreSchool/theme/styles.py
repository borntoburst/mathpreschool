from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from .fonts import get_font


FONT = get_font()


TITLE_STYLE = ParagraphStyle(
    "TITLE",
    fontName=FONT,
    fontSize=22,
    leading=28,
    alignment=TA_CENTER,
)

SECTION_STYLE = ParagraphStyle(
    "SECTION",
    fontName=FONT,
    fontSize=16,
    leading=20,
)

QUESTION_STYLE = ParagraphStyle(
    "QUESTION",
    fontName=FONT,
    fontSize=14,
    leading=18,
)

HEADER_STYLE = ParagraphStyle(
    "HEADER",
    fontName=FONT,
    fontSize=13,
    leading=16,
)
