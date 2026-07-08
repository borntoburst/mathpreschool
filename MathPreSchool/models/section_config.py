from dataclasses import dataclass

@dataclass
class SectionConfig:

    title: str
    generator: object
    count: int

    priority: int = 3
    color: str = "#FFFFFF"
    icon: str = ""
