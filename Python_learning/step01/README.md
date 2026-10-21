# Step 1: Analyze Markdown files

This command-line tool scans one Markdown file or a folder of Markdown files. It practices Python functions, collections, comprehensions, modules, generators, file handling, exceptions, type hints, dataclasses, and JSON serialization.

For each matching file, it returns a `DocumentSummary` dataclass containing the file name, matching headings, inline Markdown link URLs, and a whitespace-separated word count. The CLI converts each dataclass to a dictionary with `dataclasses.asdict()` before writing JSON.

## Run it

From the parent directory that contains the `step01` package, run:

```powershell
# Scan a folder recursively
python -m step01.cli "D:\path\to\markdown-files"

# Scan one Markdown file and choose both filters
python -m step01.cli "D:\path\to\markdown-files\notes.md" --search_word "RAG" --phrase "vector database"
```

Both filters default to `python`. Matching is case-insensitive. A file appears in the JSON output only when its content contains the phrase and at least one heading contains the search word. Files that pass the phrase filter but have no matching heading are omitted.

The JSON output is an array. Each item has this shape:

```json
{
  "file": "notes.md",
  "headings": ["Python and RAG"],
  "links": ["https://example.com"],
  "word_count": 42
}
```

The word count splits source text on whitespace, so Markdown syntax and punctuation may be counted as part of a word.

## Error handling

- A missing path or a non-Markdown file path produces an error.
- Empty files produce a warning and are skipped.
- Unreadable files produce an error and are skipped; other files continue to be processed.
- Non-Markdown files in a folder are ignored.

## Try these cases

1. Scan a folder with Markdown files both at its top level and in a subfolder.
2. Use a phrase that appears in only one file.
3. Use a heading search word that matches some, but not all, headings.
4. Try an empty Markdown file and a missing path.
5. Explain why `read_file_lines()` uses `with` and `yield`.
6. Explain why `DocumentSummary` is a dataclass and why `asdict()` is used before `json.dumps()`.
7. Change a field type temporarily and see whether your editor or type checker reports incompatible values. Type hints help static tools; Python does not generally enforce them at runtime.

## Helpful resource

Read the [official Python tutorial](https://docs.python.org/3/tutorial/).
