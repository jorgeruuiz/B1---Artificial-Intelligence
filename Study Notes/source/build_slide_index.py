"""Build the exam slide locator from curated, page-checked concept entries.

Outputs one PDF, editable TeX, and Markdown in Study Notes. No workbook is edited.
Pages always mean physical PDF pages, counted from 1, including title pages.
"""
from pathlib import Path
import logging
import re
import shutil
import subprocess
import sys
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
NOTES = ROOT / 'Study Notes'
BUILD = ROOT / '.study_build' / 'slide_index'
STEM = 'AI_SLIDES_EXAM_INDEX'
TOPICS = {
    '1': 'Learning fundamentals, shallow and Bayesian learning',
    '2': 'Reinforcement learning',
    '3': 'Neural networks and deep learning fundamentals',
    '4': 'CNNs and transfer learning',
    '5': 'Advanced deep learning',
    'L4': 'Lab 4 supplement: deployment, explainability and compression',
}

# Topic, exact PDF filename stem, page count, and "PDF pages | concept" rows.
DECKS = [
('1', '1.1. Fundamentals', 45, '''
4-6 | Machine learning, models, assumptions, inductive bias; No Free Lunch
10-14 | Supervised learning; regression versus classification
15-17 | Unsupervised learning; dimensionality reduction and clustering
18-23 | Reinforcement learning and combinations of learning strategies
24-26 | Abstraction, partial information; correlation versus causation
27-30 | Data quality, sampling bias, Big Data limitations, feature choice
31-32, 41 | Training, validation and test sets; model selection and evaluation
33-34, 36 | k-nearest neighbours (k-NN): prediction, distance and choice of k
37-39 | k-NN examples: dataset size, splits, digits and image difficulty
40-44 | ML workflow: frame problem, explore data, compare and tune models
'''),
('1', '1.2. Shallow Learning', 85, '''
4-8 | Linear regression, Gaussian noise, likelihood and least squares
9, 26-31 | Negative log-likelihood; gradient descent and stochastic updates
11-12 | Basis-function expansion; polynomial regression
13-15 | Overfitting, bias-variance trade-off and model complexity
16-18 | Ridge / L2 regularization; Gaussian prior and MAP interpretation
19-20 | Lasso / L1 regularization; sparsity and coefficients set to zero
21-25 | Hyperparameters, validation splits and cross-validation
27-32 | Learning rate; batch GD versus SGD; mini-batches and momentum
33 | Other optimization algorithms: overview
34-39 | Outliers; robust regression, L1/Laplace, Huber and RANSAC
40 | Regression metrics: MAE, MSE, RMSE, median error and R-squared
42 | Bayesian ridge and ARD: regression comparison
43 | Feature scaling / standardization and its importance
45-48 | Linear classification, decision boundary, perceptron and sigmoid
49-53 | Logistic regression: Bernoulli likelihood, cross-entropy and training
54-56 | Multiclass / multinomial logistic regression and softmax
57-59 | MLP preview; hidden layers and nonlinear activations
60 | True/false positives and negatives; TP, TN, FP, FN
61-62 | Accuracy, precision and recall: definitions and interpretation
63-64 | Classification threshold; precision-recall trade-off and PR curve
65 | F1 / F-beta; confusion-matrix orientation
66-67 | Read a multiclass confusion matrix; per-class and aggregate metrics
68-70 | PCA; dimensionality reduction and its effect on a classifier
71 | K-means clustering
72-75 | SVM: separating hyperplanes, maximum margin and support vectors
76 | Soft-margin / non-separable SVM
77 | SVM optimization: Lagrange formulation
78-79 | Nonlinear feature maps and the kernel trick
81 | Classification and regression trees (CART)
82-83 | Ensembles; bootstrap sampling, bagging and random forests
84 | Boosting; AdaBoost and gradient boosting
'''),
('1', '1.3. Bayesian Learning', 58, '''
4-6 | Bayesian reasoning; prior, likelihood, posterior and Bayes rule
7-8 | Bayesian prediction versus ML/MAP point estimates
9-13 | Bayesian linear regression; Gaussian prior, likelihood and posterior
10-12 | Multivariate Gaussians; covariance, marginals and conditioning
14 | Posterior predictive distribution; prediction uncertainty
15-20 | Regression in feature space; weight-space versus function-space views
21-27 | Polynomial, Fourier, bell, Heaviside and exponential basis functions
28-30 | Learned/many features; kernel trick and transition to Gaussian processes
31-35 | GP definition, joint distributions, correlation and conditioning
36 | Nonparametric models; training data versus fixed parameter vectors
37-43 | Kernel families: squared exponential, Matern, linear, periodic, neural
44-45 | Combining kernels; linear plus periodic structure
46-47 | Kernel hyperparameters: lengthscale, signal variance and noise
48 | Automatic Relevance Determination (ARD); per-dimension lengthscales
49-50 | Hyperparameter learning; marginal likelihood and complexity/fit trade-off
51 | GP predictive mean and variance; regression summary equations
52 | Cholesky-based GP computation
53-56 | Nonzero means, hierarchical Bayes, non-Gaussian likelihoods and GP extensions
'''),
('2', '2.1. Introduction to Reinforcement Learning', 16, '''
2-3 | What RL is; agent interaction versus supervised/unsupervised learning
5-6 | Rewards, costs and the reward hypothesis
7-9 | Agent-environment loop; deterministic/stochastic gridworld
10 | Partial observation and generalized decision-process introduction
11-13 | Transition/reward model, policy and value function
14-16 | Planning with a known model versus learning through interaction
'''),
('2', '2.2. Markov decision processes', 26, '''
2-3 | Markov property; MDP tuple: states, actions, transitions, rewards, discount
4-5 | Racing example and search-tree representation
6 | Policy: probability of an action given a state
7-10 | Return, discount factor gamma, finite/infinite horizon; discounting quiz
11 | State value V and action value Q
12-15 | Bellman expectation equations; recursive value evaluation
16-17 | Optimal V/Q functions and optimal policy
18-19 | Bellman optimality equations; maximization over actions
20 | Dynamic programming: why the model is required
21-22 | Iterative policy evaluation and stopping criterion
23-24 | Value iteration and greedy action selection
'''),
('2', '2.3. Q-learning', 48, '''
3-5 | MDP recap and unknown transition/reward models
6-10 | Model-based versus model-free learning; passive prediction versus control
11-13 | Monte Carlo policy evaluation from complete episodes
14-15 | Incremental mean and incremental Monte Carlo update
16-20 | MC limitations; bootstrapping and temporal-difference learning
21 | Constant learning rates and forgetting old observations
22-26 | MC versus TD versus dynamic programming; update equations
23 | Monte Carlo value-update formula
24 | TD(0) value update and TD error
27-28 | Control and Q-values; greedy action selection without a transition model
29 | SARSA update: sampled next action
30-33 | Exploration versus exploitation; epsilon-greedy and regret
34-36 | Q-learning target, update formula and algorithm
37-38 | On-policy versus off-policy; SARSA versus Q-learning
39-42 | Large state spaces, features and linear value-function approximation
43-44 | Approximate Q-learning; TD-error-based weight updates
45 | Worked Pacman feature/Q-value/weight-update example
46 | Online least squares / gradient interpretation
47 | Deadly triad: function approximation, bootstrapping and off-policy learning
'''),
('2', '2.4. Policy Search', 19, '''
2-3 | Policy-based versus value-based RL; advantages and limitations
4-5 | Trajectory probability and its factorization
6-7 | Expected-return objective; gradient ascent on policy parameters
8-10 | Policy-gradient derivation and sampled update
11 | Softmax policy over action scores
12-15 | Automatic differentiation and REINFORCE; return-weighted log probability
16-17 | Actor-critic: actor policy, critic value/Q estimate
18-19 | Local/global policy optimization; gradient-free alternatives
'''),
('3', '3.1. Introduction to Deep Learning', 41, '''
6-10 | AI, ML and deep learning; what deep learning means
11-25 | Application examples: language, vision, control, science and engineering
26-29 | Deep learning and Big Data; opportunities and limitations
30-32, 36-37 | DL pipeline, learning methodology and overfitting
33-35 | Collecting and labeling data; coverage, classes and variability
38-39 | Handcrafted versus learned features; representation learning
'''),
('3', '3.2. Shallow NN', 51, '''
4-6 | Linear regression versus a shallow neural-network model
7-9 | ReLU activation; example network and its ten parameters
10-17 | Hidden-unit construction; weighted sums and piecewise-linear output
18 | Activation patterns / active hidden units
19-22 | Network diagrams, weights and hidden width
23-24 | Universal approximation theorem
26-28 | Multiple outputs; shared hidden representation and output-specific weights
30-37 | Multiple inputs; activation boundaries and regions in 2D
39-42 | General input/hidden/output dimensions; parameter-count exercise
44-47 | Number of linear regions; dependence on input dimension and hidden width
49-50 | Terminology: layers, units, biases and weights
51 | Alternative activation functions
'''),
('3', '3.3. Deep Learning Fundamentals', 44, '''
3-7 | Neuron/perceptron recap; composition of nonlinear layers
8-11 | Depth, width, matrix formulation and deep-network parameter shapes
12-14 | Shallow versus deep capacity; depth efficiency and linear regions
16-21 | Scores / logits; mapping inputs to class scores
22-23 | Loss functions; multiclass SVM / hinge loss
24-26 | Softmax cross-entropy; score/probability interpretation and loss exercise
27-28 | Choosing a task loss; adding regularization
29-35 | Optimization, gradient descent, SGD and mini-batch noise
31, 36 | Local minima, saddle points and optimization difficulties
37-39 | Momentum and optimizer variants
40-42 | Adam: moment estimates, normalization and bias correction
43-44 | Parameters, hyperparameters and the training pipeline
'''),
('3', '3.4. Deep Learning Fundamentals II', 53, '''
3-7 | Forward pass, backward pass, gradients and chain rule
8-17 | Scalar backpropagation examples and classroom exercise
18-22 | Computation graphs; local backward operations and autograd
23-25 | Input normalization; random initialization, He and gradient scale
26-29 | Generalization gap; explicit L2 regularization / weight decay
30-31 | Implicit regularization; SGD and early stopping
32, 34 | Dropout; randomly disabling hidden units during training
33-35 | More data, noise and label-preserving data augmentation
36-38 | Capacity, generalization and double descent
39-42 | Hyperparameter choices and overall training recipe
44-48 | Matrix derivatives; forward and backward propagation through layers
49-50 | ReLU derivative
51-52 | Gradients with respect to weights and biases
53 | Backpropagation: efficiency and limitations
'''),
('4', '4.1. CNNs', 111, '''
4-11 | Image structure; local connectivity, weight sharing and convolutional features
12-14 | One-dimensional convolution and filter sliding
15-18 | Kernel, stride, padding, dilation; output-size formula and questions
19-23 | Feature maps/channels and receptive fields
24-30 | 2D/RGB convolution; input/output channels and parameter counts
31-32 | Downsampling, pooling and strided convolution
33-35 | Upsampling, interpolation, unpooling and transposed convolution
36 | 1-by-1 / pointwise convolution; mixing channels
37-43 | AlexNet, DeConvNet and feature-map visualization
44-47 | VGG; small filters, depth and receptive-field comparison
48-50 | Activation memory, batch size and deeper architectures
51-54 | Vanishing gradients; ResNet, identity shortcuts and bottleneck blocks
55-56 | Batch normalization: statistics, gamma/beta and parameter count
57 | BN training versus inference; running statistics, eval mode and folding
58-59 | Why normalization helps; batch/layer/instance/group normalization
60-62 | ResNet family; addition versus concatenation; residual/BN quick questions
63 | Inception/GoogLeNet and DenseNet modules
64 | MobileNet depthwise-separable convolution; EfficientNet scaling
65-66 | Vision Transformer / ConvNeXt comparison and architecture trends
67-70 | Transfer learning and frozen feature extraction
71-74 | Fine-tuning; dataset size/domain similarity and adaptation choices
75-81 | Initial loss, overfitting a tiny set, learning curves, learning-rate decay
82-86 | Detection, box regression, Faster R-CNN and YOLO
87-88 | PoseNet; position/orientation regression
90-93 | Semantic segmentation, FCN, SegNet and instance segmentation/Mask R-CNN
94-101 | Video feature fusion, multimodal inputs and temporal-order limitations
102-105 | Task summary; 1D/2D/3D engineering applications and simulation surrogates
106 | Classroom calculation: feature-map sizes and convolution parameters
108-110 | Lab 3 connection: toy CNNs and pretrained-model fine-tuning
'''),
('5', '5.1. Sequence Models', 34, '''
3-6 | Sequential order, variable lengths, recurrence and shared weights
7-9 | Vanilla RNN equations; hidden state and character-level predictions
10-12 | Generated sequences and interpretable recurrent units
13-15 | Backpropagation through time (BPTT); vanishing/exploding gradients
14, 16 | Truncated BPTT; memory cost and long-range gradient limitations
16 | Gradient clipping, initialization and architectural remedies
17-20 | LSTM cell/hidden states; forget, input, candidate and output gates
21 | Additive memory path; GRU and its gates
22 | Stacked and bidirectional recurrent networks
23-24 | Video action recognition and dense captioning
25-27 | Temporal convolutional networks (TCN); causal/dilated filters; WaveNet
28 | Recurrent seq2seq encoder-decoder; fixed context vector
29 | Teacher forcing, inference feedback, exposure bias and scheduled sampling
30-31 | Attention over encoder states; captioning with attention
32 | Summary equations: RNN, BPTT, LSTM, seq2seq and attention
33 | Character-RNN practical exercise
'''),
('5', '5.1. Extra Material', 7, '''
2-4 | LSTM cell diagrams and gates
5 | Tiny LSTM: matrix dimensions, vocabulary, hidden width and parameter counts
6 | Learned parameters versus computed states; changing vocabulary or hidden width
7 | Worked LSTM update: gates, cell/hidden state and next-character scores
'''),
('5', '5.2. Transformers', 43, '''
3-8 | RNN/CNN/attention comparison; weighted context and query/key/value intuition
9-10 | Self-attention: value projections, query-key scores and softmax weights
11 | Numerical attention example; shared parameters versus input-dependent weights
12-14 | Matrix attention, tensor shapes, row softmax and square-root scaling
15 | Permutation equivariance / order blindness; need for positional information
16-17 | Sinusoidal, learned, relative, rotary (RoPE) and ALiBi positions
18 | Encoder-only, decoder-only and encoder-decoder overview
19 | Tokenization: words, characters, subwords and BPE
20-22 | Token embeddings, embedding table and contextual representations
23-24 | Transformer block and multi-head attention; concatenate and project
25, 27 | Residual connections; Add & Norm and layer normalization
26 | Positionwise feed-forward MLP
28-29 | Encoder stack, masked language modeling and CLS readout
30 | Autoregressive factorization; next-token cross-entropy and training parallelism
31 | Causal mask; future-token leakage and zero attention to forbidden positions
32-35 | Self-attention versus cross-attention; three transformer families
36 | Quadratic attention cost; KV cache, FlashAttention and grouped-query attention
37-40 | Vision Transformers: patches, projection, positions, CLS and hybrid designs
41-42 | A/B classroom attention exercise; simplified divide-by-three normalization
'''),
('5', '5.3. Foundation models', 28, '''
5-8 | Transformer-family recap; encoder, decoder and cross-attention
9-11 | Foundation-model definition; broad pretraining and downstream transfer
12-13 | Scale, data, hardware; total versus active MoE parameters; shared biases
14 | Training stages: self-supervised pretraining, SFT, preference RL, verifiable RL
15 | BERT: masked-token and next-sentence pretraining examples
16-17 | GPT-style generation and multimodal model examples; post-training
19-20 | CLIP: image-text embeddings, contrastive alignment and zero-shot classification
21 | DINOv2: self-distillation, visual features and downstream transfer
22 | SAM: promptable segmentation
23-25 | Text-conditioned image generation; text encoder, denoiser and VAE decoder
26 | Efficiency, explainability and fairness questions
'''),
('5', '5.4. Unsupervised learning', 38, '''
2-7 | Supervision strategies; unlabeled data and semi-supervised learning
7 | When unlabeled data helps: distribution relevance
9-11 | PCA: variance, projection, compression and retained components
12-18 | t-SNE: local neighborhoods, perplexity and visualization pitfalls
17-18 | Visualizing high-dimensional CNN features
19-20 | K-means: initialization, assignments and centroid updates
21 | Hierarchical clustering: agglomerative versus divisive
22 | Latent Dirichlet Allocation (LDA); topic mixtures, not discriminant analysis
24-27 | Self-supervised pretraining and proxy/pretext tasks
26-27 | Patch position, jigsaws, colorization and inpainting examples
28-29 | Contrastive learning; positive/negative pairs and triplet ideas
30-31 | BYOL: online/target networks and learning without negative pairs
32 | SuperPoint: self-supervised keypoint detection and description
33 | Semi-supervised teacher-student learning, memory banks and pixel-level contrast
34-36 | Connection to foundation models; PCA versus t-SNE summary
'''),
('5', '5.5. Generative Models', 26, '''
3-6 | Discriminative versus generative modeling; learning a data distribution
7 | Autoencoder: encoder, latent code, decoder and reconstruction
8 | AE versus VAE; latent distributions, reconstruction plus KL regularization
9-12 | GANs: generator/discriminator roles and adversarial training
13 | GAN instability, weak gradients and mode collapse
14 | CycleGAN: unpaired translation and cycle consistency
15-16 | Image editing/style-transfer applications
17 | Forward diffusion: progressive Gaussian noising
18-19 | Learned reverse diffusion; denoising training versus sampling
5, 20-21 | Conditional / latent diffusion; text representations and image decoding
22 | AE/VAE/GAN/diffusion comparison: objective, stability, speed, quality, latent space
25-26 | Course map: AI, ML, neural networks, deep learning and application areas
'''),
('L4', 'manolo_presentation', 15, '''
2 | Explainable AI (XAI) and model compression: definitions
3-4 | AI governance / regulatory context discussed in the briefing
5 | Trustworthiness, fairness, transparency and robustness
6 | Edge deployment: latency, memory, compute, energy and privacy
7 | Grad-CAM: class-specific image evidence and heatmaps
8 | Compression families: quantization, pruning, distillation and low-rank methods
9 | FP32 versus INT8 quantization; memory reduction and accuracy trade-off
10 | Magnitude pruning, sparsity, fine-tuning and hardware-dependent speed
11 | Compare accuracy and explanations before/after compression
12 | Lab notebook workflow and evaluation tasks
'''),
]

