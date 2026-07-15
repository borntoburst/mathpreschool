from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from theme.styles import SECTION_STYLE

from theme.spacing import SECTION_SPACE


class SectionRenderer:

    def render(self, title):

        return [

            Paragraph(

                title,

                SECTION_STYLE

            ),

            Spacer(1, SECTION_SPACE)

        ]
