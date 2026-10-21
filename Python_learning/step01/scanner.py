import re
from pathlib import Path
from collections.abc import Iterator

def read_file_lines(file_path: Path) -> Iterator[str]:
    """Yield a file's lines one at a time, closing it when iteration finishes."""
    with file_path.open("r", encoding="utf-8") as file:
        yield from file


def extract_headings(lines: list[str]) -> list[str]:
    """Return text from Markdown ATX headings (for example, '# Title')."""
    headings: list[str] = []

    for line in lines:
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            headings.append(match.group(1))

    return headings


def extract_links(lines: list[str]) -> list[str]:
    """Return URLs from inline Markdown links, such as [Python](https://...)."""
    links: list[str] = []

    for line in lines:
        links.extend(re.findall(r"\[[^\]]*\]\(([^)]+)\)", line))

    return links


def count_words(lines: list[str]) -> int:
    """Count whitespace-separated words in the Markdown source."""
    return sum(len(line.split()) for line in lines)
