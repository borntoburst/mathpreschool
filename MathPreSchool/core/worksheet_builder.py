from utils.uniqueness import UniqueQuestionGenerator


class WorksheetBuilder:

    def __init__(self, config):

        self.config = config
        self.unique = UniqueQuestionGenerator()

    def _generate_unique(self, generator):

        while True:

            question = generator.generate(self.config)

            if self.unique.add(question.text):

                return question

    def build(self, sections):

        worksheet = []

        answers = []

        for section in sections:

            questions = []

            for _ in range(int(section.count)):

                q = self._generate_unique(
                    section.generator
                )

                questions.append(q)

                answers.append({

                    "question": q.text,

                    "answer": q.answer

                })

            worksheet.append({

                "title": section.title,

                "questions": questions,

                "priority": section.priority,

                "color": section.color,

                "icon": section.icon

            })

        return worksheet, answers
