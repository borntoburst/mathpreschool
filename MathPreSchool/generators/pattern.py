import random
from models.question import Question

class PatternGenerator:

    def generate(self, config):

        mode = random.choice([
            "increase",
            "alternate",
            "shape"
        ])

        if mode == "increase":

            start = random.randint(1,20)

            step = random.randint(1,5)

            seq = [
                start,
                start+step,
                start+step*2,
                start+step*3
            ]

            answer = start+step*4

            return Question(
                f"{seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ____",
                str(answer),
                "pattern"
            )

        elif mode == "alternate":

            a = random.randint(1,9)
            b = random.randint(1,9)

            return Question(
                f"{a}, {b}, {a}, {b}, ____",
                str(a),
                "pattern"
            )

        else:

            return Question(
                "🔺 🔵 🔺 🔵 ____",
                "🔺",
                "pattern"
            )