# Repeated references deliberately provide direct routes for common exam lookups.
QUICK = [
('Training / validation / test; cross-validation', [('1.1', '31-32, 41'), ('1.2', '21-25')]),
('Regression errors; classification metrics / confusion matrix', [('1.2', '40, 60-67')]),
('Bayesian posterior / prediction; Gaussian-process equations', [('1.3', '13-14, 51-52')]),
('Discounted returns and Bellman equations', [('2.2', '8-19')]),
('MC / TD update; SARSA versus Q-learning', [('2.3', '23-24, 29, 35-38')]),
('Dense-network dimensions and parameter counts', [('3.2', '39-42'), ('3.3', '8-10')]),
('Hinge / softmax loss; backpropagation exercise', [('3.3', '23-26'), ('3.4', '8-17')]),
('Convolution output size, parameters and receptive field', [('4.1', '17, 20-23, 30, 106')]),
('Residuals; BN count and train/eval; normalization variants', [('4.1', '52-59, 62')]),
('LSTM dimensions, parameter counts and one-step update', [('5.1E', '5-7')]),
('Attention calculation, shapes and classroom A/B exercise', [('5.2', '11-13, 42')]),
('Causal mask, cross-attention, KV cache and image patches', [('5.2', '31-40')]),
('PCA / t-SNE; k-means / topic mixtures', [('5.4', '9-22')]),
('Pretraining / SFT / RL; CLIP, DINOv2 and SAM', [('5.3', '14, 19-22')]),
('AE / VAE / GAN / diffusion: meanings and comparisons', [('5.5', '7-13, 17-22')]),
]

