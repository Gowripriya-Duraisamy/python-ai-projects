# Step 1: Analyze Markdown files

This command-line tool practices functions, lists, dictionaries, generators, regular expressions, type hints, file handling, exceptions, and JSON output. It summarizes Markdown files with headings that match a search word and file content that includes a phrase.

## Run it

From this directory, pass either one `.md` file or a folder. Folder scans include subfolders.

```powershell
# Scan a folder recursively
python -m step01.cli "D:\path\to\markdown-files"

# Scan one Markdown file and choose both filters
python -m step01.cli "D:\path\to\markdown-files" --search_word "RAG" --phrase "vector database"
```

Both filters default to `python`. Matching is case-insensitive. A file appears in the JSON output only when it contains the phrase and has at least one heading containing the search word. A file that passes the phrase filter but has no matching heading is omitted.

The JSON output is an array of summaries. Each summary contains the file name, matching headings, inline Markdown link URLs, and a whitespace-separated word count. Markdown syntax and punctuation may be included in the count.

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

## Helpful resource

Read the [official Python tutorial](https://docs.python.org/3/tutorial/).
