from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional, Set
import random

from models import Question, Difficulty


class BaseGenerator(ABC):
    """
    Lớp cơ sở cho mọi Generator.

    Nguyên tắc SOLID: Generator CHỈ chịu trách nhiệm sinh dữ liệu Question.
    - KHÔNG quyết định độ khó tổng thể (đó là việc của Difficulty Engine)
    - KHÔNG kiểm tra hợp lệ cuối cùng của cả worksheet (đó là việc của Validator)
    - KHÔNG tính bố cục / số cột (đó là việc của Layout Engine)

    Mỗi Generator tự đảm bảo TỪNG câu hỏi nó sinh ra là hợp lệ về mặt
    fingermath (không nhớ, không mượn, trong giới hạn finger_limit) bằng
    rejection sampling — Validator ở tầng trên sẽ kiểm tra lại lần cuối
    trên toàn bộ worksheet (trùng lặp giữa các section, v.v.).
    """

    MAX_ATTEMPTS_PER_QUESTION = 200

    def __init__(self, rng: random.Random):
        self.rng = rng

    @abstractmethod
    def _try_generate_one(
        self,
        index: int,
        difficulty: Difficulty,
        min_number: int,
        max_number: int,
        finger_limit: int,
    ) -> Optional[Question]:
        """Thử sinh MỘT câu hỏi. Trả về None nếu lần thử không thỏa điều kiện."""
        raise NotImplementedError

    def generate(
        self,
        count: int,
        difficulty: Difficulty,
        min_number: int,
        max_number: int,
        finger_limit: int,
    ) -> List[Question]:
        """
        Sinh `count` câu hỏi không trùng lặp (theo display_text).
        Ném RuntimeError nếu không thể sinh đủ số lượng trong giới hạn thử.
        """
        questions: List[Question] = []
        seen_texts: Set[str] = set()

        for i in range(count):
            question: Optional[Question] = None
            for _ in range(self.MAX_ATTEMPTS_PER_QUESTION):
                candidate = self._try_generate_one(
                    index=i,
                    difficulty=difficulty,
                    min_number=min_number,
                    max_number=max_number,
                    finger_limit=finger_limit,
                )
                if candidate is None:
                    continue
                if candidate.display_text in seen_texts:
                    continue
                question = candidate
                break

            if question is None:
                raise RuntimeError(
                    f"Không thể sinh câu hỏi hợp lệ thứ {i + 1}/{count} "
                    f"(min={min_number}, max={max_number}, finger_limit={finger_limit}). "
                    "Hãy nới rộng khoảng số hoặc giảm số lượng câu hỏi."
                )

            seen_texts.add(question.display_text)
            questions.append(question)

        return questions
