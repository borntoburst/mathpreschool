import os
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import (
    ParagraphStyle
)
from theme.fonts import register_fonts
from theme.styles import (
    TITLE_STYLE,
    SECTION_STYLE,
    QUESTION_STYLE,
    HEADER_STYLE,
)
from reportlab.lib.enums import TA_CENTER

class PDFExporter:

    def export(
        self,
        filename,
        worksheet_data
    ):
        register_fonts()
        doc = SimpleDocTemplate(
            filename,
            leftMargin=25,
            rightMargin=25,
            topMargin=20,
            bottomMargin=20
        )

      

        title_style = ParagraphStyle(
            "Title",
            fontName="Helvetica",
            fontSize=22
        )

        section_style = ParagraphStyle(
            "Section",
            fontName="Helvetica"
        )

        question_style = ParagraphStyle(
            "Question",
            fontName="Helvetica",
            fontSize=14,
        )

        content = []
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
                "Name: _______________________",
                HEADER_STYLE
            )
        )

        content.append(
            Spacer(1, 15)
        )

        for section in worksheet_data:

            content.append(
                Paragraph(
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
