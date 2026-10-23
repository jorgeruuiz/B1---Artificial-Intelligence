"""Build question-only mock papers and PDFs from the editable question bank."""
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
NOTES = ROOT / 'Study Notes'
SOURCE = Path(__file__).resolve().parent
BUILD = ROOT / '.study_build' / 'exam_practice'
BUILD.mkdir(parents=True, exist_ok=True)
bank_path = NOTES / 'AI_EXAM_PRACTICE_QUESTIONS.md'
bank = bank_path.read_text(encoding='utf-8')
questions = {}
for match in re.finditer(r'^### (Q\d{3}) · (MC|Short|Calculation)\n(.*?)(?=^#{1,3} |\Z)', bank, re.M | re.S):
    questions[match[1]] = (match[2], match[3].strip())
expected = {f'Q{i:03}' for i in range(1, 129)}
assert set(questions) == expected, 'Missing or unexpected question identifiers'
assert len(re.findall(r'^### Q\d{3}', bank, re.M)) == len(expected), 'Duplicate question identifier'
for qid, (kind, body) in questions.items():
    options = re.findall(r'^- ([A-D])\. ', body, re.M)
    assert options == (list('ABCD') if kind == 'MC' else []), (qid, options)
papers = [
    ('A', [1, 8, 10, 16, 18, 28, 30, 35, 37, 42, 53, 57, 70, 71, 81, 89, 91, 99, 109, 116],
     [22, 46, 32, 64, 77, 84, 98, 119]),
    ('B', [2, 7, 11, 17, 19, 20, 27, 31, 39, 40, 44, 55, 58, 60, 67, 82, 90, 94, 101, 117],
     [23, 50, 61, 76, 86, 95, 103, 111]),
]
used = set()
mock = ['''---
title: "Artificial Intelligence: Two One-Hour Mock Papers"
subtitle: "Questions only · 23 October 2026"
author: "MAICE · Artificial Intelligence"
lang: en-GB
---

# Instructions

Each paper contains **20 multiple-choice questions and 8 short questions**, including **2 small calculations**. The papers contain different questions drawn from `AI_EXAM_PRACTICE_QUESTIONS.md`. They are suggested practice formats, not the teachers' announced question count or marking scheme.

Allow **60 minutes per paper**: 20 minutes for multiple choice, 32 minutes for short questions, and 8 minutes to review. Choose exactly one option for each MC question. Keep written responses to 1–3 sentences unless a short list is requested. For calculations, show a formula and substitution.

No answer key, marked options, or worked solutions are included. The bank identifiers are retained so you can locate each question and its source topic after finishing. The PDFs include writing space after short questions.

Use the source map in the full question bank to review the relevant slides after attempting a paper. The Lab 4 supplement is available in the bank but is not included in these two lecture-based mock papers.
''']
for label, mc_ids, short_ids in papers:
    all_ids = [f'Q{i:03}' for i in mc_ids + short_ids]
    assert not used.intersection(all_ids), 'Repeated question between papers'
    used.update(all_ids)
    assert len(mc_ids) == 20 and len(short_ids) == 8
    assert all(questions[f'Q{i:03}'][0] == 'MC' for i in mc_ids)
    assert sum(questions[f'Q{i:03}'][0] == 'Calculation' for i in short_ids) == 2
    assert all(questions[f'Q{i:03}'][0] != 'MC' for i in short_ids)
    mock.append(f'\n# Paper {label} · Multiple choice\n\nSuggested time: 20 minutes. Choose one best answer per question.\n')
    for n, i in enumerate(mc_ids, 1):
        qid = f'Q{i:03}'
        kind, body = questions[qid]
        mock.append(f'\n### {n}. {qid} · {kind}\n\n{body}\n')
    mock.append(f'\n# Paper {label} · Short questions\n\nSuggested time: 32 minutes. Then use the final 8 minutes to review the whole paper.\n')
    for n, i in enumerate(short_ids, 21):
        qid = f'Q{i:03}'
        kind, body = questions[qid]
        mock.append(f'\n### {n}. {qid} · {kind}\n\n{body}\n')
mock_path = NOTES / 'AI_EXAM_MOCK_PAPERS.md'
mock_path.write_text('\n'.join(mock), encoding='utf-8')
for path in (bank_path, mock_path):
    tex = BUILD / (path.stem + '.tex')
    subprocess.run([
        'pandoc', str(path), '-f', 'markdown', '-t', 'latex', '-s',
        '--lua-filter', str(SOURCE / 'layout.lua'),
        '--include-in-header', str(SOURCE / 'header.tex'),
        '-V', 'documentclass=article', '-V', 'fontsize=10pt',
        '-V', 'geometry:a4paper,margin=20mm,headheight=15pt',
        '-V', 'colorlinks=true', '-V', 'urlcolor=blue', '-o', str(tex),
    ], check=True)
    for _ in range(2):
        result = subprocess.run([
            'pdflatex', '-interaction=nonstopmode', '-halt-on-error',
            '-output-directory', str(BUILD), str(tex),
        ], cwd=ROOT, capture_output=True, text=True, errors='replace')
        if result.returncode:
            print(result.stdout[-6000:])
            print(result.stderr[-2000:])
            raise SystemExit(result.returncode)
    log = tex.with_suffix('.log').read_text(encoding='utf-8', errors='replace')
    warnings = [line for line in log.splitlines() if 'Overfull' in line or 'Missing character' in line]
    if warnings:
        print(path.name, 'layout warnings:', '\n'.join(warnings))
    pdf = NOTES / (path.stem + '.pdf')
    shutil.copyfile(tex.with_suffix('.pdf'), pdf)
    print('Built:', pdf.relative_to(ROOT))
counts = {kind: sum(value[0] == kind for value in questions.values()) for kind in ('MC', 'Short', 'Calculation')}
print('Validated question bank:', len(questions), counts)
print('Validated mocks: 28 questions each, 2 calculations each, no repeated questions.')
