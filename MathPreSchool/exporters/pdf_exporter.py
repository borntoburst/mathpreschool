import os
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import TA_CENTER

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

FONT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "NotoSans-Regular.ttf"
)

st.write("FONT_PATH =", FONT_PATH)
st.write("EXISTS =", os.path.exists(FONT_PATH))

pdfmetrics.registerFont(
    TTFont("NotoSans", FONT_PATH)
)

class PDFExporter:

    def export(
        self,
        filename,
        worksheet_data
    ):
        pdfmetrics.registerFont(
            TTFont(
                "NotoSans",
                "assets/NotoSans-Regular.ttf"
            )
        )
        doc = SimpleDocTemplate(
            filename,
            leftMargin=25,
            rightMargin=25,
            topMargin=20,
            bottomMargin=20
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "Title",
            fontName="NotoSans",
            fontSize=22
        )

        section_style = ParagraphStyle(
            "Section",
            fontName="NotoSans"
        )

        question_style = ParagraphStyle(
            "Question",
            fontName="NotoSans"
        )

        content = []

        # Header

        content.append(
            Paragraph(
                "MATHPRESCHOOL",
                title_style
            )
        )

        content.append(
            Spacer(1, 10)
        )

        content.append(
            Paragraph(
                "Student Name: __________________________",
                question_style
            )
        )

        content.append(
            Spacer(1, 15)
        )

        # Sections

        for section in worksheet_data:

            content.append(
                Paragraph(
                    section["title"],
                    section_style
                )
            )

            content.append(
                Spacer(1, 5)
            )

            rows = []

            questions = section["questions"]

            half = (len(questions) + 1) // 2

            left = questions[:half]
            right = questions[half:]

            while len(right) < len(left):
                right.append(None)

            for i in range(len(left)):

                left_text = (
                    f"{i+1}. {left[i].text}"
                )

                if right[i]:
                    right_text = (
                        f"{half+i+1}. {right[i].text}"
                    )
                else:
                    right_text = ""

                rows.append(
                    [
                        Paragraph(
                            left_text,
                            question_style
                        ),
                        Paragraph(
                            right_text,
                            question_style
                        )
                    ]
                )

            table = Table(
                rows,
                colWidths=[260, 260]
            )

            table.setStyle(
                TableStyle([
                    ("VALIGN", (0,0), (-1,-1), "TOP"),
                    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
                ])
            )

            content.append(table)

            content.append(
                Spacer(1, 10)
            )

        doc.build(content)
