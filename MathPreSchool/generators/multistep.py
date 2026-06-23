import random
from models.question import Question

class MultiStepGenerator:

    def generate(self, config):

        start = random.randint(
            10,
            config.max_number
        )

        a = random.randint(
            1,
            config.finger_limit
        )

        b = random.randint(
            1,
            config.finger_limit
        )

        answer = start + a - b

        return Question(
            f"{start} + {a} - {b} = ____",
            str(answer),
            "multistep"
        )