def deck_code(title):
    if title == 'manolo_presentation':
        return 'L4'
    if title == '5.1. Extra Material':
        return '5.1E'
    return title[:3]

def parse_rows(raw):
    return [(pages.strip(), concept.strip()) for pages, concept in
            (line.split('|', 1) for line in raw.strip().splitlines())]

def tex_escape(s):
    mapping = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
               '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}',
               '^': r'\textasciicircum{}'}
    return ''.join(mapping.get(c,c) for c in s)

def tex_url(s):
    return s.replace('%', r'\%').replace('#', r'\#').replace('_', r'\_')

def source_url(title, pages=None):
    rel = ('Lab Sessions/Lab4/' if title == 'manolo_presentation' else 'Lecture Slides/') + title + '.pdf'
    url = '../' + quote(rel, safe='/')
    if pages:
        url += '#page=' + re.search(r'\d+',pages).group(0)
    return url

def page_tex(title, pages):
    return r'\href{' + tex_url(source_url(title,pages)) + '}{' + pages.replace('-', '--') + '}'

def validate():
    sys.path.insert(0,str(ROOT / '.study_build/deps'))
    from pypdf import PdfReader
    logging.getLogger('pypdf').setLevel(logging.ERROR)
    catalog = {}
    total = 0
    for topic,title,count,raw in DECKS:
        rel = ('Lab Sessions/Lab4/' if topic == 'L4' else 'Lecture Slides/') + title + '.pdf'
        assert len(PdfReader(ROOT / rel).pages) == count, title
        rows = parse_rows(raw)
        assert len(set(concept for _,concept in rows)) == len(rows), title
        for pages,concept in rows:
            assert concept and re.fullmatch(r'\d+(?:-\d+)?(?:, \d+(?:-\d+)?)*',pages), (title,pages)
            assert all(1 <= int(n) <= count for n in re.findall(r'\d+',pages)), (title,pages)
        catalog[deck_code(title)] = (title,count)
        total += len(rows)
    for _, refs in QUICK:
        for code,pages in refs:
            assert code in catalog
            assert all(1 <= int(n) <= catalog[code][1] for n in re.findall(r'\d+',pages))
    assert len(catalog) == len(DECKS) == 19
    return catalog,total

