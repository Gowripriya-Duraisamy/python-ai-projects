import sys
import argparse
import json
from pathlib import Path
from .search import summarize_markdown

def get_summaries(file_path: Path, args) -> dict[str, str | list[str] | int] | None:
    summary = None
    try:
        summary = summarize_markdown(file_path, args.search_word, args.phrase)
    except ValueError as error:
        print(f"WARNING: {file_path.name}: {error}", file=sys.stderr)
    except (OSError, UnicodeError) as error:
        print(f"ERROR: cannot read {file_path.name}: {error}", file=sys.stderr)
    
    return summary

def summarize_folder(args) -> list[dict[str, str | list[str] | int]]:
    """Summarize one Markdown file or Markdown files recursively in a folder.

    Problems with individual files are reported and skipped so other files
    can still be processed.
    """
    folder_path: Path = args.folder
   
    if not folder_path.exists():
        raise FileNotFoundError(f"folder does not exist: {folder_path}")
    if folder_path.is_file() and folder_path.suffix != ".md":
        raise FileNotFoundError(f"not a md file: {folder_path}")
    if folder_path.is_file() and folder_path.suffix == ".md":
        summary = get_summaries(folder_path, args)
        return [summary] if summary else []
    if not folder_path.is_dir():
        raise NotADirectoryError(f"not a folder: {folder_path}")

    summaries: list[dict[str, str | list[str] | int]] = []
    for file_path in sorted(folder_path.rglob("*.md")):
        summary = get_summaries(file_path, args)
        if summary:
            summaries.append(summary)

    return summaries if len(summaries) > 0 else []

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Summarize headings, links, and word counts in Markdown files."
    )
    parser.add_argument("folder", type=Path, help="Markdown file or folder containing .md files")
    parser.add_argument("--search_word", type=str, help="word to search for in the .md files", default="python")
    parser.add_argument("--phrase", type=str, help="phrase to filter .md files", default="python" )
    args = parser.parse_args()

    try:
        summaries = summarize_folder(args)
    except (FileNotFoundError, NotADirectoryError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(json.dumps(summaries, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())