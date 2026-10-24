"""Validate and publish the slide-by-slide question bank and two mock papers.

Edit decks/*.md; these are the authoritative, question-only sources.
Python's standard library, Pandoc, and pdfLaTeX are required. No answer key exists.
"""
from pathlib import Path
from collections import Counter
from urllib.parse import quote
import argparse
import random
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
NOTES = ROOT / 'Study Notes'
SOURCE = Path(__file__).resolve().parent
BUILD = ROOT / '.study_build' / 'exam_practice'

# Code, exact local PDF title, PDF page count. Order keeps the LSTM extra beside 5.1.
CATALOG = [
    ('1.1', '1.1. Fundamentals', 45),
    ('1.2', '1.2. Shallow Learning', 85),
    ('1.3', '1.3. Bayesian Learning', 58),
    ('2.1', '2.1. Introduction to Reinforcement Learning', 16),
    ('2.2', '2.2. Markov decision processes', 26),
    ('2.3', '2.3. Q-learning', 48),
    ('2.4', '2.4. Policy Search', 19),
    ('3.1', '3.1. Introduction to Deep Learning', 41),
    ('3.2', '3.2. Shallow NN', 51),
    ('3.3', '3.3. Deep Learning Fundamentals', 44),
    ('3.4', '3.4. Deep Learning Fundamentals II', 53),
    ('4.1', '4.1. CNNs', 111),
    ('5.1', '5.1. Sequence Models', 34),
    ('5.1E', '5.1. Extra Material', 7),
    ('5.2', '5.2. Transformers', 43),
    ('5.3', '5.3. Foundation models', 28),
    ('5.4', '5.4. Unsupervised learning', 38),
    ('5.5', '5.5. Generative Models', 26),
    ('L4', 'manolo_presentation', 15),
]
KINDS = {'M': 'MC', 'S': 'Short', 'C': 'Calculation'}
PAPERS = [
    ('A', ['1.1-M05', '1.2-M03', '1.2-M06', '1.3-M06', '2.1-M09', '2.2-M01',
           '2.2-M07', '2.3-M06', '2.4-M06', '3.1-M04', '3.2-M05', '3.3-M06',
           '3.4-M08', '4.1-M08', '5.1-M09', '5.1E-M09', '5.2-M08', '5.3-M06',
           '5.4-M03', '5.5-M08'],
          ['1.2-C01', '3.2-C01', '1.3-S03', '2.3-S04', '2.4-S06', '4.1-S05',
           '5.2-S04', '5.5-S06']),
    ('B', ['1.1-M09', '1.2-M08', '1.2-M10', '1.3-M08', '2.1-M04', '2.2-M10',
           '2.3-M10', '2.4-M03', '3.1-M07', '3.2-M07', '3.3-M10', '3.4-M03',
           '4.1-M06', '4.1-M10', '5.1-M07', '5.1E-M08', '5.2-M09', '5.3-M05',
           '5.4-M10', '5.5-M05'],
          ['2.3-C01', '4.1-C01', '1.1-S04', '3.3-S05', '3.4-S01', '5.1-S06',
           '5.3-S04', '5.4-S06']),
]

