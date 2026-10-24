# Rebuild the expanded exam practice files

The editable question sources are in `decks/`, one Markdown file per slide PDF. Edit those files, then run `build.py` with Python 3. Pandoc and pdfLaTeX must be on PATH. Use `--markdown-only` to validate and regenerate both Markdown documents without compiling PDFs.

Each source must contain M01–M10, S01–S07, and C01–C03: 10 multiple-choice, 7 short-answer, and 3 calculation questions. The heading after `|` gives PDF pages counted from 1. The build adds the deck code to every ID, links sources, and shuffles MC options reproducibly without creating an answer key.

There are 18 teaching-deck sections (including the separately supplied LSTM extra material) plus one Lab 4 supplement: 380 questions total. The administrative presentation and mathematical-background PDFs are deliberately excluded at the user's request. Numerical questions are small practice applications of the cited slide concepts.

`build.py` contains the source catalog and two disjoint mock-paper selections. It checks IDs, exact duplicate prompts, question-type counts, option uniqueness, source-file existence, page bounds, and mock composition. Generated Markdown/PDF files are in `Study Notes/`; temporary TeX files and logs are in `.study_build/exam_practice/`.

## Editable answer workbook

`build_workbook.py` exports the published question-bank Markdown to `../AI_EXAM_PRACTICE_WORKBOOK.tex` and compiles its PDF. It preserves the published wording, IDs, source references, and option order, and adds an empty `solution` environment after every question. The exported TeX embeds all formatting and needs no local style files; compile it directly with pdfLaTeX after entering answers.

The exporter uses `workbook_layout.lua`, `header.tex`, and `workbook_answers.tex`. Use `--tex-only` to skip compilation. It refuses to overwrite an existing workbook by default, protecting entered answers. `--force` explicitly replaces it: back up any completed work first. The ordinary `build.py` does not regenerate the workbook. Temporary workbook files are kept in `.study_build/exam_workbook/`.
