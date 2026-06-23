import random
from models.question import Question

class ComparisonGenerator:

    def generate(self, config):

        mode = random.choice([
            "number",
            "calc",
            "reasoning"
        ])

        if mode == "number":

            a = random.randint(0,config.max_number)
            b = random.randint(0,config.max_number)

            ans = ">" if a>b else "<" if a<b else "="

            return Question(
                f"{a} ___ {b}",
                ans,
                "comparison"
            )

        elif mode == "calc":

            a = random.randint(0,config.max_number)
            b = random.randint(1,config.finger_limit)

            result = a+b

            target = result + random.randint(-3,3)

            ans = ">" if result>target else "<" if result<target else "="

            return Question(
                f"{a}+{b} ___ {target}",
                ans,
                "comparison"
            )

        else:
            
            max_base = max(
                config.min_number,
                config.max_number - config.finger_limit
            )
        
            base = random.randint(
                config.min_number,
                max_base
            )
        
            x = random.randint(
                1,
                min(
                    config.finger_limit,
                    config.max_number - base
                )
            )
        
            y = random.randint(
                1,
                min(
                    config.finger_limit,
                    config.max_number - base
                )
            )

            ans = ">" if x>y else "<" if x<y else "="

            return Question(
                f"{base}+{x} ___ {base}+{y}",
                ans,
                "comparison"
            )
