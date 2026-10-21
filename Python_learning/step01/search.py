from .scanner import read_file_lines, extract_headings, extract_links, count_words
from pathlib import Path

def extract_search_headings(lines: list[str], search_word: str) -> list[str]:
    headings = extract_headings(lines)
    return [heading for heading in headings if search_word.casefold() in heading.casefold()]

def summarize_markdown(file_path: Path, search_word: str, phrase: str) -> dict[str, str | list[str] | int] | None:
    """Read one Markdown file and return its headings, links, and word count."""
    lines = list(read_file_lines(file_path))

    if not any(line.strip() for line in lines):
        raise ValueError("file is empty")

    if not any(phrase.casefold() in line.casefold() for line in lines):
        return None

    headings = extract_search_headings(lines, search_word)

    return {
        "file": file_path.name,
        "headings": headings,
        "links": extract_links(lines),
        "word_count": count_words(lines),
    } if len(headings) > 0 else None
