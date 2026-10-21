from dataclasses import dataclass

@dataclass
class DocumentSummary:
    file: str
    headings: list[str]
    links: list[str]
    word_count: int