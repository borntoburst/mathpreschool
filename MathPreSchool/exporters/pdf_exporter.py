from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import TA_CENTER


class PDFExporter:

    def export(
        self,
        filename,
        worksheet_data
    ):

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
            parent=styles["Title"],
            alignment=TA_CENTER,
            fontSize=22,
            leading=26
        )

        section_style = ParagraphStyle(
            "Section",
            parent=styles["Heading2"],
            fontSize=15,
            leading=18
        )

        question_style = ParagraphStyle(
            "Question",
            parent=styles["Normal"],
            fontSize=14,
            leading=18
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
