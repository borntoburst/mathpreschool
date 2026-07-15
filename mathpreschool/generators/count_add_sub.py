from __future__ import annotations
from typing import Optional, Tuple

from models import Question, QuestionType, Difficulty
from .base import BaseGenerator


class CountAddSubGenerator(BaseGenerator):
    """
    Sinh câu hỏi dạng "a + b = ___" hoặc "a - b = ___".

    Ràng buộc bắt buộc theo thiết kế FingerMath:
    - b (số được thêm/bớt) luôn <= finger_limit VÀ luôn nằm trong khoảng 0-9
      (chỉ dùng một bàn tay để đếm thêm/bớt).
    - Phép cộng không được phát sinh nhớ: (a % 10) + b <= 9.
    - Phép trừ không được phát sinh mượn: (a % 10) >= b.
    - Tuyệt đối KHÔNG sinh phép cộng/trừ trực tiếp hai số có hai chữ số
      (đã tự động thỏa vì b luôn là số có một chữ số, a chỉ đóng vai trò
      số nền được "đếm thêm/bớt", không phải số hạng thứ hai có 2 chữ số).
    """

    def _difficulty_amount_range(self, difficulty: Difficulty, finger_limit: int) -> Tuple[int, int]:
        """Quyết định khoảng giá trị của b (số thêm/bớt) theo độ khó."""
        finger_limit = max(1, min(finger_limit, 9))
        if difficulty == Difficulty.EASY:
            return 1, min(3, finger_limit)
        if difficulty == Difficulty.NORMAL:
            return 1, finger_limit
        # HARD: ưu tiên số thêm/bớt lớn, gần sát finger_limit hơn
        low = max(1, finger_limit - 2)
        return low, finger_limit

    def _difficulty_operator_weights(self, difficulty: Difficulty) -> Tuple[float, float]:
        """Trả về (trọng số cộng, trọng số trừ)."""
        if difficulty == Difficulty.EASY:
            return 0.8, 0.2   # trẻ mới học: ưu tiên cộng
        if difficulty == Difficulty.NORMAL:
            return 0.5, 0.5
        return 0.4, 0.6       # HARD: ưu tiên trừ (khó hơn với trẻ)

    def _choose_operator(self, difficulty: Difficulty) -> str:
        w_add, w_sub = self._difficulty_operator_weights(difficulty)
        return self.rng.choices(["+", "-"], weights=[w_add, w_sub], k=1)[0]

    def _try_generate_one(
        self,
        index: int,
        difficulty: Difficulty,
        min_number: int,
        max_number: int,
        finger_limit: int,
    ) -> Optional[Question]:
        finger_limit = max(1, min(finger_limit, 9))
        amount_low, amount_high = self._difficulty_amount_range(difficulty, finger_limit)
        amount = self.rng.randint(amount_low, amount_high)

        a = self.rng.randint(min_number, max_number)
        ones_digit = a % 10

        operator = self._choose_operator(difficulty)

        if operator == "+":
            if ones_digit + amount > 9:
                return None  # sẽ phát sinh nhớ -> loại
            result = a + amount
            display_text = f"{a} + {amount} = ___"
        else:
            if ones_digit < amount:
                return None  # sẽ phát sinh mượn -> loại
            result = a - amount
            if result < 0:
                return None
            display_text = f"{a} - {amount} = ___"

        question_id = f"count_add_sub_{index}_{self.rng.randint(0, 10_000_000)}"
        return Question(
            id=question_id,
            type=QuestionType.COUNT_ADD_SUB,
            difficulty=difficulty,
            display_text=display_text,
            answer=str(result),
            operands=[a, amount],
            finger_limit_used=amount,
            requires_carry=False,
            requires_borrow=False,
            metadata={"operator": operator},
        )