def load_questions():
    decks, questions, prompts = [], {}, set()
    expected_ids = [f'{prefix}{i:02}' for prefix, count in [('M', 10), ('S', 7), ('C', 3)]
                    for i in range(1, count + 1)]
    for code, pdf_title, page_count in CATALOG:
        source = (SOURCE / 'decks' / f'{code}.md').read_text(encoding='utf-8')
        heading = re.match(r'# (.+)\n', source).group(1)
        if code != 'L4':
            assert heading == pdf_title, (code, 'Deck heading does not match PDF title')
        relative_pdf = (f'Lab Sessions/Lab4/{pdf_title}.pdf' if code == 'L4'
                        else f'Lecture Slides/{pdf_title}.pdf')
        assert (ROOT / relative_pdf).is_file(), relative_pdf
        pdf_link = '../' + quote(relative_pdf, safe='/')
        matches = list(re.finditer(r'^### ([MSC]\d{2}) \| ([\d–, ]+)\n(.*?)(?=^### |\Z)', source, re.M | re.S))
        assert [m[1] for m in matches] == expected_ids, (code, 'Expected exactly 10 MC, 7 short, 3 calculations')
        entries = []
        for match in matches:
            local_id, pages, body = match[1], match[2], match[3].strip()
            qid = f'{code}-{local_id}'
            kind = KINDS[local_id[0]]
            page_numbers = [int(x) for x in re.findall(r'\d+', pages)]
            assert all(1 <= n <= page_count for n in page_numbers), (qid, 'Page outside source PDF')
            options = re.findall(r'^- ([A-D])\. (.+)$', body, re.M)
            if kind == 'MC':
                assert [x[0] for x in options] == list('ABCD'), (qid, 'Four labelled options required')
                choices = [x[1] for x in options]
                assert len(set(choices)) == 4, (qid, 'Duplicate options')
                prompt = body.split('\n- A. ', 1)[0]
                # Stable shuffling removes patterned option positions; no key is produced.
                random.Random('AI-course-2026-' + qid).shuffle(choices)
                body = prompt + '\n\n' + '\n'.join(f'- {letter}. {choice}' for letter, choice in zip('ABCD', choices))
            else:
                assert not options, (qid, 'Unexpected MC options')
                prompt = body
            assert prompt not in prompts, (qid, 'Exact duplicate prompt')
            prompts.add(prompt)
            assert qid not in questions
            question = dict(id=qid, kind=kind, body=body, pages=pages, title=pdf_title,
                            link=pdf_link + '#page=' + str(page_numbers[0]), deck=code)
            questions[qid] = question
            entries.append(question)
        decks.append(dict(code=code, title=heading, pdf_title=pdf_title, link=pdf_link, questions=entries))
    assert len(questions) == 380
    assert not any(code.startswith('0') for code, _, _ in CATALOG)
    return decks, questions

def render_question(q, number=None, show_title=False):
    label = f'{number}. ' if number is not None else ''
    source_label = f'{q["title"]}.pdf · PDF pp. {q["pages"]}' if show_title else f'PDF pp. {q["pages"]}'
    return (f'\n### {label}{q["id"]} · {q["kind"]}\n\n'
            f'*Source: [{source_label}]({q["link"]}).*\n\n{q["body"]}\n')

def write_documents(decks, questions):
    bank = ['''---
title: "Artificial Intelligence: Slide-by-Slide Exam Practice"
subtitle: "10 multiple choice + 7 short answers + 3 easy calculations per deck"
author: "Questions only · 24 October 2026"
---

# How to use this question bank

**380 questions, with no answers or worked solutions:** 360 questions for the 18 teaching PDFs, plus a separate 20-question Lab 4 supplement. **0. Presentation and 0.1. Math background are excluded.** Each teaching PDF has its own section, using its exact filename title. The separate **5.1. Extra Material** PDF has its own LSTM section, identified by `5.1E` in question IDs.

Every section contains exactly:

- **M01–M10: 10 multiple-choice questions.** Choose one best answer from A–D.
- **S01–S07: 7 short-answer questions.** Aim for 1–3 sentences, or a few brief points when asked.
- **C01–C03: 3 easy calculation problems.** Show a short calculation; no long derivations or multi-step training simulations are needed.

Questions prioritize definitions, the meaning of values and hyperparameters, distinctions between methods, and small applications of the concepts. Parameter counts include biases only when stated. Numerical examples are newly constructed practice applications; the source pages identify the underlying concept, not necessarily an identical exercise in the slides. Introductory decks use simple data or representation calculations appropriate to their content.

**Source references count PDF pages from 1, including title pages**, rather than using printed slide numbers. Each question has a page reference under its ID. For example, `3.2-C01` is calculation 1 from **3.2. Shallow NN.pdf**. Click the source reference to open the relevant local PDF.

This is a revision bank, not one exam. A useful deck-level session is about 30–40 minutes. For full-course timing, the accompanying **AI_EXAM_MOCK_PAPERS.pdf** contains two different one-hour papers: 20 MC questions and 8 short questions each, including 2 calculations. Allow 20 minutes for MC, 32 minutes for short questions, and 8 minutes to review. These are practice formats, not a prediction of the teachers' question count or topic weighting.
''']
    for deck in decks:
        bank.append(f'\n# {deck["title"]}\n\n**Slides:** [{deck["pdf_title"]}.pdf]({deck["link"]}). '
                    '**20 questions: 10 MC · 7 short answers · 3 easy calculations.**\n')
        if deck['code'] == 'L4':
            bank.append('\nSupplement from the Lab 4 briefing. This is separate from the numbered lecture PDFs.\n')
        previous = None
        for q in deck['questions']:
            if q['kind'] != previous:
                heading = {'MC': 'Multiple choice', 'Short': 'Short answers', 'Calculation': 'Easy calculations'}[q['kind']]
                bank.append(f'\n## {heading}\n')
                previous = q['kind']
            bank.append(render_question(q))
    bank_path = NOTES / 'AI_EXAM_PRACTICE_QUESTIONS.md'
    bank_path.write_text('\n'.join(bank), encoding='utf-8')
    mock = ['''---
title: "Artificial Intelligence: Two One-Hour Mock Papers"
subtitle: "From the expanded slide-by-slide bank · Questions only"
author: "24 October 2026"
---

# Instructions

Each paper contains **20 multiple-choice questions and 8 short questions**, including **2 easy calculations**. Allow **60 minutes per paper**: 20 minutes for MC, 32 minutes for short questions, and 8 minutes to review. Choose one best option for each MC question. Keep written answers to 1–3 sentences unless a brief list is requested.

The papers use different questions from the expanded bank. Source titles, PDF page references, and stable question IDs are retained for review after your attempt. No answers, marked options, or worked solutions are included. The PDFs provide writing space for short answers.

**0. Presentation and 0.1. Math background are excluded.** The Lab 4 supplement is available separately in the bank. The question count and timing are suggested practice formats, not the teachers' confirmed marking scheme.
''']
    used = set()
    for label, mc, short in PAPERS:
        assert len(mc) == 20 and len(short) == 8
        assert all(questions[q]['kind'] == 'MC' for q in mc)
        assert Counter(questions[q]['kind'] for q in short) == {'Short': 6, 'Calculation': 2}
        assert len(set(mc + short)) == 28
        assert not used.intersection(mc + short), 'Repeated mock question'
        used.update(mc + short)
        mock.append(f'\n# Paper {label} · Multiple choice\n\nSuggested time: 20 minutes.\n')
        mock.extend(render_question(questions[q], i, True) for i, q in enumerate(mc, 1))
        mock.append(f'\n# Paper {label} · Short questions\n\nSuggested time: 32 minutes, then 8 minutes to review the paper.\n')
        mock.extend(render_question(questions[q], i, True) for i, q in enumerate(short, 21))
    mock_path = NOTES / 'AI_EXAM_MOCK_PAPERS.md'
    mock_path.write_text('\n'.join(mock), encoding='utf-8')
    return bank_path, mock_path

