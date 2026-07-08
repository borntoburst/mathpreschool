from utils.uniqueness import UniqueQuestionGenerator


class WorksheetBuilder:

    def __init__(self, sections):

        self.sections = sections

        self.unique = UniqueQuestionGenerator()

    def build(self, config):

        worksheet = []

        answers = []

        for section in self.sections:

            questions = []

            for _ in range(section.count):

                while True:

                    q = section.generator.generate(config)

                    if self.unique.add(q.text):
                        break

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

        return worksheet, answers                "questions": questions
            })

        return worksheet_data, answers
