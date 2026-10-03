# Artificial Intelligence study notes

English explanatory notes based on the teacher PDFs supplied in **Lecture Slides**, following the style of the Data Science and Computational Engineering notes.

Read the PDFs in order, or jump to the topic you are revising:

| PDF | Contents | Teacher slide decks |
| --- | --- | --- |
| [0. Mathematical background.pdf](0.%20Mathematical%20background.pdf) | Probability, Gaussian conditioning, entropy, KL, likelihood and constrained optimization | 0.1 |
| [1. Learning fundamentals, shallow and Bayesian learning.pdf](1.%20Learning%20fundamentals,%20shallow%20and%20Bayesian%20learning.pdf) | Methodology, regression, classification, metrics, PCA, clustering, SVMs, ensembles, Bayesian regression and GPs | 1.1–1.3 |
| [2. Reinforcement learning.pdf](2.%20Reinforcement%20learning.pdf) | MDPs, Bellman equations, planning, MC, TD, SARSA, Q-learning, approximation, REINFORCE and actor–critic | 2.1–2.4 |
| [3. Neural networks and deep learning fundamentals.pdf](3.%20Neural%20networks%20and%20deep%20learning%20fundamentals.pdf) | Shallow networks, capacity, deep composition, losses, optimization, worked backpropagation, initialization and regularization | 3.1–3.4 |
| [4. CNNs and transfer learning.pdf](4.%20CNNs%20and%20transfer%20learning.pdf) | Convolution sizes, parameters, receptive fields, architectures, transfer learning, diagnostics and structured outputs | 4.1 |

Each volume has a contents page, explanations, worked calculations, revision questions with answers, and teacher-slide references using **PDF page numbers counted from 1**. Additional numerical examples are explanatory calculations derived from the teacher's concepts; examples taken directly from slides are identified. Mathematical corrections and qualifications are marked beside the corresponding material.

The course presentation (`0. Presentation.pdf`) establishes the course outline but is not a separate theoretical lesson. The supplied X.1 and X.2 decks had identical extracted text to 3.1 and 3.2; they added no separate content. Topics mentioned only as future course material—such as ethics, explainability, generative models and transformers—are not expanded into unsupplied lessons. The CNN deck's introductory references to these ideas remain in context.

The editable LaTeX is in `source/`, with a shared `notes_style.tex`. Extracted teacher-slide text is retained in `source/slide_text/` as a source aid; equations in the PDFs are authoritative where extraction loses symbols. `source/coverage.md` maps supplied content to the volumes.

To rebuild all PDFs from this subject folder in PowerShell:

```powershell
& '.\Study Notes\source\build.ps1'
```

The script runs pdfLaTeX three times per volume to resolve contents, pagination and hyperlinks, including volumes with two-page contents lists. A pdfLaTeX installation with the packages used in `notes_style.tex` is required. It copies the final PDFs to `Study Notes` and keeps compiler files in `source/build`.