PREAMBLE = r'''\documentclass[10pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[a4paper,margin=16mm,headheight=14pt]{geometry}
\usepackage{array,longtable,booktabs,xcolor,fancyhdr,titlesec,microtype}
\usepackage{hyperref}
\definecolor{navy}{HTML}{163653}
\definecolor{teal}{HTML}{007F86}
\hypersetup{colorlinks=true,linkcolor=navy,urlcolor=teal,filecolor=teal,
pdftitle={Artificial Intelligence - Exam Slide Index}}
\pagestyle{fancy}\fancyhf{}
\newcommand{\currenttopic}{Quick lookup}
\fancyhead[L]{\small\sffamily Artificial Intelligence: slide index}
\fancyhead[R]{\small\sffamily\currenttopic}
\fancyfoot[C]{\small\thepage}
\setlength{\parindent}{0pt}\setlength{\parskip}{4pt}
\setlength{\emergencystretch}{3em}
\setlength{\LTpre}{3pt}\setlength{\LTpost}{5pt}
\setcounter{secnumdepth}{0}
\titleformat{\section}{\Large\sffamily\bfseries\color{navy}}{}{0pt}{}
\titleformat{\subsection}{\normalsize\sffamily\bfseries\color{teal}}{}{0pt}{}
\titlespacing*{\section}{0pt}{4pt}{5pt}
\titlespacing*{\subsection}{0pt}{9pt}{3pt}
\newcolumntype{P}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcommand{\deckheading}[1]{\par\begingroup\skip0=\pagegoal\advance\skip0 by-\pagetotal\ifdim\skip0<7\baselineskip\newpage\fi\endgroup\subsection{#1}}
\begin{document}
\section{Exam slide index}
\textbf{Find a concept, its exact slide PDF, and the page to open.}
Organized by main topics 1--5, with individual slide decks inside each topic.

\textbf{All numbers are PDF pages, starting at 1 and including the title slide.}
They are not necessarily the numbers printed on the slides. For example, PDF page 40
in 1.2 is printed slide 41; PDF page 51 in 1.3 is printed slide 54.
Use the PDF reader's page counter. Ranges include repeated reveal slides.

The detailed tables cover the lecture theory and exercises. Lab 4 briefing material
has a separate final section. \textbf{5.1E} means \textbf{5.1. Extra Material.pdf}.
Page references link to the local slide files when this index stays in Study Notes;
whether a link opens directly at the requested page depends on the PDF reader.

\begin{tabular}{@{}P{.84\linewidth}r@{}}
\toprule\textbf{Main topic / detailed index} & \textbf{Index page}\\\midrule
'''

