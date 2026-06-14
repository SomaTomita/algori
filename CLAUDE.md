# algori — algorithm learning repository

A **learning** repository for data structures and algorithms. This is teaching material, not production code.
Each `.py` is a self-contained script that runs on its own, paired with an explanation (`concept.md` / `README.md`).

## Most important: what "good code" means here (overrides global settings)

In this repo, **the explanatory comments and the side-by-side multiple solutions are themselves the deliverable**. My usual
defaults — "surgical change / minimal comments / keep only the single optimal solution" — **do not apply here**.

- **Do not delete or summarize** explanatory comments (why it works, complexity, `common mistakes`, traces).
- **Intentionally keep** the naive → optimal progression. Do not consolidate it down to "just the optimal solution" on your own.
- Prioritize **what can be learned by reading** over conciseness. Three similar lines are fine if it serves the teaching.
- When editing an existing file, match the explanation style and granularity of that chapter. When in doubt, imitate nearby files.

## Language

- Prose (docstrings, comments, `.md`) is in **Japanese**. Code identifiers are in English.
- Exception: the problem-statement docstrings in `neetcode/` transcribe the **original LeetCode English verbatim** (to follow the submission format).

## File shape (`basic/` and `Top6InterviewConcepts/`)

Teaching scripts follow this template:

1. Module docstring — problem description + `例:` + `制約:` (include the LeetCode # if there is one)
2. Imports such as `from typing import List`
3. Define solutions in **naive → optimal** order. Write the time/space complexity in each function's docstring
4. Explanatory comment blocks such as `なぜ O(1) か` / `よくある間違い` / comparisons with list
5. In `if __name__ == "__main__":`, lay out `test_cases` (tuples of input, expected value) and print `OK`/`NG` to verify
6. If needed, a `*_traced` version — same logic as the main one but prints each step, for learning

## `neetcode/` shape

LeetCode mirror format. The `class Solution:` method signature and the problem statement use the original English. Comments are light.

## Running and verifying

- Verification = **run the script and check the `__main__` output**. `python3 path/to/file.py`
- There is **no** pytest, coverage, lint/format tooling, or CI. Do not bring in a test harness or TDD workflow.
- Dependencies are the **standard library only** (`typing`, `collections`, `heapq`, etc.). Do **not** add `requirements.txt`,
  `pyproject.toml`, or packaging.
- Type annotations are required. Use the built-in generic notation `dict[int, int]` / `list[int]` (Python 3.9+; local is 3.14).

## Directory layout

```
vscode/
├── basic/                  Intro material based on a transcription of the Sheldon Chai DSA course (00_foundations 〜 08_heaps)
│                           Each chapter is README.md (concepts, diagrams, templates) + *.py (worked examples + traces)
├── Top6InterviewConcepts/  6 concepts common in interviews. Each chapter has concept.md + a representative medium-difficulty problem *.py
└── neetcode/               LeetCode per-problem collection (by data structure). class Solution format
```

`.idea/` is JetBrains IDE configuration. Do not touch it.

## Git

- Conventional Commits. The scope is the chapter/collection name (e.g., `docs(basic): add hashmaps chapter README`).
- Commit messages are in short English. One commit = one topic.
- **Do not add Claude as a co-author**. Do not attach a `Co-Authored-By` trailer or any generated-tool signature.
