# Artificial Intelligence study notes

## Exam slide index

- [Slide index (PDF)](AI_SLIDES_EXAM_INDEX.pdf) · [Editable LaTeX](AI_SLIDES_EXAM_INDEX.tex) · [Markdown](AI_SLIDES_EXAM_INDEX.md)

The 12-page locator groups concepts and methods by main topic 1–5, then by exact slide PDF title, with a separate Lab 4 briefing supplement. The first page provides quick routes to common calculations and comparisons. References use physical PDF pages starting at 1, including the title page; printed slide numbers sometimes differ. Local links require keeping the index in `Study Notes` beside the existing course folders; jumping to a particular page depends on the PDF reader. Presentation and mathematical-background decks are excluded.

Edit `source/build_slide_index.py` to maintain the concept mappings, then run it with Python (with `pypdf` installed or available in `.study_build/deps`) and `pdflatex` on PATH. It validates source PDF lengths and page bounds, generates the Markdown and standalone LaTeX, and compiles the index. Alternatively, edit and compile the standalone `.tex` directly; regeneration replaces those direct edits. This build does not modify the answer workbook.

## Exam practice — questions only

The expanded practice bank is organized by exact slide PDF title, with **10 multiple-choice questions, 7 short-answer questions, and 3 easy calculation problems per deck**. It contains **360 questions across 18 teaching PDFs**, including the separate LSTM extra material, plus a **20-question Lab 4 explainability/compression supplement**: **380 questions total**. The administrative presentation and mathematical-background PDFs are excluded. Each question includes its source PDF page reference. No answers are included.

- [Question bank (PDF)](AI_EXAM_PRACTICE_QUESTIONS.pdf) · [Editable Markdown](AI_EXAM_PRACTICE_QUESTIONS.md)
- [Two one-hour mock papers (PDF)](AI_EXAM_MOCK_PAPERS.pdf) · [Markdown](AI_EXAM_MOCK_PAPERS.md)
- [Editable LaTeX answer workbook](AI_EXAM_PRACTICE_WORKBOOK.tex) · [Blank workbook PDF](AI_EXAM_PRACTICE_WORKBOOK.pdf)

The standalone LaTeX workbook preserves all 380 questions and their multiple-choice option order. Type your responses in the labelled `solution` environments after each question, then compile with pdfLaTeX (twice for the contents page). Empty blocks show handwriting space; typed responses replace that space. Upload the completed `.tex` and/or PDF for feedback. No separate local style files are required. Edit the workbook directly after entering answers; regenerating it would discard them.

Each updated mock contains 20 multiple-choice questions and 8 short questions, including 2 small calculations, drawn from the expanded bank. Edit the per-deck sources and follow the rebuild instructions in [exam_practice_source](exam_practice_source/README.md).

## Explanatory study notes — grouped by main topic

English explanatory notes based on the teacher PDFs supplied in **Lecture Slides**, following the style of the Data Science and Computational Engineering notes.

**Organization:** keep one explanatory PDF per main course topic: **1, 2, 3, 4 and 5**, with the existing mathematical-background volume as Topic 0. Subtopics such as 5.1–5.5 belong inside their main-topic volume. This grouping applies to the study notes; the practice questions retain their requested slide-by-slide organization.

Read the PDFs in order, or jump to the topic you are revising:

| PDF | Contents | Teacher slide decks |
| --- | --- | --- |
| [0. Mathematical background.pdf](0.%20Mathematical%20background.pdf) | Probability, Gaussian conditioning, entropy, KL, likelihood and constrained optimization | 0.1 |
| [1. Learning fundamentals, shallow and Bayesian learning.pdf](1.%20Learning%20fundamentals,%20shallow%20and%20Bayesian%20learning.pdf) | Methodology, regression, classification, metrics, PCA, clustering, SVMs, ensembles, Bayesian regression and GPs | 1.1–1.3 |
| [2. Reinforcement learning.pdf](2.%20Reinforcement%20learning.pdf) | MDPs, Bellman equations, planning, MC, TD, SARSA, Q-learning, approximation, REINFORCE and actor–critic | 2.1–2.4 |
| [3. Neural networks and deep learning fundamentals.pdf](3.%20Neural%20networks%20and%20deep%20learning%20fundamentals.pdf) | Shallow networks, capacity, deep composition, losses, optimization, worked backpropagation, initialization and regularization | 3.1–3.4 |
| [4. CNNs and transfer learning.pdf](4.%20CNNs%20and%20transfer%20learning.pdf) | Convolution sizes, parameters, receptive fields, architectures, transfer learning, diagnostics and structured outputs | 4.1 |
| [5. Advanced deep learning.pdf](5.%20Advanced%20deep%20learning.pdf) | Sequence models and LSTM extra material; attention and transformers; foundation models; unsupervised/self-supervised learning; generative models | 5.1–5.5 + 5.1 Extra Material |

Topic 5 contains all five chapters with one cover, one contents list and continuous pagination. Its internal headings retain the slide codes for navigation. Residual connections and normalization are included in Topic 4. The superseded separate chapter PDFs and standalone sources are preserved in `archive/separate_volumes/`; they are not the primary study-note organization.

Topic 3 references now match the current 44-page **3.3** deck. Topic 4 references now match the current 111-page **4.1** deck, including its expanded residual/normalization material. Earlier printed theory remains useful, but its page references may reflect older slide versions.

Each volume has a contents page, explanations, worked calculations, revision questions with answers, and teacher-slide references using **PDF page numbers counted from 1**. Additional numerical examples are explanatory calculations derived from the teacher's concepts; examples taken directly from slides are identified. Mathematical corrections and qualifications are marked beside the corresponding material.

The course presentation (`0. Presentation.pdf`) establishes the outline but is not a separate theoretical lesson. The initially supplied X.1 and X.2 decks had identical extracted text to 3.1 and 3.2; they added no separate content. The later 5.1–5.5 PDFs are covered together in Topic 5. Efficiency, explainability and fairness are discussed at the level introduced in those lectures; the separate Lab 4 briefing also has a practice-question supplement in the bank.

The editable LaTeX is in `source/`, with a shared `notes_style.tex`. Extracted teacher-slide text is retained in `source/slide_text/` as a source aid; equations in the PDFs are authoritative where extraction loses symbols. `source/coverage.md` maps supplied content to the volumes.

Edit `Topic_0.tex` through `Topic_5.tex` for the main volumes. The file `cnn_residual_normalization.tex` supplies the expanded material inside Topic 4. Topic 5 preserves the complete explanations, examples, revision questions/answers and source guides from the five previously separate chapters. The practice workbook remains yours to complete.

To rebuild all PDFs from this subject folder in PowerShell:

```powershell
& '.\Study Notes\source\build.ps1'
```

The script runs pdfLaTeX three times per volume to resolve contents, pagination and hyperlinks, including volumes with two-page contents lists. A pdfLaTeX installation with the packages used in `notes_style.tex` is required. It copies the final PDFs to `Study Notes` and keeps compiler files in `source/build`.

To rebuild only Topic 5, use `& '.\Study Notes\source\build.ps1' -Topics '5'`. The build publishes only main-topic volumes 0–5. Building these study notes does not regenerate the answer workbook.
