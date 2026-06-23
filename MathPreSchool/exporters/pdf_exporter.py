from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


class PDFExporter:

    def export(
        self,
        filename,
        worksheet_data
    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        content = []

        title = Paragraph(
            "MathPreSchool Worksheet",
            styles["Title"]
        )

        content.append(title)

        content.append(
            Spacer(1,12)
        )

        content.append(
            Paragraph(
                "Student Name: __________________",
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1,20)
        )

        for section in worksheet_data:

            content.append(
                Paragraph(
                    section["title"],
                    styles["Heading2"]
                )
            )

            content.append(
                Spacer(1,8)
            )

            for index, question in enumerate(
                section["questions"],
                start=1
            ):

                content.append(
                    Paragraph(
                        f"{index}. {question.text}",
                        styles["Normal"]
                    )
                )

            content.append(
                Spacer(1,15)
            )

        doc.build(content)