def build_documents(catalog,total):
    tex = [PREAMBLE]
    md = ['# Artificial Intelligence — exam slide index\n',
          '**PDF page numbers start at 1 and include title pages.** They may differ from printed slide numbers, especially in 1.2 and 1.3. This index points to the original slide PDFs, not the study-note PDFs.\n',
          'Grouped by main topic 1–5, with exact slide-deck titles beneath each topic. 5.1E means the separate LSTM extra-material PDF. The Lab 4 briefing appears as a supplement.\n',
          '## Quick lookup\n\n| Find | Slide PDF and pages |\n| --- | --- |\n']
    for topic,title in TOPICS.items():
        label = topic + '. ' + title if topic != 'L4' else title
        tex.append(r'\hyperref[topic' + topic + ']{' + tex_escape(label) + r'} & \pageref{topic' + topic + r'}\\' + '\n')
    tex.append(r'\bottomrule\end{tabular}' + '\n\n' + r'\subsection{Common calculations and distinctions}' + '\n')
    tex.append(r'\begin{longtable}{@{}P{.62\linewidth}P{.34\linewidth}@{}}' + '\n' +
               r'\toprule\textbf{Find} & \textbf{Deck: PDF pages}\\\midrule\endhead' + '\n')
    for text,refs in QUICK:
        texrefs = [r'\textbf{' + code + '}: ' + page_tex(catalog[code][0],pages) for code,pages in refs]
        mdrefs = ['[' + code + ': ' + pages + '](' + source_url(catalog[code][0],pages) + ')' for code,pages in refs]
        tex.append(tex_escape(text) + ' & ' + '; '.join(texrefs) + r'\\[3pt]' + '\n')
        md.append('| ' + text + ' | ' + '; '.join(mdrefs) + ' |\n')
    tex.append(r'\bottomrule\end{longtable}' + '\n')
    for topic,heading in TOPICS.items():
        label = topic + '. ' + heading if topic != 'L4' else heading
        tex.append('\n' + r'\clearpage\renewcommand{\currenttopic}{' + ('Topic '+topic if topic!='L4' else 'Lab 4 supplement') + '}\n' +
                   r'\section{' + tex_escape(label) + r'}\label{topic' + topic + '}\n')
        md.append('\n## ' + label + '\n')
        for deck_topic,title,count,raw in DECKS:
            if deck_topic != topic:
                continue
            display = title + '.pdf'
            if topic == 'L4':
                display = 'manolo_presentation.pdf (Lab Sessions / Lab4)'
            tex.append(r'\deckheading{' + tex_escape(display) + '}\n')
            tex.append(r'{\small ' + str(count) + ' PDF pages. ')
            if title == '5.1. Extra Material':
                tex.append('Separate PDF; lookup code 5.1E. ')
            tex.append(r'\href{' + tex_url(source_url(title)) + r'}{Open this slide PDF.}}\par' + '\n')
            tex.append(r'\begin{longtable}{@{}P{.79\linewidth}P{.17\linewidth}@{}}' + '\n' +
                       r'\toprule\textbf{Concept / method / exercise} & \textbf{PDF pages}\\\midrule\endfirsthead' + '\n' +
                       r'\multicolumn{2}{@{}l}{\small\textbf{' + tex_escape(title) + r' -- continued}}\\' + '\n' +
                       r'\toprule\textbf{Concept / method / exercise} & \textbf{PDF pages}\\\midrule\endhead' + '\n')
            md.append('\n### ' + display + '\n\n| Concept / method / exercise | PDF pages |\n| --- | --- |\n')
            for pages,concept in parse_rows(raw):
                tex.append(tex_escape(concept) + ' & ' + page_tex(title,pages) + r'\\[3pt]' + '\n')
                md.append('| ' + concept + ' | [' + pages + '](' + source_url(title,pages) + ') |\n')
            tex.append(r'\bottomrule\end{longtable}' + '\n')
    tex.append('\n' + r'\end{document}' + '\n')
    texpath = NOTES / (STEM+'.tex')
    texpath.write_text(''.join(tex),encoding='utf-8',newline='\n')
    (NOTES / (STEM+'.md')).write_text(''.join(md),encoding='utf-8',newline='\n')
    print(f'Generated {total} concept entries across {len(DECKS)} slide PDFs, plus {len(QUICK)} quick-lookup rows.')
    return texpath

def main():
    catalog,total = validate()
    texpath = build_documents(catalog,total)
    BUILD.mkdir(parents=True,exist_ok=True)
    for _ in range(3):
        result = subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',
                                 '-output-directory',str(BUILD),str(texpath)],
                                cwd=NOTES,capture_output=True,text=True,errors='replace')
        if result.returncode:
            print(result.stdout[-6000:])
            print(result.stderr[-2000:])
            raise SystemExit(result.returncode)
    log = (BUILD/(STEM+'.log')).read_text(encoding='utf-8',errors='replace')
    warnings = [line for line in log.splitlines() if any(s in line for s in ['Overfull','Missing character','undefined references'])]
    if warnings:
        print('Layout warnings:\n'+'\n'.join(warnings))
    shutil.copyfile(BUILD/(STEM+'.pdf'),NOTES/(STEM+'.pdf'))
    print('Built',STEM+'.pdf')

if __name__ == '__main__':
    main()
