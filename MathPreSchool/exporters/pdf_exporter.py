from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from reportlab.lib import colors

from theme.fonts import register_fonts
from theme.styles import (
    TITLE_STYLE,
    SECTION_STYLE,
    QUESTION_STYLE,
    HEADER_STYLE,
)


class PDFExporter:

    def export(self, filename, worksheet_data):

        register_fonts()

        doc = SimpleDocTemplate(
            filename,
            leftMargin=25,
            rightMargin=25,
            topMargin=20,
            bottomMargin=20,
        )

        content = []

        # ==========================
        # Header
        # ==========================

        content.append(
            Paragraph(
                "MATHPRESCHOOL",
                TITLE_STYLE
            )
        )

        content.append(Spacer(1, 12))

        content.append(
            Paragraph(
                "Name: ______________________________",
                HEADER_STYLE
            )
        )

        content.append(Spacer(1, 20))

        # ==========================
        # Sections
        # ==========================

        for section in worksheet_data:

            header = Table(
                [[Paragraph(section["title"], SECTION_STYLE)]],
                colWidths=[540]
            )

            header.setStyle(
                TableStyle([
                    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E3F2FD")),
                    ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#1565C0")),
                    ("LINEBELOW", (0, 0), (-1, -1), 1, colors.HexColor("#1565C0")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ])
            )

            content.append(header)

            content.append(Spacer(1, 8))

            questions = section["questions"]

            half = (len(questions) + 1) // 2

            left = questions[:half]

            right = questions[half:]

            while len(right) < len(left):
                right.append(None)

            rows = []

            for i in range(len(left)):

                left_text = left[i].text

                if right[i]:
                    right_text = right[i].text
                else:
                    right_text = ""

                rows.append([
                    Paragraph(left_text, QUESTION_STYLE),
                    Paragraph(right_text, QUESTION_STYLE)
                ])

            table = Table(
                rows,
                colWidths=[260, 260]
            )

            table.setStyle(
                TableStyle([
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ])
            )

            content.append(table)

            content.append(Spacer(1, 15))

        doc.build(content)
