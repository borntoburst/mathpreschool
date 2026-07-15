from reportlab.platypus import SimpleDocTemplate

from theme.fonts import register_fonts

from renderers.header_renderer import HeaderRenderer

from renderers.section_renderer import SectionRenderer

from renderers.question_grid_renderer import QuestionGridRenderer

from theme.spacing import PAGE_MARGIN


class PDFExporter:

    def export(self, filename, worksheet):

        register_fonts()

        doc = SimpleDocTemplate(

            filename,

            leftMargin=PAGE_MARGIN,

            rightMargin=PAGE_MARGIN,

            topMargin=PAGE_MARGIN,

            bottomMargin=PAGE_MARGIN

        )

        story = []

        story.extend(

            HeaderRenderer().render()

        )

        for section in worksheet:

            story.extend(

                SectionRenderer().render(

                    section["title"]

                )

            )

            story.append(

                QuestionGridRenderer().render(

                    section["questions"]

                )

            )

        doc.build(story)
