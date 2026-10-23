# Rebuild the exam practice files

Edit `Study Notes/AI_EXAM_PRACTICE_QUESTIONS.md`, then run `build.py` with Python 3 from any working directory. Pandoc and pdfLaTeX must be on PATH. The script generates both mock-paper Markdown and both PDFs, validates question numbering and choices, and verifies that each mock contains 20 MC questions and 8 short questions including 2 calculations.

The two mock selections are defined in `build.py`. The generated files contain no answer key. Temporary LaTeX files and logs are kept in the course root's `.study_build/exam_practice/`.
