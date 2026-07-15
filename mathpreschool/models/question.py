from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List


class QuestionType(str, Enum):
    """5 nhóm bài tập chính theo thiết kế MathPreSchool."""
    COUNT_ADD_SUB = "count_add_sub"   # Đếm thêm - Đếm bớt
    FILL_MISSING = "fill_missing"     # Điền số còn thiếu (□+a=b, a+□=b, □-a=b)
    COMPARE = "compare"               # So sánh (số-số, phép-phép, phép-số)
    PATTERN = "pattern"               # Quy luật (dãy số)
    MULTI_STEP = "multi_step"         # Tính nhiều bước (2-3 bước)


class Difficulty(str, Enum):
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"


class ComparisonOperator(str, Enum):
    LESS_THAN = "<"
    GREATER_THAN = ">"
    EQUAL = "="


@dataclass(frozen=True)
class Question:
    """
    Model bất biến (immutable) đại diện cho MỘT câu hỏi duy nhất.
    Đây là nguồn dữ liệu duy nhất (single source of truth) được dùng
    xuyên suốt Preview, PDF và mọi định dạng xuất khác — không tái sinh nội dung.
    """
    id: str
    type: QuestionType
    difficulty: Difficulty
    display_text: str                      # VD: "3 + 2 = ___" hoặc "□ + 4 = 7"
    answer: str                            # Đáp án chính thức (string để linh hoạt mọi dạng)
    operands: List[int] = field(default_factory=list)   # Số hạng, để Validator kiểm tra giới hạn
    finger_limit_used: Optional[int] = None              # Số ngón tay cần dùng để giải câu này
    requires_carry: bool = False           # Cộng có nhớ? (Validator phải luôn == False)
    requires_borrow: bool = False          # Trừ có mượn? (Validator phải luôn == False)
    metadata: dict = field(default_factory=dict)  # Bước trung gian, kiểu quy luật, v.v.

    def char_length(self) -> int:
        """Dùng bởi Question Estimator để ước lượng kích thước hiển thị trên trang A4."""
        return len(self.display_text)

    def is_valid_fingermath(self) -> bool:
        """Kiểm tra nhanh: không cộng nhớ, không trừ mượn."""
        return not self.requires_carry and not self.requires_borrow
