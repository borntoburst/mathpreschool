from utils.uniqueness import UniqueQuestionGenerator

class WorksheetBuilder:

    def __init__(self, generators):
        self.generators = generators

    def build(self, config):

        unique = UniqueQuestionGenerator()

        worksheet_data = []
        answers = []

        for title, generator, count in self.generators:

            questions = []

            for _ in range(count):

                while True:

                    q = generator.generate(config)

                    if unique.add(q.text):
                        break

                questions.append(q)

                answers.append({
                    "question": q.text,
                    "answer": q.answer
                })

            worksheet_data.append({
                "title": title,
                "questions": questions
            })

        return worksheet_data, answers
