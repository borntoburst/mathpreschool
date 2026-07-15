from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from .question import Question, QuestionType, Difficulty


@dataclass
class WorksheetSection:
    """
    Một nhóm câu hỏi cùng loại (VD toàn bộ phần "Quy luật").
    Layout Engine tính bố cục riêng cho từng section, bao gồm cả số cột (Question Grid).
    """
    title: str
    question_type: QuestionType
    questions: List[Question] = field(default_factory=list)
    columns: int = 1  # Do Layout Engine / Question Grid quyết định, không set cứng

    def question_count(self) -> int:
        return len(self.questions)

    def average_char_length(self) -> float:
        if not self.questions:
            return 0.0
        return sum(q.char_length() for q in self.questions) / len(self.questions)


@dataclass
class Worksheet:
    """
    Model tổng đại diện cho MỘT worksheet hoàn chỉnh.
    Được sinh đúng MỘT LẦN dựa trên seed xác định khi người dùng nhấn Generate.
    Preview, PDF hay bất kỳ Renderer nào khác đều đọc trực tiếp từ đây.
    """
    id: str
    title: str
    seed: int
    min_number: int
    max_number: int
    finger_limit: int
    difficulty: Difficulty
    sections: List[WorksheetSection] = field(default_factory=list)
    student_name_field: bool = True
    theme_name: str = "default"

    def total_question_count(self) -> int:
        return sum(s.question_count() for s in self.sections)

    def all_questions(self) -> List[Question]:
        result: List[Question] = []
        for s in self.sections:
            result.extend(s.questions)
        return result

    def get_section(self, question_type: QuestionType) -> WorksheetSection | None:
        for s in self.sections:
            if s.question_type == question_type:
                return s
        return None
