# Source coverage

References throughout the notes count PDF pages from 1, including title slides. Repeated reveal slides and image-only illustrations are consolidated into explanations of their underlying concept, rather than repeated as separate sections.

| Supplied deck | Pages | Coverage |
| --- | ---: | --- |
| 0. Presentation | 15 | Course scope in README; administrative details are not repeated as study theory. |
| 0.1. Math background | 11 | Topic 0: probability, random variables, Gaussian identities, information theory, MLE and Lagrange regularization. |
| 1.1. Fundamentals | 45 | Topic 1: learning settings, inductive bias, data, methodology, splits and k-NN. Applications illustrate the concepts. |
| 1.2. Shallow Learning | 85 | Topic 1: regression, regularization, optimization, robust fitting, metrics, classification, PCA, clustering, SVM, kernels, CART and ensembles. Neural-network previews lead into Topic 3. |
| 1.3. Bayesian Learning | 58 | Topic 1: uncertainty, Gaussian regression posterior/predictive, basis functions, GPs, kernels, ARD, marginal likelihood, Cholesky, and introductory extensions. |
| 2.1. Introduction to Reinforcement Learning | 16 | Topic 2: interaction, reward, gridworld, policy, model, value, planning and partial-observation introduction. |
| 2.2. Markov decision processes | 26 | Topic 2: Markov states, returns, values, Bellman expectation/optimality and dynamic programming. |
| 2.3. Q-learning | 48 | Topic 2: model-based/model-free, incremental MC, TD, exploration, regret, SARSA/Q-learning, features, worked Pacman calculation and deadly triad. |
| 2.4. Policy Search | 19 | Topic 2: policy objectives, trajectory likelihood, gradients, softmax policy, REINFORCE, actor–critic and optimization alternatives. |
| 3.1. Introduction to Deep Learning | 41 | Topic 3: definitions, applications, data and representation-learning pipeline. |
| 3.2. Shallow NN | 51 | Topic 3: ReLU construction, shapes/counts, approximation theorem, activation regions and terminology. |
| 3.3. Deep Learning Fundamentals | 48 | Topic 3: deep composition, representation capacity, scores, losses, SGD, momentum, Adam and hyperparameters. |
| 3.4. Deep Learning Fundamentals II | 53 | Topic 3: scalar/matrix backprop, autograd, initialization, normalization, explicit/implicit regularization, dropout, augmentation and double descent. |
| 4.1. CNNs | 98 | Topic 4: convolution, stride/padding/dilation, channels, receptive fields, pooling/upsampling, architecture modules, transfer learning, training diagnostics, task extensions, engineering applications and slide exercise. |
| X.1 / X.2 (initially supplied) | 41 / 51 | Extracted text identical to 3.1 / 3.2; no separate content. |

## Clarifications made in context

- Gaussian conditioning uses subtraction in conditional covariance; Gaussian mixtures need not be Gaussian; linear combinations must include covariance terms where relevant.
- Natural-log information is measured in nats; realized posterior-versus-prior KL is distinct from a particular entropy reduction; their expected relation is mutual information.
- MLE unbiasedness and asymptotic statements need conditions and correct scaling.
- Ridge loss scaling, logistic uniqueness/separation, PCA matrix orientation, F-beta weighting, and multiclass versus one-vs-rest accuracy are made explicit.
- RL rewards are indexed consistently after actions. Terminal continuation is zero, but the entering reward remains. Q-learning does not need a sampled successor action; convergence conditions and the deadly triad are qualified.
- Approximate Q-learning differentiates only the current prediction (semi-gradient); the slide Pacman weights are calculated before rounding.
- Neural-network approximation results are existence results; activation regions live in input space. Backpropagation is separated from optimization. Dropout and batch-normalization training/inference distinctions are explained.
- Convolution output-size calculations include floor and dilation; the 240-by-240 exercise gives distinct answers for stated padding assumptions. Historical model examples are kept as slide examples.

No lab solutions or teacher files were edited. The lab references connect the supplied theory to the named practical tasks.