def build_pdf(path, contents=False):
    BUILD.mkdir(parents=True, exist_ok=True)
    tex = BUILD / (path.stem + '.tex')
    cmd = ['pandoc', str(path), '-f', 'markdown', '-t', 'latex', '-s',
           '--lua-filter', str(SOURCE / 'layout.lua'),
           '--include-in-header', str(SOURCE / 'header.tex'),
           '-V', 'documentclass=article', '-V', 'fontsize=10pt',
           '-V', 'geometry:a4paper,margin=20mm,headheight=15pt',
           '-V', 'colorlinks=true', '-V', 'urlcolor=examteal', '-o', str(tex)]
    if contents:
        cmd += ['--toc', '--toc-depth=1']
    subprocess.run(cmd, check=True)
    for _ in range(3 if contents else 2):
        result = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                                 '-output-directory', str(BUILD), str(tex)],
                                cwd=ROOT, capture_output=True, text=True, errors='replace')
        if result.returncode:
            print(result.stdout[-6000:])
            print(result.stderr[-2000:])
            raise SystemExit(result.returncode)
    log = tex.with_suffix('.log').read_text(encoding='utf-8', errors='replace')
    warnings = [line for line in log.splitlines() if 'Overfull' in line or 'Missing character' in line]
    if warnings:
        print(path.name, 'layout warnings:', '\n'.join(warnings))
    shutil.copyfile(tex.with_suffix('.pdf'), path.with_suffix('.pdf'))
    print('Built:', path.with_suffix('.pdf').relative_to(ROOT))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--markdown-only', action='store_true')
    args = parser.parse_args()
    decks, questions = load_questions()
    paths = write_documents(decks, questions)
    counts = Counter(q['kind'] for q in questions.values())
    assert counts == {'MC': 190, 'Short': 133, 'Calculation': 57}
    print(f'Validated {len(decks)} sections, each 10 MC + 7 short + 3 calculations.')
    print('Total:', len(questions), dict(counts))
    print('Validated unique IDs, unique prompts, four distinct MC options, source files/page bounds, and two disjoint mocks.')
    if not args.markdown_only:
        for path in paths:
            build_pdf(path, contents=path == paths[0])

if __name__ == '__main__':
    main()
