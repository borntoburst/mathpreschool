from dataclasses import dataclass

@dataclass
class Question:
    text: str
    answer: str
    question_type: str