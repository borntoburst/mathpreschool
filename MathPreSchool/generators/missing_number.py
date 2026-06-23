import random
from models.question import Question

class MissingNumberGenerator:

    def generate(self, config):

        small = random.randint(
            1,
            config.finger_limit
        )

        mode = random.choice([
            "plus",
            "minus"
        ])

        if mode == "plus":

            answer = random.randint(
                config.min_number,
                config.max_number - small
            )

            result = answer + small

            return Question(
                f"□ + {small} = {result}",
                str(answer),
                "missing"
            )

        else:

            answer = random.randint(
                small,
                config.max_number
            )

            result = answer - small

            return Question(
                f"□ - {small} = {result}",
                str(answer),
                "missing"
            )