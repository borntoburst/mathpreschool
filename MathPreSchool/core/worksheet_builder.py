from utils.uniqueness import UniqueQuestionGenerator


class WorksheetBuilder:

    def __init__(self, config):

        self.config = config
        self.unique = UniqueQuestionGenerator()

    def build(self, sections):

        worksheet = []

        for section in sections:

            section_questions = []

            for _ in range(section.count):

                while True:

                    q = section.generator.generate(self.config)

                    if self.unique.add(q.text):
                        break

                section_questions.append(q)

            worksheet.append({
                "title": section.title,
                "questions": section_questions,
                "priority": section.priority,
                "color": section.color,
                "icon": getattr(section, "icon", "")
            })

        return worksheet
