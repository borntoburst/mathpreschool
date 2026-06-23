from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class AnswerExporter:

    def export(
        self,
        filename,
        answers
    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "MathPreSchool Answer Key",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1,20)
        )

        for index, item in enumerate(
            answers,
            start=1
        ):

            content.append(
                Paragraph(
                    f"{index}. {item['question']} = {item['answer']}",
                    styles["Normal"]
                )
            )

        doc.build(content)