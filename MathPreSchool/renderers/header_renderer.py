from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from theme.styles import TITLE_STYLE
from theme.styles import HEADER_STYLE

from theme.spacing import HEADER_SPACE


class HeaderRenderer:

    def render(self):

        content = []

        content.append(

            Paragraph(

                "MATHPRESCHOOL",

                TITLE_STYLE

            )

        )

        content.append(

            Spacer(1, HEADER_SPACE)

        )

        content.append(

            Paragraph(

                "Student: __________________________",

                HEADER_STYLE

            )

        )

        content.append(

            Spacer(1, HEADER_SPACE)

        )

        return content
