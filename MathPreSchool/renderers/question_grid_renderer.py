from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.platypus import Paragraph

from reportlab.lib import colors

from theme.styles import QUESTION_STYLE


class QuestionGridRenderer:

    def render(self, questions):

        columns = 3

        rows = []

        temp = []

        for question in questions:

            temp.append(

                Paragraph(

                    question.text.replace("□","______"),

                    QUESTION_STYLE

                )

            )

            if len(temp) == columns:

                rows.append(temp)

                temp = []

        if temp:

            while len(temp) < columns:

                temp.append("")

            rows.append(temp)

        table = Table(

            rows,

            colWidths=[170,170,170]

        )

        table.setStyle(

            TableStyle([

                ("BOTTOMPADDING",(0,0),(-1,-1),2),

                ("TOPPADDING",(0,0),(-1,-1),2),

                ("LEFTPADDING",(0,0),(-1,-1),4),

                ("RIGHTPADDING",(0,0),(-1,-1),4),

                ("VALIGN",(0,0),(-1,-1),"TOP"),

            ])

        )

        return table
