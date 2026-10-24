"""Export the published bank to a standalone, editable LaTeX answer workbook.

Reads the published Markdown so question text and MC option order are preserved.
Refuses to overwrite an existing workbook unless --force is explicitly supplied.
Once answers are entered, compile that .tex directly; do not regenerate it.
"""
from pathlib import Path
import argparse
import re
import shutil
import subprocess

SOURCE = Path(__file__).resolve().parent
NOTES = SOURCE.parent
ROOT = NOTES.parent
BUILD = ROOT / '.study_build' / 'exam_workbook'
OUTPUT = NOTES / 'AI_EXAM_PRACTICE_WORKBOOK.tex'

INTRO = r'''---
title: "Artificial Intelligence: Practice Workbook"
subtitle: "380 questions with editable answer spaces"
author: "Slide-by-slide practice"
---

# Using this workbook

This workbook contains the same **380 questions**, multiple-choice option order,
question IDs, slide titles, and source page references as
**AI_EXAM_PRACTICE_QUESTIONS.pdf**. It includes 18 teaching PDFs and the separate
Lab 4 supplement. **0. Presentation and 0.1. Math background are excluded.**
There are no supplied answers or worked solutions.

**To type your solutions:** open **AI_EXAM_PRACTICE_WORKBOOK.tex** in a LaTeX
editor. Each question is followed by a `solution` environment labelled with its
ID. Type your response on the blank line between `\begin{solution}` and
`\end{solution}`. Lines starting with `%` are comments and do not appear in the
PDF: put your answer on its own line, without `%`. Keep the question IDs and
option order unchanged so your responses can be checked reliably.

- **Multiple choice:** enter A, B, C, or D. A brief explanation is optional.
- **Short answers:** usually write 1--3 sentences or a few brief points.
- **Calculations:** show the short calculation and your final result. Use
  `$...$` for inline mathematics or `\[...\]` for a displayed equation.

Empty answer blocks provide handwriting space. Once you type a response, that
space is replaced by your text. You can change the optional dimension in square
brackets to adjust the blank space if you prefer printing the workbook.

**Compile with pdfLaTeX**, twice to update the table of contents. This is a
standalone `.tex` file: you can upload it directly to Overleaf or use your usual
LaTeX editor. The course slide PDFs are needed only if you want the local source
links to open; their absence does not prevent compilation. Source references
count PDF pages from 1, including title pages.

**For feedback:** upload your completed `.tex` file, preferably together with its
compiled PDF. You may submit one section at a time. Leave unattempted questions
blank so they can be distinguished from your answers. Save a copy before editing;
do not regenerate the workbook after entering solutions, because regeneration
replaces its contents.

This editable file is for preparation before the exam. For timed practice,
follow the announced exam rules: answer on paper, consult offline PDFs, and do
not type or use text search. The full workbook is a question bank, not a single
one-hour paper.

'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tex-only', action='store_true', help='Export without compiling the PDF')
    parser.add_argument('--force', action='store_true', help='Replace an existing workbook, discarding any answers in it')
    args = parser.parse_args()
    if OUTPUT.exists() and not args.force:
        raise SystemExit(f'Refusing to overwrite {OUTPUT.name}; it may contain your answers. '
                         'Compile it directly, or back it up before explicitly using --force.')

    markdown = (NOTES / 'AI_EXAM_PRACTICE_QUESTIONS.md').read_text(encoding='utf-8')
    first_deck = re.search(r'^# 1\.1\. Fundamentals\s*$', markdown, re.M)
    assert first_deck, 'First teaching-deck heading missing'
    question_body = markdown[first_deck.start():]
    ids = re.findall(r'^### ((?:\d\.\dE?|L4)-[MSC]\d{2}) \u00b7 ', question_body, re.M)
    assert len(ids) == len(set(ids)) == 380, 'Expected 380 unique question IDs'
    BUILD.mkdir(parents=True, exist_ok=True)
    intermediate = BUILD / 'workbook.md'
    intermediate.write_text(INTRO + question_body, encoding='utf-8')
    generated = BUILD / OUTPUT.name
    subprocess.run([
        'pandoc', str(intermediate), '-f', 'markdown', '-t', 'latex', '-s',
        '--lua-filter', str(SOURCE / 'workbook_layout.lua'),
        '--include-in-header', str(SOURCE / 'header.tex'),
        '--include-in-header', str(SOURCE / 'workbook_answers.tex'),
        '-V', 'documentclass=article', '-V', 'fontsize=10pt',
        '-V', 'geometry:a4paper,margin=20mm,headheight=15pt',
        '-V', 'colorlinks=true', '-V', 'urlcolor=examteal',
        '--toc', '--toc-depth=1', '-o', str(generated)
    ], check=True)
    tex = generated.read_text(encoding='utf-8')
    answer_ids = re.findall(r'\\begin\{solution\}\[[^\]]+\]\{([^}]+)\}', tex)
    assert answer_ids == ids, 'Answer blocks must match every question in order'
    assert len(re.findall(r'^% QUESTION ', tex, re.M)) == 380
    assert not re.search(r'\\(?:input|include)\{', tex), 'Workbook must be self-contained'
    help_comment = (
        '% EDIT THIS FILE to write your own answers. No answers are supplied.\n'
        '% Find each \\begin{solution}[...]{QUESTION-ID}, and type on the blank line inside.\n'
        '% Do not put a % before your answer: that would hide it from the PDF.\n'
        '% Compile with pdfLaTeX twice. Upload this file and/or its PDF for review.\n'
        '% Preserve question IDs and MC option order. Do not regenerate after adding answers.\n\n'
    )
    OUTPUT.write_text(help_comment + tex, encoding='utf-8')
    print('Exported standalone TeX: 380 questions and 380 empty answer blocks.')
    if args.tex_only:
        return
    for _ in range(3):
        result = subprocess.run([
            'pdflatex', '-interaction=nonstopmode', '-halt-on-error',
            '-output-directory', str(BUILD), str(OUTPUT)
        ], cwd=NOTES, capture_output=True, text=True, errors='replace')
        if result.returncode:
            print(result.stdout[-6000:])
            print(result.stderr[-2000:])
            raise SystemExit(result.returncode)
    log = (BUILD / OUTPUT.with_suffix('.log').name).read_text(encoding='utf-8', errors='replace')
    warnings = [line for line in log.splitlines() if 'Overfull' in line or 'Missing character' in line]
    if warnings:
        print('Layout warnings:', '\n'.join(warnings))
    shutil.copyfile(BUILD / OUTPUT.with_suffix('.pdf').name, OUTPUT.with_suffix('.pdf'))
    print('Built PDF:', OUTPUT.with_suffix('.pdf').name)


if __name__ == '__main__':
    main()
