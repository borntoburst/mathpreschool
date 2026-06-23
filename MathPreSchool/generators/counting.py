import random
from models.question import Question

class CountingGenerator:

    def generate(self, config):

        op = random.choice(["+","-"])

        a = random.randint(
            config.min_number,
            config.max_number
        )

        b = random.randint(
            1,
            config.finger_limit
        )

        if op == "+":

            if a + b > config.max_number:
                a = config.max_number - b

            return Question(
                f"{a} + {b} = ____",
                str(a+b),
                "counting"
            )

        else:

            if a < b:
                a = b

            return Question(
                f"{a} - {b} = ____",
                str(a-b),
                "counting"
            )