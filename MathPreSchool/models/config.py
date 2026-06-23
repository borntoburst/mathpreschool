from dataclasses import dataclass

@dataclass
class WorksheetConfig:

    min_number: int
    max_number: int

    finger_limit: int = 10

    q1_count: int = 10
    q2_count: int = 10
    q3_count: int = 10
    q4_count: int = 6
    q5_count: int = 10